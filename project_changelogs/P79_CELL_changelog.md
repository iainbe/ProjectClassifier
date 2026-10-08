# P79_CELL — project changelog

## 26/09/12 — project_id renamed

- `P79` → `P79-CELL` — suffixed convention; all FKs cascaded (claims, sources, review history, permission tracker).

## 26/10/07 — register edits (decisions 3 and 4)
- lifecycle REPORTING_COMPLETE -> IN_PROGRESS until client acceptance is recorded.

## 26/10/08 — claims restored

- 8 claims restored to `04_claims.csv` (they were deleted in commit eb2674d on 26/09/16; recovered from commit 4a92a71). See `claims_restore_RECORD.csv`. Counts of coded claims, and so evidence-kind counts for this project, rise accordingly.

## 26/10/08 — Marked delivered

- `lifecycle_status` IN_PROGRESS to COMPLETED (Iain: the business case work is delivered). A GBP 5,000 inc VAT prepayment has been received for a further piece of work the client has not yet specified; recorded in notes and provenance, not as a deliverable. Client acceptance still UNKNOWN.
