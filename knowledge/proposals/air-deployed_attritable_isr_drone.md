# Air-deployed Attritable ISR Drone with Automatic Target Recognition (ATR)

## Document Metadata
- Type: Phase I Proposal
- Client/Agency: Naval Air Warfare Center Aircraft Division (NAWCAD), Webster Outlying Field, Airborne Systems Integration Division
- Program/Solicitation: Broad Agency Announcement (BAA) N68335-25-R-0403
- Date: 2025-10-22 (last modified)
- BST Products/Systems Referenced: S0 AD (Air-deployed fixed-wing UAS)
- Key Personnel: Jack Elston, Maciej Stachura (Aircraft and Flight Control)
- Partners: ByLight (ATR Model Development and Deployment)

## Executive Summary
Black Swift Technologies proposes developing an air-deployed Group 1 unmanned aircraft system equipped with an EO/IR camera and automated target recognition (ATR) capability to conduct ISR operations within contested environments and adversary integrated air defense (IAD) envelopes. The system would be deployed from a Common Launch Tube (CLT) aboard platforms like the P-8 Poseidon, operate autonomously with minimal communication requirements, and provide near-real-time target detection and classification using onboard AI/ML edge processing.

## Technical Approach

**Operational Concept:**
- A P-8 conducting ISR outside enemy territorial airspace deploys the S0 AD via Common Launch Tube
- Aircraft autonomously transits to target area and executes autonomous search patterns
- ATR payload detects enemy systems in near-real-time
- Compact target data is packaged for low-bandwidth transmission back to P-8 for dissemination over tactical datalinks

**Key Technical Features:**
1. **Air-deployed fixed-wing platform** - Deployed from CLT for extended reach from manned aircraft with fixed-wing range and speed advantages
2. **Automatic Target Recognition** - Computer vision edge processing for near-real-time classification and reporting
3. **Low-Comm Operation** - Fully autonomous flight control with target information optimized for low-bandwidth, long-range communication in limited transmissions
4. **Compact integrated payload** - Low-SWaP EO/IR camera with Graphics Processing Unit for onboard AI/ML processing
5. **Intuitive operation** - Single-operator control with autonomous mission execution
6. **Swarm-capable** - Modular, open flight control software supporting swarm control layer integration

## Products & Capabilities Described

### S0 AD (Air-deployed variant of S0)
**What it is:** A Group 1 fixed-wing unmanned aircraft system designed for air deployment

**Specifications:**
- Wingspan: 3 ft
- Weight: 3.5 lb
- Cruise Speed: 45 knots
- Max Endurance: 2 hours
- Max Range: 90 nm (command link limited)
- Deployment: Common Launch Tube compatible
- Flight Control: Autonomous capable, modular open architecture

**Proposed Use:** Deployed from P-8 or other manned platforms to penetrate contested airspace and conduct ISR where larger platforms cannot operate

**BST Experience:** Currently operating S0 AD for NOAA hurricane missions (duration not specified in document)

### ATR Payload (EO/IR Camera + Processing Hardware)
**What it is:** Gimballed EO/IR camera with onboard AI/ML processing hardware for automated target recognition

**Specifications:**
- Low-SWaP design to fit within aircraft weight constraints
- Graphics Processing Unit for edge computing inference
- Trained models for adversary system classification
- Compact data formatting for transmission

**Proposed Use:** Autonomous search patterns to detect and classify enemy military systems, with automated reporting of target location and characteristics

## Use Cases & Applications

**Primary Use Case:** Naval ISR in contested environments
- Detecting and locating enemy formations and integrated air defense systems
- Operating within adversary IAD envelope where manned platforms and large UAS cannot safely operate
- Maritime situational awareness from air-deployed perspective
- Support to Expeditionary Strike Groups and USMC stand-in forces

**Deployment Context:**
- Launch from P-8 Poseidon or similar naval patrol aircraft
- Operations in denied or sensitive areas at low altitude
- Extended sensor reach of US tactical network into near-peer competitor territories

## Research Areas of Interest Addressed

The proposal maps to multiple BAA interest areas:

**Platform:** Autonomous UAS operations, expendable/low-cost surveillance, SWaP optimization, powertrain enhancements

**Payload:** EO systems engineering, unattended remote controlled sensor technology, low-SWaP edge computing

**Computing:** AI/ML insertion into airborne sensors, rapid detection/identification/targeting technologies, machine/deep learning for pattern analysis

**Specific Areas:** 
- Multi-sensor payloads with enhanced data fusion and autonomous operations reducing datalink throughput (2.2.1)
- Enhanced airborne payloads for maritime situational awareness with reduced SWaP (2.2.2)
- Reduced launch/recovery footprint and alternative site capability (2.2.4)
- Persistent secure datalinks with OTH communication (2.2.7)
- Advanced detection and processing improving naval capabilities while reducing cost (2.2.10)
- Lightweight, expendable air-launched UAS for increased survivability and force multiplication (2.2.11)

## Development Milestones & Approach

**Milestone 1: Program Kickoff and System-level Design**
- Kickoff with Navy representatives and project partners
- Definition of system-level interfaces, performance metrics, SWaP budgets
- Finalization of subcontract agreements

**Milestone 2: Component Design and Procurement**
- S0 AD aircraft design modifications for payload integration
- ATR model inferencing hardware selection
- EO/IR camera and processing hardware integration design
- Potential ATR model retraining for smaller implementation

**Milestone 3: Subsystem Integration and Testing**
- Flight test coordination
- Fabrication and purchase of modified components
- Aircraft assembly and payload integration
- ATR model performance characterization
- Flight testing at design weight

**Milestone 4: Mission-specific Capabilities**
- User interface for system operation and target detection display
- Autonomous flight patterns and payload control for target search
- Target data transmission system
- Local system testing

**Milestone 5: Final Test and Demonstration**
- Final flight test and ATR capability demonstration

**Deliverables:**
- System Design Package
- System Test Reports (tracking performance against metrics)
- Final Report

## Technology Challenges Identified

1. **ML Classification for ATR on Low-SWaP Hardware** - Inference of trained models within power, thermal, and weight constraints of Group 1 platform
2. **Overall SWaP Management** - Meeting size, weight, and power constraints while maintaining air-deployment capability from CLT

## Key Personnel & Organizations

**Black Swift Technologies:**
- Jack Elston (Aircraft and Flight Control)
- Maciej Stachura (Aircraft and Flight Control)
- Facilities: Wind tunnel, prototype/manufacturing shop, flight test locations

**ByLight (Subcontractor):**
- Principal engineers and facilities for ATR model development and deployment (details not fully specified in document)

## Sponsors & Users

**Potential Sponsors:**
- PEO(U&W): PMA-263, PMA-266
- PEO(A): PMA-261, PMA-275, PMA-290, PMA-299

**Anticipated Users:**
- USMC stand-in forces
- Navy Intelligence
- Expeditionary Strike Groups

## Cost and Schedule

- **Instrument Type:** Research OT (Other Transaction)
- **Technology Progression:** TRL 4 → TRL 6
- **Cost/PoP Details:** Section incomplete in document (ROM cost estimate, period of performance, cost sharing not provided)

## Future Development Concepts

1. **Swarm Operations** - Intelligent tasking and simultaneous operation of multiple S0 AD aircraft with ATR capability
2. **Integration with Loitering Munitions** - Handoff of detected target data to loitering munition systems for follow-on engagement

## Notable Details

**Operational Advantages:**
- Attritable design philosophy - expendable platform reduces risk to manned assets
- Contested environment capability - fills gap where high-altitude/space-based systems and manned platforms are limited
- Autonomous operation reduces communications burden on tactical networks
- Compact data transmission enables operation on disadvantaged networks common in maritime and denied area operations
- Small logistics footprint enables deployment from platforms lacking organic UAS support infrastructure

**Competitive/Strategic Advantages:**
- BST operational experience with S0 AD on real-world NOAA hurricane missions
- Existing air-deployment infrastructure and CLT compatibility
- Modular software architecture enabling rapid payload integration and future swarm capability
- Open architecture supporting integration with Navy tactical systems and datalinks

**Technical Differentiation:**
- Fixed-wing platform offers greater range and endurance than rotorcraft Group 1 alternatives
- Edge processing AI/ML reduces real-time datalink requirements
- Single-operator interface reduces manning requirements
- Integration of gimballed sensor and processing into compact form factor