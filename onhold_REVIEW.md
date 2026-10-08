# Review: add ON_HOLD to lifecycle_status

Date: 26/10/08. Status: ANALYSIS ONLY, nothing changed. Iain's instruction: "Add On Hold to lifecycle values." Awaiting his answers on the open points below.
Lanes run (advisory): blindspot, deepthink, sheldon, thad, shaz, fok. Not run, with reasons: sark/load-the-team (lane selection done here), wishful (nothing to size or feasibility-test), skin (no audience-facing output), grey (no buyer or competitor intelligence). All six returned READY-WITH-FIXES, sheldon PARTIALLY PROVEN.

## Facts agreed
- Lifecycle values today: COMPLETED 59, IN_PROGRESS 11 (P31-PRODPARK among them). `08_tenders.csv` has no lifecycle column, so no tender is affected.
- Readers: `eligibility_report.py` line 71 (E1 needs COMPLETED; every other value, including a typo, gets E1 FAIL), `question_sheet.py` (COMPLETED only), `regenerate_index.py` (copies), `selection_view.py` (prints). Nothing validates the vocabulary. ON_HOLD would fail E1 by default, which is correct.
- Evidence that P31 is paused: Iain's statement only (provenance FP-0122). No document, no pause date, no reason, no resume date. The Drive register's use of ON_HOLD is unverified beyond P31. No other project has recorded evidence of a hold.
- Stale items found: the P31 index card still says COMPLETED; the ontology draft line 67 says 57 of 70 COMPLETED (measured 59) and maps PHASE_COMPLETE_AWAITING_INSTRUCTION to COMPLETED while line 132 maps it to IN_PROGRESS.

## Where the lanes agree
1. Add the value, as an additive change, with a definition that separates it from IN_PROGRESS, CANCELLED, `programme_status` and phases: ON_HOLD describes the commission only; it is independent of `programme_status`; it applies to a project row or a phase row, never a parent aggregate; a phase complete and waiting for the next instruction is not a hold.
2. A hold needs a reason, a since-date and an expected resume or review date, otherwise it becomes a graveyard and an 18-month hold looks like last week's. Do not add columns (a schema change): require them in `notes` as `ON HOLD: reason; since YY/MM/DD; resume by YY/MM/DD`, checked by an additive check, with a sweep prompt for holds older than six months (a prompt only, never an automatic status change).
3. Only Iain sets or clears ON_HOLD, recorded in a provenance row.
4. Do not touch the E1 COMPLETED branch (test-strength rule). Add an additive vocabulary check (`tools/check_lifecycle.py`) listing values outside the codebook set (PROPOSED, COMMISSIONED, IN_PROGRESS, COMPLETED, CANCELLED, UNKNOWN, BID_PENDING, ON_HOLD), plus `tests/test_lifecycle_vocab.py` (ON_HOLD, COMPLETED, a typo, empty). This also closes a risk the lanes found: a mistyped lifecycle currently looks like a genuine "not delivered" result.
5. Reporting: the eligibility report lists held projects explicitly and the selection view prints a legend ("ON_HOLD: paused, not delivered"); the question sheet states held projects are not asked about acceptance.
6. Codebook v1.4 restates the full lifecycle list; fix the stale items (regenerate the P31 card, correct the ontology draft lines) and update the Drive merge brief. Verify what the Drive register means by ON_HOLD before the merge.
7. Each change a separate revertible commit with the closure triple.

## Open points for Iain
1. Boundary: do P82-KOTOR and P83-BCWB (phase complete, awaiting instruction, programme_status PHASE_COMPLETE_AWAITING_INSTRUCTION) stay IN_PROGRESS? Recommended: yes, they are waiting for the next phase, not paused.
2. For P31: who paused it (the client or Fifth Sector), since when, and when is it expected to resume? Any written trace?
3. Is any other project paused (P68, P73 have end dates in the past; P79-CELL is waiting on the client)?
4. P31 still passes the citable check (delivered data fragment, DELIVERED_WORK). Keep that, or should a paused project not be citable as delivered?
5. Approve the notes convention (no new columns) and the six-month sweep prompt.
