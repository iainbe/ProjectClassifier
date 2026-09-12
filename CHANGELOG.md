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
