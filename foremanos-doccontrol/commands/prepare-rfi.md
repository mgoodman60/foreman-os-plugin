---
description: Draft RFIs with auto-filled references
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [topic description, or "transmittal"]
---

## Overview
Draft RFIs and transmittals efficiently by auto-populating project intelligence. This command generates professional documents with correct numbering, team routing, and spec/drawing references resolved automatically.

**Skills Referenced:**
- `${CLAUDE_PLUGIN_ROOT}/skills/rfi-preparer/SKILL.md` - RFI methodology and templates
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` - Project team and configuration
- If available, the `pdf` Cowork skill for PDF creation and form filling when generating RFI documents

## Execution Steps

### 1. Determine Document Type
- Check if `$ARGUMENTS` contains "transmittal" → create Transmittal
- Otherwise → create RFI
- If no argument provided, ask user which type they need

### 2. Get Next Sequential Number
- For **RFI**: Query `rfi-log.json`, find highest RFI number, assign RFI-[N+1]
- For **Transmittal**: Query `submittal-log.json`, find highest transmittal number, assign TRANS-[N+1]
- Display assigned number to user

### 3. Gather Issue Description
- If topic provided in `$ARGUMENTS`: use as starting point
- Otherwise: ask user "What is the question/issue you need clarification on?"
- Encourage specificity with examples:
  - RFI example: "Clarification needed on door schedule coordination with MEP rough-in"
  - Transmittal example: "Submitting mechanical equipment schedule for approval"

### 4. Auto-Resolve Location References
Use drawing-reference-resolution to:
- Parse location references in description (room numbers, grid coordinates, page numbers)
- Cross-reference against `plans-spatial.json` (drawing_references, room_schedule, grid_lines, building_areas)
- Auto-complete ambiguous references
- Suggest correct drawing reference format if needed
- Example: "room 202" → "Room 202 (Floor 2, Grid B3, Drawing A-101)"

### 5. Auto-Resolve Spec Section References
- Parse any spec section references mentioned
- Cross-reference against `specs-quality.json` (spec_sections)
- Auto-complete section numbers and titles
- Link to relevant spec content
- Example: "hardware schedule" → "Division 08 71 00 Hardware Specification (Section 3.1)"

### 6. Auto-Fill Project Team
Load from `project-config.json` (project_basics):
- **From** (Preparer): Logged-in user or GC contact
- **To** (Recipients):
  - For RFI: Architect and Owner per contractual requirements
  - For Transmittal: Contractor/Subcontractor based on scope
- **Cc**: Distribution list from project_basics or contract_team

### 7. Draft Professional Document Text
Based on document type:

**For RFI:**
- Issue/Question statement (clear, specific)
- Background context (drawings, specs, schedule affected)
- Impact assessment (cost, schedule, scope implications)
- Specific information requested
- Proposed deadline for response
- Reference attachments (drawings, submittals, specs)

**For Transmittal:**
- Document being transmitted and purpose
- Submission status (for information, for approval, for review)
- List of items enclosed (item count, descriptions)
- Spec sections and drawings referenced
- Requested actions/approval timeline
- Any special handling or storage requirements

### 8. Present to User for Review and Editing
Display formatted document with:
- Header: Document number, date, project info
- Body: Drafted text
- Footer: Routing information, distribution list
- Edit capabilities:
  - **Edit text**: Refine language and details
  - **Add attachment**: Link drawings, spec excerpts, submittals
  - **Change recipients**: Modify To/Cc list if needed
  - **Preview**: See formatted version

### 9. Save as Draft
Store in appropriate log as "draft" status:
- **For RFI**: Add entry to `rfi-log.json` with status "Draft - Pending Review"
- **For Transmittal**: Add entry to `submittal-log.json` transmittal section with status "Draft"
- Save editable version to project files
- Record date created, draft version number

### 10. Export and Distribution Options
Once finalized:
- **Export as PDF**: Generate {PROJECT_CODE}_{RFI-number or TRANS-number}_{date}.pdf — save to `folder_mapping.rfis` for RFIs or `folder_mapping.submittals` for transmittals. Fall back to the user's output folder if folder_mapping is not populated.
- **Change status to**: "Issued" (update `rfi-log.json` or `submittal-log.json` in `folder_mapping.ai_output`)
- **Email routing**: Remind user of standard recipients and approval chain
- **Print option**: Format for hardcopy distribution if needed
- **Track**: Update log with issue date when sent

### 11. Save & Log
1. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | prepare-rfi | [RFI or transmittal] | [document number]
   ```
