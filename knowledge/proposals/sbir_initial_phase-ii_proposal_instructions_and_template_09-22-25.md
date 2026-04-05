# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking and Classification

## Document Metadata
- Type: SBIR Phase II Initial Proposal
- Client/Agency: U.S. Navy (Naval Air Warfare Center Aircraft Division / NAVAIR)
- Program/Solicitation: Topic N251-016
- Date: January 4, 2025 (submitted January 9, 2025; due January 12, 2025)
- BST Products/Systems Referenced: S0 (air-deployed UAS), S0-MAD (magnetic anomaly detection variant), S0-Acoustic (acoustic sensing variant), E2 (multirotor deployment platform)
- Key Personnel: Dr. Jack Elston (PI/CEO), Tim Rorick (Ultra Maritime), Paul DeMond (Ultra Maritime), Jeff Orton (QuSpin consultant)

## Executive Summary
Black Swift Technologies proposes to develop a production-ready Sonobuoy-Launched Unmanned Aerial System (SL UAS) capable of performing magnetic anomaly detection (MAD) and deploying in-water passive acoustic sensors to support Anti-Submarine Warfare (ASW) cued search, detection, tracking, and classification. Building on successful Phase I completion demonstrating magnetic noise floor below 20 pT/√Hz and mechanical compatibility with the LAU-126A sonobuoy launch container, Phase II will fabricate, integrate, and validate two distinct aircraft variants (S0-MAD and S0-Acoustic) with coordinated multi-sensor operations capability.

## Technical Approach

### Phase I Foundation
- Demonstrated mechanical compatibility of S0 platform with LAU-126A launch envelope (size, mass, center-of-gravity, structural loading)
- Achieved magnetic noise floor <20 pT/√Hz in 0.01–100 Hz band (exceeds Navy Phase I threshold requirement)
- Validated integration of high-sensitivity magnetometer and deployable acoustic sensing payload within S0 architecture

### Phase II Technical Strategy

**Magnetic Sensing (S0-MAD):**
- Hardened S0-MAD airframe for dynamic launch and flight environments
- Integration of optically pumped atomic magnetometer (QuSpin QTFM Gen-2)
- Magnetic noise mitigation strategies: magnetic shielding of propulsion components, optimized sensor placement via short structural booms, calibration-informed compensation techniques
- Target: maintain <20 pT/√Hz and <3 nT heading error during flight maneuvers
- Sensor placement via short structural boom to decouple from aircraft noise

**Acoustic Sensing (S0-Acoustic):**
- Parallel development of S0 variant optimized for water landing and sensor deployment
- Dual acoustic payload: hydrophone (5 Hz – 40 kHz) + electric-field sensors
- E-field sensors split into ELFE (Extremely Low Frequency Electromagnetic) and ULF (Ultra Low Frequency, 0.01–5 Hz) to extend detection bandwidth below traditional hydrophone limits
- Lightweight fiber-optic tether deployment (200 ft depth, 60+ min operating duration)
- Lightweight suspension system to isolate wave-induced noise below 100 Hz
- Integration of Jetson AGX Orin onboard processing hardware for detection/classification

**System Architecture:**
- Two separate, independent aircraft platforms (S0-MAD and S0-Acoustic) for maximum mission flexibility and cost efficiency
- Sensor-responsive autonomy and inter-vehicle coordination (Phase II Option)
- Acoustic detections from S0-Acoustic can cue adaptive search patterns in S0-MAD
- Magnetometer detections can direct deployment of multiple acoustic platforms
- Avionics-level hooks and control abstractions enabling coordinated operations without tight onboard data fusion

### Testing Progression
1. Laboratory and bench-level subsystem verification
2. Environmental and shock qualification (pneumatic launch loads, temperature –20°C to +50°C, light rain)
3. LAU-126A simulated shock testing (10G/100ms)
4. Air-launch demonstrations and flight validation
5. Water-landing tests (freshwater, then ocean environment for salt-water durability assessment)
6. Multi-modal detection against surrogate targets in maritime environment
7. End-to-end operational validation with Navy-relevant procedures

## Products & Capabilities Described

### S0 (Base Platform)
- **What it is:** Fixed-wing, air-deployed unmanned aerial system originally developed for deployment from NOAA P-3 aircraft and quadrotor drop
- **Cruise speed:** ~70 knots
- **Deployment method:** Sonobuoy-style air launch from LAU-126A launch container
- **Form factor:** Expendable, tube-launched architecture compatible with existing Navy launch infrastructure
- **Unit cost target:** <$10,000 in quantities of 100+

### S0-MAD (Magnetic Anomaly Detection Variant)
- **Payload:** Optically pumped atomic magnetometer (QuSpin QTFM Gen-2)
- **Performance threshold:** <20 pT/√Hz in 0.01–100 Hz band; <3 nT heading error
- **Phase I achievement:** Demonstrated magnetic noise below threshold in laboratory/ground-based tests
- **Phase II goal:** Validate performance in dynamic flight conditions with propulsion engagement
- **Sensor placement:** Short structural boom for optimal noise decoupling
- **Noise mitigation:** Magnetic shielding, sensor placement optimization, calibration compensation

### S0-Acoustic (Acoustic Sensing Variant)
- **Payload components:** 
  - Hydrophone (5 Hz – 40 kHz bandwidth)
  - E-field sensors (ELFE + ULF, 0.01 Hz – 5 Hz)
- **Deployment mechanism:** Fiber-optic tethered sensor string (200 ft length)
- **Terminal weight:** 2 lbs with 11-inch vertical damper disc for wave-noise isolation
- **Operating depth:** Up to 200 ft
- **Operating duration:** 60–70 minutes minimum
- **Data link:** 20 nm line-of-sight RF link with whitened digital data transmission
- **Onboard processing:** Jetson AGX Orin GPU for detection/classification algorithms
- **Water landing capability:** Fuselage redesigned for controlled water impact and sensor deployment

### Integration & Processing
- **Jetson AGX Orin:** Target detection/classification processing hardware integrated into both aircraft variants
- **Mechanical design:** Folding, stowage mechanisms for LAU-126A launch container
- **Avionics:** Sensor-responsive autonomy hooks, inter-vehicle coordination abstractions

## Use Cases & Applications

### Primary: Anti-Submarine Warfare (ASW)
- **Cued search:** Acoustic detections cue magnetometer search; MAD localizations cue acoustic deployment
- **Detection:** Magnetic anomaly and passive acoustic detection of submarine targets
- **Tracking:** Coordinated multi-platform operations for target maintenance and localization
- **Classification:** Data fusion from dual sensors enables improved classification without tight onboard processing
- **Operational concept:** Mirrors legacy P-3/P-8 ASW doctrine: acoustic arrays localize regions of interest; MAD provides detailed localization

### Secondary Applications (Mentioned)
- **Unexploded ordnance (UXO) detection:** Leveraging magnetometry for buried ordnance
- **Environmental monitoring:** Magnetic field mapping, underwater sensing
- **Infrastructure inspection:** Leveraging low-cost, expendable architecture
- **Marine research:** Engagement with marine animal research organizations noted; interest expressed in platform cost and sensing capabilities

### Operational Scenarios
- **P-8A integration:** Deployment from P-8 Poseidon maritime patrol aircraft at altitude
- **Contested maritime environments:** Distributed, attritable sensing for cost-effective coverage
- **Extended ASW operations:** Multiple sorties with expendable platforms reducing operational risk

## Phase II Objectives & Milestones

**Objective 1:** Construct multiple production-representative SL UAVs with ruggedized integration into LAU-126A launch container

**Objective 2:** Confirm magnetic sensor compliance (<20 pT/√Hz, <3 nT heading error) in dynamic flight with propulsion engagement

**Objective 3:** Develop deployable in-water acoustic subsystem (hydrophone + E-field sensors) for 200 ft depth, 60+ min operation

**Objective 4:** System-level demonstration in Navy-relevant maritime environment with coordinated SL UAS operations, air launch, autonomous flight, sensor-based cueing, and surrogate target detection

**Objective 5 (Option):** Implement sensor-responsive autonomy and multi-vehicle coordination enabling acoustic detections to cue magnetometer search and vice versa

**Objective 6 (Option):** Define transition-ready architecture, interface control documentation (ICD), and Level 3 Technical Data Package (TDP) for Navy UAS Control Segment (UCS) integration

## Work Plan & Key Milestones

**Base Phase (30 months):**
- **B.1 (Months 1–4):** Magnetic Sensing SL UAV design, manufacture, flight performance verification
- **B.2 (Months 4–13):** Flight validation of magnetic performance (pattern flights demonstrating <20 pT/√Hz, <3 nT heading error)
  - **Milestone:** Proven magnetic capability in-flight
- **B.3 (Months 6–8):** Sensor integration with onboard Jetson AGX Orin processing hardware
- **B.4 (Months 8–15):** Acoustic subsystem ground testing (laboratory characterization of hydrophone, E-field sensors)
- **B.5 (Months 14–21):** Acoustic integration and water-landing UAV prototype design, fabrication, flight testing
- **B.6 (Months 20–25):** Water-landing validation (freshwater then ocean environment)
  - **Milestone:** Acoustic UAV capability proven
- **B.7 (Months 20–29):** Environmental and shock qualification (–20°C to +50°C, 10G/100ms shock loads, light rain)
- **B.8 (Months 27–30):** End-to-end flight qualification of both platforms
  - **Milestone:** Full system demonstration with air launch, stable flight, hydrophone deployment, surrogate target detection/tracking

**Option Phase (12 months):**
- **O.1 (Months 1–6):** Classified algorithm integration (assumes Navy provides ML model; includes design to maintain unclassified system until operation, with classified data wipe before shutdown/scuttling)
- **O.2 (Months 4–11):** Swarm operations design, software development, multi-platform coordination testing
- **O.3 (Months 9–12):** Final validation with ML models loaded, Navy operator evaluation in maritime environment
  - **Deliverable:** Level 3 TDP and ICDs for UCS integration
  - **Milestone:** Product ready for Navy use

## Key Results (Phase I Achievements)

- **Magnetic noise floor:** <20 pT/√Hz in 0.01–100 Hz band (meets Navy threshold)
- **Mechanical compatibility:** Validated S0 platform fits LAU-126A launch envelope with proper mass, center-of-gravity, structural loading
- **Acoustic sensor simulation:** E-field sensor modeling completed (figures showing simulated results provided)
- **Flight heritage:** S0 demonstrated air deployment from NOAA P-3 and quadrotor drop
- **Technical foundation:** Firm foundation established for Phase II system maturation

## Subcontractors & Key Personnel

**Ultra Maritime (Subcontractor):**
- **Tim Rorick** – Acoustics Lead, 30+ years sonar/ASW experience, Purdue BSME/MSME
- **Paul DeMond** – Lead Systems Engineer, 45+ years sonobuoy/sensor systems, Program Manager for multiple Navy ASW programs (PMA-264, NUWC, DARPA)
- **Responsibility:** Acoustic and E-field sensor payload development, integration

**QuSpin, Inc. (Consultant):**
- **Jeff Orton** – Lead Engineer, 10+ years optically pumped atomic magnetometer (OPM) systems design and productization
- **Responsibility:** Magnetometer integration, platform noise mitigation strategies, sensor deployment for compact UAS

**BST Key Personnel:**
- **Dr. Jack Elston** – CEO/PI, Ph.D. 2011 (CU Boulder), expert in networked autonomous UAS, sensor payload integration, extreme-environment operations (tornadic supercells, arctic regions)

## Notable Details

### Competitive Advantages
- **Proven platform:** S0 has