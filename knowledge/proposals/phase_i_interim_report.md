# Improved UAS Robustness through Augmented Onboard Intelligence

## Document Metadata
- Type: NASA SBIR Phase I Interim Report
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR 2017, Topic: A Ruggedized UAS for Scientific Data Gathering in Harsh Environments
- Contract Number: NNX17CD08P
- Date: September 2017
- BST Products/Systems Referenced: SwiftCore Flight Management System, SwiftPilot autopilot, SuperSwift aircraft
- Key Personnel: Dr. Jack S. Elston (PI), Dr. Maciej Stachura (Machine Learning/Regulatory Expert), Dr. Cory Dixon (Wireless Network/Avionics Expert)

## Executive Summary

Black Swift Technologies proposes an onboard intelligence system using networked monitoring nodes and machine learning algorithms to provide early warning of critical subsystem failures on small UAS. The modular, weight-constrained system will observe subsystem operations and alert both the autopilot and operator to off-nominal conditions, enabling predictive maintenance and in-flight failure mitigation. Phase I focuses on identifying critical failure modes, selecting machine learning algorithms, and designing the monitoring node architecture.

## Technical Approach

**Core Architecture:**
- Distributed network of small, lightweight monitoring nodes communicating via CAN bus and UAVCAN protocol
- Each node equipped with sensors, onboard processing, and machine learning algorithms
- Nodes interface with SwiftCore autopilot and provide telemetry to ground operators
- System designed for minimal impact on vehicle performance (size, weight, power constrained)

**Key Technical Components:**

1. **Subsystem Monitoring Targets:**
   - Propulsion system (motor, propeller, speed controller degradation)
   - Onboard batteries (charge/discharge cycles, cell degradation)
   - Servos and actuators (real-time failure detection, degradation tracking)
   - Air data systems (pitot tube clogging, sensor disconnection)
   - Structural faults (G-force monitoring, fatigue tracking)

2. **Machine Learning Approach:**
   - AdaBoost (adaptive boosting) algorithm combining weak learners as binary classifiers
   - Leverages BST's heritage with simple boosting for launch detection and landing impact detection
   - Processes data from distributed monitoring nodes and autopilot sensors
   - Training data sourced from: FAA COA Accident & Incident reports (274 incidents 2009-2014), BST internal flight datasets (1,000+ flights without failures, datasets with propulsion failures, battery issues, pitot tube clogging)

3. **Monitoring Node Design:**
   - Based on existing SwiftCore interface node (flight heritage in approved NASA missions)
   - Processor: NXP Semiconductors LPC4300 DSP family with dual cores (ARM Cortex-M4 for DSP/ML computation, Cortex-M0 for sensor/peripheral management)
   - Interfaces: Multiple sensor types, CAN bus connectivity
   - Sized and weighted for deployment on platforms as small as 6 lbs, 5.5 ft wingspan
   - Persistent storage for lifetime component tracking

4. **Network Architecture:**
   - CAN bus with fault-tolerant transceiver (high differential voltage for interference protection)
   - UAVCAN protocol layer for aerospace/robotic reliability and custom message types
   - Supports long payloads for cross-node distributed algorithms
   - Single-wire operation if bus line separated

## Products & Capabilities Described

**SwiftCore Flight Management System:**
- Commercial autopilot designed with modular paradigm
- Supports addition/subtraction of sensors, actuators, payloads without redesign
- CAN bus-based communications with heritage in mission-critical systems
- Can be augmented with proposed monitoring node system

**SwiftPilot Autopilot:**
- Current implementation uses simple boosting algorithms for:
  - Launch detection (4 classifiers: forward accelerometer, airspeed change, pressure altitude, GPS ground speed)
  - Landing impact detection
- Operating history: 1,000+ flights without false negatives on launch detection
- Will interface with new distributed monitoring nodes

**Monitoring Node System (Proposed):**
- Distributable across aircraft subsystems
- Real-time fault detection capability
- Predictive maintenance tracking (analogous to "smart batteries")
- Active component monitoring with usage history and failure statistics

## Use Cases & Applications

**NASA Applications:**
- Arctic operations (Sierra UAS precedent)
- Volcanic plume characterization (DragonEye precedent)
- Severe storm measurements and satellite calibration missions
- Aircraft icing detection and mitigation (new capability)
- Extended BVLOS operations with reduced risk
- Operations by non-expert UAS operators (scientists conducting field campaigns)

**Commercial Applications:**
- Survey and GIS photogrammetry (BST primary market, up to 600 acres per flight)
- Higher-value sensor deployment (GPS RTK, scanning LIDAR) with confidence
- Pipeline and power line inspection with extended range
- NOAA atmospheric science missions (balloon-deployed gliders, higher altitude operations)
- Reduced barrier to entry for small business operators

**Failure Mitigation Examples:**
- Icing conditions: Detect and recommend climb, return-to-base, or immediate landing
- Propulsion loss: Real-time detection enables autopilot reconfiguration for safe landing
- Battery degradation: Predictive remaining flight time, preventive maintenance scheduling
- Servo failure: Real-time detection allows autopilot to switch to backup control surface or safely land

## Key Results (Phase I Interim Status)

**Completion Status:** 50% physical completion as of September 9, 2017

**Deliverables Completed/In Progress:**
1. Requirements specification and design document
2. Identification of critical subsystems and fault tree analysis
3. MATLAB-based environment for parsing flight logs and training ML algorithms
4. Subsystem models developed in MATLAB with statistical noise
5. Sensor requirements identified for failure detection
6. Test data collection initiated (real flight data + simulation data)
7. Machine learning algorithm selection (AdaBoost confirmed)
8. Processing bandwidth evaluation
9. Preliminary monitoring node processor and interface selection

**Technical Work Completed (Task Status):**
- Section 1: Preliminary work (kickoff, requirements, project management)
- Section 2: Critical subsystems identification (in progress—2.3 delayed pending input vector refinement)
- Section 3: ML algorithm development (in progress—algorithm selection and validation)
- Sections 4-6: Design phases (partially underway)

**Cumulative Costs:** $83,167 (4-month period through September 2017)
- Direct labor: $48,700 (PI Elston: 438 hours, Dr. Dixon: 226 hours, Dr. Stachura: 309 hours)
- Indirect costs (overhead 35%, G&A 15%): $26,907
- Profit: $7,561

**Known Issues:**
- Task 2.3 (subsystem model development) delayed due to refinement of input vector for ML algorithms and definition of available sensor data from each subsystem
- Recovery: Later tasks have already begun preliminary work to maintain schedule

## Notable Details

**Competitive Advantages & Heritage:**
- BST team has significant experience with distributed networked systems on small UAS (prior NASA SBIR projects)
- SwiftCore autopilot already demonstrates modular, scalable CAN-based architecture in flight
- Existing large dataset of small UAS flight data (1,000+ flights) for ML training
- Simple boosting algorithm proven reliable across 1,000+ SwiftPilot flights without false negatives

**Commercialization Path:**
- Collaboration with NASA AFRC Center Innovation Fund on electric motor failure detection using fiber optic sensing (FOSS) + machine learning
- Proposed contribution to X-57 electric aircraft project (motor failure detection)
- Commercial focus: Lower barrier to entry for GIS/survey operators, enabling higher-value payloads

**Partnerships & Advisors:**
- NASA Technical Monitor: Ricardo Arteaga
- IoT ecosystem leverage: Use of commercial miniaturized sensors and lightweight networking stacks from IoT market

**Mission Success Metrics:**
- Commercial targets: Reduce partial failures from 15.2% to 5% annually; reduce catastrophic failures from 3.8% to 0.5%
- NASA targets: Reduce partial failures from 7.7% to 5% annually; reduce catastrophic failures from 0% to 2%
- Based on commercial operators flying ~100 missions/year vs. NASA ~10 missions/year

**System Constraints:**
- Must fit on smallest BST platform (6 lbs, 5.5 ft wingspan) to ensure compatibility with legacy and future NASA UAS
- Minimal impact to payload capacity, endurance, and controllability
- Vehicle and autopilot agnostic (applicable to most COTS UAS)

**Phase II Plans:**
- Integration of monitoring system into multiple UAS platforms
- Training of ML algorithms on expanded real-world flight data
- Flight experiments with designed failures to validate detection
- Icing detection algorithm development (using environmental conditions + performance degradation)
- Vision-based GPS-denied navigation (backup during GPS loss/spoofing)
- Extended flight testing and validation of mitigation strategies