# AGENTS.md — Spillover Toolkit Working Rules

## Project differentiation rule

**Never assume that claims, sources or projects sharing a geography or client are the same project.**

Before assigning a claim or source to a project:

1. **Check the project description** in `01_projects.csv` — does the claim proposition match the project's `scope_decision` and `sector_activity`?
2. **Check the archive folder** — does the source file come from the same archive year and folder as the project's `drive_folder_path`?
3. **Check the date** — a 2021 report and a 2022 report for the same client are different projects.
4. **Check the document type** — a completed report, a feasibility study, and an unsuccessful bid are three different projects even if they share a client and geography.
5. **Check for empty `project_id`** — empty project_id means "not yet assigned", not "assign to the nearest matching project".

### Known multi-project geographies

These geographies have multiple distinct projects that must not be conflated:

- **Derby**: P35-DERBYMAP (2021 Masterplan), P23-DERBY (2022 Screen Agency), P36-DERBYCSR (2026 bid, unsuccessful)
- **Liverpool**: P08-LIVDCI, P15-LIVMUS, P19-LCRIMM, P22-LCRFILM, P33-LCRMUS
- **Kirklees**: P10-KIRK (2022-2026 cycles), P12-KIRK15 (2015)
- **South Yorkshire**: P20-SYMCA21, P24-SYMCACGP
- **Wakefield**: P27-WAKECDF, P31-PRODPARK
- **Solent**: P29-SOLENTCGP (bid), P34-SOLENTHANTS (mapping)
- **Manchester**: P02-FGTG, P03-MITIH, P06-COSTAR, P07-CC, P21-MMUCCI

### Conflation check procedure

When reviewing claims:

1. For each claim, verify the `project_id` matches the project's actual scope.
2. If a claim mentions a different geography, sector or time period than the project, check whether this is a legitimate cross-sector reference (comparator, spillover target) or a misassignment.
3. A comparator (e.g., "Liverpool Film Office as a benchmark for Derby") is legitimate. A claim about Liverpool Film Office's outcomes assigned to a Derby project is not.
4. When creating new project records, check the archive folder structure to confirm the project is distinct.

## Claim classification rules

### METHOD_OUTPUT vs CONTEXT

A **sector baseline** (GVA, employment, company count, turnover, LQ) measured by a mapping or strategy report is **CONTEXT**, not METHOD_OUTPUT.

Codebook rule: "A mapping report estimating regional GVA is CONTEXT with a descriptive estimate, not value created by the consultant."

METHOD_OUTPUT is reserved for:
- Programme delivery data (e.g., "Film Fund generated £12.08m spend")
- Analytical method application (e.g., "SNA of 272 businesses shows...")
- Evaluation approach design (e.g., "CICP evaluation approach designed with...")

### EFFECT vs CONTEXT

A sector characteristic (e.g., "Adlib Audio serves major touring productions") is **CONTEXT**, not EFFECT. An EFFECT requires evidence of change caused by an intervention, not just a description of an existing state.

### Programme effect vs Fifth Sector contribution

When Fifth Sector was the **evaluator** of a programme, programme effects are real but Fifth Sector's contribution was the evaluation. Set `fifth_sector_role=EVALUATOR` on the claim. Do not imply Fifth Sector caused the programme effect.

### Option state

All OPTION claims must have `option_state` set:
- PROPOSED: option proposed in a report or strategy
- EXERCISED: option was taken up
- EXPIRED: option from an unsuccessful bid or expired programme
- UNKNOWN: option status not yet confirmed

## Source verification rules

### Full-read rule

Before analysing any source, confirm all pages have been read. If not fully readable, mark as PARTIAL_EXTRACT or NOT_ASSESSED. Do not infer absence of an effect from an incomplete extract.

### Spot-check priority

Spot checks should prioritise:
- High-risk numerical claims (GVA, FTE, multiplier, leverage)
- High-risk causal claims (strong verbs: "caused", "enabled", "instrumental")
- EFFECT claims
- Claims with inconsistent figures
- Claims involving unsuccessful bids or expired options
- Claims with mixed data sources (BRES, LinkedIn, IDBR, Beauhurst)

## Attribution rules

### BOP-associated work

For work done by Iain as BOP Associate Director:
- `fifth_sector_role=EVALUATOR` (or DESIGNER, DELIVERER as appropriate)
- `contracting_role=ASSOCIATE`
- Do not infer Fifth Sector direct delivery from BOP work

### Unsuccessful bids

- Set `lifecycle_status=NOT_AWARDED` at project level
- Set `option_state=EXPIRED` on ALL DESIGN and OPTION claims for that project (not just OPTION effect_family)
- Do not treat unsuccessful bids as live strategic options
- Check: any DESIGN claim where `project_id` has `lifecycle_status=NOT_AWARDED` must have `option_state=EXPIRED`

## Forecast vs realised outcome rule

A forecast in an interim evaluation is NOT a realised outcome. Before treating a forecast as an effect or exercised option:

1. Check whether a final evaluation exists. If so, compare the interim forecast with the final outcome.
2. If the final evaluation does not confirm the forecast, set `option_state=EXPIRED`.
3. If no final evaluation exists, set `option_state=UNKNOWN` and add a validation action.
4. Never present a forecast figure as a confirmed outcome without a later source confirming realisation.

Example: C-G2-041 Development Fund 7.8:1 leverage forecast (2021 interim) was NOT confirmed in the 2025 final evaluation. The 7.8:1 figure in the final evaluation was a hypothetical scenario ratio, not a realised Development Fund outcome. option_state set to EXPIRED.

## value_basis rule

Every claim containing a monetary figure (£) must have `value_basis` set:

| claim_type | value_basis |
|------------|-------------|
| CONTEXT (sector baseline) | DESCRIPTIVE_ESTIMATE |
| CONTEXT (modelled estimate) | DESCRIPTIVE_ESTIMATE |
| METHOD_OUTPUT (programme output) | OBSERVED_AMOUNT |
| DESIGN (forecast) | SCENARIO_ESTIMATE |
| EFFECT (measured) | OBSERVED_AMOUNT |
| BID_SUPPORT_DELIVERED | OBSERVED_AMOUNT |

Check: scan all claims for `£[\d.]+` in `precise_proposition` and verify `value_basis` is non-empty.

## Rival explanations rule

For testimony-based EFFECT claims (where evidence is a stakeholder quote, not counterfactual analysis):

1. Keep as EFFECT/DESCRIPTIVE if the testimony is from a credible source.
2. Add `rival_explanations` noting all contributing factors and actors.
3. Do not imply sole causation from testimony alone.

Example: C-G2-056 CoSTAR attribution — testimony-based; rival_explanations added noting University of York, Wakefield Council, Production Park and national CoSTAR programme as co-contributors.

## Tender vs project distinction

Tender documents (RFQs, RFPs, ITQs, bid responses) for unsuccessful or pending bids are NOT projects. They belong in `08_tenders.csv` only. Do not create project records for:

- Unsuccessful bids (lifecycle_status=NOT_AWARDED in tenders)
- Pending tenders awaiting decision
- Pipeline opportunities

Sources linked to tender documents may have empty `project_id` — this is correct, not an error.

## QA verification checklist

Before completing any QA batch, run ALL of these checks:

1. **Unique IDs**: all registers have unique primary keys
2. **Foreign keys**: claims→projects, sources→projects, evidence→claims, evidence→sources, measurements→claims
3. **Empty project_id on claims**: all claims must have a project_id (except tender-only sources)
4. **OPTION claims without option_state**: all claims with `effect_family=OPTION` must have `option_state`
5. **Empty effect_family**: no claims with empty `effect_family`
6. **Empty fifth_sector_role**: no claims with empty `fifth_sector_role`
7. **DESIGN claims for unsuccessful bids**: if `project_id` has `lifecycle_status=NOT_AWARDED`, `option_state` must be `EXPIRED`
8. **EFFECT claims without attribution_strength**: all EFFECT claims must have `attribution_strength`
9. **Claims with £ figures but empty value_basis**: all claims with `£[\d.]+` in proposition must have `value_basis`
10. **Sector baselines mislabelled as METHOD_OUTPUT**: scan METHOD_OUTPUT claims for baseline patterns (GVA, employment, turnover, LQ, company count) and verify they are genuine method outputs
11. **Conflation check**: claim geography vs project geography — flag mismatches that aren't comparators
12. **Strong causal verbs in non-EFFECT claims**: scan for "caused", "enabled", "instrumental", "catalysed" in CONTEXT/DESIGN claims; review semantically (some are descriptive, not causal)
13. **Sources with empty project_id**: verify these are tender pipeline items, not missing assignments

## Live-work capture rules

### Bid submission trigger
When informed a bid was submitted: copy `bid_submission_record_template.md` to `bid_records/TXX_<name>.md` (bid_id = next `T-NN` from `08_tenders.csv`) and ask for any empty fields in sections 1-4 — especially `fifth_sector_contribution` (specific sections/frameworks, never generic "bid support") and `interview_involvement`. Add row to `08_tenders.csv`; add `01_projects.csv` row only if the bid work is a paid commission or deliverable body (P06/P07 precedent). See `register_update_workflow.md`.

### Bid outcome trigger
On any outcome mention: complete record section 5. Always establish `stage_reached` (highest stage, not just final result) and `notification_type` — never infer "failed" from "not awarded". Then run the section 6 register checklist.

### Project confirmation trigger
When a project is confirmed: copy `project_management_record_template.md` to `project_records/PXX-<name>_pm.md` and ask for empty fields in sections 1-3 — especially `contracting_role` (the ARRANGEMENT, not ownership), named contributors, and `reference_permission` (prompt Iain to ask the client at kickoff). Add register row + provisional index card.

### Milestone trigger
At each milestone mention: append a Milestone section to the PM record. Ask the section-5 prompts — `spillover_observed` (with source) and `problems` (record rejections as they happen).

### Schema-drift rule
Before ANY CSV edit: verify field count AND positional semantics against the header. Right column count ≠ right values — check 2-3 existing rows first. (Pass 4 repair lesson.)

### Stale-artefact rule
After card or register changes: regenerate `project_index.csv`.

### Repo sync
Canonical = this Drive folder. `ProjectClassifier/` repo is the versioned mirror — sync after register-changing sessions, commit with the trigger named, push only when asked.

### Date format convention
All dates use `YY/MM/DD` (e.g., 26/09/12). Month-precision: `YY/MM`. Year-only in date fields: `YY`. Timestamps: `YY/MM/DDThh:mm:ss`. Applies to all registers, cards, changelogs, records and fields. EXCEPTION: `extracted_text/` source files remain verbatim — never normalise dates inside source evidence. `tools/normalise_dates.py` implements the conversion rules.

### Session-closure rule (MANDATORY — no reminders needed)
Before ending ANY work session that changed toolkit files, update ALL THREE:
1. `CHANGELOG.md` — session-level entry (what changed and why)
2. `tier2_qa_review.md` — consistency-audit entry (findings, fixes, residual issues)
3. `10_review_history.csv` — audit-trail row
Plus per-project `project_changelogs/` entries for any project whose data/card changed.
A session is NOT complete until these are written. This is not optional and does not require a user reminder.

### Session-start rule
At the start of any toolkit session: check `sweep_reports/SWEEP_LATEST.md` for new Drive findings (unregistered projects, possible tenders, unregistered sources, register drift) and surface anything needing attention before other work.
