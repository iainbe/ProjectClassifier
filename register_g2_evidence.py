#!/usr/bin/env python3
"""Stage 5: Register G2 post-2020 evidence links in 05_evidence_links.csv."""
import csv, os

CSV_PATH = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit/05_evidence_links.csv")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_ids = {row["evidence_id"] for row in reader}

print(f"Existing evidence IDs: {len(existing_ids)}")

# (evidence_id, claim_id, source_id, source_locator, extract_or_observation, supports_or_contradicts, evidence_type, limitations, notes, original_locator, derived_locator, source_family_id, codebook_version, review_batch)
links = [
# P16-CICP
("E-G2-033","C-G2-024","SRC-G2-011","lines 1-84","Evaluation approach designed with mixed-methods contribution analysis CBA DiD and LinkedIn/Meetup network mapping","SUPPORTS","qualitative","Approach design not outcome report","Iain contributed mapping and methodology via BOP; marginal claim","CICP approach document","extracted_text/SRC-G2-011_v1_full.txt","CICP-FAM","1.3-candidate","G2-BATCH-B"),

# P17-LCRCSU
("E-G2-034","C-G2-025","SRC-G2-012","line 12","Creative industries employment 58840 in 2018 net increase of 14420 jobs growth of 32% between 2015 and 2018","SUPPORTS","quantitative","BRES baseline measurement not intervention effect","Employment growth from BRES time series","Leeds City Region Creative Scale Up line 12","extracted_text/SRC-G2-012_v1_full.txt","LCRCSU-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-035","C-G2-026","SRC-G2-012","lines 57/104-109","Increasing importance of creative content and digital technology in other industries including smart cities energy health fintech manufacturing","SUPPORTS","qualitative","Interpretation from strategy documents not measured outcome","Cross-sector spillover forecast from bid evidence","Leeds City Region Creative Scale Up lines 57/104-109","extracted_text/SRC-G2-012_v1_full.txt","LCRCSU-FAM","1.3-candidate","G2-BATCH-B"),

# P18-GRIMSBY
("E-G2-036","C-G2-027","SRC-G2-013","lines 539/542","Active Lives Survey: arts participation 27.3% vs 34.6% national; arts attendance 42.9% vs 52.2%","SUPPORTS","quantitative","Participation baseline from national survey","Fifth Sector contributed mapping data; Magna Vitae authored","NELC Phase 1 Report lines 539-542","extracted_text/SRC-G2-013_v1_full.txt","GRIMSBY-FAM","1.3-candidate","G2-BATCH-B"),

# P19-LCRIMM
("E-G2-037","C-G2-028","SRC-G2-014","lines 721-724","Total organisations 169; total companies 126 of which 114 LCR-based; total assets 37; investors 6","SUPPORTS","quantitative","AI web search and LinkedIn mapping","Baseline mapping of LCR immersive ecosystem","LCR Immersive report lines 721-724","extracted_text/SRC-G2-014_v1_full.txt","LCRIMM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-038","C-G2-029","SRC-G2-014","lines 461-473/1430-1543","Immersive technologies applied across 25+ non-creative sectors; case studies: Draw and Code Kinicho VEC/Bentley Aardman","SUPPORTS","qualitative","Case studies show applications but not systematic measurement","Cross-sector product spillover case studies","LCR Immersive report lines 461-473/1430-1543","extracted_text/SRC-G2-014_v1_full.txt","LCRIMM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-039","C-G2-030","SRC-G2-014","lines 191-204/853-881","Supply-chain relationships map across digital/creative manufacturing health logistics; large end-users include Alstom Cammell Laird JLR","SUPPORTS","qualitative","Network mapping not causal claim","Network spillover from mapping and survey","LCR Immersive report lines 191-204/853-881","extracted_text/SRC-G2-014_v1_full.txt","LCRIMM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-040","C-G2-031","SRC-G2-014","lines 2057-2064/2176-2186","Multiple gated investment options proposed: Institute of Creative Technology demonstrator facilities large-scale XR venue","SUPPORTS","qualitative","Design propositions not implemented","Strategic options for Growth Platform","LCR Immersive report lines 2057-2064","extracted_text/SRC-G2-014_v1_full.txt","LCRIMM-FAM","1.3-candidate","G2-BATCH-B"),

# P20-SYMCA21
("E-G2-041","C-G2-032","SRC-G2-015","line 54","South Yorkshire creative industries: over 4000 companies and workforce of over 31000 people vs official 2895 businesses and 13500 employees","SUPPORTS","quantitative","BRES undercounts freelancers; LinkedIn captures additional workforce","Baseline mapping from multiple data sources","SYMCA CCI 2021 line 54","extracted_text/SRC-G2-015_v1_full.txt","SYMCA21-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-042","C-G2-033","SRC-G2-015","lines 190-195","Only 4.8% file full accounts; <2% (101) accessed R&D grants; 36 equity investments; 8 spinouts; 6 scale-ups","SUPPORTS","quantitative","Beauhurst and Companies House analysis","Creative growth paradox finding","SYMCA CCI 2021 lines 190-195","extracted_text/SRC-G2-015_v1_full.txt","SYMCA21-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-043","C-G2-034","SRC-G2-015","lines 292-293","South Yorkshire has been free riding on Screen Yorkshire for inward investment talent and crew services","SUPPORTS","qualitative","Network dependency finding","Free-riding on Screen Yorkshire","SYMCA CCI 2021 lines 292-293","extracted_text/SRC-G2-015_v1_full.txt","SYMCA21-FAM","1.3-candidate","G2-BATCH-B"),

# P21-MMUCCI
("E-G2-044","C-G2-035","SRC-G2-016","lines 129/134-135/203/214","REF 2021 ranked second for art and design research power; 70% world-leading English research impact; 85% of outputs receive no citations; research excellence largely unknown to external stakeholders","SUPPORTS","qualitative","Internal excellence vs external awareness gap","Stakeholder interviews and desk research","MMU CCI report lines 129/134-135/203/214","extracted_text/SRC-G2-016_v1_full.txt","MMUCCI-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-045","C-G2-036","SRC-G2-016","lines 102-106/229-240","MMU weakly connected to Manchester business networks (IOD Manchester Digital Pro Manchester); BBC/Creative UK relationship transactional","SUPPORTS","qualitative","Stakeholder interview findings","Network gap findings from interviews","MMU CCI report lines 102-106/229-240","extracted_text/SRC-G2-016_v1_full.txt","MMUCCI-FAM","1.3-candidate","G2-BATCH-B"),

# P22-LCRFILM
("E-G2-046","C-G2-037","SRC-G2-017","lines 60/66","£12.08m LCR spend from £1.788m invested ratio £6.76 per £1 invested","SUPPORTS","quantitative","LFO management data; documented output","Leverage ratio from LFO financial data","LCR Film Fund evaluation lines 60/66","extracted_text/SRC-G2-017_v1_full.txt","LCRFILM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-047","C-G2-038","SRC-G2-017","lines 234-241","Indirect FTE jobs: 455 delivered vs 280 target; average cost per indirect FTE job £3930 vs £6900 business case","SUPPORTS","quantitative","Documented output data from LFO","Indirect FTE jobs from monitoring data","LCR Film Fund evaluation Table 1 lines 234-241","extracted_text/SRC-G2-017_v1_full.txt","LCRFILM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-048","C-G2-039","SRC-G2-017","lines 258-261","Development Fund: £173604 deployed vs £250000 target; 17 LCR companies vs 12 target; 43 LCR jobs vs 30 target","SUPPORTS","quantitative","Documented output data from LFO","Development Fund outputs from monitoring","LCR Film Fund evaluation lines 258-261","extracted_text/SRC-G2-017_v1_full.txt","LCRFILM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-049","C-G2-040","SRC-G2-017","lines 76/61","LFO moved from provider to partner by drawing in Fund Advisor external assessors/panel and broadcaster partners; training places for 29 LCR individuals","SUPPORTS","qualitative","Knowledge spillover from partnership model","LFO partnership evolution","LCR Film Fund evaluation lines 61/76","extracted_text/SRC-G2-017_v1_full.txt","LCRFILM-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-050","C-G2-041","SRC-G2-017","lines 138-140","Pipeline: >£6m capital demand to leverage ~£35m LCR spend; 7 seeded by Development Fund; indigenous 7.8:1 vs incoming 3.7:1","SUPPORTS","quantitative","Pipeline forecasts not realised outcomes","Development Fund seed capital option","LCR Film Fund evaluation lines 138-140","extracted_text/SRC-G2-017_v1_full.txt","LCRFILM-FAM","1.3-candidate","G2-BATCH-B"),

# P23-DERBY
("E-G2-051","C-G2-042","SRC-G2-018","lines 73/89-93/97-124","Staged start-up: 2 FTE roles at inception with scope to add grant/equity once demand proven; Liverpool comparator cost-neutral 2 FTE £100k budget","SUPPORTS","qualitative","Design proposition not implemented","Feasibility study design","Derby feasibility study lines 73/89-93/97-124","extracted_text/SRC-G2-018_v1_full.txt","DERBY-FAM","1.3-candidate","G2-BATCH-B"),

# P24-SYMCACGP
("E-G2-052","C-G2-043","SRC-G2-019","lines 56/149-156","Culture and creative industries worth up to £2bn in GVA; if as productive as national average would exceed £1bn; if South East nearly £1.4bn","SUPPORTS","quantitative","Modelled estimate using generic ONS productivity index","GVA estimate from DCMS and ONS data","SYMCA CGP final lines 56/149-156","extracted_text/SRC-G2-019_v1_full.txt","SYMCACGP-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-053","C-G2-044","SRC-G2-019","line 148","Every 1 FTE directly employed supports total footprint of 2.46 FTE (0.62 indirect + 0.84 induced)","SUPPORTS","quantitative","DCMS modelling; contextual not intervention effect","Multiplier from DCMS modelling","SYMCA CGP final line 148","extracted_text/SRC-G2-019_v1_full.txt","SYMCACGP-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-054","C-G2-045","SRC-G2-019","lines 224/259/263","1013 creative courses across region and wider TTWA; 24 providers 331 courses in SYMCA; only 5 creative apprenticeships","SUPPORTS","quantitative","Course/qualification audit","Skills mapping from course audit","SYMCA CGP final lines 224/259/263","extracted_text/SRC-G2-019_v1_full.txt","SYMCACGP-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-055","C-G2-046","SRC-G2-019","lines 59-62","Time-limited policy windows: ACE Priority Places (Barnsley Rotherham) DCMS Levelling Up for Culture NP11","SUPPORTS","qualitative","Strategic option proposition","Policy windows from consultation","SYMCA CGP final lines 59-62","extracted_text/SRC-G2-019_v1_full.txt","SYMCACGP-FAM","1.3-candidate","G2-BATCH-B"),

# P25-LANCGP
("E-G2-056","C-G2-047","SRC-G2-020","lines 144/149/166","Creative economy: 4500 businesses and 36000 jobs (6% of workforce); 980 new formations since April 2021","SUPPORTS","quantitative","IDBR April 2021 and Beauhurst analysis","Baseline from IDBR and Beauhurst","Lancashire CGP lines 144/149/166","extracted_text/SRC-G2-020_v1_full.txt","LANCGP-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-057","C-G2-048","SRC-G2-020","lines 455-458","Pennine Originals will focus on technical textiles homewares and high-quality printed goods with spillovers into aerospace and automotive","SUPPORTS","qualitative","Design proposition in grant application not outcome","Product spillover from bid design","Lancashire CGP lines 455-458","extracted_text/SRC-G2-020_v1_full.txt","LANCGP-FAM","1.3-candidate","G2-BATCH-B"),

# P26-WSBH
("E-G2-058","C-G2-049","SRC-G2-021","lines 91/166/186/214","10225 creative companies and 54428 workforce vs official 7470 businesses and 23690 employees; BRES 2021 22325","SUPPORTS","quantitative","LinkedIn not directly comparable to BRES","Baseline from BRES LinkedIn and Beauhurst","WSBH strategy lines 91/166/186/214","extracted_text/SRC-G2-021_v1_full.txt","WSBH-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-059","C-G2-050","SRC-G2-021","lines 339-340","Createch strengths in immersive/VR/AR/XR and Virtual Production being adopted across film TV games animation and live experiences","SUPPORTS","qualitative","Documented observation from mapping","Product spillover from Createch adoption","WSBH strategy lines 339-340","extracted_text/SRC-G2-021_v1_full.txt","WSBH-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-060","C-G2-051","SRC-G2-021","line 261","Creative Assembly and Red River act as anchor investors supporting supply chain of smaller digital creative businesses and contractors","SUPPORTS","qualitative","Network spillover from mapping and consultation","Anchor firm network effects","WSBH strategy line 261","extracted_text/SRC-G2-021_v1_full.txt","WSBH-FAM","1.3-candidate","G2-BATCH-B"),

# P27-WAKECDF
("E-G2-061","C-G2-052","SRC-G2-022","lines 77/324/379","CDF programme: £4.38m grant; £22.03m total value; £13.64m public capital; £6.06m private leveraged","SUPPORTS","quantitative","Documented financial data","Financial data from Council records","Wakefield CDF evaluation lines 77/324/379","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-062","C-G2-053","SRC-G2-022","lines 343-356","CCI employment 2210 to 2910 (+32%); GVA £52.8m to £94.2m (+79%); music/performing +194%; arts output £4.6m to £32.8m (+600%)","SUPPORTS","quantitative","Modelled estimates not causal attribution; report uses correlates with language","Employment and GVA from ONS BRES and DCMS","Wakefield CDF evaluation lines 343-356","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-063","C-G2-054","SRC-G2-022","lines 299/451/548/566","Creative Wakefield network grew from 150 (Apr 2020) to 837 (Oct 2024) +458%; website visits 58428 to 124527","SUPPORTS","quantitative","Documented membership data","Network growth from membership data","Wakefield CDF evaluation lines 299/451/548/566","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-064","C-G2-055","SRC-G2-022","lines 756-759","XPLOR supported 10 enterprises to introduce new-to-market products and 20 to introduce new-to-firm products","SUPPORTS","quantitative","Documented monitoring data with specific companies listed","Product spillover from XPLOR monitoring","Wakefield CDF evaluation Table 13 lines 756-759","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-065","C-G2-056","SRC-G2-022","lines 84/89/151/231-240","CDF catalysed strategic alliance between Council and Production Park instrumental in securing CoSTAR; 4Wall and Tait established UK HQs","SUPPORTS","qualitative","Attribution based on interview testimony not counterfactual","Network spillover from testimony","Wakefield CDF evaluation lines 84/89/151/231-240","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-066","C-G2-057","SRC-G2-022","line 270","Creative Leadership programme: 15 participants from 11 sub-sectors resulting in 12 new and ongoing cross-sector collaborations","SUPPORTS","quantitative","Documented programme monitoring","Knowledge spillover from programme data","Wakefield CDF evaluation line 270","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-067","C-G2-058","SRC-G2-022","lines 96/339/563/773","INTERNAL INCONSISTENCY: 120 FTE in executive summary (lines 96 563) vs 160 FTE in main body Table 14 (lines 339 773)","SUPPORTS","qualitative","Internal source inconsistency flagged","Source inconsistency documented","Wakefield CDF evaluation lines 96/339/563/773","extracted_text/SRC-G2-022_v1_full.txt","WAKECDF-FAM","1.3-candidate","G2-BATCH-B"),

# P28-CALDER
("E-G2-068","C-G2-059","SRC-G2-023","lines 78/86/107/126","655 ONS firms (880 Beauhurst); 2360 BRES employment; 7375 LinkedIn workforce; 1620 freelance (32%)","SUPPORTS","quantitative","LinkedIn not comparable to BRES; 83% report employment status","Baseline from multiple data sources","Calderdale report lines 78/86/107/126","extracted_text/SRC-G2-023_v1_full.txt","CALDER-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-069","C-G2-060","SRC-G2-023","line 190","New blended creative and digital skills in demand across health finance construction and other sectors","SUPPORTS","qualitative","Interpretation of skills-market data","Cross-sector skills demand hypothesis","Calderdale report line 190","extracted_text/SRC-G2-023_v1_full.txt","CALDER-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-070","C-G2-061","SRC-G2-023","lines 237-266","Screen Yorkshire Connected Campus links TV/film professionals production companies broadcasters and students across Yorkshire HEIs and FE colleges","SUPPORTS","qualitative","Documented network; unclear if Calderdale College joining","Network spillover from documented network","Calderdale report lines 237-266","extracted_text/SRC-G2-023_v1_full.txt","CALDER-FAM","1.3-candidate","G2-BATCH-B"),

# P29-SOLENTCGP
("E-G2-071","C-G2-062","SRC-G2-024","lines 111/156","4510 active CI businesses (10.7% of 42000); 40000 CI jobs with £1.5bn GVA (Lightcast)","SUPPORTS","quantitative","Beauhurst 33% higher than IDBR; freelance not accurately measured","Baseline from Beauhurst and Lightcast","Solent CGP draft lines 111/156","extracted_text/SRC-G2-024_v1_full.txt","SOLENTCGP-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-072","C-G2-063","SRC-G2-024","line 318","Createch cohort designed for IP for live events museums film/VFX virtual production and games with spillovers into maritime aerospace logistics","SUPPORTS","qualitative","Design proposition in draft application","Product spillover from bid design","Solent CGP draft line 318","extracted_text/SRC-G2-024_v1_full.txt","SOLENTCGP-FAM","1.3-candidate","G2-BATCH-B"),

# P30-HEREFORD
("E-G2-073","C-G2-064","SRC-G2-025","lines 105-107","590 official creative businesses flat vs 2019; over 4000 LinkedIn professionals c.3x larger","SUPPORTS","quantitative","Limited data collection obscures true sector size","Baseline from ONS/DCMS and LinkedIn","Herefordshire review lines 105-107","extracted_text/SRC-G2-025_v1_full.txt","HEREFORD-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-074","C-G2-065","SRC-G2-025","line 155","Opportunity to pioneer rural creative economy models with cross-cutting skills for agritech ecotourism and wellbeing","SUPPORTS","qualitative","Strategic hypothesis not realised","Rural creative economy option","Herefordshire review line 155","extracted_text/SRC-G2-025_v1_full.txt","HEREFORD-FAM","1.3-candidate","G2-BATCH-B"),

# P31-PRODPARK
("E-G2-075","C-G2-066","SRC-G2-026","lines 13-25","LinkedIn industry codes mapped to BRES SIC07 for West Yorkshire/Wakefield; BRES 2022 columns empty","SUPPORTS","quantitative","Data fragment only; incomplete; BRES columns empty","Data fragment from table","Production Park GVA data lines 13-25","extracted_text/SRC-G2-026_v1_full.txt","PRODPARK-FAM","1.3-candidate","G2-BATCH-B"),

# P32-SURREY
("E-G2-076","C-G2-067","SRC-G2-027","lines 5/14-17","£7.2 billion annually; over 17000 companies; 115000+ workforce; 12% real growth since 2019 vs UK average 2%","SUPPORTS","quantitative","Underlying data sources not shown in text","Baseline from mapping evidence","Surrey+ strategy lines 5/14-17","extracted_text/SRC-G2-027_v1_full.txt","SURREY-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-077","C-G2-068","SRC-G2-027","lines 46-47","Farnborough aircraft hangars turned to sound stages; Sony Professional at Pinewood developing camera systems for Warner Bros/Apple F1 movie","SUPPORTS","qualitative","Documented examples of aerospace-to-screen transfer","Product spillover from documented examples","Surrey+ strategy lines 46-47","extracted_text/SRC-G2-027_v1_full.txt","SURREY-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-078","C-G2-069","SRC-G2-027","lines 149-153","£3-4m strategic investment over 3 years could catalyse 450-600 new jobs £15-20m economic value and over £30m private investment","SUPPORTS","quantitative","Modelled forecast not observed outcome","Investment forecast from modelling","Surrey+ strategy lines 149-153","extracted_text/SRC-G2-027_v1_full.txt","SURREY-FAM","1.3-candidate","G2-BATCH-B"),

# P33-LCRMUS
("E-G2-079","C-G2-070","SRC-G2-028","lines 266/282/289/801","Direct GVA £405.9m (Integrated Case); total economic impact £779.8m (Type II multiplier 1.92); 14370 headcount 7215 FTE","SUPPORTS","quantitative","Modelled estimate; Tier 4 data quality low (50% confidence)","GVA from four-tier workforce model","LCR Music report lines 266/282/289/801","extracted_text/SRC-G2-028_v1_full.txt","LCRMUS-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-080","C-G2-071","SRC-G2-028","line 88","Adlib Audio serves major touring productions festivals and corporate events across UK and internationally","SUPPORTS","qualitative","Documented business fact","Product spillover from Adlib cross-sector services","LCR Music report line 88","extracted_text/SRC-G2-028_v1_full.txt","LCRMUS-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-081","C-G2-072","SRC-G2-028","lines 311-334","SNA of 272 businesses: 12% of connections within closed triangles; only 0.6% of possible connections exist; average degree 1.67","SUPPORTS","quantitative","SNA maps existing structure; low connectivity limits spillover claims","SNA results from LinkedIn workforce movement","LCR Music report lines 311-334","extracted_text/SRC-G2-028_v1_full.txt","LCRMUS-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-082","C-G2-073","SRC-G2-028","lines 104/338/846-868","£1bn by 2035 target requires 2.5% CAGR; growth levers: IP capture £100m production export £75m formalisation £60m venues £50m music-tech £43m","SUPPORTS","quantitative","Modelled targets not realised outcomes","Growth scenarios and levers from modelling","LCR Music report lines 104/338/846-868","extracted_text/SRC-G2-028_v1_full.txt","LCRMUS-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-083","C-G2-074","SRC-G2-028","line 360","Moving 20% of artists from performance-fee-only to performance-plus-IP-ownership could shift £40-85m in captured GVA","SUPPORTS","quantitative","Modelled design proposition","IP capture option from modelling","LCR Music report line 360","extracted_text/SRC-G2-028_v1_full.txt","LCRMUS-FAM","1.3-candidate","G2-BATCH-B"),

# P34-SOLENTHANTS
("E-G2-084","C-G2-075","SRC-G2-029","lines 15/23/90/367","Creative Industries GVA estimated £5.25bn (reconciled); 39980 BRES employees; 80511 LinkedIn workforce; 7530 IDBR businesses","SUPPORTS","quantitative","DCMS top-down £6.9bn almost certainly overestimate; 31% IT contraction","Reconciled GVA from multiple sources","Solent Hampshire mapping lines 15/23/90/367","extracted_text/SRC-G2-029_v1_full.txt","SOLENTHANTS-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-085","C-G2-076","SRC-G2-029","line 98","Freelancers play critical role in innovation and knowledge transfer between creative firms and other sectors and between universities and cultural organisations","SUPPORTS","qualitative","Interpretation from LinkedIn analysis","Knowledge spillover interpretation from LinkedIn","Solent Hampshire mapping line 98","extracted_text/SRC-G2-029_v1_full.txt","SOLENTHANTS-FAM","1.3-candidate","G2-BATCH-B"),
("E-G2-086","C-G2-077","SRC-G2-029","lines 26/115/117","SHCA creative economy is network of interconnected specialised hubs; advertising/marketing co-located with professional services indicating B2B ecosystem","SUPPORTS","qualitative","Interpretation from HDBSCAN and LQ mapping; HDBSCAN caveat re accountants","Network spillover from spatial mapping","Solent Hampshire mapping lines 26/115/117","extracted_text/SRC-G2-029_v1_full.txt","SOLENTHANTS-FAM","1.3-candidate","G2-BATCH-B"),
]

new_rows = []
for l in links:
    eid = l[0]
    if eid in existing_ids:
        print(f"SKIP {eid}")
        continue
    row = {h: l[i] if i < len(l) else "" for i, h in enumerate(header)}
    new_rows.append(row)
    print(f"ADD  {eid}: {l[1]}")

if new_rows:
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        for row in new_rows:
            writer.writerow(row)
    print(f"\nAppended {len(new_rows)} evidence links")
print("Stage 5 complete.")
