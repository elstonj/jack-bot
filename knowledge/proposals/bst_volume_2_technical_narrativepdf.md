# S3-EW: A Modular Payload Vehicle for Agile Electronic Warfare Swarms with VTOL Ground Launch from Confined Terrain

## Document Metadata
- **Type:** SBIR Phase I Technical Proposal
- **Client/Agency:** U.S. Department of Air Force (DAF), through Defense Small Business Innovation Research (DSIP)
- **Program/Solicitation:** DAF26BZ01-NV003 (Topic: Agile EW with VTOL Ground Launch from Confined Terrain)
- **Solicitation Number:** F26BZ-NV003-0062
- **Date:** Submitted 2026 (document dated June 3, 2026)
- **BST Products/Systems Referenced:** S3 (VTOL fixed-wing UAS), S2, S0, SwiftPilot™ (autopilot), SwiftTab™ (mission UI), SwiftStation™ (ground station), SwiftCore™ (mission system/cooperative control), MAIM (Modular Aircraft Interface Module)
- **Key Personnel:** Dr. Jack Elston (PI), Dr. Maciej Stachura (CTO)
- **Subcontractor:** SkyMesa Systems (RF/SIGINT mission layer)

## Executive Summary
Black Swift Technologies proposes to develop the S3-EW, an EW-mission variant of the production S3 multi-mission VTOL fixed-wing UAS, specifically designed for agile electronic warfare swarms (3-10 aircraft) capable of VTOL ground launch from austere/confined terrain. The proposal addresses a critical gap in current Group 2 UAS inventory by combining an airframe that already exceeds all stated Key Performance Parameters (≥5 lb payload, ≥45 min endurance, ≥100 km range, ≤5 min deployment), a full-stack integrated avionics suite with native cooperative-control capabilities (SwiftCore), and a mission-layer RF/SIGINT processing engine (SkyMesa Locus) that converts raw RF observations into operator-ready confidence-scored emitter tracks with bounded geolocation. Phase I focuses on six technical objectives that retire highest-risk questions before Phase II demonstration: CONOPS development, field deployment validation, modular payload interface design, antenna architecture trade, baseline RF/SIGINT payload design, and Phase II planning.

## Technical Approach

### Problem Statement
The proposal identifies four core engineering challenges that motivated the S3-EW approach:

1. **Antenna Baseline Challenge:** VHF/lower-UHF RF direction finding requires antenna arrays with baselines proportional to wavelength. Group 1 multirotor quadcopters produce sub-wavelength baselines yielding bearing errors of tens of degrees. The S3-EW's 4-meter wingspan provides ~4 wavelengths at 300 MHz and ~13 wavelengths at 1 GHz, enabling sub-degree DF accuracy through proper antenna placement and multi-aircraft cooperative TDOA/FDOA geolocation.

2. **RF Product Generation Bottleneck:** Current Group 2 SIGINT platforms ship raw RF data without operationally-consumable mission products. The bottleneck is not RF collection but transition from raw observations to operator-trusted tracks. Solution requires confidence-scored emitter tracks with bounded uncertainty regions, tactical format outputs (TAK/CoT or JSON), and low-latency cueing support.

3. **Swarm CONOPS at 3-10 Aircraft Scale:** Multi-aircraft RF fusion at this scale must handle duplicate tracks, ambiguity, RF dropout, time-varying geometry, and competing operator-workload constraints. This is a mission-software problem, not an airframe problem.

4. **Deployment/Performance Trade:** Platforms meeting NV003 endurance/range KPPs typically require pneumatic launchers, runways, or recovery nets (defeating confined-terrain requirement). Platforms launching from confined terrain typically fail payload/endurance/range KPPs. The S3 solves this through VTOL launch/recovery without infrastructure, combined with proven flight performance exceeding all stated KPPs.

### System Architecture and Key Discriminators

**Vehicle Platform (S3 Baseline):**
- 4-meter wingspan, VTOL fixed-wing architecture
- Demonstrated **2.7 kg (6 lb) payload capacity** vs. ≥5 lb requirement
- Demonstrated **110 min maximum endurance** (90 min nominal) vs. ≥45 min requirement
- Demonstrated **110 km (60 nm) maximum range** vs. ≥100 km requirement
- **20,000 ft MSL service ceiling**, 30-knot wind tolerance
- Tool-free assembly: 6 major components disassemble into portable cases (single-person carry), reassemble in minutes
- VTOL launch/recovery eliminates launcher, runway, and recovery-net dependencies

**Full-Stack Integration (BST Discriminator):**
BST designs and builds the complete flight stack:
- **SwiftPilot™** (autopilot)
- **SwiftCore™** (mission system with cooperative-control native capabilities)
- **SwiftTab™** (mission UI)
- **SwiftStation™** (ground station)
- Inter-aircraft data link
- Modular payload interface

This eliminates chronic integration friction from multi-vendor approaches where airframe, autopilot, payload, and ground-station vendors have never flown together. Cooperative-control behaviors (3-10 aircraft, coordinated lines of bearing, TDOA/FDOA flight geometries) are first-class capabilities in SwiftCore, demonstrated during DAF ADONIS project (2026) and descended from Dr. Stachura's doctoral work on cooperative communication-relay UAS control.

**RF/SIGINT Heritage (BST Discriminator):**
- **Diverse-Source GPS (DS-GPS):** NOAA SBIR project (January 2021). SDR-based alternative navigation using triangulated signals of opportunity (RF emitters in known locations). Performs real-time detection, characterization, geolocation, and fusion with onboard autonomy decisions on small UAS. Processing chain (detect → characterize → geolocate → fuse) directly transfers to S3-EW SIGINT.
- **Multi-Modal RF Airspace Awareness on S2:** NASA wildfire project integrating ADS-B receivers, FAA Remote ID receivers, and SDR-based non-cooperating-emitter detection. Mission semantics (distinguish friendly/cooperative/non-cooperating tracks in degraded RF conditions) parallel airborne counter-UAS detection.

**Mission-Layer Processing (SkyMesa Locus):**
- Ingests: RF observations, platform pose, timing, antenna calibration metadata
- Produces: Confidence-scored RF cues, bounded geolocation estimates with explicit uncertainty regions, emitter tracks with ACQUIRE/TRACK/COAST/REACQUIRE/AMBIGUOUS/DROP states, profile-aligned TAK/CoT and JSON outputs, deterministic replay artifacts for objective quality evaluation
- **Performance Validation:** In a scored intermittent-emitter replay scenario, Locus reduced CEP90 from 6.19 km (AoA-only baseline) to 1.60 km; eliminated >5 km tail frames; removed false-lock segments
- **Operational Behavior:** Publishes when evidence is consistent, coasts when RF degrades, preserves ambiguity rather than locking onto wrong answers, carries reason codes to operator

## Products & Capabilities Described

### S3 (Production VTOL Fixed-Wing UAS)
- **What it is:** Production-ready VTOL fixed-wing UAS with proven field deployment and multi-aircraft cooperative operational heritage
- **Specifications:**
  - Wingspan: 4 meters
  - Payload capacity: 2.7 kg (6 lb) demonstrated
  - Endurance: 110 min max / 90 min nominal
  - Range: 110 km (60 nm) demonstrated
  - Service ceiling: 20,000 ft MSL
  - Wind tolerance: 30 knots
  - MTOW: <55 lb (Group 2/3 compliant)
  - Modular, tool-free assembly in minutes
  - VTOL launch/recovery, no infrastructure required
- **Proposed Use in S3-EW:** Base platform for EW mission variant with antenna mounts and modular EW payload-agnostic interface added

### S3-EW (Proposed EW Mission Variant)
- **What it is:** S3 airframe optimized for passive RF/SIGINT swarm operations with modular payload interface, antenna architecture, and full integration with SkyMesa Locus mission layer
- **Proposed Modifications (Phase I Design):**
  - Antenna mounts and field-swappable antenna modules
  - EW payload-agnostic modular interface based on MOD PAYLOAD Standard (Revision 6.1, Volume III MPu class)
  - Supplemental RF/SIGINT requirements on top of MOD PAYLOAD baseline
  - Timing, pose, and frequency-reference architecture for passive RF cueing and geolocation
  - RF coexistence management for passive RF/SIGINT payloads and future EW payloads
  - Field deployment procedure refined for two-person DAF crew with unfamiliar payloads
  - Transport case design for complete system (airframe, propulsion, payload, antenna, ground station, datalink)

### SwiftCore™ (Mission System)
- **What it is:** Modular flight management system with native cooperative-control capabilities
- **Capabilities for S3-EW:**
  - Swarm mission planning and orchestration (3-10 aircraft)
  - Leader/follower role definition
  - Cooperative sensor-based-control behaviors: line-of-bearing intersection, fly-to-maximize-geometry maneuvers, emitter-tracking flight patterns
  - Multi-aircraft cooperative flight heritage: VORTEX2 (2009-2010), NASA CRATER volcanic missions (concluded 2025), NOAA Hurricane Ernesto deployment (4 aircraft simultaneous, 2024), DAF ADONIS (2026)
  - Time-synchronized data collection across swarm
  - Operator-workload optimization for single-operator control of 3-10 aircraft

### SkyMesa Locus (RF/SIGINT Mission Layer)
- **What it is:** Purpose-built software layer for converting airborne passive RF observations into operator-ready intelligence products
- **Functional Inputs:** RF observations (IQ samples or feature vectors), platform pose, timing, antenna calibration metadata, RF front-end state
- **Functional Outputs:**
  - Confidence-scored RF cues with bearing/sector information
  - Bounded geolocation estimates with explicit uncertainty regions
  - Emitter tracks with state machine (ACQUIRE/TRACK/COAST/REACQUIRE/AMBIGUOUS/DROP)
  - TAK/CoT and JSON formatted outputs for downstream C2/tactical systems
  - Deterministic replay and objective quality evaluation (OQE) artifacts
  - Multi-aircraft track association and deduplication logic
  - Next-look recommendations for improved geometry
- **Performance Evidence:** 3.59 km improvement in geolocation accuracy (CEP90: 6.19 km → 1.60 km) on intermittent-emitter scenario with explicit uncertainty region improvements

### SwiftPilot™, SwiftTab™, SwiftStation™
- **Autopilot (SwiftPilot™):** Full-stack flight control with cooperative behaviors
- **Mission UI (SwiftTab™):** Operator interface for swarm mission planning and monitoring
- **Ground Station (SwiftStation™):** Command and telemetry backbone
- **Note:** Document does not detail technical specifications for these components

## Use Cases & Applications

### Phase II Reference Operational Scenarios (from CONOPS, Task 1)

1. **Single-Aircraft Passive RF Scout (C-UAS Reference Thread)**
   - Single S3-EW carries passive RF/SIGINT payload to detect cooperative or non-cooperative UAS emitters
   - Outputs: RF cueing, bearing/sector information, confidence-scored tracks
   - Handoff paths: SwiftCore, TAK/CoT, JSON, or operator display

2. **Swarm-Versus-Swarm / Counter-Swarm RF Cueing** (Primary Phase II Mission Thread)
   - Multiple S3-EW aircraft operate as distributed passive RF nodes against swarms or surrogate swarms
   - Locus fuses RF observations, pose, timing, signal features to reduce duplicate tracks, preserve ambiguity, generate next-look recommendations
   - Informed by SkyMesa's "Game of Drones 26-2" RF swarm/counter-swarm CONOPS work with Air Force stakeholders
   - Supports cue handoff to downstream sensors, C2, or