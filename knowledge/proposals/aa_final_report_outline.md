# AA Final Report Outline

## Document Metadata
- Type: Final report outline/working notes
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR Phase I, Terrain Following topic
- Date: Created 2019-01-17, Modified 2019-01-30
- BST Products/Systems Referenced: S2 (fixed-wing UAS), SwiftCore autopilot, SDK
- Key Personnel: Josh (referenced for CAD/modeling tools)

## Executive Summary
This is a working outline for a NASA SBIR Phase I final report on terrain-following autonomous flight capabilities. BST conducted extensive sensor integration work (cameras, LiDAR, radar, laser altimeters), developed hardware and algorithms for obstacle detection and avoidance, created Gazebo simulation environments, and implemented terrain-following altitude controllers for both multirotor and S2 fixed-wing platforms.

## Technical Approach

### Imaging Hardware & Machine Vision
- **GPU-accelerated colorization**: Implemented Nvidia TX2 GPU processing to accelerate Bayer format image colorization and correction from 2 FPS to 25 FPS (standard ML camera libraries didn't support performant ARM color processing)
- **Precision timing**: Developed nanosecond-precision camera timestamps with time alignment mechanisms synching camera clocks to TX2 via PPS (pulse-per-second) signals from IMU and GPS
- **Stereo vision**: Designed stereo camera system with calibration, rectification, and deep learning-enhanced block matching algorithms (replacing basic OpenCV approaches)
- **Web video streaming**: Developed 1080p video streaming to web interface for operator feedback and debugging

### LiDAR Integration
- Identified lighter, more accessible options (Ouster OS1, potentially RoboSense)
- Simulated full point cloud matching Ouster 16-channel spinning system in Gazebo
- Demonstrated strong terrain and tree resolution for terrain following

### Radar Assessment
- Reviewed FCC regulations; determined 76/77 GHz automotive radars cannot be used for airborne applications
- 77 GHz preferred over 24 GHz for better range resolution (~5 GHz vs. ~200 MHz bandwidth) and angular resolution
- Identified small patch radar vendor: low power, lightweight, long-range, low-cost, but limited performance (single beam, wide angles, strongest return only, no Doppler)
- Note: Did not obtain actual radar flight data despite efforts; simulated basic radar in Gazebo with path forward for more complex modeling

### Laser Altimetry
- Costa Rica flights showed 1-2 m range degradation in fog
- Heavy snow flights also showed 1-2 m range degradation
- Integrated narrow-beam sonar initially (very noisy/inaccurate), switched to 1D laser for cleaner simulation results

### Sensor Fusion & Obstacle Avoidance
- **SLAM**: Applied SLAM techniques (historically used with LiDAR, stereo, ultrasonic) to build environment maps with heterogeneous sensor fusion
- **Voxel grid overlays**: Short time-history voxel grids filter LiDAR and stereo data to assess obstacle likelihood
- **Obstacle avoidance**: Discretized reactive controllers based on sensor data; identified MIT paper approach as preferred over RRT or vector field methods (latter require good maps not expected in terrain following scenarios)
- **Sensor fusion requirements documented**: Different coverages, rates, noise characteristics, data volumes, and types (intensities for lasers, SNR/Doppler for radar, disparity for stereo)

### Terrain Following Control
- **Altitude controller**: Developed AGL (above-ground-level) controller measuring altitude and correcting for pitch/roll
- **PID control with slope estimation**: PID converts AGL error to z-axis velocity; controller computes terrain slope via regression to smooth control commands
- **Predictive control**: Uses forward-facing laser (on quadcopter) to predict terrain ahead; estimated terrain height from AGL vs. GPS height difference
- **Limitations**: SDK limited to ~20 Hz external control (faster overruns autopilot interface); pure PID fails on large AGL steps (boxes, trees); faster controller needed in firmware
- **Safety logic**: Climbing preferred over descending; descent rate limited

## Products & Capabilities Described

### S2 (Fixed-Wing UAS)
- Created CAD model in Gazebo with sensor integration
- Developed S2-specific SWIL (software-in-the-loop) simulation using bounding boxes for collision detection
- Path forward: incorporate moments of inertia/weight, motor plugin from multirotor, lift/drag plugins for control surfaces, mesh models for ailerons/ruddervators/flaps

### Jetson TX2
- Identified TX2 carrier cards for embedded processing
- Worked extensively on image processing libraries/deployment
- Resolved issues with ML camera Bayer format transmission and colorization (GPU-accelerated solution)
- Integrated with stereo algorithms and deep learning implementations

### SwiftCore Autopilot & SDK
- Published GPS, pressure, magnetometer, and laser altitude data to autopilot
- SDK subscribed to autopilot and provided waypoint/altitude commands
- External control limited to ~20 Hz due to communication interface bottleneck
- Integrated with Gazebo for SWIL testing

## Use Cases & Applications

- **Terrain following autonomous flight**: Low-altitude autonomous navigation maintaining safe clearance above ground/obstacles
- **Forest/canopy environment navigation**: Tested with simulated trees (~6 m tall) and real data from Costa Rica flights
- **All-weather operations**: Laser altimetry degradation in fog/snow noted; radar's all-weather capability emphasized as appealing despite performance tradeoffs
- **Arctic/mountainous terrain**: Implied by emphasis on varied terrain simulation
- **Obstacle avoidance in GPS-denied/complex environments**: SLAM and reactive control for densely vegetated or structurally complex terrain

## Simulation Work (Gazebo)

### Multi-rotor SWIL
- Existing simulation designed to fly like fixed-wing (constant speed, banking for heading)
- Integrated 1D laser, stereo cameras, LiDAR, fixed forward-facing radar
- Designed large square flight paths for testing

### World Development
- Built Cambridge, MA demo world (1 km²) using DAE/STL meshes from QGIS terrain data
- Added obstacles: reactor cooling tower, 8 oak trees (~6 m), 10×10×5 m box
- Identified models available online: light posts, gas stations, pine trees, walls, Jersey barriers
- Path forward: use DAE tools, photogrammetry-based canopy meshes, build procedural terrain

### Sensor Models Integrated
- Stereo cameras with dynamic pixeling
- LiDAR (16-channel spinning)
- Narrow-beam sonar and 1D laser
- Forward-facing radar (basic, with path for advanced ray-tracing)
- Downward camera

## Key Results/Findings

- **Performance improvements**: GPU acceleration increased image processing from 2 FPS to 25 FPS
- **Simulation validation**: SWIL successfully validated terrain following algorithms; demonstrated sensor fusion with heterogeneous data
- **Sensor trade studies**: LiDAR superior for terrain resolution but weight concerns; radar all-weather capability appealing but performance-limited; stereo vision viable with GPU acceleration
- **Terrain prediction**: Historic flight data and height maps can estimate flat terrain vs. canopy (via std. deviation analysis)
- **Control limitations**: Pure PID AGL control fails on step responses; slope-based predictive control improves performance; reactive obstacle avoidance preferred over map-based planning

## Notable Details

- **FCC regulatory constraint**: 77 GHz automotive radars cannot be used airborne (significant finding for sensor selection)
- **Commercialization partnership**: Imaging hardware work done with IPOZ; they requested stereo depth and operator feedback improvements
- **GPU acceleration innovation**: Custom implementation of colorization/correction on Jetson TX2 addresses limitation in commercial ML camera software (Ximea, Point Grey/FLIR)
- **Timing precision**: Developed kernel module for tight nanosecond-precision time alignment critical for multi-sensor fusion
- **Radar data gap**: Despite efforts, did not obtain actual radar flight test data (only simulation)
- **Deadline note**: Phase II Implementation Plan and Final Report marked "in work" at document creation date

**Note**: This document is a working outline with informal annotations and editorial comments (bracketed [a]-[d]), not a polished final report. Substantial content remains to be written for final deliverable.