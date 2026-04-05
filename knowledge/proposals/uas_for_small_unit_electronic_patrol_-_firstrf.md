# UAS for Small Unit Electronic Patrol - FirstRF

## Document Metadata
- **Type:** Phase I Proposal
- **Client/Agency:** Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field, Airborne Systems Integration Division
- **Program/Solicitation:** Broad Agency Announcement (BAA) N68335-25-R-0403
- **Date:** Submitted 2025 (document modified through November 2024)
- **BST Products/Systems Referenced:** S2 fixed-wing UAS, S0 VTOL, S3 VTOL
- **Key Personnel:** Jack Elston, Maciej Stachura (Aircraft and Flight Control); Daniel Prendergast (last editor)
- **Subcontractors:** FirstRF (RF Antenna Arrays), additional RF Signal Processing/Classification partner TBD

## Executive Summary
Black Swift Technologies proposes to develop a Group 1 vertical takeoff and landing (VTOL) fixed-wing UAS equipped with integrated RF detection, classification, and localization capabilities to address USMC Stand-In Force (SIF) gaps in small unit ISR. The system will detect, identify, and geolocate RF-emitting enemy formations in company-level areas of operation, enabling battalion and company commanders to conduct electronic surveillance without higher headquarters coordination or support.

## Operational Gap & Mission Need
- **Problem:** USMC Stand-In Force units have EO/IR surveillance capabilities but lack RF spectrum surveillance at small unit level
- **Limitation:** EO/IR sensors degrade in obscured weather; adversaries are reducing visible signatures
- **Current Practice:** Electronic surveillance assets historically retained at higher command levels; too large/heavy for small units
- **Solution Value:** Distributing RF ISR capability to company/battalion level improves coverage, responsiveness, and operational autonomy; reduces dependency on higher HQ coordination and communications in contested environments

## Technical Approach

### System Concept
A Group 1 VTOL fixed-wing UAS with integrated onboard RF payload and signal processing for:
- Real-time detection, identification, classification, and geolocation of RF sources
- Autonomous patrol execution over company area of operation
- Near-real-time signal classification (friendly/unknown/threat discrimination across ground, maritime, airborne domains)
- Compact data reporting optimized for low-bandwidth tactical mesh networks

### Key Technical Features
- **RF Threat Surveillance:** Detection, identification, geolocation of RF-emitting formations
- **Rapid Signal Classification:** Near-real-time automated RF signal discrimination
- **Data Reporting on Disadvantaged Networks:** Compact data formats for low-bandwidth links
- **Fixed-Wing VTOL Design:** No specialized launch/recovery equipment required; retains fixed-wing speed, range, endurance advantages
- **Compact, Integrated Payload:** RF antennas embedded in flight surfaces to minimize SWaP while enhancing reception and localization accuracy
- **Portability:** Full system in single hardened case; assembled and launched by single person in <10 minutes
- **Operational Simplicity:** Intuitive, autonomous single-operator control

## Products & Capabilities Described

### S2 Fixed-Wing UAS (Prime Platform)
- **What it is:** Black Swift's Group 1 VTOL fixed-wing unmanned aircraft
- **Specifications:**
  - Wingspan: 9 ft
  - MGTOW: 20 lb
  - Payload capacity: 5 lb
  - Cruise speed: 40 kts
  - Max endurance: 2 hrs
  - Max range: 25 nm (command link limited)
- **Proposed Use:** Base aircraft for RF payload integration; design modifications for antenna array integration
- **Why Selected:** Proven VTOL platform, existing flight control expertise, sufficient payload capacity for RF systems

### RF Payload System (FirstRF Subcontractor)
- **Components:** Antenna arrays, RF signal processing hardware, ML-based RF signal classifier
- **Capabilities:** Wideband RF detection and localization via surface-integrated antenna arrays
- **Technical Challenges:** Integration of antennas into flight surfaces for effective wideband RF detection; antenna design for compact, low-SWaP implementation

### Signal Processing & Classification (TBD Subcontractor)
- **Function:** Real-time RF signal analysis, automated classification, localization algorithms
- **Technical Approach:** Machine learning/deep learning on low-SWaP hardware; transfer learning or re-training of existing RF signal classifiers
- **Data Output:** Formatted for low-bandwidth transmission via tactical mesh networks

## Use Cases & Applications

### Primary Mission: Small Unit Electronic Patrol
- **User:** USMC Stand-In Force (battalion/company-level operations)
- **Scenario:** 
  - Launched by operations center personnel
  - Executes autonomous patrol search patterns over company area of operation
  - Detects and classifies RF emitters (friendly/unknown/threat)
  - Executes localization flight patterns upon detection
  - Reports target data to operations center and other assets via tactical mesh network
- **Operational Environment:** Contested areas; highly mobile small units; separated by large distances; minimized communications dependency

### Secondary Users
- USMC stand-in forces
- Navy Special Warfare

### Future Enhancement Concepts
- Cross-cue to second RF system to accelerate localization
- Cross-cue to EO/IR platform for target confirmation

## Technology Challenges
1. **Antenna Integration:** Integrating antennas into flight surfaces for effective, wideband RF detection and localization without degrading aerodynamics
2. **Signal Processing on Constrained Hardware:** ML-based signal classification on low-SWaP embedded systems
3. **Overall SWaP Minimization:** Keeping total system compact and lightweight to minimize logistics and operations footprint while maintaining performance

## Research Areas of Interest Addressed
The proposal maps to multiple BAA research interests:

**Payload-Related:**
- 2.1.2.a – Electronic Warfare (EW) and cyber capabilities
- 2.1.2.b – Enhanced airborne networking of autonomous vehicles, manned aircraft, and ground/afloat systems
- 2.1.2.c – RF techniques for target detection, geolocation, MTI, passive systems, tracking
- 2.1.2.d – RF antenna technologies and communications techniques

**Advanced Computing:**
- 2.1.3.a – Signal processing
- 2.1.3.b – RF signal analysis and processing technologies
- 2.1.3.c – Machine/deep learning for raw data and pattern analysis

**Specific Areas (2.2.x):**
- 2.2.1 – Multi-sensor payloads with onboard data fusion, autonomous ops, reduced data throughput on disadvantaged links
- 2.2.4 – UAS solutions with minimal launch/recovery footprint, capability for alternative operational sites
- 2.2.10 – Systems providing advanced data processing, reduced processing time, reduced SWAP, increased detection range, reduced probability of detection, lower total ownership cost
- 2.2.11 – Low-cost lightweight UAS/sensor technologies as force multipliers, improved survivability, lower total ownership cost

## Risk Mitigation through BST Expertise
- **VTOL Aircraft:** Two successful commercial VTOL models (S0, S3) demonstrate BST's VTOL design and production capability
- **RF Payloads:** Previous RF radiometer integration (AFRL/AFWERX SBIR Phase II); experience with RF-transparent materials, RF noise mitigation, RF shielding
- **Payload-Based Flight Control:** Demonstrated capability through hurricane flight control algorithms that respond to real-time local environmental conditions

## Development Milestones (Phase I)

**Milestone 1: Program Kickoff and System-level Design**
- Kickoff with Navy and subcontractors
- Define system-level interfaces, performance metrics, SWaP budgets
- Finalize subcontracts

**Milestone 2: Component Design and Procurement**
- S2 aircraft design modifications
- Antenna array design and simulation
- Flight surface modifications for antenna integration
- RF signal classifier hardware selection
- ML classifier transfer learning or re-training approach

**Milestone 3: Subsystem Integration and Testing**
- Fabricate antenna-integrated flight surfaces
- Integrate aircraft and payload
- Basic flight testing

**Milestone 4: Mission-Specific Capabilities**
- Autonomous flight patterns for RF ID and localization
- Payload data transmission protocols
- Operations UI and RF detection display
- Local system testing

**Milestone 5: Final Test and Demonstration**
- Flight test at DoD emitter range

## Phase I Deliverables
- System Design Package
- System Test Reports (performance metrics status)
- Final Report

## Technology Progression
- **Target TRL Advancement:** TRL 4 → TRL 6 (by end of Phase I)

## Cost and Period of Performance
- **Instrument Type:** Research OT
- **Cost and PoP:** Section incomplete in source document
- **Anticipated Sponsors:** PEO(U&W) (PMA-262, PMA-263, PMA-266); PEO(A) (PMA-290)

## Notable Details

### Competitive Advantages
- **Organic Small Unit Capability:** Eliminates need for small units to request higher headquarters support; improves operational autonomy
- **Multi-Domain Detection:** Can discriminate RF threats across ground, maritime, and airborne domains
- **Low-Bandwidth Optimized:** Data compression and packaging for disadvantaged networks enables operation in contested comms environments
- **Rapid Deployment:** Single-person assembly in <10 minutes with portable hardened case
- **Integration Simplicity:** Embedded antenna design reduces visible signature and SWaP

### Key Design Drivers
- **SWaP:** Critical constraint across antenna arrays, signal processing hardware, and overall system
- **Autonomy:** Intuitive single-operator control with autonomous flight patterns and signal localization
- **Robustness:** Hardened packaging for small unit field operations

### Program Status
- Document created October 3, 2025; modified November 24, 2024 (date discrepancy suggests revision history)
- Final cost estimate and period of performance sections incomplete/to be filled
- Some subcontractor details (FirstRF principal engineers/facilities) and TBD RF signal processing partner not yet specified in this version