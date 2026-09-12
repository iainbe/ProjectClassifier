# Bid Submission Record — Template

**Purpose:** completed WHEN a bid is submitted — not retrospectively. Captures contribution and outcome-stage detail that is otherwise lost (see P06-COSTAR / P07-CC: "failed bid" was actually shortlisted-on-submission).
**Location:** copy to `bid_records/TXX_<short_name>.md` at submission.
**Feeds:** `08_tenders.csv` row at submission; outcome section completed on notification; register/card/claims updated at outcome.
**ID rule:** `bid_id` = next sequential `T-NN` from `08_tenders.csv` (T03, T04...) — same ID used for the file, the tenders row, and any project row. Do NOT invent a separate ID scheme.

---

## 1. Bid identity (at submission)

| Field | Value | Notes |
|---|---|---|
| `bid_id` | T-NN | Next sequential ID from 08_tenders.csv (T03, T04...) |
| `tender_title` | | As stated by buyer |
| `buyer` | | Organisation holding the contract |
| `contracting_party` | | Who we actually contract with (may differ from buyer — see P02 MMU) |
| `procurement_route` | | FORMAL_RFP / FRAMEWORK / DIRECT_PROPOSAL / CONSORTIUM_BID / GRANT_APPLICATION |
| `deadline` | | |
| `submission_date` | | |
| `submission_portal_ref` | | Confirmation/portal reference |
| `08_tenders_row` | | opportunity_id — same as bid_id |
| `register_row` | | 01_projects.csv project_id IF the bid work itself is a paid commission (P06/P07 precedent) or produces a deliverable body of work — otherwise leave blank |

## 2. Our position (at submission)

| Field | Value | Notes |
|---|---|---|
| `our_role` | | LEAD / PARTNER / SUBCONTRACTOR / ADVISORY / BIDDER / ASSOCIATE |
| `prime_contractor` | | Who holds the head contract if awarded |
| `consortium_partners` | | All partners and their roles |
| `lead_author` | | Who wrote it (names — see P04 lesson: record co-lead at the time) |
| `fifth_sector_contribution` | | SPECIFIC sections/frameworks/methods we designed or wrote — NOT generic "bid support" (see P06/P07 lesson: LEAD/DRIVE/ACCELERATE, five-case structure) |
| `interview_involvement` | | Will Fifth Sector attend interview/presentation if shortlisted? Y/N |

## 3. Value and scope (at submission)

| Field | Value | Notes |
|---|---|---|
| `total_bid_value` | | Full programme/contract value |
| `fifth_sector_value` | | Our fee/share if awarded |
| `delivery_scope` | | What we would actually deliver if awarded |
| `delivery_dates` | | Proposed start/end |

## 4. Evidence base (at submission)

| Field | Value | Notes |
|---|---|---|
| `precedent_cards_cited` | | Which project_index_cards were referenced — link to project_index.csv rows |
| `claims_used` | | Specific claim IDs cited as track record |
| `methods_proposed` | | Methods from 03_methods.csv being reused/proposed |
| `spillover_elements` | | Which spillover types / option elements the bid addresses |

## 5. Outcome (COMPLETE ON NOTIFICATION — do not leave open)

| Field | Value | Notes |
|---|---|---|
| `notification_type` | | FORMAL / INFORMAL / NONE_RECEIVED (see P06 lesson: informal via partner is still a recordable fact) |
| `stage_reached` | | SUBMITTED / SHORTLISTED / INTERVIEW / AWARDED / NOT_AWARDED — record the HIGHEST stage reached, not just the final result |
| `outcome_date` | | |
| `outcome_detail` | | e.g. "shortlisted on submission, unsuccessful at interview — Fifth Sector not involved in interview" |
| `feedback_received` | | Scores, comments, debrief notes |
| `panel_scores` | | Criterion-level scores verbatim if provided (won AND lost bids) — e.g. "Experience 4.00/4, Methodology 4.00/4, overall 92.83%" |
| `feedback_source` | | Who provided it |

## 6. Post-outcome register actions (checklist — complete ALL)

- [ ] `08_tenders.csv`: actual_outcome, outcome_source_id, feedback_status updated
- [ ] `01_projects.csv` (if `register_row` set): lifecycle_status updated (SUBMITTED / SHORTLISTED_NOT_AWARDED / AWARDED / NOT_AWARDED)
- [ ] Index card: lifecycle_status, client_decision_use, precedent_strength updated — record the HIGHEST stage, not just final result
- [ ] `04_claims.csv`: any OPTION claims updated (option_state PROPOSED → EXERCISED/EXPIRED)
- [ ] `09_publication_assets.csv`: if outcome changes what can be cited, update permitted_wording
- [ ] `10_review_history.csv`: entry logged
- [ ] `project_index.csv`: regenerated
- [ ] Repo sync: committed to ProjectClassifier

## 7. Lessons (complete within a week of outcome)

| Field | Value |
|---|---|
| `what_worked` | |
| `what_didnt` | |
| `reusable_material` | Sections/frameworks worth keeping for future bids |
| `next_time` | |
