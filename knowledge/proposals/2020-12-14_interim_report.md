# A Novel Aerial Drone Platform for Exploration of Titan - 2019 Phase II Interim Report

## Document Metadata
- Type: Interim Report
- Client/Agency: NASA
- Program/Solicitation: 2019 Phase II SBIR; Contract Number 80NSSC19C0332
- Date: December 14, 2020
- BST Products/Systems Referenced: SwiftPilot autopilot, JSBSim simulation environment, flight simulation models
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This interim report documents BST's progress on developing a flight simulation environment and flight control systems for Creare's Titan Ringlet drone platform. BST has integrated Titan atmospheric models into their simulation tools, developed aerodynamic models of the ringlet aircraft, integrated avionics into a terrestrial prototype (MiniSwarm), and conducted initial flight testing demonstrating stable hover and forward flight control.

## Technical Approach

### Flight Simulation
- Extended BST's existing planetary flight simulation environment to model both Earth and Titan atmospheres
- Integrated Titan-GRAM atmospheric model into JSBSim simulation interface
- Titan-GRAM integration passes altitude, coordinate, and time data to generate atmospheric properties (pressure, temperature, density) that override JSBSim's default ISA1976 model
- Approach functional but limited: Titan-GRAM outputs variably-spaced data requiring CSV conversion; JSBSim has questionable support for non-Earth atmospheric models

### Aircraft Aerodynamic Modeling
- Developed Python scripts utilizing AVL (Athena Vortex Lattice) to generate full aerodynamic models from geometry definitions
- Workflow generates JSBSim-compatible models incorporating wind/atmospheric models and autopilot inputs
- Previously validated on Earth and Venus; extended to Titan atmospheric and gravity conditions
- Models the annular (ring-wing) aircraft geometry provided by Creare

### Flight Control Development
- Designed and developed controller and control gains for takeoff, landing, and mission execution
- Customized existing attitude control algorithms for high-stability multi-rotor and tail-sitter aircraft control
- Targeted flight modes: vertical hovering (takeoff), transition to horizontal flight, sustained horizontal flight, precision landing
- Used simulation to develop and tune controls for both Titan vehicle and terrestrial prototype

### Hardware-in-the-Loop (HIL) Simulation
- Utilized HIL capabilities to validate flight algorithms using actual hardware before flight testing
- Bridge between simulation and physical flights to reduce risk

## Products & Capabilities Described

### SwiftPilot Autopilot
- Core avionics component integrated into terrestrial prototype
- Includes integrated attitude control and flight mode management
- Supports multiple flight modes and autonomous mission execution

### Terrestrial Prototype Integration
- Platform: MiniSwarm (ring-wing aircraft variant)
- Integrated components: SwiftPilot, actuators, RC receiver, power supply board, laser altimeter, GNSS receiver
- Avionics system mass: 1.4 kg
- Propulsion system: Modified from original design to 9x6 propellers with 960kV motors
- Battery: 4850mAh 4S LiPo
- Thrust-to-weight ratio: 3:1 (intentionally overpowered for margin)
- ESC replacement: Upgraded from original DYS 4-in-1 ESC to allow better parameter control and consistent motor RPM

### BST Simulation Environment
- Planetary flight simulation capability
- Support for multiple atmospheric models
- Real-time and faster-than-realtime execution modes
- Integration with JSBSim open-source flight dynamics model

## Use Cases & Applications

**Primary Application: Titan Atmospheric Exploration**
- Aerial drone platform designed for operation in Titan's dense nitrogen atmosphere (1.5x Earth sea-level pressure, much colder temperatures)
- Ring-wing (annular wing) design optimized for Titan's atmospheric conditions
- Proposed missions: autonomous flight with multiple flight modes, orbit demonstrations, data collection from aerial platform

**Terrestrial Validation**
- Boulder, CO flight testing to validate control algorithms and flight dynamics models
- Analog demonstrations of autonomous mission sequences intended for Titan operations

## Key Results

### Simulation Development (Completed)
- Titan-GRAM successfully integrated into JSBSim interface
- JSB aerodynamic model of Titan vehicle developed
- Functional atmospheric property override system established

### Avionics Integration (Completed)
- SwiftPilot and supporting systems successfully integrated into MiniSwarm prototype
- System mass optimized and balanced
- Propulsion system upgraded for adequate thrust margin

### Flight Testing Results (MiniSwarm Prototype)
- **Gross Takeoff Weight**: 1.42 kg
- **Flight sorties completed**: 4 flights
- **Hover power consumption**: 192 W (13.2 A)
- **Maximum forward flight speed**: 13 m/s
- **Stability**: Strong pitch/roll control in both hover and forward flight
- **Control performance**: Pitch angle maintained at 60° throughout forward flight test; responsive control response; good heading control

### Specific Findings
- Initial battery placement (top-mounted) caused structural bending oscillations; moving battery to central, rigid location significantly reduced vibrations and improved attitude control tracking
- Aircraft demonstrated excellent stability in transition between hover and forward flight modes
- Pitot tube airspeed measurement (13 m/s) correlated well with GPS ground speed
- Forward flight test conducted without flap control, demonstrating rotor-only attitude control sufficiency
- Pilot notes indicated aircraft responsiveness and good control characteristics

## Notable Details

### Project Schedule Status (as of Dec 2020)
- ✓ Complete simulation environment models (target: month 5)
- ✓ Complete drone flight dynamics models (target: month 11)
- ✓ Complete integration of avionics with terrestrial prototype (target: month 13)
- In progress: Flight permission (target: month 13)
- Planned: Terrestrial flight testing (target: month 16)

### Technical Innovations
- Custom Python/AVL workflow for rapid aerodynamic model generation from geometry
- Novel atmospheric model integration approach for non-Earth planetary simulations
- Ring-wing (annular) aircraft design adapted for extreme atmospheric environments

### Collaborative Partners
- Creare Inc.: Provided ringlet drone design, terrestrial prototype airframe, motors, and speed controllers

### Risk Mitigation
- Overpowered propulsion system (3:1 T/W ratio) provides structural and component upgrade margin
- Hardware-in-the-Loop testing planned before final flight validation
- Formal NASA Airworthiness and Flight Safety Review Board and Flight Readiness Review Board approval process underway

### Technical Challenges Addressed
- Titan-GRAM not originally designed for dynamic single-point execution; BST developed text parsing solution
- JSBSim limited support for non-Earth atmospheres; BST implemented property override approach
- Original propulsion system insufficient for loaded prototype; system upgraded with performance margin
- ESC reliability issues; replaced with unit allowing better parameter control
- Structural vibration from battery placement; solved through repositioning and rigid mounting