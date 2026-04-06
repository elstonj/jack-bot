# Autonomous Quad-Biplane Flight Controller - Month 5 Report

## Document Metadata
- Type: Interim Report (Month 5 of contract)
- Client/Agency: Creare (subcontractor); SBIR Project for unnamed sponsor
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: 2019-10-21
- BST Products/Systems Referenced: S2 (fixed-wing aircraft), E2/E3 (multi-rotor), SwiftCore autopilot, SwiftTab UI
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing an autonomous flight controller for Creare's Quad-Biplane aircraft capable of vertical takeoff/landing and horizontal flight for shipboard operations. During Month 5, BST completed avionics integration, designed power and GNSS boards, advanced autopilot firmware development, and evaluated simulation environments (migrating from Gazebo to JSBSim for improved fixed-wing accuracy).

## Technical Approach

### Autopilot Algorithm Development
- Adapting BST's existing autopilot flight control algorithms for Quad-Biplane application
- Customizing attitude control algorithms (proven on multi-rotors) for stable flight across multiple modes
- Developing "outer loop" controller for mission objectives (trajectory, altitude) that sets targets for inner loop stable flight algorithms
- Leveraging existing software to minimize implementation effort

### Precision Landing Algorithm
- Integration of Creare's Landing Location Detection software (visual target identification)
- Algorithm receives relative coordinates and adjusts flight path for precision landings
- Target accuracy: 0.1 m in no-wind conditions on moving ship decks

### Ground Controller Implementation
- Integration of Quad-Biplane algorithm into ground flight controller system
- Operator capabilities: mission planning, flight monitoring, autonomous mission execution

### Avionics Integration
- Battery/avionics stack designed to allow CG adjustment by repositioning batteries within fuselage
- Modular approach enables scaling from two to four battery levels
- Integrated with KDE motors (70A maximum per motor)

## Products & Capabilities Described

### SwiftCore Autopilot
- Core flight control system being adapted for VTOL operations
- Manages attitude control and state machine transitions
- Hardware-in-the-loop (HWIL) simulation capable
- Can operate fixed-wing and multi-rotor modes

### Power Board
- Measures battery voltage, current draw, and coulomb count
- Current design supports up to 6S battery packs
- Configuration: two 6S packs in series for vehicle power
- Current limitation: 165A per board; possible to exceed with four 70A motors
- Mitigation options: firmware to limit PWM command upper end, or change current sense resistor for wider range/lower accuracy

### GNSS Board
- Significant challenge due to vehicle orientation changes between vertical hover and horizontal flight
- Design options under consideration:
  1. Fixed orientation optimized for horizontal flight (simplest, risky for takeoff/landing)
  2. Moving platform to reorient with aircraft (complex, flight modification required)
  3. Helical antenna replacement for multi-orientation performance (hand installation, impedance matching required)
  4. Dual GNSS units with firmware switching (requires CAN bus bandwidth assessment)

### S2 and E2/E3 Airframes
- S2: fixed-wing aircraft used for simulation validation
- E2/E3: multi-rotor platform with real-world flight data for model comparison

## Use Cases & Applications

**Shipboard Operations**
- Vertical takeoff and landing on ship decks
- Precision landing accuracy target: 0.1 m
- Integration with NOAA aerosol sensor instrument
- Simulation of ship wake pattern operations (future capability)

**Flight Modes**
1. Vertical hovering (takeoff)
2. Transition to horizontal flight
3. Horizontal fixed-wing flight
4. Precision landing on moving platform

## Key Results (Month 5 Progress)

### Avionics Integration
- Received copter frame from Creare
- Battery/avionics stack assembled with modular design for CG adjustment
- Wings and motor wiring remain for next phase

### Simulation Development
- **Gazebo assessment**: Reliable for multi-rotor, but rudimentary fixed-wing plugins
- **JSBSim selection**: Open-source, modular, accurate, well-maintained, hardware-in-the-loop capable
- **Framework**: OpenEaagles (open-source C++ framework, used extensively for DIS-compliant distributed simulation)
- **Validation plan**: Construct models of S2 and E2 using real-world flight data for accuracy comparison

### Autopilot Firmware Progress
- Flight and autopilot state machine updates implemented
- Foundation laid for VTOL-specific control algorithm implementation
- Leverages existing code from fixed-wing and multi-rotor architectures

### Control Algorithm Validation (Gazebo)
- Hover-to-forward-flight transition tested (25 seconds total):
  - Altitude drop during transition: 5 m
  - Vertical descent rate: max 1.5 m/s, near zero within 10 seconds
  - Return to hover: smooth, 2.4 m rise
- Full state machine development (including forward flight navigation) ongoing

## Testing Plan

### Phase 1: Local Testing (Boulder, CO)
- Within 14 CFR Part 107 regulations
- Request waivers for operation above 400 feet (within visual line of sight)
- Demonstrate all flight modes including precision landings on moving platform

### Phase 2: Beyond Visual Line of Sight (BVLOS)
- Griffiss UAS Test Site, Rome, NY
- Creare managing clearance coordination
- Integration support: Creare to provide guidance on moving platform operations

## Notable Details

- **Hardware-in-the-loop simulation**: Critical capability for reducing development time and improving reliability
- **Modular design philosophy**: Autopilot firmware architecture designed to leverage proven multi-rotor attitude control with VTOL-specific outer loop controllers
- **Simulation accuracy prioritized**: Team changed from Gazebo to JSBSim despite unplanned effort, believing accuracy gains will save significant flight testing time
- **Future wind modeling**: JSBSim will eventually support ship wake pattern simulation for operational validation
- **Current motor specifications**: KDE motors, four motors per vehicle, 70A maximum per motor
- **Battery configuration**: Two 6S packs in series (12S nominal)