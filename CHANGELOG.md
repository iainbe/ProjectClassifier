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

## 26/09/12 — Drive sweep agent installed

- `tools/drive_sweep.py` + `tools/sweep_config.json`: periodic Drive scanner — detects new/changed/deleted files, classifies gaps (UNREGISTERED_PROJECT?, POSSIBLE_TENDER, DRIFT, SOURCE_UPDATED, UNREGISTERED_SOURCE), folder-level collapse
- `sweep_reports/` created; SWEEP_LATEST.md always current + dated snapshots
- launchd job installed: weekday 09:00 (`com.thefifthsector.toolkit-sweep`)
- Register fix: drive_folder_path filled for P75, P78, P79, P80, P81, P82, P83 (Active projects folders)
- Baseline findings: Creative Scotland Salaries (69 files) unregistered; ~10 unregistered Active proposals folders; 5,805 unregistered sources in registered project folders
- AGENTS.md session-start rule added (check SWEEP_LATEST.md)

## 26/09/12 — Sweep README + naming/transition protocol (draft)

- `tools/README_sweep.md`: plain-language agent doc for sharing (Jon testing) — what it does, how to test, matrix tuning, honest limitations
- `naming_and_transition_protocol.md` DRAFT: folder/file naming conventions codified (YYYY folders, YYMMDD files, no-trailing-spaces); bid→project = MOVE to `Active projects/YYYY Name/Proposal/` (single canonical location); renaming rule (same-action register update)
- Open questions left for Iain/Jon: move vs duplicate confirmed?; `Proposal/` vs `Bid/` naming; retroactive tidy vs forward-only

## 26/09/12 — Protocol approved + proposal triage registered

- Protocol APPROVED: move (not duplicate), `Proposal/` subfolder, one-time tidy
- Tidy done: Maritime Belfast trailing space fixed; BEYOND scene-setter filed; NO proposals are won/live-as-project (Iain) — all stay in Active proposals
- 7 unregistered Active proposals triaged from folder evidence and registered: T06-BEYOND, T07-BTM, T08-BRUSSELS, T09-CSG, T10-MARBEL, T11-NEXTWAVE, T12-PLYIMM (08_tenders rows + bid_records created; buyer/stage inferred, marked for Iain confirmation)
- drive_folder_path filled for 7 Active-projects register rows

## 26/09/12 — Live tender test (T01-BCAT) complete

- Requirement map + precedent match run on live bid (UK_1412, deadline 26/09/26, budget £65k+VAT, eval 20/30/50)
- VERIFIED against register: Liverpool £406m→£780m (canonical SRC-G2-028: £405.9m→£779.8m), MITIH gated sequence, FGTG, NES 200+ firms, P22 Film Fund, P75 True North, P83 BC reports
- CAUGHT: AMGEN (USW AHRC) + Creative Scotland Salaries cited in live bid but UNREGISTERED; P64/P69 possible duplicate; T01 had no bid record (created retrospectively); FGTG client wording tension (bid: GMCA/Innovate UK; register: MMU prime)
- Clarifications intel surfaced: UK-return priority (Q6), transferable methodology (Q7), insurance negotiable (Q8/9)
- Gap: ODA/international development = weakest essential criterion

## 26/09/12 — Cited-but-unregistered projects fixed

- P85-AMGEN registered: DIRECT_PROPOSAL to University of South Wales (Iain) — PRIME, Places evidence for USW-led AMGEN CICP2 bid
- P86-CSSAL registered: Creative Scotland Salary Benchmarking — PRIME, proposal pack submitted, award status flagged for confirmation
- P64/P69 cross-linked as related-but-distinct commissions (framework design vs evaluation delivery); date inconsistency on P64 sources flagged
- T01 bid record updated with register anchors

## 26/09/12 — P86-CSSAL status: PREFERRED_BIDDER

- Creative Scotland letter: preferred bidder; award confirmed after standstill ends 26/09/18 (Iain)
- On confirmation → workflow Trigger 3: PM record + provisional index card

## 26/09/12 — P64 resolved: Business Case Justification, outcome CONFIRMED

- BCJ = Business Case Justification (Iain); delivered Oct 22-Mar 23; WYCA confirmed funding to Wakefield Council
- P64 dates corrected (23/01→22/10 start per source dates); renamed; distinct-commission link to P69 confirmed
- Claim C-R4-001 added: funding-unlock outcome, option value EXERCISED — BCJ unlocked the programme P69 evaluated

## 26/09/12 — P02-FGTG client clarified (Iain)

- Man Met commissioned + project-managed on behalf of GM partners and universities — Fifth Sector contracted to MMU as consortium lead
- T01 wording flag resolved: recommended edit logged in bid record (name MMU as commissioner, not GMCA/Innovate UK)

## 26/09/12 — P85-AMGEN completed (Iain)

- USW initial bid shortlisted; Fifth Sector direct proposal accepted (£10k incl VAT); Places evidence for full submission COMPLETED; USW outcome pending
- Claim C-R4-002 added; P06/P07 wording pattern applies (completed evidence work, not funded project)

## 26/09/12 — T01-BCAT SUBMITTED

- Bid submitted ahead of 26/09/26 deadline (Iain); documents frozen — no wording changes applied
- Tenders row → SUBMITTED_AWAITING_RESULT; bid record updated; outcome trigger armed
- NOTE: FGTG wording recommendation NOT applied — submitted version retains original text

## 26/09/12 — QA pass + session-closure enforcement

- REVIEW (agents lenses): sweep script + README + workflow + registers re-checked
- BUG FIXED: sweep state tuple-vs-list comparison made every file report "changed" (24,501 false deltas) — fixed to list() compare; now correct deltas
- FIXED: dead seen_folders code removed; stale TND- example in workflow; README path unusable for Jon (full path + machine-varies note); 6 review-history IDs normalised to hyphenated
- DOCUMENTED: sweep blindspots — empty folders invisible, renames show as delete+new, gdoc stubs approximate, DRIFT fires on own session edits
- AUTOMATION: tools/check_session_closure.sh installed as repo pre-commit hook — commits changing toolkit files without all 3 audit artefacts (CHANGELOG/audit/history) are blocked; --no-verify bypass for emergencies

## 26/09/12 — Jon access note

- tools/JON_ACCESS.md: web-Drive route (jon@thefifthsector.co.uk) is canonical access; share links/file IDs (not filesystem paths) for pulling into Places; script-running requires local mount (Iain-side)
- README_sweep.md updated to point at access note

## 26/09/12 — Jon docs folded + tenders-folder matching

- tools/JON_SWEEP_GUIDE.md: single doc for Jon (access route, what sweep does, categories, web-testable checklist, limits, feedback format); replaces JON_ACCESS.md + README_sweep.md (deleted)
- Sweep improvement: Active proposals folders now matched to 08_tenders via 'Drive folder:' notes (T01/T02 recorded) — registered tender folders classify TENDER_FILE instead of UNREGISTERED_PROJECT?

## 26/09/12 — Repo pushed + register-extension batch B (6 cards)

- Repo pushed to GitHub (16 commits, 40113e0..2e7d2d7)
- Priority cards created: P81-WB6 (skills-pivot + 3-phase gated funding), P82-KOTOR (ministerial declaration — dates corrected 25→26 on file evidence), P83-BCWB (3-country institutional design, honest incompleteness), P27-WAKECDF (Green Book anchor: £22.03m from £4.38m), P64-BCJ (funding-unlock, option EXERCISED), P69-OURYEAR (£4.2m evaluation, model adopted by WYCA/ACE)
- All DRAFT pending Iain walkthrough; flags: P81 lacks claims/sources rows, P82 year-error confirm, P64 WYCA letter to register
- project_index.csv regenerated

## 26/09/12 — P82 date correction REVERTED (my error)

- Iain clarified: TWO Berlin Process events — Kotor 2025 ministerial + Herceg Novi 2026 forum
- My earlier "correction" (25→26) conflated them: reverted P82 register + SRC-G2-083/084 to 25/05 (Kotor 27-28 May 2025 — correct per filenames 250527/250528 in 2025 Projects)
- 2026-dated materials (briefing, EWG report, contract addendum) = Herceg Novi 2026 follow-on — flagged in card as phase-boundary question for Iain
- Lesson: filename-year inference is not sufficient when two same-named events exist in different years — confirm before correcting

## 26/09/12 — P82/P83 confirmed one CEC programme arc

- Iain: Kotor 2025 + Herceg Novi 2026 + council development = same Creative Economy Councils work, all phase-complete awaiting instruction
- Cross-links recorded on P82/P83; P82 card updated
