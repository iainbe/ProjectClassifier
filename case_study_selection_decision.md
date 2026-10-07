# Case-study selection scheme — decision state

**Status: PROPOSED, awaiting Iain's encoding decision. Nothing implemented.**
**Date:** 26/10/07

This document captures the ontology, the classification scheme and the storage options exactly as reviewed, so the decision can be taken without re-running the analysis. No register or schema changes have been made on this basis.

## 1. The ontology

Five entities:

| Entity | Definition | Current home |
|---|---|---|
| Project | The thing done — the substance | `01_projects.csv`, index cards |
| Case study | A telling of a project for a specific tender — a derived artefact | Nowhere — produced ad hoc per bid |
| Tender requirement | What the buyer asks to see, in their scoring language | `08_tenders.csv` |
| Referee | A person + permission state + contact | `11_permission_requests.csv` |
| Criterion | The scoring item the case study is serving ("comparable work", "proven record", "relevant experience") | `08_tenders.csv` notes; not modelled |

Project attributes that decide selection, and whether the register holds them:

| Attribute | Register coverage |
|---|---|
| Work genre | `sector_activity` — 40+ free-text values, needs domain rollup |
| Client type | `client_type` — populated |
| Geography | `geography` — populated |
| Scale | `contract_value` — on cards only, thin |
| Recency | `date_start` / `date_end` — populated |
| Role | `fifth_sector_role` populated; `contracting_role` empty on 26/68 projects |
| What was measured | `effect_family` on claims (CONTEXT / METHOD_OUTPUT / EFFECT / OPTION) |
| Method currency | `03_methods.method_status` — only APPLIED / PROPOSED in use; no SUPERSEDED |
| Delivered state | `lifecycle_status` — populated |
| Nameable | `citation_status` — present on 58/68 cards |
| Referee available | `reference_permission` on cards + `11_permission_requests.csv` |

Demand-side domains (derived from 22 tenders + 68 projects; open and demand-led — new tender demand creates domains):

1. Sector mapping / economic baseline
2. Institutional/venue impact
3. Programme/fund evaluation
4. Framework/method design
5. Strategy/policy
6. Data/digital infrastructure
7. Skills/business support
8. Heritage/visitor economy
9. Research/consortium support

Cross-cutting tender lens (not a domain): contribution-framed vs descriptive briefs — boosts measured-change evidence wherever it sits.

## 2. The classification scheme

**Stage 0 — hard gates** (binary; a fail excludes):
- `lifecycle_status` = COMPLETED and client-accepted
- `citation_status` in {PUBLIC_REPORT, DELIVERED_WORK}
- Referee ESTABLISHED or verbally secured for this tender
- Method not superseded in an answer-changing way

**Stage 1 — intrinsic tier** (standing; populated lazily, gate-passers only — ~20 projects):
- FLAGSHIP: delivered <=3yr, TFS prime+lead, measured change/spillovers, current method
- STRONG: TFS-led, solid evidence, current method
- SUPPORTING: older, narrower, associate-led (worded as personal track record), or descriptive
- LEGACY: superseded method or weak attribution evidence
- Excluded: NOT_AWARDED projects (expired options are not delivery evidence)

Intrinsic signals, three classes evidenced so far:
- Delivery evidence — completed paid work (P75-LANC)
- Method transfer — client adopted the output and applied it themselves; strongest when externally validated (P85-AMGEN: USW applied Places evidence in own submission, shortlisted; P87-TRUENORTH: same reuse pattern, no validation)
- Supersession — older method where the newer approach would change the answer (P16-CICP: 5+yr, associate, design-only)

**Stage 2 — per-tender fit**: domain match, client type, geography, scale credibility, referee warmth. Fit drives selection; tier tiebreaks. Maximise domain coverage across a multi-strand brief.

**Stage 3 — composition** (separate from selection): sheet-ready headline figure, comparability first line, permitted wording (associate = "as BOP Associate Director"; design = "designed the evaluation approach"), referee named. The case-study artefact records: which projects used, wording used, tender, score received — the learning loop.

## 3. Storage options — parameters

**A. Bank register** — new `12_case_studies.csv` (project_id, tier, domains, referee, last-used).
Cost: new file to maintain; duplicates card facts; referee tracking redundant with `11_permission_requests`; drift risk as second source of truth.
Benefit: fastest tender-time scan.

**B. Rules + project fields** — AGENTS.md rules + two columns on `01_projects.csv` (`case_study_tier`, `comparability_domains`).
Cost: register grows to 31 fields; tier is derived and can drift stale silently; multi-valued domains sit poorly in a flat field; no room for rationale or use history.
Benefit: queryable immediately; zero new files; cheapest structured option.

**C. Rules only** — AGENTS.md prose, re-derived per tender.
Cost: nothing persists; no learning loop; inconsistent application risk; referees untracked.
Benefit: zero maintenance; nothing to keep current.

**D. Card blocks + rules + existing registers** — AGENTS.md rules; `case_study` block on ~15-20 sheet-worthy cards (tier, domains, sheet-ready headline, use history); referee asks via `11_permission_requests` (REFEREE scope); supersession via `03_methods.method_status=SUPERSEDED`; `regenerate_index.py` extended to compile tier/domains into `project_index.csv`.
Cost: highest setup — card blocks, index generator extension, one-off domain rollup of `sector_activity` and `method_family`.
Benefit: accreting substrate — rationale, wording used and score received accumulate per card; the continuous-improvement loop the scheme is designed around; scan view preserved via index.

## 4. Decision state

- Iain initially selected **B (rules + project fields)**; work stopped before implementation.
- Re-pricing against the wider corpus and the corrected scheme changed the recommendation to **D**, with B as the cheaper halfway point.
- Decision remains **open**. CICP2 family (P75/P85/P87) is the worked example the scheme is calibrated on.

## 5. Register debt the review exposed (independent of encoding choice)

- `contracting_role` empty on 26/68 projects — associate-penalty rule can't run
- `citation_status` absent on 10/68 cards — gate can't run on those
- No `SUPERSEDED` value in `03_methods.method_status`
- `sector_activity` and `method_family` need rollup into the domain list

## 6. Related standing questions

- Whether "case study" as a first-class object (tender + projects used + wording + score received) gets its own register or lives on cards
- How per-tender fit scores persist between tenders
- Whether `project_index.csv` becomes the compiled gate-view (cards -> index) or stays a pure index
