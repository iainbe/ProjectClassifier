# Requirements: T22-VAIMP (V&A impact study of the V&A on UK creative industries)

Read by tools/selection_view.py (`--requirements T22-VAIMP`). Lines of the form `key: value` between the two `---` rules, and under each `## item:` heading, are read as data; everything else is for people. This is the operator's reading of the buyer's ask, recorded so a view can be regenerated exactly. Iain to correct. Where the ITT wording is not quoted, the source is the T22 row of `08_tenders.csv` (a summary of the ITT pack received 26/10/07); verbatim quotes still to be added from the ITT pack and Clarification Issue 1 (26/10/06).

---
tender_id: T22-VAIMP
buyer: Victoria and Albert Museum (Board of Trustees, NDPB of DCMS)
deadline: 26/10/19 10:00 Europe/London
budget: Fixed fee cap GBP 60,000
decision: BID (Iain, 26/10/07)
scoring: Case studies 20% (scored first); Team 20%; Proposal 50%; Price 10%
kill_gate: score below 6/10 on any criterion excludes, scored sequentially (case studies, team, proposal, price); below 50% on any qualitative criterion rejectable
frozen_on: 26/10/08
source: 08_tenders.csv row T22-VAIMP; ITT pack; Clarification Issue 1 (26/10/06); review lanes run 26/10/08 (tier2_qa_review.md)
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
anonymisation_rule: anonymised case studies allowed only if the client and referee can be disclosed under a mutual NDA on request (Clarification Q12)
citation_rule: delivered work citable unless a restriction marker exists (AGENTS.md citation rules); wording capped at the cited claim's evidence class (ontology decision 11)
wording_source: 08_tenders.csv mandatory_requirements ("5 comparable case studies incl. named referee each, max 2pp total"); verbatim ITT wording not yet added
comparability_note: the ITT does not define "comparable" (Grey lane, 26/10/08); the keywords are our inference from "impact of an institution on creative industries", spillovers and "material difference over time"
known_limits: keywords search project names and descriptions only, not claim text (Fok lane); the view cannot see projects whose claims are not coded
