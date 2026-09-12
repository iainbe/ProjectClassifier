# CHANGELOG — Spillover Toolkit

Session-level record of all changes. Per-project detail lives in `project_changelogs/`; per-item audit trail in `10_review_history.csv`; QA findings in `tier2_qa_review.md`.

**Update rule (AGENTS.md):** this file, `tier2_qa_review.md` and `10_review_history.csv` are updated at the END of every work session — no exceptions, no reminders needed.

---

## 26/09/12 — Live-work capture system + date normalisation

- **Templates:** `bid_submission_record_template.md`, `project_management_record_template.md` created; milestone prompts converted to self-contained checklist
- **Workflow:** `register_update_workflow.md` — 5-trigger pipeline (bid submitted → outcome → confirmed → milestone → completion) + repo sync
- **AGENTS.md:** live-work capture rules, schema-drift rule, stale-artefact rule, YY/MM/DD date convention, session-closure rule added
- **SHELDON+SKiN review:** ID scheme fixed (T-NN aligned to 08_tenders); register-row rule codified; `tools/regenerate_index.py` persisted with built-in schema-drift check
- **Dates:** ~2,300 conversions to YY/MM/DD across all registers/cards/docs; `extracted_text/` untouched; `tools/normalise_dates.py` persisted
- **Schema repairs:** `08_tenders.csv` T02/T03/T04 extra-field drift fixed (3rd drift instance this session)

## 26/09/12 — R3 card walkthrough complete + permissions cleared

- **All 10 pilot cards REVIEWED:** P04-P09 (earlier) + P01, P02, P03, P10
- **Register schema repair:** 15 pilot rows realigned; 74 claim fields realigned; backups retained
- **Permission gate:** all 10 projects APPROVED_NAMED for tender citation; `09_publication_assets.csv` populated (TENDER_ONLY — website gate separate)
- **Corrections:** P06/P07 shortlisted-not-failed (precedent WEAK→MODERATE); P03 rejection history recorded; P10 option informal/unevidenced
- **Index:** `project_index.csv` created (65 rows)

## 26/09/12 — Method QA (five-agent review)

- **QA of overall method** using SHELDON/THAD/DEEPTHINK/BLINDSPOT/SKiN/WISHFUL: register schema-drift found (15 rows); walkthrough method validated; self-attestation provenance preserved
- **Audit:** Pass 4-5 appended to `tier2_qa_review.md`
- **Skills:** reviewer skill family committed to ProjectClassifier repo (commit 40113e0)
