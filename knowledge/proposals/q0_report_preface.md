# Improved UAS Robustness through Augmented Onboard Intelligence – Q0 Report Preface

## Document Metadata
- **Type:** SBIR Phase II Quarterly Report (Q0/Preface)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2017 SBIR Phase II, Topic A1.09 "Vehicle Safety- Internal Situational Awareness and Response"
- **Contract Number:** 80NSSC18C0042
- **Date:** October 2018 (Report date); Document created/modified 2018-10-12
- **BST Products/Systems Referenced:** S2 aircraft, SwiftCore, SwiftTab, CAN bus architecture, UAVCAN protocol
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator)
  - Dr. Maciej Stachura (Machine Learning Algorithm Design and Regulatory Expert)
  - Dr. Dan Connors (Computer Vision and Machine Learning Expert)
  - Ricardo Arteaga (NASA Technical Monitor)

---

## Executive Summary

Black Swift Technologies proposes to develop an onboard intelligence system to improve UAS reliability and robustness through networked monitoring nodes, machine learning algorithms, and automated diagnostics. The system will detect potential failures in critical subsystems (communications, propulsion, actuators, power), provide early warning to operators and autopilots, and enable both in-flight mitigation and predictive maintenance scheduling. Phase II will integrate this system onto the S2 aircraft platform, validate algorithms through extensive flight testing, and deploy a customer-facing web portal for post-flight analysis and fleet monitoring.

---

## Technical Approach

**Core Architecture:**
- Decentralized networked monitoring nodes that cooperate with a centralized flight management node
- Four distinct node types: actuator monitoring node, battery monitoring node, vision node, and flight management node
- All nodes share common core architecture based on existing SwiftCore codebase
- Communication backbone: CAN bus with UAVCAN protocol (industry-proven, open-source, supports third-party integration)

**Hardware & Firmware:**
- Small, lightweight, low-power nodes designed to minimize aircraft performance impact
- Vision node: NVIDIA Jetson board with camera interface
- Flight Management Node: runs Linux, processes fusion data, communicates with autopilot and operator
- Nodes interface with various sensors: accelerometers, current/voltage monitors, servo feedback, vision cameras
- Firmware development based on existing SwiftCore codebase to reduce development time

**Machine Learning Approach:**
- Algorithms trained on 6+ years of BST historical flight data (customer and internal flights since 2011)
- Multiple algorithm types developed for different subsystems:
  - Wireless communication performance tracking
  - Battery health classification and remaining flight time estimation
  - Propulsion system efficiency monitoring and motor failure detection
  - Actuator/servo performance tracking and maintenance prediction
  - Landing site selection using vision and wind estimation
  - Aircraft icing detection via off-nominal performance characterization
- Algorithms designed to identify outliers and anomalies without explicit fault signatures
- Data gathering from extensive bench-top testing of failure modes

**Integration & User Interface:**
- Updated communications protocol (UAVCAN extensions) for failure alerts and diagnostics
- Operator interface based on manned aircraft ECAM (Electronic Centralized Aircraft Monitoring) concepts
- Simple, intuitive alerts to avoid overwhelming operators with information
- New UI features in SwiftTab application with fault injection framework for training
- Web-based post-flight analysis: customers upload flight logs for automated assessment and maintenance recommendations

---

## Products & Capabilities Described

### **S2 Aircraft**
- **What it is:** Proven small UAS platform previously developed by BST under a prior NASA SBIR
- **Use in Phase II:** Primary testbed for flight validation of the monitoring system; described as proven platform for conducting scientific campaigns in difficult/dangerous areas
- **Specifications:** Small fixed-wing aircraft designed for extended operations

### **SwiftCore**
- **What it is:** Existing BST avionics/firmware codebase
- **Use in Phase II:** Foundation for monitoring node firmware development; provides basis for common node architecture and CAN bus interface implementation

### **SwiftTab**
- **What it is:** Existing BST user interface application for aircraft operation
- **Use in Phase II:** Will be updated with new UI components for failure alerts, maintenance notifications, and guided fault resolution checklists (based on ECAM model)

### **Monitoring Nodes (Proposed Hardware)**
Four types of specialized monitoring nodes:

1. **Actuator Monitoring Node**
   - Interfaces with servo motors, control surfaces
   - Tracks actuator performance, detects degradation
   - Identifies servo failures (jam, reduced response, drift)
   - Trains algorithms on servo failure modes through bench testing

2. **Battery Monitoring Node**
   - Monitors battery voltage, current, temperature
   - Tracks health over charge cycles, identifies imbalances
   - Classifies remaining flight time and battery condition
   - Detects charging anomalies and cell degradation

3. **Vision Node** (with NVIDIA Jetson)
   - Onboard computer vision processing
   - Safe landing area detection from aerial imagery
   - Wind estimation integration
   - Potential for additional vision-based diagnostics

4. **Flight Management Node**
   - Centralized processing and data fusion
   - Runs onboard Linux; coordinates sensor data from other nodes
   - Communicates with autopilot (S2 avionics)
   - Provides alerts to operator via SwiftTab interface
   - Logs data for post-flight analysis and web portal processing

### **Web Portal**
- **What it is:** Customer-facing online platform for post-flight diagnostics
- **Capabilities:**
  - Customers upload flight log files
  - Runs same machine learning algorithms as onboard system on uploaded data
  - Automatic assessment of communication, propulsion, and other subsystems
  - Maintenance recommendations based on degraded performance detection
  - Fleet dashboard showing historical flight data and health metrics
  - Modular design allowing addition of new monitoring algorithm visualizations
- **Commercial Advantage:** Open data format allows non-BST aircraft operators to participate, expanding market reach
- **Data Utility:** Growing database enables continuous algorithm improvement through anonymized customer data

---

## Use Cases & Applications

### **NASA Applications**
1. **Reduced Training Requirements:** Enables NASA scientists to conduct field campaigns directly without extensive UAS operator training
2. **Arctic/Extreme Environment Operations:** Deploy in high-risk areas (e.g., Sierra UAS in Arctic) with automated icing detection and environmental hazard monitoring
3. **Volcanic Plume Characterization:** Support DragonEye-type missions with enhanced diagnostics reducing flight risk
4. **Earth Science Missions:** Extend mission duration and frequency through automated maintenance management; enable operations in previously considered too-risky areas

### **Commercial Applications**
1. **Survey & GIS:** Enable use of expensive payloads (GPS RTK, scanning LIDAR, photogrammetry) with confidence in aircraft reliability
2. **High-Value Sensor Operations:** Reduce risk of costly payload loss, making advanced sensing economically viable for tree-covered or complex terrain mapping
3. **Beyond Visual Line of Sight (BVLOS) Operations:** Provide safety case for FAA approval through improved failure detection and mitigation
4. **Autonomous Operations:** Support path toward fully autonomous flights without direct human oversight through onboard diagnostics and mitigation
5. **Fleet Management:** Commercial operators can manage multiple aircraft with confidence in maintenance schedules and failure prediction

### **Specific Technical Challenges Addressed**
- **Icing Detection:** Use multi-sensor fusion and machine learning to detect ice accumulation effects on aircraft performance (no existing reliable small-UAS solution)
- **Predictive Maintenance:** "Smart component" concept—monitoring nodes paired with subsystems (analogous to smart batteries) track usage history and recommend maintenance schedules
- **Communications Robustness:** Detect antenna selection errors, deployment failures, and signal degradation
- **Safe Landing Site Detection:** Automated identification of suitable landing areas in emergency scenarios

---

## Key Technical Objectives (Phase II)

1. Finalize and validate designs of actuator/battery monitoring nodes, vision node, and flight management node
2. Develop and train machine learning algorithms for failure identification and landing site detection using augmented datasets
3. Conduct extensive bench-top testing of servo, battery, ESC, motor, and propeller failure modes to generate training data
4. Implement intuitive operator interface features for failure/maintenance alerts (ECAM-style)
5. Deploy customer web portal for algorithm iteration and commercial validation
6. Validate full system through flight testing on S2 with designed-failure experiments and reliability analysis

---

## Work Plan & Schedule

**Duration:** 24 months (8 quarters)

**Major Quarterly Milestones:**

| Quarter | Key Deliverables |
|---------|-----------------|
| Q1 | Requirements finalized; FAA/NASA flight test paperwork submitted; UI/portal mockups; core firmware ready |
| Q2 | Bench testing data collected (actuators, battery, motor, ESC, propellers); vision training datasets generated; customer database designed |
| Q3 | Algorithms developed: actuator monitoring, power system monitoring, landing site selection; web app threading implemented |
| Q4 | Flight Management Node and Vision Node designs completed; portal customer interface developed; beta web app release |
| Q5 | Nodes constructed and validated; operator interface updates; failure alert communication protocol implemented |
| Q6 | Realistic system failures created for SWIL/HWIL; fault injection mechanisms developed |
| Q7 | Flight deployment and validation; reliability analysis vs. historical data |
| Q8 | Final documentation (report, briefing chart, summary report, NTSR) submitted |

**Key Testing Activities:**
- Bench-top testing of all servo, battery, ESC, motor, and propeller failure modes
- Hardware-in-the-Loop (HWIL) and Software-in-the-Loop (SWIL) simulations with fault injection
- Flight Readiness Review (FRR) with NASA/FAA for planned failure injection flights
- Flight testing at Pawnee National Grassland with designed failure scenarios

---

## Project Status (As of Report Date)

- **Contract Number:** 80NSSC18C0042
- **Cumulative Costs (as of 07/13/18):** $71,763.45
- **Estimated Physical Completion:** 12.5%
- **Report Type:** Q0 (Preface/Planning document for Phase II)

---

## Key Personnel & Roles

| Person | Role | Responsibility |
|--------|------|-----------------|
| Dr. Jack S. Elston | Principal Investigator | Overall project management, system design, flight testing coordination |
| Dr. Maciej Stachura | Machine Learning & Regulatory Expert | Algorithm design/training, regulatory reviews, HWIL/SWIL development |
| Dr. Dan Connors | Computer Vision & ML Expert | Vision node design/validation, landing site algorithms, vision algorithm development |
| Ricardo Arteaga | NASA Technical Monitor | Client oversight and requirements validation |

---

## Notable Details & Competitive Advantages

### **Phase I Accomplishments (Foundation for Phase II)**
- Identified critical UAS failure modes from historical data analysis
- Developed initial machine learning algorithms for:
  - Wireless communication range tracking (detected antenna selection errors in past flight data)
  - Battery health and remaining flight time classification
  - Motor/propulsion degradation detection
  - Actuator performance monitoring
  - Aircraft launcher performance tracking
- Built alpha version of web portal for post-flight diagnostics
- Established network architecture (CAN/UAVCAN) for multi-node integration

### **Unique Capabilities**
1. **Historical Dataset:** 6+ years of flight data (customer + internal) since 2011—rare advantage for training robust algorithms
2. **Platform Agnosticism:** Designed for integration with third-party UAS; open data format for web portal allows non-BST aircraft participation
3. **Regulatory Experience:** BST has completed 7 Airworthiness Flight Safety Review Boards (AFSRB) and Flight Readiness Review Boards (FRRB) in prior 3 years—demonstrated expertise in NASA/FAA compliance for UAS flight testing
4. **ECAM-Style Interface:** Adoption of manned aircraft certification standards for operator training and fault resolution, improving commercial credibility and acceptance
5. **Smart Component Concept:** Permanent pairing of monitoring nodes with subsystems (analogous to smart batteries) provides continuous lifecycle tracking—novel for small UAS industry

### **Commercial Strategy**
- Early validation through customer-facing web portal (incentivizes flight data uploads)
- Modular, extensible design (nodes can be added incrementally)
- Open architecture (hooks for third-party UAS) expands market beyond BST platforms
- Published data format encourages adoption by non-BST operators
- Continuous algorithm improvement through anonymized customer data