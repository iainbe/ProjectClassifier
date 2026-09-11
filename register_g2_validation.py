#!/usr/bin/env python3
"""Tier 2 Stage C: Validation actions for post-2020 G2 projects."""
import csv, os

CSV_PATH = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit/07_validation_actions.csv")

with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames
    existing_ids = {row["validation_id"] for row in reader}

print(f"Existing validation IDs: {len(existing_ids)}")

# Use the first header row (line 1) which has the full field set
# Fields: validation_id,claim_id,open_question,proposed_method,data_access_consent_needs,priority,effort_estimate,owner,approval_status,result,stopping_rule,notes,source_id,opportunity_id,issue_id,gate,review_status,codebook_version,review_batch

validations = [
# P16-CICP
("VAL-G2-001","C-G2-024","Confirm Iain's specific contribution to CICP evaluation approach — sector/workforce mapping and methodology design via BOP","Review BOP/Frontier contract records or correspondence","Iain confirmation obtained 2026-09-11","LOW","15min","Iain","APPROVED","RESOLVED — Iain confirmed sector/workforce mapping and methodology design contribution via BOP; marginal claim","Stop after Iain confirmation","CICP marginal claim confirmed","","ISSUE-G2-001","CONTRACTING_ROLE","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P17-LCRCSU
("VAL-G2-002","C-G2-025","Verify BRES employment figures for Leeds City Region 2015-2018","Cross-check ONS Nomisweb BRES data","Public data accessible","LOW","30min","Devin","NOT_REQUESTED","PENDING","Stop if BRES data unavailable; figures stand as reported","BRES is official data; source cited in report","SRC-G2-012","","ISSUE-G2-002","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P18-GRIMSBY
("VAL-G2-003","C-G2-027","Confirm Fifth Sector's specific mapping data contribution to Grimsby/NE Lincs study","Iain confirmation or review of source document","Iain confirmed 2026-09-11","LOW","15min","Iain","APPROVED","RESOLVED — Iain confirmed mapping data contribution; Magna Vitae authored report","Stop after Iain confirmation","Mapping data contribution confirmed","","","ISSUE-G2-003","CONTRACTING_ROLE","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P19-LCRIMM
("VAL-G2-004","C-G2-029","Verify cross-sector case study claims (Draw and Code Kinicho VEC/Bentley) against source document","Spot-check lines 461-473 and 1430-1543 of extracted text","Internal source available","MEDIUM","30min","Devin","NOT_REQUESTED","PENDING","Stop if case studies cannot be verified in source","Case studies documented in report; spot-check needed","SRC-G2-014","","ISSUE-G2-004","SOURCE_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P20-SYMCA21
("VAL-G2-005","C-G2-033","Verify creative growth paradox figures (4.8% full accounts <2% R&D grants 36 equity 8 spinouts 6 scale-ups)","Spot-check lines 190-195 of extracted text","Internal source available","MEDIUM","20min","Devin","NOT_REQUESTED","PENDING","Stop if figures cannot be verified","Key finding; needs spot-check","SRC-G2-015","","ISSUE-G2-005","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P21-MMUCCI
("VAL-G2-006","","Verify MMU stakeholder interview sample size and methodology","Check report for interview count and selection method","Internal source available","LOW","15min","Devin","NOT_REQUESTED","PENDING","Stop if methodology unclear","Stakeholder interviews Mar-Aug 2022; sample size not recorded in claims","SRC-G2-016","","ISSUE-G2-006","METHODOLOGY_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P22-LCRFILM
("VAL-G2-007","C-G2-037","Verify £6.76 leverage ratio and £12.08m LCR spend against LFO financial data","Spot-check lines 60/66 of extracted text","Internal source available","HIGH","20min","Devin","NOT_REQUESTED","PENDING","Stop if figures cannot be verified","Richest quantitative evidence; high-risk numeric claim","SRC-G2-017","","ISSUE-G2-007","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),
("VAL-G2-008","C-G2-041","Verify Development Fund pipeline forecasts (7.8:1 indigenous vs 3.7:1 incoming)","Spot-check lines 138-140 of extracted text","Internal source available","MEDIUM","20min","Devin","NOT_REQUESTED","PENDING","Stop if forecasts cannot be verified","Forecast not realised; option value claim","SRC-G2-017","","ISSUE-G2-008","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P23-DERBY
("VAL-G2-009","","Confirm whether Derby/ Derbyshire film office was established after feasibility study","Check for post-feasibility implementation evidence","May require Iain knowledge","LOW","15min","Iain","NOT_REQUESTED","PENDING","Stop if no evidence; design proposition stands as unimplemented","Feasibility study; outcome unknown","","","ISSUE-G2-009","BID_OUTCOME","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P24-SYMCACGP
("VAL-G2-010","C-G2-043","Verify £2bn GVA upper estimate methodology and assumptions","Spot-check lines 56/149-156 of extracted text","Internal source available","MEDIUM","20min","Devin","NOT_REQUESTED","PENDING","Stop if methodology unclear","Modelled using generic ONS productivity index; key caveat","SRC-G2-019","","ISSUE-G2-010","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P25-LANCGP
("VAL-G2-011","C-G2-048","Confirm Lancashire CGP bid outcome — Iain confirmed unsuccessful 2026-09-11","Iain confirmation","Obtained","LOW","5min","Iain","APPROVED","RESOLVED — BID UNSUCCESSFUL; programme not awarded","Stop after confirmation","Bid unsuccessful confirmed by Iain","","","ISSUE-G2-011","BID_OUTCOME","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P26-WSBH
("VAL-G2-012","C-G2-049","Verify WSBH company count (10225 Beauhurst vs 7470 official)","Spot-check lines 91/166/186/214 of extracted text","Internal source available","MEDIUM","20min","Devin","NOT_REQUESTED","PENDING","Stop if figures cannot be verified","Baseline mapping; Beauhurst 38.6% greater than official","SRC-G2-021","","ISSUE-G2-012","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P27-WAKECDF
("VAL-G2-013","C-G2-058","Resolve internal inconsistency: 120 FTE (exec summary) vs 160 FTE (main body Table 14)","Inspect original document Tables 1 and 14","Internal source available","HIGH","30min","Iain","NOT_REQUESTED","PENDING","Stop if original cannot resolve; preserve both figures","Critical inconsistency in jobs figure; both recorded in measurements","SRC-G2-022","","ISSUE-G2-013","CONSISTENCY_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),
("VAL-G2-014","C-G2-053","Verify Wakefield CCI employment +32% and GVA +79% — modelled not causal","Spot-check lines 343-356 of extracted text","Internal source available","HIGH","30min","Devin","NOT_REQUESTED","PENDING","Stop if figures cannot be verified","Report uses correlates with language; modelled not causal attribution","SRC-G2-022","","ISSUE-G2-014","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),
("VAL-G2-015","C-G2-056","Verify CoSTAR attribution claim — CDF catalysed alliance instrumental in securing CoSTAR","Spot-check lines 84/89/151/231-240","Internal source available","HIGH","30min","Iain","NOT_REQUESTED","PENDING","Stop if attribution unclear; testimony-based not counterfactual","Attribution based on interview testimony; needs Iain review","SRC-G2-022","","ISSUE-G2-015","ATTRIBUTION_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P28-CALDER
("VAL-G2-016","","Verify Calderdale music deep dive data (378 LinkedIn 273 MU members 63 licensed venues)","Spot-check music section of extracted text","Internal source available","LOW","20min","Devin","NOT_REQUESTED","PENDING","Stop if figures cannot be verified","Music deep dive; multiple data sources","SRC-G2-023","","ISSUE-G2-016","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P29-SOLENTCGP
("VAL-G2-017","C-G2-063","Confirm Solent CGP bid outcome — Iain confirmed unsuccessful 2026-09-11","Iain confirmation","Obtained","LOW","5min","Iain","APPROVED","RESOLVED — BID UNSUCCESSFUL; programme not awarded","Stop after confirmation","Draft application; bid unsuccessful confirmed by Iain","","","ISSUE-G2-017","BID_OUTCOME","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P30-HEREFORD
("VAL-G2-018","","Confirm Herefordshire lead consultant role — Iain confirmed 2026-09-11","Iain confirmation","Obtained","LOW","5min","Iain","APPROVED","RESOLVED — Iain confirmed lead consultant","Stop after confirmation","Lead consultant confirmed","","","ISSUE-G2-018","CONTRACTING_ROLE","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P31-PRODPARK
("VAL-G2-019","C-G2-066","Note: Production Park data fragment is incomplete — BRES 2022 columns empty","No action needed; data fragment flagged as incomplete","N/A","LOW","5min","Devin","APPROVED","RESOLVED — Data fragment incomplete; BRES columns empty; supplements P27-WAKECDF","Stop after flagging","Incomplete extract; no spillover evidence","SRC-G2-026","","ISSUE-G2-019","DATA_QUALITY","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P32-SURREY
("VAL-G2-020","C-G2-067","Verify Surrey+ £7.2bn value and 17000 companies — underlying data sources not shown in text","Spot-check lines 5/14-17 of extracted text","Internal source available","MEDIUM","20min","Devin","NOT_REQUESTED","PENDING","Stop if data sources cannot be identified","Underlying data sources not shown in text; needs verification","SRC-G2-027","","ISSUE-G2-020","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),
("VAL-G2-021","C-G2-068","Verify Farnborough hangars-to-sound-stages claim","Spot-check lines 46-47 of extracted text","Internal source available","MEDIUM","15min","Devin","NOT_REQUESTED","PENDING","Stop if claim cannot be verified","Product spillover example; needs verification","SRC-G2-027","","ISSUE-G2-021","SOURCE_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P33-LCRMUS
("VAL-G2-022","C-G2-070","Verify LCR Music £405.9m direct GVA and £779.8m total impact — four-tier workforce model","Spot-check lines 266/282/289/801 of extracted text","Internal source available","HIGH","30min","Devin","NOT_REQUESTED","PENDING","Stop if figures cannot be verified","Richest methodological innovation; modelled estimate with Tier 4 caveats","SRC-G2-028","","ISSUE-G2-022","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),
("VAL-G2-023","C-G2-072","Verify SNA results (272 businesses 12% closed triangles 0.6% possible connections avg degree 1.67)","Spot-check lines 311-334 of extracted text","Internal source available","MEDIUM","20min","Devin","NOT_REQUESTED","PENDING","Stop if SNA results cannot be verified","SNA is methodological innovation; key finding","SRC-G2-028","","ISSUE-G2-023","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),

# P34-SOLENTHANTS
("VAL-G2-024","C-G2-075","Verify reconciled GVA £5.25bn vs DCMS top-down £6.9bn — source states £6.9bn almost certainly overestimate","Spot-check lines 15/23/90/367 of extracted text","Internal source available","HIGH","30min","Devin","NOT_REQUESTED","PENDING","Stop if reconciliation cannot be verified","Key reconciliation; DCMS overestimate flagged in source","SRC-G2-029","","ISSUE-G2-024","NUMERIC_CHECK","REVIEWED","1.3-candidate","G2-BATCH-B"),
]

new_rows = []
for v in validations:
    vid = v[0]
    if vid in existing_ids:
        print(f"SKIP {vid}")
        continue
    row = {h: v[i] if i < len(v) else "" for i, h in enumerate(header)}
    new_rows.append(row)
    print(f"ADD  {vid}")

if new_rows:
    with open(CSV_PATH, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        for row in new_rows:
            clean = {k: val for k, val in row.items() if k is not None}
            writer.writerow(clean)
    print(f"\nAppended {len(new_rows)} validation actions")
print("Stage C complete.")
