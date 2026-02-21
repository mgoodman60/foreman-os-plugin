# Schedule - Deep Extraction Guide

Extract comprehensive sequencing logic, float analysis, and activity details from CPM schedules (Primavera P6, MS Project, Asta Powerproject).

---

## Extraction Priority

| Priority | Data | Purpose |
|----------|------|---------|
| **CRITICAL** | Milestones with dates | Contract compliance, progress tracking |
| **CRITICAL** | Critical path activities (float = 0) | Focus field resources |
| **HIGH** | Activity durations and dates | Daily progress measurement |
| **HIGH** | Predecessor/successor logic | Understand delay impacts |
| **MEDIUM** | Float values | Identify schedule flexibility |
| **MEDIUM** | Constraints | Understand hard dates |
| **LOW** | Resource loading | Site congestion prediction |

---

## Activity-Level Data

**For EVERY activity**, extract:

- **Activity ID**: Unique code (e.g., "A1010", "SITE-020")
- **Activity name**: Description (e.g., "Excavate footings", "Erect PEMB columns")
- **Planned duration**: Days
- **Start date**: Early start (or actual if started)
- **Finish date**: Early finish (or actual if complete)
- **Total float**: Schedule flexibility in days (0 = critical)
- **Percent complete**: 0-100%

**Example extraction**:
```
A1020 | Form and pour footings | 5 days | Start: 02/16/26 | Finish: 02/20/26 | Float: 0 | 0%
A1030 | Cure footings | 3 days | Start: 02/21/26 | Finish: 02/23/26 | Float: 0 | 0%
A2010 | Prep/pour SOG | 2 days | Start: 03/09/26 | Finish: 03/10/26 | Float: 2 | 0%
```

---

## Predecessor/Successor Relationships

**CRITICAL for understanding sequencing**:

For each activity, extract:
- **Predecessors**: Which activities must finish (or start) before this starts
- **Successors**: Which activities depend on this one
- **Relationship type**:
  - **FS** (Finish-to-Start): Predecessor finishes, then successor starts [most common]
  - **SS** (Start-to-Start): Both start together
  - **FF** (Finish-to-Finish): Both finish together
  - **SF** (Start-to-Finish): Rare
- **Lag time**: Days to wait (e.g., "+7 days for concrete cure")
- **Lead time**: Overlap (e.g., "-2 days, start before predecessor finishes")

**Example**:
```
Activity: "Pour SOG"
  Predecessors:
    - "Place rebar in SOG" (FS)
    - "MEP underslab rough-in" (FS)
  Successors:
    - "SOG cure time" (FS)
    - "Survey slab elevation" (FS+1)

Activity: "SOG cure time" (7 days)
  Predecessors:
    - "Pour SOG" (FS)
  Successors:
    - "PEMB erection" (FS) [Can't start erecting until cured]
```

This logic explains WHY delays cascade.

---

## Critical Path

**IDENTIFY ALL ACTIVITIES WITH FLOAT = 0**:

These are the critical path - no schedule flexibility. Any delay to these delays project completion.

**Extract**:
- Full sequence from mobilization to final completion
- Activity IDs and names
- Durations
- Start/finish dates

**Example**:
```
Critical Path Activities (Float = 0):
1. Mobilization (02/16/26 - 02/16/26, 1 day)
2. Site utilities installation (02/17/26 - 02/23/26, 5 days)
3. Excavate footings (02/24/26 - 02/27/26, 3 days)
4. Form/pour footings (02/28/26 - 03/04/26, 4 days)
5. Cure footings (03/05/26 - 03/07/26, 3 days)
6. Prep/pour SOG (03/09/26 - 03/10/26, 2 days)
7. SOG cure (03/11/26 - 03/17/26, 7 days)
8. PEMB erection (03/18/26 - 03/29/26, 10 days)
... continues to Final Completion
```

---

## Near-Critical Activities

**Activities with float < 5 days** (adjustable threshold):

These could become critical if they slip. Flag for close monitoring.

**Example**:
```
Near-Critical (Float 1-4 days):
- Rough grading (Float: 2 days)
- MEP underslab (Float: 3 days)
- Drywall (Float: 4 days)
```

---

## Constraints

**Extract constraint types and dates**:

- **ASAP** (As Soon As Possible): Default, no constraint
- **SNET** (Start No Earlier Than): Can't start before ___ date
- **SNLT** (Start No Later Than): Must start by ___ date
- **FNET** (Finish No Earlier Than): Can't finish before ___ date
- **FNLT** (Finish No Later Than): Must finish by ___ date
- **MSO** (Must Start On): Hard constraint, must start on ___ date
- **MFO** (Must Finish On): Hard constraint, must finish on ___ date (common for milestones)

**Example**:
```
Activity: "Substantial Completion"
  Constraint: MFO (Must Finish On)
  Date: 07/29/26
  Note: Contractual milestone, cannot slip
```

---

## Milestones

**EXTRACT ALL MILESTONES** (zero-duration activities):

Always flag these key milestone types:
- **NTP / Start date**
- **Permit obtained**
- **Foundation complete**
- **Structure topping out** / **PEMB erected**
- **Building dried in / weathertight**
- **MEP rough-in complete**
- **Framing inspection**
- **Insulation inspection**
- **Substantial completion**
- **Final completion**
- **Occupancy / move-in**

**Example**:
```
Milestones:
- NTP: 01/21/26
- PEMB on site: 03/05/26
- PEMB erected / dried in: 04/20/26
- MEP rough inspection: 05/18/26
- Substantial completion: 07/29/26 (MFO constraint)
- Final completion: 08/12/26 (MFO constraint)
```

---

## Weather-Sensitive Activities

**Identify activities affected by weather**:

By calendar assignment or description keywords:
- Earthwork, grading, excavation
- Concrete placement (footings, walls, SOG, paving)
- Masonry
- Roofing, waterproofing
- Exterior painting
- Paving, striping
- Landscaping, seeding

**Note calendar**:
- 5-day: No weekends
- 6-day: Saturdays included
- Weather days: Reduced productivity on rain/snow days

**Example**:
```
Weather-Sensitive Activities:
- Rough grading (5-day calendar, 10 days duration)
- Pour SOG (5-day calendar, 2 days duration)
- PEMB erection (6-day calendar, 10 days duration, weather may delay)
- Roofing (5-day calendar, no work in rain or wind >25 mph)
- Paving (5-day calendar, no work in rain or temp <50°F)
```

---

## Baseline vs. Current Schedule

If schedule has been updated:

**Extract variance**:
- **Baseline date**: Original planned date
- **Current date**: Updated forecast date
- **Variance**: Days ahead (+) or behind (-)

**Example**:
```
Substantial Completion:
- Baseline: 07/15/26
- Current: 07/29/26
- Variance: +14 days behind baseline
- Reason: PEMB delivery delayed 2 weeks
```

---

## Activity Codes / WBS

If schedule uses codes for filtering:

**Extract**:
- **Phase**: Sitework, Foundation, Framing, MEP Rough, Finishes, Closeout
- **Area**: North Wing, South Wing, Building A, Site
- **Responsible party**: GC, Sub name, Owner
- **Trade/CSI**: 03 Concrete, 05 Steel, 09 Finishes

**Purpose**: Filter schedule views by trade for coordination.

---

## Resource Loading (If Available)

For activities with resources:

**Extract**:
- **Labor**: Crew size, man-hours
- **Equipment**: Type (crane, excavator), hours, $/hr
- **Materials**: Quantities, cost

**Use**: Predict site congestion, equipment conflicts, procurement timing.

---

## Output Structure

```json
{
  "schedule": {
    "current_phase": "Foundation",
    "percent_complete": "15%",
    "milestones": [
      {
        "name": "Substantial Completion",
        "date": "2026-07-29",
        "status": "upcoming",
        "original_date": "2026-07-15",
        "variance_days": 14,
        "constraint": "MFO",
        "notes": "Contractual milestone"
      },
      ...
    ],
    "critical_path": [
      {
        "id": "A1020",
        "name": "Form and pour footings",
        "duration": 5,
        "start": "2026-02-16",
        "finish": "2026-02-20",
        "float": 0,
        "predecessors": ["A1010 (FS)"],
        "successors": ["A1030 (FS)"]
      },
      ...
    ],
    "near_critical": [
      {"id": "A2015", "name": "MEP underslab", "float": 3},
      ...
    ],
    "weather_sensitive": [
      {"id": "A1005", "name": "Rough grading", "calendar": "5-day"},
      ...
    ]
  }
}
```

---

## Integration with Daily Reports

Schedule data enables:
- **Milestone tracking**: "PEMB dried-in milestone achieved (3 days ahead of baseline)"
- **Critical path focus**: "Completed critical activity: Pour SOG (on schedule)"
- **Float monitoring**: "Drywall activity has 4 days float remaining"
- **Weather impact**: "Grading delayed 1 day due to rain (weather-sensitive activity)"
- **Sequencing explanation**: "Cannot start PEMB erection until SOG cures (7-day cure per schedule logic)"
