#!/usr/bin/env python3
"""Regenerate project_index.csv from 01_projects.csv + project_index_cards/.
Run from the spillover-toolkit root after any card or register change.
Schema-drift check is built in: verifies register header matches expected fields.
"""
import csv, re, os, sys

EXPECTED_TAIL = ['contracting_role','prime_contractor','relationship_evidence',
                 'review_status','codebook_version','review_batch']
CARD_DIR = 'project_index_cards'
CARD_FIELDS = ['precedent_strength','evidence_strength','contract_value',
               'commercial_reuse','headline_finding','spillover_types_identified',
               'card_status','client_decision_use','lifecycle_status']

def card_field(path, field):
    if not os.path.exists(path): return ''
    txt = open(path).read()
    m = re.search(rf'`{re.escape(field)}`\s*\|\s*([^|]+)\|', txt)
    return m.group(1).strip() if m else ''

def main():
    with open('01_projects.csv') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        missing = [c for c in EXPECTED_TAIL if c not in header]
        if missing:
            sys.exit(f"SCHEMA DRIFT: register missing columns {missing} — repair before indexing")
        register = list(reader)

    rows_out = []
    for row in register:
        pid = row['project_id']
        card_file = os.path.join(CARD_DIR, pid.replace('-','_') + '_index_card.md')
        has_card = os.path.exists(card_file)
        cf = {f: card_field(card_file, f) for f in CARD_FIELDS} if has_card else {}
        spill = cf.get('spillover_types_identified','')
        spill = ';'.join(re.findall(r'(KNOWLEDGE|PRODUCT|NETWORK|OPTION)', spill)) if spill else ''
        lifecycle = cf.get('lifecycle_status','').split('—')[0].strip()[:24] or row['lifecycle_status']
        rows_out.append({
            'project_id': pid, 'project_name': row['canonical_name'], 'client': row['client'],
            'geography': row['geography'], 'date_start': row['date_start'], 'date_end': row['date_end'],
            'lifecycle_status': lifecycle, 'contracting_role': row['contracting_role'],
            'prime_contractor': row['prime_contractor'], 'contract_value': cf.get('contract_value','')[:40],
            'card_status': cf.get('card_status','') or ('NO_CARD' if not has_card else ''),
            'precedent_strength': cf.get('precedent_strength','').split('—')[0].strip()[:12],
            'evidence_strength': cf.get('evidence_strength','').split('—')[0].strip()[:12],
            'spillover_types': spill,
            'client_decision_use': cf.get('client_decision_use','')[:60],
            'commercial_reuse': cf.get('commercial_reuse','').split('—')[0].strip(),
            'headline_finding': cf.get('headline_finding','')[:150],
        })

    with open('project_index.csv','w',newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
        w.writeheader()
        w.writerows(rows_out)
    print(f"project_index.csv regenerated: {len(rows_out)} rows "
          f"({sum(1 for r in rows_out if r['card_status']!='NO_CARD')} with cards)")

if __name__ == '__main__':
    main()
