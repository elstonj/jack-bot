# AN UNCREWED CARRIER AIRCRAFT FOR AIR-DEPLOYED S0 OPERATIONS IN TROPICAL CYCLONES WITH AN ASSESSED GROWTH PATH TO NEXT-GENERATION AIRBORNE RADAR

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center; NOAA Office of Oceanic and Atmospheric Research / Atlantic Oceanographic and Meteorological Laboratory
- **Program/Solicitation:** Not explicitly identified as SBIR/STTR topic in header; document references existing SBIR lineage (N251-016, STTR N6833525C0270, Air Force AF192-005)
- **Date:** August 19, 2026
- **BST Products/Systems Referenced:** S0 (air-deployed uncrewed aircraft), S3, SwiftCore™ (flight management system), SwiftTab™ (operator display), SwiftStation™ (command, control, telemetry), SwiftPilot™
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary

Black Swift Technologies proposes a purpose-built uncrewed carrier aircraft to transport, release, and relay multiple S0 air-deployed aircraft into tropical cyclones, decoupling boundary-layer sampling density from crewed aircraft sortie availability. The carrier will augment (not replace) NOAA's WP-3D reconnaissance fleet by freeing crewed-aircraft capacity for radar, dropsonde, and remote-sensing missions while enabling scaled-up S0 operations. The base effort delivers carrier conceptual design, dispenser architecture, storm-penetration environmental requirements, autonomy architecture, and an assessed pathway for next-generation remote sensing including compact Doppler radar and microwave-sounding-based three-dimensional wind retrieval.

## Technical Approach

**Carrier Aircraft Concept:**
- Sized first by S0 magazine (6–12 stations), endurance (8–12 hours), and storm environment rather than sensor aperture
- Baseline MTOW: 550–1,000 lb; growth variant: 1,100–1,900 lb
- Twin heavy-fuel piston propulsion with hybrid-electric augmentation under evaluation
- Conventional runway basing from coastal operating bases
- Multi-engine requirement (not single-engine) for core-penetration safety redundancy
- Penetration airspeed: 110–160 kt (baseline), 130–180 kt (growth)

**S0 Carriage & Release:**
- Self-contained S0 release architecture without separate launch tube (contrasts with WP-3D drop-tube approach)
- Per-station installed mass target: materially below current 8–10 lb tube-based installations around 3 lb aircraft
- Direct external-station release with integrated retention and separation aerodynamics
- Magazine arrangement trades address aerodynamic penalties and outer-mold-line treatment
- Sequenced, multi-aircraft simultaneous release with health checks and pre-release conditioning

**Environmental Design Basis (Storm-Derived):**
- Design gust loads well beyond normal-category assumptions
- Sustained heavy water ingestion, hail impact, lightning, supercooled liquid water (melting layer), salt exposure at low altitude
- Environmental requirements derived from WP-3D operating record and NOAA storm data (Task 4 deliverable)
- Ice-protection, structural qualification, and propulsion redundancy treated as requirements from outset, not afterthoughts

**Autonomy & Communications:**
- SwiftCore autonomous mission execution for storm patterns
- Flight-critical command & control architecturally independent of mission payload and science data paths
- Load-limiting and contingency autonomy: gust loading, structural margin, ice accretion, energy state, and link health monitoring with approved-threshold response
- 430 MHz meteorological-band relay for S0 air-deployed observations (tested to 400 km)
- Separation of flight-critical control from science-data telemetry; loss of relay/downlink does not remove aircraft control
- Satellite communications for state/prioritized observations alongside line-of-sight relay
- Operator retains launch authority, mission supervision, hold/divert/terminate access

**Operational Concept:**
- Autonomous storm-pattern execution under NOAA-coordinated airspace authorization
- Mission owner designates S0 release points against observing objective
- Released S0 descend into boundary layer, reporting 3D winds, pressure, temperature, humidity through carrier relay
- Advanced sensing (when mature) allows carrier flight patterns and S0 release locations to be coordinated for synergistic observations
- Mission geometry becomes part of observation design

## Products & Capabilities Described

### **S0 Aircraft**
- **What it is:** Uncrewed air-deployed atmospheric sampler with swiveling-wing architecture
- **Status:** Operationally deployed since October 2023 (first deployment in Tropical Storm Tammy); holds world record for highest wind speed measured by uncrewed aircraft (240 mph, Hurricane Milton, October 2024, verified by NCAR)
- **In this context:** Primary payload for carrier; 6–12 units per mission carried and sequentially released into boundary layer
- **Specifications:** ~3 lb; self-contained with integrated atmospheric sensor suite; can measure 3D winds, pressure, temperature, humidity; descends to ~100 ft above ocean surface; 71-minute mission duration demonstrated
- **Heritage:** Deployed from WP-3D since 2023; 2025 season: >1,300 S0 instruments deployed across 417 flight hours, 63 flights into six hurricanes; data assimilated into NOAA hurricane forecast model (2026 season first time)

### **Carrier Air Vehicle (Proposed)**
- **What it is:** Purpose-built, uncrewed fixed-wing conventional-takeoff aircraft
- **Mission:** Transport magazine of S0 aircraft, release on planned/dynamic patterns, remain on station as relay node, support integrated sensor payload
- **Specifications (Planning Estimates):**
  - Baseline: 550–1,000 lb MTOW
  - Growth variant: 1,100–1,900 lb MTOW
  - Endurance: 8–12 hours
  - Multi-engine heavy-fuel piston; hybrid-electric assist under trade
  - Conventional runway operations
- **Payload capacity:** 55–110 lb useful (baseline); TBD growth variant
- **Proposed use:** Independent S0 delivery platform freeing WP-3D capacity; augments rather than replaces crewed fleet
- **Not specified in this design phase:** Final configuration (clean-sheet vs. adapted airframe) TBD during base effort

### **Propulsion & Reliability**
- Multi-engine (required, not optional) for single-point-failure recovery in core penetration
- Hybrid-electric augmentation under evaluation for failure-mode diversity (electric path fails differently than combustion: immune to water ingestion, induction icing, fuel-system disturbance)
- Sized for modest contribution: short-duration climb, altitude hold, egress recovery if combustion engines compromised
- Conditional on environmental qualification: motors, power electronics, wiring, connectors, energy storage must qualify for sustained heavy precipitation, melting-layer icing, salt exposure, vibration/gust-load spectrum

### **Relay & Communications Payload**
- 430 MHz relay for S0 command and telemetry
- Sized for larger simultaneous-link count than crewed WP-3D (current limit: two S0 simultaneously due to channel availability, not aircraft limitation)
- Satellite communications backup for state/prioritized data
- UHF command-and-telemetry chain with characterized antenna and cable losses; AVAPS interference mitigation proven
- Link budget and RF coexistence operationally proven on S0 program

### **Dispenser Architecture (Proposed)**
- Underwing stations with self-contained S0 retention, conditioning, release hardware
- Trade: tube-free vs. tube-based configuration
- Sequencing and health-check logic
- Separation design for high-gust environment
- Interface-control information and separation test approach (Task 3 deliverable)

### **Next-Generation Sensing (Research Objectives, Not Fielded Yet)**

**Candidate Approaches Under Trade:**
1. **Reduced-Aperture Doppler Radar**
   - Smaller form factor than legacy Tail Doppler Radar
   - Constrained by antenna aperture and transmitter power
   - Candidate for baseline carrier integration

2. **Microwave Atmospheric Sounding**
   - Multi-frequency microwave sounder proven in hurricanes
   - Heritage on ATMS (polar-orbiting weather satellites)
   - Retrieves vertically resolved temperature, water vapor, cloud-liquid-water through clouds
   - **High-payoff research objective:** Derive storm-relative 3D winds by tracking moisture and hydrometeor structure in sequential observations, constrained by simultaneous S0 in-situ measurements
   - May extend wind retrieval beyond strong-precipitation regions
   - Fallback value (even if TDR-class winds not achieved): temperature/moisture structure, cloud liquid water, precipitation, SFMR-class surface wind/rain

3. **SFMR-Class Radiometer Measurements**
   - Advanced surface wind and rain-rate measurements
   - Compact implementation targeted

4. **Compact S0 Rain Radar**
   - Near-field Doppler rain radar on S0 airframe
   - Provides local precipitation and relative-velocity measurements along trajectory
   - Low-cost radar chips (auto collision-avoidance technology) as technology basis
   - Validation against reference weather radar planned

**Research Rationale:**
- TDR is observation benchmark; distributed uncrewed architecture creates new opportunities through complementary sensing
- Microwave sounding + S0 direct observations intended to recover 3D winds without full-scale TDR
- Failure to achieve TDR-class performance does not eliminate microwave sensor value (fallback products listed above)
- Assessment will determine which concepts fit baseline carrier vs. require growth-variant aircraft

**Payload Envelopes (Task 6 Deliverable):**
- Mass, volume, aperture, power, cooling, scan geometry, data rate for most promising concepts
- Determination of baseline vs. growth-variant accommodation
- Rough growth-variant design where required

## Use Cases & Applications

### **Primary Mission: Tropical Cyclone Boundary-Layer Sampling**
- **Observing Gap Addressed:** Satellites, radars, buoys, vessels, crewed aircraft lack required access, altitude coverage, timing, or spatial resolution in boundary layer
- **S0 Contribution:** Targeted in-situ 3D winds, pressure, temperature, humidity in region too hazardous for crewed continuous sampling
- **Current Operations (2025 Season):** 1,300+ instruments deployed, 417 flight hours, 63 flights into six hurricanes
- **2026 Season:** Small uncrewed aircraft data assimilated into NOAA hurricane forecast model (first time)

### **Intensification of Boundary-Layer Sampling**
- **Current Constraint:** Boundary-layer sampling density limited by WP-3D sortie availability and crew duty day; 4 S0 per typical sortie (two pairs, one later in mission if time allows)
- **Proposed Solution:** Dedicated carrier enables planned, dynamic spatial/temporal release patterns independent of crewed sortie availability
- **Coverage Improvement:** Longer loiter time, planned dynamic release adjustment, remain on-station as relay node, support additional sensing

### **Freeing Crewed-Fleet Capacity**
- **WP-3D Current Constraint:** Simultaneous radar, dropsonde, remote-sensing, and S0-carriage missions share a single platform and crew duty day
- **Proposed Outcome:** Moving S0 carriage to dedicated uncrewed aircraft returns WP-3D capacity to radar, dropsonde, and remote-sensing collection
- **Result:** More of both observation types rather than reallocation between them; more complete storm description

### **Capacity Transition (2030 Timeframe)**
- **Strategic Context:** WP-3D aircraft retire ~2030; C-130J replacements enter service 2030
- **Problem:** C-130J has no tail structure for existing Tail Doppler Radar transfer; TDR re-installation approach not yet determined (as of latest oversight reporting)
- **Role of Carrier:** Add observing capacity across WP-3D–to-C-130J transition without adding crewed airframes or reducing reconnaissance missions

### **Advanced Sensing Validation**
- **Distributed Architecture Advantage:** Carrier remote sensing can be coordinated with S0 direct observations for complementary validation
- **S0 as Constraint:** In-situ measurements within remotely sensed storm volumes allow repeated carrier observations to be validated and constrained
- **Research Path:** Microwave sounding + S0 wind/