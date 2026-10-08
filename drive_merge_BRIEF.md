# Brief: merge the Drive toolkit folder and the git repo (hand-off, 26/10/08)

Written for an agent that can work inside Drive. Nothing has been copied either way. The Drive connector available to the earlier session could not overwrite file contents, so no sync was run.

## Situation
The Drive folder is the working canonical; the git repo (github.com/iainbe/ProjectClassifier, branch `claude/dazzling-hamilton-qutf3k`, merged state to be pushed to `main`) is the mirror. Both were edited on 26/10/08 and they diverged. Neither may overwrite the other. Before touching anything read `AGENTS.md`, `register_update_workflow.md` and `tools/README_sweep.md` (final-version rules).

## Known differences found at 02:44 (Drive `01_projects.csv`, checked by value)
- Drive has five projects the repo lacks: P91-WBSKILLS (British Council Western Balkans Creative Skills Programme, IN_PROGRESS), P92-BAY (The Bay Cultural Compact Sector Mapping, South Lakeland), P93-WOW (Writing on the Wall NPO Application Support), P95-LIVCS30 (Liverpool Cultural Strategy 2030), P96-LIVDI (LCR Digital Infrastructure Action Plan). Add them to the repo; each needs the full field set (see `tools/README_sweep.md` rule 4) and a changelog entry. P94 is absent from both: ask whether it exists.
- Drive's thirty-first column header is `client_accepted  ` (trailing spaces) and holds PAID_IN_FULL or PART_PAID, a payment status. In the repo the same column holds Y / UNKNOWN client acceptance with provenance. Do not merge the two meanings: give payment status its own new column (suggest `payment_status`) and keep `client_accepted` Y/N/UNKNOWN. This is a schema change: needs the full review-lane set (AGENTS.md) and Iain's approval before commit.
- Drive P51 (South Yorkshire ARG evaluation) has corrected name, dates (22/08 to 23), sector activity and folder path, and its role reads EVALUATOR only; the repo has role EVALUATOR;LEAD_CONSULTANT (Iain instruction) and contracting role DIRECT (Iain, 26/10/08). Take the Drive name, dates and folder, keep the repo roles.
- Drive P31-PRODPARK lifecycle is ON_HOLD; the repo says COMPLETED. Ask Iain which is right.
- Drive `04_claims.csv` is 239,822 bytes, the same size as the repo before 244 deleted claims were restored. The repo now has 595 claims (444,844 bytes, md5 1a0e609e1b12ea2555c5b81fcd87e09f at commit e177a1a). Check whether Drive holds any claim the repo lacks (compare IDs) before replacing it.
- Not yet compared: `02_sources`, `03_methods`, `05` to `08`, `10_review_history`, `11`, `14` to `16` (Drive `14_fact_provenance.csv` is 2,222 bytes against 31,600 in the repo; Drive `10_review_history.csv` is 114,552 bytes against 121,330). Compare each by ID, never by position.

## What the repo has that Drive lacks (keep)
Client acceptance answers, contracting roles, citation status, P54 NOT_AWARDED, P88 purchase order, 249 restored claims, 387 cleared claims-column cells, the 14_fact_provenance rows, three method statements, tender requirement file T22, people and involvement registers, QA item 14, codebook v1.4 additions, the ontology draft (revision 4).

## Rules
- Compare by ID and header name, not by row position. Keep each file's existing line endings (claims, evidence, methods, measurements use CRLF; projects and sources use LF; the validation file is mixed).
- Record every row added, changed or removed in a record file; do not remove rows that are not in the record.
- Do not weaken any test, gate or QA item. Present analysis before committing any schema change. One revertible commit per fix. Complete the session-closure triple.
- Do not copy anything to Drive that has not been merged and checked by ID. After the merge: regenerate `project_index.csv`, run `tools/eligibility_report.py`, `tools/check_claims_columns.py` (26 held cells expected) and the QA checklist; then copy the merged registers into both locations and verify size and md5 match.
- Nothing is sent to any client. Iain makes the decisions flagged above.
