# Website Boxes - Terrain Following

## Document Metadata
- Type: NASA SBIR Phase II Proposal Supporting Material (website content boxes)
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR Phase II
- Date: 2019-01-25 (document creation/modification date)
- BST Products/Systems Referenced: S2 UAS, SwiftCore Flight Management System
- Key Personnel: Not named in this document

## Executive Summary
BST proposes a Phase II effort to develop an autonomous terrain-following and obstacle-avoidance system for fixed-wing UAS (extensible to multi-rotor platforms). The system uses state-of-the-art sensors, control algorithms, and onboard processing to enable low-altitude automated flight in rugged terrain, forests, and degraded visibility conditions. The technology will be integrated with the S2 UAS and advance from TRL 5 to TRL 7.

## Technical Approach
- **Sensor Diversity**: Multi-sensor suite designed to function in degraded conditions (low light, fog, heavy precipitation)
- **Machine Perception & Cognition**: High-level decision-making algorithms for terrain identification and avoidance
- **Modular Design**: Built to integrate across multiple UAS platforms, specifically targeted for S2 UAS integration
- **Integration Point**: SwiftCore Flight Management System on S2 UAS
- **Key Technical Components**:
  - Simulation environment for high-fidelity mission recreation
  - Terrain-following and obstacle-avoidance algorithms
  - Sensor fusion for obstacle identification
  - Software and hardware interfaces for sensor/processing suite integration

## Products & Capabilities Described

### S2 UAS
- Mission-proven platform from previous NASA SBIR successes
- Already tested in NASA campaigns (including volcanic vent sampling in Costa Rica)
- Will serve as primary demonstration platform for Phase II work
- First commercial deployment target for terrain-following technology

### SwiftCore Flight Management System
- Flight control system on S2 UAS
- Will integrate new sensing and processing suite for autonomous terrain navigation

## Use Cases & Applications

### NASA Applications
- Volcanic vent sampling (demonstrated need identified in Costa Rica campaign)
- Higher-resolution soil moisture measurements (using BST sensor)
- Surface flux calculations above arctic tundra
- Transfer to legacy NASA UAS platforms

### Non-NASA Applications
- Infrastructure inspection with reliable low-altitude flights
- Leak detection
- Mountain mapping and survey applications
- Rock slide mitigation
- Avalanche prediction
- Geographic information systems (GIS) and survey operations

## Technical Objectives & Deliverables

**Phase II Objectives:**
1. Complete system design from Phase I foundation
2. Validate with flight testing
3. Enable low-altitude fixed-wing flight in all terrain types (mountains, forests)

**Key Deliverables:**
1. **Simulation Environment**: Finalized high-fidelity mission simulation with improved environment models and enhanced simulated sensor suite
2. **Algorithm Development**: Terrain-following, obstacle identification (sensor fusion), and obstacle avoidance algorithms validated in both simulation and flight hardware
3. **Hardware Development**: Software and hardware interfaces integrating sensing/processing suite to SwiftCore on S2 UAS
4. **Flight Testing**: Demonstration flights validating automatic terrain following and obstacle avoidance in relevant environments

## Technology Readiness Level Progression
- **Start (Phase I)**: TRL 5 (Component/breadboard validation in relevant environment)
- **End (Phase II)**: TRL 7 (System prototype demonstration in operational environment)

## Notable Details
- **Extensibility**: While focused on fixed-wing aircraft, system is designed to extend to multi-rotor platforms
- **Weather Resilience**: Unique emphasis on sensor diversity for operation in degraded visibility (fog, precipitation, low light)
- **Commercial Path**: Phase II work explicitly positioned as first step toward commercialization through S2 integration
- **Problem Origin**: Need for terrain-following capability identified during actual NASA field campaign (Costa Rica volcanic monitoring), demonstrating real operational requirement
- **Competitive Advantage**: Fixed-wing focus addresses gap in the market; most autonomous low-altitude terrain navigation work has focused on multi-rotor platforms