# RFI and Submittal Data - Deep Extraction Guide

Extract actionable intelligence from RFI logs, submittal logs, and submittal packages. These documents drive procurement timeline, schedule sequencing, and design clarifications that impact field operations.

---

## Table of Contents

1. [Document Classification](#document-classification)
2. [RFI Log Extraction](#rfi-log-extraction)
3. [Submittal Log Extraction](#submittal-log-extraction)
4. [Submittal Package Extraction](#submittal-package-extraction)
5. [Vendor and Supplier Data Extraction](#vendor-and-supplier-data-extraction)
6. [Cross-Referencing and Linking](#cross-referencing-and-linking)
7. [Quality and Confidence](#quality-and-confidence)

---

## Document Classification

### Pass 1: Metadata and Document Structure

Identify document type through metadata and structural analysis:

**Metadata Signals:**

| Signal | Type | Confidence |
|--------|------|------------|
| Title contains "RFI Log" or "Request for Information" | RFI Log | High |
| Title contains "Submittal Log" or "Submittal Schedule" | Submittal Log | High |
| Title contains product name, model, manufacturer | Submittal Package | High |
| Subject field lists CSI section or trade | Submittal Package | Medium |
| File includes specification excerpt or performance data | Submittal Package | High |
| Filename pattern: "_[number]_" or "Sub-###" | Submittal Package | High |
| Table structure with RFI/Submittal numbers in sequence | Log Document | High |

**Creator Application Signals:**

| Creator | Likely Type |
|---------|------------|
| Microsoft Excel | RFI Log, Submittal Log |
| Microsoft Word | RFI Correspondence, Cover Letter |
| Adobe InDesign, Publisher | Spec excerpts, compiled submittals |
| Adobe Acrobat (multi-source) | Submittal package (compiled from multiple sources) |
| Manufacturer software (CAD, PDM) | Product data sheet, shop drawing |

### Pass 2: Structural Patterns

**RFI Log Structure:**
- Sequential numbering (RFI-001, RFI-002, etc.)
- Column headers: Number, Date, Subject, Status, Response, etc.
- Typically tabular format
- May include separate response column or linked correspondence

**Submittal Log Structure:**
- Spec section numbers (e.g., 03300, 05120)
- Column headers: Number, Section, Title, Submitted, Status, Lead Time
- Tabular format with status tracking
- May reference document locations or file paths

**Submittal Package Structure:**
- Product identification (manufacturer, model)
- Technical specifications section
- Performance data, test results, certifications
- Installation details or shop drawings
- Company letterhead or document control information

**RFI Correspondence Structure:**
- Question/clarification narrative text
- Reference to drawings (sheet/detail numbers)
- Reference to spec sections
- Formal response format
- Dates and signatures

---

## RFI Log Extraction

Extract all RFIs from log documents to enable schedule impact analysis, blocking work tracking, and response accountability.

### Core Fields for Each RFI

| Field | Type | Priority | Notes |
|-------|------|----------|-------|
| **RFI Number** | Text | CRITICAL | Pattern: "RFI-###" or "#" |
| **Date Submitted** | Date | CRITICAL | When question was formally posed |
| **Date Response Received** | Date | HIGH | Track response time (SLA tracking) |
| **Subject** | Text | CRITICAL | Brief title of question |
| **Description** | Text | HIGH | Full question text if available |
| **Drawing References** | Text | CRITICAL | Sheet numbers, detail numbers (S-101, Detail 3/S-101) |
| **Specification References** | Text | HIGH | CSI sections (03300, 05120) or section titles |
| **Trade/Discipline** | Text | HIGH | Concrete, Steel, Mechanical, Electrical, etc. |
| **Blocks Work** | Boolean | CRITICAL | Critical flag: can field work proceed without answer? |
| **Blocking Details** | Text | CRITICAL | What work is prevented/delayed |
| **Status** | Enum | CRITICAL | Open, Answered, Closed, Pending, Rejected |
| **Response Summary** | Text | HIGH | Key points of response (if not separate document) |
| **Responder** | Text | MEDIUM | Who answered (Architect, Engineer, Owner, etc.) |
| **Follow-up Required** | Boolean | MEDIUM | Does response require additional clarification? |
| **Impact on Schedule** | Text | HIGH | How does delay affect sequencing (if known) |

### Extraction Priority Table

| Priority | Data | Purpose |
|----------|------|---------|
| **CRITICAL** | RFI number + date submitted | Track RFI by sequence and timeline |
| **CRITICAL** | Blocks work? + what work | Identify critical path RFIs |
| **CRITICAL** | Drawing/spec references | Cross-reference to design docs |
| **CRITICAL** | Status + response date | Measure response time SLA |
| **HIGH** | Subject and description | Enable keyword search and categorization |
| **HIGH** | Trade classification | Route to correct subcontractor/discipline |
| **MEDIUM** | Responder and response summary | Track authority and precedent |
| **MEDIUM** | Follow-up needed flag | Predict future RFI volume |

### Extraction Method: RFI Log Table

For RFI log documents, extract from tabular format:

**Example RFI Log Entry:**

```
RFI-007
  Number: RFI-007 (or simply 007)
  Date Submitted: 01/15/26
  Date Response: 01/22/26 (7 days)
  Subject: CMU wall height tolerance at Grid A-B
  Description: Design shows ±1/4" tolerance but spec is silent. 
               What tolerance applies to perimeter walls?
  Drawing Refs: A-101 (floor plan), S-101 (details)
  Spec Refs: 04 20 00 (Unit Masonry)
  Trade: Masonry
  Blocks Work: Yes - cannot lay course unless tolerance is defined
  Blocking Details: Perimeter wall layout affected; 2-day delay if not answered
  Status: Answered
  Response: Tolerance is ±1/2" per section 04 20 00, subsection 3.2.1. 
            Confirm with inspector at first course.
  Responder: Structural Engineer
  Follow-up: No
  Schedule Impact: No impact (answered within 1 week, schedule float available)
```

### Handling Multiple RFI Responses

Some RFIs may have:
- **Initial response**: Incomplete or partial answer
- **Follow-up response**: Clarification or additional information
- **Final response**: Engineering change order (ECO) or decision documented

**Extract as separate records if:**
- Responses arrive on different dates
- Responses contain contradictory information (flag as issue)
- Follow-up RFI is issued (link as "Related RFI: RFI-008")

**Consolidate as single record if:**
- All responses arrive together
- Response is clearly addendum to prior response

### Blocking Work Analysis

When "Blocks Work = Yes", extract detailed impact:

```
RFI-012
  Blocking Details:
    - Prevents: Foundation form setting for Column Grid C
    - Reason: RFI asks about column diameter (24" vs. 30")
    - Affects: 200 linear feet of Grade Beam
    - Work Start: Scheduled for 01/28/26
    - Critical Path: Yes (is foundation on critical path?)
    - Crew Size Affected: 4-person forming crew
    - Duration of Delay: Varies (1-3 days depending on answer)
```

### RFI Response Time Tracking

Extract dates to calculate response SLA:

| Metric | Extraction | Typical SLA |
|--------|-----------|------------|
| Days to Response | Response Date - Submitted Date | 5-7 business days |
| Days Open | Today - Submitted Date (if still open) | Should escalate >7 days |
| Days to Close | Close Date - Response Date | 1-3 days (receipt to closeout) |

---

## Submittal Log Extraction

Extract submittal information to track procurement timeline, critical path impacts, and review/approval status.

### Core Fields for Each Submittal

| Field | Type | Priority | Notes |
|-------|------|----------|-------|
| **Submittal Number** | Text | CRITICAL | Pattern: "03300-1", "S-001", "Sub-###" |
| **Specification Section** | Text | CRITICAL | CSI format: "03 30 00" or "032000" |
| **Section Title** | Text | HIGH | "Cast-in-Place Concrete" or "Structural Steel Fabrication" |
| **Item/Product Description** | Text | HIGH | "Concrete mix designs for footings" |
| **Submitted Date** | Date | CRITICAL | When submittal was sent for review |
| **Reviewed Date** | Date | HIGH | When approval/comments returned |
| **Status** | Enum | CRITICAL | Submitted, Under Review, Approved, Approved as Noted, Revise & Resubmit, Rejected |
| **Lead Time** | Duration | CRITICAL | Weeks from approval to delivery/availability |
| **Critical Path** | Boolean | HIGH | Is this on critical path to construction start? |
| **Manufacturer** | Text | MEDIUM | Company name if applicable |
| **Model/Part Number** | Text | MEDIUM | Specific product identifier |
| **Comments** | Text | HIGH | Review comments or reasons for rejection |
| **Approver** | Text | MEDIUM | Architect, Engineer, Owner rep |
| **Resubmittal Needed** | Boolean | MEDIUM | Does this require revision and resubmission? |
| **Resubmittal Date** | Date | MEDIUM | When resubmittal was sent |
| **Final Status Date** | Date | HIGH | When finally approved/resolved |

### Extraction Priority Table

| Priority | Data | Purpose |
|----------|------|---------|
| **CRITICAL** | Submittal number + spec section | Link to procurement and scheduling |
| **CRITICAL** | Status + review date | Track approval progress |
| **CRITICAL** | Submitted date + lead time | Calculate procurement deadline |
| **HIGH** | Critical path flag | Identify schedule driver submittals |
| **HIGH** | Comments/reasons for rejection | Prevent re-approval of same issues |
| **MEDIUM** | Manufacturer + model | Verify field installation against submittal |
| **MEDIUM** | Approver | Track sign-off authority |

### Extraction Method: Submittal Log Table

For submittal log documents:

**Example Submittal Log Entry:**

```
03300-1
  Number: 03300-1 (or "S-001" or "Concrete-1")
  Section: 03 30 00
  Title: Cast-in-Place Concrete
  Item: Concrete mix designs for footings, walls, and SOG
  Submitted: 12/12/25
  Reviewed: 12/19/25 (7 days)
  Status: Approved as Noted
  Lead Time: 2 weeks (ready-mix no lead time, testing 1 week)
  Critical Path: Yes
  Manufacturer: XYZ Ready Mix Co.
  Model/Product: Custom mix per specification
  Comments: Approve mix designs. Provide SDS for air entrainment admixture.
            Confirm testing lab address before placement.
  Approver: Structural Engineer
  Resubmittal Needed: No (SDS provided separately)
  Final Status: Approved 12/21/25
  Schedule Impact: No impact; received before procurement deadline
```

### Handling Resubmittals

Track resubmittal cycle:

```
05120-1 (Original)
  Submitted: 01/08/26
  Status: Revise & Resubmit
  Comments: Shop drawings do not show connection details at Grid C. 
            Provide bolted connection details with torque specifications.
  
05120-1 (Resubmittal)
  Submitted: 01/15/26 (7 days)
  Status: Approved as Noted
  Comments: Connection details adequate. Mark all bolts for full-tension
            tensioning per AISC standards. See RFI-008 for grid clarification.
  Approver: Structural Engineer
  Final Status: Approved 01/17/26
```

**Link RFI to Submittal Resubmittal:**
- If comments reference an RFI, extract the link
- Example: "See RFI-008 for grid clarification" → Link 05120-1 to RFI-008

### Submittal Criticality Analysis

Extract schedule impact for each submittal:

```
03300-1: CRITICAL PATH
  Approval Date: 12/21/25
  Lead Time: 2 weeks (ready-mix procurement)
  Required By (field): 01/05/26 (foundation concrete pour scheduled 01/10/26)
  Margin: 6 days
  Risk: Low (long lead time for concrete is rare)
  
05120-2: CRITICAL PATH
  Approval Date: 02/03/26 (pending)
  Lead Time: 8 weeks (fabrication)
  Required By (field): 03/15/26 (steel erection scheduled 03/20/26)
  Margin: 5 days
  Risk: High (long fabrication lead; any delay affects frame erection)
  Status Flag: MONITOR - if not approved by 01/15/26, escalate
```

---

## Submittal Package Extraction

When processing actual submittal packages (PDFs containing product data sheets, shop drawings, test reports), extract detailed product and performance information.

### Document Structure: Submittal Package

Submittal packages typically contain:

1. **Cover letter or transmittal** - Submittal number, section, date, approvals
2. **Product data/spec sheet** - Manufacturer specs, dimensions, materials
3. **Performance data** - Test results, certifications, test lab reports
4. **Installation details** - How to install, connection methods
5. **Shop drawings** (if applicable) - Detailed fabrication drawings
6. **Certifications** - Mill certs, test reports, UL/NFPA approvals

### Core Extraction Fields: Product Data

| Field | Type | Priority | Notes |
|-------|------|----------|-------|
| **Product Name** | Text | CRITICAL | Full commercial product name |
| **Manufacturer** | Text | CRITICAL | Company name and location |
| **Model Number** | Text | CRITICAL | Exact part/model identifier |
| **Description** | Text | MEDIUM | Functional description |
| **Material Composition** | Text | HIGH | What is it made from (steel, concrete, wood, etc.) |
| **Dimensions** | Text | HIGH | Length × Width × Height or Diameter × Depth |
| **Unit Weight** | Number | HIGH | Pounds/kilograms per unit |
| **Color/Finish** | Text | MEDIUM | Color code, surface finish type |
| **Installation Method** | Text | HIGH | How does it attach or connect? |
| **Connection Details** | Text | HIGH | Bolt size/type, weld specs, fastener requirements |

### Performance Data Extraction

| Field | Type | Priority | Notes |
|-------|------|----------|-------|
| **Strength/Load Rating** | Number + Unit | CRITICAL | PSI, kips, kN, lbs per linear foot |
| **Fire Rating** | Text | CRITICAL | 1-hr, 2-hr, 3-hr if applicable |
| **Acoustic Performance** | Number + Unit | MEDIUM | STC rating, NRC coefficient |
| **R-Value or U-Value** | Number | HIGH | Thermal performance rating |
| **Test Standard** | Text | CRITICAL | ASTM F1234, UL 2000, NFPA 72 |
| **Test Lab** | Text | MEDIUM | UL, ETL, ICC, other test authority |
| **Test Date** | Date | MEDIUM | When was test performed (currency check) |
| **Certifications** | Text | CRITICAL | UL listed, FM approved, ETL, APA, etc. |
| **Warranty** | Duration | MEDIUM | Years of coverage |

### Extraction Method: Product Data Sheet

**Example Submittal Package - Concrete Mix Design:**

```
Submittal Number: 03300-2 (Concrete - Elevated Slabs)
Manufacturer: ABC Ready Mix Concrete, Denver, CO
Product: Custom concrete mix design
Cover Letter Date: 01/18/26
Section: 03 30 00 (Cast-in-Place Concrete)

Product Specifications:
  Mix Design Name: "Elevated Slab Mix - 4000 PSI"
  Compressive Strength: 4,000 PSI at 28 days
  Slump: 4 inches ± 1 inch
  Air Content: 5.5% ± 1.5%
  Water/Cement Ratio: 0.45 maximum
  Aggregate Size: 3/4 inch nominal maximum
  
Material Composition:
  Cement: Portland Type I
  Coarse Aggregate: Granite, oven-dry bulk density 103 lb/cf
  Fine Aggregate: Sand, FM 2.8
  Water: Potable
  Admixtures: 
    - Air entrainment: ASTM C260
    - Water reducer: ASTM C494 Type F
    - Accelerator: ASTM C494 Type C (cold weather only)

Performance Data:
  Test Method: ASTM C39 (compression test)
  Test Lab: Colorado Materials Testing Lab
  Test Date: 12/15/25 (mix design batch testing)
  Results:
    - 7-day: 3,200 PSI
    - 28-day: 4,050 PSI (target 4,000 PSI)
    - Slump: 4 inches
    - Air: 5.8%
  
Certifications:
  NSF/ANSI 61 (drinking water contact approved)
  Meets ACI 318 standards
  
Installation Requirements:
  Placement Temp: Minimum 50°F, Maximum 90°F
  Cold Weather (<40°F ambient): Insulated blankets, heat as required
  Hot Weather (>90°F ambient): Ice in mix, cool aggregates
  Curing: 7 days minimum for slabs (wet curing or membrane curing)
  Testing: 1 set per 50 CY or per day (whichever is more) = 4 cylinders
  
Supplier Information:
  Plant Location: (Address with coordinates for delivery)
  Delivery Hours: 6:00 AM - 4:00 PM Mon-Fri
  Ready-Mix Trucks Available: 12 (for high-volume pours)
  Lead Time: 0 days (daily ordering)
  Minimum Order: 5 CY per truck
  Ready-Mix Unit Price: $152/CY (as of 01/18/26)
```

**Example Submittal Package - Structural Steel:**

```
Submittal Number: 05120-3 (Structural Steel Fabrication)
Manufacturer: Midwest Steel Fabricators, Chicago, IL
Product: Structural steel frame, Column Grid A-D, Rows 1-4
Cover Letter Date: 01/22/26
Section: 05 12 00 (Structural Steel)

Products/Materials:
  Steel Grade: ASTM A992 (Fy = 50 ksi, Fu = 65 ksi)
  Primary Members: W24×104 beams, W14×90 columns
  Bolts: ASTM A325 Type 1, high-strength bolts
    - Sizes: 7/8" diameter (moment connections), 3/4" diameter (simple)
    - Torque: 125 ft-lbs (7/8"), 95 ft-lbs (3/4") - snug then full tension
  Welds: ASTM E7018 electrodes (shielded metal arc)
    - E70XX series
    - Inspection: 100% visual, 10% UT on moment connections

Fabrication Drawing References:
  Shop Drawing Package: 05120-3-SDxx (Sheets 1-8)
  - Detail 1/05120-3-SD1: Moment Connection at Grid C, Row 2
  - Detail 2/05120-3-SD2: Column Splice Details
  - Detail 3/05120-3-SD3: Beam Splice and Bolt Layouts
  Cross-reference to design drawings: S-101, S-102, S-201

Performance Data:
  Yield Strength: 50 ksi minimum (ASTM A992)
  Tensile Strength: 65 ksi minimum
  Deflection Limits: L/240 for beams under live load
  
Quality & Certifications:
  Fabricator: Certified AISC (American Institute of Steel Construction)
  Testing:
    - Mill test certificates provided (tension, hardness)
    - Bolt tension verification after full tensioning
  Painting: SSPC-PA2 surface prep, (primer to be applied per contract)
  
Lead Time & Schedule:
  Approval Date: (pending - submitted 01/22/26)
  Fabrication Time: 8 weeks from approval
  Ready for Shipment: Week of (date + 8 weeks)
  Delivery to Site: (truck schedule to be confirmed)
  Installation Schedule: Frame erection 03/20/26 (requires approval by 01/25/26)
  
Connection Details (Key Extracts):
  Moment Connection (Grid C, Row 2):
    - Type: Bolted moment splice
    - Bolts: 8 × 7/8" A325 bolts, high-strength
    - Torque Spec: 125 ft-lbs full tension, per AISC specifications
    - Plate Thickness: 1-1/2" flange, 5/8" web
    - Filler Plates: Where needed for grip
  
  Column Base Plate:
    - Material: ASTM A36
    - Thickness: 2 inches
    - Anchor Bolts: 6 × 1-1/4" dia., 24 inches embedment in concrete
    - Grout: Non-shrink, 2-inch minimum thickness
```

**Example Submittal Package - Mechanical Equipment:**

```
Submittal Number: 15050-1 (HVAC Equipment)
Manufacturer: Carrier Corp., Syracuse, NY
Product: Rooftop packaged air-handling unit (RTU)
Cover Letter Date: 02/01/26
Section: 15 05 00 (HVAC Equipment)

Product Name: Carrier AquaEdge Chiller, Model 30XA380
Capacity: 400 tons of refrigeration (TR)
Refrigerant: HFC-410A
Condenser Type: Air-cooled
Compressor: Centrifugal, variable capacity

Dimensions & Weight:
  Length: 15'-6"
  Width: 8'-2"
  Height: 7'-10" (with condenser fan)
  Operating Weight: 28,500 lbs
  Shipping Weight: 32,000 lbs
  Installation Notes: Requires reinforced roof framing (see attached structural calcs)

Performance Data:
  Cooling Capacity: 400 TR at AHRI rated conditions
  Efficiency: 16.2 EER (Energy Efficiency Ratio)
  Sound Level: 78 dBA at 10 feet
  Refrigerant Charge: 2,800 lbs (HFC-410A)
  Operating Pressure Range: 80-400 psig

Testing & Certifications:
  AHRI Certification: Certificate #123456789
  UL Listed: Yes (U.S. and Canada)
  Safety Standards: UL 1995, CSA C22.2 No. 236
  Efficiency Standards: 10 CFR Part 431 (DOE certified)
  Sound Rating: Per ISO 3744

Installation Requirements:
  Electrical: 480V, 3-phase, 60 Hz, 380 amps
  Electrical Panel: 500 amp main disconnect required
  Cooling Water: 2,000 GPM ± 10% flow requirement
  Water Temp: 55°F-85°F supply, 70°F-95°F return
  Water Quality: Cooling tower water treatment per Carrier specs
  Vibration Isolation: Elastomeric isolators required
  Connection: Flanged connections for water and suction/discharge
  
Lead Time:
  Approval Date: (pending)
  Manufacturing: 12 weeks from order
  Shipping: 2 weeks
  Installation: Requires 2 weeks for mechanical + electrical + controls
  Equipment Delivery Deadline: (critical path date)
  
Warranty:
  Compressor: 5 years parts and labor
  Heat Exchanger: 10 years parts, 5 years labor
  Electrical Components: 2 years
  
Supplier Contact:
  Local Representative: (name, phone, email)
  Factory Support: (phone, email for technical issues)
  Parts Availability: (local stocking distributor)
```

---

## Vendor and Supplier Data Extraction

When submittals include vendor quotes, catalogs, or capability statements, extract supplier information for procurement tracking.

### Core Vendor Fields

| Field | Type | Priority | Notes |
|-------|------|----------|-------|
| **Company Name** | Text | CRITICAL | Legal name (not dba) |
| **Address** | Text | CRITICAL | Street, city, state, ZIP |
| **Phone** | Phone | HIGH | Main number and sales contact |
| **Email** | Email | HIGH | Quotes and technical contact |
| **Website** | URL | MEDIUM | For reference and capabilities |
| **Primary Products/Services** | Text | HIGH | What they specialize in |
| **Certifications** | Text | HIGH | ISO, UL, AISC, NFPA, industry-specific |
| **Key Capabilities** | Text | MEDIUM | Fabrication, testing, installation services |
| **Lead Time Standard** | Duration | CRITICAL | Typical delivery time |
| **Lead Time for This Project** | Duration | CRITICAL | Specific delivery date if quoted |
| **Unit Price** | Currency | MEDIUM | $/unit if applicable |
| **Minimum Order Quantity** | Number | MEDIUM | MOQ for this product |
| **Payment Terms** | Text | MEDIUM | Net 30, COD, etc. |
| **Local Representative** | Text | MEDIUM | On-site contact for support |

### Extraction Method: Vendor Quote or Capability Statement

**Example Vendor Data from Submittal Cover Letter:**

```
Submittal: 03300-1
Vendor: ABC Ready Mix Concrete, Denver, CO

Company Details:
  Legal Name: ABC Concrete Company, Inc.
  Address: 2850 E. Platte Ave., Denver, CO 80210
  Phone: (303) 555-0147
  Technical Contact: Jim Henderson, Technical Rep
  Email: jim.henderson@abcconcrete.com
  Website: www.abcconcrete.com
  
Capabilities:
  - Ready-mix concrete production (daily)
  - Custom mix design per ASTM, ACI standards
  - Truck delivery to site (12-truck fleet)
  - On-site testing and slump verification
  - Pumping services available (subcontracted)
  
Certifications:
  - NSF/ANSI 61 certified (drinking water contact)
  - NRMCA member (National Ready Mix Concrete Assoc.)
  - QC certified per ASTM standards
  - ACI Concrete Practice Programs
  
Lead Times:
  Standard: Next-day delivery
  This Project: Daily ordering, no advance lead time required
  Special Mixes: Up to 1 week if special admixtures needed
  
Pricing & Terms:
  Price: $152/CY (subject to change monthly)
  Minimum Order: 5 CY per truck
  Payment Terms: Net 15 (invoice date)
  Ready-Mix Trucks: 8-yard capacity standard
  
Delivery Constraints:
  Hours: 6:00 AM - 4:00 PM, Monday-Friday
  Access: Require clear access road, 18-foot clearance minimum
  Weekend/Holiday: Premium rate +$15/CY (approval required)
```

**Example Vendor Data from Steel Fabricator Submittal:**

```
Submittal: 05120-3
Vendor: Midwest Steel Fabricators, Chicago, IL

Company Details:
  Legal Name: Midwest Steel Fabricators, Inc.
  Address: 3400 S. Ashland Ave., Chicago, IL 60608
  Phone: (312) 555-0198
  Sales Contact: Sarah Martinez, Project Manager
  Email: smartinez@midweststeel.com
  Website: www.midweststeel.com
  
Capabilities:
  - Structural steel fabrication (up to 500 tons/month)
  - AISC certified shop (Shop Certification Category C)
  - Bolted connections (snug-tight and full-tension)
  - Welded connections with CWI inspection
  - Architectural steel finishes available
  - Detailing and CAD services included
  
Certifications:
  - AISC Certified (Category C - highest level)
  - AWS Certified (American Welding Society)
  - NDE inspectors on staff (UT, MT, PT)
  - ISO 9001:2015 Quality Management
  
Lead Times:
  Standard: 10-12 weeks from approval
  This Project: 8 weeks (expedite available with premium)
  Expedite Cost: +15% of fabrication cost
  
Pricing & Terms:
  Quoted Price: $85/lb of structural steel (escalation clause for material)
  Estimated Total Tonnage: 280 tons
  Estimated Cost: $23,800 (280 tons × 2,000 lbs/ton × $85/lb)
  Payment Terms: 1/3 on order, 1/3 at progress, 1/3 at completion
  Change Order Rate: Time + materials @ $95/labor hour
  
Key Personnel:
  Project Manager: Sarah Martinez, (312) 555-0198 ext. 201
  Quality Manager: John Wong, (312) 555-0198 ext. 305
  Safety Officer: Robert Davis, (312) 555-0198 ext. 410
  
Delivery:
  Ship Via: Common carrier (freight cost separate)
  Destination: Site address (freight pre-paid by vendor)
  Unloading: Vendor provides forklift assist if needed (hourly rate $150/hr)
```

---

## Cross-Referencing and Linking

Link RFIs, submittals, and vendor data to enable comprehensive intelligence about procurement, design decisions, and field sequencing.

### RFI-to-Submittal Links

When an RFI impacts or is resolved by a submittal:

**Link Type 1: RFI blocks submittal approval**
```
RFI-008: "Grid A column location tolerance?"
  Blocks: Submittal 05120-1 (Structural steel fabrication)
  Link: "Cannot approve steel until grid tolerance confirmed"
  Status: RFI answered 01/16/26 → Submittal approved 01/20/26
  Impact: 4-day delay in steel approval
```

**Link Type 2: Submittal response addresses RFI**
```
RFI-012: "What is concrete mix design for Grade Beams?"
  Resolved By: Submittal 03300-2 (Concrete mix design documentation)
  Link: "See page 2, Grade Beam Mix Design"
  Status: RFI closed upon submittal approval
```

**Link Type 3: Submittal resubmittal due to RFI comments**
```
Submittal 05120-2 (Original)
  Status: Revise & Resubmit
  Reason: Comments reference RFI-010 (Connection detail clarification)
  Link: "Design team requires clarification from RFI-010 before approval"
  
Submittal 05120-2 (Resubmittal)
  Date: 01/28/26 (12 days later, per RFI-010 response date)
  Link: "Updated per RFI-010 response received 01/26/26"
  Status: Approved 02/01/26
```

### Specification-to-Submittal Links

Link submittals to specification requirements:

```
Submittal 03300-1 (Concrete Mix Design)
  Section: 03 30 00 (Cast-in-Place Concrete)
  Spec Requirements Verified:
    - Mix strength: 4,000 PSI per spec requirement
    - W/C ratio: 0.45 max per 03 30 00, Para 2.3.1
    - Air content: 5.5% ± 1.5% per 03 30 00, Para 2.3.2
    - Slump: 4" ± 1" per 03 30 00, Para 2.3.3
    - Testing frequency: 1 set per 50 CY per 03 30 00, Para 3.2.1
  Status: All submittal specs meet specification requirements ✓
```

### Drawing-to-RFI Links

Cross-reference RFI questions to design drawings:

```
RFI-015: "Foundation wall height at Grid C?"
  Referenced Drawings: A-101 (Floor Plan), S-101 (Foundation Detail)
  Question: Design shows 8'-4" at Grid C but 7'-8" at Grid A. Which is correct?
  Response Drawing: S-101, Detail 3/S-101 shows 8'-4" with ±1/2" tolerance
  Resolved: Grid C is 8'-4" (matches Grid A when tolerance considered)
  Link: Ground floor elevation drawing updated per RFI response
```

### Submittal-to-Submittal Dependencies

Track dependencies between submittals:

```
Submittal 15050-1 (HVAC Chiller - 400 TR)
  Dependent On: 03300-2 (Concrete - Roof slab structural capacity verification)
  Link: "Rooftop equipment requires confirmation of roof structural capacity"
  Sequence: 03300-2 must be approved first for equipment installation planning
  
Submittal 15060-1 (Piping and Pumps)
  Dependent On: 15050-1 (HVAC equipment specifications)
  Link: "Cooling loop connections sized based on equipment specs"
  Sequence: 15050-1 approval triggers 15060-1 submittal
```

### Schedule Impact Linkage

Track how RFI delays and submittal approvals impact schedule:

```
Critical Path Analysis:
  RFI-007 (01/15/26): CMU wall tolerance
  Response: 01/22/26 (7 days, within float)
  
  RFI-008 (01/16/26): Steel grid tolerance
  Response: 01/22/26 (6 days, within float) 
  
  Submittal 05120-1: Structural Steel
  Submitted: 01/22/26 (after RFI-008 response)
  Approved: 01/26/26 (4 days)
  Lead Time: 8 weeks to fabrication completion
  Delivery Date: 03/18/26
  Installation Scheduled: 03/20/26
  Status: 2-day float on critical path
  Risk: High - any further delays compress schedule
```

### Vendor Capability Links

Link submittals to vendor capabilities and prior performance:

```
Submittal 03300-1 (ABC Ready Mix Concrete)
  Vendor: ABC Concrete Company, Denver, CO
  Prior Projects: 
    - XYZ Tower (2024): 8,000 CY delivered on-time
    - ABC Building (2023): Custom mixes for 12-week project
  Capabilities Match:
    - Custom mix design ✓
    - Daily delivery ✓
    - On-site testing ✓
    - Pumping services (available subcontracted) ✓
  Confidence Level: High (proven track record)
```

---

## Cross-Referencing Table Template

Use this table to track all links between RFIs, submittals, specs, and drawings:

| RFI # | Submittal # | Spec Section | Drawing Ref | Issue | Status | Impact |
|-------|-------------|--------------|-------------|-------|--------|--------|
| RFI-007 | — | 04 20 00 | A-101, S-101 | Wall tolerance | Closed | +2 days delay |
| RFI-008 | 05120-1 | 05 12 00 | S-101, S-102 | Grid tolerance | Closed | Submittal wait time |
| RFI-012 | 03300-1 | 03 30 00 | S-101 | Mix design clarity | Closed | None |
| — | 05120-2 | 05 12 00 | S-201 | See RFI-010 | Approved | Tied to RFI-010 |
| — | 15050-1 | 15 05 00 | M-101 | Equipment capacity | Approved | Dependent on roof slab |

---

## Quality and Confidence

### Validation Checks

Before accepting extracted data, verify:

| Check | Method | Action |
|-------|--------|--------|
| RFI numbers are sequential | Compare RFI-001 through RFI-XXX | Flag gaps or duplicates |
| Dates are chronological | Response Date ≥ Submitted Date | Flag if reversed |
| Status field is valid | Match against enum: Open, Answered, Closed | Flag invalid values |
| Cross-references exist | Verify drawing/section numbers in design docs | Note as "verify in plans/specs" if unfound |
| Lead times are realistic | Compare to industry standards | Flag if <1 day or >52 weeks |
| Blocking work is justified | RFI answer must be critical to work | Flag if blocking claim seems weak |

### Confidence Scoring

Rate confidence of each extraction:

**HIGH Confidence** (95%+)
- Data directly copied from structured table
- Dates in standard format (MM/DD/YY)
- Status from predefined list
- Numbers clearly readable

**MEDIUM Confidence** (75-95%)
- Data extracted from narrative text
- Dates inferred from context
- Status approximated from wording ("almost approved" → "Approved as Noted")
- Numbers interpreted from unclear handwriting

**LOW Confidence** (<75%)
- Data from poor-quality scans
- Handwritten entries
- Conflicting information in document
- Reference document not available for verification

### Common Extraction Errors and Prevention

| Error | Cause | Prevention |
|-------|-------|-----------|
| RFI marked "Answered" but no response documented | RFI log has status column but no response column | Extract response separately; cross-check with RFI correspondence files |
| Submittal status incorrect | Confusion between "Submitted" and "Status" columns | Verify with date columns: Status should be result of review |
| Lead time unrealistic | Confusion between "lead time" and "days to approval" | Lead time = time from approval to delivery, not approval time |
| Wrong spec section | OCR error or misread section number | Verify section numbers exist in specifications TOC |
| Missing blocking work flag | Assumed not critical if RFI response was quick | Review work sequencing schedule; assess if answer could have been pending |

### Documentation Requirements

For each RFI or submittal extracted, maintain:

1. **Source document** - Save original PDF with metadata
2. **Extraction date and time** - When was this data pulled?
3. **Extractor notes** - Any confidence issues or clarifications
4. **Verification status** - Has data been cross-checked to source docs?
5. **Related files** - Links to RFI correspondence, submittal packages, photos

**Example Extraction Record:**

```
RFI-007 (CMU Wall Tolerance)
  Source Document: RFI_Log_January_2026.pdf (pages 2-3)
  Extraction Date: 02/10/26, 10:45 AM
  Extracted By: Field Documentation System
  Confidence: HIGH
  
  Extractor Notes:
    - Response found in separate RFI correspondence file (RFI-007_Response.pdf)
    - Date 01/22/26 verified against email header
    - Blocking work validated against schedule: CMU work on critical path
    
  Verification:
    - Drawing references verified: A-101 and S-101 exist in drawing set ✓
    - Spec section 04 20 00 exists in specification ✓
    - RFI response cross-checked: "See S-101, Detail 3/S-101" ✓
    
  Related Files:
    - RFI_Log_January_2026.pdf (source)
    - RFI-007_Response.pdf (response correspondence)
    - S-101_Detail3_CMU.pdf (referenced detail)
    - 04_20_00_Unit_Masonry_Spec.pdf (referenced spec)
```

---

## Integration with Construction Workflows

### Daily Report Integration

Use RFI and submittal data to auto-populate daily reports:

- **Work Pending RFI Response**: Flag if today's scheduled work blocked by open RFI
  - Example: "CMU wall layout pending RFI-007 response (due by 01/20/26)"

- **Submittal Status Updates**: Track approval progress for scheduled procurements
  - Example: "Structural steel submittal approved 01/26/26; fabrication 8 weeks = delivery 03/18/26"

- **Vendor Coordination**: Log calls/communications to approved vendors
  - Example: "Contacted ABC Ready Mix re: delivery schedule for 01/10/26 concrete pour"

### Schedule Integration

- **Schedule Risk Analysis**: Identify critical path RFIs and submittals
  - If RFI is open + blocking + 5+ days to response = escalate
  - If submittal pending approval + lead time ≤ days until needed = risk

- **Procurement Timeline**: Calculate submit/approve/deliver dates for each submittal
  - Track margin between approval date and required-by date

### Quality Control Integration

- **Pre-Installation Verification**: When equipment arrives, compare to submittal specs
  - Example: "Steel delivery 03/18/26: verify bolts are ASTM A325, 7/8" diameter per submittal 05120-1"

- **Change Order Tracking**: Link submittals to any related change orders
  - Example: "RFI-015 response resulted in ECO #003 for additional framing cost"

---

## Summary of Key Extraction Tables

### RFI Log Extraction Summary

**Minimum fields required:**
- RFI Number, Date Submitted, Subject, Drawing Refs, Spec Refs, Status, Blocks Work, Lead Time Impact

**Optional but valuable:**
- Response, Responder, Follow-up, Schedule Impact, Related RFI/Submittal

### Submittal Log Extraction Summary

**Minimum fields required:**
- Submittal Number, Spec Section, Item, Status, Lead Time, Critical Path, Comments

**Optional but valuable:**
- Manufacturer, Model, Approver, Resubmittal Needed, Final Status Date

### Submittal Package Extraction Summary

**Minimum fields required:**
- Product Name, Manufacturer, Model, Performance Data (strength/ratings), Certifications, Lead Time

**Optional but valuable:**
- Dimensions, Weight, Installation Details, Connection Specs, Testing Results

### Vendor Data Extraction Summary

**Minimum fields required:**
- Company Name, Address, Phone, Email, Certifications, Lead Time, Price

**Optional but valuable:**
- Capabilities, Key Personnel, Payment Terms, Prior Projects

---

## Reference Standards and Specifications

### Industry Standards Referenced

- **ASTM Standards**: For material testing and performance specs
  - ASTM C39 - Compression test of concrete
  - ASTM C494 - Concrete admixtures
  - ASTM F1234 - Product testing standards (varies by material)

- **ACI Standards**: American Concrete Institute
  - ACI 318 - Building Code Requirements for Structural Concrete
  - ACI 305 - Hot Weather Concreting
  - ACI 306 - Cold Weather Concreting

- **AISC Standards**: American Institute of Steel Construction
  - AISC 360 - Structural Steel Design and Construction
  - AISC 358 - Prequalified Connections (bolted/welded)

- **CSI Format**: MasterFormat 2016 for specification section numbering
  - 03 30 00 - Cast-in-Place Concrete
  - 04 20 00 - Unit Masonry
  - 05 12 00 - Structural Steel
  - 15 05 00 - HVAC Equipment
  - etc.

- **UL/ETL Certifications**: Product safety and performance
- **NFPA Standards**: Fire protection systems (NFPA 72, etc.)
- **EPA Standards**: Environmental compliance (SWPPP, etc.)

---

**This reference guide enables systematic extraction and cross-referencing of RFI and submittal data to support scheduling, procurement, quality control, and project management.**
