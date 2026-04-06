# AF 20.3 - CSO1: Machine Learning Software for Predicting and Improving UAS Maintenance Schedules

## Document Metadata
- Type: SBIR Phase I Proposal - Technical Volume
- Client/Agency: U.S. Air Force
- Program/Solicitation: AF 20.3 - CSO1 (Artificial Intelligence/Machine Learning); Proposal Number FX203-CSO1-1421
- Date: Submitted 2020 (created/modified 2021-02-03 to 2021-05-31)
- BST Products/Systems Referenced: SwiftCore Flight Management System, avionics monitoring system, proprietary monitoring nodes
- Key Personnel: Dr. Jack S. Elston (Principal Investigator, CEO); Dr. Maciej Stachura (CTO, Machine Learning Algorithm Design and Regulatory Expert)

## Executive Summary
Black Swift Technologies proposes developing a machine learning-based predictive maintenance system for UAS to address critical gaps in current UAS maintenance practices, which rely on outdated owner's manual schedules and lack systematic monitoring. The solution leverages unsupervised learning for anomaly detection to flag aircraft operating "out of family" without requiring manually labeled failure data, addressing both USAF mission readiness and commercial safety/insurance cost reduction needs.

## Technical Approach

### Core Technology: Three-Layer Maintenance System
BST proposes building on its existing avionics monitoring system with three complementary approaches:

1. **Direct Tracking for Failures**: Existing onboard system monitoring (failed sensors, low battery, lost comms, etc.)

2. **Supervised Learning**: Statistical methods using labeled telemetry data to detect known failures (servo motors, propellers, weather damage like icing). Outputs directly inform maintenance personnel what needs repair/replacement.

3. **Unsupervised Learning for Anomaly Detection** (Primary Phase I focus): Novel approach using algorithms that build models of normal aircraft behavior across diverse missions and flight conditions, then flag aircraft that deviate from these models. Key advantage: **does not require manually tagged/labeled failure data**, enabling analysis of tens of thousands of flight logs at scale.

### Data & Platform
- **Data Source**: USAF flight logs and telemetry data; supplemented by BST's proprietary monitoring nodes if needed
- **Delivery Platform**: Web-based dashboard with simplified red/yellow/green diagnostic ratings per subsystem; drill-down capability for detailed analysis; designed for non-specialist technicians
- **Analysis Location**: Work performed on BST systems; does not require access to military facilities

## Products & Capabilities Described

### SwiftCore Flight Management System
- BST's highly capable autopilot system
- Serves as technical anchor for avionics work
- Integrated payload interface capability
- Proven in atmospheric sampling campaigns

### Avionics Monitoring System
- Current baseline for Phase I feasibility study
- Collects and stores telemetry data from UAS
- Will be adapted for ML-based predictive maintenance
- Web-based dashboard interface for diagnostics

### Proprietary Monitoring Nodes
- BST-developed sensor/monitoring hardware
- Can be installed on candidate platforms to supplement data collection
- Enable real-time data capture if USAF desires
- Available for use during Phase I trials

## Use Cases & Applications

### Military (Primary)
- UAS mission readiness improvement across USAF fleet
- Prevention of critical failures above populated areas or beyond visual line of sight (BVLOS)
- Reduction of mission failure risk from inadequate maintenance
- Safety improvement for systems carrying fuel or explosive payloads

### Commercial (Dual-Use)
- Small UAS operating in populated areas (reducing insurance costs through demonstrated safety improvements)
- Standard maintenance for commercial UAS operations
- Reduction of maintenance overhead costs
- Vehicle reliability and safety certification benefits

### Key Stakeholder Engagement
- Center for Unmanned Aircraft Systems (Air Force Academy, Department of Electrical and Computer Engineering)
- Dr. George York and Col. Brian Neff identified as primary technical contacts
- AF Life Cycle Management Command (LCMC) and System Program Office (SPO) for fielding/maintenance integration

## Phase I Objectives & Work Plan

### Feasibility Study Duration
90 days maximum

### Task Sequence
1. **Identify and engage potential stakeholders** at Center for Unmanned Aircraft Systems
2. **Explore research areas**: Access UAS flight logs, mission failure records, and performance data to build unsupervised learning datasets
3. **Determine adaptations**: Identify modifications needed to meet Center for Unmanned Aircraft Systems requirements
4. **Engage key stakeholders**: Present adapted solution, seek signed MOUs for Phase II transition
5. **Prepare Phase II transition**: Develop timeline and milestones for prototype delivery

### Deliverables
1. Understanding of Center for Unmanned Aircraft Systems' goals
2. Plan to adapt ML early warning technology
3. Concept for commercializing adapted solution

### Commitment Timeline
- Kickoff meeting within 30 calendar days of contract award
- Monthly progress reports as directed
- Final reports (SF 298 and DD Form 882) upon feasibility study completion

## Key Problem Statement

### Current UAS Maintenance Deficiencies
- **Lack of onboard monitoring**: Most UAS have no systematic state information for critical subsystems (e.g., servo motors operate open-loop, unmonitored)
- **Inadequate documentation**: Maintenance relies on printed owner's manuals with limited scope; contrasts sharply with certified mechanic schedules for manned aircraft
- **Safety risks**: Failures above populated areas or BVLOS can cause injury/death; loss of vehicle, avionics, payload is expensive; systems carrying fuel/explosives present catastrophic risk
- **Data standardization problem**: No standard format for UAS telemetry recording/storage, making flight log collection/analysis extremely time-consuming
- **Manual data tagging burden**: Current ML approaches require laborious manual labeling of failures, preventing scalability

### Competitive Advantage of Proposed Solution
- **No labeled data requirement**: Unsupervised learning enables analysis at scale without manual tagging
- **Dual-use value**: Addresses both military readiness and commercial insurance/safety market
- **Integrated expertise**: BST designs and builds all UAS subsystems in-house, providing unique insight into failure modes
- **Proven platform**: Builds on existing, deployed monitoring system rather than developing from scratch

## Company Background & Commercialization Context

### BST Overview
- Founded 2011, based in Boulder, Colorado
- Specializes in reliable, robust UAS for demanding atmospheric environments (high-altitude, arctic, desert, corrosive particulates, strong turbulence)
- Design and build all aspects in-house: vehicle design, avionics, firmware, algorithms, payload interfacing

### SBIR Track Record
- 11 total SBIR awards (5 Phase II efforts)
- Over $4.3M in non-dilutive SBIR funding earned
- Current major contracts: NASA, NOAA, U.S. Geological Survey

### Commercial Traction
- **2019 Revenue**: $1.5M (achieved without dilutive investment)
- **Soil Moisture Mapping UAS** (NASA SBIR, CCRPP phase): $417,157 in non-NASA commercial investment for commercialization
- Commercial customers demonstrate preference for BST due to capability in difficult flying conditions

### Relevant Prior Work
- Multiple atmospheric sampling campaigns with SwiftCore-based systems
- Tornadic supercell intercepts (VORTEX2)
- Over 100 COA (Certificate of Airworthiness) applications authored
- 300+ flight experiments at CU Boulder involving cooperative multi-aircraft operations and communication-aware information gathering

## Key Personnel Qualifications

### Dr. Jack S. Elston (Principal Investigator, CEO)
- **Education**: Ph.D., University of Colorado Boulder (complex meshed networks, UAS, control algorithms for tornadic supercell in situ sampling)
- **Role at BST**: CEO and technical lead on avionics; creator of SwiftCore autopilot system
- **Experience**: Involved in development of four different UAS; 100+ COA applications
- **Commitment**: Full-time employment, substantial time allocation to project
- **Publications**: "Net-Centric Communication and Control for a Heterogeneous Unmanned Aircraft System" (2009); "A Layered Approach to Networked Command and Control of Complex UAS" (2013)

### Dr. Maciej Stachura (CTO, Machine Learning & Regulatory Expert)
- **Education**: M.S. and Ph.D. Aerospace Engineering, University of Colorado Boulder
- **Experience**: 300+ flight experiments; led NASA AFSRB and Flight Readiness Review Board process for UAS National Airspace System operations
- **SBIR Leadership**: PI for Phase I and Phase II NASA SBIR on soil moisture mapping UAS development and commercialization
- **Publications**: "Communication-Aware Information-Gathering Experiments with an Unmanned Aircraft System" (2017); "L-band Soil Moisture mapping using a suas for validation and calibration of SMAP" (2016)

## Notable Details

### Regulatory & Clearance Status
- No anticipated need for clearances, certifications, or approvals for Phase I
- Will obtain through proper channels if required in Phase II

### Resource Requirements
- Work to be conducted entirely at BST Boulder, Colorado offices
- No military facility access required for Phase I
- No subcontractors or consultants anticipated (engaged defense innovation consultants for proposal documentation/stakeholder identification only)

### Stakeholder Contacts
- **Dr. George York**: george.york@usafa.edu / (719) 333-4210
- **Col. Brian Neff**: brian.neff@usafa.edu / (719) 333-3190

### Significance to Broader USAF Goals
- Research results could impact USAF UAS operations worldwide
- Currently no systematic solution for analyzing flight logs without manual data structuring
- Potential to enable new generation of improved UAS design through better understanding of subsystem performance and failure modes