# Drive Sweep Agent — what it is and how to test it

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
cd "My Drive/Website 2026/spillover-toolkit"
python3 tools/drive_sweep.py        # run a sweep now
open sweep_reports/SWEEP_LATEST.md  # read the report
```

**Manual test:** create a dummy file (e.g. `Active projects/test_sweep.txt`), run the script, confirm it appears in the report under UNREGISTERED_PROJECT?, delete it, run again.

## Schedule

Installed as a launchd job — runs weekday mornings at 09:00 (`com.thefifthsector.toolkit-sweep`). To change frequency or disable: `~/Library/LaunchAgents/com.thefifthsector.toolkit-sweep.plist` (unload with `launchctl unload`).

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

## Feedback wanted

- Are the categories right? Anything flagging that shouldn't, or vice versa?
- Report format useful? Too much/too little detail?
- Right schedule?
