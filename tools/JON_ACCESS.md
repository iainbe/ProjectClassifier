# Access note for Jon — use the web-based Drive

**Route:** `drive.google.com` signed in as **jon@thefifthsector.co.uk** → shared items → `Website 2026/spillover-toolkit`.

## Why this route

- The toolkit lives in Iain's Drive; the shared web access is your canonical way in — **not** filesystem paths
- Local paths like `/Users/iainbe/.../My Drive/...` exist only on Iain's machine. Anything written for you uses Drive-relative paths or share links
- **For Places:** when pulling toolkit material, use the **Drive share link / file ID**, never a filesystem path. File IDs are stable across every machine and account; paths are not

## Getting a share link

Right-click any file or folder in web Drive → Share → copy link. The link contains the stable ID:
`drive.google.com/file/d/<FILE_ID>/...` — store the ID or link in Places as the source reference.

## What you can do via web access

| Thing | Works via web Drive? |
|---|---|
| Read registers (CSVs), cards, changelogs | Yes |
| Read `sweep_reports/SWEEP_LATEST.md` + dated reports | Yes — latest findings always there |
| Pull files into Places via share link/file ID | Yes — the intended route |
| **Run `tools/drive_sweep.py`** | **No** — needs a local filesystem mount (Iain's machine or a synced folder) |
| Run `tools/regenerate_index.py`, `normalise_dates.py` | No — same reason |

## Sweep reports for you

The scheduled sweep (weekday 09:00, Iain's machine) writes its report into `sweep_reports/` which you can read via web Drive — the UNREGISTERED_SOURCE and SOURCE_UPDATED sections are the ones most relevant to Places (new material appearing in registered project folders).

## Feedback

Flag anything mis-categorised or missing in the sweep reports, or where the `sweep_config.json` matrix needs tuning (new watch roots, tender keywords, non-project folders).
