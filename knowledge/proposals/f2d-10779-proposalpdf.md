# An All-Weather UAS for Persistent Base Security and Rapid Response

## Document Metadata
- **Type:** SBIR Phase II Proposal (Direct-to-Phase II)
- **Client/Agency:** U.S. Air Force
- **Program/Solicitation:** AFX244-DPCSO1, Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions with a Clear Air Force Stakeholder Need
- **Proposal Number:** F2D-10779
- **CAGE Code:** 6PGF9
- **Date:** 2023 (submitted)
- **BST Products/Systems Referenced:** S2 (commercial fixed-wing UAS), S3 (VTOL version of S2), SwiftCore (modular avionics system), SwiftTab UI
- **Key Personnel:** Dr. Jack Elston (Founder/CEO, Principal Investigator), Dr. Maciej Stachura (Founder/CTO, Lead Engineer)

## Executive Summary
Black Swift Technologies proposes to develop an all-weather VTOL unmanned aircraft system (S3) specifically adapted for persistent base security and rapid incident response at Air Force installations. The system will integrate advanced machine learning-based object detection, autonomous operation capabilities, and weather-hardened design to enable 24/7/365 perimeter surveillance operations in extreme conditions (tested at -30°F and 45+ mph sustained winds) while significantly reducing operator workload and training requirements.

## Technical Approach

### Core Platform: S3 VTOL UAS
- **Type:** Group 2 fixed-wing VTOL (vertical takeoff and landing)
- **Heritage:** Derivative of commercially successful S2 UAS with proven operation in extreme environments (arctic, volcanic, hurricane, tornado research)
- **Key Specifications:**
  - Maximum Takeoff Weight: 33 lbs
  - Maximum Flight Time: 90 minutes
  - Maximum Payload: 5 lbs
  - Cruise Speed/Max Speed: 45 mph / 100 mph
  - Target Unit Cost: Under $50K per aircraft

### Four Primary Technical Objectives

**1. Perimeter Search Capability**
- Integration of HD45 gimbal from Trillium Engineering as primary sensor
- Real-time machine vision algorithms for automated object detection and classification
- Requirement: 100% success rate in identifying pre-placed test objects near perimeter
- Dual neural networks: single-shot detector for people detection; semantic segmentation for safe landing zone identification

**2. Data Transmission Integration**
- Integration with Android Tactical Assault Kit (ATAK) for command/control and sensor data transmission
- Current system uses commercial COTS radio to ground station via SwiftTab UI
- Deliverable: Seamless integration with Air Force ground infrastructure with minimal operator retraining
- Real-time data relay in response to anomalous activity detection

**3. All-Weather Operational Readiness**
- Design modifications to maintain mission-ready status in harsh outdoor conditions for extended periods (not just while airborne)
- Temperature rating: capable of operation at -20°F or lower; tested at JBER conditions (-30°F observed, 45+ mph sustained winds)
- Weather performance metrics to establish: minimum temperature operation, maximum sustained wind/gusts, rain/snow capability

**4. Workload Reduction**
- Automated preflight self-checks and system readiness monitoring
- Automated post-flight checks
- Machine learning/vision automation for perimeter surveillance tasks
- Flight planning UI allowing new surveillance missions to be input in under 1 minute
- On-board preventative maintenance and failure detection

### Avionics & Control Systems
- **SwiftCore:** Truly modular avionics architecture with well-defined interfaces between intelligent nodes
- Designed and programmed by UAS technology experts (not loose collection of programmers)
- Enables subsystem tracking, preventative maintenance, safety through redundancy, automated sensor-driven control
- Open interfaces for third-party component integration
- All major components (avionics, software, radios, ground systems) designed and manufactured in the United States

### Vision Processing Unit (VPU)
- Current implementation: Intel Myriad-X VPU (onboard)
- Machine learning networks developed for:
  - Safe/automated landing with collision avoidance
  - Perimeter defense object detection and classification
  - GPU-denied navigation (GPS jamming/spoofing detection and mitigation - developed with NOAA)

## Products & Capabilities Described

### S3 VTOL UAS
- **What it is:** Vertical takeoff/landing fixed-wing UAS in late-stage prototype development (planned commercial release Q1 2024); derivative of proven commercial S2 platform
- **Proposed use for JBER:** Adapted for year-round base perimeter surveillance and incident response in extreme weather conditions
- **Specifications:** 33 lbs MTOW, 90-min endurance, 5 lbs max payload, 45/100 mph cruise/max speed
- **Key differentiator:** All-weather capability tested in conditions (-30°F, 45+ mph winds) where competing "drone-in-a-box" solutions (Skydio, EasyAerial) cannot operate
- **Current traction:** Early adopter release to small customer group; University of Maryland Eastern Shore purchase order for 2 aircraft + support contract ($150K); Institute of Arctic and Alpine Research purchase ($48K)

### SwiftCore Avionics System
- **What it is:** Modular architecture with open interfaces and well-defined intelligent nodes
- **Function:** Simplifies third-party component addition; enables advanced capabilities (tracking, preventative maintenance, redundancy, sensor automation)
- **Benefit:** Reduced operator workload, programmative risk reduction, next-generation capabilities like preventative maintenance

### Machine Learning/Vision Capabilities
- Single-shot detector neural network for person/object detection
- Semantic segmentation network for safe landing zone identification
- Trained on datasets for automated threat detection in perimeter defense context
- Runs on onboard VPU in real-time with minimal latency
- Originally developed for safe/automated landing, now adapted for perimeter defense

### Payload Integration
- Modular payload system allowing flight-line conversion for different mission types
- HD45 gimbal from Trillium Engineering planned as primary sensor for base security variant
- Custom data pipelines for both onboard machine vision processing and ground station relay

## Use Cases & Applications

### Primary Use Case: Joint Base Elmendorf-Richardson (JBER), Alaska
- **Mission:** 24/7/365 base perimeter surveillance and incident response
- **Operational Context:** Extreme temperatures (-30°F observed), sustained winds (45+ mph), winter conditions
- **Customer:** 673d Security Forces Squadron (Lt Col Michael Kennedy, TSgt Donald Nachand); Air Force Security Forces Center (MSgt Dustin Spooner)
- **Requirement:** Must be ready to launch at moment's notice from outdoor storage in -20°F+ conditions
- **End-user validation:** JBER evaluated 40+ UAS platforms and identified capability gaps this proposal addresses

### Related Commercial/Government Use Cases (S2/S3 Heritage)
- **NASA:** Volcano monitoring, vehicle design, soil moisture mapping, CO2 detection, aircraft platforms
- **NOAA:** Hurricane observations, soil moisture mapping, aircraft platforms
- **USGS:** Volcano monitoring, soil moisture mapping
- **DOE:** Solar panel inspections
- **University of Maryland Eastern Shore:** Medical supply cargo delivery in winter conditions over Chesapeake Bay
- **Institute of Arctic and Alpine Research:** Moisture and methane mapping north of Anchorage
- **Colorado Center of Excellence for Advanced Technology Aerial Firefighting:** Interest in ATAK-based situational awareness for fire operations

### Broader Air Force Applications
- Base security at installations vulnerable to extreme weather (Eielson AFB, Malmstrom AFB mentioned)
- Integration into Integrated Base Defense Security System (IBDSS) program of record
- Joint All Domain Command and Control (JADC2) multi-domain capability
- Scaling to MAJCOM-level adoption across Air Combat Command

## Key Phase I Results
- Feasibility study completed with roadmap and timeline for Phase II initiatives
- Direct engagement with JBER end-users identified specific operational needs
- Extensive Air Force stakeholder outreach:
  - 63 federal government contact attempts
  - 30 successful email contacts, 6 phone, 1 in-person
  - 8 unique federal government organizations reached
  - 36 unique USAF organizations contacted
- Identified empowered end-users (673d SFS at JBER) and customers (AFSFC) committed to Phase II collaboration

## Phase II Technical Objectives & Key Results

### Objective 1: Perimeter Search Capability Development
- Select payload package(s); document pros/cons of sensor options
- Validate payload performance with documented metrics (sensor range vs. target size, coverage area per flight/hour)
- Demonstrate 100% success rate in automated identification of pre-placed test objects using neural networks

### Objective 2: Data Transmission to AF Operators
- Demonstrate S3 sensor data integration through ATAK
- Measure latency of anomalous activity data relay to operators
- Demonstrate continuous data transmission throughout full mission without dropouts

### Objective 3: All-Weather Operation
- Successful mission demonstration below -10°F
- Establish lowest operational temperature capability
- Measure maximum sustained wind and wind gusts for takeoff/landing
- Measure maximum rain/snow operational capability

### Objective 4: Operator Workload Reduction
- Compile current workload metrics for existing UAS operations (setup, flight, post-flight, maintenance)
- Identify and rank workload reduction opportunities through autonomy
- Implement and test changes at BST facility and JBER
- Deliver one-page assessment of equipment and personnel workload requirements for daily perimeter security operations

## Phase II Milestones & Deliverables

| Milestone | Timeline | Deliverable | Acceptance Criteria | Funding |
|-----------|----------|-------------|-------------------|---------|
| 01 | Award + 1 month | Kick-off & AF Requirements Analysis | End-user/customer agreement on specifications | $64,085 |
| 02 | Award + 6 months | Initial functional prototype (MVP1) development & testing | AF customer acceptance via status report | $297,802 |
| 03 | Award + 10 months | MVP2 with autonomous capabilities | AF customer acceptance via status report | $124,895 |
| 04 | Award + 12 months | AF mission-specific interfaces & UI (ATAK integration) | AF acceptance via software-in-the-loop simulation | $180,530 |
| 05 | Award + 14 months | MVP3 with surveillance payload integration | AF technical monitor acceptance | $199,483 |
| 06 | Award + 15 months | MVP4: Full S3 UAS with final AF customizations + spare parts | Physical acceptance by AF end-user | $225,663 |
| 07 | Award + 16 months | Final prototype testing & reporting | Test report endorsed by AF end-user | $106,675 |
| 08 | Award + 18 months | Additional reporting/documentation as required | AF-endorsed reports | $50,000 |
| **Total Phase II** | | | | **$1,248,733** |

### Major Work Tasks
1. Requirements research and development (1.1-1.6)
2. Ground systems interface development (2.1-2.4)
3. Workload reduction implementation (3.1-3.5)
4. Cold weather readiness design and validation (4.1-4.3)
5. Mission payload integration (5.1-5.5)
6. Full mission testing (6.1-6.3)
7. Reporting and documentation (7.1-7.4)

### Key Deliverables
- Flight demonstration at or within 50 miles of JBER with data analysis package
- One-page assessment of UAS equipment/personnel workload requirements
- Delivery of demonstration hardware (S3 aircraft, sensor payload, ground support equipment) to customer for further validation/deployment
- Final comprehensive report with project summary, technical results, feasibility analysis
- Quarterly status reports (max 15 slides)
- Operating manual, training regime, updated interface documentation
- Safety documentation including preliminary hazard analysis (hardware development deliverable)

## Commercialization Strategy

### Commercial Product Vision
- S3 VTOL UAS as primary product for market entry; derivative of proven commercial S2 (3+ years in market)
- 13 S2 UAS units built and sold; current sales price just under $65K (aircraft, launcher, ground systems, training)
- S3 planned commercial release: Q1 2024
- Phase II deliverables to produce production-ready S3 for base security; first