# Runway Integrity Validation through Soil Moisture Measurements using sUAS

## Document Metadata
- **Type:** Technical & Safety Review Board (TRB/SRB) Briefing
- **Client/Agency:** U.S. Air Force / AFWERX / AFRL
- **Program/Solicitation:** AFVentures - Open Topic SBIR Phase II
- **Date:** 10 December 2024
- **AFRL Tracking Number:** RG-2023-48
- **BST Products/Systems Referenced:** E2 (rotary-wing UAS), SwiftCore (autopilot software), SwiftPilot (autopilot), SwiftTab (tablet GCS), Soil Moisture Sensor Suite
- **Key Personnel:** 
  - Jack Elston (CEO & Principal Investigator, PIC)
  - Dan Prendergast (Software Engineer & Test Lead)
  - Dr. Maciej Stachura (Founder & CTO, VO)

---

## Executive Summary

Black Swift Technologies proposes to validate a novel soil moisture sensor payload integrated with their E2 quadcopter to assess runway integrity by measuring surface soil moisture and calculating bearing capacity. The system will conduct 15 flights (~8 hours total) across two test locations in Colorado, collecting radiometer, NDVI, and thermal sensor data correlated with ground-truth cone penetrometer measurements to develop and verify analytical and empirical models for predicting soil load-bearing capacity within 3% accuracy.

---

## Technical Approach

### Overall Methodology
1. **Data Collection Phase:** Fly area coverage patterns at ~50 ft AGL, 5-6 knots airspeed to collect sensor data
2. **Ground Truth Correlation:** Simultaneously collect manual soil moisture (conductivity probe) and soil integrity (cone penetrometer) measurements ±30 minutes of airborne measurements
3. **Analytical Verification:** Validate ability to calculate soil integrity from surface soil moisture using analytical models
4. **Empirical Model Development:** Develop and verify alternate empirical models to predict soil integrity from sensor measurements

### Test Objectives
- **Objective 1:** Verify ability to calculate soil integrity from surface soil moisture using analytical models across 3 soil types at 4 different moisture levels
- **Objective 2:** Develop and verify empirical models across at least 8 soil types (4%-40% sand content) at 4 moisture levels

### Data Collection Requirements
- **Airborne Sensor Data:** Time, lat/long, altitude, roll/pitch/yaw, thermal measurement, NDVI measurement, radiometer brightness temperature
- **Ground Truth Data:** Date, time, lat/long, soil moisture measurement (%), soil integrity measurement (CBR/RCI), soil type

### Acceptance Criteria
- Calculated soil integrity must be within **3% of cone penetrometer measurements**
- Empirical model predictions must be within **3% of measured soil integrity**

---

## Products & Capabilities Described

### E2 Quadcopter (Airframe)
- **Type:** Group 2, Rotary-wing UAS
- **Dimensions:** 57" diagonal
- **MGTOW:** 25 lbs
- **Max Payload:** 4.5 lbs
- **Flight History:** 4,260 hours, previous operation proven
- **Mishap History:** 2 mishaps (last in 2020); both resolved with design changes
- **Manufacturer:** Black Swift Technologies
- **Serial Number:** E20006
- **Registration:** FA3HY4NTLH (FAA registered)
- **Cost:** $25,000 (vehicle + payload)
- **Unmodified:** No airframe modifications for this test

### SwiftCore Autopilot & SwiftPilot
- **Current Build:** #461 (software version 3.2.8)
- **Capabilities:** 
  - Waypoint-based autonomous flight with real-time position plotting
  - Manual override via RC handset (secondary control link)
  - Lost-link automatic return-to-home with autonomous landing
  - Altitude geo-fencing; horizontal boundary visualization on tablet
- **Software Management:** Version control via GitLab with Git Flow methodology, automated testing via Jenkins
- **Flight Control Logic:** Independent of command link; automatically executes lost-link profile if both datalinks fail

### SwiftTab (Ground Control Station)
- **Platform:** Android tablet with WiFi interface
- **Primary Function:** Waypoint mission planning and execution, real-time telemetry display, boundary visualization
- **Secondary GCS:** Futaba RC handset for manual direct control

### Soil Moisture Sensor Suite
- **Integration:** Mounted on E2 payload interface
- **Measurement Depth:** Top 10 cm of soil
- **Output:** Soil moisture percentage (%), can be converted to load-bearing capacity via models
- **Sensor Components:**
  - **L-band Radiometer:** Measures brightness temperature (L-band energy) in degrees Kelvin; calibrated against known-value targets (standing water, reflective tarps); qualification in progress
  - **NDVI Sensor:** Measures vegetation index (health/quantity); previously validated against factory-calibrated Micasense Altum during prior project flight testing; good performance with acceptable bias
  - **IR Thermal Sensor:** Measures ground surface temperature (degrees Celsius); validated against Fieldscope TDR 350 reference with ±5°C accuracy
- **Power:** Supplied from aircraft main battery through payload interface; monitored with low-battery warnings; flights terminate with 15-minute reserve
- **Signal Processing:** 
  - Onboard filtering and averaging of raw sensor data within footprints
  - Data logged on back-end processor board
  - Post-flight processing calculates soil moisture and soil integrity (CBR/RCI)
- **EMI/EMC:** Passive sensors; shielded circuitry to prevent interference with flight control
- **No Flight Control Coupling:** Sensor suite does not interface with navigation or flight control algorithms

---

## Use Cases & Applications

### Primary Use Case: Runway Integrity Assessment
- **Application:** Assess pavement/soil load-bearing capacity and integrity for military runway operations
- **Operational Context:** Enables rapid assessment of runway usability after degradation events (rain, flooding, traffic)
- **Benefit:** Non-destructive, airborne method to map runway integrity across large areas without ground team penetrometer surveys

### Test Locations
1. **Sunny Slope Sod Farm, Longmont, CO**
   - Private subcontracted land
   - 7 sorties / ~3.5 flight hours
   - Test area: ~2600' x 1200'
   - Operation altitude: <50 ft AGL
   
2. **McIntosh Lake Nature Area, Longmont, CO**
   - Public open space
   - 8 sorties / ~4 flight hours
   - Test areas: Multiple sections (1800' x 1500', 750' x 1500')
   - Operation altitude: <50 ft AGL

### Test Sequencing by Soil Moisture Condition
- Sorties timed to capture dry (<10%), wet (>30%), and intermediate (10-30%) soil moisture states
- Data collection across first rainfall event, follow-up measurements at +1 and +2 days post-rain
- Supplemental flights in January for extended seasonal variation

---

## Key Results / Test Status

### Current Status (as of 10 December 2024)
- **Test Plan:** Version 4.1 finalized (as of 5 Nov 2024)
- **Regulatory Approvals:**
  - Cyber review: **Complete** (no AFRL RMF requirements, per 5 Dec 2024)
  - Environmental: **Complete for test location 1** (AF Form 813 approved as CatEx 24, 22 Nov 2024)
  - Environmental: **Pending for test location 2** (to be resubmitted when location confirmed)
  - Spectrum Management: All radios/emitters FCC compliant
  - Proper Use Memorandum: N/A per FTPM determination

### Airworthiness Assessment
- **Status:** Preliminary assessment underway
- **Aircraft Owner/Operator:** Black Swift Technologies (COCO)
- **Delegated Technical Authority:** Matt Alsleben (AFWERX)
- **Expected Determination:** Civil Aircraft Operation (CAO)
- **CAO Letter:** To be prepared upon CAO determination

### Payload Qualification Results (Completed)
- **NDVI Sensor:** Validated against Micasense Altum reference; very good match with slight acceptable bias
- **Thermal Sensor:** Validated against Fieldscope TDR 350 reference; bias within camera error specification (±5°C)
- **Radiometer:** Calibration against ground targets (3% / 33% / 85% reflectance standards); Red channel shows good performance; NIR requires further calibration

### Technical Review Board Assessment
The briefing was presented to the TRB/SRB on 10 December 2024 for risk assessment and approval of test execution.

---

## Notable Details

### Aircraft Operability & History
- **Previous Flight Experience:** E2 has logged 4,260 operational flight hours across multiple projects
- **Pilot Qualifications:**
  - Jack Elston (PIC): Part 107 Remote Pilot Certificate; 620+ UAS hours, 1,200+ missions
  - Maciej Stachura (VO): Part 107 Remote Pilot Certificate + Private Pilot Certificate; 280+ UAS hours, 400+ manned aircraft hours
- **Insurance:** Global Aerospace liability policy
- **Backup Pilot:** Another Part 107-certified operator available if primary unavailable

### Safety & Contingency Planning
- **Lost Link Procedures:** Dual independent control links (tablet + RC handset); if both fail, aircraft automatically returns to pre-programmed landing point
- **Loss of Sight:** PIC sends aircraft to landing point via tablet
- **Collision Avoidance:** Maintained VLOS with visual scan; Part 107 compliant operations
- **Boundary Management:**
  - Operations Box: Autonomous flight within geo-fenced area
  - Caution Boundary: PIC takes manual control with RC handset to return to ops box
  - Kill Boundary: PIC terminates both datalinks; E2 executes lost-link profile and lands automatically
  - Kill boundary calculated with worst-case drift (10 kt airspeed + 10 kt wind + 4 sec reaction time = 50m / 164 ft buffer)

### Weather Operating Limits
- **Day operations only**
- **Ceiling:** ≥1000 ft AGL
- **Winds:** <10 knots (including gusts)
- **Precipitation:** None
- **Visibility:** ≥3 statute miles

### Risk Identification & Mitigation
**Two Primary THAs:**

1. **THA #1 - Loss of Control**
   - Cause: CG shift / flight dynamics from soil moisture sensor
   - Severity: 3 (Marginal) | Probability: C (Occasional)
   - Mitigations: Flight controller stability independent of CG; preflight controllability checks; practice flights in small area; benign flight conditions (low speed/altitude)
   - Corrective Action: Take manual control via handset

2. **THA #2 - Loss of Command Link**
   - Cause: EMI from new sensor
   - Severity: 4 (Negligible) | Probability: D (Remote)
   - Mitigations: Preflight control checks with sensor powered; aircraft stability independent of command link; auto-landing after link timeout
   - Corrective Action: Take manual control via handset

**Additional Hazards Documented** (12 total in hazard analysis):
- Lithium battery fire/explosion
- Loss of electrical power
- Structural failure
- Loss of vehicle position (GPS)
- Loss of propulsion
- Autopilot failure
- Loss of handset/tablet
- Airspace violation
- Bird strike
- Mid-air collision

All hazards have defined mitigations and corrective actions.

### Software & Hardware Quality Assurance
- **Software:** GitLab version control with Git Flow methodology; Jenkins automated build/testing; "Main" branch = operational version
- **Hardware:** Onshape CAD with version control; Asana project management for design changes; versioned BOMs and assembly guides; quality control checks of all subsystems
- **Sensor Suite:** RF characteristics simulated with Ansys HFSS; bench testing with known-value targets; integration testing for EMI/RF noise

### Spectrum & Communications
- **Primary Datalink:** Microhard P900 Transceiver (902-