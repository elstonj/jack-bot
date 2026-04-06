# Mustang Integration Report

## Document Metadata
- Type: Integration report / Technical documentation
- Client/Agency: By Light (aircraft provider)
- Program/Solicitation: Not specified
- Date: October 7, 2025 (prepared); received aircraft October 1, 2025
- BST Products/Systems Referenced: S2 Avionics, CAN-based flight control system, ESC, autopilot, servo programming software
- Key Personnel: Ethan Domagala (last editor)

## Executive Summary
Black Swift Technologies received a By Light Mustang aircraft on October 1, 2025 for avionics integration. After identifying issues with the existing avionics and hardware, BST replaced internal systems (except servo motors) with their own S2 avionics package, including redesigned control boards, autopilot, communications systems, and associated wiring/calibration.

## Technical Approach

**Avionics Removal & Analysis:**
- Full removal of By Light avionics with comprehensive wiring documentation
- Systematic removal of power distribution, autopilot, communications, and ESC central tray

**S2 Avionics Installation:**
- BST S2 avionics use **CAN (Controller Area Network) protocol** for surface actuation and sensor reporting
- Two stacks of control boards mounted on modified avionics tray:
  - **Forward stack**: aileron/wing control surfaces (two boards)
  - **Aft stack**: ruddervator/tail surfaces (two boards)
- Each control surface has a dedicated actuator board plus one additional board for radio inputs

**Servo Calibration:**
- In-house servo programming procedures applied post-installation
- Surface deflection endpoints calibrated:
  - Ruddervators: ±20 degrees
  - Ailerons: +20 degrees / -15 degrees (asymmetric)

**Hardware Modifications:**
- Aircraft motor and ESC replaced with BST's standard 6s aircraft motor (original deemed inefficient)
- GPS antenna mounted on top of fuselage for optimal reception
- Pitot tube replaced with nose-mounted setup for improved airspeed accuracy in any aircraft orientation

**Car Launch Integration:**
- By Light's car launch mechanism refurbished and mounted to SUV rooftop rack
- Secured with four additional U-bolts
- Test conducted at 40 mph and 65 mph with aircraft powered on (no release)
- Aircraft visually generated lift at approximately 60 mph and pulled vertically on launch mechanism

## Products & Capabilities Described

**S2 Avionics System:**
- CAN-based flight control architecture
- Modular actuator board design with dedicated boards per control surface
- Integrated autopilot and radio communication handling
- Supports multiple servo motor control with programmable endpoint calibration
- Compatible with external sensor inputs (GPS, pitot airspeed, radio)

**ESC & Motor Configuration:**
- 6S LiPo compatible motor and ESC
- Swappable/configurable for different aircraft platforms

## Use Cases & Applications
- Catapult-launched aircraft operations using car-launch mechanism
- Extended-range surveillance/monitoring (implied by launch system and GPS/airspeed emphasis)

## Key Results
- Successful avionics integration into By Light Mustang airframe
- System validated during dynamic testing at highway speeds (40-65 mph)
- Aircraft demonstrated aerodynamic lift generation at ~60 mph on launch mechanism
- GPS and airspeed telemetry functional during test runs
- Launch mechanism verified ready for flight operations

## Notable Details
- BST chose full internal hardware replacement (except servos) for rapid diagnostics and team familiarity rather than retrofitting By Light systems
- Decision-driven by project timeline constraints
- Demonstrates BST's capability to rapidly integrate existing airframes with their avionics
- Original By Light hardware had identified deficiencies (inefficient motor/ESC, poor pitot design, rusty launch hardware)
- CAN protocol choice enables efficient multi-board communication and scalability
- Asymmetric aileron calibration suggests specific control authority requirements
- Aircraft is composite (fiberglass) construction