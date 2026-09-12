#!/usr/bin/env python3
"""
Deepen P03-MITIH, P05-WMCA, P06-COSTAR, P07-CC, P09-CDEC in one batch.
All sources read in full.

P03-MITIH: SRC-R2-04 (Createch ecosystem report, Oct 2025, recommendations rejected)
P05-WMCA: SRC-R2-06 (WMCA scale-up mapping, Jan 2020, BOP with Fifth Sector sub)
P06-COSTAR: SRC-R2-07 (CoSTAR bid support, Jan 2023, bid NOT successful)
P07-CC: SRC-R2-08 (Creative City inception, Sep 2020, application NOT successful)
P09-CDEC: SRC-R2-10 (CDEC challenges paper, Apr 2012, advisory role)
"""

import csv
import os

TOOLKIT_DIR = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit"

NEXT_CLAIM = 412
NEXT_EVIDENCE = 318

REVIEW_BATCH = "G2-BATCH-D"
CODEBOOK = "1.3-candidate"

def make_claim(claim_num, project_id, proposition, claim_type, effect_family, event_period, **kwargs):
    cid = f"C-G2-{claim_num:03d}"
    defaults = {
        "claim_id": cid, "project_id": project_id,
        "precise_proposition": proposition, "effect_family": effect_family,
        "mechanism": "", "option_subtype": "", "originator": "The Fifth Sector",
        "recipient": "", "intended_beneficiary_status": "INTENDED",
        "event_period": event_period, "claim_direction": "BENEFICIAL",
        "outcome_status": "REPORTED", "attribution_strength": "DESCRIPTIVE",
        "value_status": "NONE", "boundary_recipient": "INTENDED",
        "boundary_org": "WITHIN_ORG", "boundary_sector": "WITHIN_SECTOR",
        "boundary_geography": "WITHIN_AREA", "boundary_chain": "WITHIN_CHAIN",
        "compensation": "COMPENSATED", "intent": "DESIGNED_IN",
        "timing": "REALISED", "direction": "BENEFICIAL",
        "beneficiaries": "", "cost_bearers": "", "access_barriers": "",
        "evidence_sufficiency": "Sufficient from source",
        "source_quality": "primary", "independence": "UNKNOWN",
        "coverage": "COMPLETE", "time_lag": "CONTEMPORARY",
        "contrary_evidence": "NONE_FOUND_IN_REVIEW",
        "reviewer_confidence": "MEDIUM", "commercial_reuse": "INTERNAL_ONLY",
        "fifth_sector_role": "DESIGNER;DELIVERER",
        "review_status": "REVIEWED", "publication_status": "INTERNAL_ONLY",
        "notes": "", "claim_type": claim_type, "method_ids": "",
        "generating_intervention": "", "fifth_sector_contribution": "",
        "contracting_role": "", "tie_change": "", "option_state": "",
        "option_holder": "", "exercise_access": "", "prediction": "",
        "rival_explanations": "", "disconfirming_evidence": "",
        "observation_window": event_period, "source_review_state": "REVIEWED",
        "value_basis": "", "value_review_status": "NOT_REVIEWED",
        "permission_status": "UNKNOWN", "rights_status": "UNKNOWN",
        "consent_status": "", "causal_assumptions": "",
        "codebook_version": CODEBOOK, "review_batch": REVIEW_BATCH,
    }
    defaults.update(kwargs)
    return defaults

def make_evidence(ev_num, claim_id, source_id, locator, extract, source_family, supports="SUPPORTS", etype="quantitative", limitations="", notes=""):
    eid = f"E-G2-{ev_num:03d}"
    return {
        "evidence_id": eid, "claim_id": claim_id, "source_id": source_id,
        "source_locator": locator, "extract_or_observation": extract,
        "supports_or_contradicts": supports, "evidence_type": etype,
        "limitations": limitations, "reviewer": "Devin",
        "review_date": "2026-09-12", "notes": notes,
        "original_locator": locator,
        "derived_locator": f"extracted_text/{source_id}_v1_full.txt",
        "source_family_id": source_family, "source_review_state": "REVIEWED",
        "codebook_version": CODEBOOK, "review_batch": REVIEW_BATCH,
    }

all_claims = []
all_evidence = []
n = NEXT_CLAIM
ev_n = NEXT_EVIDENCE

# ============================================================
# P03-MITIH (SRC-R2-04)
# ============================================================
PID = "P03-MITIH"
SRC = "SRC-R2-04"
FAM = "MITIH-FAM"
EP = "2025-10"
M_ECO = "M-R3-007"  # ecosystem_mapping
M_SNA = "M-R3-008"  # social_network_analysis
M_INV = "M-R3-009"  # investment_sequence_design

p03_claims = [
    (n, PID, "Realtime's Virtual Production department operates as integrated team with 3D animators, audio specialists, and studio production crews working on same commercial projects across games, film, and episodic television", "EFFECT", "PRODUCT", EP, {"method_ids": M_ECO, "outcome_status": "REPORTED", "notes": "Proof of concept for convergence; commercial operation delivering paid work"}),
    (n+1, PID, "Immersive-related roles generated 3,847 job postings 2020-2024 in GM, growing from 612 in 2020 to 891 in 2024 (46% increase)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ECO, "value_status": "NONE", "notes": "Job market data confirms convergence is not outlier"}),
    (n+2, PID, "In 2024, 34% of immersive postings requested animation skills, 28% requested audio expertise, and 41% requested studio production experience, confirming cross-sector convergence in employer demand", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_ECO, "notes": "Skills from animation, audio, and studio production appear in same job postings"}),
    (n+3, PID, "Communication skills appear in 51,419 total job postings 2020-2024, growing 15% from 8,934 to 10,247, indicating sustained demand for collaborative capability", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ECO, "notes": "Top employer demand skill; appears across all three focus sectors and all job levels"}),
    (n+4, PID, "Agile methodology appears in 37,229 total postings, growing 38% from 6,123 to 8,456, indicating shift toward collaborative, adaptive capability", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ECO, "notes": "Second-highest demand skill; 38% growth indicates structural shift"}),
    (n+5, PID, "JavaScript job postings declined 74% from 7,812 in 2020 to 2,001 in 2024, reflecting shift from narrow technical specialisation toward integration fluency", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ECO, "notes": "Traditional technical skills in decline; low-code and AI tooling rising"}),
    (n+6, PID, "Microsoft Azure job postings declined 61% from 7,454 in 2020 to 2,936 in 2024, confirming shift away from narrow technical specialisation", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ECO, "notes": "Adjacent technical skill decline; same pattern as JavaScript"}),
    (n+7, PID, "Only 26 UKRI awards totalling £2.01M were made to GM firms for collaborative R&D in creative projects 2019-2024, reflecting mismatch between funding mechanisms and creative sector needs", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ECO, "value_status": "MONETARY", "value_basis": "OBSERVED_AMOUNT", "notes": "Funding gap evidence; not shortage of fundable ideas but mechanism mismatch"}),
    (n+8, PID, "RNCM's Michelle Phillips identified specific equipment gap: one portable EEG cap at £17,000 each; second cap would enable concert hall research", "EFFECT", "KNOWLEDGE", EP, {"method_ids": M_ECO, "value_status": "MONETARY", "value_basis": "SCENARIO_ESTIMATE", "notes": "Specific fundable gap; modest cost infrastructure barrier"}),
    (n+9, PID, "Effective intervention to support cross-sector capabilities could cost £10,000-£50,000 per initiative, compared to £500,000+ to rebuild lost production teams", "DESIGN", "OPTION", EP, {"method_ids": M_ECO, "value_status": "MONETARY", "value_basis": "SCENARIO_ESTIMATE", "option_subtype": "COST_COMPARISON", "option_state": "IDENTIFIED", "notes": "Cost comparison; prevention vs replacement"}),
    (n+10, PID, "Social network analysis confirms microbusinesses show bridging characteristics connecting nodes across network rather than dominance in any one market vertical", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_SNA, "notes": "SNA finding; microbusinesses as connectors not competitors"}),
    (n+11, PID, "Report documents one microbusiness that enabled three-way immersive prototype between education, wellness, and animation without any formal funding route", "EFFECT", "NETWORK", EP, {"method_ids": M_SNA, "outcome_status": "REPORTED", "notes": "Stabilising organisation example; unfunded but strategically essential"}),
    (n+12, PID, "Traditional innovation funding designed for high-growth ventures actively works against stabilising microbusinesses that prioritise long-term relationships, sustainable growth, and community benefit", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_ECO, "notes": "Structural funding mismatch; perverse consequence of funding model design"}),
    (n+13, PID, "Three market validation questions identified before expansion: graduate supply vs market demand, AI impact on workforce requirements, and revenue models underpinning immersive work (product vs advertising funded)", "DESIGN", "OPTION", EP, {"method_ids": M_INV, "option_subtype": "VALIDATION_QUESTIONS", "option_state": "IDENTIFIED", "option_holder": "MITIH", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Critical questions requiring market validation before investment"}),
    (n+14, PID, "Gated investment sequence proposed: immediate demand validation (3-4 months), then Phase 1 ecosystem strengthening (12-18 months), then Phase 2 training expansion (36-48 months)", "DESIGN", "OPTION", EP, {"method_ids": M_INV, "option_subtype": "GATED_SEQUENCE", "option_state": "PROPOSED", "option_holder": "MITIH", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Risk-managed sequence; proceed/pause/pivot criteria at each gate"}),
    (n+15, PID, "Advertising-funded immersive work shows 70% failure rates for new entrants, contrasting with product-funded work which creates sustainable career pathways", "CONTEXT", "KNOWLEDGE", EP, {"method_ids": M_INV, "notes": "Revenue model distinction; business model determines career viability"}),
    (n+16, PID, "Fifth Sector delivered createch ecosystem report to Salford City Council and MITIH over three months in early 2025; report findings accepted but recommendations rejected by client", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_ECO, "outcome_status": "DELIVERED", "notes": "Report delivered; findings valid but recommendations rejected; unpublished"}),
]

for c in p03_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "full report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["£","%","3,847","51,419","37,229","16,348","31,240","28,594","26 ","2.01","17,000","10,000","50,000","500,000","70%","612","891","74%","61%","15%","38%","33%","34%","28%","41%"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P05-WMCA (SRC-R2-06)
# ============================================================
PID = "P05-WMCA"
SRC = "SRC-R2-06"
FAM = "WMCA-FAM"
EP = "2020-01"
M_SCALE = "M-R3-012"  # scaleup_mapping

p05_claims = [
    (n, PID, "14,903 active DCMS Creative Industries companies registered in West Midlands at Companies House, of which 4,267 aged less than two years, 7,291 aged 2-10 years, and 3,345 aged 11+ years", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_SCALE, "notes": "Total business population; DueDil analysis"}),
    (n+1, PID, "Only 26 companies (of 645 shortlisted) met both CAG criteria (10% turnover growth and 8+ employees), with 50% in IT/software/computer services", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_SCALE, "notes": "CAG eligibility; very few meet both criteria; high bar for creative businesses"}),
    (n+2, PID, "645 businesses shortlisted from 2,336 longlist: 596 DCMS CI SIC code companies and 49 non-DCMS companies uncovered through keyword search", "METHOD_OUTPUT", "CONTEXTUAL", EP, {"method_ids": M_SCALE, "notes": "Shortlist methodology; AI web search, LinkedIn, Crunchbase, GRAND, recruitment analysis"}),
    (n+3, PID, "IT/software/computer services dominate shortlist at 240 companies (37%), followed by music/performing/visual arts at 89 (14%) and advertising/marketing at 79 (12%)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_SCALE, "notes": "Sector breakdown; IT dominant in shortlist and CAG-eligible"}),
    (n+4, PID, "168 businesses scored 'Very Good' on scale-up confidence (meeting 2-3 scale-up criteria), with 48% in IT/software/computer services and 19% in non-DCMS sectors", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_SCALE, "notes": "Scale-up potential; private investment, public investment, social media, recruitment criteria"}),
    (n+5, PID, "253 businesses scored 'Good' on scale-up confidence (meeting 1 criterion), with 22% in music/performing/visual arts and 18% in advertising/marketing", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_SCALE, "notes": "Additional scale-up potential; broader pool beyond CAG criteria"}),
    (n+6, PID, "98 businesses failing to meet either CAG criterion showed scale-up potential, with 25 scoring 'Very Good' on scale-up confidence", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_SCALE, "notes": "CAG criteria miss real scale-up potential; scale-up scoring more effective than CAG alone"}),
    (n+7, PID, "Creative supply chain groupings: Creative Content 325 (50%), Creative Services 183 (28%), Creative Originals 57 (9%), Creative Experiences 50 (8%), with 30 (5%) using creative/immersive tech in non-creative applications", "METHOD_OUTPUT", "PRODUCT", EP, {"method_ids": M_SCALE, "notes": "Supply chain analysis; four-chain methodology from 2017/18 GBSLEP mapping"}),
    (n+8, PID, "49 non-DCMS sector businesses identified through keyword search whose products either formed part of creative supply chain or made extensive use of creative and immersive technologies", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_SCALE, "notes": "Non-DCMS creative businesses; supply chain adjacency; VR/immersive in non-creative sectors"}),
    (n+9, PID, "Fifth Sector contributed scale-up mapping methodology and data analysis as BOP Consulting subcontractor, using AI web search, LinkedIn, Crunchbase, and GRAND database", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_SCALE, "outcome_status": "DELIVERED", "fifth_sector_role": "SUBCONTRACTOR", "contracting_role": "SUBCONTRACTOR", "notes": "BOP prime, Fifth Sector sub; Iain Bennett named as author"}),
]

for c in p05_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "full report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["14,903","4,267","7,291","3,345","2,336","645","596","49","26","240","89","79","168","253","98","25","325","183","57","50","30","37%","14%","12%","48%","19%","22%","18%","50%","28%","9%","8%","5%","10%"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P06-COSTAR (SRC-R2-07)
# ============================================================
PID = "P06-COSTAR"
SRC = "SRC-R2-07"
FAM = "COSTAR-FAM"
EP = "2023-01"
M_BID = "M-R3-013"  # bid_support

p06_claims = [
    (n, PID, "dock10 is UK's biggest multi-camera TV studio outside London with 6+ multi-camera studios, green screen studio, orchestral studio, 200Gbps broadcast network, and award-winning post-production", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_BID, "notes": "dock10 current capability; most versatile production facility outside London"}),
    (n+1, PID, "CoSTAR consortium proposed to transform real time media production workflows extending live/as live, 3D and interactive content to larger range of producers", "DESIGN", "OPTION", EP, {"method_ids": M_BID, "option_subtype": "RESEARCH_INFRASTRUCTURE", "option_state": "PROPOSED", "option_holder": "dock10 consortium", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Bid vision; 2D→3D, interactive→immersive, scalable mixed reality"}),
    (n+2, PID, "Factory Academy reports 65% of participants with diversity data come from underrepresented and/or low socio-economic backgrounds", "EFFECT", "KNOWLEDGE", EP, {"method_ids": M_BID, "outcome_status": "REPORTED", "notes": "EDI outcome; Factory Academy funded through GMCA Adult Education Budget"}),
    (n+3, PID, "LaTurbo Avedon's Factory International Fortnite Creative installation welcomed more than 1.7M visitors, demonstrating mass audience reach for digital arts", "EFFECT", "PRODUCT", EP, {"method_ids": M_BID, "outcome_status": "REPORTED", "notes": "Digital arts reach; Factory International Virtual Factory programme"}),
    (n+4, PID, "Online learning hub proposed to reach up to 10,000 individuals over first three years of CoSTAR project", "DESIGN", "OPTION", EP, {"method_ids": M_BID, "option_subtype": "SKILLS_PROGRAMME", "option_state": "PROPOSED", "option_holder": "Factory International", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Skills output; digital skills for virtual production"}),
    (n+5, PID, "Growth Company delivering GM-wide Create Growth programme with £1.2M funding 2023-26 to support growth of 160 creative businesses, building on DCMS Creative Scale Up pilot", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_BID, "value_status": "MONETARY", "value_basis": "OBSERVED_AMOUNT", "notes": "Aligned investment; existing brokerage and knowledge transfer infrastructure"}),
    (n+6, PID, "dock10 committed to carbon neutrality through offset by 2025 with 5% annual reduction toward net-zero by 2035, with ISO 14001 and 50001 accreditation", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_BID, "notes": "Environmental sustainability; Albert sustainable production certification pioneer"}),
    (n+7, PID, "CoSTAR bid proposed multi-talent motion capture, facial capture, 3D photogrammetry, GPU processing farm, spatial audio, immersive display, and AI computing facilities", "DESIGN", "OPTION", EP, {"method_ids": M_BID, "option_subtype": "CAPITAL_EQUIPMENT", "option_state": "PROPOSED", "option_holder": "dock10 consortium", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Equipment list; TRL 7-9 close-to-market R&D"}),
    (n+8, PID, "Theory of change: democratisation of live production allowing UK producers across larger range of genres to co-create programming for national and international distribution", "DESIGN", "OPTION", EP, {"method_ids": M_BID, "option_subtype": "THEORY_OF_CHANGE", "option_state": "PROPOSED", "option_holder": "dock10 consortium", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Theory of change; invert the pyramid by removing bottlenecks"}),
    (n+9, PID, "Fifth Sector delivered CoSTAR bid support document with theory of change, strategic fit, and delivery plan for Manchester consortium; bid NOT successful", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_BID, "outcome_status": "DELIVERED", "notes": "Bid support delivered; bid NOT successful (confirmed by Iain 2026-09-09); Oct 2025 consortium plan is for different/revived consortium"}),
]

for c in p06_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "full report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["£1.2M","10,000","1.7M","65%","5%","200Gbps","6+"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P07-CC (SRC-R2-08)
# ============================================================
PID = "P07-CC"
SRC = "SRC-R2-08"
FAM = "CC-FAM"
EP = "2020-09"
M_INCEP = "M-R3-014"  # inception_design

p07_claims = [
    (n, PID, "Creative City+ inception note proposed five work packages: project initiation, EOI review, statistical base/supply chain analysis, business/stakeholder engagement, and options assessment/bid drafting", "DESIGN", "OPTION", EP, {"method_ids": M_INCEP, "option_subtype": "WORK_PACKAGES", "option_state": "PROPOSED", "option_holder": "GMCA", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Inception note; five work packages with five key deliverables"}),
    (n+1, PID, "Proposed statistical base would cover Creative Industries, Retail (physical), and eCommerce within GM city region, with value chain analysis across creative content, experience, originals, and services", "DESIGN", "OPTION", EP, {"method_ids": M_INCEP, "option_subtype": "METHODOLOGY_DESIGN", "option_state": "PROPOSED", "option_holder": "GMCA", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Statistical base design; cross-sector analysis spanning creative and retail"}),
    (n+2, PID, "Inception note proposed HMT five-case model for bid development with theory of change, options assessment, and stakeholder engagement up to six meetings", "DESIGN", "OPTION", EP, {"method_ids": M_INCEP, "option_subtype": "BID_METHODOLOGY", "option_state": "PROPOSED", "option_holder": "GMCA", "exercise_access": "FUNDING_DECISION", "outcome_status": "PROPOSED", "notes": "Bid methodology; HMT five-case model; SIPF context"}),
    (n+3, PID, "Fifth Sector delivered inception note for Creative City+ SIPF bid support; application NOT successful and project did not proceed beyond inception", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_INCEP, "outcome_status": "DELIVERED", "notes": "Inception delivered; SIPF application NOT successful; project did not proceed"}),
]

for c in p07_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "entire inception note", c[2][:200], FAM,
        etype="qualitative", notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P09-CDEC (SRC-R2-10)
# ============================================================
PID = "P09-CDEC"
SRC = "SRC-R2-10"
FAM = "CDEC-FAM"
EP = "2012-04"
M_CHAL = "M-R3-017"  # challenges_analysis

p09_claims = [
    (n, PID, "UK creative industries in 2012 accounted for 6.4% of GVA with over 182,000 companies, 1.3M employees, and £17.3bn exports annually", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_CHAL, "value_status": "MONETARY", "value_basis": "OBSERVED_AMOUNT", "notes": "2012 baseline figures; 13 CI sectors from advertising to video games"}),
    (n+1, PID, "Convergence argument: if ICT (5% GVA) and creative industries (6.4% GVA) were pulling together, outcome could be transformative for digital economy", "DESIGN", "OPTION", EP, {"method_ids": M_CHAL, "option_subtype": "CONVERGENCE_PROPOSITION", "option_state": "PROPOSED", "notes": "Convergence proposition; content + technology sectors"}),
    (n+2, PID, "Global content delivery platforms (iPad/iTunes, Kindle, PS3) being created outside UK, with lion's share of value chain extracted elsewhere", "CONTEXT", "KNOWLEDGE", EP, {"method_ids": M_CHAL, "notes": "Competitive challenge; value chain extraction by foreign platforms"}),
    (n+3, PID, "Innovation in creative industries is market-led rather than technology-led, based around commissioning, responding to creative brief, or exploiting commercial opportunities", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_CHAL, "notes": "Innovation model; no agreed model; R&D spend and patents of limited relevance"}),
    (n+4, PID, "Creative industry innovation tends to be highly collaborative with individuals and small businesses coming together on project basis within informal networks", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_CHAL, "notes": "Collaborative innovation; non-exclusive; project-by-project; informal partnerships"}),
    (n+5, PID, "CDEC should provide both 'the street' and 'the lab' - creative professionals innovate by drawing on cultural phenomena and emerging trends, not campus or science park environments", "DESIGN", "OPTION", EP, {"method_ids": M_CHAL, "option_subtype": "FACILITY_DESIGN", "option_state": "PROPOSED", "notes": "Facility design principle; street-level embeddedness needed"}),
    (n+6, PID, "CDEC should address 'two cultures' challenge by providing forum for technologists and creative professionals to experiment and test new products", "DESIGN", "OPTION", EP, {"method_ids": M_CHAL, "option_subtype": "COLLABORATION_MECHANISM", "option_state": "PROPOSED", "notes": "Two cultures challenge; Snow's divide between sciences and humanities"}),
    (n+7, PID, "Small creative businesses need 'two-way street' in CDEC participation: not just selling services to large tech companies but also benefiting and learning", "DESIGN", "OPTION", EP, {"method_ids": M_CHAL, "option_subtype": "PARTICIPATION_MODEL", "option_state": "PROPOSED", "notes": "Participation principle; mutual benefit not one-way extraction"}),
    (n+8, PID, "Fifth Sector provided advisory/consultative input to CDEC challenges paper for Technology Strategy Board; paper finalised April 2012", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_CHAL, "outcome_status": "DELIVERED", "fifth_sector_role": "ADVISOR", "contracting_role": "ADVISOR", "notes": "Advisory role; challenges paper finalised; oldest project in pilot"}),
]

for c in p09_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "entire challenges paper", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["6.4%","5%","182,000","1.3M","£17.3bn"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# Write all claims
claims_file = os.path.join(TOOLKIT_DIR, "04_claims.csv")
with open(claims_file, "a") as f:
    for claim in all_claims:
        row = []
        for col in ["claim_id","project_id","precise_proposition","effect_family","mechanism","option_subtype","originator","recipient","intended_beneficiary_status","event_period","claim_direction","outcome_status","attribution_strength","value_status","boundary_recipient","boundary_org","boundary_sector","boundary_geography","boundary_chain","compensation","intent","timing","direction","beneficiaries","cost_bearers","access_barriers","evidence_sufficiency","source_quality","independence","coverage","time_lag","contrary_evidence","reviewer_confidence","commercial_reuse","fifth_sector_role","review_status","publication_status","notes","claim_type","method_ids","generating_intervention","fifth_sector_contribution","contracting_role","tie_change","option_state","option_holder","exercise_access","prediction","rival_explanations","disconfirming_evidence","observation_window","source_review_state","value_basis","value_review_status","permission_status","rights_status","consent_status","causal_assumptions","codebook_version","review_batch"]:
            val = claim.get(col, "")
            if "," in str(val) or '"' in str(val) or "\n" in str(val):
                val = str(val).replace('"', '""')
                val = f'"{val}"'
            row.append(str(val))
        f.write(",".join(row) + "\n")

# Write all evidence links
evidence_file = os.path.join(TOOLKIT_DIR, "05_evidence_links.csv")
with open(evidence_file, "a") as f:
    for ev in all_evidence:
        row = []
        for col in ["evidence_id","claim_id","source_id","source_locator","extract_or_observation","supports_or_contradicts","evidence_type","limitations","reviewer","review_date","notes","original_locator","derived_locator","source_family_id","source_review_state","codebook_version","review_batch"]:
            val = ev.get(col, "")
            if "," in str(val) or '"' in str(val) or "\n" in str(val):
                val = str(val).replace('"', '""')
                val = f'"{val}"'
            row.append(str(val))
        f.write(",".join(row) + "\n")

print(f"Added {len(all_claims)} claims across 5 projects")
print(f"Added {len(all_evidence)} evidence links")
print(f"Claim IDs: C-G2-{NEXT_CLAIM:03d} to C-G2-{NEXT_CLAIM + len(all_claims) - 1:03d}")
print(f"Evidence IDs: E-G2-{NEXT_EVIDENCE:03d} to E-G2-{NEXT_EVIDENCE + len(all_evidence) - 1:03d}")

# Print per-project counts
from collections import Counter
proj_counts = Counter(c["project_id"] for c in all_claims)
for p, cnt in sorted(proj_counts.items()):
    print(f"  {p}: +{cnt} claims")
