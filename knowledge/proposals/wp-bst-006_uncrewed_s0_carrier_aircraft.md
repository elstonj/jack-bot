# AN UNCREWED CARRIER AIRCRAFT FOR AIR-DEPLOYED S0 OPERATIONS IN TROPICAL CYCLONES WITH AN ASSESSED GROWTH PATH TO NEXT-GENERATION AIRBORNE RADAR

## Document Metadata
- **Type:** White paper / proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center; NOAA Office of Oceanic and Atmospheric Research / Atlantic Oceanographic and Meteorological Laboratory (AOML)
- **Program/Solicitation:** Standalone proposal; mentions NOAA IDIQ (1305M226D0012), SBIR Phase III pathway (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005), and NOAA Broad Agency Announcement (open through 30 Sept 2026)
- **Date:** August 19, 2026
- **BST Products/Systems Referenced:** 
  - S0 (air-deployed uncrewed aircraft for boundary-layer sampling in tropical cyclones)
  - S3 (VTOL fixed-wing reference platform)
  - SwiftCore™ (flight-management system)
  - SwiftTab™ (operator display interface)
  - SwiftStation™ (command, control, and telemetry link)
  - SwiftPilot™ (autonomy software)
- **Key Personnel:** Jack Elston (last editor)

---

## Executive Summary

Black Swift Technologies proposes an uncrewed carrier aircraft purpose-designed to transport, release, and relay multiple S0 aircraft into tropical cyclones, enabling boundary-layer sampling to scale independently of crewed WP-3D sortie availability. The carrier augments (rather than replaces) the reconnaissance fleet, freeing the WP-3D to focus on radar, dropsonde, and remote-sensing missions that require human crews. In parallel, BST and sensor-development partner Weather Stream, Inc. assess a next-generation distributed sensing architecture combining compact Doppler radar, microwave atmospheric sounding, SFMR-class radiometer measurements, and S0 in-situ observations to recover three-dimensional wind fields and precipitation structure. The program is gated: the base effort delivers a decision-quality conceptual design for an S0 carrier plus a radar-pathway assessment; separable options build and fly the carrier, qualify the dispenser, demonstrate in-storm operations, and retire advanced sensor risk.

---

## Technical Approach

### Carrier Air Vehicle Concept
- **Configuration:** Purpose-built uncrewed aircraft (not an adaptation of existing platforms like MQ-9)
- **Primary payload:** 6–12 underwing S0 stations (baseline); growth variant accommodates additional radar/sensing payload
- **Sizing drivers:** S0 magazine capacity, 8–12 hour endurance, storm-penetration environment (not large sensor aperture)
- **Baseline MTOW:** 550–1,000 lb; growth variant 1,100–1,900 lb
- **Propulsion:** Twin heavy-fuel piston engines with hybrid-electric augmentation under evaluation (multi-engine is a requirement, not a preference, for survival in eyewall power-loss scenarios)
- **Penetration airspeed:** 110–160 kt (baseline); 130–180 kt (growth)
- **Basing:** Conventional runway, coastal operating base

### S0 Dispenser Architecture
- **Self-contained S0 design:** Eliminates external launch tube required for WP-3D air deployment; S0 carries own retention interface and separation aerodynamics
- **Per-station installed mass:** Significantly below the 8–10 lb tube-based baseline (exact figure TBD in Task 3)
- **Magazine arrangement:** Trade between 6–12 external underwing stations; typical WP-3D practice releases 2–4 S0 per sortie, constrained by command-and-telemetry channel availability rather than aircraft capacity
- **Release sequencing:** Managed by carrier autonomy against observing requirement rather than shared sortie constraints

### Autonomy & Command-Control Architecture
- **SwiftCore-based mission execution:** Autonomous pattern flying, S0 release sequencing, relay payload operation
- **Flight-critical vs. mission-payload separation:** Command-and-control remains independent of mission data; loss of relay or science downlink does not remove flight control
- **Load-limiting autonomy:** Gust-load, structural-margin, ice-accretion, and energy-state monitoring with threshold-triggered altitude change, pattern truncation, egress, or diversion
- **Operator authority:** Operator retains launch authority, mission supervision, and hold/divert/terminate functions
- **UHF command-and-telemetry:** 430 MHz meteorological allocation; characterized to 400 km range; proven with WP-3D S0 deployments since 2023
- **Storm-field simulation:** Hardware-in-the-loop environment couples carrier autonomy to realistic hurricane wind and rain fields (leverages NCAR atmospheric-system support from S0 development)

### Environmental & Structural Requirements
- **Design basis:** Derived from WP-3D operating record and NOAA storm data
- **Gust-load and maneuver spectrum:** Core penetration implies design loads well beyond normal-category assumptions
- **Water ingestion and hail:** Sustained heavy precipitation, hail impact
- **Icing:** Supercooled liquid water in melting layer
- **Lightning, salt/humidity exposure:** Low-altitude sustained exposure
- **Qualification approach:** Identify cost-driving requirements; determine which relaxed-envelope trade-offs materially reduce cost

### Hybrid-Electric Propulsion Evaluation
- **Rationale:** Electric power path fails differently than combustion engines; water ingestion, induction icing, and fuel-system disturbance do not affect motors and stored energy
- **Sizing:** Modest hybrid contribution for short-duration climb, altitude hold, and egress (provides recovery path independent of combustion engine operation)
- **Trade conditions:** Motors, power electronics, connectors, wiring, and energy storage must be qualified for sustained heavy precipitation, melting-layer icing, salt exposure, and penetration vibration and gust loads; energy-storage mass trades directly against endurance
- **Status:** Under evaluation in Task 4 trade rather than adopted on efficiency grounds

---

## Products & Capabilities Described

### S0 (Expendable Air-Deployed Aircraft)
- **What it is:** Uncrewed aircraft released from crewed hosts; swiveling-wing architecture with integrated atmospheric sensor suite
- **Current performance:** 71-minute mission endurance from Tropical Storm Tammy (Oct 2023); descended to ~100 ft above ocean; holds world record for highest wind speed measured by uncrewed aircraft: 240 mph in Hurricane Milton (Oct 2024, verified by NCAR)
- **Operational heritage:** NOAA AOML deployed S0 from WP-3D since 2023; integrated into NOAA hurricane forecast model for 2026 season assimilation
- **Measurements:** Three-dimensional winds, pressure, temperature, humidity in tropical cyclone boundary layer
- **Release packaging (current):** 6-inch diameter, 36-inch long launch tube; ~8–10 lb installed mass per aircraft including tube, sabot, retention, conditioning, release hardware
- **Proposed (carrier-based):** Self-contained S0 with integrated retention and separation aerodynamics; no external tube
- **Data link:** 430 MHz UHF command-and-telemetry through carrier relay; proven to 400 km range
- **Non-recoverable:** Each release consumes an aircraft (as with current WP-3D deployment)

### SwiftCore Flight-Management System
- **Function:** Autonomous mission execution from launch through recovery; aircraft health monitoring; payload interfaces; automated fault response
- **Reuse:** Directly applicable to carrier autonomy; couples to storm-field simulation environment for navigation, sampling logic, load-limiting, and contingency testing against realistic wind and rain fields
- **Status:** Proven on S0 program since 2023

### SwiftTab & SwiftStation
- **SwiftTab:** Operator display and authority interface
- **SwiftStation:** Command, control, and telemetry link management
- **Status:** Operationally proven with NOAA S0 deployments

### S3 (Reference Platform)
- **What it is:** VTOL fixed-wing aircraft in BST's current line
- **Relevance to carrier design:** Not a direct airframe basis; provides reference for payload interface discipline, autonomy stack, and demonstrated ability to field new configurations
- **Specifications:** 2.7 kg payload capacity, 110 min flight time, 110 km range, 20,000 ft MSL ceiling, 30-knot wind resistance
- **Payload heritage:** Microwave radiometers, electro-optical/thermal imagers, atmospheric probes, trace-gas instruments, aerosol sensors

---

## Use Cases & Applications

### Primary Use Case: Tropical Cyclone Boundary-Layer Sampling
- **Mission:** Release S0 aircraft from uncrewed carrier into hurricane boundary layer
- **Observing objective:** Collect three-dimensional winds, pressure, temperature, humidity in regions unsafe for crewed aircraft
- **Current operational gap:** NOAA's WP-3D is the only platform delivering boundary-layer in-situ measurements; limited by crewed sortie availability, crew duty day, and shared carriage with other sensor missions (radar, dropsondes)
- **Proposed solution:** Dedicated carrier removes S0 carriage from shared sortie; enables release in planned spatial/temporal patterns driven by observing requirement rather than by shared-mission constraints
- **Scale:** 2025 season: 1,300+ S0 instruments deployed from WP-3D fleet across 417 flight hours and 63 flights into 6 hurricanes

### Secondary Use Case: Remote Sensing & Next-Generation Wind Retrieval
- **Distributed observing system:** Carrier remote sensing (compact Doppler radar, microwave sounding, SFMR-class surface measurements) plus simultaneous S0 direct observations within remotely sensed volume
- **Research objective:** Determine whether repeated microwave observations of moisture and hydrometeor structure, constrained by S0 in-situ measurements, can recover useful three-dimensional storm-relative winds without requiring full-scale Tail Doppler Radar
- **Potential outcome:** Extension of wind retrieval beyond strong-precipitation regions; validation of satellite microwave-sounding moisture-tracking methods at airborne timescales

---

## Key Results

This is a proposal/white paper, not a completed study report. However, it documents BST's operational track record:

### S0 Program Results (2023–2026)
- **First deployment:** October 2023, Tropical Storm Tammy; 71-minute flight; descended to ~100 ft above ocean
- **Record measurement:** 240 mph peak wind in Hurricane Milton (October 2024); verified by NCAR
- **2025 operational scale:** 1,300+ S0 instruments, 417 flight hours, 63 flights, 6 hurricanes
- **Model integration:** NOAA hurricane forecast model assimilating small uncrewed aircraft data (2026 season)
- **Measurement validation:** NOAA has validated both the measurement and the operational S0 concept

---

## Notable Details

### Why a Purpose-Built Carrier vs. Existing Platforms (MQ-9, etc.)

BST explicitly argues against adaptation of DoD inventory aircraft:

1. **Propulsion redundancy:** MQ-9 is single-engine; disqualifying for sustained eyewall penetration where engine failure has no recovery path
2. **Certified weather envelope:** Air Force guidance restricts MQ-9 flight into forecast moderate or worse icing and minimizes known icing; mission design excludes tropical cyclone core environment
3. **Structural design basis:** MQ-9 optimized for long-endurance ISR in permissive airspace; not designed for eyewall gust-load spectrum, icing, or hail environment; requalification would be a major structural program
4. **Right-sizing:** MQ-9 cost reflects survivability, multi-role weapons/ISR provisioning, secure military datalinks, worldwide deployment/sustainment; tropical cyclone reconnaissance does not require these and should not pay for them; resulting platform is larger, costlier per flight hour, more infrastructure-dependent than NOAA mission needs
5. **Acquisition posture:** Government program office, export control, contractor ground segment, sustainment tail designed for different mission; poor fit for NOAA fleet of 2–3 aircraft operating from non-fixed coastal base

### Capacity Argument & WP-3D Transition Risk

- **Crewed capacity constraint:** Federal oversight reporting shows reconnaissance demand growing faster than NOAA and Air Force capacity can absorb
- **Fleet retirement:** WP-3D scheduled to retire ~2030