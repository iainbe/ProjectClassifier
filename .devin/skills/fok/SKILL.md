---
name: fok
description: Route Foresight Places questions to existing evidence, challenge weak premises, combine compatible sources and derive defensible new insight with a useful forward path for every evidence gap; use for place intelligence, data discovery, cross-source analysis and evidence gaps.
---

# FoK — Font of Knowledge

## Jonbot alignment

When `$jonbot` is active, read its current behavioural sources before this review. Apply its collaboration contract while preserving FoK's evidence-routing role.

Start with the human question, not the database. FoK has four duties:

1. route the question to the evidence and methods already present;
2. be the smartass who challenges a bad premise, weak denominator, invalid
   proxy, incompatible join or unjustified claim;
3. combine compatible evidence across identity, geography, sector, time and
   claim state to seek insight that no single source states; and
4. return the strongest defensible finding, contradictions, uncertainty and
   the next discriminating question.

Run `scripts/query_fok.sh "<question>"` from this skill to obtain the governed
recipes, sources, join keys, claim ceilings and freshness checks. The route is
an analysis plan, never a finding. Inspect current source coverage and execute
the necessary read-only queries or existing services before interpreting it.
For a locally Product-bound investigation, run the backend command with
`--evidence-receipt` first. It proves scope and coverage only; a caveated or
missing family is a gap, never a negative finding.
For the supported recipe screen, `--evidence-screen` may return
`insufficient_evidence`. Report that state plainly, name the exact missing or
caveated evidence, and use `ways_forward` to offer the smallest recovery path
and a useful lower-claim question. Never force a finding from uncovered
sources, and never make the gap the final answer.

Read [references/question-routing.md](references/question-routing.md) when
answering an analytical question. Read
[references/places-data-estate.md](references/places-data-estate.md) only for
physical location, source onboarding or governance work.
Read [references/multi-scope-acquisition.md](references/multi-scope-acquisition.md)
whenever the question or universe is national, sector-specific, international,
cross-border or otherwise not a conventional local-authority scope. A lack of
UK/local-authority data parity is an evidence-profile fact, never a reason to
abandon the scope or pretend that no useful source can be found.

Never average away disagreement between official, provider, Foresight-derived,
modelled and stakeholder evidence. Preserve `observed`, `provider-estimated`,
`Foresight-lookalike`, `predicted`, `modelled value`, `scenario` and `unknown`
as distinct lanes. A useful FoK answer explains what the combination changes;
it is not a table list, a refusal, or a bare failure state. `needs_question`,
`needs_clarification`, `scope_unavailable`, `insufficient_evidence`,
`no_executable_recipe`, `not_testable`, blocked and deferred mean “change the
route”, not “stop”. Return the supplied `ways_forward` actions, then state the
strongest defensible lower-claim route available now.

For structural, causal, counterfactual or forecast questions, inspect returned
method cards as well as capabilities. A method card supplies its live status,
requirements, current evidence state, claim ceiling, prohibited uses,
`ways_forward` and MrU impact. Never turn an
`active_diagnostic`, `counterfactual_candidate`, `definition_only` or restricted
legacy method into a causal result. If the method's source, calibration, donor
policy, claim status, persistence or snapshot projection changes, route the
declared impact to `$mr-universe` before Product use.

For a material evidence gap, FoK owns active source recovery: inspect the
estate and its adapters first, then seek authoritative/provider sources and
assess rights, provenance, schema, identity, coverage, time, comparability,
cost and ingestion feasibility. Where the task authorises acquisition and a
governed local onboarding path exists, carry it out and record its receipt;
otherwise return the precise acquisition action/owner. Landing a source is not
admission or Product proof, but incomplete parity is never permission to stop
looking, invent zeroes or silently delete an analytical dimension.

When a question depends on weak, partial, indirect or conflicting signals,
FoK **must consult `$grey`** before presenting a final analytical reading.
Give Grey the decision/question, source routes tried, relevant observations and
gaps, comparisons or baselines, and live constraints. Incorporate Grey's best
current reading, competing explanations and next discriminating evidence. Grey
is advisory: it must never convert an imperfect evidence profile into a veto,
but it must keep proxies, models and observations visibly distinct.

When recovery exposes a genuine data-existence, access, licensing, cost,
comparability or ingestion-feasibility uncertainty, FoK **must consult
`$wishful`** before concluding that the family is unavailable or narrowing the
outcome. Give WISHFUL the intended decision/measure, scope and grain, missing
family, discovery already performed, candidate providers/adapters, rights and
access constraints, time/cost limits, and the best lower-claim analysis.
Incorporate its ranked feasible routes into FoK's `ways_forward`. WISHFUL is an
advisory HOW route: it does not let FoK manufacture evidence, waive admission,
or turn an unavailable source into a negative finding.
