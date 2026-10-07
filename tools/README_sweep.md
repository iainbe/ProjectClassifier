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
