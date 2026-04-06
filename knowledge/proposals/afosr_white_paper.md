# Communication Aware Avionics

## Document Metadata
- **Type:** White Paper / SBIR Phase I Proposal
- **Client/Agency:** Air Force Office of Scientific Research (AFOSR)
- **Program/Solicitation:** AFOSR SBIR (topic area not specified)
- **Date:** Submitted December 15, 2012 (modified January 9, 2013)
- **BST Products/Systems Referenced:** Communication-aware avionics system (prototype under development); Tempest UAS system (Vortex2)
- **Key Personnel:** Jack Elston (President, Black Swift Technologies); Eric Frew (Director, Research and Engineering Center for Unmanned Vehicles, University of Colorado Boulder)

## Executive Summary
Black Swift Technologies proposes to develop a commercially viable, tightly integrated avionics system that unifies autopilot, flight computer, and mesh-based network functionality for small unmanned aircraft. By enabling direct communication between the communications subsystem and control algorithms, the system will support advanced autonomous capabilities including delay-tolerant networking, data ferrying, and communication-aware mission planning—addressing a critical gap in current small UAS avionics offerings.

## Technical Approach

**Core Innovation:** Tight integration of three traditionally separate systems:
- Autopilot
- Flight computer
- Mesh-based network solution (using COTS radios)

**Key Integration Features:**
- Low-level interfaces between communication, flight computer, and autopilot subsystems
- Communications subsystem has access to aircraft telemetry to intelligently route data and adjust radio parameters based on aircraft state
- Control algorithms have direct access to autopilot and communication interfaces
- Support for multiple link interfaces and radio types per platform
- Modular and programmable router architecture with hierarchical management
- Gateway functionality to bridge legacy and disparate networks

**Software Architecture:**
- Implementation of NetUAS architecture (developed at University of Colorado)
- Service discovery mechanisms
- Firmware providing communication statistics and control
- Communication-centric libraries for networking and control primitives
- Real-time user interface updated dynamically based on environmental changes

## Products & Capabilities Described

### Communication-Aware Avionics System
- **What it is:** An integrated avionics package combining autopilot, flight computer, and mesh networking into a single, tightly coupled system
- **Proposed use:** Enable small UAS to conduct communication-aware missions where routing, network topology, and mission planning are jointly optimized
- **Key capabilities:**
  - Support for multiple COTS radios with different protocols and frequencies
  - Mobile ad-hoc quasi-stable mesh network management
  - Interdependent switching/routing, topology management, and QoS
  - RF localization, delay-tolerant networking, controlled mobility in airborne mesh networks, RF-based SLAM

### Prototype (Existing System)
- BST has already developed a prototype at University of Colorado Boulder
- Interfaces to three different COTS radios operating on different protocols and frequencies
- Airborne and ground-based node capability
- Onboard NetUAS implementation enabling service discovery and heterogeneous network gateways

## Use Cases & Applications

- **Data ferrying:** Using aircraft mobility to transport data between disconnected network segments
- **Delay-tolerant networking:** Operating in environments with intermittent connectivity
- **Network-centric missions:** Maintaining constant communication with ground stations or specific nodes
- **Cooperative multi-platform operations:** Chaining aerial and mobile ground nodes to extend and maintain data links
- **Real-time collaborative sensing:** Gathering data from distributed ground nodes using aircraft as mobile relays
- **RTK GPS applications:** Leveraging network timing precision for accurate positioning
- **Road surveillance:** AFRL-referenced application using communication-aware chaining

**Historical Examples Referenced:**
- Vortex2 Tempest UAS system (tornado observation, demonstrated chaining of aerial and mobile ground nodes)
- AFRL road surveillance UAS (cooperative tracking with communication-aware coordination)

## Technical Objectives

1. **Hardware modification:** Implement full communication-aware solution as commercially viable product with low-level interfaces between communication, flight computer, and autopilot

2. **Firmware development:** Provide communication statistics and control, aircraft control and telemetry through standard interfaces for autonomous guidance algorithms

3. **Software libraries:** Create communication-centric libraries providing networking and control primitives for communication-aware tasks (data gathering from ground nodes, maintaining contact with specific nodes)

4. **User interface:** Tailor interface to provide mission planners with real-time information on communication capabilities and control state of all network nodes; update dynamically based on environmental changes (noise, interference)

## Program Timeline & Budget

**PHASE I:** Concept and design (6 months assumed)
- Deliverables: Conceptual models, functional requirements, component architectures, communications radio identification and interfaces, avionics system design, autopilot interfaces, user interface design, test plan with airspace access strategy

**PHASE II:** Prototype development and flight validation
- Deliverables: Functional prototype demonstration, final documentation and software, Concept of Operations for sampling missions, Phase II final report
- Key objective: Gain airspace access and validate system through experimentation

**PHASE III:** Commercialization and regulatory pathway
- Deliverables: Production-ready software, hardware, documentation
- Focus: Path to commercialization, NAS (National Airspace System) compliance, targeting public entities initially (predating commercial UAS authorization)

## Notable Details

**Competitive Position:**
- Identified gap: No commercially available integrated avionics system currently supports communication-aware mission architectures
- Existing work has been "very specific to the particular application" and lacks generalizability
- BST's approach provides the first general, commercializable solution

**Existing Research Foundation:**
- Based on peer-reviewed publications and proven field operations (Tempest/Vortex2, AFRL projects)
- Builds on University of Colorado's NetUAS architecture research
- Jack Elston and Eric Frew are recognized experts in UAS communications and control

**Regulatory Awareness:**
- Document acknowledges current regulations require mission termination upon communication failure
- Phase III explicitly addresses how to overcome NAS (National Airspace System) regulations
- Strategy includes targeting public entities initially, before commercial airspace is opened

**Technology Maturity:**
- Prototype already operational at University of Colorado
- Proof-of-concept demonstrated in field research
- Proposal moves from research prototype to commercial product