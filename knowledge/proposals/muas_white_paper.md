# Intelli-Copter Micro-Unmanned Aerial System White Paper

## Document Metadata
- Type: White Paper
- Client/Agency: Not explicitly stated (appears to be for a customer with cave/indoor mapping requirements)
- Program/Solicitation: Not specified
- Date: 15 June 2013
- BST Products/Systems Referenced: MUAS (Micro-Unmanned Aerial System), mesh communication system, communication-aware planning
- Key Personnel: Not named in document
- Partners: Chiaro Technologies (structured light technology provider)

## Executive Summary
Black Swift Technologies proposes developing an integrated Micro-Unmanned Aerial System (MUAS) capable of autonomous indoor and cave environment navigation and mapping. The system combines a custom vertical-flight micro helicopter with advanced 3D imaging sensors, GPS-denied autopilot, mesh networking, and tablet-based controls to enable minimally-trained operators to conduct rapid imaging and 3D mapping in constrained environments where no fieldable UAS currently exists.

## Technical Approach

### System Architecture Overview
The integrated MUAS consists of six primary subsystems:

1. **Vehicle**: Custom-designed micro helicopter with 30+ minute flight time
2. **Autopilot**: Augmented or fully autonomous operation in GPS-denied environments
3. **EO/IR Cameras**: Remote video display with real-time transmission
4. **3D Imaging Payload**: Structured light technology for navigation and mapping
5. **Communication System**: Ad-hoc wireless mesh network with multi-hop capability
6. **Operator Control Unit**: Tablet-based with touch/gesture controls

### System Mass & Power Budget
- **Total System Weight**: 1,010 grams
  - Vehicle: 700g (69%)
  - EO/IR Cameras: 150g (15%)
  - Structured Light: 100g (10%)
  - Autopilot: 35g (3%)
  - Comm Radio: 25g (2%)

- **Total System Power**: 184.5W
  - Vehicle (propulsion): 175W (95%)
  - EO/IR Cameras: 3W (2%)
  - Structured Light: 4W (2%)
  - Autopilot: 1W (1%)
  - Comm Radio: 1.5W (1%)

- **Total Volume**: 230 cm³

## Products & Capabilities Described

### Black Swift MUAS System
- **What it is**: Custom-integrated micro helicopter system for autonomous/augmented flight with multi-sensor payload
- **Proposed use**: Indoor and cave environment mapping and imaging in GPS-denied conditions
- **Key specifications**:
  - Minimum 30-minute flight time
  - Man-portable and ruggedized
  - Fully autonomous or augmented manual control
  - Multi-vehicle capable from single operator control unit

### Communication System (BST Unique Capability)
- **What it is**: Ad-hoc networked RF communication system with multi-hop mesh network architecture
- **Proposed use**: Vehicle control, cooperative operations, range extension through relay chains
- **Unique feature - Communication-Aware Planning**:
  - Automatically configures assets as relays for optimal communication chains
  - Requires no operator intervention for relay deployment/repositioning
  - Automatically detects available MUAS assets and tasks them as relays
  - Continuously updates relay positioning based on environment
  - Allows operator focus to remain on lead vehicle in cave/indoor operations

### Navigation System (SLAM-based)
- **What it is**: Simultaneous Localization and Mapping based on EO/IR feature detection and 3D structured light point clouds
- **Proposed use**: Flight and navigation in GPS-denied indoor/cave environments
- **Components**:
  - Sonic range finders (zenith and nadir orientation) for vertical position detection and passageway identification
  - Nadir sonar for autonomous landing detection
  - EO/IR live video feed transmitted in real-time to users

### Structured Light 3D Imaging Payload
- **What it is**: Integration of Chiaro Technologies' 3Dx10 structured light system, miniaturized for MUAS
- **Chiaro 3Dx10 specifications**:
  - Point cloud generator for precise 3D capture and measurement
  - Class 1, eye-safe light source with specialized optics projecting invisible light
  - IR-CMOS image sensor with pixel-by-pixel analysis
  - Parallel processing suitable for FPGA or GPU implementation
  - Configurable projector and camera modules
- **Proposed use**: Provide 360-degree point cloud of operational environment; enable centimeter-level accuracy mapping
- **Advantages**: Overcome bright-light performance degradation; enable operation in black-out conditions

### EO/IR Camera System
- **What it is**: Electro-optical and infrared imaging system
- **Proposed use**: Remote operator video display; navigation via feature detection and object tracking; collision avoidance
- **Specifications**:
  - COTS board-level cameras
  - H.264 hardware video compression
  - High-quality video feed over mesh network
  - Omni-directional viewing capability for situational awareness
  - Operator ability to select video view windows from panorama for higher resolution

### Ground Element - Operator Control Unit
- **What it is**: Tablet-based device with intuitive interface
- **Proposed features**:
  - Touch and gesture-based controls
  - 3D map navigation
  - Real-time and forensic video display/playback
  - Multi-vehicle control capability

## Use Cases & Applications

### Primary Mission
- **Indoor and cave environment mapping and imaging** in GPS-denied conditions
- Minimally-trained operator requirements
- Rapid navigation and 3D mapping of highly constrained environments
- Interior building mapping
- Cave exploration and documentation

### Operational Scenarios
- **Multi-vehicle cooperative operations**: Single operator controlling multiple MUAS assets
- **Communication-limited environments**: Automatic relay network configuration (particularly for cave operations with severe range limitations)
- **Black-out/darkness conditions**: IR imaging and structured light operation without visible light
- **Bright light conditions**: Structured light system designed to overcome bright-light performance degradation

## Program Development Plan

### Vehicle Development
- Flight performance optimization
- Power source selection/optimization

### Airborne Sensors Development
- **Structured Light**: Leverage Chiaro Technologies' expertise for miniaturized MUAS-compatible solution
- **Camera**: COTS board-level EO/IR cameras with H.264 hardware compression
- **Navigation**: Integrate and improve SLAM algorithms using 3D point cloud, EO/IR image features, and inertial measurements
- **Processing**: 
  - FPGA solution for sensor front-end, video encoding, and point cloud generation (Chiaro partnership)
  - Single-board computer for flight control, mission functionality, cooperative mapping, and flight path planning
- **Communication**: COTS radio solutions for mesh protocol testing and operational environment propagation analysis

### Ground Element Development
- **Communication**: Antenna and amplifier solution designed for mesh radio; optimize for deployment ease, size, and weight
- **Processing**: 3D map generation algorithms; efficient mapping path planning; real-time/forensic display and playback on tablet
- **Display**: Intuitive gesture and multi-touch interface for 3D map navigation, vehicle control, and video management

### Integration and Testing
- Program plan included with IMP/IMS and milestones (document references but does not detail)

## Risk Analysis
Document includes Technology Readiness assessments for:
- Vehicle
- Sensor
- Ground display
- Integrated Capability

Risk Summary section referenced but not detailed in provided text.

## Notable Details

### Competitive/Unique Advantages
1. **Communication-Aware Planning**: Automatic relay configuration without operator intervention—distinctive BST capability for cave/confined environment operations
2. **GPS-Denied Navigation**: SLAM-based approach viable for fully enclosed environments
3. **Structured Light Integration**: Partnership with Chiaro Technologies for miniaturized 3D imaging
4. **Multi-Vehicle Control**: Single operator control of multiple MUAS assets with cooperative mapping

### Key Constraints Addressed
- No existing fieldable UAS available for stated mission objectives
- GPS-denied operation requirement
- Constrained/confined environment navigation and mapping
- Operator simplicity (minimally-trained personnel)
- Man-portable ruggedized system
- Black-out and bright-light operational capability

### Project Status
Document dated June 2013; located in "Completed/Inactive/Unsubmitted Projects" folder, suggesting this proposal/concept was not executed or was discontinued.

### Technical Dependencies
- Chiaro Technologies partnership for structured light sensor and FPGA processing
- COTS radio solutions for mesh networking
- COTS board-level camera modules
- Commercial tablet platforms for ground control unit