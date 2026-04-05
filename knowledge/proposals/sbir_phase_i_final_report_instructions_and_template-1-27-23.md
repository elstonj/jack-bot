# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking and Classification - Phase I Final Report

## Document Metadata
- **Type:** SBIR Phase I Final Report
- **Client/Agency:** U.S. Department of the Navy (DON), Naval Air Warfare Center (NAVAIR)
- **Program/Solicitation:** SBIR Topic N251-016
- **Date:** Phase I Period: July 30, 2025 – January 12, 2026 (document prepared by March 2026)
- **Contract Number:** N6833525C0492
- **BST Products/Systems Referenced:** S0 UAS (Air-Deployed), S1 UAS (testing platform), SwiftPilot (command and control)
- **Key Personnel:** 
  - Jack Elston (CEO, Principal Investigator)
  - Maciej Stachura (Report Prepared By)
  - Angel R. Ruiz-Reyes (Navy TPOC)

## Executive Summary

Black Swift Technologies conducted a Phase I feasibility study to modify the BST S0 unmanned aerial system (UAS) for integration into the Navy's P-8A Poseidon aircraft as an expendable sonobuoy-launched asset supporting anti-submarine warfare (ASW) operations. The research established technical feasibility for integrating a high-sensitivity magnetometer (QuSpin QTFM Gen-2), deployable passive acoustic hydrophone sensor, and AI compute module (NVIDIA Jetson AGX Orin) within strict Size, Weight, and Power (SWaP) constraints of a standard LAU-126A Sonobuoy Launch Container (SLC). Ground and flight testing demonstrated that the platform's magnetic noise floor is manageable at five-foot separation distance, achieving 1.5 pT/√Hz—below the Navy's 20 pT/√Hz threshold—while maintaining total system weight under the 39-pound maximum.

## Technical Approach

### Core Methodology
- **Systems Engineering Focus:** Integration of commercial-off-the-shelf (COTS) sensing technologies into the existing S0 platform to meet SWaP-C requirements
- **Test-Heavy Approach:** Spectral density analysis to characterize magnetic noise floor relative to Navy thresholds; ground and flight testing to validate assumptions
- **Dual-Aircraft Architecture:** Program decision to split magnetic and acoustic sensing into two separate S0 variants to maximize mission flexibility and sensor performance

### Key Design Decisions
1. **Magnetometer Integration:** QuSpin QTFM Gen-2 mounted on extendable nose boom to achieve 5-foot separation from electric motor, with optional MuMetal magnetic shielding around motor
2. **Acoustic Subsystem:** Collaboration with Ultra Maritime (replacing initial Cetacean Research Technology partnership) and Cetacean Research Technology to design lightweight hydrophone with independent battery power and fiber-optic tether transmission
3. **Compute Architecture:** NVIDIA Jetson AGX Orin 64GB for edge processing and machine learning, integrated with existing S0 avionics
4. **Platform Modifications:** Modified battery using pouch cells (reduced magnetic interference), widened fuselage, extendable boom design, water-sealed avionics compartment with foam buoyancy layer

## Products & Capabilities Described

### S0 Air-Deployed UAS (Modified Variants)

**S0-MAD Variant (Magnetometer Aircraft)**
- Integrates QuSpin QTFM Gen-2 magnetometer on nose boom
- Houses NVIDIA Jetson AGX Orin compute module in widened fuselage
- Modified pouch-cell battery to reduce electromagnetic interference
- Specifications:
  - Cruise speed: 70 knots (modified from 50 knots baseline)
  - Endurance: 120 minutes (exceeds 70-minute Navy requirement)
  - Operational altitude: 50–2,000 ft
  - Range: 20 nm LOS (extending to 50 nm with modification)
  - Weight: 15.6 lbs base platform; total system under 39 lb requirement
  - Stowed dimensions: 4.875 in. diameter × 36 in. length (fits LAU-126A SLC)
  - Payload volume: >94.4 cubic inches
  - Operational life: 5 years shelf life (objective: 9 years)

**S0-Acoustic Variant (Hydrophone Aircraft)**
- Designed for controlled water landing and hydrophone deployment
- Houses UM multi-sensor acoustic payload (hydrophone + E-field sensors)
- Water-sealed, foam-buoyed avionics compartment
- Stores 200-foot fiber-optic tethered hydrophone assembly beneath wing pivot
- Uses frangible belly deployment mechanism

### Sensor Payloads

**QuSpin QTFM Gen-2 Magnetometer**
- **Performance:** 3 pT/√Hz in-air noise level (exceeds Navy requirement of 20 pT/√Hz)
- **Measurement bandwidth:** 500 Hz (exceeds 100 Hz requirement)
- **Range:** ±150 μT (exceeds 100 μT requirement)
- **Heading error:** <3 nT uncompensated
- **Operating temperature:** -15°C to 55°C (exceeds -20°C to 50°C requirement)
- **Physical specs:** Sensor head 17.7 × 19.8 × 35.8 mm (12 g), ECU housing 14.7 × 24.4 × 92.3 mm (29 g)
- **Power consumption:** 2.5 W nominal, 3.5 W during startup

**Ultra Maritime Acoustic Sensor Suite**
- **Acoustic frequency coverage:** 5 Hz – 40 kHz (omnidirectional hydrophone)
- **E-field frequency coverage:** 0.01 Hz – 5 Hz (two pairs of ULF and ELFE probes)
- **Hydrophone design:** Acceleration-cancelling design with very low noise preamplifier (10+ dB below Q53H CO specification; 6-8 dB improvement possible with textured ceramic)
- **Operating depth:** 200 ft threshold (400 ft objective)
- **Deployment time:** 120 seconds gravity-based (60 seconds objective)
- **Operating life:** 60 minutes threshold, 70 minutes objective
- **Sensor calibration accuracy:** ±2 dB threshold (±1 dB objective)
- **Detection range:** 20 nm LOS (50 nm objective with increased RF power)
- **Physical packaging:** 4-inch diameter × 6.5-inch length (81.7 cubic inches), with suspension system to reduce mechanically-induced noise
- **Power consumption:** <2.5 W for acoustic sensor; ~5 W with RF communications

**NVIDIA Jetson AGX Orin 64GB Compute Module**
- **AI Performance:** 275 TOPS (meets Navy requirement)
- **GPU:** 2048-core with 64 Tensor cores, max frequency 1.3 GHz
- **CPU:** 12-core @ 2.2 GHz
- **Memory:** 64 GB RAM
- **Power consumption:** 15 W – 60 W
- **Physical dimensions:** 110 mm × 110 mm × 71.65 mm
- **Function:** Edge processing, machine learning-based submarine detection/classification, onboard data fusion

### Command & Control
- **SwiftPilot:** Existing BST command and control system; planned extension to UAS Control Segment (UCS) architecture in Phase II
- **Autonomous capabilities:** Pre-programmed waypoint tracks, autonomous target cueing hooks (tested in non-MAD variants)
- **Control interface:** Portable control tablet

## Use Cases & Applications

### Primary Mission
- **Anti-Submarine Warfare (ASW) for U.S. Navy P-8A Poseidon aircraft**
- Cued search, detection, localization, tracking, and classification of hostile submarines
- Maritime Domain Awareness operations in task force protection scenarios

### Operational Concept
1. Sonobuoy-launched deployment from P-8A Poseidon via LAU-126A launch container
2. Two-aircraft distributed search: S0-MAD performs magnetic anomaly detection on signal-based flight patterns; S0-Acoustic executes controlled water landing and deploys tethered hydrophone
3. Coordinated cueing: MAD detections trigger targeted acoustic deployment; acoustic localizations cue refined MAD search patterns
4. On-board machine learning processes both magnetic and acoustic sensor data for autonomous target classification
5. Automated mission termination with classified data sanitization and platform scuttling

### Extended Applications
- NOAA hurricane operations (existing S0 operational use)
- Air Force use cases (noted as expansion target)
- Volcanic and geological monitoring (implied by broader platform capabilities)

## Key Results

### B.1: Requirements Analysis and Preliminary Design

**Component Selection Validation:**
- QuSpin QTFM Gen-2 meets all Navy magnetometer specifications with margin
- NVIDIA Jetson AGX Orin selected for 275 TOPS AI performance and sufficient compute density; despite being largest internal component, confirmed to fit within S0 launch tube
- Acoustic hydrophone design feasibility confirmed through collaboration with industry expert (Ultra Maritime)

**Integration Feasibility:**
- S0 platform inherently compatible with SLC constraints; total package weight 15.6 lbs (well under 39 lb maximum)
- Payload volume of modified S0 exceeds 94.4 cubic inch requirement
- 200-foot fiber-optic tethered hydrophone assembly can be stored within aft fuselage compartment

### B.2: Platform Modifications

**Mechanical Compatibility:**
- Folded S0 airframe with deployment tube closely matches weight, size, and center of gravity of existing 36B BT expendable assets
- Ensures identical launch dynamics to current sonobuoy operations; >30 drops through P-3 free-fall chute without separation issues
- Full SLUAV system meets MIL-L-81745B loading specification (~10G for 100ms)

**Design Modifications Completed:**
- Battery redesigned with pouch cells to reduce electromagnetic interference from steel cases
- Fuselage widened underneath wing to accommodate Jetson SBC and maximize motor-sensor separation
- Extendable nose boom design for magnetometer mounting at optimal 5-foot separation
- S0-Acoustic variant includes water-sealed, foam-buoyed avionics compartment and frangible belly deployment mechanism for 200-foot hydrophone assembly

### B.3: Sensor Integration and Testing

#### Magnetometer Testing Results

**S1 Flight Testing (Surrogate Platform):**
- Identified significant heading error (120–150 nT) and high-frequency aliasing from motor throttling
- Platform noise measured at 250–600 pT/√Hz (10–30x requirements), attributed to proximity of larger S1 motor
- Aliasing identified as primary issue (filters ineffective); motor shielding previously demonstrated 10x noise reduction

**S0 Ground Testing (Primary Platform):**
- **Distance-dependent measurements (RMS and spectral density analysis):**
  - 50 ft: 1.5 pT/√Hz (meets requirement)
  - 20 ft: 1.4 pT/√Hz (meets requirement)
  - 10 ft: 1.4 pT/√Hz (meets requirement)
  - **5 ft: 1.4 pT/√Hz – twice as good as 20 pT/√Hz requirement**, providing design margin
  - 0 ft: 34.9 pT/√Hz (exceeds requirement due to proximity)

- **Frequency analysis:**
  - Full frequency range (0–100 Hz) stays below Navy threshold except at 60 Hz (expected from ground-based power line noise)
  - At 5-foot and 2.5-foot distances: no throttle-induced noise visible
  - 400 MHz communications antenna noise detected at 0 and 2.5 ft; antenna relocated to >2.5 ft in updated CAD

- **Key Finding:** 5-foot nose boom separation provides acceptable magnetometer placement without requiring towed sensor design or additional shielding; 2.5-foot separation also viable with updated antenna placement

**Shielding Development:**
- MuMetal magnetic shielding material sourced and prototyped around S0 motor
- Prototype demonstrates feasibility; reserved for Phase II testing if required or for enhanced performance

**Calibration Strategy:**
- In-flight calibration procedure developed (figure-eight patterns, ~5 