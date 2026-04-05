# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- **Type:** NOAA SBIR Phase II Interim Report
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- **Program/Solicitation:** SBIR Phase II; Federal Grant Award Number NA20OAR0210087
- **Date:** October 2022 (Submission); Covering April 30, 2022 – October 30, 2022
- **Project Period:** May 1, 2021 – April 30, 2023
- **BST Products/Systems Referenced:** Black Swift E2 quadrotor, DepthAI stereo cameras (OAK-D, OAK-FFC-3P), SwiftCore payload integration
- **Key Personnel:** Jack Elston (CEO, Project Director/PI), Nick Juarez, Dan Dole-Muinos, Maciej Stachura; Technical Monitor: Phil Hall (NOAA OAR)

## Executive Summary
Black Swift Technologies is developing a GPS-denied navigation system (Diverse-Source GPS or DS-GPS) to enable beyond line-of-sight (BLOS) UAS operations in the National Airspace System. The Phase II interim report documents progress on a multi-sensor fusion approach combining stereo vision, inertial measurement units, and signals of opportunity to provide continuous positioning at ≤50m RMS error without GPS, in a standalone package under 350g and costing below $6,000 per unit.

## Technical Approach

### Overall System Architecture
The DS-GPS system comprises four integrated components:

1. **GPS Monitoring:** Detects GPS spoofing/jamming to trigger autonomous fallback to vision-based navigation; alerts aircraft and operator to initiate safe mission termination procedures.

2. **Inertial Estimation:** Fuses optical flow from stereo vision with on-board IMU and air-data sensors to compensate for rapid drift caused by atmospheric wind; addresses inadequacy of standard MEMS-based INS on commercial UAS.

3. **Absolute Position Estimation:** Combines machine vision (depth estimation, visual SLAM), neural network-assisted odometry, and signals of opportunity (LTE timing advance from cellular towers, RF emitters like TV/cellular towers) to periodically provide unbiased position fixes.

4. **Sensor Fusion:** Generalized Kalman filter-based architecture ingesting position and velocity estimates from multiple sources (frequent or infrequent) to produce fused position output with accuracy bounds for mission planning.

### Vision System (Primary Technical Focus of Phase II)

**Stereo Depth Estimation:**
- Tested Intel OAK-D (fixed 7.5cm baseline) and OAK-FFC-3P (modular, adjustable baseline up to 24cm)
- Baseline adjustment extends depth detection range: 7.5cm baseline limited to ~10m; 24cm baseline extends to ~30+m
- Classical stereo disparity processing generates on-board depth maps via Myriad-X processor
- Neural-assisted depth estimation using HITNET and CREStereo models outperforms classical stereo, maintaining accuracy beyond 20m even with short baselines

**Training Data Generation:**
- Leveraged BST's extensive photogrammetry repository (survey-grade maps up to 3000+ acres) to simulate realistic stereo camera data
- Automated pipeline using Blender for 3D map manipulation and synthetic data generation
- Augmentation techniques applied: Gaussian noise, geometrical transforms, gamma/color adjustments
- Addresses critical lack of publicly available top-down aerial training datasets (most data is from ground vehicles)

**Calibration:**
- Comprehensive stereo-inertial calibration using Kalibr toolbox to compute:
  - Homogeneous transformation matrices between camera and IMU frames
  - Camera intrinsics/extrinsics, IMU noise coefficients (accelerometer, gyroscope)
  - Camera-IMU temporal synchronization offset
- Achieved sub-pixel reprojection errors (<1 pixel) for high-quality rectification
- Critical for accurate disparity/depth maps, especially with adjusted baselines

**SLAM/Visual-Inertial Odometry Approaches Evaluated:**

1. **ORB-SLAM3:** Upgraded from Phase I (monocular-only) to stereo-inertial mode; reuses all historical information for loop closure; global bundle adjustment for high precision but computationally intensive; high memory footprint constrains embedded deployment on Jetson Nano.

2. **RTABMap:** Modular architecture enables fusion of multiple odometry sources (ORB-SLAM, OKVIS, MSCKF-VIO, VINS-Fusion); Frame-to-Map (F2M) default approach faster than global optimization; supports RGB-D mode for dense point clouds; successfully ported to Jetson Nano for flight testing.

3. **HybVIO:** Novel hybrid filtering-based VIO + optimization-based SLAM; demonstrates consistent absolute position estimation with lower computational burden; robust IMU bias modeling and outlier rejection; outperforms ORB-SLAM/RTABMap in speed; selected for embedded deployment.

**RGB-D Sensing & Depth-aided SLAM:**
- Fusion of dense depth maps (from stereo) with RGB imagery significantly improves SLAM robustness vs. monocular approaches
- Adding depth information enables loop closure detection and localization refinement using color mapping
- Phase I simulation confirmed depth-aided SLAM produces more accurate, stable trajectories than RGB-only

### Signals of Opportunity
- **LTE-based Ranging:** Discovered viable technique using LTE timing advance (TA) from cellular towers to calculate pseudorange; BladeRF 2.0 micro xA5 software-defined radio (SDR) selected for signal processing
- RACH (Random Access Channel) message transmission capability implemented
- Hardware selection complete; synchronization to real towers under investigation (simulated tower testing successful)
- Potential to enable navigation at night/in low-visibility weather

### Sensor Fusion Algorithm
- Generalized Kalman filter formulation accepting heterogeneous measurements (frequent stereo odometry, infrequent SLAM loop closures, sporadic signals of opportunity)
- Outputs fused position estimate + uncertainty bounds for downstream mission planning
- Phase I demonstrated feasibility; Phase II focused on completing general formulation and validation with real flight data

## Products & Capabilities Described

### DS-GPS Module
- **Function:** Standalone navigation system replacing GPS for BLOS operations
- **Form Factor:** Single hardware package with serial interface compatible with standard GPS avionics interfaces
- **Target Specifications (End of Phase II):**
  - Position accuracy: ≤50m RMS error without GPS
  - Weight: <350g
  - Cost per unit: <$6,000
  - Operating envelope: Mountable on various BST aircraft
  - 20Hz position estimate update rate

### Hardware Components
- **Stereo Camera Payload:** OAK-FFC-3P breakout cameras (Left/Right/RGB) + Myriad-X computing board + NVIDIA Jetson SBC (host processing)
- **Sensors:** On-board IMU (from stereo cameras), laser altimeter, autopilot air-data
- **Optional:** BladeRF 2.0 micro xA5 SDR for signals-of-opportunity processing

### Software Stack
- **Vision Processing:** DepthAI framework, CREStereo/HITNET neural networks (depth estimation), optical flow algorithms
- **SLAM/VIO:** ORB-SLAM3, RTABMap, HybVIO (ROS and standalone implementations)
- **Calibration:** Kalibr toolbox
- **Fusion:** Generalized Kalman filter with multi-source ingestion
- **ML Training:** TensorFlow, OpenVINO toolkit (neural network optimization for embedded inference)
- **Analysis:** Neptune framework (ML metrics tracking)

## Use Cases & Applications

1. **Beyond Visual Line-of-Sight (BVLOS) Operations:** Enable FAA UTM system compliance for remote UAS operations without continuous line-of-sight
2. **GPS-Denied Environments:** Urban canyons, high-latitude regions, high-altitude operations, underground/indoor navigation
3. **Anti-Jamming/Spoofing:** Autonomous fallback when GPS signal is compromised; continue mission or execute safe abort
4. **Emergency/Autonomous Landing:** Safe landing capability without GPS in failure scenarios
5. **Pipeline Inspection:** Long-range monitoring of energy infrastructure in remote areas
6. **Drone Delivery:** Safe autonomous delivery in GPS-vulnerable areas
7. **Environmental Monitoring:** Remote environmental data collection requiring reliable long-duration missions

## Key Results (Interim Report - April to October 2022)

### Completed/Near-Complete Milestones
1. **Dense Training Data Generation:** 80% complete; Blender-based photogrammetry simulation pipeline operational; augmentation scripts finalized; ready for neural network fine-tuning
2. **RGB-D Sensing:** Comparative testing of classical stereo (DepthAI) vs. neural-assisted (HITNET) depth estimation completed on flight data
   - HITNET maintains accuracy to 20m+ even with 7.5cm baseline (classical stereo degraded >10m)
   - 24cm baseline extends classical stereo performance to 30m+
3. **Stereo-Inertial Calibration:** Completed using Kalibr; transformation matrices, noise coefficients, and synchronization parameters extracted for all SLAM/VIO algorithms
4. **SLAM Implementation:** 
   - ORB-SLAM3 stereo-inertial mode successfully integrated
   - RTABMap ported to Jetson Nano; RGB-D mode tested
   - HybVIO implemented as standalone and in-progress ROS integration
5. **Optical Flow:** 85% complete; real-time performance evaluated on prerecorded flight data
6. **Vision System Payload:** Designed and integrated OAK-FFC-3P + Jetson + Myriad-X; modular design allows mounting on multiple BST platforms; weight tracking <350g target

### In-Progress/Partial Completion
1. **GPS Monitoring:** 90% complete; firmware modification for spoofing/jamming detection on hold pending integration testing with full DS-GPS system
2. **Signals of Opportunity (LTE):** 50% complete; timing advance pseudorange algorithm validated; SDR hardware selected; real tower synchronization issues under investigation
3. **Sensor Fusion:** 20% complete; headless data gathering pipeline established; standalone USRP E310 testing initiated; full multi-source fusion formulation pending SLAM/VIO finalization
4. **Training & Tuning of Neural Networks:** On hold until real-time SLAM/VIO performance baseline established for identifying failure modes to target with fine-tuning datasets

### Key Technical Findings
- Neural-assisted stereo depth estimation (HITNET, CREStereo) significantly outperforms classical stereo matching for this application, extending range and reducing noise
- Stereo-inertial SLAM dramatically improves robustness over monocular approaches; loop closure detection critical for long-duration missions
- HybVIO shows superior speed and embedded resource efficiency vs. ORB-SLAM3/RTABMap without sacrificing accuracy
- Baseline adjustment (stereo rig modification) directly extends effective depth range; 24cm baseline achieves ~30m+ detection vs. ~10m with fixed 7.5cm
- Calibration quality (reprojection error <1 pixel) essential for reliable depth and SLAM performance

### Project Status
- **Overall Completion:** ~75% of Phase II work completed as of October 2022
- **Budget Status:** On budget; $296,668.29 cumulative costs through October 2022
- **Timeline:** Project period extends to April 30, 2023; first article flight testing planned by final date
- **Risks/Challenges:** No significant delays reported; SLAM/VIO real-time performance optimization ongoing

## Notable Details

### Competitive/Unique Advantages
1. **Proprietary Photogrammetry Repository:** BST's extensive survey-grade aerial map collection enables rapid synthetic training data generation without expensive field campaigns—major accelerator for deep learning model development
2. **Top-Down View Specialization:** Training datasets explicitly tailored to overhead aircraft perspective (not generic car-driving datasets), improving network generalization to actual mission profile
3. **Modular Hardware Design:** OAK-FFC-3P with adjustable baseline allows field reconfiguration for mission-specific depth ranges without redesign
4. **Multi-Algorithm Evaluation:** Systematic benchmarking of ORB-SLAM3, RTABMap, HybVIO provides flexibility to select best performer for target embedded platform constraints