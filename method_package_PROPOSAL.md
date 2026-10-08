# Method selection package (PROPOSAL, 26/10/08): for lane review, then Iain's approval

Status: proposal only. Nothing below is applied to `03_methods.csv`, the codebook or any tool except the new read-only `tools/method_view.py`. Drafts present in the repo: `method_family_rollup_DRAFT.csv`, `method_repair_PREVIEW.csv`, `method_new_rows_DRAFT.csv`, `method_statements/MS-01..03`. Per the review-team rule in AGENTS.md, the lane team reviews this package once, the combined analysis goes to Iain, and only then is each item applied as its own commit.

## What is proposed (in commit order)

1. **Repair 19 shifted method rows** (M-G2-010 to M-G2-028). Each row has its fields shifted one column from `outputs` onward (the `outputs` value sits in `source_ids`, the notes in `source_ids`... and so on). All 19 match one exact pattern, so the fix is mechanical: insert an empty `outputs` and shift the rest right. Preview: `method_repair_PREVIEW.csv`. Data fix, no schema change. Not a weakening of any test.
2. **Register two missing method rows**: M-S261008-01 (Beatles attribution bridge, P78-BEATLES) and M-S261008-02 (Production Fund final evaluation, P88-LCRPF24). Draft: `method_new_rows_DRAFT.csv`.
3. **Fix references**: claim method link `M-G2-009` points to no method row; four methods are never referenced by any claim.
4. **Rolled-up family**: add `method_family_rollup` (eight families) beside the 42 existing labels via the mapping in `method_family_rollup_DRAFT.csv`; old labels stay. Taxonomy change.
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
