# AA Phase 2 Workplan Draft

## Document Metadata
- Type: Phase II SBIR workplan/proposal
- Client/Agency: NASA
- Program/Solicitation: 2018 NASA SBIR, Terrain Following topic
- Date: 2019-01-24 (created), 2019-01-25 (last modified)
- BST Products/Systems Referenced: S2 (aircraft), BST Autopilot, TX2 (NVIDIA Jetson), BST SDK, SWIL (Software-in-the-Loop), HWIL (Hardware-in-the-Loop)
- Key Personnel: Not named in document

## Executive Summary
This Phase II workplan outlines BST's approach to developing autonomous terrain-following and obstacle-avoidance capabilities for small UAS. The work spans simulation environment development, algorithm development across multiple sensor modalities (lidar, stereo vision, laser altimeter, radar), hardware integration on the S2 platform, and extensive flight testing validation.

## Technical Approach

### Simulation Environment Development (Section 2)
- Comprehensive sensor modeling (radar, camera, 1D laser, lidar) with realistic noise, fault injection, and point cloud generation
- S2 aircraft CAD model with aerodynamic characterization (coefficients, moments of inertia, motor/prop parameters)
- Integration with BST Autopilot and control surface mapping
- Terrain generation from QGIS data and photogrammetry meshes
- Integration of new data types (images, stereo, laser point clouds, radar point clouds) into BST SDK
- SWIL (Gazebo-based) and HWIL development with TX2 interface
- Scenario-specific simulations: canopy, agriculture, volcano/mountain, takeoff/landing, urban

### Algorithm Development (Section 3)
- **Laser Altimeter (3.1)**: False return mitigation, firmware implementation, flight data verification
- **Lidar (3.2)**: False return mitigation, obstacle injection, TX2 implementation
- **Terrain Following (3.3-3.11)**: PID/slope control on S2, height map control, trajectory generation, discretized climb and turnout controllers
- **Machine Vision - Stereo Depth (3.4, 3.6)**: Stereo depth algorithm evaluation and downselection, homogenous terrain and weather detection, calibration methodology
- **Machine Vision - Downward (3.5, 3.7)**: Z-velocity aided AGL estimation, calibration methodology
- **Obstacle Mapping & Sensor Fusion (3.8-3.10)**: Voxel-based grids, SLAM (LiDAR, stereo, radar, heterogeneous), machine learning obstacle identification
- **Advanced Control**: Wind estimation, trajectory propagation/collision detection, integrated obstacle avoidance simulation
- **Radar (3.17)**: Sensor design, realistic return plugins, signal processing

### Hardware Development (Section 4)
- TX2 firmware development with SDK, autopilot, and sensor interfaces
- Mechanical integration mockup and EMI testing
- S2 component modifications for commercial integration
- Radar sensor procurement from subcontractor

## Products & Capabilities Described

### S2 Aircraft
- Small UAS platform serving as primary flight test vehicle
- CAD model to be developed with aerodynamic characterization
- Modifications for commercial integration planned
- Will be integrated with multiple sensor suites and TX2 processing

### BST Autopilot
- Firmware platform for implementing terrain-following and control algorithms
- Integration with sensors and external processing (TX2)
- Control mapping and tuning for new algorithms
- Support for PID control, wind estimation, trajectory generation

### TX2 (NVIDIA Jetson)
- Embedded processor for real-time vision and lidar processing
- Interface to BST Autopilot and sensors
- Running machine vision stereo/downward algorithms
- Embedded obstacle mapping and SLAM implementations

### BST SDK
- Integration of new data types: stereo images, laser/radar point clouds, timing information
- Interface layer for SWIL/HWIL testing

### Simulation Systems
- **SWIL (Software-in-the-Loop)**: Gazebo-based with simulation clock
- **HWIL (Hardware-in-the-Loop)**: TX2-based hardware interface for algorithm testing

## Use Cases & Applications

1. **Agricultural Terrain Operations**: Terrain following over flat and rugged farm terrain with obstacle avoidance
2. **Mountainous/Rugged Terrain**: Terrain following with 30m altitude maintenance over rugged topography
3. **Canopy Operations**: Flight through or near dense vegetation with collision avoidance
4. **Volcanic/Mountain Survey**: Operation in elevated terrain with optional smoke conditions
5. **Urban Environment**: Autonomous navigation in built-up areas
6. **Takeoff/Landing**: Autonomous operations with obstacles on approach/departure paths

## Flight Testing Plan (Section 5)
- **Test Sites**: Agricultural terrain, mountainous terrain, canopy areas
- **Iterative Terrain Following Tests**: Data gathering across identified areas
- **Obstacle Avoidance**: Manual flight with obstacles, then automated flight
- **Open-Loop Testing**: Algorithm validation in diverse terrain
- **Functional Demonstrations**:
  - Terrain following (flat terrain, 10m altitude)
  - Terrain following (rugged terrain, 30m altitude)
  - Simulated obstacle avoidance (flat terrain)
  - Real obstacle avoidance (flat terrain)

## Notable Details

### Sensor Suite
- Laser altimeter(s) for low-altitude AGL measurement
- Lidar for 3D obstacle detection
- Stereo camera pair for depth estimation
- Downward-looking camera for optical flow/AGL
- Radar for potential adverse weather operation

### Key Technical Purchases
- Laser altimeters
- Lidar unit(s)
- Stereo cameras
- Downward cameras
- TX2 processing unit
- High-performance GPU-equipped server at BST for simulation
- Radar sensor from subcontractor

### Simulation Realism Features
- Wind and wind estimation plugins
- Photogrammetry-based terrain meshes
- Sensor-specific noise and fault injection
- Multiple simultaneous sensor simulation (heterogeneous sensor fusion)

### Algorithmic Sophistication
- SLAM-based approach evaluated across multiple sensor modalities
- Machine learning for obstacle classification
- Voxel-based and SLAM-based obstacle mapping compared
- Wind estimation integrated with terrain following control

### Risk Management
- Dedicated risk review and update process (1.4)
- Redundant test approaches (simulation, HWIL, flight)
- Post-processed flight data verification at each stage
- Hardware downselection process for cameras based on testing