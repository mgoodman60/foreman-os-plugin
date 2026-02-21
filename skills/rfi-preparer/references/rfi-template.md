# RFI Form Template

## Overview

This template defines the standard Request for Information (RFI) form structure, layout, auto-fill rules, and professional formatting standards. RFIs are formal written requests from the General Contractor (via the Superintendent) to the Architect or Engineer for clarification, direction, or decisions on conflicts and ambiguities in the contract documents.

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

#### RFI Number
- **Label**: RFI No.
- **Width**: 33% (left side)
- **Font Size**: 11pt, Bold
- **Data Source**: Next available from rfi_log (e.g., "RFI-048")
- **Auto-fill**: Yes
- **Editable**: No
- **Required**: Yes
- **Logic**: 
  - Query rfi_log for highest RFI number issued
  - Increment by 1
  - Format as "RFI-XXX" with zero-padded 3-digit number
  - If rfi_log is empty, start at RFI-001

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

#### From (Sender)
- **Label**: From
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: project_basics.superintendent (name, title, company)
- **Auto-fill**: Yes
- **Editable**: Yes (user may override)
- **Required**: Yes
- **Format**:
  ```
  From:  [Superintendent Name], Superintendent
         [General Contractor Name]
  ```

#### To (Primary Recipient)
- **Label**: To
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-selected based on question topic:
  - Architectural questions → project_basics.architect
  - Structural/MEP questions → project_basics.engineer
  - Default → project_basics.architect
- **Auto-fill**: Yes, with smart selection
- **Editable**: Yes (user may change recipient)
- **Required**: Yes
- **Format**:
  ```
  To:    [Architect/Engineer Name], [Title]
         [Architecture/Engineering Firm Name]
         [Address, Phone, Email]
  ```

#### CC (Carbon Copy)
- **Label**: CC
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: 
  - If To = Architect, CC = Engineer (if exists in project_basics)
  - If To = Engineer, CC = Architect (if exists)
  - Optionally include General Contractor project manager
- **Auto-fill**: Yes (optional)
- **Editable**: Yes (user may add/remove)
- **Required**: No
- **Format**: One recipient per line

### Subject Matter

#### Subject Line
- **Label**: Subject
- **Width**: Full width
- **Font Size**: 11pt, Bold
- **Data Source**: User-provided; system can suggest based on description
- **Auto-fill**: No (required user input)
- **Editable**: Yes
- **Required**: Yes
- **Guidelines**:
  - Keep to one line, max 80 characters
  - Be specific ("Conflict in exterior wall assembly at Grid G-H between Arch and Struct drawings" rather than "Wall Question")
  - Lead with topic area if possible

#### Drawing Reference(s)
- **Label**: Drawing Reference(s)
- **Width**: Full width
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-resolved from documents_loaded based on location description
- **Auto-fill**: Yes (with confirmation)
- **Editable**: Yes
- **Required**: Sometimes (if question relates to a specific drawing)
- **Format**:
  ```
  Drawing Reference(s):
  Sheet A-201 (Second Floor Plan), Grid G-H
  Sheet A-301 (Exterior Elevations), East Elevation
  Sheet S-204 (Structural Floor Plan), Level 2
  ```
- **Logic**:
  1. User provides location description in Question field (e.g., "second floor, east side, wall between mechanical room and lobby")
  2. System auto-resolves to:
     - Building Area: "East Wing"
     - Grid Lines: "E-G, Lines 2-4"
     - Floor Level: "2"
  3. System searches documents_loaded for:
     - Architectural plans: "A-2XX" matching Level 2 and East Wing
     - Structural plans: "S-2XX" matching Level 2
     - Relevant building system plans (M, E, P) if related to MEP question
  4. Results are pre-filled with sheet numbers and grid references
  5. User confirms or edits

#### Spec Reference(s)
- **Label**: Spec Section(s)
- **Width**: Full width
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-resolved from spec_sections based on work type
- **Auto-fill**: Yes (with confirmation)
- **Editable**: Yes
- **Required**: Sometimes (if question relates to a specification)
- **Format**:
  ```
  Spec Section(s):
  Division 08, Section 08 54 00 – Specialty Glass and Glazing
  Division 09, Section 09 65 16 – Resilient Base and Accessories
  ```
- **Logic**:
  1. User describes the question (e.g., "what type of base trim in hallways?")
  2. System analyzes description and searches spec_sections for matching divisions/sections
  3. Common keywords: "exterior wall" → Search Div 07, 08; "flooring" → Div 09; "doors" → Div 08; "mechanical" → Div 23; "electrical" → Div 26
  4. Returns matching sections, user confirms
  5. If no match, user may leave blank or manually enter

### Question and Response Area

#### Description / Question
- **Label**: Description / Question
- **Width**: Full width
- **Height**: 3-4 inches (proportional, allows 150-300 words)
- **Font Size**: 11pt, Regular
- **Data Source**: User-provided casual description; system transforms to professional language
- **Auto-fill**: Partial (user describes casually, system drafts formal version below)
- **Editable**: Yes (both casual input and professional draft)
- **Required**: Yes
- **Guidelines**:
  - User can describe in casual language: "There's a conflict on the floor plan. The Arch drawing shows the wall goes one way but the Struct drawing shows it different. We need to know which one we're building to."
  - System auto-generates professional version:
    ```
    DESCRIPTION:
    A conflict exists in the exterior wall assembly at Grid G-H on Level 2. Architectural drawing Sheet A-201 
    indicates the wall extends from Grid G to Grid H with a continuous header. Structural drawing Sheet S-204 
    shows the wall segment ending at Grid G with a moment connection. These conditions are mutually exclusive. 
    Clarification is required to proceed with framing and coordination.
    ```
  - Professional language standards:
    - Clear, specific reference to drawings and specs (sheet numbers, grid coordinates)
    - State the conflict or ambiguity explicitly ("A conflict exists...")
    - Explain why clarification is needed ("...required to proceed with...")
    - Use construction terminology correctly
    - No blame or judgment ("The Arch drawing shows..." not "The Architect got it wrong...")
    - One question per RFI (or clearly separate multiple questions)

#### Suggested Resolution
- **Label**: Suggested Resolution / Recommendation
- **Width**: Full width
- **Height**: 2-3 inches (proportional, allows 100-200 words)
- **Font Size**: 11pt, Regular, Italic
- **Data Source**: User optional; system may suggest based on question type
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: No (but strongly recommended; shows collaboration and speeds response)
- **Guidelines**:
  - Start with: "We recommend..." or "The following clarification would allow work to proceed:"
  - Propose a solution if feasible
  - Reference drawings/specs to support recommendation
  - Show it's a collaborative attempt to solve the problem
  - Example:
    ```
    SUGGESTED RESOLUTION:
    We recommend adoption of the Structural plan condition (Sheet S-204), which aligns with the moment 
    connection detail at Section 4/S-301. We can coordinate mechanical ducts around this condition. 
    If Architectural intent differs, please provide a revised drawing or written directive.
    ```

#### Priority
- **Label**: Priority
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: User selection (default = Routine)
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: Yes
- **Options**:
  - **Routine** – Can be addressed in normal review cycle (5-10 business days response expected)
  - **Urgent** – Affects near-term work, needs response within 2-3 business days
  - **Critical** – Stops work or creates safety issue, needs response within 24 hours
- **Logic**: 
  - Default to Routine
  - User selects based on schedule impact
  - If Critical, system may suggest email/phone notification in addition to formal RFI

#### Required Response Date
- **Label**: Required Response Date
- **Width**: 50%
- **Font Size**: 11pt, Regular
- **Data Source**: Auto-calculated based on Priority and project schedule
- **Auto-fill**: Yes (user may override)
- **Editable**: Yes
- **Required**: Yes
- **Format**: MM/DD/YYYY
- **Logic**:
  - Routine: Current Date + 7 business days
  - Urgent: Current Date + 3 business days
  - Critical: Current Date + 1 business day
  - Check project schedule to avoid weekends and holidays
  - Display in form for confirmation

#### Schedule Impact Statement
- **Label**: Schedule Impact
- **Width**: Full width
- **Height**: 1-2 inches
- **Font Size**: 11pt, Regular
- **Data Source**: User optional; system may suggest based on priority and schedule
- **Auto-fill**: No
- **Editable**: Yes
- **Required**: No
- **Guidelines**:
  - Explain what work cannot proceed pending response
  - Example: "Framing of Level 2 East Wing cannot proceed until wall layout is confirmed. Current schedule shows framing starting 2/28/2026. Delay impacts substantial completion date."
  - Helps Architect/Engineer prioritize response

### Footer

#### RFI Log Reference
- **Label**: None (metadata)
- **Font Size**: 9pt, Gray #666666
- **Content**: "RFI-048 | Draft | Created: 02/16/2026 by [User Name]"
- **Auto-fill**: Yes
- **Purpose**: Tracking when created, by whom, current status

#### Signature Block
- **Layout**:
  ```
  SUBMITTED BY:                          RECEIVED BY:
  
  _________________________              _________________________
  [Superintendent Name]                  [Architect/Engineer]
  Superintendent                         [Title]
  [Date]                                 [Date]
  
  
  RESPONSE / RESOLUTION:
  
  _________________________________________________________________
  [Architect/Engineer Response]
  
  _________________________
  [Signature]                 [Date]
  ```
- **Font Size**: 11pt, Regular
- **Auto-fill**: Yes (Submitted By section)
- **Editable**: Yes (user may add notes)

## Visual Design and Styling

### Color Palette
- **Headers (Project Name, Major Sections)**: Navy #1B2A4A, Bold, 14pt
- **Field Labels**: Navy #1B2A4A, Bold, 11pt
- **Field Values**: Regular text, 11pt
- **Accent Lines**: Blue #2E5EAA (horizontal rule under header)
- **Background Sections**: Light Blue #EDF2F9 for major sections (From/To, Drawing Ref, Spec Ref, etc.)
- **Borders**: Light Gray #CCCCCC for form boxes

### Layout
- **Page Size**: US Letter (8.5" x 11")
- **Margins**: 0.75" top/bottom, 1" left/right
- **Font Family**: Arial or Helvetica (for PDF compatibility)
- **Line Spacing**: 1.5 for readability
- **Grid System**: 2-column for From/To, 3-column for Date/RFI/Project (aligned and balanced)

### PDF Generation
- **Tool/Library**: Preferred PDF library (e.g., wkhtmltopdf, weasyprint, pdfkit)
- **Orientation**: Portrait
- **Quality**: 300 DPI for print
- **Embeds**: Include company logos in header if available (from project_basics)
- **Accessibility**: Searchable text (not image-based)
- **Signature Lines**: Sufficient blank space (0.5" height) with light gray underline

## Example RFI (Fully Filled)

```
═══════════════════════════════════════════════════════════════════════

                          REQUEST FOR INFORMATION (RFI)

═══════════════════════════════════════════════════════════════════════

Project Name: Harmony Plaza Office & Retail Development
Project No.: HM-2025-001                                    RFI No.: RFI-048
                                                             Date: 02/16/2026

───────────────────────────────────────────────────────────────────────

From:    James Richardson, Superintendent
         Coastal Construction Group, Inc.
         Phone: (415) 555-0123 | Email: j.richardson@coastalconstruction.com

To:      Margaret Chen, Principal Architect
         Chen & Associates Architecture
         Phone: (415) 555-0456 | Email: m.chen@chenarch.com

CC:      David Wu, Structural Engineer
         Structural Solutions, Inc.


Subject: Conflict in Exterior Wall Assembly—Grid G-H, Level 2, East Wing


Drawing Reference(s):
  • Sheet A-201 (Second Floor Plan), Grid G-H
  • Sheet A-301 (Exterior Elevations), East Elevation  
  • Sheet S-204 (Structural Floor Plan), Level 2


Spec Section(s):
  • Division 07, Section 07 26 00 – Vapor Retarders
  • Division 08, Section 08 11 13 – Hollow Metal Doors and Frames
  • Division 08, Section 08 54 00 – Specialty Glass and Glazing


───────────────────────────────────────────────────────────────────────

DESCRIPTION / QUESTION:

A conflict exists in the exterior wall assembly at Grid G-H on Level 2, East Wing 
(between the mechanical room and the main lobby). Architectural drawing Sheet A-201 
indicates the wall extends continuously from Grid G to Grid H with a full-height 
header and window opening (per Sheet A-301, East Elevation). Structural drawing 
Sheet S-204 shows the wall segment ending at Grid G with a moment connection to the 
floor slab, and no wall element between Grid G and Grid H.

These conditions are mutually exclusive. The framing crew cannot proceed with either 
exterior framing or mechanical rough-in until this conflict is resolved.


SUGGESTED RESOLUTION:

We recommend adoption of the Structural plan condition (Sheet S-204) with a moment 
connection at Grid G and a revision to the Architectural floor plan to remove the wall 
segment between Grid G-H. This would align mechanical ductwork routing and simplify the 
exterior glazing system. If the full-height window is essential to the Architectural design, 
please provide a revised Structural plan showing how the loading is resolved, or provide a 
written directive with the Architectural intent.


Priority: URGENT
  [X] Routine (5-10 business days)
  [ ] Urgent (2-3 business days)
  [ ] Critical (24 hours)

Required Response Date: 02/21/2026 (5 business days)


Schedule Impact:
  Exterior framing of Level 2 East Wing, mechanical rough-in, and coordination of 
  building systems cannot proceed pending this clarification. Current schedule indicates 
  Level 2 exterior wall framing begins 02/24/2026. A delay of 2-3 days will impact 
  overall project completion and subsequent phase mobilization.

───────────────────────────────────────────────────────────────────────

SUBMITTED BY:                                RECEIVED BY:


_______________________________              ________________________________
James Richardson                            [To be signed by Recipient]
Superintendent
Coastal Construction Group, Inc.            [Title]
02/16/2026
                                            [Date]


RESPONSE / RESOLUTION:

_____________________________________________________________________
[Architect/Engineer to provide written response, including any revised drawings 
or directives]


_______________________________              _______________________________
[Signature]                                  [Date]

═══════════════════════════════════════════════════════════════════════
RFI-048 | Draft | Created: 02/16/2026 by James Richardson | Last Modified: 02/16/2026
═══════════════════════════════════════════════════════════════════════
```

## Auto-Fill Rules Summary

| Field | Data Source | Auto-Fill | Smart Selection |
|-------|-------------|-----------|-----------------|
| Project Name | project_basics | Yes | No |
| Project No. | project_basics | Yes | No |
| RFI No. | rfi_log (next sequence) | Yes | No |
| Date | System date | Yes | Editable |
| From | project_basics.superintendent | Yes | No |
| To | Based on topic (Arch/Eng) | Yes | Smart selection |
| CC | Opposite discipline | Yes | Optional |
| Subject | User input | No | Suggested |
| Drawing Ref | documents_loaded + location resolution | Yes | Confirmed |
| Spec Ref | spec_sections + keyword match | Yes | Confirmed |
| Description | User casual input → Professional draft | Partial | Professional generation |
| Suggested Res. | None (user guidance) | No | No |
| Priority | Default Routine | No | User selection |
| Response Date | Auto-calc from Priority + schedule | Yes | Editable |
| Schedule Impact | None (user guidance) | No | No |

## Notes for Implementation

1. **Location Resolution**: The "Drawing Reference" and location information requires integration with the drawing-reference-resolution module (see separate documentation)
2. **Professional Language Generation**: The transformation from casual user description to professional RFI language should be guided by examples and rules in the Description field guidelines above
3. **Confirmation Steps**: Always show the user the auto-resolved data (Drawing Ref, Spec Ref, To recipient) before finalizing, allowing edits
4. **Status Tracking**: RFI starts as "Draft" in rfi_log; user can change to "Issued" after approval; Architect response changes status to "Answered" or "On Hold"
5. **Export Options**: Provide both HTML display (for on-screen review) and PDF export (for printing and distribution)

