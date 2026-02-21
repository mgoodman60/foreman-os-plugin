# pay-application — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the pay-application skill.



## Percentage Complete Calculation

Percentage complete is the critical metric driving all payment calculations. It reflects actual work progress against the contract scope.

### Core Logic

```
Percent Complete = (Work Completed + Materials Stored) / Revised Contract Amount × 100%
```

### Validation Rules

1. **No Backward Movement**: Once a line item reaches a certain percent complete, it cannot decrease
   - If PAY-001 shows Concrete at 50% complete, PAY-002 cannot show Concrete at less than 50%
   - Violation: System blocks update and requires user review

2. **Cannot Exceed Contract Amount**: Total billable amount (work + materials) cannot exceed revised contract amount
   - If revised contract is $200,000, billable amount is capped at $200,000
   - System calculates percent complete capped at 100%

3. **Materiality Threshold**: Changes <$100 may be flagged as "immaterial" and allowed to vary slightly
   - Useful for minor rounding or adjustment of stored materials

4. **Work Complete Before Materials**: Work completion typically precedes (or equals) material storage removal
   - Flag if materials stored exceeds work completed (suggests materials received but not yet installed)

### W Principles Retainage Policy

W Principles uses a flat 10% retainage throughout the project:

| Project Progress | Retainage Rate | Application |
|------------------|----------------|-------------|
| 0–99% complete | 10% | Applied to all work and materials (flat rate) |
| 100% (Substantial Completion) | 0% | All retainage released at substantial completion |
| Final Payment | 0% | No retainage, final balances paid |

**Implementation Logic:**
```python
def calculate_retainage(line_item):
  if project_percent_complete < 1.00:
    retainage_rate = 0.10  # W Principles: flat 10% until substantial completion
  else:
    retainage_rate = 0.00

  work_retainage = line_item['work_completed'] * retainage_rate
  materials_retainage = line_item['materials_stored'] * retainage_rate
  return work_retainage + materials_retainage
```

**Contract Override Option:**
- Some contracts may specify different retainage rates — check project-config.json for per-project overrides
- W Principles default is flat 10%; override only if contract explicitly states otherwise



## Pay Application Numbering System

Pay application IDs follow the format **PAY-{NNN}** where NNN is a zero-padded three-digit counter:
- First pay app: PAY-001
- Second pay app: PAY-002
- Pattern: PAY-100, PAY-101, etc.

**Key Rules:**
- Numbers auto-increment based on highest existing pay app
- **Numbers are locked immediately upon creation** — never reused
- Sequential integrity maintained across all sessions
- Each PAY-NNN corresponds to a single billing period



## Change Order Integration

Approved change orders automatically update the revised contract amount but do not alter the SOV structure.

### Workflow

1. **Change Order Approved**: CO reaches "approved" status in change-order-log.json
2. **Pay App System Detects**: Next time pay app is generated or status reviewed, system checks for new approved COs
3. **Revised Contract Updated**:
   ```
   Revised Contract Amount = Original Contract Amount + Sum(All Approved COs)
   ```
4. **SOV Line Items Updated**: Each line item's revised contract amount reflects applicable COs
5. **Percent Complete Recalculated**: Based on new revised contract amount
6. **G702/G703 Reflects Change**: Shows original contract, CO adjustments, and revised amount on document

### Example

**Original Contract**: $2,770,000
**After CO-001 (Approved +$50,000)**: $2,820,000
**After CO-003 (Approved -$15,000)**: $2,805,000
**Current Revised Contract**: $2,805,000

All subsequent pay apps reference the $2,805,000 revised amount.



## Stored Materials Tracking

Materials on site but not yet installed are billable and subject to retainage, but tracked separately from installed work.

### Stored Materials Workflow

1. **Subcontractor Delivers Material**: Materials arrive on site
2. **Superintendent Verifies**: Confirms receipt, location, and condition against packing slip
3. **Log as Stored Material**: Update pay-app-log.json with amount and location
4. **Include in Billing**: Stored materials count toward percent complete calculation
5. **Upon Installation**: Work crew installs material
6. **Reclassify as Work Completed**: Move amount from "materials stored" to "work completed" in next pay app
7. **Continued Retainage**: If materials stored at <50% complete, both retain at 10%; same for installed work

### Accounting Treatment

- **Billable but not yet working**: Allows contractor to invoice for delivered materials even if not yet installed
- **Typical scenario**: Long-lead items (HVAC units, roof trusses) delivered and stored weeks before installation
- **Owner benefit**: Owns materials once stored (security interest)
- **Contractor cash flow**: Improves by billing upon delivery, not delayed until installation



## Stored Materials Example

**Pay Period**: Feb 1–28, 2026
- PEMB Steel arrives on 02/15
- Weight: 80 tons at $200/ton = $16,000
- Stored on site (awaiting March erection)

**Pay App PAY-001 (Through Feb 28)**:
- Work Completed: $150,000
- Materials Stored: $16,000 (PEMB steel)
- Billable: $166,000
- Percent Complete: $166,000 / $2,805,000 = 5.9%
- Retainage (10%): $16,600
- Amount Due: $149,400

**Pay App PAY-002 (Through Mar 31)**:
- Work Completed (including PEMB erection): $300,000 (includes that $16,000 steel now installed)
- Materials Stored (new arrivals): $25,000
- Previous Billing (from PAY-001): $166,000
- Cumulative Work Completed: $300,000 + $25,000 = $325,000
- Percent Complete: $325,000 / $2,805,000 = 11.6%
- Retainage (10%): $32,500
- Prior retainage released: $16,600
- New retainage: $32,500 - $16,600 = $15,900 additional held
- Amount Due This Period: (325,000 - 166,000) - $15,900 = $143,100



## Data Structure & Storage

All pay application data is stored in `pay-app-log.json`:

```json
{
  "pay_apps": [
    {
      "id": "PAY-001",
      "period_number": 1,
      "period_start_date": "2026-02-01",
      "period_end_date": "2026-02-28",
      "application_date": "2026-03-01",
      "status": "submitted",
      "created_date": "2026-03-01",
      "submitted_date": "2026-03-02",
      "paid_date": "2026-03-10",
      "paid_amount": 149400,
      "schedule_of_values": [ /* array of line items */ ],
      "original_contract_amount": 2770000,
      "change_orders_applied": [ /* array of approved CO refs */ ],
      "revised_contract_amount": 2805000,
      "cumulative_statistics": { /* running totals */ },
      "retainage_tracking": { /* 10%/5% breakdown */ },
      "lien_waivers": { /* 4 types tracked */ },
      "sub_pay_apps": [ /* individual sub apps */ ]
    }
  ]
}
```



## Daily Report Integration for % Complete

The daily report captures field progress and feeds directly into pay application % complete calculations.

### Field Observation Mapping

**Daily Report Structure for Progress:**
```json
{
  "date": "2026-02-14",
  "weather": "Clear, 55°F",
  "daily_activities": [
    {
      "activity_id": "ACT-023",
      "description": "Foundation walls excavation, Grid B-1 through B-4",
      "trade": "Sitework",
      "csi_division": "02",
      "quantity": "450 cubic yards",
      "quantity_unit": "cy",
      "percent_progress": "100",
      "comments": "Completed 3.5' fill removal and prepared for concrete"
    },
    {
      "activity_id": "ACT-024",
      "description": "Concrete foundation placement, Grid A-1 to A-2",
      "trade": "Concrete",
      "csi_division": "03",
      "quantity": "180 cubic yards",
      "quantity_unit": "cy",
      "percent_progress": "75",
      "comments": "Poured 135 cy, 45 cy scheduled tomorrow morning"
    }
  ]
}
```

### Pay App % Complete Algorithm

**For Each SOV Line Item:**

1. **Sum completed quantities** from daily_activities for matching CSI division and period
   - Example: "Sitework" daily activities in Feb show 450 cy completed

2. **Map to contract value** using productivity rates or contract breakdown
   - Example: Contract SOV-002 budgets $220,000 for Sitework
   - If 450 cy represents, say, 38.6% of total scope → $85,000 earned value

3. **Add materials stored** from procurement-log.json (delivered but not installed)
   - Example: PEMB steel ($16,000) delivered and stored 02/15
   - Add to work completed: $85,000 + $16,000 = $101,000

4. **Calculate % Complete**
   - $101,000 / $220,000 = 45.9% for this line item

5. **Flag Discrepancies**
   - If schedule shows 52% complete but field shows 45%, flag: "Schedule/field variance 7%. Review?"
   - Encourage superintendent input: "Schedule shows higher completion. Are you being conservative? Schedule ahead?"

### W Principles Retainage Calculation

**Automated Calculation (Flat 10%):**
```python
def determine_retainage_rate(project_percent_complete):
    if project_percent_complete < 1.00:
        return 0.10  # W Principles: flat 10% until substantial completion
    else:
        return 0.00  # 0% at substantial completion
```

**Example Progression (Flat 10%):**
- PAY-001 (12% complete): 10% retainage = $16,600 held
- PAY-002 (28% complete): 10% retainage = $27,600 total held
- PAY-003 (45% complete): 10% retainage = $44,000 total held
- PAY-004 (52% complete): 10% retainage (stays flat) = $57,200 total held
- PAY-005 (75% complete): 10% retainage = $82,500 total held
- PAY-007 (100% at Substantial Completion): 0% retainage; all retainage released



## Lien Waiver Types and Requirements

Lien waivers are legal documents that waive a party's right to file a mechanic's lien against the property. They are essential to the pay application process because they protect the owner from double-payment claims and ensure the payment chain flows properly from owner to GC to subcontractors to suppliers.

### Four Types of Lien Waivers (Per AIA Standard Forms)

#### 1. Conditional Waiver on Progress Payment

**Purpose**: Waives lien rights ONLY upon actual receipt of payment. The waiver is not effective until the check clears or the wire transfer is confirmed.

**When Used**: Submitted by each subcontractor with each monthly pay application. The GC collects conditional progress waivers from all subs and submits them to the owner along with the GC's pay application.

**Key Feature**: If the payment bounces or is never received, the waiver is void and the sub retains full lien rights.

**AIA Form**: G706A (Contractor's Affidavit of Release of Liens) references conditional waivers.

**Example Language**: "Upon receipt of the sum of $45,000.00, the undersigned waives and releases any and all lien rights through the date of February 28, 2026, for labor, services, equipment, or materials furnished to the project."

#### 2. Unconditional Waiver on Progress Payment

**Purpose**: Waives lien rights regardless of whether payment has been received. This is an absolute waiver for the specified period and amount.

**When Used**: Submitted after payment has been received and confirmed. Typically, unconditional waivers for Period N are collected after the GC receives payment for Period N and distributes it to subs. These unconditional waivers are then submitted with the pay application for Period N+1.

**Key Feature**: Once signed, the sub cannot file a lien for the covered period, even if the payment is later reversed or disputed.

**Risk**: Subs should NEVER sign unconditional waivers until they have confirmed receipt of payment. Signing an unconditional waiver before payment is received eliminates lien protection.

#### 3. Conditional Waiver on Final Payment

**Purpose**: Waives ALL lien rights for the entire project, conditioned upon receipt of the final payment amount.

**When Used**: Submitted with the final pay application. The sub signs a conditional final waiver stating that upon receipt of the final payment (including all retainage), they waive all lien rights for all work performed on the project.

**Key Feature**: Covers all work from project start through completion, not just a single billing period. Effective only upon receipt of the stated final payment amount.

#### 4. Unconditional Waiver on Final Payment

**Purpose**: Final and absolute waiver of all lien rights for the entire project. No conditions, no contingencies.

**When Used**: This is the last document collected before the owner makes final payment. After the sub receives final payment (including retainage release), the sub signs the unconditional final waiver. This closes out all lien exposure for that sub on the project.

**Key Feature**: Once signed, the sub has permanently waived all lien rights. There is no recourse for additional payment after this waiver is executed.

### When Each Type Is Required in the Pay App Cycle

```
PAY APP CYCLE                           WAIVER TYPE REQUIRED
─────────────────────────────────────────────────────────────────
Pay App N submitted to owner        →   Conditional Progress (current period N)
                                    +   Unconditional Progress (prior period N-1)
Owner approves and pays             →   GC distributes to subs
Subs confirm receipt of payment     →   Subs sign Unconditional Progress (period N)
Pay App N+1 submitted               →   Conditional Progress (period N+1)
                                    +   Unconditional Progress (period N)
...
Final Pay App submitted             →   Conditional Final (all work)
                                    +   Unconditional Progress (prior period)
Owner makes final payment           →   GC distributes final payment
Subs confirm receipt                →   Subs sign Unconditional Final
Project closeout complete           →   All waivers on file; lien exposure = $0
```

### Waiver Collection Checklist

For each pay application period, the GC must collect:

**From Each Subcontractor**:
- Conditional progress waiver for current period (submitted with pay app)
- Unconditional progress waiver for previous period (submitted after payment received)

**From Each Sub's Suppliers** (if applicable):
- Conditional progress waiver from material suppliers to sub
- Particularly important for large material purchases (steel, PEMB, major equipment)
- GC may require sub to provide supplier waivers as condition of payment

**GC Responsibility**:
- Track all waivers in pay-app-log.json lien_waivers section
- Do not submit pay app to owner without all conditional progress waivers
- Do not release retainage without all unconditional final waivers
- Maintain copies of all executed waivers in project files

### Waiver Tracking Table

```
Sub Name              Waiver Type              Period        Amount       Received Date   Status
Walker Construction   Conditional Progress     Feb 2026     $45,000      02/28/26        Received
Walker Construction   Unconditional Progress   Jan 2026     $32,000      02/15/26        Received
W Principles          Conditional Progress     Feb 2026     $67,200      02/28/26        Received
W Principles          Unconditional Progress   Jan 2026     $0           N/A             N/A (first period)
Davis & Plomin        Conditional Progress     Feb 2026     $75,700      02/28/26        Received
Alexander Steel       Conditional Progress     Feb 2026     $120,000     PENDING         OUTSTANDING
EKD Framing           Conditional Progress     Feb 2026     $55,000      02/27/26        Received
Schiller Doors        Conditional Progress     Feb 2026     $0           N/A             No work this period
```

### Common Waiver Issues

1. **Conditional vs. Unconditional Confusion**: Subs sometimes sign unconditional waivers thinking they are conditional. Always verify waiver type before signing. Unconditional waivers cannot be revoked.

2. **"Through Date" vs. "Through Amount" Discrepancy**: The waiver must specify both the date through which lien rights are waived AND the dollar amount. If the "through date" is February 28 but the amount covers only January work, there is a gap in coverage.

3. **Partial Waivers**: Some subs attempt to submit waivers for less than the full invoiced amount (e.g., waiving $40,000 on a $45,000 invoice). Partial waivers create lien exposure for the uncovered amount. GC should require full-amount waivers.

4. **Supplier Waivers Missing**: GC collects waivers from subs, but subs may not collect waivers from their material suppliers. If a supplier files a lien, the owner is exposed even though the sub signed a waiver. Best practice: require sub to provide supplier waivers for purchases exceeding $10,000.

5. **Expired or Stale Waivers**: Waivers should be dated within the current billing period. A waiver dated 60 days ago may not cover recent work. Always verify waiver dates match the pay app period.

---



## State-Specific Lien Law Awareness

Lien waiver requirements, forms, and filing deadlines vary significantly by state. Using the wrong form or missing a deadline can invalidate lien rights or create legal exposure.

### Statutory Lien Waiver Forms

Several states mandate the use of specific statutory lien waiver forms. Using a non-statutory form in these states may render the waiver unenforceable:

- **California**: Civil Code Section 8132-8138 prescribes exact waiver language for all four types. Non-statutory forms are void.
- **Texas**: Property Code Chapter 53 requires specific statutory forms. Waivers that deviate from statutory language are unenforceable.
- **Michigan**: Construction Lien Act Section 570.1115 prescribes statutory waiver forms.
- **Georgia**: O.C.G.A. Section 44-14-366 establishes waiver requirements.
- **Arizona**: A.R.S. Section 33-1008 prescribes statutory forms.
- **Other States**: Many states have no statutory form requirement; AIA standard forms are generally accepted.

**Best Practice**: Always verify the lien waiver form requirements for the state where the project is located. When in doubt, use the state's statutory form.

### Preliminary Notice Requirements

A preliminary notice (also called a preliminary lien notice or pre-lien notice) is a document that a sub, supplier, or laborer must file to preserve their lien rights. Requirements vary by state:

- **Who Must File**: In most states, subcontractors and material suppliers who do not have a direct contract with the owner must file preliminary notice. Some states require all parties (including GCs) to file.
- **When to File**: Typically within 20-30 days of first furnishing labor or materials to the project. California requires filing within 20 days; Texas requires filing within the 2nd or 3rd month of work.
- **What Happens If You Don't File**: In many states, failure to file preliminary notice waives the right to file a mechanic's lien entirely. The sub or supplier loses all lien protection.
- **GC Awareness**: GC should track whether subs and suppliers have filed preliminary notices. If a sub has NOT filed preliminary notice, their lien rights may be limited, which affects the GC's waiver collection strategy.

### Filing Deadlines

Mechanic's lien filing deadlines vary widely by state:

- **California**: 90 days from completion of work (for direct contractors), 90 days from notice of completion (for subs/suppliers)
- **Texas**: GCs: 4th month after work complete. Subs: 2nd month after work complete (residential) or 3rd month (commercial).
- **Florida**: 90 days from last furnishing labor/materials
- **New York**: 8 months from completion (private work); 30 days from acceptance (public work)
- **Kentucky**: 6 months from last day labor performed or materials furnished
- **Ohio**: 60 days from completion or last furnishing date

**GC Impact**: If a sub files a lien, the owner may withhold payment from the GC until the lien is resolved. GC must track sub lien filing status and ensure timely waiver collection to prevent lien filings.

### Stop Notice / Notice to Withhold

A stop notice (or notice to withhold) is a legal mechanism that an unpaid sub or supplier can use to require the owner to withhold funds from the GC:

- **How It Works**: The unpaid party serves a written notice on the owner stating that they have not been paid and demanding that the owner withhold sufficient funds from the GC to cover the claim.
- **GC Responsibility**: If a stop notice is filed, the GC must resolve the payment dispute with the sub before the owner will release withheld funds.
- **Prevention**: Timely payment to subs and collection of lien waivers prevents stop notice filings. Track all sub payment status in the pay app cycle.

**Cross-Reference**: See the contract-administration skill for a comprehensive state-by-state lien law guide, including filing deadlines, preliminary notice requirements, and statutory waiver forms.

---



## Pay App Lien Waiver Workflow

The lien waiver workflow is a step-by-step process that ensures proper waiver collection, payment distribution, and lien protection throughout the pay app cycle.

### Step-by-Step Process

**Step 1: GC Submits Pay App with Conditional Waivers**

The GC prepares the monthly pay application (G702/G703) and collects conditional progress waivers from all active subcontractors for the current billing period. The pay app package submitted to the owner includes:
- G702 Application and Certificate for Payment
- G703 Continuation Sheet (detailed SOV)
- Conditional progress waivers from all subs (current period)
- Unconditional progress waivers from all subs (previous period, if payment was received)

**Step 2: Owner/Architect Reviews and Approves**

The architect reviews the pay app for accuracy, verifies percentage complete against field observations, and certifies the payment amount. The owner reviews the architect's certification and approves payment.

**Step 3: Owner Issues Payment to GC**

The owner issues payment to the GC for the approved amount (less retainage). Payment is typically due within 30 days of pay app submission (per contract terms, often AIA A201 Section 9.6).

**Step 4: GC Distributes Payment to Subs**

Upon receipt of owner payment, the GC distributes payment to each subcontractor per their approved billing amounts (less retainage and any back-charges). Many states require the GC to pay subs within a specified number of days after receiving owner payment (e.g., 7 days in many states).

**Step 5: GC Collects Unconditional Waivers from Subs**

After subs receive and confirm payment for the current period, the GC collects unconditional progress waivers from each sub. These unconditional waivers confirm that payment was received and lien rights for the covered period are permanently waived.

**Step 6: Unconditional Waivers Submitted with Next Pay App**

The unconditional waivers for Period N are included in the pay app package for Period N+1. This creates a rolling waiver trail:
- Pay App N+1 includes: Conditional waivers for Period N+1 + Unconditional waivers for Period N

### Tracking Table Format for the Superintendent

The superintendent should maintain a waiver tracking table that is updated with each pay app cycle:

```
══════════════════════════════════════════════════════════════════════════════════
LIEN WAIVER TRACKING — PAY APP PERIOD: February 2026 (PAY-001)
Project: MOSC-825021 | Updated: 03/01/2026
══════════════════════════════════════════════════════════════════════════════════

                          CONDITIONAL PROGRESS (Feb)     UNCONDITIONAL PROGRESS (Jan)
Sub Name              Amount       Received   Status     Amount       Received   Status
────────────────────────────────────────────────────────────────────────────────────────
Walker Construction   $45,000      02/28      OK         N/A          N/A        First Period
W Principles          $67,200      02/28      OK         N/A          N/A        First Period
Davis & Plomin        $75,700      02/28      OK         N/A          N/A        First Period
Alexander Steel       $120,000     PENDING    CHASE      N/A          N/A        First Period
EKD Framing           $55,000      02/27      OK         N/A          N/A        First Period
Hek Glass             $0           N/A        No Work    N/A          N/A        First Period
Stidham Cabinets      $0           N/A        No Work    N/A          N/A        First Period
Schiller Doors        $0           N/A        No Work    N/A          N/A        First Period
────────────────────────────────────────────────────────────────────────────────────────

SUMMARY:
  Conditional waivers received: 4 of 5 required
  Conditional waivers pending: 1 (Alexander Steel — PEMB materials)
  Unconditional waivers: N/A (first billing period)
  PAY APP HOLD: Cannot submit to owner until Alexander conditional received

ACTION ITEMS:
  [ ] Contact Alexander Steel — request conditional waiver by 03/03
  [ ] Verify Alexander PEMB delivery receipt matches waiver amount
  [ ] Submit pay app to owner upon receipt of all conditional waivers

══════════════════════════════════════════════════════════════════════════════════
```

---



## Integration & Reporting

### Morning Brief Integration

**Overdue Payments:**
- Query pay-app-log.json for pay apps with status "pending payment" and submitted_date > 30 days ago
- Display: "PAY-002 submitted 2026-02-10, still pending from owner (31 days). Escalate?"

**Missing Lien Waivers:**
- For pay apps in "draft" or "submitted" status, check lien_waivers.conditional_progress
- Count received vs. required
- Display: "PAY-001 ready to submit. Pending: 3 conditional waivers (W Principles, Alexander, Electrical). Request today?"

### Weekly Report Integration

**Billing Summary Section:**
```
BILLING SUMMARY — Week of 02/10–02/14

This Period Billings:
  Completed work:     $50,000
  Stored materials:   $8,500
  Subtotal:          $58,500
  Retainage (10%):   -$5,850
  Net Due:           $52,650

Year-to-Date Billings:
  Total Billed:      $166,000
  Total Retainage:   $16,600
  Total Paid:        $149,400
  Outstanding:       $16,600

Cash Flow Projection:
  PAY-001 paid 03/10 (+$149,400)
  PAY-002 due 03/24 (est. $55,000)
  Projected month-end cash: +$165,000
```

### Change Order Auto-Integration

**Workflow:**
1. Change Order approved (CO-001, +$50,000)
2. Next `/pay-app prepare` command runs
3. System detects CO-001 in change-order-log.json with status = "approved"
4. Updates SOV line items with CO amount applied
5. Recalculates revised_contract_amount and percent_complete
6. G702/G703 documents show CO in "Change Order Adjustments" column

**G702/G703 Change Order Section:**
```
SCHEDULE OF VALUES — With Change Order Adjustments

Original Contract Amount:        $2,770,000
Change Orders:
  CO-001 (Approve +$50,000)        +$50,000
  CO-003 (Approved -$15,000)       -$15,000
  ───────────────────────────
Revised Contract Amount:        $2,805,000
```

### Closeout Integration

**Final Pay Application Checklist:**
1. Verify all work 100% complete (or authorized remaining work)
2. Collect all unconditional final lien waivers
3. Verify all change orders fully invoiced
4. Release all retainage
5. Verify all sub final invoices received and reconciled
6. Issue final G702 (no retention)
7. Obtain architect final certification

**Data Structure for Final Status:**
```json
{
  "id": "PAY-008",
  "status": "final",
  "is_final_pay_app": true,
  "total_work_completed": 2805000,
  "percent_complete": 100.00,
  "retainage_rate": 0.00,
  "total_retainage": 0,
  "lien_waivers_required": {
    "unconditional_final": 8,
    "unconditional_final_received": 8,
    "final_status": "complete"
  },
  "closeout_checklist": {
    "punch_list_complete": true,
    "architect_sign_off": true,
    "all_lien_waivers_received": true,
    "retainage_released": true,
    "final_account_reconciliation": true
  }
}
```



## Advanced Scenarios

### Multi-Location or Phased Projects

For projects with multiple buildings or phases:
- Create separate SOV per building/phase if contracts separate
- Or use SOV with phase/location prefix: "Building A - Sitework", "Building B - Sitework"
- Pay applications can be per-building or consolidated depending on contract structure

### Performance Bonds vs. Retainage

Some contracts use performance bonds instead of retainage:
- Override standard 10%/5% with 0% retainage
- Store reference to bond: "Bonded by Fidelity Surety, Bond #5000123"
- Track bond status in project config

### Stored Materials Dispute Resolution

If subcontractor disputes stored material value:
1. Request photographic evidence or invoice from sub
2. Compare to procurement-log.json verified delivery
3. Allow superintendent to adjust if discrepancy identified
4. Document adjustment reason in pay-app-log.json notes
5. Flag for reconciliation at project closeout



## Error Handling & Validation

**SOV Imbalance Prevention:**
- Warn if SOV line items don't sum to contract amount
- Prevent pay app creation if SOV unbalanced
- Force rebalancing before proceeding

**Percent Complete Regression Prevention:**
- Block any attempt to decrease line item % complete
- Require manual superintendent override with justification
- Log override in version history

**Retainage Calculation Validation:**
- Verify retainage never exceeds 10% of work (or contract-specified rate)
- Verify amount due never negative
- Verify cumulative retainage matches sum of individual pay app retainages

**Lien Waiver Enforcement:**
- Cannot mark pay app as "submitted" if conditional progress waivers pending
- Cannot process final payment if any unconditional final waivers missing
- System enforces payment waterfall rules


