# Group 1 Air-deployed Attritable UAS with EO/IR Automatic Target Recognition

## Document Metadata
- Type: BAA Proposal/Capability Brief
- Client/Agency: Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field, Airborne Systems Integration Division
- Program/Solicitation: BAA No. N68335-26-R-0458 (NAWCAD WOLF Airborne Systems Integration BAA)
- Date: 2026-04-20
- BST Products/Systems Referenced: S0-AD (air-deployed UAS)
- Key Personnel: 
  - Jack Elston (BST PI/CEO, Technical POC)
  - Beck Cotter (Administrative POC)
  - Peter Torrione (CoVar Chief Technologist, Subcontractor)

## Executive Summary
Black Swift Technologies proposes integrating a tube-launched Group 1 UAS (S0-AD platform) with low-SWaP EO/IR sensing and CoVar's ACES AI/ML-based automatic target recognition (ATR) to enable autonomous ISR operations in contested, denied environments. The system emphasizes low-cost attritable deployment compatible with existing Navy sonobuoy launch infrastructure, minimal operator burden, and onboard processing to reduce communications bandwidth requirements by ~80%.

## Technical Approach

**Platform (TRL 9):**
- S0-AD fixed-wing UAS: proven air-deployed platform designed for tube-launch from P-3 aircraft
- 50+ successful NOAA P-3 deployments, including operations in Category 5 hurricanes
- Compatible with existing sonobuoy launch infrastructure without modification
- Reconfigured from atmospheric sensing to ISR payload configuration
- Replaces existing sensor suite with nose-mounted EO/IR gimballed camera and GPU-based processing hardware

**ATR Payload (TRL 7-8):**
- CoVar ACES (ATR software): AI/ML-based real-time detection and classification from EO/IR video streams
- Optimized for edge deployment on low-SWaP hardware with real-time inference onboard
- Provides enhanced outputs: target pose, orientation, range estimation
- Formatted for tactical system integration: Cursor-on-Target (CoT), TAK messaging, NTCDL
- Demonstrated performance in Project Convergence, NATO exercises, National Training Center (NTC) events
- Transitioning into Army programs of record (e.g., XM30)

**Key Technical Features:**
- Fully autonomous operation with minimal communications; only high-value detections transmitted
- Low-bandwidth data products optimized for long-range links
- Real-time detection and classification of ground vehicles, personnel, unmanned surface vessels, UAS
- Single-operator use with minimal interaction during mission execution
- Attritable design for one-time use in critical scenarios and adversary weapons engagement zones (WEZ)

**Five Milestone Approach (24 months):**
1. **M1 (6 months):** Program kickoff, system-level design, CONOPS, requirements, architecture, performance metrics, SWaP budgets
2. **M2 (10 months):** Component selection (EO/IR sensor, onboard processing hardware), detailed mechanical/electrical/software design modifications
3. **M3 (8 months):** Fabrication, assembly, integration, initial flight testing to validate aircraft performance, payload operation, system stability at design weight
4. **M4 (7 months):** Mission-specific capabilities—autonomous search, onboard ATR processing, low-bandwidth transmission, tactical data network integration (CoT, TAK, NTCDL), user interface development, end-to-end validation with unclassified models
5. **M5 (9 months):** Airworthiness and cybersecurity certification, classified ATR model integration, final flight demonstrations in representative ISR scenarios

**Technology Risk Mitigation:**
- ATR challenge: CoVar ACES framework is mature, high-throughput, low-latency solution designed specifically for edge deployment; targeted optimization during effort will improve efficiency (frames per watt)
- EO/IR sensor integration challenge: Mitigated through BST partnerships with camera vendors, prior experience integrating compact sensors on small UAS, and vertically integrated avionics architecture enabling system-level optimization of power, compute, and sensor interfaces

## Products & Capabilities Described

**S0-AD UAS:**
- Air-deployed, fixed-wing Group 1 platform
- Tube-launch compatible with P-3 aircraft sonobuoy infrastructure
- Demonstrated extreme weather performance (Cat 5 hurricanes, high winds, turbulence, precipitation)
- Purpose: Rapid extension of ISR coverage from manned aircraft while maintaining fixed-wing range and efficiency
- Status: TRL 9 (operational heritage)

**ACES ATR Software (CoVar):**
- Real-time machine learning-based target detection and classification
- Target types: ground vehicles, personnel, unmanned surface vessels, UAS
- Operational conditions: varying conditions and complex backgrounds
- Edge-optimized: runs on low-SWaP onboard hardware without reliance on high-bandwidth communications
- Enhanced outputs: pose, orientation, range estimation
- Integration capability: Cursor-on-Target (CoT), TAK, NTCDL formats
- Status: TRL 7-8; demonstrated in military exercises and programs of record

**EO/IR Sensor Payload:**
- Gimballed nose-mounted camera
- Meets SWaP constraints while maintaining image quality for ATR reliability
- Details on specific sensor not provided in proposal abstract

**Onboard GPU-based Processing Hardware:**
- Enables real-time ATR inference
- Low-SWaP design
- Details on specific compute platform not provided

## Use Cases & Applications

**Primary Mission Context:**
- ISR operations within contested/denied environments
- Operations within adversary threat rings and integrated air defense (IAD) systems
- Distributed sensing to extend Navy and joint sensor networks into contested regions

**Specific Applications:**
- **Maritime awareness:** Enhanced manned and unmanned airborne payloads providing greater maritime situational awareness
- **Multi-platform deployment:** >5-10× area coverage per sortie via multi-node deployment
- **Autonomous search operations:** Autonomous search behaviors, minimal operator interaction
- **Rapid engagement support:** Direct tactical data network outputs for reduced time to engagement

**Potential End-Users:**
- Navy Task Force intelligence organizations
- USMC stand-in forces
- SOCOM units
- Possible sponsors: PEO(U&W)–PMA-263 (STUAS), PEO(A)–PMA-290 (P-8), PMA-299, PMA-263 (H-60), SOCOM AT&L-ST

## Key Results
No results reported; this is a proposal for future development. Expected outcomes upon completion:
- >80% reduction in communications bandwidth through onboard ATR processing
- >10× reduction in ISR cost per asset through attritable design
- >5-10× area coverage per sortie via multi-node deployment
- Reduced operator workload through autonomous operation
- Reduced time to engagement with direct tactical network outputs

## Notable Details

**Operational Payoff/Transition Targets:**
- Provides air-deployed, distributed ISR inside denied areas
- Low-cost, attritable systems designed for one-time use in adversary WEZ
- Direct integration with Navy tactical networks (CoT, TAK, NTCDL)
- Rapid transition pathway via compatibility with existing sonobuoy launch infrastructure

**Team Structure:**
- Prime: Black Swift Technologies LLC
- Subcontractor: CoVar (ACES ATR software development and deployment)

**Facilities and Infrastructure:**
- BST: Wind tunnel, in-house manufacturing and prototyping, established flight test locations
- CoVar: Computational resources (CPU, GPU, network-attached storage) for data storage, model training, system evaluation at CUI and SECRET levels; TS facility clearance; all personnel cleared to SECRET level minimum

**Cost and Schedule:**
- Total 24-month effort: $1,927,856 ($955,699 Year 1 + $972,157 Year 2)
- Year 1 breakdown: Labor $267,868 (BST) + $248,000 (subcontractor) + $8,000 (materials) + $90,000 (equipment—6 S0 UAS units, EO/IR components) + $16,000 (travel) = $629,868 subtotal; with 46.67% OH and 18.32% G&A, total with 7% fixed fee = $955,699
- Year 2: Similar structure, $972,157 total
- Key milestones: M1-5 design (months 1-6); M2-4 procurement/interface (months 4-13); M3 integration/test (months 9-16); M4 mission capabilities (months 12-18); M5 final demos/certification (months 17-24)
- Critical gates: Initial flight test (M10), final ISR demonstration (M22)

**Technology Readiness:**
- S0-AD aircraft: TRL 9
- EO/IR sensor payload: Mature commercial technology
- ACES ATR: TRL 7-8
- Integrated system: Begins at TRL 5-6, advances to TRL 7 through flight demonstrations in operationally relevant environment

**Future Development:**
- Coordinated multi-aircraft operations
- Control handoff to other UAS operators
- Adaptive tasking and retasking
- Collaborative sensing across multiple platforms with complementary sensors
- Direct cueing of downstream systems (loitering munitions, other effectors)

**Alignment with BAA Areas of Interest:**
- 2.1.1 Platform-Related: UAS autonomous operations, expendable/low-cost surveillance capabilities
- 2.1.3 Advanced Computing: AI/ML insertion into airborne sensors, rapid precision detection/identification
- 2.2.2 Enhanced maritime situational awareness with reduced SWAP and total ownership cost
- 2.2.10 Advanced data processing, reduced processing/dissemination time, improved survivability, reduced cost
- 2.2.11 Lightweight, low-cost expendable air-launched UAS and sensors for early warning, survivability, force multiplication