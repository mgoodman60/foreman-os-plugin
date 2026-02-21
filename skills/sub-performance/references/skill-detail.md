# sub-performance — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the sub-performance skill.



## Scorecard Data Model (JSON Schema)

Each subcontractor scorecard is stored in a structured JSON record, enabling queries, historical tracking, and trend analysis.

```json
{
  "sub_scorecards": [
    {
      "scorecard_id": "MOSC-SC-001-Walker",
      "project_id": "MOSC-825021",
      "project_name": "Morehead One Senior Care",
      "evaluation_period": "2026-01-21 to 2026-02-28",
      "evaluation_period_phase": "Foundation / Sitework",
      "subcontractor": {
        "name": "Walker Construction",
        "trade": "Excavation / Sitework",
        "contract_id": "SC-825021-Walker",
        "contact": {
          "company_name": "Walker Construction LLC",
          "superintendent": "Juan Rodriguez",
          "phone": "+1-606-234-5678",
          "email": "jrodriguez@walker-construction.com"
        }
      },
      "evaluation_date": "2026-02-28",
      "evaluated_by": "John Smith (Super)",
      "evaluation_notes": "Strong start to project. Reliable schedule performance, excellent safety culture, good quality. Site cleanliness and crew conduct exemplary. Early candidate for incentive bonus.",
      "dimension_scores": {
        "schedule_adherence": {
          "dimension": "Schedule Adherence",
          "weight": 0.25,
          "score": 8,
          "max_score": 10,
          "data_points": {
            "ppc": {
              "value": 87,
              "unit": "%",
              "data_source": "last-planner / PPC by trade",
              "period": "4-week rolling average"
            },
            "crew_consistency": {
              "promised_headcount": 4,
              "average_headcount": 4,
              "consistency": 100,
              "unit": "%",
              "data_source": "daily-report-format",
              "notes": "Crew size consistent throughout evaluation period"
            },
            "milestone_achievement": {
              "milestones_tracked": [
                {
                  "milestone": "Mobilization",
                  "scheduled_date": "2026-01-23",
                  "actual_date": "2026-01-22",
                  "status": "early",
                  "days_variance": -1
                },
                {
                  "milestone": "Excavation north lot complete",
                  "scheduled_date": "2026-02-15",
                  "actual_date": "2026-02-14",
                  "status": "early",
                  "days_variance": -1
                }
              ]
            }
          },
          "scoring_notes": "PPC 87% is solid; crew size consistent; mobilization on time. Minor: 1 task deferred to next phase due to ground saturation (weather, not sub's fault). Rating: 8/10"
        },
        "quality": {
          "dimension": "Quality",
          "weight": 0.25,
          "score": 8,
          "max_score": 10,
          "data_points": {
            "first_pass_inspection_rate": {
              "value": 93,
              "unit": "%",
              "data_source": "inspection-tracker / quality-management",
              "inspections_conducted": 15,
              "inspections_passed": 14,
              "inspections_failed": 1,
              "notes": "1 failed inspection: footing rebar spacing slightly off; remediated same day"
            },
            "punch_list_items": {
              "total_items": 6,
              "sf_completed_by_sub": 1000,
              "items_per_1000_sf": 6,
              "data_source": "punch-list",
              "items": [
                {
                  "item": "Site grade stake slightly out of tolerance",
                  "responsible_trade": "Walker",
                  "severity": "minor",
                  "status": "corrected"
                }
              ]
            },
            "rework_frequency": {
              "value": 2,
              "unit": "%",
              "data_source": "quality-management / daily-report-format"
            },
            "warranty_callbacks": {
              "post_completion_callbacks": 0,
              "data_source": "closeout phase (future)"
            }
          },
          "scoring_notes": "FPIR 93% is excellent. Punch list 6/1000 SF is low (goal <10). Rework 2% is minimal. No callbacks yet. Rating: 8/10"
        },
        "safety": {
          "dimension": "Safety",
          "weight": 0.20,
          "score": 10,
          "max_score": 10,
          "data_points": {
            "recordable_incidents": {
              "count": 0,
              "data_source": "safety-management",
              "note": "No OSHA-recordable incidents"
            },
            "near_miss_events": {
              "count": 0,
              "data_source": "safety-management",
              "note": "Zero near-misses reported"
            },
            "toolbox_talk_attendance": {
              "attendance_rate": 100,
              "unit": "%",
              "talks_conducted": 5,
              "data_source": "safety-management",
              "note": "Weekly toolbox talks attended by all crew members"
            },
            "housekeeping_scores": {
              "average_score": 95,
              "unit": "%",
              "inspections": 8,
              "data_source": "daily-report-format",
              "note": "Site consistently clean and organized; debris cleared daily"
            },
            "ppe_compliance": {
              "compliance_rate": 100,
              "unit": "%",
              "observations": 20,
              "data_source": "daily site observations",
              "note": "All crew members observed with hard hat, hi-vis, steel-toe boots"
            },
            "competent_person_certifications": {
              "required_certifications": ["OSHA Excavation Competent Person"],
              "status": "current",
              "data_source": "contract compliance"
            }
          },
          "scoring_notes": "Perfect safety record. Zero recordables, zero near-misses, 100% toolbox talk attendance, excellent housekeeping, 100% PPE compliance. All certifications current. Exemplary safety culture. Rating: 10/10"
        },
        "responsiveness": {
          "dimension": "Responsiveness",
          "weight": 0.15,
          "score": 9,
          "max_score": 10,
          "data_points": {
            "rfi_response_time": {
              "average_days": 1.5,
              "unit": "business days",
              "rfis_issued": 4,
              "rfis_answered": 4,
              "data_source": "rfi-preparer",
              "response_times": [
                {
                  "rfi_id": "RFI-001",
                  "date_issued": "2026-02-10",
                  "date_answered": "2026-02-11",
                  "days_to_respond": 1
                },
                {
                  "rfi_id": "RFI-004",
                  "date_issued": "2026-02-25",
                  "date_answered": "2026-02-26",
                  "days_to_respond": 1
                }
              ]
            },
            "submittal_turnaround": {
              "average_days": 3,
              "unit": "business days",
              "submittals": 2,
              "data_source": "submittal-intelligence"
            },
            "communication_quality": {
              "rating": 9,
              "note": "Responses clear, complete, professional. Proactively flags scheduling conflicts."
            },
            "issue_resolution_speed": {
              "average_resolution_days": 2,
              "note": "Issues resolved promptly; escalates appropriately to Super"
            }
          },
          "scoring_notes": "RFI response avg 1.5 days (excellent). Submittal turnaround 3 days (excellent). Communication clear and proactive. Issues resolved quickly. Rating: 9/10"
        },
        "professionalism": {
          "dimension": "Professionalism",
          "weight": 0.15,
          "score": 9,
          "max_score": 10,
          "data_points": {
            "crew_conduct": {
              "superintendent_rating": 9,
              "note": "Crew respectful, cooperative, well-organized. Positive attitude throughout project.",
              "incident_complaints": 0,
              "data_source": "daily-report-format / super observations"
            },
            "site_cleanliness": {
              "superintendent_rating": 9,
              "note": "Site staging orderly. Debris cleaned daily. No violations.",
              "data_source": "daily site walks"
            },
            "trade_cooperation": {
              "superintendent_rating": 9,
              "note": "Excellent coordination with W Principles on sequencing. Early notification of schedule changes.",
              "coordination_incidents": 0
            },
            "contract_compliance": {
              "insurance_status": "current",
              "documentation_status": "complete and timely",
              "workers_comp_cert": "on file, verified",
              "general_liability": "on file, verified",
              "data_source": "contract compliance tracking"
            },
            "change_order_negotiations": {
              "change_orders_processed": 0,
              "fairness_rating": "N/A (no COs yet)",
              "note": "No change orders to date. Expectations: fair based on professionalism shown."
            }
          },
          "overall_professionalism_rating": 9,
          "super_comment": "Excellent contractor. Model for site professionalism, crew conduct, and cooperation. Highly recommend incentive recognition.",
          "scoring_notes": "Exemplary crew conduct, site cleanliness, cooperation, and compliance. Rating: 9/10"
        }
      },
      "composite_score": {
        "schedule_adherence_weighted": 2.0,
        "quality_weighted": 2.0,
        "safety_weighted": 2.0,
        "responsiveness_weighted": 1.35,
        "professionalism_weighted": 1.35,
        "total_composite": 8.7,
        "calculation": "(8 × 0.25) + (8 × 0.25) + (10 × 0.20) + (9 × 0.15) + (9 × 0.15) = 8.7"
      },
      "rating": {
        "rating_name": "GOOD",
        "rating_code": "GOOD",
        "score_band": "7.0-8.9",
        "status": "Standard Operations - Continue Monitoring",
        "color_code": "#4CAF50"
      },
      "performance_actions": {
        "recognition": [
          "Excellent safety culture - zero recordables",
          "Strong schedule reliability (87% PPC)",
          "High first-pass inspection rate (93%)"
        ],
        "improvement_opportunities": [],
        "formal_actions": "None; continue as planned"
      },
      "trend_data": {
        "historical_scores": [
          {
            "period": "WK1-2 (01/21-02/07)",
            "composite": 8.3,
            "rating": "GOOD"
          },
          {
            "period": "WK3-4 (02/10-02/28)",
            "composite": 8.7,
            "rating": "GOOD"
          }
        ],
        "trend_direction": "stable-to-improving",
        "trajectory": "Positive; trending toward 9.0 (Excellent) by project completion"
      },
      "next_evaluation_date": "2026-03-31",
      "comments_and_notes": "Strong start. Candidate for preferred bidder status and incentive bonus if performance sustained through remainder of project. Monitor for any safety incidents; maintain current high standards."
    }
  ]
}
```

---



## Automated Data Collection

The sub-performance skill aggregates data from multiple Foreman OS skills. Understanding which data is auto-pulled and which requires manual input ensures scorecards stay current and accurate.

### Auto-Pulled Data (Automated Daily/Weekly)

| Dimension | Data Point | Source Skill | Refresh Frequency |
|---|---|---|---|
| Schedule | PPC by Trade | last-planner | Weekly (EOW Friday) |
| Schedule | Crew headcount vs. promised | daily-report-format | Daily |
| Schedule | Milestone dates (actual vs. scheduled) | look-ahead-planner + daily-report-format | Weekly |
| Quality | First-Pass Inspection Rate | inspection-tracker / quality-management | Daily |
| Quality | Punch list items by trade | punch-list | Daily |
| Quality | Rework log (completed tasks) | quality-management | Daily |
| Safety | Recordable incidents | safety-management | Real-time (incident logged immediately) |
| Safety | Near-miss events | safety-management | Daily |
| Safety | Housekeeping scores | daily-report-format | Daily |
| Responsiveness | RFI response times | rfi-preparer | Daily (responses logged as received) |
| Responsiveness | Submittal turnaround times | submittal-intelligence | Daily |

### Manual Input (Weekly or Phase-End)

| Dimension | Data Point | Who Inputs | Frequency |
|---|---|---|---|
| Professionalism | Crew conduct rating | Superintendent | Weekly (Friday EOW) |
| Professionalism | Site cleanliness rating | Superintendent | Weekly (Friday EOW) |
| Professionalism | Trade cooperation assessment | Superintendent | Weekly (Friday EOW) |
| Professionalism | Contract compliance verification | PM / Safety Manager | Weekly |
| Responsiveness | Communication quality | Superintendent | As needed (monthly summary) |
| Quality | Warranty callback tracking | PM / Superintendent | Post-completion phase |

### Data Freshness

- **Schedule, Quality, Safety data**: Updated daily, scorecard refreshed weekly
- **Professionalism data**: Manually entered Friday EOW, scorecard refreshed weekly
- **Composite scorecard**: Recalculated weekly (every Friday EOW)
- **Trend data**: Historical scores stored and graphed (4-week, 12-week, lifetime views available)

---



## Performance Actions by Score Level

Each rating tier triggers specific actions designed to reinforce excellence, support improvement, or escalate risk.

### Excellent (9.0-10.0)

**Recommended Actions:**

1. **Public Recognition**
   - Feature in monthly project newsletter or social media
   - Superintendent commendation letter sent to sub company leadership
   - Announce safety/quality milestone publicly on site

2. **Preferred Bidder List**
   - Add to company's preferred vendor list for future projects
   - Priority bid invitation on next comparable project
   - Multi-project contract discounts (e.g., 2-3% on next 2-3 projects)

3. **Contract Incentives**
   - Bonus eligibility for on-time completion (if applicable): 0.5-1% of contract value
   - Safety incentive: $500-$1,000 bonus for zero recordables through project completion
   - Quality incentive: $250-$500 bonus if punch list <10 items and first-pass rate >95%

4. **Business Development**
   - Testimonial request for company marketing materials
   - Reference for other general contractors
   - Consideration for self-perform scope on future GC projects

**Communication Approach:**
- Positive, collaborative tone
- Highlight specific achievements (e.g., "Your 87% PPC and zero safety incidents have earned recognition")
- Discuss future partnership opportunities

---

### Good (7.0-8.9)

**Recommended Actions:**

1. **Standard Operations**
   - Continue current work pace and procedures
   - No formal corrective action needed
   - Annual performance review at project closeout

2. **Monitoring**
   - Track PPC weekly; flag if drops below 75% for discussion
   - Monitor quality metrics; address any upward trend in punch list items
   - Continue routine safety audits

3. **Optional Development**
   - Offer improvement suggestions in next performance review (e.g., "Responsiveness is solid at 8/10; consider even tighter RFI turnaround target of <2 days")
   - Invite to project improvement initiatives (e.g., Lean, prefabrication pilots)

**Communication Approach:**
- Positive, balanced tone
- "Your scorecard shows solid, reliable performance. We appreciate your professionalism and partnership."
- Frame improvement suggestions as optional growth opportunities, not mandates

---

### Needs Improvement (5.0-6.9)

**Recommended Actions:**

1. **Performance Meeting (Scheduled within 7 days of rating)**
   - Super, PM, and sub leadership meet in person
   - Review scorecard in detail; explain scoring methodology
   - Discuss specific blockers: "Your PPC is 71%, which is below project average of 78%. What's blocking your work?"
   - Ask for root cause analysis: Is it labor, material, design, or external constraints?

2. **Improvement Plan (30-day document)**
   - Sub submits written 30-day improvement plan addressing each weak dimension
   - Goals: "Increase PPC to 78% by 03/31", "Reduce punch list rate to <10/1000 SF", etc.
   - Identify resources needed: additional crew, training, procurement support
   - Assign accountability (sub superintendent or PM point-person)

3. **Increased Monitoring**
   - Weekly (not just EOW) touchbase with sub foreman
   - More frequent site inspections for quality (2x/week instead of weekly)
   - Safety audits increased (weekly instead of monthly)
   - RFI/submittal response times tracked daily

4. **Escalation Trigger**
   - If scorecard doesn't improve to 6.5+ by end of 30-day period, escalate to formal corrective action letter

**Communication Approach:**
- Professional, supportive tone
- "Your scorecard shows opportunity for improvement. Let's work together to identify and remove blockers."
- Treat as collaborative problem-solving, not punishment
- Provide resources (crew training, material expediting support) if within GC's control

---

### At Risk (<5.0)

**Recommended Actions:**

1. **Formal Corrective Action Letter**
   - Issued immediately upon <5.0 rating
   - Specifies performance deficiencies: "Responsiveness score 2/10 (RFI turnaround 12 days vs. project standard 3 days); Schedule score 4/10 (PPC 62% vs. project average 78%)"
   - Sets 10-day requirement to respond in writing with corrective action plan
   - States contractual consequences: "Failure to achieve improvement may result in work stoppage, contract termination, or back charges for delay damages"

2. **Immediate Intervention Meeting**
   - General Contractor leadership (PM, VP, or Principal) meets with sub company leadership
   - Format: firm, professional, solution-oriented
   - Clear timeline: "By [date], we need to see documented improvement in [specific areas]. We will re-score on [date]."
   - Establish daily communication cadence (super to sub foreman, daily huddle, no excuses)

3. **Contract Review**
   - PM reviews contract for termination clauses
   - Document all deficiencies as breach of contract
   - Evaluate financial and schedule impact of replacement sub
   - Assess liquidated damages claim or back-charge opportunity

4. **Replacement Sub Procurement**
   - Simultaneously source replacement sub (if termination is likely)
   - Establish acceleration clause: replacement sub can start immediately with overlap period
   - Plan transition to minimize schedule impact

5. **Daily Escalation Monitoring**
   - Daily scorecards submitted by sub foreman (checklist format)
   - Daily review by Super and PM
   - Weekly re-scoring of critical dimensions (Schedule, Responsiveness)
   - Open constraint log every day (any blockers?)

6. **Second Scorecard (10 days post-letter)**
   - Re-score all dimensions
   - If improvement to 5.0-6.0 range: Continue intensive monitoring; 2nd 30-day improvement plan
   - If no improvement or decline: Proceed to contract termination

**Communication Approach:**
- Firm, professional, serious tone
- Clear documentation and paper trail
- No ambiguity: "Here is what we need to see; here is when; here are the consequences."
- Remain respectful, but leave no doubt about seriousness of situation

**Example Corrective Action Letter:**

```
TO:         [Sub Company] Superintendent [Name]
DATE:       February 28, 2026
PROJECT:    Morehead One Senior Care (MOSC-825021)
SUBJECT:    FORMAL CORRECTIVE ACTION NOTICE — Performance Deficiency

Dear [Name]:

This letter is formal notice of performance deficiencies on the MOSC project, as documented in the Subcontractor Performance Scorecard dated 02/28/2026.

PERFORMANCE DEFICIENCIES:

Dimension              Score    Project Standard   Variance
─────────────────────────────────────────────────────────
Responsiveness        2/10     8/10               CRITICAL
Schedule Adherence    4/10     7.5/10             CRITICAL
Professionalism       4/10     7/10               CRITICAL
Quality               5/10     7.5/10             Significant
Safety                7/10     8.5/10             Marginal
─────────────────────────────────────────────────────────
COMPOSITE             4.5/10   7.2/10             AT RISK

SPECIFIC ISSUES:

1. Responsiveness: RFI response time averaging 12 days vs. project standard of 3 days.
   Door/hardware submittals overdue 24 days as of 02/28/2026. This delay is blocking
   downstream trades and threatening project schedule.

2. Schedule Adherence: PPC 62% vs. project average 78%. Crew size inconsistent with
   commitments; promised 5, showing 2-3. Two weekly commitments deferred mid-week without
   notice.

3. Professionalism: Multiple incidents of poor site coordination; crew leaving debris
   and blocking MEP staging area. Insurance documentation incomplete (liability cert
   missing 10 days past due date).

REQUIRED CORRECTIVE ACTIONS:

By March 10, 2026 (10 days), submit written Corrective Action Plan addressing:

1. RFI Turnaround: Commit to 3-day response by March 10. Submit daily RFI status
   report (due 4 PM daily) starting March 3.

2. Submittal Processing: Commit to all door/hardware submittals complete and approved
   by March 5. Identify expediting resources (additional staff, supplier escalation).

3. Schedule Adherence: Increase crew size to promised 5 personnel by March 3. Commit
   to weekly PPC target of 80%+ starting week of March 3.

4. Insurance/Compliance: Submit missing documentation by March 3. Commit to all
   paperwork on time and complete going forward.

5. Site Management: Assign dedicated crew member to daily site cleanup (6:00 AM
   before work start, 4:00 PM after work). Super will verify compliance daily.

CONSEQUENCES:

Failure to demonstrate sustained improvement by March 17, 2026 (2-week checkpoint)
may result in:
- Work stoppage until corrective action demonstrated
- Contract termination for cause per Section [X] of subcontract
- Back charges for delay damages and re-mobilization costs
- Removal from future bid lists

NEXT STEPS:

1. This letter received and acknowledged by you by COB February 29, 2026 (email signature).
2. Corrective Action Plan submitted by March 10, 2026.
3. Re-scoring meeting scheduled for March 17, 2026 at 8:00 AM on site.

We value your company and partnership. We are committed to supporting you in meeting
project standards. However, current performance is unacceptable and must improve immediately.

Please confirm receipt of this letter and your commitment to the corrective action plan.

Sincerely,

John Smith
Superintendent
W Principles General Contracting
john.smith@w-principles.com
(606) 555-1234
```

---



## Command: /sub-score

The sub-performance skill provides the following commands for generating and managing subcontractor scorecards.

### /sub-score [sub_name]
**Purpose**: View the current scorecard for a specific subcontractor.

**Usage:**
```
/sub-score Walker Construction
/sub-score "W Principles"
/sub-score Schiller
```

**Output:**
Displays full scorecard for the named sub, including:
- All five dimension scores (1-10, with evidence)
- Composite score and rating
- Trend data (prior periods)
- Specific strengths and improvement areas
- Recommended actions

**Example Output:**
```
════════════════════════════════════════════════════════════════
SUBCONTRACTOR PERFORMANCE SCORECARD
Walker Construction — Excavation / Sitework
Project: MOSC-825021 | Period: 01/21-02/28/2026
════════════════════════════════════════════════════════════════

DIMENSION SCORES:
  Schedule Adherence (25%):    8/10  ●●●●●●●● Green (PPC 87%)
  Quality (25%):               8/10  ●●●●●●●● Green (FPIR 93%)
  Safety (20%):               10/10  ●●●●●●●●●● Excellent (Zero recordables)
  Responsiveness (15%):        9/10  ●●●●●●●●● Excellent (RFI <2 days)
  Professionalism (15%):       9/10  ●●●●●●●●● Excellent (Super rating)

COMPOSITE SCORE: 8.7 / 10.0  ✓ GOOD

Rating:        GOOD (7.0-8.9)
Status:        Standard Operations - Continue Monitoring
Trend:         Stable to Improving (8.3 → 8.7 over 4 weeks)

STRENGTHS:
  ✓ Exceptional safety culture (zero incidents, 100% compliance)
  ✓ Reliable schedule performance (87% PPC, consistent crew)
  ✓ High quality (93% FPIR, minimal punch list)
  ✓ Excellent responsiveness (<2 day RFI turnaround)
  ✓ Exemplary professionalism (crew conduct, cooperation, site cleanliness)

AREAS FOR IMPROVEMENT:
  • Minor: 1 of 15 inspections failed (footing rebar spacing) — remediated

RECOMMENDED ACTIONS:
  → Maintain current performance level
  → Continue recognition for safety excellence
  → Consider for preferred bidder list on future projects
  → Candidate for completion incentive bonus if performance sustained

NEXT SCORECARD: 03/31/2026

────────────────────────────────────────────────────────────────
```

---

### /sub-score all
**Purpose**: Display scorecard summary table for all subcontractors on project.

**Usage:**
```
/sub-score all
/sub-score all --sort performance
/sub-score all --sort trade
```

**Output:**
Tabular view of all subs, sorted by rating or trade.

**Example Output:**
```
════════════════════════════════════════════════════════════════════════════════════
SUBCONTRACTOR PERFORMANCE SUMMARY — All Subs (MOSC-825021)
Assessment Period: 01/21-02/28/2026 | Updated: 02/28/2026
════════════════════════════════════════════════════════════════════════════════════

Sub Name                Trade                 Score  Rating      Status              Action
───────────────────────────────────────────────────────────────────────────────────
Walker Construction     Excavation/Sitework   8.7    GOOD        Continue Monitor    None
Alexander Construc.     PEMB Erection         8.9    GOOD        Continue Monitor    None
Davis & Plomin          HVAC/Mechanical       8.1    GOOD        Continue Monitor    None
EKD                     CFS Framing/Drywall   8.3    GOOD        Continue Monitor    None
W Principles (Self)     Concrete              7.05   GOOD        Continue Monitor    None
Hek Glass               Glazing               6.8    NEEDS IMPV   Performance Mtg    Monitor
Stidham Cabinets        Casework              6.2    NEEDS IMPV   Performance Mtg    Monitor
Schiller (Supplier)     Doors/Hardware        4.55   AT RISK      Corrective Action  Escalate
─────────────────────────────────────────────────────────────────────────────────────

PROJECT AVERAGE COMPOSITE SCORE: 7.32 / 10.0  (GOOD)

Green (9.0-10.0):        0 subs
Green (7.0-8.9):         5 subs  ✓✓✓✓✓
Yellow (5.0-6.9):        2 subs  ⚠⚠
Red (<5.0):              1 sub   ✗

ESCALATIONS REQUIRED:
  [1] Schiller — Formal corrective action letter sent 02/28. RFI turnaround 12 days
      (vs. 3-day standard). Submittals overdue 24 days. Expect response plan by 03/10.

NOTEWORTHY PERFORMANCE:
  ★ Walker Construction — Exemplary across all dimensions; zero safety incidents
  ★ Alexander Construction — Strong start; track record from prior projects excellent
  ★ Davis & Plomin — Solid all-around; candidate for expanded scope on future projects

═════════════════════════════════════════════════════════════════════════════════════
```

---

### /sub-score rate [sub_name]
**Purpose**: Manually enter or update the Professionalism dimension score (manual superintendent rating).

**Usage:**
```
/sub-score rate "Walker Construction"
/sub-score rate "Davis & Plomin" 8
```

**Process:**
1. Prompts superintendent to rate crew conduct, site cleanliness, cooperation, and compliance
2. Asks for specific observations and incidents
3. Calculates professionalism score based on input
4. Updates composite score
5. Stores entry with date and evaluator name

**Example Dialogue:**
```
PROFESSIONALISM RATING — Walker Construction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. CREW CONDUCT (1-10)
   How would you rate this sub's crew behavior?
   (Respectful, cooperative, professional? Conflicts? Attitude issues?)
   → Enter rating: 9
   → Notes: Crew is organized, courteous to other trades, always ready to cooperate

2. SITE CLEANLINESS (1-10)
   How do you rate the sub's site organization and housekeeping?
   (Clean, organized staging? Debris managed? OSHA compliance?)
   → Enter rating: 9
   → Notes: Site cleaned daily; no debris blocking walkways; staging area orderly

3. TRADE COOPERATION (1-10)
   How well does this sub coordinate with other trades?
   (Accommodates sequencing? Communicates? Blocks others? Courteous?)
   → Enter rating: 9
   → Notes: Excellent. Proactively coordinates with W Principles on adjacent work.

4. CONTRACT COMPLIANCE (1-10)
   Are insurance, documentation, and paperwork on time and complete?
   (Insurance current? Submittals timely? No missing docs?)
   → Enter rating: 9
   → Notes: All insurance on file and current. Paperwork always complete.

5. OVERALL COMMENT (optional)
   Any additional notes about this sub's professionalism?
   → "Excellent contractor. Model for site conduct and cooperation.
     Highly recommend for future work."

PROFESSIONALISM SCORE CALCULATED: 9/10
Evaluator: John Smith (Superintendent)
Date: 02/28/2026 at 4:15 PM

Updating composite scorecard...
Old Composite: 8.5 → New Composite: 8.7 ✓
```

---

### /sub-score trend [sub_name]
**Purpose**: Show historical performance trend over time for a specific subcontractor.

**Usage:**
```
/sub-score trend Walker Construction
/sub-score trend "W Principles" --weeks 12
/sub-score trend Schiller --chart
```

**Output:**
Line chart and table of scores over time, with trend analysis.

**Example Output:**
```
════════════════════════════════════════════════════════════════════════════
PERFORMANCE TREND — Walker Construction (12-Week History)
Project: MOSC-825021 | Current Score: 8.7 (GOOD)
════════════════════════════════════════════════════════════════════════════

COMPOSITE SCORE TREND:
10.0 |
 9.5 |
 9.0 |               ◆─────◆       ← Target: 8.5+
 8.5 |     ◆─────◆────      (Stable high performance)
 8.0 |
 7.5 |
 7.0 |
     └────┬────┬────┬────┬────┬────┬─
         Wk1  Wk2  Wk3  Wk4  Wk5  Wk6

DETAILED SCORECARD HISTORY:

Period              Composite  Rating      Schedule  Quality  Safety  Resp.  Prof.
─────────────────────────────────────────────────────────────────────────────────
Wk1-2 (01/21-02/07)   8.3    GOOD         8         8        10      9      8
Wk3-4 (02/10-02/28)   8.7    GOOD         8         8        10      9      9

TREND ANALYSIS:
  Direction: ↗ Improving (8.3 → 8.7 over 4 weeks; +0.4 point improvement)
  Consistency: Stable high performance across all dimensions
  Trajectory: Trending toward 9.0 (Excellent) if performance sustained
  Forecast: Likely to achieve EXCELLENT (9.0+) by project completion if current standards maintained

DIMENSION TRENDS:
  Schedule:      8 → 8  (Stable) — Consistent PPC >85%
  Quality:       8 → 8  (Stable) — Consistent FPIR >90%
  Safety:       10 →10  (Stable) — Perfect record maintained
  Responsiveness: 9 → 9  (Stable) — Excellent RFI/submittal turnaround
  Professionalism: 8 → 9  (↗ Improving) — Increased site cooperation observed

KEY OBSERVATIONS:
  ✓ Walker demonstrates consistent excellence with steady improvement trajectory
  ✓ Safety performance exemplary and sustained
  ✓ Schedule reliability above project average
  ✓ No significant weaknesses
  ✓ Recommended for preferred bidder status and incentive recognition

════════════════════════════════════════════════════════════════════════════════════
```

---

### /sub-score report
**Purpose**: Generate formal performance report (PDF/docx) suitable for project files, owner communication, or future bidding reference.

**Usage:**
```
/sub-score report Walker Construction
/sub-score report all
/sub-score report all --output PDF --include-trend
```

**Output:**
Professional report document (PDF or Word) including:
- Executive summary (composite score, rating, status)
- Detailed dimension analysis with evidence and data
- Strengths and improvement areas
- Trend analysis and charts
- Recommended actions
- Superintendent certification and signature block

**Report Sections:**
1. Cover page (project name, sub name, evaluation period, date)
2. Executive summary (1-page)
3. Scorecard detail (full breakdown of all 5 dimensions)
4. Data evidence (supporting charts, PPC data, inspection records)
5. Trend analysis (charts, forecast)
6. Recommendation and actions
7. Signature block (Superintendent, PM, Principal)

---



## Subcontractor Pre-Qualification Criteria

Pre-qualification is the process of evaluating a subcontractor's capability, financial strength, safety record, and experience BEFORE inviting them to bid on a project. Pre-qualification reduces risk by filtering out subs who lack the capacity, track record, or financial stability to perform the work reliably.

### Financial Capacity

Financial capacity determines whether a sub can fund the work (labor, materials, equipment) between progress payments and absorb the cash flow impact of retainage.

- **Annual Revenue**: Sub's annual revenue should be at least 2x the anticipated subcontract value. A sub with $500K annual revenue bidding on a $400K subcontract is overextended.
- **Net Worth**: Sub's net worth (assets minus liabilities) should exceed 50% of the anticipated subcontract value. Projects exceeding 50% of the sub's net worth represent a financial risk flag — the sub may not have sufficient reserves to fund the work if payment delays occur.
- **Risk Flag**: If the subcontract value exceeds 50% of the sub's net worth, the sub is at elevated financial risk. Require additional bonding or financial guarantees, or consider an alternate sub.
- **Financial Statement Availability**: Request audited or reviewed financial statements (last 2-3 years). Compiled statements are acceptable for smaller subs. Tax returns are a minimum if formal financials are unavailable.

### Bonding Capacity

Bonding capacity demonstrates that a surety company has evaluated the sub's financial strength and is willing to guarantee their performance.

- **Single Project Limit**: The maximum bond the surety will issue for a single project. The subcontract value must be within this limit.
- **Aggregate Limit**: The total bonding capacity across all active projects. If the sub is already bonded on multiple projects near their aggregate limit, they may not have capacity for your project.
- **Bonding Company Rating**: The surety company should be rated A- or better by AM Best. Sureties rated below A- may have insufficient financial strength to pay claims.
- **Bond Types**: Performance bond (guarantees completion) and payment bond (guarantees payment to sub-subs and suppliers). Both should be available if required by contract.

### Safety Record

Safety performance is a leading indicator of overall management quality. Subs with poor safety records often have poor quality and schedule performance as well.

- **EMR (Experience Modification Rate)**:
  - EMR is calculated by the sub's workers compensation insurance carrier based on actual claims history vs. expected claims for the sub's industry classification
  - EMR < 1.0 = better than industry average (GOOD)
  - EMR < 0.75 = significantly better than average (EXCELLENT)
  - EMR > 1.0 = worse than industry average (CAUTION)
  - EMR > 1.5 = significantly worse than average (DISQUALIFYING for many GCs)
  - Request 3-year EMR history to assess trend

- **TRIR (Total Recordable Incident Rate)**:
  - Number of OSHA-recordable injuries per 200,000 hours worked
  - Industry average varies by trade; residential construction ~4.0, commercial ~3.0
  - Target: Below industry average for the sub's trade classification
  - Request 3-year TRIR history

- **DART Rate (Days Away, Restricted, or Transferred)**:
  - Measures severity of injuries (not just frequency)
  - Lower DART = less severe injuries and faster return to work
  - Target: Below industry average for trade classification

### Experience

Experience on projects of similar type, size, and complexity is one of the strongest predictors of performance.

- **Similar Project Type**: Has the sub completed projects of the same type (healthcare, senior living, education, industrial, retail)? Healthcare and senior living have unique regulatory requirements (life safety, infection control, ADA compliance) that subs without experience may not understand.
- **Similar Project Size**: Has the sub completed projects of similar dollar value and physical scope? A sub experienced with $50K projects may struggle to manage a $500K scope.
- **Geographic Familiarity**: Is the sub familiar with local building codes, inspection requirements, labor markets, and weather conditions? Out-of-state subs may underestimate local conditions.
- **Years in Business**: Minimum 3 years in continuous business operation. New companies (<3 years) have higher failure rates and less established management systems.

### References

- **Minimum 3 Recent Projects**: Request references from 3 projects completed within the last 3 years that are similar in scope to the proposed work.
- **Contact Information**: Owner or GC project manager name, phone, and email for each reference.
- **Reference Check Questions**: Did the sub complete on time? Within budget? Quality of work? Safety record? Responsiveness? Would you hire them again?

### Workforce

- **Key Personnel Proposed**: Identify the project superintendent, foreman, and any specialized personnel (e.g., certified welders, licensed electricians) who will be assigned to the project. Evaluate their experience and tenure with the sub.
- **Skilled Labor Availability**: Does the sub have access to sufficient skilled labor to staff the project? Are they union or non-union? Do they have an apprenticeship program?
- **Self-Perform Capability**: What percentage of the work will the sub self-perform vs. sub-subcontract? Subs who self-perform more work generally have better quality control.

### Backlog

- **Current Committed Work**: What other projects is the sub currently working on? What is the total value of committed work?
- **Capacity to Take on New Project**: Does the sub have sufficient management bandwidth and labor capacity to take on the proposed project without overextending?
- **Schedule Availability**: Can the sub's proposed key personnel be available for the project's anticipated start date and duration?

---



## Pre-Qualification Questionnaire Template

The pre-qualification questionnaire is a structured form sent to prospective subcontractors to collect the information needed for pre-qualification evaluation.

### Company Information

```
SUBCONTRACTOR PRE-QUALIFICATION QUESTIONNAIRE

SECTION 1: COMPANY INFORMATION

Legal Company Name:         _________________________________________________
DBA (if different):         _________________________________________________
Street Address:             _________________________________________________
City / State / ZIP:         _________________________________________________
Phone:                      _________________________________________________
Primary Contact Name:       _________________________________________________
Primary Contact Email:      _________________________________________________
Primary Contact Phone:      _________________________________________________

Type of Entity:             [ ] Corporation  [ ] LLC  [ ] Partnership  [ ] Sole Proprietor
State of Incorporation:     _________________________________________________
Years in Business:          _________________________________________________
Federal Tax ID (EIN):       _________________________________________________

Contractor License Number:  _________________________________________________
License State:              _________________________________________________
License Expiration Date:    _________________________________________________
License Classifications:    _________________________________________________
```

### Financial Information

```
SECTION 2: FINANCIAL INFORMATION

Annual Revenue (last 3 years):
  Year 1 (most recent):    $_________________________________________________
  Year 2:                   $_________________________________________________
  Year 3:                   $_________________________________________________

Bonding Capacity:
  Bonding Company Name:     _________________________________________________
  AM Best Rating:           _________________________________________________
  Single Project Limit:     $_________________________________________________
  Aggregate Limit:          $_________________________________________________
  Agent Name / Phone:       _________________________________________________

Bank Reference:
  Bank Name:                _________________________________________________
  Branch / City:            _________________________________________________
  Account Manager / Phone:  _________________________________________________

Financial Statement Availability:
  [ ] Audited (last ___ years available)
  [ ] Reviewed (last ___ years available)
  [ ] Compiled (last ___ years available)
  [ ] Tax Returns (last ___ years available)
```

### Safety Information

```
SECTION 3: SAFETY INFORMATION

Experience Modification Rate (EMR) — last 3 years:
  Year 1 (most recent):    _________
  Year 2:                   _________
  Year 3:                   _________

Total Recordable Incident Rate (TRIR) — last 3 years:
  Year 1 (most recent):    _________
  Year 2:                   _________
  Year 3:                   _________

DART Rate — last 3 years:
  Year 1 (most recent):    _________
  Year 2:                   _________
  Year 3:                   _________

Safety Program:
  [ ] Written safety program in place
  [ ] OSHA 10-hour training required for all field employees
  [ ] OSHA 30-hour training for supervisors
  [ ] Substance abuse testing program
  [ ] Equipment inspection program

Safety Training Program Description:
  _________________________________________________________________________
  _________________________________________________________________________

Full-Time Safety Staff:
  [ ] Yes — Number of full-time safety personnel: ____
  [ ] No — Safety managed by: _______________________________________________

OSHA Citations (last 5 years):
  [ ] None
  [ ] Yes — Describe: ______________________________________________________
```

### Experience

```
SECTION 4: EXPERIENCE — 5 RECENT COMPARABLE PROJECTS

Project 1:
  Project Name:             _________________________________________________
  Owner:                    _________________________________________________
  General Contractor:       _________________________________________________
  Contract Value:           $_________________________________________________
  Scope of Work:            _________________________________________________
  Completion Date:          _________________________________________________
  Reference Contact:        _________________________ Phone: ________________

Project 2:
  Project Name:             _________________________________________________
  Owner:                    _________________________________________________
  General Contractor:       _________________________________________________
  Contract Value:           $_________________________________________________
  Scope of Work:            _________________________________________________
  Completion Date:          _________________________________________________
  Reference Contact:        _________________________ Phone: ________________

Project 3:
  Project Name:             _________________________________________________
  Owner:                    _________________________________________________
  General Contractor:       _________________________________________________
  Contract Value:           $_________________________________________________
  Scope of Work:            _________________________________________________
  Completion Date:          _________________________________________________
  Reference Contact:        _________________________ Phone: ________________

Project 4:
  Project Name:             _________________________________________________
  Owner:                    _________________________________________________
  General Contractor:       _________________________________________________
  Contract Value:           $_________________________________________________
  Scope of Work:            _________________________________________________
  Completion Date:          _________________________________________________
  Reference Contact:        _________________________ Phone: ________________

Project 5:
  Project Name:             _________________________________________________
  Owner:                    _________________________________________________
  General Contractor:       _________________________________________________
  Contract Value:           $_________________________________________________
  Scope of Work:            _________________________________________________
  Completion Date:          _________________________________________________
  Reference Contact:        _________________________ Phone: ________________
```

### Workforce

```
SECTION 5: WORKFORCE

Total Employees:            _________________________________________________
Total Field Employees:      _________________________________________________

Key Personnel Proposed for This Project:
  Project Manager:          _________________________ Years w/Company: ______
  Superintendent:           _________________________ Years w/Company: ______
  Foreman:                  _________________________ Years w/Company: ______
  Specialized:              _________________________ Certification: ________

Union / Non-Union:          [ ] Union (Local ______)  [ ] Non-Union  [ ] Both
Apprenticeship Program:     [ ] Yes  [ ] No
  If yes, describe: ________________________________________________________
```

### Insurance

```
SECTION 6: INSURANCE

General Liability:
  Carrier:                  _________________________________________________
  Per Occurrence Limit:     $_________________________________________________
  General Aggregate Limit:  $_________________________________________________
  Policy Expiration Date:   _________________________________________________

Automobile Liability:
  Carrier:                  _________________________________________________
  Combined Single Limit:    $_________________________________________________

Umbrella / Excess Liability:
  Carrier:                  _________________________________________________
  Limit:                    $_________________________________________________

Workers Compensation:
  Carrier:                  _________________________________________________
  Statutory Limits:         [ ] Yes  [ ] No
  Employer's Liability:     $_________________________________________________
```

### Equipment and Legal

```
SECTION 7: EQUIPMENT

Major Equipment Owned:      _________________________________________________
                            _________________________________________________
Major Equipment Available
for Rent/Lease:             _________________________________________________
                            _________________________________________________

SECTION 8: LEGAL

Pending Litigation:         [ ] None  [ ] Yes — Describe: __________________
                            _________________________________________________

Disputes in Past 5 Years:   [ ] None  [ ] Yes — Describe: __________________
                            _________________________________________________

Surety Claims Filed Against Company: [ ] None  [ ] Yes — Describe: _________
                            _________________________________________________

Contract Terminations
(last 10 years):            [ ] None  [ ] Yes — Describe: __________________
                            _________________________________________________

CERTIFICATION:

I certify that the information provided in this questionnaire is true, complete,
and accurate to the best of my knowledge. I authorize the requesting party to
verify any information provided and to contact references listed.

Signature: _________________________ Date: ______________
Print Name: ________________________ Title: ______________
```

---



## Pre-Qualification Scoring Matrix

The pre-qualification scoring matrix provides a standardized, weighted evaluation of each prospective subcontractor based on the questionnaire responses, reference checks, and financial analysis.

### Scoring Rubric

Each category is scored 1-5 based on the evaluation criteria:

| Score | Meaning |
|-------|---------|
| 5 | Excellent — Exceeds all requirements; best-in-class |
| 4 | Good — Meets all requirements with some strengths |
| 3 | Acceptable — Meets minimum requirements |
| 2 | Below Standard — Does not meet one or more requirements; risk present |
| 1 | Unacceptable — Significant deficiencies; high risk |

### Weighted Scoring Matrix

```
Category              Weight    Score (1-5)    Weighted Score
──────────────────────────────────────────────────────────────
Financial              20%      ___            ___
Safety                 25%      ___            ___
Experience             25%      ___            ___
Workforce              15%      ___            ___
References             10%      ___            ___
Insurance/Legal         5%      ___            ___
──────────────────────────────────────────────────────────────
TOTAL                 100%                     ___
```

### Category Scoring Guidelines

**Financial (20%)**:
- 5: Annual revenue > 3x subcontract value; bonding capacity exceeds requirements; audited financials available; strong bank reference
- 4: Revenue > 2x subcontract value; bonding adequate; reviewed financials; good bank reference
- 3: Revenue > 1.5x; bonding at limit; compiled financials; satisfactory bank reference
- 2: Revenue < 1.5x; bonding may be insufficient; limited financials; weak bank reference
- 1: Revenue < subcontract value; no bonding; no financials available

**Safety (25%)**:
- 5: EMR < 0.75; zero OSHA citations; comprehensive safety program; full-time safety staff; TRIR well below industry average
- 4: EMR 0.75-0.99; no citations; written safety program; TRIR at or below average
- 3: EMR 1.0-1.2; no serious citations; basic safety program; TRIR at industry average
- 2: EMR 1.2-1.5; minor citations; minimal safety program; TRIR above average
- 1: EMR > 1.5; serious citations; no formal safety program; TRIR significantly above average

**Experience (25%)**:
- 5: 5+ comparable projects completed successfully; extensive experience in project type and size; > 10 years in business; strong geographic familiarity
- 4: 3-4 comparable projects; good experience match; 5-10 years in business
- 3: 2-3 somewhat comparable projects; adequate experience; 3-5 years in business
- 2: 1 comparable project; limited experience in type or size; < 3 years in business
- 1: No comparable projects; no relevant experience; new company

**Workforce (15%)**:
- 5: Experienced key personnel with long tenure; strong labor force; self-perform > 80%; apprenticeship program
- 4: Good key personnel; adequate labor; self-perform 60-80%
- 3: Acceptable personnel; may need to supplement labor; self-perform 40-60%
- 2: Key personnel untested; labor concerns; heavy sub-subcontracting
- 1: No identified key personnel; labor shortage; entirely sub-subcontracted

**References (10%)**:
- 5: All references highly positive; would rehire enthusiastically; on-time, on-budget, high quality
- 4: References mostly positive; minor issues noted; would rehire
- 3: Mixed references; some concerns noted; would rehire with conditions
- 2: References raise concerns; schedule or quality issues; would not rehire without reservations
- 1: Negative references; significant problems reported; would not rehire

**Insurance/Legal (5%)**:
- 5: All insurance meets or exceeds requirements; no litigation; no surety claims; no terminations
- 4: Insurance meets requirements; minor past litigation resolved; no surety claims
- 3: Insurance adequate; some past disputes; no active litigation
- 2: Insurance gaps; active or recent litigation; surety claim filed
- 1: Insufficient insurance; multiple active lawsuits; surety claims; past terminations

### Qualification Thresholds

- **Minimum Qualifying Score**: 3.5 weighted average. Subs scoring below 3.5 are not invited to bid.
- **Preferred Qualification**: 4.0+ weighted average. Subs scoring 4.0 or above are placed on the preferred bidder list.

### Automatic Disqualifiers

The following conditions result in automatic disqualification regardless of overall score:

1. **EMR > 1.5**: Safety record too poor to allow on jobsite. Insurance costs will be excessive.
2. **Active Litigation Against the GC**: Conflict of interest prevents fair working relationship.
3. **No Bonding Capacity**: If the contract requires bonding and the sub cannot obtain bonds, they cannot perform.
4. **License Not Current**: Working without a current, valid contractor's license is illegal and creates liability exposure.
5. **Insufficient Insurance**: If the sub cannot meet the project's minimum insurance requirements, they cannot work on site.
6. **False Information on Questionnaire**: Any materially false statement on the pre-qualification questionnaire is grounds for immediate disqualification and permanent removal from bid lists.

### Pre-Qualification Scoring Example

```
SUBCONTRACTOR PRE-QUALIFICATION EVALUATION
Sub: ABC Mechanical, Inc. | Trade: HVAC | Evaluator: PM Smith | Date: 01/15/2026

Category              Weight    Score    Weighted    Notes
──────────────────────────────────────────────────────────────
Financial              20%      4        0.80        Revenue $1.2M vs $400K contract; bonding OK
Safety                 25%      5        1.25        EMR 0.68; zero citations; full safety program
Experience             25%      4        1.00        3 similar healthcare projects; 8 yrs in business
Workforce              15%      3        0.45        Good super; labor may need supplementing
References             10%      4        0.40        3 positive references; 1 minor schedule concern
Insurance/Legal         5%      5        0.25        All insurance exceeds minimums; no litigation
──────────────────────────────────────────────────────────────
TOTAL                 100%               4.15        QUALIFIED — Preferred Bidder

Automatic Disqualifiers: [ ] None found
Recommendation: INVITE TO BID — Place on preferred bidder list
```

**Cross-Reference**: See the estimating-intelligence skill for bid leveling procedures after pre-qualification. Pre-qualification determines WHO can bid; bid leveling evaluates the bids received from qualified subs to ensure apples-to-apples comparison.

---



## Integration Points

The sub-performance skill integrates with multiple Foreman OS skills to pull data and enable workflows.

### 1. last-planner Skill
**Data Flow**: PPC by Trade → Schedule Adherence Score
- Last planner calculates PPC (Percent Plan Complete) for each sub weekly
- sub-performance pulls PPC into Schedule Adherence dimension
- Subs with PPC >85% earn 9-10 score; subs <60% earn 2-4
- Pareto analysis of PPC variances (prerequisites, material, labor) feeds performance discussion

**Example**:
- Last Planner calculates: Walker Construction 87% PPC this week
- sub-performance updates: Walker schedule score = 8 (based on 87% PPC)
- If Walker maintains >85% PPC for 4 weeks, trend shows stability

---

### 2. inspection-tracker / quality-management Skill
**Data Flow**: First-Pass Inspection Rate (FPIR), Punch List Items → Quality Score
- Quality-management tracks inspections by trade (pass/fail)
- sub-performance pulls FPIR = (inspections passed) / (total inspections) × 100
- Punch list skill provides items per 1000 SF by responsible trade
- Rework log tracks completed rework by sub

**Example**:
- Quality-management: EKD (Drywall) — 14 of 15 inspections passed = 93% FPIR
- sub-performance: Quality score = 8 (based on 93% FPIR, 6 punch list items/1000 SF, 2% rework)

---

### 3. safety-management Skill
**Data Flow**: Incidents, Near-Misses, Housekeeping, PPE Compliance → Safety Score
- Safety-management logs recordable incidents, near-misses, safety audits
- sub-performance pulls incident count and severity
- Toolbox talk attendance, housekeeping scores, PPE observations feed safety rating
- Zero recordables + 100% compliance = 10; incidents drop score to 3-7

**Example**:
- Safety-management: Walker Construction — zero recordables, zero near-misses, 5 toolbox talks, 100% attendance, housekeeping avg 95%
- sub-performance: Safety score = 10 (perfect record)

---

### 4. rfi-preparer Skill
**Data Flow**: RFI Response Times → Responsiveness Score
- RFI preparer logs RFI issued date and response received date
- sub-performance calculates average response time per trade
- <3 day avg = 10; 3-5 days = 8; 5-7 = 6; 7-14 = 4; >14 = 2

**Example**:
- RFI Log: Walker issued 4 RFIs; responded in 1, 1, 2, 2 days (avg 1.5 days)
- sub-performance: Responsiveness score = 10 (RFI portion) due to excellent turnaround

---

### 5. submittal-intelligence Skill
**Data Flow**: Submittal Turnaround Times → Responsiveness Score
- Submittal-intelligence tracks date received, date reviewed, date approved, date returned
- sub-performance calculates turnaround = (date approved - date received)
- <5 days = 10; 5-7 = 8; 7-10 = 6; 10-14 = 4; >14 = 2

**Example**:
- Submittal Log: Schiller doors/hardware submitted 01/20, approved 02/13 = 24 days
- sub-performance: Responsiveness score = 2 (critical delay)

---

### 6. daily-report-format Skill
**Data Flow**: Crew Counts, Work Completion, Observations → Schedule, Professionalism, Safety
- Daily reports document crew headcount (promised vs. actual)
- Work completion status (task complete, in progress, blocked)
- Observations (crew conduct, site cleanliness, blockages)
- sub-performance aggregates across 4+ weeks to assess trends

**Example**:
- Daily reports (4 weeks): W Principles promised 4-person crew; actual 2-3. Crew showed 75% consistency.
- sub-performance: Schedule score adjusted downward for crew inconsistency (from 8 to 6)

---

### 7. project-dashboard Skill
**Integration**: Sub Scorecard Section with Radar Charts
- Project dashboard displays sub performance summary (all subs, composite scores)
- Radar chart visualization of 5 dimensions for each sub (visual at-a-glance assessment)
- Trend indicators (↑↓→ showing direction)
- Color-coded status (green/yellow/red)

**Example Dashboard Widget**:
```
┌─────────────────────────────────────────────┐
│ SUBCONTRACTOR PERFORMANCE SUMMARY           │
├─────────────────────────────────────────────┤
│ Walker Construction:     8.7 ✓ GOOD         │
│ Alexander Construction:  8.9 ✓ GOOD         │
│ Davis & Plomin:          8.1 ✓ GOOD         │
│ EKD:                     8.3 ✓ GOOD         │
│ W Principles:            7.0 ✓ GOOD         │
│ Hek Glass:               6.8 ⚠ NEEDS IMPV   │
│ Stidham Cabinets:        6.2 ⚠ NEEDS IMPV   │
│ Schiller:                4.55 ✗ AT RISK     │
└─────────────────────────────────────────────┘
```

---

### 8. pay-application Skill
**Integration**: Performance Data Supports Back-Charges
- Pay-app skill processes sub invoices and GC back-charges
- sub-performance data links quality failures, schedule delays, safety incidents to back-charge documentation
- Example: Sub quality score 4/10 with punch list 50/1000 SF → GC back-charges sub for rework labor

**Example**:
- Stidham Cabinets invoice: $25,000 for cabinet installation
- sub-performance quality: 4/10 (FPIR 82%, punch list 35/1000 SF = rework needed)
- GC applies back-charge: $1,500 (6% of contract value) for rework labor and inspection
- Pay-app shows: Invoice $25,000 - Back-charge $1,500 = Final pay $23,500

---



## Radar Chart Visualization

Each subcontractor scorecard displays a 5-axis radar chart showing performance across all dimensions.

### Radar Chart Interpretation

```
                          SCHEDULE (25%)
                               10
                              /  \
                            9      9
                          /          \
                    PROF(15%) 8      8 QUALITY(25%)
                       /      |      \
                     /        |        \
                    9         |         8
                  /           |           \
               /              |              \
            RESPONS(15%) 8----+----9 SAFETY(20%)
                 \             |             /
                   \           |           /
                    \          |          /
                      \        |        /
                        \      |      /
                          \    |    /
                            \ | /
                             \|/


Legend:
  ● Walker (Composite 8.7) — Balanced excellence across all dimensions
  ○ W Principles (Composite 7.0) — Solid schedule/quality, room for improvement in responsiveness
```

### Radar Chart Data

The 5 axes (100% = 10/10):

| Axis | Walker | W Principles | Schiller |
|---|---|---|---|
| Schedule (25%) | 8/10 (100%) | 6/10 (75%) | 5/10 (63%) |
| Quality (25%) | 8/10 (100%) | 6/10 (75%) | 5/10 (63%) |
| Safety (20%) | 10/10 (100%) | 9/10 (90%) | 5/10 (63%) |
| Responsiveness (15%) | 9/10 (90%) | 8/10 (80%) | 2/10 (20%) |
| Professionalism (15%) | 9/10 (90%) | 7/10 (70%) | 5/10 (63%) |

**Visualization**: Radar chart shows Walker as a "full pentagon" (balanced excellence), W Principles as slightly dented on responsiveness, Schiller severely dented on responsiveness (narrow spike).

---



## Back-Charge Documentation

Performance data provides objective foundation for back-charge claims.

### Back-Charge Categories

**1. Quality Back-Charges**
- Rework labor: Sub's punch list items require GC labor to remediate
- Inspection time: Excessive inspection cycles due to high failure rate
- Warranty callbacks: Post-completion rework for sub's deficiencies
- Documentation: "Stidham Cabinets punch list: 12 items; GC labor to correct: 16 hrs @ $75/hr = $1,200 back-charge"

**2. Schedule Back-Charges**
- Delay damages: Sub's low PPC causes downstream delays; GC incurs extended supervision, equipment rental
- Acceleration cost: GC must pay for expedited labor/material to recover schedule lost to sub
- Documentation: "W Principles concrete schedule delays (50% PPC) caused 3-week delay to PEMB erection; extended super cost 3 weeks × $150/day = $3,150 back-charge"

**3. Safety Back-Charges**
- Safety remediation: Sub's inadequate safety practices require GC to hire safety officer or remediate hazards
- Incident costs: Sub caused incident; GC absorbs medical, workers comp, reporting costs
- Documentation: "Walker excavation near-miss (utility strike) caused 1-day shutdown; GC paid for utility locating, investigation, re-training: $800 back-charge"

**4. Responsiveness Back-Charges**
- Expediting costs: Sub's slow RFI response causes design delays; GC pays for expediting or re-work
- Coordination labor: GC super spends excessive time chasing sub for approvals/submissions
- Documentation: "Schiller submittals overdue 24 days delayed door installation schedule; GC incurred 20 hrs coordination labor: $1,500 back-charge"

### Back-Charge Documentation Workflow

1. **Scorecard Triggers Back-Charge Review**: When sub scores <6.0 on any dimension, PM reviews back-charge opportunities
2. **Document Supporting Evidence**: Daily reports, inspection records, RFI logs, timesheets
3. **Calculate Damages**: Labor hours × rate, equipment rental extended, material acceleration costs
4. **Prepare Back-Charge Letter**: Formal notice citing specific deficiencies and calculated damage
5. **Link to Pay-Application**: Back-charge deducted from next sub invoice
6. **Dispute Resolution**: Sub can dispute back-charge with supporting evidence; escalate if contested

### Example Back-Charge Memo

```
BACK-CHARGE NOTICE
═════════════════════════════════════════════════════════════════

TO:         Schiller Doors & Hardware
FROM:       John Smith, Superintendent, W Principles GC
DATE:       February 28, 2026
PROJECT:    Morehead One Senior Care (MOSC-825021)
SUBJECT:    Back-Charge for Submittal Processing Delays

─────────────────────────────────────────────────────────────────

SCOPE OF BACK-CHARGE:

Schiller's performance scorecard dated 02/28/2026 reflects critical delays
in submittal processing:

  Responsiveness Score: 2/10
  RFI Response Time: 12 days (project standard: 3 days)
  Submittal Turnaround: 24 days overdue (standard: 5 days)
  Impact: Door/hardware installation schedule blocked; downstream trades delayed

COST BREAKDOWN:

1. Superintendent Expediting Labor
   Dates: 02/10 - 02/28 (4 weeks)
   Labor: Escalation calls, follow-up emails, coordination meetings
   Time: 20 hours @ $75/hour (Superintendent T&M rate)
   Cost: $1,500

2. Schedule Delay Impact
   Delay Period: 02/10 - 02/28 (18 days overdue)
   GC Extended Supervision: 18 days × $150/day (Super onsite cost)
   Cost: $2,700

TOTAL BACK-CHARGE: $4,200

JUSTIFICATION:

Schiller's submittals are contractually required within 5 days of receipt
for GC review and approval. 24-day delay (vs. standard 5 days) is 4.8x
baseline and represents material breach of contract duty.

GC's back-charge reflects actual labor expended to expedite and
mitigate schedule impact. This is consistent with contract § 7.2
(Contractor's Right to Recover Costs Incurred Due to Sub's Deficiency).

RESOLUTION:

GC proposes:
Option 1: Schiller accepts back-charge; deducted from next progress payment
Option 2: Schiller disputes back-charge in writing by 03/07/2026; parties
          meet to review supporting documentation and negotiate settlement

Contact John Smith (john.smith@w-principles.com / 606-555-1234) to discuss.

Sincerely,

John Smith
Superintendent, W Principles GC
```

---



## End-of-Project Evaluation

At project closeout, conduct final comprehensive scorecard for each sub to build institutional memory and inform future bidding.

### Final Scorecard Process (Post-Substantial Completion)

1. **Compile Full-Project Data** (Weeks 1 - Substantial Completion)
   - All PPC data by trade across entire project
   - Complete inspection history (FPIR)
   - Final punch list (closeout items)
   - Warranty callback data (if available; extend for 30-day post-completion)
   - Safety record (full project, zero-incident or documented incidents)
   - RFI/submittal complete history
   - Contract compliance audit

2. **Conduct Final Performance Meeting** (1 week before final payment)
   - Super, PM, and sub leadership meet for 1-hour review
   - Present final scorecard (all five dimensions)
   - Discuss strengths, challenges, and lessons learned
   - Gather sub's feedback: "What did we do well? What could we improve?"
   - Document meeting minutes

3. **Calculate Final Composite Score**
   - Use same weighted formula: (Schedule 0.25) + (Quality 0.25) + (Safety 0.20) + (Responsiveness 0.15) + (Professionalism 0.15)
   - Final rating: Excellent (9+), Good (7-8.9), Needs Improvement (5-6.9), At Risk (<5)

4. **Store Final Scorecard in Project Archive**
   - File location: Project files, "03 - Subcontractors / [Sub Name] / FINAL SCORECARD"
   - Include: All data, charts, photos, correspondence
   - Timestamp: Completion date, evaluators' signatures

5. **Add to Company Preferred Vendor Database**
   - Extract final scorecard to centralized vendor database
   - Include project name, dates, final score, and superintendent notes
   - Track across multiple projects for trend analysis (does sub improve over time?)

### Final Scorecard Example: Project Closeout

```
═══════════════════════════════════════════════════════════════════════════════
FINAL SUBCONTRACTOR PERFORMANCE SCORECARD
Walker Construction — Excavation / Sitework
Project: Morehead One Senior Care (MOSC-825021) | Duration: 01/21 - 08/12/2026
═══════════════════════════════════════════════════════════════════════════════

EXECUTIVE SUMMARY:

Walker Construction delivered excellent performance across all project phases,
consistently exceeding industry standards for schedule reliability, quality,
safety, and professionalism. Recommended for Preferred Bidder list and future
multi-project partnerships.

═══════════════════════════════════════════════════════════════════════════════

FINAL DIMENSION SCORES (Full 30-Week Project):

  Schedule Adherence (25%):     8.8/10  ✓ Green
    → PPC Average (30 weeks): 86.2% (project avg: 76%)
    → Crew Consistency: 100% (promised vs. actual)
    → Mobilization: 1 day early; Demobilization: Efficient, no delays
    → Assessment: Excellent reliability; sub completed commitments more reliably
                  than 90% of project average

  Quality (25%):                8.6/10  ✓ Green
    → First-Pass Inspection Rate: 91% (project avg: 85%)
    → Punch List Items: 8 per 1000 SF (project avg: 15)
    → Rework Frequency: 2% (project avg: 4%)
    → Warranty Callbacks (Post-Completion): 0
    → Assessment: High-quality work; minimal rework; strong inspection performance

  Safety (20%):                10.0/10 ✓✓ Excellent
    → Recordable Incidents: 0
    → Near-Miss Events: 0
    → Toolbox Talk Attendance: 100% (all 26 sessions, all crew)
    → Housekeeping Score: 96% average (site walk scores)
    → PPE Compliance: 100% (no lapses observed in 100+ site inspections)
    → OSHA Citations: 0
    → Assessment: Perfect safety record; exemplary safety culture; model contractor

  Responsiveness (15%):         8.9/10  ✓ Green
    → RFI Response Time: Average 2.1 days (project standard: 3 days)
    → Submittal Turnaround: Average 4.2 days (project standard: 5 days)
    → Communication Quality: 9/10 (clear, professional, proactive)
    → Issue Resolution Speed: 1.8 days average
    → Assessment: Consistently exceeds project responsiveness standards;
                  proactive communication throughout

  Professionalism (15%):        9.1/10  ✓ Green
    → Crew Conduct: 9/10 (respectful, cooperative, professional)
    → Site Cleanliness: 9/10 (organized, debris managed daily)
    → Trade Cooperation: 10/10 (excellent coordination, zero conflicts)
    → Contract Compliance: 10/10 (insurance timely, paperwork complete)
    → Change Order Fairness: 10/10 (reasonable negotiations, no disputes)
    → Owner/Architect Feedback: 9/10 (positive comments throughout project)
    → Assessment: Model contractor; exemplary professionalism; high marks from
                  all project stakeholders

───────────────────────────────────────────────────────────────────────────────

COMPOSITE SCORE CALCULATION:

  (8.8 × 0.25) + (8.6 × 0.25) + (10.0 × 0.20) + (8.9 × 0.15) + (9.1 × 0.15)
  = 2.20 + 2.15 + 2.00 + 1.335 + 1.365
  = 9.05 / 10.0

FINAL RATING:  EXCELLENT (9.05/10.0)  ✓✓✓

═══════════════════════════════════════════════════════════════════════════════

STRENGTHS (Notable Achievements):

  ★ Perfect Safety Record
    • Zero recordable incidents, zero near-misses across entire 30-week project
    • 100% toolbox talk attendance; crew trained and engaged in safety
    • Consistent housekeeping; exemplary hazard awareness
    • Model for other subs; shared best practices

  ★ Schedule Reliability
    • 86.2% PPC far exceeds project average (76%)
    • Crew size consistent with commitments; no staffing issues
    • Early mobilization; efficient demobilization
    • Enabled downstream trades to plan and execute confidently

  ★ Quality Craftsmanship
    • 91% FPIR (first-pass inspection rate) indicates rigorous quality control
    • Punch list items minimal (8/1000 SF vs. project avg 15)
    • Rework frequency just 2% (half project average)
    • Owner satisfaction high; no post-completion callbacks

  ★ Professional Conduct
    • Crew behavior exemplary; zero conflicts with other trades
    • Proactive coordination; helped solve sequencing issues
    • Insurance and documentation always on time and complete
    • Superintendent and owner praised "Walker's professionalism and partnership"

═══════════════════════════════════════════════════════════════════════════════

AREAS OF EXCELLENCE (Outstanding Relative to Typical Subs):

  1. Safety Culture — Zero recordables is exceptional (industry avg: 1-2 per major project)
  2. Schedule Reliability — 86% PPC is top-quartile (typical: 70-80%)
  3. Quality Control — FPIR 91% exceeds most trades (typical: 80-85%)
  4. Responsiveness — Average 2.1-day RFI response beats standard by 30%
  5. Professional Conduct — No conflicts, zero disputes, model behavior

═══════════════════════════════════════════════════════════════════════════════

RECOMMENDATIONS FOR FUTURE PROJECTS:

  ✓✓ PREFERRED BIDDER STATUS
    Add Walker Construction to company's preferred vendor list.
    Priority bid invitation on comparable excavation/sitework scope.

  ✓✓ PERFORMANCE INCENTIVE / RECOGNITION
    Recommend annual performance bonus or credit (e.g., 2% discount on next
    2-3 projects) for exceptional achievement.

  ✓✓ EXPANDED SCOPE OPPORTUNITY
    Consider offering expanded scope on future projects; Walker has demonstrated
    ability to manage larger, more complex work.

  ✓✓ TEAM SHARING / BEST PRACTICES
    Walker's safety and quality practices should be documented and shared as
    models for other subs on future projects.

═══════════════════════════════════════════════════════════════════════════════

FINAL CERTIFICATION:

This scorecard reflects objective assessment of Walker Construction's performance
on MOSC project 01/21 - 08/12/2026. Assessment based on documented data from
daily reports, inspections, safety records, RFI/submittal logs, and superintendent
observations.

Evaluated By:     John Smith, Superintendent
Reviewed By:      Mike Johnson, Project Manager
Approved By:      [Principal signature]
Date:             August 15, 2026

═══════════════════════════════════════════════════════════════════════════════
```

---



## Best Practices for Fair, Objective Subcontractor Evaluation

To ensure scorecards remain objective, transparent, and effective:

### 1. Use Data, Not Opinions
- **Measure facts**: PPC (from last-planner), FPIR (from inspections), RFI response times (from RFI log)
- **Avoid gut feelings**: Don't rate "overall quality" without FPIR or punch list data
- **Document sources**: Every score point to a data source (daily report, inspection record, RFI log)
- **Avoid personality bias**: Rate the sub's work performance, not whether you like their foreman

### 2. Weight Dimensions Fairly
- Five dimensions (25%, 25%, 20%, 15%, 15%) reflect industry best practice
- Schedule and Quality equally weighted (50% total) because both critical to project success
- Safety heavily weighted (20%) because safety is non-negotiable
- Responsiveness and Professionalism (30% combined) support collaboration
- Adjust weights if project-specific priorities differ (e.g., heavy on Quality for precision manufacturing assembly)

### 3. Calibrate Scoring Thresholds
- Define specific, measurable thresholds for each score level (1-10)
- Example: "PPC 90%+ = 10; 80-89% = 8; 70-79% = 6" — not ambiguous
- Publish thresholds to all subs at project start so expectations are clear
- Calibrate against industry norms and project baselines

### 4. Separate Performance from Blame
- **Variance analysis**: Assign variance categories (Prerequisites, Material, Labor, etc.) to understand root cause
- **Not always the sub's fault**: If a sub's PPC is low due to supplier delays (Material variance), don't penalize Schedule score unfairly
- **Example**: W Principles concrete PPC = 62%. Root cause: 60% of incomplete work = "Prerequisites" (prior phases not complete). Adjustment: Don't lower Schedule score for externally-caused delays; instead note "W Principles responding appropriately to dependencies."

### 5. Transparency and Communication
- **Publish methodology**: Share scoring rubric with all subs at project start
- **Share scorecards regularly**: Monthly or phase-end scorecard shared with sub leadership (not just Internal GC review)
- **Explain scores**: When sharing scorecard, walk through the evidence: "Your PPC is 71% (6/10 score) because you completed 7 of 10 commitments. These two were deferred due to material delay (not your fault); these three due to labor/crew size."
- **Open dialogue**: Invite sub input: "Do you disagree with this assessment? Here's the data we're using. What are we missing?"

### 6. Consistency Across Subs and Projects
- **Use same rubric for all subs**: Every trade (excavation, concrete, framing, MEP) scored using same 5 dimensions and thresholds
- **Compare within trade**: A mechanical sub's PPC is compared to other mechanical subs, not to excavation subs (different work types have different reliability profiles)
- **Track across projects**: If a sub scores 8.2 on Project A and 6.1 on Project B, investigate: Did sub's management change? Was Project B more complex? Does sub have a learning curve on new scopes?

### 7. Avoid Retroactive Judgment
- **Capture data in real time**: Don't wait until project end to assess performance; document weekly
- **Weekly snapshots**: Calculate dimensional scores weekly so subs see trends and can course-correct
- **No surprises**: Final scorecard should confirm the running assessment, not introduce new information
- **Example**: At week 4, tell sub "Your schedule score is 6/10; PPC is 68%. Here's your trend. Let's discuss how to improve." Don't wait until final scorecard to say "You're at 5/10, below our standard."

### 8. Provide Feedback and Development Opportunity
- **Coaching mindset**: Scorecards are tools for improvement, not just judgment
- **Performance meetings**: For subs scoring 5-6.9 (Needs Improvement), offer support: "Your PPC is low. What constraints are blocking your work? Can we help expedite material? Add crew?" Don't just say "Do better."
- **Recognize improvement**: Track trends; celebrate subs who score 6.0 in week 2 but 7.5 by week 8
- **Example**: "Davis & Plomin, your safety score went from 7/10 to 9/10 after implementing our suggested toolbox talk format. Excellent response to feedback."

### 9. Document and Archive
- **Centralized database**: Store all scorecards (per-project, per-sub) in accessible location
- **Historical tracking**: Track sub performance over 3-5 projects; look for patterns (does sub improve over time? Maintain excellence? Decline?)
- **Preferred vendor management**: Subs with 3+ projects at 8.0+ composite score → Preferred Bidder list; subs with 2+ projects below 5.0 → Do Not Bid list
- **Institutional learning**: Use database to inform future bidding: "Walker averaged 8.6 across 3 projects; Schiller averaged 5.1 across 2 projects."

### 10. Balance Accountability with Partnership
- **Accountability**: Scorecards hold subs to clear standards; low scores trigger corrective action
- **Partnership**: Approach as collaborative problem-solving, not adversarial
- **Long-term relationships**: Good subs become repeat partners; you benefit from continuity, institutional knowledge, team chemistry
- **Example tone**: Not: "Your performance is unacceptable; we're replacing you." Better: "Your scorecard shows challenges; let's solve these together so you can succeed on future work."

---



## Summary

The sub-performance scorecard skill transforms subcontractor evaluation from informal, opinion-based judgment to objective, data-driven assessment. By measuring five critical dimensions (Schedule, Quality, Safety, Responsiveness, Professionalism) against transparent criteria, the skill enables:

- **Informed bidding decisions** backed by track record data
- **Fair performance conversations** grounded in evidence, not personalities
- **Early intervention** for at-risk subs before problems cascade
- **Recognition and incentives** for excellent subs
- **Back-charge documentation** supported by objective performance data
- **Institutional memory** across projects and years
- **Continuous improvement** through feedback and coaching

Implemented consistently, sub-performance scorecards elevate project quality, schedule reliability, safety, and team professionalism while building long-term vendor relationships with proven, capable partners.


