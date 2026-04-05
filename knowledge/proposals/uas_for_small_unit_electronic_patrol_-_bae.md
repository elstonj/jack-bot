# UAS for Small Unit Electronic Patrol - BAE Systems Integration

## Document Metadata
- **Type:** Phase I Proposal
- **Client/Agency:** Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field, Airborne Systems Integration Division
- **Program/Solicitation:** Broad Agency Announcement (BAA) N68335-25-R-0403
- **Date:** Submitted late 2024/early 2025 (modified 2025-12-03)
- **BST Products/Systems Referenced:** S2 (fixed-wing UAS), S0 VTOL, S3 VTOL
- **Key Personnel:** Jack Elston, Maciej Stachura (Aircraft and Flight Control); Daniel Prendergast (last editor)
- **Partners:** BAE Systems (RF antenna arrays, RF signal processing and ML classification)

## Executive Summary
Black Swift Technologies proposes to develop a Group 1 vertical takeoff and landing (VTOL) fixed-wing unmanned aerial system equipped with integrated RF detection, classification, and localization capabilities to address a critical gap in small-unit (battalion/company-level) intelligence, surveillance, and reconnaissance (ISR) in the USMC Stand-In Force concept. The system will enable small units to detect, identify, and geolocate enemy RF emitters without relying on higher-level command assets, dramatically improving situational awareness and operational tempo in contested environments.

## Technical Approach

### Overall Concept
- **Platform:** Modified Black Swift S2 fixed-wing VTOL UAS with integrated RF payload and onboard signal processing
- **Mission:** Autonomous patrolling of company area of operations (AO) to detect, classify, and localize RF-emitting adversary formations
- **Key Differentiator:** Distribution of electronic surveillance capability to battalion/company level rather than retention at higher command; single-operator deployment and operation

### System Features
1. **RF Threat Surveillance:** Detection, identification, and geolocation of RF-emitting formations across ground, maritime, and airborne domains
2. **Rapid Signal Classification:** Near-real-time classification of RF signals to discriminate friendly, unknown, and potential threat sources
3. **Low-Bandwidth Data Reporting:** Compact signal/target data format optimized for disadvantaged networks
4. **Fixed-Wing VTOL Design:** No specialized launch/recovery equipment; retains speed, range, endurance advantages
5. **Integrated Payload:** RF antennas embedded in flight surfaces to minimize size, weight, and power (SWaP) while enhancing reception and localization accuracy
6. **Portability:** Full system in single hardened case; assembly and launch by single person in under 10 minutes
7. **Autonomous Operation:** Intuitive single-operator control

### Five-Milestone Development Plan

**Milestone 1: Program Kickoff and System-level Design**
- Kickoff with Navy and subcontractors
- Definition of system interfaces, performance metrics, SWaP budgets
- Finalization of subcontracts

**Milestone 2: Component Design and Procurement**
- S2 aircraft design modifications
- Antenna array design and simulation
- Flight surface modifications for antenna integration
- RF signal classifier hardware selection
- Signal classifier training/transfer learning

**Milestone 3: Subsystem Integration and Testing**
- Antenna-integrated surface fabrication
- Aircraft-payload integration
- Basic flight testing

**Milestone 4: Mission-specific Capabilities**
- Autonomous flight patterns for RF identification and localization
- Payload data transmission protocols
- Operator UI and RF source detection display
- Local system testing

**Milestone 5: Final Test and Demonstration**
- Flight test at DoD emitter range

## Products & Capabilities Described

### S2 Fixed-Wing VTOL UAS
- **What it is:** Black Swift's Group 1 vertical takeoff and landing fixed-wing unmanned aircraft
- **Proposed use:** Base platform for RF surveillance payload; modifications for antenna integration into flight surfaces
- **Specifications:**
  - Wingspan: 9 ft
  - Maximum Gross Takeoff Weight (MGTOW): 20 lb
  - Payload capacity: 5 lb
  - Cruise speed: 40 kts
  - Maximum endurance: 2 hrs
  - Maximum range: 25 nm (command link limited)
- **Relevant prior BST experience:** Wind tunnel testing, prototype/manufacturing capabilities, flight test locations available

### S0 VTOL and S3 VTOL
- **What they are:** Commercially sold VTOL aircraft models developed by Black Swift
- **Relevance:** Demonstrate BST's proven expertise in VTOL aircraft design and manufacturing, reducing technical risk

### RF Antenna Arrays (BAE Systems responsibility)
- Integrated into S2 flight surfaces
- Designed for wideband RF detection and localization
- Embedded design to minimize aircraft SWaP impact
- Antenna array details (coverage bandwidths, detectable target emitters, etc.) noted as discussion section in proposal but not fully detailed in provided text

### RF Signal Processing and ML Classification (BAE Systems responsibility)
- Onboard signal processing for real-time RF signal analysis
- Classification of RF signals across ground, maritime, and airborne domains
- Machine learning/deep learning algorithms for pattern analysis
- Hardware selection targeting low-SWaP implementation
- Potential use of transfer learning/retraining approaches

## Use Cases & Applications

### Primary Mission
**Small Unit Electronic Patrol - USMC Stand-In Force (SIF)**
- Detection and localization of enemy RF emitters in battalion/company area of operations
- Execution of autonomous patrolling search patterns
- Real-time classification of RF signals as friendly, unknown, or threat
- Transmission of target data to operations center and tactical mesh network
- Support for units operating independently in contested environments with large separation distances

### Operational Context
- **User Community:** USMC stand-in forces, Navy Special Warfare
- **Environment:** Contested environments requiring small, highly mobile, low-signature forces
- **Key Advantage:** Eliminates need for higher-level command coordination; dramatically improves response time and operational tempo for small units

### Current Operational Gap
- EO/IR sensors (already present at battalion/company/platoon level) degraded in obscured weather
- Adversary forces reducing size and visible signatures
- Electronic surveillance traditionally retained at higher command levels on platforms too large for small-unit support
- No organic RF spectrum surveillance capability at small-unit level

## Technical Challenges
1. **Antenna Integration:** Embedding antennas into flight surfaces while maintaining effective, wideband RF detection and localization capability
2. **Low-SWaP Signal Processing:** Implementing signal processing and ML classification on hardware with severe size, weight, and power constraints
3. **Overall System SWaP:** Minimizing total system logistics and operations footprint while integrating RF payload and processing

## Key Personnel and Facilities

### Black Swift Technologies (Prime Contractor) - Aircraft and Flight Control
- **Personnel:** Jack Elston, Maciej Stachura
- **Facilities:** Wind tunnel, prototype/manufacturing shop, flight test locations

### BAE Systems (Subcontractor)
- **RF Antenna Arrays:** Principal Engineers and facilities not specified in proposal
- **RF Signal Processing and ML Classification:** Principal Engineers and facilities not specified in proposal

## Areas of Interest Addressed

### Research Area of Interest Category
- **2.1.2.a - Electronic Warfare (EW) and cyber capabilities**
- **2.1.2.b - Enhanced airborne networking of autonomous vehicles, manned aircraft, and ground/afloat systems**
- **2.1.2.c - RF techniques and radar technologies for land and maritime target detection, geolocation, Moving Target Identification (MTI)**
- **2.1.2.d - RF antenna technologies and communications techniques**
- **2.1.3.a - Signal processing**
- **2.1.3.b - RF Signal analysis and processing technologies and techniques**
- **2.1.3.c - Machine or deep learning for raw data and/or pattern analysis**

### Specific Areas of Interest
- **2.2.1:** Collaborative multi-sensor payloads with onboard data fusion and autonomous operations for reduced data throughput
- **2.2.2:** Enhanced airborne payloads for greater maritime situational awareness
- **2.2.4:** UAS solutions with minimal launch/recovery footprint for alternative operational sites
- **2.2.10:** Manned/unmanned systems increasing naval capabilities through advanced processing and detection
- **2.2.11:** Lightweight, low-cost expendable UAS and sensor technologies for naval capability enhancement

## Risk Mitigation & Competitive Advantages

### Risk-Mitigating Company Expertise
1. **VTOL Aircraft:** BST has developed and successfully commercialized two VTOL models (S0 and S3), demonstrating mature VTOL design and manufacturing capability
2. **RF Payloads:** Recent integration of RF radiometer payload for soil moisture measurement (AFRL/AFWERX SBIR Phase II); proven experience with RF-transparent materials, RF noise mitigation, and RF shielding
3. **Payload-based Flight Control Algorithms:** Demonstrated capability in hurricane flight control based on real-time sensor data and environmental parameters, applicable to RF-guided autonomous flight patterns

### Key Competitive Advantages
- Single-operator deployment and launch (under 10 minutes)
- Fixed-wing VTOL platform (no specialized launch/recovery equipment)
- Integrated, compact design in single hardened case
- Intuitive autonomous operation
- Proven manufacturing and flight test capabilities

## Deliverables
1. System Design Package
2. System Test Reports (status against performance metrics)
3. Final Report

## Cost and Schedule
- **Instrument Type:** Research OT
- **Technology Progression:** TRL 4 → TRL 6
- **Period of Performance:** Not specified in provided text
- **Cost Estimate:** Not specified in provided text (section marked for completion)

## Future Development Roadmap
1. **Cross-cueing of multiple systems:** Deploy second system upon initial RF detection to improve localization time and speed
2. **EO/IR integration:** Cross-cue to EO/IR platform for target confirmation

## Notable Details
- **Operational Context:** Directly supports USMC Stand-In Force (SIF) concept for contested environments
- **Potential Sponsors:** PEO(U&W) (PMA-262, PMA-263, PMA-266); PEO(A) (PMA-290)
- **Network Integration:** Target data transmitted via tactical mesh network for multi-unit coordination
- **Signature Management:** System designed as low-signature asset for small units operating in denied/contested environments
- **Cost Focus:** Emphasis on inexpensive, lightweight, and intuitive system to enable wide distribution to small units without increasing logistics burden