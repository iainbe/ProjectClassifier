# File Naming + Bid→Project Transition Protocol — APPROVED 26/09/12

**Purpose:** consistent naming so the sweep, registers and humans all read the same structure. Built on existing conventions (YYYY folders, YYMMDD files) rather than new invention.

## 1. Folder naming

| Location | Convention | Example |
|---|---|---|
| Active projects | `YYYY <Place/Client> <short name>` | `2026 WB6 Creative Pulse` |
| Active proposals | `YYYY <Client> <short name>` | `2026 British Council Art and Tech` |
| Archive projects | `Archive projects/YYYY Projects/YYYY <name>` | `2017 Projects/2017 GBSLEP creative economy mapping` |

**Rules:**
- Year prefix always (sorts chronologically)
- Single spaces only — no double spaces, **no trailing spaces** (e.g. `2026 Maritime Belfast ` currently has one — breaks path matching)
- Short, stable names — the folder name becomes the register's `drive_folder_path`; renaming breaks the link
- Avoid special characters (`'`, `&`, `:`) where avoidable; smart quotes in filenames cause mismatches

## 2. File naming

| Convention | Example |
|---|---|
| `YYMMDD <descriptor>` | `251024 MITIH Createch Ecosystem Report.docx` |
| Versioned drafts | `..._v2`, `..._v3` |
| Canonical deliverable | copied to toolkit `canonical/PXX-<project>/` — never "final" as a name |

**Rules:**
- Date prefix = date of that version (YYMMDD, matching the YY/MM/DD register convention)
- No "final" in filenames — version numbers and canonical registration do that job (P03 lesson: "final" is a claim, not a fact)
- No `NEW`, `LATEST`, `USE THIS` decorations — the register records which is canonical

## 3. Bid → Project transition

**Recommendation: MOVE, don't duplicate.**

| Stage | Location | Register action |
|---|---|---|
| Bid live | `Active proposals/YYYY <name>/` | `08_tenders.csv` row + `bid_records/TXX_<name>.md` |
| **Bid WON** | **Move folder →** `Active projects/YYYY <name>/Proposal/` | `01_projects.csv` row + PM record + provisional card; `drive_folder_path` = project folder root |
| Bid lost | Stays in `Active proposals/` until archive cycle → `Archive proposals/` | outcome recorded in tenders row + bid record §5-6 |

**On win, create this structure:**
```
Active projects/2026 <Name>/
  Proposal/            <- moved intact from Active proposals
  Project management/  <- PM record, client comms, contracts
  Deliverables/        <- working drafts
  (canonical versions get copied to toolkit canonical/PXX/ at each stage gate)
```

**Why move not duplicate:** one canonical location per piece of work. Duplicating creates "which copy is real?" drift — the same class of problem the canonical_version_protocol was built to kill. The bid record's `08_tenders_row` + the project row's `drive_folder_path` preserve the link both directions.

**Why a `Proposal/` subfolder not flat:** the proposal stays readable as a unit (evaluators ask for bid documents later), and the project folder gains clean siblings for the delivery phase.

**Edge cases:**
- **Bid work is itself a paid commission** (P06/P07 pattern): register row exists from submission; on loss it stays with lifecycle SHORTLISTED_NOT_AWARDED — folder handling same as won (it's still company work delivered)
- **Consortium bids we didn't lead:** same structure; `contracting_role` records the arrangement
- **Direct commissions (no bid):** folder goes straight to `Active projects/YYYY <name>/` with `Proposal/` holding the engagement letter/SOW

## 4. Renaming rule

If a folder must be renamed: update `drive_folder_path` in `01_projects.csv` **in the same action** — the sweep will otherwise flag the old path as deleted + new folder as unregistered. (Sweep makes the breakage visible within 24h regardless, but same-action updating keeps the record clean.)

---
**Approved decisions (Iain, 26/09/12):**
1. MOVE (not duplicate) — proposal folder becomes `Proposal/` subfolder of the project
2. Subfolder name: `Proposal/`
3. Retroactive: one-time tidy approved — in progress (trailing-space fix on Maritime Belfast done; BEYOND scene-setter filed; remaining moves pending bid-outcome confirmation)
