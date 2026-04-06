# BST AFX236 D2P2 Technical Volume

## Document Metadata
- **Type:** SBIR Phase II Direct-to-Phase II (D2P2) Proposal - Technical Volume II
- **Client/Agency:** U.S. Air Force (Department of Defense)
- **Program/Solicitation:** AFX236-DPCSO1 - Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions with Clear DAF Stakeholder Need
- **Date:** October 23, 2023 (created/modified)
- **Proposal Number:** F2D-9055
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** S2 UAS, S3 UAS (VTOL), SwiftCore avionics, SwiftTab UI, Vision Processing Unit (VPU - Intel Myriad-X based)
- **Key Personnel:** Jack Elston (last editor), Lt Col Michael Dunn (NSDL Director - end-user), SrA Shane D. Smith (NSDL Innovation Specialist - customer), MSgt Harland and MSgt Carey (319 Reconnaissance Wing)

## Executive Summary
Black Swift Technologies proposes to develop an all-weather, autonomous multi-mission small Unmanned Aircraft System (sUAS) based on its S3 VTOL platform for Air Force base perimeter security and incident response. The work focuses on adapting the S3 with enhanced autonomy, machine vision/AI capabilities, all-weather operational modifications, and integration with Air Force ground systems (ATAK) to enable 24/7/365 operations in extreme conditions, particularly at locations like Grand Forks AFB with temperatures reaching -30°F and sustained winds to 45 mph.

## Technical Approach

### Core Strategy
BST proposes adapting its commercially-developed S3 (VTOL derivative of the S2 UAS) with four primary technical modifications:

1. **Perimeter Search Payload Integration:** Install HD45 gimbal (or similar EO/IR payload) from Trillium Engineering with onboard neural networks for real-time object detection and classification using machine vision algorithms.

2. **Ground System Integration:** Develop software interfaces to integrate S3 command/control and sensor data transmission with Android Tactical Assault Kit (ATAK) / Android Team Awareness Kit, the system currently used at Grand Forks AFB for perimeter surveillance operations.

3. **Cold Weather Readiness:** Engineer hardware modifications to enable the S3 to remain mission-ready (not just airborne) in sustained temperatures of -10°F or lower, addressing Grand Forks AFB requirement for immediate launch capability in extreme conditions.

4. **Workload Reduction:** Implement automated preflight checks, system readiness monitoring, and post-flight procedures; develop simplified mission planning tools allowing operators to define new surveillance missions in under 1 minute; deploy machine learning-based preventative maintenance algorithms.

### Technical Foundation
- **Avionics:** SwiftCore modular avionics system with well-defined interfaces between intelligent nodes
- **Vision Processing:** Intel Myriad-X Vision Processing Unit (VPU) running onboard neural networks for:
  - Single-shot detector networks for person/object detection
  - Semantic segmentation networks for safe landing zone identification
  - GPS-denied navigation capability (NOAA collaboration for jamming/spoofing detection)
- **Flight Management System:** Designed to minimize operator workload while improving data quality; customizable for mission requirements
- **All-component U.S. manufacturing and design requirement met

## Products & Capabilities Described

### S3 UAS (VTOL Fixed-Wing)
- **Classification:** Group 2, small UAS with vertical takeoff/landing capability
- **Specifications:**
  - Maximum Takeoff Weight: 33 lbs
  - Maximum Flight Time: 90 minutes
  - Maximum Payload: 5 lbs
  - Cruise Speed / Max Speed: 45 mph / 100 mph
- **Heritage:** Derivative of commercially successful S2 UAS, which has flown 104+ missions in Northern Greenland and operates for NASA, NOAA, USGS
- **Designed for extreme environments:** high altitude, arctic, volcanoes, hurricanes, tornadic thunderstorms
- **Modular payload system:** Quick reconfiguration on flight line for different mission types
- **Proposed price point:** Under $50K per aircraft for DAF (2-5x cost reduction vs. DoD-specific UAS)

### SwiftCore Avionics System
- Modular architecture with defined interfaces
- Enables simplified third-party component integration
- Supports subsystem tracking, preventative maintenance, safety through redundancy, automated sensor-driven control
- Designed/programmed exclusively by UAS technology experts

### Vision/AI Capabilities
- Machine learning-based neural networks for real-time threat detection
- Semantic segmentation for hazard avoidance and landing zone identification
- GPS-denied navigation development (with NOAA partnership)
- Preventative maintenance algorithms running on onboard processing

### HD45 EO/IR Gimbal (Trillium Engineering)
- Payload integration point for perimeter surveillance mission
- Provides video stream for onboard neural network processing

## Use Cases & Applications

### Primary DAF Application
**Base Perimeter Security and Incident Response (Grand Forks AFB)**
- 24/7/365 round-the-clock perimeter observations for change detection
- Rapid response to security incidents
- All-weather operation in extreme Arctic conditions (-30°F temperatures, 45+ mph sustained winds)
- Automated target detection and tracking
- Integration with existing ATAK ground control systems

### Secondary Non-Defense Government Applications
- **NASA:** Vehicle design, soil moisture mapping, CO2 detection, platform provision (S2 primarily)
- **NOAA:** Hurricane observations, soil moisture mapping, aircraft platforms (S2)
- **USGS:** Volcano monitoring, soil moisture mapping
- **DOE:** Solar panel inspections (E2 UAS)
- Fire/wildfire monitoring and mitigation
- Volcano monitoring and assessment
- Tornado and hurricane weather observations
- Arctic gas monitoring and coastal surveys

### Commercial/Scientific Applications
- University of Maryland Eastern Shore: Purchase order in place for 2 S3 aircraft ($150K total) for beyond-visual-line-of-sight medical supply cargo delivery in winter conditions
- Aerial photography/surveying
- Precision agriculture
- Wind energy surveying (Embry Riddle, Alerion partnerships)

## Key Results (Phase I-Type Feasibility Study)

### Customer Engagement Results
- Total federal government contact attempts: 63
- Successful email contacts: 30
- Successful phone contacts: 6
- Successful in-person contacts: 1
- Unique federal organizations contacted: 8
- Unique federal organizations reached: 8
- Unique USAF organizations contacted: 36

### Identified End-Users and Customers
- **Primary End-User:** 319 Reconnaissance Wing (319 RW) / North Spark Defense Laboratory (NSDL), Grand Forks AFB
  - Lt Col Michael Dunn (NSDL Director)
  - SrA Shane D. Smith (NSDL Innovation Specialist)
  - MSgt Jason Carey (Collaborative Lead)
  - Captain Daniel Rust
- **Key Finding:** Grand Forks AFB has evaluated over 40 UAS for this application and identified capability gaps addressed by this SBIR
- **NSDL Commitment:** Access to GrandSky (dedicated UAS development/testing environment); NSDL charged with championing autonomous sUAS innovation at Grand Forks

## Phase II Technical Objectives and Key Results

### Technical Objective 1: Perimeter Search Capabilities
**Key Results:**
1. Document pros/cons of various sensor packages; select one for demonstration
2. Validate payload performance at BST test area; provide coverage metrics (range vs. target size, coverage area per flight/hour)
3. Demonstrate 100% success rate identifying pre-placed test objects using machine learning-deployed real-time hazard detection

### Technical Objective 2: Mission Data Transmission
**Key Results:**
1. Demonstrate integration of S3 sensor data through ATAK
2. Transmit anomalous activity data and measure operator notification lag
3. Demonstrate continuous data transmission through ATAK for full mission without dropouts

### Technical Objective 3: All-Weather Operation
**Key Results:**
1. Demonstrate successful mission in temperatures below -10°F
2. Provide lowest operating temperature specification
3. Measure maximum sustained wind and gust takeoff/landing capability
4. Measure maximum rain/snow operational capability

### Technical Objective 4: Workload Reduction
**Key Results:**
1. Compile current UAS operation workload metrics with Grand Forks AFB operators (setup, flight, post-flight, maintenance)
2. List and rank areas for workload reduction through autonomy
3. Implement and test changes at BST facility and Grand Forks AFB
4. Deliver one-page assessment of S3 equipment/personnel requirements for daily perimeter security; measure resource reduction

## Phase II Work Plan (7 Tasks, 18-Month Duration, NTE $1.25M)

### Task 1: Requirements & Use Cases Analysis (Month 1 kickoff)
- Current S3 specifications delivery
- TPOC pain point identification (workload, maintenance for current base UAS)
- Requirements research (autonomy, AI, payload enhancements, communications)
- Requirements documentation, verification/validation methods, interface control document

### Task 2: Ground Systems Integration (Months 2+)
- Hardware procurement (aircraft and emulated ground systems)
- Wireless radio interface development and ground testing
- ATAK command/control software interfaces
- Sensor data pipelines (raw video + neural network output)

### Task 3: Workload Reduction (Months 3+)
- Hardware/software modifications for automated preflight, system readiness, post-flight checks
- Flight testing at BST site
- Flight planning/UI tools for mission setup in <1 minute
- 10 consecutive simulated missions
- Final one-page workload assessment

### Task 4: Cold Weather Readiness (Months 4+)
- Hardware design for continuous mission-ready state in cold
- Ground validation and payload performance testing
- Local flight tests validating ground tests

### Task 5: Mission Payload Functionality (Months 5+)
- Mechanical interface design (EO/IR payload mounting)
- Electrical/data interface design (payload to VPU)
- Customer-approved target list for detection/classification
- Neural network modification/implementation for object classification
- Local flight test: 100% success rate identifying pre-placed objects

### Task 6: Full Mission Testing (Months 6+)
- Complete system testing locally in conditions simulating North Dakota environment
- Iteration and system readiness updates
- Minimum 1-hour continuous operation at <-10°F on-site or within 50 miles of Grand Forks AFB

### Task 7: Reporting & Delivery (Month 18)
- Data collection and visualization demonstrating requirements met
- Results write-up
- Operating manuals, training regimen, interface documentation
- Flight demonstration at/within 50 miles of Grand Forks AFB
- Hardware delivery: S3 aircraft, sensor package, ground support equipment provided to customer

### Milestone Schedule Summary
| Milestone | Timeline | Deliverable | Payment |
|-----------|----------|-------------|---------|
| 01 | Award +1 mo | Customer requirements & specifications | $50,000 |
| 02 | Award +3 mo | Preliminary designs, algorithm designs, risk analysis | $XXXX |
| 03 | Award +6 mo | Hardware design changes, manufacturing readiness | $XXXX |
| 04 | Award +8 mo | Software/firmware for communications | $XXXX |
| 05 | Award +10 mo | Functional prototypes for testing | $XXXX |
| 06 | Award +12 mo | Bench-top test plan development | $XXXX |
| 07 | Award +16 mo | Proof-of-concept bench testing results | $XXXX |
| 08 | Award +18 mo | Final report | $50,000 |

## Notable Details

### Compliance & Regulatory
- **Flight Testing:** Yes, outdoor UAS; location: Sunny Slope Sod Farm, Longmont, CO
- **Government Personnel/Facilities:** Yes, involvement planned
- **Hardware/Software Delivery:** Yes
- **Hazardous Materials/Weapons:** None
- **Human Subjects/Animal Testing:** None

### Intellectual Property Strategy
- **Approach:** Trade secrets protection preferred over patents (to avoid market disclosure requirements)
- **Evaluation:** Will assess Phase III-developed technologies