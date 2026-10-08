# Review: displaced values in four claims columns (VAL-S261008-11)

Date: 26/10/08. Status: ANALYSIS ONLY, nothing changed in 04_claims.csv. Awaiting Iain's decision.
Lanes run (all advisory): sark/load-the-team, blindspot, deepthink, sheldon, wishful, thad, shaz, skin, fok. Skipped: grey (no buyer or competitor intelligence involved). Out of scope: pigpen, mr-universe, jonbot, place-skills-research.

## Facts (re-measured by three lanes, all agreed)
- 04_claims.csv: 590 rows, 60 columns. Header positions are contrary_evidence 32, reviewer_confidence 33, commercial_reuse 34, publication_status 37 (1-based; the proposal's 31, 32, 33, 36 were 0-based).
- contrary_evidence: 5 displaced role strings (C-G2-040, 054, 055, 056, 057; current role EVALUATOR). reviewer_confidence: 53 displaced claim types (32 equal claim_type; 21 differ and are the pre-retype types of retyped claims; 2 further cells are empty). commercial_reuse: 54 displaced method IDs (all in method_ids). publication_status: 301 displaced batch codes (all equal review_batch).
- No tool reads the four columns. Writers: deepen_*.py hard-code the defaults (NONE_FOUND_IN_REVIEW, MEDIUM, INTERNAL_ONLY); the writer of the batch codes is not traced.
- 08_tenders.csv and 01_projects.csv do not have these columns.
- Recovery: the 21 types are in claims_repair_RECORD.csv; the 5 role strings are in git only; the repo is shallow (first visible commit 4a92a71).

## Where the lanes agree
1. Option A (leave and document) is weakest: invalid values stay in governed fields. Only sheldon rated it ready; fok, thad, skin, shaz, blindspot, deepthink, sark rated it needs-more-work or ready-with-fixes at best.
2. Option B (clear the 387 exact duplicates: 301 batch codes, 54 method IDs, 32 claim types; one commit per column) is READY-WITH-FIXES in every lane.
3. Option C (also clear the 21 types and 5 roles) is NEEDS-MORE-WORK or READY-WITH-FIXES only with Iain's explicit sign-off: it removes the only in-row trace of the retype and of the earlier role reading.
4. Cleared cells stay EMPTY, never a default. A default would assert a review that was not made.

## FIX-NEEDED (combined, de-duplicated)
1. Record file first, `claims_legacy_clear_RECORD.csv`: claim_id, column name, old value, new value (empty), claim_type, review_batch, base commit hash; pinned to HEAD; row counts equal cells cleared. Include the 5 role strings (git-only today). Owner Claude, small.
2. Restore test: clear then restore on a copy; diff against HEAD must be zero. Owner Claude, small.
3. Edit by header name, never position; assert the header and check 2 or 3 untouched rows before and after (schema-drift rule). Owner Claude, XS.
4. New additive check `tools/check_claims_columns.py` (QA checklist item 14, called from the session-closure hook): per-column allowed values, plus a cross-column rule "value must not equal another column's value in the same row". Fails on current data, passes after clearing, fails on a seeded bad row. Adds a gate, weakens none. Owner Claude, about 1 hour.
5. Codebook lines: empty = not recorded, and a future gate must treat an empty publication_status or commercial_reuse as INTERNAL_ONLY, never as unrestricted; the 260 INTERNAL_ONLY, 260 NONE_FOUND_IN_REVIEW and 521 MEDIUM values are script defaults, not review outcomes. Owner Iain approves, Claude edits.
6. Trace the writer of the batch codes and method IDs and guard it, otherwise a re-import undoes the clear. Owner Claude, medium.
7. Correct the stale counts in VAL-S261008-11 (66 role strings is now 5; two empty reviewer_confidence cells were not counted).
8. Closure: regenerate project_index.csv, run eligibility_report.py, update CHANGELOG, tier2_qa_review.md, 10_review_history.csv, one commit per column.

## Generality
- All 23 tenders and 70 projects: the columns do not exist there, so B and C touch only 04_claims.csv; the new check is written as a per-file table so it can be reused.
- Future case 1, a new 60+ column register: header-keyed checks, not position. Fix 4 generalises.
- Future case 2, a client audit of a claim field: the record file plus a pinned commit answers it; documentation alone (Option A) does not.
- Future case 3, an import writing batch codes into the wrong column again: only fix 4 (and fix 6) catches it.

## Recommendation
Option B with fixes 1 to 8, holding the 21 retyped types and 5 role strings for Iain's ruling as a separate later commit.

## Decisions for Iain
1. Go ahead with Option B (387 cells cleared, empty, one commit per column)?
2. The 21 retyped types and 5 role strings: keep for now (recommended) or clear after they are in the record file?
3. Approve the codebook rule that empty means not recorded and is treated as INTERNAL_ONLY?
4. Approve the new check as QA item 14?
