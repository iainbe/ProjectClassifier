# R2 Neutral Source Packets — Coding Instructions

**Date:** 26/09/09
**Codebook version:** v1.1 (candidate)
**Review batch:** R2

## Overview

This file defines the 12 atomic claim units and 2 opportunity packets for R2 bounded validation. Each packet contains:
- A neutral question (no expected labels)
- The source file(s) to read
- The specific sections/scope to code
- Prior exposure disclosure

## Coding protocol

1. **Iain codes first and locks.** Iain records initial labels privately, confirms lock to Devin (date/time only, no labels revealed).
2. **Devin codes without seeing Iain's labels.** Devin records dated INITIAL_CODE rows.
3. **Iain submits locked labels.** Both sets compared.
4. **Adjudicate disagreements.** Iain decides disposition with rationale.
5. **Record in 10_review_history.csv.**

## 12 Atomic Claim Units

### R2-D01 (P01-NES) — Baseline economic scale from two differently dated reports
- **Question:** What claim about baseline economic scale can be made from two differently dated reports, and what version authority remains unresolved? Restrict to title/date, scope, headline numbers and corresponding methodology qualifiers.
- **Sources:** SRC-R2-01 (Pinning Stones FINAL, Apr 20), SRC-R2-02 (NES Creative Industries Report, May 8)
- **Scope:** Title/date, scope, headline numbers, methodology qualifiers
- **Prior exposure:** Conflicting numbers already discussed
- **Files:** `extracted_text/SRC-R2-01_v1_full.txt`, `extracted_text/SRC-R2-02_v1_full.txt`

### R2-D02 (P02-FGTG) — Workshop planning vs actual delivery
- **Question:** What does the dated update establish about workshop planning versus actual delivery? Do not determine the later programme outcome from this update alone.
- **Source:** SRC-R2-03 (FG2G Update, Nov 6)
- **Scope:** Entire update
- **Prior exposure:** Transcript partially read earlier
- **File:** `extracted_text/SRC-R2-03_v1_full.txt`

### R2-D03 (P03-MITIH) — Investment-sequence appendix
- **Question:** What does the investment-sequence appendix establish about proposed future choices, their holder and their exercise?
- **Source:** SRC-R2-04 (MITIH Oct 24 report)
- **Scope:** Appendix
- **Prior exposure:** Appendix already discussed
- **File:** `extracted_text/SRC-R2-04_v1_full.txt`

### R2-D04 (P03-MITIH) — Bridging organisations and network structure
- **Question:** What does the report's bridging-organisations discussion establish about existing network structure versus changed ties attributable to an intervention?
- **Source:** SRC-R2-04 (MITIH Oct 24 report)
- **Scope:** Section 4
- **Prior exposure:** Section already discussed
- **File:** `extracted_text/SRC-R2-04_v1_full.txt`

### R2-D05 (P04-GBSLEP) — Intermediaries and knowledge transfer
- **Question:** What does the account of intermediaries/knowledge transfer establish about effects investigated and Fifth Sector/Bennett's role in them?
- **Source:** SRC-R2-05 (GBSLEP report, 17/12)
- **Scope:** Executive-summary cultural organisations/intermediaries subsections
- **Prior exposure:** Passage already discussed
- **File:** `extracted_text/SRC-R2-05_v1_full.txt`

### R2-D06 (P05-WMCA) — Document type behind a filename containing "final"
- **Question:** What evidence of method proposal/application is provided by the actual document type behind a filename containing "final"?
- **Source:** SRC-R2-06 (WMCA final report PDF, 20/01/09) — CORRECTED from client quotation response
- **Scope:** Cover/quotation and methodology section
- **Prior exposure:** Document-type error already discussed
- **File:** `extracted_text/SRC-R2-06_v1_full.txt`
- **Note:** The original R2 source was a client-authored quotation response (190730 final.docx). The corrected source is the 20/01/09 final report PDF (BOP Consulting deliverable). This correction is itself part of the diagnostic — the filename "final" on the original source was misleading.

### R2-D07 (P06-COSTAR) — Bid-support work and funding outcome
- **Question:** What can this Manchester case-for-support establish about bid-support work and the funding outcome of that particular consortium?
- **Source:** SRC-R2-07 (CoSTAR Case ad Delivery, 23/01/30)
- **Scope:** Cover, strategic fit and theory of change
- **Prior exposure:** National/local conflation already discussed
- **File:** `extracted_text/SRC-R2-07_v1_full.txt`
- **Note:** Bid was NOT successful (confirmed by Iain 26/09/09). The 25/10 consortium plan is for a different/revived consortium.

### R2-D08 (P02-FGTG) — Post-workshop effects test
- **Question:** Does this reviewed update contain an actual specified test of post-workshop effects, and what conclusion is permissible if the relevant follow-up evidence is outside this packet?
- **Source:** SRC-R2-03 (FG2G Update, Nov 6)
- **Scope:** Entire update
- **Prior exposure:** Missing-versus-null error already discussed
- **File:** `extracted_text/SRC-R2-03_v1_full.txt`

### R2-T01 (P07-CC) — Atomic method/output/design proposition
- **Question:** Identify one atomic method/output/design proposition and assess what the inception document supports; preserve commission/programme distinction.
- **Source:** SRC-R2-08 (Creative City inception, 20/09/14)
- **Scope:** Entire short inception note
- **Prior exposure:** Source appeared in previous pilot; prior labels excluded from new packet
- **File:** `extracted_text/SRC-R2-08_v1_full.txt`
- **Note:** SIPF application NOT successful (confirmed by Iain 26/09/09). Project did not proceed beyond inception.

### R2-T02 (P08-LIVDCI) — Method reuse/role and proposal vs delivery
- **Question:** Identify one atomic proposition about method reuse/role, and separate what the supplier proposal reports from independently verified delivery.
- **Sources:** SRC-R2-09 (proposal, 24/01/05), SRC-R2-09B (final report, 24/07/08)
- **Scope:** Proposal: experience and methodology sections only. Final report: full for context.
- **Prior exposure:** Proposal partially read in prior pilot
- **Files:** `extracted_text/SRC-R2-09_v1_full.txt`, `extracted_text/SRC-R2-09B_v1_full.txt`
- **Note:** Final report accepted by client (confirmed by Iain 26/09/09). This is a proposal-vs-delivery test.

### R2-T03 (P09-CDEC) — Atomic proposed cross-sector mechanism
- **Question:** Identify one atomic proposed cross-sector mechanism; state what would disconfirm it and what occurrence evidence this draft supplies.
- **Source:** SRC-R2-10 (CDEC challenges paper V2 draft, 12/04/24)
- **Scope:** Introduction, convergence and recommendations
- **Prior exposure:** Draft read in prior pilot
- **File:** `extracted_text/SRC-R2-10_v1_full.txt`
- **Note:** Challenges paper was finalised (confirmed by Iain 26/09/09). Fifth Sector had advisory/consultative role. Oldest project in pilot (2012).

### R2-T04 (P10-KIRK) — Monetary baseline proposition
- **Question:** Identify one atomic monetary baseline proposition and distinguish amount, basis, review and intervention attribution.
- **Source:** SRC-R2-11 (Kirklees 2024 final, 24/09/23) — CORRECTED from Jul 18 version
- **Scope:** Executive summary and economic-impact methodology only
- **Prior exposure:** Headline discussed; prior AI summary exists
- **File:** `extracted_text/SRC-R2-11_v1_full.txt`
- **Note:** 2022 and 2024 reports accepted (confirmed by Iain 26/09/09). 2026 report in progress. P10-KIRK is a three-report method evolution case study.

## 2 Opportunity Packets

### R2-O01 / T04-LCRFILM — Buyer-owned staging and conflicting dates
- **Purpose:** Buyer-owned staging; real criteria; conflicting dates; missing attached requirements
- **Source:** SRC-R2-12 (LCR Screen Sector Research ITQ)
- **Scope:** Entire ITQ and existing derived extract only
- **Result to produce:** Requirement map, explicit missingness/contradictions, gate profile and as-at test decision. No explanation of historical loss.
- **File:** `extracted_text/SRC-R2-12_v1_full.txt`
- **Note:** A stated "attached technical brief" or contract may be needed for definitive compliance. Log the gap and HOLD; seek a named addition rather than crawl the folder.

### R2-O02 / T01-BCAT — Explicit analytical requirements and contract unknowns
- **Purpose:** Explicit analytical requirements; clarification hierarchy; mandatory capability and contract unknowns
- **Sources:** SRC-R2-13 (RFP), SRC-R2-14 (Clarifications), SRC-R2-15 (Annex1 Agreement draft)
- **Scope:** Full RFP; clarifications with sheet/cell identifiers; draft agreement terms
- **Result to produce:** Buyer-source map and HOLD/other decision justified by the documents; do not use the old approach summary as a proxy for buyer wording or verified supplier capability.
- **Files:** `extracted_text/SRC-R2-13_v1_full.txt`, `extracted_text/SRC-R2-14_v1_full_sheets.csv`, `extracted_text/SRC-R2-15_v1_full.txt`

## Key coding fields

For each unit, code:
- `claim_type` — contextual/baseline finding, method application/delivered output, recommendation/design, client decision use, intervention effect
- `effect_family` — DIRECT / PRODUCT / KNOWLEDGE / NETWORK / OPTION / OTHER / N/A
- `method_status` — NOT_IDENTIFIED / PROPOSED / APPLIED / CORROBORATED / UNKNOWN
- `evidence_status` — NOT_ASSESSED / HYPOTHESIS / REPORTED / CORROBORATED / CONTRADICTED / NOT_DETECTED
- `timing` — forecast, bid status, lifecycle
- `analytical_role` — designer, deliverer, evaluator, advisor, interpreter
- `contracting_role` — prime, subcontractor, associate, partner, unknown
- `attribution_strength` — contribution, causal estimate, distinctiveness only
- `value_status` / `value_basis` / `value_review`
- `permission_status` — not requested/unknown, request sent/pending, approved, prohibited
- `option_state` / `option_subtype` — where relevant
- `tie_change` — new, reactivated, strengthened, pre-existing — where relevant

## Rules to check

- No context mislabelled as created impact
- No proposals mislabelled as delivered programmes
- No costs labelled as benefits
- No monetary values labelled non-monetary
- No missing evidence labelled NULL
- No unverified rights
- No outcomes dated before exposure
- No unsupported causal escalation
- No unknown procurement gates yielding BID
- No incorrect precedent links
