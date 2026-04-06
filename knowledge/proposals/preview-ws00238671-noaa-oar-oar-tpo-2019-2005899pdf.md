# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- **Type:** NOAA SBIR Phase I Proposal (Application/Technical Proposal)
- **Client/Agency:** NOAA Office of Atmospheric Research (NOAA-OAR)
- **Program/Solicitation:** FY 2019 Small Business Innovation Research (SBIR) Program; NOAA-OAR-OAR-TPO-2019-2005899
- **Date:** April 12, 2019 (submitted); Project Period: July 1, 2019 – February 29, 2020
- **BST Products/Systems Referenced:** S2 UAS, SwiftCore Flight Management System/Autopilot
- **Key Personnel:** 
  - Dr. Jack S. Elston (CEO, Principal Investigator) – Avionics/firmware lead
  - Austin Anderson (Machine Vision Lead)
  - Dr. Maciej Stachura (CTO, State Estimation Lead)

---

## Executive Summary
Black Swift Technologies proposed developing a Diverse-Source Global Positioning System (DS-GPS) to enable safe Beyond-Line-of-Sight (BLOS) UAS operations when GPS is unavailable, jammed, or spoofed. The system combines optical flow-based inertial navigation with vision-based absolute position correction, sensor fusion, and exploration of signals of opportunity (RF navigation sources) to maintain positioning accuracy within 50 meters RMS in GPS-denied environments. Phase I focused on hardware development, algorithm validation, and feasibility assessment of autonomous navigation techniques.

---

## Technical Approach

### System Architecture (4 Key Components)
1. **GPS Monitoring:** Detects GPS jamming/spoofing by monitoring Automatic Gain Control (AGC) and Carrier-to-Noise Density (C/N₀) ratios; switches system to DS-GPS on signal loss.

2. **Inertial Estimation:** High-rate position/velocity estimation (20 Hz output) using:
   - IMU (3-axis accelerometer, gyroscope, magnetometer)
   - Static/dynamic pressure and digital elevation maps for altitude
   - Laser altimeter (up to 120m range; longer-range 1km+ systems evaluated)
   - Optical flow sensor (downward-facing) for velocity estimation
   - Wind estimation via Unscented Kalman Filter combining optical flow with true airspeed

3. **Absolute Position Estimation:** Periodic position updates via:
   - Keyframe following (saves visually-rich images at known GPS positions; returns to matched keyframes if GPS lost)
   - SLAM (Simultaneous Localization and Mapping) for dense terrain mapping
   - Road/coastline following using semantic segmentation (deep learning)
   - Preprocessing of flight plans using satellite imagery to ensure visually-rich coverage

4. **Sensor Fusion:** Combines inertial and absolute measurements to maintain accuracy; suggests flight paths following roads/coastlines for improved localization.

### Hardware Integration
- Standalone package designed to interface as external GPS unit to standard autopilot systems
- Based on existing SwiftCore avionics (reuses firmware, hardware, algorithms)
- Integration with Jetson TX2 single-board computer
- Optical flow camera (machine vision)

### Signals of Opportunity (Phase II focus)
- **Dedicated aviation signals:** VOR (VHF Omnidirectional Range) via software-defined radios; nationwide coverage above 5,000 ft AGL
- **General RF signals:** TV tower, cellular, WiFi signals
- Assessment during Phase I; implementation in Phase II

---

## Products & Capabilities Described

### S2 UAS
- **What it is:** Modular fixed-wing platform for atmospheric science
- **Role in proposal:** Primary vehicle for Phase I flight testing and algorithm validation; integration platform for DS-GPS hardware prototype

### SwiftCore Flight Management System
- **What it is:** BST's proprietary autopilot with onboard avionics suite
- **Specifications/Capabilities:**
  - Highly capable with proven reliability in field campaigns
  - Includes IMU, pressure sensors, airdata systems
  - Interfaces with external sensors and provides position/velocity outputs
- **Role in proposal:** DS-GPS outputs designed to interface seamlessly with SwiftCore and other commercial autopilots via standard GPS-like serial interface

### DS-GPS System (Proposed Product)
- **Target Specifications (Phase II goals):**
  - Cost: <$6,000 per unit (standalone)
  - Weight: <350 grams
  - Position accuracy: 50m RMS without GPS
  - Serial interface for integration with standard avionics
  - 20 Hz update rate for position/velocity

---

## Use Cases & Applications

### Primary Mission Profile
- **BLOS operations in GPS-denied areas** (urban canyons, high latitudes, high altitudes, RF jamming/spoofing scenarios)
- **Safe return-to-home** capability when GPS is unavailable
- **Commercial UAS operations** under FAA's UAS Traffic Management (UTM) system
- **Emergency procedures:** Autonomous safe landing and mission abort

### Specific Environmental Scenarios
- Homogeneous terrain (snow-covered plains, large bodies of water) where optical flow alone is insufficient
- Low-light and inclement weather conditions (addressed via signals of opportunity backup)
- Nighttime operations (potential future capability)
- Both fixed-wing and multirotor platforms

---

## Phase I Technical Objectives & Milestones

### Objectives
1. Develop and flight-test inertial navigation hardware and algorithms
2. Design and validate vision-based absolute positioning algorithms
3. Assess feasibility of signals of opportunity (VOR, TV, cellular, WiFi)
4. Develop plan for GPS spoofing detection

### Deliverables (6-month Phase I)
1. **Inertial Navigation Hardware Prototype:** Integrated IMU/pressure/optical flow system on S2 UAS; Jetson TX2 processing
2. **Flight Test Data:** Inertial solution performance validation in varying wind conditions
3. **Absolute Position Algorithm Demonstration:** Vision algorithms tested on geotagged photos; performance validated on embedded hardware
4. **GPS Spoofing Detection Plan:** Survey of detection techniques; hardware selection and simulation methodology
5. **Signals of Opportunity Assessment:** Feasibility evaluation of RF navigation sources for IFR operations

### Phase II Objectives (not executed in this proposal)
- Complete vision-based absolute position system implementation
- Sensor fusion integration
- Full system flight testing

---

## Key Technical Details & Innovations

### Optical Flow Integration
- **Challenge:** Accurate range estimation to scale optical flow velocity; performance degradation over homogeneous terrain
- **Solution:** Laser altimeter (4cm accuracy to 120m; longer-range systems for higher altitudes); DEM data fallback; wind estimation to maintain accuracy when optical flow degrades

### Vision-Based Localization Techniques
- **Keyframe Following:** Lightweight; relies on GPS loss detection accuracy; requires retracing flight path
- **SLAM:** Denser mapping; higher computational load; risk of position divergence if localization fails
- **Semantic Segmentation:** Deep learning for road/coastline detection; demonstrates feasibility for structured features

### Wind Estimation
- Unscented Kalman Filter fuses optical flow, true airspeed (from dynamic pressure), attitude, and inertial measurements
- Critical for maintaining inertial navigation accuracy during GPS-denied periods over wind-affected flights

### GPS Spoofing Detection
- Monitors AGC and C/N₀ ratio changes; exploits characteristic signature differences between legitimate satellite signals and spoofed signals
- Literature-based approach; Phase I assessment to select implementation method

---

## Related BST Capabilities & Prior Work

### Ongoing BST Research Areas
1. **Preventative Maintenance:** Machine learning algorithms for onboard subsystem health monitoring
2. **Autonomous Safe Landing:** NASA-funded effort for automatic detection of safe landing areas in loss-of-propulsion scenarios
3. **Machine Vision:** Deep learning for semantic segmentation (safe landing area identification, road detection)
4. **Cooperative Multi-UAS Operations:** Networked command/control of heterogeneous platforms

### Prior Experience
- Dr. Elston's background: Tornadic supercell penetration (VORTEX2), high-altitude fixed-wing operations, extensive COA approvals
- Dr. Stachura: 300+ flight experiments, 140+ FAA Certificates of Authorization, airworthiness review processes
- Team expertise: UAS design, avionics integration, atmospheric sampling in hazardous conditions

---

## Competitive Advantages

1. **Integrated Hardware/Software:** Leverages existing SwiftCore avionics; reuses proven algorithms and hardware
2. **Flight-Ready Platform:** S2 UAS provides immediate integration and validation pathway
3. **Multi-Modal Absolute Positioning:** Combines vision, SLAM, road-following, and RF signals (robustness to single-mode failure)
4. **Regulatory Alignment:** Designed explicitly for FAA UTM system requirements
5. **Commercial Viability:** Standalone, affordable package interchangeable with standard GPS receivers

---

## Regulatory & Safety Context

### FAA/UTM Requirements Addressed
- BLOS operations require performance authorization in 4 areas: navigation, communications, intent-sharing, collision avoidance, and real-time FAA connectivity
- BST positioned this as critical gap: reliable positioning in GPS-denied scenarios
- Compatible with case-by-case evaluation pathway toward streamlined approvals

### Safety Criticality
- Position information essential for:
  - Safe separation from other aircraft
  - Hazard avoidance on ground
  - Emergency procedures (return-to-home, safe landing)
  - Continuous reporting to UAS Service Supplier (USS) in UTM

---

## Notable Details

- **Team Size:** 6 employees (as of January 2019)
- **Company Status:** Small Business; no venture capital/private equity ownership
- **Federal Funding:** $116,095 Phase I contract
- **Location:** Boulder, Colorado (3200 Valmont Rd, Ste 7)
- **Prior NOAA SBIR Success:** Referenced previous Phase I effort in which aircraft was fully designed and flown
- **Interdisciplinary Approach:** Integrates inertial navigation, computer vision, machine learning, RF engineering, and autopilot design
- **Document Quality:** Technically detailed with clear system diagrams, Gantt charts, performance analysis, and literature citations

---

## Assessment Notes

This Phase I proposal demonstrates strong technical depth and practical focus on a well-defined regulatory gap. The DS-GPS system directly addresses FAA/UTM requirements and builds on BST's existing avionics infrastructure. The proposal balances ambitious flight testing (Phase I prototype) with feasible Phase I deliverables (algorithm development, feasibility studies) and clear Phase II implementation roadmap. Key risk areas acknowledged: optical flow reliability in homogeneous terrain, computational overhead of SLAM, practical spoofing detection implementation, and RF signal availability in diverse geographic conditions. The team's extensive UAS operational experience (150+ publications, 300+ flight experiments) provides strong credibility for execution.