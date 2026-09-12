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
STATE_PATH = os.path.join(TK, CFG['state_file'])
REPORT_DIR = os.path.join(TK, CFG['report_dir'])

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
    with open(os.path.join(TK, CFG['register_sources'])) as f:
        for r in csv.DictReader(f):
            for c in ('original_locator', 'controlled_location', 'title'):
                v = (r.get(c) or '').strip()
                if v: src_names.add(os.path.basename(v))
    return proj_folders, src_names

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

def classify(rel, proj_folders, src_names, non_proj):
    # toolkit-internal changes
    if rel.startswith('Website 2026/spillover-toolkit/'):
        return ('DRIFT', 'register/toolkit file changed outside a session')
    # inside a registered project folder?
    for pf, pid in proj_folders.items():
        if rel.startswith(pf + '/'):
            base = os.path.basename(rel)
            tag = 'SOURCE_UPDATED' if base in src_names else 'UNREGISTERED_SOURCE'
            return (tag, f'in registered project {pid}')
    # known non-project folder?
    for npf in non_proj:
        if rel.startswith(npf + '/') or rel == npf:
            return ('NON_PROJECT', 'known admin/resource folder')
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
    proj_folders, src_names = load_registers()
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
        tag, note = classify(rel, proj_folders, src_names, non_proj)
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

    order = {'UNREGISTERED_PROJECT?':0,'POSSIBLE_TENDER':1,'DRIFT':2,
             'SOURCE_UPDATED':3,'UNREGISTERED_SOURCE':4,'NEW_FILE':5,'NON_PROJECT':6}
    findings.sort(key=lambda x: order.get(x[0], 9))

    now_ts = datetime.now()
    stamp = now_ts.strftime('%y/%m/%d %H:%M')
    lines = [f"# Drive sweep — {stamp}\n",
             f"Scanned: {sum(1 for w in CFG['watch_roots'])} watch roots; "
             f"{len(now)} files tracked; {len(placeholders)} cloud placeholders\n"]
    if not old:
        lines.append("**First run — baseline snapshot taken. All existing files treated as baseline; "
                     "findings below are classification of what is already unregistered.**\n")
    for tag in ['UNREGISTERED_PROJECT?','POSSIBLE_TENDER','DRIFT','SOURCE_UPDATED','UNREGISTERED_SOURCE','NEW_FILE','NON_PROJECT']:
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

    n_hi = sum(1 for f in findings if f[0] in ('UNREGISTERED_PROJECT?','POSSIBLE_TENDER','DRIFT','UNREGISTERED_SOURCE','SOURCE_UPDATED'))
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
