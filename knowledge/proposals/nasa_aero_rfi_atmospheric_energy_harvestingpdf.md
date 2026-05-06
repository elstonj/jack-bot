# NASA Aero RFI Atmospheric Energy Harvesting

## Document Metadata
- Type: RFI Response (Request for Information)
- Client/Agency: NASA Aeronautics Research Mission Directorate (ARMD), Aeronautics Flight Accelerator (AFA)
- Program/Solicitation: NASA ARMD AFA RFI; Notice ID 80AFRC26SS013
- Date: 2026-05-04
- BST Products/Systems Referenced: S2, S0, S3, SwiftCore FMS, multi-hole probe wind sensor, AeroPod
- Key Personnel: Dr. Jack Elston (CEO, Technical POC); Beck Cotter (Administrative POC)

## Executive Summary
Black Swift Technologies proposes flight maturation of an onboard atmospheric energy-harvesting capability that opportunistically extracts energy from environmental wind regimes (ridge soaring, thermal soaring, dynamic soaring) to extend small UAS mission endurance by 2–3× without requiring airframe redesigns or external infrastructure. The system combines BST's existing 100 Hz multi-hole probe wind sensor with SwiftCore's deterministic-fallback flight management system, operating entirely at the software and avionics level. Three flight-test spirals would mature the soaring controller from TRL 4 (simulation-validated) to TRL 7 (flight-relevant) by FY28, with essential NASA partnership for AFRC airworthiness extensions, Glenn aerodynamics expertise, and access to NASA ranges with predictable atmospheric phenomena.

## Technical Approach

### Core Architecture
- **Wind Sensing:** BST's U.S.-market-only 100 Hz multi-hole probe (hemispherical 5- or 9-port configuration), integrated on S2 nose cone or S0 nose port; validated against NOAA radiosondes and aircraft-derived wind references in prior NASA Phase III work (80NSSC22CA192).
- **Flight Management Substrate:** SwiftCore FMS with deterministic-fallback supervisor architecture (parallel AFA RFI submission). Soaring controller is sandboxed as a non-deterministic optimization module under a deterministic envelope-authority supervisor, preserving safety while permitting full control authority within approved envelopes.
- **Algorithm Heritage:** Position-hold and roaming soaring controller variants from completed NASA SBIR Phase II 80NSSC19C0181 (Venus Dynamic Soaring). Controllers are ported from hardware-in-the-loop (HIL) validation to flight-relevant maturity.
- **New Subsystems (under this AFA):**
  - Onboard shear-gradient and thermal-encounter detector (fusing multi-hole probe, INS, and air-data outputs at 100 Hz)
  - Energy-state estimator (tracks total mechanical-plus-electrical energy; arbitrates soaring opportunities against mission tasking)
  - Mission-aware soaring trajectory planner (consumes publicly available weather forecast products: HRRR, NDFD, RAP at ~3 km grid resolution; closed-loop controller refines onto sub-kilometer phenomena)
- **Validation Environment:** JSBSim-based 6-DOF HIL environment with BST aircraft models (from Venus SBIR lineage); documented scenarios for offline verification and validation.

### Three-Spiral Test Plan
1. **Spiral 1 (FY26): Ridge Soaring** – Closed-loop ridge soaring on S2 (10 ft wingspan fixed-wing). Target ≥60 min continuous ridge soaring with continuous power-offset measurement; demonstrate ≥30% mean propulsive power offset over 60-min sortie.
2. **Spiral 2 (FY27): Thermal Soaring** – Autonomous thermal-soaring on S2. Target multi-hour cruise with autonomous thermal capture; demonstrate ≥70% thermal-capture probability per detected thermal.
3. **Spiral 3 (FY28): Dynamic Ocean Soaring** – Dynamic soaring on S0 (1.2 kg air-deployable, 91.4 cm wingspan) in operationally representative coastal shear layer. Target ≥5 sustained energy-extracting dynamic-soaring loops; validate over marine boundary layer.

### Safety & Airworthiness Strategy
- Soaring controller operates as a "sandbox" within SwiftCore deterministic-fallback supervisor; only envelope-authority commands are executed after validation against pre-approved flight envelopes.
- Spiral 1 ridge soaring remains within existing AFRC S2 Airworthiness Specification (AWS) envelope before progressively extending to thermal and dynamic soaring in Spirals 2 and 3.
- Seeded-fault and operational flight-test data collected under AFRC airworthiness for use by ARMD's airspace-safety, autonomy verification & validation (V&V), and atmospheric-science communities.

## Products & Capabilities Described

### S2 (Spirals 1 & 2 Host Platform)
- **What:** 10 ft wingspan fixed-wing small UAS
- **Specifications:** 14,000 ft ceiling; 2 hr nominal endurance baseline; 30 mph max winds; 5 lb modular nose-cone payload capacity; lithium-polymer battery
- **Integration:** Hosts SwiftCore FMS, multi-hole probe sensor, soaring stack; existing AFRC AWS in place
- **Use in AFA:** Primary platform for ridge-soaring and thermal-soaring validation across Spirals 1 and 2

### S0 (Spiral 3 Host Platform)
- **What:** 1.2 kg air-deployable fixed-wing
- **Specifications:** 91.4 cm wingspan; 22.5 m/s cruise speed; 100 min powered endurance baseline; 257.5 km/h survival winds; lithium-ion battery; hurricane-validated airframe
- **Integration:** Carries same SwiftCore FMS, multi-hole probe, and soaring controller (aerodynamic parameters only vary per airframe)
- **Use in AFA:** Spiral 3 dynamic ocean-soaring validation; deployable from carrier aircraft (NOAA WP-3D, USAF WC-130J, NASA B-200 King Air, Gulfstream III) or ground tube launcher

### SwiftCore Flight Management System
- **What:** Production autopilot with deterministic-fallback autonomy substrate
- **Current State:** TRL 9 (flight-validated, in production across all BST platforms)
- **AFA Role:** Serves as safe-sandbox autonomy host for soaring controller; maintains envelope authority while permitting controller full control authority within pre-approved envelopes
- **Deliverable:** SwiftCore SDK extension enabling any third-party SwiftCore-licensed platform to adopt the soaring stack at the avionics layer without per-airframe re-engineering

### Multi-Hole Probe Wind Sensor
- **What:** 100 Hz onboard 3D wind-estimation sensor (5- or 9-port hemispherical configuration)
- **Current State:** TRL 9 (production, fielded across S0/S2/S3/E2); validated against NOAA radiosonde and aircraft-derived reference data
- **Capability:** Provides real-time high-rate wind-field measurement essential for closed-loop soaring control
- **AFA Role:** Core sensing input for shear-gradient detection, thermal-encounter detection, and soaring control loop

### Soaring Control Algorithms (from NASA SBIR Phase II 80NSSC19C0181)
- **What:** Two variants – position-hold controller (maintains aircraft within a bounded updraft) and roaming controller (searches for and transitions between thermal/shear resources)
- **Current State:** TRL 4 (validated in HIL; Earth-analog soaring validated in simulation)
- **AFA Maturation:** Port from HIL to flight-relevant TRL 7 across three spirals
- **Ownership:** Entirely BST-owned, validated soaring algorithms from Venus SBIR lineage

### Shear-Gradient & Thermal-Encounter Detector (New)
- **What:** Onboard detection subsystem fusing multi-hole probe, inertial navigation system (INS), and air-data outputs at 100 Hz
- **Current State:** TRL 3 (new under this AFA)
- **AFA Maturation:** Develop and flight-validate to TRL 7
- **Function:** Identifies favorable soaring regions (terrain-induced shear, thermal plumes, boundary-layer wind-shear gradients) in real-time

### Energy-State Estimator (New)
- **What:** Onboard kinetic + potential + battery-state energy accounting subsystem
- **Current State:** TRL 4
- **AFA Maturation:** Develop and flight-validate to TRL 7
- **Function:** Tracks total mechanical-plus-electrical energy; arbitrates soaring-controller opportunities against mission tasking (e.g., "is it worth detouring 2 km to climb a thermal if we need to reach waypoint X in 15 min?")

### Mission-Aware Soaring Trajectory Planner
- **What:** Flight-planning subsystem that inserts soaring opportunities within mission tasking; consumes public weather forecast products (HRRR, NDFD, RAP)
- **Current State:** TRL 3
- **AFA Maturation:** Develop and flight-validate to TRL 6
- **Resolution:** Plans at ~3 km forecast resolution; closed-loop controller refines onto sub-kilometer phenomena via onboard wind sensing

## Use Cases & Applications

### Federal Science & Surveillance
- **NASA Earth-Science Campaigns:** Persistent atmospheric profiling, in-situ measurement campaigns benefiting from 2–3× endurance gain
- **NASA FireSense & ESTO:** Extended fire-perimeter surveillance
- **NOAA Hurricane Reconnaissance:** Boundary-layer sampling, soil-moisture campaigns; 2024 validation flights on NOAA WP-3D in Hurricanes Ernesto, Helene, Milton (Category 5), Francine, Tammy
- **USGS & USFS:** Persistent volcano monitoring, fire-perimeter surveillance in mountainous terrain (precedent: 25 km BVLOS volcanic sampling at Makushin, Aleutian Islands)

### Defense & ISR
- **DoD Long-Range ISR:** Extended endurance for intelligence, surveillance, reconnaissance missions
- **GPS-Denied Operations:** Soaring capability enhances resilience in denied-airspace environments
- **Replicator-Class Autonomous-Mass Missions:** Endurance multiplier for operationally relevant atmospheres (Arctic, Pacific, denied airspace)

### Commercial Applications
- **Utility Inspections:** Power-line, wind-turbine, infrastructure inspections with extended coverage
- **Oil & Gas Methane Surveys:** Multi-billion-dollar addressable market for persistent methane detection
- **Agricultural Mapping:** Extended survey coverage without battery/payload tradeoffs
- **Coastal Monitoring:** Dynamic soaring over ocean boundary layer for marine surveillance

### Planetary Science (Cross-Cut)
- **Mars & Venus Upper-Atmosphere Missions:** Algorithms directly applicable to planetary dynamic-soaring for atmospheric survey (science & technology crossover from Venus SBIR Phase II)

### Test Ranges & Demonstration Sites
- **AFRC Edwards:** Spirals 1 and 2 (ridge and thermal soaring)
- **BST Longmont Test Site:** Fallback for Spiral 1 ridge-soaring
- **AFRC Pacific Test Ranges / Coastal Alternatives:** Spiral 3 dynamic ocean soaring (NOAA coordination option)

## Key Technical Objectives & Performance Targets

### Objectives
1. Mature soaring controller from TRL 4 (HIL) to TRL 7 (flight-relevant) through three closed-loop flight spirals
2. Develop and flight-validate onboard shear-gradient and thermal-encounter detector at 100 Hz (fusion of multi-hole probe, INS, air-data)
3. Develop and flight-validate onboard energy-state estimator (tracks mechanical + electrical energy; arbitrates against mission tasking)
4. Demonstrate ≥30% mean propulsive power offset across 60 min closed-loop ridge-soaring sortie on S2 (Spiral 1)
5. Demonstrate ≥70% thermal-capture probability per detected thermal (Spiral 2)
6. Demonstrate ≥5 sustained energy-extracting dynamic-soaring loops in operationally representative shear (Spiral 3)
7. Deliver flight-validated soaring-stack reference design and SwiftCore SDK extension for third-party adoption without per-airframe re-engineering

### Key Performance Parameters (Table 1 Summary)

| Parameter | Current State | FY28 Target |
|--------