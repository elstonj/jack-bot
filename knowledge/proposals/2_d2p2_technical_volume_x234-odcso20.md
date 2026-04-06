# D2P2 Technical Volume (X234-ODCSO20)

## Document Metadata
- **Type:** SBIR Phase II Proposal (Direct-to-Phase II)
- **Client/Agency:** U.S. Air Force (Department of the Air Force)
- **Program/Solicitation:** AFX234-DCSO2 – Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions with a Clear Air Force Stakeholder Need
- **Proposal Number:** F2D-7516
- **Date:** Submitted October 23, 2023
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** S2, S3, SwiftCore avionics, SwiftTab UI, Vision Processing Unit (VPU)
- **Key Personnel:** Dr. Jack Elston (CEO/PI), Dr. Maciej Stachura (CTO/Lead Engineer), Ed Kase (Business Development)

---

## Executive Summary

Black Swift Technologies proposes to develop an all-weather, autonomous small UAS (sUAS) based on the S3 platform for persistent perimeter security and rapid incident response at U.S. Air Force bases, particularly those in extreme cold and wind environments like Grand Forks AFB. The system will integrate advanced machine vision and machine learning capabilities for automated threat detection, command-and-control integration with military systems (ATAK), and significantly reduced operator workload through onboard autonomy, addressing critical capability gaps in base security operations across challenging weather conditions.

---

## Technical Approach

### Core Platform
The S3 is a Group 2 fixed-wing VTOL UAS derived from BST's commercially successful S2 platform. Key specifications:
- Maximum Takeoff Weight: 33 lbs
- Maximum Flight Time: 90 minutes
- Maximum Payload: 5 lbs
- Cruise Speed/Max Speed: 45 mph / 100 mph
- Designed for extreme environment operations

### Key Technical Modifications for Phase II

**1. Perimeter Search & AI Detection**
- Integration of HD45 gimbal payload from Trillium Engineering for electro-optical/infrared (EO/IR) sensor capability
- Onboard Vision Processing Unit (currently Intel Myriad-X based) running single-shot detector neural networks for real-time person detection
- Semantic segmentation networks for safe autonomous landing site identification
- 100% success rate demonstration requirement for detecting pre-placed test objects using machine learning

**2. Ground System Integration**
- Command and control integration with Android Tactical Assault Kit (ATAK) military system
- Data transmission protocols for secure, real-time relay of sensor data and threat identification
- Software interfaces supporting both raw video feeds and higher-level data from onboard neural networks

**3. All-Weather Hardening**
- Hardware modifications for sustained operation at -10°F or lower while in mission-ready state (not just during flight)
- Enhanced cold-weather component selection and thermal management
- Validation for operation in sustained winds up to 45 mph with precipitation capability
- Ground testing at extreme thermal and environmental conditions

**4. Workload Reduction Through Autonomy**
- Automated preflight self-checks and system readiness monitoring
- Automated post-flight checks
- Enhanced flight planning tools abstracting beyond waypoint creation—operators can input full surveillance missions in under 1 minute
- Machine learning-based onboard preventative maintenance and failure detection
- Reduced cognitive load for operators via mission automation

### Hardware & Software Components
- All major components designed and manufactured in the United States
- SwiftCore avionics system with modular architecture and well-defined interfaces
- Enhanced firmware for autonomous functions and subsystem health monitoring
- Integration with existing BST-developed vision and machine learning algorithms originally designed for safe/automated landing

---

## Products & Capabilities Described

### S3 VTOL UAS
**What it is:** A derivative of the commercially successful S2, the S3 is a vertical takeoff-and-landing fixed-wing UAS designed for harsh environments. Currently in late-stage prototype development with planned commercial release in Q1 2023.

**How it was proposed to be used:** As the base platform for an all-weather, autonomous perimeter security and rapid response system for Air Force bases. The modular payload system allows rapid reconfiguration between missions on the flight line.

**Specifications:**
- 33 lbs MTOW, 90-minute endurance, 5 lb max payload
- 45 mph cruise / 100 mph max speed
- VTOL capability eliminates need for runway
- Proven heritage in extreme environments (Arctic, volcano, hurricane, tornado operations)

**Competitive advantages:**
- 2x–5x cost reduction compared to DoD-specific UAS platforms (targeted <$50K per aircraft)
- All-weather operation capability (addressing major gap in current "drone-in-a-box" solutions)
- Lower operator workload through onboard autonomy
- Modular payload design and open interfaces

### SwiftCore Avionics System
**What it is:** A modular avionics architecture with well-defined interfaces between intelligent nodes, designed exclusively by UAS technology experts.

**How it was proposed to be used:** Provides the foundation for autonomous operation, multi-subsystem tracking, preventative maintenance monitoring, redundancy-based safety, and automated sensor-driven control.

**Capabilities:**
- Simplified third-party component integration
- Subsystem health monitoring and predictive maintenance
- Automated mission execution with minimal operator oversight
- Networking capabilities for cooperative control

### Vision Processing Unit (VPU) & Machine Learning
**What it is:** Intel Myriad-X based processing unit running on-board neural networks for real-time object detection and scene understanding.

**How it was proposed to be used:**
- Single-shot detector networks for person/threat detection in perimeter surveillance
- Semantic segmentation for safe landing site identification
- Detection and classification of objects specific to base security mission

**Heritage applications:** Originally developed for automated UAS landing, collision avoidance, GPS-denied navigation (jamming/spoofing detection in partnership with NOAA).

### SwiftTab UI
**What it is:** Current ground station user interface based on Android tablets.

**Proposed enhancement:** Integration with ATAK (Android Tactical Assault Kit) to provide seamless integration with existing Air Force command-and-control systems and situational awareness tools, minimizing operator training requirements.

---

## Use Cases & Applications

### Primary Use Case: Air Force Base Perimeter Security & Rapid Response
**Operational Context:**
- 24/7/365 persistent surveillance of base perimeters
- Rapid incident response capability
- All-weather operation in locations like Grand Forks AFB (temperatures to -30°F, sustained winds to 45 mph)
- Mission-ready status even after extended outdoor storage in cold conditions

**Specific End-User:** 319th Reconnaissance Wing / North Spark Defense Laboratory at Grand Forks AFB

**Key Requirements Addressed:**
- Elimination of weather-imposed operational constraints (current limiting factor for existing small UAS)
- Round-clock observations essential for change detection
- Significantly reduced operator cognitive load to enable focus on other mission functions
- Quick-response capability for incident investigation
- Seamless integration with existing base security procedures and systems

### Potential Expansion Use Cases
- **Emergency Response:** Rapid deployment for emergency management and security force incidents
- **Change Detection:** Continuous data collection for perimeter anomaly identification
- **Scientific Missions:** Leverage S3 heritage in volcano monitoring, wildfire assessment, Arctic research, hurricane observation (non-defense civil applications)
- **Medical Supply Delivery:** University of Maryland Eastern Shore planned winter deployment over Chesapeake Bay in difficult conditions

### Non-Defense Government Applications
BST actively supplies S2 UAS to:
- NASA (volcano monitoring, vehicle design, soil moisture, CO2 detection)
- NOAA (hurricane observation, soil moisture, instrument calibration)
- USGS (volcano monitoring, soil moisture, wildfire mitigation)
- Universities (Embry Riddle, University of Colorado, etc.)

The S3 is payload-compatible with existing S2 scientific missions and would provide improved all-weather capability and reduced workload for these applications.

---

## Phase II Technical Objectives & Key Results

### Technical Objective 1: Perimeter Search Capabilities
**Key Results:**
1. Payload selection document with pros/cons analysis of sensor packages
2. Performance metrics including sensor range vs. target size and coverage area per flight/hour
3. Demonstration of 100% success rate in identifying pre-placed test objects using automated ML classification

### Technical Objective 2: Mission Data Transmission
**Key Results:**
1. Integration of S3 sensor data through ATAK or equivalent Grand Forks AFB systems
2. Measurement of data transmission lag for anomalous activity alerts
3. Demonstration of continuous error-free data transmission throughout full mission

### Technical Objective 3: All-Weather Operation
**Key Results:**
1. Successful mission demonstration at temperatures below -10°F
2. Determination of minimum operating temperature
3. Measurement of maximum sustainable wind speeds for takeoff/landing
4. Characterization of maximum rain/snow operation capability

### Technical Objective 4: Workload Reduction
**Key Results:**
1. Compilation of baseline workload metrics for current UAS operations (setup, flight, post-flight, maintenance)
2. Ranked list of workload reduction opportunities through autonomy
3. Implementation and local testing of autonomy improvements
4. One-page assessment of equipment and personnel requirements for daily perimeter security with quantified resource reduction

---

## Phase II Work Plan (Non-Proprietary)

### Task 1: Requirements & Use Cases (Months 0–2)
- Finalize S3 specifications and end-user requirements
- Identify operator and maintenance workload pain points
- Research autonomy, AI, and payload enhancement requirements
- Develop requirements and interface control documents

**Deliverable (Month 2):** Updated product & technical requirements document

### Task 2: Ground System Integration (Months 2–12)
- Procure aircraft and ground system hardware
- Develop and validate wireless radio interfaces
- Create software interfaces for ATAK command and control
- Implement data pipelines for raw sensor video and processed threat identification

**Deliverable (Month 12):** Software/firmware package with secure wireless communication

### Task 3: Workload Reduction (Months 2–12)
- Implement automated preflight, in-flight, and post-flight checks
- Develop mission planning UI allowing sub-1-minute mission setup
- Conduct 10 consecutive simulated surveillance missions with finalized tools
- Provide one-page assessment of personnel and equipment requirements

**Deliverable (Month 12):** Operational procedures and workload assessment document

### Task 4: Cold Weather Readiness (Months 6–14)
- Design hardware modifications for continuous mission-ready state at extreme cold
- Ground validation and performance testing at temperature and weather extremes
- Flight test local conditions replicating Grand Forks environment

**Deliverable (Month 14):** Cold-weather qualified aircraft and testing data

### Task 5: Mission Payload Functionality (Months 2–14)
- Mechanical integration of HD45 gimbal or equivalent
- Electrical and data interface from EO/IR payload to VPU
- Object detection and classification network development and training
- Local flight test demonstrating 100% success rate on test object identification

**Deliverable (Month 14):** Flight-qualified payload-integrated system

### Task 6: Full Mission Testing (Months 12–18)
- Full-up system testing in conditions matching North Dakota demonstration environment
- Iteration and refinement based on results
- Conduct minimum one hour continuous operation below -10°F at or near Grand Forks AFB

**Deliverable (Month 18):** Flight test data and operational readiness report

### Task 7: Reporting (Months 14–18)
- Data collection and visualization
- Results writeup and technical documentation
- Operating manuals, training regimen, and updated interface documents

**Deliverable (Month 18):** Final report, operating manuals, and training materials

### Milestone Schedule Summary
| Milestone | Month | Deliverable | Payment |
|-----------|-------|-------------|---------|
| Finalize customer requirements | 2 | Updated work plan | $64,085 |
| Preliminary design & algorithms | 4 | Engineering designs with risk assessment | $297,802 |
| Design integration changes | 8 | Mechanical/electrical modifications | $124,895 |
| Software & firmware development | 12 | C2 software and secure communication | $180,530 |
| Functional prototype builds | 14 | Benchtop-ready prototypes | $199,483 |
| Bench-top test plan | 14 | Testing protocol | $225,663 |
| Proof-of-concept testing | 15 | System performance validation | $106,675 |
| Final report submission