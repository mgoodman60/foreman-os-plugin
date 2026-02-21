# Submittal Transmittal Form Template

## Overview

This template defines the standard Submittal Transmittal form structure, used as a cover sheet for submittal packages (product data, shop drawings, samples, test reports, certifications) being sent from the General Contractor to the Architect/Engineer for review and approval. The transmittal documents what is being submitted, why, and when a response is required.

## Form Fields and Data Mapping

### Header Information

#### Project Name
- **Label**: Project Name
- **Width**: Full width
- **Font Size**: 14pt, Navy #1B2A4A, Bold
- **Data Source**: project_basics.project_name
- **Auto-fill**: Yes
- **Editable**: No (read-only)
- **Required**: Yes

#### Project Number
- **Label**: Project No.
- **Width**: 33% (right side)
- **Font Size**: 11pt, Regular
- **Data Source**: project_basics.project_number
- **Auto-fill**: Yes
- **Editable**: No
- **Required**: Yes

#### Transmittal Number
- **Label**: Transmittal No.
- **Width**: 33% (left side)
- **Font Size**: 11pt, Bold
- **Data Source**: Next available from submittal_log (e.g., "TRANS-024")
- **Auto-fill**: Yes
- **Editable**: No
- **Required**: Yes
- **Logic**:
  - Query submittal_log for highest transmittal number issued
  - Increment by 1
  - Format as "TRANS-XXX" with zero-padded 3-digit number
  - If submittal_log is empty, start at TRANS-001
  - Alternative format: "ST-024" or "SUB-024" per project standards

#### Date
- **Label**: Date
- **Width**: 34% (middle-right)
- **Font Size**: 11pt, Regular
- **Data Source**: Current date (system date)
- **Auto-fill**: Yes
- **Editable**: Yes (user may backdate if needed)
- **Required**: Yes
- **Format**: MM/DD/YYYY

### Sender and Recipient

#### From (Submitter)
- **Label**: From / Submitted By
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: project_basics.general_contractor or project_basics.superintendent
- **Auto-fill**: Yes
- **Editable**: Yes
- **Required**: Yes
- **Format**:
  ```
  From:    [General Contractor Name]
           [Superintendent Name], Superintendent
           [Address, Phone, Email]
  ```

#### To (Recipient / Approving Authority)
- **Label**: To / Submitted To
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-selected based on submittal type:
  - Shop drawings / Technical submittals → Architect
  - Structural calculations → Structural Engineer
  - MEP system submittals → Mechanical/Electrical/Plumbing Engineer
  - Default → Architect
- **Auto-fill**: Yes, with smart selection
- **Editable**: Yes (user may change recipient)
- **Required**: Yes
- **Format**:
  ```
  To:      [Architect/Engineer Name], [Title]
           [Firm Name]
           [Address, Phone, Email]
  ```

#### CC (Carbon Copy)
- **Label**: CC
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: 
  - General Contractor project manager (if not sender)
  - Other disciplines if multi-disciplinary submittal
  - Prime contractor if subcontractor is submitting
- **Auto-fill**: Optional
- **Editable**: Yes
- **Required**: No

### Submittal Information

#### Description / Item
- **Label**: Item Description / Description of Submittal
- **Width**: Full width
- **Font Size**: 11pt, Regular
- **Data Source**: User-provided; system may suggest based on spec section
- **Auto-fill**: No (required user input)
- **Editable**: Yes
- **Required**: Yes
- **Guidelines**:
  - Be specific and concise
  - Examples:
    - "Shop drawings for curtain wall system, Grid A-D, Levels 1-2"
    - "Product data and samples for carpet flooring, building finishes"
    - "Structural calculations for Level 2 moment connection at Grid G-H"
    - "HVAC schedule and equipment specifications"
    - "Electrical load analysis and panel schedule"

#### Spec Section
- **Label**: Spec Section
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-selected from spec_sections based on item description
- **Auto-fill**: Yes (with confirmation)
- **Editable**: Yes
- **Required**: Yes
- **Format**:
  ```
  Division 08, Section 08 54 00 – Specialty Glass and Glazing
  or
  Div 08 | Sec 08 54 00 (abbreviated)
  ```
- **Logic**:
  1. User describes item (e.g., "curtain wall shop drawings")
  2. System searches spec_sections for matching division/section
  3. Common keywords: "curtain wall" → Div 08; "flooring" → Div 09; "HVAC" → Div 23; "Electrical" → Div 26; "Plumbing" → Div 22
  4. Returns matching section with full CSI MasterFormat title
  5. User confirms or edits

#### Manufacturer / Product
- **Label**: Manufacturer / Product
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-populated from subcontractors or submittal_log if available
- **Auto-fill**: Yes (optional)
- **Editable**: Yes
- **Required**: Sometimes (depends on submittal type)
- **Format**:
  ```
  [Manufacturer Name], [Product Line/Model Number]
  Example: Kawneer Curtain Wall System, Model 1600UT
  ```

#### Number of Copies
- **Label**: Number of Copies / Pages
- **Width**: 25%
- **Font Size**: 11pt, Regular
- **Data Source**: User input; default = 2 (one for Architect, one for record)
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: Yes
- **Format**: Numeric, with note "(including record copies)"

#### Submitted For
- **Label**: Submitted For
- **Width**: Full width
- **Font Size**: 11pt, Regular
- **Data Source**: User selection; default = "Review"
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: Yes
- **Options**:
  - **[X] Review** – Request for comments and feedback (no approval yet)
  - **[ ] Approval** – Request for approval; cannot proceed without signature
  - **[ ] Approval & Release** – Request for approval and permission to order/fabricate
  - **[ ] Information** – Submittal for record/tracking, not requiring response
  - **[ ] Resubmit** – Resubmission after revision per Architect comments
- **Logic**:
  - Default to "Review" for first submission
  - Change to "Approval & Release" if schedule is critical
  - "Resubmit" when resubmitting after revision
  - "Information" for transmittals that are FYI only

### Remarks and Details

#### Remarks
- **Label**: Remarks / Notes
- **Width**: Full width
- **Height**: 2-3 inches (proportional, allows 100-200 words)
- **Font Size**: 11pt, Regular
- **Data Source**: User optional
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: No (but recommended)
- **Guidelines**:
  - Use for any special instructions or context
  - Examples:
    - "Curtain wall system includes third-party certifications (attached). Mock-up of Mullion Profile A-2 recommended for review before full production."
    - "Flooring samples submitted in three color options per Architectural request. Recommend selection within 5 business days to maintain delivery schedule."
    - "MEP shop drawings incorporate revisions per RFI-047. Equipment delivery is 8 weeks from approval."
    - "Resubmission per Architect comments dated 02/10/2026. See attached marked-up drawings."
  - Keep professional tone
  - Reference related RFIs or previous communications if relevant

#### Response Required By
- **Label**: Response Required By
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-calculated based on spec section and project schedule
- **Auto-fill**: Yes (user may override)
- **Editable**: Yes
- **Required**: Yes
- **Format**: MM/DD/YYYY
- **Logic**:
  - Standard submittal review period: 7 business days
  - Critical path items (affecting schedule): 3-5 business days
  - User may shorten if needed for schedule
  - Calculate from project schedule to avoid weekends/holidays

#### Schedule Impact (Optional)
- **Label**: Schedule Impact / Critical Item
- **Width**: Full width
- **Font Size**: 11pt, Regular, Italic
- **Data Source**: User optional
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: No
- **Guidelines**:
  - Indicate if approval is critical to project schedule
  - Example: "Equipment approval required by 03/15/2026 to maintain 8-week delivery for installation on 05/15/2026. Project substantial completion is 06/30/2026."
  - Helps prioritize Architect review

### Footer

#### Transmittal Log Reference
- **Label**: None (metadata)
- **Font Size**: 9pt, Gray #666666
- **Content**: "TRANS-024 | Submitted | Created: 02/16/2026 by [User Name]"
- **Auto-fill**: Yes
- **Purpose**: Tracking when created, by whom, current status

#### Signature Block
- **Layout**:
  ```
  SUBMITTED BY:                          RECEIVED BY:
  
  _________________________              _________________________
  [Superintendent/Manager Name]          [Architect/Engineer]
  [Title]                                [Title]
  [Date]                                 [Date]
  
  
  REVIEWED / APPROVED BY:
  
  _________________________              _________________________
  [Architect/Engineer Signature]         [Date]
  
  COMMENTS:
  __________________________________________________________________
  __________________________________________________________________
  ```
- **Font Size**: 11pt, Regular
- **Auto-fill**: Yes (Submitted By section)
- **Editable**: Yes

### Itemized Submittal Table (for Multi-Item Transmittals)

For transmittals containing multiple items (e.g., submittal covering 5 different products or sections):

**Table Columns**:
| Item | Description | Spec Section | Manufacturer | Copies | Comments |
|------|-------------|--------------|--------------|--------|----------|
| 1 | [Item] | [Div/Sec] | [Mfr] | 2 | [Notes] |
| 2 | [Item] | [Div/Sec] | [Mfr] | 2 | [Notes] |

- **Font Size**: 10pt, Regular
- **Width**: Full width
- **Auto-fill**: Partial (Spec Section, Manufacturer from project data)
- **Use When**: Transmitting 3+ items in a single cover

## Visual Design and Styling

### Color Palette
- **Headers (Project Name, Major Sections)**: Navy #1B2A4A, Bold, 14pt
- **Field Labels**: Navy #1B2A4A, Bold, 11pt
- **Field Values**: Regular text, 11pt
- **Accent Lines**: Blue #2E5EAA (horizontal rule under header)
- **Background Sections**: Light Blue #EDF2F9 for major sections (From/To, Item Details, Remarks)
- **Checkbox Sections**: Light blue background for "Submitted For" options
- **Borders**: Light Gray #CCCCCC for form boxes and tables

### Layout
- **Page Size**: US Letter (8.5" x 11")
- **Margins**: 0.75" top/bottom, 1" left/right
- **Font Family**: Arial or Helvetica (for PDF compatibility)
- **Line Spacing**: 1.5 for readability
- **Grid System**: 2-column for From/To, Project/Trans No., 3-column for Date

### PDF Generation
- **Tool/Library**: Preferred PDF library (e.g., wkhtmltopdf, weasyprint, pdfkit)
- **Orientation**: Portrait
- **Quality**: 300 DPI for print
- **Embeds**: Include company logos in header if available
- **Accessibility**: Searchable text (not image-based)
- **Signature Lines**: Sufficient blank space (0.5" height) with light gray underline

## Example Transmittal (Fully Filled)

```
═══════════════════════════════════════════════════════════════════════

                      SUBMITTAL TRANSMITTAL COVER SHEET

═══════════════════════════════════════════════════════════════════════

Project Name: Harmony Plaza Office & Retail Development
Project No.: HM-2025-001                            Transmittal No.: TRANS-024
                                                             Date: 02/16/2026

───────────────────────────────────────────────────────────────────────

From:    Coastal Construction Group, Inc.
         James Richardson, Superintendent
         120 Maritime Drive, San Francisco, CA 94105
         Phone: (415) 555-0123 | Email: j.richardson@coastalconstruction.com

To:      Chen & Associates Architecture
         Margaret Chen, Principal Architect
         1275 Market Street, San Francisco, CA 94103
         Phone: (415) 555-0456 | Email: m.chen@chenarch.com

CC:      David Wu, Structural Engineer (Structural Solutions, Inc.)


───────────────────────────────────────────────────────────────────────

ITEM DESCRIPTION / SUBMITTAL DETAILS:

Item:            Curtain Wall System – Shop Drawings & Product Data
Spec Section:    Division 08, Section 08 54 00 – Specialty Glass and Glazing
Manufacturer:    Kawneer Curtain Wall System, Model 1600UT
Number of Copies: 3 (including record copy)

Submitted For:
  [X] Review – Request for comments and feedback
  [ ] Approval – Request for approval before proceeding
  [ ] Approval & Release – Request for approval and permission to order
  [ ] Information – Submittal for record only
  [ ] Resubmit – Resubmission with revisions

Response Required By: 02/23/2026 (5 business days)


───────────────────────────────────────────────────────────────────────

REMARKS / NOTES:

The attached curtain wall shop drawings incorporate finalized Mullion Profile A-2 
and spandrel panel details per your review comments from our earlier coordination 
meeting (01/15/2026).

INCLUDED IN THIS SUBMITTAL:
  • Curtain wall elevations (Sheets CW-101 through CW-105)
  • Mullion and glass details (Sheets CW-201 through CW-205)
  • Thermal break and sealant specifications
  • Third-party certifications (structural, thermal, and air infiltration)
  • Product data for all structural silicone sealants
  • Certificate of Compliance from manufacturer

REVIEW NOTES:
  • Mock-up of Mullion Profile A-2 and glass interface is recommended at full scale 
    before production fabrication begins.
  • Delivery schedule: 8 weeks from approval. Critical to approve by 03/10/2026 to 
    maintain installation schedule (Levels 1-2 glazing work begins 05/15/2026).
  • Structural calculations for moment connection at Grid G-H have been incorporated 
    per RFI-048 resolution. See Sheet CW-203, Detail 4.

SCHEDULE IMPACT:
  Approval by 03/10/2026 is CRITICAL. Curtain wall manufacturer's 8-week lead time 
  places equipment delivery at 05/01/2026. Glazing installation on Levels 1-2 is 
  scheduled to begin 05/15/2026. Any delay in approval will impact the project 
  completion date (current target: 06/30/2026).


───────────────────────────────────────────────────────────────────────

SUBMITTED BY:                          RECEIVED BY:


_______________________________        ________________________________
James Richardson                      [Signature – Architect/Engineer]
Superintendent
Coastal Construction Group, Inc.      [Printed Name & Title]
02/16/2026
                                      [Date]


REVIEWED / APPROVED BY:

_______________________________        _______________________________
[Architect/Engineer Signature]        [Date]


COMMENTS / CONDITIONS:

_____________________________________________________________________
[Architect/Engineer to provide approval comments, conditions, or 
rejection with required revisions]

_____________________________________________________________________

═══════════════════════════════════════════════════════════════════════
TRANS-024 | Submitted | Created: 02/16/2026 by James Richardson
═══════════════════════════════════════════════════════════════════════
```

## Multi-Item Transmittal Example

```
═══════════════════════════════════════════════════════════════════════

                      SUBMITTAL TRANSMITTAL COVER SHEET

═══════════════════════════════════════════════════════════════════════

Project Name: Harmony Plaza Office & Retail Development
Project No.: HM-2025-001                            Transmittal No.: TRANS-025
                                                             Date: 02/16/2026

From:    Coastal Construction Group, Inc.
         James Richardson, Superintendent

To:      Chen & Associates Architecture
         Margaret Chen, Principal Architect

───────────────────────────────────────────────────────────────────────

SUBMITTALS INCLUDED IN THIS TRANSMITTAL:

┌──────┬──────────────────────────────┬──────────────┬──────────────┬──────┐
│ Item │ Description                  │ Spec Section │ Manufacturer │ Copies│
├──────┼──────────────────────────────┼──────────────┼──────────────┼──────┤
│  1   │ Curtain Wall Shop Drawings   │ 08 54 00     │ Kawneer 1600 │  3   │
├──────┼──────────────────────────────┼──────────────┼──────────────┼──────┤
│  2   │ Curtain Wall Sealants &      │ 08 54 00     │ Dow Corning  │  2   │
│      │ Product Specifications       │              │ (attachment) │      │
├──────┼──────────────────────────────┼──────────────┼──────────────┼──────┤
│  3   │ Glass Specs & Thermal        │ 08 53 00     │ Saint-Gobain │  2   │
│      │ Performance Data             │              │ Sec-Series   │      │
├──────┼──────────────────────────────┼──────────────┼──────────────┼──────┤
│  4   │ Third-Party Structural       │ 08 54 00     │ SGS / Cert.  │  1   │
│      │ Certifications               │              │ of Compliance│      │
└──────┴──────────────────────────────┴──────────────┴──────────────┴──────┘

Submitted For:
  [X] Review – Request for comments and feedback
  [ ] Approval – Request for approval before proceeding

Response Required By: 02/23/2026

[Remarks, Signature Block, etc. – same format as above]
```

## Auto-Fill Rules Summary

| Field | Data Source | Auto-Fill | Smart Selection |
|-------|-------------|-----------|-----------------|
| Project Name | project_basics | Yes | No |
| Project No. | project_basics | Yes | No |
| Transmittal No. | submittal_log (next sequence) | Yes | No |
| Date | System date | Yes | Editable |
| From | project_basics.GC or superintendent | Yes | No |
| To | Based on item type (Arch/Eng) | Yes | Smart selection |
| Description | User input | No | Suggested |
| Spec Section | spec_sections + keyword match | Yes | Confirmed |
| Manufacturer | subcontractors + submittal_log | Yes | Optional |
| Number of Copies | Default 2 | No | User selection |
| Submitted For | Default Review | No | User selection |
| Response Date | Auto-calc from spec section | Yes | Editable |
| Remarks | None (user guidance) | No | No |
| Schedule Impact | None (user guidance) | No | No |

## Notes for Implementation

1. **Smart Selection**: "To" recipient is automatically selected based on submittal type:
   - Shop drawings, product data → Architect
   - Structural calculations → Structural Engineer
   - MEP system data → Appropriate Engineer
   - Default → Architect

2. **Spec Section Matching**: System searches spec_sections using keywords from user's item description

3. **Confirmation Steps**: Always show user the auto-resolved fields (Spec Section, To recipient, Response Date) before finalizing

4. **Status Tracking**: Transmittal starts as "Submitted" in submittal_log; Architect response changes status to "Approved", "Approved with Conditions", or "Rejected"

5. **Multiple Items**: If submitting 3+ items, display as table instead of single-item form

6. **Export Options**: Provide HTML display and PDF export with professional formatting

7. **Linking**: Transmittal can reference related RFIs or coordination memos for context

