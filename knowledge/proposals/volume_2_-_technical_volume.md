# AF 20.3 - CSO1 AI/ML Predictive Maintenance for UAS - Phase II SBIR Proposal

## Document Metadata
- **Type:** SBIR Phase II Proposal - Technical Volume
- **Client/Agency:** U.S. Air Force (AFWERX/AFRL)
- **Program/Solicitation:** AF 20.3 - CSO1 (Artificial Intelligence / Machine Learning)
- **Proposal Number:** F2-14757
- **Date:** Submitted 2020 (document modified June 2021)
- **BST Products/Systems Referenced:** SwiftCore FMS, S2 fixed-wing UAS, S0 fixed-wing UAS, E2 multirotor
- **Key Personnel:** Dr. Jack Elston (Principal Investigator, CEO/Founder), Dr. Maciej Stachura (CTO/Machine Learning Lead, Canadian citizen on TN VISA)

## Executive Summary
Black Swift Technologies proposes to develop an AI/machine learning-based predictive maintenance system for unmanned aircraft systems (UAS) operating in both Defense and commercial environments. The system will use unsupervised learning algorithms (specifically GANs and time-series anomaly detection) to analyze flight telemetry data from multiple autopilot systems (SwiftCore, Piccolo, Dronecode derivatives) and alert operators to maintenance needs or reduced operational capability before failures occur. Phase II will demonstrate the system on U.S. Air Force Group 2 fixed-wing aircraft equipped with Piccolo autopilots, integrate AFRL flight data, and validate real-time onboard anomaly detection capabilities.

## Technical Approach

### Problem Statement
- UAS currently have a ~100x higher failure rate per flight hour than general aviation aircraft
- Majority of UAS failures (~80%) are equipment failures rather than pilot error
- UAS lack onboard monitoring and standardized maintenance schedules (unlike manned aircraft with certified mechanics)
- Failures of expensive UAS systems (particularly when carrying $100k+ sensors) result in significant financial loss and safety risks if failure occurs BVLOS or over populated areas
- Current maintenance is ad-hoc with no predictive capability

### Core Technical Solution
**Unsupervised Machine Learning Approach:**
- Uses Generative Adversarial Networks (GANs) specifically designed for time-series data anomaly detection
- Primary ML library: Orion (open-source library for unsupervised time-series anomaly detection)
- Two-step training process:
  1. Train GANs to predict expected outputs (RSSI, propulsion power, control parameters, etc.) based on flight state variables
  2. Use sliding-window comparison of predicted vs. actual output; flag deviations >N standard deviations as anomalies
- Platform-agnostic algorithm development that can be adapted to multiple autopilot systems

### Multi-System Support
The system will integrate data from:
- **SwiftCore** (BST's proprietary autopilot with tight hardware integration)
- **Piccolo** (Cloud Cap; widely used on military Group 2 UAS)
- **Dronecode derivatives** (open-source autopilot used on commercial and military small multirotors)
- **DJI systems** (commercial civilian operations only; separate portal due to Defense restrictions)

### Implementation Architecture
- Cloud-based web portal for log ingestion, analysis, and user interface
- Secure database with role-based access control (separate DoD/commercial instances)
- REST API for end-user custom analysis development
- Optional embedded implementation on aircraft (real-time onboard anomaly detection)

### Novel Sensors
Phase I identified potential for adding small embedded sensors to improve detection:
- **Acoustic sensors** for vibration/failure detection (new to UAS; proven in industrial machinery maintenance)
- **Thermal sensors** for propulsion/power system anomalies
- Potential for controlled failure testing on BST aircraft to create training datasets

## Products & Capabilities Described

### 1. AI Predictive Maintenance Web Portal
**What it is:**
- Cloud-hosted SaaS platform for automated anomaly detection on UAS flight data
- Dual-use (separate Defense and commercial instances)
- Web UI for uploading logs, viewing analysis results, extracting maintenance recommendations
- Machine learning backend performing real-time and batch analysis

**Proposed Use in This Context:**
- AFRL and other DAF customers upload flight logs from Piccolo-equipped Group 2 UAS
- System automatically parses logs and detects maintenance issues matching reported failures
- Demonstrates improved detection performance vs. non-ML baseline
- Eventually integrated into BST aircraft operations monitoring

**Specifications/Performance Claims:**
- Comms subsystem anomaly detection: demonstrates improved failure detection vs. baseline
- Propulsion system detection: 100% accuracy on detecting degraded propulsion; predicts time-of-flight impact to within 5% accuracy
- Focus on minimizing false positives and false negatives
- Currently in early deployment with NASA, NOAA, NREL (free access for testing/feedback)

**Current Commercial Status:**
- Early version deployed to NASA, NOAA, and some commercial BST customers (free access as part of aircraft purchases)
- No revenue realized to date; used to validate utility and work through bugs
- Offered at no cost as part of SwiftCore FMS as value-added selling point

### 2. SwiftCore Flight Management System (FMS)
**What it is:**
- BST's proprietary autopilot/flight management system for UAS
- Offers tight hardware/software integration enabling early anomaly detection

**Use in This Context:**
- Baseline flight data source for algorithm development and training
- Full integration with predictive maintenance algorithms (embedded and cloud-based)
- Competitive advantage: deep understanding of SwiftCore internals enables better fault detection
- Used in 5 flight test demonstrations to validate real-time onboard anomaly detection

**Installed Customer Base:**
- NASA, NOAA, USGS (primarily for extreme environment data collection)
- Growing customer base in research and advanced capability applications
- Partner: Alerion (wind turbine inspection on SwiftCore-equipped E2 multirotor in Europe)

### 3. S2 Fixed-Wing UAS
**What it is:**
- BST's primary fixed-wing unmanned aircraft
- Group 2-equivalent size/capability; designed for challenging atmospheric missions
- Equipped with SwiftCore FMS and customizable sensor payloads

**Use in This Context:**
- Platform for Phase II flight demonstrations and certification for AFRL use
- 5 test flights planned with onboard anomaly detection algorithms
- Test scenarios include simulated degraded propulsion (propeller damage) to validate detection accuracy
- Will be certified for DoD use with documentation of airworthiness, emergency procedures, and maintenance requirements
- All design/manufacturing by BST in Colorado (no foreign components; meets recent DoD requirements)

**Performance Specifications:**
- Designed for high-altitude, arctic, desert, corrosive particulates, strong turbulence
- Previously certified for NASA, NOAA, DOE missions

### 4. S0 Fixed-Wing UAS
**What it is:**
- Another BST fixed-wing platform
- Mentioned for training/support activities

### 5. E2 Multirotor
**What it is:**
- BST's small multirotor platform
- Used in Alerion's wind turbine inspection system (onboard edge AI integration)

## Use Cases & Applications

### Primary Phase II Use Case: AFRL Group 2 UAS Maintenance
- AFRL operates Group 2 (>55 lbs) fixed-wing UAS equipped with Piccolo autopilots
- Use case: Automated detection of maintenance needs from flight logs to improve operational readiness
- Subsystems monitored: communications, propulsion efficiency, control system degradation
- Expected benefit: Prevent costly system losses and improve tactical capability for field commanders

### Secondary DoD Use Case: Travis AFB Security Operations
- 60th Security Forces Squadron at Travis AFB operates Dronecode-based "drone in a box" multirotor ISR systems (tethered and untethered)
- Use case: Remote operations support where AI-based health monitoring improves mission-critical AFB security readiness
- Interest expressed in integrating with SwiftCore for advanced capabilities

### Performance Envelope Identification (AFRL-Requested)
- Novel use case identified during Phase I customer exploration
- System will detect when aircraft/environmental conditions might prevent mission execution
- Techniques for anomaly detection repurposed for performance envelope tracking
- Real-time onboard capability planned for decision support (e.g., auto-terminating a mission if performance degrades below minimum required)

### Commercial Use Cases
- **NASA, NOAA, NREL operations:** Already using early portal version to monitor S2 aircraft operations
- **Commercial UAS operators:** Insurance risk reduction; safety improvement for BVLOS operations in National Airspace
- **High-value sensor protection:** Customers carrying $100k+ payloads benefit from early failure prevention
- **Multirotor service companies:** Automation of tedious log analysis and maintenance scheduling

### Industrial Partnerships
- **Alerion (European partner):** Early adopter using portal to monitor E2 multirotor wind turbine inspection system; expressed strong interest in new Phase II capabilities

## Key Results (Phase I)

### Phase I Feasibility Findings
1. **Confirmed USAF Interest:** AFRL and 60th SFS both confirmed high interest in AI-based predictive maintenance
2. **Data Availability:** AFRL has substantial Piccolo flight logs, maintenance records, and failure reports available for algorithm training
3. **Technical Validation:** Proof-of-concept GAN-based anomaly detection on RSSI (comms subsystem) shows promise vs. prior approaches
4. **Algorithm Development:** Identified time-series GAN techniques with lower false positive rates than traditional supervised approaches
5. **Hardware Integration Opportunity:** Discovered potential for embedded sensors (acoustic, thermal) to augment telemetry-based detection
6. **Integration Challenge Identified:** USAF uses combination of manual logs + multiple software systems for maintenance tracking; ML can help integrate these sources
7. **Dual-Use Potential Confirmed:** Technology applicable to both Defense (Piccolo, Dronecode) and commercial (DJI, others) autopilots

## Phase II Technical Objectives & Key Results

### Objective 1: Integration of Piccolo Flight Data (Months 0-4)
**Deliverable:** System demonstration with AFRL-supplied data (Award + 4 months)
- Automatic parsing of AFRL Piccolo flight logs
- Population of cloud database with AFRL data
- Baseline non-ML algorithm performance established for comparison
- AFRL user logins enabling data upload and analysis viewing

### Objective 2: Anomaly Detection Algorithm Development (Months 4-8)
**Deliverable:** GAN implementation demonstration (Award + 8 months)
- Improved failure/degraded performance detection on comms subsystem vs. baseline
- Algorithm expansion to propulsion and control actuators
- Open API delivery for end-user custom analysis tool development
- Training on BST and AFRL Piccolo datasets

### Objective 3: Real-Time Onboard Performance Envelope Demonstration (Months 8-12)
**Deliverable:** S2 certification + flight tests (Award + 12 months)
- S2 airworthiness certification documentation for AFRL/USAF use
- 5 flight tests with onboard propulsion subsystem anomaly detection
- Subset of flights include degraded propulsion scenarios
- Performance targets:
  - 100% detection accuracy of degraded propulsion anomalies
  - Time-of-flight impact prediction within 5% accuracy

### Objective 4: System Transition to AFRL
**Deliverable:** Final report + training (Award + 13-15 months)
- Working web portal delivered to AFRL for operational use
- Piccolo system support fully integrated
- Training of AFRL end-users on portal operation
- Final technical documentation and user manuals
- Commercialization status update

## Notable Details

### Competitive Advantages
1. **Multi-Autopilot Support:** Only system known to support multiple different flight management systems (SwiftCore, Piccolo, Dronecode derivatives, potential DJI)
2. **Deep Autopilot Knowledge:** BST designs and manufactures complete UAS stack (airframe, avionics, FMS, firmware, comms), enabling better understanding of system failures
3. **Vertical Integration:** Full control over hardware/software stack; no reliance on third-party components vulnerable to embargoes
4. **Existing Deployed Base:** Early portal already in use by NASA, NOAA, NREL; can immediately push Phase II improvements to users
5. **Onboard Edge AI:** Capability to deploy algorithms directly on aircraft (SwiftCore integration) for real-time decision support
6. **Commercial Traction:** Early adopters