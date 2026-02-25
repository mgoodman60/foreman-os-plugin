---
description: Risk register and mitigation tracking
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: [add|review|report|matrix]
---

# Risk Management Command

## Overview

Proactive risk management for construction superintendents and project managers. Add risks to the register, conduct monthly risk reviews with probability/impact re-assessment, generate risk reports with heat maps and trend analysis, and display the 5x5 risk matrix with current risks plotted.

## Skills Referenced
- `${CLAUDE_PLUGIN_ROOT}/skills/risk-management/SKILL.md` — Full risk management system: identification methods, 5x5 assessment framework, construction-specific categories, mitigation strategies, contingency management, weather/force majeure planning, monthly review process
- `${CLAUDE_PLUGIN_ROOT}/skills/project-data/SKILL.md` — Project configuration and data context
- `${CLAUDE_PLUGIN_ROOT}/skills/delay-tracker/SKILL.md` — Delay tracking integration (when risks materialize into delays)

**Output Skills**: See the `docx` Cowork skill for .docx report generation best practices.

## Execution Steps

### Step 1: Load Project Configuration

Search for project-data files in the user's working directory (check `AI - Project Brain/` first, then root):
- `project-config.json` (project_basics, folder_mapping)
- `risk-register.json` (risks, closed_risks, contingency_budget)
- `schedule.json` (current phase, active work types — for risk context)
- `directory.json` (subcontractors — for risk owner assignment)
- `delay-log.json` (existing delays — for cross-referencing materialized risks)

If no project config: "No project set up yet. Run `/set-project` first."

If no `risk-register.json` exists, initialize an empty one:
```json
{
  "risk_register": {
    "project_id": "[from project-config]",
    "last_updated": "[now]",
    "next_review_date": "[30 days from now]",
    "contingency_budget": {
      "original_allocation": 0,
      "current_remaining": 0,
      "drawdowns": []
    },
    "risks": [],
    "closed_risks": [],
    "version_history": []
  }
}
```

### Step 2: Parse Arguments for Sub-Action

Examine `$ARGUMENTS` to determine which operation:
- **"add"** — Add a new risk to the register (guided identification and assessment)
- **"review"** — Review and update existing risks (monthly risk review format)
- **"report"** — Generate risk report (top risks, heat map, contingency status, trend analysis)
- **"matrix"** — Display 5x5 risk matrix with current risks plotted by position

If no sub-action provided, show usage:
```
Usage: /risk [add|review|report|matrix]
Examples:
  /risk add                  → Add a new risk to the register
  /risk review               → Conduct monthly risk review (re-assess all active risks)
  /risk report               → Generate risk report with top risks, heat map, and trends
  /risk matrix               → Display 5x5 risk matrix with current risks plotted
```

### Step 3: ADD Sub-Action

Walk the user through risk identification and assessment conversationally:

1. **Category**: Which risk category? Present the 10 categories from the skill:
   - Site Conditions, Weather, Labor, Supply Chain, Regulatory, Design, Subcontractor, Financial, Force Majeure, Safety
2. **Description**: Clear, specific description of the risk event. Prompt for specificity: "What exactly could happen?"
3. **Root Cause**: What is driving this risk? What conditions make it possible?
4. **Probability**: Rate 1-5 using the probability scale. Show the scale definitions for reference.
5. **Impact**: Rate 1-5 using the impact scale. Assess both schedule and cost impact; use the higher rating.
6. **Score & Priority**: Calculate automatically (P x I). Announce the priority category (Low/Medium/High/Critical).
7. **Risk Owner**: Who is responsible for monitoring this risk? Resolve against directory.json if possible.
8. **Mitigation Strategy**: Select primary strategy (Avoidance, Transfer, Reduction, Acceptance). Use the decision framework from the skill.
9. **Mitigation Actions**: What specific actions will be taken? List 2-5 concrete actions.
10. **Contingency Plan**: What will the team do if the risk materializes despite mitigation?
11. **Trigger Conditions**: What observable conditions indicate this risk is materializing? List 1-3 triggers.
12. **Related Activities**: Which schedule activities are affected? Resolve against schedule.json.
13. **Cost Exposure**: Estimated cost impact in dollars if risk materializes.
14. **Schedule Exposure**: Estimated schedule impact in calendar days if risk materializes.

Auto-assign unique ID: `R-NNN` (increment from highest existing risk ID).

Calculate score and assign priority:
- 1-4: Low (Green)
- 5-9: Medium (Yellow)
- 10-15: High (Orange)
- 16-25: Critical (Red)

Save to `risk-register.json` in the `risks` array. Log to version_history.

If risk is Critical (16-25), alert: "This is a CRITICAL risk. Recommend immediate escalation to project leadership and daily monitoring until mitigation is in place."

### Step 4: REVIEW Sub-Action

Conduct a structured risk review following the monthly review meeting format:

1. **Summary Dashboard**: Display current risk register summary:
   - Total active risks by priority (Critical, High, Medium, Low)
   - Risks added since last review
   - Risks closed since last review
   - Risks that materialized since last review
   - Contingency status (remaining vs. original, burn rate vs. project % complete)

2. **Critical Risk Review**: For each Critical risk (score 16-25):
   - Display current risk details
   - Ask: "Has anything changed? Update probability? Impact? Status?"
   - If P or I changed, recalculate score and priority
   - Ask: "Are mitigation actions effective? Any new trigger conditions observed?"
   - Record review notes and updated assessment

3. **High Risk Review**: For each High risk (score 10-15):
   - Display current risk details
   - Ask for status update and P/I re-assessment
   - Record review notes

4. **Medium and Low Risk Quick Review**: Present list of Medium and Low risks.
   - Ask: "Any of these need attention or re-assessment?"
   - Update any flagged risks

5. **New Risk Identification**: Ask: "Are there any new risks to add? Consider:
   - Phase transitions in the next 30 days
   - Weather forecast concerns
   - Critical procurements approaching
   - Subcontractor mobilization issues
   - Recent RFIs or change orders that introduce risk"
   - If yes, walk through the ADD process for each new risk

6. **Risk Closure**: Ask: "Are any risks ready to close?" For risks where:
   - The risk event window has passed
   - The risk has been fully mitigated
   - The activity is complete and risk no longer applies
   - Move to `closed_risks` array with resolution date and notes

7. **Contingency Review**: Review contingency drawdowns and burn rate.
   - If burn rate exceeds healthy range, flag for attention.
   - Recommend contingency release for retired risk categories if appropriate.

Update `last_reviewed` date on all reviewed risks. Set `next_review_date` to 30 days from today. Save updated `risk-register.json`. Log review to version_history.

### Step 5: REPORT Sub-Action

Generate a comprehensive risk report:

1. **Report Period**: Determine reporting period (default: since last review; or specify date range from arguments).

2. **Report Contents**:
   - **Executive Summary**: Total risks, distribution by priority, key changes since last report
   - **Top 10 Risks Table**: Ranked by score, showing ID, category, description, P, I, score, priority, trend, owner
   - **Risk Heat Map**: 5x5 matrix with current risk IDs plotted in their P/I positions (ASCII format for terminal, or formatted for .docx)
   - **Contingency Status**: Original allocation, current remaining, drawdowns this period, burn rate assessment
   - **Trend Analysis**: Risk count trend, average score trend, contingency consumption trend (if multiple review cycles exist)
   - **Materialized Risks**: Any risks that became actual events, with outcome vs. predicted impact
   - **Newly Identified Risks**: Risks added since last report
   - **Closed Risks**: Risks retired since last report with resolution summary
   - **Upcoming Risk Windows**: Activities in next 30 days that involve High or Critical risks
   - **Recommendations**: Actions recommended based on current risk profile

3. **Output**:
   - Display summary in terminal
   - Save full report to `{folder_mapping.ai_output}/{PROJECT_CODE}_Risk_Report_{date}.docx`
   - Confirm file location to user

Log report generation to version_history.

### Step 6: MATRIX Sub-Action

Display the 5x5 risk matrix with all active risks plotted:

1. Load all active risks from `risk-register.json`.

2. Plot each risk by its probability (Y-axis) and impact (X-axis) position.

3. Display the matrix in ASCII format:
   ```
   RISK MATRIX — [Project Name] — [Date]
   Active Risks: [count] | Critical: [count] | High: [count] | Medium: [count] | Low: [count]

                             I M P A C T
                    1          2          3          4          5
                 Negligible   Minor    Moderate    Major    Critical
            +----------+----------+----------+----------+----------+
       5    |          |          |          | R-015    |          |
    Almost  |          |          |          |          |          |
    Certain |          |          |          |          |          |
            +----------+----------+----------+----------+----------+
       4    |          |          | R-007    | R-001    |          |
    Likely  |          |          | R-012    |          |          |
            |          |          |          |          |          |
   P        +----------+----------+----------+----------+----------+
   R   3    |          | R-009    | R-005    | R-003    |          |
   O Poss-  |          | R-011    | R-008    |          |          |
   B ible   |          |          |          |          |          |
   A        +----------+----------+----------+----------+----------+
   B   2    |          | R-010    | R-006    |          |          |
   I Unlikely|         |          |          |          |          |
   L        |          |          |          |          |          |
   I        +----------+----------+----------+----------+----------+
   T   1    |          |          |          |          |          |
   Y Rare   |          |          |          |          |          |
            |          |          |          |          |          |
            +----------+----------+----------+----------+----------+
   ```

4. Below the matrix, list each risk ID with its short description for reference:
   ```
   Risk Legend:
   R-001: Structural steel delivery delay (Supply Chain) — Score: 16 CRITICAL
   R-003: High water table at foundations (Site Conditions) — Score: 12 HIGH
   R-005: HVAC sub capacity concerns (Subcontractor) — Score: 9 MEDIUM
   ...
   ```

5. Include contingency summary line:
   ```
   Contingency: $185,000 remaining of $250,000 (74%) | Project 35% complete | Burn Rate: 1.06
   ```

### Step 7: Save & Log

1. Write updated `risk-register.json`
2. Update `project-config.json` version_history:
   ```
   [TIMESTAMP] | risk-management | [sub_action] | [R-NNN or "report generated" or "review completed" or "matrix displayed"]
   ```
3. If risk added with Critical priority, surface alert in next `/morning-brief`
4. If risk materialized, prompt user to create `/delay log` entry if schedule impact exists
5. If project data changed significantly, regenerate `CLAUDE.md` to reflect latest risk status

## Integration Points
- **Morning Brief** (`/morning-brief`): Surfaces top 3-5 risks relevant to today's planned work; weather risk alerts
- **Daily Report** (`/daily-report`): Risk events observed in field auto-suggest risk register updates
- **Weekly Report** (`/weekly-report`): Aggregates risk status summary for the week
- **Dashboard** (`/dashboard`): Risk KPI cards (total risks, critical count, contingency remaining, burn rate)
- **Delay Tracker** (`/delay`): Materialized risks cross-link to delay log entries
- **Cost Tracking** (`/cost`): Contingency drawdowns reflected in cost tracking; budget risk alerts
- **Change Orders** (`/change-order`): Change events evaluated for new risk introduction
- **Last Planner** (`/last-planner`): Low PPC triggers risk review; constraints map to risk register
