# Autonomous Quad-Biplane Flight Controller - Month 12 Report

## Document Metadata
- Type: Interim Report
- Client/Agency: Creare (subcontractor role for NOAA aerosol sensor integration)
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: 2020-05-20
- BST Products/Systems Referenced: Black Swift Autopilot, Ground Flight Controller System
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies was engaged by Creare to develop autonomous flight control algorithms and ground control systems for a Quad-Biplane aircraft capable of VTOL shipboard operations. This Month 12 report documents continued flight testing progress, including successful autonomous transition testing on a small prototype and the larger "Double Eagle" platform, along with ongoing debugging of airspeed sensor issues.

## Technical Approach

### 1. Autopilot Algorithm Development
- Adapted BST's existing autopilot flight control algorithms for Quad-Biplane application
- Customized attitude control algorithms (originally developed for multi-rotor stability) for high-stability fixed-wing flight control
- Developed "outer loop" controller for mission objectives (flight trajectory, altitude) that commands targets to stable flight algorithms
- Leveraged existing BST software to minimize implementation effort

### 2. Precision Landing Algorithm
- Coordinated with Creare's Landing Location Detection software (visually identifies shipboard landing target coordinates)
- BST autopilot integrates relative coordinate data for precision landing path refinement
- Target accuracy: 0.1 m in no-wind conditions for shipboard deck landings

### 3. Ground Controller Implementation
- Integrated Quad-Biplane algorithm into ground flight controller system
- Features: mission planning, flight monitoring, autonomous mission execution

### 4. Avionics Integration Support
- Worked with Creare to identify suitable avionics, radios, and NOAA aerosol sensor integration
- Provided autopilot hardware and ground station hardware to Creare for integration

### 5. Flight Testing Plan
- Local testing near Boulder, CO (within 14 CFR Part 107 regulations)
- Advanced testing at Griffiss UAS test site in Rome, NY for Beyond Visual Line of Sight (BVLOS) operations
- Altitude waivers requested (above 400 ft but within line of sight)
- Test objectives: all flight modes, precision landings on moving platform (simulating shipboard operations)

## Products & Capabilities Described

### Black Swift Autopilot
- Multi-mode flight control system capable of:
  - Vertical hovering (takeoff)
  - Transition to horizontal flight
  - Horizontal fixed-wing flight
  - Precision landing with <0.1m accuracy
- Attitude control: roll and pitch control loops with fast response times (0.51-0.52 seconds for Double Eagle)
- Supports autonomous waypoint navigation

### Ground Flight Controller System
- Mission planning and execution
- Real-time flight monitoring
- Autonomous operation command and control

## Use Cases & Applications

**Primary Application:** Autonomous shipboard operations for the Quad-Biplane
- VTOL operations from moving naval platforms (ship decks)
- Payload delivery: NOAA aerosol sensor instrument
- Precision landing under challenging maritime conditions
- BVLOS operations for extended range missions

## Key Results (Month 12 Report)

### Small Prototype Testing
- 28 flights across 6 test days
- Successfully tested autonomous transition algorithms, forward flight, and return transition
- Forward flight achieved at 12 m/s ground speed (~15 m/s airspeed)
- Issues identified:
  - **Airspeed sensor problem**: Pitot tube system (same used on BST fixed-wing aircraft) reading inaccurately (~4 m/s max vs. expected 10-15 m/s). Debugging ongoing; temporarily using GPS speed for feedback instead
  - Rotor controller saturation on lower end requiring further tuning

### Double Eagle Hover Testing
- 30 hover tests across 3 days
- Full autonomous waypoint navigation achieved
- Excellent control loop performance:
  - Roll control: 0.52s response time, no overshoot
  - Pitch control: 0.51s response time, no overshoot
  - (Note: <1 second response is considered excellent for fixed-wing aircraft)

### Double Eagle Transition Testing
- 4 successful transition flights
- Smooth transitions to 70° forward pitch (20° pitched up in fixed-wing frame)
- Achieved 12 m/s ground speed at ~0° angle of attack
- Stable transitions both forward and reverse with no major stability issues

## Notable Details

- **Platform Designation**: "Double Eagle" (larger platform than small prototype)
- **Technical Achievements**: Very fast control response times indicate well-tuned attitude control algorithms; ability to handle multi-mode flight (VTOL/transition/forward-flight) in single airframe
- **Technical Challenges**: Pitot airspeed measurement reliability in VTOL configuration requires resolution (temporary GPS-based solution)
- **Regulatory Approach**: Leveraging Part 107 for initial testing, pursuing waivers and BVLOS clearance through FAA coordination with Griffiss test site
- **Cross-organizational Collaboration**: Integration with Creare's landing detection algorithms and NOAA sensor payload; leveraging Creare's experience with drone operations from moving platforms