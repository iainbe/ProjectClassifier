#!/usr/bin/env python3
"""Tier 2 Stage A: Measurements batch 1 (P16-P22) in 06_measurements.csv.
Also records evidence quality assessment in notes."""
import csv, os

CSV_PATH = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit/06_measurements.csv")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_ids = {row["measurement_id"] for row in reader}

print(f"Existing measurement IDs: {len(existing_ids)}")

# Evidence quality assessment:
# P16-CICP: THIN (approach document only, marginal claim)
# P17-LCRCSU: MODERATE (bid evidence base, BRES/ONS data)
# P18-GRIMSBY: THIN (participation baselines only, no economic data, data contributor)
# P19-LCRIMM: MODERATE (169 orgs mapped, survey n=56, case studies)
# P20-SYMCA21: MODERATE (4000+ companies, multi-source, but baseline only)
# P21-MMUCCI: THIN (interview-based, no quantitative baselines)
# P22-LCRFILM: RICH (documented output data, leverage, FTE, pipeline)

measurements = [
# P16-CICP — no numeric claims to measure (approach document only)

# P17-LCRCSU
("MEAS-G2-001","C-G2-025","LCR creative industries employment","58840","","workers","Leeds City Region creative economy","44420 (2015)","Leeds City Region","2018","National average growth lower","BRES time series 2015-2018","BRES employment analysis via Nomisweb","v1","BRES excludes freelancers below VAT threshold","","LCRCSU employment baseline","SRC-G2-012","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","BRES official data; excludes freelancers","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-002","C-G2-025","LCR CI employment growth","14420","","jobs","Leeds City Region creative economy","44420 (2015)","Leeds City Region","2015-2018","","Net increase 2015-2018","BRES year-over-year comparison","v1","32% growth rate","","LCRCSU employment growth","SRC-G2-012","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P18-GRIMSBY
("MEAS-G2-003","C-G2-027","Grimsby arts participation rate","27.3","","percent","Grimsby residents","34.6 (national)","Grimsby","2017","National average 34.6%","Active Lives Survey","Arts participation from Active Lives Survey","v1","National survey sub-sample for Grimsby","","Grimsby participation baseline","SRC-G2-013","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","percent","Sub-sample for local area","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P19-LCRIMM
("MEAS-G2-004","C-G2-028","LCR immersive organisations","169","","organisations","LCR immersive ecosystem","","Liverpool City Region","2020","","AI web search + LinkedIn mapping","AI-powered web search company database","v1","SIC/SOC codes cannot capture immersive sector","","LCRIMM ecosystem size","SRC-G2-014","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","AI web search estimate; survey self-selecting","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-005","C-G2-028","LCR immersive companies","126","","companies","LCR immersive companies","","Liverpool City Region","2020","","Of which 114 LCR-based","AI web search company database","v1","","","LCRIMM company count","SRC-G2-014","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P20-SYMCA21
("MEAS-G2-006","C-G2-032","SYMCA CI company count (LinkedIn/Beauhurst)","4000","","companies","South Yorkshire creative economy","2895 (IDBR official)","South Yorkshire","2022","Official IDBR 2895","Companies House cleansed + Beauhurst","Companies House cleansed + Beauhurst","v1","LinkedIn not comparable to BRES; BRES undercounts freelancers","","SYMCA21 company baseline","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","Companies House cleansed 4025 businesses","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-007","C-G2-032","SYMCA CI workforce (LinkedIn)","31000","","workers","South Yorkshire creative economy","13500 (BRES official)","South Yorkshire","2022","Official BRES 13500","LinkedIn workforce profiling","LinkedIn via Curator Technologies","v1","LinkedIn captures freelancers missed by BRES; 60% freelance estimated","","SYMCA21 workforce baseline","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","LinkedIn overcounts vs BRES","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-008","C-G2-033","SYMCA full accounts filers","4.8","","percent","South Yorkshire creative companies","","South Yorkshire","2022","","Companies House analysis","Companies House filing analysis","v1","","","SYMCA21 creative growth paradox","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","percent","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-009","C-G2-033","SYMCA R&D grant recipients","101","","companies","South Yorkshire creative companies","","South Yorkshire","2022","","Beauhurst R&D grant tracking","Beauhurst analysis","v1","<2% of total","","SYMCA21 R&D access","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-010","C-G2-033","SYMCA equity investments","36","","investments","South Yorkshire creative companies","","South Yorkshire","2022","","Beauhurst equity tracking","Beauhurst analysis","v1","","","SYMCA21 equity investment","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-011","C-G2-033","SYMCA spinouts","8","","spinouts","South Yorkshire creative companies","","South Yorkshire","2022","","Beauhurst spinout tracking","Beauhurst analysis","v1","","","SYMCA21 spinouts","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-012","C-G2-033","SYMCA scale-ups","6","","scale-ups","South Yorkshire creative companies","","South Yorkshire","2022","","Beauhurst scale-up tracking","Beauhurst analysis","v1","","","SYMCA21 scale-ups","SRC-G2-015","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P21-MMUCCI — no numeric claims (qualitative audit only)

# P22-LCRFILM
("MEAS-G2-013","C-G2-037","LCR Film Fund leverage ratio","6.76","","GBP per GBP","LCR Film Fund investments","","Liverpool City Region","2021","Target 3:1 film 5:1 TV","LFO management data","LFO financial records","v1","COVID shut filming Mar-Jul 2020","","LCRFILM leverage","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","Documented from LFO data","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-014","C-G2-037","LCR Film Fund LCR spend","12080000","","GBP","LCR Film Fund investments","","Liverpool City Region","2021","","LFO management data","LFO financial records","v1","","","LCRFILM total spend","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-015","C-G2-037","LCR Film Fund capital invested","1788000","","GBP","LCR Film Fund capital","","Liverpool City Region","2021","","LFO management data","LFO financial records","v1","Of £2m capital budget","","LCRFILM capital deployed","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-016","C-G2-038","LCR Film Fund indirect FTE jobs","455","","FTE","LCR film/TV productions","","Liverpool City Region","2021","Target 280 FTE","LFO monitoring data","LFO job tracking","v1","COVID distorted investment profile","","LCRFILM indirect FTE","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","FTE","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-017","C-G2-038","LCR Film Fund cost per FTE","3930","","GBP per FTE","LCR Film Fund","","Liverpool City Region","2021","Business case estimate £6900","LFO financial data / FTE count","Cost per FTE calculation","v1","Below business case estimate","","LCRFILM cost per FTE","SRC-G2-017","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","BENEFIT","GBP per FTE","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-018","C-G2-039","Development Fund deployed","173604","","GBP","LCR Development Fund","","Liverpool City Region","2021","Target £250000","LFO management data","LFO financial records","v1","","","LCRFILM Development Fund","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-019","C-G2-039","Development Fund companies supported","17","","companies","LCR Development Fund","","Liverpool City Region","2021","Target 12","LFO monitoring data","LFO company tracking","v1","","","LCRFILM Dev Fund companies","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-020","C-G2-039","Development Fund jobs supported","43","","jobs","LCR Development Fund","","Liverpool City Region","2021","Target 30","LFO monitoring data","LFO job tracking","v1","","","LCRFILM Dev Fund jobs","SRC-G2-017","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
]

new_rows = []
for m in measurements:
    mid = m[0]
    if mid in existing_ids:
        print(f"SKIP {mid}")
        continue
    row = {h: m[i] if i < len(m) else "" for i, h in enumerate(header)}
    new_rows.append(row)
    print(f"ADD  {mid}: {m[2]}")

if new_rows:
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        for row in new_rows:
            writer.writerow(row)
    print(f"\nAppended {len(new_rows)} measurements (batch 1)")
print("Stage A complete.")
