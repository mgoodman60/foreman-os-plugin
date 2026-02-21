---
description: Track change orders and T&M tags
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [add/status/log] [details]
---

# Change Order Management Command

## Overview

Track change orders from initiation through resolution. This command enables construction superintendents to:
- **Add** new change orders with complete project intelligence
- **Update** CO status through the workflow (draft → submitted → under_review → approved/rejected/void)
- **Generate** professional CO Log documents for stakeholder distribution

Auto-populates project data, manages CO numbering, tracks cost and schedule impacts, and integrates with morning briefs, daily reports, and weekly summaries.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/change-order-tracker/SKILL.md` — Core CO lifecycle management, numbering, status workflow, cost/schedule tracking
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration, folder structure, team assignments
- `${CLAUDE_PLUGIN_ROOT}/skills/estimating-intelligence/SKILL.md` — Unit cost validation and pricing review for change order cost evaluation

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration
Load `project-config.json` for version_history and folder_mapping.
Load `change-order-log.json` for existing change orders.

If the config file is not found, inform the user:
> "Project configuration not found. Please run `/set-project` first to initialize your project structure."

### Step 2: Parse Arguments for Sub-Action
Examine `$ARGUMENTS` to determine which operation:
- **"add"** — Create a new change order
- **"status"** — Update an existing CO's status
- **"log"** — Generate and export CO Log document

If no sub-action provided, show usage:
```
Usage: /change-order [add/status/log] [details]
Examples:
  /change-order add
  /change-order status CO-001
  /change-order log
```

### Step 3: Process "add" Sub-Action
Collect CO details conversationally:
1. **CO Description**: What change is being requested?
2. **Originator**: Who initiated (owner/architect/field staff/subcontractor)?
3. **Affected Spec Sections**: Which specification sections are impacted?
4. **Cost Impact**: Estimate additional cost (or note as TBD)
5. **Schedule Impact**: Estimated days impact (or zero if none)
6. **Affected Subs**: Which subcontractors are involved?
7. **Linked Documents**: Any associated ASIs, RFIs, or RFQs?

**Auto-assign CO Number**: Query `change-order-log.json` for highest CO-NNN, increment by 1. Lock immediately.

**Store in `change-order-log.json`**:
```json
{
  "id": "CO-001",
  "description": "[user input]",
  "originator": "[owner|architect|field|sub]",
  "date_submitted": "[ISO 8601]",
  "status": "draft",
  "cost_impact": "[number|TBD]",
  "schedule_impact_days": "[number]",
  "affected_spec_sections": ["[section]"],
  "affected_subs": ["[sub name]"],
  "linked_asis": ["[ASI-NNN]"],
  "linked_rfis": ["[RFI-NNN]"],
  "approved_by": null,
  "resolution_date": null,
  "notes": ""
}
```

### Step 4: Process "status" Sub-Action
1. Display all current COs from `change-order-log.json` with status badges (draft | submitted | under_review | approved | rejected | void)
2. Prompt user to select a CO to update
3. Show current status and allow advancement:
   - **draft** → submitted
   - **submitted** → under_review
   - **under_review** → approved / rejected / void
4. Collect additional data:
   - **Approved Amount** (if approved): Final cost
   - **Approved By**: Project manager or owner name
   - **Resolution Notes**: Explanation or conditions
   - **Resolution Date**: When approved/rejected (auto-populated with today's date)
5. Update CO record and save to `change-order-log.json`

### Step 5: Process "log" Sub-Action
Generate a professional CO Log document (.docx format):
1. Extract all COs from `change-order-log.json` sorted by CO number
2. Create table with columns:
   - CO ID
   - Description
   - Originator
   - Date Submitted
   - Status (with visual badge)
   - Cost Impact
   - Schedule Impact (days)
   - Approved By
3. Include summary section:
   - Total CO Count by Status
   - Total Cost Impact (approved + pending)
   - Total Schedule Impact (days)
   - Cost by Originator
4. Save to `{{folder_mapping.change_orders}}/CO_Log_[YYYYMMDD].docx`
5. Confirm file location to user

### Step 6: Save & Log
1. Write updated `change-order-log.json`
2. Update `project-config.json` version_history with timestamp and action:
   ```
   [TIMESTAMP] | change-order | [sub-action] | [CO-NNN or "log generated"]
   ```
3. Confirm completion to user with summary of changes
4. If project data changed significantly, regenerate `CLAUDE.md` to reflect the latest project state

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces all COs with "pending" or "under_review" status
- **Daily Report** (`/daily-report`): Can reference associated COs in daily entries
- **Weekly Report** (`/weekly-report`): Includes CO summary section with status breakdown
- **ASI Tracker** (`/asis`): Auto-links related ASIs to COs
- **RFI Tracker** (`/rfis`): Auto-links related RFIs to COs

## Notes
- All CO numbers are immutable once assigned
- Cost impacts are tracked separately (estimate vs. approved amount)
- Schedule impacts accumulate and affect critical path
- CO Log is a read-only archive document; updates are captured separately
