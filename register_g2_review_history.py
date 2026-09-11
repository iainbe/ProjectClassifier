#!/usr/bin/env python3
"""Tier 2 Stage D: Review history entries for G2 post-2020 registration."""
import csv, os

CSV_PATH = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit/10_review_history.csv")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_ids = {row["review_id"] for row in reader}

print(f"Existing review IDs: {len(existing_ids)}")

entries = [
("REV-G2-003","G2-BATCH-B","PROJECT","P16-CICP","programme_status","INITIAL_CODE","Devin","2026-09-11","1.3-candidate","","","NOT_APPLICABLE","","","Evaluation approach document; not a programme","Devin","RESOLVED","",""),
("REV-G2-004","G2-BATCH-B","PROJECT","P18-GRIMSBY","contracting_role","INITIAL_CODE","Devin","2026-09-11","1.3-candidate","","","SUBCONTRACTOR","","","Iain confirmed mapping data contribution; Magna Vitae prime","Iain","RESOLVED","",""),
("REV-G2-005","G2-BATCH-B","PROJECT","P25-LANCGP","programme_status","RECODE","Devin","2026-09-11","1.3-candidate","","UNKNOWN","NOT_AWARDED","","","Iain confirmed bid unsuccessful 2026-09-11","Iain","RESOLVED","",""),
("REV-G2-006","G2-BATCH-B","PROJECT","P29-SOLENTCGP","programme_status","RECODE","Devin","2026-09-11","1.3-candidate","","UNKNOWN","NOT_AWARDED","","","Iain confirmed bid unsuccessful 2026-09-11","Iain","RESOLVED","",""),
("REV-G2-007","G2-BATCH-B","PROJECT","P30-HEREFORD","contracting_role","INITIAL_CODE","Devin","2026-09-11","1.3-candidate","","","PRIME","","","Iain confirmed lead consultant 2026-09-11","Iain","RESOLVED","",""),
("REV-G2-008","G2-BATCH-B","PROJECT","P32-SURREY","contracting_role","INITIAL_CODE","Devin","2026-09-11","1.3-candidate","","","PRIME","","","Iain confirmed lead consultant 2026-09-11","Iain","RESOLVED","",""),
("REV-G2-009","G2-BATCH-B","CLAIM","C-G2-058","notes","REVIEW_NOTE","Devin","2026-09-11","1.3-candidate","","","INTERNAL INCONSISTENCY: 120 vs 160 FTE jobs","","","Source inconsistency flagged; both figures preserved in measurements MEAS-G2-042 and MEAS-G2-043","Devin","OPEN","",""),
("REV-G2-010","G2-BATCH-B","CLAIM","C-G2-075","notes","REVIEW_NOTE","Devin","2026-09-11","1.3-candidate","","","DCMS top-down £6.9bn almost certainly overestimate; reconciled to £5.25bn","","","Source explicitly states £6.9bn is overestimate; reconciliation preserves both","Devin","RESOLVED","",""),
("REV-G2-011","G2-BATCH-B","RULE","RULE-G2-001","rule_check","RULE_CHECK","Devin","2026-09-11","1.3-candidate","","","PASS","","","All 54 new claims have claim_type assigned; no context mislabelled as effect","Devin","RESOLVED","",""),
("REV-G2-012","G2-BATCH-B","RULE","RULE-G2-002","rule_check","RULE_CHECK","Devin","2026-09-11","1.3-candidate","","","PASS","","","All modelled GVA tagged DESCRIPTIVE_ESTIMATE not OBSERVED_AMOUNT; no forecast labelled as realised","Devin","RESOLVED","",""),
("REV-G2-013","G2-BATCH-B","RULE","RULE-G2-003","rule_check","RULE_CHECK","Devin","2026-09-11","1.3-candidate","","","PASS","","","All bid-support DESIGN claims tagged with programme_status; Lancashire and Solent correctly NOT_AWARDED","Devin","RESOLVED","",""),
("REV-G2-014","G2-BATCH-B","RULE","RULE-G2-004","rule_check","RULE_CHECK","Devin","2026-09-11","1.3-candidate","","","PASS","","","All 54 claims have method_ids linking to registered methods; all 68 measurements link to claims","Devin","RESOLVED","",""),
("REV-G2-015","G2-BATCH-B","RULE","RULE-G2-005","rule_check","RULE_CHECK","Devin","2026-09-11","1.3-candidate","","","PASS","","","All 54 evidence links have valid claim_id and source_id foreign keys","Devin","RESOLVED","",""),
("REV-G2-016","G2-BATCH-B","RULE","RULE-G2-006","rule_check","RULE_CHECK","Devin","2026-09-11","1.3-candidate","","","PASS","","","No monetary values labelled NON_MONETARY; no costs labelled benefits","Devin","RESOLVED","",""),
("REV-G2-017","G2-BATCH-B","REVIEW","G2-BATCH-B","lens_A","REVIEW_NOTE","Devin","2026-09-11","1.3-candidate","","","Lens A (review pass) applied to all 54 claims","","","Claim wording checked for specificity testability and boundedness; modelled estimates distinguished from observed amounts; forecasts distinguished from realised outcomes","Devin","RESOLVED","",""),
("REV-G2-018","G2-BATCH-B","REVIEW","G2-BATCH-B","lens_B","REVIEW_NOTE","Devin","2026-09-11","1.3-candidate","","","Lens B (evidence analysis) applied to high-risk claims","","","Testimony provenance checked for Wakefield CoSTAR attribution; causal assumptions documented for employment/GVA growth claims; boundary/distribution checked for cross-sector spillover claims","Devin","RESOLVED","",""),
]

new_rows = []
for e in entries:
    rid = e[0]
    if rid in existing_ids:
        print(f"SKIP {rid}")
        continue
    row = {h: e[i] if i < len(e) else "" for i, h in enumerate(header)}
    new_rows.append(row)
    print(f"ADD  {rid}")

if new_rows:
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        for row in new_rows:
            clean = {k: v for k, v in row.items() if k is not None}
            writer.writerow(clean)
    print(f"\nAppended {len(new_rows)} review history entries")
print("Stage D complete.")
