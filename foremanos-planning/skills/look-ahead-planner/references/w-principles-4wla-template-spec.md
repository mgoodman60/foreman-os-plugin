# W Principles 4WLA Template Specification

This document is the authoritative specification for the W Principles 4-Week Look-Ahead (4WLA) Excel template. Use this when the actual template file (`AI - Project Brain/Templates/3WLA TEMPLATE.xlsx`) cannot be opened (e.g., OneDrive sync placeholder).

> **Template file**: `3WLA TEMPLATE.xlsx` (located in `AI - Project Brain/Templates/`)
> **Preferred approach**: Load and clone the actual .xlsx template, then populate with data. Only fall back to this spec if the file is unreadable.

---

## Sheet Structure

Single sheet ("Sheet1"). Dimensions: B1:AL123.

### Column Layout

| Range | Purpose | Width |
|-------|---------|-------|
| A | Spacer | 4.1 |
| B:I | Description of Work (merged per row) | B=8.4, C=5.6, G=7.1, H=5.6, I=15.4 |
| J:P | Week 1 days (M T W TH F Sa Su) | J=7.1, K=7.6, others default |
| Q:W | Week 2 days (M T W TH F Sa Su) | Q=7.6, S=7.9, U=7.9 |
| X:AD | Week 3 days (M T W TH F Sa Su) | X=7.9, Y=7.9, AC=7.9, AD=7.6 |
| AE:AK | Week 4 days (M T W TH F Sa Su) | AE=6.7, AJ=6.7 |
| AL | Notes | 47.6 |

### Row Layout

| Row(s) | Purpose | Formatting |
|--------|---------|------------|
| 1-3 | Company header (logo, project name, dates, PM/Super) | Merged ranges: B1:I1, J1:AC1, B2:I2, AF2:AI2, B3:I3, J3:U3, W3:AD3, AG3:AI3 |
| 4-9 | Spacer rows | Empty |
| 10-11 | Title: "4WLA TEMPLATE" (or "4WLA {PROJECT_CODE}") | B10:I11 merged, Bold, 18pt Calibri, center/center aligned |
| 12 | Spacer | Empty |
| 13 | Column headers | B13:I14="Description of Work" (merged, bold), J13:AK13="Dates" (merged, bold), AL13:AL14="Notes" (merged, bold). All have thin borders and shaded background. |
| 14 | Day abbreviations | M, T, W, TH, F, Sa, Su repeated 4 times. 11pt Calibri, centered. Sa/Su columns have shaded fill. F columns (N, U, AB, AI) have thick right border (week separator). |
| 15 | **Section 1 date header** | Dates for all 28 days. 10pt Calibri, centered, shaded fill, thin borders. Bold. Row height 15.75. |
| 16-19 | Section 1 activity rows (4 rows) | B:I merged per row, thin borders top/bottom. |
| 20 | **Section 2 date header** | Same as row 15. Row height 15.75. |
| 21-27 | Section 2 activity rows (7 rows) | B:I merged per row. |
| 28 | **Section 3 date header** | Same as row 15. Row height 15.75. |
| 29-32 | Section 3 activity rows (4 rows) | B:I merged per row. |
| 33 | **Section 4 date header** | Same as row 15. Row height 15.75. |
| 34-38 | Section 4 activity rows (5 rows) | B:I merged per row. |
| 39 | Separator row | J39:R39 merged (section label, bold). |
| 40 | **Action Items header** | B40:I40="Action Items" (bold, shaded), J40:L40="Project" (bold, centered, shaded), N40="Responsible" (bold, shaded), R40:T40="Complete By" (bold, centered, shaded), V40:X40="Status" (bold, centered, shaded). All have top/thin border. |
| 41 | Separator row | 7.5 row height. |
| 42-52 | Action item rows | Columns: B:I (item), J:L (project), N:P (responsible), R:T (due date), V:X (status). All merged per column group. |
| 53-123 | Extended activity rows | B:I merged per row. Available for additional activities or overflow. |

### Image

1 embedded image (company logo) in the header area (rows 1-9). The logo should be placed near cell B1.

---

## Formatting Details

### Font
- **Primary**: Calibri throughout
- **Title (row 10)**: 18pt, Bold
- **Headers (rows 13-14, 40)**: 11pt, Bold
- **Date header rows (15, 20, 28, 33)**: 10pt, Bold
- **Activity rows**: 11pt, regular
- **Day abbreviation cells**: 11pt, centered

### Borders
- **Friday columns** (N, U, AB, AI): Thick right border — this is the week separator
- **Sa/Su to next M**: Thin right border on Su columns (P, W, AD, AK)
- **Interior day columns**: Hair right border
- **Date header rows**: Thin top/bottom borders
- **Activity rows**: Thin top/bottom borders on B:I cells
- **Action Items section**: Thin top border on header row

### Fills (Shading)
- **Saturday and Sunday columns** (O, P, V, W, AC, AD, AE, AJ, AK): Shaded background fill (light gray)
- **Wednesday columns** (L, S, Z, AG): Shaded background fill (lighter)
- **Date header rows** (15, 20, 28, 33): Shaded background on all date cells
- **Column headers** (row 13): Shaded background
- **Day abbreviation row** (14): Sa/Su and W columns shaded
- **Action Items header** (row 40): Shaded background

### Color Coding for Activity Bars
When populating activity bars across day columns:
- **Critical path**: Red fill (#DC3545)
- **Near-critical (1-5 days float)**: Amber fill (#FFC107)
- **Normal/On-track (6+ days float)**: Blue fill (#2E5EAA)
- **Completed**: Green fill (#28A745)
- **Weather-blocked**: Gray fill (#6C757D)

### Alignment
- **Description of Work** (B:I): Left-aligned, vertical center
- **Day abbreviations and dates**: Horizontal center
- **Notes column** (AL): Left-aligned, wrap text
- **Title**: Horizontal center, vertical center

---

## Date Population

All 4 date header rows (15, 20, 28, 33) contain the same set of 28 consecutive dates starting from the Monday of the current work week. The dates span columns J through AI (4 weeks x 7 days = 28 columns).

Date format in cells: Excel date values formatted as short date (displays as M/D or similar).

**Week boundaries**:
- Week 1: J-P (Mon-Sun)
- Week 2: Q-W (Mon-Sun)
- Week 3: X-AD (Mon-Sun)
- Week 4: AE-AK (Mon-Sun)

---

## Activity Row Usage

### Section Groupings (recommended)
The 4 sections can be used to group activities by trade category or phase:
- **Section 1** (rows 16-19): Sitework / Earthwork / Foundations
- **Section 2** (rows 21-27): Structural / Framing / Envelope
- **Section 3** (rows 29-32): MEP / Rough-ins
- **Section 4** (rows 34-38): Finishes / Misc / Milestones

These groupings are flexible — adapt to the current project phase.

### Extended Rows (53-123)
When more than 20 activities are needed, use the extended activity rows (53-123). These follow the same B:I merged format but do not have repeated date headers. The day columns (J-AK) should be formatted consistently with the main sections above.

### Activity Bar Rendering
For each activity in the lookahead window:
1. Write the activity description in the B:I merged cell
2. For each day the activity is scheduled, fill the corresponding day column cell with the appropriate status color
3. Optionally add a short text label in the first day cell (e.g., "Start" or crew count)

---

## Action Items Section

Row 40 headers, rows 42-52 data. Use this section to list blockers, pending decisions, and coordination items. Each row has:
- **B:I** — Action item description
- **J:L** — Project identifier
- **N:P** — Responsible party
- **R:T** — Target completion date
- **V:X** — Status (Open / In Progress / Complete / Blocked)

---

## Output File Naming and Location

**File name**: `{PROJECT_CODE}_4WLA_{YYYY-MM-DD}.xlsx`
**Example**: `MOSC_4WLA_2026-02-20.xlsx`

**Save location priority**:
1. `folder_mapping.schedules` (e.g., `09 - Schedule/`)
2. `folder_mapping.ai_output` (e.g., `AI - Project Brain/`)
3. Working directory root

This ensures the 4WLA is saved directly to the local project folder and doesn't depend on OneDrive sync.
