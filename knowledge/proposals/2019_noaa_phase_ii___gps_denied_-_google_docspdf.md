# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: SBIR Phase II Proposal
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research
- Program/Solicitation: NOAA SBIR 2019 Phase II; Topic 9.5.01 (Advanced UAS Observing Platforms)
- Federal Grant Award Number: NOAA-OAR-OAR-TPO-2020-2006595
- Date: Submitted October 14, 2020
- Proposed Period of Performance: April 1, 2021 – March 31, 2023
- BST Products/Systems Referenced: S1 UAS, S2 UAS, SwiftCore, SwiftPilot autopilot, E2 multirotor
- Key Personnel: Dr. Jack S. Elston (CEO, Principal Investigator), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposed developing a Diverse-Source Global Positioning System (DS-GPS) to enable GPS-denied Beyond Line of Sight (BLOS) operations for unmanned aircraft systems. The system would provide accurate position and velocity information during GPS jamming, spoofing, or hardware failure through sensor fusion combining optical flow, SLAM, signals of opportunity, and inertial measurement—allowing aircraft to safely navigate and report position to the UAS Traffic Management (UTM) system even without GPS. The Phase II effort built on Phase I validation of optical flow algorithms and absolute positioning techniques with continuous flight testing to create a commercial product.

## Technical Approach

### Core System Architecture
The DS-GPS system augments a standard GPS receiver with multiple additional sensing capabilities to estimate inertial velocity and absolute position. A standard GPS receiver is continuously monitored; if degraded by jamming, spoofing, or environmental effects, alternative sensors take over as primary navigation sources.

### Multi-Source Position Estimation
The system combines four primary positioning techniques:

1. **Optical Flow (Visual Odometry)** - High-rate (~20-27 Hz) velocity estimation from downward-facing camera using pixel tracking and optical flow algorithms. Provides inertial velocity measurements necessary for UAS control. Phase I demonstrated 27 fps real-time performance on Jetson TX2 embedded hardware. Phase II planned improvements using neural-assisted Volumetric Correspondence Networks (VCN) trained on synthetic datasets to achieve more accurate depth-relative flow.

2. **SLAM (Simultaneous Localization and Mapping)** - Absolute position estimation using monocular and RGB-D camera data. Phase I testing with ORB-SLAM2 achieved consistent <50m error across different flights and terrain. Phase II planned upgrade to ORB-SLAM3 with per-pixel depth from neural-assisted stereo cameras, with simulation showing ~4x error reduction when depth is added. Intel Myriad X-based DepthAI hardware selected for real-time depth generation.

3. **Signals of Opportunity (SoOp)** - RF-based absolute positioning using software-defined radios (SDR) to receive and process civilian broadcast signals including:
   - GSM/LTE cellular (200 kHz – 80 MHz channels, research showing 3-5m accuracy possible)
   - AM/FM radio (535-1605 kHz / 88-108 MHz, 10-200 kHz channels)
   - ATSC TV (US VHF/UHF, 6 MHz channels, simulation suggesting 50m accuracy)
   - DVB TV (Europe, UHF 1.7 MHz, research showing 40m accuracy)

4. **GPS Monitoring & Spoofing Detection** - Dual-layer approach:
   - Hardware-based detection using u-Blox GPS receiver's built-in spoofing/jamming detection flags
   - AGC (Automatic Gain Control) monitoring to detect jamming before solution degrades
   - Correlator peak asymmetry analysis for spoofing detection
   - C/N0 (Carrier-to-Noise) ratio monitoring combined with AGC for interference classification

### Sensor Fusion
Kalman filter-based sensor fusion algorithm ingests position and velocity estimates from any number of sources (frequent or infrequent) to produce integrated 20 Hz position estimate with error bounds suitable for mission planning. Architecture accepts outputs from optical flow, SLAM, and signals of opportunity as independent measurements.

### Training Data Generation
To overcome lack of publicly available training datasets from aircraft perspective, BST leveraged:
- Existing survey-grade photogrammetry maps (up to 3000 acres, 5 cm Ground Sample Distance)
- Gazebo simulation environment modified with downward-facing camera simulation
- Automated synthetic dataset generation from photogrammetry with per-pixel 3D positions and truth trajectories
- Hardware-in-the-loop (HWIL) simulation using actual Jetson TX2 hardware receiving simulated video streams

## Products & Capabilities Described

### Diverse-Source GPS (DS-GPS) System
**What it is:** A standalone GPS replacement package that outputs GPS-like serial data for integration with existing UAS autopilots and avionics.

**Specifications (Phase II targets):**
- Price: <$2,000 per unit (reduced from Phase I $6,000 target)
- Weight: <350g
- Position accuracy: ±50m RMS without GPS
- Update rate: 20 Hz position, 20-27 Hz velocity
- Output interface: Serial port with GPS-compatible protocol
- Operating altitude: Nominal 120m AGL, tested from 50-400+ feet

**Key capabilities:**
- GPS jamming/spoofing detection
- Continuous position updates during GPS denial
- Error bounds estimation for each position solution
- Integration compatibility with standard autopilots (tested with u-Blox receiver and Jetson TX2)

### Hardware Components
- **Vision System:** Downward-facing machine vision camera with embedded processing
- **Compute:** Jetson TX2 single-board computer (Phase I); Intel Myriad X via DepthAI (Phase II)
- **Inertial:** IMU with pressure sensors for altitude
- **Radio:** Software-defined radio (SDR) capability for signals of opportunity
- **GPS:** u-Blox GPS receiver with spoofing/jamming detection
- **Integration:** Designed for S-series BST aircraft; adaptable to other commercial UAS

## Use Cases & Applications

### Intended Applications
- Coastline monitoring (natural asset surveillance)
- Power line and pipeline inspection (extended range linear inspections)
- Package delivery (long-distance commercial operations)
- Environmental monitoring and mapping
- BLOS survey operations
- Any commercial/government UAS operation requiring extended range beyond line-of-sight

### Operational Scenarios
- **Urban canyon environments** - GPS multipath degradation
- **High latitude operations** - Poor satellite geometry
- **High altitude operations** - Solution quality degradation
- **GPS jamming areas** - Active interference from anti-drone systems or low-cost commercial jammers
- **GPS spoofing attacks** - Potential from state actors or adversaries with SDR equipment
- **Adverse weather** - Night operations, fog, or heavy cloud cover (when using signals of opportunity)

### UTM Compliance
System directly addresses FAA UAS Traffic Management (UTM) requirements for BLOS operations:
- Continuous position reporting to UAS Service Supplier (USS)
- Reliable navigation data for maintaining aircraft spacing
- Capability to safely navigate home without GPS

## Key Results (from Phase I, Foundation for Phase II)

### Optical Flow Algorithm
- Successfully implemented and flight-tested on Jetson TX2 at 27 fps
- Demonstrated velocity estimation within GPS accuracy across multiple test flights
- Identified critical need for depth estimation to correct flat-earth assumption errors
- Performance degradation at higher altitudes (50m vs 120m AGL) attributed to depth inaccuracy

### Absolute Positioning (SLAM)
- ORB-SLAM2 monocular version: Consistently maintained <50m position error across diverse flights
- RTAB-Map depth-based algorithm: Showed promise but required depth maps not available in Phase I
- Simulation testing demonstrated ~4x error reduction when per-pixel depth data added
- Multiple secondary absolute positioning algorithms developed (key frame matching, road following, shoreline detection)

### GPS Degradation Detection
- Confirmed u-Blox commercial spoofing flag availability and effectiveness
- Identified AGC monitoring as reliable jamming detection method
- Surveyed correlator peak asymmetry technique for spoofing detection
- Planned Phase II implementation with actual jamming/spoofing test setup

### Signals of Opportunity Assessment
- Identified LTE, GSM, AM/FM, ATSC, and DVB TV as viable navigation sources
- LTE/GSM: 3-5m positioning accuracy demonstrated in research
- TV signals: 40-50m positioning accuracy feasible
- Concluded narrower-bandwidth signals preferable for software-defined radio implementation

### Flight Testing
- Phase I conducted aggressive flight tests with optical flow algorithm operational
- Generated high-quality flight data for SLAM algorithm validation
- Tested on both S1 and S2 aircraft with Jetson TX2 embedded machine vision payload
- Demonstrated end-to-end system integration feasibility

## Notable Details

### Competitive Advantages
- **Existing infrastructure:** BST's survey-grade photogrammetry repository enables rapid generation of training datasets without expensive new data collection
- **Hardware maturity:** Multiple components (Jetson TX2, DepthAI, u-Blox receivers) are production-ready and cost-optimized
- **UAS expertise:** Deep integration experience with own aircraft platforms (S1, S2, E2) de-risks operational validation
- **Regulatory alignment:** Built explicitly to UTM rules rather than reverse-engineered from generic positioning

### Risk Mitigation Achievements
- Optical flow algorithm: Validated in Phase I, performance sufficient for Phase II integration
- SLAM accuracy: Multiple algorithms tested; ORB-SLAM2 selected with clear upgrade path (ORB-SLAM3)
- Depth estimation: Intel Myriad X hardware selected with clear performance improvement trajectory
- GPS spoofing detection: Commercial receiver capability confirmed; reduces complexity vs. custom solution

### Market Opportunity
- Estimated vast target market: government and commercial users requiring BLOS operations
- Primary segments: infrastructure inspection, mapping, delivery services
- Commercial drone use expected to accelerate as regulatory frameworks mature
- BST premise: BLOS capability is primary enabler for expanded UAS adoption

### Financial Details
- Requested Phase II funding: $395,730.81
- Phase II cost target for product: <$2,000/unit (down from $6,000 Phase I estimate)
- Weight target: <350g (critical for small UAS compatibility)
- Positioned for commercial production and integration into both BST and third-party aircraft

### Technical Novelty
- **Domain-specific training data:** Synthetic generation from photogrammetry specifically addresses lack of aircraft-perspective datasets (most available data from ground vehicle perspective)
- **Multi-source fusion:** Integration of vision, inertial, and RF sources uniquely positions system for resilience against single-mode failures
- **Embedded processing:** Real-time neural network deployment on Jetson TX2 and Myriad X chipsets advances UAS autonomy

### Standards & Compliance
- Explicitly designed around UTM rules and FAA performance authorization criteria
- GPS-compatible serial output ensures drop-in compatibility with existing autopilots
- Addresses identified critical capabilities gap for safe BLOS operations per FAA guidance