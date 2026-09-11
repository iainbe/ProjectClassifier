#!/usr/bin/env python3
"""Extract text from G2 Phase 1 post-2020 cohort sources (20 projects, 80% effort)."""
import os
from docx import Document

DRIVE = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive")
OUT = os.path.join(DRIVE, "Website 2026/spillover-toolkit/extracted_text")

sources = [
    # 6. CICP (2020) - approach doc only; no final evaluation report in folder
    ("SRC-G2-011", "Archive projects/Google project folders/2020/UKRI AHRC - Creative Industries Clusters Progr - (2020-2024)/ProJ 1.1- approach-final.docx", "docx"),
    # 7. Leeds City Region Creative Scale Up (2020)
    ("SRC-G2-012", "Archive projects/2020 Projects/2020 Leeds City Region Creative Scale Up/200730 Leeds CIty Region Creative Scale Up v2.0.docx", "docx"),
    # 9. Grimsby CCI (2020) - Phase 1 Report FINAL
    ("SRC-G2-013", "Archive projects/2020 Projects/2020 Grimsby CCI/NELC Phase 1 Report FINAL.pdf", "pdf"),
    # 10. LCR Immersive (2019) - final report May 2020
    ("SRC-G2-014", "Archive projects/2019 Projects/2019 LCR Growth Company Immersive tech/Reporting/Liverpool City Region Immersive Sector final report May 2020.pdf", "pdf"),
    # 11. SYMCA CCI (2021) - main report
    ("SRC-G2-015", "Archive projects/2021 Projects/2021 SYMCA CCI research/200608 SYMCA Cultural and Creative Industries 1.1.docx", "docx"),
    # 12. MMU CCI (2021) - report v2
    ("SRC-G2-016", "Archive projects/2021 Projects/2021 MMU CCI/Reporting/221014 Man Met CCI report v2.docx", "docx"),
    # 13. LCR Film & TV Production Fund (2020-21) - interim evaluation
    ("SRC-G2-017", "Archive projects/2020 Projects/2020 Liverpool Film Fund evaluation/Reporting/210204 Liverpool Production Fund Interim Evaluation draft report.docx", "docx"),
    # 14. Derby Screen Agency (2022) - feasibility study
    ("SRC-G2-018", "Archive projects/2022 Projects/2022 Derby Screen Agency/220809 Derby(s) Film Office feasibility study.pdf", "pdf"),
    # 15. SYMCA Create Growth (2022) - final report
    ("SRC-G2-019", "Archive projects/2022 Projects/2022 SYMCA Create Growth/2022 SYMCA CGP Reporting/SYMCA Cultural and Creative Industries final report.docx", "docx"),
    # 16. Lancashire Create Growth (2022) - FINAL
    ("SRC-G2-020", "Archive projects/2022 Projects/2022 Lancashire Create Growth/Lancashire Create Growth Programme FINAL.pdf", "pdf"),
    # 17. West Sussex Brighton (2022) - v2
    ("SRC-G2-021", "Archive projects/2022 Projects/2022 West Sussex Brighton Hove Lewes/2022 West Sussex Reporting/230421 West Sussex Brighton Hove Lewes CI v2.docx", "docx"),
    # 18. Wakefield CDF (2022-25) - FINAL evaluation
    ("SRC-G2-022", "Archive projects/2025 Projects/2022 Wakefield CDF - Local Programme Evaluation/2024 CDF2 Reporting/250929 CDF Evaluation FINAL.docx", "docx"),
    # 19. Calderdale (2023) - final report
    ("SRC-G2-023", "Archive projects/2023 Projects/2023 Calderdale/2023 Calderdale reporting/231219 Calderdale CCI report final.docx", "docx"),
    # 20. Solent CGP (2023) - bid development full application
    ("SRC-G2-024", "Archive projects/2023 Projects/2023 Solent CGP/2023 Solent CGP Proposal/CGP Expansion FullApplication Form_Solent_DRAFT.docx", "docx"),
    # 21. Herefordshire (2024) - Culture Strategy Review latest
    ("SRC-G2-025", "Archive projects/2024 Projects/2024 Herefordshire/2024 Herefordshire reporting/260617 Herefordshire Culture Strategy Review.docx", "docx"),
    # 22. Production Park GVA (2024) - GVA data doc
    ("SRC-G2-026", "Archive projects/2024 Projects/2024 Production Park GVA/240719 Production Park GVA data.docx", "docx"),
    # 23. Surrey+ Corridor (2024) - latest draft
    ("SRC-G2-027", "Archive projects/2024 Projects/2024 Surrey+ Corridor/2025 Surrey+ Reporting/250818 Human Rewrite IB CLEAN.docx", "docx"),
    # 24. LCR Music (2025) - final report
    ("SRC-G2-028", "Archive projects/2025 Projects/2025 Liverpool Music/2025 Liverpool Music reporting/260222 LCR_Music_Economy_Final_Report.docx", "docx"),
    # 25. Solent Hampshire (2025) - CI Mapping
    ("SRC-G2-029", "Archive projects/2025 Projects/2025 Solent and Hampshire CI/2025 Solent and Hants Reporting/250718 Solent and Hampshire CA CI Mapping.docx", "docx"),
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
        if ftype == "docx":
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

            print(f"OK {source_id}: {para_count} paras, {table_count} tables, {len(content)} chars")
        elif ftype == "pdf":
            from PyPDF2 import PdfReader
            reader = PdfReader(full_path)
            lines = []
            for i, page in enumerate(reader.pages):
                lines.append(f"\n[PAGE {i+1}]")
                text = page.extract_text()
                if text:
                    lines.append(text)
            content = "\n".join(lines)
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"OK {source_id}: {len(reader.pages)} pages, {len(content)} chars")

        print(f"  -> {out_file}")

    except Exception as e:
        print(f"ERROR {source_id}: {e}")
        import traceback
        traceback.print_exc()
