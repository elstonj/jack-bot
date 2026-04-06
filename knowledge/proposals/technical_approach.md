# 2020 Venus SBIR Phase II Technical Approach

## Document Metadata
- Type: Technical approach (proposal component)
- Client/Agency: NASA (SBIR Phase II)
- Program/Solicitation: Venus SBIR (Phase II)
- Date: 2020 (submitted/proposal; document modified 2021-11-11 to 2021-11-13)
- BST Products/Systems Referenced: SwiftCore autopilot, HWIL (Hardware-in-the-Loop) simulation capability, Titan Ringlet drone (previous version), Venus Ringlet aircraft (proposed)
- Key Personnel: Jack Elston (last editor)
- Partner: Creare (UAS hardware partner)

## Executive Summary
Black Swift Technologies proposed extending its planetary simulation capabilities to model Venus atmospheric conditions and develop a high-fidelity unmanned aircraft model based on Creare's UAS design. The Phase II effort would validate a concept of operations for autonomous aircraft operations in the Venus upper atmosphere, including balloon docking procedures, through Earth analog flight testing and integrated simulation.

## Technical Approach

### Simulation Environment Development
- BST possesses an existing catalog of Venus atmospheric datasets from multiple sources at scales sufficient for simulating small aircraft flight through various Venus atmospheric regions (day and night conditions)
- Established relationships with Venus atmospheric modeling groups for generating custom data if needed
- Initial Phase II work will identify and select optimal atmospheric datasets representing full mission profile including rapid altitude changes and balloon docking procedures

### Aircraft Modeling
- BST has a simplified workflow for aircraft model creation using an established framework
- Will develop Venus Ringlet aircraft model (based on Creare UAS design) for both Earth and Venus environments
- Earth analog model will be validated through flight testing; discrepancies used to improve Venus model
- Medium-fidelity aerodynamic database will be generated using Euler or panel methods
- Database will account for varying aircraft attitude, control surface deflections, and airspeeds

### Docking Scenario Simulation
- Development of simulated docking scenario with Creare-selected hardware-based sensor simulation
- Creation of simplified but accurate simulated balloon for concept validation
- Essential for evaluating controller accuracy and validating UAS docking capability post-release

### Flight Control & Algorithms
- Customization of existing attitude control algorithms originally developed for multirotors and tailsitter aircraft
- Support for multiple flight modes: balloon gondola release, vertical hovering, transition to horizontal flight, horizontal cruise, and precision docking
- Approach leverages existing software to minimize implementation effort

### Hardware & Avionics Integration
- BST previously provided Creare with CAD versions of SwiftCore autopilot hardware for Earth analog prototype avionics compartment sizing
- Phase II will use Phase I vehicle design to inform propulsion system and component selection
- Early Phase II: procurement and installation of complete vehicle setup (avionics, propulsion, power) into Earth analog prototype

### Validation & Flight Testing
- HWIL testing using actual hardware before live flight testing
- Flight approval process through NASA AFSRB (Aerospace Safety Review Board) and FRRB (Flight Readiness Review Board)
- Initial flight tests with Phase I vehicle at local sites for parameter logging and data gathering
- Final demonstration flights in Boulder, CO showing all flight modes plus autonomous mission analog to Venus operations

## Products & Capabilities Described

### SwiftCore Autopilot
- BST's autopilot system for aircraft control
- Modular avionics setup compatible with multiple aircraft platforms
- Customizable attitude control algorithms
- Previously provided to Creare in CAD format for design integration

### HWIL (Hardware-in-the-Loop) Simulation
- BST's simulation capability allowing hardware testing before live flight
- Enables validation of algorithms using actual flight hardware in simulated environments
- Used for pre-approval testing to derisk flight campaigns

### Planetary Simulation Capability
- Existing BST infrastructure for atmospheric and environmental simulation
- Previously developed for other planetary missions (mentioned Titan Ringlet reference)
- Extensible to Venus conditions

### Venus Ringlet Aircraft
- Proposed unmanned aircraft design based on Creare UAS partnership
- Medium-fidelity aerodynamic modeling capability
- Support for multiple flight regimes and autonomous docking

## Use Cases & Applications

**Primary Application:** Venus upper atmosphere scientific operations
- Autonomous aircraft operating in Venus atmosphere (altitude profile and conditions TBD)
- Release from high-altitude balloon gondola
- Autonomous horizontal flight and precision docking return to balloon
- Day and night operations in Venus atmospheric conditions
- Alternative platform for Venus atmospheric sampling/observation

**Earth Analog Testing:** Boulder, CO flight test campaign demonstrating prototype capability before Venus application

## Notable Details

- **Leverage of Existing Work:** Proposal builds on prior SBIR work and Titan Ringlet drone development; emphasis on reusing proven algorithms and frameworks
- **Partnership Integration:** Close collaboration with Creare on hardware design, sensor selection, and vehicle integration
- **Regulatory Path:** Clear identification of NASA approval process (AFSRB/FRRB) required for flight testing
- **Validation Strategy:** Two-phase validation: simulation (HWIL) → flight testing → algorithm refinement
- **Atmospheric Data:** BST maintains relationships with active Venus modeling research groups, enabling access to current atmospheric models
- **Competitive Advantage:** Combination of planetary simulation expertise, autopilot/control systems, and prior Earth UAS experience positions BST to bridge terrestrial and planetary flight operations

## Status Note
This document is part of a "Completed/Inactive/Unsubmitted Projects" folder, suggesting this particular proposal or project phase may not have been funded or has concluded.