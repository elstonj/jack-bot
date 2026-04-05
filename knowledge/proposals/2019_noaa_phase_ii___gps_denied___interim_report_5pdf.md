# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System – 2019 NOAA Phase II Interim Report

## Document Metadata
- **Type:** SBIR Phase II Interim Report
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- **Program/Solicitation:** NOAA SBIR Phase II; Grant Award Number NA20OAR0210087
- **Date:** February 2022 (Interim Report for period Oct 30, 2022 – Jan 30, 2023)
- **Project Period:** May 1, 2021 – April 30, 2023
- **BST Products/Systems Referenced:** E2 quadrotor, DepthAI stereo cameras (OAK-D, OAK-FFC-3P), Jetson embedded systems, SwiftCore autopilot/IMU sensors
- **Key Personnel:** Jack Elston (CEO/PD/PI), Nick Juarez, Dan Dole-Muinos, Maciej Stachura; Technical Monitor: Phil Hall (NOAA OAR)

---

## Executive Summary
Black Swift Technologies is developing a diverse-source GPS-denied navigation system (DS-GPS) to enable beyond-visual-line-of-sight (BVLOS) UAS operations in GPS-denied or GPS-compromised environments. The Phase II effort focuses on integrating visual odometry, simultaneous localization and mapping (SLAM), inertial navigation, and signals of opportunity into a single hardware module weighing <350g and costing <$6,000, providing navigation accuracy of 50m RMS error without GPS.

---

## Technical Approach

### Core System Architecture
The DS-GPS system comprises four key components:

1. **GPS Monitoring**
   - Detects GPS spoofing and jamming events
   - Triggers fallback to DS-GPS when GPS is compromised
   - Alerts operator to initiate safe mission conclusion procedures (e.g., return home)

2. **Inertial Estimation**
   - Fuses optical flow with DepthAI onboard sensors (IMU, airdata)
   - Compensates for rapid drift caused by wind and sensor bias/noise
   - Maintains accurate short-term position estimates

3. **Absolute Position Estimation**
   - Machine vision algorithms combined with neural-network-assisted depth estimation
   - Signals of opportunity: RF emitters (cell towers, TV stations)
   - SLAM algorithms for environment mapping and localization

4. **Sensor Fusion**
   - Kalman filter-based fusion combining:
     - Inertial solution (high rate, low-drift)
     - Visual odometry from optical flow
     - SLAM absolute position estimates
     - Signals of opportunity (when available)
   - Outputs 20Hz position estimates with error bounds
   - Serial interface compatible with standard GPS connections

### Vision System Implementation

**Stereo Depth Estimation:**
- Tested OAK-D (7.5 cm fixed baseline) and OAK-FFC-3P (modular, adjustable baseline up to 24 cm)
- Compared classical stereo disparity with neural-assisted approaches:
  - **HITNET** (TensorFlow-based depth estimation): performs better than onboard disparity at ranges >10m with neural networks able to predict depth up to 20m+ despite short baseline
  - **CREStereo**: ranked 1st on Middlebury and ETH3D benchmarks; supports onboard inference on Intel Myriad-X chipset
  - **DepthAI native disparity**: generates onboard depth maps but exhibits significant noise >10m altitude

**Calibration & Rectification:**
- Kalibr toolbox used for stereo-IMU calibration
- Computed transformation matrices between camera and IMU frames
- Achieved reprojection error <1 pixel
- Validated stereo baseline adjustments (7.5 cm vs. 24 cm) with flight data

**Training Data Generation:**
- Utilized BST's existing survey-grade photogrammetry repository (high-resolution maps of up to 3000+ acres)
- Automated pipeline to generate synthetic stereo pairs from 3D photogrammetry models using Blender
- Data augmentation: Gaussian noise, geometric transforms, gamma/color adjustments
- Addresses scarcity of public top-down aircraft perspective datasets

### SLAM & Visual-Inertial Odometry (VIO)

**Algorithms Evaluated:**
- **ORB-SLAM3**: Full visual-inertial stereo mode with IMU integration; global bundle adjustment ensures accuracy but high memory usage; challenges for Jetson Nano deployment
- **RTABMap**: Frame-to-Map (F2M) odometry with modular VIO integration (OKVIS, VINS-Fusion, OpenVINS); faster pose optimization; lower memory; supports ORB-SLAM2 as front-end
- **HybVIO**: Novel hybrid filtering-based VIO + optimization-based SLAM; robust IMU bias modeling; fastest performance; minimal resource consumption; embedded-friendly

**Implementation Status:**
- ORB-SLAM3 successfully implemented with stereo-inertial calibration and ported to ROS
- RTABMap deployed on Jetson Nano with RGB-D mode (dense point cloud generation)
- HybVIO being ported to embedded Jetson board; showing best speed/resource balance

### Optical Flow & Attitude Correction
- Fusion of inertial data with neural-assisted optical flow for real-time velocity estimation
- Kalman filtering for drift correction and attitude-based adjustment
- Integration with SLAM for robust pose estimation

### Signals of Opportunity
- **LTE Timing Advance (TA):** Extracting timing advance from cell tower RACH messages to compute pseudorange
- **Hardware:** BladeRF 2.0 micro xA5 software-defined radio selected for LTE signal processing
- **Status:** Software implementation complete; hardware synchronization with real towers under investigation

---

## Products & Capabilities Described

### DS-GPS Module Specifications (Target)
| Specification | Target Value |
|---|---|
| Cost per Unit | <$6,000 |
| Weight | <350g |
| Position Accuracy (without GPS) | 50m RMS error |
| Update Rate | 20 Hz |
| Output Interface | Serial (GPS-compatible) |

### Key Hardware Components
- **Stereo Cameras:** OAK-D or OAK-FFC-3P (modular, baseline-adjustable)
- **Compute:** Intel Myriad-X (onboard inference), NVIDIA Jetson Nano (SBC host)
- **Sensors:** IMU, laser altimeter, airdata sensor (autopilot-integrated)
- **SDR:** BladeRF 2.0 micro xA5 (for LTE signals of opportunity)

### Payload Design
- Modular, lightweight design (<350g total) for mounting on various BST aircraft
- Tested on BST E2 quadrotor
- Currently under optimization for real-time processing resource efficiency

---

## Use Cases & Applications

1. **BVLOS Operations in National Airspace System (NAS)**
   - Requires FAA performance authorization (UTM framework)
   - Addresses navigation, communication, aircraft avoidance, and FAA connectivity

2. **Pipeline Inspection** (long-range, remote)
   - Energy sector environmental monitoring
   - GPS-denied areas (dense urban, industrial structures)

3. **Drone Delivery**
   - Rapid delivery of critical/life-saving packages
   - Social distancing support (COVID-19 context)

4. **Urban Canyons & High-Latitude Operations**
   - GPS signal loss in built environments
   - High-altitude operations with degraded GPS

5. **GPS-Jamming/Spoofing Resilience**
   - Military/critical infrastructure protection scenarios
   - Autonomous safe-landing on GPS loss

---

## Key Results

### Phase II Accomplishments (as of February 2022)

| Task | Completion % | Status |
|---|---|---|
| GPS Monitoring | 90% | On hold pending firmware testing post-integration |
| Dense Training Data Generation | 80% | Blender-based photogrammetry pipeline, automated augmentation complete |
| Optical Flow Algorithm Design | 85% | Real-time performance analysis ongoing |
| SLAM (Simultaneous Localization & Mapping) | 85% | Stereo-inertial calibration, RTAMap/ORB-SLAM3 tested |
| Visual Odometry | 80% | IMU fusion pipeline, multi-VIO approach comparison |
| Signals of Opportunity (LTE) | 50% | Hardware selected (BladeRF); syncing with real towers in progress |
| Sensor Fusion | 20% | Headless data gathering pipeline established |

### Vision System Flight Test Results

**Depth Estimation Performance (OAK-D, 7.5cm baseline):**
- Onboard DepthAI disparity: unreliable >10m altitude
- HITNET neural-assisted depth: accurate to 20m+ (outperforms disparity despite short baseline)
- Ground truth: laser altimeter data

**Depth Estimation Performance (OAK-FFC-3P, 24cm baseline):**
- Improved onboard disparity performance
- Pitch/attitude effects on accuracy identified
- Inertial correction planned for Phase II

**Calibration Results:**
- Reprojection error achieved <1 pixel (quality standard met)
- Stereo-IMU transformation matrices computed for SLAM integration

### Key Technical Findings

1. **Neural-Assisted Depth Superior to Classical Stereo:** HITNET networks outperform onboard disparity at operational ranges despite hardware constraints
2. **Baseline Tradeoff:** Longer baselines improve range but increase physical footprint; neural networks mitigate short-baseline limitations
3. **Stereo-Inertial Integration Essential:** SLAM/VIO accuracy significantly improved when IMU data fused with vision
4. **Algorithm Selection:** HybVIO shows best resource efficiency for embedded deployment; ORB-SLAM3 more accurate but memory-intensive
5. **Photogrammetry-Based Training:** BST's existing survey data enables rapid synthetic dataset generation, avoiding expensive field data collection

### Budget Status
- Cumulative costs as of February 2022: $296,668.29
- 75% of work completed
- Project on budget

---

## Notable Details

### Partnerships & Collaborations
- **NOAA Technical Monitor:** Phil Hall (OAR)
- **Technology Partners (implied):** Intel (Myriad-X, OpenVINO), NVIDIA (Jetson), OpenAI/research community (SLAM/VIO algorithms)
- **No formal external partnerships** listed

### Competitive Advantages Highlighted
1. **Existing Photogrammetry Repository:** BST's customer-provided survey data enables rapid, cost-effective training dataset generation
2. **Specialized Top-Down Perspective:** Addresses unique aircraft navigation problem domain (most public datasets from ground/car perspective)
3. **Commercial Off-the-Shelf (COTS) Integration:** Leverages affordable embedded components (OAK cameras, Jetson) while maintaining custom algorithm development
4. **Modular Payload Design:** Compatible with multiple BST aircraft platforms

### Regulatory/Standards Alignment
- **FAA UTM Framework:** System designed to meet BLOS performance authorization requirements
- **FCC Compliance:** Spooﬁng/jamming detection testing planned to meet regulatory standards
- **GPS-Like Output:** Serial interface maintains compatibility with existing avionics ecosystems

### Risk Mitigation Strategies
1. **Redundant Absolute Position Methods:** SLAM + signals of opportunity + visual odometry
2. **Real-Time Drift Detection:** Kalman filter error bounds enable mission planning decisions
3. **Emergency Landing Capability:** Integration with BST's machine-learning-based autonomous safe landing
4. **Graceful Degradation:** System continues operating in multiple SLAM/VIO modes if primary method fails

### Outstanding Challenges
1. **Signals of Opportunity Syncing:** LTE timing advance synchronization with real towers still under investigation
2. **Embedded Real-Time Performance:** Optimizing SLAM/VIO algorithms for Jetson Nano resource constraints
3. **Optical Flow Outlier Handling:** Strategies for visually-poor/blurry/overexposed frame scenarios pending
4. **Attitude Correction Integration:** Kalman filtering for optical flow drift correction dependent on completion of SLAM/VIO baseline testing

### Dissemination
- **Larta Program Pitch Event**