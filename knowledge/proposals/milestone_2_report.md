# Milestone 2 Report: Virtual Redundancy for Safety Assurance in the Presence of Sensor Failures

## Document Metadata
- Type: Progress report (Milestone 2)
- Client/Agency: U.S. Army (via Barron Associates subcontract)
- Program/Solicitation: SBIR Phase I subcontract with Barron Associates
- Date: September 10, 2016
- BST Products/Systems Referenced: SwiftCore Flight Management System (FMS), SwiftPilot autopilot, SwiftTab UI, Virtual Sensor System Interface
- Key Personnel: Jack Elston (last editor)

## Executive Summary
Black Swift Technologies completed Milestone 2 of a subcontract to develop virtual sensor redundancy capabilities for safety assurance. The report documents the development of a hardware-in-the-loop (HWIL) simulation environment integrating SwiftCore with Simulink, implementation of a virtual CAN bus interface for sensor injection, and setup of a realistic simulation platform using an UltraStick dynamics model for controller tuning and validation.

## Technical Approach

### SwiftCore FMS Development
- Updated existing SwiftCore Flight Management System with new code to interface with Simulink environment
- Developed firmware for attached Linux single board computer to support Barron Associates' virtual sensor system
- Wrote bootloader for autopilot allowing code uploads via SD card interface, enabling remote code updates after shipment to Barron

### Hardware-in-the-Loop (HWIL) Simulation Setup
- Abandoned initial software-in-the-loop (SIL) approach due to Windows environment restrictions and limited value
- Implemented cross-platform HWIL setup using serial connection between Simulink and autopilot
- Serial protocol chosen over TCP/UDP sockets to significantly reduce communications latency
- Modified HWIL Simulink model to communicate directly with hardware
- Implemented serial interface in Simulink
- Updated autopilot hardware to allow UART to function as a virtual CAN bus

### Virtual CAN Bus Interface
- Virtual CAN bus replicates mechanisms of actual CAN bus on SwiftCore-equipped aircraft
- Allows attachment of additional sensors for redundancy or improved accuracy
- Supports connection of up to 64 different actuators or motors
- Enables hardware adaptation to different vehicle types without redesign

### Virtual Sensor System Integration
- Concise messages containing virtual sensor data transmitted through virtual CAN bus at rates matching real sensors
- Autopilot ignores onboard sensor values upon detection of virtual sensor information
- Autopilot employs virtual sensors to determine state estimate and control values
- Control values sent back over virtual CAN bus to Simulink model
- Validation performed by setting constant sensor input values and observing actuator outputs
- Real-time Simulink execution ensures realistic HWIL simulation

## Products & Capabilities Described

### SwiftCore Flight Management System
- Full-featured FMS with onboard sensor suite for safe aircraft control
- CAN bus architecture for sensor and actuator integration
- Telemetry downlink capability
- SwiftTab UI for monitoring and control

### SwiftPilot Autopilot
- Contains all necessary onboard sensors for safe aircraft control
- Supports virtual CAN bus interface for sensor injection
- Bootloader capability for remote code updates
- Actuator command output over CAN bus
- Telemetry transmission

### SwiftTab UI
- Flight management interface
- Displays sensor values from autopilot telemetry
- Shows estimated state of autopilot
- Visualization tool for HWIL tuning

### Virtual Sensor System Interface
- Receives simulated sensor data via virtual CAN bus
- Interfaces sensor data to autopilot control algorithms
- Returns actuator commands for validation

## Use Cases & Applications

- Small unmanned aircraft systems (UAS) flight control and safety assurance
- Virtual sensor redundancy for fault tolerance
- Simulation-based controller tuning without flight testing
- Support for UltraStick model aircraft platform (both conventional and electric versions)

## Key Results

### Completed Work
- SwiftCore FMS updated and configured for HWIL simulation
- Virtual CAN bus successfully implemented as UART-based interface
- Serial interface developed in Simulink for autopilot communication
- Real-time Simulink execution established
- Virtual sensor system successfully tested with constant values
- Sensor data verified through SwiftTab telemetry display
- Actuator outputs confirmed in Simulink display
- State estimation validation achieved through telemetry and actuator output observation

### Planned Next Steps
- Integration of Barron-provided Virtual Sensor System with UltraStick dynamics model
- Execution of controller tuning using SwiftTab and X-Plane visualization
- Delivery of complete HWIL environment to Barron Associates for continued virtual sensor toolkit development

## Notable Details

- Pragmatic pivot from SIL to HWIL approach based on technical constraints and project value
- Serial protocol choice prioritized latency reduction over other communication options
- System designed for portability—can be shipped to partner and supported remotely
- Architecture supports flexible vehicle adaptation through modular sensor/actuator framework
- X-Plane visualization integration for enhanced simulation fidelity during tuning
- Use of industry-standard UltraStick dynamics model (University of Minnesota) for realistic simulation
- Clear integration pathway for Barron Associates' virtual sensor toolkit into realistic flight simulation environment