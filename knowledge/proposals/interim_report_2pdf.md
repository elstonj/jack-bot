# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: Phase I Interim Report (SBIR)
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA) - Office of Oceanic and Atmospheric Research
- Program/Solicitation: NOAA SBIR Phase I, Grant Award Number NA20OAR0021000
- Date: August 2020 (Interim Report covering January 1, 2020 - August 31, 2020)
- BST Products/Systems Referenced: S2 UAS, Jetson TX2
- Key Personnel: Jack Elston (CEO, Project Director/Principal Investigator)

## Executive Summary
Black Swift Technologies proposed to develop a GPS-independent positioning system to enable beyond-line-of-sight (BLOS) UAS operations that can function during GPS loss, jamming, or spoofing. The system combines high-rate inertial navigation with lower-rate absolute position solutions and includes GPS monitoring for spoofing/jamming detection. Phase I focused on developing and flight-testing the inertial solution and designing algorithms for absolute position estimation based on machine vision and signals of opportunity.

## Technical Approach

### Core System Architecture
The DS-GPS (Diverse-Source GPS) system comprises four integrated components:

1. **GPS Monitoring Subsystem**: Detects GPS spoofing and jamming; triggers mode switching
2. **Inertial Estimation**: MEMS IMU + optical flow fusion to maintain accurate position estimate during GPS denial
3. **Absolute Position Estimation**: Machine vision and signals of opportunity to provide periodic unbiased position corrections
4. **Sensor Fusion**: Combines inertial and absolute solutions, provides 20Hz position updates

### Key Technical Algorithms Developed

**Preprocessing Algorithm Design**
- Analyzes proposed flight areas to recommend best navigation techniques
- Accesses open-source data: OpenStreetMaps (roads, coastlines), ArcGIS satellite imagery (30cm, 60cm, 1m resolution), RF transmitter databases (OpenCelliD, Antennas Direct)
- Tools developed to automatically pull road/coastline maps and assess optical navigation suitability
- Uses ORB feature extraction on satellite imagery to calculate figure-of-merit for optical tracking performance per sub-window
- Image preprocessing with adaptive sharpening to improve feature detection accuracy

**Key Frame Following Algorithm**
- Maps environment during GPS-available phase by collecting downward-facing imagery at calculated intervals based on field-of-view, ground speed, and altitude
- Extracts ORB features and saves descriptors with GPS-tagged coordinates (key frame memory)
- During GPS loss, switches to localization mode: continuous image capture + optical flow integration for speed estimation
- Performs feature matching against n-nearest keyframes; homography transform projects keyframe into current camera view
- Generates absolute position correction from 5-point homography, averaged with standard deviation tracking
- Fuses corrected position with optical flow using adaptive weighting based on match confidence

Flight test simulation results (50m and 120m AGL mapping):
- Achieved position errors below 50m RMS target for most segments
- Lower altitude (50m) provided more accurate laser altimeter readings and better optical flow estimation but limited field of view
- Higher altitude (120m) offered superior cross-range coverage and fewer required keyframes
- Banking maneuvers caused temporary errors exceeding 50m target due to reduced feature matching success
- 1 Hz update rate during localization maintained errors below targets for 45+ seconds using optical flow alone

**SLAM Algorithm Development**
Two approaches evaluated:

*RTAB-Map (Depth-based SLAM):*
- Evaluated RGB-D SLAM for full 3D map generation
- Developed depth simulation from monocular camera using IMU pitch/roll + laser altimeter + flat-earth assumption
- Converted simulated depth from spherical to Cartesian coordinates for RTAB compatibility
- Issues: Wild map drift without global optimizer; characteristic "bathtub" distortion in point clouds; excessive processing demands for embedded targets
- Optical flow odometry drift caused map skewing; loop closures made minimal corrections
- Conclusion: Simulated depth insufficient; true depth sensors (stereo, LiDAR) needed for reliable nighttime operation

*ORB-SLAM2 (Monocular SLAM):*
- Selected for cutting-edge performance; produces scale-invariant trajectory
- Successfully ported to Jetson TX2 embedded hardware
- GPU-accelerated version achieved 27 FPS with optimized parameters (750 ORB features, 1.5 pyramid scale step, 6 pyramid levels)
- Resource utilization: 2.5 CPU cores, 2.6 GB memory (32% of available), ~25% GPU average
- Developed automatic scale correction using laser altimeter and flat-earth ground range estimation
- Implemented two transformation methods:
  1. GPS-based affine transform for GPS-available periods (3x4 transform matrix)
  2. Scale-corrected rotation for GPS-denied operations
- Achieved 50m error target with proper GPS training phase

**Road Following Algorithm Development**
- Developed deep learning network for road identification and segmentation from satellite imagery
- Identified open-source training data (high-resolution satellite imagery)
- Developed classic machine vision techniques to extract coastlines from satellite data
- Created algorithms for:
  - Road segment recognition and localization with uncertainty estimation
  - Coastline segment recognition in maps
  - Preprocessing of map data for localization
- Demonstrated localization in simulation using road/coastline network constraints

### Navigation Signals Assessment
**Traditional Navigation Signals:**
- Identified existing navigation aids applicable to UAS (e.g., DME, VOR, NDBs)
- Surveyed hardware requirements for signal processing on UAS platforms

**Signals of Opportunity:**
- Assessed multiple signal standards for navigation viability
- Software-defined radio (SDR) hardware packages identified
- Conducted literature review of signals-of-opportunity navigation techniques
- Performed TV signal simulation (tested feasibility of cellular and TV tower signals)
- Conclusion: Signals of opportunity viable for nighttime/low-visibility operations; requires Phase II implementation

### GPS Spoofing & Jamming Detection
- Comprehensive literature review of detection methods completed
- GPS jamming detection: multiple methods examined; recommendations provided for Phase II
- GPS spoofing detection: multiple methods examined; recommendations provided for Phase II
- Hardware selection: Two candidate options identified capable of detecting both spoofing and jamming

## Products & Capabilities Described

### S2 UAS (Black Swift Aircraft)
- Primary flight test platform
- Equipped with:
  - Downward-facing machine vision camera
  - Laser altimeter
  - IMU with pressure sensors
  - Jetson TX2 embedded processor
  - Optical flow sensors
  - Airdata sensors
- Capable of GPS-denied navigation with proposed DS-GPS system integrated as external GPS-like unit
- Previously demonstrated full design and flight testing within Phase I on prior NOAA SBIR effort

### DS-GPS Hardware Module (Proposed Phase II Product)
- **Price target**: <$6,000 per unit
- **Weight target**: <350g
- **Position accuracy target**: 50m RMS error without GPS
- **Interface**: GPS-compatible serial port for direct integration with existing avionics
- **Components**: Optical flow instrument, MEMS IMU, pressure sensors, machine vision camera, Jetson TX2, GPS monitor hardware
- **Update rate**: 20 Hz position estimates with error bounds

## Use Cases & Applications

### BLOS Operations in GPS-Denied Environments
- Missions in areas with jamming/spoofing threat
- Extended duration flights beyond line-of-sight radio range
- Return-home capability during GPS loss

### Environmental Monitoring
- Hurricane/tropical storm sampling (implied NOAA application)
- Volcano monitoring
- Methane/emissions detection (referenced in context of BST capabilities)
- Arctic operations in high-latitude/high-magnetic-declination environments

### Day/Night All-Weather Operations
- Optical navigation: daylight and twilight conditions
- Signals of opportunity: nighttime capability (TV, cellular signals)
- Hybrid approach enables 24-hour BLOS operations

## Key Results (Phase I Interim)

### Completed Milestones
1. **Hardware prototype**: IMU board with pressure sensors, Jetson TX2, machine vision camera integrated into S2 UAS
2. **Inertial navigation algorithms**: Implemented and flight-tested with optical flow fusion
3. **Absolute position solutions**: Demonstrated via key frame following and ORB-SLAM2 methods
4. **Preprocessing algorithms**: Fully functional for flight area analysis
5. **SLAM evaluation**: Comprehensive assessment of RTAB-Map and ORB-SLAM2; recommendations for Phase II

### Algorithm Performance Data
- **Key frame following**: 50m RMS error achieved with 50m altitude mapping; errors stay below target for extended GPS-denied periods
- **ORB-SLAM2 on embedded hardware**: 27 FPS real-time processing; 50m localization error target achievable with GPS training phase
- **Optical flow alone**: Maintains <50m error for 45+ seconds without absolute corrections
- **Feature extraction**: ORB-based preprocessing accurately predicts optical navigation performance via satellite imagery analysis

### Technical Validation
- Preprocessing algorithm validated on multiple test areas (Boulder, CO sod farm; Potsdam, Germany; Milbridge, ME)
- Flight test data from S2 UAS processed for algorithm validation
- Hardware-in-loop (HWIL) simulations using Gazebo RGB-D camera models
- All major algorithms successfully ported to Jetson TX2 embedded hardware

## Notable Details

### Partnerships & Collaborations
- NOAA Office of Oceanic and Atmospheric Research (funding agency)
- No external commercial partners mentioned in Phase I work
- Leverages open-source tools: OpenStreetMaps, ArcGIS, RTAB-Map, ORB-SLAM2, ROS

### Unique Capabilities & Advantages
- Deep learning road segmentation and machine vision-based localization
- Diverse source fusion: optical flow + key frame matching + SLAM + signals of opportunity
- Embedded real-time processing on Jetson TX2 (proven feasibility at 27 FPS)
- Adaptive preprocessing to assess flight area suitability before mission
- GPS compatibility: drop-in replacement for standard GPS units via serial interface
- Proven Phase I flight testing capability (referenced prior NOAA project where full aircraft designed/built in Phase I)

### Phase II Plan
- Complete vision-based absolute position system implementation
- Full sensor fusion integration with extended Kalman filter (EKF)
- GPS spoofing detection implementation
- GPS jamming detection implementation
- Signals of opportunity implementation (TV, cellular signals)
- Full flight testing of integrated DS-GPS system
- Hardware packaging and optimization for production prototype

### Challenges Identified
- RTAB-Map RGB-D approach unfeasible with simulated depth; requires true depth sensors
- Optical flow drift over extended periods without absolute corrections
- Laser altimeter range limitations above 120m AGL
- Feature ambiguity in homogeneous terrain (fields with repeating patterns)
- Banking maneuvers reduce feature matching reliability
- Older satellite imagery may not capture current terrain state; seasonal variations not captured
- ORB-SLAM2 requires post-processing transforms during Phase I; Phase II requires fully automatic real-time implementation

### Dissemination & Training
- Report indicates quarterly reporting to NOAA
- Results available in post-processing demonstrations and simulations
- Flight test data collected with S2 UAS for ongoing algorithm refinement