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

- Set `programme_status=NOT_AWARDED` at project level
- Set `option_state=EXPIRED` on OPTION claims
- Do not treat unsuccessful bids as live strategic options
