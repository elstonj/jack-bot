# S3-EW: A Modular Payload Vehicle for Agile Electronic Warfare Swarms with VTOL Ground Launch from Confined Terrain

## Document Metadata
- **Type:** Phase I SBIR Technical Volume (Volume 2)
- **Client/Agency:** Department of the Air Force (DAF)
- **Program/Solicitation:** DAF26BZ01-NV003; DSIP Proposal Number F26BZ-NV003-0062
- **Date:** 2026-05-26 (draft)
- **BST Products/Systems Referenced:** S3, S0, S2, SwiftPilot™, SwiftTab™, SwiftStation™, SwiftCore™ FMS, DS-GPS
- **Key Personnel:** 
  - Dr. Jack Elston (PI, CEO)
  - Dr. Maciej Stachura (Co-Investigator, CTO)
  - Mechanical/Structural Lead [TBD]
  - RF/Payload Engineer [TBD]
  - SkyMesa Systems lead engineer (Arthur Shune, unverified)

## Executive Summary

Black Swift Technologies proposes the **S3-EW**, an electronic warfare variant of the production S3 multi-mission VTOL fixed-wing UAS, to meet DAF26BZ01-NV003 requirements for a low-cost, rapidly reconfigurable, ground-launched small UAS capable of swarm operations (3–10 vehicles) with sophisticated EW payloads. The S3-EW leverages a decade of BST flight heritage in extreme environments (hurricanes, volcanoes, high-altitude operations) to deliver ≥5 lb payload capacity, ≥45 min endurance, ≥100 km range, ≤5-min deployment from confined terrain, and a ~4 m wingspan enabling unprecedented antenna baseline integration for VHF/UHF direction-finding accuracy unattainable on quadcopter platforms.

## Technical Approach

### Core Platform Strategy
BST proposes to modify the **production S3** baseline—already exceeding all published NV003 KPPs—with mission-specific antenna integration and a field-swappable SIGINT payload architecture. This approach eliminates platform-invention risk by leveraging existing, flight-proven S3 maturity.

**S3 Baseline Specifications:**
- Payload capacity: 2.7 kg (6 lb) demonstrated
- Max endurance: 110 min; nominal: 90 min
- Range: 110 km (60 nm) maximum
- Service ceiling: 20,000 ft MSL
- Wind tolerance: 30 kt (15 m/s)
- Wingspan: ~4 m composite fixed-wing
- Launch/recovery: VTOL, no runway/catapult required
- IP42 ingress protection (weather-hardened)
- MTOW: ≤11.3 kg envelope

### Why the S3 Fits NV003 Uniquely

1. **VTOL Deployment (≤5-min requirement):** Native vertical launch/recovery from unprepared, confined terrain; no launcher, runway, or recovery-net dependencies. Tool-free field assembly with captive fasteners and quick-latch mechanisms.

2. **Weather Hardening:** Inherited IP42 rating, reinforced composite airframe, and weather sealing from hurricane (S0) and volcanic (S2) lineage enable operation in dirty, turbulent, particulate-laden conditions that ground quadcopters.

3. **High Service Ceiling (20,000 ft MSL):** Operates above terrain masking, surface ducting, and clutter; extended RF horizon (~170 nm at 20,000 ft). Ongoing USGS-funded Popocatépetl operations (Mexico, elevation 17,694 ft) validate sustained autonomous flight near ceiling in mountain-wave turbulence.

4. **4 m Wingspan for Rich Antenna Integration:** Provides structural baseline **>10× larger** than any Group 2 quadcopter. Wing-embedded conformal antenna elements at multiple positions along span enable interferometric DF baselines up to ~4 m, unlocking VHF/UHF DF accuracy unattainable on smaller platforms. At 300 MHz, 4 m baseline ≈ 4 wavelengths (sub-degree DF accuracy with calibration); at 1 GHz, ≈ 13 wavelengths (high accuracy with ambiguity resolution).

### Modular Payload Interface Philosophy

The S3-EW features a **standardized, field-swappable payload tray** (power, data, mechanical, RF feed) allowing rapid reconfiguration across SIGINT, electronic attack (EA), communications relay, and counter-UAS detection missions without airframe modification. Lineage from S2 nose-cone modularity.

**Power Interface:**
- 28 V regulated primary
- 12 V auxiliary
- 5 V signaling

**Data Interface:**
- One 10 GbE channel for SDR I/Q streaming
- One 1 GbE for command/control
- One CAN-FD for low-rate status
- One PPS + IRIG-B for distributed timing

**RF Feed:** Antenna array feed pass-through with selectable element routing.

### Phase I Technical Objectives

| Objective | Scope | Key Deliverable |
|-----------|-------|-----------------|
| 1. System Architecture & Modular Interface | S3-EW block diagram, open payload ICD, external interface spec | Interface Control Document (ICD) Rev. A |
| 2. Quick-Assembly / VTOL Deployment | Field deployment concept, tool-free assembly, ≤5-min time budget | Deployment time budget, transport-case ICD, assembly procedure |
| 3. Antenna Feasibility (4 m wingspan) | Conformal antenna trade study (HF/VHF/UHF/L/S/C bands), DF baseline optimization | Antenna trade matrix, baseline & objective configs, simulated patterns, DF accuracy bounds (CRLB) |
| 4. SIGINT Payload & SWaP-C | RF front end, wideband SDR (30 MHz–6 GHz+), edge processor, CSAC reference, thermal design | Payload block diagram, vendor matrix, SWaP-C budget summary (±10% closure) |
| 5. Swarm CONOPS & Cooperative Geolocation | 3–10 aircraft swarm definition, inter-aircraft data link (MANET), time sync, cooperative DF/TDOA/FDOA | CONOPS document, geolocation accuracy simulation (CRLB), Phase II demo plan |
| 6. Risk Management & Phase II Planning | Risk register, mitigation plan, Phase II SoW draft | Risk register, Phase II cost volume |

---

## Products & Capabilities Described

### **S3 (Production Platform)**
- **What it is:** Next-generation BST multi-mission VTOL fixed-wing UAS; successor to S2 and S0, integrating >10 years of extreme-environment flight experience.
- **Specifications:** 2.7 kg payload, 110 min endurance, 110 km range, 20,000 ft ceiling, 30 kt wind tolerance, 4 m wingspan, IP42 weather sealing.
- **Heritage:** Hurricane reconnaissance (NOAA), volcanic plume observation (USGS Popocatépetl, Makushin), wildfire airspace surveillance, soil-integrity mapping.
- **S3-EW adaptation:** Addition of wing-embedded conformal antenna arrays and field-swappable SIGINT/EW payload bay; no airframe redesign.

### **S2 (Earlier Generation)**
- **What it is:** 3 m wingspan composite fixed-wing UAS with 2.3 kg payload.
- **Heritage:** Volcanic observations (Poás, Costa Rica; Makushin, Alaska), highest-threat USGS volcano category operations, first BVLOS missions without visual observer.
- **Relationship to S3-EW:** Modular payload architecture (nose-cone swap) lineage; multi-aircraft cooperative operations (NASA CRATER mission, Poás).

### **S0 (Tube-Launched Variant)**
- **What it is:** 2.6 lb lightest platform ever to successfully sample tropical cyclone; air-deployed from NOAA WP-3D Hurricane Hunter P-3 aircraft.
- **Heritage:** Record-setting NOAA hurricane missions (Ernesto 2024, Helene, Milton, Beryl, Melissa 2025); first continuous high-resolution Category 5 eye data. Guinness World Record: 240 mph wind speed (Hurricane Milton), longest endurance inside tropical cyclone.
- **Relevance to S3-EW:** Environmental ruggedness, multi-aircraft cooperative operations, sensor-based control in extreme atmospheric conditions, simultaneous multi-aircraft workflows in degraded RF environments.

### **SwiftCore™ FMS (Flight Management System)**
- **What it is:** Full-stack BST autopilot and mission-control software stack (SwiftPilot avionics, SwiftTab operator interface, SwiftStation ground station).
- **Capabilities:**
  - Native cooperative-control and swarm orchestration behaviors (3–10 aircraft)
  - Sensor-based control for geolocation maneuvers (line-of-bearing intersection, fly-to-maximize-geometry)
  - Cooperative communication-relay flight laws (lineage from Dr. Stachura's PhD work)
  - Terrain-following profiles using DEMs
  - Line-of-sight (LoS) communication checks and battery-endurance prediction for multi-aircraft missions
  - Autonomous mission planning and dynamic baseline reconfiguration during airframe attrition
- **Flight Heritage:**
  - VORTEX2: First UAS intercept of tornadic supercell; 72+ missions in extreme conditions without loss.
  - NASA CRATER mission (Poás, Costa Rica, concluded 2025): Multi-aircraft S2 photogrammetry and trace-gas collection with cooperative control.
  - NOAA Hurricane Ernesto (2024): Four-aircraft simultaneous deployments; four-aircraft Hurricane Melissa (2025) Category 5 mission.
- **S3-EW role:** Primary autopilot and swarm orchestration platform; hosting cooperative-geolocation flight laws and real-time swarm mission adaptation.

### **DS-GPS (Diverse-Source GPS Navigation)**
- **What it is:** SDR-based alternative-navigation pipeline developed under NOAA SBIR (awarded January 2021); fuses triangulated signals of opportunity (RF emitters) with machine vision to provide position updates when GNSS is unavailable.
- **Technical foundation:** SDR signal detection, RF emitter triangulation, real-time fusion, onboard autonomy decisions.
- **Relevance to S3-EW:** Direct technical lineage from atmospheric science into RF signal processing; transitions cleanly to SIGINT engineering and onboard geolocation autonomy.
- **Phase II growth:** GPS-denied S3-EW operation via CSAC + DS-GPS holdover (success criterion: ≤100 m navigation error over 10-min GPS-denied segment).

### **SwiftPilot™ Avionics**
- Dedicated autopilot module onboard S3-EW; provides IMU/GPS fusion, autonomy, and cooperative-control law execution.
- Mass allocation: ~0.6 kg; power: 15 W / 25 W peak.
- No modification required for S3-EW; production avionics.

### **Inter-Aircraft Data Link (MANET)**
- Proposed mesh-style low-probability-of-intercept MANET in 1.3–2.4 GHz band for swarm command, status, and cooperative DF/TDOA/FDOA metadata exchange.
- Growth path to encrypted Type-1 in Phase II/III.
- Mass: ~0.2 kg; power: 5 W / 10 W.

---

## Use Cases & Applications

### **Primary: NV003 Agile Electronic Warfare Swarms**
- **Mission:** 3–10 aircraft cooperative SIGINT and EW operations in support of Air Force Future Operating Concept (AFFOC) distributed sensing, "pulsed airpower," and Agile Combat Employment (ACE).
- **Scenario:** Rapid deployment from austere/confined terrain (no infrastructure), 5-min field assembly, cooperative RF geolocation of emitters at 5–50 km standoff, sustained ≥90-min orbit-hour loiter, modular payload reconfiguration for SIGINT / EA / relay missions.
- **Threat model:**