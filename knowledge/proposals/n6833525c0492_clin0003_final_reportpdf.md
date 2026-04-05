# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking and Classification

## Document Metadata
- **Type:** Phase I SBIR Final Report
- **Client/Agency:** U.S. Navy, Naval Air Warfare Center (NAVAIR)
- **Program/Solicitation:** SBIR Topic N251-016
- **Contract Number:** N6833525C0492
- **Date:** January 12, 2026
- **Period of Performance:** July 30, 2025 – January 12, 2026
- **BST Products/Systems Referenced:** S0 UAS (Air-Deployed), S1 UAS (surrogate platform for testing)
- **Key Personnel:** 
  - Jack Elston (CEO, Principal Investigator)
  - Maciej Stachura (Prepared by)
  - TPOC: Angel R. Ruiz-Reyes (Navy)

---

## Executive Summary

Black Swift Technologies successfully demonstrated the technical feasibility of modifying the S0 UAS platform to integrate a high-sensitivity QuSpin QTFM Gen-2 magnetometer and a deployable passive acoustic hydrophone sensor within strict SWaP constraints of the LAU-126A Sonobuoy Launch Container (SLC). Phase I work encompassed platform design modifications, electromagnetic interference characterization, and preliminary design of a fiber-optic tethered hydrophone system. Ground testing confirmed that magnetic noise from the electric motor dissipates to acceptable levels at 5 feet distance, with spectral density below Navy's 20 pT/√Hz threshold. The S0 UAS fits within SLC dimensions at 15.6 lbs, maintaining the 39 lb maximum weight limit. The research established that the proposed Sonobuoy-Launched (SL) UAS design is viable for Navy anti-submarine warfare operations, with principal risk areas (platform noise and packaging density) effectively mitigated through design and testing.

---

## Technical Approach

**Systems Engineering Focus:**
The approach integrated commercial-off-the-shelf (COTS) sensing technologies into BST's S0 UAS to meet the LAU-126A SLC constraints. The methodology prioritized:
1. Mitigation of magnetic interference from the aircraft's electric propulsion system
2. Development of a lightweight deployable acoustic sensor
3. Validation through incremental ground and flight experiments

**Test-Heavy Methodology:**
- Spectral density analysis to characterize magnetic noise floor relative to Navy threshold of 20 pT/√Hz
- Goal was to prove through ground testing that the QuSpin magnetometer could be positioned on the S0 and remain below threshold requirements with all aircraft systems running (no shielding initially)
- Magnetic shielding (MuMetal) and sensor boom reserved for Phase II refinement

**Acoustic Subsystem Development:**
- Collaboration with Cetacean Research Technology (CRT) for initial design
- Modeling of hydrodynamic drag and sink rate to ensure 200-foot deployment within 120-second threshold
- Transitioned to Ultra Maritime (UM) as acoustic provider to optimize low-frequency performance and maintain packaging constraints

**Architecture Integration:**
- NVIDIA Jetson AGX Orin 64GB compute module for edge processing and AI capabilities
- Primary-chemistry battery (A23 cell) powering hydrophone locally to avoid power draw from UAS
- Fiber-optic tether (lightweight alternative to copper cabling) for data transmission from hydrophone to circling aircraft

---

## Products & Capabilities Described

### BST S0 UAS
**What it is:** An air-deployed, Group 1 unmanned aerial system designed for expendable operations, already in operational use by NOAA for hurricane operations.

**Specifications:**
- **Weight (package in tube):** 15.6 lbs (meets 39 lb Navy maximum)
- **Dimensions (stowed):** 5" × 37" currently (compatible with LAU-126A SLC: 4.875" × 36")
- **Cruise speed:** 50 knots current; capable of 70 knots with modified motor/propeller
- **Endurance:** 120 minutes (exceeds Navy 70-minute threshold)
- **Operational altitude:** 30–10,000 feet (Navy requirement: 50–2,000 ft)
- **Payload volume:** Greater than 94.4 cu. in.
- **Temperature range:** -40°C to 50°C (Navy: -20°C to 50°C)
- **Range:** 270 nm (Navy LOS requirement: 20 nm extending to 50 nm)
- **Command & Control:** BST SwiftPilot (to be extended to UAS Control Segment architecture in Phase II)

**Proposed Use in ASW Context:**
- Two variants planned: S0-Acoustic (executes water landing, deploys hydrophone) and S0-MAD (conducts magnetic anomaly detection via signal-based flight patterns)
- Platform supports AI/ML algorithms for autonomous target classification and data fusion
- Designed to support classified algorithm loading immediately prior to launch; automated sanitization erases all classified data before battery exhaustion
- Must scuttle upon mission completion to prevent exploitation

---

### QuSpin QTFM Gen-2 Magnetometer
**What it is:** Optically pumped atomic scalar magnetometer selected for high sensitivity and compact form factor.

**Specifications:**
- **MAD in-air noise level:** 3 pT/√Hz (Navy requirement: 20 pT/√Hz) – superior performance
- **Measurement bandwidth:** 500 Hz (Navy min: 100 Hz)
- **Range:** 150 µT (Navy min: 100 µT)
- **Temperature range:** -15°C to 55°C (Navy: 0°C to 50°C)
- **Heading error:** <3 nT uncompensated (meets requirement)
- **Size:** 17.7×19.8×35.8 mm (sensor head); 14.7×24.4×92.3 mm (ECU housing)
- **Weight:** 12g (sensor head) + 29g (electronics/ECU)
- **Power:** +5V or 10-12V input; 2.5W typical, 3.5W during startup

**Proposed Integration:**
- Sensor head mounted on small nose boom (5 feet from aircraft) to isolate from motor interference
- ECU housed in S0 fuselage, directly integrated with aircraft avionics
- MuMetal magnetic shielding planned around electric motor to reduce dynamic noise
- In-flight calibration option (figure-eight patterns) to mitigate heading errors

---

### NVIDIA Jetson AGX Orin 64GB
**What it is:** Single-board computer (SBC) for edge AI processing and data fusion.

**Specifications:**
- **AI Performance:** 275 TOPS (meets Navy requirement)
- **GPU cores:** 2048 CUDA cores with 64 Tensor cores
- **CPU cores:** 12-core @ 2.2 GHz
- **Memory:** 64 GB RAM (meets Navy requirement)
- **Max GPU frequency:** 1.3 GHz (meets requirement)
- **Size:** 110mm × 110mm × 71.65mm (largest internal component but fits within launch tube)
- **Power:** 15–60W

**Proposed Use:**
- Supports real-time ML algorithms for submarine detection, classification, localization
- Enables sensor data fusion from magnetic and acoustic modalities
- Sufficient for autonomous operations and coordinated platform cueing

---

### Hydrophone/Acoustic Sensor
**What it is:** Deployable passive acoustic sensor developed in collaboration with Cetacean Research Technology (CRT) and optimized by Ultra Maritime (UM).

**Proposed Specifications:**
- **Operating life:** 70 minutes (Navy threshold: 60 min; objective: 70 min)
- **Max operating depth:** 200 feet (Navy threshold; objective 400 ft)
- **Deployment time:** 120 seconds gravity-based (Navy threshold)
- **Frequency coverage:** 1 Hz – 25 kHz
- **Sensor directivity:** Omnidirectional (threshold); higher gain/direction-finding objective
- **Calibration accuracy:** ±2 dB (Navy threshold)
- **Detection range:** >20 nm (Navy 20 nm LOS extending to 50 nm)
- **Size:** 1" diameter × 2" length; 2mm diameter fiber-optic tether × 200 feet
- **Power:** ~30 mA @ 12VDC (via A23 primary-chemistry battery in hydrophone)

**Architecture:**
- Self-powered via A23 primary-chemistry battery integrated in hydrophone housing
- Microphone, ADC, battery, data transmission device potted in water-tight housing
- Water-sensitive switch activates upon submersion
- Data transmission via lightweight fiber-optic tether (reduces weight vs. copper cabling)
- Stored in aft fuselage of S0 during flight; deployed after water landing
- Scuttling mechanism (automatic based on battery life remaining; objective: also on-command)

**Acoustic Sensor Variants (Ultra Maritime Recommendations):**
1. **CO (Calibrated Omnidirectional):** 5 Hz – 40 kHz; simplest/lowest cost; modified version from UM's Q53H sonobuoy; achievable 6–8 dB reduction in self-noise
2. **Directional Hydrophones:** 5 Hz – 2.5 kHz; larger/more complex; provide bearing estimation and directivity
3. **E-Field Sensing:** 0.01 Hz – 5 Hz (splits into ULF: 0.05–20 mHz and ELFE: 0.5–10 Hz); alternative technology for low-frequency extension; less susceptible to platform motion noise; very low data rates

**Packaging:** Notional 4" diameter × 6.5" length (81.7 cu. in. volume) including suspension system for vibration isolation.

---

## Use Cases & Applications

**Primary Mission:** Anti-Submarine Warfare (ASW) for U.S. Navy P-8A Poseidon aircraft

**Operational Concept:**
1. **Deployment:** SL UAS launches from P-8A via LAU-126A Sonobuoy Launch Container
2. **Search & Detection:** 
   - S0-MAD variant conducts signal-based flight patterns to detect submarine magnetic signatures
   - S0-Acoustic variant executes water landing and deploys tethered hydrophone for passive acoustic monitoring
3. **Coordinated Operations:**
   - Magnetic detections cue targeted deployment of acoustic platforms
   - Acoustic localization fixes cue refined search patterns for magnetic variant
   - Machine-learning algorithms fuse multi-modal sensor data for classification
4. **Autonomy:** Pre-programmed waypoint flights with hooks for autonomous target tracking
5. **Operator Control:** Manual adjustment of search patterns via SwiftPilot control tablet (extends to UAS Control Segment architecture in Phase II)
6. **End-of-Mission:** Automated scuttling upon mission completion or battery exhaustion

**Key Tactical Advantages:**
- Expendable asset—no recovery required (reduces platform security burden)
- Distributed, collaborative sensing from complementary sensor modalities
- AI-driven autonomous operations with rapid sensor fusion
- Support for Maritime Domain Awareness and task force protection

---

## Key Results

### B.1 Requirements Analysis and Preliminary Design

**Component Selection Validation:**
- **Jetson AGX Orin 64GB:** Confirmed fits within BST launch tube; satisfies 275 TOPS AI requirement and 64 GB RAM requirement
- **QuSpin QTFM Gen-2:** Superior 3 pT/√Hz in-air noise (vs. 20 pT/√Hz requirement); 12g sensor head allows nose-boom mounting; compact ECU integrates directly with avionics
- **Hydrophone (CRT/UM):** Feasible design with self-powered architecture; 1 Hz – 25 kHz frequency range addresses Navy requirements within SWaP envelope; fiber-optic tether reduces weight vs. copper alternatives
- **S0 UAS Platform:** Already inherently compatible with SLC constraints; 15.6 lbs package meets 39 lb threshold; existing endurance/speed/altitude capabilities meet Navy requirements

**Design Decisions:**
- Decision made to split magnetic and acoustic sensing into two separate UAS variants to maximize mission flexibility
- Switched acoustic provider from CRT to Ultra Maritime (UM) to better achieve low-range measurements and maintain small package size
- Option preserved to integrate both sensors on single