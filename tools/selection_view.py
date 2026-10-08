#!/usr/bin/env python3
"""Selection view: read-only candidate list for one tender requirement. Run from the toolkit root.

    python3 tools/selection_view.py --tender T22-VAIMP --label "Case studies of comparable work" \
        --keywords "evaluat|impact|visitor|heritage" --kinds delivered_output,effect_reported,effect_as_evaluator

Takes the eligibility report (run tools/eligibility_report.py first) and keeps the projects whose
subject text matches --keywords and that hold at least one of the evidence kinds the buyer wants.
Candidates are listed in alphabetical order. Nothing is ranked across kinds or scored (Iain
decisions 5 and 6). The keywords and kinds are the operator's reading of the buyer's ask and must be
checked by Iain. Unrecorded facts are UNKNOWN, never PASS. Referee permission is the final
submission stage and is shown, not used to exclude.
Output: selection_views/<tender>.md (derived; regenerate after register changes).
"""
import argparse, csv, os, re

def rows(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tender', required=True); ap.add_argument('--label', required=True)
    ap.add_argument('--keywords', required=True); ap.add_argument('--kinds', required=True)
    a = ap.parse_args()
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
    L = ['# Candidate view: %s - %s' % (a.tender, a.label), '',
         'Derived, read-only. **Not a recommendation and not ranked.** Subject keywords: `%s`. Evidence kinds wanted: %s.' % (a.keywords, ', '.join(kinds)),
         'These are the operator\'s reading of the buyer\'s ask; Iain to correct. Candidates are in alphabetical order; kinds are never ranked against each other.', '',
         '%d candidates.' % len(cands), '',
         '| Project | Client | Lifecycle | Delivered / accepted | Citable | Lapsed option | Method current | Role wording | Referee | Evidence kinds held (claims) |',
         '|---|---|---|---|---|---|---|---|---|---|']
    for _, pid in cands:
        e = elig[pid]
        held = ', '.join('%s %s' % (k.replace('_', ' '), e[k]) for k in ['delivered_output', 'effect_reported', 'effect_as_evaluator', 'documented_use', 'design', 'context'] if int(e[k]) > 0)
        L.append('| %s (%s) | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
            e['project_name'], pid, e['client'][:34], e['lifecycle_status'], e['E1_delivered'], e['E2_citable'], e['E3_lapsed_option'],
            e['E4_method_current'], e['E5_role_wording'], e['referee_permission'].replace('_', ' ').lower(), held))
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
    open('selection_views/%s.md' % a.tender, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('selection_views/%s.md written: %d candidates' % (a.tender, len(cands)))

if __name__ == '__main__':
    main()
