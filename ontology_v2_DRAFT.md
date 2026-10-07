# Ontology v2 — DRAFT v2 for review (not adopted, not committed)

**Status:** DRAFT 26/10/07, revision 2 after THAD (advisory), generalisation dry-run across tenders, and consistency audit against the registers. Nothing here is implemented. No register, schema or rule has been changed on this basis (the only repo edit alongside it is the proposed review-protocol rule in `AGENTS.md`, also uncommitted). Supersedes the open options in `case_study_selection_decision.md` if adopted.

## 0. Principles

1. The **register is authoritative**. Cards, `project_index.csv` and any selection view are derived.
2. **Nothing is stored that can be computed.** No stored tier, score or ranking. A selection view is regenerated with an as-of date.
3. **No numeric weights** until 15–20 scored uses exist and a held-out test against human choices passes. Until then ordering is lexicographic and explainable.
4. **Review lanes advise; they never block.** Lanes return FIX-NEEDED lists. Eligibility checks (section 4) filter candidates; they are not review verdicts.
5. **Buyer rules are data on the requirement.** No tender's particular rules are built into the ontology.
6. **Open vocabularies, closed core.** Question types and domain labels grow by adding a row; core fields use fixed values.
7. **Designed against all tenders, not one.** Tested on every tender with usable wording (T01, T13, T21, T22, T05) and on hypothetical shapes (section 11).

## 1. Entities

| Entity | Definition | Home | Key |
|---|---|---|---|
| Project | The work done | `01_projects.csv` | `P##-NAME` |
| Source / Claim / Method | as now | `02`, `04`, `03` | `SRC-…`, `C-…`, `M-…` |
| Opportunity | A tender, bid or direct approach | `08_tenders.csv` | existing `T##-NAME` (e.g. `T01-BCAT`) |
| **Requirement** (new) | One thing a buyer asks for, with its scoring rule | `12_requirements.csv` | `<tender id>#<n>` (e.g. `T22-VA#1`) |
| **Use** (new) | Append-only log of which subject served which requirement | `13_uses.csv` | `U-…` |
| Referee record | Permission state and contact | `11_permission_requests.csv` — **single source of truth** | `PR-…` |

A **subject** of a Use is one of: PROJECT, METHOD, PERSON (team member/CV), AUTHORED (new content written for this tender, e.g. a fresh theory of change). A case study is a Use of a Project; a method statement is a Use of a Method (or AUTHORED); a team section is a Use of PERSON subjects. These are uses, not entities.

## 2. Requirement record

Core: `tender_id`, `ordinal`, `stage` (COMPLIANCE, QUALITY, PRICE, INTERVIEW), `question_type`, `weight`, `text_ref` (source and locator), `inferred` (Y/N).

`question_type` is an open list. Seed: COMPARABLE_WORK, TRACK_RECORD, METHOD, TEAM, PRICE, ADDED_VALUE, UNDERSTANDING_OF_BRIEF, PROJECT_MANAGEMENT_RISK, COMPLIANCE, DATA_PROTECTION, ACCESSIBILITY_OUTPUT, INTERVIEW, COMMERCIAL_TERMS, OTHER. A requirement may carry more than one type and a list of `sub_elements`.

Optional parameters (each tender uses the ones it states): `items_asked`, `referee_required` (Y/N/UNSPECIFIED), `anonymisation_allowed` (Y/N), `disclosure_condition`, `citation_rule` (what work may be cited: delivered only / NDA-bound if disclosable), `length_limit` (words or pages, per section), `score_scale` (e.g. 0–4, 0–10, %), `normalisation` (absolute / relative to best), `threshold_rule` (per-criterion minimum, mean-score reject, shortlist %), `sequence_order` (position in sequential scoring), `price_formula`, `insurance_minima`, `hard_stop`, `consortium_role`, `amends` (a published clarification that changes meaning, e.g. T01 Q6/Q7).

Domain (sector mapping, programme evaluation…) is a *matching label* on projects and methods, rolled up from `sector_activity` and `method_family`. A requirement may also state a domain or comparability condition (e.g. "comparable studies in sector mapping"); when it does, domain is used for matching on that requirement.

## 3. Claim taxonomy (codebook v1.3, no new vocabulary)

| Axis | Field | v1.3 values | Question |
|---|---|---|---|
| What is asserted | `claim_type` | CONTEXT, METHOD_OUTPUT, BID_SUPPORT_DELIVERED, DESIGN, DECISION_USE, EFFECT, UNKNOWN | What kind of statement? |
| Form of change | `effect_family` | DIRECT, PRODUCT, KNOWLEDGE, NETWORK, OPTION, OTHER, NOT_APPLICABLE, UNKNOWN | What form, if any? |
| Evidence state | `outcome_status`, `attribution_strength`, `value_basis` | REPORTED/CORROBORATED/…; DESCRIPTIVE/TESTIMONY/…; as AGENTS.md | How well evidenced? |

Corrections needed (none made): 107 claims use `effect_family=CONTEXTUAL`, which no codebook version defines — recode to NOT_APPLICABLE; 1 claim has an empty `effect_family`; `case_study_selection_decision.md` line 30 labels `claim_type` values as `effect_family` (AGENTS.md itself is correct); `DECISION_USE` is defined (codebook line 39) and used by 0 claims — a client reusing our output is coded here with a documentary source; card-only `METHOD_TRANSFER` (University of South Wales AMGEN bid card and changelog) is not a codebook value and is retired in favour of DECISION_USE.

**Evidence class** (derived per claim; a project or method takes the highest class among its claims; ties shown as ties). Precedence high to low: CORROBORATED_EFFECT (EFFECT + CORROBORATED) > REPORTED_EFFECT (EFFECT + REPORTED) > DOCUMENTED_USE (DECISION_USE with registered source) > DELIVERED_OUTPUT (METHOD_OUTPUT or BID_SUPPORT_DELIVERED) > DESIGN_ONLY > CONTEXT_ONLY > NOT_ESTABLISHED (e.g. EFFECT + NOT_MEASURED). ASSERTED (reported by Iain, no registered source) sits below DELIVERED_OUTPUT and is shown separately; it is cleared when a source is registered. Current counts: CONTEXT_ONLY 116, DESIGN_ONLY 86, DELIVERED_OUTPUT 68, REPORTED_EFFECT 47, CORROBORATED_EFFECT 0, NOT_ESTABLISHED 2, DOCUMENTED_USE 0.

## 4. Eligibility checks (PASS / FAIL / UNKNOWN / N/A)

UNKNOWN is shown and listed for fixing; it is never treated as pass or fail. N/A is used where the check cannot apply.

| Check | Rule | Fields |
|---|---|---|
| E1 Delivered | `lifecycle_status` COMPLETED and `client_accepted` Y | register; **new column `client_accepted`** (Y/N/UNKNOWN) |
| E2 Citable as the requirement allows | `citation_status` meets the requirement's `citation_rule` (default: DELIVERED_WORK or PUBLIC_REPORT) | **new register column `citation_status`** |
| E3 Not a lapsed option | a bid-support commission is judged on its own delivery; the programme outcome is `programme_status` | `programme_status` (needs backfill, 47 blank) |
| E4 Method current | method not superseded in an answer-changing way; N/A if the project has no method rows | `03_methods.method_status` (+ SUPERSEDED) |
| E5 Role wording resolvable | `contracting_role` set; `prime_contractor` required when role is not PRIME/DIRECT | register |

**Lifecycle vocabulary.** Reconcile with codebook v1.3 §6.3 (PROPOSED, COMMISSIONED, IN_PROGRESS, COMPLETED, CANCELLED, UNKNOWN) rather than inventing a third set; 57 of 70 projects are already COMPLETED. Proposed v1.4 additions: NOT_AWARDED, BID_PENDING. Mapping: ACTIVE, ONGOING, IN_PROGRESS → IN_PROGRESS; COMPLETE_NOT_CLOSED, REPORTING_COMPLETE, PHASE_COMPLETE_AWAITING_INSTRUCTION → COMPLETED (closure detail in a note); PREFERRED_BIDDER, LIVE_BID → BID_PENDING. Phased or cyclical work (e.g. Kirklees Creative Industries Mapping, marked ongoing but with delivered cycles) is modelled as phases (`parent_project_id`, `phase_name`), not forced into one value. Bid support that was delivered while the bid failed (CoSTAR bid support; Creative City SIPF application; the Lancaster True North bid support) is COMPLETED with `programme_status=NOT_AWARDED`; AGENTS.md "Unsuccessful bids" and QA check 7 need a carve-out for these.

## 5. Matching and ordering (no weights)

For each Requirement, candidates are the Projects (or Methods, People) whose checks are not FAIL. Strict order:
1. Fit: question-type coverage, then domain label where the requirement states it, then client type/geography where stated.
2. Highest evidence class.
3. Role: PRIME, DIRECT, SUBCONTRACTOR, ASSOCIATE/ADVISORY (wording rule applies; never ranked as prime).
4. Recency.
Ties are shown. Where a requirement asks for more than one item, selection maximises coverage of its sub-elements before depth. Output shows the rule that placed each candidate and a ranked reserve per slot. For AUTHORED subjects the output is an **evidence-gap list**: what the register can support, what it cannot, and which projects could ground the new content.

## 6. Composition

For each selected subject: sheet-ready headline figure with correct `value_basis` and the source's own wording; comparability first line; permitted role wording (associate = "as BOP Associate Director"; design = "designed the evaluation approach"; contracting structure named). Client-supplied data is cited as client data.

## 7. Submission readiness (conditional)

Runs only when the requirement has `referee_required=Y` or states a disclosure condition. For each selected item: NAMED referee confirmed (from `11_permission_requests.csv`), ANONYMISE (only if `anonymisation_allowed`, applying the `disclosure_condition`), or SWAP FOR RESERVE. Asks are issued as soon as selection is made. `reference_permission` on projects is derived from `11_permission_requests.csv`, not stored separately; status vocabulary and owner for that file to be defined (DRAFTED, SENT, ESTABLISHED, DECLINED, CAPPED).

## 8. Method statements and team sections

Method: same pipeline with Method subjects (`03_methods.csv`; `method_family` rolled up to about 10; E4 applies; evidence from the claims the method produced via `method_ids` on claims — join coverage to be audited). Team: PERSON subjects need a people register (new, small): name, role, relevant projects, availability. Not designed here beyond the entity; flagged as a gap.

## 9. Use log

`13_uses.csv`: tender, requirement, subject type and id, wording used, referee outcome, `score_received`, `score_scale`, outcome. Append-only. Scores do not feed ordering until 15–20 comparable scored uses exist; they are an audit trail. Unused strong candidates are logged with the reason.

## 10. Fact authority and maintenance

| Fact | Authoritative | Derived |
|---|---|---|
| lifecycle, role, dates, client, citation_status, contract value, client_accepted | `01_projects.csv` | cards, `project_index.csv` |
| permission state | `11_permission_requests.csv` | `reference_permission` on projects/cards |
| claim classification | `04_claims.csv` | card findings |
| buyer rules | `12_requirements.csv` | — |

`regenerate_index.py` (lines 13, 38 read lifecycle and contract value from cards) is changed to read the register. Stale-artefact rule extended: regenerate the selection view after any change to the register, claims, methods, requirements or permissions.

**New QA checklist items** (added to AGENTS.md on adoption): uses→projects/methods and uses→requirements foreign keys valid; no stored tier or score column anywhere; CONTEXTUAL count = 0; dangling claim/evidence references = 0; every UNKNOWN check listed on a fix list; tender IDs in requirements match `08_tenders.csv`. Every fix is a separate commit that satisfies the session-closure hook.

## 11. Generality tests (recorded results to be added)

Requirement records back-filled for T01, T13, T21, T22, T05 (and inferred for T04, T02, T14), marked inferred where applicable. Hypothetical (a) evaluation commission asking for a theory of change and method, no case studies: handled via AUTHORED subjects and the evidence-gap output. Hypothetical (b) sector-mapping tender asking for 3 comparable studies and CVs: handled via domain-stated matching, composition rule for figures, and PERSON subjects. Still to test: social-value, accreditation and framework call-off questions.

## 12. Register fixes this depends on (ordered; prerequisites first)

1. Add register columns `citation_status`, `client_accepted`; derive `reference_permission` from `11_permission_requests.csv`. Header check first (schema-drift rule).
2. Reconcile `lifecycle_status` with the codebook (section 4); backfill `programme_status`.
3. Sync cards to register; change `regenerate_index.py`.
4. Backfill `contracting_role` (27 empty: Proving Services Suffolk (FHRG); BAC + LIVR Project Evaluation; Lancashire Digital Strategy; Tees Valley Creative Economy Baseline; WMGC Pitch Books; Wakefield Creative Skills Development; UKRI Liverpool Visit and CoSTAR Engagement; SYMCA ARG Evaluation; Somerset Cultural Strategy; Manchester Place Partnership; Rushmoor Cultural Strategy and Compact; Plymouth National Marine Park; Leicester Cultural Compact; Theatre Royal Plymouth Engagement; University of Liverpool Heritage CPD; Wakefield Our Year 2024 Business Case Justification (BCJ); WYCA WY Create; Wakefield Our Year 24 Evaluation; Wakefield CCI Skills Needs Assessment; City St George's SCCI; Lancaster AHRC CIC; Lancaster Uni Horizon Bid (Virtual Agora); CELL; Southampton Forward Strategic Review; WB6 Creative Economy Pulse; Herefordshire Culture Strategy; LCR Production Fund Final Evaluation (2024-25)) and `citation_status` for the ten earliest projects (North East Scotland Creative Industries Mapping; From Good to Great (Innovate GM / Innovate UK); MITIH Createch Ecosystem (MediaCity ITIH); GBSLEP Creative Economy Mapping; WMCA Creative Business Scaleup; CoSTAR bid support; Creative City (SIPF application); Liverpool City Region Digital & Creative Industries Cluster Mapping; Creative Digital Economy Catapult challenges paper; Kirklees Creative Industries Mapping (three cycles: 2022 2024 2026)) and where still UNKNOWN (Wakefield Our Year 2024 Business Case Justification (BCJ); Wakefield Our Year 24 Evaluation; WB6 Creative Economy Pulse; British Council Kotor Exchange Pilot (FCDO-funded); British Council Creative Economy Council Development (MNE NM + WB)).
5. Recode CONTEXTUAL (107); fix one empty `effect_family`; fix the label in the decision doc; code DECISION_USE; retire METHOD_TRANSFER.
6. Resolve dangling references (40 claim IDs on 16 cards; 254 evidence-link rows pointing at 249 absent claims).
7. Roll up `sector_activity` (60 values) and `method_family` (41) to about 10 each; normalise `client_type` (15 variants differ by case); add SUPERSEDED; repair `08_tenders.csv` T04 drift.
8. Create `12_requirements.csv`, `13_uses.csv`; back-fill requirements.

Dry-run on today's data (70 projects), using the checks as written, for orientation only: E1 0 pass / 9 fail / 61 unknown (no `client_accepted`); E2 50 / 5 / 15; E3 21 / 6 / 43; E4 34 / 0 / 36 (becoming N/A); E5 40 / 0 / 30. The method cannot yet select anything usable: items 1–4 above come first.

## 13. Decisions taken (26/10/07, Iain) and still open

**Test-strength rule (Iain, 26/10/07):** no existing check, gate or QA test may be weakened, relaxed or made "not applicable" without Iain's explicit permission. Lane suggestions that would do so (treat a check over 50% UNKNOWN as unused; E4 "not applicable" where a project has no method rows; time-boxing the 254 dangling evidence links; backfilling only 20-25 projects) are NOT adopted. In this draft E4 returns UNKNOWN, not N/A, where there are no method rows.

**Taken**
1. Direction approved: register is truth; existing codebook claim axes; a case study is a use of a project against a tender requirement. Nothing built.
2. Scope: staged build plus a minimal append-only use log from now. Two register columns (`citation_status`, `client_accepted`), one computed selection view, requirements as free text in tender notes; `12_requirements.csv` only after the same structure has been retyped three times.
3. Lifecycle: align to codebook v1.3 section 6.3 plus BID_PENDING, with one name per stage (historical variants collapsed). ACTIVE, ONGOING, IN_PROGRESS -> IN_PROGRESS; unclosed work (COMPLETE_NOT_CLOSED, REPORTING_COMPLETE, PHASE_COMPLETE_AWAITING_INSTRUCTION) -> IN_PROGRESS until client acceptance is recorded; PREFERRED_BIDDER -> BID_PENDING. The same one-name principle is to be checked on other fields (card lifecycle variants, `client_type` case, `sector_activity` styles, `method_family` near-duplicates), each as its own decision.
4. Bids as projects: apply the existing AGENTS.md rule (a project row only for a paid commission; our own bids in `08_tenders.csv` only). Solent Create Growth Programme bid development stays a project (paid, completed, programme NOT_AWARDED). Derby Culture Strategic Review bid moves to tenders only (to be executed in the build step; its four sources re-pointed).
5. Evaluator-reported effects: adopted as a separate named sub-class ("programme effect reported, as evaluator"), visible and counted, with wording capped at the evaluator role. Iain: do NOT assume a delivered output carries more weight than an evaluation finding; they are different classes of output, not a hierarchy. CONSEQUENCE: the single evidence-class ladder in section 3 is withdrawn pending decision 6.
6. Evidence kinds: the single ladder is replaced by parallel kinds (delivered output; evaluation finding; programme effect reported as evaluator; documented use by a client; design or recommendation; context or baseline), never ranked against each other. Each tender requirement names the kinds it wants. Strength (e.g. corroborated, reported, descriptive) is shown within each kind. A project displays its mix of kinds with counts, not a single label. Sections 3 and 5 of this draft are to be rewritten accordingly (revision 3).
7. Client reuse: card-only `METHOD_TRANSFER` retired in favour of the codebook's `DECISION_USE`, recorded as asserted until a source document is registered (e.g. for the University of South Wales AMGEN bid: their submission or AHRC feedback).
8. AGENTS.md: the review-team rule (full lane set, all advisory, generality test, analysis before commit, separate revertible commits) is adopted, together with a standing rule that no test, gate or QA check may be weakened without the user's explicit permission. Edit made in AGENTS.md, uncommitted pending the commit decision.

**Executed 26/10/07 (register edits):** decisions 2, 3 and 4 and the three project facts are now in the register (31-field register, lifecycle aligned, Derby bid row retired, Lancashire / Lancaster Horizon / Creative Scotland recorded). Not yet done: Kirklees phase rows, client_accepted and early citation_status backfill, Lancaster re-key. See CHANGELOG session 26/10/07 (5).

**Facts established (now written to the register)**
- Lancashire Create Growth Programme bid: paid; direct contract with Lancashire County Council; PO 321786253/0, GBP 10,000 ex VAT; invoice 1221 GBP 12,000 incl VAT, balance 0.00. Register role SUBCONTRACTOR to become DIRECT.
- Lancaster University Horizon bid (Virtual Agora): paid; direct; PO 500215141 (8 Oct 2025) GBP 4,158.33 ex VAT (workshop preparation 2,083.33; bid writing 2,075.00); invoice INV-1339 GBP 4,990.00 incl VAT paid by BACS 23 Oct 2025; bid NOT_AWARDED. Note: the figure "fee <GBP 5k" held on another Lancaster row matches this invoice and may be misattached.
- Creative Scotland salary benchmarking framework: awarded and signed (per Iain); Agreement CS/CA1019, 30 Sep-30 Oct 2026, GBP 11,750 ex VAT (confirmed by Iain; equals the agreement's maximum of GBP 14,100 incl VAT at 20%); direct; live, so IN_PROGRESS and not eligible as delivered evidence until complete.

**Still open (one at a time)**
8. Permission requests: `11_permission_requests.csv` as the single source of permission state; plain-language single-question ask template; owner and chase interval.
9. Evidence class: restate principle 3 honestly (lexicographic order is weighting by another name) and cap case-study wording at the cited claim's own class?
10. Provenance on backfilled gating fields (who, when, basis) and a candidates-considered log?
11. Where requirements live (`12_requirements.csv` vs free text) after the three-times test; people register; method selection; rollups.

## 14. Reversal

Everything in this draft is one uncommitted file plus one uncommitted AGENTS.md edit. Adoption would be a series of separate, individually revertible commits, one per item in section 12, each with its own changelog entry.
