# The Drive Sweep — guide + test for Jon

**Your access:** `drive.google.com` signed in as **jon@thefifthsector.co.uk** → shared items → `Website 2026/ProjectClassifier`. Web Drive is the canonical route — never filesystem paths (they only exist on Iain's machine).

**For Places:** pull toolkit material via **share link / file ID** (right-click → Share → copy link; the ID is stable across machines and accounts). Store that, not paths.

---

## What the sweep is

A script that scans Fifth Sector's Drive areas — `Active projects`, `Active proposals`, `Archive projects`, `Archive proposals`, and the toolkit itself — compares every file to its last snapshot, and reports anything new, changed, or missing versus the project registers. It exists because the registers were rebuilt retroactively and gaps kept appearing; the sweep makes drift visible as it happens instead of years later.

**It runs on Iain's machine** (weekday 09:00, scheduled) — you don't run it directly, but you **can trigger it remotely**: drop any file into `Website 2026/sweep_requests/` in Drive and a sweep fires within ~5 minutes of sync. Trigger files are deleted after the run — they're consumed, not kept. You read its output and judge whether it's catching the right things.

## What it reports

| Category | Meaning |
|---|---|
| `UNREGISTERED_PROJECT?` | Folder with no row in `01_projects.csv` |
| `POSSIBLE_TENDER` | Filename matches bid/proposal/RFP patterns |
| `UNREGISTERED_SOURCE` | File inside a known project folder but not in `02_sources.csv` |
| `SOURCE_UPDATED` | A registered source file changed since registration |
| `TENDER_FILE` | New/changed file inside a registered tender folder (new bid material) |
| `VERSION_AMBIGUITY` | A registered source points at a folder holding multiple candidate files — the register needs the canonical version picked, not just any file |
| `DRIFT` | Toolkit register file changed between sweeps |
| `NON_PROJECT` | Known admin folders — flagged but expected |
| Deleted / `.icloud` placeholders | Listed at report end |

Output: `sweep_reports/SWEEP_LATEST.md` (always current) + dated snapshots. The sections most relevant to you: **UNREGISTERED_SOURCE** and **SOURCE_UPDATED** — new material landing in registered project folders that Places may want.

## What you can test (web Drive only)

1. **Sanity read** — open `sweep_reports/SWEEP_LATEST.md`. Do the categories make sense? Is anything mis-filed?
2. **False-positive hunt** — pick an `UNREGISTERED_PROJECT?` or `UNREGISTERED_SOURCE` finding: is it genuinely unregistered, or is it inside a project that IS registered (matcher miss)?
3. **Live test** — create a file via web Drive in a watched area (e.g. `Active proposals/test_jon.txt`). After the next 09:00 weekday run (or ask Iain/Devin to run `tools/drive_sweep.py`), check it appears in `SWEEP_LATEST.md`. Then delete it and check it shows under Deleted next run.
4. **Config check** — look at `tools/sweep_config.json`: are the watch roots and tender keywords right? Anything missing you'd expect flagged?

## Known limits

- Detection only — never moves, renames or deletes anything
- Empty new folders are invisible until a file lands in them
- Renames appear as delete+new
- `.gdoc`/`.gslides` edits in browser may not update the stub timestamp — detection approximate
- `DRIFT` fires on our own session edits too — only meaningful when no session happened
- First run was a baseline — judge it on deltas, not the big initial list

## Feedback format

Send Iain/Devin: **finding → what it should be → why**. E.g. "`Active proposals/2026 X` flagged UNREGISTERED_PROJECT? → it's T09 in the tenders register → tenders rows aren't matched to folders." That kind of report tunes the matrix fast.

## Final-version rules (26/10/08, after the ontology final pass)

These apply to anyone acting on a sweep finding. They replace nothing above; they add what the final ontology (`ontology_v2_DRAFT.md`, revision 4) needs.

**1. A sweep writes only reports.** `drive_sweep.py` writes `sweep_reports/` and `tools/sweep_state.json`. It never writes a register (`01` to `16`), a card, a claims file or a method file. If a sweep session or any agent acting on a sweep saves a register, it saves only the rows it changed.

**2. Never save a whole register from an older copy.** On 26/09/16 an agent session saved `04_claims.csv` from a stale copy and 251 claims disappeared (commit eb2674d; found and restored 26/10/08, VAL-S261008-13). Before saving any register: open the live copy, compare row counts and IDs, save with a record file listing every row added, changed or removed, and stop if the save would remove rows that are not in that record. A save that loses more than a handful of rows is an error until proved otherwise.

**3. One file tree, one mirror; guard before copying.** The Drive toolkit folder IS the git working tree — there is no separate repo copy to compare or hand-sync (`ontology_v2_DRAFT.md` section 17, resolved 26/10/08). The 26/10/08 divergence was between branches and is merged into `main`. If any external copy of a register ever needs writing onto this tree (e.g. an export from another machine or connector), run `python3 tools/sync_guard.py SOURCE TARGET` first: it refuses copies that drop rows, lose IDs, mismatch headers or overwrite a newer file, and `--force "reason"` logs the override to `sync_guard_log.csv`.

**4. Turning a finding into a register change (final ontology).**
- `UNREGISTERED_PROJECT?` or `POSSIBLE_TENDER`: first decide what it is. Our own bid, pending or lost: `08_tenders.csv` only, no project row, empty `project_id` on its sources. A paid commission, including bid support delivered while the bid failed: a project row, lifecycle describing the commission, `programme_status` NOT_AWARDED for the bid outcome, every DESIGN and OPTION claim `option_state` EXPIRED. Delivered work: a project row. Check the folder, year, document type and client against the project differentiation rule in AGENTS.md before assigning anything to an existing project.
- A new or changed project row needs these facts, each from Iain or a document, with its basis in `14_fact_provenance.csv`: `lifecycle_status`, `contracting_role` and `prime_contractor` (PRIME, DIRECT, SUBCONTRACTOR, ASSOCIATE, ADVISORY; BOP associate work is ASSOCIATE with BOP Consulting as prime), `citation_status`, `client_accepted` (Y, N or UNKNOWN only: payment status is not acceptance and lives in the separate `payment_status` column — values PAID_IN_FULL, PART_PAID or blank). An unknown stays UNKNOWN; the eligibility checks never treat it as a pass.
- `UNREGISTERED_SOURCE` and `SOURCE_UPDATED`: register or refresh the source, extract it in full including tables (extraction rules in AGENTS.md), mark PARTIAL_EXTRACT or NOT_ASSESSED if not fully read, and code claims only from sources read in full. `VERSION_AMBIGUITY`: pick the canonical dated, non-draft version; never the first alphabetically. Before declaring evidence missing, check both archives (Drive and OneDrive-TheFifthSector).
- New claims carry `claim_type`, `effect_family` (NOT_APPLICABLE for pure context), `fifth_sector_role`, `value_basis` wherever a pound figure appears, `attribution_strength` for EFFECT, and `option_state` for options. The governed columns `publication_status`, `commercial_reuse`, `reviewer_confidence`, `contrary_evidence` hold only codebook values or stay empty (empty means not recorded); run `python3 -I tools/check_claims_columns.py` before saving (expected today: the 26 held cells only).
- After any register change: regenerate `project_index.csv`, run `python3 tools/eligibility_report.py`, and complete the session-closure triple (CHANGELOG.md, tier2_qa_review.md, 10_review_history.csv) plus per-project changelogs.

**5. New files the DRIFT list now covers.** `13_selections.csv`, `14_fact_provenance.csv`, `15_people.csv`, `16_involvement.csv`, `tender_requirements/`, `method_statements/`, `method_views/`, `selection_views/`, `iain_question_sheet.md`, `eligibility_report.*` and the `claims_*_RECORD.csv` files sit inside the watched toolkit folder, so a change to any is reported as DRIFT. Derived files (views, sheets, reports) are regenerated by tools, never edited by hand.

**5b. Holds.** `python3 -I tools/check_lifecycle.py` lists projects whose lifecycle is ON_HOLD and prompts (never changes a status) when a hold is more than six months old or has no since date; run it at session start with the sweep checks.

**6. Built since this was written.** `tools/sync_guard.py` now refuses a copy removing many register rows (26/10/08). Still pending: adding `tools/check_claims_columns.py` to the pre-commit hook (it fails until the 26 held cells are settled). Each addition keeps all existing checks.
