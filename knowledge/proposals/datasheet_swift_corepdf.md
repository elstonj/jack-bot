# SwiftCore Flight Management System Datasheet

## Document Metadata
- Type: Product datasheet
- Client/Agency: General (sales/marketing material)
- Program/Solicitation: N/A
- Date: Created 2022-12-20 (modified 2020-10-25)
- BST Products/Systems Referenced: SwiftCore, SwiftPilot, SwiftTab, SwiftStation, S2 UAS
- Key Personnel: Jack Elston (last editor); Daniel Hesselius (University of Colorado, quoted)

## Executive Summary
SwiftCore is Black Swift Technologies' modular, end-to-end flight management system (FMS) for autonomous unmanned aircraft systems. The system enables operators to plan and execute autonomous flights with minimal training using an intuitive tablet-based interface, and has been deployed by NASA, NOAA, and major research institutions.

## Technical Approach
SwiftCore is designed as a fully integrated avionics solution composed of four integrated components:
1. **SwiftPilot autopilot** - core flight control system
2. **SwiftTab** - tablet-based mission planning and monitoring interface
3. **SwiftStation** - tripod-mounted ground control station
4. **Application-specific sensor integrations** - customizable for mission requirements

The system employs "smart" sensor-based autonomous control that modifies flight paths based on real-time sensor inputs to minimize operator workload and improve data quality. Flight planning is accomplished in minutes using gesture-based, intuitive controls on a handheld Android tablet.

## Products & Capabilities Described

### SwiftCore Flight Management System (FMS)
- End-to-end avionics solution for autonomous UAS control, communication, and command
- Modular, robust design optimized for nomadic scientific field campaigns in harsh environments
- Enables advanced, sensor-driven autonomous control systems

### SwiftPilot Autopilot
- **Size:** 6.7 cm × 4.0 cm × 1.8 cm
- **Weight:** 50 grams
- **Accuracy:** 9 DOF IMU with differential and static pressure sensing; 10 Hz GPS; 1 kHz altitude update rate
- **Processing:** Gumstix Overo payload (1 GHz Cortex-A8)
- **Interfaces:** CAN, UART, I2C, SPI, USB, Ethernet, GPIO

### SwiftTab User Interface
- **Platform:** Android-based tablet
- **Interface:** Gesture and multi-touch controls
- **Telemetry:** Real-time monitoring of all autopilot, mission, and aircraft parameters
- Enables confident deployment with minimal training

### SwiftStation Ground Station
- **Size:** 15 cm × 30 cm × 35 cm
- **Weight:** 0.9 kg
- **Features:** Tripod-mounted; dual 900 MHz and GPS antennas; incorporates SwiftPilot autopilot for fully autonomous launch-to-landing operations
- **Customization:** Multiple radio solutions and expandable via custom modules

## Use Cases & Applications
- Scientific field research missions (NASA-approved and NOAA-deployed)
- Academic research (CU, UTSI)
- Commercial operations
- Missions over topologically diverse terrain
- Harsh environment operations

## Notable Details
- **Industry Recognition:** Quoted endorsement from University of Colorado's Director of Flight Operations praising SwiftCore's superior fixed-wing autopilot capability
- **Customization:** Fully customizable integration into any UAS platform to meet mission-specific demands
- **Operational Philosophy:** "Modular by Design, Accurate by Nature™" tagline reflects product design principles
- **Proven Track Record:** Demonstrated cost-effectiveness and reliability in major scientific deployments
- **Accessibility:** Designed to enable rapid deployment and minimal operator training while maintaining data quality