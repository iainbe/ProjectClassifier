# P08-LIVDCI — Project Index Card (REVIEWED)

**Card status:** REVIEWED — populated from full read of canonical final report (SRC-R2-09B); consistency confirmed by Iain 26/09/12 (PRIME role, client acceptance, rating split).
**Reviewed by:** Devin (full read, QA lenses) + Iain (consistency confirmation)

---

## A. Client-facing side

### A1. Project identity

| Field | Value | Source |
|---|---|---|
| `project_id` | P08-LIVDCI | 01_projects.csv |
| `project_name` | Liverpool City Region Digital & Creative Industries Cluster Mapping | 01_projects.csv |
| `client` | Liverpool City Region Combined Authority | 01_projects.csv |
| `client_contact` | NOT_ESTABLISHED | 09_publication_assets.csv |
| `reference_permission` | NOT_ESTABLISHED | permission_status |
| `commission_date` | ~24/01 (proposal 24/01/05) | file system metadata |
| `completion_date` | 24/07/08 (final report accepted by client) | canonical version record + Iain confirmation |
| `contract_value` | NOT_ESTABLISHED | 06_measurements.csv |
| `contracting_role` | PRIME — Iain confirmed 26/09/12 | VAL-R3-015 |
| `prime_contractor` | The Fifth Sector | VAL-R3-015 |
| `geography` | Liverpool City Region (Liverpool, Wirral, Sefton, Knowsley, St Helens, Halton) | SRC-R2-09B |
| `sector_focus` | Digital & creative industries cluster mapping | SRC-R2-09B |
| `lifecycle_status` | COMPLETED — final report accepted by client; Iain confirmed 26/09/09 | 01_projects.csv |

### A2. Brief summary

| Field | Value | Source |
|---|---|---|
| `brief_summary` | Liverpool City Region commissioned The Fifth Sector to map the digital and creative industries cluster across the city region. The study combined official statistics (BRES, ONS, DCMS) with innovative data analysis (LinkedIn, Beauhurst, Companies House, DataCity) to reveal a substantially larger creative economy than national statistics suggested, including a large freelance workforce invisible to conventional data sources. | SRC-R2-09B Executive Summary |
| `key_deliverables` | (1) Final report: LiverpoolCityRegion_DigitalCreative_final (24/07/08, DOCX+PDF, 844 paras, 27 tables, 85 pages); (2) Proposal: LCR DCI Cluster mapping (24/01/05, DOCX, 274 paras); (3) Changes document (24/07/08, DOCX) | canonical version records |
| `client_objective` | Evidence to demonstrate the scale, clustering, and economic contribution of LCR's digital and creative industries to inform regional economic strategy | SRC-R2-09B |
| `scope_boundary` | Digital and creative industries cluster mapping across LCR; four supply chains (Creative Content, Creative Experiences, Creative Originals, Creative Services); business counts, workforce, GVA, LQ, skills supply; includes freelance workforce analysis | SRC-R2-09B Contents |

### A3. Key findings (client-facing)

| Field | Value | Source |
|---|---|---|
| `headline_finding` | LCR's digital and creative economy comprises over 6,500 businesses and 51,000 professionals including 20,000+ freelancers — 66% more businesses than ONS IDBR data suggests — contributing an estimated £4.0 billion in GVA | SRC-R2-09B lines 153, 220, 357 |
| `key_findings` | (1) 6,500 active businesses (Beauhurst) vs ~3,905 IDBR 2023 — 66% more; (2) 51,000 digital/creative professionals, 20,000+ freelance/self-employed; (3) 1,750 more Creative Industries firms, 1,450 more digital firms than ONS; (4) IDBR underreports Cultural sectors by 87%; (5) £4.0bn GVA (main text) / £4.5bn (appendix — methodological refinement); (6) LQ 1.15; (7) four supply chains mapped; (8) 51,779 LinkedIn digital/creative workforce; £77,252 GVA per capita | SRC-R2-09B lines 153, 220, 227, 357, 751, 967 |
| `quantified_results` | 6,500 businesses; 51,000 professionals; 20,000+ freelancers; £4.0bn/£4.5bn GVA; 1.15 LQ; 51,779 workforce; £77,252 GVA per capita; 1,750/1,450 more firms than ONS; 87% IDBR underreporting | 06_measurements.csv |
| `client_decision_use` | NOT_ESTABLISHED — no decision-use claim found in reviewed claims | 04_claims.csv |
| `evidence_strength` | MEDIUM — substantial quantitative mapping (27 tables, 85 pages); PRIME contractor; multiple data sources; innovative methodology; but headline GVA figures are modelled estimates not observed outcomes; Iain confirmed split rating 26/09/12 | Derived |

### A4. Permitted use

| Field | Value | Source |
|---|---|---|
| `citation_status` | DELIVERED_WORK — completed as PRIME; not web-published — PUB-P08-LIVDCI TENDER_ONLY_NOT_WEBSITE | 01_projects.csv lifecycle_status + 09_publication_assets.csv; Devin 26/09/16, pending Iain confirmation |
| `commercial_reuse` | APPROVED_NAMED — approved for tender citation by Iain 26/09/12 | Iain confirmation |
| `permitted_wording` | May be named in tender submissions (Iain approved 26/09/12) | Iain confirmation |
| `expiry` | NOT_ESTABLISHED | 09_publication_assets.csv |
| `reference_status` | CLEARED for tender naming 26/09/12; website publication still requires separate gate | Iain confirmation |

---

## B. Inward-facing side

### B1. Methodological significance

| Field | Value | Source |
|---|---|---|
| `methods_used` | Creative economy cluster mapping using BRES, ONS/NOMIS, DCMS Economic Estimates, LinkedIn (77,252 profiles), Beauhurst, Companies House, DataCity; four supply chain taxonomy; LinkedIn-based clustering analysis; GVA estimation from workforce data; LQ analysis; skills supply mapping | SRC-R2-09B |
| `method_innovation` | LinkedIn-based clustering analysis to overcome national data limitations at city region level; Beauhurst vs IDBR business count reconciliation; four supply chain taxonomy; LinkedIn workforce data for freelance/self-employed capture; DataCity real-time industrial classification | SRC-R2-09B |
| `method_evolution` | 3 phases: proposal (24/01, rev=307) → outline and drafting (24/06, 4 versions in 3 days) → final report (24/07, table count jumped 6→27). Final report went through outline → draft → final in ~1 month | changelog |
| `breakthrough_points` | LinkedIn-based clustering analysis when national data showed no clustering at city region level; Beauhurst/IDBR reconciliation revealing 66% undercount | SRC-R2-09B |
| `spillover_types_identified` | KNOWLEDGE (creative skills in non-creative sectors); PRODUCT (creative content/services supply chains); NETWORK (cluster analysis); OPTION (creative economy as platform for growth) | 04_claims.csv |
| `spillover_evidence_strength` | KNOWLEDGE: DOCUMENTED (51,000 professionals, 20,000+ freelancers); PRODUCT: DOCUMENTED (supply chain GVA); NETWORK: DOCUMENTED (cluster analysis, LQ 1.15); OPTION: INTERPRETATION (creative economy as growth platform) | Derived |
| `option_analysis` | Creative economy mapped as platform for wider economic growth; LinkedIn clustering analysis reveals network structure invisible to official statistics | SRC-R2-09B |
| `causal_analysis` | DESCRIPTIVE — mapping and estimation, no counterfactual | 04_claims.csv |
| `measurement_approach` | Quantitative mapping: BRES employment, ONS/NOMIS, DCMS Economic Estimates, LinkedIn workforce, Beauhurst business counts, GVA estimation from workforce productivity; LQ analysis | SRC-R2-09B |

### B2. Repeatability and transferability

| Field | Value | Source |
|---|---|---|
| `repeatability` | HIGH — methodology is repeatable for other city regions; LinkedIn + Beauhurst + DataCity approach overcomes ONS data limitations; requires LinkedIn data access and Beauhurst/Companies House analysis | Derived |
| `transfer_conditions` | LinkedIn data access; Beauhurst/Companies House records; DCMS Economic Estimates; local stakeholder network for consultation | Derived |
| `data_dependencies` | BRES, ONS/NOMIS, DCMS Economic Estimates, LinkedIn (77,252 profiles), Beauhurst, Companies House, DataCity, IDBR | SRC-R2-09B credits |
| `access_requirements` | LinkedIn data access; Beauhurst/Companies House records; ONS microdata; local stakeholder network | SRC-R2-09B |
| `effort_estimate` | ~6 months (Jan–24/07) | Notes |
| `reuse_examples` | LinkedIn workforce methodology originally developed in P04-GBSLEP (2017); reused in P08 and later projects: LCR Music Economy (P19), Calderdale Music (P16), SYMCA (P20), WSBH (P21), Somerset (P52), Rushmoor (P57), TVCA (P46), Solent (P29) | 04_claims.csv |

### B3. Tender relevance

| Field | Value | Source |
|---|---|---|
| `tender_relevance_tags` | cluster-mapping, digital-creative-industries, liverpool-city-region, linkedin-analysis, beauhurst, four-supply-chains, freelance-workforce, GVA-estimation, LQ-analysis | Derived |
| `buyer_types` | Combined authority, city region, LEP | Derived |
| `precedent_strength` | STRONG — substantial quantitative mapping; PRIME contractor; innovative methodology; multiple data sources; client accepted report | Derived |
| `precedent_caveats` | GVA figures are modelled estimates not observed outcomes; £4.0bn/£4.5bn discrepancy is methodological refinement; LinkedIn data has inherent limitations (penetration, self-reporting) | Derived |
| `positioning_notes` | Flagship project for creative economy mapping capability; demonstrates LinkedIn + alternative data methodology; PRIME contractor role | Derived |
| `comparable_tenders` | NOT_ESTABLISHED | 08_tenders.csv |

### B4. Quality and review status

| Field | Value | Source |
|---|---|---|
| `card_status` | REVIEWED | 26/09/12 |
| `last_reviewed` | 26/09/12 | 10_review_history.csv |
| `reviewed_by` | Devin (full read, QA lenses) + Iain (consistency confirmation 26/09/12) | — |
| `source_claims` | C-G2-* claims for P08 | 04_claims.csv |
| `source_measurements` | M-G2-* measurements for P08 | 06_measurements.csv |
| `unresolved_issues` | (1) Specific sub-sector business counts not extractable from text (tables are embedded images); (2) £4.0bn vs £4.5bn GVA discrepancy preserved as methodological refinement | 07_validation_actions.csv |
| `superseded_by` | None | — |
