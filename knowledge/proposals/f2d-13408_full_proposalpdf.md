# An All-Weather UAS for Persistent Base Security and Rapid Response

## Document Metadata
- Type: SBIR Direct-to-Phase II Proposal
- Client/Agency: United States Air Force (USAF), RGV Command
- Program/Solicitation: AFX246-DPCSO1 (Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies)
- Date: Submitted 05/23/2024 (Cover sheet); Proposal Number F2D-13408
- BST Products/Systems Referenced: S3 (VTOL fixed-wing UAS), S2 (predecessor commercial UAS), SwiftCore avionics system, Vision Processing Unit (VPU - Intel Myriad-X based)
- Key Personnel: Dr. Jack Elston (CEO, Principal Investigator, Corporate Official, Contract Negotiator); Lt Col Michael Kennedy (673d SFS Commander, primary end-user); TSgt Donald Nachand (673d SFS Innovation NCO); MSgt Dustin Spooner (Air Force Security Forces Center lead customer)

## Executive Summary
Black Swift Technologies proposes to enhance its S3 vertical takeoff and landing (VTOL) fixed-wing UAS with advanced autonomous capabilities and computer vision for all-weather base perimeter security and rapid incident response. The S3 will be integrated with automatic target recognition (ATR), ATAK command-and-control compatibility, cold-weather ruggedization, and workload-reduction autonomous features to provide a reliable, weather-agnostic alternative to traditional security force personnel patrols at Air Force bases, with a target cost under $50K per aircraft.

## Technical Approach

### Core System Architecture
- **Platform**: S3 VTOL fixed-wing UAS (derivative of successful commercial S2, currently in late-stage prototype development)
- **Flight Management System**: SwiftCore avionics architecture—modular design with well-defined interfaces enabling integration of third-party components
- **Onboard Computer Vision**: Vision Processing Unit (VPU) based on Intel Myriad-X hardware for real-time machine learning inference
- **Sensor Integration**: Modular payload system with planned integration of HD45 gimbal from Trillium Engineering (EO/IR sensor)

### Key Technical Modifications (Phase II Objectives)
1. **Perimeter Search Capabilities**
   - Integration of EO/IR payload (HD45 gimbal) for primary surveillance sensor
   - Adaptation/implementation of neural networks for automatic target recognition and object classification
   - Machine learning models trained to detect unauthorized personnel and vehicles
   - Performance metric: 100% success rate identifying pre-placed test objects

2. **Mission Data Transmission & C2 Integration**
   - Software interfaces to integrate with Android Team Awareness Kit (ATAK) for command/control and sensor data relay
   - Real-time anomaly detection reporting with minimal latency
   - Compatibility with existing USAF ground infrastructure
   - Continuous data transmission without dropouts during full missions

3. **All-Weather Operational Readiness**
   - Hardware modifications to allow continuous ready-to-launch status in temperatures as low as -20°F or lower
   - Demonstrated operation below -10°F continuous sustained operation
   - Cold-soak resistance (aircraft functional after extended outdoor exposure, not just during flight)
   - Maximum sustained wind/gust testing for takeoff and landing
   - Rain/snow operational capability assessment

4. **Workload Reduction Through Autonomy**
   - Automated preflight self-checks
   - Automated system readiness assessment
   - Automated post-flight checks
   - Mission planning tool allowing new surveillance mission input in under 1 minute
   - Reduction in setup, flight, post-flight, and maintenance operator hours

### Manufacturing & Integration
- All major components (avionics, software, radios, ground systems) designed and manufactured in the United States
- Composite work outsourced to Northwind Composites (Idaho)
- PCB manufacturing to Advanced Assembly (Denver)
- 3D printing to Jaws Tech (Idaho)
- Current production capacity: 2 S3 airframes per month; scalable to 20 per month with additional suppliers
- Design leverages field-proven capabilities from S2 successful deployments

## Products & Capabilities Described

### S3 UAS (Primary Product)
**What it is:**
- Group 2 fixed-wing UAS with vertical takeoff and landing (VTOL) capability
- Maximum takeoff weight: 33 lbs
- Maximum flight time: 90 minutes
- Maximum payload: 5 lbs
- Cruise speed: 45 mph / Maximum speed: 100 mph
- Derivative of commercially successful S2 with heritage in extreme-environment operations

**Proposed Use in This Context:**
- Primary platform for USAF base perimeter surveillance and rapid incident response
- Operates autonomously with minimal operator intervention in all-weather conditions
- Modularity enables quick payload reconfiguration on flight line for varied missions

**Specifications & Performance Claims:**
- All-weather capability proven through heritage in volcano monitoring, Arctic surveys, hurricane observation, tornado flights
- Recent S2 completion of 100+ successful missions in Northern Greenland demonstrates capability in extreme conditions
- User-friendly autonomous operation with terrain-aware navigation
- Onboard computer vision for GPS-denied navigation and hazard detection
- Target cost: under $50K per aircraft
- Price advantage: 2x-5x cost reduction vs. DoD-specific UAS for similar missions

### SwiftCore Avionics System
**What it is:**
- Modular architecture flight management system with well-defined interfaces between intelligent nodes
- Designed exclusively by UAS technology experts
- Open architecture enabling third-party component integration

**Capabilities:**
- Autonomous flight with reduced operator workload
- Subsystem tracking and safety through redundancy
- Preventative maintenance capability
- Automated sensor-driven control
- Field-proven across multiple aircraft types and difficult applications

### Vision Processing Unit (VPU) Integration
**What it is:**
- Intel Myriad-X based onboard computer vision processor
- Real-time machine learning inference capability

**Demonstrated Capabilities:**
- Single-shot detector neural networks for personnel detection
- Semantic segmentation networks for pixel-level image classification
- Safe landing zone selection in engine-out scenarios
- Machine learning-based preventative maintenance and failure detection

### ATAK Integration
**What it is:**
- Android Team Awareness Kit (civilian and military versions available)
- Command and control interface compatible with existing USAF infrastructure

**Proposed Use:**
- Mission-critical information relay to decision-makers
- Integration of S3 sensor data and threat alerts into existing Air Force C2 systems
- Minimal operator training required (leverages existing military/federal workflows)

## Use Cases & Applications

### Primary Use Case: USAF Base Perimeter Security
- **Location**: Joint Base Elmendorf-Richardson (JBER) as proving ground
- **Mission Profile**: Persistent perimeter patrol, incident response, rapid deployment
- **Operating Environment**: Extreme winds (up to 45 mph sustained), temperatures to -30°F, precipitation
- **End-User**: 673d Security Forces Squadron (673d SFS), JBER
- **Customer**: Air Force Security Forces Center (AFSFC), Joint Base San Antonio

### Additional Identified Customers & Interest
- **North Spark at Grand Forks AFB**: MOU highlighting perimeter security UAS issues in inclement weather
- **Royal Spark at RAF Mildenhall**: Letter of support citing severe wind challenges
- **Planned Expansion**: Multiple USAF bases globally (identified as large, sustainable market)

### Non-Defense Commercial Applications
BST's S3 platform maintains compatibility with existing S2 commercial customer base:
- **NASA**: Volcano monitoring, vehicle design, soil moisture mapping, CO₂ detection, aircraft platforms
- **NOAA**: Hurricane observations, soil moisture mapping, aircraft platforms
- **USGS**: Volcano monitoring, soil moisture mapping
- **DOE**: Solar panel inspections (E2 UAS)
- **Embry Riddle**: Wind sensors for manned/unmanned aircraft
- **Alertion**: Wind turbine inspections

Expected expansion into:
- Earth Science missions focusing on severe weather operations where current government/commercial UAS struggle
- Wildfire monitoring and assessment
- Tornado and hurricane research
- Arctic environmental monitoring
- Methane and environmental gas monitoring
- Coastal monitoring

## Key Results (Phase I - Type "Feasibility Study")

### Customer Discovery & Engagement
- **Total Federal Government contact attempts**: 63
- **Successful email contacts**: 30
- **Successful phone contacts**: 6
- **Successful in-person contacts**: 1
- **Unique Federal Government organizations contacted**: 8 (all reached)
- **Unique USAF organizations contacted**: 36

### Primary Deliverable: Requirements Roadmap
Created detailed roadmap and timeline of initiatives required for successful Phase II development, including:
- Customer-specific modifications needed
- Functional requirements and use cases derived from USAF organizations contacted
- Integration pathway with existing command/control systems
- Timeline for validation at JBER

### Stakeholder Identification
- **Primary End-User**: 673d SFS, JBER (Lt Col Michael Kennedy - Commander; TSgt Donald Nachand - Innovation NCO)
- **Customer Organization**: Air Force Security Forces Center, AFSFC (MSgt Dustin Spooner - Lead)
- **Empowerment Level**: High; JBER has evaluated 40+ UAS for this application and identified specific capability gaps
- **Advocacy**: AFSFC has authority to advocate for SFS adoption across functional enterprise

## Phase II Technical Objectives & Key Results (Planned)

### Technical Objective 1: Perimeter Search Capabilities
- Select payload package with pros/cons assessment (HD45 gimbal planned)
- Validate payload performance metrics: sensor range vs. target size, coverage area per flight/hour
- Demonstrate 100% success rate identifying pre-placed test objects using neural networks

### Technical Objective 2: Mission Data Transmission
- Demonstrate S3 sensor data integration through ATAK interface
- Measure data transmission lag and anomaly alert timing
- Demonstrate continuous transmission without dropouts during full mission

### Technical Objective 3: All-Weather Operation
- Successful mission in temperatures below -10°F
- Determine lowest operable temperature
- Maximum sustained wind/gust measurements for takeoff and landing
- Maximum rain/snow operational capability

### Technical Objective 4: Workload Reduction
- Compile operator workload metrics for current systems (setup, flight, post-flight, maintenance)
- Identify and rank areas for automation-driven workload reduction
- Implement changes and test at BST facility and JBER
- Produce one-page assessment of equipment and personnel requirements for daily operations

## Notable Details

### Competitive Advantages & Strategic Positioning
1. **All-Weather Capability**: S3 inherits heritage from systems proven in extreme conditions globally (high-altitude, Arctic, hurricanes, tornadoes, volcanoes)
2. **Modularity & Open Architecture**: SwiftCore avionics enables simplified third-party integration and reduces operator training burden
3. **Cost Competitiveness**: Target $50K per aircraft—2x-5x less expensive than existing DoD-specific UAS for similar missions
4. **Proven Design Heritage**: S2 commercial success provides low technical risk; over 100 missions in Northern Greenland demonstrates extreme-environment reliability
5. **Existing Commercial Traction**: Purchase order for 2 S3 aircraft from University of Maryland Eastern Shore ($150K contract, medical supply cargo delivery); S3 sold to Institute of Arctic and Alpine Research ($48K, moisture/methane mapping mission)

### Intellectual Property Strategy
- Primary protection through trade secrets with customer NDAs
- Patent disclosure and prosecution deferred until Phase III evaluation to avoid defensive positioning in patent litigation
- Several promising research areas identified for potential patent development in conjunction with Phase III

### Supply Chain & Manufacturing
- 3,000 sq ft facility in Boulder, CO with simulation and test equipment
- Completely US-manufactured airframes (composites, PCBs, 3D printing all domestic)
- Current capacity: 2 airframes/month; scalable to 20/month; pathway to higher volumes
- Established relationships with Northwind Composites, Advanced Assembly, Jaws Tech enable rapid scaling

### Financing & Growth Trajectory
- Founded 2011; bootstrapped from founder funding through 2016
- Demonstrated continued growth since 2016 as commercial entity
- Currently planning equity capital raise with investor interest expressed
- Capital Factory accelerator membership providing capital-raising support
- Favorable prospects for capital raise based on team strength, technology, and existing products

### Commercialization Strategy
- **Phase III Pathway**: 673d SFS to coordinate with chain of command through 16th AF and AFSFC for Phase III contract and budget commitments aligned with Phase II completion
- **NDAA UAS