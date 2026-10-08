#!/usr/bin/env python3
"""Eligibility report: read-only. Run from the toolkit root.

For every project in 01_projects.csv, returns PASS / FAIL / UNKNOWN on five checks and
shows the kinds of evidence it holds. Nothing is stored as a tier, score or ranking.
Unrecorded facts are UNKNOWN, never PASS (no check is weakened; Iain rule 26/10/07).

Checks (ontology_v2_DRAFT.md section 4, decisions 2-6):
  E1 Delivered       lifecycle COMPLETED and client_accepted = Y
  E2 Citable         citation_status is DELIVERED_WORK or PUBLIC_REPORT
  E3 Lapsed option   on a project with a NOT_AWARDED marker (lifecycle or programme_status),
                     every DESIGN and OPTION claim must be EXPIRED
  E4 Method current  has method rows and none SUPERSEDED (UNKNOWN when there are no rows); also FAIL when a method row
                     links (statement_id) to a method statement whose status is SUPERSEDED (added 26/10/08, additive:
                     every earlier UNKNOWN, PASS and FAIL result is unchanged). A linked DRAFT or missing statement only adds a note
  E5 Role wording    contracting_role set, and prime_contractor set when the role is not PRIME/DIRECT
Referee permission is NOT a check: referees are cited in the tender and asked only once
shortlisted (Iain 26/10/08); the state is derived from 11_permission_requests.csv. Evidence kinds are parallel and never ranked against each other.

Provenance (Iain decision 12, 26/10/08): 14_fact_provenance.csv records the basis of backfilled gating facts
(DOCUMENT, WRITTEN_CLIENT, VERBAL_CLIENT, IAIN_STATEMENT, INFERRED). The report shows the basis beside the E1, E2
and E5 results and counts results with no basis recorded. Basis is displayed only: it never changes a PASS, FAIL
or UNKNOWN.

Outputs: eligibility_report.csv and eligibility_report.md (derived; regenerate after any
change to the register, claims, methods or permission file).
"""
import csv, collections, glob, os, re

def rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def statement_status():
    """statement_id -> status, read from the header of method_statements/MS-*.md."""
    out = {}
    for path in glob.glob('method_statements/MS-*.md'):
        inside = False; d = {}
        for line in open(path, encoding='utf-8'):
            line = line.rstrip('\n')
            if line.strip() == '---': inside = not inside; continue
            m = re.match(r'^([a-z_]+): (.*)$', line) if inside else None
            if m: d[m.group(1)] = m.group(2)
        if d.get('statement_id'): out[d['statement_id']] = d.get('status', '')
    return out

def main():
    P = rows('01_projects.csv'); C = rows('04_claims.csv'); M = rows('03_methods.csv')
    claims = collections.defaultdict(list)
    for c in C:
        claims[c['project_id']].append(c)
    methods = collections.defaultdict(list)
    for m in M:
        methods[m['project_id']].append(m)
    est = set()
    if os.path.exists('11_permission_requests.csv'):
        for r in rows('11_permission_requests.csv'):
            if 'NAMED_REFEREE' in r['permission_scope'] and r['status'] == 'ESTABLISHED':
                est.update(x.strip() for x in r['project_ids'].split(';') if x.strip())

    prov = {}
    if os.path.exists('14_fact_provenance.csv'):
        for r in rows('14_fact_provenance.csv'):
            prov[(r['project_id'], r['field'])] = r['basis']   # later rows win
    stmt = statement_status()
    out = []
    for p in P:
        pid = p['project_id']; cl = claims.get(pid, []); life = p['lifecycle_status']
        # E1
        acc = p.get('client_accepted', '') or 'UNKNOWN'
        if life == 'COMPLETED':
            e1 = 'PASS' if acc == 'Y' else ('FAIL' if acc == 'N' else 'UNKNOWN')
        else:
            e1 = 'FAIL'
        # E2
        cit = p.get('citation_status', '') or 'UNKNOWN'
        e2 = 'PASS' if cit in ('DELIVERED_WORK', 'PUBLIC_REPORT') else ('UNKNOWN' if cit == 'UNKNOWN' else 'FAIL')
        # E3
        marked = life == 'NOT_AWARDED' or p.get('programme_status', '') == 'NOT_AWARDED'
        bad = [c for c in cl if marked and (c['claim_type'] == 'DESIGN' or c['effect_family'] == 'OPTION') and c['option_state'] != 'EXPIRED']
        e3 = 'FAIL' if bad else 'PASS'
        # E4
        ms = methods.get(pid, [])
        e4 = 'UNKNOWN' if not ms else ('FAIL' if any(m['method_status'] == 'SUPERSEDED' for m in ms) else 'PASS')
        e4_note = ''
        linked = sorted({m.get('statement_id', '') for m in ms if m.get('statement_id')})
        if linked:
            if e4 == 'PASS' and any(stmt.get(x) == 'SUPERSEDED' for x in linked):
                e4 = 'FAIL'; e4_note = 'linked method statement is SUPERSEDED: ' + ';'.join(x for x in linked if stmt.get(x) == 'SUPERSEDED')
            else:
                notes = ['%s is %s' % (x, stmt[x]) for x in linked if x in stmt and stmt[x] != 'CURRENT'] + ['%s not found' % x for x in linked if x not in stmt]
                e4_note = 'linked statement ' + '; '.join(notes) if notes else ''
        # E5
        role = p.get('contracting_role', ''); prime = p.get('prime_contractor', '')
        if not role:
            e5 = 'UNKNOWN'
        elif role in ('PRIME', 'DIRECT') or prime:
            e5 = 'PASS'
        else:
            e5 = 'UNKNOWN'
        # evidence kinds (parallel counts)
        k = collections.Counter()
        for c in cl:
            t = c['claim_type']; role_c = c.get('fifth_sector_role', '')
            if t in ('METHOD_OUTPUT', 'BID_SUPPORT_DELIVERED'): k['delivered_output'] += 1
            elif t == 'EFFECT': k['effect_as_evaluator' if 'EVALUATOR' in role_c else 'effect_reported'] += 1
            elif t == 'DECISION_USE': k['documented_use'] += 1
            elif t == 'DESIGN': k['design'] += 1
            elif t == 'CONTEXT': k['context'] += 1
        corroborated = sum(1 for c in cl if c.get('outcome_status') == 'CORROBORATED')
        out.append({
            'project_id': pid, 'project_name': p['canonical_name'], 'client': p['client'], 'lifecycle_status': life,
            'E1_delivered': e1, 'E2_citable': e2, 'E3_lapsed_option': e3, 'E4_method_current': e4, 'E5_role_wording': e5,
            'delivered_output': k['delivered_output'], 'effect_reported': k['effect_reported'],
            'effect_as_evaluator': k['effect_as_evaluator'], 'documented_use': k['documented_use'],
            'design': k['design'], 'context': k['context'], 'corroborated_claims': corroborated,
            'E1_basis': prov.get((pid, 'client_accepted'), '') or ('no basis recorded' if e1 == 'PASS' else ''),
            'E2_basis': prov.get((pid, 'citation_status'), '') or ('no basis recorded' if e2 == 'PASS' else ''),
            'E5_basis': prov.get((pid, 'contracting_role'), '') or ('no basis recorded' if e5 == 'PASS' else ''),
            'E4_note': e4_note,
            'referee_permission': 'ESTABLISHED' if pid in est else 'NOT_ESTABLISHED',
            'fully_determinable': 'YES' if 'UNKNOWN' not in (e1, e2, e3, e4, e5) else 'NO',
        })
    with open('eligibility_report.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

    checks = ['E1_delivered', 'E2_citable', 'E3_lapsed_option', 'E4_method_current', 'E5_role_wording']
    done = [o for o in out if o['lifecycle_status'] == 'COMPLETED']
    L = ['# Eligibility report (derived, read-only)', '',
         'Generated by `tools/eligibility_report.py`. UNKNOWN means not recorded; it is never treated as a pass.', '',
         '## Counts over all %d projects' % len(out), '', '| Check | PASS | FAIL | UNKNOWN |', '|---|---|---|---|']
    for c in checks:
        n = collections.Counter(o[c] for o in out)
        L.append('| %s | %d | %d | %d |' % (c, n['PASS'], n['FAIL'], n['UNKNOWN']))
    L += ['', 'Completed projects: %d. Fully determinable (no UNKNOWN): %d. All five PASS: %d.' % (
        len(done), sum(o['fully_determinable'] == 'YES' for o in out),
        sum(all(o[c] == 'PASS' for c in checks) for o in out)), '',
        '## What blocks the most completed projects (fix these first)', '']
    unk = {c: [o for o in done if o[c] == 'UNKNOWN'] for c in checks}
    L += ['| Missing fact | Completed projects blocked |', '|---|---|']
    labels = {'E1_delivered': 'Client acceptance not recorded', 'E2_citable': 'Citation status not recorded',
              'E3_lapsed_option': 'Open design/option claims on a lapsed bid', 'E4_method_current': 'No method rows registered',
              'E5_role_wording': 'Contracting role or prime contractor missing'}
    for c in sorted(checks, key=lambda c: -len(unk[c])):
        L.append('| %s | %d |' % (labels[c], len(unk[c])))
    L += ['', '## Basis of PASS results (from 14_fact_provenance.csv)', '', '| Check | PASS with a recorded basis | PASS with no basis recorded |', '|---|---|---|']
    for c, b in [('E1_delivered', 'E1_basis'), ('E2_citable', 'E2_basis'), ('E5_role_wording', 'E5_basis')]:
        passed = [o for o in out if o[c] == 'PASS']
        none = sum(1 for o in passed if o[b] == 'no basis recorded')
        L.append('| %s | %d | %d |' % (c, len(passed) - none, none))
    byclient = collections.Counter(o['client'] for o in unk['E1_delivered'])
    L += ['', '## Client acceptance, grouped by client (one answer per client may clear several projects)', '',
          '| Client | Completed projects with acceptance unrecorded |', '|---|---|']
    for cl_, n in byclient.most_common(): L.append('| %s | %d |' % (cl_, n))
    L += ['', '## Citation status not recorded (completed projects)', '']
    L += ['- %s (%s)' % (o['project_name'], o['project_id']) for o in unk['E2_citable']] or ['- none']
    L += ['', '## Contracting role or prime contractor missing (completed projects)', '']
    L += ['- %s (%s)' % (o['project_name'], o['project_id']) for o in unk['E5_role_wording']] or ['- none']
    L += ['', '## Failing checks on completed projects', '']
    for c in checks:
        fails = [o for o in done if o[c] == 'FAIL']
        if fails: L += ['- %s: %s' % (c, '; '.join('%s (%s)' % (o['project_name'], o['project_id']) for o in fails))]
    L += ['', 'Evidence kinds are shown side by side in `eligibility_report.csv` and are never ranked against each other.',
          'Referee permission is the final submission stage and is not a check here.']
    open('eligibility_report.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('eligibility_report.csv and .md written: %d projects' % len(out))

if __name__ == '__main__':
    main()
