# Autonomous Quad-Biplane Flight Controller - Month 8 Interim Report

## Document Metadata
- **Type:** Interim Progress Report
- **Client/Agency:** Creare (subcontractor on SBIR project for NOAA/shipboard operations)
- **Program/Solicitation:** SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- **Contract Number:** S649
- **Date:** 2020-01-20 (Month 8 report; document modified through 2020-03-23)
- **BST Products/Systems Referenced:** Autopilot (flight control algorithms), Ground Station/Flight Controller, Navigation algorithms
- **Key Personnel:** Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is providing design and engineering services to Creare for development of an autonomous Quad-Biplane flight controller capable of VTOL shipboard operations. Month 8 focused on integrating control algorithms, state machines, and user interface code, with prototype aircraft testing revealing issues in transition speed, navigation tracking, and airspeed measurement that are being addressed through controller refinements and coordinated turn implementation.

## Technical Approach

### Autopilot Algorithm Development
- Adapting BST's existing autopilot flight control algorithms for Quad-Biplane application
- Customizing attitude control algorithms (originally developed for multi-rotor stability) for four distinct flight modes:
  - Vertical hovering flight for takeoff
  - Transition to horizontal flight
  - Horizontal flight
  - Precision landing
- Implementing "outer loop" controller for mission trajectory and altitude objectives
- Using "zero-roll technique" to integrate VTOL code with existing navigation code
- Leveraging existing software to minimize implementation effort

### Precision Landing
- Landing accuracy target: **0.1 m in no-wind conditions**
- Creare developing Landing Location Detection software for visual shipboard target identification
- Autopilot receives relative coordinates to fine-tune flight path

### Ground Station
- Integration of Quad-Biplane algorithms into ground flight controller system
- Operator capabilities: plan, monitor, execute autonomous mission profiles

### Avionics Integration
- BST identifying suitable avionics and radios compatible with autopilot, Quad-Biplane, and NOAA aerosol sensor instrument
- Hardware provision for integration support

### Testing Plan
- Local flight testing in Boulder, CO (14 CFR Part 107 compliant)
- Requests for altitude waivers (above 400 feet, within line of sight)
- Beyond Visual Line of Sight (BVLOS) testing campaign at Griffiss UAS Test Site, Rome, NY
- Testing demonstrations: all flight modes including precision landings on moving platform simulating shipboard operations

## Products & Capabilities Described

### BST Autopilot
- **What it is:** Onboard flight control system with embedded code, state machine, navigation algorithms, and estimator implementation
- **Flight modes:** Hover, transition, forward flight, landing
- **Capabilities described:**
  - Stable attitude control for multi-rotor flight
  - Navigation tracking (adapted from fixed-wing and multirotor applications)
  - State machine management for mode transitions
  - Failsafe deployment system (rotor disable + parachute deployment)
  - Coordinated turn controller (under development)
- **Features:** Software-in-the-loop simulation validation, telemetry output to ground station, parameter customization for VTOL variant

### Ground Station/User Interface
- Waypoint planning and visualization
- Flight trajectory display
- Telemetry reception and display
- Parameter adjustment interface
- Integration with onboard autopilot via command/control links

## Use Cases & Applications
- **Primary mission:** Shipboard autonomous operations (NOAA aerosol sensor delivery to/from moving vessels)
- **Operational profile:** Vertical takeoff from ship deck → transition to forward flight for transit → return and precision landing on moving platform
- **Environment:** Marine operations with precision landing requirements
- **Regulatory context:** BVLOS operations coordination with FAA-approved test site

## Key Results (Month 8)

### Completed Work
- Full state machine implementation and integration
- Integration of VTOL code with navigation code (zero-roll technique)
- Complete simulation validation of integrated code
- Flight testing of prototype aircraft
- User interface integration with new autopilot code
- Prototype safety upgrades: parachute failsafe system, onboard camera (with power issues being addressed)

### Technical Issues Identified & Fixes Applied

1. **Fast Transition Problem**
   - **Issue:** Prototype aircraft transitioned from hover to forward flight in ~0.3s, reaching only 4 m/s airspeed (below wing stall speed), causing tip stall/wing-over
   - **Root cause:** Step input command from hover to forward flight
   - **Fix:** Implemented slower transition controller with 1-2 second smooth ramp instead of step input

2. **Navigation Tracking**
   - **Issue:** Slow tracking response around corners, "oversteering" behavior, inaccurate waypoint tracking on square flight plan
   - **Status:** Suspected coding issue; navigation algorithm itself verified for both fixed-wing and multirotor
   - **Next steps:** Implement coordinated turns to test effectiveness

3. **Airspeed Dips During Turns**
   - **Issue:** Indicated airspeed (IAS) dips observed when aircraft turns at waypoint corners
   - **Investigation:** Uncertain whether caused by pitot tube rotation with aircraft or zero-roll navigation technique
   - **Next steps:** Implement coordinated turn controller and compare results with zero-roll method

### Prototype Aircraft Status
- Capable of transitioning between flight modes
- Safety improvements implemented (parachute failsafe)
- Onboard recording camera added (power delivery being optimized)
- Multiple test flights completed; issues documented and targeted for resolution

## Next Month Deliverables
1. Video documentation (ground and onboard footage)
2. Navigation tracking fixes
3. Coordinated turn controller implementation and comparison with zero-roll method
4. Hover test of "Double Eagle" (second aircraft variant)
5. Autopilot integration completion on Double Eagle
6. Gain tuning optimization
7. Vertical takeoff and land testing with wings installed on Double Eagle

## Notable Details
- **Partner roles:** Creare provides Landing Location Detection software, BVLOS clearance coordination, shipboard operations expertise; BST provides autopilot/ground station development and flight testing
- **Safety features:** Automated parachute deployment in loss-of-control scenarios
- **Testing rigor:** Multiple iterations between simulation, local testing, and progressively more complex flight profiles
- **Technical leverage:** Adaptation of proven fixed-wing and multirotor algorithms to novel VTOL aircraft type
- **Regulatory coordination:** Working toward BVLOS waiver approval for advanced testing beyond standard Part 107 constraints