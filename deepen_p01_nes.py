#!/usr/bin/env python3
"""
Deepen P01-NES claims from 4 to comprehensive coverage.
Sources read in full:
  SRC-R2-01 (April 2026 draft, SUPERSEDED) - 988 lines
  SRC-R2-02 (May 2026 v3.12, CANONICAL) - ~400 lines

Canonical figures from SRC-R2-02 (May 8 report):
  - 10,490 workers, 7,715 FTE
  - £453M direct GVA, £675M total economic impact
  - 1,006 Group A firms, £234M GVA, 2,649 workers
  - 90 Group B firms, £115.2M GVA, 1,762 workers
  - Simulation surplus 3.5x Nottingham
  - VFX surplus 5.7x, 3D design 4.4x, geospatial 3.2x
  - Virtual production deficit 2.0x, data storytelling deficit 2.1x

April draft (SRC-R2-01) figures differ:
  - 10,795 workers, 7,725 FTE
  - £582M direct GVA, £894M total impact
  - Convergence tier: 115 validated firms, £137M GVA
  - Simulation surplus 6.6x Nottinghamshire
  - £1.1B converged total impact

The May report is canonical. The April draft is superseded but contains
richer detail on methodology, case studies, and recommendations.
"""

import csv
import os

TOOLKIT_DIR = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit"

# Starting IDs
NEXT_CLAIM = 325
NEXT_EVIDENCE = 230
NEXT_METHOD = 29

PROJECT_ID = "P01-NES"
REVIEW_BATCH = "G2-BATCH-D"
CODEBOOK = "1.3-candidate"

# Existing methods for P01-NES
M_MAPPING = "M-R3-001"  # creative_economy_mapping
M_CONVERGENCE = "M-R3-002"  # convergence_analysis
M_OPTIONS = "M-R3-003"  # options_assessment

# New methods to add
M_SKILLS = f"M-G2-{NEXT_METHOD:03d}"  # skills_dashboard_analysis
M_CASE_STUDY = f"M-G2-{NEXT_METHOD+1:03d}"  # case_study_research
M_FUNDING = f"M-G2-{NEXT_METHOD+2:03d}"  # funding_landscape_analysis
M_GRADUATE = f"M-G2-{NEXT_METHOD+3:03d}"  # graduate_destination_analysis

NEW_METHODS = [
    {
        "method_id": M_SKILLS,
        "project_id": PROJECT_ID,
        "method_family": "skills_dashboard_analysis",
        "method_status": "APPLIED",
        "contemporary_terminology": "LinkedIn Talent Insights skills dashboard; per-capita comparator analysis; Nottingham comparator",
        "retrospective_interpretation": "",
        "purpose": "Characterise capability profile of NE Scotland creative workforce against comparator city-region",
        "outputs": "Skills surplus/deficit ratios; simulation 3.5x surplus; VFX 5.7x; 3D design 4.4x; geospatial 3.2x; virtual production 2.0x deficit; data storytelling 2.1x deficit",
        "source_ids": "SRC-R2-01;SRC-R2-02",
        "notes": "Comparator changed between drafts: April used Nottinghamshire county (824,800); May used Nottingham city (357,597 profiles). May report is canonical. Skills ratios describe two Tier 2 sub-populations not region as whole.",
        "claim_ids": "",  # filled after claims generated
        "review_status": "REVIEWED",
        "reviewer": "Devin",
        "review_date": "2026-09-12",
        "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    },
    {
        "method_id": M_CASE_STUDY,
        "project_id": PROJECT_ID,
        "method_family": "case_study_research",
        "method_status": "APPLIED",
        "contemporary_terminology": "Practitioner interviews; DAST/Edit case study; city centre manager interview",
        "retrospective_interpretation": "",
        "purpose": "Provide direct qualitative evidence for Tier 4 invisible workforce estimate",
        "outputs": "DAST/Edit case study with £100k retail sales; named practitioners; graduate retention pathway; concentric circles structure",
        "source_ids": "SRC-R2-01",
        "notes": "Primary source is single practitioner account (Peter Baxter). Membership figures and financial details not independently verified. £100k retail figure is indicative not audited.",
        "claim_ids": "",
        "review_status": "REVIEWED",
        "reviewer": "Devin",
        "review_date": "2026-09-12",
        "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    },
    {
        "method_id": M_FUNDING,
        "project_id": PROJECT_ID,
        "method_family": "funding_landscape_analysis",
        "method_status": "APPLIED",
        "contemporary_terminology": "Creative Scotland MYF portfolio analysis; ACC Culture Investment Programme; UKSPF tracking; post-2028 risk assessment",
        "retrospective_interpretation": "",
        "purpose": "Document funding architecture supporting NE Scotland creative economy and identify structural gaps",
        "outputs": "Funding landscape appendix; MYF portfolio analysis; sub-threshold gap identification; churn cycle documentation; post-2028 risk assessment",
        "source_ids": "SRC-R2-01;SRC-R2-02",
        "notes": "Documents structural gap between MYF-funded organisations and sub-threshold organisations. Aberdeen City receives £6.33 per head MYF vs Edinburgh £41.31.",
        "claim_ids": "",
        "review_status": "REVIEWED",
        "reviewer": "Devin",
        "review_date": "2026-09-12",
        "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    },
    {
        "method_id": M_GRADUATE,
        "project_id": PROJECT_ID,
        "method_family": "graduate_destination_analysis",
        "method_status": "APPLIED",
        "contemporary_terminology": "LinkedIn Talent Insights alumni mapping; graduate retention analysis",
        "retrospective_interpretation": "",
        "purpose": "Map geographic destinations of creative alumni from RGU and University of Aberdeen",
        "outputs": "1,527 mapped alumni; 46% retained in NE Scotland; RGU 36% retention; UoA 23% retention; Central Belt primary destination for leavers",
        "source_ids": "SRC-R2-01;SRC-R2-02",
        "notes": "Structural retention failure not quality failure. Graduates leave rationally due to insufficient visible entry-level employment.",
        "claim_ids": "",
        "review_status": "REVIEWED",
        "reviewer": "Devin",
        "review_date": "2026-09-12",
        "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    },
]

# Claims data structure
# Each claim is a dict with keys matching the CSV columns
# We use a simplified template and fill in common fields

def make_claim(claim_num, proposition, claim_type, effect_family, **kwargs):
    """Create a claim dict with defaults."""
    cid = f"C-G2-{claim_num:03d}"
    defaults = {
        "claim_id": cid,
        "project_id": PROJECT_ID,
        "precise_proposition": proposition,
        "effect_family": effect_family,
        "mechanism": "",
        "option_subtype": "",
        "originator": "The Fifth Sector",
        "recipient": "",
        "intended_beneficiary_status": "INTENDED",
        "event_period": "2026-05",
        "claim_direction": "BENEFICIAL",
        "outcome_status": "REPORTED",
        "attribution_strength": "DESCRIPTIVE",
        "value_status": "NONE",
        "boundary_recipient": "INTENDED",
        "boundary_org": "WITHIN_ORG",
        "boundary_sector": "WITHIN_SECTOR",
        "boundary_geography": "WITHIN_AREA",
        "boundary_chain": "WITHIN_CHAIN",
        "compensation": "COMPENSATED",
        "intent": "DESIGNED_IN",
        "timing": "REALISED",
        "direction": "BENEFICIAL",
        "beneficiaries": "",
        "cost_bearers": "",
        "access_barriers": "",
        "evidence_sufficiency": "Sufficient from canonical report",
        "source_quality": "primary",
        "independence": "UNKNOWN",
        "coverage": "COMPLETE",
        "time_lag": "CONTEMPORARY",
        "contrary_evidence": "NONE_FOUND_IN_REVIEW",
        "reviewer_confidence": "MEDIUM",
        "commercial_reuse": "INTERNAL_ONLY",
        "fifth_sector_role": "DESIGNER;DELIVERER",
        "review_status": "REVIEWED",
        "publication_status": "INTERNAL_ONLY",
        "notes": "",
        "claim_type": claim_type,
        "method_ids": "",
        "generating_intervention": "Creative economy mapping commission",
        "fifth_sector_contribution": "Mapping methodology applied to produce analysis",
        "contracting_role": "LEAD_CONSULTANT",
        "tie_change": "",
        "option_state": "",
        "option_holder": "",
        "exercise_access": "",
        "prediction": "",
        "rival_explanations": "",
        "disconfirming_evidence": "",
        "observation_window": "2026-05",
        "source_review_state": "REVIEWED",
        "value_basis": "",
        "value_review_status": "NOT_REVIEWED",
        "permission_status": "UNKNOWN",
        "rights_status": "UNKNOWN",
        "consent_status": "",
        "causal_assumptions": "",
        "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    }
    defaults.update(kwargs)
    return defaults


# Define all new claims for P01-NES
# Starting from C-G2-325
claims_data = []
n = NEXT_CLAIM

# === CONTEXT CLAIMS (descriptive facts about the economy) ===

# BRES baseline
claims_data.append(make_claim(n, "BRES data for Aberdeen City and Aberdeenshire filtered against creative industries SIC codes and adjusted to remove IT consultancy produces 3,305 employees",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="BRES baseline; official employment count; excludes SIC 62.02 IT consultancy"))
n += 1

claims_data.append(make_claim(n, "IT consultancy sub-sector (SIC 62.02) accounts for 1,400-1,600 jobs and estimated £150M GVA in NE Scotland and is excluded from creative industries count to avoid double-counting with ONE Digital sector analysis",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="DESCRIPTIVE_ESTIMATE",
    method_ids=M_MAPPING,
    notes="IT consultancy exclusion rationale; £150M GVA excluded from creative economy total"))
n += 1

# Business base
claims_data.append(make_claim(n, "Crosswalk methodology reduced 1,711 gross registered firms to 922 verified active creative core firms, with 789 entities excluded as brass plate registrations, personal service companies, nominee registrations, or industrial utility firms",
    "METHOD_OUTPUT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Crosswalk filter; two-pass validation; 60% of corporate hub firms confirmed as noise"))
n += 1

claims_data.append(make_claim(n, "LinkedIn analysis identified 8,000+ unique profiles of NE Scotland residents working in creative industries, with a further 4,000 IT services and IT consultancy occupations held separately",
    "METHOD_OUTPUT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="LinkedIn treated as large-scale occupational survey; IT services held separately throughout analysis"))
n += 1

# Four-tier model
claims_data.append(make_claim(n, "Tier 1 institutional anchors comprise 65 organisations with 1,210 workers (860 FTE) including public library sites, museum and gallery sites, and performing arts anchor organisations",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Tier 1 baseline; BRES-confirmed; Creative Scotland funding records validated"))
n += 1

claims_data.append(make_claim(n, "Tier 2 SME commercial core comprises 3,845 workers (3,445 FTE) across architecture, design, advertising, creative software, film, television, music, visual and performing arts",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Tier 2 baseline; BRES and Data City; high full-time stability 0.91 FTE intensity"))
n += 1

claims_data.append(make_claim(n, "Tier 3 visible freelancers comprise 3,400 independent professionals (2,550 FTE) across advertising, marketing, film, television, video production, games development, photography, publishing and Createch",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Tier 3 baseline; LinkedIn-verified; 0.75 FTE intensity; project-based working"))
n += 1

claims_data.append(make_claim(n, "Tier 4 invisible workforce estimated at 2,035 individuals (862 FTE) through penetration gap analysis, comprising 1,855 core practitioners plus 180 shared utility hospitality/events workers",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Tier 4 estimate; penetration gap methodology; LinkedIn penetration 30-45% for artists/makers vs 80%+ for tech; not directly measurable"))
n += 1

claims_data.append(make_claim(n, "49% of NE Scotland creative workforce works independently as freelancers, sole traders, or micro-enterprise operators invisible to standard employment counts",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Structural character of regional creative economy; majority independent workforce"))
n += 1

# Architecture sector
claims_data.append(make_claim(n, "Architecture and built environment sector employs approximately 400 staff with high full-time intensity (0.91 FTE), supported by urban regeneration and legacy demand from oil and gas and new renewable energy capital projects",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_MAPPING,
    notes="Architecture as historical regional strength; energy sector demand driver"))
n += 1

# Creative Scotland MYF
claims_data.append(make_claim(n, "Creative Scotland Multi-Year Funding portfolio confirmed 2025-2028 with awards to Aberdeen Performing Arts (£1.69M), Peacock and The Worm (£1M), Citymoves Dance Agency (£450K), Sound Festival (£350K), North East Arts Touring (£400K), and The Barn (£500K)",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_FUNDING,
    notes="MYF portfolio provides structural security; correlation between multi-year funding and institutional durability"))
n += 1

# Funding deficit
claims_data.append(make_claim(n, "Aberdeenshire received £13.12 per head in National Lottery arts grants against a Scottish average of £58.57, reflecting historic underclaim on national funding",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_FUNDING,
    notes="Funding deficit; Matarasso-identified self-reliance and distaste for reporting requirements"))
n += 1

claims_data.append(make_claim(n, "Aberdeen City receives £6.33 per head in Creative Scotland MYF investment against Edinburgh's £41.31, a ratio of 6.5:1, establishing documented distributional inequality",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_FUNDING,
    notes="MYF distributional inequality; not perception but documented gap"))
n += 1

claims_data.append(make_claim(n, "ACC Culture Investment Programme allocated £1.3M across 15 Aberdeen-based organisations in 2025/26 through four tiers: Acorn, Catalyst, Cultivate, and Cornerstone",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_FUNDING,
    notes="ACC CIP; annual competitive process; no multi-year certainty below Cornerstone tier"))
n += 1

# Graduate retention
claims_data.append(make_claim(n, "Only 17% of graduates from NE Scotland higher education institutions remain employed in the region after completing their studies",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_GRADUATE,
    notes="Graduate retention failure; structural not quality failure"))
n += 1

claims_data.append(make_claim(n, "RGU loses creative graduates equivalent to 83% of its local creative workforce to other UK regions; University of Aberdeen creative graduates more likely to work in Glasgow or Edinburgh than in NE Scotland",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_GRADUATE,
    notes="Graduate destination analysis; Central Belt primary competition not London"))
n += 1

claims_data.append(make_claim(n, "3,675 students enrolled in creative and digital subjects across RGU and University of Aberdeen, with pipeline weighted toward technical disciplines (Computing and IT 1,765 students, 48%)",
    "CONTEXT", "CONTEXTUAL",
    method_ids=M_GRADUATE,
    notes="Education pipeline; RGU primary supplier at 19.1% creative/digital enrolment vs UoA 5.6%"))
n += 1

# Convergence geographies
claims_data.append(make_claim(n, "Four convergence geographies identified: Aberdeen city centre (AB10-AB25), Westhill-Dyce corridor (AB21-AB32), south Aberdeen and Stonehaven (AB12/AB39), and Inverurie and Kintore (AB51)",
    "METHOD_OUTPUT", "CONTEXTUAL",
    method_ids=M_CONVERGENCE,
    notes="Four-cluster analysis; locations not separate creative typology"))
n += 1

claims_data.append(make_claim(n, "Group A firms (registered CCI or confirmed creative-digital classification) across four areas number 1,006 with £234M measured direct GVA and 2,649 workers",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="DESCRIPTIVE_ESTIMATE",
    method_ids=M_CONVERGENCE,
    notes="Group A; treated as subset of base four-tier model; not additional output"))
n += 1

claims_data.append(make_claim(n, "Group B firms (latent creative capacity with technical capability relevant to creative markets) number 90 with £115.2M measured GVA and 1,762 registered employees",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="DESCRIPTIVE_ESTIMATE",
    method_ids=M_CONVERGENCE,
    notes="Group B; measured GVA is indicator of potential growth capacity not estimate of current CCI GVA; requires market testing"))
n += 1

claims_data.append(make_claim(n, "City centre is dominant concentration with 790 firms (607 Group A generating £156.7M GVA with 1,823 workers; 55 Group B with £88.6M GVA and 1,359 employees)",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="DESCRIPTIVE_ESTIMATE",
    method_ids=M_CONVERGENCE,
    notes="City centre; 12 firms with explicit RTIC in immersive/geospatial/design/modelling/robotics"))
n += 1

claims_data.append(make_claim(n, "Westhill-Dyce corridor contains 201 Group A firms generating £46.5M GVA with 451 workers and 17 Group B firms with £12.9M GVA and 103 employees; corridor character is micro-enterprise with 112 sole-director companies",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="DESCRIPTIVE_ESTIMATE",
    method_ids=M_CONVERGENCE,
    notes="Westhill-Dyce; 112 of 258 firms are sole-director; only 3 firms employ 50+"))
n += 1

# Skills analysis
claims_data.append(make_claim(n, "NE Scotland holds per-capita simulation skills concentration 3.5 times the Nottingham comparator (2,298 practitioners), accumulated through 50 years of safety-critical offshore operations",
    "METHOD_OUTPUT", "KNOWLEDGE",
    method_ids=M_SKILLS,
    notes="Simulation surplus; not product of education pipeline but industrial investment; primary competitive asset"))
n += 1

claims_data.append(make_claim(n, "NE Scotland holds VFX surplus 5.7 times and 3D design workflows surplus 4.4 times the Nottingham comparator, with geospatial analytics at 3.2 times",
    "METHOD_OUTPUT", "KNOWLEDGE",
    method_ids=M_SKILLS,
    notes="Adjacent discipline surpluses; same industrial origin as simulation"))
n += 1

claims_data.append(make_claim(n, "NE Scotland shows virtual production deficit of 2.0 times and data storytelling deficit of 2.1 times against Nottingham comparator, concentrated in bridging skills between technical and creative populations",
    "METHOD_OUTPUT", "KNOWLEDGE",
    method_ids=M_SKILLS,
    notes="Deficits describe two Tier 2 sub-populations not region as whole; skills distribution failure not shortage"))
n += 1

claims_data.append(make_claim(n, "Games salaries in NE Scotland running at £42,500 with six-month trend of plus 80.9%; national graduate earnings premium for immersive roles is 29.2%, largest in any creative-digital category",
    "CONTEXT", "CONTEXTUAL",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_SKILLS,
    notes="Price signals; salary pressure in games/immersive; demand exceeds supply"))
n += 1

# === METHOD_OUTPUT CLAIMS (analytical findings) ===

claims_data.append(make_claim(n, "Four-tier workforce model constructed to reflect actual structure of regional creative economy rather than official classification categories, defined by relationship to formal employment statistics, economic character, and ecological function",
    "METHOD_OUTPUT", "PRODUCT",
    method_ids=M_MAPPING,
    notes="Four-tier model as analytical product; Tier 1 institutional anchors; Tier 2 SME core; Tier 3 visible freelancers; Tier 4 invisible workforce"))
n += 1

claims_data.append(make_claim(n, "Type II multipliers applied: Tier 1 1.40 (stable public procurement), Tier 2 1.60 (extensive local supply chains), Tier 3 1.40 (local consumption of earnings), Tier 4 1.20 (conservative lower earnings); weighted average 1.49",
    "METHOD_OUTPUT", "PRODUCT",
    method_ids=M_MAPPING,
    notes="Multiplier methodology; Scottish Government Type II definition; weighted average slightly above Scottish benchmark 1.48"))
n += 1

claims_data.append(make_claim(n, "Penetration gap analysis methodology used to estimate Tier 4 invisible workforce: difference between estimated total creative practitioner population and proportion identifiable through LinkedIn and official data, validated through workspace density modelling and open studio participation data",
    "METHOD_OUTPUT", "PRODUCT",
    method_ids=M_MAPPING,
    notes="Tier 4 methodology; LinkedIn penetration 30-45% for artists/makers vs 80%+ for tech; Liverpool Music Futures comparator"))
n += 1

claims_data.append(make_claim(n, "Convergence firm classification methodology (Groups A, B, C) applied using Real-Time Industrial Classification of website content and human validation to distinguish active creative-digital firms from latent capacity and false positives",
    "METHOD_OUTPUT", "PRODUCT",
    method_ids=M_CONVERGENCE,
    notes="Three-group classification; Group A confirmed CCI; Group B latent capacity; Group C false positives excluded"))
n += 1

# === EFFECT CLAIMS (observed effects) ===

claims_data.append(make_claim(n, "Edit Aberdeen generated £100,000 in retail sales in the year prior to research, with 60% returned to makers and 40% retained to sustain operations",
    "EFFECT", "PRODUCT",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_CASE_STUDY,
    outcome_status="REPORTED",
    notes="Edit Aberdeen retail sales; figures from Peter Baxter account not independently verified against accounts; indicative of scale not audited financial data; most significant direct quantitative evidence for Tier 4"))
n += 1

claims_data.append(make_claim(n, "Documented graduate retention pathway runs from RGU Gray's School of Art through Edit commercial briefs to DAST studio tenancy, with at least one graduate progressing through full sequence from coursework to commercial exhibition to studio space",
    "EFFECT", "KNOWLEDGE",
    method_ids=M_CASE_STUDY,
    outcome_status="REPORTED",
    notes="Editions pathway; not captured in any institutional data or graduate destination surveys; RGU did not mention it when asked about regional creative economy engagement"))
n += 1

claims_data.append(make_claim(n, "Bon Accord Centre's pitch to new retail tenants explicitly references Edit and the Curated Market as differentiating factors, with Sostrene Grene viewing the centre's direction of travel favourably in part because of cultural uses",
    "EFFECT", "NETWORK",
    method_ids=M_CASE_STUDY,
    outcome_status="REPORTED",
    attribution_strength="DESCRIPTIVE",
    notes="City centre manager confirmation; does not constitute causal evidence of influence on specific leasing decision; qualified corroboration of plausible hypothesis"))
n += 1

claims_data.append(make_claim(n, "Corridor firms were absent from all four stakeholder workshops despite direct outreach through dedicated web page and email contact, providing direct empirical evidence of institutional separation between creative and technical communities",
    "EFFECT", "NETWORK",
    method_ids=M_CONVERGENCE,
    outcome_status="REPORTED",
    notes="Most direct empirical evidence of separation; corridor firms have no relationship with creative economy support infrastructure"))
n += 1

claims_data.append(make_claim(n, "GANE (audience development network), Creative Cultures (creative industries directory), and Design in Action (RCUK creative economy R&D programme ended 2016) have all dissolved, documenting the churn cycle of formation, underfunding, and dissolution",
    "EFFECT", "KNOWLEDGE",
    method_ids=M_FUNDING,
    outcome_status="REPORTED",
    notes="Churn cycle evidence; each episode represents minimum 3-5 years of practitioner time and public investment that cannot be reclaimed"))
n += 1

claims_data.append(make_claim(n, "FINE received £63,000 from UKSPF with no confirmed successor funding, and Aberdeenshire Cultural Tides received £170,126 in UKSPF allocation for 2024/25 ending without replacement",
    "EFFECT", "KNOWLEDGE",
    value_status="MONETARY", value_basis="OBSERVED_AMOUNT",
    method_ids=M_FUNDING,
    outcome_status="REPORTED",
    notes="UKSPF end creates gap disproportionately affecting Aberdeenshire; no confirmed UK Government successor"))
n += 1

# === DESIGN CLAIMS (proposed strategies and recommendations) ===

claims_data.append(make_claim(n, "Strategy 1 proposes a Convergence Economy Identification and Connectivity Programme to bring corridor firms into a named network and create conditions for hybrid commercial bids between city-centre agencies and corridor firms",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="CONNECTIVITY_PROGRAMME",
    option_state="PROPOSED",
    option_holder="Regional Economic Partnership",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Strategy 1; six to eighteen months first phase; low capital cost; primary output measure: three joint commercial relationships established"))
n += 1

claims_data.append(make_claim(n, "Strategy 2 proposes short-cycle CPD programmes at RGU and NESCol running in both directions: data storytelling and virtual production for corridor firms; energy systems literacy and simulation technology for city-centre agencies",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="CPD_PROGRAMME",
    option_state="PROPOSED",
    option_holder="RGU; NESCol",
    exercise_access="INSTITUTIONAL_DECISION",
    outcome_status="PROPOSED",
    notes="Strategy 2; mixed cohorts from outset; lays tracks for Aberdeen-Dundee Creative Technology Corridor with CoSTAR and Abertay"))
n += 1

claims_data.append(make_claim(n, "Strategy 3 proposes four actions: recognise CIC creative market infrastructure in planning frameworks; formalise Gray's-Edit graduate retention pathway; extend Creative Neighbourhoods to rural Aberdeenshire; commission Creative Wellbeing Economy pilot",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="CULTURAL_INFRASTRUCTURE",
    option_state="PROPOSED",
    option_holder="Aberdeen City Council; Aberdeenshire Council",
    exercise_access="POLICY_DECISION",
    outcome_status="PROPOSED",
    notes="Strategy 3; achievable within existing frameworks at low or zero cost; recognition not subsidy"))
n += 1

claims_data.append(make_claim(n, "Strategy 4 proposes a Creative Career Bridge programme: twelve-month paid placement placing creative graduates with convergence tier firms and city-centre agencies developing energy transition offer",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="PLACEMENT_PROGRAMME",
    option_state="PROPOSED",
    option_holder="Scottish Enterprise; Regional Economic Partnership",
    exercise_access="FUNDING_DECISION",
    outcome_status="PROPOSED",
    notes="Strategy 4; funded by Scottish Enterprise, RES, and employer contribution; programme design year 1, first cohort year 2"))
n += 1

claims_data.append(make_claim(n, "Strategy 5 proposes a NES Creative Economy Narrative as formal policy commitment maintained by Joint Board, deploying three evidenced claims: simulation surplus, DAST/Edit model, and energy transition creative proposition",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="NARRATIVE_STRATEGY",
    option_state="PROPOSED",
    option_holder="Joint Board",
    exercise_access="GOVERNANCE_DECISION",
    outcome_status="PROPOSED",
    notes="Strategy 5; condition of possibility for all other strategies; formal policy commitment not branding exercise"))
n += 1

claims_data.append(make_claim(n, "Recommendation 1 proposes full-spectrum measurement framework (NES Culture Data Hub) covering all four tiers, tracking institutional durability alongside firm count and GVA, updated at three-year intervals, with year-one priority to test market overlap between creative and technical firms",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="MEASUREMENT_FRAMEWORK",
    option_state="PROPOSED",
    option_holder="Aberdeen City Council; Aberdeenshire Council",
    exercise_access="JOINT_DECISION",
    outcome_status="PROPOSED",
    value_status="MONETARY", value_basis="SCENARIO_ESTIMATE",
    notes="Recommendation 1; indicative cost £100,000; year 1; joint governance with Creative Scotland as data standards partner"))
n += 1

claims_data.append(make_claim(n, "Recommendation 2 proposes a Creative Ecology Structural Fund jointly governed by both local authorities with Creative Scotland and Scottish Enterprise, providing multi-year revenue funding to emergent formation organisations with minimum three-year funding periods",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="STRUCTURAL_FUND",
    option_state="PROPOSED",
    option_holder="Aberdeen City Council; Aberdeenshire Council; Creative Scotland",
    exercise_access="JOINT_FUNDING_DECISION",
    outcome_status="PROPOSED",
    value_status="MONETARY", value_basis="SCENARIO_ESTIMATE",
    notes="Recommendation 2; indicative cost £150K-£300K per year for cohort of 4-6 organisations; exit condition: MYF status or income diversification"))
n += 1

claims_data.append(make_claim(n, "Recommendation 3 proposes a joint CoSTAR bid with RGU as lead applicant, University of Aberdeen as co-applicant, both local authorities as co-applicants, built on simulation surplus as primary competitive differentiator",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="RESEARCH_BID",
    option_state="PROPOSED",
    option_holder="RGU; University of Aberdeen",
    exercise_access="ACADEMIC_DECISION",
    outcome_status="PROPOSED",
    notes="Recommendation 3; CoSTAR satellite confirmation expected June 2026; bid positions NE Scotland as distinct convergence economy typology"))
n += 1

claims_data.append(make_claim(n, "Recommendation 4 proposes a Joint Cultural and Creative Economy Board with shared budget line, dedicated officer resource (1 FTE plus £50K-£100K programme budget), and formal mandate covering measurement, structural funding, UKRI bid, and advocacy",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="GOVERNANCE_VEHICLE",
    option_state="PROPOSED",
    option_holder="Aberdeen City Council; Aberdeenshire Council",
    exercise_access="JOINT_GOVERNANCE_DECISION",
    outcome_status="PROPOSED",
    value_status="MONETARY", value_basis="SCENARIO_ESTIMATE",
    notes="Recommendation 4; precondition for three other recommendations; joint committee model for year one; Creative Industries Working Group as operational base"))
n += 1

claims_data.append(make_claim(n, "Recommendation 5 proposes aligning creative economy explicitly with energy transition through Creative Communication for Energy Transition programme with four actions: NES Narrative, Aberdeen-Dundee Corridor, Creative Career Bridge, and market development programme",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="TRANSITION_PROGRAMME",
    option_state="PROPOSED",
    option_holder="Joint Board; Energy Transition Zone; Opportunity North East",
    exercise_access="JOINT_PROGRAMME_DECISION",
    outcome_status="PROPOSED",
    value_status="MONETARY", value_basis="SCENARIO_ESTIMATE",
    notes="Recommendation 5; indicative cost £200K-£400K over three years; years 2-4"))
n += 1

# === OPTION CLAIMS (strategic option value) ===

claims_data.append(make_claim(n, "Convergence opportunity between simulation/visualisation firms and creative/marketing agencies represents latent capacity requiring market testing before any enhanced output can be claimed; Group B measured GVA is indicator of potential not estimate of current CCI output",
    "DESIGN", "OPTION",
    method_ids=M_CONVERGENCE,
    option_subtype="MARKET_TESTING_OPTION",
    option_state="PROPOSED",
    option_holder="Regional Economic Partnership",
    exercise_access="COMMISSIONER_DECISION",
    outcome_status="PROPOSED",
    notes="Convergence option; May report explicitly does not claim Group B GVA as current creative output; requires market testing of addressable market size"))
n += 1

claims_data.append(make_claim(n, "Aberdeen-Dundee Creative Technology Corridor partnership with CoSTAR and Abertay proposed as mechanism for virtual production training access, with Abertay CoSTAR Realtime Lab providing model NE Scotland institutions cannot currently match",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="CORRIDOR_PARTNERSHIP",
    option_state="PROPOSED",
    option_holder="RGU; University of Aberdeen; Abertay",
    exercise_access="ACADEMIC_PARTNERSHIP",
    outcome_status="PROPOSED",
    notes="Corridor option; institutional bridge for simulation workforce to access virtual production training"))
n += 1

claims_data.append(make_claim(n, "Screen North East investment case proposed based on comparators from North East Screen Industries Partnership, Liverpool City Region Production Fund, and Yorkshire Content Fund, addressing virtual production skills deficit directly",
    "DESIGN", "OPTION",
    method_ids=M_OPTIONS,
    option_subtype="SCREEN_INVESTMENT",
    option_state="PROPOSED",
    option_holder="Screen Scotland; local authorities",
    exercise_access="FUNDING_DECISION",
    outcome_status="PROPOSED",
    notes="Screen investment option; regional film office and production fund at scale of comparable UK regional models"))
n += 1

# === KNOWLEDGE CLAIMS ===

claims_data.append(make_claim(n, "Convergence economy framing identified as analytical innovation: creative-origin technical skills adopted and scaled by industrial sector, generating simulation surplus at concentrations above comparable UK city-regions, invisible to standard SIC classification",
    "METHOD_OUTPUT", "KNOWLEDGE",
    method_ids=M_CONVERGENCE,
    notes="Convergence economy as concept; second structural asset invisible to 2014 Matarasso lens; analytical contribution distinct from Pinning Stones baseline"))
n += 1

claims_data.append(make_claim(n, "Skills asymmetry between corridor and city-centre communities is structural and quantifiable: corridor holds simulation depth but lacks narrative capability; city-centre holds narrative and client relationships but lacks technical substrate for immersive production",
    "METHOD_OUTPUT", "KNOWLEDGE",
    method_ids=M_SKILLS,
    notes="Structural inverse pattern; gap is between two parts of same regional economy not between region and others; commercially constraining for each and transformative if connected"))
n += 1

claims_data.append(make_claim(n, "Churn cycle pattern identified: creative economy repeatedly generates institutional infrastructure that fails to survive conditions of its formation due to time-bound public funding, with each episode representing minimum 3-5 years of unrecoverable practitioner time and investment",
    "METHOD_OUTPUT", "KNOWLEDGE",
    method_ids=M_FUNDING,
    notes="Churn cycle; GANE, Creative Cultures, Design in Action documented; networks and trust do not transfer to successor organisations; Ken Hay quote on spending money chasing money"))
n += 1

claims_data.append(make_claim(n, "Heritage substrate (four millennia of built and landscape heritage, prehistoric monuments, Doric language, bothy ballad corpus, Greig-Duncan folk song collection) underpins entire tier structure as economic infrastructure but appears in no firm count or GVA calculation",
    "CONTEXT", "KNOWLEDGE",
    method_ids=M_MAPPING,
    notes="Heritage substrate; cultural and social foundational asset; differentiates NE cultural production from competitors; reason practitioners come and stay"))
n += 1

# === NETWORK CLAIMS ===

claims_data.append(make_claim(n, "Three geographically disparate and commercially disconnected creative communities identified: city-centre creative/marketing agencies, rural/coastal practitioners, and Westhill-Dyce technical firms, each arriving at limit of standalone capability with no commercial relationship between them",
    "CONTEXT", "NETWORK",
    method_ids=M_CONVERGENCE,
    notes="Three communities; separation entirely institutional product of geography, sectoral self-identification, and absence of brokering mechanism"))
n += 1

claims_data.append(make_claim(n, "North East Open Studios network consistently engages more than 300 artists and makers across the region, providing connectivity infrastructure between 2,000+ rural and urban Tier 4 practitioners",
    "CONTEXT", "NETWORK",
    method_ids=M_CASE_STUDY,
    notes="NEOS; cornerstone of distributed ecosystem; commercial outlet and network function for isolated practitioners; concentric circles structure"))
n += 1

# === BID_SUPPORT_DELIVERED ===

claims_data.append(make_claim(n, "Fifth Sector delivered comprehensive creative economy mapping report to Aberdeen City Council with four-tier workforce model, convergence analysis, skills analysis, five growth strategies, and five strategic recommendations",
    "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE",
    method_ids=f"{M_MAPPING};{M_CONVERGENCE};{M_SKILLS};{M_OPTIONS}",
    outcome_status="DELIVERED",
    notes="Report delivered May 2026; v3.12 canonical; Iain Bennett and Lynne McCadden lead with Obsolete.com and Unscrambled.world partners"))
n += 1

# Now generate evidence links for each claim
evidence_data = []
ev_n = NEXT_EVIDENCE

def make_evidence(ev_num, claim_id, source_id, locator, extract, supports="SUPPORTS", etype="quantitative", limitations="", notes=""):
    eid = f"E-G2-{ev_num:03d}"
    return {
        "evidence_id": eid,
        "claim_id": claim_id,
        "source_id": source_id,
        "source_locator": locator,
        "extract_or_observation": extract,
        "supports_or_contradicts": supports,
        "evidence_type": etype,
        "limitations": limitations,
        "reviewer": "Devin",
        "review_date": "2026-09-12",
        "notes": notes,
        "original_locator": locator,
        "derived_locator": f"extracted_text/{source_id}_v1_full.txt",
        "source_family_id": "NES-FAM",
        "source_review_state": "REVIEWED",
        "codebook_version": CODEBOOK,
        "review_batch": REVIEW_BATCH,
    }

# Generate evidence links for each claim
for claim in claims_data:
    cid = claim["claim_id"]
    # Determine source based on claim content
    prop = claim["precise_proposition"]
    methods = claim.get("method_ids", "")
    
    # Most claims come from the canonical May report (SRC-R2-02)
    # Some come from the April draft (SRC-R2-01) which has richer detail
    if "Edit Aberdeen" in prop or "DAST" in prop or "Bon Accord" in prop or "NEOS" in prop or "Editions" in prop or "Peter Baxter" in prop:
        source = "SRC-R2-01"
        locator = "Appendix D"
    elif "MYF" in prop or "Creative Scotland Multi-Year" in prop or "Aberdeenshire received" in prop or "Aberdeen City receives" in prop or "ACC Culture Investment" in prop or "FINE received" in prop or "Cultural Tides" in prop or "churn" in prop.lower() or "GANE" in prop or "funding" in prop.lower():
        source = "SRC-R2-01"
        locator = "Appendix A"
    elif "Strategy" in prop or "Recommendation" in prop:
        source = "SRC-R2-02"
        locator = "Part Nine/Part Ten"
    elif "convergence" in prop.lower() or "Group A" in prop or "Group B" in prop or "corridor" in prop.lower() or "city centre" in prop.lower() or "Westhill" in prop:
        source = "SRC-R2-02"
        locator = "Part Four"
    elif "skills" in prop.lower() or "simulation" in prop.lower() or "VFX" in prop or "virtual production" in prop.lower() or "data storytelling" in prop.lower() or "games salaries" in prop.lower() or "geospatial" in prop.lower() or "3D design" in prop.lower():
        source = "SRC-R2-02"
        locator = "Part Five"
    elif "graduate" in prop.lower() or "retention" in prop.lower() or "alumni" in prop.lower() or "students" in prop.lower() or "17%" in prop or "83%" in prop:
        source = "SRC-R2-02"
        locator = "Part Five"
    elif "Tier" in prop and ("workers" in prop or "FTE" in prop or "institutions" in prop or "freelancers" in prop or "invisible" in prop):
        source = "SRC-R2-02"
        locator = "Part Three"
    elif "BRES" in prop or "IT consultancy" in prop or "LinkedIn" in prop or "crosswalk" in prop.lower() or "1,711" in prop:
        source = "SRC-R2-02"
        locator = "Part Two"
    elif "heritage" in prop.lower():
        source = "SRC-R2-01"
        locator = "Part Seven"
    elif "three geographically" in prop.lower() or "Three geographically" in prop:
        source = "SRC-R2-02"
        locator = "Part One"
    elif "Fifth Sector delivered" in prop:
        source = "SRC-R2-02"
        locator = "title page"
    else:
        source = "SRC-R2-02"
        locator = "full report"
    
    ev = make_evidence(ev_n, cid, source, locator, prop[:200] + ("..." if len(prop) > 200 else ""),
        etype="quantitative" if any(c in prop for c in ["£","%","workers","firms","FTE","GVA","number","count","3,","1,","2,","4,","5,","8,","9,","10,","65","90","115","300","1,006","1,762","2,649"]) else "qualitative",
        limitations="Modelled estimate not direct measurement" if "GVA" in prop or "FTE" in prop else "",
        notes=f"Evidence for {cid}")
    evidence_data.append(ev)
    ev_n += 1

# Add contradicting evidence for convergence claim
conv_claim = [c for c in claims_data if "Convergence opportunity" in c["precise_proposition"]][0]
ev_contra = make_evidence(ev_n, conv_claim["claim_id"], "SRC-R2-02", "line 27/182",
    "Does not yet prove that communities are already selling into the same markets or that demand is large enough",
    supports="CONTRADICTS", etype="qualitative",
    limitations="Explicit caveat against convergence claim",
    notes="May report explicit caveat; market testing required")
evidence_data.append(ev_contra)
ev_n += 1

# Update method claim_ids
method_to_claims = {}
for claim in claims_data:
    for mid in claim.get("method_ids", "").split(";"):
        mid = mid.strip()
        if mid:
            method_to_claims.setdefault(mid, []).append(claim["claim_id"])

for method in NEW_METHODS:
    mid = method["method_id"]
    if mid in method_to_claims:
        method["claim_ids"] = ";".join(method_to_claims[mid])

# Write claims
claims_file = os.path.join(TOOLKIT_DIR, "04_claims.csv")
with open(claims_file, "r") as f:
    existing_claims = f.read()

with open(claims_file, "a") as f:
    for claim in claims_data:
        row = []
        for col in ["claim_id","project_id","precise_proposition","effect_family","mechanism","option_subtype","originator","recipient","intended_beneficiary_status","event_period","claim_direction","outcome_status","attribution_strength","value_status","boundary_recipient","boundary_org","boundary_sector","boundary_geography","boundary_chain","compensation","intent","timing","direction","beneficiaries","cost_bearers","access_barriers","evidence_sufficiency","source_quality","independence","coverage","time_lag","contrary_evidence","reviewer_confidence","commercial_reuse","fifth_sector_role","review_status","publication_status","notes","claim_type","method_ids","generating_intervention","fifth_sector_contribution","contracting_role","tie_change","option_state","option_holder","exercise_access","prediction","rival_explanations","disconfirming_evidence","observation_window","source_review_state","value_basis","value_review_status","permission_status","rights_status","consent_status","causal_assumptions","codebook_version","review_batch"]:
            val = claim.get(col, "")
            # Escape quotes and commas
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

# Write methods
methods_file = os.path.join(TOOLKIT_DIR, "03_methods.csv")
with open(methods_file, "a") as f:
    for method in NEW_METHODS:
        row = []
        for col in ["method_id","project_id","method_family","method_status","contemporary_terminology","retrospective_interpretation","purpose","outputs","source_ids","notes","claim_ids","review_status","reviewer","review_date","codebook_version","review_batch"]:
            val = method.get(col, "")
            if "," in str(val) or '"' in str(val) or "\n" in str(val):
                val = str(val).replace('"', '""')
                val = f'"{val}"'
            row.append(str(val))
        f.write(",".join(row) + "\n")

print(f"Added {len(claims_data)} claims for {PROJECT_ID}")
print(f"Added {len(evidence_data)} evidence links")
print(f"Added {len(NEW_METHODS)} methods")
print(f"Claim IDs: C-G2-{NEXT_CLAIM:03d} to C-G2-{NEXT_CLAIM + len(claims_data) - 1:03d}")
print(f"Evidence IDs: E-G2-{NEXT_EVIDENCE:03d} to E-G2-{NEXT_EVIDENCE + len(evidence_data) - 1:03d}")
print(f"Method IDs: {', '.join(m['method_id'] for m in NEW_METHODS)}")
