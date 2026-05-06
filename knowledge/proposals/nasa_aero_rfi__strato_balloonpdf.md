# NASA Aero RFI - Strato Balloon

## Document Metadata
- **Type:** RFI Response (Request for Information)
- **Client/Agency:** NASA ARMD (Aeronautics Research Mission Directorate)
- **Program/Solicitation:** NASA Aeronautics Flight Accelerator (AFA) RFI; Notice ID 80AFRC26SS013
- **Date:** 2026-05-04 (submission date; meetings referenced February–May 2025)
- **BST Products/Systems Referenced:** S0 (air-deployed UAS), S2 (fixed-wing), S2 VTOL, E2 (multirotor), SwiftCore FMS, MultiScat sensor suite
- **Key Personnel:** Dr. Jack Elston (CEO, Technical POC); Beck Cotter (Administrative POC); mentioned collaborators: Matthew Fladeland (NASA Ames), David North and Steven Geuther (NASA Langley), Joe Cione (NOAA HRD), Mark Bullock (Science and Technology Corporation, subcontractor on Venus Phase I)

---

## Executive Summary

Black Swift Technologies proposes maturing a stratospheric hybrid observing architecture in which a high-altitude, long-endurance (HALE) Aerostar Thunderhead-class balloon serves as a mothership for a vertically-arrayed, heated launch cradle that pneumatically deploys one or more S0 air-deployed UAS to sample the lower atmosphere (down to 10 m AGL). The system combines a balloon's days-to-weeks persistence with expendable sub-$20K airframes capable of descending below weather and smoke opacity—closing the "surface-to-near-space" observational gap. Three flight-test spirals from FY26–FY28 will mature the heated cradle, cold-start thermal management, and balloon-side dispenser from TRL 3–4 to TRL 7.

---

## Technical Approach

### System Architecture
- **Balloon Carrier:** Aerostar Thunderhead-class HALE balloon, float altitudes 60,000–100,000 ft, days-to-weeks endurance, 200 W+ continuous gondola power, 500 lb payload capacity, steerable for station-keeping over targets
- **Deployment Vehicle:** S0 air-deployed UAS (1.2 kg, 91.4 cm wingspan, flight-validated in four 2024 hurricanes including Category 5 Hurricane Milton)
- **Launch System:** Vertically-arrayed, heated launch cradle with pneumatic (cold-gas) ejection mechanism—balloon-safe design avoiding pyrotechnic damage
- **FMS:** SwiftCore Flight Management System with deterministic-fallback architecture; NDAA-compliant, U.S.-domestic, ASDA-compliant
- **Payload Integration:** Machine-vision camera (LUCID Phoenix 6.3 MP at 100 Hz for plume/fire-edge tracking); multi-hole probe (3D winds, temperature, humidity, pressure at 100 Hz); magnetometer and water-vapor sensor (optional per Ames request)
- **Communications:** S0-to-gondola RF link (125 nm range, Microhard P401); gondola-to-ground via Iridium/Starlink satellite backhaul (<5 min latency)

### Three-Spiral Flight Test Plan
1. **Spiral 1 (FY26 Q4–FY27 Q2):** Low-cost meteorological-balloon drop test (<25 kft) validating release dynamics and cold-start protocol over unpopulated test range (Longmont, CO or NASA-coordinated site)
2. **Spiral 2 (FY27):** 45-kft FireSense-aligned demonstration with multi-S0 release and machine-vision plume tracking over controlled burn
3. **Spiral 3 (FY28):** 60-kft+ release into high-shear environment (hurricane outflow or active wildfire convection) with end-to-end satellite backhaul to NASA Ames and/or NOAA HRD

---

## Products & Capabilities Described

### S0 Air-Deployed UAS
- **What it is:** Flight-validated, expendable 1.2 kg tube-launched airframe; 91.4 cm wingspan; 22.5 m/s cruise speed; 120-min endurance (heritage) improving to 100+ min with optimized cold-start profile
- **Heritage:** Deployed from NOAA WP-3D Hurricane Hunters into four major 2024 storms (Ernesto, Helene, Milton, Francine); survived Category 5 phase of Hurricane Milton; 268-mission WP-3D heritage; 23 documented S0 deployments in 2025 hurricane season
- **Performance specs:**
  - Max wind tolerance: 257.5 km/h
  - Minimum altitude: 10 m AGL/ASL
  - Maximum powered ceiling: 15 kft on single battery
  - RF range to platform: 125 nm
  - Glide-to-powered-cruise transition: <5 s from P-3 drop tube (target ≤10 s from 60 kft balloon)
- **Proposed use:** On-demand release from balloon gondola for descending profiles through low atmosphere where satellites cannot penetrate (smoke, rain, volcanic plume)

### SwiftCore FMS
- **What it is:** Deterministic-fallback flight management substrate; production autopilot; NDAA-compliant, U.S.-domestic, ASDA-compliant supply chain
- **Use in this effort:** Provides autonomous flight control, release orchestration, and GPS-denied descent capability (via vision-aided inertial navigation from prior NOAA Phase II work)
- **Deployed on:** All BST platforms (S0, S2, S2 VTOL, E2)

### Heated Cradle & Dispenser (New Flight Articles)
- **What it is:** Vertically-arrayed multi-tube launch cradle with integrated thermal management (heater) to maintain S0 batteries and avionics ≥0°C through 48-hour stratospheric pre-launch loiter at –60°C ambient; pneumatic ejection mechanism (cold-gas, balloon-safe)
- **Current TRL:** 3–4 (paper architecture, lab bench thermal models, 2020 Venus Phase I concept work)
- **Target TRL by FY28:** 7 (flight-relevant for FireSense and operational deployment)
- **Design constraints:** Part 101 frangibility compliance; no thermal or pressure-wave damage to balloon envelope; supports coordinated release of ≥4 S0 from single gondola
- **NASA role:** Langley to lead or co-engineer gondola-side dispenser interface; Glenn IRT exposure of thermal envelope; Langley test cells for cold-gas ejection validation

### Aerostar Thunderhead HALE Balloon
- **Role:** Mothership for cradle and S0 deployment
- **Specs (commercial partner–provided):** 60,000–100,000 ft float altitude; days-to-weeks endurance; 200 W+ continuous gondola power; 500 lb payload capacity; steerable for station-keeping
- **Ground operations:** Aerostar (Sioux Falls, SD / Rapid City, ND) or NASA-supported launch range

---

## Use Cases & Applications

### Primary (NASA/Federal)
1. **Wildfire Monitoring (FireSense Program, NASA Ames)**
   - Real-time in-situ plume data assimilation into WRF-SFIRE for active-fire wind-field mapping
   - Convective-column atmospheric chemistry sampling (permitted because asset is expendable, mitigating flight-safety constraints on recoverable platforms)
   - Pyrocumulus and lower-stratosphere sampling (DCOTS mission analog)

2. **Hurricane Research (NOAA HRD)**
   - Boundary-layer inflow/outflow sampling beneath tropical cyclones
   - Intensity-prediction improvement via in-situ data (Cione et al. 2016, 2020 precedent)
   - Spiral 3 integration with hurricane outflow release at 60+ kft

3. **Volcanic Monitoring (USGS Volcano Disaster Assistance Program)**
   - Plume monitoring and composition sampling
   - Building on BST S2 heritage: 25-km BVLOS volcanic-vent sampling at Makushin (Aleutian Islands) with SO₂/CO₂ payloads

4. **NASA Earth Science Campaigns**
   - DCOTS (Dynamics and Chemistry of the Upper Troposphere and Stratosphere)
   - ESTO (Earth Science Technology Office) sensor integration and validation

### Secondary (Commercial & Defense)
- **U.S. Forest Service / CAL FIRE:** Wildfire detection and response coordination
- **Oil-and-Gas Infrastructure:** Utility-scale pipeline observation; methane mapping
- **Maritime Surveillance:** Traffic surveillance over remote oceanic regions
- **DoD Dual-Use (Replicator-class ISR):** Persistent ISR over contested/denied airspace; Arctic perimeter monitoring; GPS-denied air-deployed sensor delivery

---

## Key Results (Heritage & Projections)

### Existing S0 Flight Heritage
- **Hurricane Operations:** 4 major 2024 storms; 268-mission WP-3D career total; 23 documented deployments in 2025 season; survived Category 5 Hurricane Milton
- **Extreme Environment Validation:** No competing sub-$20K expendable airframe has equivalent hurricane-grade flight pedigree
- **Other Field Campaigns:** VORTEX2 tornadic supercell interception (first UAS); Greenland Arctic profiling to 14 kft; Costa Rican rainforest soil-moisture mapping; August 2025 NASA-NSSC 24-hour wildfire airspace-persistence demo (Sunny Slope Sod Farm, Longmont, CO)

### Key Performance Targets (Table 1 & 2 Summary)
| KPP | Current | FY28 Target |
|-----|---------|-------------|
| Pneumatic ejection success & controlled flight | Validated from NOAA P-3 (15 kft) in 4 hurricanes | 100% from balloon at 60+ kft |
| S0 battery/avionics temp during pre-launch | Lab benchtop (≥0°C) | ≥0°C through 48 hr at –60°C ambient |
| 3D wind vector accuracy | ±0.5 m/s | ±0.2 m/s in high-shear regimes |
| Release-to-powered-cruise time | <5 s from P-3 | ≤10 s from 60 kft |
| Multi-aircraft release per mission | 1 | ≥4 |
| End-to-end RF backhaul | 125 nm S0–platform direct | Iridium/Starlink, <5 min latency |
| Integrated stack TRL | 4–6 (Venus Phase I) | 7 (FireSense flight-relevant) |
| Airworthiness coverage | AFRC AWS (S2); FAA COAs (S0) | AWS extension to balloon-deployed S0; Part 108 compliance |

---

## Notable Details

### Revolutionary Thesis
The proposal frames the persistent observation gap as a **deployment-economics problem**, not a sensor problem:
- Radiosondes: one-shot vertical profile, no retasking
- Satellites: blocked by smoke, rain, volcanic plumes (4–9 km resolution)
- Crewed Hurricane Hunters/Global Hawk HALE UAS: persistence-limited or financially prohibitive at scale
- **BST solution:** Stratospheric balloon ($M investment, days-to-weeks duration) hosting sub-$20K expendable airframes (releasable on demand) compresses cost-per-in-situ-data-point by **1–2 orders of magnitude** vs. crewed flight; enables ~10 flight tests for cost of 1 crewed mission

### Market & Competitive Differentiation
- **Market Size:** Global environmental-sensing/atmospheric-monitoring market exceeds $13.2B annually; wildfire detection/monitoring alone $2.72B (2024) with 10.4% CAGR
- **BST Addressable Opportunity (FY26–FY30):** $4–7M annually (federal purpose-built balloon-deployed atmospheric-profiling drones), with commercial tailwind from utility-scale wildfire and oil-and-gas monitoring; dual-