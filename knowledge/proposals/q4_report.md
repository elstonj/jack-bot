# Improved UAS Robustness through Augmented Onboard Intelligence - 2017 Phase II Quarterly Report #4

## Document Metadata
- Type: NASA SBIR Phase II Quarterly Progress Report
- Client/Agency: NASA (Small Business Innovation Research program)
- Program/Solicitation: NASA SBIR A1.09 "Vehicle Safety - Internal Situational Awareness and Response"; Contract Number: 80NSSC18C0042
- Date: April 2019 (Q4 Report for Phase II)
- BST Products/Systems Referenced: S2 (fixed-wing UAS), S1 (UAS), SwiftCore (avionics core), SwiftTab (operator interface/GCS), CAN bus, UAVCAN protocol
- Key Personnel: Dr. Jack S. Elston (PI), Dr. Maciej Stachura (Machine Learning & Regulatory Expert), Austin Anderson (Project Lead), Brandon Gilles (Machine Vision Expert), Dr. Dixon, Dr. Connors

## Executive Summary
This Phase II SBIR effort develops a networked onboard intelligence system to improve small UAS reliability and robustness through automated fault detection, diagnostics, and maintenance prediction using machine learning algorithms. The system monitors critical subsystems (communications, actuators, power, propulsion) via distributed monitoring nodes communicating over CAN/UAVCAN, with a centralized flight management node fusing data to detect failures and provide early warnings to operators. By Q4, the project was 50% complete with $370,267 cumulative costs; bench testing of failure modes was underway, landing site detection algorithms were being refined, and flight testing planning was in progress.

## Technical Approach

**Overall Architecture:**
- Decentralized networked monitoring nodes (actuator, battery, vision, flight management) communicating via CAN bus and UAVCAN protocol
- Centralized flight management node fuses data from distributed sensors to identify system-wide faults
- Machine learning algorithms trained on historical BST flight data (2011-present) and bench-test generated datasets to classify failures and predict maintenance needs
- Post-flight cloud-based analysis via customer web portal for scalable deployment to non-BST platforms

**Key Technologies:**
- NVIDIA Jetson TX2 processor for flight management node
- Machine vision (semantic segmentation networks) for landing site detection
- CAN bus (industry-proven) + UAVCAN (open-source) for onboard networking
- SwiftCore firmware as baseline for monitoring node development
- Cloud computing for algorithm development before deployment to embedded systems

**Data-Driven Approach:**
- Phase I identified common UAS failure modes from historical incident data
- Algorithms trained on 8+ years of BST flight logs (both internal and customer flights)
- Bench testing of specific failure modes (servo wear, battery degradation, motor/ESC failures) to generate labeled training datasets
- Semi-supervised approach for vision algorithm training (automated annotation + manual review)

## Products & Capabilities Described

### S2 Aircraft
- Fixed-wing small UAS platform used for Phase II flight testing and validation
- Previously developed under NASA SBIR (Soil Moisture Mapping program)
- Primary test bed for the onboard intelligence system
- Proven track record in scientific campaigns in challenging environments

### S1 Aircraft
- Smaller UAS platform used for initial flight testing of specific failure modes (propeller damage, bent motor shaft)
- Baseline for propeller and propulsion testing before scaling to S2

### Monitoring Nodes (Four Types)
1. **Actuator Monitoring Node**: Tracks servo/control surface performance, detects wear and failure modes
2. **Battery Monitoring Node**: Monitors cell voltage, current, temperature; predicts remaining flight time and battery health
3. **Vision Node**: NVIDIA Jetson-based computer vision system for semantic segmentation; performs landing site detection and obstacle identification
4. **Flight Management Node**: Centralized node running primary ML algorithms, CAN bus master, communicates with autopilot and operator

### Algorithms Developed/In-Development
- **Wireless Communication Monitoring**: Detects antenna misconfiguration, reduced link quality, prevented communication losses
- **Propulsion System Monitoring**: Tracks efficiency, detects damaged propellers, degraded motors, payload changes; uses motor current, accelerometer data
- **Actuator Monitoring**: Predicts servo wear and failures; trained on long-duration bench testing (840+ hours per servo)
- **Battery Health Monitoring**: Predicts remaining useful life, detects imbalance, charging issues, long-term degradation
- **Landing Site Selection**: Semantic segmentation-based detection of safe landing areas; trained on aerial imagery with multi-scale annotations
- **Aircraft Icing Detection**: Detects icing conditions through multi-sensor fusion without explicit aircraft model

### SwiftTab Operator Interface
- Updated with ECAM-like (Electronic Centralized Aircraft Monitor) display concepts from manned aviation
- Intuitive fault alert presentation to avoid operator overload
- Guided checklists for resolving detected faults
- Integrated with monitoring system to display maintenance recommendations

### Customer Portal (Web-Based)
- Cloud-hosted platform for customers to upload flight logs
- Runs same ML algorithms for post-flight analysis
- Dashboard displays aircraft fleet status, maintenance recommendations, subsystem health metrics
- Database stores customer flight data and metadata for algorithm improvement
- Open data format to support non-BST UAS platforms
- Beta release planned by end of Phase II

## Use Cases & Applications

**NASA Applications:**
- Reduced training burden for NASA scientists to operate UAS in field campaigns
- Extended operations into previously high-risk environments (Arctic operations, volcanic plume sampling)
- Icing detection for operations in challenging weather
- Improved safety for beyond-visual-line-of-sight (BVLOS) and autonomous flights
- Support for Earth Science missions requiring frequent, reliable UAS deployments

**Commercial Applications:**
- Survey and GIS companies deploying expensive sensors (RTK-GPS, scanning LIDAR) with confidence
- 3D mapping in vegetation-dense areas where photogrammetry fails
- Enabling commercial justification for BVLOS and autonomous operations with FAA
- Reduction of user error and maintenance mistakes in small UAS operations
- Market enablement for higher-value payloads through increased reliability

## Key Results (Q4 Report)

**Completed Work:**
- Actuator and battery management node firmware prototyped and bench-tested
- Servo bench testing conducted: 840+ hours per servo with automated continuous monitoring; identified average aileron servo loading
- Servo test rig upgraded from single-servo to 5-servo parallel testing capability
- Battery failure modes identified; automatic charge/discharge testing harness designed
- Motor failure modes prioritized (long-term wear > catastrophic failures); remote testing facility identification in progress
- Propeller testing approach finalized (flight-only testing due to difficulty replicating in-flight conditions); initial chipped propeller flight test completed on S1
- Propulsion algorithms enhanced with weather compensation and payload weight adjustment; validated against historic S1/S2 data and observed icing conditions
- Landing site detection algorithms significantly improved:
  - Semantic segmentation approach identified and implemented
  - Semi-supervised annotation pipeline developed (automatic + manual review)
  - Two new candidate networks identified with expected performance improvements
  - Initial training pipeline established; new dataset incorporated and scaled for GSD matching
  - Initial training of first new network completed; ready for parameter sweeping
- Customer database refactored and deployed to cloud with security/access control
- Web portal enhanced with database interface, data plotting/download tools, separate production/development versions
- Flight testing applications and safety case documentation prepared for NASA review

**In Progress:**
- Long-term servo testing (targeting 1000+ hours per servo; minimal ongoing effort required)
- Battery bench testing (estimated 3 months duration; software tools adapted from servo testing)
- Landing site algorithm porting to vision node processor; dataset annotation continuing
- Design of flight management and vision nodes

**Project Status:**
- 50% physical completion as of April 12, 2019
- Cumulative costs: $370,267.43
- Major quarterly milestones on track for Q4 completion

## Notable Details

**Heritage and Proven Capability:**
- BST has successfully completed 7 flight safety review boards (AFSRB) and flight readiness reviews (FRRB) in past 3 years
- Demonstrated expertise with NASA regulatory processes; secured FAA and NASA flight permissions previously
- Phase I work provided proof-of-concept for algorithms; already generating customer value through alpha online portal

**Phase I Innovations Leveraged:**
- Quantified UAS failure modes from accident investigation
- Developed initial ML algorithms for comm, battery, motor, propulsion, launcher monitoring
- Designed modular monitoring node architecture with common core
- Assessed onboard network requirements and protocol needs

**Technical Risk Mitigation:**
- Agile development approach: "test early, test often" with extensive bench testing before flight trials
- Iterative hardware-in-the-loop (HWIL) and software-in-the-loop (SWIL) simulation with fault injection capability
- Decentralized architecture allows early implementation of individual subsystems; phased integration reduces integration risk
- Extended bench testing (1000+ hours per component) ensures data sufficiency for ML training

**Commercialization Strategy:**
- Cloud-based portal with open data format enables adoption beyond BST platforms
- Addresses market need for reliability in expensive payload operations
- Supports FAA certification pathway for BVLOS operations by providing maintainability evidence

**Hardware Specifications (as identified):**
- Flight management node: NVIDIA Jetson TX2 processor on commercial carrier card
- Vision node: Jetson-based with machine vision camera interface
- Monitoring nodes: Custom embedded platforms with CAN interface, low SWaP (Size, Weight, Power)
- Network: CAN bus + UAVCAN protocol (open-source, industry-proven)

**Data Scale:**
- 8+ years of BST flight history (internal + customer flights since 2011)
- Bench testing planned: 1000+ hours per servo, ~3 months battery testing, extended motor wear testing
- Vision training: Multiple aerial semantic segmentation datasets incorporated with GSD-scale augmentation

**Regulatory Engagement:**
- NASA technical monitor: Ricardo Arteaga
- Flight testing location: Pawnee National Grassland (Colorado)
- Planning for flight permission application with fault injection provisions