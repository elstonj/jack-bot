# Autonomous Quad-Biplane Flight Controller – Month 3 Report

## Document Metadata
- **Type:** Interim Project Report
- **Client/Agency:** Creare (subcontractor)
- **Program/Solicitation:** SBIR Project: "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- **Date:** August 20, 2019
- **Contract Number:** S649
- **BST Products/Systems Referenced:** SwiftPilot (autopilot), SwiftPilot simulation environment, Gazebo simulator
- **Key Personnel:** Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing autonomous flight control algorithms for Creare's Quad-Biplane VTOL aircraft intended for shipboard operations. Month 3 focused on implementing a unified state estimator for multi-phase flight, designing the controller architecture, establishing operator input modes, and refining aerodynamic modeling in the Gazebo simulation environment. The aircraft must achieve precision landings with 0.1 m accuracy on moving platforms.

## Technical Approach

### Unified State Estimator
- Implemented cascading estimator operating across different flight phases (previously required separate compilation for fixed-wing vs. multirotor)
- Four-level hierarchy:
  1. **Attitude/attitude rate:** 1 kHz computation using accelerometers and gyroscope
  2. **Yaw/heading:** Magnetometer-corrected during VTOL/hover; GPS heading in forward flight (critical for high-wind navigation accuracy)
  3. **Lateral position/velocity:** GPS + accelerometer fusion; airspeed measured via dynamic pressure sensor (VTOL operations use inertial velocities only); airspeed measurement triggers VTOL-to-fixed-wing transition
  4. **Vertical position/velocity:** GPS + static pressure fusion; laser altimeter augmentation during takeoff/landing for aggressive landing profiles in high winds

- Validated in BST simulation environment; now flies both VTOL and fixed-wing missions with same estimator code

### Controller Design
- Leverages existing multi-rotor and fixed-wing control configurations to simplify VTOL algorithm development
- Multiple upper-level loops already in place regulating higher-level functionality
- Architecture prepared; implementation planned for next month ahead of flight testing

### Operator Input & Flight Modes
Three operational modes available (after power-on self test confirms manual handset presence):
1. **Full operator control:** Direct control surface deflections for fixed-wing; roll/pitch/yaw/climb rate commands for multirotor; VTOL restricted to VTOL testing only
2. **Augmented control:** Operator specifies turn rate, climb rate, and airspeed (with automatic limits); multirotor uses body-relative velocities; VTOL with coordinated turn logic; automatic proximity detection and flare for landing
3. **Automatic control:** Waypoint-based autonomous flight with operator-specified transition parameters

### Flight Modes & Transitions
Nine defined modes with automatic/manual transitions:
1. **Initialize** – Autopilot boot with component verification
2. **Calibrate** – Preflight deflection/throttle commands for setup
3. **Preflight** – Checklist completion and flight detection
4. **Launch** – Motor enablement and climbout altitude/thrust setting
5. **Climbout** – Climb to desired altitude/location/heading; enters terminate if timeout exceeded
6. **Flying** – Active flight; triggers VTOL forward-flight transition; ends on landing command or system termination
7. **Landing** – Transition from cruise to landing corridor to vertical descent to flare (with laser altimeter feedback); abortable
8. **Landed** – Motors off; ready for new flight cycle
9. **Terminate** – Emergency descent: fixed-wing cuts engine and glides with user-commanded roll; multirotor descends rapidly; VTOL uses multirotor descent scheme or spiral descent if aerodynamic surfaces added

## Products & Capabilities Described

### SwiftPilot Autopilot
- **What it is:** BST's core flight control autopilot software
- **Use in this context:** Adapted for Quad-Biplane VTOL application with unified state estimator and new controller architecture
- **Capabilities demonstrated:** 
  - Cascading sensor fusion (1 kHz attitude, GPS/magnetometer heading, GPS/pressure altitude, laser altimeter landing augmentation)
  - Multi-mode operator interface
  - Automatic flight mode transitions
  - Precision landing with ground-based landing location detection integration
  - Fixed-wing, multirotor, and VTOL control in single codebase

### SwiftPilot Simulation Environment
- Used for validating unified estimator in simulated VTOL and fixed-wing flights
- Gazebo-based with piecewise linear aerodynamic coefficient modeling

### Ground Controller
- Planned integration with Quad-Biplane system
- Features: mission planning, monitoring, autonomous mission execution
- Integration support for Creare avionics and NOAA aerosol sensor instrument

## Use Cases & Applications

### Primary Application: Shipboard VTOL Operations
- **Mission profile:** Vertical takeoff → transition to horizontal flight → autonomous navigation → precision landing on moving ship deck
- **Landing accuracy target:** 0.1 m in no-wind conditions
- **Precision landing approach:** Creare's Landing Location Detection identifies shipboard landing target coordinates; SwiftPilot receives relative coordinates to fine-tune flight path
- **Platform simulation:** Testing includes landings on moving platform to simulate shipboard deck operations (leveraging Creare's prior experience)

### Instrument payload:** NOAA aerosol sensor instrument

## Key Results

### Month 3 Achievements
1. **Unified estimator implementation complete:** Transitioned from dual-codebase (separate fixed-wing and multirotor compilations) to single runtime-switchable estimator; maintains all existing algorithm and code from both prior estimators
2. **Aerodynamic modeling refined:** XFLR5 model from Creare processed into Gazebo piecewise linear format for simulation
   - Parameters captured per half-wing (see table below)
   - Coefficients averaged across expected Reynolds number range (variation noted as low for Double Eagle flight envelope)
   - 6-DOF dynamics computed using CAD-derived inertia matrix
3. **Controller architecture defined:** Upper-level loops in place; implementation planned
4. **Simulation validated:** Gazebo model refined to enable accurate preflight testing; BST's prior experience suggests minimal tuning required post-flight-test

### Aerodynamic Parameters (Double Eagle half-wing)
| Parameter | Value |
|-----------|-------|
| C<sub>L,α</sub> | 4.75 |
| C<sub>L,α,stall</sub> | -3.85 |
| α<sub>stall</sub> | 0.639 |
| C<sub>D,α</sub> | 0.642 |
| C<sub>D,α,stall</sub> | -0.923 |
| C<sub>M,α</sub> | -1.8 |
| C<sub>M,α,stall</sub> | 0 |

## Notable Details

### Project Scope & Deliverables
1. **Autopilot Algorithm Development** – Adaptation and customization of existing BST flight control for VTOL with outer-loop mission execution
2. **Precision Landing Algorithm** – Integration of Creare's Landing Location Detection with SwiftPilot guidance
3. **Ground Controller Implementation** – Mission planning, monitoring, execution
4. **Integration Support** – Avionics/radio selection; hardware provision
5. **Flight Testing Plan:**
   - Local Boulder, CO testing (14 CFR Part 107 compliance; altitude waivers sought)
   - Beyond Visual Line of Sight (BVLOS) testing at Griffiss UAS test site, Rome, NY
   - All flight modes including precision landings on moving platform
   - BST flight test; Creare to coordinate Griffiss clearance
6. **Program Management** – Technical progress tracking, expense management, joint project meetings

### Competitive Advantages & Technical Notes
- **Code reuse strategy:** Minimizes implementation effort by leveraging existing multi-rotor and fixed-wing control architectures
- **Sensor fusion sophistication:** Dynamic estimator switching (magnetometer vs. GPS heading; airspeed-triggered VTOL/fixed-wing transition) optimized for real-world conditions
- **Simulation fidelity:** Gazebo model validated against XFLR5 aerodynamic data; BST's prior aircraft successfully flew with simulation-derived parameters requiring minimal post-test tuning
- **Emergency landing redundancy:** VTOL termination mode uses rapid multirotor descent as primary with secondary spiral descent option if aerodynamic surfaces added
- **Wind resilience:** Laser altimeter-augmented descent enables aggressive landing profiles critical for high-wind shipboard operations

### Partnership & Coordination
- **Creare:** Aircraft design, Landing Location Detection software, landing target identification, aerodynamic modeling (XFLR5), shipboard operations guidance, Griffiss coordination
- **NOAA:** Aerosol sensor instrument payload
- **Griffiss UAS Test Site:** BVLOS testing venue and airspace coordination