# Autonomous Quad-Biplane Flight Controller - Month 7 Interim Report

## Document Metadata
- Type: Interim Project Report
- Client/Agency: Creare (SBIR Project)
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: December 20, 2019
- BST Products/Systems Referenced: SwiftTab (ground control station), Autopilot flight control algorithms, flight controller hardware
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing an autonomous flight controller for Creare's Quad-Biplane VTOL aircraft for potential shipboard operations. Month 7 focused on refactoring the SwiftTab ground control software to support VTOL vehicle types alongside existing fixed-wing and multicopter platforms, conducting thrust stand validation testing, and updating project milestones.

## Technical Approach

### Autopilot Algorithm Development
- Adapted existing BST autopilot flight control algorithms for Quad-Biplane application
- Customized attitude control algorithms designed for multi-rotor stable flight
- Developing "outer loop" controller for mission objectives (flight trajectory, altitude) that feeds targets to stable flight algorithms
- Flight modes to support: vertical hovering (takeoff), transition to horizontal flight, horizontal flight, precision landing

### Precision Landing
- Creare developing Landing Location Detection software to visually identify shipboard landing target coordinates
- BST autopilot receives relative coordinates to fine-tune flight path
- Target precision: 0.1 m accuracy in no-wind conditions

### Ground Control Station
- Integrated Quad-Biplane algorithm into ground flight controller system
- Features: mission planning, flight monitoring, autonomous mission execution

### Integration & Testing Approach
- Local flight testing in Boulder, CO (14 CFR Part 107 compliance, with altitude waivers requested)
- BVLOS testing campaign at Griffiss UAS test site in Rome, NY
- Demonstration of all flight modes including precision landings on moving platform (simulating shipboard operations)

## Products & Capabilities Described

### SwiftTab (Ground Control Station)
- **What it is**: Ground control software for planning and executing autonomous missions
- **Refactoring work**: Redesigned from vehicle-type-specific architecture to vehicle-agnostic architecture
  - Previous design: Instance checks throughout code with duplicated UI elements and controllers
  - New design: Abstract top-level UAV class with abstract methods for all vehicle types (fixed-wing, multicopter, VTOL)
  - Benefits: Code reuse, reduced boilerplate, easier testing, net reduction in lines of code
- **Specific improvements**: 
  - LandingView and LaunchView consolidated across vehicle types
  - Rotor objects and surface calibration moved to top-level abstract adapter
  - UI elements now use vehicle-agnostic constructors

### BST Autopilot System
- Flight control algorithms for attitude stability
- Outer loop controller for mission-level navigation
- Integration with ground control station
- Motor performance characterization (KDE motor evaluation)

## Use Cases & Applications
- **Shipboard VTOL Operations**: Autonomous takeoff, transition, flight, and precision landing on moving ship decks
- **Aerosol Sensor Deployment**: Aircraft equipped with NOAA aerosol sensor instrument
- **BVLOS Operations**: Extended range autonomous missions beyond visual line of sight

## Key Results

### Thrust Stand Validation
- Validated KDE motor performance charts against BST test stand measurements
- Corrected for density altitude differences (3300' KDE vs. 5500' BST)
- Strong agreement between KDE published data and BST test measurements enabled use of KDE performance data in controller
- Motor performance curve fit implemented in simulation

### SwiftTab Refactoring Results
- Successful code generalization enabling VTOL support without duplicating fixed-wing and multicopter code
- Reduction in total codebase lines
- Vehicle-agnostic UI structure replacing prior vehicle-specific directory structure
- Ready for VTOL testing with lower risk of new bugs due to code heritage

### Schedule Status
- **Work Completed**: ~50% of contract hours (244 of 524 hours) at Month 7
- **Upcoming Milestones**:
  - Small prototype flight testing completion: End of January (with onboard camera)
  - First Double Eagle flights: February
  - Creare test flights in Rome, NY: Last two weeks of April

## Notable Details
- **Test Aircraft**: "Double Eagle" aircraft designated for VTOL testing
- **Static Testing**: Motor testing performed on BST's static thrust stand
- **Collaboration**: Joint meetings with Creare; Creare has prior experience with drone operations from moving platforms
- **Regulatory**: Operating under 14 CFR Part 107 with waiver requests for operations above 400 feet (within line of sight)
- **Test Site**: Griffiss UAS test site in Rome, NY for BVLOS testing clearance