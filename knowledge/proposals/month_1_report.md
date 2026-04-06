# Autonomous Quad-Biplane Flight Controller - Month 1 Report

## Document Metadata
- Type: Interim project report
- Client/Agency: Creare (partnership/subcontract)
- Program/Solicitation: Contract Number S649
- Date: 2019-06-20
- BST Products/Systems Referenced: SwiftCore avionics, custom autopilot system
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies completed initial avionics integration work for Creare's autonomous quad-biplane VTOL project. BST designed a modular SwiftCore-based avionics architecture using CAN bus connectivity and developed custom protective housings for the avionics and GNSS/magnetometer systems.

## Technical Approach
- **Architecture**: Modular SwiftCore avionics system based on CAN bus architecture
- **Sensor/Actuator Integration**: CAN lines distributed to each rotor with boards for attaching ESCs, pitot tube, and potential servo connections
- **Communication**: P900 radio from Microhard (900MHz, 1W) for primary link; Futaba 14SG RC transmitter with sBus receiver for backup manual flight control
- **Power Management**: Power connectors sized for up to 70A output; battery system still in selection phase
- **Environmental Protection**: Custom 3D-printed case base with carbon fiber lid to seal avionics from water and dust
- **Payload Interface**: Serial interface provided from autopilot to payload
- **Design Philosophy**: Modular layout designed for easy addition of future aerodynamic control surfaces

## Products & Capabilities Described

### SwiftCore Avionics
- Modular autopilot avionics system
- Integrates via CAN bus architecture
- Provides GNSS/magnetometer functionality
- Includes serial payload interface capability
- Designed for scalable sensor/actuator integration

### Custom Avionics Enclosure
- 3D-printed base with carbon fiber lid
- Provides water/dust sealing
- Protects avionics in aircraft environment where aeroshell provides insufficient protection

### GNSS/Magnetometer Board
- Separate CAN bus-connected module
- Custom protective case designed
- Plugs into main avionics architecture

## Use Cases & Applications
- Autonomous VTOL (quad-biplane) flight operations
- Extended autonomous operations in potentially wet/dusty environments
- Payload delivery/support (serial interface for payload control)

## Notable Details
- **Design Modularity**: SwiftCore's modular approach enabled clean integration into Creare's airframe without extensive custom development
- **CAN Bus Architecture**: Selected to simplify wiring over long airframe distances and eliminate analog signal runs
- **Incremental Development**: Design allows future addition of aerodynamic control surfaces without major rework
- **Integration Partners**: Collaboration with Creare on layout and conceptual design
- **Standard Components**: Leveraged commercial-off-the-shelf (COTS) radio (Microhard P900) and RC control (Futaba 14SG)
- **Power Considerations**: 70A capability indicates support for quad-rotor ESCs and significant payload/sensor draw

## Status
Month 1 complete; avionics layout finalized and custom case designs created. Battery system selection outstanding.