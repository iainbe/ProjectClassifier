#!/usr/bin/env python3
"""Tier 2 Stage B: Measurements batch 2 (P23-P34) in 06_measurements.csv."""
import csv, os

CSV_PATH = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit/06_measurements.csv")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_ids = {row["measurement_id"] for row in reader}

print(f"Existing measurement IDs: {len(existing_ids)}")

# Evidence quality assessment:
# P23-DERBY: THIN (survey n=17, no local baseline, design proposition)
# P24-SYMCACGP: MODERATE (4025 companies, GVA modelled, extends P20)
# P25-LANCGP: MODERATE (4500 businesses, bid application not outcome)
# P26-WSBH: MODERATE (10225 companies, multi-source, 3-phase plan)
# P27-WAKECDF: RICH (£22.03m total, +32% employment, +79% GVA, 458% network, 10 new products, CoSTAR)
# P28-CALDER: MODERATE (655 ONS firms, 7375 LinkedIn, music deep dive)
# P29-SOLENTCGP: MODERATE (4510 businesses, draft application)
# P30-HEREFORD: MODERATE (590 businesses, 4000+ LinkedIn, rural context)
# P31-PRODPARK: THIN (data fragment, incomplete)
# P32-SURREY: MODERATE (£7.2bn, 17000 companies, 115000 workforce)
# P33-LCRMUS: RICH (£405.9m GVA, SNA, four-tier model, 38 tables)
# P34-SOLENTHANTS: MODERATE (£5.25bn GVA reconciled, HDBSCAN, 11 tables)

measurements = [
# P23-DERBY — no numeric claims (feasibility design proposition only)

# P24-SYMCACGP
("MEAS-G2-021","C-G2-043","SYMCA CCI GVA (upper estimate)","2000000000","","GBP","South Yorkshire creative economy","","South Yorkshire","2022","ONS national average would exceed £1bn","DCMS GVA + ONS productivity index","DCMS GVA estimation with ONS regional productivity","v1","Generic ONS productivity index; BRES pre-pandemic","","SYMCACGP GVA upper","SRC-G2-019","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","Modelled estimate using generic productivity index","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-022","C-G2-044","SYMCA CCI multiplier","2.46","","FTE per FTE","South Yorkshire arts/culture","","South Yorkshire","2022","","DCMS modelling","DCMS total footprint multiplier","v1","Contextual not intervention effect","","SYMCACGP multiplier","SRC-G2-019","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","FTE per FTE","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-023","C-G2-045","SYMCA creative courses","1013","","courses","South Yorkshire and wider TTVA","","South Yorkshire","2022","","Course/qualification audit","Course mapping across providers","v1","","","SYMCACGP courses","SRC-G2-019","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-024","C-G2-045","SYMCA creative apprenticeships","5","","apprenticeships","South Yorkshire","","South Yorkshire","2022","","Course/qualification audit","Apprenticeship mapping","v1","","","SYMCACGP apprenticeships","SRC-G2-019","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P25-LANCGP
("MEAS-G2-025","C-G2-047","Lancashire CI businesses","4500","","businesses","Lancashire creative economy","","Lancashire","2022","","IDBR + Beauhurst","IDBR April 2021 + Beauhurst","v1","","","LANCGP business count","SRC-G2-020","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-026","C-G2-047","Lancashire CI jobs","36000","","jobs","Lancashire creative economy","","Lancashire","2022","6% of workforce","IDBR + Beauhurst","IDBR + Beauhurst analysis","v1","","","LANCGP job count","SRC-G2-020","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P26-WSBH
("MEAS-G2-027","C-G2-049","WSBH CI companies (Beauhurst)","10225","","companies","WSBH area creative economy","7470 (official IDBR)","West Sussex/Brighton/Hove/Lewes","2023","Official IDBR 7470","Beauhurst + LinkedIn","Beauhurst active businesses + LinkedIn","v1","Beauhurst 38.6% greater than official","","WSBH company count","SRC-G2-021","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-028","C-G2-049","WSBH CI workforce (LinkedIn)","54428","","workers","WSBH area creative economy","23690 (BRES official)","West Sussex/Brighton/Hove/Lewes","2023","Official BRES 23690","LinkedIn workforce profiling","LinkedIn via Curator Technologies","v1","LinkedIn not comparable to BRES; 21000 freelance (38.9%)","","WSBH workforce","SRC-G2-021","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P27-WAKECDF
("MEAS-G2-029","C-G2-052","Wakefield CDF total value","22030000","","GBP","CDF programme total","","Wakefield","2025","","Financial records","Council financial records","v1","Construction overruns required additional £2.1m Council funding","","WAKECDF total value","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-030","C-G2-052","Wakefield CDF grant","4380000","","GBP","CDF grant from DCMS","","Wakefield","2025","","Financial records","Council financial records","v1","","","WAKECDF grant","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-031","C-G2-052","Wakefield CDF private leveraged","6060000","","GBP","Private/partner capital leveraged","","Wakefield","2025","","Financial records","Council financial records","v1","","","WAKECDF private leverage","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-032","C-G2-053","Wakefield CCI employment growth","32","","percent","Wakefield CCI","2210 (2020)","Wakefield","2020-2023","","ONS BRES","BRES 2020 vs 2023","v1","Modelled not causal; ONS business count fell slightly","","WAKECDF employment growth","SRC-G2-022","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","percent","Report uses correlates with language","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-033","C-G2-053","Wakefield CCI employment (2023)","2910","","workers","Wakefield CCI","2210 (2020)","Wakefield","2023","","ONS BRES","BRES 2023","v1","","","WAKECDF employment 2023","SRC-G2-022","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-034","C-G2-053","Wakefield CCI GVA growth","79","","percent","Wakefield CCI","52.8 (2020)","Wakefield","2020-2023","","DCMS GVA estimation","DCMS GVA estimates","v1","Modelled not causal","","WAKECDF GVA growth","SRC-G2-022","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","percent","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-035","C-G2-053","Wakefield CCI GVA (2023)","94200000","","GBP","Wakefield CCI","52800000 (2020)","Wakefield","2023","","DCMS GVA estimation","DCMS GVA estimates","v1","","","WAKECDF GVA 2023","SRC-G2-022","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-036","C-G2-054","Creative Wakefield network growth","458","","percent","Creative Wakefield members","150 (Apr 2020)","Wakefield","2020-2024","","Membership data","Creative Wakefield membership records","v1","","","WAKECDF network growth","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","percent","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-037","C-G2-054","Creative Wakefield members (2024)","837","","members","Creative Wakefield network","150 (Apr 2020)","Wakefield","2024","","Membership data","Creative Wakefield membership records","v1","","","WAKECDF network size","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-038","C-G2-055","XPLOR new-to-market products","10","","products","XPLOR enterprises","","Wakefield","2025","","Programme monitoring data","XPLOR monitoring records","v1","Specific companies listed in Table 13","","WAKECDF new products","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-039","C-G2-055","XPLOR new-to-firm products","20","","products","XPLOR enterprises","","Wakefield","2025","","Programme monitoring data","XPLOR monitoring records","v1","","","WAKECDF new-to-firm","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-040","C-G2-057","Creative Leadership participants","15","","participants","Creative Leadership programme","","Wakefield","2025","","Programme monitoring","Programme records","v1","From 11 sub-sectors","","WAKECDF leadership","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-041","C-G2-057","Creative Leadership collaborations","12","","collaborations","Creative Leadership programme","","Wakefield","2025","","Programme monitoring","Programme records","v1","Cross-sector collaborations","","WAKECDF collaborations","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-042","C-G2-058","Wakefield jobs (exec summary)","120","","FTE","CDF programme","","Wakefield","2025","Main body says 160","Executive summary Table 1","Executive summary","v1","INTERNAL INCONSISTENCY with 160 FTE in main body","","WAKECDF jobs (exec summary)","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","FTE","Source inconsistency: 120 vs 160 FTE","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-043","C-G2-058","Wakefield jobs (main body)","160","","FTE","CDF programme","","Wakefield","2025","Exec summary says 120","Main body Table 14","Main body Table 14","v1","INTERNAL INCONSISTENCY with 120 FTE in exec summary","","WAKECDF jobs (main body)","SRC-G2-022","OBSERVED_AMOUNT","NOT_REVIEWED","BENEFIT","FTE","Source inconsistency: 120 vs 160 FTE","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P28-CALDER
("MEAS-G2-044","C-G2-059","Calderdale ONS firms","655","","firms","Calderdale CCI","","Calderdale","2023","","ONS/IDBR","ONS IDBR 2015-2023","v1","","","CALDER ONS firms","SRC-G2-023","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-045","C-G2-059","Calderdale BRES employment","2360","","workers","Calderdale CCI","","Calderdale","2023","","BRES 2022","BRES 2022","v1","","","CALDER BRES employment","SRC-G2-023","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-046","C-G2-059","Calderdale LinkedIn workforce","7375","","workers","Calderdale CCI","","Calderdale","2023","","LinkedIn July 2023","LinkedIn via Curator Technologies","v1","LinkedIn not comparable to BRES; 83% report employment status","","CALDER LinkedIn workforce","SRC-G2-023","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P29-SOLENTCGP
("MEAS-G2-047","C-G2-062","Solent CI businesses","4510","","businesses","Solent creative economy","42000 (total all sectors)","Solent","2023","10.7% of total","Beauhurst","Beauhurst Sept 2023","v1","Beauhurst 33% higher than IDBR","","SOLENTCGP business count","SRC-G2-024","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-048","C-G2-062","Solent CI jobs","40000","","jobs","Solent creative economy","","Solent","2023","","Lightcast","Lightcast employment data","v1","Freelance not accurately measured","","SOLENTCGP job count","SRC-G2-024","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-049","C-G2-062","Solent CI GVA","1500000000","","GBP","Solent creative economy","","Solent","2023","","Lightcast + Oxford Economics","Lightcast GVA estimation","v1","","","SOLENTCGP GVA","SRC-G2-024","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P30-HEREFORD
("MEAS-G2-050","C-G2-064","Herefordshire official creative businesses","590","","businesses","Herefordshire creative economy","","Herefordshire","2024","","ONS/DCMS","ONS/DCMS official data","v1","Limited data collection obscures true sector size","","HEREFORD business count","SRC-G2-025","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-051","C-G2-064","Herefordshire LinkedIn professionals","4000","","professionals","Herefordshire creative economy","","Herefordshire","2024","3x larger than official","LinkedIn","LinkedIn workforce profiling","v1","","","HEREFORD LinkedIn","SRC-G2-025","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P31-PRODPARK — no reliable numeric claims (BRES columns empty)

# P32-SURREY
("MEAS-G2-052","C-G2-067","Surrey+ creative corridor value","7200000000","","GBP","Surrey+ creative corridor","","Surrey+ corridor","2024","","Mapping evidence","Mapping evidence (sources not shown in text)","v1","Underlying data sources not shown in text","","SURREY corridor value","SRC-G2-027","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-053","C-G2-067","Surrey+ companies","17000","","companies","Surrey+ creative corridor","","Surrey+ corridor","2024","","Mapping evidence","Mapping evidence","v1","90% micro-businesses <5 employees","","SURREY company count","SRC-G2-027","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-054","C-G2-067","Surrey+ workforce","115000","","workers","Surrey+ creative corridor","","Surrey+ corridor","2024","12% growth since 2019 vs UK 2%","Mapping evidence","Mapping evidence","v1","43% freelance","","SURREY workforce","SRC-G2-027","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P33-LCRMUS
("MEAS-G2-055","C-G2-070","LCR Music direct GVA (Integrated)","405900000","","GBP","LCR music economy","","Liverpool City Region","2025","","Four-tier workforce model + GVA attribution","Four-tier workforce model + GVA per FTE by subsector","v1","Tier 4 data quality low (50% confidence); LinkedIn coverage ~45%","","LCRMUS direct GVA","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","Modelled estimate; GVA per FTE ranges £25174 to £145798","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-056","C-G2-070","LCR Music total economic impact","779800000","","GBP","LCR music economy total","","Liverpool City Region","2025","","Type II multiplier 1.92 applied to direct GVA","Four-tier workforce model + Type II multiplier","v1","Multiplier assumptions apply","","LCRMUS total impact","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-057","C-G2-070","LCR Music headcount","14370","","workers","LCR music economy","","Liverpool City Region","2025","","Four-tier workforce model","Four-tier workforce model","v1","","","LCRMUS headcount","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-058","C-G2-070","LCR Music FTE","7215","","FTE","LCR music economy","","Liverpool City Region","2025","","Four-tier workforce model","Four-tier workforce model","v1","","","LCRMUS FTE","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","FTE","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-059","C-G2-072","LCR Music SNA businesses","272","","businesses","LCR music businesses","","Liverpool City Region","2025","","Social network analysis","SNA of LinkedIn workforce movement","v1","Low connectivity limits spillover claims","","LCRMUS SNA sample","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-060","C-G2-072","LCR Music SNA closed triangles","12","","percent","LCR music business connections","","Liverpool City Region","2025","","SNA","SNA triangle analysis","v1","Only 0.6% of possible connections exist","","LCRMUS SNA triangles","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","percent","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-061","C-G2-072","LCR Music SNA average degree","1.67","","connections per business","LCR music businesses","","Liverpool City Region","2025","","SNA","SNA degree analysis","v1","","","LCRMUS SNA degree","SRC-G2-028","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","connections per business","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-062","C-G2-073","LCR Music £1bn target","1000000000","","GBP","LCR music economy target","779800000 (2025 baseline)","Liverpool City Region","2035","2.5% CAGR required","Growth scenario modelling","Four growth scenarios (Organic to Transformational)","v1","Modelled targets not realised outcomes","","LCRMUS growth target","SRC-G2-028","SCENARIO_ESTIMATE","NOT_REVIEWED","BENEFIT","GBP nominal","4 growth levers: IP capture £100m production export £75m formalisation £60m venues £50m music-tech £43m","Devin","2026-09-11","LCR Music Board","Growth strategy implementation","No expiry specified","","","","No demand validation","No probability basis","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-063","C-G2-074","LCR Music IP capture shift","40000000","","GBP lower bound","LCR artists moving to IP ownership","","Liverpool City Region","UNKNOWN","","Scenario modelling","20% artist shift scenario","v1","Modelled design proposition","","LCRMUS IP capture (lower)","SRC-G2-028","SCENARIO_ESTIMATE","NOT_REVIEWED","BENEFIT","GBP nominal","IP capture leaks to London; streaming revenue decline","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-064","C-G2-074","LCR Music IP capture shift (upper)","85000000","","GBP upper bound","LCR artists moving to IP ownership","","Liverpool City Region","UNKNOWN","","Scenario modelling","20% artist shift scenario","v1","Modelled design proposition","","LCRMUS IP capture (upper)","SRC-G2-028","SCENARIO_ESTIMATE","NOT_REVIEWED","BENEFIT","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),

# P34-SOLENTHANTS
("MEAS-G2-065","C-G2-075","Solent/Hampshire CI GVA (reconciled)","5250000000","","GBP","SHCA creative economy","6900000000 (DCMS top-down)","Solent and Hampshire","2025","DCMS £6.9bn almost certainly overestimate","ONS regional output + DCMS reconciliation","ONS regional output £3.4bn + DCMS scaled reconciliation","v1","DCMS top-down overestimate; 31% IT contraction","","SOLENTHANTS GVA reconciled","SRC-G2-029","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","GBP nominal","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-066","C-G2-075","Solent/Hampshire BRES employees","39980","","workers","SHCA creative economy","","Solent and Hampshire","2025","","BRES 2023","BRES 2023","v1","","","SOLENTHANTS BRES","SRC-G2-029","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-067","C-G2-075","Solent/Hampshire LinkedIn workforce","80511","","workers","SHCA creative economy","","Solent and Hampshire","2025","","LinkedIn April 2025","LinkedIn via Curator Technologies","v1","LinkedIn over-represents advertising/design 6-8x BRES","","SOLENTHANTS LinkedIn","SRC-G2-029","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
("MEAS-G2-068","C-G2-075","Solent/Hampshire IDBR businesses","7530","","businesses","SHCA creative economy","","Solent and Hampshire","2025","","IDBR","IDBR","v1","","","SOLENTHANTS IDBR","SRC-G2-029","DESCRIPTIVE_ESTIMATE","NOT_REVIEWED","ECONOMIC_BASELINE","count","","Devin","2026-09-11","","","","","","","","1.3-candidate","G2-BATCH-B"),
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
    print(f"\nAppended {len(new_rows)} measurements (batch 2)")
print("Stage B complete.")
