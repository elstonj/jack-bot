# Autonomous Quad-Biplane Flight Controller - Month 4 Report

## Document Metadata
- Type: Interim technical report
- Client/Agency: Creare (subcontractor); SBIR Project for unspecified government agency
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Date: 2019-09-20
- Contract Number: S649
- BST Products/Systems Referenced: SwiftCore autopilot system
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing an autonomous flight controller for Creare's Quad-Biplane VTOL aircraft designed for shipboard operations. This Month 4 report details the cascaded control architecture for managing vertical takeoff, transition to forward flight, and precision landing phases, with implementation focused on quaternion-based attitude control leveraging BST's existing SwiftCore autopilot algorithms.

## Technical Approach

### Overall Control Architecture
- **Cascaded design structure**: Navigation control → lateral/longitudinal control loops → attitude/thrust controller → core controller → individual rotor commands
- **Navigation control** selects desired 3D position, converted to accelerations in x, y, z
- **Attitude/thrust controller** converts to desired quaternion attitude (qd) and thrust (dt)
- **Core controller** computes individual rotor commands from quaternion commands and thrust

### Flight Phases Controlled

**Takeoff (3 phases):**
1. **Vertical Climb** (to safe height, typically 5m)
   - Navigation commands position (px, py) and safe height (pz)
   - Aircraft climbs vertically, maintains takeoff yaw orientation
   - Faces into wind for even wing force

2. **Climbout Phase** (to climbout altitude, typically 20m)
   - Rapid climb at user-specified angle, pitched into wind
   - Roll command set to zero; pitch holds climbout path angle
   - Yaw oriented into wind
   - Longitudinal controller commands vertical rate (vz,c) of 3-5 m/s
   - User can set climbout angle from shallow (60°) to vertical (90°) for obstacle clearance

3. **Transition to Forward Flight**
   - Aircraft held at climbout altitude until indicated airspeed exceeds vmin (1.2 × vstall)
   - Navigation controller switches to waypoint navigation
   - Expected duration: 2-5 seconds

**Landing (3 phases):**
1. **Transition to Landing Approach**
   - Fixed-wing navigation descends aircraft to landing height
   - Slows to vmin at landing point
   - Onboard wind estimator ensures flight direction is into wind

2. **Final Approach**
   - Longitudinal controller commands vertical velocity (vz,descent)
   - Navigation tracks approach angle
   - Roll command zero; yaw keeps aircraft pointed into wind

3. **Terminal Descent**
   - Straight-down descent until ground impact
   - Aircraft holds yaw angle, uses roll/pitch to hold position
   - Safe height threshold same as takeoff safe height

### Core Controller Implementation

**Quaternion-based control strategy:**
- Unified controller for all three flight phases (vertical, transition, forward)
- Three-step cascade system:

1. **Attitude error to body rate conversion** (proportional gain control on each axis using quaternion error)
   - Computes error between desired quaternion (qd) and actual quaternion (q)
   - Uses conjugate of qd in calculation

2. **Body rate to torque commands** (PID control for each axis)
   - Generates desired torque commands (Tx, Ty, Tz) for each body axis

3. **Torque and thrust to rotor commands**
   - Uses control matrix M to map torque/thrust commands to individual motor commands
   - Matrix derivation based on rotor geometry and thrust curves

**Key advantages of quaternion approach:**
- Eliminates singularities at 90-degree pitch angles (critical for forward flight)
- Single attitude/thrust controller for all flight phases
- No transitions or controller handoffs required

### Control Matrix Calculation
For the Creare Double Eagle with 4 rotors and 7-degree rotor angle:
- First step: Compute inverse of M (nx4 matrix where n = rotor count)
- Each column based on rotor location (x,y,z)i, thrust coefficient (Ct), and rotor thrust direction vector [tx, ty, tz]T
- Individual rotor commands (ui) computed using pseudo-inverse of V
- Validation conducted using motor/prop thrust curve provided by Creare

## Products & Capabilities Described

### SwiftCore Autopilot System
- **What it is**: BST's modular autopilot system with existing multirotor and fixed-wing control algorithms
- **Application in Quad-Biplane**: Higher-level control loops (lateral, longitudinal, navigation) adapted from SwiftCore's existing controllers; core controller unified to handle all flight phases
- **Reuse strategy**: Leveraging existing software to minimize implementation effort while adapting for VTOL/hybrid flight modes

## Use Cases & Applications

**Primary Use Case: Shipboard VTOL Operations**
- Vertical takeoff and landing from moving ship decks
- Precision landing accuracy target: 0.1 m in no-wind conditions
- Wind-aware flight control (wind estimation for stable landing in high-wind conditions)
- Autonomous mission execution with waypoint navigation
- Potential integration with NOAA aerosol sensor instrument

**Flight Testing Plans:**
- Local testing in Boulder, CO (within 14 CFR Part 107 regulations, with altitude waivers)
- Beyond Visual Line of Sight (BVLOS) testing at Griffiss UAS test site, Rome, NY
- Precision landing tests on moving platform to simulate shipboard operations

## Notable Details

### Partnership & Integration
- **Creare's responsibilities**: Landing Location Detection software (visual target identification for precision landing), Quad-Biplane airframe design, experience with drone operations from moving platforms
- **BST's responsibilities**: Autopilot algorithm development and customization, precision landing algorithm integration, ground controller implementation, avionics/radio integration support, flight testing
- **Third-party integration**: NOAA aerosol sensor instrument; Griffiss UAS test site for BVLOS operations

### Technical Specifications
- Safe height (vertical climb and terminal descent): Typically 5m, user-adjustable
- Climbout altitude: Typically 20m, user-adjustable
- Climbout vertical rate: 3-5 m/s (user-set)
- Landing approach: Into-wind orientation mandatory for safety
- Minimum airspeed threshold (vmin): 1.2 × stall velocity
- Quad-rotor platform with 7-degree rotor tilt angle

### Operational Flexibility
- Tablet UI for user control and parameter selection
- Adjustable climbout angles and altitudes for obstacle avoidance
- Wind-adaptive flight control throughout all phases
- Waypoint-based navigation for forward flight phase

### Current Project Status
- Month 4: Control architecture design and simulation validation in progress
- Control matrix validated for vertical flight phase
- Remaining work: Simulate climbout and transition phases; prepare for avionics integration into actual aircraft