---
name: deepthink
description: Apply rigorous cross-examination to claims, passages or sections of a document. Test them against the rest of the document and cited sources, identifying logical gaps, contradictions and over-claims before content is committed.
allowed-tools:
  - read
  - grep
  - glob
  - exec
triggers:
  - user
  - model
---

# Deepthink

Apply rigorous cross-examination to any claim, passage or section of a document.

## Required review

1. Freeze the exact claim, passage, version, audience and decision it supports.
2. Restate the claim in its strongest fair form before challenging it.
3. Check it against the document's other sections, definitions, data, conclusions, recommendations and stated limitations.
4. Trace cited sources and distinguish direct evidence, inference, interpretation, assumption, prediction and rhetoric.
5. Test whether the evidence supports the claim's population, grain, geography, time period, comparator, causality, precision and confidence.
6. Look for denominator errors, selection effects, missing counterevidence, category errors, circular reasoning, scope drift, survivorship bias, proxy substitution and contradictions.
7. Identify what would change the conclusion and what additional evidence would resolve the uncertainty.
8. Provide a defensible rewrite where the original claim is too strong.

If the passage is part of a larger document, always cross-check the whole document before reporting. Apply the review proactively to significant assertions affecting conclusions, recommendations or funding cases. Do not edit the source unless explicitly authorised.

## Required receipt

Return:

- Claim or passage under review
- Strongest fair interpretation
- Evidence checked
- Cross-document consistency findings
- Logical gaps and over-claims
- Alternative interpretations
- Confidence classification: `SUPPORTED`, `PLAUSIBLE`, `UNKNOWN`, `CONTRADICTED` or `UNSUPPORTED`
- Recommended wording
- Evidence needed before commitment
- Residual risk and re-review trigger
