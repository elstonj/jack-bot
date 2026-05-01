# NASA Aero RFI Atmospheric Energy Harvesting

## Document Metadata
- **Type:** RFI Response / Capability Proposal
- **Client/Agency:** NASA ARMD (Aeronautics Research Mission Directorate)
- **Program/Solicitation:** NASA Aeronautics Flight Accelerator (AFA) RFI; Notice ID 80AFRC26SS013
- **Date:** 2026-04-30 (submission date)
- **BST Products/Systems Referenced:** S2 (fixed-wing), S0 (air-deployable), S3 (VTOL), E2 (multirotor), SwiftCore Flight Management System, Multi-hole probe wind sensor
- **Key Personnel:** Dr. Jack Elston (CEO, PI), Dr. Maciej Stachura (CTO, Lead Control and Estimation Engineer), Dr. Stachura (first to lead BST AFSRB)

---

## Executive Summary

Black Swift Technologies proposes to mature an onboard atmospheric energy-harvesting capability—combining wind sensing, thermal/shear detection, energy estimation, and autonomous soaring control—that extends small UAS mission endurance by 2–3× through three flight-test spirals across ridge soaring (FY26–27), thermal soaring (FY27), and dynamic ocean soaring (FY28). The capability is implemented entirely at the avionics layer on existing BST airframes using production hardware (100 Hz multi-hole probe) and SwiftCore FMS, with no airframe redesign, advancing ARMD's Transform Airframes and Revolutionize Methods objectives.

---

## Technical Approach

### Core Innovation
BST's thesis is that atmospheric energy-harvesting has been understood physics for 140+ years (Lord Rayleigh, 1883) and proven by human glider pilots and radio-controlled soaring, but has never been productized as flight-software autonomy for small UAS. The barrier has been twofold: (1) onboard wind-field measurement at the rate and accuracy closed-loop soaring demands, and (2) a safety-critical autonomy substrate willing to host non-deterministic optimization control.

BST's solution:
- **100 Hz multi-hole probe wind sensor:** The only U.S. commercial off-the-shelf sensor of this rate flown on small UAS; already production hardware on every BST airframe (S0, S2, S3, E2).
- **SwiftCore deterministic-fallback FMS:** Only U.S. flight-validated substrate permitting a soaring optimizer full control authority while a deterministic supervisor retains envelope authority (subject of parallel AFA RFI on Adaptive and Secure Autonomy).

### Nine Integrated Subsystems
1. BST host airframe (S2 for Spirals 1–2; S0 for Spiral 3)
2. SwiftCore FMS with deterministic-fallback supervisor
3. Multi-hole probe wind sensor (100 Hz, 5- or 9-port hemispherical configuration)
4. Onboard shear-gradient and thermal-encounter detector (new under AFA; fuses MHP, INS, air-data)
5. Energy-state estimator (tracks total mechanical + electrical energy; arbitrates soaring vs. mission tasking)
6. Soaring control algorithm (position-hold and roaming variants from NASA SBIR Phase II 80NSSC19C0181 Venus lineage; ported from HIL to flight-relevant)
7. Mission-aware soaring trajectory planner (consumes public weather forecasts at ~3 km resolution; refines onto sub-km phenomena via onboard 100 Hz wind field)
8. JSBSim 6-DOF HIL environment for offline V&V (from Venus SBIR lineage)
9. AFRC range and AWS infrastructure for closed-loop flight validation

### Three Soaring Regimes Targeted
- **Ridge soaring:** Terrain-deflected wind over mountains (fire perimeter, BVLOS infrastructure monitoring)
- **Thermal soaring:** Solar-driven convective updrafts (atmospheric profiling, agricultural/methane survey)
- **Dynamic ocean soaring:** Vertical wind shear over coastal/open-ocean boundaries (hurricane-corridor surveillance, oceanic profiling)

---

## Products & Capabilities Described

### S2 (Fixed-Wing Host Airframe)
- 10 ft wingspan, 14,000 ft ceiling
- 2 hr nominal powered endurance baseline
- 30 mph max operational winds
- 5 lb modular nose-cone payload capacity
- AFRC Airworthiness Safety approval in place
- Used in Spirals 1 and 2 (ridge and thermal soaring)

### S0 (Air-Deployable Host Airframe)
- 1.2 kg total mass, 91.4 cm wingspan
- 22.5 m/s cruise speed
- 100-min powered endurance baseline
- 257.5 km/h survival winds; hurricane-validated
- Air-deployable from carrier aircraft (NOAA WP-3D, USAF WC-130J, NASA B-200 King Air, Gulfstream III) or ground-tube launcher
- Used in Spiral 3 (dynamic ocean soaring)

### SwiftCore Flight Management System
- Production autopilot with deterministic-fallback safety substrate
- Hosts soaring control, detection, and estimation modules as sandboxed components
- Supervisor retains envelope authority (attitude, rate, velocity, geofence) while permitting soaring optimizer wide latitude
- Already TRL 9 (flight-validated production hardware)
- NDAA-compliant with U.S., Taiwan, and Japan-sourced electronics; entirely U.S. mechanical fabrication
- Supports SBIR Phase III SDK extensions for third-party adoption without per-airframe re-engineering

### Multi-Hole Probe (100 Hz Wind Sensor)
- 5-port or 9-port hemispherical configuration
- Provides 3D wind vector at 100 Hz
- Already integrated and flown on S0, S2, E2 platforms
- TRL 9 (production hardware)
- Validated against NOAA radiosonde and aircraft-derived references in prior NASA Phase III work (80NSSC22CA192)
- Enables real-time wind-field estimation on the aircraft

### Soaring Control Algorithms
- **Position-hold controller:** Maintains aircraft position within a thermal or ridge-lift zone
- **Roaming controller:** Plans extended cruise paths between thermal/ridge encounters
- Developed and validated in HIL under NASA SBIR Phase II 80NSSC19C0181 (Venus dynamic soaring)
- TRL 4 today (HIL maturation); target TRL 7 by FY28
- Closed-loop authority mediated by SwiftCore deterministic-fallback supervisor

### Onboard Shear-Gradient & Thermal-Encounter Detector
- New development under this AFA effort
- Fuses multi-hole probe, INS (inertial), and air-data outputs
- Runs on SwiftCore SBC at 100 Hz
- Detects vertical-wind gradients (ridge lift, wind shear) and thermal signatures
- TRL 3 today; target TRL 7 by FY28

### Energy-State Estimator
- Tracks total mechanical (kinetic + potential) plus electrical (battery) energy
- Arbitrates soaring opportunities against mission tasking and reserve power requirements
- TRL 4 today; target TRL 7 by FY28

### Mission-Aware Soaring Trajectory Planner
- Consumes public weather forecast products (HRRR, NDFD, RAP at ~3 km grid resolution)
- Plans soaring insertions into nominal mission tasking
- Operates at mission-planning timescale (offline or pre-flight)
- TRL 3 today; target TRL 6 by FY28

---

## Use Cases & Applications

### Civil Applications
- **NASA FireSense:** Persistent fire monitoring and perimeter mapping
- **NASA Earth-Science SMD:** Long-duration sensor campaigns (ESTO missions)
- **NOAA Hurricane Research Division:** Boundary-layer sampling, oceanic atmospheric profiling; dynamic ocean soaring directly applicable to marine shear environments
- **NOAA NWS:** Upper-air program persistence
- **NOAA SPLASH:** Soil-moisture campaigns
- **USGS:** Persistent volcano caldera monitoring (Makushin/Aleutian Islands; planned Chile deployment)
- **USFS:** Extended sortie persistence over fire perimeters in mountainous terrain (natural ridge-soaring environment)
- **Ames atmospheric-sciences:** In-situ profiling; Mars and Venus dynamic-soaring analog work

### Defense Applications
- DoD long-range ISR with extended endurance
- GPS-denied resilient operations (Arctic, Pacific, denied airspace)
- Replicator-class autonomous-mass missions in operationally relevant atmospheres

### Commercial Applications
- Utility and pipeline persistence monitoring
- Oil-and-gas methane survey
- Agricultural and crop-stress mapping
- Infrastructure inspection
- Multi-billion-dollar annual addressable market where 2–3× endurance at zero airframe-redesign cost represents competitive discontinuity

### Planetary Science (Cross-Cutting)
- Venus upper-atmosphere observations (lineage from 80NSSC19C0181)
- Mars dynamic soaring (similar physics; algorithms applicable in current form)
- Phase III commercialization vector independent of terrestrial markets

---

## Key Technical Objectives & Performance Targets

### Primary Objectives
1. Mature soaring controller from TRL 4 (HIL) to TRL 7 (flight-relevant) via three closed-loop flight spirals
2. Develop and flight-validate onboard shear-gradient and thermal-encounter detector (100 Hz, SBC-based)
3. Develop and flight-validate energy-state estimator (mechanical + electrical energy accounting)
4. Demonstrate ≥ 30% mean propulsive power offset across 60-minute closed-loop ridge-soaring sortie (Spiral 1, S2)
5. Demonstrate ≥ 70% thermal-capture probability per detected thermal (Spiral 2, S2)
6. Demonstrate ≥ 5 sustained energy-extracting dynamic-soaring loops in operationally representative shear (Spiral 3, S0)
7. Deliver flight-validated soaring-stack reference design and SwiftCore SDK extension usable by third-party SwiftCore-licensed platforms without per-airframe re-engineering

### Key Performance Parameters

| Parameter | Now (BST Heritage) | FY28 AFA Target |
|-----------|-------------------|-----------------|
| Endurance gain in mission-relevant winds | Simulated only (Venus SBIR Phase II HIL) | ≥ 2× over baseline; demonstrated in flight |
| Onboard 3D wind estimation rate | 100 Hz (S2 multi-hole probe, validated NOAA) | 100 Hz with online shear-gradient detection |
| Soaring controller closed-loop authority | Open-loop guidance only | Closed-loop with deterministic-fallback supervisor |
| Power-offset fraction in ridge soaring | N/A in flight | ≥ 30% mean over 60-min sortie |
| Thermal capture probability per encounter | N/A in flight | ≥ 70% capture given detected thermal |
| Dynamic-soaring loop completion | N/A in flight (Earth) | ≥ 5 sustained loops over coastal shear layer |
| Integration burden onto host airframe | Avionics-level only | Drop-in for any SwiftCore-based airframe |
| Integrated stack TRL | Algorithms TRL 4 (HIL); sensors TRL 9 | TRL 7 (flight-relevant) |
| Airworthiness coverage | AFRC AWS for S2; FAA COAs | AWS extension to soaring envelopes |

### Three-Spiral Flight-Test Plan

**Spiral 1 (FY26 Q4 – FY27 Q2): Ridge Soaring on S2**
- Location: Colorado Front Range (AFRC Edwards or BST Longmont test site as fallback)
- Target: ≥ 60 min closed-loop ridge soaring with continuous power-offset measurement
- Goal: ≥ 30% mean power offset

**Spiral 2 (FY27): Autonomous Thermal Soaring on S2**
- Location: Great Plains
- Target: Multi-hour cruise with autonomous thermal capture
- Goal: ≥ 70% thermal-capture probability per detected thermal; multi-hour endurance gain

**Spiral 