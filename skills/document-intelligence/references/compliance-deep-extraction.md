# Compliance - Deep Extraction Guide

Extract specific requirements from geotech, safety, SWPPP, and inspection documents.

## Geotechnical Report

**EXTRACT EXACT NUMBERS**:

- **Bearing capacity**: _____ PSF for spread footings
- **Allowable soil pressure**: _____ PSF
- **Water table depth**: ___ feet below grade
- **Frost depth**: ___ inches (affects footer depth)
- **Unsuitable soils**: Depth range to remove

**Compaction Requirements**:
- **Density**: "95% of modified proctor" or "98% standard proctor"
- **Lift thickness**: "8 inches loose, 6 inches compacted"
- **Testing frequency**: "1 test per 2,500 SF per lift" or "1 test per 500 CY"

**Example**:
```
Bearing: 3,000 PSF for footings at 4 feet depth
Water table: 12 feet below grade
Frost: 36 inches
Unsuitable: Remove top 2 feet of fill, replace with structural fill
Compaction: 95% modified proctor, 8" lifts max, test every 2,500 SF per lift
```

## SWPPP

**EXTRACT**:
- **Permit number**: State NPDES or equivalent
- **BMP locations**: Grid coordinates or descriptions
- **Rainfall threshold**: e.g., "0.5 inches in 24 hours"
- **Inspection frequency**: "Weekly + within 24 hours after qualifying rain"
- **Corrective action timeline**: "Immediate" or "Within 7 days"

**Example**:
```
Permit: KY0123456
BMPs:
  - Silt fence: Site perimeter, 1,200 LF
  - Inlet protection: All 6 storm inlets
  - Stabilized entrance: Main gate, 50'x20'
Inspection trigger: 0.5" rain in 24 hours
Inspection freq: Weekly + after rain events
Corrective action: Immediate for failures, 7 days for maintenance
```

## Special Inspections

**Hold Points**:
- Activity requiring inspection BEFORE proceeding
- Example: "Pre-placement rebar inspection before concrete"

**Witness Points**:
- Inspector should be present, but work can proceed
- Example: "Concrete placement (witness optional)"

**Testing Frequencies**:
- Extract with exact numbers
- Example: "Concrete: 1 set per 50 CY", "Compaction: 1 test per 2,500 SF"
