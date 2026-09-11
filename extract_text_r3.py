#!/usr/bin/env python3
"""Extract text from R3 supplementary sources (FGTG final report + options doc)."""
import os
from docx import Document

DRIVE = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive")
OUT = os.path.join(DRIVE, "Website 2026/spillover-toolkit/extracted_text")

sources = [
    ("SRC-R3-01", "Archive projects/2024 Projects/2024 Man Met From Good to Great/2025 FGTG reporting/250617 From Good to Great workshop report.docx", "docx"),
    ("SRC-R3-02", "Archive projects/2024 Projects/2024 Man Met From Good to Great/2025 FGTG reporting/250613 GMCA FGTG options for devolved approach.docx", "docx"),
    ("SRC-R3-03", "Archive projects/2024 Projects/2024 Man Met From Good to Great/2025 FGTG reporting/Workshop analysis 110625.docx", "docx"),
]

for source_id, rel_path, ftype in sources:
    full_path = os.path.join(DRIVE, rel_path)
    out_file = os.path.join(OUT, f"{source_id}_v1_full.txt")

    if os.path.exists(out_file):
        print(f"SKIP {source_id}: output already exists")
        continue

    if not os.path.exists(full_path):
        print(f"MISSING {source_id}: {full_path}")
        continue

    try:
        doc = Document(full_path)
        lines = []
        para_count = 0
        table_count = 0

        for para in doc.paragraphs:
            lines.append(para.text)
            para_count += 1

        for table in doc.tables:
            table_count += 1
            lines.append(f"\n[TABLE {table_count}]")
            for row in table.rows:
                cells = [cell.text.strip() for cell in row.cells]
                lines.append(" | ".join(cells))
            lines.append("[/TABLE]\n")

        content = "\n".join(lines)
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"OK {source_id}: {para_count} paragraphs, {table_count} tables, {len(content)} chars, {len(lines)} lines")
        print(f"  -> {out_file}")

        # Warnings
        warnings = []
        warnings.append("Headers/footers not captured")
        warnings.append("Footnotes not captured")
        warnings.append("Images not captured")
        warnings.append("DOCX formatting not captured")
        print(f"  Warnings: {'; '.join(warnings)}")

    except Exception as e:
        print(f"ERROR {source_id}: {e}")
