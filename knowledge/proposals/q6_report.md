# Improved UAS Robustness through Augmented Onboard Intelligence - Q6 Report

## Document Metadata
- **Type:** Quarterly Progress Report (Q6 of Phase II SBIR)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2017 SBIR Phase II, Topic A1.09 "Vehicle Safety - Internal Situational Awareness and Response"
- **Contract Number:** 80NSSC18C0042
- **Date:** October 2019 (Report covers Q6 of 24-month Phase II)
- **BST Products/Systems Referenced:** S2 UAS, S1 aircraft, SwiftCore, SwiftTab, CAN bus architecture, UAVCAN protocol
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator)
  - Dr. Maciej Stachura (Machine Learning Algorithm Design and Regulatory Expert)
  - Austin Anderson (Project Lead)
  - Brandon Gilles (Machine Vision Expert)
  - Dr. Dan Connors (Computer Vision/Vision Node Subcontractor)
  - NASA Technical Monitor: Ricardo Arteaga

## Executive Summary
Black Swift Technologies is developing an onboard intelligent monitoring system for small UAS that provides early fault detection, predictive maintenance alerts, and autonomous diagnostics through networked monitoring nodes and machine learning algorithms. The Phase II effort aims to integrate this system onto the S2 aircraft platform and develop a customer-facing web portal for post-processing analysis, with extensive flight validation planned. As of Q6 (October 2019), the project is 75% complete with cumulative costs of $553,852.

## Technical Approach

### Core System Architecture
BST proposes a **decentralized-centralized hybrid architecture** combining:
- **Multiple specialized monitoring nodes** (actuator, battery, vision, flight management) operating independently
- **Central flight management node** for system-wide awareness and correlation of multi-subsystem issues
- **Robust onboard communication bus** using industry-standard CAN architecture and open-source UAVCAN protocol
- **Machine learning algorithms** running both onboard and in post-processing to detect anomalies and predict failures

### Key Technical Components

**Hardware Development:**
- Four distinct monitoring node types sharing common core firmware (based on SwiftCore)
- Flight Management Node: High-performance central processor running Linux-based algorithms
- Vision Node: NVIDIA Jetson board with camera interface for landing site selection and environmental hazard detection
- Actuator/Battery/Motor/ESC monitoring nodes: Small, lightweight specialized sensor interfaces via CAN bus
- All nodes designed for minimal weight/power impact on aircraft performance

**Software & Algorithms:**
- Phase I validated algorithms for:
  - Wireless communication subsystem performance tracking
  - Propulsion system efficiency monitoring and degradation detection
  - Battery health classification
  - Motor failure detection
  - Actuator performance monitoring
  - Aircraft launcher tracking
- Phase II expansion to include:
  - Icing detection (via multi-sensor fusion)
  - Safe landing site detection and selection
  - Predictive maintenance scheduling
  - Servo/propeller failure detection

**Operator Interface:**
- ECAM (Electronic Centralized Aircraft Monitor) system-based UI design for SwiftTab application
- Intuitive pop-up checklists and guidance flows for handling off-nominal conditions
- Real-time and post-flight diagnostics displays

**Commercialization Vector:**
- Online portal for customers to upload flight logs
- Cloud-based machine learning analysis (same algorithms as onboard)
- Cumulative database of flight data for continuous algorithm improvement
- Published data format allowing integration with non-BST UAS platforms

## Products & Capabilities Described

### S2 UAS
- **What it is:** BST's proven fixed-wing unmanned aircraft system
- **Use in this project:** Primary flight test platform for validation of monitoring system
- **Heritage:** Previously developed under NASA SBIR; proven for scientific missions including soil moisture mapping
- **Role:** Extensive flight testing with injected failures to validate algorithms and hardware integration

### S1 Aircraft
- **What it is:** Smaller BST UAS platform
- **Use in this project:** Initial integration platform for vision node before deployment to S2

### SwiftCore Avionics/Flight Management System
- **What it is:** BST's existing flight management and autopilot system
- **Use in this project:** 
  - Communication protocol backbone (proprietary BST protocol)
  - Firmware development baseline for new monitoring nodes
  - Integration point for all monitoring system data
  - Updated to display new machine learning-based diagnostics

### Monitoring Nodes
Four specialized node types developed:

**Flight Management Node:**
- Central processing hub
- Runs primary machine learning algorithms for system-level analytics
- Interfaces with autopilot and operator communications
- Linux-based OS for computational capacity

**Vision Node:**
- NVIDIA Jetson-based processor
- Camera input for safe landing site detection
- Real-time environmental hazard detection
- Integrated with main FMS via CAN bus

**Actuator Monitoring Node:**
- Tracks servo/control surface performance
- Detects actuator failures and degradation
- Maintenance recommendations

**Battery Management Node:**
- Battery health and state monitoring
- Imbalance detection
- Degradation tracking over time
- Integration with battery management IC

**Propulsion System Monitoring:**
- Motor performance tracking
- ESC parameter monitoring
- Propeller condition assessment (chip detection, imbalance)
- Efficiency trending for predictive maintenance

### CAN Bus / UAVCAN Network
- **What it is:** Industry-proven communication backbone
- **Use in this project:** Interconnection of all monitoring nodes; data fusion point
- **Advantage:** Open standard allowing third-party integration

### SwiftTab Ground Station Software
- Operator interface application
- Updated to display ECAM-style failure alerts
- Integration of machine learning algorithm results

### Customer Portal (Web Application)
- **Purpose:** Post-flight log analysis and fleet monitoring
- **Features (developed/in-development):**
  - Flight data upload and storage
  - Dashboard view of fleet health status
  - Machine learning algorithm results visualization
  - Predictive maintenance recommendations
  - Drill-down pages for detailed analysis
  - Modular widget design for algorithm visualization
- **Database:** Customer details, log files, algorithm hyperparameters
- **Scalability:** Threaded implementation for multi-user support

## Use Cases & Applications

### NASA Applications
1. **Arctic Operations** - Deployment of S2 in harsh environments (e.g., Sierra UAS Arctic missions) with enhanced reliability monitoring
2. **Volcanic Plume Characterization** - DragonEye-type missions with icing detection and environmental hazard awareness
3. **Earth Science Missions** - Long-duration campaigns requiring autonomous anomaly detection and maintenance scheduling
4. **Reduced Operator Training** - Enable scientists (non-UAS experts) to safely operate vehicles through automated diagnostics

### Non-NASA Commercial Applications
1. **Survey and GIS Operations** - Operators using expensive payloads (GPS RTK, scanning LIDAR) with confidence in system reliability
2. **Pipeline Inspection** - Potential energy sector partnerships (mentioned in Q6 report)
3. **3D Mapping in Challenging Terrain** - LIDAR use in vegetated areas previously avoided due to high crash risk
4. **BVLOS (Beyond Visual Line of Sight) Operations** - Enabling FAA approvals through demonstrated reliability and autonomous failure mitigation
5. **Fully Autonomous Missions** - Groundwork for unmanned operations without direct human oversight

### Specific Failure Modes Addressed
- Lost communication events (wireless subsystem monitoring)
- Servo/actuator failures (performance tracking, maintenance prediction)
- Motor degradation (efficiency trending, failure detection)
- Battery failures (cell imbalance, capacity degradation)
- Propeller damage (chip detection, imbalance detection)
- Aircraft icing (multi-sensor fusion detection)
- Unsafe landing sites (vision-based detection and safe zone identification)
- ESC overheating/overcurrent
- Bent motor shafts
- Failed motor windings

## Key Results (Q6 Report)

### Completed/In-Progress Technical Activities

**Hardware Development (Section 2.0):**
- Battery management node: Firmware development ongoing with new battery management IC
- Flight Management Node: Sizing and algorithm development completed; options defined
- Vision Node: Hardware assembled and integrated; initial safe landing algorithms evaluated
- Integration path identified: Initial S1 aircraft test before S2 deployment

**Machine Learning Algorithm Development (Section 3.0):**
- **Communications Subsystem Monitoring:** Significantly advanced; algorithms developed to monitor range and link quality
  - Phase I example: Identified cases of reduced performance from incorrectly selected antennas or undeployed ground station antenna
- **Propulsion System Monitoring:** Finalized algorithms; deployment to customer portal in progress
  - Detected efficiency outliers corresponding to payload configuration changes
  - Consistent performance baseline established across similar systems
- **Landing Site Selection Algorithm:** Significant development with improved training using BST image data and algorithm porting to vision node
- **Servo/Propeller Monitoring:** Algorithms based on comms monitoring approach being explored for chipped gear detection

**Operator Interface (Section 4.0):**
- SwiftTab application updated with ECAM-style messages (limited initial set; more planned)
- UI framework designed for failure resolution guidance flows

**Customer Portal (Section 6.0):**
- **Beta release conducted** with initial users identified
- New features added based on early feedback
- Portal development transitioned toward aircraft-centric model
- Views for machine learning algorithm results under development
- Hosting and database infrastructure established

**Field Testing & Commercialization (Section 8.2):**
- **Greenland Flight Campaign:** Early beta deployment with S2 UAS for difficult mission
  - BST algorithms used by team relatively new to UAS operations
  - Improved safety and aircraft performance monitoring
  - Post-processing algorithm insights gathered
  - Important validation of practical system utility
- **Press release and video** on safe landing algorithm performance
- Energy sector partnership exploration for pipeline inspection applications

### Project Status
- **Physical Completion:** 75% (as of October 2019)
- **Cumulative Costs:** $553,852 of planned budget
- **Schedule:** On track for Q8 completion (final report and deliverables)

### Quarterly Milestones Achieved
The Q6 report is the quarterly milestone report itself, covering completion of Tasks 2.0-6.0 preliminary phases with:
- Hardware design finalized for all node types
- Algorithms refined and being deployed
- UI/portal development with beta user feedback
- Flight testing preparation underway

## Notable Details

### Phase I Foundation
The Phase II work builds on Phase I accomplishments including:
1. **Quantification of UAS failures** - Analysis of root causes to prioritize monitoring targets
2. **Machine learning algorithm validation** - Using 8+ years of BST flight data (2011-2019) from internal and customer flights
3. **Monitoring node architecture** - Common firmware core reduces development time
4. **Onboard network specification** - Assessment of data flow requirements completed

### Competitive Advantages
- **Historic flight database** - 8+ years of real operational data for algorithm training and validation
- **Proven platform (S2)** - Extensive flight test heritage; multiple successful NASA AFSRB/FRRB reviews (7 times in 3 years)
- **Multi-domain expertise** - Team includes ML specialists (Dr. Stachura), computer vision (Dr. Connors), avionics (Dr. Elston)
- **Commercialization pathway** - Early beta deployment in Greenland demonstrated practical value
- **Platform agnosticism** - Designed for integration with third-party UAS through published data formats

### Regulatory & Safety Approach
- **FAA/NASA experience** - Multiple successful Flight Readiness Reviews and Airworthiness Flight Safety Review Board approvals
- **Fault injection testing** - Plan to deliberately induce failures in flight for algorithm validation
- **ECAM-based design** - Proven human factors approach from manned aviation
- **Incremental deployment** - "Test early, test often" Agile approach minimizes risk

### Risk Management
Phase I risks reviewed and mitigated; additional risks identified and tracked:
- Mitigation strategies defined for algorithm performance in novel failure modes
- Sensor selection validated through bench testing
- Processing bandwidth/power requirements assessed

### Subsystem Failure Testing
Extensive bench-top testing planned/in-progress (Section 5.0):
- Servo failure modes (40 hours planned)
- Battery failure modes (40 hours)
- ESC failure modes (40 hours)
- Motor failure modes (40 hours)
- Propeller failure modes (40 hours)
- Data collected for machine learning training and validation

### Commercialization Strategy
**Online Portal Model:**
-