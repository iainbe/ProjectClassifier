# Codebook v1.4 additions (CANDIDATE, 26/10/08): method statement layer

Status: candidate additions to `codebook_v1.3.md`, proposed by the method package, lane-reviewed 26/10/08 (eight advisory lanes, none blocking), applied by Iain's instruction to proceed in the agreed order. Register `codebook_version` values stay `1.3-candidate` until Iain approves a v1.4 release. Nothing in v1.3 is removed or weakened.

## 1. `method_status` gains SUPERSEDED (section 6.1)

| Code | Evidence required |
|---|---|
| SUPERSEDED | A later method or approach replaces this one in a way that would change the answer a bid gives; record what replaced it in `notes`. Not used for methods that are merely older |

Effect on checks: E4 (method current) already returns FAIL when any method row is SUPERSEDED; that rule is unchanged. A later additive step makes E4 also FAIL when a linked method statement is SUPERSEDED.

## 2. New field `statement_id` on `03_methods.csv` (last column)

Links a method row (one application on one project) to a reusable method statement in `method_statements/MS-nn_*.md`. Blank means no statement exists for that method. A method row links to at most one statement; a statement lists its applications in its own header, and `tools/method_view.py` flags any mismatch between the two.

## 2b. New field `method_family_rollup` on `03_methods.csv` (last column)

One of ten rolled-up families (GENERAL_SECTOR_MAPPING, THEMATIC_AND_SUBSECTOR_MAPPING, DATA_PROFILING_AND_LANDSCAPE, ECOSYSTEM_AND_NETWORK_ANALYSIS, ECONOMIC_ASSESSMENT, EVALUATION, STRATEGY_AND_OPTIONS, FEASIBILITY, BID_AND_PROPOSAL_SUPPORT, FACILITATION_AND_QUALITY), set from the mapping in `method_family_map.csv`. The 41 free-text `method_family` labels are kept unchanged. No family holds more than a fifth of the methods (lane review: Fok, Blindspot, Wishful). The family is a filter for choosing methods; it must not appear in claim wording, and it does not say how a method was labelled originally (the old label stays beside it).

## 3. Method statement status (not a register field)

CURRENT, DRAFT or SUPERSEDED, held in the statement file header. Only Iain sets CURRENT. A statement also records `evidence_class` (DELIVERED, DESIGN_ONLY, PROPOSED), `disclosure_status` (CLEARED, NOT_CLEARED, CHECK_OWN_CONTRACT), `as_at_date`, `evidence_review_date`, `reviewed_by` and `next_action`.

## 4. Rules carried over

Wording is capped at the evidence class of the claims behind a statement. Contribution claims name the contracting structure. BOP Consulting and other competitors are never asked for permission (PR-07). Statements are written when a requirement needs them, not for every method.
