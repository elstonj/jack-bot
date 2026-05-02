# NASA Aero RFI Response: S3 Nomad

## Document Metadata
- **Type:** RFI Response (Request for Information)
- **Client/Agency:** NASA ARMD (Aeronautics Research Mission Directorate), Aeronautics Flight Accelerator program
- **Program/Solicitation:** NASA Aeronautics Flight Accelerator RFI; Notice ID 80AFRC26SS013
- **Date:** Submitted 2026 (document created/modified May 1, 2026)
- **BST Products/Systems Referenced:** S3 Nomad (VTOL fixed-wing UAS), S2 (heritage platform), SwiftCore (FMS/autopilot), ECAM (predictive maintenance), Remote-ID integration, TAK (Tactical Awareness Kit)
- **Key Personnel:** 
  - Dr. Jack Elston (CEO, Technical POC)
  - Beck Cotter (Administrative POC)
  - Dr. Stachura (Flight Safety Review chair)
  - Collaboration with NASA Ames: Hae Soo Yang, Kris Xue (ACERO), Lynne Martin (Wildfire Airspace Management), Matthew Fladeland (FireSense), Intelligent Systems Division

## Executive Summary

Black Swift Technologies proposes the flight maturation of the **S3 Nomad**, a VTOL fixed-wing UAS configured for fully autonomous, infrastructure-free persistent operations lasting days to months. The revolutionary concept reframes 24/7 persistent observation as an **autonomy problem** rather than an aerodynamics problem: a swarm of 2–3 modest-endurance aircraft (90-minute sorties each) autonomously coordinating launch-fly-land-recharge-relaunch cycles with synchronized handoffs delivers continuous coverage at a fraction of the cost of HALE UAS or crewed observation aircraft. BST proposes three flight-test spirals (7-day, 30-day, 90-day demonstrations) to mature the persistence stack to TRL 7 by end of FY28, with direct transition to FireSense, ACERO, and SPLASH operational missions.

## Technical Approach

### Core Thesis
The proposal pivots on a paradigm shift: instead of developing ultra-long-endurance single aircraft (HALE), deploy a swarm of modest-endurance VTOL platforms with deterministic autonomous coordination.

### Key Technical Components

**Autonomous Operations Loop (Per Aircraft):**
1. VTOL launch with no operator, no launcher, no runway
2. Tasked mission flight
3. Computer-vision and ML-driven autonomous landing-site selection
4. Solar-augmented battery recharge during ground dwell
5. ECAM (Engine Condition and Health Monitoring) self-check
6. Multi-aircraft handoff coordination via SATCOM
7. Repeat

**Multi-Aircraft Coordination:**
- Two or more S3 aircraft maintain continuous on-station coverage
- Synchronized handoff timing with sub-minute coverage gaps
- SATCOM-only (Iridium for short-burst tasking, Starlink for payload backhaul)
- No ground station required; no operator intervention during persistent operation

**Core Autonomy Stack (New Development):**
- **SwiftCore FMS** with deterministic-fallback supervisor: production autopilot validated in prior SBIR work; serves as safety envelope for ML modules
- **Autonomous landing-site selection:** CV/ML module running in WASM (WebAssembly) sandbox on SBC; validated by deterministic supervisor against pre-approved geofence, terrain, and obstacle-clearance envelopes
- **Solar-augmented energy management:** Mission-aware power optimization; target is net-positive energy balance during ≥50% of mission day-cycle
- **Multi-aircraft handoff orchestration:** Validated at 24-hour scale in August 2025 NSSC demo; scales to 3+ aircraft over 90 days
- **SATCOM-only C2:** Iridium/Starlink integration; ECAM-driven autonomous abort, fallback, and graceful failure
- **TAK and Remote-ID integration:** Feeds ACERO UTM kit for airspace deconfliction

## Products & Capabilities Described

### S3 Nomad (VTOL Fixed-Wing UAS)
- **Status:** Airframe at TRL 7–8 (flight-validated production); persistence stack at TRL 3–5
- **Specifications:**
  - 110 min max sortie endurance / 90 min nominal
  - 2.7 kg modular field-swappable payload
  - 20,000 ft MSL ceiling
  - 30 kt sustained wind tolerance (40 kt gust target)
  - 60 nm (110 km) communication range
  - IP42 environmental sealing (dust/splash resistant)
  - Tiltrotor VTOL configuration
  - GNSS-aided inertial navigation with vision-aided fallback (GPS-denied resilience)
  - FAA Remote-ID compliant (MOC RID-ASTM-F3586-22-NOA-22-01); serial range BST1FS30000–S39999
  - BIS-classified EAR99 with CCATS request submitted January 2026

**Payload Bay (Field-Swappable):**
- Atmospheric sensors: temperature, humidity, pressure, dewpoint
- Wind/multi-hole probe payloads
- IR/EO imaging (NOAA NightFOX heritage from August 2025 demo)
- Surface-condition sensors: soil moisture radiometer, snow water equivalent
- Chemical/particulate/methane sensors

### SwiftCore FMS
- Deterministic-fallback architecture for safety-critical autonomy
- Wind-aware autonomous flight planning
- Production-grade autopilot across S0, S2, S2-VTOL, S3, E2 platforms
- NDAA-compliant (domestic supply chain)
- Remote-ID and TAK integration capability
- WASM sandbox for hosting ML/CV modules under deterministic supervision

### ECAM (Engine Condition and Health Monitoring)
- ML-based anomaly detection on telemetry
- Predictive maintenance module
- Autonomous mission-abort triggers based on health state

### August 2025 NASA-NSSC 24-Hour Persistence Demonstration (Heritage)
- Two S2 airframes with NOAA NightFOX IR payload
- Synchronized launch-fly-land-recharge handoff cycles
- Maintained continuous IR coverage of simulated fire-line for 24 hours
- Integrated Remote-ID detection system for wide-area drone awareness
- TAK integration with USFS incident-command tooling
- Claimed as "only validated 24-hour fully synchronized multi-aircraft persistence demonstration of its kind in U.S. small-UAS market"

## Use Cases & Applications

### Federal Earth-Observation and Disaster Response
- **NASA:** FireSense (persistent fire-line monitoring), ACERO (airspace-management co-flight), ESTO (Earth-science persistent campaigns), SMD Earth-science missions
- **USFS & CAL FIRE:** 24/7 active-fire IR persistence, extending August 2025 NightFOX demo
- **NOAA:** WPO SPLASH (soil-moisture mapping), hurricane-corridor sentinel patrol with autonomous re-tasking
- **USGS:** VDAP (Volcano Disaster Assistance Program) persistent caldera monitoring at Makushin and Chile
- **DoD (Department of War):** Replicator-class persistent ISR, perimeter-security autonomous patrol, GPS-denied resilient operations

### Commercial Markets
- Utility-scale wildfire detection
- Oil-and-gas methane survey (estimated $850M+ annual demand)
- Agricultural and pipeline persistence monitoring
- Infrastructure inspection

### Dual-Use Defense (Larger Market than Civil)
- Persistent ISR in Arctic and contested regions
- Autonomous mass operations (Replicator-class)
- GPS-denied resilient operations

## Key Results (from August 2025 Demonstration)

**24-Hour Synchronized Multi-Aircraft Persistence Demonstration (August 27, 2025, Longmont, Colorado)**
- **Participants:** BST, NASA Ames, U.S. Forest Service
- **Platforms:** Two BST S2 airframes
- **Payload:** NOAA NightFOX IR camera
- **Operations:** Executed synchronized launch-fly-land-recharge handoff cycles to maintain continuous IR coverage of simulated fire-line target for full 24-hour mission
- **Integration:** Remote-ID detection system, AI-based ground signal detection, TAK integration with USFS incident-command tooling
- **Significance:** Validated the operational baseline for the proposed AFA effort's Spiral 1 7-day extension

## Technical Objectives (AFA Program)

1. **Mature multi-aircraft synchronized handoff:** Scale from 24-hour, single-site, 2-aircraft (August 2025) to 90-day, three-site, three-aircraft demonstration by FY28
2. **Autonomous landing-site selection:** Develop and flight-validate CV/ML module in SwiftCore WASM sandbox with deterministic-fallback supervision; achieve ≤5 m circular error from nominated site
3. **Solar-augmented energy:** Integrate wing-skin energy harvesting with mission-aware power optimization; target net-positive energy balance during ≥50% of mission day-cycle
4. **Operator-free SATCOM C2:** Demonstrate over full 90-day Spiral 3 with ECAM-driven autonomous abort, fallback, and graceful failure logic
5. **ACERO UTM integration:** Demonstrate consumption of S3 Remote-ID/TAK feed for operational airspace deconfliction during multi-aircraft persistent mission
6. **Reference operational profile:** Deliver flight-validated profile adoptable directly by NASA, USFS, NOAA for FireSense, ACERO, SPLASH campaigns

## Three-Spiral Flight Test Plan

| **Spiral** | **Duration** | **Sites** | **Aircraft** | **Key Objectives** | **Timeline** |
|---|---|---|---|---|---|
| **Spiral 1** | 7 days | 1 (Longmont/Crows Landing) | 2 | Synchronized handoff extension; battery-only baseline; Direct extension of Aug 2025 demo | FY26 |
| **Spiral 2** | 30 days | 2 (geographically separated) | 2-3 | Autonomous landing-site selection; ACERO co-flight wildfire airspace integration; solar augmentation introduction | FY27 |
| **Spiral 3** | 90 days | 3 | 3 | Completely unattended (no human in loop after launch); ACERO UTM kit integration; TAK consumption | FY27–FY28 |

## Key Performance Parameters (Now vs. FY28 Target)

| KPP | Current / Heritage | FY28 AFA Target |
|---|---|---|
| Continuous on-station persistence | 24 hr (Aug 2025 demo, S2) | ≥30 days, no human in loop |
| Single-aircraft sortie endurance | 110 min max / 90 min nominal (S3 datasheet) | Maintained with mission-aware energy mgmt |
| Wind tolerance for VTOL recovery | 30 kt sustained (S3 datasheet) | 30 kt sustained, 40 kt gust |
| Autonomous landing-site selection accuracy | Manual mission planning | ≤5 m circular error from CV/ML-selected site |
| Multi-aircraft handoff timing | Synchronized 2-aircraft at NSSC demo | ≥3 aircraft, sub-minute coverage gap |
| Solar/battery energy balance | Battery only | Net-positive day-cycle for ≥50% of mission |
| Operator infrastructure required | Launcher + ground crew (S2) | None: SATCOM-only oversight |
| Integrated stack TRL | S3 airframe TRL 7–8; persistence stack TRL 4–5 | TRL 7 (flight-relevant, multi-week) |
| Airworthiness coverage | AFRC AWS for S2; FAA COAs | AWS extension to S3 nomadic ops; Part 108 BVLOS |

## Subsystem TRL Progression

| Subsystem | Description | Now | FY28 |
|---|---|---|---|
| S3 VTOL airframe | 2.7 kg payload, 20,000 ft, 30 kt wind, 60 nm range, IP42 | TRL 8 | TRL 9 |