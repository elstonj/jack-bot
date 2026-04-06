# Autonomous Quad-Biplane Flight Controller - Month 9 Interim Report

## Document Metadata
- Type: Interim Project Report (Month 9)
- Client/Agency: Creare (subcontractor); NOAA (end user for aerosol sensor)
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: 2020-02-20
- BST Products/Systems Referenced: Black Swift Autopilot, Ground Flight Controller System
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing an autonomous flight control system for Creare's Quad-Biplane VTOL aircraft capable of shipboard operations. This interim report documents Month 9 progress on autopilot algorithm development, firmware improvements to attitude control, and initial flight testing of two prototype platforms (small tailsitter and Double Eagle). The team addressed yaw control deficiencies through motor cant modifications and quaternion-based controller refinements while encountering structural issues with the Double Eagle motor mounts.

## Technical Approach

### Autopilot Algorithm Development
- Adaptation of BST's existing autopilot flight control algorithms for Quad-Biplane multi-rotor application
- Customization of attitude control algorithms to handle multiple flight modes: vertical hovering (takeoff), transition to horizontal flight, horizontal flight, and precision landing
- Development of "outer loop" controller to achieve mission trajectory and altitude objectives, setting control targets for stable flight algorithms
- Leverage of existing BST software to minimize implementation efforts

### Attitude Control & Motor Cant
- Added 6° cant to motors on small tailsitter prototype to improve yaw control in high winds
- Motor cant achieved using washers under motor mounts
- Testing validated code improvements prior to Double Eagle flight testing
- Resulted in significantly better yaw control performance in wind conditions

### Quaternion-Based Attitude Controller Refinement
- Identified issue with initial full state attitude controller: magnitude of control effort normalized across all three axes to 1, causing insufficient control authority on yaw axis during forward flight
- Problem manifested as "curvy" flight paths and poor heading control
- Implemented new "reduced attitude state control" technique using two-step process:
  1. First step: Formulate control inputs for "tilt" controller (aircraft z-axis direction) and yaw controller
  2. Combined into full state controller with proper scaling
  3. Third control axis calculated separately
- New formulation allows better control authority distribution and improved heading control

### Navigation & Path Tracking
- Continued work on controller implementation with modifications to improve navigation tracking
- State machine updates to transition code from prototype to production state
- Multiple code fixes and simulations to validate changes with focus on safety improvements

## Products & Capabilities Described

### Black Swift Autopilot
- Existing flight control algorithms adapted for Quad-Biplane application
- Supports multiple flight modes (hover, transition, horizontal flight, precision landing)
- Quaternion-based attitude control with refined control authority distribution
- Integrates with precision landing algorithms developed by Creare
- Supports ground controller system for mission planning, monitoring, and autonomous flight execution

### Ground Flight Controller System
- Integration of Quad-Biplane algorithms into ground station
- Features for operators to plan, monitor, and execute autonomous mission profiles
- Support for BVLOS (Beyond Visual Line of Sight) testing capabilities
- Hardware provided by BST for integration with Creare's platform

## Use Cases & Applications

### Shipboard Operations
- Precision landing on ship decks with target accuracy of 0.1 m in no-wind conditions
- Support for landing on moving platforms (carrier operations)
- Quad-Biplane capable of vertical takeoff and horizontal flight for shipboard deployment

### Mission Instrument Payload
- Integration support for NOAA's aerosol sensor instrument
- Identification and integration of suitable avionics and radios

### Flight Testing Locations
- Local testing in Boulder, CO (14 CFR Part 107 compliant operations)
- Griffiss UAS test site in Rome, NY (BVLOS testing campaign)
- Altitude waiver requests for operations above 400 feet within line-of-sight

## Testing & Development Status

### Small Tailsitter Prototype
- Completed testing of motor cant modifications (6°)
- Demonstrated improved yaw control in wind conditions
- Code validation platform for Double Eagle implementation

### Double Eagle Platform
- Initial flight testing begun in February 2020
- **Critical Issue Discovered:** Motor mounts lack structural integrity to handle rotor loads
- Complete failure of one motor mount during rotor spin-up; others showing varying degrees of damage
- BST working with Creare to obtain new motor mount design and resume testing

## Notable Details

- **Precision Landing Requirement:** 0.1 m accuracy in no-wind conditions via Creare's Landing Location Detection software providing relative coordinates to BST autopilot
- **Partnership Structure:** BST (autopilot and flight control), Creare (platform design, landing detection, regulatory coordination), NOAA (sensor payload)
- **Regulatory Approach:** Initial Part 107 compliant local flights with altitude waiver requests; BVLOS testing through Griffiss UAS test site clearance
- **Software Maturation Goal:** Transition code from prototype to production state with emphasis on safety improvements and state machine robustness
- **Control Architecture:** Outer loop (mission-level) controlling inner loop (stable flight algorithms) with separation of concerns for algorithm reusability