---
description: Environmental compliance and LEED tracking
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [leed|swppp|hazmat|waste|report]
---

# Environmental Compliance Command

## Overview

Environmental compliance management for construction superintendents. Track LEED v4.1 construction credits, conduct and document SWPPP inspections, log hazardous materials events, track waste diversion rates, manage dust/noise monitoring, and generate professional environmental compliance reports.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/environmental-compliance/SKILL.md` — Full environmental compliance system: LEED, SWPPP, hazmat, waste, dust, noise, incidents
- `${CLAUDE_PLUGIN_ROOT}/skills/environmental-compliance/references/leed-construction-guide.md` — LEED v4.1 BD+C construction-phase credit details
- `${CLAUDE_PLUGIN_ROOT}/skills/environmental-compliance/references/hazmat-awareness-guide.md` — Hazardous materials field procedures and identification
- `${CLAUDE_PLUGIN_ROOT}/skills/environmental-compliance/references/bmp-field-guide.md` — BMP installation and maintenance specifications
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `environmental-log.json` (LEED credits, SWPPP inspections, waste tracking, hazmat events, dust/noise, incidents)
- `schedule.json` (current phase — determines which environmental activities are relevant)
- `specs-quality.json` (environmental spec requirements, if extracted)
- `directory.json` (subcontractors and haulers)

If no project config: "No project set up yet. Run `/set-project` first."

If `environmental-log.json` does not exist, create it with the schema from the environmental-compliance SKILL.md, populated with project basics from `project-config.json`.

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"leed"** — Track LEED credit status, log product VOC data, update waste diversion for LEED, review documentation completeness
- **"swppp"** — Conduct and document a SWPPP inspection, log corrective actions, review inspection history
- **"hazmat"** — Log a hazardous materials event (asbestos discovery, lead paint finding, mold, contaminated soil, spill)
- **"waste"** — Enter waste hauling weight tickets, calculate diversion rates, update monthly tracking
- **"report"** — Generate environmental compliance report (summary of all environmental data for a period)

If no sub-action provided, show usage:
```
Usage: /environmental [leed|swppp|hazmat|waste|report]
Examples:
  /environmental leed              → Review LEED credit status and documentation gaps
  /environmental leed voc          → Log a product VOC entry for low-emitting materials tracking
  /environmental swppp             → Conduct a SWPPP inspection (guided checklist)
  /environmental swppp corrective  → Log a corrective action for a SWPPP deficiency
  /environmental hazmat            → Log a hazardous materials event
  /environmental hazmat spill      → Log an environmental spill incident
  /environmental waste             → Enter waste weight tickets and calculate diversion rate
  /environmental waste monthly     → Generate monthly waste diversion summary
  /environmental report            → Generate environmental compliance summary report
  /environmental report monthly    → Generate monthly environmental compliance report
```

### Step 3: LEED Sub-Action

Manage LEED construction-phase credit tracking:

1. **Status Review** (`/environmental leed`):
   - Display all tracked LEED credits with current status (in_progress, on_track, at_risk, complete)
   - Show current waste diversion rate vs. target
   - Flag documentation gaps (missing photos, weight tickets, product data)
   - List upcoming documentation deadlines

2. **VOC Product Entry** (`/environmental leed voc`):
   - Collect product info: name, manufacturer, category (paint, adhesive, sealant, flooring)
   - Collect VOC content (g/L) from product data sheet
   - Compare against LEED limit for category
   - Flag non-compliant products BEFORE installation
   - Save to `environmental-log.json` leed.product_tracking array
   - Auto-calculate compliance percentage by category

3. **EPD/HPD Tracking** (`/environmental leed epd`):
   - Log products with Environmental Product Declarations or Health Product Declarations
   - Track toward LEED MR Credit: Building Product Disclosure
   - Save to product_tracking with epd/hpd flags

4. **IAQ Status** (`/environmental leed iaq`):
   - Review IAQ management checklist status
   - Document duct protection, material storage, filter status
   - Schedule flush-out or IAQ testing pre-occupancy

Auto-assign IDs for product entries. Save all updates to `environmental-log.json`.

### Step 4: SWPPP Sub-Action

Conduct and document SWPPP inspections:

1. **Inspection** (`/environmental swppp`):
   - Determine inspection type: routine_weekly, post_storm, or special
   - If post_storm: collect rainfall amount (inches in 24 hours)
   - Walk through SWPPP inspection checklist items from the environmental-compliance skill
   - For each BMP category: pass/deficiency noted
   - Document findings with description
   - If deficiencies found: create corrective action entries with responsible party and deadline
   - Collect photo references
   - Auto-assign ID: `SWPPP-INS-NNN` (increment from highest existing)
   - Save to `environmental-log.json` swppp.inspections array

2. **Corrective Action** (`/environmental swppp corrective`):
   - Display open corrective actions from previous inspections
   - Update status: in_progress, completed
   - Log completion date and verification notes
   - Attach verification photos

3. **History** (`/environmental swppp history`):
   - Display recent SWPPP inspections (last 30 days)
   - Show inspection frequency compliance (weekly + post-storm)
   - Flag any gaps in inspection schedule
   - Show corrective action closure rate

### Step 5: HAZMAT Sub-Action

Log hazardous materials events:

1. **Event Logging** (`/environmental hazmat`):
   - Collect event type: asbestos_survey, asbestos_disturbance, lead_found, lead_abatement, mold_discovery, contaminated_soil, silica_exposure, other
   - Collect date, location, description
   - Collect action taken and current status
   - For spills: collect material, quantity, media affected, agencies notified, cleanup status
   - Reference the hazmat-awareness-guide for proper response procedures
   - Auto-assign ID: `HAZMAT-NNN` or `ENV-INC-NNN` (for spill incidents)
   - Save to `environmental-log.json` hazmat.events or incidents array

2. **Spill Incident** (`/environmental hazmat spill`):
   - Guided data collection per the environmental incident response section of the skill
   - Material, quantity, location, cause, media affected
   - Response actions taken (containment, cleanup, notification)
   - Determine if reportable (compare against CERCLA RQ thresholds from skill)
   - If reportable: confirm agencies notified (NRC, state, local)
   - Document cleanup verification and waste disposal
   - Root cause analysis and corrective actions
   - Save to `environmental-log.json` incidents array

3. **Training Record** (`/environmental hazmat training`):
   - Log hazmat awareness training events
   - Topic, date, attendees, trainer
   - Save to `environmental-log.json` hazmat.training_records array

### Step 6: WASTE Sub-Action

Track construction waste management:

1. **Weight Ticket Entry** (`/environmental waste`):
   - Collect hauling data: date, hauler, material type, weight (tons), destination (recycler or landfill)
   - Auto-calculate running monthly totals by stream
   - Auto-calculate monthly and cumulative diversion rates
   - Flag if diversion rate drops below project target
   - Save to `environmental-log.json` waste_management.monthly_tracking

2. **Monthly Summary** (`/environmental waste monthly`):
   - Generate monthly waste diversion summary table
   - Show each waste stream with tonnage
   - Calculate monthly diversion rate
   - Update cumulative project diversion rate
   - Compare against LEED target (50% or 75%)
   - Highlight streams with improvement opportunities

3. **Hauler Certification** (`/environmental waste hauler`):
   - Log hauler recycling facility certifications
   - Verify and document diversion capability
   - Save to `environmental-log.json` waste_management.hauler_certifications

### Step 7: REPORT Sub-Action

Generate environmental compliance reports:

1. Determine period: weekly (default) or monthly from arguments
2. Pull all environmental data for the period from `environmental-log.json`
3. Include:
   - **LEED Credit Status**: Current status of all tracked credits, diversion rate, documentation gaps
   - **SWPPP Compliance**: Inspections conducted, deficiencies found, corrective action closure rate, inspection frequency compliance
   - **Waste Diversion**: Monthly and cumulative diversion rates by stream, comparison to target
   - **Hazmat Events**: Any events during period, status, actions taken
   - **Dust/Noise Monitoring**: Readings, compliance status, any exceedances and mitigation
   - **Environmental Incidents**: Spills, releases, or other incidents
   - **Regulatory Compliance Summary**: Permit status, upcoming deadlines, training records
   - **Recommendations**: Based on data trends (areas needing attention)
4. Save to `{folder_mapping.ai_output}/{PROJECT_CODE}_Environmental_Report_{date}.docx`
5. Confirm file location to user

### Step 8: Save & Log

1. Write updated `environmental-log.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | environmental | [sub_action] | [ID or description]
   ```
3. If SWPPP deficiency or hazmat event logged, surface alert in next `/morning-brief`
4. If waste diversion rate drops below target, flag in next `/morning-brief`
5. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest environmental status

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces SWPPP inspection due dates, open corrective actions, environmental alerts, waste diversion status
- **Daily Report** (`/daily-report`): Environmental observations section (weather/BMP status, dust control, noise, waste hauling)
- **Weekly Report** (`/weekly-report`): Aggregates environmental metrics for the week
- **Dashboard** (`/dashboard`): Environmental compliance cards (SWPPP status, diversion rate, LEED credit progress)
- **Closeout** (`/closeout`): LEED documentation package, NOT filing, final waste diversion report
- **Safety** (`/safety`): Cross-reference hazmat events, silica exposure, spill response with safety incident tracking
- **Inspections** (`/inspections`): Environmental permits tracked alongside building permits
