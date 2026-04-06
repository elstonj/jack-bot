# Sensor Fusion and Algorithms for Mapping at Low Altitude Above Rugged Terrain

## Document Metadata
- **Type:** NASA SBIR Phase II Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** SBIR 2018-II, Subtopic A.02 (proposal number: SBIR-2018-II-A.02-9342)
- **Date:** 2019 (submitted February 15, 2019)
- **BST Products/Systems Referenced:** S2 UAS, SwiftPilot avionics, TX2 processing system
- **Key Personnel:** Dr. Maciej Stachura (Principal Investigator), Austin Anderson (Lead Engineer), Dr. Jack S. Elston (Avionics Engineer), Josh Fromm (Aircraft Design and Integration)

## Executive Summary
This Phase II proposal seeks to develop a sensor fusion and terrain-following/obstacle-avoidance system for fixed-wing UAS operating at low altitude over rugged terrain. Building on Phase I accomplishments, BST proposes to integrate multiple sensing modalities (radar, lidar, stereo vision, laser altimeter) with advanced on-board algorithms to enable autonomous low-altitude flight and safe navigation around obstacles—capabilities critical for scientific missions like volcanic plume sampling and forest monitoring, as well as routine beyond-visual-line-of-sight operations.

## Technical Approach

**Core Strategy:**
- Develop a modular terrain-following and obstacle-avoidance subsystem deployable on multiple platforms, initially on the S2 UAS
- Employ heterogeneous sensor fusion combining active sensors (radar, lidar, laser altimeter) with passive sensors (stereo vision, cameras)
- Implement real-time onboard processing using TX2 computing platform with algorithms for:
  - Terrain height estimation and tracking
  - Obstacle detection and avoidance
  - Sensor data fusion
  - Path planning and control

**Key Technical Elements:**

1. **Sensor Suite Options:** Three candidate packages were selected based on Phase I analysis:
   - **Small Radar + Stereo Package:** μSharp Patch radar (70-120m range), dual stereo cameras (50m range), laser altimeter, downward camera, TX2 processor. Total: 344g, 12.93W, $3,892
   - **Long Range Radar + Stereo Package:** LR-D1 radar (250m range), dual stereo cameras, laser altimeter, downward camera, TX2. Total: 601g, 23.43W, $7,192
   - **Lidar Package:** OS-1-16 LiDAR (100m+ range), laser altimeter, downward camera, TX2. Total: 617g, 25.2W, $5,294

2. **Terrain Following Algorithm:**
   - PID-based control using forward-pitched (60°) laser altimeter to anticipate upcoming terrain
   - Slope-based controller using AGL history to predict terrain variation
   - Running terrain height map generation from historical flight data
   - Mitigation strategies for inclement weather (fog, snow, rain) affecting laser performance

3. **Obstacle Avoidance Strategy:**
   - Discrete control laws: Climb-out controller (short obstacles) and turn-out controller (tall obstacles)
   - Kinematic analysis determined detection requirements: 60-100m range needed for aggressive maneuvers at S2's cruise speed
   - Trajectory propagation and collision detection using projected flight path
   - Sensor fusion via voxel filters or Extended Kalman Filter (EKF) approaches

4. **Processing & Simulation:**
   - Gazebo-based simulation environment with sensor models (lidar, radar, stereo, laser altimeter)
   - Terrain models imported from QGIS elevation data
   - BST SwiftPilot autopilot SDK integration for algorithm testing
   - Custom GPU-based colorization tools for machine vision cameras on TX2

## Products & Capabilities Described

### S2 UAS
- Mission-proven fixed-wing platform
- Cruise speed: high enough to require long-range obstacle sensing
- Capable of low-altitude flight (10m AGL minimum requirement)
- Altitude ceiling: 4,267m MSL
- Supports modular sensor integration
- Used as primary demonstration platform for Phase II

### SwiftPilot Avionics
- BST autopilot system with SDK
- Supports external control via SDK interface
- Can command independent lateral and vertical velocity components
- CAN bus integration for sensor data
- Enables real-time algorithm deployment and testing

### TX2 Processing System
- NVIDIA Jetson TX2 embedded processor (ARM-based)
- Carrier cards with USB3 ports and mSATA/SD card interfaces
- GPU acceleration for image processing
- Colorization and white-balance processing: custom GPU tools enabling 20 FPS on TX2 (vs. 2 FPS with stock drivers)
- Machine vision camera integration via USB3
- Custom drivers and firmware management tools developed in Phase I

### Custom Stereo Camera System
- Long-range stereo depth sensor (50m range demonstrated)
- 45° horizontal field-of-view
- Mountable under S2 wings (0.18-3m baseline options)
- 1080p resolution with global shutter for low motion blur
- Phase I prototype showed 150m range in clear conditions
- Addressed through advanced stereo matching algorithms and GPU processing

### Sensor Suite Components
- **Radars:** μSharp Patch (120m), LR-D1 (250m), automotive radar (rejected due to FCC airborne restrictions)
- **Lidars:** Ouster OS-1-16 (100m+ range, 16 channels, 20Hz)
- **Laser Altimeter:** LightWare LW20/C (downward-facing, 0.55W, $370)
- **Cameras:** Ximea machine vision cameras with global shutter, LiUSB30 stereo pairs

## Use Cases & Applications

**Scientific Missions:**
- Volcanic plume and CO2 emission sampling (low-altitude flights near terrain obstacles and tall trees)
- Forest biofuel calculation
- Invasive plant species identification
- Rock and mudslide monitoring
- Snowpack analysis

**Infrastructure & Operational:**
- Pipeline and infrastructure inspection
- High-resolution aerial imagery over large areas
- Night and low-light operations (beyond-visual-line-of-sight capability)
- Operations in areas with limited landing space
- Wildfire and disaster monitoring with temporary flight restrictions

**Specific Mission Constraints Addressed:**
- Heavy rain, light snow (50% sensor performance reduction tolerance)
- Low-light conditions (dusk, dawn) with 50% passive sensor degradation
- Rugged terrain exceeding aircraft climb capabilities
- Obstacles including tall trees (>10m) and towers
- Maximum operating power budget: 50W for sensing package
- Maximum mass budget: 1kg for sensing package
- Cost target: <$10,000 for sensing package

## Key Results from Phase I

### Mission Requirements & Analysis
- Established system requirements: 10m minimum AGL, 4,267m maximum altitude, heavy rain/light snow tolerance
- Compiled typical obstacles with size/shape estimates and detection range analysis
- Kinematic analysis showed:
  - Standard climb maneuvers require 100m detection range
  - Aggressive turn maneuvers require 60m detection range with no tailwind, 100m with 10 m/s tailwind
  - 45° horizontal field-of-view needed to encompass most wide obstacles

### Sensor Comparative Analysis
- Evaluated 10+ sensor types: 1D lasers, 3D lidars, automotive/kit radars, single/stereo/structured-light cameras, thermal
- Selected three complementary sensor packages balancing SWaP-C and performance
- Automotive radar excluded due to FCC airborne frequency restrictions; alternative bands identified

### Machine Vision Development
- Developed custom GPU-based colorization for TX2, achieving 20 FPS (vs. 2 FPS with stock drivers)
- Prototyped long-range stereo cameras with 100cm baseline: 150m range demonstrated in simulation, 104-113m in outdoor testing
- Integrated global-shutter camera, USB3 interface, and low-distortion lens for motion blur reduction
- Validated on parallel commercial photogrammetry project (underwater system)

### Simulation Environment (Gazebo)
- Created rich simulation with S2 and multi-rotor aircraft models
- Developed 1km × 1km terrain from Cambridge, MA elevation data with satellite imagery overlay
- Sensor models: laser altimeter, 3D lidar (stock and mechanically-steering variants), stereo cameras, radar (sonar-based prototype)
- Obstacle models: tree grove, 100m cooling tower, 10×10×5m solid box
- Weather simulation: fog rendering (transparent to laser but occludes passive sensors)

### Terrain Following Algorithm Development
- Implemented PID-based AGL tracking in simulation using BST autopilot SDK
- Demonstrated forward-pitched (60°) laser altimeter provides ~1+ second terrain lookahead at 10-30m AGL
- Developed slope-based controller using AGL history for smoother terrain tracking
- Terrain height estimation algorithm created, mapping AGL + position to ground mesh
- Weather impact analysis on historical S2 flights:
  - Clear conditions: reliable AGL tracking
  - Heavy fog (Costa Rica volcano): AGL dropout above 60m, false 1-2m returns
  - Heavy snow (S1 flight): false 1-2m returns throughout flight
  - Mitigation strategy: GPS/pressure altitude validation against AGL change rate

### Obstacle Avoidance Algorithms
- Reviewed and selected Barry's trajectory propagation approach with discrete control laws
- Identified two primary controllers: climb-out (short obstacles) and turn-out (tall obstacles)
- Validated feasibility through kinematic analysis
- Proposed multi-sensor fusion approaches: voxel filters (simple, fast) and EKF (noise-model-based)
- Explored deep learning semantic segmentation for obstacle classification (>10 Hz performance on TX2)

## Notable Details

**Phase I Accomplishments Enabling Phase II:**
1. Selection of two concrete sensor package configurations ready for hardware build and flight test
2. Custom stereo depth camera system design with demonstrated feasibility (simulation and prototype)
3. Complete Gazebo simulation framework ready for algorithm iteration
4. Terrain following algorithms already implemented and tested in simulation
5. Demonstrated TX2 machine vision processing capability through parallel commercial project

**Competitive Advantages & Feasibility:**
- Leverages fixed-wing platform's efficiency and endurance vs. multi-rotor VTOL alternatives
- Heterogeneous sensor fusion mitigates individual sensor weaknesses (e.g., lidar in fog, vision in low light)
- Modular design applicable to multiple platforms beyond S2
- Strong foundation from Phase I significantly de-risks Phase II execution
- Addresses real scientific mission gaps (current operations restricted to level terrain with few obstacles)

**Technical Risks Identified & Mitigation:**
- Custom stereo vision system feasibility: **Mitigated** through simulation and prototype validation
- TX2 GPU processing performance: **Mitigated** through custom colorization tools achieving 20 FPS
- Weather performance of laser altimeter: **Addressed** with hybrid sensor fusion strategy and false-return rejection
- Long-range obstacle detection: **Validated** through kinematic analysis and sensor selection process

**Commercialization Path:**
- Phase III target: production-ready terrain-following/obstacle-avoidance module for S2
- Market applications: scientific research (volcanoes, forests, disaster monitoring), infrastructure inspection
- Commercial capability: modular subsystem deployable on multiple platforms
- Business plan includes phases for algorithm refinement, flight testing, and market validation

**Related BST Activities:**
- Safe2Ditch technology mentioned as complementary capability for autonomous safe-area landing
- Parallel commercial photogrammetry project accelerating machine vision hardware development
- Ongoing NASA-funded landing zone detection project exploring deep learning segmentation