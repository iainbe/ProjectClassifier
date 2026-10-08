#!/usr/bin/env python3
"""People view: read-only. Run from the toolkit root.

    python3 tools/people_view.py              all people with the projects they can be credited with
    python3 tools/people_view.py --person PER-01

Joins 15_people.csv and 16_involvement.csv to the project register so a team section states, for each person,
the project, their role on it, the contracting arrangement (never implying ownership of a prime's deliverable),
and the basis. A person is credited only with what 16_involvement.csv records; an empty list means nothing is
recorded, not that nothing was done. Contact details and CVs are not held here (ontology decision 14).
"""
import argparse, csv

def rows(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--person'); a = ap.parse_args()
    ppl = rows('15_people.csv'); inv = rows('16_involvement.csv'); reg = {r['project_id']: r for r in rows('01_projects.csv')}
    for p in ppl:
        if a.person and p['person_id'] != a.person: continue
        print('%s  %s  (%s, %s)  named in bids: %s' % (p['person_id'], p['name'], p['organisation'], p['status'], p['named_in_bids_ok']))
        mine = [i for i in inv if i['person_id'] == p['person_id']]
        if not mine: print('   no involvement recorded')
        for i in mine:
            pr = reg.get(i['project_id'], {})
            arr = pr.get('contracting_role', '') or 'contracting role not recorded'
            if pr.get('prime_contractor') and arr not in ('PRIME', 'DIRECT'): arr += ' to ' + pr['prime_contractor']
            print('   %s (%s): %s, %s; contracting: %s; basis: %s' % (pr.get('canonical_name', i['project_id']), i['project_id'], i['role_on_project'], i['period'], arr, i['basis']))
        print()

if __name__ == '__main__':
    main()
