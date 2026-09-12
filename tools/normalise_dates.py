#!/usr/bin/env python3
"""Normalise all dates to YY/MM/DD across toolkit CSVs and Markdown.
Rules:
  A) machine dates everywhere: YYYY-MM-DD, YYYY.MM.DD, ISO timestamps -> YY/MM/DD
  B) YYYY-MM and bare YYYY: only in date-typed CSV columns or MD table cells
     whose whole value is a date (avoids '2023-26' ranges in prose and
     '2025 Projects' folder paths)
  C) unambiguous English: 'Dec 2017' -> 17/12, 'Oct 24, 2025' -> 25/10/24
"""
import csv, re, glob, sys, io

MONTHS = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,
          'sep':9,'oct':10,'nov':11,'dec':12}
MONTH_RE = r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*'
DATE_COL_RE = re.compile(r'date|deadline|period|window|horizon|as_at', re.I)

def conv_machine(s):
    s = re.sub(r'20(\d{2})-(\d{2})-(\d{2})(T\d{2}:\d{2}:\d{2}Z?)', r'\1/\2/\3\4', s)
    s = re.sub(r'20(\d{2})-(\d{2})-(\d{2})', r'\1/\2/\3', s)
    s = re.sub(r'20(\d{2})\.(\d{2})\.(\d{2})', r'\1/\2/\3', s)
    return s

def conv_english(s):
    def mdy(m):
        mon = MONTHS[m.group(1).lower()[:3]]
        return f"{int(m.group(3))%100:02d}/{mon:02d}/{int(m.group(2)):02d}"
    s = re.sub(MONTH_RE + r'\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(20\d{2})', mdy, s)
    def my(m):
        mon = MONTHS[m.group(1).lower()[:3]]
        return f"{int(m.group(2))%100:02d}/{mon:02d}"
    s = re.sub(MONTH_RE + r'\s+(20\d{2})\b', my, s)
    return s

def conv_datetype(s):
    """Apply YYYY-MM -> YY/MM and bare YYYY -> YY inside a value that is
    entirely date-like (possibly a range or ~-prefixed)."""
    s = conv_machine(s)
    s = re.sub(r'20(\d{2})-(\d{2})\b', r'\1/\2', s)
    s = re.sub(r'\b20(\d{2})\b', r'\1', s)
    return s

def is_pure_date_value(v):
    """Value is only date-ish tokens: digits, /, -, ., ~, spaces, 'to', commas."""
    t = v.strip()
    if not t: return False
    t2 = re.sub(r'20\d{2}[-./]?\d{0,2}[-./]?\d{0,2}|\bto\b|~|\s|,', '', t)
    return t2 == '' or re.fullmatch(r'[-/., ]*', t2) is not None and bool(re.search(r'20\d{2}', t))

# --- CSVs ---
for path in sorted(glob.glob('*.csv')):
    if path.endswith('.bak'): continue
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)
    date_cols = {c for c in header if DATE_COL_RE.search(c)}
    changed = 0
    for row in rows:
        for c in header:
            v = row.get(c)
            if not isinstance(v, str): continue
            orig = v
            if c in date_cols and is_pure_date_value(v):
                v = conv_datetype(v)
                v = conv_english(v)
            else:
                v = conv_machine(v)
                v = conv_english(v)
            if v != orig:
                row[c] = v
                changed += 1
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)
    print(f"{path}: {changed} cells changed")

# --- Markdown files ---
for path in sorted(glob.glob('**/*.md', recursive=True)):
    txt = open(path).read()
    orig = txt
    # Pass B first inside table cells: cell value that is pure-date-like
    def cell_conv(m):
        prefix, val, suffix = m.group(1), m.group(2), m.group(3)
        v = val.strip()
        if is_pure_date_value(v):
            return prefix + ' ' + conv_datetype(v) + ' ' + suffix
        return m.group(0)
    txt = re.sub(r'(\|[^\n|]*\|)\s*([^|\n]+?)\s*(\|)', cell_conv, txt)
    txt = conv_machine(txt)
    txt = conv_english(txt)
    if txt != orig:
        open(path,'w').write(txt)
        print(f"{path}: changed")
