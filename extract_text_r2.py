#!/usr/bin/env python3
"""R2 source extraction script. Extracts approved M1 manifest sources to full derivatives.
Never overwrites existing files. Records warnings and coverage."""
import os, sys, datetime, traceback

DRIVE = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive"
OUT = os.path.join(DRIVE, "Website 2026/spillover-toolkit/extracted_text")

SOURCES = [
    ("SRC-R2-01", "Active projects/2025 NE Scotland/2025 NE Scotland reporting/260420_Pinning_stones_convergence_economy_FINAL.docx", "docx"),
    ("SRC-R2-02", "Active projects/2025 NE Scotland/2025 NE Scotland reporting/260508 NES_Creative_Industries_Report.docx", "docx"),
    ("SRC-R2-03", "Archive projects/2024 Projects/2024 Man Met From Good to Great/2024 FGTG Phase 2/241106 FG2G Update.docx", "docx"),
    ("SRC-R2-04", "Archive projects/2025 Projects/2025 MITIH Createch ecosystem/2025 MITIH Reporting/251024 MITIH Createch Ecosystem Report.docx", "docx"),
    ("SRC-R2-05", "Archive projects/2017 Projects/2017 GBSLEP creative economy mapping/171212 GBSLEP Creative Economy report.docx", "docx"),
    # SRC-R2-06 CORRECTED: original was "190730 final.docx" (client quotation response, NOT the report).
    # WMCA is BOP Consulting prime, Fifth Sector subcontractor (confirmed by Iain).
    # Canonical final report PDF UNRESOLVED (three candidates: Dec 4, Dec 13 2019, Jan 9 2020).
    # Using Jan 9, 2020 PDF (latest) as proposed canonical pending Iain confirmation.
    ("SRC-R2-06", "Archive projects/2020 Projects/2020 WMCA Creative Scaleup/200109 WMCA Creative Business scale-up final report.pdf", "pdf"),
    ("SRC-R2-07", "Archive projects/2022 Projects/2022 CoSTAR/CoSTAR bid material/230125 CoSTAR Case ad Delivery.docx", "docx"),
    ("SRC-R2-08", "Archive projects/2020 Projects/2020 Creative City/Creative City project inception/200914 Creative City project inception.docx", "docx"),
    # SRC-R2-09 CORRECTED: original was the proposal only. Iain confirmed "use both".
    # The proposal remains as a source (testing proposal vs delivery).
    # The final report is added as SRC-R2-09B.
    ("SRC-R2-09", "Archive projects/2024 Projects/2024 Liverpool DCI/2024 LCR Cluster Mapping Proposal/240105 LCR DCI Cluster mapping_TheFifthSector.docx", "docx"),
    ("SRC-R2-09B", "Archive projects/2024 Projects/2024 Liverpool DCI/LCR DCI reporting/LiverpoolCityRegion_DigitalCreative_final.docx", "docx"),
    ("SRC-R2-10", "Archive projects/2012 Projects/2012 Creative Digital Economy Catapult/CDEC challenges paper V2 - draft_IB.docx", "docx"),
    # SRC-R2-11 CORRECTED: original was Jul 18, 2024 version (528 paras, 18 tables).
    # Canonical is Sep 23, 2024 "final" (544 paras, 19 tables) — later, with more content.
    # P10-KIRK is a special case: three reports (2022, 2024, 2026) as method evolution case study.
    ("SRC-R2-11", "Archive projects/2021 Projects/2021 Kirklees CI mapping/Reporting/240718 Kirklees Creative Economy 2024 final.docx", "docx"),
    ("SRC-R2-12", "Archive proposals/2026 Proposals lost/2026 LCR Film Impact/LCR Screen Sector Research Invitation to Quote.pdf", "pdf"),
    ("SRC-R2-13", "Active proposals/2026 British Council Art and Tech/UK_1412RFPdocument.pdf", "pdf"),
    ("SRC-R2-14", "Active proposals/2026 British Council Art and Tech/UK_1412 - Clarifications 03.09.26.xlsx", "xlsx"),
    ("SRC-R2-15", "Active proposals/2026 British Council Art and Tech/UK_1412-Annex1-Agreement.docx", "docx"),
]

def extract_docx(path):
    from docx import Document
    doc = Document(path)
    lines = []
    warnings = []
    # Paragraphs
    for p in doc.paragraphs:
        lines.append(p.text)
    # Tables
    for i, table in enumerate(doc.tables):
        lines.append(f"\n[TABLE {i+1}]")
        for row in table.rows:
            cells = [cell.text for cell in row.cells]
            lines.append(" | ".join(cells))
        lines.append(f"[END TABLE {i+1}]\n")
    # Footnotes/headers/footers not captured by python-docx
    if doc.tables:
        warnings.append(f"Extracted {len(doc.tables)} table(s). Headers/footers/footnotes/images not captured.")
    else:
        warnings.append("No tables found. Headers/footers/footnotes/images not captured.")
    return "\n".join(lines), warnings

def extract_pdf(path):
    from PyPDF2 import PdfReader
    reader = PdfReader(path)
    lines = []
    warnings = []
    for i, page in enumerate(reader.pages):
        lines.append(f"\n[PAGE {i+1}]")
        text = page.extract_text() or ""
        lines.append(text)
    warnings.append(f"Extracted {len(reader.pages)} page(s). Images/tables/form-fields not captured.")
    return "\n".join(lines), warnings

def extract_xlsx(path):
    from openpyxl import load_workbook
    wb = load_workbook(path, data_only=True)
    lines = []
    warnings = []
    for ws in wb.worksheets:
        lines.append(f"\n[SHEET: {ws.title}]")
        row_count = 0
        for row in ws.iter_rows(values_only=True):
            cells = [str(c) if c is not None else "" for c in row]
            lines.append(" | ".join(cells))
            row_count += 1
        lines.append(f"[END SHEET: {ws.title}, {row_count} rows]\n")
    warnings.append(f"Extracted {len(wb.worksheets)} sheet(s) with data_only=True (cached values). Formulas/hidden sheets/formatting not captured.")
    return "\n".join(lines), warnings

log = []
for src_id, rel_path, ftype in SOURCES:
    full_path = os.path.join(DRIVE, rel_path)
    if ftype == "xlsx":
        out_file = os.path.join(OUT, f"{src_id}_v1_full_sheets.csv")
    else:
        out_file = os.path.join(OUT, f"{src_id}_v1_full.txt")

    if os.path.exists(out_file):
        log.append(f"{src_id}: SKIP (output already exists: {os.path.basename(out_file)})")
        continue

    if not os.path.exists(full_path):
        log.append(f"{src_id}: ERROR (source not found: {rel_path})")
        continue

    try:
        if ftype == "docx":
            text, warnings = extract_docx(full_path)
        elif ftype == "pdf":
            text, warnings = extract_pdf(full_path)
        elif ftype == "xlsx":
            text, warnings = extract_xlsx(full_path)
        else:
            log.append(f"{src_id}: ERROR (unknown type {ftype})")
            continue

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(text)

        line_count = text.count("\n") + 1
        char_count = len(text)
        log.append(f"{src_id}: OK -> {os.path.basename(out_file)} ({line_count} lines, {char_count} chars)")
        for w in warnings:
            log.append(f"  WARNING: {w}")
    except Exception as e:
        log.append(f"{src_id}: EXCEPTION ({e})")
        log.append(traceback.format_exc())

print("\n".join(log))
print(f"\nExtraction completed: {datetime.datetime.now().isoformat()}")
