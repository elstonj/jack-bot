# S3-EW: A Modular Payload Vehicle for Agile Electronic Warfare Swarms with VTOL Ground Launch from Confined Terrain

## Document Metadata
- **Type:** SBIR Phase I Technical Volume (Volume 2)
- **Client/Agency:** Department of the Air Force (DAF)
- **Program/Solicitation:** DAF26BZ01-NV003 (Agile EW)
- **Date:** Draft as of 2026-05-26 (submission date TBD)
- **DSIP Proposal Number:** F26BZ-NV003-0062
- **BST Products/Systems Referenced:** S3, S2, S0, SwiftPilot™, SwiftTab™, SwiftStation™, SwiftCore FMS, DS-GPS
- **Key Personnel:** Dr. Jack Elston (PI, CEO), Dr. Maciej Stachura (Co-Investigator, CTO), Mechanical/Structural Lead [TBD], RF/Payload Engineer [TBD]
- **Subcontractor:** SkyMesa Systems (RF geolocation and spectrum-awareness software)

## Executive Summary

Black Swift Technologies proposes the S3-EW, an electronic-warfare mission variant of the production S3 multi-mission VTOL fixed-wing UAS, to meet the DAF's requirement for a low-cost, ground-launched small UAS capable of rapid payload reconfiguration and swarm operations (3–10 aircraft) across diverse EW payloads. The S3-EW meets or exceeds all published Key Performance Parameters (KPPs)—5 lb payload capacity, 45 min endurance, 100 km range, and ≤5 min deployment—while providing the ~4 m composite-wing antenna baseline that enables interferometric direction finding (DF) at VHF/UHF frequencies. Phase I will retire the highest-risk feasibility questions through antenna integration studies, SIGINT payload SWaP-C trades, swarm CONOPS simulation, and a credible preliminary design package leading to Phase II flight demonstrations.

## Technical Approach

**Platform Selection and Rationale:**
BST proposes to leverage the production S3 platform (next-generation VTOL fixed-wing aircraft) as the baseline for the S3-EW. The S3 represents a decade of operational experience from the S2 and S0 platforms, including world-record hurricane flights, USGS volcano observations, and NOAA wildfire work. Key attributes:

- **VTOL Launch & Recovery:** Native vertical takeoff and landing from unprepared, confined terrain, eliminating launcher, catapult, or recovery-net dependencies that prevent rapid deployment under Agile Combat Employment (ACE) doctrine.
- **Proven Endurance & Range:** 110 min maximum / 90 min nominal endurance and 110 km (60 nm) range exceed the stated KPPs by 2× and meet range requirements, respectively.
- **Service Ceiling:** 20,000 ft MSL operational ceiling places RF sensors well above terrain masking and surface ducting that limit ground-based and low-altitude SIGINT.
- **Environmental Ruggedness:** IP42 ingress protection, reinforced composite airframe, and weather sealing inherited from hurricane-class (S0) and volcanic-plume-class (S2) operations; demonstrated in Category 5 hurricanes and active volcanic craters.
- **Wind Tolerance:** 30 kt (15 m/s) wind-holding capability exceeds typical Group 2 quadcopter limits, enabling operations in the turbulent, high-altitude environments where EW missions operate.
- **Antenna Baseline:** ~4 m composite wing span provides structural real estate for wing-embedded conformal antenna elements—more than an order of magnitude larger than quadcopter platforms and substantially larger than the S2.
- **Quick Assembly:** Designed for field assembly in minutes from transport cases with tool-free quick-disconnect fasteners (captive quarter-turn fasteners, rotor-arm latching, payload tray insertion).

**Technical Gap Addressed:**
Most Group 2 UAS either are fragile multirotors with insufficient antenna baseline for effective EW payloads, or are fixed-wing aircraft requiring catapults, runways, or recovery nets incompatible with ACE austere-deployment requirements. The S3-EW uniquely combines VTOL infrastructure-free launch/recovery with long-endurance fixed-wing performance and the structural antenna baseline needed for coherent direction-finding at HF/VHF/UHF frequencies.

**Technical Approach Overview:**

1. **Airframe & Avionics Modification (Task 2):** Define S3-EW system block diagram including airframe, propulsion, SwiftCore avionics, payload bay, antenna integration, RF front end, SDR, edge processor, data link, ground segment, and external interfaces.

2. **Antenna Feasibility Study (Task 3):** Trade conformal antenna integration approaches (planar printed dipoles, tapered-slot elements, fragmented apertures, additive-manufactured structural antennas) leveraging the ~4 m wing span. Recommend baseline multi-element conformal array distributed along leading edge (up to 4 positions per wing) with ~4 m maximum interferometric baseline, plus objective wideband configuration with wing-tip pods and fuselage-mounted elements.

3. **SIGINT/EW Payload SWaP-C (Task 4):** Define baseline SIGINT payload—wideband dual-channel coherent SDR (30 MHz to 6 GHz minimum, growth to ≥18 GHz), low-noise RF front end with multi-octave preselection, multi-channel coherent reference oscillator, edge compute module for real-time energy detection/classification, and SSD forensic storage. Lock SWaP budget against S3 MTOW envelope with ≥10% mass margin and thermal conduction path to wing/fuselage skin. Integrate chip-scale atomic clock (CSAC, e.g., SA.45s) for inter-aircraft TDOA/FDOA coherence.

4. **Swarm CONOPS & Cooperative Geolocation (Task 5):** Leverage SwiftCore cooperative-control heritage (VORTEX2, CRATER, 4-aircraft Hurricane Ernesto 2024 deployment) to define 3–10 aircraft swarm architecture. Simulate cooperative DF, TDOA, and FDOA geolocation accuracy using published Cramér–Rao lower bound (CRLB) results parameterized across number of aircraft (1, 2, 3, 5, 7, 10), standoff range (5, 10, 20, 50 km), inter-aircraft separation (1, 5, 10, 25 km), and time-sync error (sub-microsecond with CSAC). Preliminary analysis indicates 100–300 m geolocation accuracy at 20–30 km standoff against narrowband emitters with three CSAC-disciplined S3-EW aircraft.

5. **Modular Payload Interface (Task 3):** Adopt SOCOM Modular Payload Standard; define mounts, power connections (28 V regulated, 12 V auxiliary, 5 V signaling), high-speed data interfaces (10 GbE for SDR, 1 GbE for C2, CAN-FD for status), time synchronization (PPS + IRIG-B), mechanical mounting, and antenna feed pass-through. Lineage from S2 nose-cone field-swappable architecture.

6. **Field Deployment Workflow (Task 2):** Define ≤5-minute deployment from arrival to airborne via hardened transport case, tool-free assembly sequence, and two-person operator workflow at SOF/USAF technician skill level. Validate via deployment time budget with margin against 300-second total.

7. **Subcontractor Integration (Task 6):** SkyMesa Systems provides RF geolocation algorithms and emitter-tracking software pipeline consuming SDR I/Q streams and outputting bounded geolocation cues for SwiftCore. Fixed-scope teaming agreement and ICD defined at Phase I kickoff.

## Products & Capabilities Described

### S3 (Production Platform)
- **What it is:** Next-generation VTOL fixed-wing UAS, production baseline representing a decade of hard-environment flight experience from S0 and S2.
- **Specifications:**
  - Payload capacity: 2.7 kg (6 lb)
  - Maximum endurance: 110 min
  - Nominal endurance: 90 min
  - Maximum range: 110 km (60 nm)
  - Service ceiling: 20,000 ft MSL
  - Wind tolerance: 30 kt (15 m/s)
  - Wingspan: ~4 m
  - IP42 ingress protection
  - MTOW envelope: ≤11.3 kg (in Phase I SWaP budget)
- **How used in S3-EW context:** Baseline airframe and avionics (SwiftPilot autopilot, SwiftTab user interface, SwiftStation ground station) require minimal modification to field an EW-mission variant with wing-embedded conformal antennas and SIGINT payload integration.

### SwiftCore Flight Management System (FMS)
- **What it is:** Modular, AI-ready flight management system with cooperative-control capabilities, autopilot (SwiftPilot™), user interface (SwiftTab™), and ground station (SwiftStation™).
- **How used in S3-EW context:** SwiftCore hosts swarm orchestration, cooperative sensor-based control behaviors (line-of-bearing intersection, fly-to-maximize-geometry maneuvers, emitter-tracking patterns), and mission autonomy for 3–10 aircraft operating as coordinated swarm. Direct lineal descent from cooperative communication-relay control law developed during Dr. Stachura's PhD.
- **Capabilities:** 
  - Cooperative-control heritage from VORTEX2 (tornado interception), CRATER (multi-aircraft volcanic mission at Poás, Costa Rica), and 4-aircraft simultaneous NOAA Hurricane Ernesto (2024) deployments.
  - Terrain-following profiles using digital elevation models.
  - Multi-aircraft mission planning with battery-endurance prediction.
  - Autonomous cooperative geolocation maneuver execution.
  - Integrated line-of-sight communication checks.

### S0 (Tube-Launched UAS)
- **What it is:** Air-deployed, tube-launched UAS (2.6 lb gross, lightest platform ever to successfully sample tropical cyclones).
- **How used in S3-EW context:** Proof of concept for multi-aircraft simultaneous operations and extreme-environment field validation. Four S0 aircraft deployed simultaneously into Hurricane Ernesto (2024); World Record hurricane endurance and highest wind-speed measurements (240 mph in Hurricane Milton eyewall, NCAR-verified Guinness Record).

### S2 (3 m Wingspan Fixed-Wing)
- **What it is:** 3 m wingspan composite fixed-wing platform with field-swappable nose-cone payload interface.
- **How used in S3-EW context:** Precursor to S3; established proof of concept for modular field-swappable payloads, austere mountainous operations (USGS Makushin volcano work), and multi-aircraft volcanic-plume deployments (Poás CRATER mission). Nose-cone design informs S3-EW modular payload tray architecture.

### DS-GPS (Diverse-Source GPS)
- **What it is:** SDR-based alternative-navigation pipeline using triangulated signals of opportunity fused with machine vision to provide position updates when GNSS unavailable; developed under NOAA SBIR (awarded January 2021).
- **How used in S3-EW context:** Foundational SIGINT engineering demonstrating SDR signal detection, RF emitter triangulation, real-time fusion, and onboard autonomy decisions. Transitions directly to S3-EW SIGINT processing pipeline and Phase II GPS-denied operation validation.

## Use Cases & Applications

### Primary Mission: Agile EW Swarms (NV003)
- **Cooperative RF sensing and geolocation** across 3–10 coordinated aircraft
- **Direction finding (DF)** at VHF/UHF frequencies via wing-embedded conformal antenna arrays with ~4 m interferometric baselines
- **Time-difference-of-arrival (TDOA) and Frequency-difference-of-arrival (FDOA) geolocation** against cooperative and non-cooperating RF emitters at 5–50 km standoff
- **Rapid modular payload reconfiguration** in austere, unprepared terrain (5 min deployment from arrival to airborne)