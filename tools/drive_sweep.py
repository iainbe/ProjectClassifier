#!/usr/bin/env python3
"""Drive sweep — detect new/changed files on Google Drive vs toolkit registers.
Writes sweep_reports/SWEEP_LATEST.md + dated report; macOS notification summary.
Run manually or via launchd (tools/com.thefifthsector.toolkit-sweep.plist).
"""
import csv, json, os, re, subprocess, sys, time
from datetime import datetime

TK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # toolkit root
CFG = json.load(open(os.path.join(TK, 'tools', 'sweep_config.json')))
DRIVE = CFG['drive_root']
IGNORE = [re.compile(p) for p in CFG['ignore_patterns']]
TENDER_RE = re.compile('|'.join(CFG['tender_patterns']), re.I)
OUTCOME_RE = re.compile('|'.join(CFG.get('outcome_patterns', [])), re.I) if CFG.get('outcome_patterns') else None
PROPOSAL_ROOTS = ('Active proposals', 'Archive proposals')
STATE_PATH = os.path.join(TK, CFG['state_file'])
REPORT_DIR = os.path.join(TK, CFG['report_dir'])
DRIFT_ROOTS = tuple(w['path'].rstrip('/') + '/' for w in CFG['watch_roots'] if w.get('severity') == 'DRIFT')

def ignored(rel):
    return any(p.search(os.path.basename(rel)) or p.search(rel) for p in IGNORE)

def load_registers():
    """Map registered folders (01_projects) and source locators (02_sources)."""
    proj_folders = {}
    with open(os.path.join(TK, CFG['register_projects'])) as f:
        for r in csv.DictReader(f):
            for fp in (r.get('drive_folder_path') or '').split(';'):
                fp = fp.strip().rstrip('/')
                if fp:
                    proj_folders[fp] = r['project_id']
    src_names = set()
    src_dir_locs = {}  # controlled_location -> source_id, where location is a directory
    with open(os.path.join(TK, CFG['register_sources'])) as f:
        for r in csv.DictReader(f):
            for c in ('original_locator', 'controlled_location', 'title'):
                v = (r.get(c) or '').strip()
                if v: src_names.add(os.path.basename(v))
            cl = (r.get('controlled_location') or '').strip().rstrip('/')
            if cl and not os.path.splitext(cl)[1]:
                src_dir_locs[cl] = r['source_id']
    tender_folders = {}
    with open(os.path.join(TK, CFG['register_tenders'])) as f:
        for r in csv.DictReader(f):
            m = re.search(r'Drive folder:\s*([^|]+)', r.get('notes') or '')
            if m:
                # tolerate a history parenthetical after the path, e.g.
                # "…/2026 Next Wave (moved 26/10/02 from Active proposals/…)"
                path = re.sub(r'\s*\(.*', '', m.group(1)).strip().rstrip('/')
                if path:
                    tender_folders[path] = r['opportunity_id']
    # basename -> tender id, for tender folders moved out of their registered path
    # (e.g. a lost bid moved to Archive proposals/2026 Proposals lost/). Literal
    # path matches take precedence; first registration wins on basename collision.
    tender_basenames = {}
    for tf, tid in tender_folders.items():
        tender_basenames.setdefault(os.path.basename(tf), tid)
    return proj_folders, src_names, tender_folders, src_dir_locs, tender_basenames

def scan():
    """Walk watch roots -> {relpath: (mtime, size)} and list of icloud placeholders."""
    files, placeholders = {}, []
    for wr in CFG['watch_roots']:
        base = os.path.join(DRIVE, wr['path'])
        if not os.path.isdir(base): continue
        for root, dirs, names in os.walk(base):
            dirs[:] = [d for d in dirs if not ignored(d)]
            for n in names:
                rel = os.path.relpath(os.path.join(root, n), DRIVE)
                if ignored(rel): continue
                if n.endswith(CFG['icloud_suffix']):
                    placeholders.append(rel); continue
                try:
                    st = os.stat(os.path.join(DRIVE, rel))
                    files[rel] = (st.st_mtime, st.st_size)
                except OSError:
                    pass
    return files, placeholders

def outcome_hit(rel):
    return bool(OUTCOME_RE and OUTCOME_RE.search(os.path.basename(rel)))

def classify(rel, proj_folders, src_names, non_proj, tender_folders, tender_basenames):
    # toolkit-internal changes
    if rel.startswith(DRIFT_ROOTS):
        return ('DRIFT', 'register/toolkit file changed outside a session')
    # inside a registered project folder?
    for pf, pid in proj_folders.items():
        if rel.startswith(pf + '/'):
            base = os.path.basename(rel)
            tag = 'SOURCE_UPDATED' if base in src_names else 'UNREGISTERED_SOURCE'
            return (tag, f'in registered project {pid}')
    # inside a registered tender folder at its registered path?
    for tf, tid in tender_folders.items():
        if rel.startswith(tf + '/'):
            if outcome_hit(rel):
                return ('TENDER_OUTCOME?', f'outcome/feedback file in registered tender {tid} — log outcome and feedback in 08_tenders.csv')
            return ('TENDER_FILE', f'in registered tender {tid}')
    # inside a tender folder moved off its registered path? (basename match on
    # any ancestor segment, so subfolders of the tender folder still attribute)
    if rel.split('/')[0] in PROPOSAL_ROOTS:
        for seg in rel.split('/')[1:-1]:
            if seg in tender_basenames:
                tid = tender_basenames[seg]
                if outcome_hit(rel):
                    return ('TENDER_OUTCOME?', f'outcome/feedback file in moved folder for registered tender {tid} — log outcome and feedback in 08_tenders.csv')
                return ('TENDER_FILE', f'in registered tender {tid} (folder moved from registered path)')
    # known non-project folder?
    for npf in non_proj:
        if rel.startswith(npf + '/') or rel == npf:
            return ('NON_PROJECT', 'known admin/resource folder')
    # outcome/feedback file anywhere under proposals roots, unattributed
    if rel.split('/')[0] in PROPOSAL_ROOTS and outcome_hit(rel):
        return ('TENDER_OUTCOME?', 'possible outcome/feedback file — attribute to a tender and log in 08_tenders.csv')
    if TENDER_RE.search(os.path.basename(rel)):
        return ('POSSIBLE_TENDER', 'filename matches tender/bid pattern')
    # file under Active/Archive projects/proposals but no registered folder matched
    # -> collapse to folder-level: find the project-folder segment
    parts = rel.split('/')
    if parts[0] in ('Active projects', 'Archive projects', 'Active proposals', 'Archive proposals'):
        # project folder = first two segments (e.g. 'Active projects/2026 X')
        # or three under Archive year folders ('Archive projects/2017 Projects/2017 X')
        if parts[0].startswith('Archive') and len(parts) >= 3 and parts[1].endswith('Projects') or \
           parts[0].startswith('Archive') and len(parts) >= 3 and parts[1].endswith('proposals'):
            folder = '/'.join(parts[:3])
        else:
            folder = '/'.join(parts[:2])
        return ('UNREGISTERED_PROJECT?', f'folder "{folder}" not in register')
    return ('NEW_FILE', 'new file in watched area')

def main():
    proj_folders, src_names, tender_folders, src_dir_locs, tender_basenames = load_registers()
    try:
        old = json.load(open(STATE_PATH))
    except (OSError, json.JSONDecodeError):
        old = {}
    now, placeholders = scan()
    now_ser = {k: list(v) for k, v in now.items()}

    new = [k for k in now if k not in old]
    changed = [k for k in now if k in old and list(now[k]) != old[k]]
    deleted = [k for k in old if k not in now]

    non_proj = CFG.get('non_project_folders', [])
    findings = []
    for rel in new + changed:
        tag, note = classify(rel, proj_folders, src_names, non_proj, tender_folders, tender_basenames)
        if tag == 'UNREGISTERED_PROJECT?':
            findings.append((tag, note, note, 'new'))
            continue
        findings.append((tag, rel, note, 'new' if rel in new else 'modified'))
    # collapse duplicate folder findings, keep counts
    collapsed, folder_counts = [], {}
    for t, rel, note, kind in findings:
        if t == 'UNREGISTERED_PROJECT?':
            folder_counts[rel] = folder_counts.get(rel, 0) + 1
        else:
            collapsed.append((t, rel, note, kind))
    for note, cnt in sorted(folder_counts.items()):
        collapsed.append(('UNREGISTERED_PROJECT?', note.split('"')[1], note, f'{cnt} files'))
    findings = collapsed

    # TENDER_MOVED?: registered tender folder no longer seen at its registered path
    for tf, tid in tender_folders.items():
        if any(k.startswith(tf + '/') for k in now):
            continue
        base = os.path.basename(tf)
        moved_to = sorted({os.path.dirname(k) for k in now
                           if k.split('/')[0] in PROPOSAL_ROOTS and base in k.split('/')[1:-1]})
        if moved_to:
            findings.append(('TENDER_MOVED?', moved_to[0],
                f'registered tender {tid}: "{tf}" no longer seen; folder now at "{moved_to[0]}" — update the Drive folder note', 'moved'))
        else:
            findings.append(('TENDER_MOVED?', tf,
                f'registered tender {tid}: registered folder not seen in scan — moved, renamed or deleted?', 'missing'))

    # VERSION_AMBIGUITY: registered source whose location is a folder with multiple candidates
    for cl, sid in src_dir_locs.items():
        p = os.path.join(DRIVE, cl)
        if not os.path.isdir(p): continue
        cands = [n for n in os.listdir(p) if n.lower().endswith(('.docx', '.pdf', '.pptx')) and not ignored(n)]
        if len(cands) > 1:
            findings.append(('VERSION_AMBIGUITY', cl,
                f'{sid}: folder location holds {len(cands)} candidate files — canonical selection required, not alphabetical', 'registered'))

    order = {'TENDER_OUTCOME?':0,'TENDER_MOVED?':1,'UNREGISTERED_PROJECT?':2,'POSSIBLE_TENDER':3,'DRIFT':4,
             'SOURCE_UPDATED':5,'UNREGISTERED_SOURCE':6,'TENDER_FILE':7,'VERSION_AMBIGUITY':8,'NEW_FILE':9,'NON_PROJECT':10}
    findings.sort(key=lambda x: order.get(x[0], 9))

    now_ts = datetime.now()
    stamp = now_ts.strftime('%y/%m/%d %H:%M')
    lines = [f"# Drive sweep — {stamp}\n",
             f"Scanned: {sum(1 for w in CFG['watch_roots'])} watch roots; "
             f"{len(now)} files tracked; {len(placeholders)} cloud placeholders\n"]
    if not old:
        lines.append("**First run — baseline snapshot taken. All existing files treated as baseline; "
                     "findings below are classification of what is already unregistered.**\n")
    for tag in ['TENDER_OUTCOME?','TENDER_MOVED?','UNREGISTERED_PROJECT?','POSSIBLE_TENDER','DRIFT','SOURCE_UPDATED','UNREGISTERED_SOURCE','TENDER_FILE','VERSION_AMBIGUITY','NEW_FILE','NON_PROJECT']:
        group = [f for f in findings if f[0]==tag]
        if not group: continue
        lines.append(f"\n## {tag} ({len(group)})\n")
        for t, rel, note, kind in group[:60]:
            lines.append(f"- `{rel}` — {note} ({kind})")
        if len(group) > 60:
            lines.append(f"- … +{len(group)-60} more")
    if deleted:
        lines.append(f"\n## Deleted since last sweep ({len(deleted)})\n")
        for rel in deleted[:20]: lines.append(f"- `{rel}`")
    if placeholders:
        lines.append(f"\n## Cloud placeholders (not downloaded) ({len(placeholders)})\n")
        for rel in placeholders[:20]: lines.append(f"- `{rel}`")

    report = '\n'.join(lines) + '\n'
    os.makedirs(REPORT_DIR, exist_ok=True)
    dated = os.path.join(REPORT_DIR, now_ts.strftime('SWEEP-%y%m%d-%H%M.md'))
    open(dated,'w').write(report)
    open(os.path.join(REPORT_DIR,'SWEEP_LATEST.md'),'w').write(report)
    json.dump(now_ser, open(STATE_PATH,'w'))

    n_hi = sum(1 for f in findings if f[0] in ('TENDER_OUTCOME?','TENDER_MOVED?','UNREGISTERED_PROJECT?','POSSIBLE_TENDER','DRIFT','UNREGISTERED_SOURCE','SOURCE_UPDATED','TENDER_FILE','VERSION_AMBIGUITY'))
    summary = f"{len(new)} new, {len(changed)} changed, {n_hi} need attention — see SWEEP_LATEST.md"
    try:
        subprocess.run(['osascript','-e',
            f'display notification "{summary}" with title "Toolkit Drive Sweep"'], check=False)
    except OSError:
        pass
    print(f"Sweep {stamp}: {summary}")
    print(f"Report: {dated}")

if __name__ == '__main__':
    main()
