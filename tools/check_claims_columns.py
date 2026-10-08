#!/usr/bin/env python3
"""Claims column check (QA checklist item 14). Read-only. Run from the toolkit root:  python3 -I tools/check_claims_columns.py
Keys every test by header name. Four governed columns of 04_claims.csv must hold only codebook values (empty = not recorded),
and must never hold a value that belongs to another field of the same row (a batch code, method ID, claim type or role list).
Exit 1 on any violation. Self-test: python3 -I tools/check_claims_columns.py --self-test (seeds a bad row, expects failure).
Rules from codebook_v1.3.md section 10 and the evidence-summary line: publication_status, commercial_reuse, reviewer_confidence,
contrary_evidence. A table, so another register or column can be added by adding an entry."""
import csv, io, sys

RULES = {
    'publication_status': {'INTERNAL_ONLY', 'CANDIDATE', 'APPROVED', 'PUBLISHED', 'WITHHELD', 'EXPIRED'},
    'commercial_reuse': {'INTERNAL_ONLY', 'ANONYMISED_DRAFT', 'PERMISSION_PENDING', 'APPROVED_NAMED', 'PROHIBITED'},
    'reviewer_confidence': {'HIGH', 'MEDIUM', 'LOW', 'NOT_ASSESSED'},
    'contrary_evidence': {'PRESENT', 'NONE_FOUND_IN_REVIEW', 'NOT_ASSESSED'},
}
CROSS = ['review_batch', 'claim_type', 'fifth_sector_role', 'method_ids']   # a governed value must not equal these fields

def check(rows):
    h = rows[0]; ix = {c: i for i, c in enumerate(h)}
    bad = []
    for col in RULES: assert col in ix, 'missing column ' + col
    for n, r in enumerate(rows[1:], start=2):
        for col, allowed in RULES.items():
            v = r[ix[col]]
            if v == '' or v in allowed: continue
            why = 'not a codebook value'
            for other in CROSS:
                if other in ix and r[ix[other]] and (v == r[ix[other]] or v in r[ix[other]].split(';')): why = 'copy of ' + other
            bad.append((r[ix['claim_id']], col, v, why, n))
    return bad

def load(path='04_claims.csv'):
    return list(csv.reader(io.StringIO(open(path, 'rb').read().decode('utf-8'), newline='')))

if __name__ == '__main__':
    rows = load()
    if '--self-test' in sys.argv:
        rows = [list(r) for r in rows]; ix = rows[0].index('publication_status'); rows[1][ix] = 'G2-BATCH-X'
        assert check(rows), 'self-test failed: seeded bad row not caught'; print('self-test OK: seeded bad row caught'); sys.exit(0)
    bad = check(rows)
    for b in bad[:60]: print('VIOLATION', *b)
    print(f'{len(bad)} violation(s) in {len(rows) - 1} claims')
    sys.exit(1 if bad else 0)
