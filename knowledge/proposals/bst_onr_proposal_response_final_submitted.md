# S0-MET / S0-ARO: 6.4 ONR Subcontract Response

## Document Metadata
- **Type:** Proposal response / Technical approach document
- **Client/Agency:** Office of Naval Research (ONR); Prime contractor: University of Washington (PI: Dr. Elizabeth Sanabia)
- **Program/Solicitation:** ONR 6.4 (Advanced Component Development & Prototypes)
- **Date:** Submitted May 14–15, 2026
- **BST Products/Systems Referenced:** Hurricane-S0 sUAS (2–3 units per year over 3 years), WC-130J support equipment (operator interface, base station)
- **Key Personnel:** Jack Elston (BST Subcontractor PI), M. Stachura (CTO), Beck Cotter (last editor)

---

## Executive Summary

Black Swift Technologies is subcontractor to University of Washington on a 3-year ONR 6.4 program developing an A-size tube-deployable small unmanned aircraft system (sUAS) to characterize weather, sea-surface temperature (SST), and atmospheric refractivity in the marine boundary layer for deployment from WC-130J host aircraft. BST will deliver 2–3 Hurricane-S0 aircraft per year with incrementally added capabilities: Year 1 focuses on VHF datalink and SST sensor integration; Year 2 adds radar-driven low-altitude flight control, wave-state estimation, two-way VHF, and real-time data pipeline to Navy operational models; Year 3 adds a GPS Airborne Radio Occultation (ARO) feasibility study and hurricane-season forward-operating-location deployment.

---

## Technical Approach

### Year 1: Hurricane-S0 + SST + VHF Datalink + C-130 Support Equipment

**Airborne Platform:**
- Two Hurricane-S0 aircraft in current LAU-126A-compatible A-size tube configuration
- Existing sensor stack: pressure, temperature, humidity, altitude, lat/lon/time, 3D winds, radar altimeter (wave heights), aircraft state (heading, speed, pitch, roll, yaw via IMU and dual-antenna GNSS)
- GNSS architecture (u-blox ZED-F9H + ZED-F9P, 40 cm baseline, Linx ANT-GNCP-C25L125100 antenna) unchanged for navigation and heading

**C-130J Support Equipment (ship-loose, non-flight-critical):**
- Operator interface: ruggedized laptop/tablet running BST ground-control software; displays aircraft state, meteorological observations, deployment status, quick-look mission summaries; supports multiple concurrent S0 aircraft
- Base station: VHF receiver, antenna feed, modem, decoder; captures S0 telemetry from 162.25–173.5 MHz, decodes and pipes structured data to operator interface; provides radio-link health metrics (RSSI, BER, packet rate)
- Both subsystems build on existing BST P-3 operator interface/base station deployed for NOAA hurricane operations

**SST Sensor (Best Effort):**
- Downward-looking compact IR pyrometer with narrow FOV in 8–14 µm atmospheric window
- Candidate: Melexis MLX90640 array (32×24, ~50 mm class, <5 g) or Heimann HTPA module
- Calibration against co-located in-situ buoy or Sanabia drop-thermistor reference
- Risk: airframe thermal reflections; scheduled 4-week integration with Month 3 go/no-go review; descope to Year 2 if calibration uncertainty exceeds ±0.5 K

**VHF Datalink (Downlink Only Year 1):**
- Radio: Doodle Labs Mesh Rider Helix-V (RM-2050-V series, 144–235 MHz) recommended; rationale: correct band for sonobuoy frequencies, shared Smart Radio software stack with existing BST integrations, IP-based mesh simplifies Year 2 GTS/RTDHS upload, comparable SWaP to P400 (~70 g, <5 W TX)
- Fallback: Microhard L-series VHF or custom ADRV9002-based SDR
- Channel programmability verification in 162.25–173.5 MHz green-coded sonobuoy band is Month 1 action

**VHF Antenna:**
- Replace current 32 cm PCB monopole (designed for 430 MHz) with 45 cm spring-steel whip with base-loading coil (~3–6 µH)
- Target frequency: 162.25–173.5 MHz (center 168 MHz)
- Expected performance: 70–85% radiation efficiency, 8–10 MHz 2:1 VSWR bandwidth, toroidal pattern with maximum gain at horizon
- Mechanical: extend existing flip-out hinge by 13 cm; spring qualification against tube-launch shock (450 g) and slipstream loads

**Link Budget Analysis (168 MHz vs. 430 MHz baseline):**
| Parameter | 430 MHz Baseline | 168 MHz Proposed | Delta |
|-----------|------------------|------------------|-------|
| FSPL at 400 km | 137.2 dB | 128.5 dB | −8.7 dB |
| TX antenna efficiency | 60–80% | 70–85% | ≈ 0 dB |
| Channel BW | 12.5 kHz | 12.5 kHz | 0 dB |
| Net link margin | baseline | — | +7 to +9 dB |

With 5 W TX, narrowband 12.5 kHz operation, and 45 cm base-loaded whip, VHF link should match or exceed ~400 km range at UHF.

**Spectrum Authorization (Long-Lead):**
- VHF 136–174 MHz is government-allocated (NTIA)
- DD Form 1494 filed in Month 1 of Year 1; lead time 4–9 months (single longest-pole schedule item)
- Coordination through 53rd WRS frequency manager and Navy Marine Corps Spectrum Office
- Year 1 authorization for downlink only (UAS→aircraft); Year 2 amendment for uplink initiated as soon as Y1 clears

**Deployment Profile:**
- Profiles from ~10,000 ft AGL down to as close to sea surface as possible (target ~10 m / 33 ft AGL)
- Primary scientific focus in lowest 500 m

**Operational Support:**
- BST representative travels for two separate 4-day trips to Keesler AFB, Biloxi, MS for integration, deployments, on-site data QA/QC
- Travel via Gulfport; lodging at Courtyard by Marriott, D'Iberville

### Year 2: Radar-Following, Wave-State, Two-Way VHF, Data Pipeline

**Hardware:**
- Two to three additional S0 aircraft; same airframe and sensor configuration as Year 1
- Hardware substantially unchanged from Y1

**Active Radar-Driven Low-Altitude Flight:**
- Tighten role of existing 50 Hz radar altimeter in flight-control loop for wave-following (rather than fixed-altitude hold above still-water surface)
- Control-law tuning, bench/hardware-in-the-loop verification, flight test in low-to-moderate sea state during Y2 Keesler campaign
- Goal: extend practical minimum altitude over sea by 30–50% in calm-to-moderate conditions

**Ocean-State Characterization (Wave Coefficients):**
- Using 50 Hz radar altimeter data, estimate significant wave height (Hs) and mean-squared slope (MSS) onboard via spectral-domain Extended Kalman Filter
- Models surface elevation η(s,t) as Fourier series with Gauss–Markov time updates on coefficients
- Target accuracies per SASCWATCH ONR program: Hs < 3%, MSS < 10%
- BST STTR Phase I analysis showed S0 radar noise under 50 cm sufficient to meet both targets
- Validation by intercomparison with NDBC buoys or EASI/ASIS reference buoys during Y2 deployments

**STTR In-Kind Contribution:**
- Kalman-filter algorithm, onboard real-time port, and high-rate compute architecture (STM32MP1-class heterogeneous SoC) developed under BST Navy STTR Phase II (Contract N6833525C0270, Topic N25A-T025, "Expendable Air-sea Profiling Observations in Hazardous Weather Conditions")
- UW ONR work funds marginal effort to tune filter for UW deployment profile, integrate Hs/MSS outputs into data products for Navy EM models and GTS pipelines, and execute validation campaigns

**Two-Way VHF (Uplink for Adaptive Sampling):**
- Year 1 VHF radio is bidirectional in hardware; Year 1 operates downlink only due to spectrum authorization timeline and pre-determined profile use
- Year 2: BST supports DD-1494 amendment for uplink authorization (53rd WRS frequency-manager coordination, Navy Marine Corps Spectrum Office paperwork)
- Once authorized, configure operator interface for in-flight profile commanding to support adaptive sampling
- Cost impact primarily consulting hours; no new flight hardware required

**GTS/RTDHS/Navy EM Data Pipeline:**
- In-flight: S0 streams meteorological observations over VHF link to WC-130J in real time (Y1 capability)
- On WC-130J: small gateway module (Linux SBC integrated with base station) decodes BST telemetry stream and transcodes to WMO BUFR/TAC format compliant with operational dropsonde data model (TEMP DROP, BUFR template TM 311001 family)
- Off-aircraft: BUFR message forwarded to GTS via operational Air Force/Navy gateway, to RTDHS via NOAA's standard ingest path, and to Navy-specific EM models
- Coordination through host wing's mission planning and UW's NOAA/Navy contacts (not BST-direct)

**Intercomparison:**
- Y2 flights scoped to occur over water near co-located "truth" sensor (moored buoy or co-deployed dropsonde)
- Y2 second trip targets Travis AFB for Atmospheric River mission (Biloxi as fallback if AR not supported)

### Year 3: ARO Feasibility Study + Continued Operational Flights

**ARO Feasibility Study Framing:**
- Based on Cao et al. (2025) Airborne Radio Occultation (ARO): passive limb-sounding technique observing setting/rising GNSS satellites occulted by atmospheric limb
- Receiver tracks excess Doppler/carrier phase as satellite sets behind atmosphere; bending angle inverted via Abel transform to refractivity vs. altitude
- Scripps G-IV system: Septentrio receiver, AeroAntenna multi-GNSS antenna, 1 Hz multi-frequency carrier phase, post-flight PPP-AR + ROPP processing
- **Clarification:** ARO is NOT GNSS-Reflectometry; uses direct-path signals from low-elevation satellites (no LHCP nadir antenna, no DDM, no surface scattering); fundamentally passive using standard geodetic-class GNSS hardware
- Scripps G-IV operates at 13–14 km; S0 ceiling ~15,000 ft (~4.6 km); ARO from 4.6 km vertically samples lower 3–4 km of troposphere—exactly the marine-boundary-layer / refractivity-survey volume of greatest interest (primary focus lowest 500 m)
- Y3 deliverable: feasibility demonstration with hardware-integration milestones, raw observable collection on recoverable aircraft, post-flight processing-pipeline development, and initial intercomparison of ARO-derived refractivity against Y1/Y2 derived-refractivity profiles

**Receiver Selection: Septentrio mosaic-X5 OEM Module**
- Dimensions: 31 × 31 × 4 mm; mass: 6.8 g; power: 0.6 W typical / 1.1 W max
- Multi-constellation multi-frequency: GPS L1/L2/L5, Galileo E1/E5a/E5b/E6, GLONASS L1/L2,