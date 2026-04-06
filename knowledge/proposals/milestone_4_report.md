# Milestone 4 Report: Virtual Redundancy for Safety Assurance in the Presence of Sensor Failures

## Document Metadata
- Type: Milestone Report
- Client/Agency: U.S. Army (via Barron Associates)
- Program/Solicitation: 2016 Army Phase I Subcontract
- Date: December 5, 2016
- BST Products/Systems Referenced: SwiftCore Flight Management System (FMS), SwiftPilot, SwiftTab, SwiftStation, SwiftTrainer
- Key Personnel: Not named in document

## Executive Summary
This milestone report documents the completion of a System-in-the-Loop (SIL) simulation system for the SwiftCore Flight Management System using MATLAB Simulink. The work involved modifying the UMN simulator to enable full mission simulation from launch to landing, adjusting autopilot software run rates, and establishing both hardware-in-the-loop (HWIL) and software-in-the-loop (SWIL) simulation capabilities for safety assurance testing.

## Technical Approach
- Developed a MATLAB Simulink-based blockset providing both HWIL and SWIL simulation capabilities
- Modified the UMN simulator (provided by Barron) to simulate complete flights from launch to landing rather than mid-flight starts
- Adjusted SwiftPilot autopilot software filter and estimator run rates to match real-time Simulink environment requirements
- Modeled hand-launch forces directly from recorded SwiftTrainer hand-launch data to accurately simulate launch dynamics
- Implemented ground-contact detection and initialization logic to allow realistic on-ground startup and shutdown sequences
- Tuned SwiftPilot control loops for Ultrastick aircraft simulation, modifying inner loops for indicated airspeed (IAS), roll, and pitch tracking

## Products & Capabilities Described

### SwiftCore Flight Management System (FMS)
- Core autopilot system being validated through SIL simulation
- Contains filters, estimators, and control loops for aircraft guidance and control

### SwiftPilot
- Hardware autopilot module with approximately 2-second initialization time on power-on
- Includes state estimation algorithms and flight control loops
- Can operate in both HWIL and SWIL configurations
- Supports HDOP-based preflight checklist monitoring and engine enable procedures

### SwiftTab
- Operator interface tablet application
- Connects via WiFi to SwiftStation for Ground Control Station (GCS) communications
- Provides "Ready for Launch" and "Enable Engine" controls
- Used in both HWIL and SWIL simulation workflows

### SwiftStation
- Ground station hardware providing WiFi connectivity and system coordination
- Bridges communication between SwiftTab and simulation systems

### SwiftTrainer
- Reference aircraft used for hand-launch force modeling and controller performance benchmarking
- Aerodynamically similar to Ultrastick aircraft tested in simulation

## Use Cases & Applications
- Safety assurance testing for sensor failures through virtual redundancy
- Flight management system validation via hardware and software-in-the-loop simulation
- Control loop tuning and optimization for different aircraft types
- Full mission profile testing from ground initialization through landing
- Operator training and interface validation

## Key Results
1. **Full Mission Simulation Capability**: Successfully enabled simulation of complete flights including ground initialization, hand-launch, flight, and landing phases
2. **Improved Workflow**: Ground-based startup with operator connection via SwiftTab significantly improved simulation repeatability and usability
3. **Simulator Comparison**: OpenFlight version (UMN's online version) demonstrated superior performance compared to the base Barron-provided simulator for the same aircraft and simulation rates—fundamental differences in dynamics performance remain unclear
4. **Controller Tuning Achievement**: Successfully tuned SwiftPilot control loops for Ultrastick aircraft by modifying IAS, roll, and pitch inner loops to match SwiftTrainer-equivalent performance
5. **Issue Identification**: Simulation performance limitations in flight plan tracking identified as potentially related to yaw dynamics deficiencies (missing or offset rudder control)

## Technical Modifications Completed
- **Removed in-flight start condition**: Changed from nominal mid-flight trimmed condition to ground-based static startup
- **Hand-launch block**: Added Launcher block simulating hand-launch forces derived from actual SwiftTrainer launch recordings
- **Ground contact logic**: Implemented state machine allowing ground operations and automatic simulation stop on landing
- **Navigation fixes**: Corrected ground track heading calculation in Navigation_lib.mdl
- **Altitude calculation**: Fixed minus-sign error in ground height calculation and resolved EGM-96 Geoid Model conflicts
- **Sensor additions**: Added temperature and ground track to sensor simulation block

## Notable Details
- Two UMN simulation environments tested: Barron-provided version and OpenFlight (latest online UMN version)
- Complete procedural documentation for both HWIL and SWIL workflows included (16-step procedures for initial runs, 7-step procedures for re-runs)
- Integration across multiple hardware systems (SwiftPilot, SwiftTab, SwiftStation) demonstrated and documented
- Simulation workflow allows hand-launch simulation and realistic vehicle initialization sequence matching field operations
- Project demonstrates BST's capability to integrate third-party simulators (UMN UAV simulation) with proprietary flight management systems