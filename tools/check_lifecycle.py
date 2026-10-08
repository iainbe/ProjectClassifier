#!/usr/bin/env python3
"""Lifecycle check (QA checklist item 15). Read-only. Run from the toolkit root:  python3 -I tools/check_lifecycle.py [--as-of YY/MM/DD]
1. `lifecycle_status` in 01_projects.csv must be one of the codebook values (typos no longer pass as "not delivered").
2. ON_HOLD (Iain 26/10/08) needs a hold note in `notes`:  ON HOLD: <reason>; since <YY or YY/MM or YY/MM/DD or unknown>; resume by <date or unknown>
3. An ON_HOLD project must not carry citation_status DELIVERED_WORK or PUBLIC_REPORT (a paused project is not cited as delivered; use LIVE_WORK).
4. Review prompt (never a failure, never changes a status): an ON_HOLD project whose hold is older than six months or has no since date.
Exit 1 on any violation. The E1 rule in eligibility_report.py (delivered = COMPLETED) is not touched by this check."""
import csv, re, sys

VALUES = {'PROPOSED', 'COMMISSIONED', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED', 'UNKNOWN', 'BID_PENDING', 'ON_HOLD'}
NOTE = re.compile(r'ON HOLD:\s*([^;|]+);\s*since\s*([0-9/]+|unknown);\s*resume by\s*([0-9/]+|unknown)', re.I)

def months(d):
    p = d.split('/')
    return int(p[0]) * 12 + (int(p[1]) if len(p) > 1 else 6)

def check(projects, as_of='26/10/08'):
    bad, prompts = [], []
    for p in projects:
        pid, life = p['project_id'], p.get('lifecycle_status', '')
        if life not in VALUES: bad.append((pid, 'lifecycle_status', life, 'not a codebook value'))
        if life == 'ON_HOLD':
            m = NOTE.search(p.get('notes', ''))
            if not m: bad.append((pid, 'notes', '', 'ON_HOLD needs "ON HOLD: reason; since ...; resume by ..." in notes')); prompts.append((pid, 'no hold note, so no since date'))
            else:
                since = m.group(2)
                if since == 'unknown': prompts.append((pid, 'since date unknown: ask the client or Iain'))
                elif months(as_of) - months(since) > 6: prompts.append((pid, 'hold since %s is more than six months old: review (prompt only)' % since))
            if p.get('citation_status', '') in ('DELIVERED_WORK', 'PUBLIC_REPORT'):
                bad.append((pid, 'citation_status', p['citation_status'], 'a paused project is not cited as delivered (use LIVE_WORK)'))
    return bad, prompts

if __name__ == '__main__':
    P = list(csv.DictReader(open('01_projects.csv', encoding='utf-8', newline='')))
    as_of = sys.argv[sys.argv.index('--as-of') + 1] if '--as-of' in sys.argv else '26/10/08'
    bad, prompts = check(P, as_of)
    for b in bad: print('VIOLATION', *b)
    for pr in prompts: print('REVIEW', *pr)
    print('%d violation(s), %d review prompt(s) in %d projects' % (len(bad), len(prompts), len(P)))
    sys.exit(1 if bad else 0)
