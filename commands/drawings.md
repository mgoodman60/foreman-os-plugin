---
description: Drawing revision control and distribution
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [status|add|revise|asi|audit|search|distribute]
---

# Drawing Control Command

## Overview

Central drawing management for construction projects. Track every revision, process Architect/Engineer Supplemental Instructions (ASIs), maintain current set verification, audit field documentation against the drawing log, control distribution, and extract revision cloud summaries. Prevents costly rework by ensuring the field always works from the latest approved drawings.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/drawing-control/SKILL.md` — Full drawing control system: revision tracking, ASI processing, current set verification, field audits, distribution control, change summaries
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `drawing-log.json` (drawings array, summary, revision history, distribution logs)
- `rfi-log.json` (for cross-referencing drawing references in RFIs)
- `submittal-log.json` (for cross-referencing drawing references in submittals)
- `daily-report-data.json` (for field audit — checking drawing references in reports)

If no project config: "No project set up yet. Run `/set-project` first."

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"status"** — Display current drawing set by discipline with revision and distribution status
- **"add"** — Register a new drawing in the log
- **"revise"** — Record a new revision for an existing sheet
- **"asi"** — Process an ASI and update all affected sheets
- **"audit"** — Compare field documentation against current drawing set
- **"search"** — Search drawing log by sheet number, title, or keyword
- **"distribute"** — Generate or update distribution records for a drawing revision

If no sub-action provided, show usage:
```
Usage: /drawings [status|add|revise|asi|audit|search|distribute]
Examples:
  /drawings status              → View current set by discipline
  /drawings status --discipline Arch → Architectural sheets only
  /drawings add                 → Register a new drawing
  /drawings revise A-101        → Record new revision for A-101
  /drawings asi ASI-003         → Process ASI-003 and update sheets
  /drawings audit               → Audit field docs against current set
  /drawings search "door"       → Search by keyword
  /drawings distribute A-101    → Update distribution for A-101
```

### Step 3: STATUS Sub-Action

Display the current drawing set:

1. Load `drawing-log.json`
2. Group drawings by discipline (General, Civil, Arch, Struct, Mech, Plumb, Elec, Fire)
3. For each sheet show: sheet number, title, current revision, revision date, distribution status
4. Support filter by discipline via `--discipline` argument
5. Show summary: total sheets, revision distribution, void/superseded count, last update date
6. Flag any sheets with pending distribution or unconfirmed receipts

### Step 4: ADD Sub-Action

Register a new drawing:

Collect details:
1. **Sheet Number**: Standard format (e.g., A-101)
2. **Title**: Drawing title
3. **Discipline**: Arch, Struct, Civil, Mech, Elec, Plumb, Fire, General
4. **Revision**: Initial revision (typically Rev 0)
5. **Received From**: Architect/engineer firm name
6. **File Path**: Path to the drawing PDF
7. **Notes**: Any additional context

Validate: check for duplicate sheet numbers, verify naming convention.

Auto-assign drawing ID. Save to `drawing-log.json` drawings array. Update summary counts.

### Step 5: REVISE Sub-Action

Record a new revision for an existing sheet:

1. Parse sheet number from arguments
2. Look up existing drawing in log
3. Collect:
   - New revision number (auto-increment from current)
   - Description of changes
   - ASI reference (if applicable)
   - Date received
   - Received from
   - File path to new revision
   - Distribution list (who needs new copies)
4. Automatically:
   - Mark previous revision as superseded with reason
   - Extract revision cloud summary if available
   - Queue distribution notification
   - Update project-config.json ASI log if ASI-linked

### Step 6: ASI Sub-Action

Process an ASI and update all affected sheets:

1. Parse ASI number from arguments
2. Collect:
   - Date received
   - Issued by (architect/engineer)
   - Sheets affected (comma-separated list)
   - Description of changes
   - File paths to revised drawings
3. For each affected sheet:
   - Increment revision number
   - Mark prior revision as superseded
   - Extract change summary
   - Update ASI tracking table
4. Generate distribution notice listing all changed sheets
5. Trigger re-distribution to field team

### Step 7: AUDIT Sub-Action

Compare field documentation against current drawing set:

1. Parse date range from arguments (default: last 7 days)
2. Scan `daily-report-data.json` for drawing references
3. Scan `rfi-log.json` for drawing references
4. Scan `submittal-log.json` for drawing references
5. Compare each reference against `drawing-log.json` current revisions
6. Flag any references to superseded revisions:
   - Document, date, sheet referenced, current revision vs. referenced revision
   - Recommended action (notify crew, collect void sheets)
7. Report findings: total documents scanned, issues found, actions needed

### Step 8: SEARCH Sub-Action

Search the drawing log:

1. Parse search term from arguments
2. Search across: sheet number, title, discipline, notes, revision descriptions
3. Support filters: `--discipline`, `--revision`, `--status`
4. Display matching results with key metadata

### Step 9: DISTRIBUTE Sub-Action

Manage drawing distribution:

1. Parse sheet number from arguments
2. Display current distribution list with confirmation status
3. Allow:
   - Add new recipients
   - Record receipt confirmations
   - Flag unconfirmed distributions for follow-up
   - Generate re-distribution notice

### Step 10: Save & Log

1. Write updated `drawing-log.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | drawings | [sub_action] | [sheet numbers or ASI number]
   ```
3. If new revisions issued, surface in next `/morning-brief` as drawing alerts
4. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest drawing status

## Integration Points
- **Morning Brief** (`/morning-brief`): New revisions pending distribution, unconfirmed receipts, superseded sheet alerts
- **Daily Report** (`/daily-report`): Drawing references validated against current set
- **RFI** (`/prepare-rfi`): Auto-populates current revision when referencing drawings
- **Submittal Review** (`/submittal-review`): Cross-references drawing details against submittal specs
- **Look-Ahead** (`/look-ahead`): Tracks drawing deliverable dates
- **Dashboard** (`/dashboard`): Drawing revision timeline, distribution pending count
- **Quality** (`/quality`): Checklist references validated against current drawing revisions
