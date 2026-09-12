# Register Update Workflow — how live work feeds the toolkit

**Purpose:** the bid and project records exist to stop retroactive reconstruction. This document defines the pipeline from live event → register → repo, and who/what triggers each step.

**Canonical location:** this Drive folder (`Website 2026/spillover-toolkit/`) is the working canonical. `Website 2026/ProjectClassifier/` is the versioned git mirror — it receives periodic sync commits. Never edit CSVs in the repo directly; edit here, then sync.

---

## Trigger 1 — Bid submitted

| Step | Action | Artefact |
|---|---|---|
| 1 | Copy `bid_submission_record_template.md` → `bid_records/TND-YYYY-NNN_<name>.md`, fill sections 1-4 | bid record |
| 2 | Add row to `08_tenders.csv` (opportunity_id = bid_id) | register |
| 3 | `10_review_history.csv` entry | audit trail |

**Prompt rule (AGENTS.md):** when Devin is told a bid went out, ask for any empty section 1-4 fields before proceeding — especially `fifth_sector_contribution` (specific, not "bid support") and `interview_involvement`.

## Trigger 2 — Bid outcome received

| Step | Action | Artefact |
|---|---|---|
| 1 | Complete bid record section 5 — record HIGHEST stage reached (P06 lesson: shortlisted-then-lost ≠ failed bid) | bid record |
| 2 | Run section 6 checklist: tenders CSV, project register lifecycle, card precedent/decision-use, claims option_state, publication assets, review history, index regen | registers |
| 3 | Complete section 7 lessons within a week | bid record |

**Prompt rule:** on any outcome mention, ask `notification_type` and `stage_reached` if not stated. Never infer "failed" from "not awarded" — always establish the highest stage.

## Trigger 3 — Project confirmed (work won/commissioned)

| Step | Action | Artefact |
|---|---|---|
| 1 | Copy `project_management_record_template.md` → `project_records/PXX-<name>_pm.md`, fill sections 1-4 | PM record |
| 2 | Add row to `01_projects.csv` (lifecycle = IN_PROGRESS / COMMISSIONED) | register |
| 3 | Create provisional index card from `project_index_card_template.md` (identity fields filled, rest NOT_ESTABLISHED) | card |
| 4 | Register sources in `02_sources.csv` | register |
| 5 | `10_review_history.csv` entry | audit trail |

**Prompt rule:** ask for any empty section 1-3 field at confirmation — especially `contracting_role` (arrangement not ownership), named contributors, and `reference_permission` (ask the client at kickoff; record the answer).

## Trigger 4 — Milestone / phase boundary

| Step | Action | Artefact |
|---|---|---|
| 1 | Append a Milestone section to the PM record — the prompts exist to catch spillover evidence while it happens | PM record |
| 2 | Log `new_claims_to_log` stubs → `04_claims.csv` when material | register |
| 3 | Register any new sources | register |

**Prompt rule:** at each milestone mention, ask the section-5 prompts — especially `spillover_observed` (with source) and `problems` (rejections recorded as they happen — P03 lesson).

## Trigger 5 — Project completion / acceptance

| Step | Action | Artefact |
|---|---|---|
| 1 | Complete PM record section 6 + checklist | PM record |
| 2 | Full-read sources → claims → measurements → index card REVIEWED via walkthrough | registers + card |
| 3 | `project_index.csv` regenerated | index |
| 4 | `10_review_history.csv` entry | audit trail |

## Repo sync (Drive → ProjectClassifier)

| Step | Action |
|---|---|
| 1 | After any register-changing session: `rsync -av --exclude '.git' --exclude '*.bak' spillover-toolkit/ ProjectClassifier/` (or copy changed files explicitly) |
| 2 | `cd ProjectClassifier && git status` — review diff before committing |
| 3 | Commit with message naming the trigger (e.g. "Bid record TND-2026-004 + register update") |
| 4 | Push to `git@github.com:iainbe/ProjectClassifier.git` only when asked |

**Schema-drift rule (from Pass 4 repair):** before ANY CSV edit — verify field count AND positional semantics against the header. Right column count ≠ right values. Check 2-3 existing rows first.

**Stale-artefact rule:** after card or register changes, regenerate `project_index.csv` — it derives from both, so any upstream change makes it stale.

---

## Directory map

| Path | Holds |
|---|---|
| `bid_records/` | Completed bid submission records |
| `project_records/` | Completed PM records |
| `project_index_cards/` | Index cards (client + inward sides) |
| `project_changelogs/` | Per-project change logs |
| `01-10_*.csv` | Canonical registers |
| `project_index.csv` | Derived browse index (regenerate after changes) |
| `tier2_qa_review.md` | Consistency audit |
