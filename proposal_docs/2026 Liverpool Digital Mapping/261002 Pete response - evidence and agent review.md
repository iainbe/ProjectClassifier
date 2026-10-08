# Pete response: evidence and agent review

Internal review, 2 October 2026. Accompanies the revised jobs-and-growth brief and covering response. Do not send this audit note as the opening communication to Pete.

## Decision and frozen recommendation

Recommend one bounded initial proposition study, building on the supplied baseline: decision-relevant evidence reconciliation; jobs/business trajectories; up to two commercial pathways; and a scenario-informed proposition. Carry jobs and growth in the headline, resilience within the outcomes, and confirm the decision with Pete and Simon.

The buyer-facing brief is a proposed scope. It has not been accepted, priced or sent. Its 30-38 specialist-day allowance is a fresh planning estimate for the deliberately narrower scope: 6-8 + 8-10 + 10-12 + 6-8 days. It includes up to six focused external discussions and two CA sessions, rather than the extensive workforce interviews, case programmes and comparator studies in the earlier option papers.

At the earlier papers' illustrative GBP 800/day, that would be GBP 24,000-30,400 in fees before VAT, external data and expenses. This arithmetic is an internal sensitivity, not an agreed rate or quotation. Do not publish a GBP 20,000-30,000 price range or imply the complete options programme fits that amount. Check actual staff capacity, access, evidence depth and source charges before a fixed price.

The useful compromise is an evidence-backed initial proposition, rather than a comprehensive economic study, certified population audit, regional causal evaluation or full ten-year strategy. If Pete needs one of those deeper results, re-scope and cost it.

## Sources now available

- The original ITT and 18 September working brief, previously read in full.
- The 1 October internal meeting transcript, supplied in the conversation.
- `261002 Digital & Tech ITT (1) .md`, the actual 2 October call with Peter Woodbridge, read in full. Material statements: existing defence/health work at 9:29; proposed staged brief and possible extra budget at 12:43-13:03; broad AI adoption outside this commission at 16:46.
- The user's later pasted internal transcript. Relevant discussion includes the jobs/growth framing at 14:01-17:59; hidden capability and postcode questions at 19:46-24:51; exploratory provider comparisons; investment-field exploration; and the proposed longitudinal contribution at 1:23:11. Gaming audio, remuneration, personal comments and unrelated infrastructure work are excluded.
- The analytical report, Draft 1.3, September 2026. Targeted review of the overview, contents, definition/method, demand section, scenario section 25, Annex A, hidden-capability annex and figure register. This was not a line-by-line audit of the entire long report or independent verification of every cited source.
- All three supplied CSVs, inspected for schema, row counts, relevant coverage, identifiers and examples.
- Downloads papers `00_READ_THIS_FIRST.md` through `07_DRAFT_RESPONSE_TO_PETE.md`, read as prior draft advice. Their estimates and reported findings were not treated as independently verified facts.
- The two dated Data City Explore ZIP exports and selected-company analysis ZIP in Downloads. CSV schemas, company identities, investment fields, selected filters and relevant record counts were inspected locally. No live API or production database was queried.

No source CSV, provider export, original ITT or report has been changed.

## CSV checks: what the files actually support

### Cluster file

`LCR-DT-cluster-database-2026-09.csv` contains 1,934 data rows and 68 columns. There are 1,933 nonblank distinct company numbers. The `member=True` filter selects 670 rows: 563 labelled core and 107 partial.

Those 670 rows carry 642 distinct `enterprise_key` values and 28 `enterprise_dup=True` flags. This establishes a distinction between membership rows and the file's enterprise grouping, rather than a validated independent count of local businesses. Resolve the aggregation rule before summing jobs or treating company and enterprise counts as interchangeable.

Postcodes are populated in 1,757 of all rows and 576 of the 670 member rows. The transcript's impression that most cluster records lack postcodes is not supported by this file. The schema has no latitude/longitude fields. Nonblank postcodes do not prove correct operating locations; the file separately records presence and a current Companies House postcode.

The member rows include 567 `hq_lcr`, 99 `function_lcr` and four `unknown` presence values. Latest filed-employee values are populated for 344 member rows. These are coverage counts, not local jobs totals or verification of the presence classifications.

### AI file

`LCR-AI-businesses-2026-09.csv` contains 249 rows, 53 columns and 249 distinct company numbers. Its own labels identify 143 counted AI companies, 92 AI services and 14 early-stage tracked records. Latest accounts employee values are populated for 104 rows.

The CSV's 249/143 differs from the report figure register's 246/134. This needs a dated-cohort reconciliation; it does not prove that either whole source is unusable.

Seventeen rows with a populated latest-accounts employee value record at least ten employees. That cannot be compared directly with the transcript's provider result of twenty firms: the provider uses a different population, estimates and filters. Missing filed values and reported zeros do not establish that most remaining businesses are single-person firms.

All 249 `Live job ads (LCR)` cells contain zero. Treat this as the file's recorded output, pending confirmation of collection, timing and missing-data rules. It is not proof of no hiring demand.

### Hidden-capability register

`hidden-capability-register-2026-09.csv` contains 67 rows and 15 columns, with 67 distinct organisation names. It mixes public bodies, established employers, research-related capability and different team/project evidence. It is a case-selection resource, rather than a measured total of purchasers, technology employees or local demand.

`site_employment` contains whole-time-equivalent figures, headcounts, group/site descriptions, different years and unknowns. `figures` also contains project spending and grant values. None should be summed into one jobs or demand total.

The HMRC row has `site_employment="Not found (about 3"` and `flag="500 planned in 2017)"`, indicating a semantic field split that needs source-level repair. All rows have the header's 15 fields, so this is not a simple row-width failure. Keep the originals and repair in a separately versioned derivative only after checking the intended meaning.

The register's "not found" labels reflect search coverage. They do not establish absence of capability or local suppliers.

## Data City exports: useful evidence, with a different claim ceiling

The `14h47m22s` Explore export has 614 company-year rows but 233 distinct company numbers. All 233 occur in the supplied 249-row AI register. This supports the transcript's 233-match observation, not a conclusion that the other 16 companies are false or absent.

Its metadata applies active-status, subsidiary-removal and distinct-brand filters. Establish how each exclusion and aggregation works before attributing the difference to errors in Pete's classification.

The same export contains 57 investment-round records. The `15h00m08s` export contains 5,048 company-year rows for 1,122 distinct companies, and 1,169 investment-round records. Its metadata uses selected RTICs and ITL2 regions rather than the same company-number list. It is not a like-for-like LCR cohort comparison.

Both exports include `InvestmentRounds.csv` with company, round date, type, investor and amount fields. All inspected records have `RoundVerified=false`; ask the provider what that flag means. Zero amounts, missing investor details and multiple records require a careful interpretation. These fields show that an investment-data route exists in the supplied exports, rather than establishing complete or verified local investment coverage.

Company-year rows repeat current estimates across financial years. Do not sum current headcount, turnover or GVA across every row. Location tables include operating/registered-address flags and provider-estimated location measures; their allocation method and permissions need checking.

No deal totals, local jobs totals or employment effects have been computed here. Director/contact data are unnecessary for this response and are not published.

## Scenario check

Section 25, printed pages 263-268, names Drift, Conversion and Fusion. Conversion assumes delivery of the initial action blocks; Fusion adds successful commercial pathways at scale. The report expressly calls these indicative arithmetic, not forecasts.

Use them as cases whose assumptions can be examined. They are not causal counterfactuals or promises of policy additionality. The report mixes a changing filed-company population with Section J economic context and revised vintages; those bases need reconciling before numerical stress tests.

The Fusion narrative on printed page 266 links one or two firms at 150-250 staff to 1,000-2,000 additional jobs including suppliers. The wider jobs mechanism and multiplier assumptions need evidence; they cannot be accepted merely because the arithmetic is presented.

The initial study can identify the assumptions and decision consequences. It does not promise a calibrated ten-year forecast or econometric estimate of an intervention.

## Changes made to the response

- Acknowledge the underlying files already supplied; remove the request to see files we now hold.
- Replace the menu of alternative research programmes with one bounded sequence and a clear jobs/growth question.
- Explain that metadata enrichment and reconciliation enable trajectory and opportunity work, while preserving Pete's initial research.
- Add commercial and social value, wider-market routes and resilience without assuming contraction or guaranteed local demand.
- Make the approved Data City API/licence route a condition, rather than treating a client key as automatic permission.
- Stop claiming that investment data are simply unavailable; distinguish possible source fields from a complete investment study.
- Reuse existing defence/health work and preserve Pete's AI-adoption exclusion.
- Avoid carrying the historical GBP 20,000 mapping figure, an unsupported full-ITT figure or all option-paper fees into a new quote.

## Agent receipts

All 13 local definitions were considered, with Blindspot and Deepthink applied. These are bounded analytical perspectives on a common evidence set, rather than independent organisational certification.

- SARK / Load the team: selected evidence, weak-signal, feasibility, scope, buyer-fit and delivery reviews; separated internal audit from buyer-facing copy. No external send, contract, dataset mutation or live query is authorised.
- Jonbot: supplied an actionable current response and new commissioning brief; accepted the changed evidence rather than repeating the historical mapping offer.
- THAD: PASS for issuing the documents as clearly qualified discussion drafts. BLOCK - PROOF FAILURE for claiming a validated regional baseline, causal jobs effect or investment-ready intervention. Recovery: agreed outcomes, source/rights gate and bounded case work; re-review before a quotation or commission.
- SHELDON: supplied files, schemas and export fields EXISTS. Runtime pipeline, live API parity, complete history and current permission UNKNOWN. Counts above prove file contents only; transcript reports about successful matching or deployment are not runtime evidence.
- WISHFUL: FEASIBLE IN STAGES. Preferred route: targeted evidence reuse alongside the bounded jobs/opportunity study. Fallback: a narrower decision note if access fails. Expanded fieldwork, complete reconstruction or investment research are separately costed routes, rather than automatic additions.
- GREY: strongest reading is useful initial evidence plus plausible cross-sector opportunity. Alternatives include interchangeable external supply, successful existing relationships needing no new intermediary, and job growth outside the resident population. Examine both ends of selected relationships and negative cases.
- FoK: retained identity, enterprise, geography, time and claim-state distinctions. CSV/export checks establish a source route; they do not admit records into a live Places universe or prove an economic finding.
- MrU: any future digital scope and reconciliation must use the normal governed lifecycle without overwriting the creative source or an accepted snapshot. No build, currentness audit or publication occurred.
- PIGPEN: retained supplied sources and option papers; updated the requested covering draft; placed current brief/review beside the Liverpool materials and marked the older meeting note historical. Formatting intermediates remain temporary.
- SKiN: document concept only; no new Liverpool deck or live interaction test. Lead with the decision, outputs and evidence chain. The reported changes in provider UX are not a measured usability finding here.
- SHAZ: scope six focused partner discussions rather than indefinite respondent labour; explain requested evidence, confidentiality and correction. No supplied questionnaire supports a completion-time claim.
- Place skills research: keep occupational, company/site, vacancy and resident measures distinct. No individual workforce tracking, taxonomy experiment or freelancer model has been conducted.
- Blindspot: commissioner, employer, procurement, data-provider, funder and rival lenses. Main risks are renewed scope expansion, raw/provider counts as local truth, assumed demand, unpaid reconstruction and licensing gaps. The narrower brief makes each an explicit decision or exclusion.
- Deepthink: checked report definitions/scenarios against source rows and provider filters. Evidence supports a substantial starting point; postcode absence and simple "no investment data" claims do not survive inspection. Local job totals, regional uniqueness and causal outcomes remain unproven.

## Frozen source identities

CSV SHA-256 identifiers for the inspected snapshot:

- Cluster: `b06448fa5cb6025c2807d178d4a9a054622c498b98b914615a1aae698e58fc98`
- AI: `a3c4c5aa3001f76c8e4c99cbd332899f313ea522ad224c7a5ca7320084ba54ac`
- Hidden capability: `b284cfcba9a811d71c06c33f4f5c65843348e599b03fc76ee87b5ea826143406`

Counts and examples were derived directly from these local snapshots by the lead reviewer using Python's CSV parser. Provider ZIP checks used their embedded CSVs and metadata, with company numbers compared as uppercase strings and numeric-only IDs padded to eight characters. No spreadsheet totals were treated as regional metrics.

Residual limits: no execution scripts or full source ledger supplied; no verification of the websites/filings behind every record; no fieldwork; no full PDF source audit; no live permissions or API check. The record supports the new discussion scope, while leaving contract and empirical validation gates explicit.
