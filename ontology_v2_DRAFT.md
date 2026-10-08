# Ontology v2 — DRAFT revision 4, final pass (working; not adopted; committed on the working branch)

**Status:** DRAFT revision 4, 26/10/08 (final pass: the whole draft re-run against the registers and tools; section 16 records what was checked). Not adopted. Decisions 1 to 15 (section 13) are recorded and most of their register, tool and file changes are built and committed on the working branch; what is not done is adoption: the final lane review of this whole draft, Iain's approval, and the AGENTS.md changes listed in section 15. Supersedes the open options in `case_study_selection_decision.md` if adopted.

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
| **Requirement** | What a buyer asks for, with its scoring rule, per tender (decision 13) | `tender_requirements/<tender>.md`, linked from `08_tenders.csv` `requirement_map_location` | `## item:` blocks |
| **Method statement** | Reusable "how we do this" text with status and disclosure (decision 14 and method package) | `method_statements/MS-nn_*.md`, `03_methods.csv` `statement_id` | `MS-nn` |
| **Person / involvement** | Who did what on which project (decision 14) | `15_people.csv`, `16_involvement.csv` | `PER-nn`, `INV-nnnn` |
| **Fact provenance** | Basis of a backfilled gating fact (decision 12) | `14_fact_provenance.csv` | `FP-nnnn` |
| **Selection** (new) | Append-only log of the candidates considered for a requirement item, which were chosen and why not | `13_selections.csv` | `SEL-…` |
| Referee record | Permission state and contact | `11_permission_requests.csv` — **single source of truth** | `PR-…` |

A **subject** of a Selection is one of: PROJECT, METHOD (through a method statement), PERSON (team member), AUTHORED (new content written for this tender, e.g. a fresh theory of change). A case study is a selection of a Project; a method section is a selection of a method statement (or AUTHORED); a team section is a selection of PERSON subjects. These are uses, not entities.

## 2. Requirement record

Built as one Markdown file per tender (decision 13) holding the frozen contract and one block per requested item; `tools/selection_view.py --requirements` and `tools/method_view.py --requirements` read it. The fields below remain the guide to what a file may state; they become a flat register only if three tenders share a shape. First file: `tender_requirements/T22-VAIMP.md`.

Core: `tender_id`, `ordinal`, `stage` (COMPLIANCE, QUALITY, PRICE, INTERVIEW), `question_type`, `weight`, `text_ref` (source and locator), `inferred` (Y/N).

`question_type` is an open list. Seed: COMPARABLE_WORK, TRACK_RECORD, METHOD, TEAM, PRICE, ADDED_VALUE, UNDERSTANDING_OF_BRIEF, PROJECT_MANAGEMENT_RISK, COMPLIANCE, DATA_PROTECTION, ACCESSIBILITY_OUTPUT, INTERVIEW, COMMERCIAL_TERMS, OTHER. A requirement may carry more than one type and a list of `sub_elements`.

Optional parameters (each tender uses the ones it states): `items_asked`, `referee_required` (Y/N/UNSPECIFIED), `anonymisation_allowed` (Y/N), `disclosure_condition`, `citation_rule` (what work may be cited: delivered only / NDA-bound if disclosable), `length_limit` (words or pages, per section), `score_scale` (e.g. 0–4, 0–10, %), `normalisation` (absolute / relative to best), `threshold_rule` (per-criterion minimum, mean-score reject, shortlist %), `sequence_order` (position in sequential scoring), `price_formula`, `insurance_minima`, `hard_stop`, `consortium_role`, `amends` (a published clarification that changes meaning, e.g. T01 Q6/Q7).

Domain (sector mapping, programme evaluation…) is a *matching label* on projects and methods, rolled up from `sector_activity` and `method_family`. A requirement may also state a domain or comparability condition (e.g. "comparable studies in sector mapping"); when it does, domain is used for matching on that requirement.

## 3. Claim taxonomy (codebook v1.3 plus the v1.4 additions file; no new claim vocabulary)

| Axis | Field | v1.3 values | Question |
|---|---|---|---|
| What is asserted | `claim_type` | CONTEXT, METHOD_OUTPUT, BID_SUPPORT_DELIVERED, DESIGN, DECISION_USE, EFFECT, UNKNOWN | What kind of statement? |
| Form of change | `effect_family` | DIRECT, PRODUCT, KNOWLEDGE, NETWORK, OPTION, NOT_APPLICABLE, UNKNOWN | What form, if any? |
| Evidence state | `outcome_status`, `attribution_strength`, `value_basis` | REPORTED/CORROBORATED/…; DESCRIPTIVE/TESTIMONY/…; as AGENTS.md | How well evidenced? |

**Corrections made (26/10/08).** 200 pure CONTEXT claims that used the undefined `effect_family=CONTEXTUAL` now carry NOT_APPLICABLE (record: `claims_contextual_RECORD.csv`); 5 claims that are not pure context still carry it for Iain to decide (VAL-S261008-15). No claim has an empty `effect_family`. Four governed columns (`publication_status`, `commercial_reuse`, `reviewer_confidence`, `contrary_evidence`) had 413 displaced values; 387 exact duplicates were cleared to empty (record: `claims_legacy_clear_RECORD.csv`) and 26 are held for Iain (`claims_legacy_held_LIST.csv`); empty now means not recorded and is read as INTERNAL_ONLY, enforced by `tools/check_claims_columns.py` (QA item 14). `DECISION_USE` is defined and used by 0 of 595 claims; a client reusing our output is coded here when a documentary source is registered, and card-only `METHOD_TRANSFER` is retired in favour of it. 249 claims deleted in an earlier agent commit (eb2674d) were restored (244 plus C-R5-524 to 528, five of them with normalised fields) and 49 claims with displaced role and contribution columns were repaired (CHANGELOG sessions 13a to 13h).

**Evidence kinds (decisions 5 and 6).** There is no single evidence ladder. A project shows, side by side and never ranked, how many of its claims fall in each kind: delivered output (METHOD_OUTPUT, BID_SUPPORT_DELIVERED), effect reported (EFFECT where Fifth Sector was not the evaluator), effect as evaluator (EFFECT with an EVALUATOR role), documented use (DECISION_USE), design (DESIGN), context (CONTEXT). A tender item names the kinds it wants and the kinds act as a filter (decision 10). The strength within a kind (corroborated, reported, descriptive) is shown, and wording is capped at the cited claim's class (decision 11). Current claims (595): CONTEXT 227, DESIGN 155, METHOD_OUTPUT 112, EFFECT 86, BID_SUPPORT_DELIVERED 15, DECISION_USE 0. Claim counts reflect coding effort and are not a measure of strength.

## 4. Eligibility checks (PASS / FAIL / UNKNOWN / N/A)

UNKNOWN is shown and listed for fixing; it is never treated as pass or fail. N/A is used where the check cannot apply.

| Check | Rule | Fields |
|---|---|---|
| E1 Delivered | `lifecycle_status` COMPLETED and `client_accepted` Y | register; **new column `client_accepted`** (Y/N/UNKNOWN) |
| E2 Citable as the requirement allows | `citation_status` meets the requirement's `citation_rule` (default: DELIVERED_WORK or PUBLIC_REPORT) | **new register column `citation_status`** |
| E3 Not a lapsed option | a bid-support commission is judged on its own delivery; the programme outcome is `programme_status` | `programme_status` (backfilled; NOT_APPLICABLE where there was no programme bid) |
| E4 Method current | has method rows and none is SUPERSEDED (UNKNOWN when there are no rows, never N/A); also FAIL when a linked method statement is SUPERSEDED (added 26/10/08, additive) | `03_methods.method_status`, `statement_id`, statement status |
| E5 Role wording resolvable | `contracting_role` set; `prime_contractor` required when role is not PRIME/DIRECT | register |

**Lifecycle vocabulary.** Reconcile with codebook v1.3 §6.3 (PROPOSED, COMMISSIONED, IN_PROGRESS, COMPLETED, CANCELLED, UNKNOWN) rather than inventing a third set; 57 of 70 projects are already COMPLETED. Added in the register: BID_PENDING; NOT_AWARDED is reserved for `programme_status` (decisions 3 and 4). Mapping: ACTIVE, ONGOING, IN_PROGRESS → IN_PROGRESS; COMPLETE_NOT_CLOSED, REPORTING_COMPLETE, PHASE_COMPLETE_AWAITING_INSTRUCTION → COMPLETED (closure detail in a note); PREFERRED_BIDDER, LIVE_BID → BID_PENDING. Phased or cyclical work (e.g. Kirklees Creative Industries Mapping, marked ongoing but with delivered cycles) is modelled as phases (`parent_project_id`, `phase_name`), not forced into one value. Bid support that was delivered while the bid failed (CoSTAR bid support; Creative City SIPF application; the Lancaster True North bid support) is COMPLETED with `programme_status=NOT_AWARDED`; AGENTS.md "Unsuccessful bids" and QA check 7 need a carve-out for these.

## 5. Matching and ordering (no weights)

**Decision 10 (Iain, 26/10/08): evidence kind is a filter, not a rank.** The requirement names the kinds of evidence it wants (delivered output, effect reported, effect as evaluator, documented use, design, context). A project is a candidate only if its checks are not FAIL and it holds at least one wanted kind. Kinds are never ranked against each other, and the count of claims is not a measure of strength (it reflects coding effort).

Candidates are then shown with fit, kind mix, role, recency and geography as visible columns. **Decision 10b (Iain, 26/10/08, option C):** the default view is alphabetical with no ranking. `tools/selection_view.py --order proposed` writes a separate trial view in the proposed order (kinds held, then contracting role, then most recent end date, then geography if given), each placement explained in words, no score, so it can be compared with Iain's own choices and tested after 15 to 20 scored uses. (Earlier wording of the open point: whether role, recency and geography order them, and in what sequence; the proposal is kind match, role, recency, geography with each placement shown as a reason, not a score, tested against Iain's choices after 15 to 20 scored uses). Until decided, the view lists candidates alphabetically within groups. Geography counts only where the requirement states it. Where a requirement asks for more than one item, selection maximises coverage of its sub-elements before depth. For AUTHORED subjects the output is an **evidence-gap list**: what the register can support, what it cannot, and which projects could ground the new content.

## 6. Composition

For each selected subject: sheet-ready headline figure with correct `value_basis` and the source's own wording; comparability first line; permitted role wording (associate = "as BOP Associate Director"; design = "designed the evaluation approach"; contracting structure named). Client-supplied data is cited as client data. Wording is capped at the evidence class of the cited claim (decision 11).

## 7. Submission readiness (conditional)

Runs only when the requirement has `referee_required=Y` or states a disclosure condition. For each selected item: NAMED referee confirmed (from `11_permission_requests.csv`), ANONYMISE (only if `anonymisation_allowed`, applying the `disclosure_condition`), or SWAP FOR RESERVE. Referees are normally cited by name in the tender and only asked once the bidder is shortlisted (Iain, 26/10/08), so referee permission is not a gate on selection or submission: each selected item needs a named contact chosen as likely to agree (basis recorded), and wording must never claim agreement that has not been given. The ask is sent at shortlist using the plain-language template. Where a buyer requires anonymised entries to be disclosable on request, the disclosure duty is checked per item at selection. `reference_permission` on projects is derived from `11_permission_requests.csv`, not stored separately; status vocabulary and owner for that file to be defined (DRAFTED, SENT, ESTABLISHED, DECLINED, CAPPED).

## 8. Method statements and team sections

Method statements (method package, lane-reviewed 26/10/08): three layers. A rolled-up `method_family_rollup` (ten families, none above a fifth of methods) is a filter; a reusable **method statement** (`method_statements/MS-nn_*.md`) holds the "how we do this" text, an approval card, a generic bid-ready paragraph, what we can and cannot claim, an evidence class (DELIVERED, DESIGN_ONLY), a disclosure status and a status (DRAFT, CURRENT, SUPERSEDED, set to CURRENT only by Iain); and the **applications** are the existing method rows, linked by `statement_id`. Statements are written when a requirement needs them. `tools/method_view.py` hides claim wording and figures for any statement not cleared for disclosure, flags blockers, cautions and staleness in plain English, and with `--requirements` prints which statements cover which buyer questions (for T22-VAIMP: 3 of 8 questions have no statement). E4 applies. Evidence for a statement comes from the claims its applications produced via `method_ids`; the link from claims to methods (`method_ids` on the claim) is the authority and every claim now names a registered method or none; the reverse list (`claim_ids` on the method row) was incomplete for 163 links, a pattern present since the earliest visible commit, completed 26/10/08 (VAL-S261008-19, `methods_claim_ids_RECORD.csv`); the two sides now agree both ways. Known limits: three statements exist; only five of 23 tenders carry usable requirement wording, so which method statements win points cannot be known (selection effect); BOP Consulting and other competitors are never asked for permission (PR-07).

Team: PERSON subjects use the people register (`15_people.csv`, `16_involvement.csv`, decision 14); `tools/people_view.py` states each person's role on each project with the project's contracting arrangement.

## 9. Selection log (candidates considered)

`13_selections.csv`, append-only (Iain decision 15, 26/10/08; replaces the separate `13_uses.csv` use log). Written by `tools/record_selection.py` after Iain chooses: one row per candidate shown on a tender item, with its position in the default (alphabetical) order and in the proposed order, chosen Y or N, a reason code for each candidate not chosen (WEAKER_FIT, EVIDENCE_GAP, ROLE_WORDING, RESTRICTED_OR_CONSENT, REFEREE_UNLIKELY, PAGE_LIMIT, OTHER; NOT_RECORDED when none is given, never defaulted), and for chosen items the wording used and the referee outcome. A chosen project that was not in the view is recorded as OUTSIDE_VIEW. Buyer scores and outcomes are appended later as OUTCOME rows. Scores do not feed ordering until 15 to 20 comparable scored uses exist; the log is an audit trail and the test data for the trial ordering (would the proposed order have picked what Iain picked?). The tool writes nothing without `--write`.

## 10. Fact authority and maintenance

| Fact | Authoritative | Derived |
|---|---|---|
| lifecycle, role, dates, client, citation_status, contract value, client_accepted | `01_projects.csv` | cards, `project_index.csv` |
| permission state | `11_permission_requests.csv` | `reference_permission` on projects/cards |
| claim classification | `04_claims.csv` | card findings |
| buyer rules | `12_requirements.csv` | — |
| basis of a backfilled gating fact | `14_fact_provenance.csv` | basis shown in eligibility report and selection views |

`regenerate_index.py` (lines 13, 38 read lifecycle and contract value from cards) is changed to read the register. Stale-artefact rule extended: regenerate the selection view after any change to the register, claims, methods, requirements or permissions.

**New QA checklist items** (added to AGENTS.md on adoption): selections→projects and selections→tenders foreign keys valid; every non-chosen candidate has a reason code or NOT_RECORDED; no stored tier or score column anywhere; CONTEXTUAL count = 0; dangling claim/evidence references = 0; every UNKNOWN check listed on a fix list; tender IDs in requirements match `08_tenders.csv`. Every fix is a separate commit that satisfies the session-closure hook.

## 11. Generality tests (results, 26/10/08)

Run so far: the T22-VAIMP candidate view through all nine tender-review lanes (findings in `tier2_qa_review.md` and the T22 notes), and the method package through eight lanes with the generality cases written into their briefs. Results: (a) a tender asking for a method statement for a data dashboard or framework build **fails** at present: the families and statements are evaluation and economic only, and the design can only say "no evidence"; (b) a tender where the only relevant experience is associate work for another consultancy **partly passes**: MS-03 shows the pattern (contracting structure named, reuse restriction recorded, no permission sought from a competitor). Only five of 23 tenders have usable requirement wording (T01-BCAT, T05-DERBY, T21-CSFI, T22-VAIMP, T23-TVBTV), so the design is fitted to five formal tenders; requirement files for T21 and T23 are the next test. Still untested: social-value, accreditation and framework call-off questions.

## 12. Register fixes this depends on (status 26/10/08)

1. DONE: `citation_status` and `client_accepted` columns added; `reference_permission` derived from `11_permission_requests.csv`.
2. DONE: lifecycle aligned (decision 3); `programme_status` backfilled.
3. DONE: cards synced to the register; `regenerate_index.py` reads the register.
4. MOSTLY DONE (26/10/08, Iain's answers with provenance in `14_fact_provenance.csv`): `contracting_role` and `citation_status` are now recorded on all 60 completed projects; `client_accepted` is now Y on all 59 completed projects (31 set today on Iain's bulk answer, basis IAIN_STATEMENT, no written record checked). Production Park GVA Study (P31) is on hold, not complete (Iain), and is held as IN_PROGRESS. One-pass sheet: `iain_question_sheet.md`.
5. MOSTLY DONE: 200 CONTEXTUAL recoded; 5 left (VAL-S261008-15); DECISION_USE still unused; METHOD_TRANSFER retired in the draft only (card text not yet edited).
6. DONE except one link set: 249 deleted claims restored, so evidence rows pointing at absent claims are 0 and method rows pointing at absent claims are 0. The reverse direction was not checked until the final pass: 20 restored claims (C-G2-504 to 523, on P11-ELFC and P12-KIRK15) named methods M-R3-022 and M-R3-023 that never had a row; fixed 26/10/08 by re-pointing to existing method rows or clearing the reference (VAL-S261008-18, `claims_method_links_RECORD.csv`). Cause of the deletion traced (VAL-S261008-13, section 16).
7. PARTLY DONE: `method_family` rolled up and `SUPERSEDED` added (codebook v1.4 additions); `sector_activity` (60 values) and `client_type` (15 variants, 11 after case) still to normalise, each as its own decision.
8. DONE: requirements are per-tender files (decision 13); selection log built (decision 15); T21 and T23 requirement files still to write.
9. DONE (new): displaced-column drift repaired in claims (49), methods (19), sources (50), evidence links (54), measurements (67) and single rows in tenders and validation actions; format checks for dates and version labels now catch it where field counts do not.

Current checks on 70 projects (60 completed), orientation only: E1 delivered 59 pass / 11 fail / 0 unknown (every pass rests on a recorded acceptance, most of it Iain's statement without a document); E2 citable 64 / 4 / 2; E3 lapsed option 70 / 0 / 0; E4 method current 36 pass / 34 unknown (34 projects have no method rows); E5 role wording 65 / 0 / 5. The E4 unknowns are method rows nobody has written; no check has been relaxed.

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

9. Permission requests: citing delivered work needs no permission unless a restriction marker exists (written into AGENTS.md); referee permission recorded only in the permission file and derived elsewhere; 27 of 35 requests closed as not required, 3 turned into internal checks, 5 kept as plain-language asks with owner Iain and a reminder after five working days. Executed in session 8.

**Taken 26/10/08 (A):** referee timing: referees are cited by name in the tender and asked only once shortlisted. Section 7 rewritten; the three drafted referee asks (PR-03, PR-04, PR-05) are held until shortlist. T22 review lanes raised a related risk (a named contact first hearing of it from the buyer); handled as advice on choosing a likely-to-agree contact, not as a gate.

**Taken 26/10/08 (B):** decision 10: evidence kind filters candidates and never ranks them. Section 5 rewritten. Decision 10b taken (option C): default unordered, proposed order available as a trial switch. Background: whether and how role, recency and geography order the survivors (lane advice: role is already limited through the claim's attribution wording and recency overlaps the method-current check, so ranking on them risks double counting).

**Taken 26/10/08 (C):** decision 11: case-study wording is capped at the evidence class of the claim it cites. An effect reported as evaluator is worded "the evaluation found"; a modelled estimate is worded "modelled estimate" with its boundary, price basis and status; a forecast or proposal is never worded as achieved; contribution claims name the contracting structure. First worked cases: C-S261008-018 (Beatles modelled GVA) and the P88 forecast claims.

**Taken 26/10/08 (D):** decision 12: provenance of backfilled gating facts goes in an append-only `14_fact_provenance.csv` (project, field, value, basis, source or note, recorded by, date). Basis list: DOCUMENT, WRITTEN_CLIENT, VERBAL_CLIENT, IAIN_STATEMENT, INFERRED. The register stays flat. Basis is shown beside E1, E2 and E5 results and never changes a PASS, FAIL or UNKNOWN. Seeded with 12 facts settled this week; the older backfill carries no basis and is reported as "no basis recorded" (E2: 55 of 55 PASS; E5: 39 of 44 PASS). The candidates-considered log remains open.

**Taken 26/10/08 (E):** decision 13, where requirements live: one file per tender in `tender_requirements/<tender>.md` (frozen turn contract plus one block per requested item: wording source, evidence kinds wanted, keywords, count, citation, referee and anonymisation rules, who read it and when), linked from the existing `requirement_map_location` field of `08_tenders.csv`. `selection_view.py --requirements <tender>` reads it, so a view can be regenerated exactly. Not a register: convert to a flat `12_requirements.csv` only if three tenders end up with the same shape (decision 2). First file: T22-VAIMP, from the 08_tenders row; verbatim ITT wording still to add. Candidates for the second and third files: T21-CSFI, T23-TVBTV.

**Taken 26/10/08 (F):** decision 14, people register: two small tables, `15_people.csv` (name, organisation, status, skills tags, bio location, `named_in_bids_ok` Y/N/UNKNOWN) and `16_involvement.csv` (person, project, role on the project, period, basis, source). No contact details or CVs in the repo. Tender-specific availability lives in the tender's requirements file. `tools/people_view.py` joins them to the project register so a team section states role and contracting arrangement. Seeded only from sources: Iain Bennett, Lynne McCadden and Sara Sartorius (five involvement rows from report covers and a deck) and Towell as an external partner with nothing credited. The view shows the contracting role as not recorded for both credited projects, which is the gap to fill before a team section is written.

**Taken 26/10/08 (G):** decision 15, candidates-considered log: `13_selections.csv` and `tools/record_selection.py` as described in section 9. Nothing recorded yet: no selection has been made for T22-VAIMP. The tool was tested on a scratch copy (dry run, write, outcome and error paths).

**Executed 26/10/07 (register edits):** decisions 2, 3 and 4 and the three project facts are now in the register (31-field register, lifecycle aligned, Derby bid row retired, Lancashire / Lancaster Horizon / Creative Scotland recorded). Lancaster re-key done 26/10/07 (session 6). Not yet done: Kirklees phase rows, client_accepted and early citation_status backfill. See CHANGELOG session 26/10/07 (5).

**Facts established (now written to the register)**
- Lancashire Create Growth Programme bid: paid; direct contract with Lancashire County Council; PO 321786253/0, GBP 10,000 ex VAT; invoice 1221 GBP 12,000 incl VAT, balance 0.00. Register role SUBCONTRACTOR to become DIRECT.
- Lancaster University Horizon bid (Virtual Agora): paid; direct; PO 500215141 (8 Oct 2025) GBP 4,158.33 ex VAT (workshop preparation 2,083.33; bid writing 2,075.00); invoice INV-1339 GBP 4,990.00 incl VAT paid by BACS 23 Oct 2025; bid NOT_AWARDED. Note: the figure "fee <GBP 5k" held on another Lancaster row matches this invoice and may be misattached.
- Creative Scotland salary benchmarking framework: awarded and signed (per Iain); Agreement CS/CA1019, 30 Sep-30 Oct 2026, GBP 11,750 ex VAT (confirmed by Iain; equals the agreement's maximum of GBP 14,100 incl VAT at 20%); direct; live, so IN_PROGRESS and not eligible as delivered evidence until complete.

**Decisions 8 to 15 are recorded above under their dates (permission requests; referee timing A; evidence kind as filter B; wording cap C; provenance D; requirements per tender E; people register F; selection log G; method package with statement layer).** The earlier numbered open items 8 to 11 are all closed: single permission source (9), evidence kinds and wording (5, 6, 10, 11), provenance and the selection log (12, 15), and requirements, people and methods (13, 14, method package).

**Still open (one at a time)**
- Normalise `sector_activity` (60 values) and `client_type` (15 variants; 11 after case), each as its own decision (decision 3 principle).
- Where the 5 remaining CONTEXTUAL claims go (VAL-S261008-15), the evaluator-role question on 7 claims (VAL-S261008-10), and the 26 held claims-column cells.
- Facts only Iain can supply: statement approvals and the open validation actions (`iain_question_sheet.md`). Client acceptance is recorded for every completed project; the basis is Iain's statement, not documents, and shows in the eligibility report.
- Requirement files for T21-CSFI and T23-TVBTV (the second and third; the three-times test for a flat requirements register).
- Adoption (section 15) after a final lane review of this draft.

## 14. Reversal

This draft is one file on the working branch (PR #2); the AGENTS.md edits are already committed. Adoption would be a series of separate, individually revertible commits, one per item in section 12, each with its own changelog entry.

## 15. Adoption package (not done; needs a final lane review and Iain's approval)

If Iain adopts this draft, these changes follow, each as its own commit: (1) AGENTS.md QA checklist additions: check 6 tests for a valid role code, not just non-empty (a strengthening); date and version format checks on every register; `tools/figure_check.py` as a spot-check screen; selection-log, people-register and method-link foreign keys; "no claim points at an absent method or evidence at an absent claim"; (2) the stale-artefact rule lists `iain_question_sheet.md`, `method_views/statements.md` and `selection_views/` as derived files and `tests/` as the place for fixture tests; (3) a rule that method statements are set CURRENT only by Iain and carry a disclosure status; (4) the codebook v1.4 release approving `SUPERSEDED`, `statement_id` and `method_family_rollup`; (5) register `codebook_version` labels moved from 1.3-candidate; (6) the sweep write rule, now written into `tools/README_sweep.md` and `tools/JON_SWEEP_GUIDE.md` (a sweep writes only `sweep_reports/` and its state file; a register is never saved whole; Drive and repo copies are compared before any copy), still to be lifted into AGENTS.md after the Drive and repo merge; (7) QA item 14 is already in AGENTS.md; add "no claim names an absent method" (now true: 0) and "no stored tier or score" beside it. None of these weakens an existing test.

## 16. Final pass (26/10/08): does it work?

Re-run against the registers as they stand. **Working:** all registers have unique IDs; claims, sources, evidence and measurements foreign keys resolve (two claims, C-R3-036 and C-R3-037, still have no project, VAL-S261007-14); no OPTION claim lacks an option state; no claim lacks an effect family or role; every EFFECT claim has an attribution strength; every claim with a pound figure has a value basis; no DESIGN claim on a not-awarded project is unexpired; the unit test for E4 passes; `eligibility_report.py` (70 projects), `selection_view.py --requirements T22-VAIMP` (11 candidates, default alphabetical plus the trial order), `method_view.py` (three statements, coverage of 8 buyer questions), `people_view.py`, `question_sheet.py`, `figure_check.py` (288 of 595 claims fully matched, 24 with unmatched figures, 4 citing sources with no extract) and `check_claims_columns.py` (26 violations, exactly the held cells) all run. Differences from the checklist: the QA scan found two defects the earlier checks missed: 20 claims naming absent methods (fixed, VAL-S261008-18) and 163 claim-to-method links missing from the method rows' own claim lists (fixed, VAL-S261008-19).

**Not yet working or untested:** (a) a method statement for a non-evaluation shape (dashboard or framework build) still returns "no evidence" (section 11); (b) only five of 23 tenders have requirement wording; (c) `13_selections.csv` has no rows because no selection has been made; (d) the Drive and repo copies of the registers have diverged (section 17); (e) client acceptance rests on Iain's statements, with no client document checked for the 31 recorded today; (f) the batch-code writer that displaced values in the claims file has not been traced.

**Adoption:** nothing in this draft needs more building before Iain decides. Adoption stays Iain's call; items in section 15 follow as separate commits.

## 17. Two copies of the registers (finding 26/10/08, for the Drive merge)

The Drive folder is the working canonical (`register_update_workflow.md`) and this repo is the versioned mirror, but this branch was edited directly. On 26/10/08 the Drive `01_projects.csv` had five projects the repo lacks (P91-WBSKILLS, P92-BAY, P93-WOW, P95-LIVCS30, P96-LIVDI), a payment-status column under the name `client_accepted`, corrected P51 details and P31-PRODPARK on hold; the Drive `04_claims.csv` was the pre-restore copy (239,822 bytes against 444,844 in the repo). The merge is handed to an agent that can work in Drive (`drive_merge_BRIEF.md`). No ontology rule depends on which copy wins, but the merged result must keep `client_accepted` as Y/N/UNKNOWN with payment status in its own column.
