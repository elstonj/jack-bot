# Air-deployed Attritable ISR Drone with ATR

## Document Metadata
- Type: Technical proposal (BAA response)
- Client/Agency: Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field Airborne Systems Integration Division
- Program/Solicitation: BAA No. N68335-26-R-0458 (NAWCAD WOLF Airborne Systems Integration BAA)
- Date: Submitted 2026 (document modified April 20, 2026)
- BST Products/Systems Referenced: S0-AD (air-deployed fixed-wing UAS)
- Key Personnel: Jack Elston (PI, CEO Black Swift Technologies), Peter Torrione (Chief Technologist, CoVar - subcontractor), Beck Cotter (Administrative POC)

## Executive Summary
Black Swift Technologies proposes to integrate an automated target recognition (ATR) payload with its proven S0-AD air-deployed Group 1 UAS to create a low-cost, attritable autonomous ISR platform for contested environments. The system combines an EO/IR sensor with CoVar's ACES AI/ML-based ATR software to enable autonomous detection, classification, and geolocating of targets with minimal bandwidth requirements and operator burden, deployable from existing naval aircraft tube-launch infrastructure.

## Technical Approach

**System Architecture:**
- Air-deployed, tube-launched fixed-wing Group 1 UAS (S0-AD platform)
- Nose-mounted gimballed EO/IR camera replacing existing atmospheric sensing payload
- Onboard GPU-based processing hardware for real-time ATR inference
- Low-bandwidth autonomous operation with tactical network integration (CoT, TAK, NTCDL)
- Single-operator control interface with minimal interaction during mission execution

**Development Milestones (24 months):**
1. **M1 (Months 1-6):** Program kickoff and system-level design; define CONOPS, mission requirements, system architecture, performance metrics, and SWaP budgets
2. **M2 (Months 7-16):** Component selection and detailed interface design; select EO/IR sensor and processing hardware; complete mechanical, electrical, and software design modifications
3. **M3 (Months 9-16):** System integration and flight test; fabricate modified S0-AD, integrate payloads, conduct initial flight testing
4. **M4 (Months 12-18):** Mission capability development; implement autonomous search, onboard ATR processing, low-bandwidth transmission, tactical data network integration; develop user interface; validate with representative models
5. **M5 (Months 17-24):** Final demonstration and certification; complete airworthiness and cybersecurity certification, integrate classified ATR models, conduct final flight demonstrations

**Key Technical Milestones:**
- Initial flight test: Month 10
- Final ISR demonstration: Month 22

## Products & Capabilities Described

### S0-AD (Air-Deployed Group 1 UAS)
- **What it is:** US-manufactured fixed-wing unmanned aircraft designed for tube-launch deployment from P-3 aircraft; TRL 9 (mature)
- **Current operational use:** Successfully deployed 50+ times from NOAA P-3 aircraft, including operations in Category 5 hurricanes
- **Performance characteristics:** Demonstrated reliable operation in high winds, turbulence, and precipitation; compatible with existing sonobuoy launch infrastructure without modification
- **Proposed ISR configuration:** Nose-mounted EO/IR gimballed camera replacing original atmospheric sensing payload; onboard GPU processing for real-time target recognition
- **Advantages for ISR:** Proven air-deployed platform reduces transition risk; immediate integration with Navy and maritime patrol aircraft; demonstrated performance in extreme/contested environments

### ACES ATR (Automatic Target Recognition) Payload
- **What it is:** CoVar's AI/ML-based software for real-time detection and classification from EO/IR video streams; TRL 7-8
- **Capabilities:** 
  - Detection and classification of ground vehicles, personnel, unmanned surface vessels, and UAS across varying conditions and complex backgrounds
  - Real-time edge processing on low-SWaP hardware without high-bandwidth communications
  - Enhanced outputs including target pose, orientation, and range estimation
  - Direct integration with tactical systems (CoT, TAK, NTCDL)
- **Development heritage:** Developed through multiple DoD programs (US Army, US Navy, Army Research Laboratory); demonstrated performance in Project Convergence, NATO exercises, and National Training Center events; transitioning into programs of record including Army's XM30 program
- **SWaP optimization:** Specifically designed for edge deployment on low-power GPU hardware with real-time inference capability

### Integrated EO/IR Sensor Package
- **Challenge:** Integration of gimballed EO/IR sensor meeting strict SWaP constraints while maintaining image quality for reliable ATR
- **Risk mitigation:** BST partnerships with camera vendors; prior experience integrating compact sensors on small UAS; vertically integrated avionics architecture enabling system-level optimization of power, compute, and sensor interfaces

## Use Cases & Applications

**Operational Scenarios:**
- **Contested/Denied Environments:** Low-altitude operations within adversary integrated air defense system (IAD) threat rings where manned and large ISR platforms cannot operate
- **Distributed ISR Network:** Scalable multi-platform deployment extending Navy and joint sensor networks into contested regions
- **Maritime Awareness:** Enhanced manned and unmanned airborne payload for maritime situational awareness
- **Stand-in Force Support:** Support for USMC stand-in forces operations

**Specific Tactical Uses:**
- Autonomous target detection and reporting within denied airspace
- Rapid area coverage (>5-10× per sortie via multi-node deployment)
- Operations within adversary Weapons Engagement Zones (WEZ) - low-cost, expendable nature justifies insertion into high-threat areas
- Force multiplication and supporting survivability of nearby protected platforms

**End-User Organizations:**
- Navy Task Force intelligence organizations
- USMC stand-in forces
- SOCOM units
- Potential sponsors: PEO(U&W) – PMA-263 (STUAS) and PEO(A) – PMA-290 (P-8), PMA-299 (H-60), SOCOM AT&L-ST

## Key Performance Claims & Operational Payoff

- **Area Coverage:** >5-10× area coverage per sortie through multi-node deployment
- **Communications Reduction:** >80% reduction in comms bandwidth through onboard ATR processing and only reporting high-value detections
- **Cost Efficiency:** >10× reduction in ISR cost per asset through low-cost, attritable design
- **Operator Workload:** Reduced through autonomous operation and minimal interaction
- **Time to Engagement:** Reduced via direct tactical data network outputs (CoT, TAK, NTCDL)
- **Deployment Speed:** Immediate integration with existing Navy/maritime patrol aircraft infrastructure via sonobuoy launch compatibility

## Technical Challenges & Risk Mitigation

| Challenge | Risk | Mitigation |
|-----------|------|-----------|
| Real-time ATR on low-SWaP hardware | Performance and accuracy loss | Use CoVar's ACES framework (mature, designed for edge deployment); targeted optimization during effort |
| EO/IR sensor integration within SWaP constraints | Insufficient image quality for ATR | BST partnerships with camera vendors; prior experience on small UAS; vertically integrated avionics enabling system-level optimization |

## Technology Readiness Levels
- **Aircraft (S0-AD):** TRL 9 (proven in operations)
- **ACES ATR software:** TRL 7-8 (demonstrated in operationally relevant environments)
- **Integrated system:** Begins at TRL 5-6, advances to TRL 7 through flight testing and operationally relevant demonstrations

## Cost & Schedule

**Total 24-Month Program Cost:** $1,927,856
- **Year 1:** $955,699
- **Year 2:** $972,157

**Cost Breakdown:**
- Direct Labor (BST): $267,868/year
- Subcontractor/Consultants (CoVar): $248,000/year
- Equipment (6 S0 UAS + EO/IR components): $90,000/year
- Materials: $8,000 (Y1), $5,000 (Y2)
- Travel & ODCs: $16,000 (Y1), $32,000 (Y2)
- Overhead (46.67%), G&A (18.32%), Fixed Fee/Profit (7%)

## Future Development
- Coordinated multi-aircraft operations
- Control handoff to other UAS operators
- Adaptive tasking and retasking
- Collaborative sensing across multiple platforms with complementary sensors
- Direct cueing of downstream systems (loitering munitions and other effectors)

## Notable Details

**Organizational Capabilities:**
- BST maintains in-house facilities for design, integration, and flight testing including wind tunnel for component validation, manufacturing and prototyping capabilities for rapid iteration
- CoVar provides computational resources (CPU, GPU, network-attached storage) for data storage, model training, and system evaluation at CUI and SECRET levels
- CoVar maintains TS facility clearance; all personnel cleared to SECRET level minimum

**Competitive Advantages:**
1. **Proven Platform Heritage:** 50+ successful deployments in extreme weather (Category 5 hurricanes) demonstrates reliability in contested/degraded conditions
2. **Infrastructure Compatibility:** Direct compatibility with existing sonobuoy launch infrastructure on Navy/maritime patrol aircraft—no modification required for integration
3. **Mature Component Ecosystem:** All major components (aircraft, ATR software) at TRL 7-9, reducing integration risk
4. **Rapid Transition:** Existing operational deployment infrastructure and demonstrated performance support near-term fielding
5. **Attritable Cost Model:** Low-cost design justifies deployment in high-threat areas where expensive platforms cannot go

**Standards/Integration:**
- Designed for tactical data network compatibility (Cursor-on-Target, Team Awareness Kit, NTCDL)
- Compliance with airworthiness and cybersecurity certification processes (Milestone 5 deliverable)

**Document Status:** Marked as DRAFT; last edited by Daniel Prendergast