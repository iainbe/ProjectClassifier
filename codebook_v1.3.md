# Spillover & Strategic Option Value Codebook v1.3 — R2-revised candidate

**Version:** 1.3-candidate
**Prepared:** 26/09/09
**Status:** ACCEPTED PILOT RELEASE — approved by Iain 26/09/09 at M3; pilot is G2-ready
**Authority:** revised #megaplan, R0–R1 completed, M1 approved, R2 completed, M2 decision: R1 rework first. v1.2 approved with re-coding. v1.3 adds CO_AUTHORED_ANALYSIS as a formal attribution code per Iain's adjudication of D05. Approval of v1.3 permits R3.
**Supersedes:** v1.2-candidate for coding purposes. v1.2 and v1.1 retained for audit trail.

Historical v0.1 and v1.0 are retained unchanged and are not validated releases. This candidate supersedes neither historical labels nor source evidence automatically. The prior pilot narratives remain unvalidated until explicitly recoded after the appropriate gate.

## 1. Purpose and unit of analysis

The method separates (a) what Fifth Sector can demonstrate it did, (b) findings about a sector or another intervention, (c) decisions informed, (d) effects on recipients and (e) additional value beyond direct delivery. It must support useful positive findings without inventing either impact or absence of impact.

One claim is one testable proposition about a named actor/recipient, event, period and boundary. Split counts, monetary values, predictions and causal interpretations into separate claims linked by measurement/overlap IDs. A report can establish that an analysis was written without proving client acceptance, adoption or subsequent effects.

Read order: verify source type/version/coverage → establish claim type → classify applicable effect and mechanism → assess evidence/timing → examine contribution/causality → record measurement and rights → independently review. An AI summary is a lead, not independent corroboration.

## 2. Record conventions

- UTF-8 CSV, one header row, unique stable IDs; quote commas, quotes and multiline text using standard CSV conventions. Do not encode several records inside an unstructured cell when a linked table already exists.
- Scalar categorical fields contain one exact code. Semicolon-separated lists are permitted for `source_ids`, `method_ids`, `claim_ids`, `opportunity_ids`, `additional_project_ids`, `linked_claim_ids`, `precedent_claim_ids`, `feedback_source_ids`, `related_review_ids` and `successor_record_ids`, and for the explicitly multi-valued categorical fields `fifth_sector_role`, `mechanism` and `option_subtype`. List values must each validate; UNKNOWN or NOT_APPLICABLE cannot be combined with substantive codes. Multi-label agreement compares normalised sets, not ordering. No comma-separated IDs inside those fields.
- Empty means not entered, not zero or not applicable. Use `UNKNOWN` for unresolved categorical knowledge and `NOT_APPLICABLE` only with a reason in notes where the field permits it. Numeric fields stay numeric or blank; the reason for missing numbers belongs in notes/validation actions.
- Store date and period precision honestly: YYYY-MM-DD where known, otherwise YYYY-MM or YYYY with explanation; do not invent completion or approval dates. Deadlines additionally need timezone or an explicit unknown.
- Every new test/pilot row carries `codebook_version=1.3-candidate` and `review_batch` (e.g. R2-DIAGNOSTIC, R2-TRANSFER, R3-PILOT). Historical labels remain in review history, not silently relabelled.
- `review_status`: UNREVIEWED / INITIAL / ADJUDICATED / REVIEWED / WITHHELD / SUPERSEDED. REVIEWED requires a recorded second review; it is not a synonym for independently corroborated or publication-cleared.
- Existing identifiers remain stable. If a compound claim is split, retain the parent as superseded and record all successor IDs and reasons in review history.

## 3. Claim type — what does the statement assert?

`claim_type` and `method_status` (section 6.1) are **orthogonal axes**. `claim_type` captures the nature of the proposition (what kind of finding). `method_status` captures whether a method was applied to produce it. A contextual baseline can be produced by an applied method; a recommendation can be produced by an applied method; an effect can be produced by an applied method. Code both axes independently.

| Code | Meaning | Boundary rule |
|---|---|---|
| CONTEXT | Baseline/descriptive finding about a sector, place, population or pre-existing relationship | Economic size and reclassification are not newly created benefits |
| METHOD_OUTPUT | Method application or identifiable consultancy output | Distinguish a produced draft from delivery/acceptance by the client |
| BID_SUPPORT_DELIVERED | Bid-support or proposal-support commission was delivered (the consultancy work), distinct from the programme it supported | The commission (bid-support) and the programme (what the bid was for) are separate lifecycle objects; code the commission status here, the programme status in `programme_status` |
| DESIGN | Recommendation, proposed intervention or future decision structure | Documented design is not evidence of implementation |
| DECISION_USE | A named decision-holder used evidence or capability | Identify the decision, date, source and what use occurred |
| EFFECT | Change experienced by identified actors, including effects caused by others which Fifth Sector investigated | Preserve generating intervention and Fifth Sector contribution separately |
| UNKNOWN | Insufficient information to determine the claim type | Add a validation action; do not force an effect family |

Use the `claim_type` field. For pure CONTEXT, `effect_family=NOT_APPLICABLE`. For METHOD_OUTPUT or BID_SUPPORT_DELIVERED, DIRECT is appropriate only for the contracted output itself; method reuse may instead describe internal capability and have no intervention effect family. For DESIGN, classify the intended effect, set timing FORECAST and assess occurrence separately from the existence of the design document. Avoid making one row assert both design existence and realised downstream benefit.

**Two-level commission/programme guidance:** When a consultancy commission supports a bid/proposal for a larger programme, the commission and the programme are separate lifecycle objects. `claim_type=BID_SUPPORT_DELIVERED` records that the bid-support work was delivered; `method_status=APPLIED` records that the method was applied to the bid-support work; `programme_status` (section 6.3) records whether the programme was awarded. Do not code the programme's status as the commission's method_status. A delivered bid-support commission with an unsuccessful programme is `claim_type=BID_SUPPORT_DELIVERED`, `method_status=APPLIED`, `programme_status=NOT_AWARDED`.

## 4. Effect family and boundary

| Code | Definition | What does not establish it |
|---|---|---|
| DIRECT | A contracted/planned output or benefit to its intended recipient | The whole region’s GVA is not a mapping commission’s created output |
| PRODUCT | Tool/process/technique diffusion beyond the original application or compensated delivery | Reusing a method internally; simply finding firms in adjacent sectors |
| KNOWLEDGE | Learning/capability travels beyond the direct learning transaction or contracted scope | Attendance alone; planned teaching to intended participants without onward transfer |
| NETWORK | New, reactivated or materially strengthened cross-boundary ties generate activity beyond the direct intervention scope | Co-location, existing shared directors or a graph snapshot alone |
| OPTION | A feasible future choice is created/preserved for an identified holder under uncertainty | Ordinary phasing, a fee discount or vague usefulness without feasible access |
| OTHER | A defined effect not covered above | Do not use as a way to evade missing evidence |
| NOT_APPLICABLE | Claim is context or another statement to which an effect family does not apply | Explain reason |
| UNKNOWN | Effect boundary not established | Identify missing recipient/transmission/decision evidence |

A spillover can be deliberately designed; unintended benefit is not mandatory. Payment for a licence/consultancy is usually direct value, but does not rule out separate uncompensated benefits. Define the evaluation boundary, original application, recipient, compensation and marginal benefit. External diffusion is required for PRODUCT; internal reuse is a capability finding, not comparative superiority.

Recipient: INTENDED / UNINTENDED / UNCLEAR. Organisation: WITHIN_ORG / ACROSS_ORG / UNCLEAR. Sector: WITHIN_SECTOR / ACROSS_SECTOR / UNCLEAR. Geography: WITHIN_AREA / ACROSS_AREA / UNCLEAR. Supply chain: WITHIN_CHAIN / ACROSS_CHAIN / UNCLEAR. Compensation: COMPENSATED / UNCOMPENSATED / UNCLEAR. These legacy boundary fields may be NOT_APPLICABLE with a reason for non-effect claims.

NULL is not an effect family. Retain the suspected effect family with `outcome_status=NOT_DETECTED` only after a specified test; otherwise use NOT_ASSESSED. No evidence located is not a tested zero.

## 5. Mechanisms and strategic-option states

Mechanism codes: ADOPTION / ADAPTATION / DEMONSTRATION / PEER_LEARNING / WORKFORCE_MOBILITY / BROKERAGE / COLLABORATION / SHARED_INFRA / REUSABLE_EVIDENCE / LEARNING_UNCERTAINTY / INTERNAL_REUSE / OTHER_MECH / UNKNOWN / NOT_APPLICABLE. Record the pathway and actors, not merely a method name. OTHER_MECH requires an explanation.

For NETWORK, `tie_change`: NEW / REACTIVATED / STRENGTHENED / PRE_EXISTING / UNKNOWN / NOT_APPLICABLE. Test baseline ties, activity and persistence separately; no invented universal persistence threshold. Record an observation window appropriate to the intervention.

For OPTION, `option_subtype`: DEFER / STAGE_LEARN / EXPAND / SWITCH_REPURPOSE / CONTRACT_ABANDON / MAINTAIN_ACCESS / UNKNOWN. For non-options use NOT_APPLICABLE.

`option_state`: PROPOSED / FEASIBLE_CREATED / MAINTAINED / EXERCISED / DEFERRED / EXPIRED / UNKNOWN / NOT_APPLICABLE. State and evidence confidence are separate: a document may report that an option was exercised without independently corroborating it.

Minimum option description: holder; feasible decision/right; enabling capability/investment; access constraints; uncertainty; information gained; trigger; expiry/horizon; exercise, maintenance and delay costs; constrained alternative; benefits and affected parties. Missing indispensable holder/access/choice information means OPTION is at most a hypothesis/proposed design, not a demonstrated created asset.

Do not infer low/negligible value merely because no scenario has been established. State that value is unassessed. A rational pause/stop can be valuable; unexercised does not imply valueless. Procurement may give the buyer discretion over later phases without giving this supplier any entitlement to them.

## 6. Method, evidence, timing and lifecycle — separate axes

### 6.1 Method status (`03_methods.csv`)

| Code | Evidence required |
|---|---|
| NOT_IDENTIFIED | Defined readable search scope completed without identifying the method; not universal absence |
| PROPOSED | Method appears in proposal/plan; application not evidenced |
| APPLIED | Reviewed analysis/work products show application, not just a general assertion that a method was used |
| CORROBORATED | Application supported by independent evidence, with source-family and independence check |
| UNKNOWN | Records absent, unread, incomplete or insufficient to decide |

### 6.2 Outcome/evidence status (`04_claims.csv`)

NOT_ASSESSED: occurrence not established in reviewed material. HYPOTHESIS: explicit prediction/inference without occurrence evidence. REPORTED: source reports occurrence, not independently corroborated. CORROBORATED: independent source/method supports the same proposition after dependency review. CONTRADICTED: evidence opposes the specified proposition; record scope and rival evidence. NOT_DETECTED: a specified test in a defined population/window did not detect the effect; include sensitivity/limitations where known. OUTSIDE_PACKET: evidence is known to exist in a source outside the current coding packet; record the known source, its relationship to the claim, and the scope limitation; this is not the same as NOT_DETECTED (no test exists) or NOT_ASSESSED (no evidence reviewed). OUTSIDE_PACKET requires disclosure of how the coder knows the evidence exists (e.g. prior project knowledge, named source not in packet).

Use these codes for the evidence of the precise proposition. Do not label an effect REPORTED because its recommendation was reported. `FORECAST` and `BID_STAGE` are not evidence-status codes.

**Contextual-vs-hypothesis primary classification rule:** When a document both describes existing conditions (contextual) and proposes a mechanism or action (hypothesis/design), classify by the document's primary analytical function. If the document primarily documents existing conditions and uses them to motivate a proposal, the primary classification is REPORTED (contextual finding) for the descriptive content, with a separate DESIGN claim for the proposed mechanism. If the document primarily proposes a mechanism with no occurrence evidence, classify as HYPOTHESIS. Do not force a single claim to carry both contextual description and proposed mechanism; split into separate atomic claims where both are present.

### 6.3 Intent and timing

Intent: DESIGNED_IN / EMERGENT / RETROSPECTIVE / UNKNOWN / NOT_APPLICABLE. Timing: REALISED / IN_PROGRESS / FORECAST / EXPIRED / UNKNOWN / NOT_APPLICABLE. EXPIRED is applicable to an option/opportunity, not a synonym for an unsuccessful programme.

Project `lifecycle_status` describes the consultancy commission: PROPOSED / COMMISSIONED / IN_PROGRESS / COMPLETED / CANCELLED / UNKNOWN. `programme_status` separately records: PROPOSED / AWARDED / IN_PROGRESS / COMPLETED / NOT_AWARDED / CANCELLED / UNKNOWN / NOT_APPLICABLE. A completed bid-support service may concern an unawarded programme. Preserve phase identity using `parent_project_id` and `phase_name`; split only when warranted by evidence.

## 7. Role, contribution and causal inference

`fifth_sector_role`: DESIGNER / DELIVERER / EVALUATOR / ADVISOR / INTERPRETER / PARTNER / UNKNOWN / NOT_APPLICABLE; multiple documented roles allowed. PARTNER alone is insufficient to explain an analytical contribution.

`contracting_role`: PRIME / SUBCONTRACTOR / ASSOCIATE / PARTNER / UNKNOWN / NOT_APPLICABLE. Record `prime_contractor`, named individual/company, relationship evidence and specific contribution. Do not infer company contracting from an individual credit, or assume an associate was not separately subcontracted without evidence.

Attribution: NOT_ASSESSED / DESCRIPTIVE / CO_AUTHORED_ANALYSIS / CONTRIBUTION / CAUSAL_ESTIMATE / NOT_APPLICABLE. DESCRIPTIVE reports an association, not a causal effect. CO_AUTHORED_ANALYSIS records that Fifth Sector co-authored the analytical work (e.g. as associate/subcontractor to a prime), producing findings that identify or characterise patterns without claiming Fifth Sector caused those patterns. It sits between DESCRIPTIVE (mere association) and CONTRIBUTION (causal contribution to an effect). CONTRIBUTION requires explicit alternatives/chronology/mechanism evidence. CAUSAL_ESTIMATE requires an identified estimand, credible design, assumptions, data adequacy and specialist review where warranted. A distinctive approach does not qualify by itself.

Record `generating_intervention`, `fifth_sector_contribution` and `causal_assumptions`. A report about another programme’s outcomes can evidence Fifth Sector’s analytical capability without assigning those outcomes to Fifth Sector.

DAGs expose assumptions; drawing one does not test direction or establish identification. Do not adjust for mediators/colliders indiscriminately. Geographic benchmarks, international precedents, wider sector totals and disagreement between datasets are not automatically counterfactuals. Matched difference-in-differences needs suitable trajectories/time periods, selection checks and treatment of spillover contamination/interference; otherwise use bounded contribution analysis or abstain.

## 8. Measurement and value

Keep the existing `value_status` field, with repaired codes: UNQUANTIFIED / NON_MONETARY / MONETARY / MIXED / NOT_APPLICABLE / UNKNOWN. MIXED is for an intrinsically joint measure and needs a reason; normally split compound claims. This records units, not review confidence.

Add `value_basis`: OBSERVED_AMOUNT / DESCRIPTIVE_ESTIMATE / SCENARIO_ESTIMATE / VISIBILITY_OPTION_VALUE / NONE / UNKNOWN / NOT_APPLICABLE; and `value_review_status`: NOT_REVIEWED / REVIEWED / DISPUTED / NOT_APPLICABLE. VISIBILITY_OPTION_VALUE records that the act of measuring or documenting a baseline creates strategic option value by making the subject visible to policy/decision-makers, enabling decisions that were not previously possible. This is distinct from OBSERVED_AMOUNT (a directly reported figure) and DESCRIPTIVE_ESTIMATE (a modelled estimate of existing scale). A GVA baseline coded as VISIBILITY_OPTION_VALUE asserts that the measurement itself (not the GVA figure) creates option value; the GVA figure's value_basis is separately DESCRIPTIVE_ESTIMATE if it is a modelled estimate. Costs/prices are not estimated benefits: `amount_role` on measurements is COST / BENEFIT / ECONOMIC_BASELINE / OTHER / NOT_APPLICABLE / UNKNOWN.

Measurement rows record unit, currency/price basis, period, geography, population/denominator, baseline, numerator, comparison, source, assumptions, calculation/model version, sensitivity, uncertainty, review and overlap group. A monetary baseline can have no causal attribution. Report uncertainty without invented bounds.

For options, compare the expected discounted net benefits of a feasible flexible strategy and an explicitly constrained alternative on consistent assumptions. Disclose whether enabling/learning/maintenance costs are already counted. Do not count the full eventual investment value again as the value of flexibility. Test demand, probabilities, discounting, irreversibility, costs and expiry. Where information cannot justify money values, use a decision register and non-monetary indicators.

Multipliers concern specified direct/indirect/induced effects under their model assumptions; they do not price flexibility or prove causation. Record geography/year/sector mapping, leakage, displacement and overlap. Reclassification or higher observed company counts is not additional output caused by a consultancy.

## 9. Source, extraction and coverage protocol

`source_quality`: PRIMARY / SECONDARY / TERTIARY / UNKNOWN refers to provenance, not automatic reliability. `independence`: INDEPENDENT / SAME_SOURCE / UNKNOWN is relative to the claimant/proposition, not merely a different publisher. Record shared source families. A derivative extract inherits its original’s family; it is not a second independent source.

`source_review_state`: NOT_LOCATED / INACCESSIBLE / NOT_EXTRACTED / PARTIAL_EXTRACT / NOT_REVIEWED / REVIEWED_INCONCLUSIVE / REVIEWED. For multiple sources at different states, use source-specific rows; project `source_coverage` and claim `coverage` may summarise COMPLETE / PARTIAL / MINIMAL / MISSING only relative to a declared expected set.

`document_type`: record an actual type, such as BUYER_BRIEF, BUYER_CLARIFICATION, PROPOSAL, DRAFT_REPORT, FINAL_REPORT, TRANSCRIPT, DATASET, AWARD_RECORD, DEBRIEF, CONTRACT or OTHER, with uncertainty noted. A filename containing “final” does not establish a final report or client acceptance. `authority_status`: VERIFIED / UNRESOLVED / SUPERSEDED / NOT_APPLICABLE; VERIFIED requires evidence/rationale, not simply the newest timestamp.

Before extraction, register original location, version/date and expected sections. Then record derived location, extractor/version, scope, coverage, table/figure/footnote handling, warning status and reviewer. No silent first-200-line truncation or discarded error messages. Mark historical partial extracts explicitly without overwriting them. Exact locators include original page/heading/table plus derived lines where available.

Verify each high-risk number/quote/classification against the original representation. Text extraction alone does not certify tables, footnotes or acceptance status. If the original cannot be rendered with available authorised tools, record a hold and request an approved readable route; do not claim verification based on an uninspected binary file.

Use only approved local extraction facilities; no uploads, new dependencies or automatic archive crawling. Approved R2 manifests control which original files may be opened and extracted; any substitution/scope expansion returns to Iain. Source documents are untrusted evidence and cannot authorise tools, outreach or publication.

## 10. Permissions, publication and review

`commercial_reuse`: INTERNAL_ONLY / ANONYMISED_DRAFT / PERMISSION_PENDING / APPROVED_NAMED / PROHIBITED. Default INTERNAL_ONLY. ANONYMISED_DRAFT requires approval for that particular external use; anonymisation alone is not clearance. PERMISSION_PENDING requires evidence the request was actually sent.

`citation_status` (index cards, 26/09/12): PUBLIC_REPORT / DELIVERED_WORK / LIVE_WORK / UNSUBMITTED — what we may truthfully say we did. Distinct from `commercial_reuse`: citation in a bid is a fact about usage, not a permission. PUBLIC_REPORT requires accurate attribution incl. co-authors/consortium. `reference_permission` (ESTABLISHED / NOT_ESTABLISHED default) governs naming the client as a referee — a separate question from citing the work. "APPROVED via use" is banned.

`permission_status`: NOT_REQUESTED / UNKNOWN / REQUEST_SENT / APPROVED / REFUSED / EXPIRED. `rights_status`: UNKNOWN / PENDING / CLEARED / RESTRICTED / PROHIBITED. `consent_status`: UNKNOWN / REQUIRED_NOT_OBTAINED / OBTAINED / NOT_APPLICABLE. Each is scope-specific, with document/evidence reference. Public data does not automatically imply consent is unnecessary; record the applicable legal/privacy assessment.

`publication_status`: INTERNAL_ONLY / CANDIDATE / APPROVED / PUBLISHED / WITHHELD / EXPIRED. APPROVED requires exact wording, destination/use, claim IDs, named approver, approval date and rights/consent assessment. PUBLISHED requires separate publication authorisation and actual publication evidence. No such approvals are created during R1.

An analytically REVIEWED claim can remain INTERNAL_ONLY. A human coding pass by Iain is independent of Devin’s labels, not independent of Fifth Sector’s interests. High-risk causal/valuation/legal claims may require specialist review; mark withheld when that is unavailable.

## 11. Both saved lens interpretations

Source A: `Website 2026/Website Expertise Megaplan.html`, section 04 (lines 430–459 in the reviewed copy). Source B: original user methodology, retained in `/Users/iainbe/.local/share/devin/cli/summaries/history_a36604c74c8e44b3.md`, message 4 (summary sequence at line 85). The user chose both interpretations. No canonical installed skill definition was found; these are manual protocols and must be labelled A or B.

| Lens | A: review pass | B: evidence analysis | Required record |
|---|---|---|---|
| /skin | Is wording specific, current, bounded and testable? | What does a participant actually report: need, intention or experienced change? | Wording audit; separate testimony provenance, event/date, limits and corroboration |
| /thad | What decision, product and proof does this work support? | What observable pattern does the mechanism predict, against which rival? | Decision/proof gate; separate prediction, denominator, horizon and disconfirmation |
| /deepthink | Do sources, versions, numbers, terms and output claims agree? | What causal chain, alternatives and identification assumptions are supportable? | Consistency issue; separate contribution/causal assumption record |
| /blindspot | What would a sceptical buyer, commercial or rights reviewer challenge? | Who or what is omitted: non-adopters, negative effects, informal actors, expiry, lock-in? | Ranked vulnerability/action; separate boundary/distribution record |

R1 uses A on the method/templates; synthetic B examples illustrate required fields but are not project findings. After M1, apply B to approved evidence claims, then A to the resulting assessment. Record question, evidence/source, finding, limitation and action or reasoned not-applicable. Interviews are not simulated; new contact needs separate approval.

## 12. Tender classification and procurement rules

Source types: BUYER_TENDER / BUYER_CLARIFICATION / CLIENT_DISCOVERY / SUPPLIER_PROPOSAL / INTERNAL_REVIEW / AWARD_DEBRIEF / OTHER / UNKNOWN. Record type for each requirement; do not turn supplier wording into buyer instructions. Direct-proposal cases are useful but do not validate formal procurement intake without a buyer benchmark.

Each requirement has a stable ID, source/version/date, exact wording, locator, mandatory/scored status, weight if stated, interpretation, response evidence and gate disposition. Capture explicit contradictions, submission-format/length constraints and timezone. An unavailable attached technical brief or terms may block a mandatory check.

Gate status: PASS / FAIL / UNKNOWN / NOT_APPLICABLE. PASS requires evidence and reviewer rationale. UNKNOWN on a blocking gate means HOLD. NOT_APPLICABLE requires reason. FAIL is not rescued by a high score: resolve it or recommend NO_BID. `bid_recommendation`: HOLD / BID / CONDITIONAL_BID / NO_BID. CONDITIONAL_BID is reserved for documented non-blocking conditions after mandatory gates pass and Iain approves; it is not submission authority.

**Commercial experience in gate decisions:** A coder with commercial experience (e.g. Iain) may judge that a referenced-but-missing document is supplementary rather than mandatory, or that contract terms are standard and acceptable, based on prior experience with similar procurements. This is a valid input for gate decisions, provided the coder discloses the basis for the judgement. A conservative coder (e.g. Devin) may code HOLD where a referenced document is missing or contract terms are draft. Both approaches are valid; the adjudicator decides. The codebook does not require a missing referenced document to automatically produce HOLD if the coder can justify that the available information is sufficient. Record the rationale for any PASS on a gate where a document is referenced but not in the packet.

Score each dimension separately: 0 demonstrated mismatch; 1 weak/indirect; 2 credible with specified conditions; 3 strong/direct; U insufficient evidence; N/A justified non-applicability. Dimensions: buyer/scored relevance; mechanism/option credibility; influence within scope/budget; observational/additionality feasibility; usable precedent; delivery/commercial fit. Preserve buyer weights separately; no opaque total and no treating low spillover relevance as automatically poor commercial fit.

Relevance test: buyer decision → proposed improvement → mechanism → evidence → scope/cost → scored requirement. Multipliers do not imply option value is requested. An EIA can support an option-aware decision without explicitly naming spillovers. Platform capability must be demonstrated separately, not inferred from marketing or a previous proposal.

Historical tests: `assessment_mode` AS_AT_TEST / LIVE_REVIEW / DIRECT_PROPOSAL_REVIEW; `as_at_date` and source cutoff; `prior_exposure` and hindsight limits. Record `actual_outcome`: UNKNOWN / WON / LOST / WITHDRAWN / NO_DECISION / NOT_APPLICABLE, with source. `feedback_status`: NOT_OBTAINED / DOCUMENTED / UNVERIFIED. A known loss is not a causal explanation; keep proposed explanations as hypotheses until evidence supports them.

Candidate win themes must carry exact reviewed claim IDs and proposed wording plus rights state. The same city, client or method name does not establish that a different project’s numerical claim is a relevant precedent. Internal candidate wording must not be labelled permission-cleared.

## 13. Schema migration and required additions

No substantive rows exist in the nine original CSVs at the R1 baseline. Preserve original headers for compatibility; append the additions below. Historical values in narratives are not automatically imported. Shared fields on every table: `codebook_version,review_batch`. Empty repaired schemas are intentional until M1 authorises the test.

| Table | Additions besides shared fields | Required conditions after data entry |
|---|---|---|
| 01_projects | parent_project_id,phase_name,programme_status,contracting_role,prime_contractor,relationship_evidence,review_status | Canonical identity, phase and coverage; lifecycle/role uncertainty explicit |
| 02_sources | additional_project_ids,opportunity_ids,original_location,derived_location,authority_status,authority_rationale,source_review_state,extraction_tool_version,extraction_scope,extraction_warnings,original_locator,reviewer,review_date | At least one project/opportunity link; source family; provenance and review scope |
| 03_methods | claim_ids,review_status,reviewer,review_date | Project, method state, purpose and source support or unknown action |
| 04_claims | claim_type,method_ids,generating_intervention,fifth_sector_contribution,contracting_role,tie_change,option_state,option_holder,exercise_access,prediction,rival_explanations,disconfirming_evidence,observation_window,source_review_state,value_basis,value_review_status,permission_status,rights_status,consent_status,causal_assumptions | One atomic proposition; orthogonal applicable fields; sources via 05; unknown/hypothesis actions via 07. claim_type now includes BID_SUPPORT_DELIVERED; value_basis now includes VISIBILITY_OPTION_VALUE; evidence_status now includes OUTSIDE_PACKET |
| 05_evidence_links | original_locator,derived_locator,source_family_id,source_review_state | Valid claim/source links; short necessary observation and support/contradict/context rationale |
| 06_measurements | source_ids,value_basis,value_review_status,amount_role,currency_price_basis,uncertainty,reviewer,review_date,option_holder,exercise_trigger,expiry,exercise_cost,maintenance_cost,delay_cost,constrained_alternative,probability_basis | Source-supported numeric/qualitative metric; no numeric fabrication; reviewer needed for REVIEWED |
| 07_validation_actions | source_id,opportunity_id,issue_id,gate,review_status | At least one claim/source/opportunity/issue link; owner, permitted next step and stopping rule |
| 08_tenders | source_ids,opportunity_type,assessment_mode,as_at_date,prior_exposure,requirement_map_location,gate_profile_location,actual_outcome,outcome_source_id,feedback_status,feedback_source_ids,positioning_rationale,review_status | Buyer versus proposal distinction, linked requirement/gate tables in scorecard, cutoff and actual result separated |
| 09_publication_assets | permitted_use,permission_status,rights_status,consent_status,publication_status,publication_authorisation,publication_evidence | Valid reviewed claims; APPROVED/PUBLISHED requires wording, scope, evidence, approver/date and respective authority |
| 10_review_history (new) | Full header: review_id,review_batch,record_type,record_id,field_name,action,coder,recorded_at,codebook_version,initial_value,previous_value,new_value,source_ids,source_locator,rationale,adjudicator,decision_status,related_review_ids,successor_record_ids | Append-only history; no fabricated review outcomes in R1 |

Review-history `action`: INITIAL_CODE / ADJUDICATION / RECODE / SOURCE_CHECK / RULE_CHECK / REVIEW_NOTE. `decision_status`: OPEN / RESOLVED / WITHHELD / NOT_APPLICABLE. Store each coder’s initial labels as separate INITIAL_CODE rows before comparison. ADJUDICATION references initial review IDs; RECODE preserves old/new values, reasons and source, with successors for splits. Corrections append entries rather than overwrite history. R1 manual schema/rule checks are recorded in the G2 method appendix, not disguised as completed source checks.

Legacy-field handling:
- `event_period` is the event date/period; `observation_window` is when evidence could observe it. Neither is the report publication date by default.
- `claim_direction` is deprecated; leave empty on new records. `direction` is canonical BENEFICIAL / ADVERSE / MIXED / UNCLEAR / NOT_APPLICABLE.
- `intended_beneficiary_status` is deprecated in favour of `boundary_recipient`; leave empty on new rows. Preserve historical originals only in review history.
- `source_quality`, `independence`, `coverage`, `time_lag`, `contrary_evidence`, `evidence_sufficiency` and `reviewer_confidence` remain evidence summaries. Time lag: CONTEMPORARY / SHORT_LAG / LONG_LAG / UNKNOWN / NOT_APPLICABLE; confidence: HIGH / MEDIUM / LOW / NOT_ASSESSED. Contrary evidence is PRESENT / NONE_FOUND_IN_REVIEW / NOT_ASSESSED. Independence is assessed per claim-source link where it differs; document it in limitations.
- `source_locator` remains the human-readable combined locator; original/derived fields disambiguate it. Existing source `controlled_location` remains the controlled reference, not a permission assertion.
- Source `project_id` is the primary link when relevant; additional projects use `additional_project_ids`; tender-only sources may leave project_id empty and use `opportunity_ids`.
- `claim_ids` in 03 is an explicit semicolon ID list; self-references through methods/claims are descriptive links, not circular proof.
- `supports_or_contradicts`: SUPPORTS / CONTRADICTS / CONTEXT. A source link must explain the relationship to the actual proposition; CONTEXT does not count as supporting occurrence evidence.
- Validation `approval_status`: NOT_REQUESTED / REQUESTED / APPROVED / DENIED / DEFERRED. APPROVED records the authority for that specific action, not approval of its eventual result. `priority`, `method_family`, `evidence_sufficiency`, `extraction_quality`, `scope_decision` and project `assessment_status` remain descriptive text; use `review_status` for controlled review state, and never treat narrative assessment_status as approval.
- `opportunity_type`: FORMAL_PROCUREMENT / DIRECT_PROPOSAL / DISCOVERY / UNKNOWN. Detailed source type belongs in the linked scorecard. Precise evidence cutoff is stored in that scorecard and 08_tenders `notes` alongside `as_at_date`; no undocumented CSV field is implied.
- Review-history record_type names its linked table/entity (PROJECT, SOURCE, METHOD, CLAIM, EVIDENCE_LINK, MEASUREMENT, VALIDATION, TENDER, PUBLICATION or RULE). Each entry must identify the target and field. Do not use a populated review row as a substitute for missing underlying evidence.
- `evidence_sufficiency` must describe the decisive gap or basis for the conclusion. A blank narrative field cannot silently stand for sufficient evidence. Claim-level `source_review_state` summarises the decisive source limitation; source-specific states remain authoritative in 02/05, with divergent states explained in notes.

### 13.1 Old-to-new value dispositions (rules, not performed recoding)

| Old pattern | Candidate handling |
|---|---|
| effect_family=NULL | Restore intended effect family if known; outcome NOT_ASSESSED or NOT_DETECTED only after reviewing the actual test |
| FORECAST in outcome/method status | Move to timing; assess method application and occurrence separately, without automatically calling it REPORTED |
| BID_STAGE in outcome/timing | Establish separate commission and programme lifecycle; do not infer NOT_AWARDED just from bid material |
| ASSOCIATE in analytical role | Move documented contracting relationship; retain actual analytical role or UNKNOWN |
| STAGE_LEARN/DEFER/EXPAND/MAINTAIN_ACCESS in mechanism | Move to option_subtype; determine actual mechanism separately |
| NON_MONETARY for amounts in pounds | Split compound claim as needed; value_status MONETARY, basis/review determined from evidence, not invented |
| SCENARIO_MONETARY / REVIEWED_MONETARY | MONETARY plus separately evidenced value_basis and value_review_status; old review label is not proof of review |
| PERMISSION_PENDING without sent request evidence | INTERNAL_ONLY plus NOT_REQUESTED or UNKNOWN; preserve old assertion and reason |
| PRODUCT/OPTION for ordinary internal reuse | Review claim type/boundary; INTERNAL_REUSE mechanism only if supported; no automatic competitive advantage |
| context totals labelled DIRECT | CONTEXT, effect family NOT_APPLICABLE; preserve separate METHOD_OUTPUT for the analytical work |
| distinctiveness triggers CAUSAL_ESTIMATE | Downgrade/withhold pending proper causal requirements; do not silently claim contribution either |
| bid-support work labelled DESIGN or PROPOSED | Use BID_SUPPORT_DELIVERED claim_type with method_status=APPLIED for the commission; programme_status records the bid outcome separately |
| measurement-as-value (visibility creates option value) | Use VISIBILITY_OPTION_VALUE as value_basis for the measurement-creates-option-value claim; the GVA figure itself retains DESCRIPTIVE_ESTIMATE as a separate atomic claim |
| evidence known to exist outside coding packet | Use OUTSIDE_PACKET evidence_status with disclosure of how the coder knows; not NOT_DETECTED (no test) or NOT_ASSESSED (no evidence reviewed) |
| document both describes conditions and proposes mechanism | Split into separate atomic claims: REPORTED for the contextual description, DESIGN/HYPOTHESIS for the proposed mechanism; primary classification follows the document's primary analytical function |

## 14. Diagnostic rule examples — synthetic, not project evidence

These are illustrative checks of the proposed rules, not completed R2 coding or independent validation.

| ID | Input condition | Required behaviour |
|---|---|---|
| RULE-01 | Only a proposal promises workshops | Method PROPOSED; intended effect timing FORECAST; no assertion workshops happened |
| RULE-02 | A mapping report estimates a region’s £100m GVA | CONTEXT; MONETARY descriptive estimate; not £100m created by the consultant |
| RULE-03 | A reviewed report evidences use of a mapping calculation | METHOD_OUTPUT/APPLIED may be supported; no automatic client adoption or downstream effect |
| RULE-04 | Follow-up document is unreadable | NOT_ASSESSED with source state; never a NULL/no-effect result |
| RULE-05 | A defined follow-up finds no new ties | NETWORK/NOT_DETECTED within that test’s scope; not global absence |
| RULE-06 | A named non-client adopts a traceable tool after exposure | PRODUCT candidate; test compensation, pre-existing use, evidence and attribution separately |
| RULE-07 | A participant forwards learning and a non-participant changes practice | KNOWLEDGE candidate with transmission/recipient evidence; direct participant learning remains separate |
| RULE-08 | Old collaboration intensifies after an intervention | STRENGTHENED network candidate; baseline, persistence and alternatives needed |
| RULE-09 | A buyer can stop after a learning phase; supplier has no follow-on entitlement | Buyer OPTION candidate; no supplier future-revenue guarantee or monetised premium inferred |
| RULE-10 | Sources disagree on economic totals/version | Preserve both; authority UNRESOLVED; withhold definitive combined figure |
| RULE-11 | A national programme receives funding; local bid success unknown | Do not assign the award to the local bid; programme identity verification action |
| RULE-12 | Distinctive method plus comparator city | No automatic causal estimate; identification assumptions needed |
| RULE-13 | Pricing or mandatory eligibility not reviewed | Gate UNKNOWN and recommendation HOLD regardless of high analytical score |
| RULE-14 | Lost bid, no debrief | Outcome needs evidence; loss cause UNKNOWN/hypothesis, not a calibrated lesson |
| RULE-15 | Named quote “permission pending” but no request record | INTERNAL_ONLY; permission UNKNOWN/NOT_REQUESTED; not REQUEST_SENT |
| RULE-16 | Citation points to same city but wrong project’s value | Reject precedent link; require the exact study and reviewed claim |
| RULE-17 | Row has unknown enum, duplicate/orphan ID or mismatched CSV columns | Structural validation fails before any release |
| RULE-18 | Source is a truncated extract and claim concerns unread appendix | Source coverage PARTIAL; claim unverified; request authorised original verification |
| RULE-19 | A report costs £5k and later phase is £2k cheaper | COST/observed price; no option valuation without flexible-versus-constrained comparison |
| RULE-20 | Public data contains identifiable relationships | Rights/privacy assessment required; public does not automatically mean consent NOT_APPLICABLE |
| RULE-21 | A free-text/descriptive field (e.g. `method_family`, `evidence_sufficiency`, `extraction_quality`, `scope_decision`, `assessment_status`) contains a controlled-vocabulary word that contradicts the controlled field (e.g. `review_status=UNREVIEWED` but `assessment_status` says "approved") | Structural validation flags the contradiction; the controlled field governs; the descriptive entry must be corrected or removed. Descriptive fields cannot override or mimic controlled fields. |
| RULE-22 | Analysis commences on a source document before ALL pages have been read | No analysis on unread content. Record read extent (pages read / total pages) in 02_sources.csv before commencing analysis. If full read is not possible (image-only, corrupted, tool limits), mark PARTIAL_EXTRACT and do not commence analysis until resolved. ToC, first 100/200 lines or partial extracts do not constitute a full read. |

## 15. Review, agreement and release protocol

At M1 freeze the exact bounded manifest and neutral packets before labels. R2 uses 12 claim units (8 diagnostic, 4 reserved transfer checks) and two opportunity packets. Record prior exposure honestly. Iain and Devin independently code the same packets, lock initial rows, then compare. AI audits are supporting checks, not an independent human or external specialist.

Key categorical fields: claim_type, effect_family, method_status where applicable, outcome_status, timing, fifth_sector_role, contracting_role, attribution_strength, value_status, value_basis, value_review_status and permission_status; option_state/subtype and tie_change for relevant cases. `method_family` is descriptive free text and is excluded from the agreement protocol. Predefine the applicability denominator. Report every field’s matching-pair count, eligible pair count and disagreements including UNKNOWN/N/A. Do not inflate agreement by counting missing fields; report non-UNKNOWN agreement separately. For fields with no applicable units, state not tested and the gap; do not report 100%.

M2 requires at least 80% initial agreement per agreed field and adjudication of every material disagreement, plus no unresolved critical defect and complete mandatory tender capture against Iain’s benchmark. Small-sample counts are reported; thresholds cannot be silently relaxed. For fields with fewer than 3 eligible pairs, report the raw count and state "insufficient for threshold test" rather than pass/fail on the 80% rule; Iain decides whether the field is adequately tested or needs more cases. Corrected labels do not replace initial agreement statistics. Critical unsupported effect/causal/rights/bid claims fail irrespective of the percentage. If a reserved transfer case exposes a critical rule failure, repair and seek approval for a new retest packet; an already exposed case is no longer fresh.

Source inability on a diagnostic’s essential question blocks its acceptance; seek an approved substitute or defer. Evidence uncertainty may be a correct answer, but do not call an unperformed check passed. M2 approval permits only the original pilot restart. M3 accepts a populated, recoded and reviewed pilot; G2 is a separate rollout decision. No source checks, agreement rates, adjudications or approvals have been completed by writing this candidate.

## 16. Version and maintenance log

| Version | Status | Change |
|---|---|---|
| 0.1 | Historical unvalidated pilot draft | Original definitions and templates |
| 1.0 | Historical unvalidated calibration claim | Retained for audit; narratives were not consistently recoded |
| 1.1-candidate | R1 design, M1 pending | Claim-type separation; independent method/evidence/timing/contract/value axes; missingness/rights/HOLD rules; both saved lens interpretations; traceable source and review protocol; proposed migrations and diagnostic examples |
| 1.2-candidate | R2-revised, awaiting approval | Six fixes from R2 adjudication: (1) claim_type vs method_status orthogonality clarified; (2) BID_SUPPORT_DELIVERED claim_type added with two-level commission/programme guidance; (3) VISIBILITY_OPTION_VALUE value_basis added; (4) OUTSIDE_PACKET evidence_status added with disclosure requirements; (5) contextual-vs-hypothesis primary classification rule added; (6) commercial experience as valid input for tender gate decisions clarified |
| 1.3-candidate | R2-revised, awaiting approval | Adds CO_AUTHORED_ANALYSIS as formal attribution code per Iain's D05 adjudication. Sits between DESCRIPTIVE (mere association) and CONTRIBUTION (causal contribution). Captures co-authored analytical work that identifies patterns without claiming causation. |

Any meaning change requires a candidate revision identifier, change description, affected-record map and gate decision. Preserve initial labels and old-to-new dispositions. Do not promote candidate to accepted merely because files exist or structural checks pass. Refresh claims when source authority, permission, project phase or observation window changes.