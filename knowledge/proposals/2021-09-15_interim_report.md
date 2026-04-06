# A Novel Aerial Drone Platform for Exploration of Titan: 2019 Phase II Interim Report

## Document Metadata
- Type: SBIR Phase II Interim Report
- Client/Agency: NASA
- Program/Solicitation: 2019 SBIR Phase II, Contract Number 80NSSC19C0332
- Date: September 15, 2021
- BST Products/Systems Referenced: SwiftPilot (autopilot code v3.2), JSBSim flight simulator (BST fork), flight simulation environment
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies developed flight simulation and control systems for Creare's Titan Ringlet drone as part of a NASA SBIR Phase II contract. The project aims to create a flight simulation environment for both Earth and Titan atmospheres, design flight control algorithms for the ringlet drone platform, integrate avionics into a terrestrial prototype, and validate performance through hardware-in-the-loop simulation and terrestrial flight testing.

## Technical Approach

**Flight Simulation:**
- Extended BST's existing planetary flight simulation environment to model Titan and Earth atmospheres
- Developed detailed unmanned aircraft models of Creare's ringlet drones (both Titan-designed and terrestrial prototype variants)
- Implemented capability to switch between planetary models via command line interface (Titan, Venus, Earth)
- Integrated netCDF atmospheric model ingestion to allow scientists to input custom atmospheric models directly
- Implemented 3D weighted nearest-neighbor interpolation for pressure, temperature, density, and 3D winds across sparse models

**Flight Control & Autopilot:**
- Designed controller gains and algorithms for takeoff, landing, and mission execution in various flight modes
- Customized attitude control algorithms for multi-rotor and tail-sitter aircraft stability
- Implemented mixed control schemes combining both multi-rotor (4 rotors) and fixed-wing (2 elevons) control surfaces
- Anticipated flight modes: vertical hovering, transition to horizontal flight, horizontal flight, precision landing

**Hardware Integration & Testing:**
- Integrated avionics (autopilot hardware, ground station hardware) into terrestrial prototype built by Creare
- Utilized hardware-in-the-loop simulation prior to flight testing
- Developed flight test plan with NASA Airworthiness and Flight Safety Review Board approval process
- Planned terrestrial prototype flight testing with sub-scale ring-wing prototypes at local sites
- Final tests designed to demonstrate all flight modes and autonomous mission execution as analog to Titan operations

## Products & Capabilities Described

**SwiftPilot (Autopilot Code):**
- Version 3.2 featuring mixed control schemes
- Ability to coordinate multi-rotor control with fixed-wing aerodynamic control surfaces
- Tail-sitter control capabilities
- Supports various flight modes (hover, transition, cruise, precision landing)

**JSBSim Flight Simulator (BST Fork):**
- Planetary atmospheric model switching (command-line configurable)
- netCDF file format compatibility for custom atmospheric models
- 3D wind and weather property interpolation
- Supports Titan, Venus, and Earth atmospheric modeling

**Flight Simulation Environment:**
- Models planetary atmospheres with scientific accuracy
- Integrates custom atmospheric models from atmospheric scientists
- 3D weighted nearest-neighbor interpolation for sparse models

## Use Cases & Applications

**Primary Application: Titan Exploration**
- Aerial drone platform for exploring Titan's atmosphere and surface
- Ringlet drone design optimized for Titan's dense atmosphere (1.5x Earth pressure) and low gravity (1/7 Earth)
- Autonomous mission capability for scientific data collection

**Terrestrial Validation:**
- Boulder, CO flight testing to validate control algorithms and flight dynamics models
- Sub-scale prototype testing to gather baseline performance data before full-scale Titan mission
- Energy efficiency assessment of aerodynamic control surfaces vs. multi-rotor control

## Key Results (Interim Report Status)

**Completed Activities:**
- Simulator updates and bug fixes to JSBSim fork
- netCDF atmospheric model ingestion capability implemented
- 3D wind and atmospheric property interpolation system operational
- Autopilot code upgraded to SwiftPilot v3.2 with mixed control scheme capability

**In Progress (as of September 2021):**
- Awaiting flight permission for terrestrial prototype testing
- Simulator development continuing while awaiting regulatory approval
- Autopilot code enhancements for mixed control surface operation

**Planned Milestones (Original Schedule):**
- Complete simulation environment models (month 5)
- Complete drone flight dynamics models (month 11)
- Complete avionics integration with terrestrial prototype (month 13)
- Obtain flight permission (month 13)
- Complete terrestrial flight testing (month 16)

## Notable Details

**Partnership:** Collaboration with Creare (ringlet drone design and terrestrial prototype construction)

**Unique Capabilities:**
- BST's adaptable flight simulation environment now supports multiple planetary atmospheres
- Mixed control scheme combining rotors and aerodynamic control surfaces to assess energy efficiency trade-offs
- netCDF model compatibility enables integration with scientific atmospheric models from the research community
- Hardware-in-the-loop simulation for algorithm validation before terrestrial flight testing

**Technical Innovation:**
- The ringlet drone design represents a novel approach to Titan exploration adapted to its unique atmospheric and gravitational conditions
- Aerodynamic control surface assessment for energy optimization in dense atmospheres
- Ability to rapidly prototype and validate control algorithms across multiple planetary environments