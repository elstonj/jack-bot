# Improved UAS Robustness through Augmented Onboard Intelligence: 2017 Phase II Quarterly Report #5

## Document Metadata
- Type: SBIR Phase II Quarterly Progress Report
- Client/Agency: NASA (National Aeronautics and Space Administration)
- Program/Solicitation: 2017 SBIR Phase II; Topic A1.09 "Vehicle Safety - Internal Situational Awareness and Response"
- Contract Number: 80NSSC18C0042
- Date: April 2019 (Q5 Report, covering work through mid-Q5 of 24-month Phase II)
- BST Products/Systems Referenced: S2 aircraft, SwiftCore, SwiftTab, Flight Management System (FMS)
- Key Personnel: Dr. Jack S. Elston (PI), Dr. Maciej Stachura (Machine Learning & Regulatory Expert), Austin Anderson (Project Lead), Brandon Gilles (Machine Vision Expert), Dr. Dixon, Dr. Connors

---

## Executive Summary

Black Swift Technologies is developing an onboard machine learning-based monitoring and diagnostics system for small UAS to improve reliability, subsystem failure tolerance, and enable safer autonomous operations in the National Airspace System. The Phase II effort focuses on building hardware monitoring nodes (actuator, battery, vision, flight management), training ML algorithms to detect common failure modes and maintenance needs, developing an operator interface for alerts, and creating a web-based customer portal for post-flight analysis. As of Q5, the project is 50% physically complete with cumulative costs of $370,267.43.

---

## Technical Approach

### Overall System Architecture
BST proposes a **decentralized network of specialized monitoring nodes** that cooperate with a centralized flight management node:

1. **Monitoring Node Types:**
   - **Actuator Monitoring Node**: Tracks servo performance, health, and lifetime metrics
   - **Battery Monitoring Node**: Monitors battery state of health, charge cycles, degradation
   - **Vision Node**: Runs computer vision algorithms for safe landing site detection
   - **Flight Management Node**: Centralized supervisor integrating data from all nodes and running higher-level algorithms

2. **Communications Backbone:**
   - CAN bus architecture with open-source UAVCAN protocol for inter-node communication
   - UART to CAN interfaces for legacy system integration
   - Designed for integration with both BST avionics and third-party UAS

3. **Machine Learning Approach:**
   - Train algorithms on historical flight data (BST database since 2011) and bench-test data
   - Algorithms classify faults and off-nominal conditions without requiring explicit vehicle models
   - Decentralized architecture allows iterative development and modular testing

4. **Operator Interface & Alerting:**
   - ECAM (Electronic Centralized Aircraft Monitor) style interface in SwiftTab ground station
   - Intuitive fault notification and guided resolution checklists
   - Real-time alerts to autopilot and operator for critical conditions

5. **Web Portal for Post-Processing:**
   - Customer-facing platform for uploading flight logs
   - Cloud-based execution of same ML algorithms for maintenance recommendations
   - Published data format to enable compatibility with non-BST systems
   - Builds growing database for continuous algorithm improvement

---

## Products & Capabilities Described

### S2 Aircraft
- **What it is**: Proven small fixed-wing UAS platform developed by BST under previous NASA SBIR
- **Role in Phase II**: Primary platform for integration and flight testing of the monitoring system
- **Why chosen**: Established flight-proven design with existing avionics; reduces integration risk

### SwiftCore
- **What it is**: BST's embedded autopilot/flight management system codebase
- **Use in project**: Firmware for monitoring nodes leverages existing SwiftCore architecture to reduce development time
- **Key capability**: Provides foundation for distributed computing across nodes

### SwiftTab
- **What it is**: Ground station/operator interface application
- **Phase II enhancement**: Addition of ECAM-style UI components for displaying subsystem status, failure alerts, and guided maintenance procedures
- **Data display**: Framework for intuitive presentation of fault information without overwhelming operator

### NVIDIA Jetson Boards (TX2 and Nano)
- **What it is**: Single-board computers selected for vision node
- **Use case**: Running safe landing detection deep learning algorithms
- **Constraint management**: Benchmarking ongoing to determine power/performance tradeoffs

### Monitoring Node Hardware
- **Smart Servo Interface**: New firmware being developed to interface with instrumented servos; also proposed firmware for tracking lifetime metrics on standard servos via EEPROM
- **Battery Management Chip**: Identified suitable chipset running proprietary monitoring algorithms internally; will replace custom BST software solution
- **Rolling Shutter Camera**: Selected for vision node integration (determined to work without distortion at high-speed flight via testing)
- **USB3 Integrated Camera & Lens**: Ordered for evaluation

---

## Use Cases & Applications

### Primary Failure Modes Targeted
1. **Wireless Communication Failures**: Detect lost-comm events caused by antenna selection, ground station deployment issues
2. **Propulsion System Degradation**: Track motor/ESC/propeller efficiency; identify reversed propellers, chipped propellers, motor winding failures, bent shafts
3. **Actuator Failures**: Servo performance tracking; detect control surface failures before loss of control
4. **Battery Health**: Monitor capacity degradation, charge imbalances, failures
5. **Environmental Hazards**: Aircraft icing detection and mitigation through performance monitoring
6. **Safe Landing Site Detection**: Vision-based identification of safe landing areas with wind estimation

### NASA Applications (Stated)
- **Arctic Operations**: Extension of prior Sierra UAS deployments with enhanced monitoring
- **Volcanic Plume Characterization**: Similar to prior DragonEye campaigns; reduced operational risk
- **Earth Science Missions**: Enable more frequent and capable flight campaigns with reduced maintenance expertise required
- **General Risk Reduction**: Reduce mission failure due to maintenance errors or off-nominal flight handling

### Commercial Applications (Stated)
- **Survey & GIS Operations**: Enable expensive sensors (RTK-GPS, scanning LIDAR) without prohibitive accident risk
- **3D Mapping in Vegetation**: Address areas where photogrammetry fails (dense trees)
- **Enable BLOS Operations**: Reliability improvements support FAA certification for beyond-visual-line-of-sight flights
- **Future Autonomous Flights**: Foundation for fully autonomous operations without human oversight

---

## Key Results (Q5 Report Status)

### Hardware Development Progress
- **Actuator/Battery Nodes**: Firmware refined; digital filtering reduced to minimize signal lag; CAN/UART baud rate increased; new battery management chip identified
- **Flight Management Node**: Critical algorithms explored; decision made on partitioning algorithms between embedded autopilot and high-performance SBC
- **Vision Node**: Jetson TX2 and Nano brought up and benchmarked; rolling shutter camera evaluated in flight test (no corruption detected at high speed); integrated USB3 camera with lens selected

### Algorithm Development Progress
- **Actuator Monitoring**: Quality control algorithms for servo connection validation; long-term lifetime tracking proposed; servo failure detected during flight test (data to be analyzed)
- **Battery Monitoring**: Bench testing completed; no significant difference between new and 30-cycle-tested batteries observed; battery chip approach selected over custom monitoring
- **Propulsion System**: Algorithms for reversed propeller and chipped propeller identification developed and trained; MATLAB implementation completed; Python port in progress
- **Landing Site Selection**: Deep learning network selected; data annotation flow refined; network training with heterogeneous data sources conducted; initial Jetson TX2 optimization benchmarked

### System Testing Progress
- **Servo Bench Testing**: Multiple servos tested continuously via time-series database; mechanical interface refined to minimize wear; no major failure detected yet
- **Battery Bench Testing**: Automatic discharge/manual charge testing conducted; identified risk in autonomous testing (destructive short/arcing); transitioned to battery management chip approach
- **ESC Testing**: Software developed; current estimates poor on ESC side; tachometer validation conducted with appropriate scaling factors; PWM-to-power mapping found variable with battery voltage
- **Motor Testing**: Bench testing setup; destructive testing deferred
- **Propeller Testing**: Reversed and chipped propeller scenarios tested; speed-to-power curves analyzed

### Portal Development Progress
- **Web App**: Completed internal testing phase; supports historical data download, plotting, raw queries, flight data parsing/upload
- **Customer Portal**: Features added to minimize data entry errors; aesthetic design developed; admin vs. customer feature sets determined; expected beta release early next quarter
- **Security**: Security audit undertaken in preparation for beta release

### Project Metrics
- **Physical Completion**: 50%
- **Cumulative Costs** (through 4/12/19): $370,267.43
- **Contract Duration**: 24 months (Q5 status indicates mid-project point)

### Regulatory/Flight Test Planning
- Flight test plan developed based on selected algorithms
- Flight Readiness Review (FRR) preparation underway

---

## Technical Objectives (from Original Proposal)

1. ✓ *Finalize and validate subsystem designs* (Flight Mgmt Node, Vision Node, Actuator/Battery Nodes) - **In Progress**
2. ✓ *Iterative ML algorithm design and testing* - **In Progress** (multiple algorithms at various maturity levels)
3. ✓ *Bench-top and HWIL testing* - **In Progress** (servo, battery, ESC, motor, propeller testing ongoing)
4. ✓ *UI implementation for operator alerts* - **In Progress** (initial mockups complete; ECAM-style framework being implemented)
5. ✓ *Customer web portal deployment* - **Near Completion** (internal testing complete; beta launch imminent)
6. ✓ *Flight validation on S2 aircraft* - **Planned for later in Phase II** (FRR prep underway)

---

## Notable Details

### Competitive Advantages / Differentiation
- **First to implement active part tracking/monitoring for small UAS** (acknowledged by BST team)
- **Historical data advantage**: 8+ years of BST flight data (since 2011) used to train algorithms
- **Phase I results already commercialized**: BST had built alpha online portal during Phase I showing value; algorithms found anomalies autonomously without being explicitly programmed for specific failures
- **System agnostic**: Designed to work with third-party UAS through published data formats
- **Proven regulatory track record**: BST has successfully completed 7 AFSRB/FRRB reviews in prior 3 years

### Technical Risks & Mitigation
- **Risk**: Destructive failure testing dangerous (battery testing incident)
  - **Mitigation**: Transitioned to leveraging proprietary battery management chip instead of custom solution
- **Risk**: ESC provides poor current estimates
  - **Mitigation**: External validation against tachometer; scaling factors applied
- **Risk**: Compute resources on vision node may be limiting
  - **Mitigation**: Evaluation of Jetson TX2 vs. Nano ongoing; possibility of separate supervisory SBC if needed
- **Risk**: Servo failure modes difficult to induce in lab
  - **Mitigation**: Using opportunistic flight test failure data; long-term monitoring approach

### Partnerships/Subcontractors
- **Machine Vision Expert** (Dr. Connors or Brandon Gilles) contributing to Vision Node design and Landing Site Selection algorithm development
- **Other subcontractors** mentioned in kickoff/labor planning but specific names/roles not detailed in Q5 report

### Data Strategy
- Historical data: 8+ years of BST flight logs being mined for training
- Prospective data: Bench testing generating labeled datasets for servo, battery, ESC, motor, propeller failure modes
- Customer data loop: Portal will crowdsource continuous algorithm improvement through customer uploads
- Data publication: Format to be published for ecosystem adoption

### Design Philosophy
- **Agile development**: "Test early, test often" approach with extensive validation throughout
- **Iterative hardware**: Decentralized node architecture allows phased rollout and third-party integration
- **Modular UI**: ECAM framework designed to simplify addition of new fault types
- **Cloud-first ML**: Algorithms developed on cloud resources before embedded deployment (accelerates iteration)

### Regulatory / Flight Test Path
- Flight testing at Pawnee National Grassland planned
- Coordination with NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board (FRRB)
- BST has established process and credibility with these boards
- Flight test plan includes injected failures to validate monitoring system response

---

## Work Remaining (as of Q5 end)

### Q6-Q8 Priorities (per plan)
1. **Q6**: SWIL/HWIL simulation with