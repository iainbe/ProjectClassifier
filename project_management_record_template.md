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

## 5. Milestone updates (append one section per milestone/phase — prompts for evidence WHILE it happens)

### Milestone N — [date]

| Prompt | Entry |
|---|---|
| `deliverables_status` | On track / revised / blocked |
| `emerging_findings` | Headline findings so far — numbers where quantified |
| `quantified_results` | Any numbers worth capturing NOW (GVA, jobs, firms, counts) |
| `spillover_observed` | PRODUCT / KNOWLEDGE / NETWORK effects observed or reported — with source |
| `option_elements` | Options proposed / held / exercised during this phase |
| `attribution_events` | Anything Fifth Sector did that others might later claim |
| `problems` | Rejections, disputes, revisions (see P03 lesson: record rejection history as it happens) |
| `new_claims_to_log` | Claim stubs for 04_claims.csv |
| `sources_to_register` | New documents/data for 02_sources.csv |

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
