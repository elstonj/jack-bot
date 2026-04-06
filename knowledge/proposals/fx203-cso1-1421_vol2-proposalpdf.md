# AF 20.3 - CSO1 Machine Learning UAS Maintenance Prediction System

## Document Metadata
- **Type:** SBIR Phase I Proposal
- **Client/Agency:** U.S. Air Force (SBIR Program)
- **Program/Solicitation:** AF 20.3 - CSO1 - Artificial Intelligence / Machine Learning
- **Proposal Number:** FX203-CSO1-1421
- **Date:** Submitted 2020 (proposal created/modified May 28, 2021)
- **BST Products/Systems Referenced:** SwiftCore Flight Management System, proprietary avionics monitoring system, unsupervised ML algorithms for anomaly detection
- **Key Personnel:** Dr. Jack S. Elston (Principal Investigator, CEO), Dr. Maciej Stachura (CTO, Machine Learning Algorithm Design and Regulatory Expert)

## Executive Summary
Black Swift Technologies proposes a feasibility study to develop a machine learning-based predictive maintenance system for small unmanned aircraft systems (UAS) using unsupervised learning for anomaly detection. The system will analyze flight telemetry data to identify aircraft operating outside normal parameters and recommend maintenance before critical failures occur, addressing a significant capability gap in USAF UAS fleet maintenance and reliability.

## Technical Approach

### Problem Statement
- UAS systems typically lack onboard monitoring or systematic maintenance schedules
- Users rely on limited guidance from owner's manuals
- No standardized telemetry data recording/storage across UAS platforms
- Manual data tagging for machine learning is time-consuming and labors-intensive
- Current state: no system can analyze flight logs at scale without pre-labeled failure data

### Proposed Solution
Three-tiered maintenance tracking system:

1. **Direct Tracking for Failures:** Real-time detection of sensor failures, low battery, lost comms, etc. (current capability)

2. **Supervised Learning:** Statistical methods using labeled telemetry data to identify known failures
   - Detect compromised/failed servos, damaged propellers, severe weather conditions (icing)
   - Provides actionable output for grounding aircraft and directing maintenance

3. **Unsupervised Learning for Anomaly Detection (PRIMARY PHASE I FOCUS):**
   - Build behavioral models of how aircraft should perform across varied missions and flight conditions
   - Flag aircraft operating "out of family" without requiring labeled training data
   - Enable analysis of tens of thousands of flight logs without manual tagging
   - Represents new capability not previously achievable at scale

### Baseline Technology
- Current avionics monitoring system as foundation
- Web-based dashboard delivery with red/yellow/green diagnostic ratings by subsystem
- Drill-down capability for detailed subsystem information
- Designed for accessibility by non-expert UAS technicians

### Implementation Approach
- Leverage existing USAF-collected avionics data
- If insufficient, deploy BST-developed monitoring nodes (proprietary avionics) on candidate platforms
- Algorithm work performed on BST systems
- Real-time analysis and feedback capability available

## Products & Capabilities Described

### SwiftCore Flight Management System
- Proprietary autopilot system developed by BST
- Serves as technical anchor for avionics work
- Enables payload integration for scientific research
- Has been demonstrated through multiple atmospheric sampling campaigns

### Proprietary Avionics Monitoring System
- Real-time monitoring nodes for subsystem state tracking
- Critical component monitoring (e.g., servo motors—typically open-loop and unmonitored in UAS)
- Data collection from multiple telemetry streams
- Web-based dashboard interface for maintenance personnel

### ML Anomaly Detection Software
- Unsupervised learning algorithms
- Scales to analyze large datasets (tens of thousands of flights)
- No requirement for pre-labeled failure data
- Behavioral anomaly detection across aircraft platforms
- Real-time and post-flight analysis capability

## Use Cases & Applications

### Defense Applications
- USAF small UAS fleet maintenance optimization
- Mission-readiness assurance
- Airspace dominance through improved UAS reliability
- Prevention of failures above populated areas and beyond visual line of sight (BVLOS)
- Safety-critical: prevents loss of life from in-flight failures (especially for UAS carrying fuel or explosive payloads)

### Commercial Applications
- Routine flight operations in populated areas
- Insurance cost reduction through improved safety
- Maintenance overhead reduction
- General aviation UAS operators

### Specific Stakeholders Identified
- Center for Unmanned Aircraft Systems (Air Force Academy, Department of Electrical and Computer Engineering)
- Air Force Life Cycle Management Command (LCMC)
- System Program Offices (SPO) responsible for fielding and maintaining UAS

## Phase I Work Plan

### Scope
- Engagement with Dr. George York and Col. Brian Neff at Center for Unmanned Aircraft Systems
- Identify specific AF mission needs in UAS maintenance
- Develop adaptation plan for commercial monitoring system
- Seek stakeholder interest at LCMC and SPO levels

### Tasks (5-Task Structure)
1. **Identify and engage potential stakeholders** - Focus on USAF maintenance, capabilities improvement, failure prevention
2. **Explore research areas** - Access to UAS flight logs and mission failure records for unsupervised learning dataset development
3. **Determine adaptations** - Customize technology to meet Center requirements
4. **Identify and engage key stakeholders** - Present adapted solution; target signed MOU
5. **Prepare Phase II transition** - Timeline, milestones, prototype delivery plan

### Deliverables (90-day feasibility study)
1. Understanding of Center for Unmanned Aircraft Systems' goals
2. Plan to adapt ML early warning technology
3. Commercialization concept for adapted solution

### Key Milestones
- Kickoff meeting within 30 calendar days of contract start
- Monthly progress reports/slide presentations
- Final reports (SF 298 and DD Form 882)
- Target: Signed MOU with AF Academy for Phase II progression

## Related Work & Background

### Company Background
- **Founded:** 2011, based in Boulder, CO
- **Core Business:** Design and manufacture of reliable, robust, highly accurate UAS
- **Capability Focus:** Payloads and sensitive instrumentation in demanding atmospheric environments (high-altitude, arctic, desert, corrosive particulates, strong turbulence)
- **In-house Development:** All aspects of UAS systems including scientific boards, algorithms, firmware, vehicle design, construction, payload interfacing

### SBIR Track Record
- **Total Awards:** 11 SBIR awards (including 5 Phase II efforts)
- **Non-dilutive Funding:** Over $4.3M through SBIR
- **Current Contracts:** NASA, NOAA, U.S. Geological Survey

### Notable Related Project
**Soil-Moisture Mapping UAS (NASA SBIR)**
- Currently in CCRPP phase
- Commercial traction: $417,157 in non-NASA investment for commercialization
- Demonstrates proven ability to transition research to commercial products

### Key Publications (Related Work)
- Jack Elston et al., "Net-Centric Communication and Control for a Heterogeneous Unmanned Aircraft System," Journal of Intelligent and Robotic Systems, 2009
- Jack Elston & Maciej Stachura, "A Layered Approach to Networked Command and Control of Complex UAS," Handbook of Unmanned Aerial Vehicles, 2013
- Maciej Stachura & Eric W. Frew, "Communication-Aware Information-Gathering Experiments with an Unmanned Aircraft System," Journal of Field Robotics, 2017
- Dai, Gasiewski, Stachura, Elston, "L-band Soil Moisture mapping using a sUAS for validation and calibration of SMAP," IEEE IGARSS, 2016

## Key Personnel

### Dr. Jack S. Elston – Principal Investigator, CEO
- **Education:** Ph.D., University of Colorado Boulder (meshed network UAS and control algorithms for tornadic supercell sampling)
- **Role at BST:** CEO and technical lead for all avionics work; creator of SwiftCore Flight Management System
- **Experience:** Involved in development of 4 different UAS; author/co-author of 100+ COA applications
- **Commitment:** Full-time employment; substantial commitment to project success
- **Expertise:** UAS design, flight management systems, networked UAS control

### Dr. Maciej Stachura – CTO, Machine Learning & Regulatory Expert
- **Education:** M.S. and Ph.D., both in Aerospace Engineering, University of Colorado Boulder
- **Background:** 300+ flight experiments including multi-aircraft cooperative flight, VORTEX2 (first tornadic supercell intercept)
- **Regulatory Experience:** Led NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board for NAS-certified UAS
- **SBIR Leadership:** PI for Phase I and Phase II NASA SBIR soil moisture mapping UAS
- **Expertise:** ML algorithm design, UAS flight operations, regulatory compliance, atmospheric research

## Notable Details

### Commercial Viability Already Demonstrated
- **2019 Revenue:** $1.5M
- **Customer Base:** NASA, NOAA, DOE, various commercial entities
- Achieved viability without dilutive investment

### Competitive Advantages
- In-house design and manufacturing of all UAS components
- Proven experience in demanding atmospheric environments
- Established relationships with multiple government agencies
- Track record of technology transition to commercial products
- Deep expertise in avionics and flight management systems
- CTO regulatory expertise (AFSRB/FRB experience)

### Dual-Use Appeal
- Defense application: USAF fleet maintenance and mission readiness
- Commercial application: Insurance cost reduction, routine BVLOS operations in populated areas
- Strategy explicitly frames this as "strong dual-purpose product that will not rely solely upon the USAF ongoing support"

### Stakeholder Engagement Strategy
- Direct contact established with Center for Unmanned Aircraft Systems (USAFA)
- Dr. George York: george.york@usafa.edu / (719) 333-4210
- Col. Brian Neff: brian.neff@usafa.edu / (719) 333-3190
- Clear path to MOU and Phase II through identified champions

### Facilities & Resources
- All Phase I work in BST Boulder, Colorado offices
- No military facility access required
- No subcontractors anticipated (defense innovation consultants assisted with documentation/stakeholder identification only)

### Technology Readiness Assessment
- Unsupervised learning for anomaly detection: Emerging area; BST has begun application to specific subsystems (e.g., communication performance)
- Primary Phase I goal: Demonstrate full-aircraft anomaly detection at scale—representing technology maturation beyond current state-of-art
- Supervised learning for maintenance: Already operational, being continuously enhanced
- Direct failure tracking: Established baseline capability