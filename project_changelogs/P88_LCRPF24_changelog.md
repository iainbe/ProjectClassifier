# P88-LCRPF24 changelog

## 26/10/07 — registered
- New PROVISIONAL project split from P22-LCRFILM; separately contracted in 2024 (Iain). SRC-G2-030 reassigned with path Archive projects/2024 Projects/2024 Liverpool Production Fund/2024 LPF Reporting/250609 ...docx
- Working folder moved from 2025 Projects to 2024 Projects; subset duplicate renamed ZZ superseded duplicate (safe to delete)
- Open: client, contracting_role, contract value, acceptance (VAL-S261007-01); claims (VAL-S261007-03); 2019-23 named files in the working folder (VAL-S261007-04)

## 26/10/08 — claims coded from the final evaluation

- Coded 17 claims (C-S261008-001 to -017), 17 evidence links and 13 measurements from SRC-G2-030 after a full read including the appended tables. All carry fifth_sector_role EVALUATOR (EVALUATOR;LEAD_CONSULTANT for the Fifth Sector's own comparative and scenario analysis) and a value_basis where a figure is present. Contracting role left blank pending VAL-S261007-01.
- Mix: 7 METHOD_OUTPUT (programme data, comparison, comparative analysis, spend breakdown), 5 EFFECT as evaluator with rival explanations (LFO transformation, crew base, facilities, regional spread, one unnamed producer testimony), 3 CONTEXT (long-run trends, awards, extension), 2 DESIGN (55% recoupment forecast with option_state UNKNOWN; indigenous grant scenarios PROPOSED).
- Report-internal inconsistencies recorded in claim notes, not resolved: production FTE rows sum to 858 against a stated 859; £2.82m / 859 is £3,283 not £3,284; Halton 1 vs 6 filming days in 2019; Knowsley facilities 12 vs 10; 19 award wins not reconcilable to listed awards; stated £8 target vs interim 3:1 and 5:1; interim to final ratio not like-for-like (interim £6.73M on £1.78M is 3.8:1); one production holds 36.7% of spend and the other nine give 6.54:1; recommendation (10%) vs conclusion (30% optimal).
- Not coded as DECISION_USE: the July 2024 extension approval predates the June 2025 report (VAL-S261008-04). Forecast 55% recoupment awaits confirmation (VAL-S261008-03). P22 claims C-G2-037/038 quote final figures (VAL-S261008-05, not changed).

## 26/10/08 — client acceptance recorded

- client_accepted set to Y on Iain's bulk statement (clients with several projects); basis IAIN_STATEMENT in `14_fact_provenance.csv`. No written record checked.

## 26/10/08 — Contract evidence

- No PO or contract found in Google Drive; Iain: if none is found there was none. Recorded in relationship_evidence and provenance; contracting_role still empty pending how the work was commissioned.

## 26/10/08 — Contracting role recorded

- `contracting_role`=DIRECT, `prime_contractor`=The Fifth Sector: direct commission from Liverpool City Council on behalf of LCRCA (Iain). No contract or PO exists. MS-02 text updated.

## 26/10/08 — Client wording corrected

- Iain: LCRCA is the client; Liverpool City Council led procurement. Register client unchanged; relationship_evidence, provenance, VAL-S261007-01 and MS-02 text aligned.

## 26/10/08 — Purchase order found

- Invoice INV-1322 (31/03/25) to Liverpool City Council, PO 3500515342, 9,999.00 ex VAT, paid. Earlier note that no PO existed is superseded. File not stored (bank details).
## 26/10/08 — contract value confirmed
- Invoice INV-1322 found (Downloads → project folder): "Liverpool Film Fund Evaluation" £9,999+VAT (£11,998.80), billed to Liverpool City Council, PO 3500515342, issued 31/03/25, paid in full. client_accepted → PAID_IN_FULL. Open: invoice bill-to (LCC) vs report client (LCR CA) distinction.
- LCC/LCRCA distinction RESOLVED (Iain 26/10/08): Liverpool City Council was procurement lead; commissioning client is LCR Combined Authority.
- Referee identified (Iain 26/10/08): Sarah Lovell, LCR CA — named on PR-05 (already drafted; held per shortlist rule).
