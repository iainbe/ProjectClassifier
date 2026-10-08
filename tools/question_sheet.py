#!/usr/bin/env python3
"""Question sheet: read-only. Run from the toolkit root.  python3 tools/question_sheet.py

Builds iain_question_sheet.md: every open register fact only Iain can supply, in one place, grouped so one answer can
clear several rows (for example one answer per client). Derived from the registers; rerun after answers are entered.
Answers are written into the registers by Devin, with the basis recorded in 14_fact_provenance.csv.
"""
import csv, collections, re

def rows(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    P = rows('01_projects.csv'); V = rows('07_validation_actions.csv'); S = {}
    for m in sorted(glob_statements(), key=lambda d: d['statement_id']): S[m['statement_id']] = m
    done = [p for p in P if p['lifecycle_status'] == 'COMPLETED']
    L = ['# Questions for Iain (derived; regenerate with tools/question_sheet.py)', '',
         'One pass. For each row answer Y, N or "don\'t know" (don\'t know is recorded as UNKNOWN; nothing is guessed). Rows are grouped so one answer clears several projects.', '']
    # 1 statements
    L += ['## 1. Method statements (approve for use)', '', '| Statement | Needs from you | Approve? |', '|---|---|---|']
    for sid, m in S.items():
        L.append('| %s %s | %s | |' % (sid, m.get('name', ''), m.get('next_action', '')))
    # 2 client acceptance by client
    byc = collections.defaultdict(list)
    for p in done:
        if p.get('client_accepted') in ('', 'UNKNOWN'): byc[p['client']].append(p)
    L += ['', '## 2. Did the client accept the final output? (one answer per client; %d completed projects, %d clients)' % (sum(len(v) for v in byc.values()), len(byc)), '', '| Client | Completed projects | Accepted? Y / N / don\'t know |', '|---|---|---|']
    for c, ps in sorted(byc.items(), key=lambda x: -len(x[1])):
        L.append('| %s | %s | |' % (c[:60], '; '.join('%s (%s)' % (p['canonical_name'][:40], p['project_id']) for p in ps[:4]) + (' +%d more' % (len(ps) - 4) if len(ps) > 4 else '')))
    # 3 citation status unknown
    cs = [p for p in done if p.get('citation_status') in ('', 'UNKNOWN')]
    L += ['', '## 3. May we say we delivered this? (citation status not recorded; %d completed projects)' % len(cs), '', '| Project | Default if you say "yes, delivered" | Answer |', '|---|---|---|']
    for p in cs: L.append('| %s (%s) | DELIVERED_WORK | |' % (p['canonical_name'][:60], p['project_id']))
    # 4 contracting role empty
    cr = [p for p in done if not p.get('contracting_role')]
    L += ['', '## 4. Who held the contract, and what was our part? (contracting role empty; %d completed projects)' % len(cr), '', '| Project | Client | Role: PRIME / DIRECT / SUBCONTRACTOR / ASSOCIATE / ADVISORY (prime if not us) |', '|---|---|---|']
    for p in cr: L.append('| %s (%s) | %s | |' % (p['canonical_name'][:55], p['project_id'], p['client'][:35]))
    # 5 open validation actions assigned to Iain
    op = [v for v in V if v.get('owner') == 'Iain' and v.get('approval_status') in ('PROPOSED', '')]
    L += ['', '## 5. Open validation actions owned by you (%d)' % len(op), '', '| ID | Question | Effort |', '|---|---|---|']
    for v in op: L.append('| %s | %s | %s |' % (v['validation_id'], v['open_question'][:170].replace('|', '/'), v['effort_estimate']))
    open('iain_question_sheet.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('iain_question_sheet.md written: acceptance %d clients, citation %d, roles %d, actions %d' % (len(byc), len(cs), len(cr), len(op)))

def glob_statements():
    import glob
    out = []
    for path in glob.glob('method_statements/MS-*.md'):
        d = {}; inside = False
        for line in open(path, encoding='utf-8'):
            line = line.rstrip('\n')
            if line.strip() == '---': inside = not inside; continue
            m = re.match(r'^([a-z_]+): (.*)$', line) if inside else None
            if m: d[m.group(1)] = m.group(2)
        if d.get('statement_id'): out.append(d)
    return out

if __name__ == '__main__':
    main()
