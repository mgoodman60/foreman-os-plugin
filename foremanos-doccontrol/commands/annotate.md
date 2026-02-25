---
description: Markup plans, specs, photos, and RFIs
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [plan|spec|photo|rfi] [reference]
---

# Document Annotation Command

## Overview

Construction document annotation and markup for superintendents. Mark up plan sheets with work areas, hold zones, and redlines. Extract and annotate spec sections for trade distribution. Annotate construction photos with deficiency callouts and measurement overlays. Create annotated drawing markups for RFI submission packages. All annotations are tracked as structured records with full traceability to source data.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/document-annotation/SKILL.md` — Full document annotation system: PDF markup capabilities, text annotations, symbol placement, color-coded discipline markup, layer management, annotated document production, photo markup, as-built redlines, annotation data model
- `${CLAUDE_PLUGIN_ROOT}/skills/document-annotation/references/markup-conventions-guide.md` — Field reference: standard markup symbols, color conventions by discipline, line weight conventions, cloud markup rules, text annotation standards, photo markup conventions, digital tool guidance, markup abbreviations
- `${CLAUDE_PLUGIN_ROOT}/skills/document-intelligence/SKILL.md` — Document intelligence extraction for auto-generated annotations (stub — full skill in foremanos-intel)
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/rfi-preparer/SKILL.md` — RFI tracking for cross-referencing RFI markups

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `annotation-log.json` (annotations, annotation_sets, symbol_library, layer_definitions)
- `rfi-log.json` (existing RFIs — for cross-referencing RFI markups)
- `punch-log.json` (punch list items — for photo annotation cross-referencing)
- `drawing-log.json` (drawing register — for sheet number lookup and revision tracking)

If `annotation-log.json` does not exist, create it with the empty schema:
```json
{
  "annotations": [],
  "annotation_sets": [],
  "symbol_library": {},
  "layer_definitions": [],
  "project_color_overrides": {}
}
```

Determine the next available ID for annotations (ANN-###) and annotation sets (ASET-###) by scanning existing entries.

### Step 2: Parse Arguments

The user provides one of four subcommands:
- **plan** — Mark up a plan sheet with work areas, hold zones, access routes, redlines
- **spec** — Extract and annotate relevant spec sections for trade distribution
- **photo** — Annotate construction photos with callouts, arrows, deficiency descriptions
- **rfi** — Create annotated drawing markup for RFI submission

If no argument is provided, display a summary of recent annotation activity: last 5 annotations created, open annotation sets, and annotation counts by layer.

If the user provides additional natural language after the subcommand, use it as context (e.g., `/annotate plan mark Level 2 mechanical work area for this week` or `/annotate photo punch item 47 in Room 305`).

### Step 3: PLAN — Plan Sheet Markup

When the argument is `plan`:

1. **Identify the target sheet**: Ask the user for the sheet number or identify it from context. Check `drawing-log.json` for the current revision of that sheet. Locate the source PDF in the project folder structure.

2. **Determine markup type** from user context:
   - **Work area markup**: Define zone boundaries, label with work description, color by trade, add access route arrows and staging area markers. Layer: `WORK_AREAS`.
   - **Hold zone markup**: Draw hold boundary in red, label with "HOLD" and reason, add hold point diamond symbols, reference the blocking item (RFI number, inspection, coordination issue). Layer: `HOLD_POINTS`.
   - **Redline markup**: Place revision clouds around changed areas, add revision delta symbols, annotate with change description, reference ASI/SK/CO number. Layer: `REVISIONS`.
   - **As-built markup**: Add dimension redlines showing field-measured vs. design values, mark routing changes with discipline-colored lines, add deviation notes. Layer: `AS_BUILT`.
   - **Field note markup**: Place text annotations at specific locations on the plan with observations, measurements, or coordination notes. Layer: `FIELD_NOTES`.

3. **Generate annotation records**: For each markup element:
   - Create an annotation record with all required fields (annotation_id, document_ref, type, location, content, discipline, color, layer, linked_items)
   - Apply discipline color coding per the markup conventions guide
   - Apply appropriate line weight (heavy for clouds/boundaries, medium for dimensions/leaders, light for references)

4. **Describe the annotated output**: Since programmatic PDF modification requires Python execution, describe the annotation plan in detail:
   - List each annotation with its placement coordinates, type, content, and visual properties
   - Provide the PyMuPDF/fitz code commands needed to apply each annotation
   - If the user has Python available, generate a complete annotation script

5. **Save annotation records** to `annotation-log.json`.

### Step 4: SPEC — Spec Section Annotation

When the argument is `spec`:

1. **Identify the target spec section**: Ask the user for the spec section number or trade. Cross-reference with document-intelligence extracted data if available.

2. **Extract key requirements**: Pull critical requirements from the spec section:
   - Material requirements (type, grade, strength, manufacturer)
   - Installation requirements (methods, tolerances, sequencing)
   - Testing and inspection requirements (type, frequency, acceptance criteria)
   - Submittals required (shop drawings, samples, certifications)
   - Quality control requirements (QC procedures, hold points, witness tests)
   - Environmental restrictions (temperature, humidity, wind, rain)

3. **Produce annotated field spec sheet**:
   - Format as a 1-3 page document with section header, highlighted requirements, and margin annotations
   - Critical values highlighted with yellow background
   - Hold points marked with diamond symbol and "HOLD" label
   - Plain-language notes added as margin annotations explaining technical requirements
   - Approved products/manufacturers listed from submittal log
   - Plan sheet cross-references showing where requirements apply spatially

4. **Create annotation set** linking the spec annotations to the output document.

5. **Save** annotation records and set to `annotation-log.json`.

### Step 5: PHOTO — Photo Annotation

When the argument is `photo`:

1. **Identify the target photo**: Ask the user for the photo file or identify from context (punch list item reference, daily report photo, QC inspection photo).

2. **Determine annotation type**:
   - **Punch list photo**: Add numbered deficiency callout matching punch item ID, description box with deficiency text and responsible trade, location stamp, date stamp. Cross-reference with `punch-log.json`.
   - **QC inspection photo**: Add verification marks (checkmark for pass, X for fail), measurement overlays with actual vs. required values, spec reference annotation.
   - **Progress photo**: Add work area labels, completion percentage indicators, directional arrows for work sequence.
   - **Before/after comparison**: Create side-by-side layout with "BEFORE" (red banner) and "AFTER" (green banner) labels, deficiency marks on before, acceptance marks on after.

3. **Generate annotation specification**:
   - List each annotation element with position (relative to image dimensions), content, color, and size
   - Provide Pillow (PIL) code commands for applying annotations if Python is available
   - Describe the visual output so the user can verify intent before generation

4. **Save annotation records** to `annotation-log.json` with `annotation_type: "photo_markup"`.

### Step 6: RFI — RFI Drawing Markup

When the argument is `rfi`:

1. **Identify the RFI**: Ask the user for the RFI number or identify from context. Cross-reference with `rfi-log.json` for RFI details, referenced drawings, and question text.

2. **Identify referenced sheets**: Determine which drawing sheets are referenced by the RFI. Locate source PDFs.

3. **Generate RFI markup elements**:
   - **Question area cloud**: Magenta revision cloud around the area in question on the referenced sheet
   - **RFI label**: "RFI-[NUMBER]" text with leader line pointing to the cloud
   - **Dimension callouts**: Key dimensions relevant to the RFI question highlighted in red
   - **Conflict indication**: If the RFI involves a conflict, both conflicting elements highlighted with contrasting colors and labeled
   - **Spec reference**: Annotation noting the relevant spec section
   - **Proposed solution**: If the superintendent has a proposed resolution, annotate in green with "PROPOSED" label
   - **Photo reference**: If field photos exist, add "SEE ATTACHED PHOTO" annotation

4. **Create RFI markup package** as an annotation set containing:
   - Annotated plan sheet(s)
   - Annotated detail/section views if applicable
   - Annotated field photos if applicable
   - Annotation legend

5. **Save annotation records** with `linked_items.rfi` set to the RFI number.

6. **Note for rfi-preparer**: Instruct the user to reference the annotation set ID when completing the RFI through the `/rfi` command.

### Step 7: Save and Update Version History

After any data modification:

1. Write updated `annotation-log.json` to the project data directory.

2. Add version history entry to each new or modified annotation:
   ```json
   {
     "version": 1,
     "date": "YYYY-MM-DD",
     "action": "created",
     "by": "superintendent name from project-config",
     "notes": "description of annotation purpose"
   }
   ```

3. Confirm the save with a summary:
   - New annotations added (with IDs and types)
   - Annotation sets created or updated
   - Layer summary (count of annotations per layer)
   - Linked items (RFIs, punch items, daily reports referenced)

4. Note integration implications:
   - RFI markup created? Flag for `/rfi` command
   - Punch list markup created? Flag for punch-list tracking
   - As-built markup? Flag for drawing-control revision tracking
   - Work area markup? Flag for daily-report reference

## Integration Points

This command connects to other ForemanOS commands and skills:

- **`/rfi`** — RFI markup packages cross-reference annotation set IDs; annotated drawings attach to RFI submissions
- **`/punch`** — Punch list photo annotations cross-reference punch item IDs; annotated plans show punch locations spatially
- **`/daily-report`** — Work area markup provides annotated plan references for daily report documentation
- **`/drawings`** — Annotation version tracking linked to drawing revision control; as-built markups tracked through revision cycle
- **`/bim`** — Clash location markups generated from BIM coordination data; deviation markers from field verification
- **`/look-ahead`** — Work area annotations aligned with look-ahead schedule activities
- **`/inspections`** — Hold point annotations and QC mark placement linked to inspection tracking

## Example Usage

- `/annotate` — Show recent annotation summary and activity dashboard
- `/annotate plan` — Mark up a plan sheet (prompts for sheet and markup type)
- `/annotate plan mark Level 3 mechanical work area for next week, hold zone at grid C-4 pending RFI-042` — Generate work area and hold zone markup with context
- `/annotate spec` — Extract and annotate spec section for trade distribution
- `/annotate spec concrete field spec sheet for Division 3 pour requirements` — Generate annotated concrete field spec sheet
- `/annotate photo` — Annotate a construction photo (prompts for photo and type)
- `/annotate photo punch item 47 in Room 305, cracked drywall at door frame` — Annotate punch list deficiency photo
- `/annotate rfi` — Create RFI drawing markup package
- `/annotate rfi RFI-042 duct conflict at grid C-4 Level 3` — Generate RFI markup for specific RFI with context
