# The Drive Sweep — guide + test for Jon

**Your access:** `drive.google.com` signed in as **jon@thefifthsector.co.uk** → shared items → `Website 2026/spillover-toolkit`. Web Drive is the canonical route — never filesystem paths (they only exist on Iain's machine).

**For Places:** pull toolkit material via **share link / file ID** (right-click → Share → copy link; the ID is stable across machines and accounts). Store that, not paths.

---

## What the sweep is

A script that scans Fifth Sector's Drive areas — `Active projects`, `Active proposals`, `Archive projects`, `Archive proposals`, and the toolkit itself — compares every file to its last snapshot, and reports anything new, changed, or missing versus the project registers. It exists because the registers were rebuilt retroactively and gaps kept appearing; the sweep makes drift visible as it happens instead of years later.

**It runs on Iain's machine** (weekday 09:00, scheduled) — you don't run it. You read its output and judge whether it's catching the right things.

## What it reports

| Category | Meaning |
|---|---|
| `UNREGISTERED_PROJECT?` | Folder with no row in `01_projects.csv` |
| `POSSIBLE_TENDER` | Filename matches bid/proposal/RFP patterns |
| `UNREGISTERED_SOURCE` | File inside a known project folder but not in `02_sources.csv` |
| `SOURCE_UPDATED` | A registered source file changed since registration |
| `TENDER_FILE` | New/changed file inside a registered tender folder (new bid material) |
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
