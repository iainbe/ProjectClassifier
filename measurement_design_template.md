# Measurement and Option Design — v1.1 candidate

**Template status:** R1 design; M1 pending. Blank protocol, not measurement results or approval for new data collection.
**Codebook:** `codebook_v1.1.md` (`1.1-candidate`)

## 1. Decision, claim and classification

| Field | Entry |
|---|---|
| project_id / opportunity_id / claim_id / method_ids | |
| review_batch / codebook_version / designer / date | |
| Buyer/holder decision and why the metric matters | |
| precise_proposition / claim_type / generating_intervention | |
| effect_family / mechanism / method_status | |
| outcome_status / intent / timing | |
| fifth_sector_role / contracting_role / fifth_sector_contribution | |
| attribution_strength / review_status | |

Use `04_claims.csv`, `03_methods.csv` and `06_measurements.csv`, linked through valid IDs. A baseline, a recommendation and an intervention effect are different claim types. Method status is separate from outcome evidence and timing.

## 2. Prediction, exposure and disconfirmation

| claim_id | prediction | Rival explanations | disconfirming_evidence | Event period / observation_window | Transmission/recipient evidence |
|---|---|---|---|---|---|
| | | | | | |

| measurement_id / metric | numerator | denominator / eligible population | unit | baseline value/source | geography / time_horizon | source_ids / locator |
|---|---|---|---|---|---|---|
| | | | | | | |

Record exposure definition, recipient boundary and compensation; sample frame, response/non-response, attrition, digital-visibility bias and denominator uncertainty. A larger digital count is not automatically a more accurate population estimate. Missing values remain blank with explanation, never fabricated zeroes.

## 3. Evidence and original-source quality

| source_id | Original type/date/version and locator | source_family_id / independence | authority_status | source_review_state / extraction warnings | Reviewer / original verification |
|---|---|---|---|---|---|
| | | | | | |

Use `02_sources.csv` and `05_evidence_links.csv`. Partial/unread sources cannot establish universal absence. Distinguish a reported need, hypothesised opportunity, first-hand change and independently corroborated occurrence. Preserve conflicting sources and limited test sensitivity.

## 4. Comparison and causal feasibility

| Design element | Specification / source / limitation |
|---|---|
| Estimand: effect of what, on whom, compared with what, over which period | |
| comparison / matching variables / baseline trajectory | |
| identification strategy / attribution_assumptions / causal_assumptions | |
| Selection/confounders, mediators/colliders and alternative mechanisms | |
| Sample adequacy, measurement comparability and missing data | |
| Spillover contamination/interference across comparison units | |
| Time-to-adoption or acceleration versus eventual adoption | |
| Sensitivity / falsification / robustness checks | |
| Specialist review needed and authorised route | |
| What can be concluded if identification is infeasible | |

A DAG exposes assumptions, not proof. Geographic benchmarks, international precedents and dataset disagreement are not counterfactual impact estimates by themselves. Use bounded contribution/process tracing where justified; otherwise keep attribution unassessed/descriptive. Do not escalate because the approach is distinctive.

## 5. Diffusion and network indicators

| Indicator | Definition / baseline | Recipient / denominator | Data and observation times | Comparison/rival | Evidence needed / limitation |
|---|---|---|---|---|---|
| Adoption and adaptation | | | | | |
| Time-to-adoption | | | | | |
| Changed practice / onward knowledge transfer | | | | | |
| tie_change: NEW / REACTIVATED / STRENGTHENED / PRE_EXISTING / UNKNOWN | | | | | |
| Collaboration activity and tie persistence | | | | | |
| Network density / bridging, if appropriate | | | | | |

Set a justified persistence window rather than a universal threshold. Shared directors, co-location, event attendance and static centrality alone do not establish new durable spillovers. A specified no-detection result is scoped to that test; unavailable follow-up is NOT_ASSESSED.

## 6. Monetary information and double-counting control

| claim_id / measurement_id | value_status | value_basis | value_review_status | amount_role | unit / currency_price_basis | calculation / model_version / source_ids |
|---|---|---|---|---|---|---|
| | | | | | | |

- value_status: UNQUANTIFIED / NON_MONETARY / MONETARY / MIXED / NOT_APPLICABLE / UNKNOWN.
- value_basis: OBSERVED_AMOUNT / DESCRIPTIVE_ESTIMATE / SCENARIO_ESTIMATE / NONE / UNKNOWN / NOT_APPLICABLE.
- value_review_status: NOT_REVIEWED / REVIEWED / DISPUTED / NOT_APPLICABLE.
- amount_role: COST / BENEFIT / ECONOMIC_BASELINE / OTHER / NOT_APPLICABLE / UNKNOWN.

| Valuation safeguard | Entry |
|---|---|
| Price year, unit, geography and event period | |
| sensitivity / uncertainty / probability_basis where applicable | |
| overlap_group_id / related direct-indirect-induced/spillover claims | |
| Leakage, displacement, substitution and distribution | |
| Which costs/benefits already appear elsewhere in the account | |
| Reviewer / review_date / original evidence | |

A region’s monetary GVA baseline is not consultancy-created benefit. A fee is a COST, not option value. Separate composite amounts and claims; no invented precision or sensitivity range. Multipliers require appropriate geography/year/sector assumptions and do not price flexibility or prove causation.

## 7. Strategic option register (if applicable)

| Field | Entry |
|---|---|
| claim_id / option_subtype | |
| option_state — PROPOSED / FEASIBLE_CREATED / MAINTAINED / EXERCISED / DEFERRED / EXPIRED / UNKNOWN / NOT_APPLICABLE | |
| outcome_status — evidence for the claimed state | |
| option_holder / feasible choice or decision right | |
| Enabling capability/investment / information gained / uncertainty | |
| exercise_access / access constraints | |
| exercise_trigger / expiry or horizon | |
| exercise_cost / maintenance_cost / delay_cost | |
| constrained_alternative / scenarios / probability_basis | |
| Benefits / cost bearers / distribution | |
| State-change evidence / source_ids / original locator | |

Do not equate a proposed sequence with an exercised option. Distinguish buyer discretion from supplier entitlement, and user access from merely owning a licence. An unexercised option may still have value; absence of an established scenario means value is unassessed, not automatically negligible.

### Flexible-versus-constrained comparison

| Element | Flexible strategy | Constrained alternative | Source / assumption / uncertainty |
|---|---|---|---|
| Decisions available and timing | | | |
| Enabling and learning costs | | | |
| Maintenance/exercise/delay costs | | | |
| Benefits under consistent scenarios | | | |
| Discounting, demand, expiry and irreversibility | | | |
| Net result / incremental flexibility value if defensible | | | |

Disclose whether enabling/learning/maintenance costs are already counted. Do not add the full eventual investment payoff again as an option premium or subtract speculative option value from Phase 1 fees. Non-monetary decision analysis is acceptable when monetary valuation is not supportable.

## 8. Distribution, ethics, data access and stopping rules

| beneficiaries / cost_bearers | access_barriers / direction | Non-adopters, informal or missing actors | Adverse effects / lock-in / displacement | Evidence/action |
|---|---|---|---|---|
| | | | | |

| Data / source | Access mechanism and authorised scope | rights_status / evidence | consent_status / legal/privacy assessment | Retention/security/owner | permission_status / permitted use |
|---|---|---|---|---|---|
| | | | | | |

Public availability does not automatically establish lawful linkage, licence, consent exception or client permission. New interviews, outreach, restricted data, uploads and software require separate approval.

| Decision gate | Decision / information needed | Timing / go-stop criteria | Owner | Approval reference / validation_id / stopping_rule |
|---|---|---|---|---|
| | | | | |

| Follow-up activity | Owner / observation times | Data/access/consent needed | Effort/cost basis | Approval / stopping rule |
|---|---|---|---|---|
| | | | | |

Use `07_validation_actions.csv`. Stop, qualify or withhold a claim when further work is infeasible or disproportionate; a valid stop decision need not be a programme failure.

## 9. Both saved lens protocols and review history

| Lens | Question | Evidence | Finding | Limitation / action or N/A |
|---|---|---|---|---|
| B /skin | What participant account distinguishes need, intended benefit and actual change? | | | |
| B /thad | What pattern is predicted, with which denominator/horizon and disconfirmation? | | | |
| B /deepthink | What contribution/causal reconstruction is supportable and what rivals remain? | | | |
| B /blindspot | What effects, actors, access barriers, costs or expired options are outside the frame? | | | |
| A /skin | Are metric and value claims bounded and testable? | | | |
| A /thad | Does the measurement serve a real decision with a usable output and adequate proof? | | | |
| A /deepthink | Do sources, units, periods, assumptions and linked records reconcile? | | | |
| A /blindspot | What would an evaluator, finance, privacy or delivery reviewer challenge? | | | |

| Review item | Entry |
|---|---|
| Locked initial coder review IDs and same source packet | |
| Initial agreement / applicability disagreements | |
| ADJUDICATION / RECODE / SOURCE_CHECK review IDs | |
| Second/specialist reviewer, date and limits | |
| Approved use / next gate or withheld status | |

Use `10_review_history.csv` for append-only initial labels, source checks and adjudications. All findings, approval references and reviewer outcomes here remain blank until actually performed within authorised scope.