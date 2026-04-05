# UAS for Small Unit Electronic Patrol - By Light

## Document Metadata
- Type: Phase I Proposal
- Client/Agency: Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field, Airborne Systems Integration Division
- Program/Solicitation: Broad Agency Announcement (BAA) N68335-25-R-0403
- Date: Proposal submission (document created/modified 2025-12-12)
- BST Products/Systems Referenced: S2 (fixed-wing UAS), S0 VTOL, S3 VTOL
- Key Personnel: Jack Elston, Maciej Stachura (BST - Aircraft and Flight Control); By Light subcontractor principals not named in document

## Executive Summary
Black Swift Technologies proposes a Group 1 VTOL fixed-wing UAS equipped with integrated RF payload and onboard signal processing to fill a gap in small-unit (battalion/company-level) ISR capabilities for the USMC Stand-In Force (SIF) concept. The system would detect, classify, and geolocate RF-emitting enemy formations in real-time using embedded antenna arrays and machine learning algorithms, deliverable as a compact, single-case system deployable by small units without higher command coordination.

## Operational Gap & Context
- **Problem**: USMC small units have organic EO/IR sensors but lack RF surveillance capability; EO/IR degraded in obscured weather; adversary forces reducing visible signatures
- **Current State**: Electronic surveillance traditionally retained at higher command levels; RF assets too large/heavy for small unit employment
- **Solution Need**: Lightweight, inexpensive RF surveillance asset distributable to battalion/company level to improve situational awareness and operational tempo in contested, dispersed operating environments
- **Key Advantage**: Enables small unit independent action without requesting support from higher headquarters

## Technical Approach

### Overall Concept
- Group 1 VTOL fixed-wing UAS with integrated RF payload and real-time onboard signal processing
- Launched/operated by operations center personnel; executes autonomous patrol patterns in company area of operations
- Upon RF detection, system classifies signal and executes localization flight pattern
- Target data transmitted to operations center and other assets via tactical mesh network

### Key Technical Features
1. **RF Threat Surveillance**: Detection, identification, geolocation of RF-emitting formations
2. **Rapid Signal Classification**: Near-real-time discrimination between friendly, unknown, and threat sources (ground, maritime, airborne domains)
3. **Data Reporting on Disadvantaged Networks**: Compact data formats optimized for low-bandwidth links
4. **Fixed-Wing VTOL Design**: No specialized launch/recovery equipment; retains speed, range, endurance advantages
5. **Compact, Integrated Payload**: RF antennas embedded in flight surfaces to minimize SWaP; enhanced reception and localization accuracy
6. **Small, Lightweight System**: Full system in single hardened case
7. **Rapid Deployment**: Assembly and launch by single person in under 10 minutes; intuitive autonomous operation by single operator

### Aircraft Platform: S2 Base
- **Wingspan**: 9 ft
- **MGTOW**: 20 lb
- **Payload Weight**: 5 lb
- **Cruise Speed**: 40 kts
- **Max Endurance**: 2 hrs
- **Max Range**: 25 nm (command link limited)

### Subsystem Components (to be detailed/designed)
1. **Antenna Arrays**: Integrated into flight surfaces for wideband RF detection and localization
2. **Signal Processing & ML Classification**: Hardware selection for real-time RF signal analysis on low-SWaP platform
3. **Autonomous Flight Patterns**: RF identification and localization maneuvers
4. **Data Transmission**: Payload data link to operations center
5. **User Interface**: System operation and RF detection display

## Risk Mitigation Through BST Experience
- **VTOL Aircraft**: 2 successful commercial VTOL models (S0, S3)
- **RF Payloads**: Integration experience including RF radiometer for soil moisture (AFRL/AFWERX SBIR Phase II); RF-transparent materials, noise mitigation, shielding expertise
- **Payload-based Flight Control**: Hurricane flight control algorithms based on real-time local winds/storm trajectory

## Technical Challenges Identified
1. Integration of antennas into flight surfaces for effective, wideband RF detection and localization
2. Signal processing and ML classification on low-SWaP hardware
3. Overall size, weight, power minimization to reduce logistics and operations footprint

## Development Milestones & Deliverables

### Phase I Milestones
- **Milestone 1**: Program Kickoff, System-level Design (interfaces, performance metrics, SWaP budgets, subcontract finalization)
- **Milestone 2**: Component Design & Procurement (S2 modifications, antenna array design/simulation, flight surface modifications, RF classifier hardware, ML training approach)
- **Milestone 3**: Subsystem Integration & Testing (antenna surface fabrication, aircraft/payload integration, basic flight testing)
- **Milestone 4**: Mission-specific Capabilities (autonomous RF ID/localization flight patterns, payload data transmission, operator UI, local system test)
- **Milestone 5**: Final Test & Demonstration (flight test at DoD emitter range)

### Deliverables
- System Design Package
- System Test Reports (performance metrics status)
- Final Report

## Use Cases & Applications
- **Primary User**: USMC Stand-In Force (small, mobile, low-signature units in contested environments)
- **Secondary Users**: Navy Special Warfare
- **Mission Context**: Company area of operations surveillance in denied/degraded electromagnetic environment
- **Tactical Employment**: Autonomous patrol search patterns; RF threat detection and classification; tactical mesh network data sharing

## Technology Areas of Interest Addressed
### Research Area of Interest Categories
- 2.1.2.a: Electronic Warfare (EW) and cyber capabilities
- 2.1.2.c: RF techniques and radar technologies for land/maritime target detection, geolocation, MTI, MMTI, tracking
- 2.1.2.d: RF antenna technologies and communications techniques
- 2.1.3.a: Signal processing
- 2.1.3.b: RF signal analysis and processing technologies
- 2.1.3.c: Machine/deep learning for raw data and pattern analysis

### Specific Areas of Interest Addressed
- 2.2.1: Collaborative multi-sensor payloads with onboard data fusion, autonomous operations, reduced data throughput, reduced operator workload
- 2.2.4: UAS solutions reducing launch/recovery footprint, expandable to alternative operational sites
- 2.2.10: Systems increasing naval capabilities through advanced data processing, reduced SWAP, improved detection, increased survivability
- 2.2.11: Lightweight, low-cost expendable air-launched/ground-launched UAS with sense-and-avoid, early warning, force multiplier capability at lower cost

## Teaming
- **Prime Contractor**: Black Swift Technologies LLC (aircraft, flight control, integration)
- **Subcontractor**: By Light (RF antenna arrays, RF signal processing, ML classification)
- **Facilities**: BST wind tunnel, prototype/manufacturing shop, flight test locations; By Light facilities to be specified

## Sponsors and Potential Users
**Potential Sponsors**: 
- PEO(U&W): PMA-262, PMA-263, PMA-266
- PEO(A): PMA-290

**End Users**:
- USMC Stand-In Forces
- Navy Special Warfare

## Technology Progression
- **TRL Advancement**: TRL 4 → TRL 6

## Future Development Concepts
- Cross-cue second system upon initial RF detection to improve localization speed/accuracy
- Cross-cue to EO/IR platform for target confirmation

## Notable Details
- Document indicates program structure as **Phase I only** with cost section incomplete ("Cost and Period of Performance" section header present but no data filled in)
- Instrument Type: Research OT
- System emphasizes **operational simplicity** (single operator, 10-minute deployment, autonomous operation) as critical for small-unit adoption
- **Bandwidth/Network Optimization**: Explicit focus on compact data formats for low-bandwidth tactical networks reflects understanding of small-unit comms constraints
- **Autonomy Focus**: Significant emphasis on autonomous RF localization patterns and onboard processing to reduce operator workload and enable single-operator employment
- Document includes quad chart (not transcribed here)
- By Light principal engineer names and facility details not yet populated (noted as "Principal Engineers?" in document)