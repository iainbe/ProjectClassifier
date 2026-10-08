#!/usr/bin/env python3
"""sync_guard.py — refuse destructive register copies.

Run BEFORE copying one version of a register over another (Drive <-> repo,
staging <-> canonical, branch export <-> working tree). Exits 1 and prints the
reasons if the copy would silently lose rows, drop IDs present in the target,
mismatch the header, or overwrite a newer file.

Usage:
    python3 tools/sync_guard.py SOURCE TARGET [--max-drop N] [--force "reason"]

    SOURCE  file you intend to copy FROM
    TARGET  file you intend to overwrite

Checks (CSV):
    1. header identical (field count AND names)
    2. row-count drop <= --max-drop (default 5)
    3. no ID present in TARGET is absent from SOURCE (column 1 is the ID)
    4. TARGET mtime <= SOURCE mtime (warns if the file being overwritten is newer)

Non-CSV files get check 4 plus a size-delta warning only.

--force "reason"  writes the override to sync_guard_log.csv and exits 0.
"""

import csv
import os
import sys
import time

MAX_DROP_DEFAULT = 5
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sync_guard_log.csv')


def load_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.reader(f))
    return rows[0], [r for r in rows[1:] if r and any(c.strip() for c in r)]


def main():
    args = sys.argv[1:]
    force_reason = None
    max_drop = MAX_DROP_DEFAULT
    positional = []
    i = 0
    while i < len(args):
        if args[i] == '--force':
            force_reason = args[i + 1]; i += 2
        elif args[i] == '--max-drop':
            max_drop = int(args[i + 1]); i += 2
        else:
            positional.append(args[i]); i += 1
    if len(positional) != 2:
        print(__doc__); sys.exit(2)
    src, tgt = positional
    for p in (src, tgt):
        if not os.path.exists(p):
            print(f'REFUSED: missing file {p}'); sys.exit(1)

    problems = []

    src_mt, tgt_mt = os.path.getmtime(src), os.path.getmtime(tgt)
    if tgt_mt > src_mt:
        problems.append(
            f'target is NEWER than source (target {time.ctime(tgt_mt)}, source {time.ctime(src_mt)}) '
            '— the copy would overwrite newer work')

    if src.endswith('.csv') and tgt.endswith('.csv'):
        sh, srows = load_csv(src)
        th, trows = load_csv(tgt)
        if sh != th:
            problems.append(f'header mismatch: source {len(sh)} fields vs target {len(th)} fields')
        drop = len(trows) - len(srows)
        if drop > max_drop:
            problems.append(f'row-count drop {drop} exceeds max {max_drop} ({len(trows)} -> {len(srows)})')
        if len(srows) != len(trows) or drop > 0:
            sids = {r[0] for r in srows if r}
            tids = {r[0] for r in trows if r}
            lost = sorted(tids - sids)
            if lost:
                problems.append(f'{len(lost)} IDs in target absent from source: {", ".join(lost[:10])}'
                                + (' ...' if len(lost) > 10 else ''))
    else:
        ds = os.path.getsize(src) - os.path.getsize(tgt)
        if ds < 0:
            print(f'note: non-CSV; target is {-ds} bytes larger')

    if not problems:
        print('SAFE: copy may proceed')
        sys.exit(0)

    print('REFUSED — copy would be destructive:')
    for p in problems:
        print(' -', p)
    if force_reason:
        os.makedirs(os.path.dirname(LOG), exist_ok=True)
        new = not os.path.exists(LOG)
        with open(LOG, 'a', newline='') as f:
            w = csv.writer(f)
            if new:
                w.writerow(['ts', 'source', 'target', 'problems', 'reason'])
            w.writerow([time.strftime('%y/%m/%dT%H:%M:%S'), src, tgt, ' | '.join(problems), force_reason])
        print(f'FORCED — override logged to sync_guard_log.csv: {force_reason}')
        sys.exit(0)
    print('to override: re-run with --force "reason"')
    sys.exit(1)


if __name__ == '__main__':
    main()
