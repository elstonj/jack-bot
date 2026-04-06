# Development of a Sonobuoy-Launched UAS with Advanced MAD and Acoustic Sensing Capabilities – Phase I Progress Report

## Document Metadata
- **Type:** SBIR Phase I Progress Report
- **Client/Agency:** Department of the Navy / NAVAIR (Office of Naval Research)
- **Program/Solicitation:** SBIR Topic N251-016; Proposal N251-016-0021
- **Contract Number:** N6833525C0492 CLIN0002
- **Date:** October 14, 2025 (covering July 30 – October 14, 2025)
- **Classification:** Unclassified; ITAR Restricted Topic; Distribution Statement B
- **BST Products/Systems Referenced:** S0 Air-Deployed UAS, SwiftPilot (C2 system)
- **Key Personnel:** Dr. Jack Elston (Principal Investigator), Alex Lomis (last editor)
- **Data Rights Expiration:** January 12, 2030

---

## Executive Summary

Black Swift Technologies is developing a Sonobuoy-Launched Unmanned Aerial System (SL UAS) based on the S0 platform, integrating a QuSpin QTFM Gen-2 magnetometer for Magnetic Anomaly Detection (MAD) and a passive hydrophone sensor for Anti-Submarine Warfare (ASW) target detection, localization, and classification. Phase I has established technical feasibility through requirements analysis, preliminary design, and critical ground/flight testing demonstrating magnetometer performance and platform compatibility with Navy sonobuoy launcher constraints.

---

## Technical Approach

### Overall System Architecture
- **Base Platform:** Modified BST S0 Air-Deployed UAS, designed to fit within LAU-126A Sonobuoy Launch Container (SLC)
- **Deployment Method:** Launched from P-8A maritime patrol aircraft sonobuoy launcher at high altitude; recoverable via parachute or expendable upon water landing
- **Core Objective:** Integrate sensitive MAD and passive acoustic sensing while meeting rigorous payload, SWAP, and operational constraints

### Key Subsystems and Integration Strategy

#### 1. **Magnetometer (Magnetic Anomaly Detection)**
- **Sensor:** QuSpin QTFM Gen-2
  - Measurement bandwidth: 500 Hz (exceeds 100 Hz requirement)
  - Range: 150 μT (exceeds 100 μT requirement)
  - In-air noise: 3 pT/√Hz (significantly exceeds 20 pT/√Hz requirement with 6.7× margin)
  - Heading error: <3 nT uncompensated (meets requirement)
  - Temperature range: −15 °C to 55 °C (exceeds 0–50 °C requirement)
  - **SWAP:** Sensor head 17.7×19.8×35.8 mm (12g) + ECU housing 14.7×24.4×92.3 mm (29g), 2.5 W nominal (3.5 W startup)

- **Mounting & Interference Mitigation:**
  - Sensor head mounted on small boom extending past S0 nose to separate from power/propulsion electronics
  - ECU integrated into S0 fuselage, directly connecting to avionics
  - **MuMetal shielding** applied around electric motor to reduce dynamic noise up to 10× (from motor field measurements)
  - In-flight calibration procedure planned: figure-eight patterns at ~120 m altitude (~5 minutes) to correct heading-based errors; achievable within ~75 min total endurance

- **Critical Test Results:**
  - Ground testing of S0 with motor at cruise power showed platform noise of ~1.5 pT/√Hz at distances ≥5 ft, meeting requirement
  - Noise at motor location (0 ft) measured 34.9 pT/√Hz; mitigation via boom separation and shielding expected to resolve
  - S1 flight test (larger reference platform) showed 250–600 pT/√Hz noise (10–30× requirement), primarily due to suboptimal motor positioning and larger motor (2.5× S0)
  - Heading errors of 120–150 nT observed; in-flight calibration expected to mitigate

#### 2. **Passive Hydrophone Sensor**
- **Partner:** Cetacean Research Technology (CRT)
- **Sensor Type:** Microphone-based acoustic hydrophone with integrated ADC, primary-chemistry battery, and fiber-optic data link
  - **Frequency range:** 1 Hz – 25 kHz (Navy threshold: 0.01 Hz–2.5 kHz; objective: 0.001 Hz–25 kHz)
    - Lower frequencies rejected due to: large sensor size, ADC saturation, platform motion noise, complexity of pre-amp design, and suspension challenges at low frequencies
    - Alternative technology identified: Electric-field measurements (practical DC–3 kHz) proposed as lower-cost, lower-complexity option with better platform motion immunity
  - **Operational life:** 70 minutes expected (threshold 60 min, objective 70 min)
  - **Max depth:** 200 ft threshold (objective 400 ft)
  - **Deployment:** 120 sec gravity-based deployment (objective 60 sec)
  - **Scuttle:** Automatic (commanded by BST autopilot) and on-command
  - **Directionality:** Omnidirectional (threshold); objective includes higher gain/direction-finding
  - **Calibration accuracy:** ±2 dB (threshold); ±1 dB (objective)
  - **Detection range:** >20 nm (Navy requirement 20 nm LOS, extending to 50 nm)
  - **SWAP:** 1″ dia. × 2″ length sensor; 2 mm × 200 ft fiber-optic cabling; 30 mA @ 12 VDC; A23 battery (12 V, 55 mAh)

- **Deployment Architecture:**
  - Hydrophone assembly + 200 ft fiber-optic spool stored in S0 aft fuselage
  - Water-activated switch initiates battery power upon water contact
  - Free-fall deployment; fiber-optic data link back to UAS (lightweight, reduced bandwidth vs. copper conductors)
  - Data re-broadcast via UAS primary communications antenna
  - Eliminates need for UAS power to hydrophone (reduces UAS SWAP impact)

#### 3. **Compute Platform**
- **Processor:** NVIDIA Jetson AGX Orin 64GB
  - AI Performance: 275 TOPS (meets 275 TOPS requirement)
  - GPU: 2048 CUDA cores, 64 Tensor cores, 1.3 GHz max frequency
  - CPU: 12-core @ 2.2 GHz
  - Memory: 64 GB RAM
  - **SWAP:** 110 × 110 × 71.65 mm; 15–60 W power
  - Intended for data fusion algorithms, real-time signal processing, and machine learning-based detection/classification
  - Fits within existing BST launch tube stored in SLC

#### 4. **UAS Platform (BST S0)**
- **Current Specifications (unmodified):**
  - **Packaging:** Deployment tube fits LAU-126A SLC; folded airframe stores within tube
  - **Weight (UAV + tube):** 15.6 lbs (meets 39 lb max requirement)
  - **Stowed dimensions:** 5″ × 37″ (meets 4.875″ dia. × 36″ length requirement; may be downsized further)
  - **Shelf life:** 5 years (Navy requires 9 years; to be addressed in Phase II)
  - **Launch envelope:** Matches sonobuoy specification; >30 drops via P-3 without separation issues
  - **Cruise speed:** 50 kts current, dashed to 70 kts (meets 70 kt requirement with motor/propeller upgrade)
  - **Endurance:** 120 minutes (exceeds 70 min requirement)
  - **Operational altitude:** 30–10,000 ft (exceeds 50–2,000 ft requirement)
  - **Range:** 270 nm (exceeds 20 nm LOS and 50 nm objective)
  - **Payload volume:** Sufficient for Jetson, magnetometer, hydrophone reel (exceeds 94.4 in.³)
  - **Temperature range:** −40 °C to 50 °C (exceeds −20 °C to 50 °C requirement)
  - **Precipitation capability:** Heavy rain with zero visibility (exceeds light rain requirement)
  - **Autonomy:** Pre-programmed waypoints with autonomous queuing hooks (tested with non-MAD payloads)
  - **Command & Control:** BST SwiftPilot system; to be extended to Navy UAS Control Segment (UCS) architecture in Phase II
  - **Cost:** $18,000 qty 1 (Navy requirement <$10,000 @ qty 100; BST expanding production from ~50/year toward hundreds)

- **Planned Modifications (Task B.2):**
  - Boom integration for magnetometer sensor head (5+ ft separation minimum)
  - Motor shielding (MuMetal) integration
  - Jetson AGX Orin 64GB installation
  - Hydrophone reel + 200 ft fiber-optic spool in aft fuselage
  - Aerodynamic and structural modifications for payload integration while maintaining sonobuoy launch compatibility
  - Target completion: ~one month post-report

---

## Products & Capabilities Described

### BST S0 Air-Deployed UAS
- **What it is:** Fully autonomous, expendable small Tier-1 UAS designed for air deployment from fixed-wing aircraft; currently operational with NOAA
- **Proposed use:** Modified version to serve as Sonobuoy-Launched UAS (SL UAS) with integrated MAD and acoustic sensors for Navy ASW operations
- **Key capability:** Compact, robust airframe capable of integration with complex sensor suites while maintaining sonobuoy launcher compatibility
- **Performance margin:** Exceeds most Navy requirements for speed, endurance, range, altitude, and SWAP; modifications focus on sensor integration and operational integration with P-8A

### BST SwiftPilot
- **What it is:** BST's proprietary command and control system
- **Proposed use:** Phase I control of autonomous mission execution; planned extension to Navy UAS Control Segment (UCS) architecture compatibility in Phase II
- **Capability:** Supports autonomous target tracking based on MAD and acoustic cues (Objective 5)

### QuSpin QTFM Gen-2 Magnetometer
- **What it is:** Optically-pumped alkali-vapor quantum magnetometer offering ultra-low noise magnetic field measurement
- **Proposed use:** Primary MAD sensor for submarine detection via magnetic signature anomaly
- **Key performance advantage:** 3 pT/√Hz noise specification provides 6.7× margin above 20 pT/√Hz Navy requirement; meets heading error requirement without compensation

### Hydrophone Sensor (Cetacean Research Technology)
- **What it is:** Integrated passive acoustic sensor with built-in ADC, primary battery, and fiber-optic data link
- **Proposed use:** Complementary passive acoustic detection for ASW target cuing, localization, and classification; deployed to depth via gravity
- **Key advantage:** Fiber-optic data link eliminates multi-conductor cable weight/volume; primary battery independence simplifies UAS architecture

### Jetson AGX Orin 64GB
- **What it is:** NVIDIA's high-performance AI-capable edge computing platform
- **Proposed use:** Real-time sensor fusion, signal processing, machine learning-based target detection/classification
- **Capability:** Meets all Navy performance metrics (275 TOPS, 2048 CUDA cores, 64 Tensor cores, 12-core CPU, 64 GB RAM)

---

## Use Cases & Applications

### Primary: Anti-Submarine Warfare (ASW)
- **Mission:** Cued search, detection, localization, tracking, and classification of submarines via magnetic anomaly and acoustic signatures
- **Operational context:** Launched from P-8A Poseidon maritime patrol aircraft at high altitude; operates autonomously post-deployment
- **Unique advantage:** Expendable system allows deployment over extended ocean areas without recovery logistics; sensitive sensors enable rapid threat characterization

### Secondary / Transition Opportunities (noted in report)