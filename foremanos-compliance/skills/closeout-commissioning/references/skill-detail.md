# closeout-commissioning — Detailed Reference



Extended documentation, examples, templates, and detailed criteria for the closeout-commissioning skill.



## Functional Performance Testing (FPT)

### What FPT Is

Functional Performance Testing consists of documented tests that verify building systems perform according to the design intent under all expected operating conditions. FPT goes beyond simple startup verification — it tests the system through every mode of operation, every failure scenario, and every seasonal condition.

### FPT Procedure Development

- **CxA writes** all FPT procedures (not the contractor)
- **Contractor executes** the test (operates the equipment, makes adjustments)
- **CxA witnesses** and documents results (pass/fail, measurements, observations)
- Procedures are written based on the approved sequences of operation, equipment submittals, and design documents
- Each procedure is a step-by-step test script with expected results at each step

### HVAC Mode-by-Mode Testing

**Cooling Mode:**
```
FPT — COOLING MODE VERIFICATION

Pre-Test Conditions:
- Space temperature above cooling setpoint (or simulate with setpoint adjustment)
- Outdoor conditions: cooling season or simulate with controls

Test Steps:
1. Verify thermostat/zone sensor reads space temperature accurately (±1°F of reference)
2. Set cooling setpoint below current space temperature
3. Verify cooling call initiates within [specified] minutes
4. Measure Supply Air Temperature (SAT):
   Expected: [design SAT, typically 55°F ± 2°F]
   Actual: ___°F  Pass / Fail
5. Verify compressor/condenser staging:
   Stage 1 activates at: ___°F above setpoint
   Stage 2 activates at: ___°F above setpoint
   Verify staging sequence matches sequence of operations
6. Check economizer operation (if applicable):
   OAT below changeover: economizer active (see economizer test)
   OAT above changeover: economizer locked out, mechanical cooling only
7. Verify damper positions:
   OA damper at minimum position: ___% (design: ___%  )
   RA damper modulating appropriately
8. Measure airflows vs. design:
   Total supply: ___CFM (design: ___CFM, tolerance ±10%)
   Total return: ___CFM (design: ___CFM, tolerance ±10%)
   Outdoor air: ___CFM (design: ___CFM, tolerance ±10%)
```

**Heating Mode:**
```
FPT — HEATING MODE VERIFICATION

Pre-Test Conditions:
- Space temperature below heating setpoint (or simulate)
- System in heating mode

Test Steps:
1. Verify thermostat/zone sensor reads accurately (±1°F of reference)
2. Set heating setpoint above current space temperature
3. Verify heating call initiates within [specified] minutes
4. Measure Supply Air Temperature (SAT):
   Expected: [design heating SAT, typically 90-120°F]
   Actual: ___°F  Pass / Fail
5. Verify staging:
   Gas valve: Stage 1 fires at ___°F below setpoint
   Stage 2 fires at ___°F below setpoint (if applicable)
   Electric elements: Stage sequence per design
6. Verify auxiliary/emergency heat operation (heat pumps):
   Auxiliary activates when heat pump cannot maintain setpoint
   Emergency heat activates on manual command or heat pump lockout
7. Measure SAT at full heating output
   Expected: ___°F   Actual: ___°F   Pass / Fail
```

**Unoccupied Mode:**
```
FPT — UNOCCUPIED MODE VERIFICATION

Test Steps:
1. Switch system to unoccupied schedule (via BAS or time clock)
2. Verify setback temperatures activate:
   Heating setback: ___°F (design: ___°F)
   Cooling setback: ___°F (design: ___°F)
3. Verify fan operation:
   Fan off / Fan cycling (per design):  Pass / Fail
   If cycling: verify cycle time ___min on / ___min off
4. Verify no unnecessary energy consumption:
   Exhaust fans off (unless continuous):  Pass / Fail
   Lighting in auto-off:  Pass / Fail
5. Verify unoccupied override:
   Activate override at thermostat or BAS
   System returns to occupied setpoints:  Pass / Fail
   Override timeout: ___hours (design: ___hours)
```

**Morning Warmup/Cooldown:**
```
FPT — OPTIMAL START VERIFICATION

Test Steps:
1. Set occupied start time to [time]
2. Verify optimal start engages at [calculated time before occupancy]
3. Verify pre-conditioning sequence:
   OA damper closed during warmup/cooldown:  Pass / Fail
   System transitions to occupied mode at occupied start time:  Pass / Fail
   OA damper opens to minimum position at occupied time:  Pass / Fail
4. Verify space reaches setpoint by occupied time:
   Target: space within 2°F of setpoint by occupied start
   Actual: ___°F at occupied start time   Pass / Fail
```

**Economizer Testing:**
```
FPT — ECONOMIZER VERIFICATION

Test Steps:
1. Verify changeover setpoint:
   Dry-bulb changeover: ___°F (design: ___°F)
   Enthalpy changeover: ___BTU/lb (if applicable)
2. OAT below changeover — economizer active:
   OA damper modulates from min to 100%:  Pass / Fail
   OA damper at 100% when OAT provides free cooling:  Pass / Fail
   Mechanical cooling locked out when full economizer satisfies:  Pass / Fail
3. OAT above changeover — economizer locked out:
   OA damper returns to minimum position:  Pass / Fail
   Mechanical cooling activates:  Pass / Fail
4. Verify minimum OA maintained at all times during occupied:
   Minimum OA CFM: ___ (design: ___CFM)   Pass / Fail
```

**Demand Control Ventilation (DCV):**
```
FPT — DCV VERIFICATION

Test Steps:
1. Verify CO2 sensor accuracy:
   Reference CO2: ___ppm   Sensor reading: ___ppm
   Tolerance: ±75ppm   Pass / Fail
2. Simulate high occupancy (generate CO2 or use calibration gas):
   CO2 rises above setpoint (typically 800-1000 ppm)
   OA damper modulates to increase ventilation:  Pass / Fail
3. Simulate low occupancy:
   CO2 drops below setpoint
   OA damper modulates to reduce ventilation:  Pass / Fail
4. Verify minimum ventilation maintained:
   At lowest CO2, OA damper does not close below minimum:  Pass / Fail
   Minimum OA CFM: ___ (design: ___CFM)   Pass / Fail
```

### Lighting Controls Testing

```
FPT — LIGHTING CONTROLS

Occupancy Sensors:
1. Verify sensor coverage: walk entire space, verify sensor detects motion
2. Verify timeout: vacate space, time until lights off
   Timeout: ___min (design: ___min)   Pass / Fail
3. Verify sensitivity: minor motion (seated work) keeps lights on   Pass / Fail

Daylight Harvesting:
1. Verify photosensor location and calibration
2. High daylight condition: verify lights dim to minimum or off
3. Low daylight condition: verify lights at full output
4. Transition: verify smooth dimming (no visible stepping or flicker)

Scheduling:
1. Verify on-time per schedule: lights activate at ___AM   Pass / Fail
2. Verify off-time per schedule: lights deactivate at ___PM   Pass / Fail
3. Manual override: activate after scheduled off
   Override timeout: ___hours (design: ___hours)   Pass / Fail

Emergency/Egress Lighting:
1. Simulate power failure (open breaker or use test switch)
2. Verify emergency lights activate within 10 seconds   Pass / Fail
3. Maintain illumination for 90-minute battery test
4. Measure illumination levels at end of test: ___fc (min 1fc avg)   Pass / Fail
5. Verify battery charger restores charge after test
```

### Fire/Life Safety Integration Testing

This is the most critical FPT — it verifies that all fire and life safety systems work together as an integrated system.

```
FPT — FIRE/LIFE SAFETY INTEGRATION

Pre-Test: Notify fire alarm monitoring company, AHJ, and building occupants

Initiating Device Verification:
- Smoke detectors: test each with canned smoke or magnet   Pass / Fail
- Heat detectors: test with heat gun (rate-of-rise) or listed tester   Pass / Fail
- Manual pull stations: activate each, verify alarm   Pass / Fail
- Waterflow switches: open inspector's test connection, verify alarm   Pass / Fail
- Tamper switches: close valve 2 turns, verify supervisory signal   Pass / Fail

System Integration (activate alarm, verify all responses):
1. HVAC shutdown on alarm:
   All AHUs stop (or per sequence):  Pass / Fail
   Exhaust fans stop (except stairwell pressurization):  Pass / Fail
2. Elevator recall:
   All elevators return to primary recall floor:  Pass / Fail
   Elevator on fire floor recalls to alternate floor:  Pass / Fail
3. Door hold-open release:
   All magnetic door holders release:  Pass / Fail
   Doors close and latch:  Pass / Fail
4. Stairwell pressurization:
   Stairwell fans start:  Pass / Fail
   Measure pressure differential: ___" w.c. (min 0.05", max per code)
5. Smoke damper closure:
   All smoke dampers close on alarm:  Pass / Fail
   Verify position feedback to FACP:  Pass / Fail
6. Fire pump start:
   Open inspector's test, verify pressure drop starts pump:  Pass / Fail
   Verify jockey pump does not short-cycle:  Pass / Fail
7. Generator start on utility loss:
   Simulate utility failure (open main breaker with AHJ approval)
   Generator starts within 10 seconds:  Pass / Fail
   ATS transfers load within 10 seconds:  Pass / Fail
   Emergency circuits energized:  Pass / Fail

Post-Test: Reset all systems, notify monitoring company, verify normal operation
```

### FPT Documentation

**Pre-Functional Checklist:**
- All items must be checked and signed off BEFORE FPT begins
- Contractor completes, CxA verifies
- Includes: installation per plans, connections verified, controls addressed, startup complete

**FPT Form Structure:**
- Header: project name, system, equipment ID, date, participants
- Test procedure: step-by-step instructions
- Expected result: what should happen at each step
- Actual result: what actually happened (measured values, observations)
- Pass/Fail: for each step
- Deficiency notes: description of any failures
- Trend log data: BAS screenshots showing performance during test
- Photos: equipment during test, nameplate data, control screen captures
- Sign-offs: CxA, contractor, owner's representative

---



## TAB — Testing, Adjusting, and Balancing

### What TAB Is

Testing, Adjusting, and Balancing (TAB) is the process of measuring airflow and water flow in HVAC systems, then adjusting distribution components (dampers, balancing valves) to deliver design flow rates to each space. TAB is performed by a certified, independent agency — not the installing contractor.

### Standards and Certification

- **AABC (Associated Air Balance Council):** Certifies TAB agencies, publishes National Standards for Testing and Balancing
- **NEBB (National Environmental Balancing Bureau):** Certifies TAB firms and technicians, publishes Procedural Standards
- **ASHRAE Standard 111:** Practices for Measurement, Testing, Adjusting, and Balancing of Building HVAC Systems
- Specifications typically require TAB agency to be AABC or NEBB certified

### HVAC Airflow Measurement Methods

| Method | Where Used | Accuracy | Notes |
|--------|-----------|----------|-------|
| Pitot tube traverse | In ductwork | ±5% | Most accurate, requires access to straight duct run |
| Capture hood (flow hood) | At diffusers/grilles | ±5-10% | Fast, used for individual outlet readings |
| Flow station | Permanent duct device | ±3-5% | Installed during construction, used for ongoing monitoring |
| Velometer (anemometer) | At grille face | ±10-15% | Least accurate, face velocity only — must multiply by area and Ak factor |

### Ductwork Balancing Procedure

```
TAB AIRFLOW BALANCING — SYSTEMATIC PROCEDURE

1. FAN MEASUREMENT
   - Measure total fan airflow (pitot traverse at fan discharge or return)
   - Compare to design: ___CFM actual vs. ___CFM design
   - Adjust fan speed (VFD, sheave) if total is not within ±10% of design
   - Record fan RPM, motor amps, static pressure

2. TRUNK DUCT BALANCING
   - Measure airflow in each main trunk duct
   - Proportion trunk flows to match design ratios
   - Adjust trunk balancing dampers as needed

3. BRANCH DUCT BALANCING
   - Measure airflow in each branch duct
   - Proportion branch flows to match design ratios
   - Adjust branch balancing dampers as needed

4. INDIVIDUAL OUTLET MEASUREMENT
   - Measure each supply diffuser/grille with capture hood
   - Measure each return grille with capture hood
   - Record readings on TAB report form

5. INDIVIDUAL OUTLET ADJUSTMENT
   - Adjust balancing dampers at each outlet
   - Use proportional balancing method:
     a. Set outlet with highest % of design to 100% open
     b. Reduce all other outlets proportionally
     c. Re-measure all outlets
     d. Iterate until all within ±10% of design CFM

6. VERIFY TOTALS
   - Re-measure total supply airflow
   - Re-measure total return airflow
   - Verify outdoor air quantity
   - All totals must be within ±10% of design
```

### Hydronic Balancing

```
TAB HYDRONIC BALANCING PROCEDURE

1. PUMP VERIFICATION
   - Measure pump flow rate (using circuit setter or ultrasonic flowmeter)
   - Measure pump head (suction and discharge pressure)
   - Plot operating point on pump curve
   - Verify pump is operating near design point

2. MAIN LOOP BALANCING
   - Verify total system flow matches design
   - Measure supply and return temperatures
   - Calculate system delta-T: design ΔT = ___°F, actual ΔT = ___°F

3. BRANCH/RISER BALANCING
   - Measure flow at each branch circuit setter
   - Adjust proportionally to achieve design flows

4. TERMINAL UNIT BALANCING
   - Measure flow at each coil/terminal unit using:
     • Circuit setters (preferred — permanent, repeatable)
     • Ultrasonic flowmeter (non-invasive, accurate)
     • Pressure drop across coil (less accurate, requires coil curve)
   - Adjust balancing valves to achieve design flow ±10%
   - Verify ΔT across each coil matches design
     Design ΔT: ___°F   Actual ΔT: ___°F

5. VERIFY SYSTEM
   - Re-measure total system flow
   - Check that no circuit is starved
   - Verify pump operating point has not shifted significantly
```

### TAB Acceptance Criteria

| Parameter | Tolerance |
|-----------|-----------|
| Total system supply airflow | ±10% of design |
| Total system return airflow | ±10% of design |
| Individual supply outlets | ±10% of design CFM |
| Individual return outlets | ±10% of design CFM |
| Outdoor air quantity | ±10% of design (critical for IAQ) |
| Total hydronic flow | ±10% of design |
| Individual coil/terminal flow | ±10% of design |
| Sound levels | Within specification (NC rating or dBA) |
| Vibration levels | Within specification (mils or IPS) |

### TAB Report Review

When the TAB agency submits their report, review for:
- All readings recorded (no blanks — every outlet, every coil)
- Compare each reading to design value — flag outliers
- Verify totals add up (sum of branch flows should equal trunk flow)
- Identify system deficiencies that TAB cannot fix:
  - Undersized ductwork (TAB can balance, but if total airflow is low, duct may be too small)
  - Restricted valves (stuck, closed, or undersized)
  - Failed coils (plugged, air-bound, or undersized)
  - Insufficient fan/pump capacity
- TAB agency provides recommendations for deficiencies found

### Superintendent's Role in TAB

```
SUPER'S TAB COORDINATION CHECKLIST

BEFORE TAB:
□ Schedule TAB agency (minimum 2 weeks advance notice)
□ Verify all ductwork and piping is installed and connected
□ Verify all balancing dampers are installed and accessible
□ Verify all balancing valves are installed
□ Verify controls are operational (damper actuators, valve actuators)
□ Verify filters are installed (dirty filters skew readings)
□ Verify ceilings are open for access (or ceiling tiles can be removed)
□ Verify systems have been started up and are operational
□ Provide TAB agency with design airflow/water flow data (from MEP drawings)

DURING TAB:
□ Ensure TAB agency has access to all areas
□ Resolve access issues promptly (locked rooms, occupied spaces)
□ Coordinate with controls contractor (BAS adjustments needed during TAB)
□ Address deficiencies identified by TAB (leaking duct, stuck damper)

AFTER TAB:
□ Review TAB report for completeness
□ Distribute TAB report to CxA, MEP engineer, owner
□ Schedule re-balance if deficiencies were corrected
□ Incorporate TAB results into Cx documentation
```

---



## System Startup Procedures

### HVAC Startup

**RTU/AHU (Rooftop Unit / Air Handling Unit):**

```
RTU/AHU STARTUP PROCEDURE

PRE-START CHECKLIST:
□ Filters installed (correct type, correct direction)
□ Fan belts installed, proper tension, alignment checked
□ Bearings lubricated per manufacturer
□ Fan rotation check (bump motor, verify correct rotation)
□ All dampers operate freely (manually cycle OA, RA, MA dampers)
□ Damper actuators connected and addressed in BAS
□ Coils clean and undamaged
□ Condensate drain trapped and clear
□ Electrical connections tight, proper voltage confirmed
□ Controls wired and communicating with BAS
□ Access panels secured
□ Ductwork connected and sealed
□ No construction debris in unit (critical — debris damages fans/coils)

INITIAL START:
□ Verify rotation direction matches fan arrow
□ Measure motor amperage:
  Phase A: ___A  Phase B: ___A  Phase C: ___A
  FLA (nameplate): ___A  (actual must be < FLA)
□ Check vibration (hand feel for startup, vibration meter for Cx)
□ Verify all safety controls:
  - High static pressure cutout: tested / Pass / Fail
  - Freezestat (if applicable): tested / Pass / Fail
  - Smoke detector shutdown: tested / Pass / Fail
  - Filter differential pressure switch: tested / Pass / Fail

PERFORMANCE VERIFICATION:
□ Measure Supply Air Temperature: ___°F (design: ___°F)
□ Measure total airflow (with TAB or temporary traverse): ___CFM
□ Verify BAS communication: all points reading correctly
□ Run for minimum 4 hours, re-check amperage and vibration
```

**Chiller:**

```
CHILLER STARTUP PROCEDURE

PRE-START (by installing contractor):
□ Oil charge verified per manufacturer
□ Refrigerant charge verified per manufacturer
□ Condenser water flow verified (pump operational, valves open)
□ Chilled water flow verified (pump operational, valves open)
□ Flow switches operational and tested
□ Electrical connections verified, proper voltage
□ Controls wired and communicating
□ All safeties set per manufacturer

MANUFACTURER STARTUP (required for warranty):
→ Schedule manufacturer's factory-authorized startup technician
→ Minimum 2-3 weeks advance scheduling required
→ Contractor must have all pre-start items complete before tech arrives
→ Manufacturer tech performs:
  □ Verify oil and refrigerant charge
  □ Calibrate all safeties and controls
  □ Perform initial start and run
  □ Verify compressor operation (amps, pressures, oil pressure)
  □ Verify capacity (entering/leaving water temps)
  □ Calculate approach temperature
  □ Measure kW/ton at operating conditions
  □ Set up BAS communication
  □ Document startup in warranty log

PERFORMANCE LOG (record at startup and during Cx):
  Entering Chilled Water Temp: ___°F
  Leaving Chilled Water Temp: ___°F
  Design ΔT: ___°F   Actual ΔT: ___°F
  Entering Condenser Water Temp: ___°F
  Leaving Condenser Water Temp: ___°F
  Approach Temperature: ___°F
  kW/ton: ___ (design: ___)
```

**Boiler:**

```
BOILER STARTUP PROCEDURE

PRE-START:
□ Water treatment program in place (test water chemistry)
□ Expansion tank pre-charge pressure set per design
□ Safety relief valves tested (lift test)
□ Low water cutoff tested
□ Combustion air openings verified (size per code)
□ Flue/exhaust connected and proper materials
□ Gas piping pressure tested, gas valve operational
□ Electrical connections verified
□ Controls wired and communicating
□ System filled, air purged from all high points

FIRE-UP:
□ Burner adjustment by manufacturer tech or licensed burner tech
□ Flue gas analysis:
  CO: ___ppm (target: <100 ppm)
  CO2: ___% (target: per manufacturer)
  O2: ___% (target: per manufacturer)
  Stack temp: ___°F
  Combustion efficiency: ___%
□ Safety shutdown test:
  - High limit: trip at ___°F (design: ___°F)   Pass / Fail
  - Low water cutoff: trip verified   Pass / Fail
  - Flame failure: verified (interrupt gas, verify shutdown)   Pass / Fail

OPERATING LOG:
  Supply water temp: ___°F (design: ___°F)
  Return water temp: ___°F
  ΔT: ___°F
  Stack temp: ___°F
  System pressure: ___psi
  Combustion efficiency: ___%
```

**VRF (Variable Refrigerant Flow) Systems:**

```
VRF STARTUP PROCEDURE

PRE-START:
□ Refrigerant charge per manufacturer (based on piping length — field calculation required)
□ Oil level verified in outdoor unit(s)
□ Communication wiring verified between all indoor and outdoor units
□ Each indoor unit addressed in system controller
□ Condensate drains connected and tested
□ All piping brazed, pressure tested, and insulated
□ Electrical connections verified for all indoor and outdoor units
□ Controls interface wired and communicating

COMMISSIONING (by manufacturer's authorized technician):
□ Address all indoor units in system
□ Verify communication chain (outdoor → branch controller → indoor)
□ Test each indoor unit in each mode:
  - Cooling mode: verified   Pass / Fail
  - Heating mode: verified   Pass / Fail
  - Fan only: verified   Pass / Fail
  - Auto changeover: verified   Pass / Fail
□ Verify simultaneous heating and cooling (heat recovery models)
□ Refrigerant charge adjustment per actual piping lengths

PERFORMANCE:
□ Each indoor unit capacity at design conditions
□ Outdoor unit operating within spec (pressures, amps)
□ System COP/EER at operating conditions
```

### Electrical Energization

**Pre-Energization Testing:**

```
ELECTRICAL PRE-ENERGIZATION CHECKLIST

INSULATION RESISTANCE (MEGGER) TESTING:
□ Test all feeders and branch circuits before energization
□ Minimum acceptable reading: 1 MΩ per kV + 1 MΩ
  Example: 480V system → minimum 1.48 MΩ (use 2 MΩ as practical minimum)
□ Record all readings; re-test any below minimum
□ Test phase-to-phase and phase-to-ground

VISUAL INSPECTION:
□ All connections inspected — no loose lugs, no damaged insulation
□ Wire routing per code (proper bending radius, fill, support)
□ Panel directories completed and accurate
□ Equipment labels installed per design
□ All covers and dead fronts in place

TORQUE VERIFICATION:
□ All lugs and bus bar connections torqued per manufacturer specs
□ Record torque values on verification form
□ Use calibrated torque wrench (not impact driver)
□ Re-torque after initial energization and thermal cycling (30-day re-torque)

GROUNDING SYSTEM:
□ Ground resistance tested:
  General: < 25Ω per NEC (minimum acceptable)
  Sensitive equipment: < 5Ω (recommended for data, telecom, medical)
  Lightning protection: < 10Ω
□ Grounding electrode conductor connected and tested
□ Equipment grounding conductors continuous
□ Bonding jumpers installed per code
```

**Progressive Load Application:**

```
ENERGIZATION SEQUENCE — NEVER ENERGIZE EVERYTHING AT ONCE

Step 1: MAIN SWITCHGEAR
  □ Verify incoming utility voltage: A-B: ___V  B-C: ___V  A-C: ___V
  □ Close main breaker
  □ Verify voltage on main bus
  □ Check phase rotation

Step 2: DISTRIBUTION PANELS
  □ Close distribution breakers one at a time
  □ Verify voltage at each panel
  □ Check for any unusual sounds, smells, or heat

Step 3: BRANCH CIRCUITS
  □ Energize branch panels
  □ Spot-check voltage at representative receptacles
  □ Verify GFCI and AFCI operation

Step 4: EQUIPMENT CIRCUITS
  □ Energize equipment circuits one at a time
  □ Verify motor rotation before connecting loads
  □ Check amperage draw on each circuit
```

**Emergency/Standby Power Testing:**

```
EMERGENCY POWER TESTING

GENERATOR LOAD BANK TEST:
□ Connect resistive load bank
□ Test at 25% rated load — run 30 minutes, record kW, voltage, frequency
□ Test at 50% rated load — run 30 minutes, record
□ Test at 75% rated load — run 30 minutes, record
□ Test at 100% rated load — run minimum 2 hours continuously
□ Record: voltage (all phases), frequency, kW, fuel consumption, coolant temp, oil pressure
□ Verify performance meets NFPA 110 requirements

AUTOMATIC TRANSFER SWITCH (ATS) TEST:
□ Normal → Emergency transfer:
  - Simulate utility failure (open main breaker)
  - Generator starts within ___seconds (max 10 seconds for emergency, per NFPA 110)
  - ATS transfers load within ___seconds
  - Emergency circuits energized
  - Record transfer time: ___seconds
□ Emergency → Normal retransfer:
  - Restore utility power
  - ATS retransfers after time delay: ___minutes (typically 15-30 min)
  - Generator runs unloaded for cooldown: ___minutes
  - Generator shuts down
  - Record retransfer time

UPS BATTERY TEST:
□ Simulate utility failure with UPS on load
□ Verify UPS transfers to battery without interruption
□ Run on battery for rated runtime
□ Actual runtime at rated load: ___minutes (rated: ___minutes)
□ Verify charger restores battery after test
```

### Fire Pump Acceptance Testing

```
FIRE PUMP ACCEPTANCE TEST (per NFPA 20 and NFPA 25)

FLOW TEST PROCEDURE:
Test at three points on the pump curve:

1. NO-FLOW (CHURN) CONDITION:
   - Close all test header valves
   - Record churn pressure: ___psi
   - Acceptance: ≤ 140% of rated pressure
   - Rated pressure: ___psi × 140% = ___psi max

2. 100% RATED FLOW:
   - Open test header to achieve rated GPM
   - Record flow: ___GPM and pressure: ___psi
   - Acceptance: pressure at or above rated pressure

3. 150% RATED FLOW:
   - Open test header to achieve 150% of rated GPM
   - Record flow: ___GPM and pressure: ___psi
   - Acceptance: pressure ≥ 65% of rated pressure
   - Rated pressure × 65% = ___psi minimum

PUMP CURVE VERIFICATION:
- Plot three points on manufacturer's pump curve
- All points must fall on or above the rated curve within 95%
- If any point falls below: pump fails — investigate and retest

WEEKLY/MONTHLY/ANNUAL TEST SCHEDULE (per NFPA 25):
- Weekly: no-flow (churn) test — run pump, record suction/discharge pressure
- Monthly: not required (weekly covers)
- Annually: full flow test at three points (as above)

JOCKEY PUMP TESTING:
□ Verify start pressure: ___psi (pump starts when system pressure drops to this level)
□ Verify stop pressure: ___psi (pump stops when system pressure reaches this level)
□ Verify no short cycling (pump should not start/stop more than 6 times per hour)
□ Verify jockey pump maintains system pressure between fire pump starts
```

---



## Owner Training Program

### Training Requirements by System

| System | Trainer | Attendees | Duration |
|--------|---------|-----------|----------|
| HVAC (each system type) | Manufacturer rep + controls contractor | Owner's maintenance staff, facility manager | 4-8 hours per system |
| Fire alarm | Fire alarm contractor | Owner's maintenance staff, security | 2-4 hours |
| Plumbing (domestic, sanitary) | Plumbing contractor | Owner's maintenance staff | 1-2 hours |
| Electrical (switchgear, panels, lighting) | Electrical contractor | Owner's maintenance staff, facility manager | 2-4 hours |
| Elevator | Elevator contractor | Owner's maintenance staff, security | 2-4 hours |
| BAS/Controls | Controls contractor | Owner's maintenance staff, facility manager, energy manager | 8-16 hours (most complex) |
| Specialty systems (kitchen, medical, lab) | Specialty contractor or manufacturer | Owner's operators, maintenance staff | Per system requirements |

### Training Session Format

Each training session should follow this structure:

```
TRAINING SESSION STRUCTURE

1. CLASSROOM INSTRUCTION (30-60 min)
   - System overview: what it does, major components, design intent
   - System diagram review (point to P&ID or riser diagram)
   - Sequences of operation walkthrough
   - Safety precautions and lockout/tagout procedures

2. HANDS-ON EQUIPMENT WALKTHROUGH (60-120 min)
   - Walk to each piece of equipment
   - Identify components physically (this is the compressor, this is the expansion valve...)
   - Show access panels, filter locations, drain points
   - Demonstrate isolation valves, disconnects, emergency shutoffs

3. NORMAL OPERATIONS DEMONSTRATION (30-60 min)
   - Start system from cold start
   - Change setpoints from BAS and local thermostat
   - Demonstrate mode changes (heating ↔ cooling, occupied ↔ unoccupied)
   - Show how to read BAS graphics for this system

4. ALARM/FAULT RESPONSE PROCEDURES (30-60 min)
   - Common alarms and what they mean
   - How to acknowledge alarms at panel and BAS
   - Troubleshooting steps for common faults
   - When to call for service vs. what to handle in-house
   - Emergency shutdown procedures

5. MAINTENANCE PROCEDURES DEMONSTRATION (30-60 min)
   - Filter change (type, size, frequency, procedure)
   - Belt inspection and replacement
   - Lubrication points and schedule
   - Seasonal changeover procedures
   - Cleaning requirements (coils, condensate pans, strainers)

6. Q&A (15-30 min)
   - Open questions from attendees
   - Review any areas of confusion
   - Distribute contact information for future support
```

### Training Documentation

**Attendance Sign-In:**
- All owner's maintenance staff must sign attendance sheet
- Include: name, title, date, system trained on
- Retain copy in Cx documentation and provide copy to owner

**Video Recording:**
- Record every training session (requirement for LEED Enhanced Cx)
- Use tripod-mounted camera with good audio (lapel mic on instructor preferred)
- Camera follows instructor — show equipment being discussed
- Label each recording: system name, date, trainer name, duration
- Provide recordings to owner in digital format (USB drive and cloud upload)

**Training Materials:**
- Instructor provides printed training materials to each attendee
- Include: system diagrams, sequences of operation, maintenance schedules, emergency procedures
- Digital copies provided to owner (PDF format)
- File in O&M manual section for each system

**Equipment-Specific Quick Reference Cards:**
- One-page laminated cards for each major piece of equipment
- Include: equipment name/tag, location, normal operating parameters, common alarms, emergency shutdown, filter info, service contact
- Post at each piece of equipment
- Provide extras for owner's maintenance office

### Competency Verification

At the end of each training session, verify that the owner's staff can demonstrate:

```
COMPETENCY VERIFICATION CHECKLIST

□ Normal start/stop of the system
□ Setpoint adjustment (local and BAS)
□ Alarm acknowledgment and basic troubleshooting
□ Emergency shutdown procedure
□ Filter/belt change (physically demonstrate)
□ BAS navigation to system graphics
□ Identify major components on the equipment
□ Locate isolation valves and electrical disconnects
□ Describe when to call for professional service
```

### Training Scheduling

- **Minimum 2 weeks before substantial completion:** All training must be complete before the owner assumes operational responsibility
- **Repeat sessions:** If owner's staff changes before or shortly after occupancy, provide repeat training (contract should address this)
- **Recorded sessions:** Available for future reference and new staff onboarding
- **Seasonal training:** For systems with seasonal modes (heating/cooling changeover), schedule a follow-up training session at the opposite season (e.g., train in summer, follow up in winter for heating operation)
- **BAS training:** Often requires multiple sessions due to complexity — schedule initial training plus a follow-up 30 days after occupancy when staff has real questions from daily operation

---



## References

- NFPA 101: Life Safety Code (fire safety)
- NFPA 13: Sprinkler Systems
- NFPA 20: Standard for the Installation of Stationary Pumps for Fire Protection
- NFPA 25: Standard for the Inspection, Testing, and Maintenance of Water-Based Fire Protection Systems
- NFPA 110: Standard for Emergency and Standby Power Systems
- AIA G702/G703: Application and Certificate for Payment
- CSI MasterFormat: Sections related to commissioning and closeout
- ASHRAE Guideline 0: The Commissioning Process
- ASHRAE Standard 111: Measurement, Testing, Adjusting, and Balancing of Building HVAC Systems
- AACE International Recommended Practice 29R-03: Forensic Schedule Analysis
- AABC National Standards for Testing and Balancing
- NEBB Procedural Standards for Testing, Adjusting, and Balancing
- State/Local Building Codes: Authority Having Jurisdiction (AHJ) requirements

## Warranty Tracking

### Warranty Types and Coverage

**Standard Construction Warranty:**
- Typical duration: 1 year from date of substantial completion
- Contractor responsible for defects in materials and workmanship
- Owner must report defects within warranty period
- Contractor required to repair or replace defective items

**Extended Warranties by System:**
- Roofing: 15-30 years (manufacturer material defect warranty)
- Waterproofing: 5-10 years (manufacturer and contractor joint responsibility)
- Windows and doors: 10 years (manufacturer warranty)
- HVAC equipment: 5-10 years (manufacturer parts warranty)
- Plumbing fixtures: 5 years (manufacturer warranty)
- Electrical equipment: varies by type
- Specialty systems: per equipment manufacturer

### Warranty Management

**Warranty Expiration Alerts:**
- 30-day warning before expiration
- 7-day critical warning before expiration
- Final walkthrough inspection recommended before 1-year mark

**Warranty Claim Documentation Requirements:**
- Detailed description of defect with photographs
- Date defect was discovered
- Description of impact on building operation
- Contractor or manufacturer response required within specified timeframe
- Repair or replacement completed before warranty expiration

**Warranty Tracking Data:**
- Warranty start date (typically substantial completion date)
- Warranty expiration date
- Coverage limits and exclusions
- Claim contact information (manufacturer, contractor, warranty administrator)
- Claims history and status



## Integration with Other Skills

- **Punch List Integration:** Reads from `punch-list.json` for completion status and tracks punch items to closeout
- **Inspection Integration:** Reads from `inspection-log.json` for final inspection results and documentation
- **Morning Brief Integration:** Surfaces closeout deadlines and commissioning schedule to daily briefing
- **Dashboard Integration:** Displays closeout completion percentage by category, outstanding items, and critical path items
- **Data Storage:** All data stored in `closeout-data.json` file in `folder_mapping.ai_output` directory



## ASHRAE Guideline 0 Commissioning Process

### Commissioning Process Overview

ASHRAE Guideline 0 defines commissioning (Cx) as a quality-focused process for verifying and documenting that building systems are planned, designed, installed, tested, operated, and maintained to meet the Owner's Project Requirements (OPR). The process spans the entire project lifecycle:

```
COMMISSIONING PROCESS PHASES

Pre-Design ──→ Design ──→ Construction ──→ Acceptance ──→ Post-Acceptance
    │              │            │               │               │
    ▼              ▼            ▼               ▼               ▼
  Develop        Review      Verify          Functional      Seasonal
  OPR & BOD     design for   installation    performance     testing &
  Select CxA    Cx-ability   quality         testing         warranty
  Develop       Update Cx    Pre-functional  Systems         review
  Cx plan       plan         checklists      turnover        Lessons
                Write FPT    Startup                         learned
                procedures   verification
```

### Key Commissioning Documents

**Owner's Project Requirements (OPR):**
- Written document defining the owner's expectations for the building
- Includes functional requirements, performance criteria, environmental goals, energy targets
- Created during pre-design, updated through design
- Serves as the benchmark against which all Cx testing is measured
- Must be approved by the owner before design proceeds

**Basis of Design (BOD):**
- Written document by the design team explaining how the design meets the OPR
- Includes system descriptions, design assumptions, standards applied
- References specific equipment selections and performance criteria
- Updated as design evolves
- CxA reviews BOD against OPR for alignment

**Commissioning Plan:**
- Master plan for all Cx activities across all phases
- Includes: scope, schedule, roles/responsibilities, systems to be commissioned, testing approach
- Developed in pre-design, refined through design, finalized before construction
- Updated as conditions change during construction

**Commissioning Specification:**
- Section 01 91 00 (General Commissioning Requirements) in project specifications
- Defines contractor responsibilities for Cx support
- Includes: pre-functional checklist requirements, startup documentation, FPT participation, deficiency correction
- References Cx plan and FPT procedures
- All trades must understand their Cx obligations

### CxA (Commissioning Authority) Role

The Commissioning Authority is the individual or firm responsible for leading, planning, and coordinating the commissioning process.

**Independence Requirements:**
- CxA must be independent of the design and construction teams
- Cannot be the installing contractor or a subcontractor of the installing contractor
- For LEED Enhanced Commissioning, CxA must be engaged by the owner (not the contractor)
- CxA reports directly to the owner

**CxA Responsibilities:**
- Develops the Commissioning Plan
- Reviews design documents for Cx-ability and OPR compliance
- Writes all Functional Performance Test (FPT) procedures
- Reviews contractor submittals for Cx-related equipment
- Develops and manages pre-functional checklists
- Witnesses startup of commissioned systems
- Executes or witnesses all FPTs
- Documents all Cx findings in the issues log
- Compiles the final Cx report
- Participates in owner training verification

### Construction-Phase Cx Activities

**Cx Plan Review and Updates:**
- At construction kickoff, CxA presents Cx plan to all trades
- Cx schedule integrated into master CPM schedule
- Update plan as construction conditions change (phasing, sequence, substitutions)

**Submittal Review by CxA:**
- CxA reviews submittals for equipment being commissioned
- Focus: does submitted equipment meet OPR and BOD performance criteria?
- CxA comments are advisory (architect retains approval authority)
- Flag any equipment substitutions that may impact Cx testing

**Pre-Functional Checklists:**
- Completed by installing contractor, verified by CxA
- Must be signed off BEFORE functional testing begins
- Verify: correct installation per plans and specs, proper connections, labeling, accessibility
- Examples: ductwork connected and sealed, piping flushed and pressure-tested, controls wired and addressed, filters installed

**Startup Verification:**
- CxA witnesses or verifies startup of commissioned equipment
- Contractor performs startup per manufacturer procedures
- CxA confirms: rotation correct, vibration acceptable, no alarms, basic operation verified
- Startup report filed before FPT scheduling

**Functional Performance Testing (FPT):**
- See dedicated FPT section below for detailed procedures
- CxA writes procedures, contractor executes, CxA witnesses

**Systems Manual Development:**
- Comprehensive document describing each commissioned system
- Includes: system narrative, sequences of operation, maintenance schedules, emergency procedures
- Goes beyond O&M manuals — systems manual is a "how to operate the building" guide
- CxA oversees development, contractor provides content

**O&M Manual Review:**
- CxA reviews O&M manuals for completeness and accuracy
- Verify: correct equipment data, maintenance schedules match manufacturer requirements
- Flag missing information, incorrect model numbers, or generic (non-project-specific) content

**Training Plan Execution:**
- CxA reviews training plan for adequacy
- Verifies training is delivered per plan
- May attend training sessions to verify quality
- See Owner Training Program section below for details

### Issues Log Management

The Cx issues log is the central tracking document for all commissioning findings.

**Issue Log Fields:**
```
COMMISSIONING ISSUES LOG

Issue #: [sequential number]
Date Identified: [date]
System: [HVAC, Plumbing, Electrical, Fire Protection, Controls, Envelope]
Location: [building area, floor, room]
Description: [detailed description of the finding]
Priority: [Critical / Major / Minor]
  Critical: System cannot function, safety issue, or code violation
  Major: System functions but not per design intent, performance impact
  Minor: Cosmetic, labeling, documentation issue
Responsible Party: [contractor, subcontractor, design team]
Resolution Required By: [date]
Resolution Description: [how it was fixed]
Verified By: [CxA initials and date]
Status: [Open / In Progress / Resolved / Closed]
```

**Issue Resolution Workflow:**
1. CxA identifies issue during inspection, pre-functional check, or FPT
2. Issue logged with full documentation (photos, measurements, test data)
3. Responsible party notified (typically through superintendent)
4. Resolution deadline assigned based on priority
5. Contractor corrects the deficiency
6. CxA verifies correction (re-inspection or re-test)
7. Issue closed with documentation of resolution

### Enhanced Commissioning for LEED

**EAp1 — Fundamental Commissioning (Prerequisite for all LEED certifications):**
- CxA with documented Cx experience
- Review OPR and BOD
- Develop and execute Cx plan for energy-related systems
- Verify installation and performance of commissioned systems
- Complete Cx report

**EAc1 — Enhanced Commissioning (Credits):**
Enhanced Cx adds the following requirements beyond fundamental:
- CxA involved during **design phase** (not just construction)
- CxA conducts **design document review** at each design phase (SD, DD, CD)
- CxA reviews contractor **submittals** for Cx-related equipment
- **Post-occupancy review** at 10 months after substantial completion
- Develop a **systems manual** (beyond standard O&M manuals)
- Verify **operator training** delivery and adequacy

### Envelope Commissioning (LEED Enhanced)

For LEED Enhanced Commissioning, the building envelope is included in the Cx scope:

- **Blower door testing:** Whole-building air leakage test per ASTM E779 or per-floor testing per ASTM E3158. Target: varies by climate zone and standard (Army Corps requires < 0.25 CFM75/SF of envelope)
- **Thermal imaging:** Infrared scan of building envelope during heating season, identify thermal bridges, insulation voids, air leakage paths
- **Water penetration testing:** Per ASTM E1105 (field test) or AAMA 501.2 (spray rack test) at representative window/curtain wall locations
- **Air barrier continuity verification:** Visual inspection and testing at transitions (wall-to-roof, wall-to-foundation, wall-to-window), verify sealant and membrane continuity

### Monitoring-Based Commissioning (MBCx)

MBCx extends commissioning beyond the acceptance phase into ongoing operations:

- **Permanent sensors:** Install sensors for ongoing performance monitoring (not just temporary test instruments)
- **BAS trending:** Configure Building Automation System to continuously log performance data
- **Automated fault detection:** Software algorithms that identify when systems deviate from expected performance
- **Continuous performance verification:** Compare actual operation to OPR on an ongoing basis
- **Typical MBCx duration:** 1-3 years of continuous monitoring after acceptance

---


---

> **Extended reference**: Detailed examples, templates, scoring rubrics, and best practices are in `references/skill-detail.md`.


