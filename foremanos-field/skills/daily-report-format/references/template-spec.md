# Template Specification — .docx Format

Exact visual specifications for the daily report, matching the W Principles DailyReport_v5_Fillable.docx template. Output format is .docx (Microsoft Word), with optional PDF export via LibreOffice.

## Generation Method

Use the `docx` npm library (docx-js) to generate .docx files programmatically. Follow the docx skill's guidelines for tables, headers, images, and page sizing. Key rules:

- Always use `WidthType.DXA` — never `WidthType.PERCENTAGE`
- Set both `columnWidths` on the table AND `width` on each cell
- Use `ShadingType.CLEAR` — never SOLID
- Set page size explicitly to US Letter (12240 x 15840 DXA)
- Use separate `Paragraph` elements — never `\n`
- Use `LevelFormat.BULLET` for lists — never unicode bullets

## Page Setup

- Paper: US Letter (8.5" × 11")
- Width: 12240 DXA, Height: 15840 DXA
- Margins: Top 1440, Right 1440, Bottom 1080, Left 1440 (DXA)
- Header distance: 708 DXA, Footer distance: 708 DXA
- Content area width: 9360 DXA (12240 - 1440 - 1440)
- Orientation: Portrait

## Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| Navy | #1B2A4A | Table headers background, section header text |
| Blue Accent | #2E5EAA | Section header left accent bar, "DAILY REPORT" text in header |
| Light Blue | #EDF2F9 | Section header background |
| Label Gray | #666666 | Field labels in project info, footer text |
| Border Gray | #CCCCCC | Table borders (data tables), footer top border |
| Body Text | #333333 | Weather time labels |
| White | #FFFFFF | Table header text, page background |
| Alt Row | #F5F5F5 | Alternating table row shading (data tables) |

## Typography

| Element | Font | Size (half-pts) | Weight | Color |
|---------|------|-----------------|--------|-------|
| "DAILY REPORT" header | Default | 28 (14pt) | Bold | #2E5EAA |
| Project info labels | Default | 18 (9pt) | Bold | #666666 |
| Project info values | Default | 20 (10pt) | Normal | Black |
| Section headers | Default | 20 (10pt) | Bold | #1B2A4A |
| Table headers | Default | 17 (8.5pt) | Bold | White |
| Table body | Default | 20 (10pt) | Normal | Black |
| Weather time labels | Default | 18 (9pt) | Normal | #333333 |
| Weather narrative | Default | 20 (10pt) | Normal | Black |
| Photo captions | Default | 18 (9pt) | Italic | #333333 |
| General notes | Default | 20 (10pt) | Normal | Black |
| Footer text | Default | 14 (7pt) | Normal | #666666 |

## Header Layout

Two-column table with no visible borders:

| Column | Width | Content |
|--------|-------|---------|
| Left cell | 4680 DXA | Company logo (anchored image, 2085975 x 638175 EMU ≈ 2.29" × 0.70") |
| Right cell | 4680 DXA | "DAILY REPORT" text, right-aligned, bold, #2E5EAA, 14pt |

Below the table: horizontal rule (bottom border, #2E5EAA, sz 6).

The logo image is stored in the template at `word/media/image1.png` (2639 × 808 px). When generating, copy the logo from the project's template file or AI - Project Brain/ folder.

## Footer Layout

Three-column table (3120 DXA each) with a thin gray (#CCCCCC) top border line above:

| Column | Alignment | Content |
|--------|-----------|---------|
| Left | Left | "{company_name} | {project_name}" |
| Center | Center | "Prepared by: {superintendent_name}" |
| Right | Right | "Page {PAGE} of {NUMPAGES}" |

All footer text: 7pt, #666666.

## Project Info Header

Four columns × four rows table. Full page width (5000 pct or 9360 DXA). No cell shading. Light auto borders.

Column widths (DXA): 2198, 2657, 2019, 2476

Cell margins: top 30, left 0, bottom 30, right 80 (label cols) or 0 (value cols).

| Row | Col 1 (Label) | Col 2 (Value) | Col 3 (Label) | Col 4 (Value) |
|-----|---------------|---------------|---------------|---------------|
| 1 | Project: | {project_name} | Date: | {date MM/DD/YYYY} |
| 2 | Project No: | {project_number} | Report No: | {report_number} |
| 3 | Client: | {client} | Superintendent: | {superintendent} |
| 4 | Architect: | {architect} | Project Manager: | {project_manager} |

- Label styling: Bold, #666666, 9pt (sz 18)
- Value styling: Normal, Black, 10pt (sz 20)

## Section Header Bar

Two-column table, full page width. Used before each data section.

| Column | Width | Background | Border | Content |
|--------|-------|------------|--------|---------|
| Left accent | 80 DXA | #2E5EAA | None visible | Empty paragraph |
| Header text | 9280 DXA | #EDF2F9 | None visible | Section title |

Header text cell margins: top 60, left 140, bottom 60, right 100.
Section title: Bold, #1B2A4A, 10pt (sz 20), ALL CAPS.

Spacing before each section header: 240 DXA (paragraph spacing before the section header table). After: 40 DXA (spacing before the data table).

Section names (ALL CAPS): WEATHER CONDITIONS, CREW ON SITE, MATERIALS RECEIVED, EQUIPMENT ON SITE, SCHEDULE UPDATES, VISITORS / INSPECTIONS, SITE PHOTOS, GENERAL NOTES

## Data Tables

All data tables share these properties:
- Full page width (5000 pct or 9360 DXA)
- Border: CCCCCC, single, sz 1 on all sides of each cell
- Table cell margins: left 10, right 10 (default)
- Header row: Navy (#1B2A4A) background, white bold text, 8.5pt (sz 17)
- Header cell margins: top 80, left 100, bottom 80, right 100
- Header cells: vertically centered
- Body cell margins: top 60, left 100, bottom 60, right 100
- Body cells: vertically centered
- Alternating row shading: odd rows white, even rows #F5F5F5

### Weather Table
3 equal columns (3120, 3119, 3119 DXA): Time | Temperature | Conditions
- Time column text: #333333, 9pt (sz 18) — values: "7:00 AM", "12:00 PM", "4:00 PM"
- Temperature/Conditions: default body styling
- Always 3 body rows (7 AM, 12 PM, 4 PM)

Below the weather table: weather narrative paragraph with spacing before 180 DXA, default font, 10pt.

### Crew on Site Table
3 columns (2800, 1200, 5360 DXA): Subcontractor | Headcount | Work Performed
- Include all subs with data
- Add empty rows to reach 10 minimum rows
- Final row: "TOTAL" in bold in first cell, summed headcount in second cell, third cell empty

### Materials Received Table
5 columns (1900, 1600, 1200, 1200, 3460 DXA): Material | Supplier | Quantity | PO # | Condition
- Default condition: "Good" unless noted otherwise
- If no materials: single row spanning all columns: "No material deliveries today."

### Equipment on Site Table
4 columns (2600, 2200, 1200, 3360 DXA): Equipment | Owner/Sub | Hours | Status
- Status values: Active, Idle, Down (reason)

### Schedule Updates Section
Not a table — uses labeled paragraphs:
- **Current Phase:** {phase description}
- **Percent Complete:** {percentage}
- **Upcoming Milestones:** {milestones within next 2 weeks}
- **Delays / Impacts:** {delay description with cause and duration}

Each label: Bold, 10pt. Each value: Normal, 10pt. Spacing after each: 100 DXA.

### Visitors / Inspections Table
6 columns (1500, 1500, 1860, 1200, 1200, 2100 DXA): Name | Organization | Purpose | Time In | Time Out | Result
- Result values: Pass, Fail, Conditional, N/A
- If no visitors: single row "No visitors or inspections today."

## Photo Layout

- Photos embedded as inline images within paragraphs
- Max width: 5.5 inches (5040000 EMU) for single photos, centered
- For paired photos: each ~3 inches (2743200 EMU), side by side
- Caption paragraph below each photo: Italic, 9pt (sz 18), #333333, centered
- Caption format: "[Description]. [Location reference]. [Direction if known]."
- Spacing: 60 DXA between photo and caption, 180 DXA between photo groups

## Page Breaks

- Allow natural page breaks between sections
- Never break a section header from its content (use `cantSplit` on section header table rows)
- Keep photo with its caption on same page
- Start a new page if a section would begin in the bottom 2 inches of a page

## File Naming

Primary output: `{M_D_YY}_Daily_Report_{PROJECT_CODE}.docx`
Example: `2_14_26_Daily_Report_MOSC.docx`

Optional PDF export: `{M_D_YY}_Daily_Report_{PROJECT_CODE}.pdf`
Conversion: `python3 scripts/office/soffice.py --headless --convert-to pdf {docx_file}`

Amended reports: `{M_D_YY}_Daily_Report_{PROJECT_CODE}_AMENDED.docx`

## Logo Handling

The W Principles logo is stored in the template at `11 - Daily Reports/Templates/DailyReport_v5_Fillable.docx`. When generating a report:

1. Check if `AI - Project Brain/company_logo.png` exists → use it
2. Otherwise, extract from the template: unpack the .docx, copy `word/media/image1.png`
3. If no logo available, leave the header left cell empty

The logo is embedded as an anchored drawing in the header, positioned at offset -57150 horizontal, -477520 vertical from the column, behind text. Size: 2085975 × 638175 EMU.

## Amended Report Watermark

For amended reports, add a diagonal "AMENDED" text watermark:
- Use a WordArt/text box rotated -45 degrees
- Color: light gray (#CCCCCC), 50% opacity
- Font: 72pt bold
- Centered on page
- Behind text

Also add amendment date to the header: "{amendment_date} — AMENDED" appended to the "DAILY REPORT" text.
