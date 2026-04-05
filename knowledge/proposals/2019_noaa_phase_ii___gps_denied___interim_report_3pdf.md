# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: SBIR Phase II Interim Report
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- Program/Solicitation: NOAA SBIR Phase II; Federal Grant Award Number: NA20OAR0210087
- Date: April 2022 (Submission); Reporting Period: November 1, 2021 – October 30, 2022
- BST Products/Systems Referenced: S2 (quadrotor), DepthAI stereo cameras (OAK-D, OAK-FFC-3P), Intel Myriad-X processor, Jetson Nano SBC, BladeRF 2.0 Micro xA5 SDR, Ettus E310 SDR
- Key Personnel: Jack Elston (CEO/Project Director/Principal Investigator)

## Executive Summary
Black Swift Technologies is developing a diverse-source global positioning system (DS-GPS) to enable beyond-line-of-sight (BLOS) UAS operations in GPS-denied environments. The system combines vision-based navigation (inertial estimation with optical flow, SLAM, and depth estimation using neural networks) with signals of opportunity (LTE timing advance ranging). Phase II focuses on implementing hardware, training neural networks on aircraft-perspective imagery, and investigating LTE-based ranging techniques to provide position solutions accurate to 50m RMS without GPS.

## Technical Approach

### Overall Architecture
The DS-GPS system has four key components:
1. **GPS Monitoring**: Detect GPS spoofing/jamming to trigger alternative navigation modes
2. **Inertial Estimation**: Fuse optical flow with IMU and airdata to maintain position in absence of absolute references
3. **Absolute Position Estimation**: Periodic position updates via machine vision (SLAM) and signals of opportunity
4. **Sensor Fusion**: Kalman filter-based fusion combining all measurement sources to produce position estimate with error bounds

### Vision System (Primary Approach)
The vision system architecture consists of several integrated components:

**RGB-D Sensing & Depth Estimation**
- Stereo camera hardware: Intel OAK-D (7.5cm baseline) and OAK-FFC-3P (adjustable 7.5-24cm baseline)
- Hybrid depth estimation: comparison between onboard DepthAI stereo disparity generation and neural-network-assisted depth (HITNET Hierarchical Iterative Tile Refinement Network)
- Key finding: HITNET neural network achieves accurate depth to 20m+ with 7.5cm baseline; onboard disparity degrades significantly beyond 10m
- 24cm baseline improves onboard disparity but introduces pitch-dependent errors at altitude, corrected through inertial fusion
- Payload designed for <350g weight; mounted on BST E2 quadrotor

**Visual Odometry (VO) / Optical Flow**
- Uses stereo image pairs from downward-facing camera to estimate aircraft motion between frames
- Neural-network-assisted optical flow to improve accuracy
- Fused with IMU (gyroscope, accelerometer) and laser altimeter for attitude correction and range correction
- Provides high-rate (20Hz) velocity estimates for sensor fusion

**Simultaneous Localization and Mapping (SLAM)**
- Two primary approaches evaluated:
  - **ORB-SLAM3**: Stereo-inertial mode (camera + IMU integration) with global bundle adjustment; more memory-intensive but more precise; includes loop closure for map revisit detection
  - **RTABMap**: Modular, open-source; Frame-to-Map (F2M) odometry with support for various visual-inertial odometry backends (OKVIS, MSCKF-VIO, VINS-Fusion); lower memory footprint; faster real-time performance than ORB-SLAM3
- Both operate in RGB-D mode, ingesting stereo or neural-network-generated depth maps
- Produces sparse or dense 3D point clouds and camera trajectory tracking
- Implementation on NVIDIA Jetson Nano SBC for embedded processing

**Neural Network Training Pipeline**
- **Challenge**: Lack of publicly available training data from aircraft downward perspective; most datasets from car-mounted cameras
- **Solution**: Leverage BST's large repository of survey-grade photogrammetry maps (up to 3000+ acres per map) to synthetically generate training data
- Use Blender to manipulate 3D models and simulate realistic stereo camera captures
- Data augmentation techniques: Gaussian noise, geometric transforms, gamma correction, color shifts
- Training framework: TensorFlow/TFLite for optimization and onboard inference
- Fine-tuning on outlier scenarios where depth networks fail

**Visual Challenges & Mitigation**
- Homogeneous terrain (snow, water) causes poor feature tracking; addressed with linear polarized camera filters to reduce sun reflection
- Dynamic objects (waves, vehicles) degrade SLAM performance
- Night/poor weather renders optical SLAM unusable (addressed via signals of opportunity fallback)
- Changing illumination affects loop closure detection if areas revisited after many hours

**Calibration**
- Stereo camera calibration using Charuco boards and April tags to ensure proper rectification
- Visual-inertial calibration using Kalibr toolbox to compute spatial/temporal alignment between camera and autopilot IMU
- Intrinsics, extrinsics, and synchronized timestamps critical for stereo-inertial SLAM performance

### Signals of Opportunity (Secondary Approach)
**LTE-Based Ranging**

*Background & Protocol*
- LTE frame structure: 10ms frames divided into 10 sub-frames (1ms each), each containing 2 slots of 6-7 OFDM symbols
- Primary/Secondary Synchronization Signals (PSS/SSS) and Cell-specific Reference Signal (CRS) used for ranging
- Network architecture: eNodeBs broadcast downlink signals; each eNodeB can broadcast multiple "cells" with unique Physical Cell IDs (PCIs)
- LTE stack layers: PHY (physical layer), MAC, RLC, PDCP (Layer 2), RRC, NAS (Layer 3)
- UE states: RRC_Idle and RRC_Connected

*Ranging Methodology*
- **Initial approach** (abandoned): Channel Impulse Response (CIR) based; too complex to implement within project timeline
- **Adopted approach**: Timing Advance (TA) based ranging
  - When UE initiates Random Access Channel (RACH) to connect to cell tower, eNodeB responds with Random Access Response (RAR) containing timing advance value
  - Timing advance reflects propagation delay between UE and eNodeB; directly correlates to pseudorange = propagation_delay × speed_of_light
  - Feasibility established in simulation with average 43m error
  - Advantage: Accessible without designing full LTE receiver

*Hardware Selection*
- **Initial platform**: Ettus Research E310 (embedded SDR with SoC + FPGA; 375g, 133×68×26.7mm form factor)
  - Advantages: All-in-one device; potential for streamlined future production
  - Disadvantages: Cost ($4500), inflexible, difficult to upgrade if more channels needed
- **Selected platform**: Nuand BladeRF Micro 2.0 xA5 (peripheral SDR; lower cost, flexibility, smaller)
  - Issue encountered: Unable to synchronize with real cell tower signals; simulated tower worked; under investigation

*Software Implementation*
- Evaluated multiple LTE libraries: settled on srsRAN (specifically srsUE component)
- Developed software to repeatedly transmit RACH message and extract timing advance replies
- Integration with autopilot systems for navigation

### Sensor Fusion Architecture
- Kalman filter-based algorithm to combine multiple measurement sources:
  - High-rate (20Hz) velocity from optical flow + IMU
  - Low-rate (infrequent) absolute position from SLAM loop closure, LTE timing advance, or other sources
  - Produces fused position estimate + error covariance for mission planning
- Generalized formulation accommodates any number of measurement sources at varying update rates

## Products & Capabilities Described

### DS-GPS Navigation Module
**Specifications (Phase II Target)**
- **Form factor**: Single hardware package designed as GPS replacement (serial interface with GPS-like data output)
- **Weight**: <350g
- **Cost**: <$6,000 per unit
- **Position accuracy**: 50m RMS error without GPS
- **Update rate**: 20Hz position estimates
- **Interface**: Serial port compatible with standard avionics

**Components**
1. Vision system: Stereo camera (OAK-D or OAK-FFC-3P) + DepthAI + Jetson Nano SBC + optional hardware (polarized filters, laser altimeter)
2. Signals of opportunity receiver: BladeRF 2.0 or E310 SDR + antenna
3. Sensor fusion processor: Embedded implementation of Kalman filter

### Intel OAK Stereo Cameras
- **OAK-D**: Fixed 7.5cm baseline; integrated depth processor (Myriad-X); limited to ~10m accurate depth without neural enhancement
- **OAK-FFC-3P**: Modular design (left, right, RGB + breakout board); adjustable baseline (tested 7.5cm, 24cm); allows depth range optimization; better performance with neural networks

### Neural Network Models
- **HITNET**: Hierarchical stereo depth estimation; outperforms onboard disparity; achieves 20m+ depth range with small baselines
- **Optical flow networks**: Neural-assisted to improve motion estimation accuracy
- Optimizable with OpenVINO toolkit for on-device inference

### Software Platforms
- **ORB-SLAM3**: Visual-inertial SLAM with global optimization; memory-intensive but precise
- **RTABMap**: Modular SLAM with pluggable odometry (ORB, VINS-Fusion, OKVIS); lower memory, faster real-time
- **srsRAN**: LTE stack for prototyping ranging receiver
- **ROS** (Robot Operating System): Integration framework for components

## Use Cases & Applications

### Primary Use Case: BLOS Operations in National Airspace System (NAS)
- Enable UAS beyond-visual-line-of-sight under FAA UAS Traffic Management (UTM) system
- FAA BLOS requirements: accurate navigation, communications, collision avoidance, FAA real-time connectivity
- Addresses GPS denial (jamming, spoofing, multipath in urban canyons, high latitudes/altitudes)

### Operational Scenarios
1. **Urban/GPS-Denied Areas**: Navigation using vision-based SLAM without GPS
2. **Night/Adverse Weather**: Fallback to LTE-based signals of opportunity
3. **Emergency Landing**: Inertial estimation + vision/signals maintain position during GPS loss
4. **Extended Operations**: SLAM loop closure enables multi-hour missions in mapped areas

### Environmental Challenges
- Homogeneous terrain (snow, water, desert): mitigated with optical filtering and inertial fusion
- Dynamic scenes (traffic, waves): avoided via flight planning
- Poor visibility (night, fog): LTE signals of opportunity primary navigation source
- High-altitude/high-latitude: vision + inertial + LTE hybrid approach

## Key Results (Phase II Progress through October 2022)

### Vision System Progress
1. **Dense Training Data Generation** (75% complete)
   - Successfully developed Blender-based photogrammetry 3D map manipulation pipeline
   - Automated Python scripts for data augmentation (Gaussian noise, geometric transforms, gamma, color shifts)
   - Realistic stereo camera simulation in headless mode

2. **Depth Estimation Validation**
   - Quantitative comparison: HITNET neural network achieves accurate depth to 20m+ with 7.5cm baseline (where onboard disparity fails >10m)
   - 24cm baseline improves onboard disparity but introduces altitude-dependent pitch errors
   - Neural networks outperform traditional stereo disparity on BST flight data
   - 3D visualization tools developed to identify and filter inaccurate disparity pixels

3. **SLAM Implementation** (70% complete)
   - ORB-SLAM3 successfully integrated with DepthAI stereo camera + autopilot IMU in ROS
   - RTABMap implemented with F2M odometry and VIO algorithm fusion (OKVIS, MSCKF-VIO, VINS-Fusion)
   - Visual-inertial calibration pipeline using Kalibr toolbox completed
   - Both