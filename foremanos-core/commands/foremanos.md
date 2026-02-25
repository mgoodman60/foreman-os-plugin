---
description: ForemanOS plugin directory and install guide
allowed-tools: Read
argument-hint: (none — displays plugin directory)
---

# ForemanOS Plugin Directory

Display the full ForemanOS plugin ecosystem with descriptions, command mappings, and recommended install sets.

## Plugin Overview

| Plugin | Description | Commands |
|--------|-------------|----------|
| **foremanos-core** | Project setup, data browsing, dashboards, morning briefings, rendering, and site context. Install first — backbone for all ForemanOS plugins. | `/set-project`, `/data`, `/morning-brief`, `/dashboard`, `/render`, `/site-context`, `/foremanos` |
| **foremanos-intel** | Extract intelligence from construction plans, specs, schedules, and contracts. Three-pass extraction, DWG/DXF parsing, quantitative takeoffs. | `/process-docs`, `/process-dwg` |
| **foremanos-field** | Daily reporting, safety, quality, inspections, labor tracking, and punch lists. Includes 21 field-reference trade guides. | `/log`, `/daily-report`, `/amend-report`, `/safety`, `/quality`, `/inspections`, `/labor`, `/punch-list` |
| **foremanos-planning** | Scheduling, look-aheads, Last Planner System, weekly reports, material tracking, and meeting minutes. | `/look-ahead`, `/plan`, `/schedules`, `/weekly-report`, `/material-tracker`, `/meeting-notes` |
| **foremanos-doccontrol** | RFI preparation, submittal reviews, drawing control, document annotation, and BIM coordination. | `/prepare-rfi`, `/submittal-review`, `/drawings`, `/annotate`, `/bim` |
| **foremanos-cost** | Cost tracking, earned value, pay applications, change orders, delay documentation, and claims management. | `/cost`, `/evm`, `/pay-app`, `/change-order`, `/delay`, `/claims` |
| **foremanos-compliance** | Risk registers, environmental compliance, project closeout, commissioning, subcontractor scorecards, and conflict detection. | `/risk`, `/environmental`, `/closeout`, `/conflicts`, `/sub-scorecard` |

## Recommended Install Sets

| Use Case | Plugins |
|----------|---------|
| **Getting started** | foremanos-core |
| **Daily field ops** | foremanos-core + foremanos-field |
| **Full field + planning** | foremanos-core + foremanos-field + foremanos-planning |
| **Document processing** | foremanos-core + foremanos-intel |
| **Complete superintendent** | All 7 plugins |

## Command → Plugin Mapping

| Command | Plugin |
|---------|--------|
| `/set-project` | foremanos-core |
| `/data` | foremanos-core |
| `/morning-brief` | foremanos-core |
| `/dashboard` | foremanos-core |
| `/render` | foremanos-core |
| `/site-context` | foremanos-core |
| `/foremanos` | foremanos-core |
| `/process-docs` | foremanos-intel |
| `/process-dwg` | foremanos-intel |
| `/log` | foremanos-field |
| `/daily-report` | foremanos-field |
| `/amend-report` | foremanos-field |
| `/safety` | foremanos-field |
| `/quality` | foremanos-field |
| `/inspections` | foremanos-field |
| `/labor` | foremanos-field |
| `/punch-list` | foremanos-field |
| `/look-ahead` | foremanos-planning |
| `/plan` | foremanos-planning |
| `/schedules` | foremanos-planning |
| `/weekly-report` | foremanos-planning |
| `/material-tracker` | foremanos-planning |
| `/meeting-notes` | foremanos-planning |
| `/prepare-rfi` | foremanos-doccontrol |
| `/submittal-review` | foremanos-doccontrol |
| `/drawings` | foremanos-doccontrol |
| `/annotate` | foremanos-doccontrol |
| `/bim` | foremanos-doccontrol |
| `/cost` | foremanos-cost |
| `/evm` | foremanos-cost |
| `/pay-app` | foremanos-cost |
| `/change-order` | foremanos-cost |
| `/delay` | foremanos-cost |
| `/claims` | foremanos-cost |
| `/risk` | foremanos-compliance |
| `/environmental` | foremanos-compliance |
| `/closeout` | foremanos-compliance |
| `/conflicts` | foremanos-compliance |
| `/sub-scorecard` | foremanos-compliance |

## Agents

| Agent | Plugin | Domain |
|-------|--------|--------|
| superintendent-assistant | foremanos-core | Top-level router and coordinator |
| project-data-navigator | foremanos-core | Natural language data queries |
| dashboard-intelligence-analyst | foremanos-core | Dashboards and executive briefings |
| project-health-monitor | foremanos-core | KPI monitoring and alerts |
| doc-orchestrator | foremanos-intel | Document extraction pipeline |
| data-integrity-watchdog | foremanos-intel | Data store validation |
| conflict-detection-agent | foremanos-intel | Cross-discipline conflict detection |
| field-intelligence-advisor | foremanos-field | Contextual field briefings |
| report-quality-auditor | foremanos-field | Report QA (10 daily + 6 weekly checks) |
| weekly-planning-coordinator | foremanos-planning | Last Planner System cycle |
| deadline-sentinel | foremanos-planning | Deadline monitoring across all data |

## Notes

- **foremanos-core is required** — all other plugins depend on the project-data skill it provides
- Plugins use skill stubs to reference data patterns from other plugins without requiring them to be installed
- Run `/foremanos` at any time to see this directory
