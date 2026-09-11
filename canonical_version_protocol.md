# Canonical Version Establishment and Changelog Protocol

**Status:** PROPOSED — awaiting Iain's approval before implementation. This is a new pre-R2 step (R1.5) triggered by the Pinning Stones version problem: the archive contains multiple dated drafts, some labelled "FINAL" that are not final, and the actual final may be in a subfolder with a different name.

**Authority:** M1 approval permitted R2. This protocol refines R2 source preparation. It does not expand R2's scope beyond the approved 15-source manifest; it adds a mandatory version-establishment step before any source is registered as canonical.

## 1. Problem

The archive contains stale iterations, interim drafts labelled "final," and actual final versions in subfolders with different naming conventions. Without a canonical-version step:
- R2 coding could be performed on a superseded draft.
- Version authority is assumed from filename rather than evidenced.
- The analytical value of document evolution (when methods changed, when spillovers were first identified) is lost.

## 2. Process — for each of the 10 pilot projects

### Step 1: Document inventory
For each project root (as listed in the megaplan §8 approved roots):
1. List all documents in the root and relevant subfolders, including file name, file type, file system date (created/modified), file size.
2. Record the full path. Do not modify, move, rename or delete any file.
3. Flag files with version-indicating names: dates, version numbers (v1, v2, v3.12), labels (draft, final, FINAL, update, revision), author initials, tracked-changes markers.

### Step 2: Metadata extraction
For each candidate report document:
1. **File system metadata:** created date, modified date, size, extension.
2. **Document internal metadata:** for DOCX/PDF, extract core properties (title, author, last modified by, revision number, created, modified, subject, keywords) using python-docx or PyPDF2.
3. **Title page / header text:** first 2 pages or first 50 lines, to capture the document's self-declared title, version label, date, authorship, and any "draft"/"final"/"for review" markers.
4. **Change log / version history:** if the document contains an internal changelog, revision history, or tracked changes, extract it.
5. **Cross-reference:** compare file name date, internal metadata date, and title-page date. Flag any conflicts.

### Step 3: Canonical version determination
Establish the canonical final version using evidence, not filename:
1. **Authority hierarchy** (highest to lowest):
   a. Client acceptance/sign-off evidence (email, signed approval, contract milestone).
   b. Document internal metadata: latest revision/modified date, "final" or equivalent on title page, no tracked changes.
   c. File system modified date (least authoritative — can reflect a re-save, not a content change).
2. **Version chain:** if multiple versions exist, establish the chain: earliest draft → ... → canonical final. Record each version's date, title, internal version marker, and what it appears to supersede.
3. **Conflict resolution:** if two documents both claim finality, or if the latest-by-date is not the latest-by-content, record the conflict as UNRESOLVED and flag for Iain's decision. Do not silently pick one.
4. **Superseded versions:** mark non-canonical versions as SUPERSEDED with the canonical version's ID and the basis for supersession.
5. **Missing final:** if no final version can be established (only drafts exist, or the final is inaccessible), record the project as CANONICAL_VERSION_MISSING and flag for Iain.

### Step 4: Changelog compilation
For each project, compile a structured changelog capturing the evolution from earliest available draft to canonical final:

| Field | Description |
|---|---|
| `project_id` | Project ID (P01-NES etc.) |
| `version_id` | Assigned version ID (e.g. NES-v01, NES-v02, NES-FINAL) |
| `document_path` | Full path to the document |
| `file_date` | File system date |
| `internal_date` | Document internal date |
| `title` | Document title as stated on title page |
| `version_label` | Self-declared version (draft, v2, final, etc.) |
| `author` | Stated author(s) |
| `superseded_by` | Version ID that supersedes this one, or CANONICAL |
| `change_summary` | What changed from the previous version (structure, methods, findings, numbers, recommendations) |
| `method_change` | Did the analytical method change? What was added/dropped/modified? |
| `spillover_change` | Did spillover identification change? Were new spillovers identified, reclassified, or dropped? |
| `option_change` | Did strategic option framing change? Were new options introduced, valued, or abandoned? |
| `breakthrough_flag` | Mark versions where a significant analytical breakthrough occurred (new spillover mechanism identified, option value first recognised, method substantially improved) |
| `evidence_basis` | What evidence supports this change summary (diff, side-by-side comparison, internal changelog, reviewer notes) |
| `confidence` | HIGH (internal changelog or tracked changes), MEDIUM (side-by-side comparison), LOW (inferred from dates/titles only) |
| `notes` | Any caveats, unresolved questions, or gaps |

### Step 5: Analytical layer — method and spillover evolution
The changelog is not just a bookkeeping artifact. It becomes a source for analysis:
1. **Method evolution:** when did the analytical method change? What triggered the change (client feedback, new data, internal review, breakthrough insight)?
2. **Spillover identification timeline:** when were specific spillovers first identified, reclassified, or dropped? This traces the development of Fifth Sector's analytical capability.
3. **Strategic option emergence:** when were strategic options first framed, valued, or abandoned? This shows how option-thinking entered the work.
4. **Breakthrough markers:** versions where a significant shift occurred — a new mechanism identified, a counterfactual first attempted, an option first valued. These are candidates for case-study material on the website and in tender evidence.
5. **Stability assessment:** which findings survived from early draft to final? Which were late additions? Which were dropped? Stable findings are stronger evidence; late additions need scrutiny for evidential support.

## 3. Output artifacts

| Artifact | Location | Content |
|---|---|---|
| `canonical_versions.csv` | `spillover-toolkit/` | One row per identified version per project: version ID, path, dates, title, label, authority status, superseded_by |
| `project_changelogs/` | `spillover-toolkit/` | One Markdown file per project: structured changelog with change summaries, method/spillover/option evolution, breakthrough flags |
| `version_metadata/` | `spillover-toolkit/extracted_text/` | Extracted internal metadata (core properties, title pages, internal changelogs) for each candidate document |
| `canonical/` | Within each project root | New subfolder containing copies of only the canonical final version(s). Originals remain in place untouched. Prevents accidental reference to stale versions. |

## 4. Scope and constraints

- **Scope:** the 10 approved pilot project roots only. No new projects, no full portfolio screening.
- **Read-only:** no archive files are modified, moved, renamed or deleted. Originals remain in their original locations.
- **Canonical copies:** a `canonical/` subfolder is created within each project root containing copies of the established canonical final version(s) only. Originals are not moved; the copies provide a clean reference point. The `canonical_versions.csv` records both the original path and the canonical copy path.
- **No new extraction of content:** metadata and title pages only at this stage. Full content extraction of the canonical version follows in R2 for the approved manifest sources. Non-canonical versions are not fully extracted unless a specific diagnostic question requires comparison.
- **Side-by-side comparison:** where two versions are close in date and content, a targeted diff of key sections (executive summary, methodology, headline numbers, recommendations) may be performed to establish what changed. This is read-only comparison, not new analysis.
- **Iain decision points:** any UNRESOLVED version conflict, missing final, or ambiguous authority is referred to Iain. No silent selection.
- **Changelog confidence:** every change summary carries a confidence level. LOW-confidence summaries (inferred from dates only, no content comparison) are marked as such and not treated as established findings.
- **Analytical claims:** the method/spillover/option evolution analysis is a hypothesis-generating layer, not a validated finding. It becomes evidence only after R3 review and Iain's acceptance.

## 5. Relationship to R2

This protocol runs as R1.5 — before R2 source registration:
1. R1.5 establishes which version is canonical for each project.
2. R2 registers the canonical version as the source in `02_sources.csv` with `authority_status=VERIFIED` and evidence.
3. Superseded versions are recorded with `authority_status=SUPERSEDED` and linked to the canonical version.
4. The changelog informs R2-D01 (NES version/baseline test) and other diagnostic units where version authority is the question.
5. The changelog's analytical layer (method/spillover/option evolution) is preserved for R3 and later analysis, not coded as findings in R2.

## 6. Effort estimate

- 10 projects × (inventory + metadata + canonical determination + changelog) = approximately 2-4 hours of automated extraction plus Iain review of any conflicts.
- Side-by-side diffs only where version ambiguity requires them.
- No new software; uses existing python-docx, PyPDF2, openpyxl, and standard file system access.

## 7. Approval and sequencing

**Approved with additions:** Iain approved the protocol on 2026-09-08 with two additions:
1. Create a `canonical/` subfolder within each project root containing copies of only the canonical final version(s), to prevent accidental reference to stale versions. Originals remain in place.
2. Pilot on NES first. Confirm the process works before running the other 9 projects.

**Sequencing:**
1. Run document inventory + metadata extraction for NES (P01-NES) only.
2. Present canonical version determination for Iain's review, including any conflicts.
3. Iain confirms or resolves conflicts.
4. Compile the NES changelog.
5. Create `canonical/` subfolder in the NES root with copies of the established canonical version(s).
6. Iain confirms the process works.
7. Run the remaining 9 projects.
8. R2 proceeds with canonical versions registered as sources.
