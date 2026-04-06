# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification

## Document Metadata
- **Type:** Navy SBIR Topic Description (Solicitation N251-016)
- **Client/Agency:** U.S. Navy (Naval Air Systems Command - NAVAIR)
- **Program/Solicitation:** Navy SBIR FY2025, Topic N251-016
- **Date:** 2024 (topic issued for Phase I proposals)
- **BST Products/Systems Referenced:** None specifically named in this topic document
- **Key Personnel:** Topic Points of Contact:
  - Angel Ruiz Reyes (Naval Air Systems Command) - 301-757-7955
  - Anthony Brescia (Naval Air Systems Command) - 301-342-2094

## Executive Summary
This Navy SBIR topic solicits development of an expendable Tier 1 Sonobuoy-Launched UAV (SL UAV) that combines magnetic anomaly detection (MAD) with in-water passive acoustic sensing for anti-submarine warfare (ASW) target search, detection, localization, tracking, and classification. The system must launch from a P-8A Poseidon's sonobuoy launcher system, weigh under 39 lbs, achieve 70-minute endurance, and ultimately operate in coordinated swarms with autonomous target-tracking capability via artificial intelligence.

## Technical Approach

### Aircraft Design Requirements
- Packaged in LAU-126A Sonobuoy Launch Container (SLC) or equivalent
- Maximum dimensions when stowed: 4.875 in. diameter × 36 in. length
- Unfolds after launch for stable flight transition
- Must withstand shock loads from Cartridge Activated Device (CAD) launcher or pneumatic sono-launcher
- 9-year shelf life storage capability

### Magnetic Anomaly Detection (MAD) System
- **Platform magnetic noise:** <1 pT/√Hz from DC to 100 Hz
- **Magnetometer specifications:**
  - Real-world dynamic range: ±100 µT per axis
  - No dead zones
  - Accuracy: 1 nT across -0°C to 50°C temperature range
  - In-air noise threshold: 20 pT/√Hz in 0.01–100 Hz band with raw heading error specification
- Detection methods must include harmonic field analysis, not limited to dipole models
- Magnetic characterization required at magnetometer location across varying engine speeds

### In-Water Passive Acoustic Sensor
- **Operating life:** Threshold 60 min; Objective 70 min
- **Maximum depth:** Threshold 200 ft (60.96 m); Objective 400 ft (121.92 m)
- **Deployment time:** Threshold 120 s; Objective 60 s
- **Frequency coverage:** Threshold 0.01 Hz–2.5 kHz; Objective 0.001 Hz–25 kHz
- **Directional sensitivity:** Threshold omnidirectional; Objective higher gain and/or direction-finding capability
- **Calibration accuracy:** Threshold ±2 dB; Objective ±1 dB
- **Data handling:** Whitened to environment for reduced uplink bandwidth; automatic scuttling based on battery life with command override option

### Autonomy & AI/ML Processing
- **Threshold autonomy:** Pre-programmed waypoint tracks and orbits
- **Objective autonomy:** Transition to autonomous target tracking cued by MAD system
- **Onboard processing requirements:**
  - Minimum 275 TOPS (INT8) AI performance
  - GPU: ≥1.3 GHz frequency, ≥2048 CUDA cores, ≥64 Tensor cores
  - CPU: ≥12 cores at 2.2 GHz
  - RAM: ≥64 GB
- AI/ML methods must be explicitly labeled and compared against non-linear correlation methods and weak neural-network approaches
- Must support data fusion algorithms incorporating multiple sensor types

### Operational Parameters
- **Cruise speed:** 70 knots (threshold)
- **Endurance:** 70 minutes (threshold)
- **Operational altitude:** 500–2,000 ft
- **Range:** 20 nm line-of-sight (extending to 50 nm objective)
- **Payload volume:** >94.4 in.³ (1,546.94 cm³)
- **Environmental operations:** -20°C to 50°C; light rain (visibility >1 nm)
- **Weight:** Max 39 lbs bare (not including launcher container)

### Command & Control
- Phase I & II: Any architecture acceptable
- Phase III: Must integrate with UAS Control Segment (UCS) Architecture

### Cost Target
- Final production cost: <$10,000 per unit in quantities of 100

### Security & Encryption
- Encryption methods for data transmission must be addressed in proposals
- Technology restricted under ITAR (22 CFR Parts 120-130) and potentially EAR (15 CFR Parts 730-774)
- Work in Phase II may become classified
- Contractor must be U.S. owned and operated with no foreign influence; secret-level facility and personnel security clearances required

## Use Cases & Applications

### Primary Mission: Anti-Submarine Warfare
- **Launch platform:** P-8A Poseidon maritime patrol aircraft
- **Operational context:** Cued search from Area of Uncertainty (AOU)
- **Target operations:** Detection, localization, tracking, and classification of submarine targets
- **Deployment scenario:** Multiple SL UAVs operating in coordinated swarms with collective detection and classification capability

### Dual-Use Applications (Phase III)
- Sea and earth landscape reconnaissance and detection during airborne operations
- Product innovation in reckoning and detection delivery for maritime and land-based applications

## Phase Structure & Deliverables

### Phase I Objectives
- Develop detailed SL UAV concept design
- Provide theoretical, physical, numerical, and computational methods documentation
- Build aircraft prototype with structural analysis and flight clearances
- Simulate aircraft design and MAD/acoustic operation with results verified experimentally in laboratory
- Complete magnetic characterization at magnetometer location across engine speeds
- Compare to performance of similar previously-developed SL UAVs
- Explicitly document AI/ML methods employed and compare against non-linear correlation and weak neural-network approaches
- Must meet threshold magnetic noise performance to proceed to Phase II

### Phase II Objectives
- Construct multiple operational SL UAV units with integrated MAD + acoustic systems
- Conduct full-system demonstration of combined MAD and acoustic capabilities
- Air-launch from surrogate platform to demonstrate unfolding, stable flight transition, and communications
- Subject units to shock loads replicating CAD launcher or pneumatic sono-launcher loads
- Demonstrate swarm operation capability
- Demonstrate target classification and localization
- Meet in-flight threshold performance specifications
- Prototype plans development

### Phase III Objectives
- Conduct swarm search operations with SL UAVs against relevant targets
- Detect, track, and classify targets using combined magnetic and acoustic sensor fusion
- Air-launch from relevant platform meeting sponsor demands

## Notable Details

### Technical Distinctions
- Topic emphasizes expendable design philosophy—vehicles are consumable after single-use deployment
- Must unfold reliably after launch from pneumatic/cartridge sonobuoy launcher system
- Dual-sensor fusion approach (MAD + passive acoustic) provides complementary detection modalities
- Swarm capability is progression objective, not initial requirement

### Security & Compliance Requirements
- ITAR-controlled technology; foreign national participation severely restricted
- Prospective contractors must be U.S. owned and operated per 32 U.S.C. § 2004.20 et seq.
- Must implement Defense Counterintelligence and Security Agency (DCSA) approved security procedures
- Contractor facility must achieve secret-level classification capability
- All contractor personnel must obtain Personnel Security Clearances
- Work must comply with National Industrial Security Program Operating Manual (NISPOM) per 32 CFR 2004.20

### Technical Evaluation Criteria (Implicit)
- Meeting magnetic noise threshold is a gate criterion for Phase II advancement
- Phase I success defined by meeting threshold parameters in structural analysis, simulation, and laboratory testing with TPOC confirmation
- Comparison to existing SL UAV designs required to establish baseline performance
- AI/ML transparency and validation against classical methods required

### References Context
Topic references academic work on airborne magnetic measurement noise reduction (Ash 1997), atomic magnetometry without dead zones (Ben-Kish & Romalis 2010), magnetic sensors for underwater vehicle applications (Clem et al. 2004), diamond-based magnetometry advances (Wolf et al. 2015), and standard underwater transducer/array theory (Sherman & Butler 2007).