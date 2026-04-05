# UAS for Small Unit Electronic Patrol - Phase I Proposal

## Document Metadata
- **Type:** Phase I Proposal (BAA Response)
- **Client/Agency:** Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field, Airborne Systems Integration Division
- **Program/Solicitation:** Broad Agency Announcement (BAA) N68335-25-R-0403
- **Date:** November 24, 2025 (document modified)
- **BST Products/Systems Referenced:** S2 (fixed-wing UAS), S0 VTOL, S3 (VTOL aircraft)
- **Key Personnel:** Jack Elston, Maciej Stachura (Aircraft and Flight Control - BST); 3dB Labs as subcontractor (Principal Engineers not named in document)

## Executive Summary
Black Swift Technologies proposes a Group 1 VTOL fixed-wing UAS equipped with integrated RF payload and onboard signal processing to provide small unit (battalion/company-level) electronic surveillance and reconnaissance capabilities. The system would detect, classify, and geolocate RF-emitting enemy forces in real-time, addressing a critical gap in USMC Stand-In Force ISR capabilities where EO/IR sensors are degraded in obscured weather and adversaries reduce visible signatures.

## Operational Context

**Problem Statement:**
- USMC Stand-In Force (SIF) concept requires small, highly mobile forces in contested environments
- Current small unit organic Group 1 UAS have EO/IR sensors only
- Gap: inability to detect enemy forces in poor weather or with reduced visible signatures
- Electronic surveillance assets traditionally reserved for higher command levels due to size/weight constraints on larger platforms
- Small units lack organic RF surveillance capability

**Proposed Solution Impact:**
- Distribute electronic surveillance capability to battalion/company commanders
- Enable independent operations without higher headquarters coordination
- Drastically improve small-unit battlefield situational awareness and operational tempo
- Critical for geographically dispersed independent operations

## Technical Approach

### Aircraft Platform
**Base System:** Black Swift Technologies S2 fixed-wing UAS (modified for RF payload integration)

**Specifications:**
- Wingspan: 9 ft
- Maximum Gross Takeoff Weight (MGTOW): 20 lb
- Payload Capacity: 5 lb
- Cruise Speed: 40 knots
- Maximum Endurance: 2 hours
- Maximum Range: 25 nm (command link limited)
- Design: Group 1 VTOL (vertical takeoff and landing) fixed-wing aircraft

**Key Design Features:**
- No specialized launch/recovery equipment required
- Retains speed, range, and endurance advantages of fixed-wing design
- Single hardened case containment for full system
- Assembled and launched by single person in under 10 minutes
- Intuitive autonomous operation by single operator

### RF Payload Architecture

**Detection & Classification Capabilities:**
- Wideband RF detection across ground, maritime, and airborne domains
- Near-real-time signal classification (friendly/unknown/threat discrimination)
- RF source geolocation through flight pattern execution
- Compact antenna arrays embedded in flight surfaces to minimize SWaP
- RF-transparent and shielded materials for noise mitigation

**Data Management:**
- Onboard signal processing for real-time identification and localization
- Compact data formats optimized for low-bandwidth communication
- Integration with tactical mesh networks for target data dissemination

### Operational Employment Concept
1. Launched/operated by operations center personnel
2. Executes patrolling search patterns over company area of operations (AO)
3. Detects and classifies RF signals
4. Executes localization flight patterns upon detection
5. Transmits target data to operations center and other assets via tactical mesh network

### Technical Development Milestones

**Milestone 1: Program Kickoff and System-level Design**
- Kickoff with Navy representatives and subcontractors
- Definition of system interfaces, performance metrics, SWaP budgets
- Finalization of subcontract agreements

**Milestone 2: Component Design and Procurement**
- S2 aircraft design modifications
- Antenna array design and simulation
- Flight surface design modifications for antenna integration
- RF signal classifier hardware selection
- RF classifier training/transfer learning approach

**Milestone 3: Subsystem Integration and Testing**
- Fabrication of antenna-integrated surfaces
- Aircraft and payload component integration
- Basic flight testing

**Milestone 4: Mission-specific Capabilities**
- Autonomous flight patterns for RF identification and localization
- Payload data transmission implementation
- Operator UI for RF source detection display
- Local system testing

**Milestone 5: Final Test and Demonstration**
- Flight testing at DoD emitter range

## Products & Capabilities Described

### S2 Fixed-Wing UAS
- **What it is:** Black Swift's mature Group 1 fixed-wing VTOL aircraft platform
- **Proposed use:** Base aircraft for RF surveillance system integration
- **Adaptation:** Design modifications to integrate RF antenna arrays and signal processing hardware
- **Risk mitigation:** BST has extensive VTOL development history (S0 VTOL and S3 models sold commercially)

### Integrated RF Payload System
- **What it is:** Combined RF antenna array with onboard signal processing and ML-based classification
- **Capabilities:**
  - Detection of RF emitters
  - Signal classification (friendly/unknown/threat)
  - Geolocation through autonomous flight patterns
  - Low-bandwidth optimized data reporting
- **Subcontractor:** 3dB Labs (antenna arrays and RF signal processing/ML classification)

### Signal Processing & ML Classification
- **Architecture:** Low-SWaP hardware implementation on board aircraft
- **Functionality:** Real-time RF signal analysis, classification, and localization
- **Challenge:** Implementing ML classification on severely power/weight constrained hardware

## Use Cases & Applications

**Primary Use Case:**
- USMC Stand-In Force small unit electronic patrol
- Company and battalion-level operations in contested environments

**User Communities:**
- USMC stand-in forces
- Navy Special Warfare

**Operational Scenarios:**
- Detection of adversary RF emitters in friendly area of operations
- Battlefield situational awareness in obscured weather conditions
- Independent company-level surveillance without higher headquarters support
- Force multiplier for small, mobile units operating at distance

## Areas of Interest Alignment

**Research Area Categories Addressed:**
- 2.1.2.a: Electronic Warfare (EW) and cyber capabilities
- 2.1.2.b: Enhanced airborne networking of autonomous vehicles
- 2.1.2.c: RF techniques for target detection and geolocation
- 2.1.2.d: RF antenna technologies and communications
- 2.1.3.a: Signal processing
- 2.1.3.b: RF signal analysis and processing
- 2.1.3.c: Machine/deep learning for pattern analysis

**Specific Areas Addressed:**
- 2.2.1: Collaborative multi-sensor payloads with onboard data fusion, reduced data throughput
- 2.2.2: Enhanced unmanned airborne payloads with reduced SWAP
- 2.2.4: UAS with decreased launch/recovery footprint and alternative site capability
- 2.2.10: Advanced data processing, detection algorithms, reduced processing time, reduced SWAP
- 2.2.11: Lightweight low-cost UAS technologies as force multipliers with improved survivability

## Technology Challenges

1. **Antenna Integration:** Effective integration of antenna arrays into flight surfaces for wideband RF detection and localization while maintaining aerodynamic performance
2. **Signal Processing & ML on Constrained Hardware:** Implementing classification algorithms on low-SWaP embedded systems
3. **Overall SWaP Minimization:** Keeping full integrated system within 5 lb payload budget while maintaining performance

## Risk Mitigation - Company Expertise

**VTOL Aircraft:**
- BST has developed and sold two successful commercial VTOL models (S0 VTOL and S3)
- Deep experience with vertical takeoff/landing systems

**RF Payload Integration:**
- BST has integrated multiple RF payloads
- Recent RF radiometer payload for soil moisture measurement (AFRL/AFWERX SBIR Phase II)
- Expertise in RF-transparent materials, RF noise mitigation, RF shielding

**Advanced Flight Control Algorithms:**
- Payload-based flight control (hurricane flight control based on real-time local winds and storm trajectory)
- Autonomous pattern execution capability

## Key Personnel and Facilities

**Aircraft and Flight Control (Black Swift Technologies - Prime):**
- Jack Elston
- Maciej Stachura
- Facilities: Wind tunnel, prototype/manufacturing shop, flight test locations

**RF Antenna Arrays (3dB Labs - Subcontractor):**
- Principal Engineers: [Not named in document]
- Facilities: [Not specified]

**RF Signal Processing and ML Classification (3dB Labs - Subcontractor):**
- Principal Engineers: [Not named in document]
- Facilities: [Not specified]

## Sponsors and Users

**Potential Sponsors:**
- PEO(U&W): PMA-262, PMA-263, PMA-266
- PEO(A): PMA-290

**Users:**
- USMC stand-in forces
- Navy Special Warfare

## Program Details

**Instrument Type:** Research OT (Other Transaction)

**Technology Progression:** TRL 4 → TRL 6

**Period of Performance:** Phase I BAA (specific duration not detailed in document)

**Cost/Budget:** [Section incomplete in provided document]

## Deliverables

- System Design Package
- System Test Reports (indicating status against performance metrics)
- Final Report

## Future Development/Growth Path

- **Multi-system localization:** Cross-cue second system to improve localization time and speed
- **Target confirmation:** Cross-cue to EO/IR platform for target confirmation
- Expansion of concurrent surveillance capabilities

## Notable Details

**Key Operational Advantages:**
- Single-operator deployment and operation
- Sub-10-minute assembly and launch
- No specialized launch/recovery equipment required
- Full system in single hardened case for transport
- Autonomous operation reduces operator workload
- Compact data formats for low-bandwidth tactical networks
- Addresses critical gap in small-unit ISR in Stand-In Force operations

**Competitive/Differentiating Factors:**
- Distributes electronic surveillance to lower command levels (previously only at higher levels)
- Enables independent operations without higher headquarters coordination
- Lightweight, low-cost, expendable platform approach
- Integration of RF payload into small fixed-wing platform (challenging technical achievement)

**Subcontractor Model:**
- BST (prime) provides aircraft platform and flight control
- 3dB Labs provides RF antenna arrays and signal processing/ML classification expertise
- Combines complementary specialized capabilities