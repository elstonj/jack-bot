# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification

## Document Metadata
- **Type:** SBIR Phase II Full Proposal (Draft)
- **Client/Agency:** U.S. Navy (NAVAIR / PMA-264)
- **Program/Solicitation:** Navy SBIR Topic N251-016
- **Date:** March 25, 2026 (prepared); March 16–27, 2026 (created/modified)
- **Contract Information:**
  - Topic No.: N251-016
  - Proposed Period of Performance: 42 months (30-month Base + 12-month Option)
  - Estimated Base Value: $998,862.00
  - Option 1 Value: $398,748.00
- **BST Products/Systems Referenced:** 
  - SØ (main airframe platform)
  - SØ-MAD (magnetic anomaly detection variant)
  - SØ-Acoustic (acoustic sensing variant)
  - SwiftPilot (autopilot with 3D wind sensing)
  - SwiftStation (control station)
  - SwiftTab (UI for UAS control)
  - SwiftFlow probe (5-hole probe for 3D wind measurement)
  - E2 multirotor (used for surrogate launch testing)
- **Key Personnel:**
  - **BST:** Dr. Jack Elston (PI, CEO); Beck Cotter (Proposal Specialist)
  - **Subcontractor:** Ultra Maritime (Paul DeMond) – acoustic/E-field sensor developer
  - **Navy TPOC:** Angel Reyes-Ruiz (NAVAIR)
  - **Sensor Partner:** QuSpin (magnetometer expertise)

---

## Executive Summary

Black Swift Technologies proposes a Phase II effort to fabricate, integrate, and validate a production-ready Sonobuoy-Launched Unmanned Aerial System (SL UAS) capable of performing magnetic anomaly detection (MAD) and deploying in-water passive acoustic sensors to support Anti-Submarine Warfare (ASW) cued search, detection, tracking, and classification. Building on successful Phase I demonstrations of magnetic noise floor <20 pT/√Hz in the 0.01–100 Hz band, Phase II will mature the system from bench-level feasibility to fully integrated, flight-validated prototypes compatible with the Navy's LAU-126A Sonobuoy Launch Container. The effort emphasizes hardening the platform for dynamic launch and flight environments, validating magnetic performance under in-flight calibration maneuvers, and demonstrating reliable deployment and operation of a multi-modal acoustic/E-field sensing subsystem within stringent size, weight, power, and cost constraints.

---

## Technical Approach

### Overall Architecture
The Phase II effort splits the sensing system into two dedicated aircraft variants based on the BST SØ platform:
- **SØ-MAD:** Optimized for low-noise magnetic anomaly detection using a QuSpin optically pumped atomic magnetometer mounted on an extendable nose boom
- **SØ-Acoustic:** Configured for water landing and deployment of a tethered acoustic sensing array (hydrophone + E-field probes)

This separation maximizes mission flexibility, keeps individual aircraft cost and size low, and enables advanced sensor fusion and swarming without co-locating incompatible sensor electronics.

### Magnetic Sensing Design (SØ-MAD)

**Platform-Level Noise Mitigation:**
- Transition from steel-cased cylindrical cells to high-density pouch cells to eliminate ferrous magnetic signatures in battery subsystem
- Widened fuselage mid-section to accommodate Single Board Computer (SBC) and maximize separation between magnetometer and propulsion system
- Extendable nose boom design to further increase standoff between sensor and electric motors
- Non-ferrous materials throughout to reduce EMI
- Boom-mounted QuSpin magnetometer with calibration-informed compensation techniques

**Magnetic Performance Target:** <20 pT/√Hz in 0.01–100 Hz band under dynamic flight conditions (Phase I achieved this in static/bench testing)

**In-Flight Validation Approach:**
- Multi-heading crossings at fixed 3D points from ≥4 different heading directions to verify scalar constancy
- Attitude variation maneuvers (bank and pitch angle changes) at ≥400 ft AGL altitude
- Characterization during representative propulsion profiles and throttling maneuvers
- Magnetic shielding of propulsion components retained as risk-reduction option if early flight data show margin erosion

### Acoustic Sensing Design (SØ-Acoustic)

**Multi-Modal Sensor Suite (developed by Ultra Maritime):**

1. **Hydrophone (5 Hz – 40 kHz):** Calibrated Omnidirectional (CO) sensor derived from Q53H production sonobuoy, with potential 6–8 dB self-noise improvement using textured ceramic material and acceleration-canceling suspension design (20+ dB wave motion isolation possible)

2. **E-Field Sensors (0.01 Hz – 5 Hz):**
   - **ELFE (Extremely Low Frequency Electromagnetic):** 0.5 Hz – 10 Hz band
   - **ULF (Ultra Low Frequency):** 0.05 mHz – 20 mHz band
   - Very simple probe pairs separated vertically for maximum aperture
   - Low-noise differential amplifiers; very low data-rate digitization
   - Successfully demonstrated under prior Navy SBIRs N091-019 and N192-060

**Deployment Mechanism:**
- Lightweight fiber-optic tether to decouple sensing elements from aircraft electrical and mechanical noise
- Gravity-assisted deployment from buoyant aircraft upon water landing
- Frangible belly compartment triggers sensor release (120 sec threshold, 60 sec objective)
- Elastically-loaded deployment system with compliance assembly and vertical damper
- Terminal weight (~2 lbs) assists gravity extraction of damper disc and sensor arrays

**Performance Targets:**
- Operating life: ≥60 min
- Deployment depth: ≥200 ft
- Frequency coverage: Full band 0.01 Hz–25 kHz
- Calibration accuracy per Navy requirements

### Onboard Processing & Autonomy

**Edge Computing Architecture:**
- NVIDIA Jetson AGX Orin 64GB (or equivalent, ≥275 TOPS AI compute required)
- Custom mechanical and electrical integration into fuselage while maintaining folding compatibility and LAU-126A fit
- Hardware-to-software interfaces for high-bandwidth data from magnetometer and acoustic/E-field suite
- Onboard data reduction protocols to transmit compressed detection results over long-range comms (rather than raw sensor streams)
- Automated sanitization process to erase classified binaries/ML models before scuttling; system remains unclassified at rest

**Autonomy Approach (Option Period):**
- Sensor-responsive autonomy enabling acoustic detections to cue search patterns with magnetometer assets
- Dual-mode coordination: Acoustic-to-Magnetic (cued intercept) and Magnetic-to-Acoustic (blind-search handoff)
- Multi-vehicle swarm logic for synchronized MAD flight patterns
- Real-time inter-vehicle communication for target localization and classification support

### Launch & Flight Performance

**Packaging:**
- LAU-126A sonobuoy launch container compatible
- Deployable wing folding mechanism
- Tube-compatible internal stowage configuration

**Flight Performance:**
- Airspeed: ≥70 kts (sustained)
- Endurance: ≥70 min
- Range/Communications: ≥20 nm line-of-sight (LOS) using existing BST long-range comms architecture
- Autonomous water landing capability (Acoustic variant) with buoyancy-preserved avionics bay
- Water-sealed electronics compartment; propulsion/battery common with MAD variant

### Environmental Hardening

**Shock & Vibration:**
- Cartridge Activated Device (CAD) launch qualification from LAU-126A (10G/100ms shock pulse)
- Folding wing hinges, SBC, QuSpin, and UM sensor array validated for structural integrity post-shock

**Environmental Qualification:**
- Thermal cycling: -20°C to +50°C
- Heavy rain survivability
- Saltwater corrosion resistance
- Stock SØ already TRL 9 for Category 5 hurricane weather; modifications maintain those capabilities

---

## Products & Capabilities Described

### SØ (Baseline Platform)
- **What it is:** Small, electric, fixed-wing UAS with deployable wings; existing TRL 9 system already demonstrated launching from NOAA P-3 and dropping from quadrotor
- **Use in this context:** Serves as the base airframe for both SØ-MAD and SØ-Acoustic variants
- **Key specs:** Compatible with sonobuoy deployment, long-range comms, modular payload integration

### SØ-MAD (Magnetic Anomaly Detection Variant)
- **What it is:** SØ airframe optimized for low-noise magnetometer operation
- **Specifications:**
  - Magnetic noise floor: <20 pT/√Hz (0.01–100 Hz band)
  - Heading error: <3 nT
  - Extendable nose boom with QuSpin optically pumped atomic magnetometer
  - Pouch-cell battery redesign to eliminate ferrous signatures
  - Non-ferrous fuselage modifications
- **Use:** Primary MAD asset; searches for magnetic anomalies; cues acoustic deployment
- **Performance targets:** Validated in flight under calibration maneuvers (multi-heading, attitude variation)

### SØ-Acoustic (Acoustic Sensing Variant)
- **What it is:** SØ airframe configured for water landing and deployable multi-modal acoustic sensing
- **Sensors integrated:**
  - Hydrophone (5 Hz – 40 kHz)
  - ELFE probe pair (0.5–10 Hz)
  - ULF probe pair (0.05–20 mHz)
  - All mounted on lightweight fiber-optic tether
- **Specifications:**
  - Operating depth: ≥200 ft
  - Operating life: ≥60 min
  - Deployment time: ≤120 sec (objective 60 sec)
  - Frequency coverage: 0.01 Hz – 25 kHz
  - Buoyant avionics bay with water-sealed compartment
  - Gravity-assisted sensor release mechanism
- **Use:** Deploys as stationary "tripwire" upon water landing; provides acoustic localization; cues MAD searches

### NVIDIA Jetson AGX Orin 64GB
- **What it is:** Onboard edge-computing module providing ≥275 TOPS of AI performance
- **Use in this context:** Hosts detection, classification, and coordination algorithms; enables low-latency processing of sensor streams
- **Integration:** Custom mechanical and electrical interfaces within fuselage; data reduction for long-range transmission

### QuSpin Optically Pumped Atomic Magnetometer
- **What it is:** High-sensitivity magnetometer (sub-picotesla sensitivity) in compact form factor
- **Use:** Primary MAD sensor on SØ-MAD; mounted on extendable nose boom to maximize separation from propulsion electronics
- **Partner role:** QuSpin provides subject matter expertise on calibration-informed compensation and flight data analysis

### Ultra Maritime Acoustic/E-Field Sensor Suite
- **What it is:** Multi-modal sensing payload including improved Q53H-derived hydrophone and paired E-field probes
- **Use:** Deployed from SØ-Acoustic via fiber-optic tether; detects submarines across 0.01 Hz–25 kHz band
- **Partner role:** Ultra Maritime serves as primary payload developer; provides physical dimensions, electrical interfaces, and field testing support

---

## Use Cases & Applications

### Primary Mission: ASW Cued Search, Detection, Tracking, and Classification
- **Scenario 1 (Acoustic-to-Magnetic Cued Intercept):**
  - SØ-Acoustic deploys as persistent stationary "tripwire"
  - Upon submarine detection, relays "Area of Interest" (AOI) to overhead/loitering SØ-MAD assets
  - SØ-MAD transitions to cooperative low-altitude magnetic search grid for precision localization and classification

- **Scenario 2 (Magnetic-to-Acoustic Blind-Search Handoff):**
  - SØ-MAD executes wide-area magnetic sweep pattern
  - Upon significant magnetic anomaly detection, c