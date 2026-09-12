#!/usr/bin/env python3
"""
Deepen P04-GBSLEP, P08-LIVDCI, P10-KIRK, P11-ELFC, P12-KIRK15 in one batch.

P04-GBSLEP: SRC-R2-05 (Creative Economy mapping, Dec 2017, BOP with Iain Bennett)
P08-LIVDCI: SRC-R2-09 (proposal, Jan 2024), SRC-R2-09B (final report, Jul 2024)
P10-KIRK: SRC-R2-11 (Creative Industries Mapping 2024, Jul 2024)
P11-ELFC: SRC-G2-002 (East London Fashion Cluster report, 2017)
P12-KIRK15: SRC-G2-001 (Kirklees 2015 data tables, BOP analysis)
"""

import csv
import os

TOOLKIT_DIR = "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/spillover-toolkit"

NEXT_CLAIM = 462
NEXT_EVIDENCE = 368

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
# P04-GBSLEP (SRC-R2-05)
# ============================================================
PID = "P04-GBSLEP"
SRC = "SRC-R2-05"
FAM = "GBSLEP-FAM"
EP = "2017-12"
M_MAP = "M-R3-018"  # creative_economy_mapping

p04_claims = [
    (n, PID, "Creative Economy of Greater Birmingham generates £4.1 billion in GVA, 9% of total GBSLEP output, employing 50,000 workers (5.6% of total workforce)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "Headline figure; larger share of employment than Advanced Manufacturing & Engineering"}),
    (n+1, PID, "Creative Industries businesses grew from 4,000 to 5,100 between 2010-2015, with employment growing by 1,300 jobs; IT/software grew by 1,200 jobs and Design by 1,100 jobs (238% increase)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "notes": "Business and employment growth 2010-2015; Design extraordinary growth rate"}),
    (n+2, PID, "Creative Content sector accounts for 16,850 jobs and £1.4 billion GVA, Creative Services for £1.9 billion GVA, despite recent falls in some sectors", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "Supply chain analysis; four-chain methodology"}),
    (n+3, PID, "Crafts cluster in Birmingham has LQ of 6.2, more strongly clustered than any comparable LEP area, most likely attributable to Jewellery Quarter", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_MAP, "notes": "Cluster analysis; LQ > 1.0 indicates clustering; 6.2 is exceptionally strong"}),
    (n+4, PID, "Design sector showing extraordinary growth averaging 238% between 2010-2015 across all local authorities in GBSLEP area", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "notes": "Design cluster growth; dispersed across all local authorities"}),
    (n+5, PID, "Film, TV, Video, Radio & Photography employment fell 42% from 3,700 to 2,100 jobs 2010-2015, Publishing fell 28%, Museums/Galleries/Libraries fell 12%", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "notes": "Sectoral decline; audio-visual lack of commissioning infrastructure; BBC/ITV centralisation in London"}),
    (n+6, PID, "Average size of creative businesses fell from 6.4 to 5.4 employees between 2010-2015, against UK sector average of 7+, indicating potential instability and lack of resilience", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "notes": "Business size concern; may indicate dynamism (new firm creation) or instability"}),
    (n+7, PID, "80% of Advertising & Marketing roles found outside Creative Industries (in-house marketing), while 80% of IT/Software roles within Creative Industries (outsourcing model)", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_MAP, "notes": "Creative Economy dispersal; VML analysis; different outsourcing patterns by sub-sector"}),
    (n+8, PID, "Evidence of spillovers between cultural organisations and commercial creative sector: Ikon Gallery's international specialist publishing business and Stan's Café's scalable theatre show licensed as format to producers in NY, Melbourne, Buenos Aires and Europe", "EFFECT", "KNOWLEDGE", EP, {"method_ids": M_MAP, "outcome_status": "REPORTED", "notes": "Cultural-to-commercial spillover; format licensing as IP exploitation model"}),
    (n+9, PID, "Informal intermediaries (Flatpack, Ikon, Stan's Café) provide mentoring and market information to less established companies, transferring expertise through festivals, training and workshops", "EFFECT", "KNOWLEDGE", EP, {"method_ids": M_MAP, "outcome_status": "REPORTED", "notes": "Informal intermediary role; knowledge transfer mechanism; arts organisations diversifying business models"}),
    (n+10, PID, "Games companies forced to develop own AR/VR tools found market for those applications in wider digital manufacturing sectors, demonstrating cross-sector spillover from creative to advanced manufacturing", "EFFECT", "KNOWLEDGE", EP, {"method_ids": M_MAP, "outcome_status": "REPORTED", "notes": "Cross-sector spillover; games→advanced manufacturing; lack of commissioning forced innovation"}),
    (n+11, PID, "Advertising and marketing professionals translated data analysis and behavioural insight expertise into programmatic advertising business model", "EFFECT", "KNOWLEDGE", EP, {"method_ids": M_MAP, "outcome_status": "REPORTED", "notes": "Knowledge spillover; data skills from creative services to programmatic advertising"}),
    (n+12, PID, "Birmingham is youngest and most diverse city in Europe with 40% of population aged 25 or under, but Creative Industries have yet to fully grasp diversity opportunity", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_MAP, "notes": "Diversity context; RE:Present and ASTONish programmes; broadcaster diversity potential"}),
    (n+13, PID, "If GBSLEP matched Oxfordshire performance, it would add 3,965 creative enterprises and 30,000 jobs to the economy", "DESIGN", "OPTION", EP, {"method_ids": M_MAP, "option_subtype": "COUNTERFACTUAL_SCENARIO", "option_state": "IDENTIFIED", "value_status": "MONETARY", "value_basis": "SCENARIO_ESTIMATE", "notes": "Counterfactual; unfulfilled potential benchmark"}),
    (n+14, PID, "Recommendations proposed: West Midlands Film Fund, Mercian Studios, expanded BBC production, Channel 4 relocation, and higher 'out of London' production quotas", "DESIGN", "OPTION", EP, {"method_ids": M_MAP, "option_subtype": "POLICY_RECOMMENDATIONS", "option_state": "PROPOSED", "option_holder": "GBSLEP", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "High-end content production strategy; inflection point for sector"}),
    (n+15, PID, "Iain Bennett as BOP Consulting Associate authored GBSLEP Creative Economy mapping; BOP prime contractor, Fifth Sector contribution as associate", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_MAP, "outcome_status": "DELIVERED", "fifth_sector_role": "ASSOCIATE", "contracting_role": "SUBCONTRACTOR", "notes": "BOP prime; Iain Bennett as Associate author; December 2017 publication"}),
]

for c in p04_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "full report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["£","%","3,","5,","4,","6,","2,","1,","80%","42%","28%","12%","5%","238%","6.2","1.0","1.5","6.4","5.4","7+","3,965","30,000","40%","50,000","27,500","2.1","4.1","9%","5.6%","3.1%","1,300","1,200","1,100","16,850","1.4","1.9"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P08-LIVDCI (SRC-R2-09 proposal + SRC-R2-09B final report)
# ============================================================
PID = "P08-LIVDCI"
SRC = "SRC-R2-09B"
FAM = "LIVDCI-FAM"
EP = "2024-07"
M_OODA = "M-R3-019"  # OODA loop methodology
M_LINKEDIN = "M-R3-020"  # LinkedIn workforce mapping

p08_claims = [
    (n, PID, "LCR Digital & Creative cluster has over 6,500 businesses and 51,000 digital and creative professionals including 20,000+ freelance and self-employed workers", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_LINKEDIN, "notes": "Headline mapping figure Q1 2024; Beauhurst + LinkedIn methodology"}),
    (n+1, PID, "LCR digital and creative workforce contributed £4 billion in GVA, representing around 4% of national creative industries GVA", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_LINKEDIN, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "GVA estimate; excludes visitor economy contribution from cultural events"}),
    (n+2, PID, "Beauhurst data shows 6,500 active businesses - 2,595 (66%) more than ONS IDBR 2023, with 1,750 more Creative Industries firms and 1,450 more digital firms", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_LINKEDIN, "notes": "ONS underestimates business numbers; IDBR underreports Cultural sectors by 87%"}),
    (n+3, PID, "Beauhurst suggests fewer than half of active Arts businesses recorded in IDBR, indicating systematic undercounting of cultural sector", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_LINKEDIN, "notes": "Arts undercounting; IDBR methodology limitations for microenterprises"}),
    (n+4, PID, "Skills shortage vacancies above national average: 38.2% of North West creative industries vacancies result from skills shortage in workforce", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_LINKEDIN, "notes": "Skills shortage; above national average; diversity and equity concerns"}),
    (n+5, PID, "Sector predominantly white and male, inaccessible to lower socioeconomic groups, with lack of representation of women, people of colour, disabled people in senior roles", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_LINKEDIN, "notes": "EDI challenge; leadership diversity gap"}),
    (n+6, PID, "LCR has repeatedly failed to secure national funding for cluster and innovation activities, with lower private sector investment than comparable city cores", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_OODA, "notes": "Governance failure; funding mechanism mismatch; planning constraints"}),
    (n+7, PID, "Path dependency identified: cluster assumptions contradicted by global technology and consumer behaviour trends, risking falling behind larger, better capitalised clusters", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_OODA, "notes": "Path dependency analysis; need for differentiation strategy"}),
    (n+8, PID, "Three scenarios identified: worst case (uncontrolled decline), most likely (jobs-free growth through AI), best case (competitiveness through differentiation)", "DESIGN", "OPTION", EP, {"method_ids": M_OODA, "option_subtype": "SCENARIO_ANALYSIS", "option_state": "IDENTIFIED", "option_holder": "LCRCA", "exercise_access": "COMMISSIONER_DECISION", "notes": "Scenario planning; AI displacement as central risk"}),
    (n+9, PID, "Differentiation strategy proposed: new business models leveraging independent production, collaboration between content creators and tech innovators, upskilling for AI/interactive technologies, brand narrative around unique cultural assets", "DESIGN", "OPTION", EP, {"method_ids": M_OODA, "option_subtype": "DIFFERENTIATION_STRATEGY", "option_state": "PROPOSED", "option_holder": "LCRCA", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Recommendations; break path dependency through differentiation"}),
    (n+10, PID, "Fifth Sector delivered LCR Digital & Creative Cluster mapping using OODA Loop methodology with Curator Technologies LinkedIn analysis and Obsolete.com AI advisory", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_OODA, "outcome_status": "DELIVERED", "notes": "Final report July 2024; OODA methodology; multi-source approach"}),
    (n+11, PID, "LCR Connect network and STFC/Hartree identified as nationally significant digital assets combining with Investment Zone and Freeport status for innovation ecosystem", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_OODA, "notes": "Infrastructure context; LCR Connect blueprint from Digital Infrastructure Framework"}),
    (n+12, PID, "Cross-sector opportunities identified: Creative Health, Diagnostics (AI and XR), and Industry 4.0 through collaboration with Health & Life Sciences and Manufacturing sectors", "DESIGN", "OPTION", EP, {"method_ids": M_OODA, "option_subtype": "CROSS_SECTOR_OPPORTUNITY", "option_state": "IDENTIFIED", "option_holder": "LCRCA", "exercise_access": "COMMISSIONER_DECISION", "notes": "Cross-sector convergence; DCI interacting with other priority clusters"}),
    (n+13, PID, "Eurovision 2023 generated £54 million benefit for Liverpool, raising question of how to realise this in new investment to grow supply side of cultural and creative economy", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_OODA, "value_status": "MONETARY", "value_basis": "OBSERVED_AMOUNT", "notes": "Event impact; demand-side success vs supply-side gap"}),
]

for c in p08_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "final report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["£","%","6,500","51,000","20,000","2,595","1,750","1,450","87%","38.2%","4%","54"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P10-KIRK (SRC-R2-11)
# ============================================================
PID = "P10-KIRK"
SRC = "SRC-R2-11"
FAM = "KIRK-FAM"
EP = "2024-07"
M_KIRK = "M-R3-021"  # Kirklees mapping 2024

p10_claims = [
    (n, PID, "1,698 active cultural and creative businesses in Kirklees in 2024, increase of 184 (15%) since 2022, despite IDBR showing decline from 1,025 to 940", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "notes": "Beauhurst vs IDBR discrepancy; official statistics underestimate sector"}),
    (n+1, PID, "Creative workforce in Kirklees exceeded 9,400 people in 2024, significantly higher than BRES employment figures suggest", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "notes": "LinkedIn workforce data; BRES underestimates freelance and self-employed"}),
    (n+2, PID, "GVA from Cultural and Creative Industries in Kirklees estimated at £250.9 million in 2022, increase of £75m (43%) from 2020", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "GVA growth; 43% increase 2020-2022"}),
    (n+3, PID, "899 creative business starts between April 2021 and June 2024, with 691 remaining active; highest formation rates in Crafts (68%), Advertising & Marketing (51%), Music/Performing Arts (41%)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "notes": "Business dynamism; high startup rates in multiple sub-sectors"}),
    (n+4, PID, "Huddersfield city centre microcluster: 257 businesses within 1km radius, with IT/software and Music/performing arts each qualifying as single sub-sector microclusters", "EFFECT", "NETWORK", EP, {"method_ids": M_KIRK, "outcome_status": "REPORTED", "notes": "Microcluster evidence; 763 companies (44%) within 5km of city centre"}),
    (n+5, PID, "Creative microclusters found across Kirklees: Cleckheaton (72 businesses), Holme Valley South/Holmfirth (59 businesses), with IT/software largest sub-sector in each", "EFFECT", "NETWORK", EP, {"method_ids": M_KIRK, "outcome_status": "REPORTED", "notes": "District-wide clustering; not just city centre phenomenon"}),
    (n+6, PID, "Music, performing and visual arts grew 56% (115 businesses) to become second-largest sector, with 305 businesses in 2024", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "notes": "Music sector growth; supports Kirklees Year of Music 2023"}),
    (n+7, PID, "Advertising and marketing jobs grew more than fivefold from 120 to 670 between 2020-2022, while IT/software fell from 1,760 to 1,225 - striking restructuring", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "notes": "Sectoral restructuring; advertising growth vs IT decline"}),
    (n+8, PID, "Film, TV, video, radio and photography employment grew from 230 to 505 between 2020-2022, with Music/performing arts growing from 115 to 200", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK, "notes": "Sectoral growth; film/TV and music recovery post-pandemic"}),
    (n+9, PID, "Holmfirth Art Week Fringe showed 52 venues, only one registered as creative company, revealing large 'informal' cultural economy not captured in business counts", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_KIRK, "notes": "Informal cultural economy; venues operated by charities, trusts, mutual societies"}),
    (n+10, PID, "Fifth Sector delivered Kirklees Creative Industries Mapping 2024, repeating previous 2015-2022 analysis to ascertain impact of changes over that period", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_KIRK, "outcome_status": "DELIVERED", "notes": "Repeat mapping; longitudinal analysis; July 2024 final report"}),
    (n+11, PID, "Recommendations: address discrepancy between official statistics and actual sector performance, improve creative skills training, enhance support for freelancers and micro-businesses, spread benefits across district", "DESIGN", "OPTION", EP, {"method_ids": M_KIRK, "option_subtype": "POLICY_RECOMMENDATIONS", "option_state": "PROPOSED", "option_holder": "Kirklees Council", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Policy recommendations; community wealth building approach"}),
]

for c in p10_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "final report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["£","%","1,698","184","15%","9,400","250.9","75","43%","899","691","68%","51%","41%","257","763","44%","72","59","305","115","56%","120","670","1,760","1,225","230","505","115","200","52","1,025","940"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P11-ELFC (SRC-G2-002)
# ============================================================
PID = "P11-ELFC"
SRC = "SRC-G2-002"
FAM = "ELFC-FAM"
EP = "2017-06"
M_ELFC = "M-R3-022"  # East London Fashion Cluster

p11_claims = [
    (n, PID, "UK fashion industry direct value estimated at £28.1 billion, twice automotive or chemicals industries, with total GDP contribution exceeding £50 billion (2.7% of UK GDP)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "Sector scale; global apparel market US$2.4-3 trillion"}),
    (n+1, PID, "Fashion in East London and Upper Lea Valley contributes £1.4 billion to London's economy, employs 36,000+ people, with output growing 57% 2010-2015 and 10,900 new jobs created", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "East London fashion growth; faster than rest of London economy"}),
    (n+2, PID, "LCF relocation to Queen Elizabeth Olympic Park consolidates 5,700 students and three schools into £800M Cultural Education District with UCL, V&A, Sadler's Wells", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "value_status": "MONETARY", "value_basis": "OBSERVED_AMOUNT", "notes": "LCF as catalyst; CED public-private partnership; Olympic legacy"}),
    (n+3, PID, "Two-thirds of LCF fashion design students are non-UK nationals, making Brexit threat to freedom of movement a direct risk to fashion education and talent pipeline", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "notes": "International student dependency; Brexit risk to talent supply"}),
    (n+4, PID, "ELFC vision: 21st century innovation quarter where fashion, technology, business and education meet; re-establish London as World Creative Fashion Capital by 2050", "DESIGN", "OPTION", EP, {"method_ids": M_ELFC, "option_subtype": "VISION_STATEMENT", "option_state": "PROPOSED", "option_holder": "LCF; GLA", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Vision statement; smart specialisation proposition"}),
    (n+5, PID, "Smart specialisation opportunity: reimagine London's fashion sector as globally significant digital manufacturing cluster, increasing high value employment and driving inward investment", "DESIGN", "OPTION", EP, {"method_ids": M_ELFC, "option_subtype": "SMART_SPECIALISATION", "option_state": "PROPOSED", "option_holder": "LCF; GLA", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Smart specialisation; digital manufacturing convergence"}),
    (n+6, PID, "Cross-sector spillover pathway: fashion-technology convergence will stimulate 'pull through' of innovations in digital manufacturing with wider applications in other sectors", "DESIGN", "OPTION", EP, {"method_ids": M_ELFC, "option_subtype": "SPILLOVER_PATHWAY", "option_state": "IDENTIFIED", "option_holder": "ELFC", "exercise_access": "COMMISSIONER_DECISION", "notes": "Spillover design; fashion as driver of digital manufacturing innovation"}),
    (n+7, PID, "Private sector skills investment through Fashion Technology Alliance and Stitch Academy at Hackney Walk, with public sector support for Fashioning Poplar and Building Bloqs manufacturing facilities", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "notes": "Infrastructure initiatives; mixed public-private investment model"}),
    (n+8, PID, "Plexal accelerator for fashion and IoT start-ups established at Here East by founders of fintech incubator Level 39, opening June 2017", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "notes": "Accelerator infrastructure; fashion-IoT convergence; Here East"}),
    (n+9, PID, "ELFC commissioned jointly by LCF and GLA to explore how rebirth of fashion sector could be accelerated by proximity to other centres of knowledge capital", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_ELFC, "outcome_status": "DELIVERED", "fifth_sector_role": "ASSOCIATE", "contracting_role": "SUBCONTRACTOR", "notes": "BOP Consulting associate; Iain Bennett as author; LCF/GLA joint commission"}),
    (n+10, PID, "Risk of ratchet effect: loss of capacity, opportunity and reputation could ultimately threaten London's status as world fashion city if structural barriers not addressed", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_ELFC, "notes": "Risk analysis; workspace, finance, skills, Brexit threats compound"}),
    (n+11, PID, "ELFC will coordinate different offers of specialist business support, skills development, network capability and funding across East London to address structural challenges and information failures", "DESIGN", "OPTION", EP, {"method_ids": M_ELFC, "option_subtype": "COORDINATION_MECHANISM", "option_state": "PROPOSED", "option_holder": "ELFC", "exercise_access": "COMMISSIONER_DECISION", "outcome_status": "PROPOSED", "notes": "Cluster organisation role; address information failures"}),
]

for c in p11_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "full report", c[2][:200], FAM,
        etype="quantitative" if any(x in c[2] for x in ["£","%","28.1","50","2.7%","1.4","36,000","57%","10,900","5,700","£800","66%","US$"]) else "qualitative",
        notes=f"Evidence for C-G2-{n:03d}")
    all_evidence.append(ev)
    n += 1
    ev_n += 1

# ============================================================
# P12-KIRK15 (SRC-G2-001)
# ============================================================
PID = "P12-KIRK15"
SRC = "SRC-G2-001"
FAM = "KIRK15-FAM"
EP = "2015-12"
M_KIRK15 = "M-R3-023"  # Kirklees 2015 data tables

p12_claims = [
    (n, PID, "Kirklees Creative Industries employment 2015: 3,360 jobs, with IT/software (1,250), Design (510), Museums/galleries/libraries (300), Architecture (290), Publishing (290)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK15, "notes": "2015 baseline; BRES data and BOP analysis"}),
    (n+1, PID, "Kirklees Creative Economy employment 2015: 5,020 jobs, with IT/software (1,790), Design (750), Advertising & Marketing (770), Architecture (420)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK15, "notes": "Creative Economy wider definition; includes creative occupations outside Creative Industries"}),
    (n+2, PID, "Kirklees Creative Industries GVA 2015: £100.979M, with IT/software generating £63.935M (63.3%), Advertising & Marketing £11.387M (11.3%), Design £8.242M (8.2%)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK15, "value_status": "MONETARY", "value_basis": "OBSERVED_ESTIMATE", "notes": "GVA breakdown; IT/software dominant at 63%"}),
    (n+3, PID, "Kirklees creative businesses predominantly microenterprises: 85 of 90 Advertising & Marketing businesses micro (0-9 employees), 55 of 60 Architecture, 65 of 65 Advertising agencies", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK15, "notes": "Business size profile; microenterprise dominance; only 10 IT businesses have 10+ employees"}),
    (n+4, PID, "Sole proprietor businesses in Kirklees: 30 Design, 30 IT/software, 15 Film/TV/photography, 15 Music/performing arts, 10 Advertising & Marketing", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK15, "notes": "Sole proprietor data; freelance/self-employed indicator"}),
    (n+5, PID, "Culture, media and sport occupations in Kirklees (SOC2010) fluctuated: 3,300 (2009/10), 3,800 (2010/11), 3,100 (2011/12), 5,600 (2012/13), 3,000 (2013/14)", "CONTEXT", "CONTEXTUAL", EP, {"method_ids": M_KIRK15, "notes": "Annual Population Survey; volatility in cultural occupations; 2012/13 spike"}),
    (n+6, PID, "Proportion of creative businesses below VAT threshold in Kirklees: Design 26%, Music/performing arts 20%, Film/TV/photography 21%, Advertising & Marketing 11%, IT/software 6.7%", "METHOD_OUTPUT", "KNOWLEDGE", EP, {"method_ids": M_KIRK15, "notes": "VAT threshold analysis; microenterprise indicator; Design and Music highest proportions below threshold"}),
    (n+7, PID, "Iain Bennett as BOP Consulting Associate delivered Kirklees 2015 creative economy data analysis establishing baseline for longitudinal tracking", "BID_SUPPORT_DELIVERED", "NOT_APPLICABLE", EP, {"method_ids": M_KIRK15, "outcome_status": "DELIVERED", "fifth_sector_role": "ASSOCIATE", "contracting_role": "SUBCONTRACTOR", "notes": "BOP prime; Iain Bennett as Associate; 2015 baseline data tables"}),
]

for c in p12_claims:
    all_claims.append(make_claim(*c[:6], **c[6]))
    ev = make_evidence(ev_n, f"C-G2-{n:03d}", SRC, "data tables", c[2][:200], FAM,
        etype="quantitative",
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

from collections import Counter
proj_counts = Counter(c["project_id"] for c in all_claims)
for p, cnt in sorted(proj_counts.items()):
    print(f"  {p}: +{cnt} claims")
