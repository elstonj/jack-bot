# S4 UAS RCC 323-99 Questionnaire

## Document Metadata
- **Type:** Range Safety Review Questionnaire / Technical Specification Document
- **Client/Agency:** DIU (Defense Innovation Unit) / NAVAIR, via KrateoSky
- **Program/Solicitation:** DIU/NAVAIR LC-ISR (Low-Cost ISR) Gauntlet, May-June 2027
- **Date:** 16 November 2026 (Rev 0 DRAFT)
- **BST Products/Systems Referenced:** S4 UAS, SwiftCore, SwiftPilot, SwiftTab, SwiftStation, S2, S0-AD, Chilli test bed
- **Key Personnel:** Jack Elston (last editor), BST RF lead, aerodynamicist, mission planners
- **Status:** Draft questionnaire responses; multiple items marked as "TBC" (to be confirmed) or "in preparation"

## Executive Summary
This document is Black Swift Technologies' responses to a formal Range Safety Review questionnaire for the S4 unmanned aircraft system, proposed for the DIU/NAVAIR Low-Cost ISR Gauntlet evaluation in May-June 2027. The S4 is a long-endurance (12-hour objective), tactical ISR platform designed for autonomous BVLOS operations from land-based sites with pneumatic launch and autonomous belly landing recovery.

## Technical Approach

### Aircraft Design & Configuration
- **Airframe:** 4.5 m wingspan (14.8 ft), ~1.9 m length (6.2 ft), ~0.81 m² wing area
- **Weight:** Empty ~7.0 kg (15.5 lb); Maximum Takeoff Weight 18.1 kg (40.0 lb)
- **Propulsion:** Two electric motors (dual-redundant); propellers fold for glide; Amprius SA03 lithium-ion batteries (two 6S8P packs, 1,932 Wh each, 3,865 Wh total per aircraft)
- **Performance:**
  - Service ceiling: ~15,000 ft MSL (est., not yet flight-demonstrated)
  - Endurance: 12 h design objective (40 lb, loiter ~41 kt, sea level, 500 Wh/kg cells); ~9 h with current 400 Wh/kg cells
  - Still-air range: 380–500 nm at loiter speed
  - Operational radius: ≤50 nm (limited by C2 line-of-sight on P400)
  - Glide ratio: ~20:1 (best glide, propellers folded); ~3.3 nm per 1,000 ft AGL
  - Minimum sink: ~200 fpm (1 m/s)
  - Loiter speed: 41–45 kt (21–23 m/s)
  - Cruise speed: ~50 kt (26 m/s)
  - Max speed: ~64 kt (33 m/s) level flight
  - Never-exceed speed: ~74 kt (38 m/s, TBV against wing structural design)
  - Stall speed: ~32 kt clean at MTOW, sea level
  - Rate of climb: ~600 fpm at MTOW (estimated)
  - Rate of descent: Normal 400–800 fpm (autopilot-limited); up to ~1,500 fpm with flaps and motors off

### Launch & Recovery
- **Launch:** Pneumatic rail launcher; no personnel within 30° cone forward of rail to 300 ft or within 25 ft while pressurized
- **Recovery:** Autonomous belly landing on designated landing site; no parachute
- **Landing approach:** Autonomous landing plan with landing orbit, approach, and abort orbit options

### Flight Control & Autonomy
- **Autopilot:** SwiftPilot (STM32H743 microcontroller, FreeRTOS RTOS); holds all flight authority; flies missions autonomously
- **Flight-critical software:** State estimation, guidance, control, actuator output, failsafes, radio ownership run on SwiftPilot
- **Non-critical software:** Payload processing and ATR (Automatic Target Recognition) run on companion computer via "Safe Sandbox" (envelope-checked, autopilot-supervised requests only)
- **Avionics pedigree:** SwiftCore identical to S0-AD (120+ delivered to NOAA; operational in hurricanes since 2021; SOCOM airdrops 2026)

### Navigation & Sensing
- **Position:** u-blox ZED-F9P GNSS (dual-antenna capable; primary source); dead-reckoning fallback (airspeed + heading + wind estimate) on GNSS loss
- **Attitude:** Dual ICM-20948 IMUs with EKF fusion; failover to secondary IMU on fault
- **Heading:** RM3100 magnetometer + GNSS course/velocity in EKF
- **Altitude:** MS5611 barometer (primary); GNSS altitude fallback
- **Airspeed:** MS4515DO differential pressure via pitot-static probe; GNSS groundspeed + wind estimate fallback on loss
- **Failsafe behaviors:** Sensor loss alerts operator; on loss of pressure altitude → GNSS altitude; on loss of pitot → GNSS groundspeed with conservative margins; dual IMU redundancy

### Command & Control (C2)
- **Primary C2:** Microhard P400 400 MHz frequency-hopping spread-spectrum (FHSS) link (410–480 MHz, exact channels TBD by range spectrum manager), 2 W ERP, latency <1 s
  - Uplink: GCS to aircraft
  - Downlink: Telemetry (position, attitude, airspeed, altitude, battery state, link quality, alarms)
  - Range: 50 nm planned operational radius; link budget analysis pending site geometry and GCS antenna
  - Ground range test before flight planned
  - Fade margin target: 10 dB minimum at max planned range (TBV)
  - Features: Unique network ID, optional AES-128 encryption, heartbeat/packet timeout detection, frequency hopping reduces narrowband RFI susceptibility, FEC, 32-bit CRC, ARQ retransmission
  
- **Backup C2:** Iridium 9603N SBD (satellite) transceiver
  - Independent L-band antenna (1616–1626.5 MHz)
  - Global coverage (not dependent on line-of-sight)
  - Data rate: Low (status reports, limited commands)
  - Latency: 10–60 s
  - Command authentication: Provisioned gateway IMEI only; message framing and checksums
  - Carrier board to be refreshed for S4
  
- **Tertiary C2 (Flight Test Only):** Futaba 2.4 GHz R/C link; manual backup; requires visual line-of-sight (<1 km)

- **Remote ID:** Dronetag unit with independent GNSS receiver; broadcasts via Bluetooth (~1.5 km) and LTE-M (cellular); reports position independently to network

### Payload & Sensor Subsystems
- **Primary payload:** Stabilized EO/IR gimbal (Full Motion Video, FMV) or fixed EO/IR camera with onboard Automatic Target Recognition (ATR)
- **Video downlink:** Microhard pMDDL2280 (2.2–2.8 GHz), ~30 nm est. range (S3 target 60 km); separate from C2
- **Frequencies:** Need assignment through range spectrum manager (no existing JF-12); commercial licenses for Iridium, Remote ID, 2.4 GHz R/C

### Crew & Operations
- **Crew (2–3 personnel):**
  - Pilot in Command (PIC) / Air Vehicle Operator (AVO): Commands and monitors via SwiftTab; reviews position, attitude, airspeed, altitude, battery state, link quality, alarms
  - Payload/Mission Operator: Operates EO/IR sensor and reports; may be same person during long loiter
  - Launch & Recovery Technician / Visual Observer: Launcher operation, preflight, battery handling, landing-lane clearing, visual scan near launch and recovery
  
- **Operator qualifications:** FAA Part 14 CFR 107 Remote Pilot Certificate (verify currency); BST SwiftCore/SwiftTab type training (~0.5 day for routine ops + emergency-procedure drills in simulator); PIC will have recent S4 or S-series flight time from early-2027 contractor flight test
  
- **Ground Control Stations:**
  - **SwiftTab:** Tablet running mission planning and telemetry display; shows position, attitude, airspeed, altitude, battery state, link quality, alarms; allows operator commands and in-flight retasking
  - **SwiftStation:** Desktop/laptop running GCS daemon; UPS battery + external field power; maintains telemetry and command continuity; UPS powers primary P400 ground radio
  - Iridium backup accessible from any internet-connected computer or phone, independent of SwiftStation power

### Hazardous Materials & Safety
- **Energy storage:** Two lithium-ion packs per aircraft (3,865 Wh total; UN 38.3 certified cells)
- **Fire hazard:** Crash with pack crush/penetration can cause thermal runaway and fire
  - **Mitigations:** Packs in enclosed protective compartment, separately fused, crash site treated as battery hazard (approach upwind, 30-min observation, damaged packs isolated in fireproof container)
  - Ground safety: Water/AVD extinguishers and battery fire container at launch site
  - Operational restriction: No operations over flammable vegetation during high fire danger without range approval
- **No fuel, toxic materials, ordnance, or radioactive sources**
- **Composite structure:** Carbon and glass fiber
- **Ground equipment:** Pneumatic launcher pressure vessel

---

## Products & Capabilities Described

### SwiftCore Avionics Suite
- **What it is:** Integrated avionics and flight control system; core boards identical to S0-AD (proven in NOAA with 120+ aircraft; operational in hurricanes since 2021; SOCOM airdrops 2026)
- **SwiftPilot autopilot:** STM32H743 microcontroller running FreeRTOS; holds all flight authority; executes autonomous missions
- **SwiftTab:** Ground control tablet interface for operator commands, mission planning, and real-time telemetry display
- **SwiftStation:** Ground control station software (daemon) running on desktop/laptop with UPS backup power
- **Features:**
  - Autonomous climb, transit, loiter/orbit, return, and belly landing
  - Lost-link return mode with configurable lost-comm point and loiter time
  - Dead-reckoning navigation fallback on GNSS loss
  - Multi-sensor fusion (dual IMU, magnetometer, barometer, airspeed, GNSS)
  - Sensor-failure detection with mode fallback and operator alerts
  - Dual-redundant motor control with remote engine kill
  - Safe Sandbox: Payload/ATR commands envelope-checked and autopilot-supervised
  - Configuration management with version control (Autopilot 3.3.0 current)
  - JSBSim software-in-the-loop simulator with sensor-failure injection
  - QC flight testing before release
  - Telemetry logging on aircraft and GCS
  - Battery state monitoring (voltage, current, integrated watt-hours) with low-voltage and energy-reserve warnings

### S4 UAS (Primary Product of This Document)
- **What it is:** New tactical ISR platform built from flight-proven S-series elements
  - Airframe: 4.5 m wingspan, 18.1 kg MTOW, carbon-tube fuselage (derived from BST designs, not 3D-printed)
  - 12-hour design objective endurance
  - Pneumatic rail launch, autonomous belly landing recovery
  - Stabilized EO/IR gimbal (FMV) or fixed EO/IR camera with onboard ATR
  
- **Proposed use in Gauntlet:** Low-cost, long-endurance tactical ISR platform for DIU/NAVAIR evaluation (May–June 2027)
- **Heritage elements:**
  - Avionics: SwiftCore/SwiftPilot identical to S0-AD (NOAA, 120+ aircraft)
  - Propulsion approach: Chilli long-endurance test bed (2025–26, 25–40 lb GTOW, multiple flights for By Light)
  - Wing design: 4.5 m high-performance design by same aerodynamicist
  - S2 heritage: 100+ flights in Greenland/Arctic and volcanic plumes
  
- **Performance claims (Estimates pending flight test):**
  - Service ceiling: ~15,000 ft MSL
  - Endurance: 12 h (design objective, 500 Wh/kg cells); ~9 h (current 400 Wh/kg cells)
  - Still-air range: 380–500 nm
  - Operational radius: ≤50 nm (C2 line-of-sight limit)
  - Glide: ~20:1, ~3.3 nm per 1,000 ft
  - Loiter speed: 41–45 kt

### S2 UAS
- **What it is:** Earlier-generation long-endurance tactical ISR platform
- **Flight history:** 100+ flights in Greenland/Arctic and volcanic plumes
- **Use in S4 context:** Pedigree and design precedent for S4 (wing aerodynamicist, SwiftCore heritage)

### S0-AD / S0 Platform
- **What it is:** NOAA-qualified UAS with SwiftCore avionics
- **Deployment history:** 120+ aircraft delivered to NOAA; operational in hurricanes since 2021; SOCOM airdrops 2026
- **Use in S4 context:** Proves SwiftCore reliability; avionics baseline for S4

### Chilli Long-Endurance Test Bed
- **What it is:** 2025–26 development platform built for By Light
- **Specifications:** 25–40 lb GTOW; dual-motor long-endurance configuration
- **Use in S4 context:** Validates S4 propulsion approach and long-endurance performance envelope

---

## Use Cases & Applications

### Primary Use Case: DIU/NAVAIR Low-Cost ISR Gauntlet (May–June 2027)
- **Context:** Competitive evaluation of low-cost, long-endurance tactical ISR platforms
- **Mission type:** Autonomous BVLOS long-endurance loiter with EO/IR payload
- **Operational scope:**
  - Launch from fixed land-based pneumatic rail
  - Autonomous climb and transit to operating area
  - Loiter/orbit or area search with stabilized EO/IR gimbal (FMV) or fixed camera with ATR
  - Return and autonomous belly landing at designated recovery site
  - Single aircraft per GCS
  - Planned for restricted/warning airspace (exclusive range airspace)
  - 2–3-person crew

### Tactical ISR Applications (Implicit from Design)
- Area surveillance and search
- Full Motion Video (FMV) collection from stabilized gimbal
- Automatic Target Recognition (ATR) on fixed payload
- Long-dwell persistent ISR (12-hour endurance objective)
- Low-cost, attritable platform (suitable for high-risk or austere environments)

### Environmental Monitoring (From Heritage Platforms)
- **Hurricane sampling:** S0-AD operational in hurricanes since 2021 (NOAA heritage)
- **Volcanic plume monitoring:** S2 100+ flights in volcanic operations
- **Arctic operations:** S2 100+ flights in Greenland/Arctic

---

## Key Results / Findings from Safety Review Questionnaire

This is a **questionnaire response document**, not a results report. BST's responses to Range Safety Review questions reveal the following key findings and open items:

### Safety Analysis Status
- **No formal MIL-STD-882E hazard analysis exists yet.** BST committed to provide:
  - Preliminary Hazard Analysis (PHA)
  - Subsystem FMEA (propulsion, power, C2, navigation, flight controls, launcher)
  - Deliverable date: To be confirmed

- **No quantitative PLOAdc/PCumCat analysis performed.** BST noted this is a low-cost, attritable sUAS and offered qualitative risk assessment based on flight history of common avionics and subsystems.

- **No formal software safety program (DO-178C or MIL-STD-882E software assurance).** SwiftCore developed under BST configuration control with code review, SIL simulator with sensor-failure injection, and QC flight testing.

### Loss-of-Control Mitigations
1. **Loss of C2 Link:**
   - Autopilot detects loss after configurable timeout (10–20 s, TBD per range)
   - Enters lost-comm mode: flies to operator-defined lost-comm point and orbits
   - Iridium SBD backup provides fallback telemetry and limited commands
   - If C2 not regained within operator-set loiter time or battery reserve, autonomously executes stored landing plan and belly lands
   - Operator can command immediate return or landing

2. **Loss of Navigation (GNSS):**
   - Primary: Onboard GNSS (u-blox ZED-F9P) with redundant cross-checks (Dronetag Remote ID, Iridium reports, range radar, visual observers)
   - Autopilot fallback: Dead reckoning (airspeed, heading, wind estimate) with barometric altitude hold
   - Operator can manually guide aircraft back toward GCS
   - Future: Second GNSS receiver under consideration (not in baseline)

3. **Loss of Flight Reference Data (Attitude, Heading, Altitude, Airspeed):**
   - Dual IMUs: failover to secondary on primary fault
   - Magnetometer + GNSS-derived heading: fallback on magnetometer loss
   - Barometer (primary) + GNSS altitude fallback
   - Pitot-static (primary) + GNSS groundspeed with conservative margins on pitot loss

4. **Loss of Propulsion:**
   - Single motor out: Continue on remaining motor with rudder trim; return
   - Both motors out: Controlled glide (~20:1) with 3.3 nm per 1,000 ft AGL; operator directs to nearest landing or ditch point

5. **Loss of Electrical Power:**
   - Main power loss = control loss (no independent backup battery in baseline)
   - Mitigation (proposed): Two independently fused packs feeding bus through diode-OR; redundant connectors; preflight voltage checks
   - UPS powers GCS P400 radio; Iridium backup accessible from internet-connected device

6. **Servo / Flight Control Failure:**
   - Roll control split across two aileron surfaces + flaps + rudder; closed-loop compensation if one surface sticks
   - Throttle stuck: Can be disabled remotely (autopilot remote kill + ESC per motor); stuck-high shows as unexpected current/power/airspeed; stuck-low handled as loss of propulsion
   - Precautionary return and landing on control-surface fault

### Safeguard Verification
- **Return-Home Mode:**
  - Autonomous lost-link return to operator-defined lost-comm point
  - Altitude hold within assigned airspace block
  - Deviations raise alerts
  - After loiter timeout or battery reserve, executes stored landing plan (landing orbit, approach, abort orbit)
  - Multiple rally points under consideration (TBC with range)
  - Lost-comm point and routes planned inside range boundary, over unpopulated controlled area, within GCS line of sight

- **Landing Capability:**
  - Autonomous belly landing at designated recovery site
  - Pre-planned forced-landing areas within glide reach (~3.3 nm per 1,000 ft) from every point on route
  - Landing areas: open, unpopulated, flat, inside range boundary, cleared and surveilled by range control

- **Termination:**
  - No independent Flight Termination System (FTS) in baseline
  - Termination is autopilot function: motors stop, aircraft descends inside range boundary (exact behavior to be defined and demonstrated)
  - Command authority: PIC executes on direction from Range Safety / Mission Commander
  - Independent FTS with separate battery and receiver available as option if range requires

- **Collision Avoidance:**
  - Exclusive airspace required (restricted/warning or other range airspace)
  - Visual observers near launch and recovery
  - Range surveillance radar + range control traffic advisories
  - Remote ID (network and broadcast)
  - ADS-B In receiver optional
  - Anti-collision strobe (3 SM visible) + high-visibility markings (TBC)
  - No transponder or TCAS in baseline (can be added if required)
  - Chase aircraft: Not planned

- **Weather Minimums:**
  - VMC only (no IMC flight planned, though aircraft can technically fly in cloud under autopilot)
  - Planned limits (TBV by flight test):
    - Surface wind: ≤20 kt (launch/recovery)
    - Winds aloft: ≤35 kt
    - No icing, no thunderstorms, no precipitation (optical payload constraints)

---

## Open Items & Items "To Be Confirmed" (TBC)

The document identifies numerous open items that BST committed to address before or during Gauntlet:

### Pre-Gauntlet Deliverables (BST)
1. **S4 Operator's Manual** (NATOPS-equivalent) and Normal/Emergency Procedures Checklists
   - Derived from S2 Operator's Manual and SwiftCore 3.3 documentation
   - To be delivered before safety review
   - To include Safety Hazard Keep Out Zones and dimensions

2. **S4 IFC (Instrument Flight) Datasheet, Section 1**
   - Physical dimensions and airframe details

3. **S4 Electrical Power Budget Workbook**
   - Preliminary power-required and endurance estimates
   - Flight-test-based performance charts to follow early-2027 integrated aircraft flights

4. **Preliminary Hazard Analysis (PHA) and subsystem FMEA**
   - Covers: propulsion, power, C2, navigation, flight controls, launcher
   - Deliverable date and responsible party (BST RF lead mentioned) TBC

5. **Flight History / Mishap Data per Platform**
   - Flight-hour and mishap counts
   - Corrective actions (e.g., test-bed landing damage to customer-designed fuselage; S4 uses BST carbon-tube)

6. **Link Budget Analysis**
   - Formal link budget for P400 at Gauntlet site (once range geometry and GCS antenna known)
   - Ground range test before flight
   - Fade margin analysis (target 10 dB minimum at max range)
   - RF mask/null verification via ground range test

7. **FTS / Termination Behavior Definition & Demonstration**
   - Exact termination behavior for S4 to be defined in coordination with range
   - To be demonstrated in contractor flight test and witnessed/documented for range review

8. **S4-Specific Iridium Carrier Board Refresh**
   - Current Iridium carrier board to be refreshed for S4 compatibility

### Flight Test Milestones
- Early-2027: Integrated S4 aircraft flight testing (contractor flights)
- Early-2027: Performance charts and endurance validation
- Operator qualifications: PIC to have recent S4 or S-series flight time from early-2027 contractor FT

### Items Requiring Range Coordination
1. **Frequency assignments** (via range spectrum manager):
   - P400: 410–480 MHz hopping (exact hop set TBD)
   - pMDDL2280 video: 2.2–2.8 GHz
   - Neither holds a JF-12; to be coordinated with range

2. **C2 Configuration Parameters** (per range):
   - Lost-link detection timeout (e.g., 10–20 s)
   - Lost-comm point and altitude
   - Loiter time before landing
   - Altitude limits and exceedance response
   - Geofence-breach response and automatic termination criteria

3. **Weather Minimums** (TBV by flight test):
   - Surface wind limits (launch/recovery)
   - Winds aloft limits
   - Icing and precipitation constraints

4. **Landing Area Selection & Validation:**
   - Pre-planned forced-landing areas (to be cleared and confirmed with range control)
   - Landing site surveillance and control procedures

5. **Return Home / Rally Points:**
   - Selection and verification of lost-comm point and alternate rally points
   - Integration with range airspace and boundaries

6. **Safety Hazard Keep Out Zones:**
   - Launcher 30° cone / 300 ft forward, or within 25 ft while pressurized
   - Propellers: 15 ft radius once armed
   - Landing lane: 150 ft from centerline
   - Battery charging/storage: 25 ft from aircraft ops with fire suppression
   - Distances to be confirmed in S4 Operator's Manual

7. **Fire Danger Operational Restrictions:**
   - No operations over flammable vegetation during high fire danger without range approval

8. **ATC Briefing & Procedures:**
   - Brief to cover: aircraft description, airspace block/altitudes, launch/recovery times, lost-link and termination procedures, C2 frequencies, points of contact

---

## Notable Details

### Design Heritage & Pedigree
- **SwiftCore avionics proven:** 120+ S0-AD aircraft to NOAA; operational in hurricanes since 2021; SOCOM airdrops 2026
- **Airframe design:** Based on S2 (100+ flights in Arctic/volcanic) and Chilli test bed (2025–26, 25–40 lb long-endurance)
- **Aerodynamicist:** Same designer of S2/Chilli wings; S4 uses higher-performance 4.5 m design
- **Fuselage:** BST carbon-tube design (not 3D-printed; addresses test-bed landing damage issue)

### Low-Cost, Attritable Platform Approach
- No formal MIL-STD-882E safety assurance
- No DO-178C software safety
- Qualitative risk assessment based on flight history of common subsystems
- Designed for high-risk or austere environments (implicit from "low-cost, attritable ISR")

### Configuration & Modularity
- Single aircraft per GCS (not swarming)
- Modular payload: Stabilized EO/IR gimbal (FMV) or fixed camera with onboard ATR
- Companion computer for payload/ATR isolated from flight-critical systems via Safe Sandbox

### Operational Concept
- Land-based only (no shipboard or moving-platform launch/recovery)
- Autonomous BVLOS with pneumatic launch and belly landing
- Crew: 2–3 personnel (PIC, Payload Operator, Launch/Recovery Tech + VO)
- FAA Part 107 operators with BST type training

### Backup & Redundancy
- **C2:** Primary P400 (50 nm) + Iridium SBD (global)
- **Navigation:** GNSS + dead reckoning + Remote ID cross-check
- **Propulsion:** Dual motors with independent remote kill
- **Avionics:** Dual IMUs, single GNSS (second receiver TBC)
- **Power:** Two packs with proposed diode-OR redundancy and independent fusing
- **GCS:** UPS backup + Iridium accessible from any internet device

### Limitations & Constraints (Explicitly Stated)
- **No transponder or TCAS** in baseline (can be added)
- **No formal hazard/FMEA analysis** (committed to deliver pre-Gauntlet)
- **No independent FTS** (command-based termination via C2; independent FTS available as option)
- **No parachute** (recovery via belly landing only)
- **No second GNSS receiver** in baseline (future option)
- **No servo position feedback** on baseline PWM servos (DroneCAN servos with feedback TBC)
- **No chase aircraft** planned
- **VMC only** (no IMC flight planned; aircraft can technically fly in cloud)
- **50 nm operational radius** (C2 line-of-sight limit on P400)

### Regulatory & Coordination
- **No existing UAS/ATC MOA** for the Gauntlet; will follow range procedures
- **No frequency allocation** yet (P400 and video need JF-12 or range assignment)
- **Range Commander waiver may be required** if operational risks exceed specified levels even after safeguards

### Schedule
- **Questionnaire date:** 16 November 2026 (Rev 0 DRAFT)
- **Planned Gauntlet:** May–June 2027
- **Early-2027 contractor flight test:** S4 integrated aircraft
- **Pre-Gauntlet:** PHA, FMEA, operator manuals, link budget, termination demonstration

---

## Assessment Notes

### Strengths
- Proven avionics (SwiftCore/S0-AD heritage in NOAA, hurricanes, SOCOM)
- Multi-layer redundancy in C2 (P400 + Iridium), navigation (GNSS + dead reckoning + Remote ID), propulsion (dual motors), and sensors (dual IMUs)
- Robust lost-link logic and autonomous return/landing capability
- Modular, upgradeable design (transponder, ADS-B, second GNSS, independent FTS available)
- Clear operator qualifications and training protocol

### Weaknesses / Open Issues
- **No formal safety analysis yet** (PHA/FMEA committed but not delivered at time of this questionnaire)
- **Single GNSS receiver** (no dual GNSS in baseline; dead reckoning fallback adequate for short term but not long-duration GNSS loss)
- **No independent FTS** (reliance on C2 links; command-based termination; independent FTS available as option but not baseline)
- **No transponder or detect-and-avoid** (relies on exclusive airspace and visual observers)
- **Limited endurance validation** (12 h design objective; ~9 h with current cells; no flight-demonstrated performance charts yet)
- **Configuration not finalized** (many items marked TBC, e.g., exact servo types, carrier board refresh, termination behavior definition)

### Range Safety Review Focus Areas
1. **Link budget** and fade margin at Gauntlet site (pending site geometry)
2. **Ground range RF test** (antenna masking, nulls, multipath)
3. **Frequency coordination** (410–480 MHz P400, 2.2–2.8 GHz video)
4. **Hazard analysis** (PHA/FMEA pre-Gauntlet)
5. **Lost-link return verification** (operator-defined lost-comm point, landing site, rally points)
6. **Weather minimums** (wind, icing, precipitation limits per flight test)
7. **Termination criteria and procedure** (definition, demonstration, operator authority)
8. **Operator qualification verification** (recent flight hours, type training, emergency-procedure proficiency)
9. **Fire hazard mitigation** (battery compartment, crash-site procedures, ground equipment)
10. **Airspace coordination** (exclusive range airspace, ATC briefing, geofence/boundary enforcement)