---
description: Extract intelligence from project documents
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [document type, filename, "scan", or "interactive"]
---

Process new or updated project documents. Extracts intelligence and merges it into the existing project data without overwriting what's already there.

**PROCESSING MODE — BATCH BY CATEGORY:**
This command uses a **5-phase adaptive extraction pipeline**. Documents are classified first, then processed in batches grouped by document type. The recommended batch order is: Specifications → Plans → Schedule → Contracts/Directory → RFIs/Submittals/COs → DWG/CAD → Support documents (meeting minutes, daily reports, pay apps, geotech, safety). After processing each batch, Claude MUST stop, report results, and **use AskUserQuestion** to ask the user what to process next. Claude must NEVER process the entire project in a single pass — batch checkpoints prevent context overload and ensure data quality.

**Small project exception:** For projects with ≤10 documents, classify and extract inline (skip separate classification phase). For 11-50 documents, classify inline but keep cross-referencing as a separate phase.

Read the document-intelligence skill at `${CLAUDE_PLUGIN_ROOT}/skills/document-intelligence/SKILL.md` and the project-data skill at `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` before proceeding. Also read `${CLAUDE_PLUGIN_ROOT}/skills/document-intelligence/references/extraction-rules.md` for type-specific extraction rules. After extraction is complete, read the doc-orchestrator agent at `${CLAUDE_PLUGIN_ROOT}/agents/doc-orchestrator.md` to validate extraction output and ensure data quality. If available, also read the `construction-takeoff` Cowork skill for extracting material quantities from plan sheets during document processing.

## Step 1: Load Existing Project Data

Search for `project-config.json` in the user's working directory. Check these locations in order:
1. `AI - Project Brain/project-config.json`
2. `project-config.json` in the working directory root

If not found, tell the user: "No project is set up yet. Run `/set-project` first to create your project, then come back to process documents."

If found, load it and check the `documents_loaded` array to see what's already been processed.

## Step 2: Identify What to Process

### Mode A: Specific file or type (`/process-docs ASI-003.pdf` or `/process-docs schedule`)

If `$ARGUMENTS` contains a filename:
- Locate that file in the mapped folders (using `folder_mapping` from config) and process it.
- If the file isn't found, tell the user: "I couldn't find [filename] in your project folders. Check the path or drag the file into this chat."

If `$ARGUMENTS` contains a document type (e.g., "schedule", "specs", "plans", "safety"):
- Look in the relevant mapped folder for that type
- If multiple files of that type exist, list them and **use AskUserQuestion** to ask the user which ONE to process

### Mode B: User uploads a file directly

If the user drags/drops or uploads a file into the chat:
- Process the uploaded file directly. No folder lookup needed.

### Mode C: No arguments (`/process-docs`)

If no arguments and no uploaded file:
- Tell the user: "What would you like me to process? You can:"
  - "Drag a file into this chat"
  - "Tell me a filename: `/process-docs ASI-003.pdf`"
  - "Tell me a document type: `/process-docs schedule`"
  - "Run `/process-docs scan` to see what's new in your folders"
  - "Run `/process-docs interactive` to walk through folders one at a time"

### Mode D: Scan (`/process-docs scan`)

Lightweight folder scan. Compares what's in the project folders against what's already been processed. Reports what's new, what's changed, and what's ready to process. Does NOT extract or process any documents — just looks and reports.

1. **Load folder_mapping and documents_loaded** from `project-config.json`
2. **Walk every mapped folder** — list all supported file types (`.pdf`, `.xlsx`, `.xls`, `.csv`, `.docx`, `.doc`). Record filename, full path, file size, and parent folder.
3. **Compare against documents_loaded**:
   - Not in documents_loaded -> **NEW**
   - Same filename and file size -> **UNCHANGED**
   - Same filename, different file size -> **UPDATED**
4. **Present scan report** grouped by status.

   If nothing's new: "All [X] documents are up to date. Your project intelligence is current."

   If no documents have been processed yet: list all files grouped by folder and recommend starting with specs and schedule.

This scan is read-only — safe to run as often as needed.

### Mode E: Interactive Folder Walk (`/process-docs interactive`)

**This is the recommended mode for initial project processing or reprocessing.** It walks through every mapped folder one at a time, presenting each folder's contents and asking the user whether to process it.

**Step E1: Scan all folders and build inventory**

Walk every folder in `folder_mapping`. For each folder, count files and identify document types. Build a folder inventory and present it to the user with a summary: "I found X files across Y folders. Let's go through them one folder at a time."

**Step E2: Choose processing strategy using AskUserQuestion**

Present the folder inventory and ask the user to choose a processing strategy. Options:
- "Batch by category (recommended)" — Classify all documents first, then process in optimal order: Specs → Plans → Schedule → Contracts → Support docs. Best for initial project setup.
- "Process folder by folder" — Walk through each folder sequentially, processing files within each folder
- "Skip to specific type" — Jump directly to a document type (e.g., "just the specs")

If "Batch by category" is chosen, classify all documents (Phase 1), then present the batch plan for confirmation before starting extraction (Phase 2).

If "Process folder by folder" is chosen, for each folder use **AskUserQuestion** to present the folder contents and ask:
- "Process this folder" — Process the file(s) in this folder
- "Skip this folder" — Move to the next folder
- "Process deeper (with visual analysis)" — Process with full graphical/visual extraction (for plan sheets)

**IMPORTANT:** If the folder contains multiple files, process them ONE AT A TIME within the folder. After each file, provide a brief status update. Only use AskUserQuestion between folders, not between individual files within the same folder (to avoid excessive prompting). However, if a single file is very large (>20 pages), you may split it into logical sections and process section by section.

**Step E3: Process the selected folder**

Process ONLY the files in the current folder. Follow Steps 3-8 below for each file.

**Step E4: Report results and ask for next folder**

After processing all files in the current folder, report what was extracted. Then use **AskUserQuestion** to present the NEXT folder. Continue until all folders have been offered.

**CRITICAL ANTI-LOOP RULE:** After processing each folder's files, Claude MUST:
1. Save all extracted data to the appropriate JSON files
2. Update `documents_loaded` in `project-config.json`
3. Report a concise summary of what was extracted
4. **STOP and wait for user input** via AskUserQuestion before moving to the next folder
5. NEVER process the next folder automatically — always ask first

### Duplicate Check

Before processing, check if the file is already in `documents_loaded`:
- If the same filename with the same file size exists: already processed — ask if user wants to re-extract
- If the same filename with a different file size exists: updated version — extract the changes

## Step 3: Extraction Pipeline (5-Phase Adaptive Model)

For documents being processed, run the **5-phase adaptive extraction pipeline**. This model is based on DocETL (UC Berkeley VLDB 2025), LlamaIndex Agentic Document Workflows, and validated against real project extraction data (150 docs, 93.3% confidence).

### Phase 1 — Index & Classify

Lightweight pass — text only, no deep extraction. For each document:
1. Extract PDF metadata (creator, title, dates, page count)
2. Auto-classify document type (see `doc-orchestrator.md` classification table)
3. For plan PDFs: build sheet index from TOC or title blocks
4. Build dependency graph (which docs reference which others)
5. Build batch plan: group by type, order batches optimally

**Batch order:** Specifications → Plans → Schedule → Contracts/Directory → RFIs/Submittals/COs → DWG/CAD → Support docs

**Phase 1 exit criteria:** All docs classified with ≥70% confidence; dependency graph built. If any classification <70%, present to user for confirmation before Phase 2.

**DWG files:** Classified alongside PDFs. DWG entities counted, layers listed. DWG extraction runs in parallel with PDF extraction in Phase 2.

### Phase 2 — Extract

Process batches in category order. Adaptive intensity per page:
- **Cover sheets, title pages:** 2 passes (metadata + structural scan)
- **Text-heavy docs** (specs, contracts): 3 passes (metadata + structure + deep content)
- **Plan sheets:** 4-6 passes (metadata + structure + content + visual analysis)

For each document, follow the **document-intelligence** skill's extraction methodology (see `SKILL.md`):

**Text extraction:**
- Pass 1: Metadata extraction (creator app, dates, page count, auto-classify)
- Pass 2: Structural text analysis (sheet index, TOC, tables, headers)
- Pass 3: Deep content extraction per document type (see `extraction-rules.md`)

**Visual extraction** (plan sheets and drawings only):
- Claude Vision is the **primary** visual method (always available, no dependencies)
- Convert PDF pages to images: `pdftoppm -png -r {DPI} "document.pdf" /tmp/sheet_images/sheet`
- Use the Read tool to view each image and extract: dimensions, scale data, room labels, equipment, notes, title block data
- Tesseract OCR supplements small text that Vision misses
- Python CV pipeline (`visual_plan_analyzer.py`) is an **optional enhancement** for precise coordinates when dependencies are available
- Store all visual data with `"source": "claude_vision"` or `"source": "dxf"` as appropriate

**Scale calibration** is RECOMMENDED but non-blocking:
- Attempt scale calibration per SKILL.md protocol (graphic bar → text notation → known-dimension fallback)
- If calibration fails: record `"scale_status": "uncalibrated"` and **continue extraction**
- Text-based data (room names, door marks, notes, equipment tags) are extracted regardless of scale status
- Uncalibrated sheets are flagged for later remediation (Phase 4) but do not block the pipeline

**Entity resolution — Tentative IDs:**
- During extraction, assign tentative entity references using `directory.json` and `specs-quality.json` as lookup tables
- Mark as `"entity_status": "tentative"`. Example: "D&P" → tentatively "Davis & Plomin" based on directory match
- Tentative IDs will be confirmed or corrected in Phase 3

**Inline gleaning** (validate while context is loaded):
- After extracting each page/section, spot-check key fields against the source
- Max 2 gleaning retries per page — if still failing, log and move on
- This catches OCR misreads and structural parsing errors while the source context is fresh

**Phase 2 exit criteria:** All batches processed; population rate ≥60% per active file.

### Phase 3 — Cross-Reference

Entity resolution and bidirectional linking across all extracted data:

1. **Canonical entity resolution:** Confirm tentative IDs from Phase 2. Merge duplicates. Create canonical entity registry. Update all references to canonical IDs. Mark as `"entity_status": "canonical"`. Batch entities (max 20 per resolution call).
2. **Bidirectional linking:** Submittal ↔ Procurement, RFI ↔ Drawing, Schedule ↔ Submittal, Sub ↔ Scope ↔ Spec
3. **Reference graph validation:** Check all 12 cross-reference patterns from `cross-reference-patterns.md`
4. **Dual-source reconciliation** (if DWG pipeline also ran): Compare DXF quantities vs Claude Vision quantities. DXF data merges at Priority 1 over visual estimates. Flag unresolved conflicts.
5. **Orphan reference handling:** During initial setup, orphan references are expected (specs processed before subcontracts). Track orphans in temporary queue; only flag remaining orphans after full batch completes.

**Phase 3 exit criteria:** All cross-refs validated; entity registry canonical; bidirectional links ≥90% complete.

**PM review gate at Phase 3 exit:**
- Present batch summary of all cross-reference conflicts, orphans, and quantity discrepancies >10%
- User confirms before proceeding to Phase 4

### Phase 4 — Remediate

Targeted re-extraction of items flagged by Phase 2-3 validation:
- Items with failed scale calibration → re-attempt with different method or manual review
- Cross-reference conflicts → present both values with sources to PM
- Low-confidence extractions → re-extract with higher DPI or zone cropping
- Orphan references remaining after full batch → PM decides: missing doc, data entry error, or acceptable gap

**Never auto-resolve:**
- Financial value conflicts (legal/contractual implications)
- Critical path schedule changes (contract notice requirements)
- Safety data conflicts (life safety)
- Quantity discrepancies >10% without PM confirmation

**Phase 4 exit criteria:** All auto-fixable items resolved; PM-decision items logged to `action-items.json`.

### Phase 5 — Normalize

Apply normalization patterns and generate final confidence score:
1. Run N1-N8 normalization patterns via `/data-health fix` (see `data-normalization` skill)
2. Generate phase-aware confidence report via `/data-health report`
3. Produce final extraction summary

**Phase 5 exit criteria:** N1-N8 applied; confidence score generated; final report produced.

### Processing Refinements

**DPI Recipes:**

| Document Type | DPI | Notes |
|--------------|-----|-------|
| D-size drawings (24x36, 30x42) | 150 | Crop to 1800x1200 for Vision |
| Letter-size PDFs (specs, submittals) | 200 | Standard rendering |
| High-detail areas (enlarged plans, details) | 300-350 | Zone crop specific areas |
| Text-extractable PDFs (contracts, reports) | Skip | Extract text directly, no rendering |

**Atomic Python Script Pattern:**
When updating multiple JSON files, use a single atomic Python script:
```python
import json
# Read all target files
with open('file1.json') as f: data1 = json.load(f)
with open('file2.json') as f: data2 = json.load(f)
# Modify in memory
data1['key'] = new_value
data2['items'].append(new_item)
# Write all files
with open('file1.json', 'w') as f: json.dump(data1, f, indent=2)
with open('file2.json', 'w') as f: json.dump(data2, f, indent=2)
# Print summary
print(f"Updated {len(changes)} records across 2 files")
```

**Canonical Key Names (locked — never rename):**

| File | Top-Level Array Key |
|------|-------------------|
| `schedule.json` | `activities[]` |
| `delay-log.json` | `delay_events[]` |
| `submittal-log.json` | `submittals[]` |
| `rfi-log.json` | `rfis[]` |
| `change-order-log.json` | `change_orders[]` |
| `inspection-log.json` | `inspections[]` |
| `procurement-log.json` | `items[]` |
| `action-items.json` | `items[]` |

**Coverage vs Depth:**
Index ALL sheets/sections first (Phase 1), then deep-dive critical ones (Phase 2). Don't spend 6 passes on a cover sheet. Adaptive intensity means simple pages get 2 passes, complex plan sheets get the full pipeline.

**Append-Only Merge Strategy:**
Never auto-resolve conflicts between old and new data. When re-extracting or processing revised documents:
- Old data preserved with `"superseded_by"` reference
- New data added alongside with source attribution
- PM confirms before old data is archived
- See `doc-orchestrator.md` for conflict handling methodology

## Step 4: Merge Intelligence

Use the project-data skill's merge rules when integrating new intelligence into existing config:

| Data Type | Merge Strategy |
|---|---|
| Subcontractors | Add new, update existing (match on name), never delete |
| Milestones | Update dates, add new milestones, never delete |
| Spec sections | Add new sections, update requirements, never delete |
| Grid lines | Merge (add new grids), never replace |
| Schedule (full update) | Replace current dates/critical path, keep history |
| Contract dates | Replace with newer, log change in version history |
| Weather thresholds | Update per spec section, log changes |
| Testing requirements | Add new, update frequency/agency, never delete |
| Hold points | Add new, update existing, never delete |
| Tolerances | Update per material/system |
| Safety zones | Add new, update existing |
| Geotechnical | Replace with newer data |
| SWPPP BMPs | Add new, update existing locations |
| RFIs | Add new RFIs, update status for existing |
| Submittals | Add new submittals, update status, attach product specs |
| Vendors | Add new vendors, update contact/pricing info |
| Concrete mix designs | Add new mixes, update existing, never delete |
| PEMB data | Replace with newer manufacturer data, keep version history |
| Electrical equipment | Add new, update existing, never delete |
| Permits | Add new, update expiration dates, never delete |
| Civil/utility systems | Add new runs, update inverts/sizes, never delete |

### Version History
Log all changes to key data points in the `version_history` array with date, source, field, old_value, new_value, and reason.

### Conflict Resolution
- Newer document wins, log the change
- Older document: ask the user
- Unknown dates: present both values and ask

### Document-Specific Merge Notes

Follow the detailed merge notes for each document type: RFI logs, submittal logs, vendor quotes, submittal packages, revised schedules, ASIs, change orders, sub lists, meeting minutes, geotechnical reports, safety plans, and SWPPP documents.

### Cross-Referencing After Merge

After merging new data, run cross-checks for downstream impacts based on what was processed (ASIs vs procurement, RFIs vs submittals, schedule vs procurement, sub lists vs schedule, meeting minutes vs logs, spec updates vs plan values).

## Step 5: Build Cross-References and Quantities (Incremental)

After extraction, run the **quantitative-intelligence** skill workflow — but only for data affected by the newly processed document. Update sheet cross-reference index, rebuild affected assembly chains, recalculate affected quantities, and run cross-verification.

## Step 6: Save Updated Data Files

Write changes to ONLY the data files affected by this processing run. Always update `project-config.json` to add the processed file to `documents_loaded` with these fields:

```json
{
  // Tier 1 — Core (always required)
  "filename": "document.pdf",
  "type": "schedule",
  "discipline": null,
  "date_loaded": "2026-02-12",
  "sections_extracted": [],
  "coverage_notes": "",
  "confidence": "high",

  // Tier 2 — Batch/Phase Tracking (5-phase model)
  "id": 42,
  "batch_id": "BATCH-003",
  "extraction_phase": 2,
  "status": "extracted",
  "entity_status": "tentative",

  // Tier 3 — Extraction Metadata
  "page_count": 8,
  "file_size": "2.1 MB",
  "sheet": null,
  "extraction_methods": ["text", "structural_analysis"],

  // Tier 4 — Quality Metrics
  "visual_extraction": false,
  "scale_data_extracted": false,
  "scale_calibration_method": null,
  "scale_calibration_confidence": null,

  // Tier 5 — Impact Tracking
  "data_files_updated": ["schedule.json"]
}
```

**Field reference:**
- `id`: Sequential entry identifier
- `batch_id`: Batch grouping (e.g., "BATCH-001" for specs batch)
- `extraction_phase`: Current pipeline phase (1-5)
- `status`: "pending" | "in_progress" | "extracted" | "cross_referenced" | "validated"
- `entity_status`: "tentative" (Phase 2) | "canonical" (Phase 3) | null (no entities)

See `json-schema-reference.md` for the complete 5-tier schema documentation.

## Step 7: Regenerate Project Memory File

Regenerate `CLAUDE.md` with the latest intelligence including scale data summary.

## Step 8: Post-Extraction Agent Validation

After saving extracted data (Step 6) and before presenting results to the user, invoke validation agents. Use **tiered validation** based on the current extraction phase:

**Light validation** (after Phase 1 or single-document extraction):
- Run **doc-orchestrator** only — pipeline validation checks (P1-P4), field population checks

**Full validation** (after Phase 2+ batch completion):
- Run all three agents **in parallel** using the Task tool (single message, 3 Task tool calls):

1. **doc-orchestrator** (read agent at `${CLAUDE_PLUGIN_ROOT}/agents/doc-orchestrator.md`):
   - Run pipeline validation checks scaled by phase (schema-only for Phase 1, inline gleaning for Phase 2, reference integrity for Phase 3, before/after for Phase 4, full-corpus for Phase 5)
   - Run field population checks
   - Report pass/fail summary

2. **data-integrity-watchdog** (read agent at `${CLAUDE_PLUGIN_ROOT}/agents/data-integrity-watchdog.md`):
   - Run orphan detection on updated files
   - Run cross-file conflict checks focused on files touched by this extraction
   - Report any new integrity issues

3. **conflict-detection-agent** (read agent at `${CLAUDE_PLUGIN_ROOT}/agents/conflict-detection-agent.md`):
   - Run cross-discipline conflict detection against newly extracted data
   - Compare new data against existing data in other files
   - Report conflicts classified by severity

**Agent cap:** Max 3 concurrent validation agents. Queue additional work if needed.

Present the combined agent results as part of the extraction summary:
```
Extraction Complete — [document name]

Data extracted: [summary of what was added/updated]
Files updated: [list of JSON files modified]

Agent Validation:
  doc-orchestrator: [X checks passed, Y issues]
  data-integrity-watchdog: [X clean, Y warnings]
  conflict-detection: [X conflicts found (C critical, M major, N minor)]

[If conflicts found, show top 3 by severity]
```

## Step 9: Summarize and Checkpoint

**CRITICAL — This is the anti-loop checkpoint.**

After processing each batch (or single document in non-batch mode):
1. Report what was extracted with the agent validation results from Step 8
2. **STOP processing**
3. **Use AskUserQuestion** with options: Process next batch, Reprocess deeper, Review conflicts, Run cross-references (Phase 3), Done for now, Show what's left

**NEVER automatically continue to the next batch.** Always stop and ask.

**Phase transitions:** When all Phase 2 batches are complete, prompt user to proceed to Phase 3 (Cross-Reference). When Phase 3 completes, prompt for Phase 4 (Remediate) if there are flagged items. Phase 5 (Normalize) runs automatically via `/data-health fix` after PM approves Phase 4 results.

---

## Extraction Hooks (Optional)

ForemanOS provides 4 extraction hooks in `foremanos-intel/hooks/` for automated quality guardrails. These run locally as Node.js scripts — zero API calls, zero rate limit risk, ~12ms per trigger.

| Hook | Trigger | Purpose |
|------|---------|---------|
| `project-brain-validator.js` | PreToolUse (Write\|Edit) | Validates JSON structure, canonical keys, catches empty overwrites |
| `counter-reconciler.js` | PostToolUse (Write) | Checks `_count` fields match array lengths after writes |
| `extraction-checkpoint.js` | PreCompact | Saves extraction progress before context compaction |
| `data-loss-guard.js` | PreToolUse (Write) | Warns if record count decreases (never blocks) |

To enable, add to `~/.claude/settings.json` under `hooks`:

```json
{
  "PreToolUse": [
    { "matcher": "Write|Edit", "hooks": [{ "type": "command", "command": "node path/to/foremanos-intel/hooks/project-brain-validator.js" }] },
    { "matcher": "Write", "hooks": [{ "type": "command", "command": "node path/to/foremanos-intel/hooks/data-loss-guard.js" }] }
  ],
  "PostToolUse": [
    { "matcher": "Write", "hooks": [{ "type": "command", "command": "node path/to/foremanos-intel/hooks/counter-reconciler.js" }] }
  ],
  "PreCompact": [
    { "matcher": "*", "hooks": [{ "type": "command", "command": "node path/to/foremanos-intel/hooks/extraction-checkpoint.js" }] }
  ]
}
```

Hooks are documented but **not auto-installed** — the user enables them manually. All hooks warn on stderr but never block writes.
