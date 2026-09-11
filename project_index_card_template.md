# Project Index Card Template

**Status:** R1.5 design — provisional. Cards are derived outputs, not primary evidence. They are populated from reviewed records (R3) and must trace to reviewed claim IDs. Cards may be drafted from metadata and changelogs during R1.5/R2 but carry PROVISIONAL status until R3 review confirms consistency.

**Purpose:** Quick-reference index for tender precedent search and portfolio navigation. One card per project. Two sides: client-facing (what a buyer needs to know) and inward-facing (what Fifth Sector needs to know for method, tender positioning and repeatability).

---

## A. Client-facing side

This side summarises what is externally referenceable. Every field must trace to a reviewed claim or source. Fields that cannot be evidenced are marked NOT_ESTABLISHED, not guessed.

### A1. Project identity

| Field | Description | Source |
|---|---|---|
| `project_id` | Stable project ID (P01-NES etc.) | 01_projects.csv |
| `project_name` | Canonical project name | 01_projects.csv |
| `client` | Commissioning organisation name | 01_projects.csv |
| `client_contact` | Named contact for reference (with permission status) | 01_projects.csv + 09_publication_assets.csv |
| `reference_permission` | Whether client has agreed to be named as a reference | permission_status in 04_claims.csv |
| `commission_date` | When the commission was awarded | 01_projects.csv |
| `completion_date` | When the final deliverable was accepted | 01_projects.csv (lifecycle_status=COMPLETED) |
| `contract_value` | Commission value (if disclosable). Source: typically in Proposal or Project Management folders, not Reporting folders. | 06_measurements.csv or notes |
| `contracting_role` | Fifth Sector's contracting role (PRIME / SUBCONTRACTOR / ASSOCIATE / PARTNER) | 01_projects.csv |
| `prime_contractor` | Prime contractor if Fifth Sector was not prime | 01_projects.csv |
| `geography` | Geographic scope | 01_projects.csv |
| `sector_focus` | Sector or sub-sector focus | 01_projects.csv |
| `lifecycle_status` | Current commission status | 01_projects.csv |

### A2. Brief summary

| Field | Description | Source |
|---|---|---|
| `brief_summary` | 2-3 sentence summary of what was commissioned and why | Reviewed from canonical final report + proposal |
| `key_deliverables` | List of delivered outputs (report, playbook, presentation, data) | 01_projects.csv + canonical version records |
| `client_objective` | What the client wanted to achieve | Reviewed from brief/proposal |
| `scope_boundary` | What was in and out of scope | Reviewed from brief/proposal |

### A3. Key findings (client-facing)

| Field | Description | Source |
|---|---|---|
| `headline_finding` | One-sentence headline finding the client can cite | Reviewed claim with evidence_status >= REPORTED |
| `key_findings` | 3-5 bullet-point findings, each with claim ID | 04_claims.csv (reviewed) |
| `quantified_results` | Any quantified results with value_basis and value_review_status | 06_measurements.csv (reviewed) |
| `client_decision_use` | Evidence that the client used the findings in a named decision | 04_claims.csv (claim_type=DECISION_USE) |
| `evidence_strength` | Overall evidence strength assessment (HIGH / MEDIUM / LOW / MIXED) | Derived from claim/evidence review |

### A4. Permitted use

| Field | Description | Source |
|---|---|---|
| `commercial_reuse` | Current reuse permission level | 09_publication_assets.csv |
| `permitted_wording` | Exact wording approved for external use | 09_publication_assets.csv |
| `expiry` | Any expiry on permitted use | 09_publication_assets.csv |
| `reference_status` | Whether this project can be named in tenders | permission_status + rights_status |

---

## B. Inward-facing side

This side captures methodological significance, repeatability and tender relevance. It is for internal use only and is never shared externally without separate clearance.

### B1. Methodological significance

| Field | Description | Source |
|---|---|---|
| `methods_used` | Methods applied (not just proposed) with method_status | 03_methods.csv (APPLIED or CORROBORATED) |
| `method_innovation` | What was methodologically distinctive or new | Reviewed from changelog + claim review |
| `method_evolution` | How methods changed during the project (from changelog) | project_changelogs/ |
| `breakthrough_points` | Versions where significant analytical breakthroughs occurred | project_changelogs/ |
| `spillover_types_identified` | Which spillover types were identified (PRODUCT / KNOWLEDGE / NETWORK / OPTION) | 04_claims.csv (effect_family) |
| `spillover_evidence_strength` | Evidence strength per spillover type | 04_claims.csv (evidence_status) |
| `option_analysis` | Whether strategic option analysis was performed and at what depth | 04_claims.csv (option_state/subtype) |
| `causal_analysis` | Whether causal analysis was performed and at what level (DESCRIPTIVE / CONTRIBUTION / CAUSAL_ESTIMATE) | 04_claims.csv (attribution) |
| `measurement_approach` | How effects were measured (qualitative / quantitative / mixed) | 06_measurements.csv |

### B2. Repeatability and transferability

| Field | Description | Source |
|---|---|---|
| `repeatability` | How repeatable is this method for other clients/sectors? (HIGH / MEDIUM / LOW) | Derived from method review |
| `transfer_conditions` | What conditions are needed to repeat this work elsewhere | Derived from method review |
| `data_dependencies` | What data sources were required | 02_sources.csv |
| `access_requirements` | What access/permissions were needed | 02_sources.csv + 07_validation_actions.csv |
| `effort_estimate` | Actual effort observed (days/hours) if recorded | Notes or 07_validation_actions.csv |
| `reuse_examples` | Where this method has been reused (internal or external) | 04_claims.csv (INTERNAL_REUSE mechanism) |

### B3. Tender relevance

| Field | Description | Source |
|---|---|---|
| `tender_relevance_tags` | Tags for matching to tender requirements (e.g. "creative-economy-mapping", "network-analysis", "option-valuation", "skills-assessment") | Derived from methods + findings |
| `buyer_types` | Types of buyers this work is relevant to (e.g. LEP, combined authority, university, cultural body, UKRI) | Derived from client + scope |
| `precedent_strength` | How strong a precedent is this for tender use? (STRONG / MODERATE / WEAK / NOT_ESTABLISHED) | Derived from evidence review |
| `precedent_caveats` | What limits this as a precedent (scale, geography, sector, role, age, permissions) | Derived from review |
| `positioning_notes` | How this project positions Fifth Sector for similar tenders | Derived from method + role review |
| `comparable_tenders` | Tender opportunities where this project is a relevant precedent | 08_tenders.csv (linked) |

### B4. Quality and review status

| Field | Description | Source |
|---|---|---|
| `card_status` | PROVISIONAL / REVIEWED / SUPERSEDED | Derived from review history |
| `last_reviewed` | Date of last R3 review that confirmed card consistency | 10_review_history.csv |
| `reviewed_by` | Reviewer who confirmed consistency | 10_review_history.csv |
| `source_claims` | Claim IDs that support the card's findings | 04_claims.csv |
| `source_measurements` | Measurement IDs that support quantified results | 06_measurements.csv |
| `unresolved_issues` | Any open validation actions affecting the card | 07_validation_actions.csv |
| `superseded_by` | If this card has been superseded by a later version | Review history |

---

## C. Card lifecycle

1. **R1.5 draft:** Card created from metadata, changelog and canonical version records. Status: PROVISIONAL. Fields that require reviewed claims are marked NOT_ESTABLISHED.
2. **R2 update:** Diagnostic coding may populate or correct some fields. Status remains PROVISIONAL.
3. **R3 review:** Full pilot review populates all fields from reviewed records. Iain confirms consistency between card and underlying evidence. Status: REVIEWED. R3 is the final approval gate for index cards.
4. **Ongoing:** Card is updated when claims, measurements, permissions or project status change. Each update is recorded in review history. Status returns to PROVISIONAL until next review confirms consistency.
5. **Tender use:** Only REVIEWED cards with `reference_status=CLEARED` and `commercial_reuse >= APPROVED_NAMED` may be used in tender responses. PROVISIONAL cards are internal reference only.

## D. Future: website searchability (separate later approval)

At a later stage of website development, index cards may be made searchable on www.thefifthsector.co.uk. This requires a separate approval gate beyond R3 that covers:

- **GDPR compliance:** personal data (client contacts, named individuals) must be assessed for lawful processing, consent and data subject rights. Public display of personal data requires consent or another lawful basis.
- **Data security:** searchable cards on a public website expose previously internal information. A security assessment must cover what is exposed, to whom, and whether it creates risk (commercial sensitivity, client confidentiality, competitive exposure).
- **Field-level publication control:** not all card fields are suitable for public display. The client-facing side (A) may be partially publishable; the inward-facing side (B) is internal only. Each field needs a publication classification: PUBLIC / RESTRICTED / INTERNAL.
- **Separate approval:** this is not authorised by R3, M3, G2 or any current gate. It requires its own explicit approval with GDPR assessment, security review and field-level publication decisions. It would likely fall under G5a/G5b (staged website change/publication) or a dedicated gate.

No work on website searchability is commenced or implied by creating the cards.

## D. Index card file

One Markdown file per project in `project_index_cards/`:
- `P01_NES_index_card.md`
- `P02_FGTG_index_card.md`
- etc.

A derived summary index (`project_index.csv`) provides one row per project with key fields for quick search/filter.

## E. Relationship to existing artifacts

- **01_projects.csv:** source of project identity, lifecycle, role data
- **04_claims.csv:** source of findings, spillover types, evidence status, option analysis
- **06_measurements.csv:** source of quantified results
- **03_methods.csv:** source of methods used
- **02_sources.csv:** source of data dependencies and access requirements
- **08_tenders.csv:** links to comparable tenders
- **09_publication_assets.csv:** source of permission and reuse status
- **project_changelogs/:** source of method evolution and breakthrough points
- **10_review_history.csv:** source of review status and consistency confirmation
