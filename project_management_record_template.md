# Project Management Record — Template

**Purpose:** opened WHEN a project is confirmed — not reconstructed later. Captures at inception the fields the register and index card will need (contracting role, contributors, permission), and prompts for evidence capture during delivery.
**Location:** copy to `project_records/PXX-<short>_pm.md` at confirmation.
**Feeds:** `01_projects.csv` row at confirmation; provisional index card created; milestone sections feed `04_claims.csv` / `06_measurements.csv`; completion section feeds card REVIEWED status.

---

## 1. Project identity (at confirmation)

| Field | Value | Notes |
|---|---|---|
| `project_id` | PXX-XXXX | Next sequential ID; check 01_projects.csv |
| `project_name` | | Canonical name for register |
| `client` | | Organisation commissioning the work |
| `contracting_party` | | Who the contract is actually with (may differ — see P02, P05 lessons) |
| `contracting_role` | | PRIME / SUBCONTRACTOR / ASSOCIATE / ADVISORY — the ARRANGEMENT, not ownership (all register work is Fifth Sector work; see P05 lesson) |
| `prime_contractor` | | Organisation holding head contract |
| `other_partners` | | Consortium/delivery partners and their roles |
| `contract_value` | | Total contract value |
| `fifth_sector_fee` | | Fee payable to The Fifth Sector (see P05: record even under associate arrangements) |
| `commission_date` | | |
| `delivery_dates` | | Start → end with milestones |

## 2. People (at confirmation — record WHO does WHAT now, not later)

| Field | Value | Notes |
|---|---|---|
| `fifth_sector_lead` | | |
| `fifth_sector_contributors` | | Named individuals + specific roles |
| `partner_contributors` | | Named individuals + roles (see P04 lesson: "co-lead with Jonathan Todd" recorded 9 years later — record it now) |
| `client_contact` | | Name + role + email (capture at kickoff) |
| `authorship_credit` | | How Fifth Sector will be credited in deliverables |

## 3. Permissions (at confirmation — ask while the relationship is warm)

| Field | Value | Notes |
|---|---|---|
| `reference_permission` | | Can we name this client/project in bids? ASK AT KICKOFF — record the answer |
| `name_in_public` | | Can client/project appear on website/case studies? |
| `confidentiality_terms` | | Contract clauses restricting citation |
| `data_rights` | | Who owns outputs/data; publication rights |
| `permission_record` | | Where the permission is evidenced (contract clause, email) |

## 4. Deliverables (at confirmation)

| # | Deliverable | Due | Acceptance criteria | Accepted? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

## 5. Milestone checklist (self-contained — tick items as they happen, no external prompt needed)

**How to use:** each item below is a standing reminder for the life of the project. Tick `[x]` and date it when done; re-tick a new copy each phase. Copy this block per milestone if you want per-phase records, or maintain it as one rolling list.

### Every deliverable draft sent
- [ ] _Date:_ Version filed under `canonical/` (or named consistently with version records)
- [ ] _Date:_ Emerging findings noted below (headlines, any quantified numbers)
- [ ] _Date:_ Client reaction/problems recorded — including any rejection or revision request **as it happens** (P03 lesson: Jun 2025 rejection was only reconstructable via register notes)

### Every client meeting / workshop
- [ ] _Date:_ Anything the client did with the work noted (decision-use evidence)
- [ ] _Date:_ Spillover observed or reported — PRODUCT / KNOWLEDGE / NETWORK — **with source** (who said it, where)
- [ ] _Date:_ Option elements noted — proposed / held / exercised
- [ ] _Date:_ Anything Fifth Sector did that others might later claim (attribution events)

### Every invoice / phase boundary
- [ ] _Date:_ Quantified results captured NOW — GVA, jobs, firms, counts (don't leave to the end)
- [ ] _Date:_ Claim stubs for `04_claims.csv` noted
- [ ] _Date:_ New documents/data noted for `02_sources.csv`

### Standing prompts (review monthly while project is live)
- [ ] Deliverables table (§4) still accurate? Dates/slippage recorded?
- [ ] Any rejection, dispute or revision recorded — with dates?
- [ ] Any option proposed to client that has since been exercised or expired?
- [ ] Permission status still valid? (§3 — terms can change mid-project)
- [ ] Contributors list still accurate? (people join/leave — P04 lesson)

### Notes log (free text — newest first)
| Date | Entry |
|---|---|
| | |

## 6. Completion (at acceptance — complete ALL)

| Field | Value | Notes |
|---|---|---|
| `acceptance_date` | | |
| `acceptance_evidence` | | Email/letter/minute reference |
| `revisions_history` | | Any rejection/reconciliation cycles (P03 lesson: honest revision history) |
| `client_decision_use` | | What the client did with the work — evidenced or informal |
| `actual_contribution` | | What Fifth Sector actually delivered vs proposed |

### Completion checklist
- [ ] Sources registered in `02_sources.csv` (with read status)
- [ ] Claims extracted to `04_claims.csv` (full-read rule applies)
- [ ] Measurements to `06_measurements.csv`
- [ ] Index card updated → PROVISIONAL, then walkthrough to REVIEWED
- [ ] `01_projects.csv` lifecycle_status → COMPLETED + acceptance evidence
- [ ] Permission fields refreshed in `09_publication_assets.csv` if terms changed
- [ ] `10_review_history.csv` entry
- [ ] `project_index.csv` regenerated
- [ ] Repo sync: committed to ProjectClassifier
