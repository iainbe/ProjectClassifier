# Tender / Opportunity Scorecard — v1.1 candidate

**Template status:** R1 design; M1 pending. Blank template, not bid advice or submission authority.
**Codebook:** `codebook_v1.1.md` (`1.1-candidate`)

## 1. Intake and as-at boundary

| Field | Entry |
|---|---|
| opportunity_id / buyer / opportunity_type | |
| document_version / source_ids / procurement_route | |
| assessment_mode — AS_AT_TEST / LIVE_REVIEW / DIRECT_PROPOSAL_REVIEW | |
| as_at_date / precise source cutoff (retain in notes) | |
| prior_exposure / known historic outcome / hindsight limits | |
| deadline / deadline_timezone / clarification_deadline | |
| Submission route / format / page-word limits / contradictory dates | |
| budget_stated / exclusions / fee versus verified margin | |
| Required attachments / missing documents / hierarchy of clarifications | |
| review_batch / codebook_version / review_status / assessor | |
| requirement_map_location / gate_profile_location (this saved scorecard and section) | |

Use `08_tenders.csv`; register source identities in `02_sources.csv`. A direct-client proposal is not a buyer-issued tender. Do not obtain new evidence, contact the buyer or submit anything without the appropriate gate.

| source_id | Source type | Original document_type / version / date | Actual authority and cutoff eligibility | Original/derived locators | source_review_state / gaps |
|---|---|---|---|---|---|
| | | | | | |

Source type: BUYER_TENDER / BUYER_CLARIFICATION / CLIENT_DISCOVERY / SUPPLIER_PROPOSAL / INTERNAL_REVIEW / AWARD_DEBRIEF / OTHER / UNKNOWN. This describes evidential role; source document_type describes the actual document. Existing relationship or supplier assertions do not prove compliance.

## 2. Requirement map — exact buyer evidence first

Use stable local IDs such as `<opportunity_id>-REQ-01`; no requirements are filled here. Record unavailable clauses/annexes as gaps, not invented buyer wording.

| Requirement ID | source_id / type / version/date | Exact wording and original locator | Mandatory/scored? Weight/threshold if stated | Fifth Sector interpretation | Response evidence / precedent_claim_ids | Gap/conflict / gate ID |
|---|---|---|---|---|---|---|
| | | | | | | |

Buyer criteria weights are not internal attractiveness weights. Include technical brief, exclusions, deadlines/timezones, format/length, contract, IP/data, access and mandatory capability. Do not replace a buyer quotation with the wording of our proposal.

## 3. Procurement gates

| Gate ID / topic | Requirement IDs | Blocking? (reason) | PASS / FAIL / UNKNOWN / NOT_APPLICABLE | Exact source / evidence / locator | Reviewer rationale | Escalation owner / validation_id |
|---|---|---|---|---|---|---|
| GATE-01 Mandatory eligibility and submission compliance | | | | | | |
| GATE-02 Delivery capacity and timetable | | | | | | |
| GATE-03 Required partners/specialists | | | | | | |
| GATE-04 Conflict check | | | | | | |
| GATE-05 Pricing and margin feasibility | | | | | | |
| GATE-06 Contractual exposure | | | | | | |
| GATE-07 IP/data/privacy requirements | | | | | | |
| GATE-08 Missing/conflicting instructions | | | | | | |

**Blocking UNKNOWN → HOLD.** FAIL must be resolved or lead to NO_BID; it cannot be outweighed by a score. NOT_APPLICABLE needs an evidence-based reason. Known relationships do not clear conflicts, quoted fees do not verify margins, and a platform description does not demonstrate available capability. Gates, blocking decisions and owners above are deliberately blank.

## 4. Buyer-decision relevance and methods

| Buyer decision / requirement IDs | Proposed improvement | Mechanism and intended recipient | Scope/cost and scored relevance | Evidence/alternative explanation | positioning_rationale |
|---|---|---|---|---|---|
| | | | | | |

| Effect family | EXPLICIT / IMPLICIT / ABSENT / UNCLEAR in reviewed buyer material | source_id / locator | Beneficiaries / pathway / uncertainty | Proposed data and observation window | Exercise choice/holder (options only) |
|---|---|---|---|---|---|
| PRODUCT | | | | | |
| KNOWLEDGE | | | | | |
| NETWORK | | | | | |
| OPTION | | | | | |

No automatic spillover lead because multipliers are mentioned; no automatic exclusion because a tender asks for an EIA. Describe a platform as proposed/unverified until its relevant capability is evidenced. Buyer choice over later phases is not supplier entitlement to follow-on revenue.

## 5. Scoring profile — no aggregate total

0 = demonstrated mismatch; 1 = weak/indirect; 2 = credible with specified conditions; 3 = strong/direct; U = insufficient evidence; N/A = justified non-applicability. Never turn UNKNOWN into zero or let missing fields increase a total. Low spillover relevance is not automatically poor commercial fit.

| Dimension | Score | Source-linked rationale | Conditions / gaps / clarification action |
|---|---|---|---|
| Relevance to buyer problem and scored criteria | | | |
| Credibility of proposed spillover mechanism or future option | | | |
| Ability to influence design within scope and budget | | | |
| Feasibility of observation and additionality testing | | | |
| Availability/relevance of reviewed usable precedents | | | |
| Delivery/commercial fit, separately from effect potential | | | |

## 6. Decision and candidate response

| Field | Entry |
|---|---|
| bid_recommendation — HOLD / BID / CONDITIONAL_BID / NO_BID | |
| Rationale / blockers / assumptions | |
| Remaining non-blocking conditions and owners | |
| Iain’s commercial reviewer approval / date / review IDs | |

CONDITIONAL_BID requires mandatory gates resolved, documented non-blocking conditions and Iain’s approval. It is not a workaround for a blocking unknown or permission to submit. AS_AT_TEST is a historical diagnostic, not a current bid recommendation.

| Candidate win theme | Exact precedent_claim_ids / method relevance | Proposed wording (not presumed cleared) | Study identity/role/maturity check | commercial_reuse / permission_status / rights evidence |
|---|---|---|---|---|
| | | | | |

A numerical precedent from one study cannot be attributed to another study in the same city. Keep proposed themes internal until exact wording/use is approved.

| Proposed method | Base scope | Optional enhancement | Cost basis / uncertainty | Measurement design / validation_id |
|---|---|---|---|---|
| | | | | |

Use `measurement_design_template.md` and linked 06/07 records. Clarification questions are internal drafts; sending them requires separate authorisation.

## 7. Both lens interpretations — separately recorded

| Lens | Question | Evidence | Finding | Limitation / action or N/A |
|---|---|---|---|---|
| B /skin — testimony | What do authorised client/participant accounts actually establish, rather than imply? | | | |
| B /thad — predictions | What outcome pattern would the proposed mechanism create; what would disconfirm it? | | | |
| B /deepthink — causality | What would a valid comparison require, and what cannot be inferred from this proposal? | | | |
| B /blindspot — outside frame | What beneficiaries, adverse effects, access barriers and later choices are omitted? | | | |
| A /skin — wording | Is every requirement/capability/precedent claim precise and bounded? | | | |
| A /thad — purpose/product/proof | Is this solving the buyer’s decision with an appropriate deliverable and proof? | | | |
| A /deepthink — consistency | Do buyer text, proposal scope, price, terms, deadlines and precedent identities agree? | | | |
| A /blindspot — evaluator | What would a sceptical procurement, delivery or privacy reviewer reject? | | | |

These are the two saved manual protocols, not claimed canonical installed skills. Separate B conclusions from A quality judgements.

## 8. Actual outcome and feedback — separate from as-at test

| Field | Entry |
|---|---|
| actual_outcome — UNKNOWN / WON / LOST / WITHDRAWN / NO_DECISION / NOT_APPLICABLE | |
| outcome_source_id / locator / date | |
| feedback_status — NOT_OBTAINED / DOCUMENTED / UNVERIFIED | |
| feedback_source_ids / exact feedback / date | |
| Hypothesised explanation / alternatives / evidence needed | |
| Effect of prior knowledge on original assessment | |

A folder called “lost”, or a loss alone, does not establish outcome reason. Do not turn positioning hypotheses into calibration lessons without evidence.

## 9. Risks, validation and independent review

| Issue / validation_id | Description | Source or gap | Owner / approved action / gate | Stopping rule |
|---|---|---|---|---|
| Overclaiming / wrong precedent | | | | |
| Inaccessible data / missing requirement | | | | |
| Uncontrollable adoption / interference | | | | |
| Uneconomic evaluation / unfunded later phases | | | | |
| Rights/privacy / permission not obtained | | | | |

| Review item | Entry |
|---|---|
| Iain’s source-based mandatory-requirement benchmark | |
| Locked first/second INITIAL_CODE review IDs / initial field agreement | |
| ADJUDICATION review IDs / unresolved disagreements | |
| Commercial reviewer / date / approved next scope | |

Keep initial labels and adjudications in `10_review_history.csv`; references here are not a replacement history. No gate decision, review result or permission has been prefilled.