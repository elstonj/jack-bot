# BST ONR 6.4 Proposal Response: S0-MET / S0-ARO

## Document Metadata
- **Type:** Proposal response / technical approach document
- **Client/Agency:** University of Washington (Prime), Office of Naval Research (ONR)
- **Program/Solicitation:** ONR 6.4 (Advanced Component Development & Prototypes); Subcontract under UW PI Dr. Elizabeth Sanabia
- **Date:** 2026-05-14 (created/modified)
- **BST Products/Systems Referenced:** Hurricane-S0 sUAS platform
- **Key Personnel:** Jack Elston (BST Subcontractor PI), M. Stachura (CTO), Beck Cotter (last editor)

---

## Executive Summary

Black Swift Technologies proposes to develop and deploy a tube-deployable sUAS for marine meteorological surveying aboard the WC-130J aircraft. The Hurricane-S0 platform will incrementally add capabilities over three years: Year 1 establishes VHF telemetry and basic meteorological sensing; Year 2 adds active radar-driven low-altitude flight and oceanographic wave-state estimation; Year 3 demonstrates GPS Airborne Radio Occultation (ARO) for atmospheric refractivity profiling. Total program value: $317,376 over 3 years (6-8 aircraft delivered).

---

## Technical Approach

### Year 1: Hurricane-S0 + SST + VHF Datalink + WC-130J Support Equipment

**Core Platform:**
- Two Hurricane-S0 sUAS per year in LAU-126A-compatible A-size tube configuration
- Sensors: pressure, temperature, humidity, altitude, lat/lon/time, 3D winds, 50 Hz radar altimeter (for wave heights), IMU and dual-antenna GNSS heading (heading, speed, pitch, roll, yaw)
- GNSS architecture unchanged from baseline: u-blox ZED-F9H + ZED-F9P (40 cm baseline) with existing Linx ANT-GNCP-C25L125100 antenna

**VHF Datalink (Migration from 430 MHz UHF to VHF):**
- **Radio selection:** Doodle Labs Mesh Rider Helix-V (RM-2050-V series, 144–235 MHz), ~70 g, <5 W TX, IP-based mesh. Fallback: Microhard L-series VHF or custom ADRV9002-based SDR.
- **Operating band:** 162.25–173.5 MHz (upper sonobuoy block, VHF green-list channels via 53rd WRS)
- **Antenna design:** Replace 32 cm PCB monopole (too short at VHF) with 45 cm spring-steel whip with base-loading coil (~3–6 µH), targeted at 168 MHz center. Expected performance: 70–85% radiation efficiency, 8–10 MHz 2:1 VSWR bandwidth. Mechanical qualification for tube-launch shock (450 g) and slipstream loads.
- **Link budget advantage:** At 168 MHz vs. 430 MHz baseline, path-loss advantage of 8.7 dB results in net link margin improvement of +7 to +9 dB at 400 km range, matching or exceeding existing UHF range despite lower frequency.

**Spectrum Authorization:**
- DD Form 1494 filing in Month 1 (lead time 4–9 months); critical path item
- Year 1: downlink (UAS→aircraft) only
- Coordination through 53rd WRS frequency manager and Navy Marine Corps Spectrum Office

**WC-130J Support Equipment:**
- Ruggedized operator interface (laptop/tablet running BST GCS software): displays aircraft state, battery, comms quality, GPS solution, flight state, position, altitude, heading, in-flight meteorological observations, deployment status
- Base station: VHF receiver, antenna feed, modem, decoder; captures telemetry, decodes structured data, pipes to operator interface; measures RSSI, BER, packet rate for link-quality assessment
- Both subsystems are non-flight-critical, ship-loose installations, built on existing BST P-3 platform heritage

**Sea-Surface Temperature (SST) Sensor:**
- Best-effort integration: compact downward-looking IR pyrometer (8–14 µm atmospheric window)
- Candidates: Melexis MLX90640 array (32×24, ~50 mm, <5 g) or Heimann HTPA module
- Calibration against co-located buoy or drop-thermistor reference
- **Risk:** Motor/cowling thermal reflections; Month 3 go/no-go review for ±0.5 K calibration uncertainty; descope to Year 2 if not achievable

**Deployment Profile:**
- Launch from LAU-126A at ~10,000 ft AGL
- Descent to target ~10 m (33 ft) AGL, as close to sea surface as possible
- Primary scientific focus in lowest 500 m
- Two BST field trips to Keesler AFB: 4 days each, 1 FTE per trip

---

### Year 2: Radar-Following, Wave-State Metrics, Two-way VHF, Data Pipeline

**Active Radar-Driven Low-Altitude Flight:**
- Tighten the existing 50 Hz radar altimeter role in flight-control loop
- Enable wave-following (constant altitude above moving sea surface) rather than fixed altitude above still-water surface
- Goal: extend practical minimum altitude by 30–50% in calm-to-moderate conditions
- Control-law tuning, bench/hardware-in-the-loop verification, low-to-moderate sea-state flight test during Y2 Keesler campaign

**Ocean-State Characterization:**
- Estimate significant wave height (Hs) and mean-squared slope (MSS) onboard via spectral-domain Extended Kalman Filter
- Leverages BST Navy STTR Phase II (Contract N6833525C0270, Topic N25A-T025) algorithm development as in-kind contribution
- Filter models surface elevation η(s,t) as Fourier series with Gauss–Markov time updates on coefficients
- **Target accuracies** (per SASCWATCH ONR program): Hs < 3%, MSS < 10%
- BST STTR Phase I showed S0 radar noise <50 cm is sufficient to meet targets
- On-contract validation via intercomparison with NDBC buoys and EASI/ASIS reference buoys during Y2 deployments
- Compute architecture: STM32MP1-class heterogeneous SoC for onboard real-time processing

**Two-Way VHF / Uplink for Adaptive Sampling:**
- Year 1 radio hardware is already bidirectional; Year 1 operates downlink only
- Year 2 submits DD-1494 amendment to add uplink authorization
- 53rd WRS frequency-manager coordination and Navy Marine Corps Spectrum Office paperwork
- Operator interface configured for in-flight profile commanding (pre-determined profiles in Y1 become adaptive in Y2)
- Cost impact: primarily consulting hours; no new flight hardware

**GTS / RTDHS / Navy EM Data Pipeline:**
- In-flight: S0 streams meteorological observations over VHF link to WC-130J in real time
- On WC-130J: small Linux SBC gateway module decodes BST telemetry and transcodes to WMO BUFR / TAC format compliant with operational dropsonde data model (TEMP DROP, BUFR template TM 311001)
- Off-aircraft: BUFR message forwarded to GTS via operational Air Force/Navy gateway, to RTDHS via NOAA ingest path, and to Navy-specific EM models
- Intercomparison: Y2 flights over co-located "truth" sensor (moored buoy or co-deployed dropsonde)

**Year 2 Deployments:**
- Two trips: one to Keesler AFB, one to Travis AFB for Atmospheric River mission (Biloxi fallback if AR not supported)
- 4 days each, 1 FTE per trip
- 2–3 S0 aircraft (substantially same configuration as Y1)

---

### Year 3: ARO Feasibility Study + Continued Operational Flights

**ARO Overview (Passive Limb-Sounding Technique):**
- Based on Cao et al. (2025) approach: observes setting/rising GNSS satellites occulted by atmospheric limb
- Tracks excess Doppler/carrier phase as satellite sets behind atmosphere; bending angle inverted via Abel transform to refractivity vs. altitude
- **NOT GNSS-Reflectometry:** no nadir antenna, no DDM, no surface scattering; uses direct-path signals from low-elevation satellites; fundamentally passive using standard geodetic GNSS hardware
- S0 ceiling ~15,000 ft (~4.6 km) vertically samples only lower 3–4 km of troposphere — exact volume of interest for marine-boundary-layer/refractivity objective (primary focus lowest 500 m)
- Deliverable is feasibility demonstration, not operational ARO product

**Receiver Selection — Septentrio mosaic-X5:**
- 31 × 31 × 4 mm, 6.8 g, 0.6 W typical / 1.1 W max
- Multi-constellation multi-frequency: GPS L1/L2/L5, Galileo E1/E5a/E5b/E6, GLONASS L1/L2, BeiDou B1/B2/B3, QZSS, NavIC
- Output: SBF or RINEX at 1–100 Hz with carrier phase, pseudorange, Doppler, SNR, lock-time
- Mounted on carrier PCB; net SWaP impact: ~+6 g, ~+0.5 W, +0.5 cm height vs. existing F9H
- Easily absorbed into existing payload bay

**ARO Antenna Selection — Tallysman TW7972:**
- Dual-feed broadband-LNA variant of TW3972
- Ø75 × 22 mm, ~50 g, L1/L2/L5 + E5b, integrated LNA, good phase-center stability
- Mounts cleanly on S0 top fuselage forward of wing with clear horizon-to-zenith visibility for tracking setting/rising satellites
- Existing Linx antenna retained for F9H/F9P navigation (independent systems, no impact to nav function)

**Onboard Logging & Ground Processing:**
- **Onboard:** Capture, timestamp, store raw SBF observables at 1 Hz multi-GNSS (~30–50 MB/hr) on existing autopilot SD card or small dedicated logger (Raspberry Pi Zero 2 W class)
- **Critical workflow:** Aircraft used for ARO data collection are recovered after each sortie for raw-observable download (distinction from Y1/Y2 expendable missions)
- **Ground-side processing (post-flight):** 
  - SBF → RINEX 3 conversion (Septentrio RxTools)
  - PPP-AR using RTKLib or PRIDE-PPPAR with CODE/WHU MGEX precise orbits/clocks
  - Excess-phase calculation and Savitzky–Golay filtering at first-Fresnel-zone time scale
  - Bending angle and Abel inversion to refractivity using ROM SAF ROPP toolkit
  - Intercomparison with Y1/Y2 derived-refractivity profiles
- **BST scope:** Hardware integration, ground-station SBF logging tooling, processing pipeline, algorithm development for S0 altitude regime, single-pass end-to-end demonstration on flight data. Operational ARO production processing and science validation remain UW/Scripps responsibilities.

**Total Year 3 ARO Payload SWaP:**
| Item | Mass | Power | Volume |
|------|------|-------|--------|
| Septentrio mosaic-X5 (on carrier PCB) | ~15 g | 1.1 W max | ~40 × 40 × 8 mm |
| Tallysman TW7972 antenna | ~50 g | 0.1 W (LNA bias) | Ø75 × 22 mm |
| Coax / connectors / mounting