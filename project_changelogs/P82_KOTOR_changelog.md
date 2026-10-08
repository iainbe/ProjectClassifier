# P82_KOTOR — project changelog

## 26/09/12 — project_id renamed

- `P82` → `P82-KOTOR` — suffixed convention; all FKs cascaded (claims, sources, review history, permission tracker).

## 26/10/07 — register edits (decisions 3 and 4)
- lifecycle PHASE_COMPLETE_AWAITING_INSTRUCTION -> IN_PROGRESS; programme_status still holds the old value (VAL-S261007-15).

## 26/10/08 — claims restored

- 7 claims restored to `04_claims.csv` (they were deleted in commit eb2674d on 26/09/16; recovered from commit 4a92a71). See `claims_restore_RECORD.csv`. Counts of coded claims, and so evidence-kind counts for this project, rise accordingly.
