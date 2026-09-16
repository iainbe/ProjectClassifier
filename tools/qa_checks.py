#!/usr/bin/env python3
"""Run the AGENTS.md QA verification checklist over the registers.

Reports findings; changes nothing. Exit 1 if any check fails, so it can gate a
batch. Check numbering follows the AGENTS.md "QA verification checklist".
"""
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MONEY = re.compile(r'£\s?[\d,]*\d')
CAUSAL = re.compile(r'\b(caused|enabled|instrumental|catalysed|catalyzed)\b', re.I)
BASELINE = re.compile(r'\b(gva|employment|turnover|location quotient|\blq\b|companies|businesses|firms|enterprises|headcount)\b', re.I)


def load(name):
    with open(os.path.join(ROOT, name), newline='', encoding='utf-8') as fh:
        return list(csv.DictReader(fh))


def ids(rows, key):
    return {r[key].strip() for r in rows if r[key].strip()}


def main():
    projects = load('01_projects.csv')
    sources = load('02_sources.csv')
    claims = load('04_claims.csv')
    evidence = load('05_evidence_links.csv')
    measurements = load('06_measurements.csv')
    tenders = load('08_tenders.csv')

    tender_source_ids = set()
    for t in tenders:
        for sid in t['source_ids'].replace(';', ',').split(','):
            if sid.strip():
                tender_source_ids.add(sid.strip())

    project_ids = ids(projects, 'project_id')
    claim_ids = ids(claims, 'claim_id')
    source_ids = ids(sources, 'source_id')
    not_awarded = {p['project_id'] for p in projects
                   if p['lifecycle_status'].strip().upper() == 'NOT_AWARDED'}

    findings = []

    def check(n, label, bad, fmt):
        findings.append((n, label, [fmt(r) for r in bad]))

    # 1 unique primary keys
    dupes = []
    for name, rows, key in (('01_projects', projects, 'project_id'),
                            ('02_sources', sources, 'source_id'),
                            ('04_claims', claims, 'claim_id'),
                            ('05_evidence_links', evidence, 'evidence_id'),
                            ('06_measurements', measurements, 'measurement_id'),
                            ('08_tenders', tenders, 'opportunity_id')):
        seen, dup = set(), set()
        for r in rows:
            v = r[key].strip()
            if v in seen:
                dup.add(v)
            seen.add(v)
        dupes += [f'{name}: {v}' for v in sorted(dup)]
    check(1, 'duplicate primary keys', dupes, str)

    # 2 foreign keys
    broken = []
    broken += [f'claim {c["claim_id"]} -> project {c["project_id"]}' for c in claims
               if c['project_id'].strip() and c['project_id'].strip() not in project_ids]
    broken += [f'source {s["source_id"]} -> project {s["project_id"]}' for s in sources
               if s['project_id'].strip() and s['project_id'].strip() not in project_ids]
    broken += [f'evidence {e["evidence_id"]} -> claim {e["claim_id"]}' for e in evidence
               if e['claim_id'].strip() and e['claim_id'].strip() not in claim_ids]
    broken += [f'evidence {e["evidence_id"]} -> source {e["source_id"]}' for e in evidence
               if e['source_id'].strip() and e['source_id'].strip() not in source_ids]
    broken += [f'measurement {m["measurement_id"]} -> claim {m["claim_id"]}' for m in measurements
               if m['claim_id'].strip() and m['claim_id'].strip() not in claim_ids]
    check(2, 'broken foreign keys', broken, str)

    # 3 claims with no project
    check(3, 'claims with empty project_id',
          [c for c in claims if not c['project_id'].strip()],
          lambda c: c['claim_id'])

    # 4 OPTION claims without option_state
    check(4, 'OPTION claims without option_state',
          [c for c in claims
           if c['effect_family'].strip().upper() == 'OPTION' and not c['option_state'].strip()],
          lambda c: c['claim_id'])

    # 5/6 required fields
    check(5, 'claims with empty effect_family',
          [c for c in claims if not c['effect_family'].strip()], lambda c: c['claim_id'])
    check(6, 'claims with empty fifth_sector_role',
          [c for c in claims if not c['fifth_sector_role'].strip()], lambda c: c['claim_id'])

    # 7 unsuccessful bids must expire their DESIGN/OPTION claims
    check(7, 'DESIGN/OPTION claims on NOT_AWARDED projects not EXPIRED',
          [c for c in claims
           if c['project_id'].strip() in not_awarded
           and (c['claim_type'].strip().upper() == 'DESIGN'
                or c['effect_family'].strip().upper() == 'OPTION')
           and c['option_state'].strip().upper() != 'EXPIRED'],
          lambda c: f'{c["claim_id"]} ({c["project_id"]}, option_state={c["option_state"] or "empty"})')

    # 8 EFFECT claims need attribution_strength
    check(8, 'EFFECT claims without attribution_strength',
          [c for c in claims
           if c['claim_type'].strip().upper() == 'EFFECT' and not c['attribution_strength'].strip()],
          lambda c: c['claim_id'])

    # 9 monetary claims need value_basis
    check(9, 'claims with a £ figure but no value_basis',
          [c for c in claims
           if MONEY.search(c['precise_proposition']) and not c['value_basis'].strip()],
          lambda c: c['claim_id'])

    # 10 sector baselines mislabelled (review prompt, not a hard error)
    check(10, 'METHOD_OUTPUT claims matching baseline language (review)',
          [c for c in claims
           if c['claim_type'].strip().upper() == 'METHOD_OUTPUT'
           and BASELINE.search(c['precise_proposition'])],
          lambda c: f'{c["claim_id"]} ({c["project_id"]})')

    # 12 strong causal verbs outside EFFECT (review prompt)
    check(12, 'strong causal verbs in CONTEXT/DESIGN claims (review)',
          [c for c in claims
           if c['claim_type'].strip().upper() in ('CONTEXT', 'DESIGN')
           and CAUSAL.search(c['precise_proposition'])],
          lambda c: f'{c["claim_id"]} ({c["claim_type"]})')

    # 13 sources with no project must be tender pipeline items
    check(13, 'sources with empty project_id not linked to any tender',
          [s for s in sources
           if not s['project_id'].strip()
           and not s['additional_project_ids'].strip()
           and not s['opportunity_ids'].strip()
           and s['source_id'].strip() not in tender_source_ids],
          lambda s: s['source_id'])

    failed = 0
    for n, label, bad in findings:
        if bad:
            failed += 1
            print(f'CHECK {n} — {label}: {len(bad)}')
            for item in bad[:20]:
                print(f'    {item}')
            if len(bad) > 20:
                print(f'    ... and {len(bad) - 20} more')
        else:
            print(f'CHECK {n} — {label}: clean')

    print(f'\n{len(findings) - failed}/{len(findings)} checks clean '
          f'({len(projects)} projects, {len(claims)} claims, {len(sources)} sources)')
    print('Checks 11 (conflation) and the full-read rule are semantic — not automatable here.')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
