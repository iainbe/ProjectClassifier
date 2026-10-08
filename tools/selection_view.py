#!/usr/bin/env python3
"""Selection view: read-only candidate list for one tender requirement. Run from the toolkit root.

    python3 tools/selection_view.py --requirements T22-VAIMP            (reads tender_requirements/T22-VAIMP.md)
    python3 tools/selection_view.py --tender T22-VAIMP --label "Case studies of comparable work" \
        --keywords "evaluat|impact|visitor|heritage" --kinds delivered_output,effect_reported,effect_as_evaluator

Takes the eligibility report (run tools/eligibility_report.py first) and keeps the projects whose
subject text matches --keywords and that hold at least one of the evidence kinds the buyer wants.
Candidates are listed in alphabetical order. Nothing is ranked across kinds or scored (Iain
decisions 5 and 6). The keywords and kinds are the operator's reading of the buyer's ask and must be
checked by Iain. Unrecorded facts are UNKNOWN, never PASS. The basis of a PASS (document, verbal client, Iain statement, inferred) is shown in brackets from 14_fact_provenance.csv; it never changes the result. Referee permission is the final
submission stage and is shown, not used to exclude.

Ordering (Iain decision 10b, 26/10/08, option C): the default is alphabetical, no ranking. Evidence kind is a
filter only. `--order proposed` additionally shows the PROPOSED order for comparison with your own choices:
number of wanted kinds held, then contracting role (PRIME/DIRECT, then SUBCONTRACTOR, then ASSOCIATE/ADVISORY,
then not recorded), then most recent end date, then geography if --geography is given. Each placement
is explained in words in a 'Placed because' column; there is no score. The proposed order is a trial, not a
rule: it is written to selection_views/<tender>_proposed_order.md and never replaces the default view.
Output: selection_views/<tender>.md (derived; regenerate after register changes).
"""
import argparse, csv, os, re

def rows(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def build(keywords, kinds_text, order='alpha', geography=''):
    """Candidate lists for one requirement item. Returns (kinds, elig, reg, cands, near, reasons).
    cands are (name, project_id) in the chosen order; reasons maps project_id to its 'placed because' text."""
    class a:  # keeps the original expressions unchanged
        pass
    a.keywords = keywords; a.kinds = kinds_text; a.order = order; a.geography = geography
    kinds = [k.strip() for k in a.kinds.split(',')]; rx = re.compile(a.keywords, re.I)
    elig = {r['project_id']: r for r in rows('eligibility_report.csv')}
    reg = {r['project_id']: r for r in rows('01_projects.csv')}
    checks = ['E1_delivered', 'E2_citable', 'E3_lapsed_option', 'E4_method_current', 'E5_role_wording']
    need = {'E1_delivered': 'client acceptance', 'E2_citable': 'citation status', 'E4_method_current': 'method rows',
            'E5_role_wording': 'contracting role / prime contractor'}
    cands = []; near = []
    for pid, e in elig.items():
        p = reg[pid]
        text = ' '.join([p['canonical_name'], p['sector_activity'], p['scope_decision']])
        if rx.search(text):
            if any(int(e[k]) > 0 for k in kinds):
                cands.append((p['canonical_name'].lower(), pid))
            else:
                near.append((p['canonical_name'].lower(), pid))
    cands.sort(); near.sort()
    reasons = {}
    if a.order == 'proposed':
        def datekey(v):
            m = re.match(r'^(\d\d)(?:/(\d\d))?(?:/(\d\d?))?$', v or '')
            return (int(m.group(1)) * 10000 + int(m.group(2) or 0) * 100 + int(m.group(3) or 0)) if m else 0
        rolerank = {'PRIME': 0, 'DIRECT': 0, 'SUBCONTRACTOR': 1, 'ASSOCIATE': 2, 'BOP_ASSOCIATE': 2, 'ADVISORY': 2}
        def key(item):
            pid = item[1]; e = elig[pid]; p = reg[pid]
            nk = sum(1 for k in kinds if int(e[k]) > 0)
            role = p.get('contracting_role', '')
            geo = 0 if (a.geography and a.geography.lower() in p.get('geography', '').lower()) else 1
            reasons[pid] = '%d of %d wanted kinds; role %s; ended %s%s' % (
                nk, len(kinds), role or 'not recorded', p.get('date_end') or 'not recorded',
                ('; geography ' + ('matches' if geo == 0 else 'differs')) if a.geography else '')
            return (-nk, rolerank.get(role, 3), -datekey(p.get('date_end', '')), geo, item[0])
        cands.sort(key=key)
    return kinds, elig, reg, cands, near, reasons

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tender'); ap.add_argument('--label')
    ap.add_argument('--keywords'); ap.add_argument('--kinds')
    ap.add_argument('--requirements', help='tender id; reads tender_requirements/<id>.md (Iain decision 13, 26/10/08)')
    ap.add_argument('--item', default='case-studies', help='item heading in the requirements file')
    ap.add_argument('--order', choices=['alpha', 'proposed'], default='alpha')
    ap.add_argument('--geography', default='')
    a = ap.parse_args()
    req_note = ''
    if a.requirements:
        item = {}; head = {}; cur = None
        for line in open('tender_requirements/%s.md' % a.requirements, encoding='utf-8'):
            line = line.rstrip('\n')
            if line.startswith('## item:'): cur = line.split(':', 1)[1].strip(); item[cur] = {}; continue
            m = re.match(r'^([a-z_]+): (.*)$', line)
            if m: (item[cur] if cur else head)[m.group(1)] = m.group(2)
        it = item[a.item]
        a.tender = a.tender or head['tender_id']; a.label = a.label or it['label']
        a.keywords = a.keywords or it['keywords']; a.kinds = a.kinds or it['kinds']
        req_note = 'Requirements read from `tender_requirements/%s.md` (item `%s`, frozen %s, %s).' % (a.requirements, a.item, head.get('frozen_on', '?'), head.get('status', ''))
    if not (a.tender and a.label and a.keywords and a.kinds):
        ap.error('give --requirements, or all of --tender --label --keywords --kinds')
    kinds, elig, reg, cands, near, reasons = build(a.keywords, a.kinds, a.order, a.geography)
    checks = ['E1_delivered', 'E2_citable', 'E3_lapsed_option', 'E4_method_current', 'E5_role_wording']
    need = {'E1_delivered': 'client acceptance', 'E2_citable': 'citation status', 'E4_method_current': 'method rows',
            'E5_role_wording': 'contracting role / prime contractor'}
    L = ['# Candidate view: %s - %s' % (a.tender, a.label), ''] + ([req_note, ''] if req_note else []) + [
         'Derived, read-only. **Not a recommendation and not ranked.** Subject keywords: `%s`. Evidence kinds wanted: %s.' % (a.keywords, ', '.join(kinds)),
         'These are the operator\'s reading of the buyer\'s ask; Iain to correct. Candidates are in alphabetical order; kinds are never ranked against each other.', '',
         '%d candidates.' % len(cands), '',
         '| Project | Client | Lifecycle | Delivered / accepted | Citable | Lapsed option | Method current | Role wording | Referee | Evidence kinds held (claims) |' + (' Placed because |' if reasons else ''),
         '|---|---|---|---|---|---|---|---|---|---|' + ('---|' if reasons else '')]
    for _, pid in cands:
        e = elig[pid]
        held = ', '.join('%s %s' % (k.replace('_', ' '), e[k]) for k in ['delivered_output', 'effect_reported', 'effect_as_evaluator', 'documented_use', 'design', 'context'] if int(e[k]) > 0)
        bs = lambda c, b: e[c] + (' (' + e[b].replace('_', ' ').lower() + ')' if e[c] == 'PASS' and e[b] else '')
        L.append('| %s (%s) | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            e['project_name'], pid, e['client'][:34], e['lifecycle_status'], bs('E1_delivered', 'E1_basis'), bs('E2_citable', 'E2_basis'), e['E3_lapsed_option'],
            e['E4_method_current'], bs('E5_role_wording', 'E5_basis'), e['referee_permission'].replace('_', ' ').lower(), held) + (' %s |' % reasons[pid] if reasons else ''))
    L += ['', '## Facts needed before each candidate can be used (UNKNOWN or FAIL)', '']
    for _, pid in cands:
        e = elig[pid]
        gaps = [need[c] + (' (FAIL)' if e[c] == 'FAIL' else '') for c in checks if e[c] in ('UNKNOWN', 'FAIL') and c in need]
        L.append('- %s (%s): %s' % (e['project_name'], pid, '; '.join(gaps) if gaps else 'none'))
    L += ['', '## Subject matches with NO claims of the wanted kinds registered (not in the table above)', '',
          'These match the subject but hold none of the wanted evidence kinds in the claims register, so the table above cannot show them. This does not mean they lack the evidence: the claims may simply not be coded yet.', '']
    for _, pid in near:
        e = elig[pid]
        held = ', '.join('%s %s' % (k.replace('_', ' '), e[k]) for k in ['delivered_output', 'effect_reported', 'effect_as_evaluator', 'documented_use', 'design', 'context'] if int(e[k]) > 0) or 'no claims coded'
        L.append('- %s (%s), %s, %s: holds %s' % (e['project_name'], pid, e['client'][:30], e['lifecycle_status'], held))
    if not near: L.append('- none')
    L += ['', '## Referees', '',
          'Referees are normally cited by name in the tender and only asked once the bidder is shortlisted (Iain, 26/10/08). Referee permission is therefore not needed to build or submit the case-study sheet, and the referee column above is for later. The brief asks for a contact for each case study "that is willing to give a reference", so the contact named for each should be someone likely to agree.']
    os.makedirs('selection_views', exist_ok=True)
    out = 'selection_views/%s%s.md' % (a.tender, '_proposed_order' if reasons else '')
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('%s written: %d candidates' % (out, len(cands)))

if __name__ == '__main__':
    main()
