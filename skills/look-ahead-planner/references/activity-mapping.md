# Activity Mapping Reference

This reference guide covers the data structures, algorithms, and best practices for mapping schedule activities to subcontractors, locations, material requirements, and weather constraints in the Look-Ahead Planner skill.

---

## 1. Mapping Schedule Milestones & Critical Path to Daily Activities

### Data Structure: Schedule

The project-data skill provides schedule information in the following structure:

```json
{
  "schedule": {
    "milestones": [
      {
        "id": "M001",
        "name": "Groundbreaking",
        "planned_date": "2025-03-01",
        "critical": true,
        "linked_activities": ["A001", "A002"]
      }
    ],
    "critical_path": [
      {
        "activity_id": "A001",
        "name": "Excavation & Grade Beam",
        "start_date": "2025-03-01",
        "end_date": "2025-03-14",
        "duration_days": 14,
        "float": 0,
        "dependencies": [],
        "weather_sensitive": true
      },
      {
        "activity_id": "A002",
        "name": "Concrete Cure & Formwork Removal",
        "start_date": "2025-03-15",
        "end_date": "2025-03-21",
        "duration_days": 7,
        "float": 0,
        "dependencies": ["A001"],
        "weather_sensitive": true
      }
    ],
    "near_critical": [
      {
        "activity_id": "A010",
        "name": "Temporary Power Installation",
        "start_date": "2025-03-05",
        "end_date": "2025-03-07",
        "duration_days": 3,
        "float": 2,
        "dependencies": [],
        "weather_sensitive": false
      }
    ],
    "all_activities": [
      // All activities in project, including completed, in-progress, and future
    ]
  }
}
```

### Extraction Algorithm

**Goal**: For a given lookahead window (today to today + N weeks), extract all relevant activities and organize them by calendar date.

```pseudocode
function extractActivitiesInWindow(schedule, windowStart, windowEnd):
  activities = []
  
  // Include activities that:
  // 1. Have start_date >= windowStart AND start_date <= windowEnd, OR
  // 2. Are in progress (start_date < today) AND end_date <= windowEnd
  
  for each activity in schedule.all_activities:
    if (activity.end_date < windowStart):
      // Activity already complete, skip
      continue
    
    if (activity.start_date > windowEnd):
      // Activity outside window, skip
      continue
    
    // Activity overlaps window
    activities.append(activity)
  
  // Sort chronologically
  sort activities by start_date ascending
  
  return activities
```

### Daily Breakdown Logic

**Goal**: For each day in the lookahead window, show which activities are scheduled.

```pseudocode
function buildDailyBreakdown(extractedActivities, windowStart, windowEnd):
  dailySchedule = {}
  
  // Initialize daily buckets
  for date from windowStart to windowEnd:
    dailySchedule[date] = {
      date: date,
      day_of_week: DOW(date),
      activities: [],
      milestones: [],
      blockers: []
    }
  
  // Assign activities to dates
  for each activity in extractedActivities:
    
    // Calculate actual start in window (max of activity.start_date and windowStart)
    actual_start = max(activity.start_date, windowStart)
    
    // Calculate actual end in window (min of activity.end_date and windowEnd)
    actual_end = min(activity.end_date, windowEnd)
    
    // Add activity to each day it spans
    for date from actual_start to actual_end:
      dailySchedule[date].activities.append({
        activity_id: activity.id,
        name: activity.name,
        actual_start: actual_start,
        actual_end: actual_end,
        days_remaining: (actual_end - date + 1),
        critical: activity.critical_path_flag,
        float: activity.float,
        weather_sensitive: activity.weather_sensitive
      })
  
  // Assign milestones to dates
  for each milestone in schedule.milestones:
    if (milestone.planned_date >= windowStart AND milestone.planned_date <= windowEnd):
      dailySchedule[milestone.planned_date].milestones.append(milestone)
  
  return dailySchedule
```

---

## 2. Resolving Activities to Subcontractors

### Data Structure: Subcontractor Assignments

The project-data skill provides subcontractor information:

```json
{
  "subcontractors": [
    {
      "id": "SUB001",
      "name": "ABC Excavation",
      "trades": ["Excavation", "Grading", "Site Prep"],
      "contact": {
        "foreman": "John Smith",
        "phone": "555-0101",
        "email": "john@abcexcavation.com"
      },
      "crew_capacity": 8,
      "typical_crew_size_by_activity": {
        "Excavation": 6,
        "Grading": 4,
        "Site Prep": 3
      },
      "equipment_owned": ["Excavator", "Dozer", "Grader"],
      "equipment_rented": ["Crane", "Compactor"]
    },
    {
      "id": "SUB002",
      "name": "XYZ Concrete",
      "trades": ["Concrete", "Flatwork"],
      "typical_crew_size_by_activity": {
        "Concrete Pour": 5,
        "Concrete Cure": 2
      }
    }
  ],
  "subcontractor_assignments": [
    {
      "activity_id": "A001",
      "activity_name": "Excavation & Grade Beam",
      "assigned_sub_id": "SUB001",
      "assigned_sub_name": "ABC Excavation",
      "scope": "Excavation",
      "notes": "Lead contractor"
    },
    {
      "activity_id": "A002",
      "activity_name": "Concrete Cure & Formwork Removal",
      "assigned_sub_id": "SUB002",
      "assigned_sub_name": "XYZ Concrete",
      "scope": "Concrete",
      "notes": "Depends on formwork from GC"
    }
  ]
}
```

### Resolution Algorithm

**Goal**: For each activity in the lookahead, determine the assigned subcontractor and estimate crew headcount.

```pseudocode
function resolveActivityToSubcontractor(activity, assignments, subcontractors):
  
  // Look up assignment
  assignment = findAssignment(activity.id, assignments)
  
  if (assignment is null):
    return {
      status: "unassigned",
      warning: "No subcontractor assigned to activity " + activity.id
    }
  
  // Look up subcontractor details
  sub = findSubcontractor(assignment.sub_id, subcontractors)
  
  // Determine crew headcount
  crew_size = sub.typical_crew_size_by_activity[activity.scope]
  
  if (crew_size is null):
    // Fallback to GC estimate in activity record
    crew_size = activity.estimated_crew_size OR sub.crew_capacity / 2
  
  // Check crew capacity constraints
  if (crew_size > sub.crew_capacity):
    crew_size = sub.crew_capacity
    warning = "Activity crew exceeds subcontractor capacity"
  
  return {
    sub_id: sub.id,
    sub_name: sub.name,
    foreman: sub.contact.foreman,
    phone: sub.contact.phone,
    trades: sub.trades,
    crew_size: crew_size,
    equipment_needed: activity.equipment_requirements,
    equipment_owned: sub.equipment_owned,
    equipment_to_rent: difference(activity.equipment_requirements, sub.equipment_owned),
    warnings: [...]
  }
```

### Crew Capacity Planning

When multiple activities are assigned to the same subcontractor within the lookahead window, check for resource conflicts:

```pseudocode
function checkCrewCapacity(subcontractor, activities_assigned):
  
  conflicts = []
  
  // For each day in lookahead window
  for each date:
    total_crew_needed = 0
    
    for each activity assigned to this sub:
      if (activity spans date):
        total_crew_needed += activity.crew_size
    
    if (total_crew_needed > subcontractor.crew_capacity):
      conflicts.append({
        date: date,
        crew_needed: total_crew_needed,
        crew_available: subcontractor.crew_capacity,
        shortfall: total_crew_needed - subcontractor.crew_capacity,
        activities: [list of overlapping activities]
      })
  
  if (conflicts.length > 0):
    flag: "RESOURCE_CONFLICT"
    note: "Subcontractor crew overallocated on these dates"
  
  return conflicts
```

---

## 3. Resolving Activities to Locations

### Data Structure: Site Layout

The project-data skill provides site information:

```json
{
  "site_layout": {
    "project_address": "123 Main St, Springfield, IL 62701",
    "site_dimensions": {
      "length_ft": 200,
      "width_ft": 150
    },
    "building_areas": [
      {
        "area_id": "BA001",
        "name": "Main Building - Zone A",
        "description": "Foundation and structural frame",
        "grid_extents": {
          "north_min": 100,
          "north_max": 150,
          "east_min": 0,
          "east_max": 100
        }
      },
      {
        "area_id": "BA002",
        "name": "Main Building - Zone B",
        "description": "MEP and interior finishes",
        "grid_extents": {
          "north_min": 100,
          "north_max": 150,
          "east_min": 100,
          "east_max": 200
        }
      }
    ],
    "grid_lines": {
      "baseline": "A",
      "northing_interval": 20,
      "easting_interval": 25,
      "named_lines": [
        { "direction": "north", "name": "A", "offset_ft": 0 },
        { "direction": "north", "name": "B", "offset_ft": 20 },
        { "direction": "north", "name": "C", "offset_ft": 40 },
        { "direction": "east", "name": "1", "offset_ft": 0 },
        { "direction": "east", "name": "2", "offset_ft": 25 },
        { "direction": "east", "name": "3", "offset_ft": 50 }
      ]
    },
    "access_points": [
      {
        "id": "AP001",
        "name": "Main Gate",
        "location": "East side",
        "suitable_for": ["Material delivery", "Crew access"]
      }
    ],
    "material_staging": [
      {
        "id": "MS001",
        "name": "Rebar Storage",
        "location": "Lines A-B / 1-2",
        "capacity": "50 tons"
      }
    ]
  }
}
```

### Location Resolution Algorithm

**Goal**: For each activity, determine the building area(s) and grid line references.

```pseudocode
function resolveActivityLocation(activity, siteLayout):
  
  // Activities may reference locations in different ways:
  // 1. Explicit activity.location field: "Zone A"
  // 2. Building area from activity.scope: "Foundation" → BA001
  // 3. Grid intersection from activity.grid_lines: "A-1 to C-3"
  
  locations = []
  grid_references = []
  
  // Method 1: Explicit location
  if (activity.location is not null):
    area = findBuildingArea(activity.location, siteLayout)
    if (area is not null):
      locations.append(area)
  
  // Method 2: Infer from activity type
  if (activity.activity_type == "Foundation"):
    areas = findBuildingAreasByDescription("Foundation", siteLayout)
    locations.extend(areas)
  
  if (activity.activity_type == "Interior Finishes"):
    areas = findBuildingAreasByDescription("Interior", siteLayout)
    locations.extend(areas)
  
  // Method 3: Grid line references
  if (activity.grid_lines is not null):
    grid_refs = parseGridReferences(activity.grid_lines, siteLayout)
    grid_references.extend(grid_refs)
  
  // Consolidate and deduplicate
  locations = unique(locations)
  grid_references = unique(grid_references)
  
  return {
    building_areas: locations,
    grid_lines: grid_references,
    access_point: findNearestAccess(locations[0], siteLayout.access_points),
    material_staging: findNearbyStaging(locations[0], siteLayout.material_staging),
    weather_exposure: inferWeatherExposure(locations)
  }
```

### Grid Line Parsing

Grid lines are expressed as coordinate ranges, e.g., "A-1 to C-3" (northeast corner of zone).

```pseudocode
function parseGridReferences(gridString, siteLayout):
  // Format: "A-1 to C-3" or "A1 to C3"
  // Extracts: Lines A, B, C (north) and Lines 1, 2, 3 (east)
  
  pattern = "([A-Z]+)[\-]?([0-9]+) to ([A-Z]+)[\-]?([0-9]+)"
  match = regex(gridString, pattern)
  
  if (match is null):
    return []
  
  start_north = match[1]  // e.g., "A"
  start_east = match[2]   // e.g., "1"
  end_north = match[3]    // e.g., "C"
  end_east = match[4]     // e.g., "3"
  
  // Expand to all grid lines in range
  north_lines = expandRange(start_north, end_north, siteLayout.grid_lines.north)
  east_lines = expandRange(start_east, end_east, siteLayout.grid_lines.east)
  
  return {
    north_lines: north_lines,
    east_lines: east_lines,
    intersections: cartesianProduct(north_lines, east_lines)
  }
```

---

## 4. Identifying Material Needs

### Data Structure: Material Requirements

The project-data skill provides material mapping by activity type:

```json
{
  "material_requirements_by_activity": {
    "Excavation": {
      "typical_materials": ["Soil disposal", "Fill material"],
      "equipment": ["Excavator", "Dump truck"]
    },
    "Concrete Pour": {
      "typical_materials": ["Ready-mix concrete", "Rebar", "Formwork lumber"],
      "quantities_by_size": {
        "small": "50 cy",
        "medium": "100 cy",
        "large": "300+ cy"
      },
      "lead_time_days": 7,
      "equipment": ["Concrete pump", "Vibrator"]
    },
    "Concrete Cure": {
      "typical_materials": ["Curing compound", "Plastic sheeting"],
      "equipment": [],
      "duration_days": 7,
      "weather_sensitive": true
    },
    "MEP Rough-In": {
      "typical_materials": ["Copper tubing", "PVC conduit", "Wire"],
      "equipment": [],
      "requires_submittal": true
    }
  },
  "procurement_log": [
    {
      "material_id": "MAT001",
      "name": "Ready-mix Concrete for Grade Beam",
      "quantity": "200 cubic yards",
      "unit_price": 180,
      "supplier": "Concrete Co.",
      "purchase_order": "PO-2025-001",
      "order_date": "2025-02-10",
      "promised_delivery": "2025-03-15",
      "actual_delivery": null,
      "status": "on_order",
      "related_activities": ["A002"],
      "notes": "Critical for concrete pour"
    }
  ]
}
```

### Material Identification Algorithm

**Goal**: For each activity in the lookahead, identify required materials and their procurement status.

```pseudocode
function identifyMaterialNeeds(activity, materialRequirements, procurementLog):
  
  // Look up typical materials for this activity type
  template = materialRequirements[activity.activity_type]
  
  if (template is null):
    return {
      materials: [],
      warning: "No material template for activity type: " + activity.activity_type
    }
  
  materials = []
  
  // For each typical material
  for each material_name in template.typical_materials:
    
    // Search procurement log for related materials
    procItems = findInProcurementLog(material_name, activity.id, procurementLog)
    
    for each item in procItems:
      // Check if delivery date is before activity start
      delivery_days_before_activity = activity.start_date - item.promised_delivery
      
      material_entry = {
        material_id: item.id,
        name: item.name,
        quantity: item.quantity,
        supplier: item.supplier,
        po_number: item.purchase_order,
        promised_delivery: item.promised_delivery,
        actual_delivery: item.actual_delivery,
        status: item.status,
        days_before_activity_start: delivery_days_before_activity,
        at_risk: (delivery_days_before_activity < 3),
        delivered: (item.actual_delivery is not null),
        related_activity: activity.id
      }
      
      materials.append(material_entry)
  
  return {
    materials: materials,
    total_at_risk: count(materials where at_risk == true),
    all_confirmed: count(materials where delivered == true)
  }
```

### Material Delivery Callouts

In the lookahead HTML output, material deliveries are highlighted on the day they arrive:

```pseudocode
function buildMaterialDeliveryCallouts(dailySchedule, procurementLog):
  
  for each day in dailySchedule:
    deliveries = []
    
    for each procItem in procurementLog:
      
      // If delivery is today
      if (procItem.promised_delivery == day.date):
        delivery_entry = {
          material_name: procItem.name,
          quantity: procItem.quantity,
          supplier: procItem.supplier,
          status: procItem.status,
          related_activities: procItem.related_activities,
          highlight_color: (procItem.status == "on_order" ? "amber" : "green")
        }
        deliveries.append(delivery_entry)
    
    day.material_deliveries = deliveries
  
  return dailySchedule
```

---

## 5. Determining Weather Sensitivity

### Data Structure: Weather Thresholds

The project-data skill defines weather constraints:

```json
{
  "weather_thresholds": {
    "temperature": {
      "concrete_pour_min_celsius": 10,
      "concrete_pour_max_celsius": 35,
      "exterior_paint_min_celsius": 15,
      "excavation_blocked_celsius_below": -5
    },
    "precipitation": {
      "concrete_pour_blocked_by_rain": true,
      "excavation_minor_impact": 0.5,
      "excavation_blocked_above_inch": 1.0,
      "exterior_paint_blocked_by_rain": true
    },
    "wind": {
      "crane_operations_max_knots": 20,
      "exterior_work_caution_knots": 15
    }
  },
  "weather_sensitive_activities": [
    {
      "activity_type": "Concrete Pour",
      "temperature_min": 10,
      "temperature_max": 35,
      "precipitation_max_inches": 0,
      "notes": "Concrete requires stable curing conditions"
    },
    {
      "activity_type": "Exterior Paint",
      "temperature_min": 15,
      "temperature_max": 32,
      "precipitation_max_inches": 0,
      "humidity_max_percent": 85,
      "notes": "Paint application requires dry conditions and moderate temps"
    }
  ]
}
```

### Weather Sensitivity Detection

**Goal**: For each activity, determine if it is weather-sensitive and under what conditions it may be blocked.

```pseudocode
function determineWeatherSensitivity(activity, weatherSensitiveActivities, weatherThresholds):
  
  // Look up sensitivity rules for this activity type
  sensitivity = findInWeatherSensitiveList(activity.activity_type, weatherSensitiveActivities)
  
  if (sensitivity is null):
    return {
      weather_sensitive: false,
      constraints: []
    }
  
  constraints = []
  
  if (sensitivity.temperature_min is not null):
    constraints.append({
      type: "temperature_minimum",
      value_celsius: sensitivity.temperature_min,
      description: "Min " + sensitivity.temperature_min + "°C"
    })
  
  if (sensitivity.temperature_max is not null):
    constraints.append({
      type: "temperature_maximum",
      value_celsius: sensitivity.temperature_max,
      description: "Max " + sensitivity.temperature_max + "°C"
    })
  
  if (sensitivity.precipitation_max_inches is not null):
    constraints.append({
      type: "precipitation_maximum",
      value_inches: sensitivity.precipitation_max_inches,
      description: "No more than " + sensitivity.precipitation_max_inches + " inch(es) rain"
    })
  
  if (sensitivity.humidity_max_percent is not null):
    constraints.append({
      type: "humidity_maximum",
      value_percent: sensitivity.humidity_max_percent,
      description: "Humidity < " + sensitivity.humidity_max_percent + "%"
    })
  
  return {
    weather_sensitive: true,
    activity_type: activity.activity_type,
    constraints: constraints,
    notes: sensitivity.notes
  }
```

### Forecast-Based Blocking

When the weather forecast is fetched, activities are flagged if conditions violate constraints:

```pseudocode
function checkWeatherBlocking(activity, weatherConstraints, forecast):
  
  if (activity.weather_sensitive == false):
    return {
      blocked: false,
      alerts: []
    }
  
  alerts = []
  blocked_dates = []
  
  for each day in activity.date_range:
    forecastDay = forecast[day]
    violations = []
    
    for each constraint in weatherConstraints:
      
      if (constraint.type == "temperature_minimum"):
        if (forecastDay.temp_low_celsius < constraint.value_celsius):
          violations.append("Temperature too low: " + forecastDay.temp_low_celsius + "°C")
      
      if (constraint.type == "temperature_maximum"):
        if (forecastDay.temp_high_celsius > constraint.value_celsius):
          violations.append("Temperature too high: " + forecastDay.temp_high_celsius + "°C")
      
      if (constraint.type == "precipitation_maximum"):
        if (forecastDay.precipitation_inches > constraint.value_inches):
          violations.append("Rain expected: " + forecastDay.precipitation_inches + " inches")
      
      if (constraint.type == "humidity_maximum"):
        if (forecastDay.humidity_percent > constraint.value_percent):
          violations.append("High humidity: " + forecastDay.humidity_percent + "%")
    
    if (violations.length > 0):
      blocked_dates.append(day)
      alerts.append({
        date: day,
        violations: violations,
        forecast_summary: forecastDay.summary
      })
  
  return {
    blocked: blocked_dates.length > 0,
    blocked_dates: blocked_dates,
    alerts: alerts,
    recommendation: (blocked_dates.length > 0 ? "May need to reschedule" : "Proceed as planned")
  }
```

---

## 6. Activity Duration Splitting

### Multi-Week Activity Breakdown

Activities that span multiple weeks are broken into logical daily chunks for the lookahead display.

```pseudocode
function splitActivityAcrossDays(activity, dailySchedule):
  
  // For a multi-day activity (e.g., 14-day excavation)
  // we show it on each calendar day it spans
  
  // But we also want to communicate:
  // - How many days of work remain
  // - Percent progress (if in progress)
  // - Critical milestones within the activity
  
  activity_fragments = []
  
  for each day from activity.start_date to activity.end_date:
    days_elapsed = day - activity.start_date
    days_remaining = activity.end_date - day
    percent_complete = (days_elapsed / activity.duration_days) * 100
    
    fragment = {
      date: day,
      activity_id: activity.id,
      activity_name: activity.name,
      days_elapsed: days_elapsed,
      days_remaining: days_remaining,
      percent_complete: percent_complete,
      is_start_day: (day == activity.start_date),
      is_end_day: (day == activity.end_date),
      is_in_progress: (day >= today AND day <= activity.end_date),
      display_label: formatActivityLabel(activity, days_remaining)
    }
    
    activity_fragments.append(fragment)
  
  return activity_fragments
```

### Activity Label Formatting

The lookahead display uses abbreviated labels to save space:

```
Day 1 of 14: Excavation (13 days remaining)
Day 5 of 14: Excavation (9 days remaining)
Day 14 of 14: Excavation - COMPLETE
```

---

## 7. Handling Float and Flexibility

### Critical Path vs. Near-Critical

Activities are color-coded based on available float:

| Float Status | Float (days) | Color  | Description                              |
|--------------|--------------|--------|------------------------------------------|
| Critical     | 0            | Red    | No delay tolerance; delays impact end date |
| Near-Critical| 1–5          | Amber  | Limited flexibility; monitor closely      |
| On-Track     | 6+           | Green  | Schedule slack available                 |
| Blocked      | N/A          | Gray   | Weather, material, or RFI blocking work  |

### Float Calculation

For each activity in the critical path analysis:

```pseudocode
function calculateActivityFloat(activity, criticalPath):
  
  // Forward pass: earliest start, earliest finish
  // Backward pass: latest start, latest finish
  // Float = Latest Start - Earliest Start = Latest Finish - Earliest Finish
  
  // Simplified: if activity is on critical path, float = 0
  if (activity in criticalPath):
    activity.float = 0
    activity.critical = true
  else:
    // Near-critical if float is small relative to activity duration
    if (activity.float < activity.duration_days / 3):
      activity.near_critical = true
    else:
      activity.near_critical = false
    
    activity.critical = false
  
  return activity
```

### Handling Schedule Compression

When activities have been compressed (shorter duration than typical), this is noted:

```pseudocode
function checkScheduleCompression(activity, projectBaseline):
  
  baseline_duration = projectBaseline.typical_duration[activity.type]
  compression_factor = baseline_duration / activity.duration_days
  
  if (compression_factor > 1.2):
    // Activity is compressed by 20%+ from baseline
    flag: "SCHEDULE_COMPRESSION"
    note: "Activity duration compressed " + compression_factor.toFixed(2) + "x vs. baseline"
    risk_level: "HIGH"
  
  return compression_factor
```

---

## 8. Handling Blockers and Delays

### Blocker Detection

The lookahead scans for items that may prevent an activity from starting or completing:

```pseudocode
function detectBlockers(activity, rfiLog, submittalLog, procurementLog):
  
  blockers = []
  
  // Check RFIs
  for each rfi in rfiLog:
    if (rfi.related_activities includes activity.id):
      if (rfi.status == "pending" OR rfi.status == "submitted"):
        if (rfi.due_date > activity.start_date):
          // RFI response due after activity starts - RED FLAG
          blockers.append({
            type: "RFI",
            id: rfi.id,
            description: "RFI " + rfi.id + " due " + rfi.due_date,
            severity: "CRITICAL",
            resolution_needed_by: activity.start_date
          })
  
  // Check Submittals
  for each submittal in submittalLog:
    if (submittal.related_activities includes activity.id):
      if (submittal.status == "pending" OR submittal.status == "submitted"):
        if (submittal.approval_due_date > activity.start_date):
          blockers.append({
            type: "Submittal",
            id: submittal.id,
            description: "Submittal " + submittal.id + " due " + submittal.approval_due_date,
            severity: "CRITICAL"
          })
  
  // Check Material Delivery
  for each material in activity.required_materials:
    procurement_item = findInProcurementLog(material, procurementLog)
    
    if (procurement_item is not null):
      if (procurement_item.promised_delivery > activity.start_date):
        blockers.append({
          type: "Material",
          id: procurement_item.id,
          description: material + " arrives " + procurement_item.promised_delivery,
          severity: "CRITICAL",
          days_late: procurement_item.promised_delivery - activity.start_date
        })
  
  return {
    blocker_count: blockers.length,
    blockers: blockers,
    can_start: blockers.length == 0,
    alert_level: (blockers.length > 0 ? "HIGH" : "LOW")
  }
```

### Blocker Display in Lookahead

Blockers are displayed as warning banners at the top of the lookahead:

```html
<div class="blocker-alert" style="background-color: #DC3545; color: white; padding: 12px;">
  <strong>⚠ BLOCKER:</strong> RFI-025 response due 2025-03-10 (2 days before Concrete Pour starts)
</div>
```

---

## Summary Table: Activity Mapping Rules

| Data Point          | Source                  | Resolution Method           | Notes                                 |
|---------------------|-------------------------|-----------------------------|-----------------------------------------|
| Subcontractor       | subcontractor_assignments | Direct lookup by activity ID | Flag if unassigned                      |
| Crew Headcount      | sub.typical_crew_size_by_activity | Lookup by activity type/scope | Cap at sub.crew_capacity            |
| Building Area       | activity.location + siteLayout | Parse + fuzzy match        | May span multiple areas                |
| Grid Lines          | activity.grid_lines + siteLayout | Parse range notation (A-1 to C-3) | Cartesian expansion               |
| Materials           | activity.type + material_requirements | Template lookup           | Cross-ref with procurement_log         |
| Weather Sensitivity | activity.type + weather_sensitive_activities | Template lookup | Fetch forecast and check constraints |
| Blockers            | rfiLog, submittalLog, procurementLog | Date comparison         | Flag if resolution due after activity start |
| Float & Criticality | schedule.critical_path + CPM | Lookup or recalculate     | Red (0 float), Amber (1-5), Green (6+) |

