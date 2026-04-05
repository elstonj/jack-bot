# Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System — CLIN 002 Progress Report

## Document Metadata
- **Type:** SBIR/STTR Phase I Progress Report
- **Client/Agency:** Department of the Navy / NAVAIR
- **Program/Solicitation:** BAA topic N25A-T025 (SBIR/STTR); Proposal N25A-T025-0009
- **Contract Number:** N6833525C0270
- **Date:** Report period July 7 – October 6, 2025 (submitted October 6, 2025)
- **Classification:** Unclassified; CUI; Distribution Statement B
- **BST Products/Systems Referenced:** S0 (air-deployed and VTOL variants), S2, MultiHole Pressure Probe (MHPP)
- **Key Personnel:** Dr. Jack Elston (Principal Investigator), Maciej Stachura (last editor), Joshua Cossuth (DON TPOC)
- **BST Address:** 2840 Wilderness Place Suite D, Boulder, CO 80301-5414

---

## Executive Summary

This Phase I progress report documents BST's work on refining the S0 small uncrewed aircraft system (sUAS) for Navy-specific atmospheric profiling in hazardous weather, particularly tropical cyclones. Through Tasks B1 and B2 (completed in the first reporting period), BST conducted a comprehensive review of existing profiling platforms, performed error analysis on S0 sensors, and validated S0 measurements against dropsondes, tail Doppler radar, and tower data. The S0 demonstrated significant advantages in spatial coverage, data density, turbulence measurement capability, and cost-effectiveness compared to traditional dropsondes, while also being upgraded with dual-GPS heading, radar altimeter, extended battery, and improved communications for 2025 operations.

---

## Technical Approach

### Overall Program Objectives
1. **Quantify enhanced observation capabilities** by comparing S0 performance to existing platforms (dropsondes, Tail Doppler Radar, radiosondes) and addressing the need for improved expendable in-situ profiling in challenging air-sea environments.
2. **Assess and improve S0 measurement accuracy** through calibration, validation, and error analysis, including extending operational capabilities to icing conditions.
3. **Produce new and unique observations** such as vertical wind, turbulence, and wave properties, and develop onboard algorithms to capture these data.
4. **Automatically target areas of interest** at the air-sea/ice interface using the S0's onboard computing and software APIs for adaptive sampling strategies.

### Task B1: Background Review and Comparative Analysis
- Reviewed existing atmospheric profiling platforms (Vaisala dropsonde, Skyfora Streamsonde, Tail Doppler Radar, prior-generation UAS: Aerosonde, Raytheon Coyote, Anduril Altius-600)
- Conducted detailed comparative analysis focusing on cost, data accuracy, spatial/temporal coverage, and longevity
- Analyzed results from prior S0 missions to identify strengths and improvement areas
- Compared S0 to primary Navy profiling platform (dropsonde) across multiple dimensions

### Task B2: S0 Data Analysis and Enhancements
- Performed detailed error analysis of S0 measurements (pressure, temperature, humidity, 3D winds, vertical winds, turbulence)
- Developed test plan and experiments to validate measurement accuracy and repeatability in Phase II
- Analyzed error sources in wind estimation (scale factor error, yaw/heading angle error)
- Planned icing mitigation strategies and phase-2 validation experiments
- Analyzed integration pathways with Navy systems (CLT deployment tube, P-3 external launches)
- Addressed severe weather protection (precipitation sealing, icing coatings)

---

## Products & Capabilities Described

### S0 (Small Uncrewed Aircraft System)

**Description:**
- 3-pound air-deployed fixed-wing UAS with proven capability for tropical cyclone sampling
- Also available as S0-VTOL (vertical takeoff/landing variant) for ship/shore deployment
- Expendable platform designed to be recovered via parachute
- Can carry full meteorological sensor package and multi-hole pressure probe

**Sensor Package (Standard):**
- **Thermodynamics:** Vaisala RSS421 package (pressure, temperature, relative humidity) — same sensors as Vaisala dropsondes
- **Wind Measurement:** Multi-hole pressure probe (MHPP) manufactured by BST, capable of 100 Hz sampling; current uplink limited to ~3.5 Hz
- **Sea Surface Temperature:** Downward-pointing infrared sensor
- **Altitude:** Radar altimeter (NEW in 2025) for accurate height over water; activated below 50 m
- **Heading:** Dual-GPS system (NEW in 2025) for improved yaw accuracy (0.5° vs. 3° with prior magnetometer)

**Operational Characteristics:**
- **Endurance:** 2+ hours in tropical cyclone conditions (2025 upgrade; 105 minutes in 2024)
- **Longest 2025 mission:** 111 minutes (Tropical Storm Imelda)
- **Communications range:** 210 nmi in clear air at 1,500 m altitude; 160 nmi in Tropical Storm Imelda at 150 m altitude
- **Flight capability:** Can target specific regions away from flight track, unlike dropsondes
- **Maximum wind survivability:** Proven in up to 210 kt winds (Category 5 hurricanes)

**2025 Upgrades and Improvements:**

*Data Product Improvements:*
- Dual-GPS heading system (improved wind accuracy from 1.5 m/s to 0.3 m/s or better)
- Onboard turbulence algorithms with increased processing capability
- Radar for sea surface (enables radar-guided flights down to 10 m; wave height measurements)

*Avionics Updates:*
- Firmware supporting dual-GPS operation
- 10 Hz MET data streaming
- Improved communications antenna (impedance-matched) for extended range
- Updated power control board for 6S battery support

*Ground Station / UI Updates:*
- AirOps interface additions: radar altitude, time since last comms, comms quality
- Onboard NetCDF data generation
- Real-time sUAS data viewing on P-3 workstations via web browser

*System Hardware Updates:*
- Battery upgrade: 108 Wh → 130 Wh (expected >20% endurance improvement)
- Simplified propulsion system (combined ESC, motor, cooling)
- ~25% increased top-end power output for severe downdraft handling
- Improved internal wing structure (stiffer, lighter)
- Manufacturing improvements (>50% reduction in final assembly time)
- NDAA-compliant electronics sourcing

**Measurement Performance Targets (Table B2.1):**

| Parameter | Target Value | Phase 2 Validation |
|-----------|--------------|-------------------|
| Static Pressure | ±1 hPa uncertainty; 0.01 s response | Compare vs. dropsondes, tower data, wind tunnel |
| Relative Humidity | ±4% uncertainty; 0.3–10 s response | Compare vs. dropsondes, tower, NCAR chamber |
| Air Temperature | ±0.3°C uncertainty; 0.5 s response | Compare vs. dropsondes, tower, chamber |
| 3D Winds | ±0.3 m/s uncertainty; 10 Hz (100 Hz onboard) | Compare vs. dropsondes, TDR, tower (100+ flights target) |
| Sea Surface Temperature | ±0.3°C | Compare vs. sonobuoys, floating platforms (SASCWATCH) |
| Significant Wave Height | <1 m (best case 0.2 m) | Compare vs. SASCWATCH, shore-based missions |
| Mean Squared Slope | 10% | Same as wave height |

### Multi-Hole Pressure Probe (MHPP)

**Unique Capability:**
- Only waterproof 5-hole pressure probe currently integrated on small UAS with sufficient size/weight/power (SWAP) budget
- Capable of 100 Hz wind measurement
- Enables turbulence-quality wind estimates and exchange coefficient calculations (drag, heat, moisture)

**Applications:**
- Calculating drag coefficient (C_D), momentum flux, turbulent kinetic energy
- Calculating heat exchange coefficient (C_H) and moisture exchange coefficient (C_E)
- Critical for hurricane intensity forecasting models
- Unique among current operational TC reconnaissance platforms

**Turbulence Measurements (Demonstrated):**
- Deloach et al. (2025) demonstrated calculation of momentum flux, latent/sensible heat fluxes at ~10 m altitude using 3.5 Hz data
- Derived exchange coefficients (C_D, C_H, C_E) — previously unobtainable in operational hurricane sampling
- Clear Air tests (2024) and Tropical Storm Imelda (2025) showed 4× increase in turbulence intensity between 100 m and 50 m altitude

---

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Sampling
- **Aircraft platforms:** NOAA P-3 Orion, USAF C-130J Hercules
- **Deployment:** Air-deployed from crewed reconnaissance aircraft at 2,000 m AGL
- **Operational history:** 19 launches in 2024 (Hurricanes Ernesto, Francine, Helene, Milton); initial 2025 operations in Tropical Storms Erin, Gabrielle, Imelda
- **Data applications:** 
  - High-resolution thermodynamic profiles in storm core
  - Turbulence characterization near air-sea interface
  - Exchange coefficient measurement for model validation
  - Real-time situational awareness for flight crews

### Secondary/Future Missions:
1. **USAF Applications:** Wind measurement ahead of C-130 dropzone operations
2. **Ship/Shore Deployment:** VTOL variant for Naval or Coast Guard platforms
3. **Research Campaigns:** ISARRA (International Society of Atmospheric Research using Aircraft) validation flights; SASCWATCH (ONR MURI) wave/flux studies
4. **Adaptive Sampling:** Automated targeting of areas of interest using onboard computing and API integration

---

## Key Results (Task B1 & B2 Findings)

### B1.1: Comparative Analysis — Existing Systems

**Vaisala Dropsonde (Current Standard):**
- Deployed from P-3/C-130 since late 1990s
- Single vertical profile: 2–5 min duration at ~10 m/s descent rate
- Wind data @ 4 Hz; thermodynamic @ 2 Hz
- Limitations: Cannot target specific regions; transported by wind; sensor lag/aliasing issues in ASPEN post-processing

**Skyfora Streamsonde (Emerging Alternative):**
- Up to 50 simultaneous deployments (vs. 8 for dropsonde)
- ~50% slower descent rate (double the data per profile)
- Similar sensor specs to Vaisala

**Tail Doppler Radar (P-3 TDR):**
- Coverage: ~50 km radius with 2 km horizontal / 0.5 km vertical resolution
- Can achieve 0.15 km vertical resolution in profile mode
- Vertical wind error: <1 m/s RMSE; horizontal: <2 m/s RMSE
- Advantage: Large vertical extent (0.5–18 km)
- Limitation: Constrained by P-3 flight pattern; provides kinematic data only

**Raytheon Coyote (Prior-Generation sUAS, 2014–2018):**
- ~100× more thermodynamic observations than TDR
- Similar kinematic data to TDR in boundary layer
- No longer manufactured

**Anduril Altius-600 (Current sUAS Alternative):**
- ~25 pounds; theoretical max duration 240 min (demonstrated 102 min in Hurricane Ian 2022)
- Similar sensor package to S0 (Vaisala RSS421, MHPP capable)
- Range: 130 nmi (Hurricane Ian)

**BST S0 (Current Best-in-Class):**
- 3 pounds; 2+ hours endurance (2025 upgrade)
- 210 nmi range (clear air); 160 nmi in Tropical Storm I