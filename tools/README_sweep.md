# Drive Sweep Agent — what it is and how to test it

**Access:** Jon — see `tools/JON_ACCESS.md` first; you read reports via web Drive, you don't run this script (it needs a local mount).

**What it is:** a small Python script that periodically scans Fifth Sector's Google Drive and reports anything new, changed or missing compared to the project register — so bids, sources and new projects can't silently go uncaptured.

**Why it exists:** the project registers were rebuilt retroactively and we found gaps everywhere (unregistered projects, unrecorded bid outcomes, misplaced values). The sweep makes drift visible *as it happens* instead of years later.

## What it does

1. Walks these Drive areas: `Active projects`, `Active proposals`, `Archive projects`, `Archive proposals`, `Website 2026/spillover-toolkit`
2. Compares every file to a saved snapshot (what it saw last time)
3. Classifies each new/changed file:
   - **UNREGISTERED_PROJECT?** — folder with no row in `01_projects.csv`
   - **POSSIBLE_TENDER** — filename matches bid/proposal/RFP patterns
   - **UNREGISTERED_SOURCE** — file inside a known project folder but not in `02_sources.csv`
   - **SOURCE_UPDATED** — a registered source file changed since registration
   - **DRIFT** — a toolkit register file changed outside a governed session
   - **NON_PROJECT** — known admin folders (Foresight, Templates, etc.)
   - deletions and `.icloud` placeholders listed separately
4. Writes `sweep_reports/SWEEP_LATEST.md` (always current) + a dated snapshot, and pops a macOS notification with the count

## How to test it

```bash
cd "/Users/iainbe/Library/CloudStorage/GoogleDrive-iain@thefifthsector.co.uk/My Drive/Website 2026/ProjectClassifier"
bash tools/run_sweep.sh           # run a sweep now (via the loud-failure wrapper)
open sweep_reports/SWEEP_LATEST.md  # read the report
```

**Manual test:** create a dummy file (e.g. `Active projects/test_sweep.txt`), run the script, confirm it appears in the report under UNREGISTERED_PROJECT?, delete it, run again.

## Schedule

Installed as two launchd jobs — `com.thefifthsector.toolkit-sweep` (weekday 09:00 sweep) and `com.thefifthsector.toolkit-sweep-trigger` (300s remote-trigger poll). Source plists live in `tools/`; copies are installed at `~/Library/LaunchAgents/`. To change: edit `tools/` copy, re-copy, `launchctl bootout gui/$UID <label>` then `launchctl bootstrap gui/$UID <plist>`.

**REQUIRED one-time step — disk access:** launchd children have no TCC permission for `~/Library/CloudStorage`, so both jobs exec `~/bin/toolkit-sweep-launcher` (compiled from `tools/sweep_launcher.c`, deliberately outside CloudStorage). Grant it Full Disk Access once: System Settings → Privacy & Security → Full Disk Access → + → Cmd+Shift+G → `~/bin/toolkit-sweep-launcher`. If macOS shows an "would like to access files" prompt attributed to toolkit-sweep-launcher instead, approving that also works. Until granted, runs fail at bash-open — check `sweep_reports/launchd.log` / `trigger.log` and `LAST_RUN_OK` staleness.

To rebuild the launcher after changing `sweep_launcher.c`:
```bash
clang -o ~/bin/toolkit-sweep-launcher tools/sweep_launcher.c
```

## Remote trigger (any device)

A second launchd job (`com.thefifthsector.toolkit-sweep-trigger`) polls `Website 2026/sweep_requests/` every 5 minutes via `tools/check_sweep_trigger.sh`. Because that folder lives in Google Drive, **dropping any file into it from any signed-in device (web, phone, another Mac) fires a sweep on Iain's machine** within ~5 minutes of Drive syncing it. Trigger files are consumed — the wrapper deletes them after the run.

To trigger from a phone or the web: Drive app → `Website 2026/sweep_requests/` → upload any small file or create a Google Doc there.

Note: launchd `QueueDirectories` does not fire reliably on Google Drive File Provider mounts, which is why the trigger uses a polling job instead. The main plist keeps `QueueDirectories` too — if it ever does fire, that's a bonus early run, not the mechanism to rely on.

## Loud failures and heartbeat

`tools/run_sweep.sh` wraps the Python script:

- **On success:** writes `sweep_reports/LAST_RUN_OK` (timestamp) and clears `SWEEP_FAILED.md`.
- **On failure (non-zero exit):** writes `sweep_reports/SWEEP_FAILED.md` with the log tail, prepends a failure banner to `SWEEP_LATEST.md` (last good report preserved below it), and pops a macOS notification.
- **If the job can't launch at all** (plist path wrong, agent unloaded): nothing runs, so nothing writes. Detect this by heartbeat staleness — if `LAST_RUN_OK` is missing or older than ~3 weekdays, the sweep is dead. The session-start rule in AGENTS.md checks this.
- Launchd-level errors (script missing, permissions) go to `sweep_reports/launchd.log`; script errors go to `sweep_reports/sweep.log`.

## Tuning — the "matrix"

`tools/sweep_config.json` controls everything:

| Setting | What it does |
|---|---|
| `watch_roots` | which Drive areas to scan + severity |
| `tender_patterns` | filename keywords that flag POSSIBLE_TENDER |
| `non_project_folders` | folders to classify as admin, not gaps |
| `ignore_patterns` | files to skip (temp files, .icloud handled separately) |

**Important:** the first run is a baseline — everything existing counts as "new" once. After that, sweeps only report real changes. Judge it on deltas, not the baseline.

## What it does NOT do

- It doesn't move, rename or delete anything — detection only
- It can't read `.gdoc`/`.gslides` content (Drive stubs) — detects them by name/date only
- It doesn't decide what to do — findings surface to the next toolkit session for human review
- It doesn't see files that aren't synced locally (streaming-only files appear as `.icloud` placeholders, listed at report end)
- It doesn't detect **empty new folders** — a folder only shows up once a file lands in it
- Renames appear as "deleted + new" — same content, flagged as change (acceptable noise)
- `.gdoc`/`.gslides` edits in the browser may not update the local stub's timestamp — treat their detection as approximate
- **DRIFT fires on our own session edits too** — the sweep can't tell governed edits from outside ones. DRIFT with no corresponding recent session is the signal to investigate; DRIFT after a session is expected

## Feedback wanted

- Are the categories right? Anything flagging that shouldn't, or vice versa?
- Report format useful? Too much/too little detail?
- Right schedule?

## Final-version rules (26/10/08, after the ontology final pass)

These apply to anyone acting on a sweep finding. They replace nothing above; they add what the final ontology (`ontology_v2_DRAFT.md`, revision 4) needs.

**1. A sweep writes only reports.** `drive_sweep.py` writes `sweep_reports/` and `tools/sweep_state.json`. It never writes a register (`01` to `16`), a card, a claims file or a method file. If a sweep session or any agent acting on a sweep saves a register, it saves only the rows it changed.

**2. Never save a whole register from an older copy.** On 26/09/16 an agent session saved `04_claims.csv` from a stale copy and 251 claims disappeared (commit eb2674d; found and restored 26/10/08, VAL-S261008-13). Before saving any register: open the live copy, compare row counts and IDs, save with a record file listing every row added, changed or removed, and stop if the save would remove rows that are not in that record. A save that loses more than a handful of rows is an error until proved otherwise.

**3. Two copies exist; compare before copying.** The Drive toolkit folder is the working canonical and the git repo is the mirror (`register_update_workflow.md`), but both were edited on 26/10/08 and they have diverged (`ontology_v2_DRAFT.md` section 17, `drive_merge_BRIEF.md`). The sweep does not detect this. Until it does, at the start of a toolkit session compare the two copies' register files (row counts, IDs, header names and file size) and surface any difference before other work. Which folder name the sweep's DRIFT root watches (`Website 2026/ProjectClassifier`) against which is canonical (`Website 2026/spillover-toolkit`) is to be confirmed in the merge.

**4. Turning a finding into a register change (final ontology).**
- `UNREGISTERED_PROJECT?` or `POSSIBLE_TENDER`: first decide what it is. Our own bid, pending or lost: `08_tenders.csv` only, no project row, empty `project_id` on its sources. A paid commission, including bid support delivered while the bid failed: a project row, lifecycle describing the commission, `programme_status` NOT_AWARDED for the bid outcome, every DESIGN and OPTION claim `option_state` EXPIRED. Delivered work: a project row. Check the folder, year, document type and client against the project differentiation rule in AGENTS.md before assigning anything to an existing project.
- A new or changed project row needs these facts, each from Iain or a document, with its basis in `14_fact_provenance.csv`: `lifecycle_status`, `contracting_role` and `prime_contractor` (PRIME, DIRECT, SUBCONTRACTOR, ASSOCIATE, ADVISORY; BOP associate work is ASSOCIATE with BOP Consulting as prime), `citation_status`, `client_accepted` (Y, N or UNKNOWN only: payment status is not acceptance and must not share its column). An unknown stays UNKNOWN; the eligibility checks never treat it as a pass.
- `UNREGISTERED_SOURCE` and `SOURCE_UPDATED`: register or refresh the source, extract it in full including tables (extraction rules in AGENTS.md), mark PARTIAL_EXTRACT or NOT_ASSESSED if not fully read, and code claims only from sources read in full. `VERSION_AMBIGUITY`: pick the canonical dated, non-draft version; never the first alphabetically. Before declaring evidence missing, check both archives (Drive and OneDrive-TheFifthSector).
- New claims carry `claim_type`, `effect_family` (NOT_APPLICABLE for pure context), `fifth_sector_role`, `value_basis` wherever a pound figure appears, `attribution_strength` for EFFECT, and `option_state` for options. The governed columns `publication_status`, `commercial_reuse`, `reviewer_confidence`, `contrary_evidence` hold only codebook values or stay empty (empty means not recorded); run `python3 -I tools/check_claims_columns.py` before saving (expected today: the 26 held cells only).
- After any register change: regenerate `project_index.csv`, run `python3 tools/eligibility_report.py`, and complete the session-closure triple (CHANGELOG.md, tier2_qa_review.md, 10_review_history.csv) plus per-project changelogs.

**5. New files the DRIFT list now covers.** `13_selections.csv`, `14_fact_provenance.csv`, `15_people.csv`, `16_involvement.csv`, `tender_requirements/`, `method_statements/`, `method_views/`, `selection_views/`, `iain_question_sheet.md`, `eligibility_report.*` and the `claims_*_RECORD.csv` files sit inside the watched toolkit folder, so a change to any is reported as DRIFT. Derived files (views, sheets, reports) are regenerated by tools, never edited by hand.

**6. Not built (decisions pending).** A guard that refuses a sync or save removing many register rows; a sweep check that compares the Drive and repo copies; adding `tools/check_claims_columns.py` to the pre-commit hook (it fails until the 26 held cells are settled). Each would add a check and weaken none.
