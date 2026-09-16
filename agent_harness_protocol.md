# Agent Harness Protocol — Alpha (lead) and Luna (sidekick)

**Status:** PROPOSED — protocol only. No API integration exists yet; phase 2 (§8) is not authorised until Iain approves this document.

**Purpose:** define how two external assistants are used alongside the toolkit without weakening register integrity, evidence discipline or the audit trail.

| Agent | Tool | Responsibility |
|---|---|---|
| **Alpha** | ChatGPT | Lead. Owns the plan: scope, sequencing, acceptance criteria, gate selection. Does not write to registers. |
| **Luna** | GLM-5.2 | Sidekick. Owns implementation: scripts, extracts, draft text, candidate register rows — always against an Alpha work package. |
| **Devin** | this repo | Executor of record. Applies register changes, runs the gates, writes the audit artefacts, commits. |
| **Iain** | — | Authority. Approves plans, resolves conflations and contracting questions, holds the only sign-off that converts PROVISIONAL to confirmed. |

Neither Alpha nor Luna is an author of record. Toolkit outputs are attributed to Fifth Sector work; assistant involvement is a method note, never a source.

---

## 1. Standing rule

**No external agent writes to a register.** Alpha and Luna produce plans and candidate content. Every change to `01_projects.csv` … `11_permission_requests.csv`, the index cards or the changelogs is applied by Devin (or Iain) in this repo, after the checks in `AGENTS.md`.

Rationale: schema drift, FK breakage and project conflation are the three failure modes that have actually occurred. All three are write-path failures, so the write path stays narrow.

## 2. Division of work

### Alpha (lead — plan)

1. Restate the trigger and the decision the work must support.
2. Produce a **work package** (§4) per unit of work: scope, inputs, acceptance criteria, gates, exclusions.
3. Choose the gates: `/thad`, `/sheldon`, `/blindspot`, `/deepthink`, `/wishful`, `/skin`.
4. Name the conflation risks up front (see the multi-project geography list in `AGENTS.md`), and the archive check needed for each.
5. Review Luna's returns against the acceptance criteria before they reach Devin.
6. Escalate to Iain anything requiring authority: contracting role, citation permission, option-exercise status, scope expansion.

Alpha does not draft implementation detail, and does not assert that a figure is evidenced. It states what must be evidenced.

### Luna (sidekick — implementation)

1. Work only from an Alpha work package. No package, no work.
2. Produce the artefact: script, extract, draft card, candidate rows, comparison table.
3. Return the **implementation return** (§5) with evidence for every claim: source ID, locator, quoted figure.
4. Mark anything not fully read as `PARTIAL_EXTRACT` or `NOT_ASSESSED` — never infer absence of an effect from an incomplete extract (`AGENTS.md`, full-read rule).
5. Flag, do not resolve: version ambiguity, conflation candidates, missing evidence, contradictions. These go back to Alpha, then to Iain.

## 3. Cycle

```
Trigger (Iain)
  → Alpha: work package            [plan]
  → Iain: approve / amend          [authority; required for any register-changing package]
  → Luna: implementation return    [candidate artefact + evidence]
  → Alpha: acceptance check        [against §4 criteria]
  → Devin: apply + gates + audit   [registers, /thad or /sheldon, closure artefacts, commit]
  → Iain: sign-off                 [PROVISIONAL → confirmed]
```

A cycle may loop between Luna and Alpha any number of times. It may not skip Devin for register writes, and may not skip Iain for authority questions.

## 4. Work package format (Alpha → Luna)

```
PACKAGE:        WP-<YY/MM/DD>-<slug>
TRIGGER:        what prompted this, verbatim where possible
DECISION:       the decision this supports
SCOPE:          in scope / out of scope
INPUTS:         source IDs, register rows, Drive share links (IDs, never filesystem paths)
CONFLATION:     projects that must not be merged; the archive/date/doc-type check for each
ACCEPTANCE:     numbered, testable criteria
GATES:          which of /thad /sheldon /blindspot /deepthink /wishful /skin apply
EXCLUSIONS:     what must not be changed (registers, canonical files, prose in review history)
```

## 5. Implementation return format (Luna → Alpha)

```
PACKAGE:        WP-...
ARTEFACT:       path or inline content
EVIDENCE:       per claim — claim text | source_id | locator | quoted figure
EXTRACT STATUS: FULL / PARTIAL_EXTRACT / NOT_ASSESSED per source
FLAGS:          conflation candidates, version ambiguity, missing evidence, contradictions
NOT DONE:       acceptance criteria not met and why
ASSUMPTIONS:    anything inferred rather than evidenced
```

An empty `EVIDENCE` block for a claim containing a figure is a failed return, not a partial one.

## 6. Rules both agents inherit

These are not negotiable per package; they are the toolkit's rules and apply to every return.

- **Project differentiation** — geography, client or sector overlap never implies the same project. Check description, archive folder, date and document type (`AGENTS.md`).
- **Classification** — sector baselines are CONTEXT, not METHOD_OUTPUT. A description of an existing state is CONTEXT, not EFFECT.
- **Forecast vs realised** — a forecast is never presented as an outcome without a later confirming source.
- **value_basis** — any proposition containing `£` carries a `value_basis`.
- **Citation two-field model** — `citation_status` and `reference_permission` are separate questions. "APPROVED via use" is banned.
- **Attribution** — contribution work names the contracting structure; never imply Fifth Sector ownership of a prime's or consortium's deliverable.
- **Extraction** — tables are evidence; check bare numerics under currency headers; apply `canonical_version_protocol.md` when a location is a directory.
- **Evidence location** — before declaring evidence missing, both archives are checked (G Drive and OneDrive-TheFifthSector).
- **Dates** — `YY/MM/DD` everywhere except verbatim text in `extracted_text/`.
- **Schema drift** — candidate rows state the header they were built against, with field count and positional semantics verified.

## 7. Access

Alpha and Luna work from web Drive and from this repo's public content, on the same terms as the `tools/JON_ACCESS.md` route:

- Reference material by **Drive share link or file ID**, never by a filesystem path — paths exist only on Iain's machine.
- `tools/drive_sweep.py`, `tools/regenerate_index.py` and `tools/normalise_dates.py` need a local mount and are run by Iain or Devin, not by the assistants.
- `sweep_reports/SWEEP_LATEST.md` is the shared view of Drive drift and is the first thing read at the start of a package.
- Client-identifying content is not pasted into an assistant where `reference_permission=NOT_ESTABLISHED` and the content would identify the client. Use source IDs and neutral descriptions instead.

## 8. Phase 2 — integration (not authorised)

Deferred until this protocol is approved. When authorised, the intended shape is:

- a single `tools/agents/` client with one adapter per assistant (Alpha: OpenAI API; Luna: GLM API), keys held as environment secrets, never in the repo;
- package and return objects as files under `agent_packages/`, so every exchange is diffable and auditable;
- a dry-run mode that produces candidate rows to a scratch file, never to a register;
- rate and cost logging per package.

Open questions for Iain before any of that is built: which account and billing route for each assistant; whether returns are retained in the repo or only summarised; whether client-identifying material is permitted in either vendor's context at all.

## 9. Failure handling

| Situation | Action |
|---|---|
| Luna returns unevidenced figures | Reject the return; Alpha reissues with the evidence requirement restated. Do not repair it silently. |
| Alpha's package expands scope beyond the trigger | Iain decides; do not proceed on the wider scope. |
| Two returns disagree on a figure | Record both, quote both locators, escalate. Never average or pick the convenient one. |
| An agent asserts a completed action it cannot evidence | Treat the whole return as unverified and re-run the package. |
| A register write reaches an agent's hands | Stop, revert, record the incident in `tier2_qa_review.md`. |

## 10. Session closure

Sessions involving Alpha or Luna close under the same mandatory rule as any other toolkit session: `CHANGELOG.md`, `tier2_qa_review.md` and `10_review_history.csv`, plus per-project changelogs where project data changed. The changelog entry names which agent produced the plan and which produced the implementation.
