# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: Phase I Interim Report
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- Program/Solicitation: NOAA SBIR Phase I (Grant Award Number: NA20OAR0021008)
- Date: April 2020 (Submission); Report covers January 1 – April 30, 2020
- BST Products/Systems Referenced: S1 UAS, S2 UAS, E2 multirotor (simulation), Jetson TX2 (SBC), Gazebo simulation environment
- Key Personnel: Jack Elston (CEO, Project Director/Principal Investigator)

## Executive Summary
This Phase I interim report describes BST's development of a GPS-independent navigation system (Diverse-Source GPS or DS-GPS) to enable Beyond Line-of-Sight (BLOS) UAS operations when GPS is lost, jammed, or spoofed. The system combines a visual-inertial odometry (VIO) solution for high-rate velocity estimation with optical vision-based absolute position corrections, fused via Kalman filtering and delivered in a GPS-like interface. During Phase I, BST developed and flight-tested optical flow algorithms, designed sensor fusion approaches, selected and integrated hardware, conducted HWIL simulations, and began development of vision-based absolute position estimation algorithms.

## Technical Approach

The DS-GPS system comprises four integrated components:

1. **GPS Monitoring**: Detects GPS signal degradation, jamming, or spoofing to trigger failover to the DS-GPS system and alert the operator to initiate safe mission conclusion procedures.

2. **Inertial Estimation via Visual-Inertial Odometry (VIO)**:
   - Uses downward-facing camera and optical flow to estimate ground velocity
   - Fuses optical flow with IMU, airspeed (IAS), and altimeter data
   - Compensates for body rates, yaw, attitude, and altitude variations
   - Provides high-rate (20 Hz) velocity updates with inherent drift over time
   - Position error accumulation: ~50 mm over 100-500 seconds depending on AGL and calibration accuracy

3. **Absolute Position Estimation**:
   - Machine vision algorithms comparing imagery to reference sources (satellite/aerial photos, maps)
   - Evaluation of signals-of-opportunity (TV/cellular tower RF emitters, land-based navigation aids)
   - Three proposed algorithms: Key Frame Following, SLAM, and preprocessing-based approaches
   - Provides periodic unbiased position corrections to remove drift from inertial estimates

4. **Sensor Fusion**:
   - Kalman filter architecture accepting asynchronous measurements from multiple sources
   - Maintains fixed 20 Hz output rate similar to GPS
   - Continues operation during GPS loss without mode switching
   - Generates uncertainty estimates for higher-level planning (e.g., return-home decisions)
   - Wind estimation using air data, updated via inertial velocity or absolute position measurements

## Products & Capabilities Described

### Optical Flow Algorithm
- **What it is**: Sparse Lucas-Kanade optical flow implementation running on Jetson TX2 SBC
- **Performance achieved**: 
  - Processes 1280×720 resolution at 30 FPS
  - Position drift: <50 mm over ~18-100 seconds depending on AGL and camera calibration accuracy
  - Successfully handles homogeneous terrain when operating at sufficient frame rates
- **Key innovations**:
  - Fixed grid pattern for tracking (more robust than adaptive point selection in high-altitude, fast-moving fixed-wing aircraft)
  - Compensation for aircraft body rates, pitch/roll/yaw dynamics
  - AGL-based scene depth correction critical for accurate velocity scaling
  - Camera intrinsic parameter calibration (focal length) required; 10% error translates to 10% velocity error
  - Higher reporting rates of body rate data (30 Hz vs. 3 Hz) significantly improve accuracy

### Visual-Inertial Odometry (VIO) System
- **Configuration**: Jetson TX2 SBC + See3Cam CU135 rolling-shutter camera + laser altimeter + IMU + magnetometer
- **Size/Weight/Power/Cost**: 243g, 9.35W, $975 (machine vision payload only; well under 350g and $6000 target system requirements)
- **Integration**: Deployed on S1 and S2 fixed-wing UAS platforms

### Sensor Fusion / Kalman Filter
- **Architecture**: Dual-rate system with fixed 20 Hz position/velocity output
- **Measurement inputs** (three demonstrated, fourth during GPS-on phase):
  1. Optical flow velocity estimates
  2. Air-data based velocity (true airspeed + magnetometer heading + wind estimate)
  3. Optical-based absolute position estimates
  4. GPS (when available, for bias estimation and system initialization)
- **Wind Estimation Performance**: Successfully estimated 3D wind field during GPS-nominal operation; demonstrated that air-data-only navigation accumulates 100+ mm errors within minutes due to wind variability (strong motivation for vision-based corrections)

### Key Frame Following Algorithm (80% complete at interim report)
- **Concept**: Two-stage system—mapping stage (GPS-on) logs geotagged images as navigation markers; navigation stage (GPS-off) visually matches current imagery to logged key frames to estimate position
- **Status**: Algorithm design and critical component prototyping completed; components benchmarked on embedded target; demonstration on flight data in progress

### SLAM Algorithm Development (50% complete)
- **Status**: Literature review completed; two candidate algorithms selected for prototype demonstration; plan for modifying publicly available codebases developed; not yet implemented on embedded hardware

### Hardware Integration
- **Primary test platform**: S1 (hand-launched, lower endurance, magnetometer available)
- **Alternative platform**: S2 (catapult-launched, higher capability, lacks magnetometer without significant redesign)
- **Camera selection rationale**: Rolling-shutter chosen over global-shutter due to smaller size/cost; confirmed motion distortion negligible at typical BST operating altitudes/velocities

## Use Cases & Applications

- **Beyond Line-of-Sight (BLOS) Operations**: Enables safe continuation of missions beyond radio/visual range when GPS is lost
- **GPS Denial Environments**: Operates in areas with GPS jamming or spoofing
- **Extended Missions**: Allows periodic correction of inertial drift, enabling longer loiter/surveillance missions
- **Automatic Return-Home**: Provides uncertainty estimates for safe landing decisions if alternative landing sites become necessary
- **Grid Mapping Missions**: Flight testing used repeated mapping passes over same terrain; key frame algorithm designed to exploit this pattern for back-reference navigation

## Key Results (Phase I Interim)

### Optical Flow Algorithm Results:
- **HWIL Simulation**: Position estimates accumulated <50 mm error over 500-second flight; agreed well with ground truth
- **First Flight Test (120 m AGL)**:
  - Revealed AGL estimation error (autopilot relied on GPS at high altitudes; laser altimeter only reliable <90 m)
  - Identified body-rate reporting latency (3 Hz insufficient; increased to 30 Hz)
  - Consistent 10% velocity overestimation (attributed to camera focal length calibration error)
  - Position error exceeded 50 mm target in ~15 seconds
  
- **Second Flight Test (120 m and 50 m AGL)**:
  - Lower altitude (50 m AGL) with accurate laser altimeter: position error <50 mm for ~30 seconds; with 10% focal length correction: stable for >100 seconds
  - Higher altitude (120 m): position error exceeded 50 mm in ~30 seconds
  - **Key finding**: With proper AGL, high body-rate updates, and camera calibration, VIO provides stable position estimates for sufficient duration until absolute corrections applied

### Wind Estimation / Air-Data Based Navigation:
- Demonstrated 3D wind estimation accuracy matching GPS truth during GPS-on phase
- Air-data-only navigation showed close agreement with GPS ground truth for short periods but accumulated 100+ mm errors within minutes on high wind-variability segments
- Confirms need for vision-based absolute position corrections to bound long-term position error

### Sensor Fusion Algorithm:
- Kalman filter architecture designed to handle asynchronous multi-rate measurements
- Demonstrated wind field update capability; wind estimate automatically refines as new absolute position or inertial velocity measurements arrive
- No mode-switching required during GPS loss

### Simulation & Testing Infrastructure:
- Developed Gazebo-based HWIL simulation environment with realistic terrain (Potsdam, Germany at 5 cm GSD), variable topography (Cambridge, MA), obstacles (trees, reactor cooling tower)
- Custom image-streaming plugin (H.264 encoding over UDP) enables SBC to process simulated camera feed identically to flight hardware
- Two relevant flight tests conducted at sod farm near Longmont, CO

## Notable Details

1. **COVID-19 Impact**: Planned flight test cadence significantly reduced; compensated with expanded HWIL simulation work and post-processing analysis of existing data

2. **Hardware Choices & Trade-Offs**:
   - Jetson TX2 selected over Jetson Nano for processing power despite higher cost; Nano remains option for Phase II cost reduction
   - Rolling-shutter camera chosen for size/cost; global-shutter rejected as unnecessary for BST altitudes/velocities
   - S1 chosen as primary test platform over S2 despite lower capability, due to easier logistics and availability of magnetometer

3. **Critical Technical Discoveries**:
   - AGL estimation error in BST autopilot (relies on GPS/pressure at altitude; laser-only below 90 m) was primary optical flow performance limiter
   - High-rate (30+ Hz) body-rate data transmission essential; 3 Hz reporting from autopilot caused unacceptable velocity errors
   - Camera intrinsic calibration critical; manufacturer datasheet focal length insufficient
   - Pixel disparity requirements drove camera selection: 1280×720 @ 30 FPS chosen as optimal balance

4. **Phase II Roadmap**:
   - Full integration of vision-based absolute position algorithms (key frame following, SLAM) on embedded hardware
   - Flight testing of complete fused system
   - GPU-accelerated algorithm implementation on Jetson for improved throughput
   - Evaluation of signals-of-opportunity navigation feasibility
   - GPS spoofing detection and response mechanism design/testing

5. **Project Team & Organization**:
   - Lead: Jack Elston (CEO)
   - Leveraged internal R&D efforts and related NOAA SBIR for mechanical integration, simulation tools, and flight test infrastructure
   - Demonstrated rapid prototyping and iteration cycle (algorithm → HWIL → flight test → refinement)

6. **Performance Targets** (Phase II goal):
   - Unit cost: <$6,000
   - Weight: <350 g
   - Position accuracy: 50 mm RMS without GPS
   - GPS-like serial interface for avionics compatibility
   - 20 Hz output update rate