## 26/09/16 — P01-P10 citation_status recorded; clearance view unblocked

**Trigger:** "re-sync to Drive then classify P01-P10 citation"

- `citation_status` added to the ten REVIEWED pilot cards, migrating them onto the 26/09/12 two-field model. All ten are `DELIVERED_WORK`: no publication evidence exists for any of them (`09_publication_assets.csv` records TENDER_ONLY_NOT_WEBSITE for PUB-P01 to PUB-P10), so none qualifies as `PUBLIC_REPORT`
- Attribution caveats carried in the value, not dropped: P03 the accepted deliverable is the Oct 24 reconciliation report; P04 SUBCONTRACTOR to a BOP prime; P05 BOP_ASSOCIATE; P06 shortlisted not awarded; P07 bid NOT_AWARDED; P10 earlier cycles delivered, 2026 cycle still LIVE_WORK
- `reference_permission` untouched — still NOT_ESTABLISHED on nine of ten; citation status is not permission to name the client
- New `cleared_scope` column: all ten read `TENDER_ONLY` because each `reference_status` clears tender naming and holds website publication behind a separate gate. `cleared_for_use=YES` therefore means citable in a tender, not publishable on the website
- `project_index.csv` regenerated: 10 of 68 cleared for use (was 0). Per-project changelog entries written for P01-P10
- Derivations are Devin-derived and marked pending Iain confirmation on each card

## 26/09/16 — Toolkit moved to a shared drive; Drive access is now a service account

**Trigger:** "the scoped robot account needs the org-policy exemption - how?"

- The toolkit now lives in the `Fifth Sector Project Classifier` **shared drive** as `spillover-toolkit/`, moved out of Iain's My Drive `Website 2026/`. File IDs are unchanged, so existing share links and `02_sources.csv` file-ID references still resolve
- Drive access is the `dwvin-drive@project-dashboard-auth-501608` service account (Content manager on the shared drive), replacing the personal OAuth token used earlier today — that remote has been deleted from this machine. Devin's Drive writes are now attributed to a robot account with access to this one shared drive, not to Iain's whole Drive
- Route history, for the record: service-account keys were blocked by the org policy `iam.disableServiceAccountKeyCreation` (exempted for this project only); keys then failed against My Drive with `storageQuotaExceeded`, because service accounts cannot own files in a personal Drive. The shared drive is what makes the robot account viable, not the policy exemption alone
- `tools/drive_sweep.py`: watch roots may now carry a `root` override, so the toolkit can be swept from the shared-drive mount while the project/proposal roots stay in My Drive. The hardcoded DRIFT prefix became `toolkit_path` in the config
- `tools/sweep_state.json` re-keyed (255 of 24,529 entries) from `Website 2026/spillover-toolkit/...` to `spillover-toolkit/...`, so the next sweep reports real changes rather than 255 deletions plus 255 additions
- Path references updated in `tools/JON_ACCESS.md`, `tools/JON_SWEEP_GUIDE.md`, `register_update_workflow.md`. The one-off historical scripts (`register_g2_*.py`, `extract_text_*.py`, `deepen_*.py`) keep their old absolute paths — they are spent run-once artefacts, not live tooling
- **Iain action:** Drive for desktop must have the shared drive available locally before the next scheduled sweep, at `Shared drives/Fifth Sector Project Classifier`

## 26/09/16 — Drive canonical re-synced

**Trigger:** "re-sync to Drive then classify P01-P10 citation" (first half, completed after credential resolved)

- Access route: service-account keys are blocked in the Google org by `iam.disableServiceAccountKeyCreation`, so the route is now an rclone OAuth token for Iain's own Google account, held as the org secret `RCLONE_DRIVE_TOKEN`. The abandoned `GOOGLE_DRIVE_SERVICE_ACCOUNT_JSON` secret never contained a key
- 26 files pushed to `Website 2026/spillover-toolkit` — the files changed since the 26/09/12 corpus gate (index, indexer, ten cards, ten per-project changelogs, three closure artefacts, protocol). Verified with `rclone check --download`: 26 matching, 0 differences
- Before overwriting, every replaced file was compared against its pre-session repo version and found byte-identical, so nothing edited in Drive since the last sync was clobbered
- Copy only — no Drive deletions and nothing outside the changed-file list touched

## 26/09/16 — Megaplan resumed: SKiN index corrections

**Trigger:** "Resume #megaplan" — next machine-doable step from the 26/09/12 corpus gate (SKiN corrections 1-3)

- `tools/regenerate_index.py` extended: derived `cleared_for_use` + `cleared_blocker` gate (REVIEWED card AND citable `citation_status` AND `reference_status=CLEARED`), controlled `precedent_strength` (STRONG/MODERATE/WEAK/NOT_ESTABLISHED) with the original wording moved to `precedent_note`, plus `citation_status`/`reference_permission`/`reference_status` surfaced and `arc_tags` for multi-project geographies
- `project_index.csv` regenerated: 68 rows, 68 carded, no pre-existing column values changed; strengths now 24 STRONG / 35 MODERATE / 6 WEAK / 3 NOT_ESTABLISHED (was polluted with sentence values)
- **Finding: `cleared_for_use=NO` for all 68.** The 10 REVIEWED pilot cards (P01-P10) predate the two-field citation model — they carry `commercial_reuse=APPROVED_NAMED` and `reference_status=CLEARED` but no `citation_status`. The gate does not infer citation_status from commercial_reuse; migrating those 10 cards is the unblocking step and needs Iain's per-card DELIVERED_WORK/PUBLIC_REPORT call
- Arc tags: LIVERPOOL_LCR 9, MANCHESTER 6, WAKEFIELD 6, LANCASHIRE 5, WEST_MIDS 3, SOUTH_YORKS 3, DERBY 3, KIRKLEES 2, SOLENT 2 — browsing view only, never a claim that tagged projects are the same project
- Gate routes still human-gated and untouched: R3 walkthrough of the ~15 highest-precedent cards, sending the 35 DRAFTED permission asks, 26 blank `contracting_role` fields
- Sweep check (session-start rule): `SWEEP_LATEST.md` (26/09/12 10:15) shows DRIFT only, all from our own session edits — nothing outstanding

## 26/09/16 — Agent harness protocol (Alpha lead, GLM sidekick)

**Trigger:** "Harness Alpha as main agent and GLM as sidekick" — Alpha = ChatGPT (plan), GLM-5.2 (implementation)

- New `agent_harness_protocol.md` (PROPOSED, awaiting Iain's approval): roles, cycle, work-package and implementation-return formats, inherited toolkit rules, access terms, failure handling
- Standing rule set: no external agent writes to a register — Alpha and GLM produce plans and candidate content only; Devin or Iain apply every register change
- Access follows the existing `tools/JON_ACCESS.md` route: Drive share links/file IDs, never filesystem paths; local scripts stay with Iain/Devin
- Phase 2 (API integration under `tools/agents/`) documented but **not authorised** — open questions on billing route, return retention and whether client-identifying material may enter either vendor's context
- No register data changed this session

## 26/09/12 — Cardless batch complete: all 68 projects carded

**Trigger:** "keep working through all outstanding cards, in batches"

### Coverage
- 46 new PROVISIONAL cards written across 6 thematic batches (evaluations, strategies A/B, bids/Derby/Lancaster, BOP-era specialist, misc/live)
- `project_index.csv` regenerated: **68 rows, 68 with cards, 0 cardless, 0 orphans**
- Per-project changelogs created for all newly carded projects
- `11_permission_requests.csv` extended: +26 seeded client asks (PR-10..PR-35), all DRAFTED — tracker now covers all carded projects' clients; none sent

### Notable finds during batch drafting
- **P11-ELFC** is the toolkit's origin document: GLA Economics note explicitly demanded spillover/externalities evidence (2017); contains the earliest gated investment sequence (4-stage, LCF-relocation trigger)
- **P32-SURREY**: Farnborough aerospace→screen — cleanest literal cross-sector spillover case in the register
- **P50-UKRI**: "Liverpool second most filmed UK city outside London, 6x public-investment return" + innovation-access gap (<20% grants, 4 scale-ups) — the CoSTAR origin engagement
- **P46**: Capital Investment Leverage Framework + levelling-up arithmetic + clustering premia (223%/170%) — strongest method-export set
- **P51**: evaluation-without-baseline design; **P43**: honest failure analysis — the integrity pair
- **P57**: SIC-misclassification quantification (games +50-60 businesses; experiences 4.4x) — sharpest hidden-economy method demo
- **P52**: documented non-adoption (council could not accept recommendations) — recorded honestly; P84 proposal cites it as cautionary precedent
- **P52 option states** flagged for possible revision toward EXPIRED given non-adoption — needs verification
- **P85**: PO0127+PO0130+INV-1371 registered — £10k engagement is documentary, not just confirmed
- **P86**: 92.83% scorecard registered; award pending post-standstill

### Flagged for Iain (collated in session report)
- ~15 contracting_role blanks (LEAD_CONSULTANT noted but arrangement unrecorded)
- Option-exercise status unverified across most PROPOSED options
- Several adoption/outcome questions per card's unresolved_issues

## 26/09/12 — Cardless batch 1 + project_id cascade

**Trigger:** "Proceed" (cardless card production after draft walkthrough)

### New cards (PROVISIONAL, awaiting Iain walkthrough)
- **P15_LIVMUS**: verified vs SRC-G2-010 — £100.5m turnover/2,360 jobs; >£200m full-footprint figure captured (direct+downstream framing anticipates P22 distinction); BOP prime → contribution framing TBC
- **P19_LCRIMM**: verified vs SRC-G2-014 — 169 orgs/126 cos/600+; Meetup 4-city benchmarking; gated investment options PROPOSED; Iain named co-author (stronger citation basis than P15)
- **P21_MMUCCI**: verified vs SRC-G2-016 — REF-2021-invisibility finding ("second of ALL UK HEIs... buried four clicks down"); PRIME role

### project_id cascade (orphan-card fix)
- 8 bare IDs upgraded to suffixed convention: P64→P64-BCJ, P69→P69-OURYEAR, P75→P75-LANC, P78→P78-BEATLES, P79→P79-CELL, P81→P81-WB6, P82→P82-KOTOR, P83→P83-BCWB
- FKs cascaded: 04_claims 87 fields, 02_sources 17, 01_projects 17, 08_tenders 2, 11_permission_requests 3, 10_review_history 18 structured fields (record_id/source_ids only — prose verbatim)
- **Incident:** first cascade write truncated 10_review_history (ragged row, None key) — restored from mirror, re-applied with row-level handling; 317 rows verified intact
- project_index.csv regenerated: 25 cards mapped, 43 cardless (was 46)

### Residual
- 3 new cards PROVISIONAL — Iain walkthrough pending
- Cardless backlog: 43

## 26/09/12 — Draft-card walkthrough complete; permission tracker created

**Trigger:** "review draft cards; use that as a test for client-permission"

### Card walkthrough resolutions (all 12 drafts)
- **P81**: SUBCONTRACTOR via BEYOND framework (contract awaited, invoice on receipt); Phase 2/3 marked PROPOSED not contractual; contract to carry method-attribution + citation-permission clause — new contract-practice rule added to AGENTS.md
- **P82**: SUBCONTRACTOR to University of Plymouth — FCDO contracted to UoP via BC, never touched TFS; "FCDO-funded" now qualified as programme-level
- **P83**: DIRECT — BC framework agreement, 40-day completed diary of engagements; separately funded from UoP pilot
- **P27**: DIRECT to Wakefield Council; Wakefield dual-ask agreed (P27+P64+P69)
- **P33**: published credit line verified verbatim — "The Fifth Sector Limited / Unscrambled.world — In partnership with University of Liverpool IPM"; Unscrambled=TFS subcontractor (no ask), IPM=Next Wave partner (implied); £75m Table 18 confirmed; commissioner TBC (likely LCC)
- **P22**: DIRECT via LCR Combined Authority; ask names data-vs-evaluation distinction explicitly
- **P16**: claims CAPPED at "contributed to" (Iain) — specific attribution too distant to secure; C-G2-024 rewritten; PR-07 set CAPPED/do-not-send
- **P78**: client = Beatles Legacy Group (unconstituted) — funding counterparty Liverpool BID
- **P79**: two-tier permission structure (citation now; data-reuse at clarification)

### New register: `11_permission_requests.csv`
9 requests seeded — PR-01 BEYOND contract clause; PR-02 UoP; PR-03 Wakefield dual (3 projects); PR-04 LCC commissioner (TBC); PR-05 LCR CA (+bundle check); PR-06 Lancaster bundle (P75/P87); PR-07 BOP/Frontier (CAPPED); PR-08 Liverpool BID; PR-09 LLDC two-tier.
Fields: client, contact, project_ids, scope, proposed_wording, channel, dates, status, notes — Iain-managed manually.

### Open items carried
- P78: 2016 predecessor-study provenance (repeat-measurement claim) — unconfirmed
- P33: commissioner confirmation (likely LCC)
- P81: ~15 folder docs unregistered; client email unread
- All permission statuses DRAFTED — none sent

## 26/09/12 — P79/P85 external-event statuses (Iain)

- **P79-CELL**: reporting stage COMPLETE; lifecycle corrected from DELIVERED ambiguity. Pending = client clarification on data presentation for reuse in CoSTAR Showcase bid. HARD STOP recorded: AHRC Showcase Labs call closes 26/10/29 16:00 UK (opened 26/08/24; surgeries w/b 26/09/28; ≤£4m FEC/lab, ≥50% match; award from April 2027).
- **P85-AMGEN**: full-submission outcome at AHRC discretion — external, unactionable; noted.
- **T14-COSTARSHOW** tender row registered so the deadline is tracked in the register.

## 26/09/12 — Section E corrections (Iain)

- **P86**: standstill ends 26/09/18 — FUTURE event (my "confirmable now" was wrong; award confirmation follows standstill + contract prep). Notes corrected.
- **T01**: proposed contract start recorded as PROVISIONAL Sep/Oct 2026 subject to contract (per UK1412milestones — 12-month programme, Dec 2026-Aug 2027 milestones). Award decision date not in RFP extract — remains pending.

## 26/09/12 — Section D verification items (P69/P64)

**Trigger:** "Continue to D"; user corrections: funding letter is Council-held (not provided to us); committee reports requested and withheld — use report budget figures.

### P64-BCJ — evidence basis now precise
- WYCA confirmation letter: held by Wakefield Council, not provided to Fifth Sector — recorded as EXTERNAL_HELD, search closed (not a gap).
- Committee reports: requested repeatedly and not provided — documented unavailability, per Iain do not rely on this route.
- Funding evidence anchored to report budget figures: WYCA **£850k** per OY final report (BBC public record says £800k — £50k variance flagged; report takes precedence).
- New documentary source: SRC-R5-015 — Wakefield Council PO 6040004958 (£12,500+VAT, 22/11/25) for the Impact Framework/Strategic Assessment — the BCJ commission itself now PO-evidenced.
- Attribution status: funding VERIFIED; BCJ→unlock = USER_CONFIRMED mechanism + temporal sequence.

### P69-OURYEAR — adoption claim right-sized
- Report's own wording is offer-of-template ("offers valuable learning... provides a template"), not claimed adoption — card now reflects offer + committee-noting.
- External support found anyway: WYCA CH&S Committee 14/03/25 resolved findings inform "planning and approving future large-scale cultural activities"; Years of Culture campaign continues across districts.
- Report budget verified in extract: £4.2m total, £1.965m/47% external, £850k WYCA, £2.4m Council budgets, £359,699 match (43.1% vs 3-5% typical).

### Residual D item
- reference_permission NOT_ESTABLISHED on all cards — requires client-permission exercise (Iain-led); checklist offered.

## 26/09/12 — Section C: all five quantified inconsistencies resolved

**Trigger:** user instruction "in order" — working the Section C register one at a time.

### Resolutions
1. **P27 FTE** — RESOLVED from source: cite **160 FTE** (Table 14 itemised breakdown: 40 PP workspace + 14 XPLOR + 1 traineeship + 40 PP businesses + 35 WX + 30 Xcellerator, labelled "verified, distinct, non-overlapping"). The 120 in exec summary/headline table is a stale draft figure. Secondary slip recorded: "35 new jobs" = 35 businesses; jobs = 30. C-G2-058 rewritten.
2. **P75 £1,499.70 vs £10k** — RESOLVED by Iain: INV-1357 = initial stakeholder workshop for the CICP2 bid — belongs to **new project P87-TRUENORTH**, not the P75 Places commission. SRC-R5-001 reassigned; P87 registered (live bid, paid workshop + Foresight proposal + Letters of Commitment + match-funding analyses). P75's £10k payment doc remains unlocated — flagged.
3. **P22 cumulative totals** — RECONCILED arithmetically: £12.08m = £1.788M×6.76 ratio-implied total activity (incl. induced); £6.73M = direct LCR spend (Olsberg Type II ~1.8 gap). £3,930/job = £1.788M÷455 interim; £3,284 = £2.82M÷859 final. Claims now carry both interim (2021) and final (2025) positions.
4. **P08 £4.0bn vs £4.5bn** — RESOLVED: cite **£4.0bn** (exec summary + analysis + appendix Table 8 LinkedIn 2024 = 4,000.0 £m). £4.5bn is a single narrative instance inconsistent with its own underlying table — stale draft figure.
5. **P06 Create Growth dates** — RESOLVED: cite **2022-2025** (DCMS actual); "2023-26" in same document is ACE NPO-settlement conflation. C-G2-444 proposition corrected.

### New registrations
- P87-TRUENORTH project (Lancaster CICP2 bid support — paid workshop + bid analyses)
- SRC-R5-014: Lancaster PO 5002151418 (£4,158.33+VAT, Oct 2025) on P76 Horizon bid — paid engagement evidence on a NOT_AWARDED bid
- Lancaster engagements now cleanly separated: P75 (Places evidence), P76 (Horizon bid), P87 (True North workshop + bid support)

### Section C status: COMPLETE — zero open quantified inconsistencies

## 26/09/12 — P86 outcome letter registered; score-capture rule added

**Trigger:** user filed Creative Scotland outcome email into project folder; instructed scores be logged for successful and failed proposals.

- `SRC-R5-013` registered: Creative Scotland tender outcome letter (Kelly Neill, 26/09/04) — preferred bidder, standstill ended 26/09/18, intent to award post-standstill. Reg 32(2) Public Contracts (Scotland) Regs 2006.
- `T13-CSSAL` row added to `08_tenders.csv` — the bid previously existed only as project row P86; now has full tender record with evaluation weights + outcome fields.
- **Panel scores logged** (verbatim): Price 3.71/4 (30%), Experience 4.00/4 (25%), Methodology 4.00/4 (20%), Team 3.33/4 (15%), Added value 3.00/4 (10%); overall weighted **92.83%**. Claim C-R5-527 updated; evidence link E-R5-007.
- **Score pattern noted for calibration:** maximum marks on the two criteria the evidence-led positioning feeds (experience/track record, approach/methodology); weakest on added value and team — actionable for future submissions.
- Score-capture rule added to `tender_scorecard_template.md` §8 (buyer panel scores table), `bid_submission_record_template.md` §5 (`panel_scores` field), and AGENTS.md bid-outcome trigger — verbatim scores required for won AND lost bids.
- Residual: standstill ended 26/09/18 — contract signature confirmation still pending; on award, lifecycle→CONFIRMED + PM record per Trigger 3.

## 26/09/12 — Sweep-agent VERSION_AMBIGUITY + Section B source registration

**Trigger:** user instruction "Make changes to sweep agent and future extraction; log in #changelog and move to B"

### Sweep agent + extraction rules
- `tools/drive_sweep.py`: added VERSION_AMBIGUITY finding — registered sources whose controlled_location resolves to a directory holding multiple candidate files now emit a canonical-version-review finding (joins ordering + attention count). Rationale: near-misses at WMGC (v1 picked over canonical v2a), Herefordshire (chapter over final strategy), UoL CPD (non-existent path).
- `tools/JON_SWEEP_GUIDE.md`: VERSION_AMBIGUITY row added to category table.
- `AGENTS.md`: extraction rules inserted — folder locators are ambiguous until candidates reviewed; prefer canonical/latest designated version; extract tables + paragraphs; record exact selected file; two-archive check before absence verdicts.

### Section B — three source-less projects now registered (11 sources, 5 claims, 6 evidence links)
- **P85-AMGEN**: folder located at `Google project folders/2026/` (missed by earlier year-root sweeps); drive_folder_path fixed. Sources: Microcluster Evidence Pack (canonical Places deliverable), Theory of Change Multi-Route Analysis, PO0127+PO0130+INV-1371 (formal paid-engagement trail — PO0130 dated 26/06/11), EOI+feedback. Evidence pack extracted (15,153 chars incl. tables): 8 Welsh microclusters classified core/supporting/review-drop with explicit claim-use limits — Places claim discipline mirrored. Claims C-R5-524–526 registered.
- **P86-CSSAL**: sources registered — tender brief, Schedule 4 Technical Proposal FINAL (submitted), Schedule 2 pricing + Schedule 5 form of tender, Salary Review + Benchmark Tool deliverables. Licence caution recorded: `DO NOT SEND - Lightcast originals` folder — originals not for circulation. Preferred-bidder letter is email-held, flagged as source-not-located. Claim C-R5-527 registered.
- **P35-DERBYMAP**: sources registered — Derby Cultural Masterplan FINAL (canonical), Manifesto v3 + Compact governance (extracted, 18,594 chars), ENQ692 signed outcome notification (won-commission evidence). Claim C-R5-528 registered.

### Residual
- P86 preferred-bidder letter: email-held, not in folder — request filing into project folder.
- P35/P85/P86 cards not yet produced (45 cardless count unchanged; these remain in the queue).
- Extract coverage: P85 pack + P35 manifesto extracted; P35 masterplan FINAL (hi-res PDF) and P86 Schedule 4 FINAL (PDF) registered but extraction pending.

# CHANGELOG — Spillover Toolkit

Session-level record of all changes. Per-project detail lives in `project_changelogs/`; per-item audit trail in `10_review_history.csv`; QA findings in `tier2_qa_review.md`.

**Update rule (AGENTS.md):** this file, `tier2_qa_review.md` and `10_review_history.csv` are updated at the END of every work session — no exceptions, no reminders needed.

---

## 26/09/12 — Live-work capture system + date normalisation

- **Templates:** `bid_submission_record_template.md`, `project_management_record_template.md` created; milestone prompts converted to self-contained checklist
- **Workflow:** `register_update_workflow.md` — 5-trigger pipeline (bid submitted → outcome → confirmed → milestone → completion) + repo sync
- **AGENTS.md:** live-work capture rules, schema-drift rule, stale-artefact rule, YY/MM/DD date convention, session-closure rule added
- **SHELDON+SKiN review:** ID scheme fixed (T-NN aligned to 08_tenders); register-row rule codified; `tools/regenerate_index.py` persisted with built-in schema-drift check
- **Dates:** ~2,300 conversions to YY/MM/DD across all registers/cards/docs; `extracted_text/` untouched; `tools/normalise_dates.py` persisted
- **Schema repairs:** `08_tenders.csv` T02/T03/T04 extra-field drift fixed (3rd drift instance this session)

## 26/09/12 — R3 card walkthrough complete + permissions cleared

- **All 10 pilot cards REVIEWED:** P04-P09 (earlier) + P01, P02, P03, P10
- **Register schema repair:** 15 pilot rows realigned; 74 claim fields realigned; backups retained
- **Permission gate:** all 10 projects APPROVED_NAMED for tender citation; `09_publication_assets.csv` populated (TENDER_ONLY — website gate separate)
- **Corrections:** P06/P07 shortlisted-not-failed (precedent WEAK→MODERATE); P03 rejection history recorded; P10 option informal/unevidenced
- **Index:** `project_index.csv` created (65 rows)

## 26/09/12 — Method QA (five-agent review)

- **QA of overall method** using SHELDON/THAD/DEEPTHINK/BLINDSPOT/SKiN/WISHFUL: register schema-drift found (15 rows); walkthrough method validated; self-attestation provenance preserved
- **Audit:** Pass 4-5 appended to `tier2_qa_review.md`
- **Skills:** reviewer skill family committed to ProjectClassifier repo (commit 40113e0)

## 26/09/12 — Drive sweep agent installed

- `tools/drive_sweep.py` + `tools/sweep_config.json`: periodic Drive scanner — detects new/changed/deleted files, classifies gaps (UNREGISTERED_PROJECT?, POSSIBLE_TENDER, DRIFT, SOURCE_UPDATED, UNREGISTERED_SOURCE), folder-level collapse
- `sweep_reports/` created; SWEEP_LATEST.md always current + dated snapshots
- launchd job installed: weekday 09:00 (`com.thefifthsector.toolkit-sweep`)
- Register fix: drive_folder_path filled for P75, P78, P79, P80, P81, P82, P83 (Active projects folders)
- Baseline findings: Creative Scotland Salaries (69 files) unregistered; ~10 unregistered Active proposals folders; 5,805 unregistered sources in registered project folders
- AGENTS.md session-start rule added (check SWEEP_LATEST.md)

## 26/09/12 — Sweep README + naming/transition protocol (draft)

- `tools/README_sweep.md`: plain-language agent doc for sharing (Jon testing) — what it does, how to test, matrix tuning, honest limitations
- `naming_and_transition_protocol.md` DRAFT: folder/file naming conventions codified (YYYY folders, YYMMDD files, no-trailing-spaces); bid→project = MOVE to `Active projects/YYYY Name/Proposal/` (single canonical location); renaming rule (same-action register update)
- Open questions left for Iain/Jon: move vs duplicate confirmed?; `Proposal/` vs `Bid/` naming; retroactive tidy vs forward-only

## 26/09/12 — Protocol approved + proposal triage registered

- Protocol APPROVED: move (not duplicate), `Proposal/` subfolder, one-time tidy
- Tidy done: Maritime Belfast trailing space fixed; BEYOND scene-setter filed; NO proposals are won/live-as-project (Iain) — all stay in Active proposals
- 7 unregistered Active proposals triaged from folder evidence and registered: T06-BEYOND, T07-BTM, T08-BRUSSELS, T09-CSG, T10-MARBEL, T11-NEXTWAVE, T12-PLYIMM (08_tenders rows + bid_records created; buyer/stage inferred, marked for Iain confirmation)
- drive_folder_path filled for 7 Active-projects register rows

## 26/09/12 — Live tender test (T01-BCAT) complete

- Requirement map + precedent match run on live bid (UK_1412, deadline 26/09/26, budget £65k+VAT, eval 20/30/50)
- VERIFIED against register: Liverpool £406m→£780m (canonical SRC-G2-028: £405.9m→£779.8m), MITIH gated sequence, FGTG, NES 200+ firms, P22 Film Fund, P75 True North, P83 BC reports
- CAUGHT: AMGEN (USW AHRC) + Creative Scotland Salaries cited in live bid but UNREGISTERED; P64/P69 possible duplicate; T01 had no bid record (created retrospectively); FGTG client wording tension (bid: GMCA/Innovate UK; register: MMU prime)
- Clarifications intel surfaced: UK-return priority (Q6), transferable methodology (Q7), insurance negotiable (Q8/9)
- Gap: ODA/international development = weakest essential criterion

## 26/09/12 — Cited-but-unregistered projects fixed

- P85-AMGEN registered: DIRECT_PROPOSAL to University of South Wales (Iain) — PRIME, Places evidence for USW-led AMGEN CICP2 bid
- P86-CSSAL registered: Creative Scotland Salary Benchmarking — PRIME, proposal pack submitted, award status flagged for confirmation
- P64/P69 cross-linked as related-but-distinct commissions (framework design vs evaluation delivery); date inconsistency on P64 sources flagged
- T01 bid record updated with register anchors

## 26/09/12 — P86-CSSAL status: PREFERRED_BIDDER

- Creative Scotland letter: preferred bidder; award confirmed after standstill ends 26/09/18 (Iain)
- On confirmation → workflow Trigger 3: PM record + provisional index card

## 26/09/12 — P64 resolved: Business Case Justification, outcome CONFIRMED

- BCJ = Business Case Justification (Iain); delivered Oct 22-Mar 23; WYCA confirmed funding to Wakefield Council
- P64 dates corrected (23/01→22/10 start per source dates); renamed; distinct-commission link to P69 confirmed
- Claim C-R4-001 added: funding-unlock outcome, option value EXERCISED — BCJ unlocked the programme P69 evaluated

## 26/09/12 — P02-FGTG client clarified (Iain)

- Man Met commissioned + project-managed on behalf of GM partners and universities — Fifth Sector contracted to MMU as consortium lead
- T01 wording flag resolved: recommended edit logged in bid record (name MMU as commissioner, not GMCA/Innovate UK)

## 26/09/12 — P85-AMGEN completed (Iain)

- USW initial bid shortlisted; Fifth Sector direct proposal accepted (£10k incl VAT); Places evidence for full submission COMPLETED; USW outcome pending
- Claim C-R4-002 added; P06/P07 wording pattern applies (completed evidence work, not funded project)

## 26/09/12 — T01-BCAT SUBMITTED

- Bid submitted ahead of 26/09/26 deadline (Iain); documents frozen — no wording changes applied
- Tenders row → SUBMITTED_AWAITING_RESULT; bid record updated; outcome trigger armed
- NOTE: FGTG wording recommendation NOT applied — submitted version retains original text

## 26/09/12 — QA pass + session-closure enforcement

- REVIEW (agents lenses): sweep script + README + workflow + registers re-checked
- BUG FIXED: sweep state tuple-vs-list comparison made every file report "changed" (24,501 false deltas) — fixed to list() compare; now correct deltas
- FIXED: dead seen_folders code removed; stale TND- example in workflow; README path unusable for Jon (full path + machine-varies note); 6 review-history IDs normalised to hyphenated
- DOCUMENTED: sweep blindspots — empty folders invisible, renames show as delete+new, gdoc stubs approximate, DRIFT fires on own session edits
- AUTOMATION: tools/check_session_closure.sh installed as repo pre-commit hook — commits changing toolkit files without all 3 audit artefacts (CHANGELOG/audit/history) are blocked; --no-verify bypass for emergencies

## 26/09/12 — Jon access note

- tools/JON_ACCESS.md: web-Drive route (jon@thefifthsector.co.uk) is canonical access; share links/file IDs (not filesystem paths) for pulling into Places; script-running requires local mount (Iain-side)
- README_sweep.md updated to point at access note

## 26/09/12 — Jon docs folded + tenders-folder matching

- tools/JON_SWEEP_GUIDE.md: single doc for Jon (access route, what sweep does, categories, web-testable checklist, limits, feedback format); replaces JON_ACCESS.md + README_sweep.md (deleted)
- Sweep improvement: Active proposals folders now matched to 08_tenders via 'Drive folder:' notes (T01/T02 recorded) — registered tender folders classify TENDER_FILE instead of UNREGISTERED_PROJECT?

## 26/09/12 — Repo pushed + register-extension batch B (6 cards)

- Repo pushed to GitHub (16 commits, 40113e0..2e7d2d7)
- Priority cards created: P81-WB6 (skills-pivot + 3-phase gated funding), P82-KOTOR (ministerial declaration — dates corrected 25→26 on file evidence), P83-BCWB (3-country institutional design, honest incompleteness), P27-WAKECDF (Green Book anchor: £22.03m from £4.38m), P64-BCJ (funding-unlock, option EXERCISED), P69-OURYEAR (£4.2m evaluation, model adopted by WYCA/ACE)
- All DRAFT pending Iain walkthrough; flags: P81 lacks claims/sources rows, P82 year-error confirm, P64 WYCA letter to register
- project_index.csv regenerated

## 26/09/12 — P82 date correction REVERTED (my error)

- Iain clarified: TWO Berlin Process events — Kotor 2025 ministerial + Herceg Novi 2026 forum
- My earlier "correction" (25→26) conflated them: reverted P82 register + SRC-G2-083/084 to 25/05 (Kotor 27-28 May 2025 — correct per filenames 250527/250528 in 2025 Projects)
- 2026-dated materials (briefing, EWG report, contract addendum) = Herceg Novi 2026 follow-on — flagged in card as phase-boundary question for Iain
- Lesson: filename-year inference is not sufficient when two same-named events exist in different years — confirm before correcting

## 26/09/12 — P82/P83 confirmed one CEC programme arc

- Iain: Kotor 2025 + Herceg Novi 2026 + council development = same Creative Economy Councils work, all phase-complete awaiting instruction
- Cross-links recorded on P82/P83; P82 card updated

## 26/09/12 — Batch B2: 6 citation-value index cards

- P33-LCRMUS (£406m→£780m multiplier — flagship quantified precedent), P22-LCRFILM (£6.76:1 leverage + EXPIRED-forecast example), P75-LANC (AHRC CICP2 pending), P16-CICP (national evaluation design, subcontractor), P78-BEATLES (~£10k live), P79-CELL (74k LinkedIn supply-chain map)
- All DRAFT pending Iain walkthrough; index regenerated

## 26/09/12 — Adversarial card review: challenges 1-3 resolved

- P22: SRC-G2-030 final eval located (2024 Liverpool Production Fund) + extracted; £6.76:£1→£8.69:£1, 455→859 FTE verified in tables; provenance = LFO-supplied data via Olsberg/Nordcity model + x2.0 Type II multiplier (client's agreed method, not Fifth Sector's)
- P27: SRC-G2-022 CDF Evaluation FINAL found on OneDrive (pre-migration archive) + extracted; all headline figures verified verbatim; FTE inconsistency specified (120 Table 14 vs ~160 narrative); Green Book/WELLBY framing corrected — not the report's language; Green Book provenance = Steve Sheppard/Adroit Economics HMT credentials in proposal
- P81: gated sequence £5k→£80-100k→£150-300k VERIFIED in client note v2 table (earlier "unverifiable" verdict wrong — table scan missed); stage flux = key BC staff departure mid-project (Iain)
- 02_sources.csv truncated by failed write (schema-drift hazard recurrence) — restored all 111 rows from repo mirror; SRC-G2-030 + SRC-G2-022 extract paths linked

## 26/09/12 — Card challenges 4-9 resolved

- P16: £80m corrected to £61m programme (£55m core, per official Frontier/BOP final eval — web-verified); £80m was press co-investment total; CICP2 = £50m initial
- P33: £75m export lever VERIFIED in Table 18 (earlier challenge was false positive — bare numbers under £m header); full lever menu added: £100m IP + £75m export + £60m formalisation + £50m venues + £43m music-tech = £328m→£630m
- P75: invented "remittance advice" claim removed; fee status UNCONFIRMED
- P69: adoption claims marked EFFECT-REPORTED (external confirmation not located); National Library of Korea corrected
- P82: FCDO basis marked Iain-confirmed
- Review blindspots logged: (a) docx paragraph-only scanning misses tables; (b) grep for "£N" misses bare numbers under currency headers — verification must extract tables + check bare numerics

## 26/09/12 — Two-field citation model adopted; challenges 10-11 closed

- New model (Iain-approved): citation_status (PUBLIC_REPORT/DELIVERED_WORK/LIVE_WORK/UNSUBMITTED — what we may truthfully say) + reference_permission (ESTABLISHED/NOT_ESTABLISHED — may we name the client as referee). "APPROVED via use" banned — usage is a fact, not a permission
- Applied to all 12 draft cards; card template + codebook_v1.3 + AGENTS.md updated — the model now governs how claims are cited in reports and bids
- P75: direct proposal £10k incl VAT (Iain) — PRIME confirmed
- P79: lifecycle corrected to REPORTING_COMPLETE — next phase pending client agreement on data format for CoSTAR Showcase bid reuse

## 26/09/12 — P75 remittance verdict REVERSED (OneDrive check)

- lu_remittance_advice_8032520.pdf EXISTS in OneDrive archive (P75 folder + P76 folder): £1,499.70 paid 26/05/08 vs INV-1357 (26/02/09) to The Fifth Sector Ltd from Lancaster University
- Earlier "fabrication" verdict was wrong — file was in the pre-migration archive, not the G Drive live folder; registered as SRC-R5-001
- Residual: £1,499.70 vs £10k proposal — amount relationship TBC (part-payment or separate invoice)
- Rule added: fabrication verdicts require checking BOTH archives — G Drive live folders are incomplete pre-migration

## 26/09/12 — Evidence-gap sweep: all 13 claim-linked unextracted sources resolved

- Extracted + linked: SRC-G2-035 (Lancashire), -039 (WMGC v2a canonical — was about to use v1), -040 (WMGC brief), -058 (Leicester 249k), -062 (UoL CPD — location corrected to Reporting deliverable), -064 (P64 logic chain), -066 (WYCA WYCreate), -070 (Wakefield SNA), -072 (Herefordshire FINAL — was about to use a chapter), -076 (Virtual Agora), -078 (Beatles), -082 (WB6 LinkedIn), -084 (Kotor agenda)
- Two wrong-file catches: WMGC dir-pick chose oldest version, Herefordshire dir-pick chose a chapter — corrected to canonical/latest before linking
- Register integrity checks all pass: no orphan claims, no missing option_state/value_basis, no duplicate IDs


## Session 26/09/12 (3): Five-gate corpus review

- **Five-lens adversarial review** of the full corpus (THAD/SKiN/WISHFUL/deepthink/blindspot) before case-level confirmations: `corpus_gate_review_260912.md`. Verdict: PASS to proceed, 3 standing conditions (only REVIEWED+CLEARED cards cited; permission precedes naming; role-attribution sentence rule).
- **Integrity scan:** 68 cards (10 REVIEWED/12 DRAFT/46 PROVISIONAL); 568 claims (all now evidence-linked); ~96% of claims carry no resolved permission state; 26 blank contracting_role; 27 projects PENDING.
- **2 orphan claims linked**: C-R4-001 (P64 BCJ delivery→SRC-R5-015 PO), C-R4-002 (P85 shortlist/proposal→SRC-R5-004 POs). Evidence links now 587.
- **Spot verification:** batch-card headlines confirmed verbatim against extracts (P34 £5.25bn/39,980 BRES; P32 £7.2bn/17,000 companies/Farnborough; P52 £492m/£616m/1,335 makers).
- **Key deepthink finding:** the signature "hidden workforce" claim survives as "alternative-data estimate" but a definitional-difference-vs-measurement-correction caveat must follow it into prose.
- **Key blindspot finding:** client-outcome-vs-Fifth-Sector-role conflation is the fatal risk if it reaches tender prose; the register discipline must survive translation.


## Session 26/09/16: Sweep resumed; canonical moved to Shared Drive; P78 corrected

- **Canonical folder moved to Shared Drive** (`Fifth Sector Project Classifier/spillover-toolkit`) — service-account robot access instead of personal token; mirror synced.
- **Sweep run** (first since 26/09/12): 24,728 files tracked; 1 unregistered folder (Skills prompts — non-project, SKiN/WISHFUL definitions); 100 unregistered sources (90 P78 Beatles, 1 P81-WB6 v2.1, others); 4 VERSION_AMBIGUITY; 175 DRIFT (expected, empty-state artifact).
- **P86-CSSAL**: already fully registered (PREFERRED_BIDDER, panel scores 92.83%, standstill ends 18/09). No action needed.
- **P78-BEATLES card corrected**: 2016 Beatles Legacy report authorship verified from PDF — IPM/EIUA/ICC for LCC, NOT a Fifth Sector deliverable. "Repeat-measurement" framing → "baseline-update of third-party study". £81.9m is NET impact (after deadweight/leakage/displacement/multipliers), NOT turnover. Gross ~£210m / ~5,990 jobs added. Evidence Review gate verdicts recorded.
- **3 new sources registered**: SRC-R5-016 (2016 report), SRC-R5-017 (Evidence Review, extracted), SRC-R5-018 (WB6 v2.1, not yet extracted). Sources now 129.
- **C-G2-280 linked** to SRC-R5-016 + SRC-R5-017 via E-R5-016/017. Evidence links now 589.
- **Evidence Review key findings**: PARTIALLY PROVEN (SHELDON); BLOCK: PROOF FAILURE if published with point estimate (THAD); FRICTION (SKiN). Beatles-attributable spend is assumption not measurement. 2028 demand shock (Mendes films, ~£250m marketing) unmodelled. Apple posture inversion (CONFIDENTIAL, Robin Kemp interview).


## Session 26/09/16 (2): Beatles sources batch-registered

- **142 Beatles sources registered** (SRC-R5-019 .. SRC-R5-160) — full folder inventory: 25 interview transcripts, 11 summaries, 11 guides, 22 Summit transcripts, 39 data files, 6 working papers, 6 method notes, 4 research docs, 2 report drafts, 2 contract docs, plus admin/images/emails/context.
- **Sources now 271 total** (was 129). All new sources NOT_REVIEWED — extraction and review needed before claim use.
- **Key items**: 2015 Reconstructed docx (25MB digitised 2016 report), V3 2026 draft update, Apple Experience economic case for/against, THAD review, AMION Eurovision report (structural precedent).
- **Classification**: by document type (INTERVIEW_TRANSCRIPT, DATA_FILE, WORKING_PAPER, etc.) and independence (FIRST_PARTY, CLIENT_SUPPLIED, INDEPENDENT_COMMERCIAL, INDEPENDENT_RESEARCH).


## Session 26/09/23: Sweep — P87 AHRC assessment, 5 lost tenders, Liverpool Digital, sources registered

- **Sweep run** (first since 26/09/16): 25,029 files tracked; 7 unregistered project folders; 7 unregistered sources; 6 possible tenders; 5 lost proposals registered.
- **P87-TRUENORTH**: AHRC CICP2 full application (APP114872) submitted; panel assessment week of 14/09; outcome expected week of 28/09; interviews 21-22 Oct at Steamhouse Birmingham (Year 1 Business Plan + video elevator pitch). Folder moved from Archive to Active. 4 sources, 2 claims, 2 evidence links added. Card updated.
- **P80 Southampton**: folder reorganized from "2026 South West Hampshire" to "2026 Southampton Strategic Review"; drive_folder_path updated.
- **T15-LIVDIGITAL**: new tender registered — Liverpool Digital Economy Cluster Mapping (~£20k Stage A, ~£45k+ full study); working brief extracted.
- **5 lost tenders registered**: T16-CSCC (Creative Scotland Culture Collective), T17-ESRC (Research sandpit), T18-GLAS (Glasgow Life), T19-LIVPHIL (Liverpool Philharmonic), T20-CESA (Plymouth CESA). All NOT_AWARDED.
- **6 new sources registered**: P78 Beatles (MRIO wk37, evaluation discussion note, Victoria McDermott interview, N Wyatt LCRDP), P01-NES (Foresight Places options response), Liverpool Digital brief. Sources now 281.
- **Wakefield Our Year 24 archive**: 231 files noted; final report already registered (SRC-G2-067); supporting material not batch-registered.
- **Register state**: 68 projects, 281 sources, 591 evidence links, 20 tenders.


## Session 26/10/07: Sweep infrastructure repair + catch-up sweep

- **Diagnosis**: scheduled sweep had not run since 26/09/23. The launchd plist pointed at `spillover-toolkit/tools/drive_sweep.py`, removed when the toolkit consolidated into `ProjectClassifier/`. Job fired each weekday and failed silently — errors only visible in `spillover-toolkit/sweep_reports/sweep.log`; notification step never reached. Job was also not loaded on this Mac.
- **Paths fixed**: `sweep_config.json` DRIFT watch root `Website 2026/spillover-toolkit` → `Website 2026/ProjectClassifier`; `drive_sweep.py` DRIFT classifier now derives roots from config severity instead of a hardcoded literal. Ignore patterns added for `sweep_reports/` and `sweep_state.json` (self-noise).
- **Loud failures**: new `tools/run_sweep.sh` wrapper — on failure writes `sweep_reports/SWEEP_FAILED.md`, prepends a failure banner to `SWEEP_LATEST.md`, pops a macOS notification. On success writes `sweep_reports/LAST_RUN_OK` heartbeat and clears the failure marker. Can't-launch failures are caught by heartbeat staleness (session-start rule updated to check it).
- **Remote trigger**: `Website 2026/sweep_requests/` Drive folder + `check_sweep_trigger.sh` poller (`com.thefifthsector.toolkit-sweep-trigger`, 300s StartInterval). Dropping a file in that folder from any signed-in device fires a sweep within ~5 min of sync. QueueDirectories kept on the main plist as a bonus; polling is the reliable mechanism (QueueDirectories doesn't fire dependably on Drive File Provider mounts).
- **TCC blocker found**: launchd children get EPERM even listing `~/Library/CloudStorage` — the scheduled job could never have worked; all real sweeps were manual. Fix: compiled `~/bin/toolkit-sweep-launcher` (source `tools/sweep_launcher.c`, lives outside CloudStorage); plists call it instead of /bin/bash. **Requires one-time grant**: Full Disk Access for `toolkit-sweep-launcher` in System Settings → Privacy & Security. Until granted, runs still fail (errors land in `sweep_reports/launchd.log`/`trigger.log`; heartbeat staleness detects).
- **Installed**: both plists copied to `~/Library/LaunchAgents/` and bootstrapped into `gui/501`.
- **Catch-up sweep run** (SWEEP-261007-2036): 25,304 files; 19 unregistered project folders; 54 possible tenders; 296 unregistered sources; 115 updated sources; 32 tender files; large DRIFT count (382) is baseline noise from the stale Sep-12 state and the drift-root switch — expected to quieten from the next run.
- **Headline findings**: new live proposal folders (DCMS AI Adoption, Futurecity, Oxford Economics, V&A, WY TRADS, Creative Scotland Frameworks of Impact); Liverpool Digital has formal ITT + drafted response (T15 needs updating); Beatles Report Pack delivered 26/10/07 (~350 new files, P78); P87 True North, WB6, BCWB, Kirklees folders moved to Archive (outcome/status check needed); Queen's Hall and LCR Film Impact in "2026 Proposals lost" (T02 outcome needs recording).
- **Docs updated**: README_sweep.md (paths, remote trigger, loud failures, heartbeat), JON_SWEEP_GUIDE.md (toolkit path + remote trigger), AGENTS.md session-start rule (SWEEP_FAILED + LAST_RUN_OK checks).

### Addendum: T21-CSFI registered + brief analysed (26/10/07)

- **T21-CSFI registered**: Creative Scotland "Research Examining Frameworks of Impact in the Creative Economy" — deadline noon 26/10/28, Q&A closes 26/10/16, £35-45k ex VAT, PQR 80:20 (understanding 30 / method 25 / PM 10 / team 15), 4x900-word submissions, sole supplier, contract to 30/04/27.
- **SRC-R5-171**: ITT brief registered (tender-only source, empty project_id per rule); extracted to `extracted_text/SRC-R5-171_v1_full.txt` (textutil, full read).
- **Intel registered (Iain 26/10/07)**: The Audience Agency in liquidation — institutional memory with Patrick Towell; TFCC published National Cultural Framework for LGA/CLOA 26/09/17 (governance/system model, not measurement) — likely bidder.
- **Positioning analysis delivered**: measurement-architecture framing (baseline vs contribution vs option) as differentiator; partner route recommended — Scottish wellbeing-policy specialist + Patrick Towell (audience data); Fleming framework to be cited and differentiated in review strand.
- **Towell profile updated (26/10/07)**: Patrick Towell is CEO of Creative Innovation 4 Good (founded 2023, Rio+UK); at TAA he was Director of Creative Economy & Policy and co-directed the UKRI "Towards a Blueprint for the National Cultural Data Observatory" — near-exact precedent for this commission. T21 row updated.
- **NCDO live + collaborator candidates (26/10/07)**: ncdo.org.uk confirmed operating (not just blueprint): ESRC-funded, 470+ partners, 70+ observatories mapped, 200+ datasets reviewed, Data Model/Translational Layer/Exchange Hub, Bradford 2025 demonstrator — and explicitly aligns to Fleming's LGA/CLOA framework. Sector stack = governance layer (NCF) + data layer (NCDO) + missing measurement layer (this commission). Collaborator candidates added to T21: Etic Lab (data science/ML, qual aggregation), MyCake (financial benchmarking). TAA IP access assumed via Towell (per Iain).
- **CAN questions + Towell approach drafted (26/10/07)**: 8 CAN questions filed to tender folder (scope, strategy/NPF, TAA data access, CS data route, qual strand, PMF link, format/users, post-Apr-27 phase) for PCS submission before 16/10; approach note to Patrick Towell drafted (named associate, data audit strand, NCDO docking, TAA asset disposition).
- **NCDO consortium intel (26/10/07)**: Iain spoke with Towell ~26/09 — Towell close to a deal with MyCake + Etic Lab for continuing NCDO operation. The three are a forming consortium, to be treated as a unit rather than separate candidates. Bid shape updated: TFS prime + NCDO trio named associates + Scotland wellbeing-policy specialist. Towell note rewritten as follow-up offering early joint work under TFS lead.
- **Towell note v2 (26/10/07)**: Schedule 4 check — probity form requires named roles + percentage shares for every member whether consortium or subcontractor; soft ask added. QS2 "usefulness to wider sector" criterion makes NCDO-docking a scored methodology point, added to pitch. Clause 1.17 bars public announcement of CS discussions (mention on call).
- **CAN revised for consortium intel (26/10/07)**: Q3 (TAA data access) now held pending Towell call — drop entirely if consortium holds the assets (information asymmetry worth more than CS's public answer); stealth fallback without liquidation clause if no call by 16/10. Q9 added: whether insurance applies per consortium member or to lead. Rule logged: CAN is public, no NCDO/consortium/architecture questions in it.
- **T22-VAIMP registered (26/10/07)**: V&A Impact Study ITT — study of V&A's impact on UK creative industries, fixed fee cap £60k, deadline 10:00 26/10/19, sequential kill-gate scoring (case studies first). Pack extracted as SRC-R5-172. TRIAGE: BID recommended pending Iain decision — brief cites IIPP ecosystem framing and spillovers, TFS signature territory; P78-BEATLES delivered today as fresh flagship case study. Key risks: 12-day turnaround, referee permissions, concurrency with T21.
- **T22 solo-vs-collab review (26/10/07)**: blindspot/deepthink/wishful applied. Verdict: hybrid — TFS prime + named associates via PQQ 1.14a lead+sub-consultant model. Solo passes the case-study gate but leaves Team + method-blend marks; full consortium is the highest ceiling but chains 3 unverified assumptions (deal status, availability, shares) inside 7 days. Decision point ~14/10.
- **P78-BEATLES delivered (26/10/07)**: lifecycle IN_PROGRESS → COMPLETED, end 26/10/07; citation_status → DELIVERED_WORK (unpublished — cite as delivered work, not public report); index card updated, project_index regenerated. Evidence Review caveats stand: scenario range not point estimate, Beatles-attributable spend share is an assumption. reference_permission still NOT_ESTABLISHED — referee needed for T22-VAIMP by 26/10/19.
- **Skills source synced + tender protocol mandated (26/10/07)**: foresight-agent-files skill set found in Drive (Active projects/Skills prompts/); installed grey, shaz, sark, load-the-team, fok into .devin/skills/ alongside existing blindspot/deepthink/sheldon/skin/thad/wishful. AGENTS.md gained mandatory "Tender review protocol" — full review-team pass required as initial phase of any tender review.
- **Case-study ontology team review (26/10/07)**: sheldon/grey/thad/wishful on the proposed selection scheme. Register debt exposed: contracting_role empty on 26/68 projects, citation_status missing on 10/68 cards, no SUPERSEDED method_status, sector_activity + method_family need domain rollup. Scheme amended: demand-led open domains, criterion as fifth entity, composition (telling + score-received) split from selection — case study becomes a first-class object. Encoding option still undecided.
- **CICP2 outcomes logged (26/10/07)**: P87-TRUENORTH (Lancaster) not shortlisted → NOT_AWARDED; P85-AMGEN (USW) shortlisted for next CICP2 round — positive market signal for Places evidence method. P75-LANC clarified as the earlier paid Nature-Culture Tech evidence commission feeding P87, not the bid itself; its BID_SUBMITTED lifecycle flagged as likely mislabelled.
- **P75-LANC reclassified (26/10/07)**: BID_SUBMITTED → COMPLETED — delivered paid evidence commission (Nature-Culture Tech cluster summary report), fee confirmed <£5k. Card rewritten; distinct from P87-TRUENORTH bid (not shortlisted). Now usable as a delivered current-method case study at small scale.
- **AMGEN framing + scheme amendment (26/10/07)**: P85 card updated — precedent weight is client adoption + external validation, not fee scale. Case-study ontology gains an intrinsic signal: method transfer (output portable enough for client self-application, outcome validates the method). Same-scale sibling P87 shows adoption without validation.
- **Standing rule change (26/10/07)**: AGENTS.md repo-sync rule updated — push to origin/main (github.com/iainbe/ProjectClassifier) is now required at the end of every register-changing session; replaces push-only-when-asked. Remote had drifted 15 commits behind.
- **Case-study decision document (26/10/07)**: `case_study_selection_decision.md` created — standalone capture of ontology, scheme, option parameters and open decision state. No schema or register changes made on this basis; decision remains open pending Iain.
- **T23-TVBTV registered (26/10/07)**: TVCA PROC-0881 Business Tees Valley Support Spine Framework — 7 single-supplier lots, £10m max, deadline 26/10/30, clarifications 26/10/23. Written tender (Q60/P20/SV20, min score 3 per question) only shortlists top-3 per lot; presentation stage alone decides award. Primary fit Lot 4 Creative and Cultural Industries. Source SRC-R5-173; xlsx annexes unread. Status TRIAGE — this is a delivery contract, not a research commission.
- **T23-TVBTV full team review (26/10/07)**: routes ranked — evidence-partner inside delivery consortium (strongest, via P46/P68 credibility, Teesside Uni mandated in spec); Lot 7 prime second (orchestration fits); Lot 4 prime weakest (4yr sole-supplier delivery). New facts: 2yr+2yr contract, unit rate card (workshops/coaching/cohorts), FVRA pass/fail gate. Register updated; decision pending Iain.
- **Company accounts added (26/10/07)**: `company_accounts/` — three filed years (FY23/24, FY24/25, FY25/26) copied from OneDrive + `accounts_summary.md` with key figures and FVRA-style ratios. Reading: operating margin 20-36%, acid ratio 1.22-1.44, net cash throughout — all three TVCA focus metrics green. Watch item: turnover ratio — annual contract values >~£100k will flag proportionality at ~£200k turnover, reinforcing partner/Lot-7 positioning on T23.
- **Credit signals checked (26/10/07)**: external aggregators read The Fifth Sector Ltd (07539809) as low risk — CompanyRank 80/100 (75th pct SIC peers), DataGardener "low risk", filings current, no CCJs. Creditsafe's own score still needs the manual free lookup; logged to accounts_summary.md.

## Session 26/10/07 (2): Liverpool Production Fund split into 2021 and 2024 projects

**Trigger:** Iain: "there should be two project folders, one for 2021 and one for 2024 - reallocate files and folders and update registry"

- **P22-LCRFILM** is now the 2021 interim evaluation only; **P88-LCRPF24** (new, PROVISIONAL) is the 2024-25 final evaluation. They differ in year, deliverable and evidence base (project-differentiation rule). `SRC-G2-030` (250609 final report) moved from P22 to P88 and its path updated; claims C-G2-037..041 stay on P22 and keep their evidence links to SRC-G2-030 as the interim-vs-final comparison
- **G Drive:** "2020 Liverpool Film Fund evaluation" renamed "2021 Liverpool Production Fund interim evaluation" and moved to 2021 Projects; the fuller "2024 Liverpool Production Fund" moved from 2025 Projects to 2024 Projects; the subset duplicate in 2024 Projects (verified: every file also in the fuller folder, matching names and sizes) renamed "ZZ superseded duplicate ... safe to delete". Nothing deleted. Also moved "2025 Liverpool Musiclab" into 2025 Projects (project not yet registered)
- P88 fields not evidenced (contracting_role, contract value, client acceptance, exact dates) left blank, not inferred; VAL-S261007-01..04 added. `project_index.csv` regenerated
- Residual: P22 card still mixes interim and final figures and P88 has no card or claims; per-project changelogs not yet written; Music Lab project (LCC, prime, 25/10-26/02, POs 3500530818 + 3500530819 = GBP 9,999 plus 3500535803 GBP 1,500 + VAT) not yet registered; AGENTS.md Liverpool list not yet updated

## Session 26/10/07 (3): Production Fund split completed; Music Lab registered

**Trigger:** Iain: P22 was a competed contract in its own right, P88 separately contracted in 2024; Music Lab details supplied; "proceed"

- Contracting facts recorded on P22 and P88. P22 card rewritten interim-only; P88 and P89 cards created (PROVISIONAL, no claims). Per-project changelogs written for P22, P88, P89
- **P89-LIVMUSLAB** registered: Liverpool City Council, PRIME, 25/10-26/02, original GBP 9,999 (POs 3500530818 + 3500530819) extended with GBP 1,500 + VAT (PO 3500535803). C-G2-271 moved from P75-LANC. VAL-S261007-05..07 added
- AGENTS.md Liverpool multi-project list extended with P22 (2021), P88, P89. `project_index.csv` regenerated
- Observed, not fixed: `client_type` mixes upper and lower case values (e.g. LOCAL_AUTHORITY / local_authority); `10_review_history.csv` has ragged rows

## Session 26/10/07 (4): Ontology v2 review, decisions 1-8, AGENTS.md rules, Drive undo table

**Trigger:** Iain: "use the Agents to determine options for best approach to ... ontology and weighting for selection of case studies and method statements"; later "walk me through the outstanding decisions one by one"

- **Review:** option analysis from `case_study_selection_decision.md` (A-D), then a draft `ontology_v2_DRAFT.md` (not adopted). Lanes run: THAD (advisory), generalisation dry-run across tenders, consistency audit, blindspot, deepthink, sheldon, wishful, shaz, skin, fok. Not run as agents: sark/load-the-team (lane selection done by the session) and grey (no buyer intelligence). THAD, generalisation and consistency ran on revision 1; the rest on revision 2. All advisory. Counts corrected after review: 70 projects, 27 empty `contracting_role`, 60 `sector_activity` values, 41 `method_family` values
- **Decisions taken (Iain):** (1) direction approved: register is truth, existing codebook claim axes, a case study is a use of a project against a tender requirement; (2) staged build plus a minimal use log, new register columns `citation_status` and `client_accepted`, requirements stay free text until the structure has been retyped three times; (3) lifecycle aligned to codebook v1.3 plus BID_PENDING, one name per stage, unclosed work held at IN_PROGRESS until client acceptance; (4) existing rule applied to bids held as projects; (5) evaluator-reported effects a separate sub-class, not ranked below delivered outputs; (6) evidence kinds are parallel, not a ladder; (7) client reuse coded DECISION_USE, asserted until sourced; (8) AGENTS.md review-team rule and standing test-strength rule adopted
- **AGENTS.md:** new section "Review-team protocol for method, schema and taxonomy changes": full lane set, advisory only, generality test, analysis before commit, separate revertible commits, and the standing rule that no test, gate or QA check is weakened without explicit permission
- **Facts established, not yet written to the register:** Lancashire Create Growth Programme bid: paid, direct with Lancashire County Council, GBP 10,000 ex VAT (PO 321786253/0, invoice 1221); Lancaster University Horizon bid (Virtual Agora): paid, direct, GBP 4,158.33 ex VAT (PO 500215141; invoice INV-1339 GBP 4,990.00 paid 23/10/25), not awarded; Creative Scotland salary benchmarking framework: awarded, GBP 11,750 ex VAT (agreement CS/CA1019, 30/09/26 to 30/10/26), live. No register row was changed this session step
- **Drive undo table** (changes made this day; to reverse, set the parent and title back):

| Folder (current name) | Drive folder ID | Previous name | Previous parent (name, ID) |
|---|---|---|---|
| 2025 Liverpool Musiclab | 1mbVTIDhP6RHTdddJxPYSqONW4CCnrfXd | unchanged | "2025 Projects" in the Google project folders tree, 1_6HJHqZ0ni3K07nmd3VlWJKiyEy7Qrf0 (now in Archive 2025 Projects, 1xTDlk_UIuY3FNNOzU9vwkuqVDaekxWij) |
| 2021 Liverpool Production Fund interim evaluation | 1RQzYlGCNN3R-QTJWsUkSHniajkY_vxjP | 2020 Liverpool Film Fund evaluation | "2020 Projects", 1DUlfL68Ue2sgFrcOYqSEQ0Ht5XyTGmth (now in "2021 Projects", 1roMvXyu1M5gZVFBcoE71ktfjUuAJCaZp) |
| 2024 Liverpool Production Fund (the fuller working folder) | 1pT0A8-ZJL11wd_kEId1o43_KLUDcjMcM | unchanged | "2025 Projects", 1xTDlk_UIuY3FNNOzU9vwkuqVDaekxWij (now in "2024 Projects", 1_U1XT3RGifBW_CPDzdPkn26zDPWSIZaO) |
| ZZ superseded duplicate - 2024 Liverpool Production Fund (subset, safe to delete) | 1wGKdcSQ02_pA3dO16fvKqR7fqAgJdVrF | 2024 Liverpool Production Fund | unchanged ("2024 Projects", 1_U1XT3RGifBW_CPDzdPkn26zDPWSIZaO) |

  The first three moves and the rename are described in the 26/10/07 (2) and (3) entries above. Nothing was deleted from Drive.
- **Residual:** register edits from decisions 3 and 4 (lifecycle mapping, the Derby bid to tender-only, the new columns) and the three project fact updates are not yet made; decision 9 (permission requests) is open and paused at Iain's request; the earlier Lancaster fee mix-up question stays open

## Session 26/10/07 (5): Register edits for decisions 2, 3 and 4

**Trigger:** Iain: "Make the register edits for decisions already taken"

- **New register columns** (appended at the end after a header check; register now 31 fields): `citation_status` (from the project cards, keyword only; UNKNOWN where the card lacks it: the ten earliest projects, whose cards in this repo mirror have no field although CHANGELOG 26/09/16 says it was added, so possible Drive/repo drift, VAL-S261007-09) and `client_accepted` (UNKNOWN for all projects, not inferred, VAL-S261007-08)
- **Lifecycle (decision 3):** ACTIVE/ONGOING/IN_PROGRESS and the unclosed states (COMPLETE_NOT_CLOSED, REPORTING_COMPLETE, PHASE_COMPLETE_AWAITING_INSTRUCTION) mapped to IN_PROGRESS for WYCA WY Create, Southampton Forward Strategic Review, Kirklees Creative Industries Mapping, City St George's SCCI, CELL, British Council Kotor Exchange Pilot, British Council Creative Economy Council Development. Result: COMPLETED 59, IN_PROGRESS 9, NOT_AWARDED 1 (the Lancaster True North bid support row, awaiting the Lancaster re-key). Kirklees phase rows not created (VAL-S261007-11)
- **Bids as projects (decision 4):** Derby Culture Strategic Review bid removed from the project register (own bid, tender-only; tender T05-DERBY); its 4 sources and 2 claims kept with project_id cleared; card and changelog moved to `retired/`. Creative Scotland salary benchmarking framework: IN_PROGRESS, 26/09/30 to 26/10/30, GBP 11,750 ex VAT. Lancashire Create Growth Programme bid: role DIRECT, GBP 10,000 ex VAT. Lancaster University Horizon bid: COMPLETED with programme outcome NOT_AWARDED, DIRECT, GBP 4,158.33 ex VAT. CoSTAR bid support and Creative City SIPF application follow the same model (Creative City lifecycle NOT_AWARDED -> COMPLETED with programme NOT_AWARDED)
- **AGENTS.md (strengthening only):** QA check 7 and the Unsuccessful bids rule extended to `programme_status=NOT_AWARDED`, so moving bid-support rows to COMPLETED does not drop them out of the check; Derby list now points to T05-DERBY. Applying the extended check set one CoSTAR design claim (C-R3-021) to EXPIRED
- **Tooling:** `tools/regenerate_index.py` now takes lifecycle from the register (register is authoritative) and emits `citation_status` and `client_accepted`; `project_index.csv` regenerated (69 rows)
- **QA run:** unique IDs, foreign keys, empty effect_family/role, EFFECT attribution, GBP value_basis: pass except pre-existing items on the Lancaster True North bid support row (C-R4-001 empty effect_family; C-R4-002 option without state), left for the Lancaster re-key
- **Validation actions added:** VAL-S261007-08 to -15. No test, gate or check was weakened
- **Residual:** Lancaster re-key (True North / workshop / fee mix-up); Kirklees phase rows; backfill of client_accepted and the ten earliest citation_status values; decision 9 (permission requests) paused at Iain's request

## Session 26/10/07 (6): Lancaster re-key

**Trigger:** Iain: "Go ahead with the Lancaster re-key" (after settling that the December 2025 summary report belongs to the workshop work)

- **Outcome:** IDs now follow names. **P75-LANC** = Lancaster AHRC CIC workshop and Nature-Culture Tech Creative Cluster summary report (v2), December 2025 (25/12), GBP 1,499.70 (INV-1357 dated 09/02/26, paid late by BACS 08/05/26), DIRECT, DELIVERED_WORK, folder `Archive projects/2025 Projects/2025 Lancaster AHRC CIC`. **P87-TRUENORTH** = True North CICP2 bid support, 26/06 to 26/08/20, GBP 8,333 + VAT per Iain (PO 500222361 dated 25/06/26, order total GBP 9,999.00), DIRECT, COMPLETED with programme_status NOT_AWARDED (client application not shortlisted), DELIVERED_WORK
- **Moved:** source SRC-G2-074 (True North application) P75 -> P87; source SRC-R5-001 (workshop remittance) P87 -> P75. Claim C-G2-270 stays with the workshop (its only evidence link is the True North application, now on P87)
- **QA fixes inside the re-key:** C-R4-002 (interview option) set EXPIRED; C-R4-001 empty effect_family set NOT_APPLICABLE. After this the register has no OPTION-without-state and no empty effect_family
- **Text corrected:** permission row PR-06 wording and notes (accuracy only; redesign still paused); bid record T01 (True North now P87); cards for P16, P64, P81, P85; case-study decision doc correction note; both Lancaster cards rewritten; both changelogs
- **Register effect:** lifecycle now COMPLETED 60, IN_PROGRESS 9; no lifecycle NOT_AWARDED rows remain
- **Retracted:** the VAL-S261007-10 suspicion that the "<GBP 5k" fee was the Horizon invoice; it is the workshop fee. Marked RESOLVED
- **Added:** VAL-S261007-16 (PO total GBP 9,999.00 vs GBP 8,333 + VAT), -17 (changelog cites claims C-R4-003/004 and evidence E-R5-018/019 that do not exist), -18 (workshop date and VAT of INV-1357), -19 (summary report not registered as a canonical source)
- **Residual:** items above; Kirklees phase rows; client_accepted and early citation_status backfill; decision 9 (permission requests) paused; the 254 evidence rows pointing at absent claims (pre-existing)

## Session 26/10/07 (7): True North value confirmed; changelog references corrected

**Trigger:** Iain: "The PO total is VAT-inclusive, £9,999" and "record the VAT-inclusive PO total and fix the changelog references"

- **True North bid support** (P87-TRUENORTH): value recorded as GBP 9,999 including VAT (PO 500222361), about GBP 8,333 ex VAT (exactly 8,332.50 at 20%; GBP 8,333 + VAT is the same fee rounded). Register notes, relationship evidence and card updated. VAL-S261007-16 resolved
- **Changelog references fixed:** the True North changelog cited claims C-R4-003 and C-R4-004 and evidence E-R5-018 and E-R5-019, which are not in the registers. Corrected to C-R4-001 and C-R4-002 and E-R5-602 and E-R5-603, matched by content (assessment timeline; interview claim; links from SRC-R5-161); original wording kept in brackets. The match is by content, not proven. VAL-S261007-17 resolved

## Session 26/10/07 (8): Permission requests decision (decision 9)

**Trigger:** Iain: "Continue with the permission requests decision", answered question by question

- **Rule (Iain):** citing delivered work in a tender needs no client permission unless a contract clause, NDA or client instruction restricts citation. Written into AGENTS.md citation rules, with the three things that still need permission: naming a client as a referee, reproducing client-identifying content on the website, and reusing client data
- **One place (decision 9a):** `reference_permission` is recorded only in `11_permission_requests.csv` (ESTABLISHED on a NAMED_REFEREE request). `tools/regenerate_index.py` now derives it and `project_index.csv` has a `reference_permission` column. Cards still carry a legacy line (all NOT_ESTABLISHED except one non-canonical value); the index is authoritative
- **The 35 requests (decision 9b):** 27 closed as NOT_REQUIRED (no restriction marker recorded; rows and reasons kept; reopen if one is found); 3 turned into INTERNAL_CHECK notes (University of Plymouth subcontractor wording; BOP Consulting / Frontier Economics contribution cap; Beatles Visitor Impact Study client identity); 5 client asks kept and rewritten in plain language with one question each (Wakefield Council, Liverpool City Council for the LCR music economy mapping, LCR Combined Authority, British Council contract clause, CELL client data reuse). Project IDs in the file normalised to register IDs; original text kept in notes where it carried extra detail
- **Owner and reminder (decision 9c):** the 5 live asks carry owner Iain and a reminder after five working days. Nothing has been sent; each message needs Iain's approval
- **Columns added to the permission file:** `owner`, `reminder_after_working_days` (appended at the end; 13 fields). New statuses: NOT_REQUIRED, INTERNAL_CHECK
- **Validation actions added:** VAL-S261007-20 (CELL data reuse, hard stop 29 Oct 2026), -21 (confirm the LCR music mapping commissioner), -22 (spot-check closed requests for restriction markers)
- **No test weakened:** the referee gate is unchanged (default NOT_ESTABLISHED); only requests that were never needed under the stated rule were closed, with the reason recorded

## Session 26/10/07 (9): Merged main into the branch (PR conflict)

**Trigger:** the pull request for this branch ([iainbe/ProjectClassifier#2](https://github.com/iainbe/ProjectClassifier/pull/2)) reported a merge conflict with `main`

- `main` had four commits not on the branch: tender T23-TVBTV registered (TVCA Business Tees Valley Support Spine Framework), its full-team go/no-go review, company accounts archived with ratios computed, and credit signals checked. They touched `02_sources.csv`, `08_tenders.csv`, `10_review_history.csv`, `CHANGELOG.md`, `tier2_qa_review.md` and added `company_accounts/`
- Four conflicts, resolved without rewriting history (a merge commit): `02_sources.csv` took `main`'s file (which only converted CRLF to LF and added source SRC-R5-173) and re-applied this branch's seven row changes (SRC-R3-04 to -07, SRC-G2-030, SRC-G2-074, SRC-R5-001); `10_review_history.csv`, `CHANGELOG.md` and `tier2_qa_review.md` are append-only logs, so both sides' entries are kept (main's first, then this branch's)
- Checks after the merge: no conflict markers, unique source and review IDs, source and claim project links valid, tender T23 present, review history 356 rows, `project_index.csv` regenerated. `02_sources.csv` is now LF-ended like `main`

## Session 26/10/07 (10): Eligibility report (first build step of the staged plan)

**Trigger:** Iain: "whichever makes most sense - you have a plan, right?"

- **New tool:** `tools/eligibility_report.py` (read-only) writes `eligibility_report.csv` and `eligibility_report.md`: five checks per project (delivered and accepted; citable; lapsed option; method current; role wording) as PASS / FAIL / UNKNOWN, evidence kinds shown side by side and never ranked, referee permission shown but not a check, and a ranked list of the missing facts that block the most completed projects. Unrecorded facts are UNKNOWN, never PASS; no test weakened
- **First run (69 projects, 60 completed):** delivered/accepted PASS 0, FAIL 9, UNKNOWN 60 (client acceptance not recorded); citable PASS 55, FAIL 4, UNKNOWN 10; lapsed option PASS 69; method current PASS 34, UNKNOWN 35 (no method rows registered); role wording PASS 44, UNKNOWN 25. No project is fully determinable yet
- **AGENTS.md:** stale-artefact rule now also requires running the eligibility report after register, claim, method or permission changes
- **Open question for Iain:** a project with no method rows is UNKNOWN on "method current" (27 completed projects). Either method rows are expected for every project, or "no method used" may count as not applicable; left UNKNOWN until Iain decides

## Session 26/10/07 (11): Candidate view for the V&A tender (T22-VAIMP)

**Trigger:** Iain: "Yes, run it for the V&A tender"

- **New tool:** `tools/selection_view.py` (read-only) builds a candidate list for one tender requirement from the eligibility report: subject keywords plus the evidence kinds the buyer wants; alphabetical, never ranked across kinds, UNKNOWN never a pass; also lists subject matches that hold none of the wanted kinds so nothing is silently dropped (first version omitted them; fixed in this session)
- **Output:** `selection_views/T22-VAIMP.md`. Reading of the buyer's ask (to be corrected by Iain): evaluation or impact of an institution or programme on creative industries; kinds wanted: delivered output, reported effect, effect as evaluator. Result: 9 candidates (BAC + LIVR Project Evaluation; CICP Impact and Delivery Evaluation; Creativeworks London KE Hub Evaluation; Kirklees Creative Industries Mapping (in progress); LCR Film and TV Production Fund Interim Evaluation; SYMCA ARG Evaluation; University of Liverpool Heritage CPD; Wakefield Cultural Development Fund Evaluation; Wakefield Our Year 24 Evaluation) and 3 subject matches with no coded claims (Beatles Visitor Impact Study; LCR Production Fund Final Evaluation 2024-25; SYMCA Create Growth Programme Final Report)
- **Not done:** no recommendation, shortlist or positioning conclusion was written. The tender review protocol (full advisory lane team) is still required before any positioning, case-study sheet or submission content for T22
- **Finding:** the view is limited by claim coding: the two projects the tender record calls its strongest precedents have no claims of the wanted kinds registered

## Session 12 (26/10/08): T22-VAIMP referee wording and review lanes

- **Changed:** `tools/selection_view.py`, `tools/eligibility_report.py` (docstring) and the regenerated `selection_views/T22-VAIMP.md` now say referees are cited by name in the tender and asked only once shortlisted (Iain, 26/10/08). No check was changed or weakened.
- **Review lanes run on T22-VAIMP** (blindspot, deepthink, sheldon, wishful, thad, grey, shaz, skin, fok; all advisory, none blocked). Convergent findings: no candidate is clearly an institution-impact study; Beatles Visitor Impact Study and LCR Production Fund Final Evaluation 2024-25 have no coded claims; client acceptance and several contracting roles unknown; CICP Impact and Delivery Evaluation is subcontractor work, not TFS-owned; the view's keyword filter searches names only and missed Theatre Royal Plymouth Engagement and Wakefield Our Year 2024 BCJ.
- **Not done:** no case-study sheet, shortlist or positioning written; T22 `notes` field and `ontology_v2_DRAFT.md` section 7 not yet updated; awaiting Iain's answers.

## Session 12b (26/10/08): University of Liverpool Heritage CPD final report

- **Finding:** the final report was already in the register as SRC-G2-062 but mislabelled as a research summary presentation, which led the Sheldon lane to report "proposal only". Corrected the row, re-extracted the full text from Drive (G Drive id 1ury6wz6PsYFxUNe6qYcSh-UScbEhHKR3), reworded C-G2-246 and E-G2-151, updated the P63 card.
- **Not changed:** `client_accepted` (UNKNOWN) and `citation_status`. Drafts, workshop deck and inception note remain unregistered. Added VAL-S261008-01 (acceptance and take-up) and -02 (OneDrive check).
- **Session 12b addition:** registered the P63 workshop deck as SRC-G2-089 and extracted it; no claims coded (no outcomes recorded in it). Drafts and inception note left unregistered.
- **Session 12b addition 2:** registered the P63 inception note as SRC-G2-090 and extracted it; the 22/09 and October draft reports are deliberately left unregistered (Iain instruction). No claims coded.

## Session 12c (26/10/08): Production Fund Final Evaluation claims (P88-LCRPF24)

- **Added:** 17 claims, 17 evidence links, 13 measurements from SRC-G2-030 (IDs C-S261008-001 to -017, E-S261008-, MEAS-S261008-; new prefix chosen because the P78 card cites C-G2-280 to 283, which are not in the register). Resolved VAL-S261007-03. Added VAL-S261008-03 to -05.
- **QA on the new rows:** field counts, unique IDs, foreign keys, £ claims have value_basis, EFFECT claims have attribution_strength, no empty role or effect_family. Self-review caught and fixed three errors before commit: a £ claim with no value_basis, context claims using undefined CONTEXTUAL (changed to NOT_APPLICABLE per codebook), and a causal verb in a CONTEXT proposition.
- **Not changed:** P22 claims C-G2-037/038 still quote final-period figures (VAL-S261008-05); client, contract and acceptance for P88 still provisional.

## Session 12d (26/10/08): P22 claims trimmed to interim figures

- C-G2-037 and C-G2-038 reworded to the 2021 interim position only (Iain instruction); final-period figures remain on P88 claims. E-G2-534/535 relinked as corroboration. VAL-S261008-05 resolved. No claim added or removed.

## Session 12e (26/10/08): referee timing propagated

- `ontology_v2_DRAFT.md` section 7 and decision ledger updated for the referee-timing correction; header and reversal text no longer say the draft is uncommitted. PR-03, PR-04 and PR-05 notes record that the asks are held until shortlist. Nothing sent to any client.

## Session 12f (26/10/08): ontology decision 10

- Iain: evidence kind is a filter, not a rank. `ontology_v2_DRAFT.md` section 5 rewritten and ledger item added. Ordering of survivors by role, recency and geography left open (10b). No register or tool change; the T22 view already behaves this way.

## Session 12g (26/10/08): ontology decision 10b (option C)

- `tools/selection_view.py` gained `--order proposed` (and optional `--geography`): writes `selection_views/<tender>_proposed_order.md` with kinds held, then contracting role, then most recent end date, then geography, and a plain-words 'Placed because' column. No score. Default view unchanged (alphabetical). Draft section 5 updated.
- T22 view regenerated: now 10 candidates because the LCR Production Fund Final Evaluation (P88) has coded claims.

## Session 12h (26/10/08): Beatles study registered and coded; ontology decision 11

- Registered SRC-G2-091/092, coded 10 claims, 10 evidence links, 9 measurements (C-S261008-018 to -027). Added PR-36 (INTERNAL_CHECK on publication clearance), VAL-S261008-06 and -07. P78 card updated. Ontology draft: decision 11, wording capped at the claim's own evidence class (Iain).
- Self-review: removed a stray sentence from a claim note; original-study originator corrected from the P78 card. Recalculated the headline (211.3 x 0.8 x 0.8 x 0.380 x 1.30 = 66.8, stated 66.9) and the operator percentages (match).
- **Session 12h addition:** Iain confirmed the 08 Oct study (SRC-G2-091) as the delivered version; SRC-G2-092 marked as the earlier edition; VAL-S261008-06 resolved. P78 delivery date (26/10/07 in the register) to re-check.

## Session 12i (26/10/08): P78 date, acceptance and citation

- P78 date_end corrected to 26/10/08; client_accepted set to Y (verbal, per Iain; no written record, recorded in notes); PR-36 closed; VAL-S261008-07 resolved. This clears E1 for the Beatles Visitor Impact Study. Verbal acceptance is a weaker record than written, so the basis is stated beside the value.

## Session 12j (26/10/08): provenance of backfilled facts (ontology decision 12, option B)

- New `14_fact_provenance.csv` (append-only; basis DOCUMENT / WRITTEN_CLIENT / VERBAL_CLIENT / IAIN_STATEMENT / INFERRED) seeded with 12 facts settled this week, each value checked against the register. `tools/eligibility_report.py` and `tools/selection_view.py` now show the basis beside E1, E2 and E5 PASS results and the report counts PASS results with no basis recorded (E1 0, E2 55, E5 39). Display only: no result or check changed. Ontology draft updated. AGENTS.md not changed (draft not adopted): the stale-artefact rule should list the new file on adoption.
- **Insurance registered (26/10/07)**: `company_insurance/` — Hiscox 2026 pack (PI £5m / PL £5m / EL £10m, period 06/04/26–05/04/27, £669.09/yr). Current-issue certificates kept (post-address-change versions); deduped OneDrive conflict copies. insurance_summary.md maps cover vs live tenders: **PL £5m vs CS requirement £10m is the only gap** (CAN Q9 covers whether lead cover suffices). Renewal due before 06/04/2027 — all three live contracts outlast the policy. Certificate address out of date — Iain writing to Hiscox for reissue.
- **CS insurance precedent logged (26/10/07)**: PL £10m requirement vs £5m held is not a blocker — CS previously accepted contract amendment to match existing cover. Action moves to submission-time: note current levels in the proposal so amendment can be requested at award. insurance_summary.md + T21 row updated.
- **T23 lot decision documented (26/10/08)**: `261008 T23 lot decision.md` in tender folder — seven-lot scan narrowed to Lot 4 (consortium route) + Lot 7 (prime route); actions and fallback recorded. Decision still open pending Iain.
- **T23 partner landscape assessed (26/10/08)**: Supplier Noticeboard located inside Delta workspace; Teesside contacts ordered (Charlotte Nicol first — existing LI connection; Ben Fisher second); regional incumbents mapped (Generator/Ross meeting 15/10, NE Screen/Gwynn via P46, RTC North). Curated Place assessment revised upward on CBDP evidence — live national cohort-based cultural business development for Creative Scotland; flagged as genuine Lot 4 partner + Lot 7 bench member, still needing Tees Valley anchor. Iain's subcontractor role on CS Creative Producer/CBDP work identified as uncaptured register evidence.
- **T23 noticeboard claim corrected (26/10/08)**: Supplier Noticeboard location in earlier register note overstated — press-only reference, not in ITT or visible on Delta. Note now records verification routes (Delta helpdesk / clarification Q) and marks it non-critical-path.
- **P88-CBDP registered (26/10/08)**: subcontracted delivery inside Curated Place's Creative Scotland Cultural Business Development Programme — MVP workshop + session materials for Nov 2025 cohort, archive folder verified in both Drive and OneDrive. SUBCONTRACTOR to Curated Place (CS-supported programme). Open: fee, edition coverage, Round 2 involvement, referee permission. Strategic relevance: T23 Lot 4 consortium + Lot 7 bench, T21 CS delivery familiarity.
- **P88-CBDP details confirmed (26/10/08)**: Iain — CBDP 2025 only; fee £500; 6 further sessions in 2026 so lifecycle IN_PROGRESS, citation LIVE_WORK; prior CP bid collaboration noted (CS Culture Collective, 26/08).

## Session 12k (26/10/08): merge of main into the PR branch

- Main gained P88-CBDP (Creative Scotland Cultural Business Development Programme, Curated Place subcontract), T23 notes and an insurance pack. Merged into the branch: `01_projects.csv` merged by project and field (no field-level conflicts; P88-CBDP added with the two new columns citation_status and client_accepted blank, so it reads UNKNOWN on E1 and E2), append-only logs unioned, derived files regenerated.
- **Number clash:** P88-CBDP and P88-LCRPF24 now share the number 88. Full IDs are distinct so no join breaks; the choice is left to Iain (VAL-S261008-08). Not renumbered.

## Session 12l (26/10/08): P88-CBDP renumbered to P90-CBDP

- Iain: P88-LCRPF24 keeps the number 88. The Creative Scotland Cultural Business Development Programme subcontract is now P90-CBDP: register row, card, per-project changelog and PM record renamed and edited; derived files regenerated. Earlier log entries (CHANGELOG, QA review, review history) that say P88-CBDP are left as written, because they are the audit trail. VAL-S261008-08 resolved. Any outside file, Drive folder name or sweep note that says P88-CBDP needs the same change.

## Session 12m (26/10/08): where requirements live (ontology decision 13, option B)

- New folder `tender_requirements/` with `T22-VAIMP.md` (frozen contract and the case-study item, operator reading, Iain to correct). `tools/selection_view.py --requirements T22-VAIMP` reads it; the regenerated T22 view lists the same 11 candidates as before, in both orders. T22 row of `08_tenders.csv`: `requirement_map_location` set and the review-lane findings added to `notes` (tender review protocol item 4). Ontology draft updated.

## Session 12n (26/10/08): people register (ontology decision 14, option B) and verbatim T22 wording

- New `15_people.csv` (4 people) and `16_involvement.csv` (5 rows, all from documents), plus read-only `tools/people_view.py`. No contact details or CVs held. `named_in_bids_ok` is UNKNOWN for everyone except Iain.
- `tender_requirements/T22-VAIMP.md` updated with verbatim ITT and Clarification wording (case-study item, new team item, formatting rule, scoring key, process dates). The brief (document 02) and PQQ not yet read.
- Wording note: Clarification Q12 says an anonymised case study is acceptable only if the organisation and referee can be disclosed on request; it does not say referee details may wait until shortlisting, while the ITT asks for a contact for each case study in the tender.

## Session 12o (26/10/08): V&A brief and PQQ read

- Read the brief and PQQ in full and added `brief` and `qualification` items to `tender_requirements/T22-VAIMP.md`. Findings: the PQQ reserves the right to take up references on submitted examples at any stage (risk to the referee-after-shortlist approach, advice only); our insurance meets the PQQ minimums but expires 05/04/27 before the May 2027 deliverables and certificates show an old address; the brief's case-study output asks for long-run effects on creative careers and the ecosystem, which most candidates do not evidence. Added to the T22 notes.

## Session 12p (26/10/08): current ratio for the V&A PQQ

- Current ratio computed and checked against the 2025/26 accounts PDF: 1.25 (FY25/26), 1.29, 1.44. Meets V&A PQQ 3.1.1 without a guarantor or statement. Added to `company_accounts/accounts_summary.md` and the T22 requirements file.
- **Cross-tender next-steps doc (26/10/08)**: `261008 Next steps - priority order.md` in Active proposals — ordered across T22 (referees critical path), Towell call, T21 CAN, T23 partner/bench/CAN, compliance items.
- **proposal_docs/ mirror created (26/10/08)**: all 23 .md working docs from Active proposals now versioned in the repo under the same folder structure. AGENTS.md updated — mirror is standing practice for new/changed proposal docs; ITT packs and binaries stay Drive-only.

## Session 12q (26/10/08): candidates-considered log (ontology decision 15, option B)

- New append-only `13_selections.csv` (header only: no selection has been made yet) and `tools/record_selection.py` (dry run unless `--write`; one row per candidate with default and proposed positions, chosen, reason code; OUTCOME rows for buyer scores). `tools/selection_view.py` candidate logic moved into a `build()` function so both tools share it; regenerated T22 views are byte-identical to before. Ontology draft section 9 rewritten (replaces the planned `13_uses.csv`). Branch restarted from the merged main as the previous pull request was merged.

## Session 12r (26/10/08): method selection, step 1 (draft only)

- Iain chose option B for method selection. Added `method_family_rollup_DRAFT.csv`: a proposed mapping of the 42 `method_family` labels to eight rolled-up families (all 52 method rows covered; six boundary labels flagged for Iain). Nothing in `03_methods.csv` or the codebook has changed. The full lane review of the package (rollup, SUPERSEDED status, method view) and Iain's approval come before any change is applied; each applied item will be its own commit.

## Session 12s (26/10/08): method rows repaired (method package item 1)

- Repaired the one-column shift on 19 rows of `03_methods.csv` (M-G2-010 to M-G2-028) by script: empty `outputs` inserted, remaining fields moved right. Before applying, each row was asserted to match the exact shifted pattern; after, every row passes a semantic check (source IDs, claim IDs, review status, date). Diff shows only those 19 rows. All method source IDs now resolve in `02_sources.csv`. The method package was lane-reviewed (eight lanes, none blocking); this is item 1 of the agreed order, its own commit.
- The foreign-key check found 20 claim IDs on method rows that do not exist in `04_claims.csv` (pre-existing; VAL-S261008-09).

## Session 12t (26/10/08): two method rows registered (method package item 2)

- Registered M-S261008-01 (Beatles attribution bridge, P78-BEATLES) and M-S261008-02 (Production Fund final evaluation, P88-LCRPF24) in `03_methods.csv`; their claim and source IDs were checked to exist. The draft file was removed. P88's contracting role is still not evidenced (VAL-S261007-01), noted on the row; the method view flags statements built on it.

## Session 12u (26/10/08): method statements revised after lane review (method package item 7a)

- Rewrote MS-01 to MS-03 with the lane fixes: approval card at the top, generic bid-ready paragraph, no figures, tender-specific "fit and gaps" removed, neutral wording, evidence class, disclosure status, next action. MS-02 now lists all nine claims, says the final evaluation's contracting arrangement is not evidenced, and step 5 reads "state where the bases differ". MS-03 is marked design-only and usable only as a design contribution.
- **Correction (Iain):** BOP Consulting is a competitor and is never asked for permission (PR-07 already said so). The lane suggestion to obtain BOP's written agreement is not adopted; MS-03 relies on accurate attribution capped at "contributed to" and an internal check of our own subcontract or NDA. All statements stay DRAFT; only Iain sets CURRENT.

## Session 12v (26/10/08): method view gate and plain-English flags (method package, lane fixes)

- `tools/method_view.py` rewritten: a disclosure gate (claim wording and figures withheld unless the statement's disclosure status is CLEARED), a lift badge, plain-English flags in three tiers with an owner, and new flags for malformed headers, missing required fields, CURRENT without a named reviewer, a statement with no application or an unregistered method row, and a design-only statement. Tested on a scratch copy: every new flag fires. The regenerated view contains no £ figures.
- Note: the earlier committed version of `method_views/statements.md` (commit 5c50c87, branch only, not yet on `main`) printed Beatles figures; the file is replaced. The figures remain in earlier git history of this branch.

## Session 12w (26/10/08): statement_id column and codebook v1.4 additions (method package item 5)

- Added `statement_id` as the last column of `03_methods.csv` (17 fields), filled for the six rows named by the three statements (MS-01: M-S261008-01; MS-02: M-G2-016, M-S261008-02, M-G2-021, M-G2-006; MS-03: M-G2-010); the rest are blank. Rows were checked for a single statement each. Added `codebook_v1.4_additions.md` (SUPERSEDED as a method_status value, the new field, statement status fields); v1.3 is untouched and register version labels stay 1.3-candidate.
- Checked the readers of the file: `eligibility_report.py` and `method_view.py` read columns by name (outputs byte-identical before and after); `register_g2_methods.py` takes its header from the file; `deepen_p01_nes.py` is a finished one-off script that appends 16-field rows and must not be re-run. `method_view.py` gained a link-mismatch flag. The T22 selection view was regenerated; it now shows method rows for the Beatles study and the final evaluation (that check reads PASS), a stale-artefact catch from the previous commit.

## Session 12x (26/10/08): check E4 extended additively (method package item 6)

- `tools/eligibility_report.py`: E4 (method current) now also returns FAIL when a method row links, through `statement_id`, to a method statement whose status is SUPERSEDED. Nothing else changed: no method rows is still UNKNOWN, applied rows still PASS, a SUPERSEDED method row still FAIL. A linked DRAFT or missing statement only adds an `E4_note`. Regenerating the real register left every earlier cell unchanged (70 projects, no changed cells); the six linked projects gain a note that their statement is DRAFT.
- New `tests/test_eligibility_e4.py` (six fixture cases, run with `python3 -I tests/test_eligibility_e4.py`); it passes on the new code and fails on the previous version at the new case, so it discriminates.

## Session 12y (26/10/08): claims drift repair (method package, data fix)

- 49 claims (all G2-BATCH-B) had text in `fifth_sector_role`: the role codes sat in `contrary_evidence` and the contribution text in `fifth_sector_role`. By script, with per-row assertions (role code present, contribution field empty, method and batch copies identical, review status valid): role codes moved to `fifth_sector_role`, text moved to `fifth_sector_contribution`, `contrary_evidence` cleared on those rows. Diff is 49 lines. Every claim now has a valid role code. Before-and-after values are kept in `claims_repair_RECORD.csv` (including the legacy claim type that differs from the current one in 22 rows). The eligibility report is unchanged cell for cell.
- Roles were moved as recorded, not re-judged. Seven P22 and P27 claims carry DELIVERER/DESIGNER where the evaluator rule may apply (VAL-S261008-10). Legacy copies in four other columns remain on many rows (VAL-S261008-11).

## Session 12z (26/10/08): dangling method reference M-G2-009 resolved (method package item 3)

- Claims C-G2-022 and C-G2-023 (Liverpool City of Music Strategy, P15-LIVMUS, DESIGN) named `M-G2-009`, a number missing from the method sequence. The project's only method row, M-G2-008 (music sector mapping with strategy, governance recommendations, capital projects and scenarios), already lists both claims in its own `claim_ids`; the claims were repointed to it rather than blanked, and the old value is written into each claim's notes.
- The new Beatles and Production Fund claims (seven) now carry their method IDs, closing the one-way links I left when coding them. A two-way check of method-to-claim links now finds no claim pointing at a missing method and no unmirrored method link; one reverse mismatch remains (C-R3-031, VAL-S261008-12), plus the 20 absent-claim links (VAL-S261008-09). The proposal's family count corrected to 41.

## Session 13a (26/10/08): 244 deleted claims restored

- **Found:** the sweep commit eb2674d (26/09/16) removed claims C-G2-280 to C-G2-523 (244 rows) from `04_claims.csv` without mentioning it, while keeping the 254 evidence rows that point at them; its own message and later notes still treated C-G2-280 as present, and 26/09/12 QA entries refer to claims C-G2-440 to 480 that only existed in the lost block. The same commit also made 61 legitimate edits (project IDs normalised, four inconsistency resolutions) that are kept.
- **Restored** from the last commit that held them (4a92a71, 26/09/12), inserted in ID order, with four short project IDs mapped to the current register (P78 to P78-BEATLES, P79 to P79-CELL, P81 to P81-WB6, P82 to P82-KOTOR). Record of every restored row: `claims_restore_RECORD.csv`. Claims register now 590 rows. The 244 rows are restored as they stood on 26/09/12; they are not re-reviewed.
- **Effect:** evidence rows pointing at absent claims fall from 254 to 7 (C-R5-524 to 528, separate), and method-to-claim links to absent claims from 20 to 0. Eligibility checks are unchanged except P06-COSTAR E3 (lapsed option) now reads FAIL, correctly, because its restored DESIGN claims are not yet EXPIRED (next commit). Evidence-kind counts rise for 18 projects (for example P01-NES: 14 delivered-output claims where the register showed none).

## Session 13b (26/10/08): COSTAR design claims expired

- C-G2-440, 443, 446 and 447 (CoSTAR bid, P06-COSTAR, recovered in the restoration) set to `option_state=EXPIRED`, as AGENTS.md requires for DESIGN and OPTION claims on a project whose bid was not awarded (`programme_status=NOT_AWARDED`). Check E3 for P06-COSTAR returns to PASS. Notes on each claim record the change.

## Session 13c (26/10/08): CONTEXTUAL effect family removed from pure context claims

- `CONTEXTUAL` is not a codebook value; the codebook says a pure CONTEXT claim takes `NOT_APPLICABLE` with the reason in notes. 200 claims with claim_type CONTEXT were changed by script (each note records the change; old values in `claims_contextual_RECORD.csv`). Five claims that are not pure context (one DESIGN, four METHOD_OUTPUT) keep CONTEXTUAL for Iain to decide (VAL-S261008-15). QA check 5 (empty effect_family) is unaffected; effect_family is now valid on 585 of 590 claims. No eligibility result changed.

## Session 13d (26/10/08): method family rollup applied

- Added `method_family_rollup` as the last column of `03_methods.csv` (18 fields) with ten families (the sector-baseline family split in three after the lane advice that no family should hold more than about a quarter of methods; largest is now 20%), mapped from all 41 existing labels via `method_family_map.csv`. Old labels unchanged. Codebook addendum updated. Draft rollup and repair-preview files removed (applied; history keeps them). Method view and eligibility outputs unchanged; the E4 test still passes.
- The proposal now records that only five of 23 tenders have usable requirement wording, so the requirement-type tabulation is limited and the selection effect remains.

## Session 13e (26/10/08): method view coverage table and staleness flags; SRC-G2-092 checked

- `tools/method_view.py` gained `--requirements <tender>` (a table of which statements cover which questions, from the new `coverage` item in `tender_requirements/T22-VAIMP.md`: 3 of 8 V&A questions have no statement, 5 partial) and flags for a statement older than a linked method row's review date, plus an optional `--stale-days N` (no default; Iain sets any threshold). Both fire in a scratch test.
- SRC-G2-092 (07 Oct Beatles report edition): the headline figures and sensitivity values were confirmed present in both editions; the rest was not compared, so it stays unreviewed and superseded by the delivered study.

## Session 13f (26/10/08): sources register drift repaired (46 + 4 rows)

- 46 rows of `02_sources.csv` had text in `derived_location` and every later field displaced: 27 rows by one column (a blank inserted before the original path) and 18 by two (two blanks missing before it), plus SRC-G2-022 (the second pattern with two stray duplicates, cleared) and the three sweep-written rows SRC-R5-016, -017 and -018 (notes and review fields re-aligned). By script, each row asserted against its exact pattern before editing; afterwards every `derived_location` is a path or empty, no `additional_project_ids` holds text, and all 28 fields line up with the header. Record of every row and its old value: `sources_repair_RECORD.csv`.
- SRC-R5-016's register row names an extract file that is not in the repo (VAL-S261008-16). The 46-row drift had hidden extracts from any tool that follows `derived_location`.

## Session 13g (26/10/08): figure screen

- New read-only `tools/figure_check.py` and its output `figure_check_report.md`: for every claim, each number in the proposition is looked for in the extracts of the sources its evidence links cite. After the sources repair, 284 of 312 claims with figures have every figure found in a cited extract, 26 have an unmatched figure and 2 cite a source without an extract. It ranks spot checks (AGENTS.md priority: high-risk numerical claims); it does not verify anything. The 17 claims worth checking first are VAL-S261008-17; several unmatched items are dates, unit conversions or derived ratios.

## Session 13h (26/10/08): drift repaired in evidence links, measurements, tenders and validation actions

- Format checks (dates, version labels) over every register found the same displaced-column pattern again: 54 evidence-link rows (reviewer and review date held text, the extract path sat in `notes`, family, version and batch were one to three columns early), 67 measurement rows (`probability_basis` held the codebook version, `codebook_version` the batch), one tender row (T04-LCRFILM: a split claim list and a missing cell) and one validation row (VAL-G2-001: missing `source_id`). Each fixed by script against its exact pattern; old values in `evidence_repair_RECORD.csv`, `measurements_repair_RECORD.csv` and `register_misc_repair_RECORD.csv`. After repair every date and version cell in these registers passes its format check and every row has the header's width.
- Reviewer and review date are blank on the 54 evidence rows (the old layout held notes in those cells, not people or dates). Nothing was invented.

## Session 13i (26/10/08): one-pass question sheet

- New read-only `tools/question_sheet.py` and its output `iain_question_sheet.md`: everything only Iain can supply, in one table with one answer per client where possible (59 completed projects across 50 clients for acceptance, 9 citation statuses, 20 contracting roles, 31 open validation actions, 3 statement approvals). Answers are entered into the registers by Devin with the basis written to `14_fact_provenance.csv`; nothing is guessed.
