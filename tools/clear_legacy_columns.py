#!/usr/bin/env python3
"""Clear exact-duplicate displaced values in four 04_claims.csv columns (VAL-S261008-11, Option B).
Dry run unless --write COLUMN. Keys every edit by header name. Run from the toolkit root.
  python3 -I tools/clear_legacy_columns.py                     # report only
  python3 -I tools/clear_legacy_columns.py --record            # write the record and held list
  python3 -I tools/clear_legacy_columns.py --write publication_status
Only clears a value when it is an exact copy of a field that holds it correctly:
  publication_status == review_batch; commercial_reuse in method_ids; reviewer_confidence == claim_type.
Cleared cells become empty (never a default). Values that are not copies are listed in claims_legacy_held_LIST.csv, not cleared."""
import csv, io, sys, subprocess

PATH = '04_claims.csv'
ROLES = {'DESIGNER', 'DELIVERER', 'EVALUATOR', 'LEAD_CONSULTANT', 'ADVISOR', 'INTERPRETER', 'DATA_CONTRIBUTOR'}
TYPES = {'METHOD_OUTPUT', 'DESIGN', 'CONTEXT', 'EFFECT', 'BID_SUPPORT_DELIVERED'}

def load():
    raw = open(PATH, 'rb').read()
    nl = '\r\n' if raw.count(b'\r\n') > raw.count(b'\n') / 2 else '\n'
    rows = list(csv.reader(io.StringIO(raw.decode('utf-8'), newline='')))
    return rows, nl

def classify(rows):
    h = rows[0]; ix = {c: i for i, c in enumerate(h)}
    clear, held = [], []
    for n, r in enumerate(rows[1:], start=1):
        cid, ctype, batch = r[ix['claim_id']], r[ix['claim_type']], r[ix['review_batch']]
        ps, cr, rc, ce = r[ix['publication_status']], r[ix['commercial_reuse']], r[ix['reviewer_confidence']], r[ix['contrary_evidence']]
        if ps and ps != 'INTERNAL_ONLY' and ps == batch: clear.append((n, cid, 'publication_status', ps, ctype, batch))
        elif ps and ps not in ('INTERNAL_ONLY',) and (ps.startswith('G2-BATCH') or ps.startswith('S-')): held.append((n, cid, 'publication_status', ps, ctype, batch))
        if cr.startswith('M-'):
            if cr in r[ix['method_ids']].split(';'): clear.append((n, cid, 'commercial_reuse', cr, ctype, batch))
            else: held.append((n, cid, 'commercial_reuse', cr, ctype, batch))
        if rc in TYPES:
            if rc == ctype: clear.append((n, cid, 'reviewer_confidence', rc, ctype, batch))
            else: held.append((n, cid, 'reviewer_confidence', rc, ctype, batch))
        if ce and ce != 'NONE_FOUND_IN_REVIEW' and set(ce.split(';')) <= ROLES:
            held.append((n, cid, 'contrary_evidence', ce, ctype, batch))
    return clear, held

def main():
    rows, nl = load(); h = rows[0]; ix = {c: i for i, c in enumerate(h)}
    clear, held = classify(rows)
    base = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
    by = {}
    for c in clear: by[c[2]] = by.get(c[2], 0) + 1
    print('to clear:', by, '| held:', len(held), '| base commit', base)
    if '--record' in sys.argv:
        def w(path, header, data):
            b = io.StringIO(newline=''); wr = csv.writer(b, lineterminator='\n'); wr.writerow(header); wr.writerows(data)
            open(path, 'w', encoding='utf-8', newline='').write(b.getvalue())
        w('claims_legacy_clear_RECORD.csv', ['claim_id', 'column', 'old_value', 'new_value', 'claim_type', 'review_batch', 'claims_row_number', 'base_commit', 'date', 'reason'],
          [(c[1], c[2], c[3], '', c[4], c[5], c[0], base, '26/10/08', 'exact copy of ' + {'publication_status': 'review_batch', 'commercial_reuse': 'method_ids', 'reviewer_confidence': 'claim_type'}[c[2]]) for c in clear])
        w('claims_legacy_held_LIST.csv', ['claim_id', 'column', 'old_value', 'current_claim_type', 'review_batch', 'claims_row_number', 'current_fifth_sector_role', 'base_commit', 'note'],
          [(c[1], c[2], c[3], c[4], c[5], c[0], rows[c[0]][ix['fifth_sector_role']], base,
            'pre-retype claim type; see claims_repair_RECORD.csv' if c[2] == 'reviewer_confidence' else 'older role reading; not in any other record file' if c[2] == 'contrary_evidence' else 'review') for c in held])
        print('wrote claims_legacy_clear_RECORD.csv', len(clear), 'and claims_legacy_held_LIST.csv', len(held))
    if '--write' in sys.argv:
        col = sys.argv[sys.argv.index('--write') + 1]; assert col in ('publication_status', 'commercial_reuse', 'reviewer_confidence')
        n = 0
        for (rn, cid, c, old, _t, _b) in clear:
            if c == col:
                r = rows[rn]; assert r[ix['claim_id']] == cid and r[ix[col]] == old
                r[ix[col]] = ''; n += 1
        b = io.StringIO(newline=''); csv.writer(b, lineterminator=nl).writerows(rows)
        open(PATH, 'wb').write(b.getvalue().encode('utf-8')); print('cleared', n, 'cells in', col)

if __name__ == '__main__': main()
