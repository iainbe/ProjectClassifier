# Requirements: T22-VAIMP (V&A impact study of the V&A on UK creative industries)

Read by tools/selection_view.py (`--requirements T22-VAIMP`). Lines of the form `key: value` between the two `---` rules, and under each `## item:` heading, are read as data; everything else is for people. This is the operator's reading of the buyer's ask, recorded so a view can be regenerated exactly. Iain to correct. Verbatim wording added 26/10/08 from `01 ITT - Instructions to Tenderers` (VA/CON/F26/33, Sept 2026) and Clarification Questions v1 (issued 06/10/26), both in Drive folder 2026 V&A (id 1LWqUJ9Lb8kOTREFiDT2o67qZhUdIoeAf). The brief (document 02) and the PQQ have not been read by Devin yet.

---
tender_id: T22-VAIMP
buyer: Victoria and Albert Museum (Board of Trustees, NDPB of DCMS)
deadline: 26/10/19 10:00 Europe/London
budget: Fixed fee cap GBP 60,000
decision: BID (Iain, 26/10/07)
scoring: Case studies 20% (scored first); Team 20%; Proposal 50%; Price 10%
kill_gate: score below 6/10 on any criterion excludes, scored sequentially (case studies, team, proposal, price); below 50% on any qualitative criterion rejectable
frozen_on: 26/10/08
source: ITT (VA/CON/F26/33); Clarification Issue 1 (06/10/26); 08_tenders.csv row T22-VAIMP; review lanes run 26/10/08 (tier2_qa_review.md)
format_rule: A4 portrait, font no smaller than 11pt, margins at least 2.5cm; evaluators do not read past a page limit
scoring_key: 0 to 10; 6 = meets the minimum requirement and exceeds it in some areas; 5 = meets the minimum only (and is excluded); weighted score = score/10 x weighting
process: Delta e-sourcing; closing 10:00 Monday 19 October 2026; pitches for the highest scorers on 2 or 3 November at V&A South Kensington; initial term 6 months (Clarification Q1 corrects the ITT's 5); deliverables due end May 2027
status: operator reading, not yet corrected by Iain
---

## item: case-studies
label: Case studies of comparable work (impact study of an institution on UK creative industries)
count_max: 5
page_limit: 2 pages in total for all case studies
keywords: evaluat|impact|visitor|heritage|museum|attraction|spillover
kinds: delivered_output,effect_reported,effect_as_evaluator
named_contact: each case study needs a named contact willing to give a reference
referee_rule: referees are cited by name in the tender and asked only once the bidder is shortlisted (Iain 26/10/08); name a contact likely to agree and never state agreement that has not been given
anonymisation_rule: anonymised case studies allowed only if the client and referee can be disclosed under a mutual NDA on request (Clarification Q12, verbatim: "an anonymised case study should be submitted only if you are prepared to disclose the confidential information (at a minimum, case study organisation and referee) to us should we request it later in the process"; if anonymising, describe the client, size and sector so evaluators can judge relevance). Q12 does not say referee details may be withheld until shortlisting: it asks for a contact for each case study in the tender
citation_rule: delivered work citable unless a restriction marker exists (AGENTS.md citation rules); wording capped at the cited claim's evidence class (ontology decision 11)
wording_source: ITT, Completing and submitting a Tender, item 1 (verbatim)
itt_wording: "Up to 5 comparable case studies, including a contact for each that is willing to give a reference. Maximum two pages total, regardless of the number of case studies."
scoring_wording: "Case studies of comparable work 20%"; scored first; a tender scoring under 6 on the criterion being scored is not considered further; the V&A may also reject a tender scoring under 50% on any qualitative criterion
comparability_note: the ITT does not define "comparable" (re-checked against the ITT text 26/10/08); the keywords are our inference from the contract wording ("outcomes, additional value and unique contribution of our work to the UK's creative industries") and the Q7 output ("case studies showing where and how V&A support has made a material difference to creative careers, practices or businesses over time")
known_limits: keywords search project names and descriptions only, not claim text (Fok lane); the view cannot see projects whose claims are not coded

## item: team
label: Team and relevant experience of key personnel
count_max: not stated
format_note: no required format; suggested no more than 300 words per team member (Clarification Q2)
itt_wording: "Confirmation of your team and relevant experience and evaluation expertise of key personnel that you would allocate to the project"
scoring_wording: "Team, including: Relevant research and evaluation experience and expertise, including undertaking economic assessments in line with government guidance; Sector knowledge" 20%; scored second, after case studies
people_source: 15_people.csv and 16_involvement.csv (ontology decision 14); availability for this tender is recorded here when known, not in the register
availability: not recorded
subcontractors: a single composite PQQ response may cover named sub-consultants (Clarification Q3)

## item: brief
label: What the V&A is asking the study to answer (brief, September 2026)
source: 02 Brief (read in full by Devin 26/10/08)
purpose_quote: "to build a clear, evidence-based understanding of how the V&A supports the UK's creative industries and where that support makes the greatest difference"
key_questions: seven: (1) how the V&A supports the creative industries; (2) how practitioners engage with the collection in person and online and how that adds value; (3) where and how it demonstrably influences creative careers, practices or business trajectories over time; (4) impact on the wider creative ecosystem beyond those it directly engages; (5) which support has the strongest and weakest impact and for whom; (6) what the V&A contributes that is distinctive or unlikely to happen without it; (7) where effort is invested with limited or unclear impact
outputs: impact study (quantitative and qualitative, robust headline economic measures where evidence allows, longitudinal insight); case studies of "a material difference to creative careers, practices or businesses over time"; evidence-backed impact narrative; gaps and low-impact activity; prioritised recommendations for focus, redesign or reduction; interim findings presentation (April 2027), final report, executive summary and presentation (end May 2027)
method_signals: distinguish activity, outputs and impact; combine quantitative and qualitative; informed by the Green Book and the Cultural Heritage Capital Framework (Clarification Q6: guiding, not applied in full); approaches inspired by the IIPP analysis of the BBC (public institutions as ecosystem builders, spillovers and shifts in behaviour or practice)
who_they_want: "not a standard, single discipline evaluation": a blend of economic or impact evaluation, social or behavioural research, and creative or participatory methods including storytelling; in-person attendance at London sites; weekly check-ins and show-and-tells
v_and_a_provides: programme manager, as-is picture, a researcher to collect data (Clarification Q7-Q10), internal expertise, introductions to creatives
scope_limits: UK creative industries; people over 16 with professional or academic involvement; all six sites including V&A Dundee and the V&A Wedgwood Collection; impact model out of scope ("a first step towards")
reading_for_case_studies: the brief's questions 3 and 4 and the case-study output point at long-run, ecosystem and career-level effects. Most of our candidates evidence programme delivery or evaluator-reported effects, not long-run effects on creative careers; the Beatles study is a modelled annual baseline with no effect claims. State comparability honestly and do not stretch claims beyond their evidence class

## item: qualification
label: Pre-qualification questionnaire and compliance (PQQ VA/CON/F26/33)
source: 03 PQQ (read in full by Devin 26/10/08)
financial_standing: current ratio 1 or higher in latest accounts, or a parent guarantee, or a statement of good standing
insurance_required: employer's liability GBP 5m; public liability GBP 5m; professional indemnity GBP 1m
insurance_held: PI GBP 5m, PL GBP 5m, EL GBP 10m with Hiscox to 05/04/27 (company_insurance/insurance_summary.md): meets all three. Policy expires before the end May 2027 deliverables, so renewal must be completed without a gap; certificates show an out-of-date address (Iain to write to Hiscox)
bidding_model: Part 1B; a lead bidder with sub-consultants answers 1.14(a); a single composite response covers all (Clarification Q3); changes to the group must be notified immediately
declarations: exclusion grounds under the Procurement Act 2023 (Parts 2.1 to 2.5); willingness to sign a data sharing or processing agreement and to allow DBS checks and vetting (3.3); modern slavery, net zero and carbon reporting answers (3.5, 3.6)
reference_risk: PQQ third-party checks reserve the right to "request customer details to verify examples provided and take up a reference on any of the information you provide to us" at any stage. A named referee could therefore be contacted before shortlisting. Iain's rule stands (named in the tender, formally asked once shortlisted); the risk is only that a contact is called without warning, so a brief heads-up to each chosen contact is worth considering. Advice, not a gate
