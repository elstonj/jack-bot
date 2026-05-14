# BST ONR 6.4 Proposal Response – Wx/SST/ARO sUAS for WC-130J Tube Deployment

## Document Metadata
- **Type:** Proposal response (internal draft for review)
- **Client/Agency:** University of Washington (prime); Office of Naval Research (ONR) 6.4 program
- **Program/Solicitation:** ONR 6.4 (Advanced Component Development & Prototypes); subcontract to UW PI Dr. Elizabeth Sanabia
- **Date:** 12–13 May 2026 (draft, revised from 4 May version)
- **BST Products/Systems Referenced:** S0 (Hurricane-S0 sUAS platform), LAU-126A A-size tube deployment system
- **Key Personnel:** Jack Elston (document owner), Beck Cotter, Daniel Prendergast, Maciej Stachura (reviewers); Dr. Elizabeth Sanabia (UW PI)

---

## Executive Summary

Black Swift Technologies is subcontractor to University of Washington for a 3-year ONR 6.4 program to develop and deploy an A-size tube-deployable sUAS (Hurricane-S0 platform) that measures weather (pressure, temperature, humidity, altitude, position), sea-surface temperature (SST), and atmospheric refractivity in the marine boundary layer. The system will be launched from WC-130J aircraft operating in the Gulf of Mexico from Keesler AFB, Biloxi, MS, with deliverables of 3 sUAS per year. Three key capabilities are introduced incrementally: Year 1 adds a VHF datalink and optional SST sensor; Year 2 adds a real-time data pipeline to ingest observations into the Global Telecommunications System (GTS) and Real-Time Data Hub System (RTDHS); Year 3 integrates a GPS Airborne Radio Occultation (ARO) payload for passive limb-sounding of atmospheric refractivity profiles. The program is well-aligned with the existing Hurricane-S0 platform, with technical risks concentrated in spectrum certification and RF antenna/receiver integration.

---

## Technical Approach

### Year 1: Hurricane-S0 + SST + VHF Datalink

**Aircraft baseline & sensors:**
- Existing Hurricane-S0 in LAU-126A-compatible A-size tube configuration unchanged
- Current sensors (P, T, q, altitude, lat/lon/time) retained
- Existing u-blox ZED-F9H + ZED-F9P GNSS (40 cm baseline) for navigation and heading; Linx ANT-GNCP-C25L125100 GPS antenna unchanged
- Pre-determined descent profiles from ~10,000 ft AGL to ~100 ft AGL; primary science focus in lowest 500 m

**VHF datalink (primary Year 1 innovation):**
- **Radio selection:** Doodle Labs Mesh Rider Helix-V (RM-2050-V series, 144–235 MHz)
  - Rationale: operates in sonobuoy band (162.25–173.5 MHz), same firmware/software stack as current P400, IP-based mesh supports Year 2 GTS/RTDHS pipeline, comparable SWaP (~70 g, <5 W TX)
  - Fallback options: Microhard L-series VHF or custom ADRV9002-based SDR
  - Critical action: Month 1 procurement of evaluation pair; confirm channel programmability at green-list sonobuoy frequencies via manufacturer before hardware build
  - Operating constraint: lock to narrowband (12.5 or 25 kHz) to maintain 7–9 dB link margin vs. UHF baseline

- **VHF antenna design:** 
  - Replace existing 32 cm PCB monopole (designed for 430 MHz UHF; only 0.18 λ at 168 MHz) with 45 cm spring-steel whip with base-loading coil (~3–6 µH)
  - Target: 162.25–173.5 MHz, centered at 168 MHz
  - Expected: 70–85% radiation efficiency, 8–10 MHz 2:1 VSWR bandwidth, toroidal pattern with maximum gain at horizon
  - Mechanical: extend existing flip-out hinge by 13 cm; tube-launch shock qualification (450 g) and slipstream-load testing required
  - Optional full-band agility (136–174 MHz) via PIN-diode or RF MEMS tunable matching network deferred to later phase
  
- **Link budget improvement:**
  - 168 MHz vs. 430 MHz baseline: 8.7 dB structural advantage in free-space path loss (FSPL 400 km: 128.5 dB vs. 137.2 dB)
  - Net link margin gain: +7 to +9 dB at 5 W TX, narrowband 12.5 kHz, 45 cm base-loaded whip
  - Expected range: ≥400 km (matches existing UHF link)

- **Spectrum certification (DD Form 1494):**
  - VHF (136–174 MHz) requires government spectrum coordination through Navy Marine Corps Spectrum Office and host wing frequency manager
  - Lead time: 4–9 months; **critical path item—must initiate Month 1 of Year 1, not Month 6**
  - File in parallel with hardware development

**SST sensor (best-effort Year 1 scope):**
- Candidate: compact IR pyrometer (8–14 µm atmospheric window), downward-looking
  - Options: Melexis MLX90640 (32×24 array, ~50 mm, <5 g) or Heimann HTPA module
  - Calibration target: ±0.5 K accuracy against co-located buoy or drop-thermistor reference
  - Risk: motor and cowling thermal reflections; requires flight-mounted ground test
  - Schedule: 4-week integration task with Month 3 go/no-go review
  - **Authorized descope to Year 2 if calibration uncertainty exceeds ±0.5 K**

**Mission operations:**
- BST representative travels to Keesler AFB, Biloxi, MS for Year 1 deployment
- Lodging at Courtyard by Marriott, D'Iberville, per standard
- Estimate 1 BST FTE on-site for deployment duration plus pre-deployment integration support
- Quote includes flight, lodging, per diem, rental car

### Year 2: GTS/RTDHS Real-Time Data Pipeline

**Hardware:** 3 additional sUAS units, identical Year 1 configuration (plus approved fixes)

**Software pipeline:**
- **In-flight:** S0 streams meteorological observations over VHF link to WC-130J in real time (from Year 1)
- **Onboard WC-130J:** small Linux gateway module decodes BST telemetry and transcodes to WMO BUFR/TAC format compliant with operational dropsonde data model (TEMP DROP, BUFR template TM 311001 family)
- **Off-aircraft:** BUFR message forwarded to GTS and RTDHS via existing operational Air Force/Navy gateway; coordination handled by prime (UW)

**BST scope:**
- Develop and ground-test BUFR encoder
- Run captive-carry data-pipeline rehearsal at Keesler in advance of operational flights
- Provide gateway SBC hardware
- Deployment with co-located reference sensor (moored buoy or co-deployed dropsonde) for intercomparison over water (not in hurricane)

### Year 3: GPS Airborne Radio Occultation (ARO) Integration

**ARO technique (per Cao et al. 2025):**
- Passive limb-sounding using setting and rising GNSS satellites occulted by the atmospheric limb
- Receiver tracks excess Doppler/carrier phase as satellite sets; bending angle inverted via Abel transform to refractivity vs. altitude
- NOT GNSS-reflectometry (no nadir antenna, no DDM, no surface scattering)—uses direct-path low-elevation signals and standard geodetic-class GNSS hardware
- Scripps G-IV reference: Septentrio PolaRx5/AsteRx receiver, AeroAntenna multi-GNSS antenna, 1 Hz multi-frequency carrier phase, post-flight PPP-AR + ROPP processing

**Altitude limitation as a feature:**
- Scripps G-IV operates at 13–14 km; S0 ceiling ~4.6 km (~15,000 ft)
- ARO from 4.6 km vertically samples only lowest 3–4 km of troposphere—exactly the marine boundary layer / lowest 500 m focus zone for this program
- Year 3 deliverable: feasibility demonstration and intercomparison with Year 1/2 derived-refractivity profiles, not global-scale ARO product

**ARO receiver selection: Septentrio mosaic-X5 OEM module**
- Size: 31 × 31 × 4 mm (≈4× larger footprint than ZED-F9H but fits easily on small carrier PCB)
- Mass: 6.8 g (vs. ~1 g for F9H)
- Power: 0.6 W typical / 1.1 W max (vs. ~0.4 W for F9H)
- Signals: multi-constellation, multi-frequency (GPS L1/L2/L5, Galileo E1/E5a/E5b/E6, GLONASS L1/L2, BeiDou B1/B2/B3, QZSS, NavIC)
- Output: SBF (Septentrio Binary Format) or RINEX, 1–100 Hz, with carrier phase, pseudorange, Doppler, SNR, lock-time
- Interface: serial/USB
- Net SWaP impact: ~+6 g, +0.5 W, +0.5 cm height vs. existing F9H—easily absorbed in existing payload margin

**ARO antenna selection: Tallysman TW7972 (primary recommendation)**
- Replaces existing Linx ANT-GNCP-C25L125100 (GPS L1 only, unsuitable for low-elevation satellites)
- Tallysman TW7972: dual-feed, broadband-LNA variant of TW3972
  - Size: Ø75 × 22 mm
  - Mass: ~50 g
  - Bands: L1/L2/L5 + E5b
  - Cost: ~$300–500
  - Good phase-center stability, integrated LNA, low cost
- Alternative candidates: Antcom G5Ant-2AT1 (premium phase stability, ~$1500, lighter); AeroAntenna AT1675-180-TS (used by Scripps, too heavy/large for S0)
- Mounting: top fuselage forward of wing, clear horizon-to-zenith visibility port and starboard for tracking setting/rising satellites
- **Important:** Existing Linx antenna REMAINS in place for navigation/heading; mosaic-X5 is INDEPENDENT ARO system with new Tallysman—no disruption to nav stack

**RF coexistence & integration:**
- Tallysman antenna physically separated from VHF whip and F9 antennas to avoid desense
- Plan antenna layout in Month 1 of Year 3 (or in parallel with Year 1 VHF work)
- Bench-test receiver desense vs. VHF duty cycle; apply frequency-selective filtering if needed

**Onboard processing:**
- No real-time processing required onboard
- Mosaic-X5 logs SBF/RINEX over serial/USB; all bending-angle inversion and refractivity retrieval done post-flight on ground
- Data rate: 30–50 MB/hr at 1 Hz multi-GNSS; ~50–100 MB for typical 1–2 hour sorties (trivial to store on existing autopilot SD card)
- If existing autopilot SBC has unused USB port and spare write bandwidth, no additional processor needed; otherwise add Raspberry Pi Zero 2 W (~10 g, 1.5 W) or Variscite DART-MX8M-Mini SoM (~15 g, 2 W) as dedicated logger
- Recommended baseline: log at