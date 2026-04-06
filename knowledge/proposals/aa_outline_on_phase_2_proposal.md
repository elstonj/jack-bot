# AA Outline on Phase 2 Proposal

## Document Metadata
- Type: Phase II SBIR Proposal Outline/Planning Document
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR (Terrain Following topic)
- Date: Created 2019-01-17; Modified 2019-01-25
- BST Products/Systems Referenced: S2 (aircraft), BST Autopilot, TX2 (Jetson development board), SwiftCore SDK
- Key Personnel: Not named in document

## Executive Summary
This Phase II proposal outlines Black Swift Technologies' two-year plan to develop autonomous terrain-following and obstacle-avoidance capabilities for fixed-wing UAS, leveraging the S2 platform. The work integrates multiple sensors (stereo vision, LiDAR, radar) with simulation and flight testing to create a modular, fieldable system applicable beyond the S2 aircraft.

## Technical Approach

### Simulation Work
- **Finalize Simulation Environment**: Improve radar model with sensor plugins to control scan volume; develop hardware-in-the-loop (HWIL) interfaces to TX2 and BST Autopilot; explore GPU-accelerated simulation
- **S2 Aircraft Modeling**: Evaluate and integrate existing lift/drag plugins; develop improved models as needed; update plugin and integrate with autopilot
- **Terrain Integration**: Convert photogrammetry to mesh/skin; leverage QGIS data; formalize data collection schemes (timing, images, stereo imagery, laser point clouds, radar point clouds)
- **Scenario-Specific Simulations**: Build canopy, agriculture (with buildings), volcano/mountain, takeoff/landing, homogeneous terrain, and urban simulations

### Algorithm Work
- **Terrain Following**: Run PID/slope control on S2; implement PID control in autopilot firmware
- **Height Map Control**: Develop trajectory generation and PID control; implement in firmware or on TX2
- **Machine Vision**: Evaluate stereo depth algorithms identified in Phase I; downselect and implement; convert stereo disparity to depth (with/without calibration); use downward camera with Z-velocity estimate for AGL (above ground level) estimation
- **Obstacle Identification & SLAM**: 
  - Basic voxel grid approach for LiDAR data
  - Heterogeneous sensor fusion (voxel grid across multiple sensor types)
  - Evaluate and downselect SLAM implementations/hardware
  - Implement SLAM on LiDAR, stereo, radar, and heterogeneous sensor simulations
- **Obstacle Avoidance**: Develop climbout and turnout simulations; test with long-range radar, stereo, and LiDAR

### Hardware Work
- Integrate TX2 package with BST Autopilot (modular design via SDK)
- Procure camera, radar, LiDAR, and laser hardware
- Develop TX2 firmware with interfaces to:
  - BST Autopilot
  - HWIL systems
  - Cameras, LiDAR, radar
- Full EMI testing and mechanical integration

### Flight Testing
- **Phase 1 (Data Collection)**: No algorithms running, gather sensor data
  - Flat terrain test at 30m (sod farm, no obstacles)
  - Low-altitude mountain test
  - Low-altitude tree canopy test
- **Phase 2 (Autonomous Operations)**:
  - Automated terrain following over sod farm (no obstacles)
  - Obstacle avoidance without terrain following (test on sod farm; first with man-in-the-middle, then full autonomous)
- **Regulatory**: Operate under Part 107 rules (500 ft. ceiling); test obstacle scenarios using constructed inflatable barriers

## Products & Capabilities Described

### S2 Aircraft
- Fixed-wing platform with faster flight, longer range, and different dynamics than multi-rotor systems
- Model to be developed/improved for simulation; hardware integration of TX2 and sensor packages planned
- Capable of low-altitude autonomous flight with terrain following

### BST Autopilot
- Flight management system to be integrated with TX2 sensor processing board
- PID control implementations for terrain following and height map control
- HWIL/SWIL support through Gazebo interface
- SDK-based interfaces for modular sensor integration

### TX2 (Jetson Development Board)
- Primary sensor processing hardware
- Will run stereo depth algorithms, SLAM, obstacle identification, and height map control
- Firmware development for sensor interfaces
- Modular design allowing use on platforms beyond S2

### Sensing Suite
- **Stereo Vision**: Depth estimation with/without calibration; downward-facing camera for AGL estimation
- **LiDAR**: Point cloud data; voxel grid obstacle identification; SLAM implementation
- **Radar**: Long-range detection for fixed-wing speeds; radar point clouds; SLAM implementation
- **Laser**: Acquisition planned (specific use not detailed)

### BST SDK
- Publicly available interface for SWIL/HWIL development
- Standardizes sensor access and autopilot integration for modularity

## Use Cases & Applications

1. **Terrain Following**: Autonomous low-altitude flight over varying terrain (flat, mountainous, forested)
2. **Agriculture**: Flight over agricultural land with building obstacles
3. **Volcano/Mountain Monitoring**: Autonomous flight in complex terrain environments
4. **Canopy Penetration**: Low-altitude flight over tree canopy for environmental monitoring
5. **Takeoff/Landing**: Autonomous operations from constrained locations
6. **Obstacle Avoidance**: General autonomous flight with collision avoidance
7. **Fixed-Wing UAS Operations**: Capabilities noted as applicable to fixed-wing systems (vs. multi-rotor competition)

## Notable Details

### Competitive Advantages
- **Fixed-wing platform**: Emphasizes speed, range, and different dynamics compared to multi-rotor UAS (references 3DR, DJI, and Skydio as multi-rotor competitors)
- **Modular design**: Sensor processing suite designed separately from aircraft; applicable to other platforms via BST SDK
- **Relevant sensor suite for fixed-wing**: Radar integration highlighted as particularly relevant for fixed-wing collision avoidance, which is noted as "challenging and novel" for fixed-wing UAS given speed and detection range requirements
- **Continuing NAS integration**: Modular approach supports NASA integration

### Key Requirements/Constraints
- Part 107 compliance (500 ft. ceiling)
- 2-year development timeline with Gantt breakdown and hour estimates (not detailed in outline)
- Hardware integration requiring EMI testing
- Both simulation (Gazebo-based) and flight validation approach

### Phase I Reference
Document references Phase I work identifying eight mission scenarios and downselected sensors/algorithms; Phase II will expand to include urban simulation based on customer feedback.

---

**Note**: This is a planning/outline document rather than a complete proposal. It lacks detailed budget, team information, and some sections marked "Scratch below here" contain incomplete technical descriptions. The document serves as a task breakdown and technical approach outline for Phase II development.