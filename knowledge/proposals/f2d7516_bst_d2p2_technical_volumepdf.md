# An All Weather UAS for Persistent Base Security and Rapid Response

## Document Metadata
- Type: Direct-to-Phase II Technical Volume (SBIR Proposal)
- Client/Agency: U.S. Air Force (specifically 319 Reconnaissance Wing/North Spark Defense Laboratory at Grand Forks AFB)
- Program/Solicitation: AFX234-DCSO2, Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions with a Clear Air Force Stakeholder Need
- Date: Submitted October 2023 (document created 2023-10-23, modified 2023-04-25)
- BST Products/Systems Referenced: S2, S3, SwiftCore avionics, SwiftTab UI, Vision Processing Unit (VPU), HD45 gimbal payload
- Key Personnel: Dr. Jack Elston (Founder/CEO/Principal Investigator), Dr. Maciej Stachura (Founder/CTO/Lead Engineer), Lt Col Michael Dunn (NSDL Director - customer), MSgt Jason Carey (NSDL Collaborative Lead), SrA Shane D. Smith (NSDL Innovation Specialist)

## Executive Summary
Black Swift Technologies proposes to develop an all-weather, autonomous UAS based on the S3 platform for persistent base security and rapid incident response at U.S. Air Force installations. The system will integrate advanced machine learning vision capabilities, weatherproof design for extreme cold/wind conditions, reduced operator workload through automation, and integration with existing Air Force ground systems (ATAK). This addresses a critical Air Force need for 24/7/365 perimeter surveillance and incident response capability independent of weather constraints.

## Technical Approach

### Core Platform & Architecture
- **Base platform**: S3 VTOL (vertical takeoff and landing) fixed-wing UAS, a derivative of the commercially-proven S2
- **Heritage**: Systems designed for extreme environments including high-altitude volcano observations, Arctic surveys, hurricane and fire weather observation, and tornadic thunderstorm intercepts
- **Avionics**: SwiftCore modular avionics system with well-defined interfaces between intelligent nodes, enabling simplified third-party component integration and advanced capabilities (tracking, preventative maintenance, redundancy, automated sensor control)
- **Vision Processing**: Intel Myriad-X Vision Processing Unit (VPU) onboard for real-time machine learning inference

### Four Primary Technical Objectives

**1. Perimeter Search Capabilities**
- Select and integrate EO/IR payload (Trillium Engineering HD45 gimbal or similar) onto S3
- Deploy neural networks for automated detection and classification of objects/threats
- Achieve 100% success rate detecting pre-placed test objects in subscale perimeter search scenario
- Document sensor performance metrics: range vs. target size, coverage area per flight/hour

**2. Mission Data Transmission & Integration**
- Integrate S3 sensor data transmission into Android Team Awareness Kit (ATAK) or similar Air Force ground systems
- Transmit raw video feeds and higher-level threat identification data from onboard neural networks
- Demonstrate continuous data transmission without dropouts
- Measure latency from anomaly detection to operator notification

**3. All-Weather Operations**
- Design and validate hardware modifications enabling continuous mission-ready state in extreme cold
- Test operation at temperatures below -10°F (address Grand Forks AFB's historical lows of -30°F and sustained 45 mph winds)
- Determine lowest operational temperature threshold
- Measure maximum sustained wind and gust capability for takeoff/landing
- Evaluate rain/snow operational limits

**4. Workload Reduction**
- Implement automated preflight self-checks and system readiness monitoring
- Develop automated post-flight checks
- Create flight planning/UI tools enabling perimeter surveillance mission setup in under 1 minute (abstract from waypoint creation)
- Perform 10 consecutive simulated surveillance missions
- Deliver one-page assessment of equipment and personnel workload requirements for daily perimeter security

### Machine Learning & Autonomy
- Leverage existing BST capabilities: single-shot detector neural networks for person detection; semantic segmentation networks for safe automated landing site identification
- Develop object detection/classification networks trained on perimeter surveillance scenarios
- Integrate GPS-denied navigation capability (developed with NOAA) for navigation after GPS failure/jamming
- Implement onboard preventative maintenance and failure detection algorithms

### Integration Requirements
- Open interfaces enabling integration of additional third-party components
- COTS radio communication to ground station and Android tablet
- Software interfaces for command/control through ATAK
- Data pipelines for both machine vision processing and operator relay
- DoD-specific secure data delivery interfaces

## Products & Capabilities Described

### S3 VTOL UAS
**What it is**: Group 2 fixed-wing UAS with vertical takeoff/landing capability; derivative of commercial S2 with added ruggedization and autonomy

**Specifications**:
- Maximum Takeoff Weight: 33 lbs
- Maximum Flight Time: 90 minutes
- Maximum Payload: 5 lbs
- Cruise speed: 45 mph / Max speed: 100 mph
- Target cost: Under $50K per aircraft

**Heritage**: S2 has been commercially sold for 3+ years; used by NASA, NOAA, USGS for volcano monitoring, wildfire assessment, soil moisture mapping, and satellite validation

**Proposed Modifications for This Program**:
1. New EO/IR gimbal payload with neural network-based object detection
2. Hardware ruggedization for outdoor mission-ready operation in temperatures at or below -10°F
3. Radio and software updates for Air Force ground system integration
4. Enhanced onboard autonomy software
5. ATAK integration for operator interface

### SwiftCore Avionics System
**What it is**: Modular avionics architecture with well-defined interfaces between intelligent nodes

**Capabilities**: Enables simplified addition of third-party components, subsystem tracking, preventative maintenance, safety through redundancy, automated sensor-driven control

**Advantage**: Designed and programmed exclusively by UAS technology experts rather than collection of varying-skill programmers

### Vision Processing Unit (VPU)
**Hardware**: Intel Myriad-X

**Function**: Onboard real-time machine learning inference for object detection, classification, and threat identification

### Payload: Trillium HD45 EO/IR Gimbal
**Role**: Primary sensor for perimeter surveillance mission

**Integration**: Mechanical, electrical, and data interfaces to be designed during Phase II

### SwiftTab User Interface
**Current function**: Ground station interface on Android tablet

**Proposed enhancement**: Integration with ATAK (Android Team Awareness Kit / Android Tactical Assault Kit)

## Use Cases & Applications

### Primary Mission: Base Perimeter Security and Incident Response
- **Target application**: Air Force base perimeter surveillance and rapid incident response
- **Key customer**: Grand Forks Air Force Base (319 Reconnaissance Wing/North Spark Defense Laboratory)
- **Requirements addressed**: 
  - 24/7/365 operation independent of weather
  - Minimal operator cognitive load/workload
  - Rapid response capability
  - Integration with existing Air Force procedures and systems
  - All-weather operation particularly critical at northern tier bases (Grand Forks experiences -30°F and 45 mph sustained winds)

### Secondary Applications (Leveraging S3 Heritage)
- **Arctic operations**: Gas monitoring in Arctic, coastline monitoring
- **Volcano monitoring**: High-altitude plume observation
- **Wildfire monitoring and assessment**: Nighttime fire observation capability
- **Tornado and hurricane observation**: Intercept and data collection in severe weather
- **Cargo delivery in extreme conditions**: University of Maryland Eastern Shore use case (medical supply delivery in winter over Chesapeake Bay)

### Non-Defense Government Customers Already Served
- NASA: Volcano monitoring, soil moisture mapping, vehicle design, aircraft platforms
- NOAA: Hurricane observations, soil moisture mapping
- USGS: Volcano monitoring, soil moisture mapping
- DOE: Solar panel inspections
- University customers: Wind sensing, research missions

## Key Results & Metrics

### Testing & Validation Planned for Phase II
The proposal specifies four key demonstration metrics to be achieved by end of Phase II:

1. **Perimeter Search**: 100% success rate completing subscale equivalent perimeter search with automated neural network detection of pre-placed test object
2. **Data Transmission**: Anomalous activity detection with immediate data relay to operator; integration with ATAK demonstrated
3. **Cold Weather**: At least one hour of continuous operation at less than -10°F on site or within 50 miles of Grand Forks AFB
4. **Workload Assessment**: Deliver one-page assessment of UAS equipment and personnel workload requirements for daily perimeter security

### Milestones & Deliverables
- **Month 2**: Finalized customer requirements and updated PRD ($64,085)
- **Month 4**: Preliminary concept & algorithm design with customer feedback ($297,802)
- **Month 8**: Hardware design changes for wireless integration ($124,895)
- **Month 12**: Software and firmware development ($180,531)
- **Month 14**: Functional prototype builds for bench testing ($199,483)
- **Month 15**: Bench-top test plan creation ($225,663)
- **Month 15**: Proof of concept bench testing ($106,675)
- **Month 18**: Final report and field demonstration at Grand Forks AFB ($50,000)

**Total Phase II funding**: $1,249,151 in SBIR funds

### Hardware Deliverables
- S3 aircraft with integrated payload and all modifications
- Sensor package (HD45 gimbal or equivalent)
- Ground support equipment
- Software/firmware package for ATAK integration
- Training materials and operating manual
- Safety documentation (Preliminary Hazard Analysis per MIL-STD-882E)

## Notable Details

### Competitive Advantages vs. Commercial Competitors
- **vs. "drone-in-a-box" solutions** (Skydio, Easy Aerial): Much faster response time, reduced full perimeter inspection time, all-weather operation capability (identified as major pain point with current solutions)
- **vs. other DoD UAS**: Targeted 2-5x price reduction compared to DoD-specific platforms ($50K target vs. higher-cost alternatives)
- **Unique capabilities**: 11 years proven experience in extreme environments; heritage of systems that have flown in some of Earth's harshest conditions

### Market & Commercial Potential
- **Global UAS market**: $20.71B (2018) → $52.30B (2025); CAGR 14.15%
- **Weather instrument market**: $322.86M (2018) → $496.78M (2025); CAGR 6.33%
- **Existing commercial revenue**: $750K from non-Defense S3 sales (last 12 months)
- **Committed orders**: University of Maryland Eastern Shore purchase order for 2 S3 aircraft + support contract totaling $150K for winter cargo delivery operations
- **S2 sales history**: 13 aircraft sold at ~$65K each (aircraft, launcher, ground systems, training)
- **Customer base**: NASA, NOAA, USGS, DOE, Embry Riddle, Alerion, smaller research entities

### Intellectual Property & Commercialization
- **IP Strategy**: Protection primarily through trade secrets; potential patent evaluation if Phase III awarded
- **Commercialization Plan**: 
  - Growth in non-defense markets (Earth science missions with NASA/NOAA/USGS) and defense ISR applications
  - Planned commercial S3 release Q1 2023 (proposal dated late 2023)
  - Phase III strategy: 3400 funding + partnering organizations; potential AFWERX TACFI/STRATFI programs ($1.8M-$15M matching)
  - Rapid transition strategy: Utilize sole source acquisition authority to move S3 prototype to operational environment
  - Long-term goal: Integration into Air Force force protection community's Integrated Base Defense Security System (IBDSS) program of record at Major Command scale

### Stakeholder Engagement
- **End-user commitment**: Lt Col Michael Dunn (NSDL Director), with support from MSgt Jason Carey, MSgt Harland, Captain Daniel Rust, SrA Shane D. Smith
- **Stakeholder exploration results**:
  - 63 total Federal Government contact attempts
  - 30 successful email contacts; 6 successful phone contacts; 1 in-person meeting
  - 8 unique Federal Government organizations reached
  - 36 unique USAF organizations contacted
  - Grand Forks AFB has evaluated 40+ UAS for this application; identified gaps addressed in this proposal

### Manufacturing & Regulatory
- All major S3 components (avionics, software, radios, ground systems) designed and manufactured in U.