# Air-deployed Attritable ISR Drone

## Document Metadata
- **Type:** BAA Proposal (Broad Agency Announcement response)
- **Client/Agency:** Naval Air Warfare Center Aircraft Division (NAWCAD) Webster Outlying Field, Airborne Systems Integration Division
- **Program/Solicitation:** NAWCAD WOLF Airborne Systems Integration BAA; BAA No. N68335-25-R-0458
- **Date:** 2026-04-16 (submission/modification date)
- **BST Products/Systems Referenced:** S0-AD (air-deployed fixed-wing UAS)
- **Key Personnel:** 
  - Jack Elston (PI, CEO, Black Swift Technologies) — (720) 638-9656
  - Beck Cotter (Administrative POC) — (720) 638-9656
  - Peter Torrione (Chief Technologist, CoVar, subcontractor) — (703) 442-6610

## Executive Summary
Black Swift Technologies proposes a tube-launched, Group 1 UAS equipped with EO/IR sensors and AI-enabled automatic target recognition (ATR) to enable autonomous ISR operations within contested/denied environments. The system leverages BST's proven air-deployed S0-AD platform combined with CoVar's ACES ATR software and low-SWaP edge processing to detect, classify, and geolocate targets with minimal operator burden and low-bandwidth communications, designed for rapid deployment from existing Navy sonobuoy launch infrastructure.

## Technical Approach

### Platform Foundation
- **Aircraft Base (TRL 9):** Modified S0-AD air-deployed fixed-wing UAS, proven through 50+ operational deployments from NOAA P-3 aircraft in extreme conditions (Cat 5 hurricanes)
- **Launch Method:** Tube-launched from existing sonobuoy launch infrastructure on P-3 and maritime patrol aircraft
- **Configuration Change:** Reconfigured from atmospheric sensing to ISR payload; existing sensor suite replaced with nose-mounted gimballed EO/IR camera and GPU-based processing hardware

### ATR Capability (TRL 7-8)
- **Software:** CoVar's ACES (AI/ML-based automatic target recognition framework)
- **Processing Location:** Edge-based, real-time onboard processing
- **Target Types:** Ground vehicles, personnel, unmanned surface vessels, UAS
- **Enhanced Outputs:** Target pose, orientation, and range estimation formatted for tactical integration (Cursor-on-Target/CoT, TAK, NTCDL messaging)
- **Development History:** Developed through multiple DoD efforts (US Army, US Navy, Army Research Laboratory); demonstrated in Project Convergence, NATO exercises, National Training Center (NTC) events; transitioning into Army XM30 program

### Communications & Autonomy
- **Low-Bandwidth Operation:** Fully autonomous with minimal communications; only high-value detections transmitted using compact, optimized data products
- **Operator Burden:** Single-operator interface with minimal required interaction during mission execution
- **Data Integration:** Direct integration with existing tactical data networks

## Products & Capabilities Described

### S0-AD (Air-Deployed Fixed-Wing UAS)
- **What it is:** US-manufactured Group 1 fixed-wing unmanned aircraft system designed for tube-launch deployment
- **Proven Performance:** 
  - 50+ successful deployments from NOAA P-3 aircraft
  - Demonstrated operation in extreme environments including Cat 5 hurricanes
  - Reliable performance in high winds, turbulence, and precipitation
- **Compatibility:** Compatible with existing Navy sonobuoy launch infrastructure; requires no aircraft modification
- **Proposed ISR Use:** Reconfigured with EO/IR sensor payload and onboard GPU-based ATR processing for autonomous target detection missions in contested airspace
- **Key Advantage:** Low-risk, flight-proven platform reducing transition risk and integration cost

### ACES ATR Software (CoVar)
- **What it is:** AI/ML-based real-time detection and classification framework optimized for edge computing
- **Capability:** Identifies wide range of targets (vehicles, personnel, unmanned vessels, UAS) across varying operational conditions and complex backgrounds
- **Performance Characteristics:**
  - Real-time inference on low-SWaP hardware
  - High-throughput, low-latency design
  - Provides enhanced outputs (pose, orientation, range estimation)
  - Formatted for tactical system integration (CoT, TAK, NTCDL)
- **Operational Validation:** Demonstrated strong performance in Project Convergence, NATO exercises, NTC events; algorithms consistently met/exceeded performance benchmarks in blind evaluations
- **Transition Status:** Transitioning into multiple programs of record; demonstrated in Army XM30 program

### EO/IR Sensor Payload
- **Integration:** Nose-mounted gimballed camera with GPU-based processing hardware
- **Challenge:** Meeting strict SWaP constraints while maintaining image quality for reliable ATR
- **Mitigation:** BST partnerships with camera vendors and prior small UAS sensor integration experience

## Use Cases & Applications

### Primary Mission Context
- **Environment:** Contested/denied airspace, adversary integrated air defense (IAD) systems, weapons engagement zones (WEZ)
- **Operational Gaps Addressed:** 
  - Extended reach into denied environments inaccessible to manned aircraft and large ISR platforms
  - Overcome weather obscuration, limited persistence, and insufficient resolution of standoff sensing
  - Provide rapid detection and identification of targets inside threat rings

### Specific Naval Applications
- Distributed ISR sensing across contested maritime regions
- Enhanced maritime situational awareness
- Force extension for Navy task force intelligence organizations
- USMC stand-in force operations
- SOCOM unit support

### Operational Benefits
- **Coverage:** >5–10× area coverage per sortie via multi-node deployment
- **Communications Efficiency:** >80% reduction in comms bandwidth through onboard ATR processing
- **Cost:** >10× reduction in ISR cost per asset through attritable design
- **Operator Workload:** Reduced through autonomous operation and minimal interaction requirements
- **Engagement Timeline:** Reduced time to engagement via direct tactical data network outputs

## Technical Milestones & Development Plan

**24-Month Program Structure:**

1. **Milestone 1 (M1-6):** Program kickoff and system-level design
   - Define CONOPS and mission requirements
   - Establish system architecture and interfaces
   - Develop performance metrics and SWaP budgets

2. **Milestone 2 (M4-13):** Component selection and detailed interface design
   - Select EO/IR sensor and onboard processing hardware
   - Complete mechanical, electrical, software design modifications for S0-AD integration

3. **Milestone 3 (M9-16):** System integration and flight test
   - Fabricate and assemble modified S0-AD system
   - Integrate payload and processing hardware
   - Validate aircraft performance and system stability at design weight

4. **Milestone 4 (M12-18):** Mission capability development
   - Implement autonomous search behaviors
   - Develop onboard ATR processing integration
   - Implement low-bandwidth data transmission
   - Develop tactical network integration (CoT, TAK, NTCDL)
   - Develop user interface and end-to-end validation

5. **Milestone 5 (M17-24):** Final demonstration and certification
   - Complete airworthiness and cybersecurity certification
   - Integrate classified ATR models
   - Conduct final ISR demonstrations in representative scenarios

**Key Milestones:**
- Initial flight test: Month 10
- Final ISR demonstration: Month 22

## Budget & Schedule

### Funding
- **Year 1:** $955,699
- **Year 2:** $972,157
- **Total Program:** $1,927,856

### Cost Breakdown (Year 1 example)
- Direct Labor + Fringe (BST): $267,868
- Subcontractor/Consultants (CoVar): $248,000
- Materials: $8,000
- Equipment (6 S0 UAS, EO/IR components): $90,000
- Travel & ODC: $16,000
- Subtotal: $629,868
- OH (46.67%): $125,014
- G&A (18.32%): $138,294
- Subtotal with burden: $893,176
- Fixed Fee/Profit (7%): $62,523
- **Total Year 1:** $955,699

**Period of Performance:** 24 months

**Instrument Type:** Other Transaction (OT) for Prototype

## Technology Readiness & Risk Mitigation

### TRL Progression
- **Component TRL:** 7–9 (individual components mature)
- **System Starting TRL:** 5–6 (prior demonstrations of air-deployed platforms and onboard processing)
- **Target TRL at Completion:** 7 (through system integration, flight testing, operationally relevant demonstrations)

### Technical Challenges & Mitigation

**Challenge 1: Real-time ATR on Low-SWaP Hardware**
- **Risk:** Machine-learning-based ATR must maintain real-time performance and accuracy on constrained hardware
- **Mitigation:** CoVar's ACES framework specifically designed for edge deployment; targeted optimization during effort will improve efficiency (frames per watt); mature, high-throughput, low-latency solution

**Challenge 2: EO/IR Sensor Integration within SWaP Constraints**
- **Risk:** Integrating gimballed sensor capable of meeting SWaP while maintaining image quality for ATR
- **Mitigation:** BST partnerships with camera vendors; prior experience integrating compact sensors on small UAS; vertically integrated avionics architecture enabling system-level optimization of power, compute, and sensor interfaces

## Key Personnel & Facilities

### Primary Team
- **Jack Elston** (Black Swift Technologies) – Program Manager/PI, CEO
- **Peter Torrione** (CoVar) – Chief Technologist, ATR lead

### Infrastructure
- **BST Facilities:** 
  - Wind tunnel for component validation
  - In-house manufacturing and prototyping for rapid iteration
  - Established flight test locations for evaluation and demonstration
- **CoVar Facilities:**
  - Computational resources (CPU, GPU, network-attached storage)
  - Data storage, model training, system evaluation at CUI and SECRET classification levels
  - TS facility clearance
  - All supporting personnel cleared to SECRET level minimum

## Transition & Sponsorship

### Potential Sponsors
- PEO(U&W) – PMA-263 (Small Tactical UAS)
- PEO(A) – PMA-290 (P-8), PMA-299

### End Users
- Navy Task Force intelligence organizations
- USMC stand-in forces
- SOCOM units

### Transition Targets
- PMA-263 (STUAS – Small Tactical UAS)
- PMA-290 (P-8 Poseidon)
- PMA-263 (H-60 helicopter program)
- SOCOM AT&L-ST

## Future Development & Scalability

Planned expansions beyond initial effort:
- Coordinated multi-aircraft operations
- Control handoff between UAS operators
- Adaptive tasking and retasking
- Collaborative sensing across multiple platforms with complementary sensors
- Direct cueing of downstream systems (loitering munitions, other effectors)
- Scalable deployment of multiple attritable nodes

## Notable Details & Competitive Advantages

### Integration & Compatibility
- **Existing Infrastructure:** Compatible with Navy's existing sonobuoy launch infrastructure on P-3 and maritime patrol aircraft; no aircraft modification required
- **Rapid Transition:** Demonstrated operational heritage from 50+ NOAA deployments provides low-risk foundation
- **Tactical Integration:** Direct formatting for Navy tactical data networks (CoT, TAK, NTCDL)

### Cost & Attritable Design Philosophy
- Designed as low-cost, expendable platform suitable for one-time use within adversary weapons engagement zones
- Reduces total ownership cost through attritable architecture while improving persistence
- Enables distributed deployment strategy (multiple nodes per sortie)

### Operational Advantages
- **Autonomous Operation:** Minimizes operator workload; designed for single-operator interface
- **Low Bandwidth:** >80% reduction in communications requirements through onboard ATR processing enables operation in degraded/contested communications environments
- **Rapid Detection-to-Engagement:** Direct tactical network outputs (CoT, TAK, NTCDL) reduce time-critical targeting cycle

### Technology Maturity
- All critical components (aircraft, EO/IR sensors, ATR software) are mature, proven technologies
- ATR solution has demonstrated performance across multiple DoD programs and operational exercises
- Integration effort focuses on combining proven components rather than developing new technologies
- Conservative T