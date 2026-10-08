# Method selection package (PROPOSAL, 26/10/08): for lane review, then Iain's approval

Status: proposal only. Nothing below is applied to `03_methods.csv`, the codebook or any tool except the new read-only `tools/method_view.py`. Drafts present in the repo: `method_family_rollup_DRAFT.csv`, `method_repair_PREVIEW.csv`, `method_new_rows_DRAFT.csv`, `method_statements/MS-01..03`. Per the review-team rule in AGENTS.md, the lane team reviews this package once, the combined analysis goes to Iain, and only then is each item applied as its own commit.

## What is proposed (in commit order)

1. **Repair 19 shifted method rows** (M-G2-010 to M-G2-028). Each row has its fields shifted one column from `outputs` onward (the `outputs` value sits in `source_ids`, the notes in `source_ids`... and so on). All 19 match one exact pattern, so the fix is mechanical: insert an empty `outputs` and shift the rest right. Preview: `method_repair_PREVIEW.csv`. Data fix, no schema change. Not a weakening of any test.
2. **Register two missing method rows**: M-S261008-01 (Beatles attribution bridge, P78-BEATLES) and M-S261008-02 (Production Fund final evaluation, P88-LCRPF24). Draft: `method_new_rows_DRAFT.csv`.
3. **Fix references** (DONE 26/10/08): claims C-G2-022 and C-G2-023 pointed to `M-G2-009`, which has no row; repointed to `M-G2-008`, whose own claim list already includes them. The new Beatles and Production Fund claims now name their method rows. Remaining: 20 method links to absent claims (VAL-S261008-09) and one one-way link (VAL-S261008-12).
4. **Rolled-up family**: add `method_family_rollup` (eight families) beside the 41 existing labels via the mapping in `method_family_rollup_DRAFT.csv`; old labels stay. Taxonomy change.
5. **Statement layer (schema change)**: add `statement_id` to `03_methods.csv`; statements live in `method_statements/MS-nn_*.md` with CURRENT / DRAFT / SUPERSEDED status. Codebook v1.4 gains `SUPERSEDED` as a `method_status` value.
6. **E4 "method current" extended, not weakened**: still UNKNOWN when a project has no method rows and FAIL when a method row is SUPERSEDED; additionally FAIL when a linked statement is SUPERSEDED, and a flag when the only linked statement is DRAFT.
7. **Adopt MS-01 to MS-03** after Iain's review, link their method rows, run `tools/method_view.py`.

## Design principles already agreed with Iain

Evidence kind filters, never ranks (decision 10). Wording is capped at the claim's evidence class (decision 11). Contribution claims name the contracting structure (AGENTS.md). Statements are written only when a requirement needs them. No existing test is weakened.

## Generality test cases the lanes should use

Every tender with usable wording: T01-BCAT, T13, T21-CSFI, T22-VAIMP, T05-DERBY, T23-TVBTV. Plus two hypothetical shapes: (a) a tender asking for a method statement for building a data dashboard or framework, not an evaluation; (b) a tender where the only relevant experience is associate work for another consultancy (BOP) and the prime's IP may restrict reuse of method text.

## Known weaknesses of the package (stated up front)

- MS-03 rests on a PROPOSED design-only method as subcontractor; it is the weakest statement.
- Only three statements exist; the other 49 method rows have none.
- The rollup groups 23 of 52 methods into one family (sector baseline mapping), which may be too coarse.
- Statements are drafted by Devin from registered documents; none has been reviewed by Iain.

## Correction 26/10/08 (Iain)

BOP Consulting is a competitor and is never asked for permission; PR-07 already says so (Iain 26/09/12). The lane suggestion to obtain BOP's written agreement for MS-03 is not adopted. MS-03 relies on accurate attribution capped at "contributed to", plus an internal check of our own subcontract or NDA for a confidentiality or publicity clause.

## Update 26/10/08: rollup applied and requirement types tabulated (limited)

- **Rollup applied** as an additive column `method_family_rollup` (ten families after splitting the sector-baseline family; the largest is 20% of methods). Mapping: `method_family_map.csv`. The two draft files for the rollup and the repair preview were removed once applied (history keeps them).
- **Requirement types across tenders: the register cannot support a full tabulation.** Of 23 tender rows only five (T01-BCAT, T05-DERBY, T21-CSFI, T22-VAIMP, T23-TVBTV) carry usable requirement wording. In those: price or a fixed fee appears in all of them; insurance minimums in T21, T22 and T23; financial standing in T22 and T23; a written method or approach submission in T21 (four Schedule 4 submissions), T22 (3-page proposal) and T23 (quality questions); precedent evidence as named case studies in T22 and as capability criteria in T01. This is the selection effect Fok warned of: the statements and the layer are fitted to five formal tenders, and nothing here says which method statements win points. A requirement file per tender (decision 13) is the way to grow the base; T21-CSFI and T23-TVBTV are next.
