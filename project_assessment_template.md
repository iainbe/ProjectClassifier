# Project Assessment Sheet — v1.1 candidate

**Template status:** R1 design; M1 pending. Blank template, not an assessment or approval.
**Codebook:** `codebook_v1.1.md` (`1.1-candidate`)
**Scope:** R2 only after M1; full pilot after M2. Do not populate from historical narratives without source verification.

## 1. Identity, scope and provenance

| Field | Entry |
|---|---|
| project_id / canonical_name / aliases | |
| parent_project_id / phase_name | |
| client / prime_contractor | |
| date_start / date_end (precision known) | |
| lifecycle_status — consultancy commission | |
| programme_status — underlying programme | |
| fifth_sector_role — analytical role | |
| contracting_role / relationship_evidence | |
| sector_activity / geography / scope_decision | |
| intended_beneficiaries / project_objectives | |
| source_coverage / expected source set / actual read scope | |
| assessment_owner / assessment_status | |
| review_status / review_batch / codebook_version | |

Use `01_projects.csv`. Keep COMPLETED consultancy delivery separate from an AWARDED/NOT_AWARDED/UNKNOWN programme. Do not infer contract role from a filename. All codes must match the candidate codebook; not entered is not a passed or inapplicable check.

| source_id | Actual document_type / date_version | Original / derived location and locator | authority_status / rationale | source_family_id / independence | source_review_state / warnings |
|---|---|---|---|---|---|
| | | | | | |

Use `02_sources.csv`. Record partial extraction, uninspected figures/tables, superseded versions and inaccessible evidence. Source-level quality is not a substitute for claim-level support. Missing source or incomplete review does not imply no effect.

## 2. Methods and atomic claims

| method_id | Method / contemporary terminology | method_status | Purpose / work product | source_ids / exact application evidence | claim_ids / limitation |
|---|---|---|---|---|---|
| | | | | | |

Use `03_methods.csv`: NOT_IDENTIFIED / PROPOSED / APPLIED / CORROBORATED / UNKNOWN. A promise of a method is not an applied method.

| claim_id | precise_proposition | claim_type | effect_family / mechanism | outcome_status / timing | attribution_strength | review_status |
|---|---|---|---|---|---|---|
| | | | | | | |

Create atomic rows in `04_claims.csv`. Claim types: CONTEXT / METHOD_OUTPUT / DESIGN / DECISION_USE / EFFECT / UNKNOWN. Split monetary values, counts and causal conclusions. Context normally has effect_family NOT_APPLICABLE. Do not insert NULL, FORECAST or BID_STAGE into the wrong axis.

### Complete for each retained claim (repeat as needed)

| Field | Entry / linked record |
|---|---|
| claim_id / method_ids | |
| generating_intervention / originator / recipient | |
| fifth_sector_contribution / fifth_sector_role / contracting_role | |
| event_period / observation_window / intent / timing | |
| boundary_recipient / boundary_org / boundary_sector / boundary_geography / boundary_chain / compensation | |
| prediction / rival_explanations / disconfirming_evidence | |
| tie_change / baseline ties / activity / persistence window | |
| option_subtype / option_state / option_holder / exercise_access | |
| direction / beneficiaries / cost_bearers / access_barriers | |
| value_status / value_basis / value_review_status / measurement_id | |
| source_review_state / coverage / source_quality / independence / time_lag | |
| contrary_evidence / evidence_sufficiency / reviewer_confidence | |
| causal_assumptions / identification limit | |
| commercial_reuse / permission_status / rights_status / consent_status / publication_status | |
| validation_id for unresolved evidence | |

| evidence_id | claim_id / source_id | Original page/section/table/cell | Derived locator | Necessary extract/observation | supports_or_contradicts | Source-family dependence / limitations |
|---|---|---|---|---|---|---|
| | | | | | | |

Use `05_evidence_links.csv`; measurements belong in `06_measurements.csv`. Refer to the measurement template for denominators, comparison, uncertainty, costs/baselines, option alternatives and overlap. No causal estimate from a distinctive method or comparator alone.

## 3. B — Original-methodology lenses (evidence analysis)

These are saved manual interpretations, not claimed canonical installed skills. Record evidence or a reasoned not-applicable result. No simulated interviews.

| Lens | Question | Evidence / source and locator | Finding | Limitation / rival | validation_id or N/A reason |
|---|---|---|---|---|---|
| B /skin — testimony | What is reported: need, intention or experienced change? First-hand? When? What corroborates it? | | | | |
| B /thad — predicted patterns | What observable pattern follows from the mechanism, for whom, by when? What would disconfirm it? | | | | |
| B /deepthink — causality | What changed relative to baseline; what alternatives, selection or interference remain? | | | | |
| B /blindspot — outside frame | Which actors, non-adopters, informal activity, adverse effects, unequal access or expired options are missing? | | | | |

## 4. A — Review-pass lenses (quality of the resulting assessment)

| Lens | Question | Evidence / reviewed record | Finding | Limitation | Action / N/A reason |
|---|---|---|---|---|---|
| A /skin — claim hygiene | Is every statement specific, current, bounded and testable? | | | | |
| A /thad — purpose/product/proof | What buyer/review decision, usable output and proof does it support? | | | | |
| A /deepthink — consistency | Do source versions, tables, status codes, numerical claims and precedent links agree? | | | | |
| A /blindspot — adversarial review | What would a sceptical commissioner, commercial or rights reviewer challenge? | | | | |

## 5. Summary and disposition

| Question | Source-linked answer / claim IDs |
|---|---|
| What was commissioned and actually done? | |
| What is evidenced method capability versus a proposed method? | |
| What is contextual finding, decision use, observed change or intended effect? | |
| Is any spillover transmission or feasible option established, and for whom? | |
| What belongs to the generating programme/client/partners versus Fifth Sector? | |
| What evidence contradicts or limits the findings? | |
| What would change the conclusion, and what is the proportionate stopping rule? | |
| What wording/use, if any, is permissible under actual rights evidence? | |

Do not turn an unreviewed remainder into a portfolio-wide absence claim. An outcome may remain unknown while method capability is documented. No comparative-superiority claim without comparative evidence.

## 6. Validation and independent review

| validation_id | claim_id / source_id / issue_id | Open question | Proposed next step / gate | Access/consent / owner | Stopping rule / approval_status |
|---|---|---|---|---|---|
| | | | | | |

Use `07_validation_actions.csv`; an action row is not outreach permission.

| Review item | Entry |
|---|---|
| Same source packet / cutoff / candidate version supplied to both coders | |
| Prior exposure and independence limits | |
| First-coder locked INITIAL_CODE review IDs | |
| Iain’s locked INITIAL_CODE review IDs | |
| Field-level initial agreement counts and applicability disputes | |
| ADJUDICATION review IDs / unresolved or withheld claims | |
| RECODE review IDs / superseded parents and successor claims | |
| Second reviewer / date / review_status | |
| Permitted next gate and explicit approval reference | |

`10_review_history.csv` is the append-only record of separate initial labels and adjudications. This sign-off section references it, not a replacement history. AI checks do not substitute for Iain’s independent initial coding or specialist review. Do not prefill approval, agreement or REVIEWED status.