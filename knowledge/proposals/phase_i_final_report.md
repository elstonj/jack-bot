# Improved UAS Robustness through Augmented Onboard Intelligence

## Document Metadata
- Type: Phase I Final Report (SBIR)
- Client/Agency: NASA
- Program/Solicitation: 2017 NASA SBIR Phase I (Contract NNX17CD08P)
- Date: September 2017
- BST Products/Systems Referenced: SwiftCore Flight Management System, SwiftPilot autopilot, SuperSwift UAS
- Key Personnel: Dr. Jack S. Elston (Principal Investigator), Dr. Maciej Stachura (Machine Learning Algorithm Design), Dr. Cory Dixon (Wireless Network and Avionics Expert)

## Executive Summary
Black Swift Technologies proposed development of a modular onboard monitoring system using machine learning algorithms to provide early warning of critical subsystem failures on small unmanned aircraft systems (sUAS). The Phase I effort focused on identifying critical unmonitored subsystems prone to failure, developing sensing requirements, designing an intelligent monitoring node, and establishing a distributed network architecture (based on UAVCAN protocol) to communicate fault predictions to both autopilot and operator, enabling safer and more reliable autonomous operations in harsh environments and enabling wider adoption of UAS technology.

## Technical Approach

### System Architecture
- **Modular networked monitoring nodes**: Small, distributed intelligent sensors deployed across the aircraft to observe subsystem operations
- **Machine learning integration**: Onboard processing to classify fault patterns and predict failures before they occur
- **Dual-path alerts**: Notifications sent to both autopilot (for autonomous response) and ground operator (for informed decision-making)
- **Distributed intelligence**: Nodes communicate via CAN bus to share information and coordinate system-wide fault detection
- **Designed constraints**: Limited size, weight, and power (SWaP) to avoid impacting existing vehicle performance

### Data-Driven Approach
- Leverage existing BST flight data: Over 1,000 nominal flight datasets plus datasets with captured propulsion failures, battery issues, and pitot tube clogging
- FAA COA Accident & Incident database (2009-2014): 274 incidents analyzed for failure pattern identification
- Mean Time Between Failures (MTBF) estimates from NASA Airworthiness and Flight Safety Review Boards
- Subsystem models developed in MATLAB with statistical noise based on real flight data
- Lab testing and flight experiments to generate additional training data

## Products & Capabilities Described

### SwiftCore Flight Management System
- Commercial autopilot platform from BST
- Modular design allowing sensor/actuator/payload additions without full redesign
- Uses Controller Area Network (CAN) bus for robust, mission-critical communications
- Heritage in multiple approved NASA missions
- Target interface point for monitoring node alerts and autonomous responses

### SwiftPilot Autopilot
- Existing BST system using simple boosting algorithms for event detection
- Proven heritage: Launch detection (4-classifier system) has never failed across 1,000+ flights
- Demonstrates viability of weak learner boosting approach for real-time classification
- Integrates landing impact detection, engine enable/disable logic

### Monitoring Nodes
- **Processor architecture**: NXP LPC4300 dual-core processor family
  - ARM Cortex-M4 DSP-enabled core for machine learning algorithms
  - Cortex-M0 core for sensor/peripheral management
- **Size/weight constraint**: Must fit on smallest BST UAS (6 lbs, 5.5 ft wingspan)
- **Sensor interfaces**: Expandable architecture for multiple sensor types (currently targeting propulsion, battery, servo, air data systems, structural monitoring)
- **Processing margin**: Sufficient computational headroom for algorithm expansion and future advanced algorithms
- **Storage**: Persistent memory for lifetime component usage tracking and maintenance history

### Network Architecture
- **Protocol**: Controller Area Network (CAN) with UAVCAN application layer
  - CAN: High differential voltage levels provide interference protection
  - Fault-tolerant transceiver guarantees message delivery
  - Single-wire fallback capability if bus line separates
- **UAVCAN benefits**: 
  - Lightweight protocol designed for aerospace/robotic applications
  - Standard message definitions for common sensors, actuators, subsystems
  - Data Structure Definition Language (DSDL) for custom message types
  - Support for long payloads enabling distributed ML data transmission
- **Communication flow**: Node-to-node, node-to-autopilot, node-to-operator (via telemetry)

### Machine Learning Algorithms
- **Approach**: Adaptive Boosting (AdaBoost) combining multiple weak learners
- **Weak learners**: Simple threshold classifiers on individual sensor features
- **Implementation**: On-board processing for real-time detection plus historical trend analysis
- **Training methodology**: N-fold cross-validation on flight datasets
- **Capability**: Detect failures in real-time AND predict degradation before occurrence

## Use Cases & Applications

### NASA Mission Applications
1. **Arctic Operations**: Extension of existing Sierra UAS arctic deployment capability; improved reliability enables longer/more ambitious missions in extreme cold
2. **Volcano Monitoring**: Support for DragonEye volcanic plume characterization; enhanced safety for operations in corrosive/hazardous plume environments
3. **Severe Weather Sampling**: Storm measurement campaigns (existing BST/NASA partnership); detection of icing and wind damage during flight
4. **Satellite Calibration**: Scientific field campaigns requiring high confidence in data collection
5. **Earth Science Missions**: Enable operations by non-expert scientists rather than requiring dedicated UAS pilots
6. **Aircraft Icing Detection**: Identify icing conditions through combined environmental data and performance degradation; enable autonomous return-to-base decisions
7. **Beyond Visual Line of Sight (BVLOS)**: Prerequisite capability for future autonomous monitoring missions (pipelines, power lines, long-distance transects)

### Commercial Applications (Survey/GIS Market)
1. **Photogrammetry missions**: 3D point clouds and orthomosaic imagery for areas up to 600 acres per flight
2. **High-payload operations**: Enable deployment of expensive sensors (GPS RTK, scanning LIDAR) by reducing mission failure risk
3. **Preventive maintenance automation**: Lower operator skill requirements through intelligent maintenance alerts
4. **Multi-aircraft operations**: More confident operation of small commercial fleets

### Specific Failure Detection/Mitigation Examples
- **Propulsion system degradation**: Motor wear, propeller damage detected through power monitoring and thrust analysis
- **Battery health**: Cell damage/degradation detected through cycling history and performance characterization
- **Servo/actuator failure**: Real-time detection enabling autopilot reconfiguration for safe landing before complete loss of control
- **Air data system clogging**: Pitot tube/static port blockage detected through pressure consistency checks and redundancy monitoring
- **Structural fatigue**: G-force monitoring during launch/landing cycles with cumulative stress tracking

## Key Results (Phase I Focus Areas)

### Completed Work
1. **Requirements document**: Captured all specifications for system design and evaluation
2. **Fault taxonomy and probability assessment**: 
   - Identified 5 critical unmonitored subsystem categories
   - Assigned failure likelihood rankings based on FAA database and internal flight data
   - Created fault tree analysis for each failure mode
3. **Subsystem characterization**: MATLAB models created with statistical noise based on real flight data
4. **Sensor requirements specification**: Comprehensive list of required sensors and interfaces for fault detection
5. **Machine learning algorithm selection**: Validated AdaBoost approach using existing SwiftPilot heritage
6. **Monitoring node design**: First-revision PCB design completed for NXP LPC4300 processor
7. **Network architecture design**: UAVCAN protocol validated; messaging scheme defined

### Quantitative Targets Established
- **Commercial operations**: Target reduction from 15.2% partial failures/year to 5%; from 3.8% catastrophic failures/year to 0.5%
- **NASA operations**: Target reduction from 7.7% partial failures/year to 5%; catastrophic failure rate improvement
- **Comparative benchmark**: Target catastrophic failure rate of 500 per 100,000 flight hours (vs. current BST database of ~3,800; vs. General Aviation of 6.7)
- **Mission success improvement**: Transition from 3 failure categories (Success/Partial/Catastrophic) with quantified baseline statistics to improved targets

### Commercial Developments
- **Web portal prototype**: Alpha version created for customers to upload and visualize flight logs
  - Map-based and plot-based data visualization
  - Planned evolution: Integrate ML algorithms to provide maintenance/failure alerts on customer data
  - Serves dual purpose: data collection tool for algorithm training and customer service

### Identified Phase II Deliverables
- Integration of monitoring system on multiple UAS platforms
- Machine learning algorithm training on expanded datasets
- Simulation and flight testing with induced failures
- Validation of mitigation strategies
- Exploration of X-57 project collaboration (motor failure detection in electric propulsion)

## Notable Details

### Regulatory and Safety Context
- Document cites aircraft safety requirements in context of small UAS integration into National Airspace System
- References FAA COA (Certificate of Authorization) incident data
- Positions improved UAS reliability as prerequisite for BVLOS operations and broader regulatory acceptance
- Compares sUAS failure rates to General Aviation benchmarks to establish acceptable safety targets

### BST Technical Heritage
- **Distributed architecture experience**: Multi-year history designing networked onboard systems for sUAS
- **Publish-subscribe network**: Previous auto-detection of vehicle capabilities [Elston 2013 reference]
- **Fault-tolerant design**: Message-based bus protocols with redundancy/multi-node support
- **Flight-proven autopilot**: SwiftPilot with 1,000+ flight hours of launch/landing detection without failure
- **MATLAB analysis pipeline**: Established tools for parsing flight logs and training ML algorithms

### Competitive Positioning
- First known attempt at active component-level monitoring for small UAS ("smart batteries" analogy)
- Addresses gap in small UAS compared to manned aircraft (which have extensive subsystem monitoring)
- Modular approach agnostic to vehicle platform and autopilot vendor
- Certifiable uniform architecture addressing regulatory pathway challenges

### Partnership and Commercialization Strategy
- **NASA collaboration**: Technical Monitor (Ricardo Arteaga) engaged; AFRC Center Innovation Fund proposal submitted
- **FOSS (Fiber Optic Sensing System)**: Concurrent work on electric motor failure detection using fiber optics + ML
- **Commercial customer outreach**: Alpha web portal deployed; plan for data sharing opt-in to continuously improve algorithms
- **Market expansion**: Positioned as enabler for premium payload operations and BVLOS missions in survey/GIS sector

### Cost and Resource Data
- **Phase I budget**: $124,751 total costs (as of December 2017)
- **Labor allocation**: 657 hours (Elston/PI), 340 hours (Dixon), 464 hours (Stachura) over 6-month period
- **Overhead/indirect costs**: 35% overhead + 15% G&A
- **Equipment**: No equipment purchases over $5,000 threshold
- **Subcontracts**: None

### Document Status
- Report completed September 2017; last edited January 2019
- Marked as 100% physical completion as of submission date
- Contained in folder labeled "Completed/Inactive/Unsubmitted Projects" suggesting Phase II may not have proceeded as initially planned
- Part 10 of report appears truncated (section on "Lost Communication" validation methodology is incomplete)