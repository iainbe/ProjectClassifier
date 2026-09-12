#!/usr/bin/env python3
"""
Deepen P02-FGTG claims from 4 to comprehensive coverage.
Sources read in full:
  SRC-R2-03 (FG2G Update, Nov 6 2024) - Teams meeting transcript, workshop planning
  SRC-R3-01 (From Good to Great workshop report, Jun 17 2025) - workshop outcomes
  SRC-R3-02 (GMCA FGTG options, Jun 13 2025) - strategic options document
  SRC-R3-03 (FGTG Workshop analysis, Jun 11 2025) - workshop analysis by Steve Hillier

Key distinctions:
  - SRC-R2-03 is a PLANNING transcript (workshop not yet delivered)
  - SRC-R3-01/03 confirm workshop DELIVERY with outcomes
  - SRC-R3-02 is a DESIGN/RECOMMENDATION document (proposed not implemented)
  - Workshop delivered December 2024 at MMU
  - Options document proposes devolved funding variations (NOT implemented)
"""

import csv
import os

TOOLKIT_DIR = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit"

NEXT_CLAIM = 381
NEXT_EVIDENCE = 287

PROJECT_ID = "P02-FGTG"
REVIEW_BATCH = "G2-BATCH-D"
CODEBOOK = "1.3-candidate"

# Existing methods
M_COMPANY = "M-R3-004"  # company_data_analysis
M_WORKSHOP = "M-R3-005"  # workshop_facilitation
M_OPTIONS = "M-R3-006"  # options_analysis

def make_claim(claim_num, proposition, claim_type, effect_family, **kwargs):
    cid = f"C-G2-{claim_num:03d}"
    defaults = {
        "claim_id": cid, "project_id": PROJECT_ID,
        "precise_proposition": proposition, "effect_family": effect_family,
        "mechanism": "", "option_subtype": "", "originator": "The Fifth Sector",
        "recipient": "", "intended_beneficiary_status": "INTENDED",
        "event_period": "2024-12", "claim_direction": "BENEFICIAL",
        "outcome_status": "REPORTED", "attribution_strength": "DESCRIPTIVE",
        "value_status": "NONE", "boundary_recipient": "INTENDED",
        "boundary_org": "WITHIN_ORG", "boundary_sector": "WITHIN_SECTOR",
        "boundary_geography": "WITHIN_AREA", "boundary_chain": "WITHIN_CHAIN",
        "compensation": "COMPENSATED", "intent": "DESIGNED_IN",
        "timing": "REALISED", "direction": "BENEFICIAL",
        "beneficiaries": "", "cost_bearers": "", "access_barriers": "",
        "evidence_sufficiency": "Sufficient from workshop report and analysis",
        "source_quality": "primary", "independence": "UNKNOWN",
        "coverage": "PARTIAL", "time_lag": "CONTEMPORARY",
        "contrary_evidence": "NONE_FOUND_IN_REVIEW",
        "reviewer_confidence": "MEDIUM", "commercial_reuse": "INTERNAL_ONLY",
        "fifth_sector_role": "DESIGNER;DELIVERER",
        "review_status": "REVIEWED", "publication_status": "INTERNAL_ONLY",
        "notes": "", "claim_type": claim_type, "method_ids": "",
        "generating_intervention": "Innovation funding support workshop",
        "fifth_sector_contribution": "Workshop design and delivery with MMU",
        "contracting_role": "CO_DELIVERY",
        "tie_change": "", "option_state": "", "option_holder": "",
        "exercise_access": "", "prediction": "", "rival_explanations": "",
        "disconfirming_evidence": "", "observation_window": "2024-12",
        "source_review_state": "REVIEWED", "value_basis": "",
        "value_review_status": "NOT_REVIEWED", "permission_status": "UNKNOWN",
        "rights_status": "UNKNOWN", "consent_status": "",
        "causal_assumptions": "", "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    }
    defaults.update(kwargs)
    return defaults

claims_data = []
n = NEXT_CLAIM

# === CONTEXT CLAIMS ===
claims_data.append(make_claim(n, "MMU aims to increase RD&I activity with focus on SMEs and support SMEs to access innovation funding including Innovate UK, with current success rates lower than expected",
    "CONTEXT", "CONTEXTUAL", method_ids=M_COMPANY,
    notes="MMU strategic context; Innovate UK success rates below expected for GM SMEs"))
n += 1

claims_data.append(make_claim(n, "Innovate UK and Innovate Edge already provide tailored support and promote funding opportunities, but workshop identified gaps in GM-specific ecosystem support",
    "CONTEXT", "CONTEXTUAL", method_ids=M_COMPANY,
    notes="Existing support landscape; workshop designed to complement not replace existing provision"))
n += 1

claims_data.append(make_claim(n, "Two businesses confirmed as workshop speakers: Arcadus (large engineering consultancy from green energy to civils) and Vector Homes (SME perspective)",
    "CONTEXT", "CONTEXTUAL", method_ids=M_WORKSHOP,
    notes="Speaker lineup; balance of large firm and SME perspectives"))
n += 1

claims_data.append(make_claim(n, "Workshop target was 8-10 additional businesses in room alongside two speaker businesses, with 50-50 balance between businesses and intermediaries sought",
    "CONTEXT", "CONTEXTUAL", method_ids=M_WORKSHOP,
    notes="Attendance target; balance concern raised in planning"))
n += 1

# === EFFECT CLAIMS (workshop outcomes) ===
claims_data.append(make_claim(n, "Workshop practical bid writing guidance valued by participants who appreciated succinct advice and tangible actionable guidance over theoretical presentations",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Participant feedback; practical approach resonated strongly"))
n += 1

claims_data.append(make_claim(n, "Workshop achieved ecosystem collaboration with GMCA, Growth Hub, universities, and businesses in single forum, with participant observing 'the strongest element was the whole Manchester ecosystem working together'",
    "EFFECT", "NETWORK", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Ecosystem collaboration outcome; cross-sector understanding and partnership development"))
n += 1

claims_data.append(make_claim(n, "Workshop slide sharing extended value beyond session itself, with participants distributing materials within their organisations",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Post-event value; content practical applicability and ongoing relevance"))
n += 1

claims_data.append(make_claim(n, "University IP policies identified as structural barrier to university-business collaboration, with SMEs reporting they would have to give up all IP and license it back, described as 'ridiculous' for an SME",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="IP barrier finding; complexity of IP negotiations; participants with experience on both sides noted more nuance"))
n += 1

claims_data.append(make_claim(n, "Supply chain collaboration barrier identified: 50% cost recovery rate for large companies means they lose money on every bid, making business case for investment difficult",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Supply chain gap; large firm representative identified structural difficulty; SME leading bid as junior partner seen as unrealistic"))
n += 1

claims_data.append(make_claim(n, "Content timing mismatch identified: participants found guidance would have been more useful before they had a bid, suggesting need for better alignment between content delivery and participant readiness",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Timing feedback; pre-qualification gap evidence"))
n += 1

claims_data.append(make_claim(n, "Technical and presentation issues undermined content delivery: projector failures and slides too small to read effectively",
    "EFFECT", "NOT_APPLICABLE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    claim_direction="ADVERSE",
    notes="Technical issues; some most valuable content only partially delivered"))
n += 1

claims_data.append(make_claim(n, "Business attendance remained disappointingly low despite quality content and venue, with participants suggesting improved marketing could easily attract 20+ businesses",
    "EFFECT", "NOT_APPLICABLE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Low attendance; unclear value proposition and insufficient allure beyond website identified as factors"))
n += 1

claims_data.append(make_claim(n, "Universities perceived as critical but problematic partners: slow-moving with complex internal processes difficult for SMEs to navigate, with MMU perceived as more agile than UoM",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="University engagement finding; UoM lacks self-awareness of SME experience; smaller institutions more agile"))
n += 1

claims_data.append(make_claim(n, "Participants requested breakout groups focused on specific themes such as risk management, partnering strategies, or sector-specific challenges for future workshops",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Format recommendation; demand for targeted hands-on activities"))
n += 1

claims_data.append(make_claim(n, "Participants requested real-world case studies featuring clients talking about whole process from discovering opportunity to making application",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Content recommendation; comprehensive journey mapping rather than isolated advice"))
n += 1

claims_data.append(make_claim(n, "Participants requested post-workshop application review support with one person designated to review applications before submission",
    "EFFECT", "KNOWLEDGE", method_ids=M_WORKSHOP,
    outcome_status="REPORTED",
    notes="Post-event support need; pre-qualification stage and ongoing advisory services suggested"))
n += 1

# === DESIGN CLAIMS (options document) ===
claims_data.append(make_claim(n, "Three critical systemic issues identified: Pre-Qualification Gap (SMEs enter funding without business case validation), Strategic Alignment Gap (call timing disconnected from regional priorities), and Supply Chain Investment Gap (50% cost recovery creates collaboration barriers)",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="GAP_ANALYSIS",
    option_state="IDENTIFIED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Three gaps from workshop feedback; mask deeper structural problems"))
n += 1

claims_data.append(make_claim(n, "Stage 1 proposed: Strategic Pre-Qualification (GM-led) with business case validation workshops, sector-specific readiness assessment, university-SME IP framework alignment, and supply chain mapping",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="PROCESS_STAGE",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Stage 1 of 4-stage framework; GM-led pre-qualification gateway"))
n += 1

claims_data.append(make_claim(n, "Stage 2 proposed: Enhanced Application Support (GM-enhanced) with dedicated application review service, peer mentoring from successful applicants, and technical writing support",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="PROCESS_STAGE",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Stage 2; GM-enhanced application support"))
n += 1

claims_data.append(make_claim(n, "Stage 3 proposed: Strategic Call Alignment (GM-influenced) with quarterly strategic calls aligned to GM priorities, predictable timing for key sectors, and clear success criteria",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="PROCESS_STAGE",
    option_state="PROPOSED",
    option_holder="GMCA; Innovate UK",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Stage 3; GM-influenced call programming"))
n += 1

claims_data.append(make_claim(n, "Stage 4 proposed: Enhanced Collaboration Terms (GM-negotiated) with flexible IP frameworks for university partnerships, improved cost recovery rates for supply chain partners, and risk-sharing mechanisms",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="PROCESS_STAGE",
    option_state="PROPOSED",
    option_holder="GMCA; Innovate UK",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Stage 4; GM-negotiated collaboration terms; addresses IP and cost recovery barriers"))
n += 1

claims_data.append(make_claim(n, "Pre-Qualification Service Model proposed: GM-operated pre-qualification gateway to improve success rates through validated business cases",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="SERVICE_MODEL",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Proposed variation 1; ROI: reduced wasted applications, higher quality submissions"))
n += 1

claims_data.append(make_claim(n, "Strategic Call Programming proposed: regular quarterly or six-monthly themed calls aligned to GM strategic priorities to support business planning and collaboration",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="CALL_PROGRAMMING",
    option_state="PROPOSED",
    option_holder="GMCA; Innovate UK",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Proposed variation 2; predictable pipeline supports business planning"))
n += 1

claims_data.append(make_claim(n, "Enhanced Collaboration Terms proposed: large company cost recovery increased to 65-75% for GM ecosystem projects and flexible IP frameworks assuming SME first-position IP ownership",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="COLLABORATION_TERMS",
    option_state="PROPOSED",
    option_holder="GMCA; Innovate UK",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Proposed variation 3; addresses supply chain and IP barriers directly"))
n += 1

claims_data.append(make_claim(n, "Phase 1 pilot proposed: 6 months, Advanced Manufacturing and Materials focus, 20 SMEs through pre-qualification process, with baseline metrics for application success rates and collaboration formation",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="PILOT_PHASE",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Phase 1 of 3-phase implementation; pilot approach with clear metrics"))
n += 1

claims_data.append(make_claim(n, "Phase 2 proposed: 12 months, expanding to Life Sciences and Green Tech, with university IP framework pilots and supply chain collaboration incentives",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="EXPANSION_PHASE",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Phase 2; sector expansion"))
n += 1

claims_data.append(make_claim(n, "Phase 3 proposed: 18 months, performance data collated to make case for full devolved authority, demonstrated ROI and ecosystem impact, scalable model for other Combined Authorities",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="DEVOLUTION_PHASE",
    option_state="PROPOSED",
    option_holder="GMCA; Innovate UK",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Phase 3; full devolution case; scalable model"))
n += 1

claims_data.append(make_claim(n, "KPI targets proposed: application success rate improvement 35% to 60%, dropout reduction 25%, time-to-funding reduction 25%, new ecosystem collaboration index metric",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="PERFORMANCE_METRICS",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    value_status="MONETARY", value_basis="SCENARIO_ESTIMATE",
    notes="KPIs for devolved approach; process efficiency, economic impact, and strategic alignment metrics"))
n += 1

claims_data.append(make_claim(n, "Negotiation strategy with Innovate UK proposed: GM as innovation funding laboratory, pilot approach with clear success metrics, scalable model for other Combined Authorities, reduced administrative burden through local pre-qualification",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="NEGOTIATION_STRATEGY",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Negotiation positioning; builds on existing GMCA-Innovate UK MOU"))
n += 1

# === OPTION CLAIMS ===
claims_data.append(make_claim(n, "Devolved funding variations proposed as better way to improve outcomes, building on existing MOU between GMCA and Innovate UK and increasing devolution of authority for R&D investment",
    "DESIGN", "OPTION", method_ids=M_OPTIONS,
    option_subtype="DEVOLUTION_OPTION",
    option_state="PROPOSED",
    option_holder="GMCA",
    exercise_access="NEGOTIATED_DECISION",
    outcome_status="PROPOSED",
    notes="Strategic option; devolution as mechanism for process improvement; not yet implemented"))
n += 1

# === BID_SUPPORT_DELIVERED ===
claims_data.append(make_claim(n, "Fifth Sector co-delivered innovation funding support workshop with MMU bringing together GMCA, Growth Hub, universities, and businesses for practical bid writing guidance",
    "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", method_ids=M_WORKSHOP,
    outcome_status="DELIVERED",
    notes="Workshop delivered December 2024; co-delivery with MMU; Steve Hillier and Caroline leading from MMU side"))
n += 1

# Generate evidence links
evidence_data = []
ev_n = NEXT_EVIDENCE

def make_evidence(ev_num, claim_id, source_id, locator, extract, supports="SUPPORTS", etype="quantitative", limitations="", notes=""):
    eid = f"E-G2-{ev_num:03d}"
    return {
        "evidence_id": eid, "claim_id": claim_id, "source_id": source_id,
        "source_locator": locator, "extract_or_observation": extract,
        "supports_or_contradicts": supports, "evidence_type": etype,
        "limitations": limitations, "reviewer": "Devin",
        "review_date": "2026-09-12", "notes": notes,
        "original_locator": locator,
        "derived_locator": f"extracted_text/{source_id}_v1_full.txt",
        "source_family_id": "FGTG-FAM", "source_review_state": "REVIEWED",
        "codebook_version": CODEBOOK, "review_batch": REVIEW_BATCH,
    }

for claim in claims_data:
    cid = claim["claim_id"]
    prop = claim["precise_proposition"]
    
    # Determine source
    if "Phase" in prop and ("pilot" in prop.lower() or "expansion" in prop.lower() or "devolution" in prop.lower()):
        source = "SRC-R3-02"
        locator = "Implementation Framework"
    elif "Stage" in prop and "proposed" in prop.lower():
        source = "SRC-R3-02"
        locator = "Proposed GM-Specific Process Framework"
    elif "KPI" in prop or "Negotiation strategy" in prop or "Devolved funding" in prop:
        source = "SRC-R3-02"
        locator = "KPIs/Negotiation Strategy"
    elif "Pre-Qualification Service" in prop or "Strategic Call Programming" in prop or "Enhanced Collaboration Terms" in prop:
        source = "SRC-R3-02"
        locator = "Business case for GMCA to vary delivery"
    elif "Three critical" in prop:
        source = "SRC-R3-02"
        locator = "Underlying Process Gaps"
    elif "MMU aims" in prop or "Innovate UK and Innovate Edge" in prop:
        source = "SRC-R2-03"
        locator = "briefing note discussion"
    elif "Two businesses" in prop or "8-10" in prop or "50-50" in prop:
        source = "SRC-R2-03"
        locator = "workshop planning discussion"
    elif "co-delivered" in prop or "Fifth Sector co-delivered" in prop:
        source = "SRC-R3-01"
        locator = "Summary"
    elif "practical bid writing" in prop.lower() or "ecosystem collaboration" in prop.lower() or "slide sharing" in prop.lower():
        source = "SRC-R3-01"
        locator = "Key Strengths and Successes"
    elif "IP policies" in prop or "supply chain collaboration barrier" in prop or "50% cost recovery" in prop:
        source = "SRC-R3-01"
        locator = "Critical challenges"
    elif "timing mismatch" in prop or "Technical and presentation" in prop or "Business attendance" in prop:
        source = "SRC-R3-01"
        locator = "Critical challenges"
    elif "Universities perceived" in prop or "breakout groups" in prop or "real-world case studies" in prop or "post-workshop application" in prop:
        source = "SRC-R3-01"
        locator = "Next steps/Sectoral analysis"
    else:
        source = "SRC-R3-01"
        locator = "full report"
    
    etype = "quantitative" if any(c in prop for c in ["£","%","20 ","35%","50%","60%","65%","75%","25%"]) else "qualitative"
    ev = make_evidence(ev_n, cid, source, locator, prop[:200] + ("..." if len(prop) > 200 else ""),
        etype=etype, limitations="Participant self-report" if "EFFECT" in claim["claim_type"] else "",
        notes=f"Evidence for {cid}")
    evidence_data.append(ev)
    ev_n += 1

# Write claims
claims_file = os.path.join(TOOLKIT_DIR, "04_claims.csv")
with open(claims_file, "a") as f:
    for claim in claims_data:
        row = []
        for col in ["claim_id","project_id","precise_proposition","effect_family","mechanism","option_subtype","originator","recipient","intended_beneficiary_status","event_period","claim_direction","outcome_status","attribution_strength","value_status","boundary_recipient","boundary_org","boundary_sector","boundary_geography","boundary_chain","compensation","intent","timing","direction","beneficiaries","cost_bearers","access_barriers","evidence_sufficiency","source_quality","independence","coverage","time_lag","contrary_evidence","reviewer_confidence","commercial_reuse","fifth_sector_role","review_status","publication_status","notes","claim_type","method_ids","generating_intervention","fifth_sector_contribution","contracting_role","tie_change","option_state","option_holder","exercise_access","prediction","rival_explanations","disconfirming_evidence","observation_window","source_review_state","value_basis","value_review_status","permission_status","rights_status","consent_status","causal_assumptions","codebook_version","review_batch"]:
            val = claim.get(col, "")
            if "," in str(val) or '"' in str(val) or "\n" in str(val):
                val = str(val).replace('"', '""')
                val = f'"{val}"'
            row.append(str(val))
        f.write(",".join(row) + "\n")

# Write evidence links
evidence_file = os.path.join(TOOLKIT_DIR, "05_evidence_links.csv")
with open(evidence_file, "a") as f:
    for ev in evidence_data:
        row = []
        for col in ["evidence_id","claim_id","source_id","source_locator","extract_or_observation","supports_or_contradicts","evidence_type","limitations","reviewer","review_date","notes","original_locator","derived_locator","source_family_id","source_review_state","codebook_version","review_batch"]:
            val = ev.get(col, "")
            if "," in str(val) or '"' in str(val) or "\n" in str(val):
                val = str(val).replace('"', '""')
                val = f'"{val}"'
            row.append(str(val))
        f.write(",".join(row) + "\n")

print(f"Added {len(claims_data)} claims for {PROJECT_ID}")
print(f"Added {len(evidence_data)} evidence links")
print(f"Claim IDs: C-G2-{NEXT_CLAIM:03d} to C-G2-{NEXT_CLAIM + len(claims_data) - 1:03d}")
print(f"Evidence IDs: E-G2-{NEXT_EVIDENCE:03d} to E-G2-{NEXT_EVIDENCE + len(evidence_data) - 1:03d}")
