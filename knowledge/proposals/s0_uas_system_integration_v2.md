# S0 UAS System Integration Reference: Host-Aircraft Integration of the Black Swift S0 Air-Deployed UAS

## Document Metadata
- **Type:** Technical Integration Reference / Engineering Specification
- **Client/Agency:** Multiple: NOAA (operational baseline); USAF/AFRC 53rd Weather Reconnaissance Squadron (proposed); USSOCOM (CRADA); UK Royal Navy / UK MoD (proposed)
- **Program/Solicitation:** 
  - NOAA: Operational deployment (WP-3D Orion, N42RF and N43RF)
  - USAF: AFX255-DPCSO1 Direct-to-Phase-II (D2P2), proposal F2D-16162
  - USSOCOM: CRADA 20-01-XXXX (signed 3 March 2026)
  - UK MoD: Project RAVEN, funded 21 May 2026, 1 July 2026 start (UK £ amount not stated)
- **Date:** 21 May 2026 (Revision B; supersedes Rev. A from 20 October 2025)
- **BST Products/Systems Referenced:** S0 (S0-AD air-deployed variant), SwiftCore avionics, SwiftTab operator interface, ground stations (1U rack-mount and portable carry-on variants), Microhard P400 radio
- **Key Personnel:** Jack Elston (editor), Joshua Fromm (CAD/mass properties), Alex Lomis (mass measurement), Maciej Stachura, Dan Prendergast, Bob "Bam Bam" Smith (KrateoSky), Joe Cione (NOAA)

---

## Executive Summary

This document consolidates engineering details for integrating the Black Swift S0 air-deployed unmanned aircraft system into four distinct host platforms: the NOAA WP-3D Orion (validated baseline with 21 operational deployments in the 2025 hurricane season), the USAF WC-130J (proposed D2P2 effort with 53rd Weather Reconnaissance Squadron), a USSOCOM C-130 (rear-ramp hand-deployment under a signed CRADA), and the UK Royal Navy AgustaWestland AW101 Merlin Mk2 (proposed under the UK-funded RAVEN programme starting July 2026). The S0 is packaged in an AXBT-compatible (NATO A-size sonobuoy) canister allowing deployment through existing freefall chutes, paratroop-door chutes, hand-release, and automatic sonobuoy dispensers without airframe modification. Each platform section addresses mechanical deployment, RF/antenna architecture, ground-station installation, interference mitigation, crew procedures, and outstanding integration items.

---

## Technical Approach

### Overall System Architecture

**Air Vehicle:**
- Compact, air-deployable UAS designed for extreme atmospheric environments (tropical cyclones, severe convection, marine boundary-layer studies)
- AXBT-compatible canister (4.875 in / 124 mm diameter, ~36 in / 914 mm length) enables drop-in replacement of standard sonobuoys
- Deployment sequence: gravity release through sleeve → ~0.5 s internal pilot-chute deploy → ~10–12 s descent under main chute → chute cut and swivel-wing deployment → autonomous powered flight (~30 s total release-to-powered-flight)
- SwiftCore flight management system onboard: dual IMU (redundant), dual GPS with RTK heading, magnetometers, radar altimeter (AGL), pressure/temperature/humidity sensor (Vaisala RSS421), 1.8″ modular payload bay (100 g interface)

**Ground Station Variants:**
1. **1U Rack-Mount** (NOAA P-3 production baseline)
   - 19″ 1U chassis, ruggedised, permanently installed in aircraft mission bay
   - Power: 110 VAC 60 Hz aircraft bus with internal UPS battery (45 s ride-through when UAS active, 20 s when idle)
   - Gateworks single-board computer running BST's gcsDaemon, Microhard P400 radio, encrypted Wi-Fi pod, multi-function diagnostic LED, external USB for flight-log retrieval
   - Status: Two units fielded; additional two funded by NOAA (delivery target 27 May 2026); third spare supporting three-radio test bench

2. **Portable Carry-On** (WC-130J, SOCOM, Merlin baseline)
   - Ruggedised Pelican-class travel case, ~90 lb gross weight (48 × 22 × 10 in)
   - Internal rechargeable battery ≥8 h endurance, charged from 110/220 VAC during preflight
   - Same Gateworks board, P400 radio, SwiftTab interface as 1U unit
   - Single coaxial cable to removable external antenna; optional Mini-Circuits ZVBP-435-S+ bandpass filter in-line
   - Status: Engineering build complete; fielded as test station in March 2026 P-3 multi-aircraft training

**Radio & Link Architecture:**
- Microhard P400 transceiver, narrowband mode (12.5 kHz bandwidth), frequency-agile across 400–470 MHz
- Baseline configuration (NOAA P-3): 431 MHz transmit (S0→GCS), 430 MHz receive (GCS→S0), 2 W transmit power
- Demonstrated performance (2025 hurricane season): 247 mi (215 nm) maximum air-to-ground range, 400 km point-to-point ground test
- Link uses AES-128/256 encryption; Wi-Fi between SwiftTab and GCS encrypted WPA2 on isolated network
- Lost-comms behaviour: S0 continues pre-programmed mission, holds 3,000 ft AGL hard ceiling for manned-aircraft deconfliction, executes recovery/scuttle on mission end or link restoration

**Operator Interface:**
- SwiftTab: BST Android tablet application, real-time displays of S0 range, altitude, airspeed, link quality (RSSI, packet percentage), sensor health, waypoint editing in-flight
- Encrypted Wi-Fi link to GCS; configured rugged tablet (COTS device operation not supported operationally)

---

## Products & Capabilities Described

### S0 Air Vehicle
**What it is:**
- Compact, air-deployable unmanned aircraft for extreme atmospheric sampling (hurricanes, severe convection, marine boundary layers)
- TRL 8–9 (NOAA describes operational S0 data product as TRL-9)

**Performance (2025 Hurricane Season Reference):**
- Endurance: up to 2 h powered flight; 119 min maximum demonstrated (Hurricane Melissa)
- Cruise speed: 20–22 m/s (~42 kt)
- Maximum dash: >40 m/s (<100 mph)
- Maximum measured wind: 191 kt sustained in-storm (2025), 209 kt gusts (2024 Hurricane Milton)
- Communications link range: 247 mi (215 nm) demonstrated, 190 nm design baseline
- Flight ceiling: 15,000 ft
- Operational range from host: ~80 nm (mission-limited, not link-limited)

**Canister & Mass Properties:**
- Launch mass: ~3 lb (1.4 kg) estimated (to be confirmed against current build)
- Chute module mass: 1,050 g (measured)
- Total canister + air-vehicle mass: **TBD** (action item: Joshua Fromm to provide from CAD; Alex Lomis to weigh flight-ready canister)
- Centre of gravity (packed canister): **TBD**
- Mass moment of inertia (long axis): **TBD**
- Form factor: AXBT / NATO A-size (4.875 in / 124 mm nominal diameter, ≈36 in / 914 mm length)
- Initial separation: gravity release through sleeve, internal pilot-chute deploys within ~0.5 s of slipstream exit

**Avionics & Sensors:**
- SwiftCore Flight Management System (autopilot board, redundant IMU, dual GPS with RTK heading, magnetometers, radar altimeter AGL)
- Atmospheric sensing: Vaisala RSS421 in-situ probe (P, T, RH), flush-air-sensing nosecone (3D wind vectors independent of airframe attitude)
- 1.8″ diameter modular payload bay (100 g interface); field-swappable, compatible with existing P-3 data stream and NOAA AVAPS sonde formats
- Optional integrated sensors: surface temperature sensor, radar altimeter (wave height/slope at low altitude), magnetometer (MAD—under development for US Navy and UK Royal Navy; Bartington Instruments UAS-MAG and QuSpin options competed under Navy SBIR Phase II), EO/IR camera (SOCOM CRADA evaluation)

### Ground Station Variants
**1U Rack-Mount (P-3 production):**
- Form factor: standard 19″ 1U rack chassis
- Front panel: power switch, power LED, multi-function diagnostic LED (coded fault patterns), externally accessible USB (flight-log retrieval)
- Rear panel: GPS antenna (TNC/SMA), radio antenna (TNC), Ethernet (AirOps/HDOB upload), 110 VAC inlet, internal UPS battery
- Primary power: 110 VAC 60 Hz aircraft bus
- Backup: internal OpenUPS2-based battery, seamless ride-through during brief power interruptions (UPS_SHUTDOWN_WAIT = 45 s when UAS communicating, 20 s when not; immediate shutdown at 5% SOC; UPS_HARDOFF_TOUT = 60 s)
- Networking: encrypted Wi-Fi (operator tablets) + aircraft-network Ethernet for AirOps / IWG1 / HDOB
- Status: Production. Two fielded; two additional funded by NOAA (delivery 27 May 2026); third (spare Gateworks board) supports three-radio test bench

**Portable Carry-On (WC-130J / SOCOM / Merlin):**
- Form factor: ruggedised travel case (Pelican-class), carry-on baggage certified
- Dimensions: ~48 × 22 × 10 in (approximate); ~90 lb gross with spares
- Power: internal rechargeable battery ≥8 h continuous operation
- Charge: 110/220 VAC during preflight; automatic switchover, over-discharge protection, thermal management
- RF: single coaxial cable to removable external antenna (or aircraft's existing 430 MHz antenna where present)
- Optional filter: Mini-Circuits ZVBP-435-S+ bandpass filter installable in-line to attenuate out-of-band emissions
- Status: Engineering build complete; fielded March 2026 P-3 multi-aircraft training flight

### SwiftTab Operator Interface
- Android tablet application connected to GCS over encrypted Wi-Fi
- Real-time displays: S0 range, altitude, airspeed, link quality (RSSI, valid-packet %), sensor health
- In-flight waypoint editing capability
- Provided with configured rugged tablet; unconfigured COTS device operation not operationally supported

### RF Chain & Antenna Systems

**Radio:**
- Microhard P400 transceiver, narrowband (12.5 kHz bandwidth), frequency-agile 400–470 MHz
- Baseline (NOAA P-3): 431 MHz TX, 430 MHz RX, 2 W power
- Demonstrated: 400 km point-to-point ground, 247 mi (215 nm) air-to-ground

**Antennas:**
- **P-3:** Existing 430 MHz wing-mounted antenna (from prior UAS/expendable-instrument operations); second-channel installed aft-fuselage Feb 2026 near under-tail disc radar
  - Cable losses verified (March 2026): Channel 1: 1.7 dB; Channel 2: 2.5 dB (post-replacement)
  - End-to-end antenna-to-filter-output: 12.85 dB (primary filter), 12.83 dB (backup filter)
  - Concurrent dual-channel test (March 2026): no appreciable RSSI degradation at close range; ~10–15 dB difference at range during