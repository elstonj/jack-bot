# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: SBIR Phase II Proposal
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- Program/Solicitation: NOAA SBIR Phase II; Topic 9.5.01 (Advanced UAS Observing Platforms); Grant Award Number NOAA-OAR-OAR-TPO-2020-200659
- Date: Submitted October 14, 2020
- BST Products/Systems Referenced: S1 UAS, S2 UAS, E2 multirotor, SwiftCore flight management system, SwiftPilot autopilot
- Key Personnel: Dr. Jack S. Elston (CEO, Principal Investigator), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposes to develop a Diverse-Source Global Positioning System (DS-GPS) that enables Beyond Line-of-Sight (BLOS) UAS operations in GPS-denied environments through sensor fusion combining visual odometry, SLAM, and signals of opportunity. The system will provide accurate position information (50m RMS error target) without GPS, maintaining continuous localization during GPS jamming, spoofing, or hardware failure to satisfy UAS Traffic Management (UTM) safety requirements. The commercial product will be a standalone unit costing under $2,000, weighing under 350g, with GPS-like serial output compatible with existing avionics.

## Technical Approach

### Core System Architecture
DS-GPS augments a standard GPS receiver with additional sensing to detect GPS degradation and provide alternative positioning sources. The system architecture (Figure 1) includes:
- GPS receiver with spoofing/jamming detection capability
- Downward-facing machine vision camera
- Inertial measurement unit (IMU) with pressure sensors
- Software-defined radio (SDR) for signals of opportunity
- Embedded processing (Jetson TX2 / DepthAI board)
- Kalman filter-based sensor fusion providing 20Hz position updates

### Technical Components

**1. GPS Monitoring**
- Implements Automatic Gain Control (AGC) and correlator peak analysis for detecting GPS interference
- Uses uBlox receiver with native spoofing/jamming detection flags to reduce cost/complexity
- Will characterize on-board detection system through controlled jamming/spoofing simulation
- Comparison planned against higher-end Novatel receivers referenced in literature

**2. Visual Odometry (Optical Flow)**
- Phase I successfully demonstrated optical flow algorithm running at 27 fps on Jetson TX2
- Phase II will upgrade to volumetric correspondence networks (VCN) neural-assisted optical flow using dense training data
- Algorithm steps: sparse flow tracking → optical flow computation → body rate compensation → AGL scaling → velocity estimation via magnetometer fusion
- Target: ≥20Hz velocity update rate (matching commercial GPS units)
- Phase I achieved good velocity estimation compared to GPS truth; Phase II aims to improve altitude error (Phase I showed degradation at higher AGL due to flat-earth assumption)

**3. Simultaneous Localization and Mapping (SLAM)**
- Phase I successfully tested ORB-SLAM2 (monocular) and RTAB-Map
- Phase II will upgrade to ORB-SLAM3 with RGB-D (depth per pixel)
- Leveraging Intel Myriad X DepthAI hardware for neural-assisted stereo depth generation
- Phase I results showed ~4x error reduction when depth added to RGB images
- Target: ≤50m position error bound
- Algorithm tested on multiple flights with terrain variations up to 20m within field of view

**4. Signals of Opportunity**
- Surveyed multiple RF signal sources for navigation: GSM, LTE, AM/FM radio, ATSC TV (US), DVB TV (Europe)
- Feasible navigation solutions through Time-of-Arrival (ToA) multilateration:
  - GSM: 5m position accuracy possible (post-processing)
  - LTE: 3m accuracy possible
  - ATSC TV: 50m accuracy possible
  - DVB TV: 40m accuracy possible
- Will use Software-Defined Radios (SDRs): RTL-SDR, Ettus boards, HackRF One, LimeSDR-Mini
- Advantage: RF signals difficult to jam comprehensively (unlike GPS narrow band)

**5. Sensor Fusion**
- Kalman filter-based architecture accepting position/velocity estimates from multiple sources at varying frequencies
- Maintains error bounds for mission planning
- Phase I demonstrated feasibility; Phase II will complete generalized formulation

### Hardware Implementation
- **Visual Processing**: Jetson TX2 SBC (Phase I) transitioning to DepthAI board (Intel Myriad X) for Phase II
- **Downward Camera**: Configured with same optical parameters as actual flight hardware for training simulation
- **Laser Altimeter**: Used for AGL measurement in optical flow and depth correction
- **SDRs**: Multiple options evaluated for size/weight/cost tradeoffs
- **Integration**: Designed as standalone package with serial GPS-like output; compatible with BST aircraft (S1, S2) and third-party UAS/autopilots

## Products & Capabilities Described

### DS-GPS System (Primary Product)
- **What it is**: Integrated sensor fusion system providing GPS-independent positioning through vision, inertial, and RF signal sources
- **Proposed use**: Enable BLOS operations in GPS-denied environments; provide redundant positioning for UTM compliance; detect and survive GPS jamming/spoofing
- **Specifications**:
  - Position accuracy: 50m RMS error without GPS
  - Velocity update rate: ≥20Hz
  - Weight: <350g
  - Cost target: <$2,000 per unit
  - Interface: GPS-like serial output (compatible with existing avionics)
  - Operational altitude: 400+ feet AGL (5 cm GSD training data at 120m AGL)

### Subsystems Integrated
- **Optical Flow/Visual Odometry**: High-rate (20+ Hz) inertial velocity estimation
- **SLAM**: Low-rate absolute position correction (<1Hz estimated)
- **Signals of Opportunity Receiver**: Backup positioning from RF infrastructure
- **GPS Degradation Detection**: Real-time monitoring with jamming/spoofing flags

## Use Cases & Applications

### Primary Market: Government & Commercial BLOS Operations
1. **Coastal monitoring**: Line-of-sight limited operations over water
2. **Infrastructure inspection**: Power line and pipeline inspection (may traverse areas with poor GPS)
3. **Package delivery**: Extended-range autonomous delivery missions
4. **Emergency response**: Operations over urban canyons, high latitude, or high altitude locations with GPS degradation
5. **Military/Defense**: Operations in GPS-denied/contested environments

### Specific Scenarios Addressed
- GPS jamming/spoofing by adversaries or low-cost jammers (cited UT Austin spoofing of UAS using low-cost SDR equipment)
- GPS loss in urban canyons, high latitudes, high altitudes
- Hardware failure of on-board GPS receiver
- Night operations or inclement weather (signals of opportunity fallback)
- Snow/water overflights with homogeneous terrain (vision fallback to RF signals)

## Key Results (Phase I Achievements)

### Optical Flow
- Prototype hardware assembled and integrated into S1 UAS
- Algorithm implemented on-board Jetson TX2, flight tested across multiple environments
- Generated flow fields at 27 fps on embedded hardware
- Demonstrated performance sufficient for DS-GPS incorporation

### Absolute Positioning
- ORB-SLAM2 tested on flight data; target 50m error achieved and maintained consistently across flights
- Multiple absolute positioning algorithms evaluated:
  - **Key frame matching**: Saved navigation markers for GPS coordinate matching
  - **Road following**: Semantic segmentation networks trained to match known road databases
  - **Shoreline following**: Coastline detection and matching algorithm
- Figure 4 shows ORB-SLAM2 results maintaining error below 50m target (red dashed line)

### GPS Spoofing Detection
- Evaluated jamming/spoofing detection methods; determined uBlox spoofing flag sufficient vs. higher-end Novatel solutions
- Plan established for Phase II hardware triggering and system characterization
- Identified AGC (Automatic Gain Control) monitoring as key detection metric

### Signals of Opportunity Assessment
- Comprehensive survey of feasible RF signal sources completed
- Determined viable navigation solutions for GSM, LTE, ATSC, DVB with researched accuracy estimates
- Identified narrow-bandwidth signals as preferable (easier SDR reception, lower cost)

### Training Data Infrastructure
- Gazebo simulation environment developed with:
  - Simulated downward-facing camera with accurate optical parameters
  - Simulated laser altimeter with realistic ranges
  - 5cm GSD photogrammetry terrain skinning (matching 120m AGL operating altitude)
  - Hardware-in-the-loop (HWIL) interface for actual onboard hardware testing
  - Automated video generation capability from simulation world
- E2 multirotor model created in simulation
- Demonstrated H264 encoding and UDP streaming for HWIL testing
- This infrastructure enables generation of hundreds of hours of labeled training video

## Notable Details

### Risk Mitigation & Phase I Achievements
- High-risk items retired in Phase I: jamming/spoofing detection feasibility, vision-based velocity accuracy, vision-based absolute positioning accuracy, sensor fusion architecture
- Aggressive Phase I flight testing performed to guarantee Phase II success
- Hardware-in-the-loop simulation validated attitude rate corrections critical for accurate optical flow (Figure 9 shows importance of roll/pitch/yaw compensation)

### Cost/Weight Evolution
- Phase I target: $6,000 per unit; revised to $2,000 in Phase II due to state-of-the-art machine vision hardware cost reductions
- Weight target: <350g (lightweight enough for small commercial UAS)

### Competitive Advantages
- Large proprietary repository of survey-grade photogrammetry data (sometimes exceeding 3,000 acres) enables rapid neural network training without expensive data collection
- Simulation infrastructure built in-house allows HWIL testing before flight
- Integration with BST autopilots (SwiftCore/SwiftPilot) reduces development time

### UTM Integration
- System designed to output position information continuously to UAS Service Supplier (USS) per UTM rules
- Addresses FAA case-by-case approval requirements for BLOS operations
- Enables aircraft to detect GPS degradation and continue safe operations vs. forcing visual LOS recovery
- Maintains aircraft relative spacing and local traffic avoidance capability

### Related Commercial Applications
- BST separately developing machine learning predictive maintenance and emergency autonomous landing systems; DS-GPS completes safety package for BLOS operations
- Addresses fundamental safety bottleneck: without accurate position information, aircraft cannot safely navigate or avoid hazards in BLOS operations

### Key Personnel
- **Dr. Jack S. Elston**: CEO, Principal Investigator; extensive background in autonomous systems and UAS development
- **Dr. Maciej Stachura**: Lead Engineer
- **Josh Fromm**: Aircraft Design and Integration

### Requested Funding & Timeline
- Phase II funding: $395,730.81
- Period of Performance: April 1, 2021 – March 31, 2023 (24 months)

### Technology Differentiation from Phase I Work
- Phase I limited to classical optical flow and SLAM methods due to lack of training data
- Phase II enables cutting-edge deep neural networks through automated training data generation from photogrammetry maps
- Upgrade from Jetson TX2 to DepthAI (Intel Myriad X) for real-time neural-assisted stereo depth
- Introduction of volumetric correspondence networks (VCN) for optical flow
- Upgrade from ORB-SLAM2 to ORB-SLAM3 with RGB-D support