# R2 Unit-by-Unit Walkthrough for Independent Coding

**Date:** 2026-09-09
**Purpose:** Clarify each of the 14 R2 units before Iain's independent coding pass.

---

## Diagnostic Units (D01–D08)

These target known defects from the prior audit. Each tests whether the repaired codebook and rules correctly classify a specific type of error.

---

### R2-D01 (P01-NES) — Baseline economic scale from two differently dated reports

**Question:** What claim about baseline economic scale can be made from two differently dated reports, and what version authority remains unresolved?

**Sources:**
- SRC-R2-01: "From Pinning Stones to Convergence Economy" (Apr 20, 2026) — 988 lines, 233KB
- SRC-R2-02: "Mapping of Creative Industries in Aberdeen and Aberdeenshire" (May 8, 2026) — 743 lines, 134KB

**What's in the sources:**
- Both reports cover the same commission (NES creative industries mapping for Aberdeen City Council).
- SRC-R2-01 (Apr 20) states: 10,700+ workers, £582M direct GVA, £894M total impact. With convergence: 12,000 workers, £732M GVA, £1.1B total impact.
- SRC-R2-02 (May 8) states: 10,490 workers, 7,715 FTE, £453M direct GVA, £675M total impact. It explicitly says: "It does not yet prove that these communities are already selling into the same markets."
- The numbers differ significantly between the two reports. SRC-R2-01 has higher figures and a stronger convergence claim. SRC-R2-02 is more cautious.
- The canonical version is v3.12 (in canonical/P01-NES/), but the R2 test uses both dated versions to test version/baseline distinction.

**What to code:**
- `claim_type`: Is this a contextual/baseline finding, a method application, or a recommendation?
- `effect_family`: Is a GVA figure a DIRECT effect, or is it contextual baseline?
- `method_status`: What method was APPLIED (four-tier workforce modelling, LinkedIn profiling, BRES/IDBR analysis)?
- `evidence_status`: Is the £582M REPORTED, or HYPOTHESIS? Is the convergence claim (£1.1B) a forecast or a finding?
- `version authority`: Which report's numbers are canonical? What happens when two dated reports disagree?

**Key defect being tested:** The prior audit found conflicting headline numbers discussed without version authority resolution. The codebook must distinguish baseline scale (context) from created impact (effect), and must not treat a higher number in an earlier draft as the canonical finding.

---

### R2-D02 (P02-FGTG) — Workshop planning vs actual delivery

**Question:** What does the dated update establish about workshop planning versus actual delivery? Do not determine the later programme outcome from this update alone.

**Source:** SRC-R2-03: "FG2G Update" (Nov 6, 2024) — 374 lines, 35KB

**What's in the source:**
- This is a Teams meeting transcript (39 mins), not a report.
- Steve Hillier (Manchester Met) is briefing Iain and Lynne on plans for a December workshop.
- The workshop is being planned — it has not yet happened. Dates, agenda, speakers, and attendee list are all proposed, not delivered.
- The update discusses: workshop briefing note, agenda, target audience (50/50 businesses vs support orgs), GM strategic context, Innovate UK funding landscape.
- Key quote: "We have four weeks... that's enough time probably to get the right number of companies and delegates in the room."
- There is no evidence in this document that the workshop occurred, who attended, or what outcomes resulted.

**What to code:**
- `claim_type`: Is this a method application/delivered output, or a recommendation/design? (It's a planning document, not a delivery record.)
- `method_status`: PROPOSED (workshop is planned, not delivered).
- `evidence_status`: The workshop's existence is HYPOTHESIS (proposed), not REPORTED (delivered).
- `effect_family`: N/A — no effects to classify from a planning document.
- `attribution`: Cannot attribute any intervention effect from a planning meeting.

**Key defect being tested:** The prior audit treated workshop planning as if it established delivery. The codebook must distinguish "we planned a workshop" from "we delivered a workshop and measured its effects."

---

### R2-D03 (P03-MITIH) — Investment-sequence appendix

**Question:** What does the investment-sequence appendix establish about proposed future choices, their holder and their exercise?

**Source:** SRC-R2-04: "MITIH Createch Ecosystem Report" (Oct 24, 2025) — 151 lines, 27KB

**What's in the source:**
- The report has an appendix titled "Critical questions requiring market validation" and a "Recommended investment sequence."
- The investment sequence is explicitly gated:
  - Immediate Action (3-4 months): Commission a demand validation study. Decision: "Clear proceed/pause/pivot recommendation with explicit criteria."
  - Conditional Phase 1 (12-18 months): SME stabilisation, shared infrastructure, model replication — only if validation confirms favourable conditions.
  - Conditional Phase 2 (36-48 months): Training expansion — only after Phase 1 outcomes.
- The holder of the options is not Fifth Sector — it's the funder/commissioner (Salford City Council / GMCA / UKRI).
- The options are explicitly conditional on market validation results that have not yet been obtained.

**What to code:**
- `claim_type`: This is a recommendation/design, not a delivered output.
- `effect_family`: OPTION — but is the option held by Fifth Sector or by the commissioner?
- `option_state`: PROPOSED (the investment sequence is proposed, not created). The option to proceed to Phase 2 is contingent on Phase 1 results.
- `method_status`: PROPOSED — the report proposes a method, it does not report its application.
- `evidence_status`: HYPOTHESIS — the market validation has not been conducted.
- `attribution`: Fifth Sector designed the sequence; the commissioner holds the option to exercise it.

**Key defect being tested:** The prior audit conflated proposed options with exercised options. The codebook must identify the holder, the gating condition, and whether the option has been exercised.

---

### R2-D04 (P03-MITIH) — Bridging organisations and network structure

**Question:** What does the report's bridging-organisations discussion establish about existing network structure versus changed ties attributable to an intervention?

**Source:** SRC-R2-04, Section 4: "Essential stabilising organisations are systematically underfunded" (lines 87-106)

**What's in the source:**
- The report identifies microbusinesses and SMEs as "bridging" organisations in the network.
- It states: "Social network analysis confirms the strategic position occupied by microbusinesses and SMEs within the rapidly evolving ecosystem."
- These organisations "show bridging characteristics, connecting nodes across the network, rather than dominance in any one market vertical."
- The report documents one organisation that "recently enabled a three-way immersive prototype between education, wellness, and animation without any formal funding route."
- The report recommends a "dedicated funding stream" for these organisations — this is a recommendation, not a delivered intervention.

**What to code:**
- `claim_type`: Is this a method application (social network analysis was applied) or a recommendation (fund these organisations)?
- `effect_family`: NETWORK — but is the network structure pre-existing or changed by an intervention?
- `tie_change`: The report describes existing bridging characteristics, not new ties created by an intervention. The SNA maps existing structure.
- `method_status`: APPLIED — social network analysis was conducted.
- `evidence_status`: REPORTED — the bridging characteristics are reported from SNA. But the "three-way immersive prototype" is a single reported instance, not a systematic measurement.
- `attribution`: Fifth Sector identified the bridging role; it did not create the bridging organisations or their network positions.

**Key defect being tested:** The prior audit treated existing network centrality as if it were a spillover created by Fifth Sector's intervention. The codebook must distinguish "we observed bridging" from "we caused bridging."

---

### R2-D05 (P04-GBSLEP) — Intermediaries and knowledge transfer

**Question:** What does the account of intermediaries/knowledge transfer establish about effects investigated and Fifth Sector/Bennett's role in them?

**Source:** SRC-R2-05: "GBSLEP Creative Economy report" (Dec 2017) — 2009 lines, 209KB

**Scope:** Executive summary, cultural organisations/intermediaries subsections.

**What's in the source:**
- The report is a mapping study of creative industries in Greater Birmingham & Solihull.
- BOP Consulting is the prime; Iain Bennett (Fifth Sector) was an associate/subcontractor.
- The report maps intermediaries, cultural organisations, and knowledge transfer mechanisms.
- It identifies the role of intermediaries in the creative ecosystem.
- The report is a mapping/contextual study — it documents what exists, not what was changed by an intervention.

**What to code:**
- `claim_type`: Contextual/baseline finding (mapping what exists).
- `effect_family`: KNOWLEDGE (knowledge transfer is discussed) — but is it a spillover or a description of existing patterns?
- `method_status`: APPLIED (mapping methodology was applied).
- `evidence_status`: REPORTED (intermediaries and knowledge transfer patterns are reported from the mapping).
- `analytical_role`: Fifth Sector/Bennett was ADVISOR/INTERPRETER (as BOP associate), not prime.
- `contracting_role`: SUBCONTRACTOR (BOP was prime).
- `attribution`: Fifth Sector contributed to the analysis; it did not create the knowledge transfer patterns it documents.

**Key defect being tested:** The prior audit did not distinguish Fifth Sector's role as subcontractor/associate from BOP's role as prime. The codebook must separate analytical contribution from contracting role, and must not attribute the mapped effects to Fifth Sector.

---

### R2-D06 (P05-WMCA) — Document type behind a filename containing "final"

**Question:** What evidence of method proposal/application is provided by the actual document type behind a filename containing "final"?

**Source:** SRC-R2-06: "WMCA Creative Business scale-up final report" (Jan 9, 2020 PDF) — 657 lines, 31KB

**What's in the source:**
- The corrected source is the Jan 9, 2020 PDF — the actual final report by BOP Consulting (with Curator Technologies).
- The credits page lists: "Iain Bennett, BOP Consulting; Simon Sprince and Andy Goodwin, Curator Technologies."
- The report covers: mapping creative businesses, Common Application Gateway criteria, scale-up scores, correlation analysis, creative supply chain groupings.
- It's a 17-page mapping/analysis report — a delivered output, not a proposal.
- The original R2 source (190730 final.docx) was a client-authored quotation response — the filename "final" was misleading.

**What to code:**
- `claim_type`: Method application/delivered output (the mapping was conducted and reported).
- `document_type`: Final report (PDF, BOP deliverable).
- `method_status`: APPLIED (mapping methodology was applied).
- `evidence_status`: REPORTED (scale-up scores and business counts are reported from the mapping).
- `analytical_role`: Iain Bennett was ADVISOR/INTERPRETER (as BOP associate).
- `contracting_role`: SUBCONTRACTOR (BOP was prime, confirmed by Iain).
- `attribution`: The report is BOP's deliverable. Fifth Sector's specific contribution is not separable from the report alone.

**Key defect being tested:** The prior audit treated a client-authored quotation response as the final report because the filename contained "final." The codebook must register actual document type, not infer it from filenames. This unit also tests whether the correction (using the actual final report PDF) produces a different classification.

---

### R2-D07 (P06-COSTAR) — Bid-support work and funding outcome

**Question:** What can this Manchester case-for-support establish about bid-support work and the funding outcome of that particular consortium?

**Source:** SRC-R2-07: "CoSTAR Case ad Delivery" (Jan 30, 2023) — 317 lines, 36KB

**What's in the source:**
- This is a bid-support document (Case for Support) for the CoSTAR consortium.
- The consortium includes: GMCA, SODA, Factory International, Magnopus, AND, FutureEverything, dock10.
- The document describes: strategic fit, virtual production capabilities, theory of change, innovation agenda.
- It proposes upgrading dock10's facilities for 3D performance capture, multi-talent motion capture, facial capture, etc.
- The bid was NOT successful (confirmed by Iain 2026-09-09). The Oct 2025 consortium plan is for a different/revived consortium.
- This is a national competition (UKRI CoSTAR), not a local authority mapping project.

**What to code:**
- `claim_type`: Recommendation/design (bid-support document proposing a programme).
- `document_type`: Bid-support / case for support.
- `method_status`: PROPOSED (the programme is proposed, not delivered).
- `evidence_status`: HYPOTHESIS (the capabilities and outcomes are proposed, not realised).
- `effect_family`: OPTION (the bid represents a proposed investment with future choices) — but the option was not created (bid not successful).
- `timing`: The bid status is NOT_SUCCESSFUL.
- `lifecycle`: The commission (bid-support work) was delivered; the programme it supported was not funded.
- `attribution`: Fifth Sector provided bid-support services; it did not deliver the proposed programme.

**Key defect being tested:** The prior audit risked conflating national/local competition and treating bid-support work as if it established programme delivery. The codebook must distinguish "we wrote a case for support" from "the programme was funded and delivered." It must also record the bid outcome (NOT_SUCCESSFUL).

---

### R2-D08 (P02-FGTG) — Post-workshop effects test

**Question:** Does this reviewed update contain an actual specified test of post-workshop effects, and what conclusion is permissible if the relevant follow-up evidence is outside this packet?

**Source:** SRC-R2-03: "FG2G Update" (Nov 6, 2024) — same transcript as D02.

**What's in the source:**
- As with D02, this is a planning transcript. The workshop has not yet occurred.
- There is no test of post-workshop effects because the workshop has not been delivered.
- There is no follow-up evidence in this packet — no attendance data, no participant feedback, no outcome measurement.
- The transcript discusses what the workshop aims to achieve, not what it achieved.

**What to code:**
- `claim_type`: No test is present — this is a planning document.
- `evidence_status`: NOT_DETECTED — no specified test of post-workshop effects exists in this document.
- `effect_family`: N/A — no effects to classify.
- `coverage`: The follow-up evidence is outside this packet. The permissible conclusion is "not established from this source," not "no effects occurred."
- `attribution`: Cannot attribute or deny effects from a planning document.

**Key defect being tested:** The prior audit treated missing evidence as null evidence (no effects found). The codebook must distinguish "we looked and found no test" from "no effects occurred." Missing evidence is NOT_DETECTED with a specified scope, not a null finding.

---

## Transfer Units (T01–T04)

These test rule application without expected labels in the coder packet. Prior exposure is disclosed.

---

### R2-T01 (P07-CC) — Atomic method/output/design proposition

**Question:** Identify one atomic method/output/design proposition and assess what the inception document supports; preserve commission/programme distinction.

**Source:** SRC-R2-08: "Creative City+ SIPF bid support – project inception notes" (Sep 14, 2020) — 37 lines, 2KB

**What's in the source:**
- This is a very short inception note (38 paragraphs, 0 tables) — a scoping/setup document.
- It lists proposed tasks: project inception meeting, review of EOI submission, statistical base/supply chain analysis, business and stakeholder engagement, workshop, options assessment, drafting bid response, appendices.
- It references a Gantt chart with five work packages and five key deliverables.
- The SIPF application was NOT successful (confirmed by Iain 2026-09-09). The project did not proceed beyond inception.
- This is a programme application (SIPF), not a commissioned contract. The commission/programme distinction is critical.

**What to code:**
- `claim_type`: Recommendation/design (proposed tasks for a bid-support project).
- `document_type`: Inception note (scoping document).
- `method_status`: PROPOSED (tasks are proposed, not delivered).
- `evidence_status`: HYPOTHESIS (the inception note proposes work, it does not report results).
- `commission/programme distinction`: This is a SIPF programme application that was not successful. The "commission" is a bid-support inception; the "programme" (SIPF) was not funded.
- `lifecycle`: APPLICATION NOT SUCCESSFUL — project did not proceed.
- `attribution`: Fifth Sector provided inception support; the programme it supported was not funded.

**What this tests:** Can the codebook correctly classify a very short inception note as a proposed design, not a delivered output? Can it preserve the distinction between a bid-support commission and the programme it was supporting?

---

### R2-T02 (P08-LIVDCI) — Method reuse/role and proposal vs delivery

**Question:** Identify one atomic proposition about method reuse/role, and separate what the supplier proposal reports from independently verified delivery.

**Sources:**
- SRC-R2-09: "LCR DCI Cluster mapping" proposal (Jan 5, 2024) — 293 lines, 38KB
- SRC-R2-09B: "LiverpoolCityRegion DigitalCreative final report" (Jul 8, 2024) — 1200 lines, 144KB

**What's in the sources:**
- The proposal (SRC-R2-09) lists extensive prior experience: Herefordshire, Leicester, Calderdale, South Yorkshire, West Sussex, Somerset, Tees Valley, Derby, Rushmoor, Kirklees, Liverpool Film Fund, Liverpool Cultural Strategy, LCR Music Strategy, City of London, London College of Fashion. It proposes an "OODA Loop" methodology (Observe, Orient, Determine, Act).
- The final report (SRC-R2-09B) is a 1200-line, 27-table delivered output covering: executive summary, situation, evidence, challenges (weak demand, image, cluster, skills, EDI, wider economy), findings from mapping (business numbers, digital/creative industries, cultural sectors, workforce, supply chain, clustering, GVA), skills, equality/diversity, local scene.
- The final report was accepted by the client (confirmed by Iain 2026-09-09).
- The proposal claims extensive method reuse; the final report demonstrates the method applied to LCR.

**What to code:**
- `claim_type`: The proposal is a recommendation/design; the final report is a method application/delivered output.
- `method_status`: PROPOSED (in the proposal) vs APPLIED (in the final report).
- `evidence_status`: HYPOTHESIS (in the proposal) vs REPORTED (in the final report).
- `method reuse`: The proposal claims reuse of prior mapping methods. Is this claim verified by the final report's content?
- `contracting_role`: NOT_ESTABLISHED from these sources alone — the proposal implies Fifth Sector is prime, but this needs contract verification.
- `attribution`: The proposal claims Fifth Sector's method; the final report demonstrates delivery. But the proposal's claims about prior projects are self-reported, not independently verified.

**What this tests:** Can the codebook separate what a supplier proposal claims from what the delivered output demonstrates? Can it classify method reuse as a claim (PROPOSED) vs a demonstrated application (APPLIED)?

---

### R2-T03 (P09-CDEC) — Atomic proposed cross-sector mechanism

**Question:** Identify one atomic proposed cross-sector mechanism; state what would disconfirm it and what occurrence evidence this draft supplies.

**Source:** SRC-R2-10: "CDEC challenges paper V2 - draft" (Apr 24, 2012) — 89 lines, 9KB

**What's in the source:**
- The paper proposes that closer collaboration between creative industries and ICT sectors would transform the digital economy.
- The key mechanism: "If sectors representing roughly 5% of GVA (ICT) were pulling together with another 6.4% of GVA [creative industries], the outcome could be truly transformative."
- The paper identifies convergence as the driver: digital technologies disrupting value chains, creating new markets, enabling new business models.
- It proposes that the CDEC (Catapult for the Connected Digital Economy) should foster collaboration across sectors.
- The paper is a draft (V2 - draft) but was finalised (confirmed by Iain 2026-09-09). Fifth Sector had an advisory/consultative role.
- The paper provides no occurrence evidence — it proposes a mechanism, it does not document its operation.

**What to code:**
- `claim_type`: Recommendation/design (proposes a cross-sector mechanism).
- `effect_family`: KNOWLEDGE (cross-sector collaboration) or NETWORK (new ties between ICT and creative sectors).
- `method_status`: PROPOSED (the mechanism is proposed, not applied or tested).
- `evidence_status`: HYPOTHESIS (no occurrence evidence supplied — the paper proposes, it does not document outcomes).
- `disconfirmation`: What would disconfirm the mechanism? If convergence did not create new markets, if collaboration did not generate growth, if value chain disruption led to erosion rather than enrichment.
- `attribution`: Fifth Sector advised on the challenges paper; it did not create the CDEC or its outcomes.

**What this tests:** Can the codebook identify a proposed mechanism, state what would disconfirm it, and correctly classify the absence of occurrence evidence? This is the oldest project (2012) and tests whether the codebook handles legacy advisory work.

---

### R2-T04 (P10-KIRK) — Monetary baseline proposition

**Question:** Identify one atomic monetary baseline proposition and distinguish amount, basis, review and intervention attribution.

**Source:** SRC-R2-11: "Kirklees Creative Industries Mapping 2024 Final report" (Sep 23, 2024) — 809 lines, 80KB

**Scope:** Executive summary and economic-impact methodology only.

**What's in the source:**
- The executive summary states: "We estimated the GVA from Cultural and Creative Industries in Kirklees in 2022 at £250.9 million, an increase of £75m (43%) from 2020."
- The creative workforce exceeded 9,400 people in 2024.
- There were 1,698 active cultural and creative businesses in 2024, an increase of 184 (15%) since 2022.
- The report uses LinkedIn workforce profiling, BRES/IDBR data, and GVA calculation methodology (Appendix 1).
- The GVA figure is a baseline measurement of the sector's economic scale, not an attribution of intervention effect.
- The report was accepted by the client (confirmed by Iain 2026-09-09).

**What to code:**
- `claim_type`: Contextual/baseline finding (GVA measurement).
- `effect_family`: DIRECT (it's a direct economic measurement) — but is it a spillover? No, it's a baseline scale measurement.
- `value_basis`: The £250.9M is a modelled estimate (GVA calculation from workforce data), not a reported amount.
- `value_review`: What review has the £250.9M figure undergone? Is it independently verified?
- `attribution`: The GVA is the sector's economic contribution, not an effect created by Fifth Sector. Fifth Sector measured it; it did not create it.
- `method_status`: APPLIED (mapping and GVA methodology was applied).
- `evidence_status`: REPORTED (the figure is reported from the mapping).

**What this tests:** Can the codebook distinguish a monetary baseline (the sector is worth £250.9M) from an intervention effect (Fifth Sector created £250.9M of value)? Can it classify the value basis (modelled estimate) and review status?

---

## Opportunity Packets (O01–O02)

These test tender requirement capture and gate decisions, not present eligibility or bid authority.

---

### R2-O01 / T04-LCRFILM — Buyer-owned staging and conflicting dates

**Purpose:** Buyer-owned staging; real criteria; conflicting dates; missing attached requirements.

**Source:** SRC-R2-12: "LCR Screen Sector Research Invitation to Quote" (Apr 28, 2026) — 153 lines, 7KB

**What's in the source:**
- Buyer: Liverpool City Council (with LCR Combined Authority funding).
- Project: "Economic Impact Assessment and Phased Strategic Development — Liverpool City Region Screen Industries."
- Phased structure: Phase 1 (Economic Impact Assessment) is commissioned via this ITQ. Subsequent phases (Strategic Plan, stakeholder engagement, dissemination) are potential but not committed.
- Budget: "up to £38,000 (exclusive of VAT) may be available to support this work across all phases."
- Evaluation criteria: Quality and methodological approach (60%), Relevant experience and capacity (20%), Price (20%).
- Key dates: Issue of ITQ May 6, clarification deadline May 15, submission deadline May 29, evaluation week commencing June 8, contract award week commencing June 22, Phase 1 report delivery deadline July 20.
- The ITQ references an "attached technical brief" — this is not in the R2 packet. It's a named missing document.
- Submission format: PDF, max 3 sides A4, max 1,500 words.

**What to produce:**
- Requirement map: What does the buyer explicitly require?
- Missingness/contradictions: The "attached technical brief" is referenced but not in the packet. The £38K budget is "across all phases" but only Phase 1 is commissioned — is £38K for Phase 1 alone or all phases?
- Gate profile: Which gates are PASS, FAIL, UNKNOWN?
- As-at test decision: Based on information available at the decision date, is this BID, HOLD, or NO-BID?
- No explanation of historical loss.

**What this tests:** Can the tender workflow correctly capture buyer requirements from an ITQ, identify missing documents, flag conflicting budget/scope information, and produce a gate profile with HOLD where information is missing?

---

### R2-O02 / T01-BCAT — Explicit analytical requirements and contract unknowns

**Purpose:** Explicit analytical requirements; clarification hierarchy; mandatory capability and contract unknowns.

**Sources:**
- SRC-R2-13: "British Council RFP — UK_1412" (Aug/Sep 2026) — 517 lines, 37KB
- SRC-R2-14: "British Council Clarifications" (Sep 3, 2026) — 994 lines, 221KB (XLSX)
- SRC-R2-15: "British Council Annex1 Agreement" — 493 lines, 93KB (draft agreement)

**What's in the sources:**
- Buyer: British Council.
- Project: "Evaluating the strategic and economic return of international artist-led innovation."
- The RFP seeks "an economist or strategic researcher (or team of) to conduct a mixed-methods analysis that evidences the multi-dimensional economic returns of the international art and technology sector to the UK."
- Contract duration: 1 year with option for up to 2 six-month extensions (max 2 years).
- Contract terms: "By submitting a Proposal, you are agreeing to be bound by the terms of this RFP and the Contract without further negotiation or amendment."
- The clarifications (SRC-R2-14) are an XLSX with question/answer pairs — preserve sheet/cell identifiers.
- The Annex 1 agreement (SRC-R2-15) is a draft agreement — not an executed contract.

**What to produce:**
- Buyer-source map: What does the buyer explicitly require? What are the scored criteria?
- Clarification hierarchy: What was clarified and what remains unknown?
- Mandatory capability: What capabilities are mandatory vs desirable?
- Contract unknowns: What contract terms are unclear or unfavourable?
- HOLD/other decision: Based on the documents, is this BID, HOLD, or NO-BID?
- Do not use the old approach summary as a proxy for buyer wording or verified supplier capability.

**What this tests:** Can the tender workflow correctly capture explicit analytical requirements from an RFP, track clarifications, identify contract unknowns, and produce a justified gate decision? Can it handle a multi-document tender packet (RFP + clarifications + draft agreement)?

---

## Summary

| Unit | Project | Key defect/rule tested | Source type |
|---|---|---|---|
| D01 | NES | Version/baseline distinction; conflicting headline numbers | Two dated reports |
| D02 | FGTG | Workshop planning vs delivery | Meeting transcript |
| D03 | MITIH | Proposed vs exercised option; option holder | Report appendix |
| D04 | MITIH | Existing network vs changed ties | Report section 4 |
| D05 | GBSLEP | Fifth Sector role as subcontractor; intermediaries | Mapping report |
| D06 | WMCA | Document type behind filename "final" | Final report PDF (corrected) |
| D07 | CoSTAR | Bid-support vs programme delivery; bid outcome | Case for support |
| D08 | FGTG | Missing evidence vs null evidence | Meeting transcript |
| T01 | CC | Inception note; commission/programme distinction | Inception note |
| T02 | LIVDCI | Proposal vs delivery; method reuse claims | Proposal + final report |
| T03 | CDEC | Proposed cross-sector mechanism; occurrence evidence | Challenges paper |
| T04 | KIRK | Monetary baseline vs intervention effect | Mapping report |
| O01 | LCRFILM | Buyer requirements; missing brief; budget ambiguity | ITQ |
| O02 | BCAT | RFP requirements; clarifications; contract unknowns | RFP + XLSX + draft agreement |
