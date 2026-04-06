# Old AA Phase 2 Workplan Draft

## Document Metadata
- Type: Phase II SBIR workplan / project planning document
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR, Terrain Following topic
- Date: Created 2019-01-22, Modified 2019-01-25
- BST Products/Systems Referenced: S2 (fixed-wing UAS), BST Autopilot, TX2 (NVIDIA Jetson), SwiftCore SDK (SWIL - Software-in-the-Loop, HWIL - Hardware-in-the-Loop)
- Key Personnel: Not named in document

## Executive Summary
This Phase II workplan outlines BST's proposed development of autonomous terrain-following and obstacle-avoidance capabilities for the S2 UAS platform. The plan integrates multi-sensor perception (radar, lidar, laser altimeter, stereo vision, downward camera), simulation environment development, algorithm implementation, hardware integration, and flight testing across multiple terrain types and mission scenarios.

## Technical Approach

### Simulation Environment Development (Section 2)
- **Sensor Modeling**: Development of realistic models for radar, camera, laser altimeter, and lidar with point cloud generation and fault injection capabilities
- **S2 Aircraft Modeling**: CAD development with aerodynamic coefficients, moments of inertia, motor/prop parameters; BST Autopilot integration with control mapping and tuning
- **Terrain Generation**: Methods for converting QGIS data and photogrammetry maps to 3D mesh/skin formats for simulation
- **SDK Integration**: Adding new data types to BST SDK (images, stereo images, laser point clouds, radar point clouds) with proper timing
- **SWIL/HWIL Development**: Software-in-the-Loop using Gazebo simulation clock; Hardware-in-the-Loop to both BST Autopilot and TX2
- **Simulation Hardware**: High-performance server with GPU capability for laser ray tracing
- **Scenario-Specific Simulations**: Canopy (photogrammetry-based), agriculture with buildings, volcano/mountain (with/without smoke), takeoff/landing with obstacles, homogeneous terrain, urban terrain

### Algorithm Development (Section 3)

**3.1 Laser Altimeter**
- False return mitigation development
- Implementation in autopilot firmware
- Verification with post-processed flight data

**3.2 Lidar**
- False return mitigation
- Obstacle injection plugin
- TX2 implementation
- Post-flight data verification

**3.3 Terrain Following Algorithm**
- PID/slope control on S2
- PID control in autopilot firmware
- Height map control development (update to slope control)
- Trajectory generation with PID control
- Firmware or TX2 implementation

**3.4 Machine Vision Stereo**
- Evaluate multiple stereo depth algorithms (Phase I candidates)
- Test on laptop and TX2
- Develop homogeneous terrain and weather detection
- HWIL testing and post-data verification

**3.5 Machine Vision Downward**
- Downward camera with z-velocity estimate for AGL (above ground level) estimation
- Testing across laptop, SWIL, embedded, HWIL levels

**3.6 Obstacle Tracking and Sensor Fusion**
- Basic voxel grid approach on lidar
- Heterogeneous sensor voxel grid
- SLAM evaluation and implementation on lidar, stereo, radar, and heterogeneous systems
- Machine learning for obstacle identification
- Embedded implementation with post-flight verification

**3.7 Obstacle Avoidance**
- Trajectory propagation and collision detection
- Discretized controllers (climb, turn standard, aggressive)
- Wind estimation incorporation
- Climbout and turnout simulation (ag environment with long-range radar, stereo, lidar)

**3.8 Radar Processing**
- Plugins for realistic radar returns
- Radar processing algorithm development

## Products & Capabilities Described

### S2 (Fixed-Wing UAS)
- Primary test platform for terrain following and obstacle avoidance
- CAD model to be developed with aerodynamic characterization
- Will carry multi-sensor payload (radar, lidar, laser altimeter, stereo vision, downward camera)
- Integration with BST Autopilot for autonomous control

### BST Autopilot
- Flight control system to integrate terrain-following and obstacle-avoidance algorithms
- Will implement laser altimeter mitigation, PID terrain following control, and fusion algorithms
- Interface to TX2 processing platform

### TX2 (NVIDIA Jetson)
- Embedded processor for real-time sensor processing
- Will run lidar false-return mitigation, stereo vision algorithms, obstacle tracking/sensor fusion, and machine learning models
- Requires firmware development for SDK interface, autopilot interface, HWIL interface, and multi-sensor interfaces

### BST SDK
- Software development kit to be expanded with new data types: images, stereo images, laser point clouds, radar point clouds
- Will support timing coordination across sensors
- SWIL and HWIL capabilities for testing

## Use Cases & Applications

1. **Agriculture Terrain Following**: Low-altitude flight over flat and hilly agricultural terrain with building obstacles
2. **Mountainous Terrain Following**: Flight over rugged, high-elevation terrain (30m AGL demonstrations planned)
3. **Canopy/Forest Navigation**: Flight through or above dense vegetation (photogrammetry-based simulation)
4. **Volcano/Mountain Survey**: Operation in mountainous areas with potential smoke interference
5. **Takeoff/Landing Operations**: Autonomous takeoff and landing with obstacle avoidance on approach/departure
6. **Urban Environment Navigation**: Generic urban terrain with buildings and obstacles
7. **Low-Altitude Obstacle Avoidance**: Both manual and automated flight testing with real and simulated obstacles

## Key Results
No results section present; this is a workplan draft, not a completed report. The document outlines planned work, not achieved results.

## Notable Details

- **Iterative Testing Approach**: Multi-level testing strategy (laptop → SWIL → embedded → HWIL → flight test → post-processing verification) for each algorithm
- **Multi-Sensor Integration**: Heterogeneous sensor fusion combining radar, lidar, laser altimeter, stereo vision, and downward camera
- **Specific Performance Targets**: Terrain following demonstrations at 10m AGL (flat) and 30m AGL (rugged terrain)
- **Collision Avoidance Structure**: Procurement of inflatable pylons for safe flight testing
- **Flight Test Sites**: Multiple terrain types identified (agricultural, mountainous, canopy)
- **Hardware Procurement**: Radar hardware to be developed by subcontractor with modifications
- **EMI Testing**: Full electromagnetic interference testing planned for multi-sensor integration

This appears to be a comprehensive Phase II development plan translating Phase I research into a fully integrated, flight-ready autonomous terrain-following and obstacle-avoidance system for the S2 platform. The plan emphasizes simulation fidelity and iterative verification before flight testing.