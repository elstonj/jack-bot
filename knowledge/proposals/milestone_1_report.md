# Milestone 1 Report – Virtual Redundancy for Safety Assurance in the Presence of Sensor Failures

## Document Metadata
- Type: Milestone report
- Client/Agency: U.S. Army (via Barron Associates Inc., prime contractor)
- Program/Solicitation: SBIR Phase I subcontract (BST as subcontractor to Barron Associates)
- Date: June 7, 2016
- BST Products/Systems Referenced: SwiftCore Flight Management System (FMS), SwiftPilot autopilot, Gumstix Overo, SwiftStation ground control station, SwiftTab user interface
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This milestone report documents completion of the test environment setup for a virtual sensor redundancy system designed to maintain safe aircraft operations when physical sensors fail. Black Swift Technologies assembled and configured a SwiftCore-based hardware-in-the-loop (HWIL) simulation platform and developed MATLAB/Simulink interfaces to support testing of the virtual sensor system before hardware delivery to Barron Associates.

## Technical Approach
BST implemented a dual-track simulation capability:

1. **Hardware-in-the-Loop (HWIL) Setup**: Complete SwiftCore system assembled with SwiftPilot autopilot, Gumstix Overo processor, USB simulator interface, SwiftStation ground control station, and SwiftTab tablet interface. Included custom power monitoring board measuring input voltage and system current draw with regulated voltage output.

2. **Software-in-the-Loop (SWIL) Capability**: MATLAB/Simulink module enabling pre-flight testing without physical hardware. Communications via TCP socket to simulated autopilot. Sensor data injected as simulated CAN bus packets; actuator commands received over same virtual CAN bus.

3. **Dual Interface Support**: Simulink wrapper allows operation in either Simulink environment or via MATLAB scripts. Windows-based system support in development.

## Products & Capabilities Described

### SwiftCore Flight Management System
- Complete UAS flight management platform
- Core components: SwiftPilot autopilot, Gumstix Overo onboard processor, CAN bus architecture
- Capable of HWIL and SWIL testing modes

### SwiftPilot Autopilot
- Flight control processor
- Integrates with CAN sensor bus
- Accepts simulated sensor inputs during testing
- Outputs actuator commands

### SwiftStation Ground Control Station
- Ground-based mission planning and monitoring interface
- Part of standard SwiftCore configuration

### SwiftTab User Interface
- Tablet-based interface for SwiftCore system
- Component of integrated cockpit/control solution

## Use Cases & Applications
- Unmanned aircraft system (UAS) operation with sensor fault tolerance
- Safety-critical applications requiring virtual sensor redundancy
- Testing and validation of sensor failure mitigation strategies

## Notable Details
- Custom power monitoring board designed by BST for HWIL testing
- MATLAB/Simulink integration enables vendor-agnostic simulation before hardware deployment
- Barron Associates would receive completed HWIL setup after SWIL validation
- Firmware stability verified through SWIL before hardware shipment to minimize integration issues
- Optional X-Plane integration noted for visualization capabilities
- CAN bus architecture enables sensor virtualization approach