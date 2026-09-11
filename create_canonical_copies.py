#!/usr/bin/env python3
"""R1.5: Create canonical/ subfolders with copies of confirmed canonical versions.
Originals remain untouched. Copies are for reference only."""
import os, shutil

DRIVE = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive"
TOOLKIT = os.path.join(DRIVE, "Website 2026/spillover-toolkit")

# Canonical versions for each project
# Format: (project_id, [(source_rel_path, description), ...])
CANONICAL = [
    ("P01-NES", [
        ("Active projects/2025 NE Scotland/2025 NE Scotland reporting/260605 Mapping_Creative_Industries_report_v3.12.docx", "Main report v3.12 (DOCX)"),
        ("Active projects/2025 NE Scotland/2025 NE Scotland reporting/260605 Mapping_Creative_Industries_report_v3.12.pdf", "Main report v3.12 (PDF)"),
        ("Active projects/2025 NE Scotland/2025 NE Scotland reporting/NES_Policy_Playbook_v3.docx", "Policy playbook v3 (DOCX)"),
        ("Active projects/2025 NE Scotland/2025 NE Scotland reporting/NES_Policy_Playbook_v3.pdf", "Policy playbook v3 (PDF)"),
        ("Active projects/2025 NE Scotland/2025 NE Scotland reporting/NorthEastScotland_CreativeIndustries_2026_FINAL.pptx", "Presentation (PPTX)"),
    ]),
    ("P02-FGTG", [
        ("Archive projects/2024 Projects/2024 Man Met From Good to Great/2024 FGTG Phase 2/241106 FG2G Update.docx", "FG2G Update (DOCX) — R2 source"),
        ("Archive projects/2024 Projects/2024 Man Met From Good to Great/2024 FGTG Phase 2/241106 FGTG Application Masterclass Phase 2 workshop final.docx", "Phase 2 workshop final (DOCX)"),
    ]),
    ("P03-MITIH", [
        ("Archive projects/2025 Projects/2025 MITIH Createch ecosystem/2025 MITIH Reporting/250331 MITIH_Createch_Ecosystem_report_TheFifth_Sector .docx", "Aug 17 revised report (DOCX)"),
        ("Archive projects/2025 Projects/2025 MITIH Createch ecosystem/2025 MITIH Reporting/251024 MITIH Createch Ecosystem Report.docx", "Oct 24 reconciliation document (DOCX) — R2 source"),
        ("Archive projects/2025 Projects/2025 MITIH Createch ecosystem/2025 MITIH Reporting/250331 MITIH POLICY PLAYBOOK.docx", "Policy playbook (DOCX)"),
    ]),
    ("P04-GBSLEP", [
        ("Archive projects/2017 Projects/2017 GBSLEP creative economy mapping/171212 GBSLEP Creative Economy report.docx", "Dec 2017 report (DOCX) — R2 source"),
        ("Archive projects/2017 Projects/2017 GBSLEP creative economy mapping/171212 GBSLEP Creative Economy report.pdf", "Dec 2017 report (PDF)"),
    ]),
    ("P05-WMCA", [
        ("Archive projects/2020 Projects/2020 WMCA Creative Scaleup/200109 WMCA Creative Business scale-up final report.pdf", "Jan 9 2020 final report (PDF) — canonical, confirmed by Iain"),
    ]),
    ("P06-COSTAR", [
        ("Archive projects/2022 Projects/2022 CoSTAR/CoSTAR bid material/230125 CoSTAR Case ad Delivery.docx", "Case ad Delivery (DOCX) — R2 source"),
        ("Archive projects/2022 Projects/2022 CoSTAR/CoSTAR bid material/CfS - The Fifth Sector Limited_signed.docx", "Case for Support signed (DOCX)"),
    ]),
    ("P07-CC", [
        ("Archive projects/2020 Projects/2020 Creative City/Creative City project inception/200914 Creative City project inception.docx", "Inception note (DOCX) — R2 source"),
        ("Archive projects/2020 Projects/2020 Creative City/200817 TheFifthSector_CreativeCity+_SIPF_proposal.pdf", "SIPF proposal (PDF)"),
    ]),
    ("P08-LIVDCI", [
        ("Archive projects/2024 Projects/2024 Liverpool DCI/2024 LCR Cluster Mapping Proposal/240105 LCR DCI Cluster mapping_TheFifthSector.docx", "Proposal (DOCX) — R2 source"),
        ("Archive projects/2024 Projects/2024 Liverpool DCI/LiverpoolCityRegion_DigitalCreative_final.docx", "Final report (DOCX) — canonical, accepted by client"),
        ("Archive projects/2024 Projects/2024 Liverpool DCI/LiverpoolCityRegion_DigitalCreative_final.pdf", "Final report (PDF)"),
    ]),
    ("P09-CDEC", [
        ("Archive projects/2012 Projects/2012 Creative Digital Economy Catapult/CDEC challenges paper V2 - draft_IB.docx", "Challenges paper V2 draft (DOCX) — R2 source"),
    ]),
    ("P10-KIRK", [
        ("Archive projects/2021 Projects/2021 Kirklees CI mapping/Reporting/2206 Kirklees Creative Economy final report.docx", "2022 final report (DOCX) — accepted"),
        ("Archive projects/2021 Projects/2021 Kirklees CI mapping/Reporting/2206 Kirklees Creative Economy final report.pdf", "2022 final report (PDF)"),
        ("Archive projects/2021 Projects/2021 Kirklees CI mapping/Reporting/240718 Kirklees Creative Economy 2024 final.docx", "2024 final report (DOCX) — accepted, canonical R2 source"),
        ("Archive projects/2021 Projects/2021 Kirklees CI mapping/Reporting/240718 Kirklees Creative Economy 2024 final.pdf", "2024 final report (PDF)"),
        ("Archive projects/Google project folders/2026/2026 Kirklees/260528 Kirklees-creative-industries-economic-impact-report-2026-FINAL.docx", "2026 final report (DOCX) — in progress"),
        ("Archive projects/Google project folders/2026/2026 Kirklees/kirklees-creative-economic-impact-report-2026.pdf", "2026 final report (PDF)"),
    ]),
]

log = []
for project_id, sources in CANONICAL:
    canon_dir = os.path.join(TOOLKIT, "canonical", project_id)
    os.makedirs(canon_dir, exist_ok=True)
    
    for src_rel, desc in sources:
        src_path = os.path.join(DRIVE, src_rel)
        fname = os.path.basename(src_path)
        dst_path = os.path.join(canon_dir, fname)
        
        if not os.path.exists(src_path):
            log.append(f"{project_id}: ERROR (source not found: {src_rel})")
            continue
        
        if os.path.exists(dst_path):
            log.append(f"{project_id}: SKIP (already exists: {fname})")
            continue
        
        try:
            shutil.copy2(src_path, dst_path)
            size_kb = os.path.getsize(dst_path) // 1024
            log.append(f"{project_id}: COPIED {fname} ({size_kb}KB) — {desc}")
        except Exception as e:
            log.append(f"{project_id}: ERROR copying {fname}: {e}")

print("\n".join(log))
print(f"\nCanonical copies completed: {len(log)} operations")
