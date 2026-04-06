# Development of a SL UAS with Advanced MAD and Acoustic Sensing Capabilities

## Document Metadata
- **Type:** SBIR Phase I Progress Report
- **Client/Agency:** Department of the Navy / NAVAIR
- **Program/Solicitation:** BAA Topic N251-016 (SBIR); Proposal Number N251-016-0021
- **Contract Number:** N6833525C0492, CLIN 0002
- **Date:** October 14, 2025
- **Reporting Period:** July 30 – October 14, 2025
- **BST Products/Systems Referenced:** S0 UAS (Air-Deployed), S1 UAS
- **Key Personnel:** Dr. Jack Elston (Principal Investigator), Meredith Needham (Last Editor)
- **Security Classification:** Unclassified, ITAR Restricted
- **Data Rights Expiration:** January 12, 2030

---

## Executive Summary

Black Swift Technologies is developing a Sonobuoy-Launched Unmanned Aircraft System (SL UAS) capable of being deployed from a P-8A aircraft at high altitude with integrated magnetic anomaly detection (MAD) and passive acoustic sensing for Anti-Submarine Warfare (ASW). Phase I focuses on establishing technical feasibility of integrating a QuSpin QTFM Gen-2 magnetometer and lightweight hydrophone into the modified S0 platform while addressing launch container constraints and sensor performance requirements.

---

## Technical Approach

### Overall Program Objective
Develop an expendable Tier 1 SL UAV launchable from P-8A sonobuoy launcher systems with:
- Sensitive magnetometer (MAD sensor)
- In-water passive acoustic sensor deployment capability
- Autonomous target search, detection, localization, tracking, and classification for ASW

### Phase I Technical Objectives

**Objective 1 – Sensor Integration Feasibility:**
- Assess integration of QuSpin QTFM Gen-2 magnetometer and lightweight hydrophone in SL UAS
- Evaluate noise mitigation strategies to minimize platform-induced interference
- Ensure hydrophone meets Navy sensitivity, frequency range (target: 1 Hz–25 kHz), and depth requirements (threshold 200 ft; objective 400 ft)

**Objective 2 – Platform Modification:**
- Modify existing S0 UAS to accommodate payload volume and weight constraints of Sonobuoy Launch Container (SLC) (LAU-126A or equivalent)
- Validate aerodynamic and structural modifications for successful launch and post-deployment operation

**Objective 3 – Sensor Performance Validation:**
- Conduct laboratory and bench testing to characterize magnetometer noise performance and hydrophone acoustic sensitivity
- Ensure compliance with Navy metrics:
  - Magnetometer noise threshold: 20 pT/√Hz in 0.01–100 Hz band
  - Hydrophone calibration accuracy: ±2 dB threshold; ±1 dB objective

**Objective 4 – Data Fusion Algorithm Development:**
- Design and implement algorithms combining MAD and acoustic sensor outputs for enhanced target detection and classification
- Evaluate real-time signal processing feasibility
- Explore machine learning-based optimization techniques using simulated datasets

**Objective 5 – Autonomous Operation and Communication:**
- Test autonomous target tracking based on MAD and acoustic sensor cues
- Validate communication and control systems for 50 nm minimum line-of-sight range (objective: 163 nm)
- Evaluate operational constraints on data transmission and onboard processing

---

## Products & Capabilities Described

### 1. **S0 Air-Deployed UAS**
**What it is:** Existing BST unmanned aircraft system currently in operational use by NOAA; planning to modify for Navy ASW mission

**Current unmodified specifications:**
- Speed: 50 kts (planned dash to 70 kts with motor/propeller modifications)
- Endurance: 120 minutes
- Operational altitude: 30–10,000 ft
- Range: 270 nm
- Payload volume: Greater than 94.4 in³
- Weight (UAV + deployment tube): 15.6 lbs
- Temperature range: -40°C to 50°C
- Autonomy: Pre-programmed waypoints with hooks for autonomous queuing
- Command & control: BST SwiftPilot (extensible to UCS architecture in Phase 2)
- Cost: $18,000 for qty 1; <$10,000 in quantities of 100

**Modifications for SL UAS:**
- Stowed dimensions: 5 in. × 37 in. (deployment tube can be downsized to 4.875 in. diameter × 36 in. length to fit 126A SLC)
- Storage: 5 years shelf life
- Designed to match weight, size, and center of gravity of existing 36B BT-type expendable assets for launch compatibility
- Can withstand 10G load for 100ms (per MIL-L-81745B specification)
- Over 30 systems have been dropped through P-3 free-fall chute without separation issues
- Payload modifications required for:
  - Jetson AGX Orin 64GB compute board
  - QuSpin QTFM Gen-2 magnetometer with boom extension
  - Hydrophone deployment system (200 ft fiber-optic cable)

**Proposed modifications for Navy requirements:**
- Cruise speed: Target 70 kts (currently 50 kts)
- Endurance: Target 120 min (currently 70 min minimum for mission)
- Operational altitude: Target 50–2,000 ft (vs. current 30–10,000 ft)
- Range: Target 20 nm LOS, extending to 50 nm (vs. current 270 nm)
- Temperature: Threshold -20°C to 50°C (vs. current -40°C to 50°C)
- Precipitation: Light rain with >1 nm visibility
- Autonomy: Threshold—fly pre-programmed waypoints/orbits; Objective—transition to autonomous target tracking cued by MAD
- C2: Phase I/II—any architecture; Phase III—UAS Control Segment (UCS) architecture

**Production capacity:** Expanding from ~50/year to potentially hundreds; cost reduction expected with volume increase

---

### 2. **Jetson AGX Orin 64GB (Compute Board)**

**What it is:** NVIDIA SBC providing AI/ML processing for real-time signal processing and data fusion

**Specifications vs. Navy Requirements:**

| Specification | Jetson AGX Orin 64GB | Navy Requirement |
|---|---|---|
| AI Performance | 275 TOPS | ≥275 TOPS |
| Max GPU Frequency | 1.3 GHz | ≥1.3 GHz |
| GPU Cores | 2048-core with 64 Tensor cores | ≥2048 CUDA cores + 64 Tensor cores |
| CPU Cores | 12-core | ≥12 |
| CPU Frequency | 2.2 GHz | 2.2 GHz |
| Memory (RAM) | 64 GB | ≥64 GB |
| Size | 110 mm × 110 mm × 71.65 mm | — |
| Power | 15W–60W | — |

**Integration notes:** Largest component to integrate; fits within BST launch tube stored in SLC

---

### 3. **QuSpin QTFM Gen-2 Magnetometer**

**What it is:** Quantum-based magnetometer for magnetic anomaly detection (MAD) for submarine detection

**Specifications vs. Navy Requirements:**

| Specification | QTFM Gen-2 | Navy Requirement |
|---|---|---|
| Measurement Bandwidth | 500 Hz | ≥100 Hz |
| Range | 150 μT | ≥100 μT |
| Temperature Range | -15°C to 55°C | 0°C to 50°C |
| MAD In-Air Noise Level | 3 pT/rHz | 20 pT/rHz |
| Heading Error | <3 nT uncompensated | <3 nT uncompensated |

**SWAP Specifications:**
- Sensor head: 17.7 × 19.8 × 35.8 mm; 12 grams
- ECU housing: 14.7 × 24.4 × 92.3 mm; 29 grams (ECU without housing: 6.5 g)
- Power: +5V input via sensor control board (SCB) or 10–12V direct; 2.5W normal, 3.5W during startup

**Integration approach:**
- Sensor head mounted on small boom extending past S0 nose to separate from power/propulsion electronics
- ECU housing mounted within S0 fuselage, directly connected to avionics
- Magnetic shielding (MuMetal) applied around S0 electric motor to reduce dynamic noise
- Calibration flights planned to further decrease magnetic noise via heading calibration

**Ground Testing Results (S0 platform):**
- At 5+ ft distance: 1.4–1.5 pT/√Hz noise (requirement: 20 pT/√Hz) — **2× better than required**
- At 0 ft (close to motor): 34.9 pT/√Hz noise
- Provides margin for aircraft integration while demonstrating feasibility

**Flight Testing Results (S1 platform):**
- Platform noise measured at 250–600 pT/rt(Hz) (10–30× requirements)
- Heading error observed at 120–150 nT due to magnetic interference from motor proximity
- Motor positioning on S1 suboptimal; S0 smaller motor expected to perform better
- MuMetal shielding has demonstrated 10× magnetic field reduction from electric motors in literature

---

### 4. **Hydrophone Sensor (In Development with CRT)**

**What it is:** Lightweight passive acoustic sensor for underwater target detection and classification, deployed via fiber-optic tether

**Target Specifications vs. Navy Requirements:**

| Specification | CRT Concept | Navy Threshold | Navy Objective |
|---|---|---|---|
| Operating Life | 70 min expected | 60 min | 70 min |
| Max Operating Depth | 200 ft | 200 ft | 400 ft |
| Deployment Time | 120 s (gravity-based) | 120 s | 60 s |
| Scuttle | Automatic (BST autopilot) | Auto (battery-life based) | Auto + on-command |
| Sensor Directionality | Omnidirectional | Omni | Higher gain/direction-finding |
| Frequency Coverage | 1 Hz–25 kHz | 0.01 Hz–2.5 kHz | 0.001 Hz–25 kHz |
| Sensor Noise | Low noise design | Below sea state zero | — |
| Calibration Accuracy | — | ±2 dB | ±1 dB |
| Detection Range | >20 nm | 20 nm LOS | 50 nm |

**SWAP Specifications:**
- Sensor: 1" diameter × 2" length
- Cable: 2 mm × 200 ft fiber-optic
- Power: ~30 mA @ 12 VDC (primary-chemistry battery; not drawing from UAS)

**Architecture & Design Rationale:**

*Frequency Range Challenges:*
- CRT proposes 1 Hz–25 kHz (vs. Navy objective of 0.001–25 kHz)
- Traditional piezo-based transducers not sensitive below 1 Hz
- Pre-amp design for infrasound (sub-1 Hz) requires expensive, precise circuitry
- Hydrophone sensitivity to absolute pressure changes at low frequencies; effective suspension for depth control not size-efficient at low frequencies
- Narrower frequency range (1–25 kHz) reduces communication bandwidth requirements vs. objective range

*Deployment Architecture:*
- Primary-chemistry battery (A23 cell: 12V, 55 mAh rated capacity) powers hydrophone for 60+ minute threshold
- Water-activated switch triggers microphone, ADC, and fiber-optic data transmission upon submersion
- Lightweight fiber-optic cabling (200 ft spool) replaces multi-conductor wiring—significant space/weight savings due to increased availability from UAS warfare applications
- Microphone, ADC, battery, and transmission device pot