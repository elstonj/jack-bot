# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- **Type**: SBIR Phase II Proposal
- **Client/Agency**: National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- **Program/Solicitation**: NOAA SBIR Phase II; Advanced UAS Observing Platforms (9.5.01); Federal Grant Award Number: NOAA-OAR-OAR-TPO-2020-2006595
- **Date**: Submitted October 14, 2020
- **Period of Performance**: April 1, 2021 – March 31, 2023
- **BST Products/Systems Referenced**: S1 UAS, S2 UAS, E2 multirotor, SwiftPilot autopilot, SwiftCore flight management system
- **Key Personnel**: 
  - Dr. Jack S. Elston (CEO, Principal Investigator)
  - Dr. Maciej Stachura (Lead Engineer)
  - Josh Fromm (Aircraft Design and Integration)
- **Funding Requested**: $395,730.81

## Executive Summary
Black Swift Technologies proposes to develop a Diverse-Source Global Positioning System (DS-GPS) that enables Beyond-Line-of-Sight (BLOS) UAS operations in GPS-denied environments through an augmented sensor suite combining visual odometry, simultaneous localization and mapping (SLAM), signals of opportunity, and machine learning. This system addresses critical FAA/UTM requirements for safe autonomous navigation when GPS is jammed, spoofed, or unavailable, providing accurate localization to within 50m RMS error while maintaining sub-$2,000 unit cost and 350g weight envelope.

## Technical Approach

### Core System Architecture
The DS-GPS system integrates multiple sensor sources and processing algorithms:

1. **GPS Monitoring & Spoofing Detection**: Monitors for GPS jamming and spoofing via AGC (automatic gain control) levels and correlator metrics; evaluates uBlox receiver's built-in spoofing detection capabilities
2. **Visual Odometry (Optical Flow)**: High-rate (20+ Hz) inertial velocity estimation using neural-assisted optical flow with volumetric correspondence networks (VCN) trained on synthetic datasets
3. **Absolute Positioning (SLAM)**: ORB-SLAM3 with RGB-D depth maps from neural-assisted stereo (Intel Myriad X / DepthAI hardware) providing periodic position corrections
4. **Signals of Opportunity**: Software-defined radio (SDR) receivers to extract navigation signals from cellular (GSM/LTE), TV (ATSC/DVB), and AM/FM radio towers via time-of-arrival (ToA), time-difference-of-arrival (TDoA), and power-based ranging
5. **Sensor Fusion**: Kalman filter architecture combining high-rate velocity estimates with lower-rate absolute position measurements and signals of opportunity to produce 20Hz position estimates with uncertainty bounds

### Phase II Technical Objectives

**1. GPS Monitoring**
- Implement jamming/spoofing detection on GPS receiver using AGC threshold monitoring
- Test with uBlox receiver (same as SwiftPilot autopilot) to validate spoofing flag capability
- Create hardware to inject spoofed/jammed signals for characterization and validation testing

**2. Dense Training Data Generation**
- Leverage BST's repository of survey-grade photogrammetry maps (3000+ acre areas) at 5 cm ground sample distance (GSD)
- Create synthetic training datasets via Gazebo simulation with realistic camera and sensor models
- Generate hundreds of hours of labeled video with per-pixel 3D positions and ground truth trajectories
- Extend method to stereo pairs for depth map training data

**3. Visual Odometry Enhancement**
- Implement volumetric correspondence networks (VCN) for optical flow using Phase II training data
- Improve depth estimation to handle terrain elevation variation and wide field-of-view effects (Phase I showed 20m altitude variations within field of view at 120m AGL caused errors)
- Maintain ≥20 Hz velocity update rate on embedded hardware
- Target: improved accuracy over Phase I classical optical flow approach

**4. SLAM Refinement**
- Migrate from ORB-SLAM2 to ORB-SLAM3 with RGB-D capability
- Add per-pixel depth from neural-assisted stereo cameras (DepthAI/Luxonis hardware with Intel Myriad X chipset)
- Phase I results with depth showed ~4x error reduction; Phase II target: ≤50m RMS position error

**5. Signals of Opportunity Development**
- Evaluate GSM, LTE, ATSC (US), DVB (Europe), AM/FM radio for navigation signals
- Develop real-time SDR-based receivers for cellular/TV signals using Time-of-Arrival (ToA) and Time-Difference-of-Arrival (TDoA) techniques
- Address scenarios where vision fails (night, fog, homogenous terrain like snow/water)
- Hardware candidates: Ettus boards (56 MHz BW), HackRF One (20 MHz BW), RTL-SDR ($24.95, receive-only), LimeSDR-Mini (61 MHz BW)
- ATSC simulation showed 50m position accuracy possible via TDoA; GSM/LTE studies demonstrated 5m and 3m accuracy respectively in post-processing

**6. Sensor Fusion**
- Complete generalized Kalman filter formulation accepting position/velocity from any number of sources at varying update rates
- Produce position estimates with associated uncertainty bounds for mission planning tools

## Products & Capabilities Described

### DS-GPS System (Proposed Product)
- **Purpose**: Standalone GPS-independent positioning for BLOS UAS operations in GPS-denied environments
- **Form Factor**: Affordable standalone package (<$2,000 per unit, <350g) outputting GPS-like serial interface for integration with commercial UAS and autopilots
- **Accuracy Target**: 50m RMS error without GPS
- **Update Rate**: 20 Hz position fixes with velocity updates
- **Key Features**:
  - GPS jamming/spoofing detection via AGC monitoring and receiver spoofing flags
  - Multi-source sensor fusion (vision, inertial, RF signals)
  - Uncertainty estimation for mission planning
  - Compatible with BST and third-party aircraft/autopilots

### Hardware Integration
- **Flight Computer**: Jetson TX2 SBC (Phase I proven on S1 and S2 aircraft)
- **Depth Sensing**: DepthAI board (Intel Myriad X chipset) for neural-assisted stereo
- **SDR Options**: Ettus boards, HackRF One, LimeSDR-Mini, RTL-SDR for signals of opportunity
- **GPS Receiver**: uBlox unit with spoofing detection capability (matches SwiftCore autopilot receiver)

### Simulation Infrastructure
- **Gazebo Simulation Environment**: BST E2 multirotor model with simulated downward camera, laser altimeter, and photogrammetry-textured terrain
- **Hardware-in-the-Loop (HWIL)**: UDP video streaming from simulation to actual machine vision hardware; serial interface for autopilot simulation
- **Training Data Pipeline**: Automated generation of labeled video from photogrammetry maps

## Use Cases & Applications

### Primary Market
- Government and commercial users requiring extended-range UAS operations
- Applications currently under-utilized due to GPS dependence or regulatory constraints

### Specific Mission Applications Mentioned
- **Coastal monitoring**: Requires reliable positioning over water (homogenous terrain challenge)
- **Power line and pipeline inspection**: Long-distance operation capability
- **Package delivery**: BLOS commercial operations
- **High-latitude operations**: Poor GPS performance
- **Urban canyons**: GPS signal blockage
- **Weather operations**: Fog/inclement weather environments where vision fails
- **Night operations**: Where vision-only approaches fail, signals of opportunity provide backup
- **GPS-jammed/spoofed environments**: Military/defense applications with anti-drone systems

## Key Phase I Results

### Optical Flow Algorithm
- Implemented on Jetson TX2 at 27 fps
- Flight tested on S1/S2 UAS in multiple environments and terrain types
- Demonstrated sufficient accuracy for Phase II incorporation
- HWIL simulation validated importance of body rate corrections

### Vision-Based Absolute Positioning
- **ORB-SLAM2 Algorithm**: Tested on Phase I flight data
  - Maintained <50m error in most flights when combined with flat-earth corrections
  - Performance stable across different flights and terrain types
- **Alternative Methods Evaluated**:
  - Key-frame matching: Saves navigation marker images with GPS coordinates for later matching
  - Road-following: Semantic segmentation networks trained to isolate roads for database matching
  - Shoreline-following: Coastline detection and resampling to pre-loaded maps

### GPS Spoofing Detection Plan
- Determined commercial solutions (uBlox spoofing flag) likely sufficient
- Selected AGC monitoring as primary jamming detection approach
- Evaluated Novatel G-III methodology; opted for cost/complexity reduction with standard receivers

### Signals of Opportunity Assessment
- Surveyed GSM, LTE, ATSC, DVB, AM/FM radio signals
- Reviewed navigation accuracy claims from literature:
  - GSM: ~5m accuracy (post-processing, mapping receiver required)
  - LTE: ~3m accuracy (post-processing, requires ~4 towers, assumes GPS initialization)
  - ATSC: ~50m accuracy (simulation, single-receiver architecture feasible)
  - DVB: ~40m accuracy (limited US coverage)

## Phase II Work Plan Timeline

1. **Preliminary Tasks**: System setup and preparation
2. **GPS Monitoring**: Receiver evaluation, spoofing/jamming injection testing, characterization
3. **Vision System**: Dense training data generation, VCN optical flow implementation, SLAM refinement with depth
4. **Signals of Opportunity**: Hardware procurement, algorithm development, validation with real flight data
5. **Sensor Fusion**: Complete Kalman filter formulation and uncertainty propagation
6. **Flight Testing**: Continuous validation throughout Phase II
7. **System Specification**: Final commercialization requirements documentation

## Notable Details

### Competitive Advantages & Technical Innovations
- **Synthetic Training Data Generation**: Novel approach leveraging BST's photogrammetry repository to create hundreds of hours of labeled video without expensive manual data collection
- **Hardware-in-the-Loop Simulation**: Proven methodology (Phase I) enabling algorithm testing on actual embedded hardware before flight testing
- **Integrated Multi-Source Approach**: Combining vision, inertial, RF, and GPS creates redundancy that's difficult to jam comprehensively
- **Gazebo Integration**: Custom UDP video streaming interface allows seamless transition between simulation and flight hardware
- **ORB-SLAM3 + Depth**: Phase I internal experiments showed ~4x error reduction with depth; Phase II focus on neural-assisted depth generation

### Risk Mitigation
- **Retired Phase I High-Risk Items**: GPS spoofing/jamming detection feasibility, vision-based velocity estimation accuracy, absolute positioning accuracy, sensor fusion methodology
- **Design Philosophy**: Focus on commercial-grade solutions (uBlox receivers, Jetson/Myriad X processors) rather than military-spec components to keep costs under $2,000

### Regulatory & Safety Context
- **UTM Compliance**: System designed to meet UAS Traffic Management (UTM) rules requiring near-real-time position reporting to FAA
- **Critical Safety Function**: Aircraft position information essential for collision avoidance and ground risk assessment
- **Grounded in FAA Experience**: BST identified these requirements through past FAA case-by-case BLOS authorizations

### Related BST Development
- Parallel BST efforts in predictive maintenance (machine learning for health monitoring) and autonomous safe landing
- Leverages existing **SwiftPilot autopilot** and **SwiftCore flight management system** components
- Designed for integration with both BST-manufactured and third-party commercial UAS

### Commercial Viability
- **Target Unit Price**: <$2,000 (reduced from Phase I estimate of $6,000 through machine vision hardware cost reductions)
- **Weight**: <350g (suitable for small UAS integration)
- **Interface**: GPS-like serial output allows plug-and-play integration without firmware/driver modifications
- **Market Timing**: Expected acceleration in commercial UAS adoption directly tied to expanded BLOS capabilities; DS-GPS addresses critical barrier to this expansion

### Facilities & Equipment
- BST flight test infrastructure and S1/S2 UAS
- Gazebo simulation environment with photogrammetry terrain rendering
- Large archive of survey-grade photogrammetry maps (5 cm GSD) for training data