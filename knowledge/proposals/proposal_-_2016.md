# Extensible Multi-UAS Coordination Architecture

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Topic A2.02 (UAS Technology); Project Number A2.02-7072
- **Date:** Submitted January 14, 2016
- **BST Products/Systems Referenced:** SwiftCore Flight Management System (SwiftPilot autopilot, SwiftStation ground station, SwiftTab user interface), SwiftPilot autopilot, compute node (custom hardware design), Gumstix single-board computer
- **Key Personnel:** Dr. Maciej Stachura (PI, CTO), Dr. Jack S. Elston (CEO/President, avionics expert), Dr. Cory Dixon (Director of Engineering, wireless/UI expert), Prof. Eric W. Frew (University of Colorado, guidance/control expert)

## Executive Summary
Black Swift Technologies proposes to design, develop, and test an extensible, open-architecture system for coordinating multiple heterogeneous unmanned aircraft to enable fully cooperative multi-vehicle missions controlled by a single operator. The system is built around a BST-designed compute node that serves as the hardware/software interface between individual aircraft autopilots and a distributed cooperative control architecture, leveraging the Robot Operating System (ROS) middleware and BST's SwiftTab tablet-based user interface for gesture-based multi-aircraft control.

## Technical Approach

**Core Architecture:**
- Distributed hardware and software architecture centered on a custom **compute node** that acts as the primary interface between aircraft autopilots and the cooperative control system
- Node based on existing BST design: Gumstix single-board computer (linux-based) with a snap-on circuit board interfacing to SwiftPilot autopilot
- Open-interface, layered design (OSI model) to enable rapid integration of new aircraft types, avionics systems, and sensing capabilities
- Software foundation using Robot Operating System (ROS) middleware or custom purpose-built messaging system (to be evaluated in Phase I)
- Phase I work will prototype a standalone compute node to interface with legacy NASA systems (e.g., Cloud Cap Piccolo autopilot)

**Key Technical Objectives:**
1. Design and develop compute node hardware/software with modular interfaces for heterogeneous aircraft
2. Implement and test three cooperative control algorithms (collision avoidance, formation flight, multi-UAS mapping)
3. Establish wireless mesh network architecture (10 km aircraft-to-aircraft range, expandable to 25 nodes)
4. Modify SwiftTab user interface to enable higher-level team-based mission commands rather than individual vehicle control
5. Develop API for integrating new cooperative algorithms

**Wireless Network:**
- Primary platform: P900 radio from Microhard Systems (10 km range for aircraft-to-aircraft communication, mesh networking capability)
- Generic architecture to support rapid integration of different COTS radios as needed
- Ground testing of mesh network protocols planned in Phase I

**User Interface Evolution:**
- Current SwiftTab: Android-based tablet with individual vehicle command interface
- Proposed enhancements: Gesture-based team-level commands (e.g., drawing a polygon for mapping area, dragging vehicle icon to assign it a shared task)
- Team health/status displays using graphic symbology to avoid operator overload
- Seamless multi-operator support (multiple operators, each controlling 1 or many vehicles)

## Products & Capabilities Described

### SwiftCore Flight Management System (FMS)
- **Components:** SwiftPilot autopilot, SwiftStation ground station, SwiftTab user interface
- **Features:** High-accuracy GPS, advanced mission planning, modular sensor payload architecture, Linux single-board computer for onboard algorithms
- **Development:** Built by BST team specifically for scientific missions
- **Use in this project:** SwiftPilot integration with compute node; SwiftTab modified for multi-UAS control

### Compute Node
- **What it is:** Custom-designed hardware interface board and Linux-based single-board computer providing real-time data processing and on-board cooperative algorithm execution
- **Current design:** Snap-on circuit board to SwiftPilot with Gumstix SBC
- **Proposed enhancements:** More hardware-agnostic design to support different SBC platforms; standalone version for legacy NASA autopilots
- **Use in this project:** Central element of multi-UAS coordination architecture; interfaces autopilots, payload sensors, wireless radios, and cooperative algorithms
- **Phase I Deliverable:** Prototype design and specification document

### SwiftTab User Interface
- **What it is:** Android tablet-based ground station and command interface
- **Current use:** Individual vehicle control with low-level commands
- **Proposed modifications:** Higher-level team commands, gesture-based control (polygon drawing for area mapping), graphic team status displays
- **Phase I Deliverable:** Assessment document and API design for cooperative algorithm control

## Use Cases & Applications

**Scientific/Research Missions:**
- Volumetric atmospheric sensing with spatially distributed sensors
- Atmospheric gradient measurement (key for thermodynamics, gas dispersion, gas transport)
- Severe weather sampling (thunderstorms, gust fronts)
- Boundary layer profiling
- Pollution dispersion measurement
- Remote sensing and large-area surveying
- Time-critical mapping missions (search and rescue)

**Multi-UAS Operating Concepts:**
- Single-operator multi-vehicle missions (4 aircraft in Phase I, expandable to 25)
- Cooperative formation flight (vertical stacked formations demonstrated in prior work)
- Coordinated photogrammetry mapping
- Sequential sampling strategies extending observation periods
- Collision avoidance in shared airspace

**National Airspace System (NAS) Integration:**
- Support for single-operator multi-UAS operations as pathway toward NASA Technology Roadmap goal of 4 UAS per operator (current state: 4 persons per UAS)
- Heterogeneous fleet coordination including legacy NASA systems
- Reduced operator training and certification requirements

## Prior Work & Demonstrated Experience

**BST's Previous Multi-UAS Work:**
- **CAPS (Coordinated Atmospheric Profiling System):** 2014 NASA SBIR Phase I developing turn-key coordinated atmospheric sampling system with multiple sUAS
- **VORTEX2 field campaign (2010):** First-ever manned intercept of tornadic supercell by unmanned aircraft; involved communication between aircraft, ground vehicles, and static nodes
- **MIZOPEX (2014):** Alaska-based campaign with multiple UAS classes (NASA SIERRA, ScanEagles, microUAS) in coordination with in situ sensors and satellite data; demonstrated operations of multiple UAS near NAS
- **ARM/ERASMUS:** Arctic operations with two UAS for cloud/aerosol measurement
- **MET MAP:** Four simultaneous sUAS (no aircraft-to-aircraft coordination) at different sites measuring gust fronts
- **NetUAS (2005):** Networked UAS command/control system developed with University of Colorado for cooperative control experiments

**Key Personnel Background:**
- **Dr. Stachura (PI):** 300+ flight experiments, multi-aircraft cooperative control research, secured 140+ FAA Certificates of Authorization, led NASA AFSRB/FRB process for sUAS NAS operations
- **Dr. Elston:** Designed Tempest sUAS for VORTEX2 supercell intercept, developed complex meshed network UAS and control algorithms, 300+ flight experiments, Arctic deployments
- **Prof. Frew (RECUV, CU):** 10+ years UAS design/deployment, co-leader of first-ever severe supercell sampling by unmanned aircraft, NSF CAREER Award recipient
- **Dr. Dixon:** Ph.D. research on airborne communication relays and ad hoc wireless networks, 11+ UAS platforms flown, DoD SBIR PI experience

## Work Plan & Schedule

**Phase I Duration:** 6 months

**Major Milestones:**
1. Requirements, specification, and design document
2. Compute node specifications and prototype build with software
3. Assessment and implementation of three coordination algorithms (collision avoidance, formation flight, mapping)
4. Simulation of four aircraft conducting cooperative missions (primary Phase I deliverable)
5. Final report with Phase II implementation plan

**Work Breakdown:**
- **Task 1.0 - Preliminary Work:** Kickoff meeting, requirements document, project management (127 hours)
- **Task 2.0 - Overall Architecture:** Architecture design review (ROS vs. custom analysis), compute node hardware selection, architecture prototype build (290 hours)
- **Task 3.0 - Inter-Aircraft Coordination:** Algorithm evaluation and implementation of three coordination schemes (240 hours, with 100 hours from Prof. Frew/RECUV graduate student)
- **Task 4.0 - Wireless Network:** COTS radio evaluation, mesh network ground testing, documentation (90 hours)
- **Task 5.0 - User Interface:** Current UI assessment, API design for cooperative algorithm control (100 hours)
- **Task 6.0 - Simulation & Specification:** Multi-aircraft mission simulations, results evaluation, Phase II implementation plan, final report (230 hours)

**Subcontract:** University of Colorado RECUV (320 hours, $22,965 value) for algorithm development, multi-vehicle operations, simulation, and FAA COA support

## Phase II and Commercialization Strategy

**Phase II Objectives:**
- Build and field-test four unmanned aircraft using the proposed architecture
- Conduct two field campaigns to validate architecture, algorithms, wireless mesh network, user interface
- Flight demonstrations under FAA Certificate of Authorization
- Integration testing with legacy NASA systems (Cloud Cap Piccolo autopilot compatibility)
- Refinement of CONOPS (concept of operations) and system simplicity

**Post-Phase II Commercialization:**
- Turn-key multi-UAS system for scientific and commercial applications
- Licensing of compute node to third parties and legacy NASA aircraft operators
- Participation in non-SBIR R&D projects for system validation
- Integration with evolving FAA regulations and NAS operations
- Scaling manufacturing partnership with Ability Composites and Northwind Composites

**Target Markets:**
- NASA scientific missions (aerosol monitoring, atmospheric sensing, ice zone observations)
- Disaster response and search & rescue
- Agricultural monitoring
- Remote sensing
- Environmental research

**Competitive Advantage:**
- Modular, extensible architecture supporting heterogeneous aircraft (including legacy NASA systems) without costly replacement
- Single-operator multi-vehicle capability reducing operational overhead
- Open interface (ROS-based) enabling third-party algorithm development
- Proven team expertise in cooperative UAS, NAS integration, extreme weather operations
- Early-stage FAA CoA approval pathway for multi-aircraft testing

## Notable Details

**Hardware & Software Choices:**
- **Robot Operating System (ROS):** Baseline middleware for distributed control and messaging; Phase I will evaluate costs/benefits vs. custom solution
- **Gumstix single-board computer:** Baseline; design will support hardware upgrades as more powerful/cost-effective options emerge
- **Android tablets:** SwiftTab basis, reducing cost and avoiding obsolescence through multiple vendor availability
- **P900 radio (Microhard):** Primary selection; generic radio architecture allows future upgrades

**NAS Integration Focus:**
- Proposes system architecture aligned with NASA Technology Roadmap goal of 4 UAS per operator
- Addresses NASA's need for certifiable, modular, easily-tested multi-UAS systems
- Positions technology toward larger NASA Decadal Survey goals (2500 autonomous agents)
- FAA CoA strategy developed in Phase I to enable flight testing early in Phase II

**Partnership:**
- University of Colorado Boulder RECUV provides multi-UAS expertise, algorithm development, and unique FAA multi-aircraft authorization
- Existing strong relationships between BST (Stachura, Elston) and CU (Frew, graduate students)
- CU's NSF I/UCRC leadership in unmanned aircraft provides research center infrastructure

**Phase I Deliverables:**
- Detailed architecture, circuit designs, multi-UAS testbed
- Implemented cooperative algorithms and three coordination demonstrations (via simulation)
- UI change requirement document
- FAA CoA strategy and NASA AFSRB documentation plan
- Phase II implementation roadmap

**Design Philosophy:**
- Layered OSI-based architecture for incremental verification and modular integration
- Open interfaces to avoid vendor lock-in and enable third-party contributions
- Support for legacy hardware integration to reduce obsolescence costs
- Gesture-based command interface to reduce operator cognitive load in multi-vehicle scenarios