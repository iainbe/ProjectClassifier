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
               'card_status','client_decision_use','lifecycle_status',
               'citation_status','reference_permission','reference_status']

STRENGTH_VALUES = ['STRONG','MODERATE','WEAK','NOT_ESTABLISHED']
CITABLE_STATUSES = ['PUBLIC_REPORT','DELIVERED_WORK']

# Arcs: geographies and themes spanning several distinct projects. Derived view only —
# an arc tag groups projects for browsing and never implies they are the same project.
ARCS = [
    ('LIVERPOOL_LCR', r'Liverpool|LCR|Merseyside'),
    ('MANCHESTER',    r'Manchester|Greater Manchester'),
    ('KIRKLEES',      r'Kirklees|Huddersfield'),
    ('WAKEFIELD',     r'Wakefield|Production Park'),
    ('SOUTH_YORKS',   r'South Yorkshire|SYMCA|Sheffield'),
    ('DERBY',         r'Derby'),
    ('SOLENT',        r'Solent|Hampshire'),
    ('LANCASHIRE',    r'Lancashire|Lancaster|Blackburn'),
    ('WEST_MIDS',     r'West Midlands|WMCA|Birmingham|GBSLEP'),
]


def normalise_strength(raw):
    """Controlled value + the original text as a qualifier.

    The primary value is the first controlled token in the text (so
    'MODERATE-STRONG' is MODERATE); 'NOT_CLEARED' and anything unrecognised
    become NOT_ESTABLISHED.
    """
    if not raw:
        return '', ''
    head = raw.strip()
    for value in STRENGTH_VALUES:
        if re.match(rf'\s*{value}\b', head):
            note = head[len(value):].lstrip(' —-,;').strip()
            return value, note[:80]
    return 'NOT_ESTABLISHED', head[:80]


def cleared_for_use(card_status, citation_status, reference_status):
    """Derived citation gate: REVIEWED card + citable status + cleared reference.

    Returns (YES|NO, blocker). The blocker names every failing condition, so a
    NO is actionable rather than a bare flag.
    """
    blockers = []
    if not card_status.startswith('REVIEWED'):
        blockers.append(f"card_status={card_status or 'NO_CARD'}")
    if not any(citation_status.startswith(s) for s in CITABLE_STATUSES):
        blockers.append(f"citation_status={citation_status or 'UNRECORDED'}")
    if not reference_status.upper().startswith('CLEARED'):
        blockers.append(f"reference_status={reference_status or 'UNRECORDED'}")
    return ('NO', '; '.join(blockers)[:100]) if blockers else ('YES', '')


def arc_tags(geography, project_name):
    text = f"{geography} {project_name}"
    return ';'.join(tag for tag, pattern in ARCS if re.search(pattern, text, re.I))

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
        card_status = cf.get('card_status','') or ('NO_CARD' if not has_card else '')
        citation_status = cf.get('citation_status','').strip()
        reference_status = cf.get('reference_status','').strip()
        strength, strength_note = normalise_strength(cf.get('precedent_strength',''))
        cleared, blocker = cleared_for_use(card_status, citation_status, reference_status)
        rows_out.append({
            'project_id': pid, 'project_name': row['canonical_name'], 'client': row['client'],
            'geography': row['geography'], 'date_start': row['date_start'], 'date_end': row['date_end'],
            'lifecycle_status': lifecycle, 'contracting_role': row['contracting_role'],
            'prime_contractor': row['prime_contractor'], 'contract_value': cf.get('contract_value','')[:40],
            'card_status': card_status,
            'precedent_strength': strength,
            'precedent_note': strength_note,
            'evidence_strength': cf.get('evidence_strength','').split('—')[0].strip()[:12],
            'citation_status': citation_status.split('—')[0].strip()[:30],
            'reference_permission': cf.get('reference_permission','').split('—')[0].strip()[:20],
            'reference_status': reference_status[:40],
            'cleared_for_use': cleared,
            'cleared_blocker': blocker,
            'arc_tags': arc_tags(row['geography'], row['canonical_name']),
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
          f"({sum(1 for r in rows_out if r['card_status']!='NO_CARD')} with cards, "
          f"{sum(1 for r in rows_out if r['cleared_for_use']=='YES')} cleared for use)")

if __name__ == '__main__':
    main()
