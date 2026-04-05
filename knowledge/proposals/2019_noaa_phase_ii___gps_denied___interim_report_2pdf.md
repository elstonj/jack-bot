# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: SBIR Phase II Interim Report
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- Program/Solicitation: NOAA SBIR Phase II, Grant Award Number NA20OAR0021000
- Date: October 2021 (submission date; reporting period May 1, 2021 – October 30, 2021)
- BST Products/Systems Referenced: S2 quadcopter, DepthAI stereo camera (OAK-D, OAK-FFC-3P), Ettus E3100 SDR, custom GNSS board with u-blox ZED-F9P receiver
- Key Personnel: Jack Elston (CEO, Project Director/Principal Investigator)

## Executive Summary
Black Swift Technologies is developing a GPS-denied navigation system for Beyond Line-of-Sight (BLOS) UAS operations in the National Airspace System (NAS). The system integrates multiple technologies—GPS monitoring/spoofing detection, optical flow-based visual inertial odometry (VIO), simultaneous localization and mapping (SLAM), and signals of opportunity (SoOP) processing—to provide continuous position estimates accurate to 50mm RMS without GPS. Phase II work focused on implementing these components on embedded hardware and conducting flight testing.

## Technical Approach

### Core System Architecture
The diverse-source GPS (DS-GPS) system comprises four integrated components:

1. **GPS Monitoring Module**: Detects GPS jamming and spoofing using u-blox ZED-F9P receiver with multi-constellation GNSS tracking, background noise monitoring, and anti-tamper firmware verification. Switches to DS-GPS when GPS loss/spoofing detected.

2. **Inertial Estimation (Visual Inertial Odometry)**: Combines optical flow from DepthAI stereo camera with onboard IMU, magnetometer, and laser altimeter to maintain high-rate (20Hz) velocity estimates with low drift in varying wind conditions.

3. **Absolute Position Estimation**: Uses neural-network-assisted stereo depth estimation (RGB-D sensing) integrated with SLAM (ORB-SLAM3) to periodically provide unbiased absolute position measurements and environmental mapping.

4. **Sensor Fusion**: Kalman filter-based algorithm ingests position/velocity estimates from all sources (inertial, visual odometry, SLAM, SoOP) at varying update rates to produce fused position estimate with error bounds.

### Key Technical Details

**Optical Flow & Depth Estimation:**
- Uses DepthAI OAK-D stereo camera (7.5cm baseline, 71.9° HFOV) for stereo streams
- Weighted Least Squares (WLS) filtering applied to disparity maps for edge-preserving smoothing
- 3D neural network depth estimators converted to OpenVINO .blob format for onboard inference on Intel Myriad X processor
- Explored baseline distances and resolutions to optimize depth detection range for top-down aerial view
- Initial flight testing conducted on BST S2 quadcopter

**SLAM Implementation:**
- ORB-SLAM3 selected for stereo/visual-inertial capabilities with multi-map support
- Uses Oriented FAST/Rotated BRIEF (ORB) feature detection
- Atlas mapping system handles multi-session SLAM with loop closure and map merging
- Target accuracy: ≤50mm error during Phase II
- Processes DepthAI stereo streams with neural-assisted depth for RGB-D sensing
- IMU data from DepthAI camera directly integrated

**Optical Flow Training Data Generation:**
- Leverages BST's large repository of survey-grade photogrammetry data (sometimes >3,000 acres)
- Blender-based headless data generation with Python scripts to simulate realistic stereo camera models
- Automated augmentation techniques: Gaussian noise, translation, scaling, color/gamma changes
- Generates hundreds of hours of labeled stereo video with exact 3D position and trajectory ground truth

## Products & Capabilities Described

### Existing BST Systems Referenced
- **S2 Quadcopter**: Platform for initial flight testing of optical flow/stereo systems
- **BST DepthAI Integration**: Customized stereo camera system with modular setup allowing adjustable baseline and field-of-view

### Hardware Selected for DS-GPS
- **u-blox ZED-F9P Receiver**: GNSS board with multi-constellation spoofing/jamming detection, firmware anti-tamper, consistency checks
- **DepthAI OAK-D/OAK-FFC-3P**: Intel Myriad X-based stereo cameras for real-time depth and onboard inference
- **Ettus Research E3100 SDR**: Dual receivers, wide frequency range for signals of opportunity development; chosen for UHD/GNU Radio support and portability
- **Single Board Computer (SBC)**: Aggregates and processes sensor data (host for ORB-SLAM3 and optical flow in initial phases)

### Proposed System Specifications (End of Phase II Goals)
1. Unit cost: <$6,000
2. Weight: <350g
3. Position accuracy: 50mm RMS error without GPS
4. Serial interface: GPS-like output for standard avionics integration

## Use Cases & Applications

### Primary Use Case
- **BLOS UAS Operations under UTM (UAS Traffic Management)**: Enables safe beyond-visual-line-of-sight flights in National Airspace System where GPS denial or spoofing could occur
- Performance authorization from FAA requires reliable navigation, collision avoidance, emergency landing capability, and intent sharing

### GPS-Denial Scenarios
- GPS jamming (intentional and unintentional)
- GPS spoofing attacks (verified risk: luxury yacht diverted to Greece, UAV capture attacks)
- Urban canyons with poor GPS reception
- High-latitude and high-altitude operations
- GPS receiver failure or poor solution quality

### Environmental/Mission Applications (Implied)
- All-weather operation (SoOP navigation potential for night/poor visibility conditions)
- Operations in remote regions with cellular coverage
- Search and rescue missions in GPS-denied areas

## Key Results (Phase II Interim Progress)

### Completed/Near-Complete Milestones

**GPS Monitoring (90% complete, due Oct 1, 2021):**
- u-blox ZED-F9P receiver firmware integrated for spoofing/jamming detection
- Jamming detection tested successfully with unshielded USB cable interference (repeatable across multiple environments)
- Spoofing detection capability acknowledged from u-blox test results (full-scale spoofer development deferred as out-of-scope)
- Initial firmware implementation on custom GNSS board complete

**Generation of Dense Training Data (75% complete, due Aug 27, 2021):**
- Blender-based headless simulation environment operational with Python scripting
- Photogrammetry 3D maps manipulated to generate realistic stereo camera training data
- Multiple augmentation techniques implemented: Gaussian noise, translation, scaling, color/gamma changes
- Automated Python/OpenCV augmentation pipeline developed
- Ready to generate hundreds of hours of labeled training video

**Optical Flow Algorithm Design (20% complete, due Dec 24, 2021):**
- DepthAI stereo camera inference pipeline created for video stream processing
- Real-time feasibility analysis for stereo depth estimators on embedded hardware completed
- Initial inference pipeline running on Single Board Computer (SBC) host
- Code optimization for TensorFlow Lite (TFLite) onboard execution ongoing
- HITNet (Hierarchical Iterative Tile Refinement Network) depth estimator evaluated but running slow; focus shifting to OpenVINO optimization for onboard Myriad X inference

**Simultaneous Localization and Mapping (30% complete, due April 8, 2022):**
- ORB-SLAM3 feasibility with DepthAI reviewed
- Initial stereo SLAM implementation with DepthAI camera completed
- WLS filtered disparity with ORB feature tracker generating sparse 3D terrain maps
- Feature tracker and keyframe workflow with trajectory/position database operational

**Visual Odometry (25% complete, due April 8, 2022):**
- IMU sensor acquisition pipeline from DepthAI camera module established
- Feature tracker implementation with trajectory visualization in progress

**Signals of Opportunity (15% complete, due April 1, 2022):**
- LTE, GSM (2G), CDMA (3G) signal standards assessed for navigation viability
- Ettus E3100 SDR selected as development platform
- Embedded SDR cross-compiled with UHD (USRP Hardware Driver) & GNU Radio
- LTE receiver development underway
- Software-defined radio implementation with standalone USRP E3100 accomplished
- Coverage analysis: Determined 4G/LTE superior to 2G/3G for practical deployment due to network sunsetting schedules

**Sensor Fusion (20% complete, due Oct 7, 2022):**
- Headless data gathering setup with SBC and DepthAI achieved
- Kalman filter sensor fusion algorithm demonstration from Phase I
- Phase II focus: Completing generalized formulation to ingest position/velocity from any source (frequent or infrequent) while maintaining accuracy estimates

### Signals of Opportunity Technical Analysis

**Cellular Signal Evaluation:**
- **2G/GSM**: Low power, narrow bandwidth, requires base station within few hundred meters; lacks synchronized clocks for ToA; sunsetting globally by mid-2020s; deemed impractical for forward product development
- **3G/CDMA**: Synchronous via GNSS atomic clocks; more favorable than GSM but also phased out in many regions; example: US carriers (Verizon 2022, AT&T Feb 2022, T-Mobile Apr 2022, Sprint Dec 2021); Germany (Jun 2021), other regions following
- **4G/LTE**: Expanding coverage, superior to legacy technologies in most operational regions (NA, EU, Latin America); best long-term viability; continued expansion expected; slower roll-out rate but not replaced by 5G for ~decade

**Hardware & Receiver Development:**
- Ettus E3100 chosen for portability (UHD drivers work with other Ettus models: B2xx, E3xx series)
- GNU Radio compatibility ensures platform flexibility
- Cross-compilation completed for embedded SDR targets
- LTE receiver algorithm development in progress

**Coverage Regional Analysis:**
- BST operates primarily in NA, EU, and Latin America—regions with strong 4G/LTE coverage and low GSM usage
- For future African operations, 4G would not provide sufficient coverage; GSM-based solution would be needed (but deprioritized for current product)
- Global population coverage: 3G covers 8.5% more than 4G (as of 2021), but sunsetting will reverse this; 4G coverage only increased 1.3% from 2019-2020

## Notable Details

### Partnerships & Collaborations
- **NASA**: E3100 SDR on loan to BST from NASA for evaluation
- **u-blox**: Partnership for GNSS receiver selection and testing; documentation and spoofing test verification provided
- **Intel/Luxonis**: DepthAI/OAK hardware and OpenVINO toolkit for neural network optimization
- **Ettus Research/GNU Radio Community**: SDR development platform and open-source receiver modules

### Risk Mitigation & Development Strategy
- **Data Generation Risk**: Phase I identified lack of training datasets for aircraft overhead perspective; Phase II generates synthetic training data from photogrammetry repository to eliminate data scarcity bottleneck
- **Depth Estimation Optimization**: Initial HITNet inference too slow on host; shifting to onboard Myriad X inference via OpenVINO to preserve host resources for SLAM and optical flow post-processing
- **Multi-Signal Resilience**: SoOP signals (LTE, FM radio, TV stations) enable operation beyond cellular coverage and in night/poor-visibility conditions not feasible with vision-only systems
- **SLAM Scale Ambiguity**: Addressing ORB-SLAM2's inability to produce scaled metric output; Phase II approach uses RGB-D depth to determine scale factor and rigid rotation correction between ORB reference frame and global metric frame

### Competitive Advantages Identified
1. **Diverse fusion architecture**: Combines inertial, visual, SLAM, and RF signals vs. single-source alternatives
2. **Custom training data generation**: Uses proprietary photogrammetry archive to create top-down aerial training datasets—not available commercially
3. **Embedded optimization**: Deploying neural networks on