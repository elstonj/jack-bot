# Autonomous Quad-Biplane Flight Controller - Month 6 Interim Report

## Document Metadata
- Type: Interim Progress Report
- Client/Agency: Creare (SBIR subcontractor)
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: 2019-11-20
- BST Products/Systems Referenced: Black Swift Autopilot, Ground Flight Controller, Tablet UI
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is providing autopilot design and engineering services to Creare for development of an autonomous Quad-Biplane flight controller capable of VTOL shipboard operations. During Month 6, BST built and flight-tested a small prototype tailsitter aircraft to validate autopilot algorithms before transitioning to the larger Double Eagle platform, achieving 8 successful transition tests in up to 7 mph winds.

## Technical Approach

### Autopilot Algorithm Development
- Adapting existing Black Swift autopilot flight control algorithms for Quad-Biplane application
- Customizing attitude control algorithms from multi-rotor systems for stable flight control
- Developing "outer loop" controller for mission objectives (flight trajectory, altitude) that sets control targets for stable flight algorithms
- Leveraging existing software to minimize implementation efforts

### Precision Landing Algorithm
- Creare developing Landing Location Detection software for visual identification of shipboard landing targets
- Black Swift autopilot receives relative coordinates to fine-tune flight path
- Target accuracy: 0.1 m in no-wind conditions

### Ground Controller Implementation
- Integrating Quad-Biplane algorithm into ground flight controller system
- Features include operator planning, mission monitoring, and autonomous flight execution

### Flight Testing Strategy
- Local testing in Boulder, CO (within 14 CFR Part 107)
- BVLOS testing campaign at Griffiss UAS test site in Rome, NY
- Test objectives: all flight modes, precision landings on moving platform (simulating shipboard operations)
- Creare providing guidance on moving platform operations based on prior drone experience

## Products & Capabilities Described

### Black Swift Autopilot
- Modular flight control system adaptable to various aircraft configurations
- Supports multiple flight modes: vertical hovering, transition, horizontal flight, precision landing
- Attitude control and outer-loop trajectory/altitude control capabilities
- Mission execution loop architecture

### Ground Flight Controller System
- Tablet-based UI for mission planning and monitoring
- Autonomous mission profile execution
- VTOL-specific interface elements

### Avionics Integration
- Black Swift providing suitable avionics hardware selection and integration support
- Compatible with NOAA aerosol sensor instrument payload
- Radio integration coordination with Creare and avionics selection

## Use Cases & Applications

**Primary Application:** Autonomous VTOL shipboard operations for NOAA aerosol sampling
- Precision landing on ship decks (0.1 m accuracy target)
- Beyond Visual Line of Sight (BVLOS) capable
- Integration with NOAA aerosol sensor instrument

**Flight Modes Tested:**
- Vertical hovering (takeoff/landing)
- Transition to/from horizontal flight
- Horizontal cruise flight
- Precision landing with visual target detection

## Work Completed (Month 6)

### Small Testbed Aircraft Development
- Built scaled prototype tailsitter with comparable performance to larger Double Eagle platform
- Design specifications:
  - Clark-Y airfoil
  - 0.914 m wingspan
  - 0.278 m² wing area
  - 1.6 kg mass
  - 5.76 kg/m² wing loading
  - 14 m/s cruise speed
  - Fiberglass/foam core wings on modified DJI FW450 airframe

### Flight Testing Results
- **8 transition tests completed successfully** in up to 7 mph winds
- Smooth takeoff and transition sequence validated
- Safe height: 1 m, climbout height: 2 m, climbout angle: 90° (vertical)
- Transition back to hover and manual landing demonstrated
- No incidents reported

### Avionics & Hardware
- Small prototype equipped with identical avionics to Double Eagle platform
- Enabling direct algorithm validation before larger platform integration

### User Interface Development
- Added VTOL vehicle type to communications protocol
- Implemented base VTOL vehicle type functionality in tablet UI
- Began tablet logic development for VTOL-specific UI elements (windows, dialogs)

## Remaining Work Items (Next Month)

1. Add 7.5° motor cant with shims to match Double Eagle configuration and compare flight performance
2. Complete implementation and flight-test automated landing transition algorithm
3. Perform 20 consecutive prototype flights without issues (code validation gate)
4. Begin hover testing and tuning of Double Eagle platform
5. Initiate transition flight testing of Double Eagle after prototype objectives complete

## Notable Details

- **Reference Aircraft:** Double Eagle serves as baseline performance model
  - 2.44 m wingspan, 2.44 m² wing area, 16 kg mass
  - SD7080 airfoil, 18 m/s cruise speed
  - Significantly larger than prototype (10x mass ratio)

- **Modeling & Simulation:** XFLR5 aerodynamic analysis used for aircraft design validation and performance prediction

- **Scalable Testing Approach:** Prototype platform enables risk reduction before Double Eagle transition, validating all control algorithms, estimation algorithms, and transition logic

- **Regulatory Path:** Part 107 compliant local testing with waiver requests for altitude operations above 400 feet

- **Integration Coordination:** BST working with Creare, NOAA, and Griffiss test range for avionics, payload, and airspace coordination