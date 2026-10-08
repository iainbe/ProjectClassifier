#!/usr/bin/env python3
"""Record a selection (Iain decision 15, 26/10/08). Run from the toolkit root. Appends to 13_selections.csv.

    python3 tools/record_selection.py --requirements T22-VAIMP --chosen P27-WAKECDF,P78-BEATLES,... \
        [--reason "P22-LCRFILM=EVIDENCE_GAP:interim only"] [--wording "P78-BEATLES=modelled annual estimate of ..."] \
        [--order alpha|proposed] [--write]

Without --write it only prints the rows (dry run). It rebuilds the same candidate list the selection view shows
(tools/selection_view.build), then writes ONE ROW PER CANDIDATE: its position in the default (alphabetical) order and
in the proposed order, whether Iain chose it, and for each candidate not chosen a reason code. Candidates with no
reason given are recorded as NOT_RECORDED, never defaulted. A chosen project that is not in the view is recorded as
OUTSIDE_VIEW. The log is append-only: later buyer feedback is added with --outcome, which appends an OUTCOME row.

Reason codes: WEAKER_FIT, EVIDENCE_GAP, ROLE_WORDING, RESTRICTED_OR_CONSENT, REFEREE_UNLIKELY, PAGE_LIMIT, OTHER, NOT_RECORDED.
The log is for audit and for testing the trial ordering after 15 to 20 scored uses; it feeds no ranking.
"""
import argparse, csv, datetime, os, re, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import selection_view

HEAD = ['selection_id', 'record_type', 'tender_id', 'item', 'recorded_at', 'project_id', 'project_name', 'default_position',
        'proposed_position', 'chosen', 'reason_code', 'reason_note', 'wording_used', 'referee_outcome', 'score_received',
        'score_scale', 'outcome', 'requirements_frozen_on', 'recorded_by']
REASONS = {'WEAKER_FIT', 'EVIDENCE_GAP', 'ROLE_WORDING', 'RESTRICTED_OR_CONSENT', 'REFEREE_UNLIKELY', 'PAGE_LIMIT', 'OTHER', 'NOT_RECORDED'}
FILE = '13_selections.csv'

def parse_req(tender):
    item = {}; head = {}; cur = None
    for line in open('tender_requirements/%s.md' % tender, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('## item:'): cur = line.split(':', 1)[1].strip(); item[cur] = {}; continue
        m = re.match(r'^([a-z_]+): (.*)$', line)
        if m: (item[cur] if cur else head)[m.group(1)] = m.group(2)
    return head, item

def kv(text):
    out = {}
    for part in [x for x in (text or '').split(';') if x.strip()]:
        k, _, v = part.partition('=')
        out[k.strip()] = v.strip()
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--requirements', required=True); ap.add_argument('--item', default='case-studies')
    ap.add_argument('--chosen', default=''); ap.add_argument('--reason', default=''); ap.add_argument('--wording', default='')
    ap.add_argument('--referee', default='', help='PROJECT=outcome;...'); ap.add_argument('--geography', default='')
    ap.add_argument('--outcome', metavar='SELECTION_ID'); ap.add_argument('--project'); ap.add_argument('--score'); ap.add_argument('--scale', default='10'); ap.add_argument('--result', default='')
    ap.add_argument('--write', action='store_true'); ap.add_argument('--by', default='Devin')
    a = ap.parse_args()
    head, items = parse_req(a.requirements); it = items[a.item]
    now = datetime.datetime.now().strftime('%y/%m/%dT%H:%M:%S')
    existing = list(csv.DictReader(open(FILE, newline='', encoding='utf-8'))) if os.path.exists(FILE) else []
    out = []
    if a.outcome:
        prev = [r for r in existing if r['selection_id'] == a.outcome and r['record_type'] == 'SELECTION' and r['project_id'] == a.project]
        if not prev: sys.exit('no SELECTION row for %s / %s' % (a.outcome, a.project))
        p = prev[0]
        out.append({**{k: '' for k in HEAD}, 'selection_id': a.outcome, 'record_type': 'OUTCOME', 'tender_id': p['tender_id'], 'item': p['item'],
                    'recorded_at': now, 'project_id': a.project, 'project_name': p['project_name'], 'score_received': a.score or '',
                    'score_scale': a.scale, 'outcome': a.result, 'recorded_by': a.by})
    else:
        kinds, elig, reg, alpha, near, _ = selection_view.build(it['keywords'], it['kinds'], 'alpha', a.geography)
        _, _, _, prop, _, _ = selection_view.build(it['keywords'], it['kinds'], 'proposed', a.geography)
        apos = {pid: i for i, (_, pid) in enumerate(alpha, 1)}; ppos = {pid: i for i, (_, pid) in enumerate(prop, 1)}
        chosen = [c.strip() for c in a.chosen.split(',') if c.strip()]
        reasons = {}
        for k, v in kv(a.reason).items():
            code, _, note = v.partition(':'); code = code.strip()
            if code not in REASONS: sys.exit('unknown reason code %s' % code)
            reasons[k] = (code, note.strip())
        wording = kv(a.wording); referee = kv(a.referee)
        n = len({r['selection_id'] for r in existing if r['tender_id'] == head['tender_id'] and r['item'] == a.item}) + 1
        sid = 'SEL-%s-%s-%02d' % (head['tender_id'], a.item, n)
        for pid in chosen:
            if pid not in reg: sys.exit('unknown project %s' % pid)
        listed = [pid for _, pid in alpha]
        for pid in listed + [c for c in chosen if c not in listed]:
            inview = pid in apos
            ch = pid in chosen
            code, note = ('', '') if ch else reasons.get(pid, ('NOT_RECORDED', ''))
            if ch and not inview: code, note = 'OUTSIDE_VIEW', 'chosen but not in the candidate view'
            out.append({'selection_id': sid, 'record_type': 'SELECTION', 'tender_id': head['tender_id'], 'item': a.item, 'recorded_at': now,
                        'project_id': pid, 'project_name': reg[pid]['canonical_name'], 'default_position': apos.get(pid, ''),
                        'proposed_position': ppos.get(pid, ''), 'chosen': 'Y' if ch else 'N', 'reason_code': code, 'reason_note': note,
                        'wording_used': wording.get(pid, '') if ch else '', 'referee_outcome': referee.get(pid, '') if ch else '',
                        'score_received': '', 'score_scale': '', 'outcome': '', 'requirements_frozen_on': head.get('frozen_on', ''), 'recorded_by': a.by})
    for r in out:
        print(' | '.join(str(r[k]) for k in ['selection_id', 'record_type', 'project_id', 'default_position', 'proposed_position', 'chosen', 'reason_code']))
    if not a.write:
        print('\nDRY RUN: %d rows not written (add --write)' % len(out)); return
    new = not os.path.exists(FILE)
    with open(FILE, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=HEAD, lineterminator='\n')
        if new: w.writeheader()
        w.writerows(out)
    print('\n%d rows appended to %s' % (len(out), FILE))

if __name__ == '__main__':
    main()
