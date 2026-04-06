# Questionnaire Appendices - Ringlet

## Document Metadata
- Type: Questionnaire/Compliance Appendices
- Client/Agency: Creare (aircraft owner); appears to be for regulatory/safety approval
- Program/Solicitation: 2019 Titan SBIR
- Date: 2021-07-23 (created/modified)
- BST Products/Systems Referenced: SwiftPilot, SwiftCore FMS
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This document contains hazard analysis, emergency procedures, and systems monitoring documentation for a small UAS (unmanned aircraft system) operation. It details risk assessments across 14 identified hazards, emergency response protocols for various failure scenarios, and electronic monitoring system configurations. The aircraft and sensor system are valued at less than $20,000 and are owned by Creare.

## Technical Approach & Systems Description

### SwiftPilot Autonomous Control System
- Single communication channel for autonomous control from ground station
- Employs periodic heartbeat packets from ground control station (GCS) to verify link integrity
- **Lost Link Procedures**: On communication loss, aircraft automatically transitions to a pre-programmed "lost comm waypoint" allowing re-establishment of communications or manual takeover
- Manual handset provides secondary control link independent of autopilot data link
- If manual handset link is lost while in manual control, aircraft automatically switches to autonomous control

### SwiftCore FMS (Flight Management System)
- Integrates Electronic Centralised Aircraft Monitor System (ECAMS)
- Provides real-time failure monitoring with two alert levels:
  - **Level 2 Failure (Master Caution, Yellow)**: User-initiated pop-up warnings
  - **Level 3 Failure (Master Warning, Red)**: Automatic action with no user dismissal option

## Products & Capabilities Described

### Black Swift Technologies Power Supply Board
- Custom power distribution equipment for avionics
- Supports redundant voltage regulators for autopilot systems
- Integrated into avionics package

### Communications Systems
**Telemetry & Control (Microhard P900)**
- RF Power: 1W
- Frequency: ISM 902-928 MHz
- Used for autonomous command and telemetry
- No FCC authorization required for U.S. operation

**RC Backup Link (Futaba 14SG)**
- RF Power: 36.14 mW
- Frequency: 2.405367-2.47296 GHz
- Independent radio link for manual pilot override
- No FCC authorization required for U.S. operation

### Power Systems
- 14,000mAh Lithium Ion battery pack with 18650 cells
- Battery packs fused in aircraft for safety
- Cell balancing charger with automatic fault detection
- Pre-flight battery cell checker validates pack health
- Redundant independent voltage regulators

## Use Cases & Applications
- Remote area operations (unspecified specific mission, but references Titan SBIR program)
- Visual line-of-sight (LOS) flight operations in Class G airspace under VFR conditions
- Operations conducted in remote areas with low structure and population density
- Clear weather conditions only

## Hazard Analysis & Risk Management

### 14 Identified Hazards with Mitigation:
| Hazard | Severity | Probability | Key Mitigations |
|--------|----------|-------------|-----------------|
| S01: Battery Fire | II-E (Critical/Improbable) | Fused batteries, cell balancing charger, Class D fire extinguisher, pre-flight checkers |
| S02: Autopilot Loss of Control | II-E | Pre-flight checklists, manual pilot independent control link |
| S03: Loss of Electrical Power | II-E | Pre-flight voltage verification, redundant voltage regulators |
| S04: Mid-air Collision | I-E (Catastrophic/Improbable) | NOTAMs issued, qualified observer maintaining LOS, operation at lower altitudes in remote areas |
| S05: Loss of C&C Link | III-D (Moderate/Remote) | Auto return to lost link waypoint, automatic landing |
| S06: Loss of GCS Power | III-D | Multiple independent power sources, handset backup |
| S07: Loss of Handset Power | III-D | Tablet interface for manual control redundancy |
| S08: Aircraft Crash/Fire | II-E | Fire extinguisher on ground, emergency notifications |
| S09: Aircraft Leaves Boundary | II-E | Geo-fenced flight region, LOS manual control, aerodynamic termination on boundary violation |
| S10: Lost GPS | III-D | Pre-flight GPS validation, LOS manual takeover capability |
| S11: Engine Out | III-D | Pre-flight battery checks, real-time voltage tracking, auto-landing capability |
| S12: Propeller Strike | II-E | Trained crew only, flight procedures, proper arming procedures |
| S13: Structural Failure | II-E | Routine maintenance, pre-flight checks, manual pilot skill |
| S14: Inclement Weather | IV-C (Negligible/Occasional) | Clear weather only operations, immediate termination with approaching weather |

### Risk Acceptance Framework
- Hazards in solid red area of Risk Matrix require Center Director approval
- Red cross-hatched areas require Center Director approval with rationale
- White areas approved at Project/Program Manager level
- All hazards mapped and reported to senior management

## Emergency Procedures

### Operational Emergencies
1. **Incapacitated Crew Member**: Transfer duties to certified crew; initiate lost link procedures if necessary
2. **Loss of Visual LOS**: Another team member assumes observer role; if none available, PIC initiates landing or aerodynamic termination
3. **Loss of PIC-Observer Communication**: Immediate lost link procedures or landing
4. **UA Leaves Boundary**: Aircraft programmed for aerodynamic termination; geo-fence prevents departure
5. **Near Midair Collision**: UAS gives right-of-way in all cases; follow FAA Order 8020.11
6. **Accident/Crash Recovery**: Detailed logging by PIC of all actions and notifications; comply with FAA Order 8020.11 and NTSB 830

### Ground Control Station Failures
- GCS or ground station power failure initiates lost link event
- Aircraft returns to controllable distance within visual and handset range
- Lost communications flight plan maintains safe separation
- Manual takeover and landing procedures initiated

### Aircraft Emergency Procedures
1. **Aerodynamic Surface Failure**: PIC makes manual decisions based on failure type and surface condition
2. **GPS Unit Failure**: 5-second timeout; aircraft maintains altitude/airspeed but may deviate from flight plan; initiates 20° roll descent at commanded airspeed
3. **Engine Out**: Autopilot maintains altitude via elevator for up to 10m below desired altitude; transitions to airspeed maintenance; standard landing procedure if sufficient altitude
4. **Autopilot/Servo Power Loss**: Catastrophic uncontrollable failure; PIC priority is maintaining safe airspace and issuing distress messages
5. **Structural Failures**: Response depends on failure type and condition; manual pilot decision-making required

### ECAMS Master Warnings & Cautions
**Level 2 (Master Caution) - User-Initiated Dismissal**:
- Degraded GPS, Loss of laser, Loss of static, SD Card failure, Error waypoint, Low GCS battery, Low tablet battery, Loss of mag, Loss of battery reading, Loss of propulsion, Hardware fault

**Level 3 (Master Warning) - Automatic Primary Action**:
- Lost GPS, Loss of IAS reading, Battery below minimum, Minimum voltage exceeded, Reset in-flight, Launch without preflight

**Special Handling**:
- Lost Aircraft Comms / Lost Tablet to GCS: Initiates Lost Comms Point procedure

## Notable Details

### Safety Philosophy
- Emphasis on safe operation and deconfliction with manned aircraft
- All procedures designed to maintain safe operations in National Airspace
- Remote area operations minimize risk to structures, buildings, and populated areas
- Multiple redundancies in critical systems (dual communication links, dual power supplies, manual/autonomous control options)

### Operational Constraints
- Operations limited to Class G airspace under VFR conditions
- Clear weather only
- Visual line-of-sight operations maintained
- Qualified observer required
- Handheld VHF radio for situational awareness and local air traffic communication

### Aircraft Specifications
- Combined aircraft and sensor system value: <$20,000
- Aircraft property of Creare
- Designed for research and testing operations

### Regulatory Framework
- Complies with FAA Orders 8020.11 and 7210.56
- Follows NTSB 830 accident reporting requirements
- FAR Part 91.113 traffic and collision avoidance rules
- NASA safety standards referenced (NPR 8715.3, NPR 8621.1)