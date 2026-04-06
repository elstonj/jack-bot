# Diverse-Source GPS (DS-GPS) System for GPS-Denied UAS Navigation

## Document Metadata
- **Type:** SBIR Phase I Technical Proposal
- **Client/Agency:** NOAA
- **Program/Solicitation:** NOAA 2019 SBIR Phase I, Solicitation 9.5.01 "Advanced Unmanned Aircraft Systems (UAS) Observing Platforms"
- **Date:** Submitted January 8, 2019
- **BST Products/Systems Referenced:** S2 UAS, SwiftCore autopilot, Jetson TX2
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator, CEO/co-founder)
  - Austin Anderson (Machine Vision Lead)
  - Dr. Maciej Stachura (State Estimation Lead, CTO)
  - Joshua Fromm (Mechanical Design and Integration)

## Executive Summary

Black Swift Technologies proposes development of a Diverse-Source GPS (DS-GPS) system to enable beyond-line-of-sight (BLOS) autonomous UAS operations in GPS-denied environments. The system combines inertial navigation augmented with optical flow, vision-based absolute positioning, and signals of opportunity to provide continuous positioning updates accurate to 50m RMS error without GPS. This standalone module will interface with commercial UAS like an external GPS unit, addressing a critical gap in NOAA's requirements for safe and reliable BLOS operations in remote and challenging environments.

## Technical Approach

### System Architecture
The DS-GPS system comprises four integrated components:

1. **GPS Monitoring:** Detects GPS jamming and spoofing events using carrier-to-noise density ratio (C/N₀) and automatic gain control (AGC) monitoring. Switches system to DS-GPS mode when GPS is compromised.

2. **Inertial Estimation:** Combines IMU (3-axis accelerometer, gyroscope, magnetometer), airdata sensors (static/dynamic pressure), laser altimeter, and optical flow to estimate position and velocity without GPS. Uses Unscented Kalman Filter to estimate 3D winds in real-time, allowing system to function even when optical flow performance degrades over homogenous terrain.

3. **Absolute Position Estimation:** Provides periodic unbiased position measurements using:
   - Machine vision algorithms (keyframe following, SLAM, road/coastline following)
   - Signals of opportunity (VOR, cell towers, WiFi, TV towers via software-defined radio)
   - Semantic segmentation for terrain feature identification

4. **Sensor Fusion:** Integrates high-rate inertial solution with lower-rate absolute position updates to produce 20Hz position estimates with error bounds.

### Key Technical Specifications (Phase II Target)
- **Cost:** Below $6,000 per unit
- **Weight:** Below 350g
- **Accuracy:** 50m RMS error without GPS
- **Interface:** Serial output with GPS-like data format for compatibility with standard autopilot systems
- **Update Rate:** 20Hz position solution

### Inertial Navigation Implementation
- Leverages existing SwiftCore autopilot hardware and algorithms
- Integrates optical flow sensor (motion-from-vision) with traditional IMU
- Uses pressure altitude and digital elevation maps for altitude estimation
- Laser altimeter provides accurate AGL up to 120m (extended systems to 1km+)
- Optical flow sensitive to terrain quality; system designed for robustness over homogenous terrain (water, snow) through wind estimation

### Vision-Based Absolute Position Methods

**Keyframe Following:** Logs positions and images of visually-rich areas during GPS-enabled flight. Upon GPS loss, aircraft backtracks to match current images against saved keyframes for position correction. Requires knowledge of exact GPS loss moment to avoid spoofed position logging.

**SLAM (Simultaneous Localization and Mapping):** Produces denser map of surveyed terrain; more processing-intensive. Phase I work emphasizes mapping with valid GPS signals; stability without GPS will be simulated.

**Preprocessing:** Flight plan validation against satellite imagery to identify visually-rich vs. homogenous terrain. Helps ensure optical flow sensor coverage and guides aircraft back to safe areas using dense waypoint sets.

**Road/Coastline Following:** Uses semantic segmentation (deep learning) to identify and follow roads, railways, powerlines, or coastlines. Demonstrated feasibility with semantic segmentation of RC airfield showing ability to identify impervious surfaces, buildings, and vegetation. Requires only sparse road maps rather than dense imagery.

### Signals of Opportunity Strategy

**Dedicated Aviation Signals:**
- VOR (VHF Omnidirectional Range) provides coverage above 5000' AGL with Minimum Operational Network (MON) planned for 2020
- Software-defined radio (SDR) receivers to access VOR and DME navigation signals

**General RF Signals:**
- TV tower signals (advanced signaling standards allow navigation metric extraction)
- Cell tower signals
- WiFi signals
- Advantage: More robust to jamming than dedicated signals; variety of bands prevents single-source interference

Phase I will survey existing research, downselect candidate signal types, and select SDR hardware for Phase II implementation.

### GPS Spoofing/Jamming Detection
Phase I includes evaluation of detection techniques:
- Monitor AGC and C/N₀ changes to distinguish spoofing (trend separable from nominal behavior) from noise jamming (degraded satellite availability/solution quality)
- Develop plan for Phase II hardware selection and spoofing simulation protocol meeting NOAA and FCC requirements

## Products & Capabilities Described

### S2 UAS
- Modular platform for atmospheric science missions
- Will serve as testbed for DS-GPS inertial navigation system during Phase I flight testing
- Equipped with autopilot, sensor integration, and flight test range capabilities

### SwiftCore Autopilot
- BST's autopilot system incorporating IMU, pressure sensors, airdata, and attitude/rate estimation
- Existing hardware and firmware provide foundation for inertial navigation portion of DS-GPS
- Will be adapted to include optical flow integration and sensor fusion algorithms

### Optical Flow Sensors
- Downward-facing motion-from-vision camera for lateral inertial velocity estimation
- Requires range estimation for proper scaling
- Limited to sufficient lighting and relatively clear weather; augmented by inertial solution in poor conditions
- Sensitive to terrain: performs well over textured terrain (edges, lines, textures), poorly over homogenous scenes

### Jetson TX2
- Single-board computer for onboard processing of measurements
- Will process inertial navigation algorithms and output GPS-like position/velocity data

## Use Cases & Applications

### Primary Use Case: BLOS UAS Operations in National Airspace System (NAS)
- Enables safe autonomous operations under UTM (UAS Traffic Management) system
- Addresses FAA requirement that BLOS operations maintain reliable position information for:
  - Relative aircraft spacing within UTM system
  - Avoidance of other traffic
  - Risk mitigation to people and property on ground

### Operating Environments
- GPS-denied areas (jamming, spoofing, signal loss)
- Urban canyons with poor GPS coverage
- High latitudes and high altitudes with degraded GPS
- Remote and challenging environments critical to NOAA science missions

### Specific Mission Scenarios Enabled
- Emergency return-home capability when GPS is lost
- Navigation in areas with intentional GPS jamming
- Mission continuation beyond standard GPS coverage
- Extended operations in visually-rich terrain for vision-based localization
- Low-visibility/nighttime operations (signals of opportunity mode)

### NOAA Science Context
- Document references BST's prior work in severe storm sampling (VORTEX2 tornadic supercell intercepts)
- Supports NOAA science missions in "remote and/or challenging environments"
- Enables safe operations that would otherwise require visual line-of-sight (VLO) supervision

## Phase I Technical Objectives & Work Plan

### Objectives
1. Develop and flight-test inertial navigation solution with optical flow integration
2. Demonstrate vision-based absolute position algorithms on embedded hardware
3. Evaluate feasibility of signals of opportunity for GPS-denied navigation
4. Assess GPS spoofing detection techniques and hardware requirements
5. Establish performance requirements for absolute position measurement subsystem

### Phase I Milestones (6-month timeline)

**1. Inertial Navigation Hardware Prototype**
- Integrate IMU board with pressure sensors, Jetson TX2, and machine vision camera into S2 UAS
- Reuse SwiftCore hardware and firmware where possible

**2. Flight Test of Inertial Navigation Solution**
- Implement optical flow algorithms onboard
- Test in varying wind conditions
- Assess performance against GPS data to characterize wind-related drift
- Critical for setting absolute position measurement requirements
- Builds on BST's Phase I flight test track record (prior NOAA SBIR involved full aircraft design and flight within Phase I)

**3. Preliminary Absolute Position Solution Demonstration**
- Use geotagged photos collected by BST for algorithm testing
- Demonstrate machine vision algorithms on embedded hardware
- Verify onboard performance requirements achievable

**4. GPS Spoofing Detection Plan**
- Evaluate detection techniques and select hardware
- Organize spoofing simulation method meeting regulatory requirements
- Develop implementation roadmap for Phase II

**5. Signals of Opportunity Feasibility Assessment**
- Evaluate potential for nighttime/low-visibility operations
- Inform Phase II development decisions

### Technical Approach for Phase I Inertial Solution
- Unscented Kalman Filter for sensor fusion
- Real-time 3D wind estimation from optical flow + airdata
- Robustness designed into system to function with degraded optical flow performance
- Leverages optical flow feature detection metrics for keyframe identification

### Vision-Based Absolute Positioning Research
- Evaluate keyframe following, SLAM, preprocessing, and road-following approaches
- Analyze required update rate: chart shows 50s update intervals needed for 1 m/s velocity error to maintain 50m position accuracy
- Test algorithms with existing BST imagery dataset
- Performance evaluation on embedded hardware before flight testing

### Signals of Opportunity Research Path
- Phase I: Survey literature, assess VOR coverage, downselect RF signal candidates, identify SDR hardware
- Phase II: Implement selected signal processing, conduct demonstrations

## Phase II Technical Objectives

1. **Vision-Based Absolute Position Implementation:** Integrate onboard vision system with inertial estimator; refine algorithms through data collection and post-processing across diverse terrain types

2. **Flight Test Validation:** Extensive testing in varied conditions (high/variable winds, summer/winter, rural/urban/forest/mountain terrain) to empirically characterize performance bounds and identify improvements

3. **GPS Spoofing Detection Implementation:** Complete hardware integration and detection algorithm development

4. **System Reliability Improvements:** Address nighttime/low-visibility operations; optimize for production deployment

5. **Phase II Commercialization:** Production prototype ready for sale to UAS integrators and end users

## Related Research & Development

### BST's Parallel Development Efforts
BST is simultaneously developing complementary technologies under NASA funding:

1. **Preventative Maintenance System:** Machine learning-based onboard monitoring to detect subsystem failures and suggest maintenance. Demonstrates ability to detect subtle performance degradation (icing, subsystem degradation) using machine learning + estimation techniques.

2. **Safe Landing Capability:** Automatic detection of safe landing areas during loss of propulsion. Critical for beyond-visual-line-of-sight autonomous operations. BST's approach prioritizes avoiding people/structures while finding suitable recovery areas for fixed-wing aircraft. Uses semantic segmentation similar to road-following approach.

### Foundation Technologies
- **Optical Flow:** Widely used in multirotor UAS; previous research explored for fixed-wing applications
- **Vision-Based Localization:** Prior work on road network localization for ground vehicles (Brubaker et al.)
- **Signals of Opportunity Navigation:** Previous research on cell tower-based navigation (Morales et al.); WiFi-based navigation
- **Machine Learning:** BST building on advancements in semantic segmentation for terrain analysis

### BST's Track Record
- 4 different UAS platform designs
- 100+ FAA Certificate of Authorization (COA) applications
- Hundreds of flight experiments including Arctic deployments
- Prior NOAA SBIR: Complete UAS design and flight testing within Phase I
- 300+ flight experiments (team members during prior work)
- NASA Phase II SBIR on "Improved UAS Robustness Through Augmented Onboard Intelligence"

## Key Personnel & Expertise

### Dr. Jack S. Elston (Principal Investigator)
- CEO and co-founder of Black Swift Technologies
- Ph.D. from CU Boulder in atmospheric measurement from UAS
- Led design of Tempest UAS for VORTEX2 project (first-ever unmanned aircraft intercept of tornadic supercell)
- NSF Post