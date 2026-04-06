# Black Swift Technologies - UAS Predictive Maintenance Machine Learning Proposal

## Document Metadata
- **Type:** SBIR Phase I Proposal (Technical Volume 2)
- **Client/Agency:** U.S. Air Force
- **Program/Solicitation:** AF 20.3 - CSO1 (Artificial Intelligence / Machine Learning)
- **Proposal Number:** FX203-CSO1-1421
- **Date:** October 28, 2020
- **BST Products/Systems Referenced:** SwiftCore Flight Management System, proprietary avionics monitoring system, web-based diagnostic dashboard
- **Key Personnel:** Dr. Jack S. Elston (Principal Investigator, CEO); Dr. Maciej Stachura (Chief Technology Officer, Machine Learning & Regulatory Expert)

## Executive Summary
Black Swift Technologies proposes developing a machine learning-based predictive maintenance system for USAF unmanned aircraft systems (UAS) using unsupervised learning for anomaly detection. The Phase I feasibility study will engage stakeholders at the Air Force Academy's Center for Unmanned Aircraft Systems to adapt BST's commercial monitoring system to meet specific USAF mission needs, with the goal of transitioning to a Phase II prototype that eliminates manual data tagging requirements and enables maintenance scheduling at scale.

## Technical Approach

### Core Problem & Solution
- **Problem:** UAS lack onboard monitoring and systematic maintenance. Users rely on printed owner's manual guides; critical components like servos are often unmonitored and open-loop. Telemetry data collection and analysis is time-consuming and unstandardized across platforms.
- **Solution:** Unsupervised machine learning algorithms that build models of normal aircraft behavior across varying missions and flight conditions, then flag flights that violate these models—enabling smarter predictive maintenance without requiring manual data tagging.

### Three-Layer Anomaly Detection Architecture
1. **Direct Tracking for Failures:** Real-time detection of failed sensors, low battery, lost comms, etc. (backbone of maintenance response)
2. **Supervised Learning:** Statistical methods that tie onboard telemetry to specific subsystem failures (e.g., servo motor degradation, propeller damage, icing conditions) to directly inform maintenance personnel what requires replacement
3. **Unsupervised Learning for Anomaly Detection (Primary Phase I Focus):** Flags aircraft for maintenance when performance is "out of family," applicable to whole-aircraft analysis without labeled failure datasets

### Delivery Platform
- Web-based dashboard with simplified red/yellow/green diagnostic ratings for each subsystem
- Drill-down capability for detailed information on specific systems
- Designed for accessibility by non-specialist technicians (not requiring highly skilled UAS personnel)

### Data & Implementation Strategy
- Primary approach: obtain existing USAF flight log and telemetry data for algorithm development
- Secondary capability: BST's proprietary monitoring nodes can be installed aboard candidate platforms to supplement datasets if existing USAF data proves insufficient
- Algorithm work performed on BST systems; data sourcing from USAF stakeholders

## Products & Capabilities Described

### SwiftCore Flight Management System
- Proprietary autopilot system developed and maintained by Dr. Elston
- Technical lead for all avionics work
- Integrates payloads into UAS for scientific research applications
- Supports complex atmospheric sampling campaigns

### Current Avionics Monitoring System
- Existing baseline BST system to be adapted for USAF maintenance applications
- Already tracks subsystem-level failures and communications performance
- Will be enhanced with supervised and unsupervised ML capabilities

### Web-Based Diagnostic Dashboard
- Simplified interface for maintenance decision-making
- Color-coded health status (red/yellow/green) by subsystem
- Hierarchical drill-down for detailed fault information

## Use Cases & Applications

### USAF Mission Needs (via Center for Unmanned Aircraft Systems)
- UAS maintenance scheduling and optimization
- Improving overall UAS capabilities and reliability
- Understanding and preventing UAS failures
- Supporting BVLOS (beyond visual line of sight) operations by ensuring aircraft safety above populated areas
- Addressing risk of fuel and explosive payload malfunctions

### Commercial Applications
- Routine commercial UAS operations in populated areas
- Insurance cost reduction through improved vehicle safety
- Dual-use product with both military and civilian market potential

### Specific Anomaly Detection Examples
- Compromised or failed servo motors
- Damaged propellers
- Severe weather conditions (e.g., icing buildup)
- Communication performance degradation
- "Out of family" performance across entire aircraft

## Phase I Deliverables & Work Plan

### Timeline
- 90-day feasibility study
- Kickoff meeting within 30 calendar days of contract start

### Key Tasks
1. **Stakeholder Identification & Engagement:** Work with Dr. George York and Col. Brian Neff at Air Force Academy's Center for Unmanned Aircraft Systems
2. **Research Exploration:** Access UAS flight logs and mission failure records; understand requirements
3. **Technology Adaptation:** Determine required modifications to BST's current system
4. **Customer Engagement:** Present adapted solution outline; obtain signed MOU for Phase II transition
5. **Phase II Preparation:** Develop timeline and milestone schedule for prototype delivery

### Deliverables
1. Understanding of Center for Unmanned Aerial Systems' goals
2. Adaptation plan for BST's ML early warning technology
3. Commercialization concept for adapted solution
4. SF 298 and DD Form 882 final reports

## Key Personnel

### Dr. Jack S. Elston (Principal Investigator, CEO)
- Ph.D. from University of Colorado Boulder (meshed network UAS and control algorithms for tornadic supercell sampling)
- Technical lead for all BST avionics work
- Developer of SwiftCore Flight Management System autopilot
- Authored 100+ COA (Certificates of Airworthiness) applications
- Directly involved in development of four different unmanned aircraft systems
- Full-time commitment for contract duration
- Published work: Net-centric communication and control for heterogeneous UAS; layered approach to networked command and control

### Dr. Maciej Stachura (Machine Learning Algorithm Design & Regulatory Expert, CTO)
- M.S. and Ph.D. in Aerospace Engineering, University of Colorado Boulder
- 300+ flight experiments including multi-aircraft cooperative flight and VORTEX2 tornadic supercell intercept campaign
- Led NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board process for UAS in National Airspace System
- PI for Phase I and Phase II NASA SBIR on soil moisture mapping UAS (commercialization ongoing)
- Published work: Communication-aware information gathering experiments; L-band soil moisture mapping validation

## Related Work & Company Context

### Company Background
- Founded: 2011, based in Boulder, Colorado
- Focus: Reliable, robust, highly accurate UAS capable of carrying payloads in demanding atmospheric environments (high-altitude, arctic, desert, corrosive particulates, strong turbulence)
- Design philosophy: In-house development of all UAS systems (scientific application boards, algorithms, firmware, vehicle design, construction, payload interfacing)

### SBIR Track Record
- **11 total SBIR awards** including 5 Phase II efforts
- **$4.3M+ in non-dilutive SBIR funding**
- Current contracts with NASA, NOAA, U.S. Geological Survey

### Commercial Revenue & Traction
- **$1.5M revenue in 2019** (achieved without dilutive investment)
- **Soil-moisture mapping UAS:** Currently in CCRPP phase of NASA SBIR program; earned $417,157 in non-NASA commercial investment for further commercialization

### Why Organizations Choose BST
- Proven ability to achieve mission goals in difficult flying conditions (high altitude, arctic, adverse weather, etc.)

## Notable Details

### Partnerships & Stakeholder Engagement
- **Primary AF Academy Partners:**
  - Dr. George York / george.york@usafa.edu / (719) 333-4210
  - Col. Brian Neff / brian.neff@usafa.edu / (719) 333-3190
- Additional target engagement: AF Life Cycle Management Command (LCMC) and System Program Office (SPO)
- Used defense innovation consultants to prepare documentation and identify USAF stakeholders

### Phase II Pathway
- Phase I success contingent on obtaining signed MOU with Center for Unmanned Aircraft Systems and AF Academy
- Phase II prototype will deliver adapted solution meeting Dr. York's and Col. Neff's stated mission goals

### Facilities & Resources
- All Phase I work conducted at BST's Boulder, Colorado offices
- No military facility access required
- No subcontractors or consultants anticipated (defense innovation consultants used only for documentation/stakeholder identification)

### Regulatory & Clearance Status
- No clearances, certifications, or approvals anticipated for Phase I
- Will obtain through proper channels if needed
- Track record of successful AFSRB and Flight Readiness Review Board processes (Dr. Stachura leadership)

### Technology Readiness
- Solution leverages existing BST avionics monitoring capabilities (already operational)
- Unsupervised ML methodology is new area of UAS research—BST has begun applying techniques to communication performance subsystems
- Phase I focuses on scaling these techniques to whole-aircraft analysis without labeled failure data (novel at scale)