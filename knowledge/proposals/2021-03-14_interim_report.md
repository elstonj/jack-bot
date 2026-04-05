# A Novel Aerial Drone Platform for Exploration of Titan – 2019 Phase II Interim Report

## Document Metadata
- **Type**: Interim Report (Phase II SBIR)
- **Client/Agency**: NASA
- **Program/Solicitation**: SBIR 2019; Contract Number 80NSSC19C0332
- **Date**: March 17, 2021
- **BST Products/Systems Referenced**: SwiftCore autopilot, S2 aircraft, JSBSim integration
- **Key Personnel**: Ben Busby (last editor)
- **Partner**: Creare (developing Titan Ringlet drone)

## Executive Summary
Black Swift Technologies developed a flight simulation environment for Titan and Earth atmospheres, integrated their SwiftCore autopilot into JSBSim, and conducted validation testing with the BST S2 aircraft model and Creare's Titan Ringlet drone. The project aimed to enable flight control development and performance validation for a terrestrial prototype before eventual deployment on Titan.

## Technical Approach

### Flight Simulation Environment
- Extended BST's existing planetary flight simulation capabilities to model Titan's atmosphere
- Developed unmanned aircraft models for both Creare's Titan Ringlet drone and terrestrial prototype variant
- Created networked Titan-GRAM atmospheric model integration via RESTful API deployed to https://atmosphere.bst.aero
- API structure: `/titan_gram/[lat]/[lon]/[alt]` returning JSON with temperature, density, pressure, wind vectors, and location data

### Autopilot Integration with JSBSim
- Integrated BST SwiftCore autopilot into JSBSim flight dynamics simulation
- Developed custom translation layers and plugin architecture to abstract JSBSim's poorly-documented interfaces
- Implemented socket-based communication (UDP from JSBSim, TCP from autopilot) using SDK-level CAN packet parsing
- Built command-line interface for headless operation, enabling remote execution and CI/GitLab integration
- Achieved 500Hz sensor polling rate—significant improvement over Gazebo (20-80Hz) and XPlane (20-80Hz)

### Flight Control Development
- Designed and developed controllers and tuning gains for takeoff, landing, and mission execution
- Customized attitude control algorithms for multi-rotor and tail-sitter aircraft
- Anticipated flight modes: vertical hovering, horizontal flight transition, horizontal flight, precision landing
- Simplified Python-based controller developed for collaboration with Creare on transition control optimization

### Avionics Integration & Testing Plan
- Integration of SwiftCore autopilot and ground station hardware into Creare's terrestrial prototype airframe
- Hardware-in-the-loop (HIL) simulation prior to physical flight testing
- Terrestrial flight testing in Boulder, CO with existing sub-scale ring-wing prototypes
- NASA Airworthiness and Flight Safety Review Board and Flight Readiness Review Board approval required

## Products & Capabilities Described

### SwiftCore Autopilot
- Provides attitude control and flight management for multi-rotor and tail-sitter aircraft
- Software-in-the-loop (SIL) interface with JSBSim via TCP socket
- Generic CAN packet parsing for simplified message definition and extensibility
- 500Hz sensor polling capability

### S2 Aircraft
- BST's existing aircraft model, used for validation testing on both Earth and Titan
- Successfully demonstrated in 1-minute glide tests on Titan (commanded 18 m/s, motors disabled)
- Showed significant performance improvement on Titan due to low gravity (9.81 m/s² Earth vs. 1.35 m/s² Titan) and higher atmospheric density

### Creare Titan Ringlet Drone
- Multi-rotor design adapted from terrestrial prototype
- Intended for atmospheric and aerodynamic exploration of Titan
- Motor model issues identified during Titan simulation testing (insufficient lift for takeoff/hover)—under investigation with Creare

### Titan-GRAM Atmospheric Model API
- Modified FORTRAN-based Titan-GRAM code to support networked queries
- Removes user input requirements and hardcoded paths
- Handles concurrent requests via unique ID assignment
- Returns: model name, temperature (K), density (kg/m³), pressure (N/m²), east/north wind (m/s), lat/lon, altitude

## Use Cases & Applications

### Primary Application
Exploration of Titan's atmosphere via aerial drone platform, enabling:
- Atmospheric sampling and analysis
- Aerodynamic testing in Titan's unique environment (1.5x Earth atmospheric density, lower gravity)
- Autonomous mission execution with precise landing capability

### Terrestrial Validation
- Prototype flight testing in Boulder, CO to demonstrate all flight modes
- Data-gathering flights at local sites to validate simulation models
- Autonomous mission analog to desired Titan behavior

## Key Results

### Completed/Verified
1. **Networked Titan-GRAM integration**: RESTful API operational, supporting concurrent requests with JSON atmospheric data response
2. **JSBSim autopilot integration**: Fully functional socket-based interface with 500Hz real-time execution capability
3. **S2 aircraft validation**: Successfully demonstrated straight-and-level glide flight on Titan in simulation (1-minute test), showing improved performance vs. Earth baseline
4. **Simulation performance**: 500Hz polling rate achieved, enabling realistic sensor and control model testing

### Outstanding Issues
- **Creare Ringlet Titan model**: Motor lift insufficient for takeoff/hover in simulation; root cause under investigation with partner

## Project Schedule Status (as of March 2021)
- Month 5: Complete simulation environment models ✓
- Month 11: Complete drone flight dynamics models ✓
- Month 13: Complete avionics integration with terrestrial prototype (in progress)
- Month 13: Complete flight permission (in progress)
- Month 16: Complete terrestrial flight testing (pending)

## Notable Details

### Technical Innovations
- Forked JSBSim internally to allow model additions and core modifications without affecting upstream repository
- Generic CAN packet approach eliminates boilerplate code and simplifies packet type modifications
- Python-based architecture enabling easy collaboration with external partners (Creare)
- Simplified external controller allowing shared development on transition logic

### Unique Capabilities Demonstrated
- End-to-end cross-planetary simulation (same aircraft model flown on both Earth and Titan)
- Real-time atmospheric model integration via web service
- Significant simulation speed improvement (25x faster than prior tools) for controller development
- Hardware-in-the-loop workflow supporting realistic sensor and flight control validation

### Partnership & Integration
- Close collaboration with Creare (drone airframe provider)
- BST responsible for all flight control, autopilot, simulation, and avionics integration
- External controller architecture allows Creare participation in transition control development

### Competitive/Unique Positioning
- BST's existing planetary flight simulation infrastructure adapted for Titan atmosphere
- Proprietary SwiftCore autopilot customized for novel low-gravity, high-density flight environment
- Network-accessible atmospheric model supporting distributed simulation and development