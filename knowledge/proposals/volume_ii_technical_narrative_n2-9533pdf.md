# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System

## Document Metadata
- **Type:** Phase II STTR Technical Proposal (Volume II Technical Narrative)
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR N25A-T025; Topic N2-9533
- **Date:** 2026-02-25
- **BST Products/Systems Referenced:** S0 UAS (air-deployable, expendable), S0-VTOL (shipboard, reusable), S0-LR (long-range, land-based, reusable)
- **Key Personnel:** Jack Elston (Principal Investigator), Maciej Stachura, Jun Zhang, Joshua Wadler, John Park
- **Partner Organizations:** Embry-Riddle Aeronautical University (ERAU), University of Miami (UM), Old Dominion University (ODU)

## Executive Summary

Black Swift Technologies proposes Phase II STTR to transition the S0 unmanned aircraft system from a NOAA-operational research platform into a Navy-adoptable atmospheric profiling capability for hazardous maritime weather. Building on Phase I validation demonstrating comparable or superior performance to dropsondes at ~10x lower cost per profile and orders-of-magnitude improvements in data density, Phase II focuses on: (1) completing sensor calibration and response characterization in ocean environments, (2) transitioning the system to turnkey operational status, (3) advancing turbulence and wave-state algorithms to real-time onboard execution, (4) demonstrating forecast improvements in Navy models, (5) enabling cold-weather/Arctic operations, (6) implementing autonomous adaptive sampling using AI, and (7) integration with Navy/Air Force launch platforms (P-8, C-130, MH-60).

## Technical Approach

### Core Mission & Strategic Justification

**Operational Gap Addressed:**
- Tropical cyclone and severe maritime storm forecasting severely constrained by sparse in-situ observations over oceans, especially in marine boundary layer where air-sea momentum, heat, and moisture exchange governs storm intensity and structure evolution
- Existing systems (dropsondes, satellites) limited by: episodic sampling (dropsonde profiles last 2-10 minutes), high cost ($1,000/dropsonde), poor boundary-layer coverage, limited spatial/temporal resolution
- Vertically-resolved in-situ profiles produce disproportionately large forecast error reductions per observation compared to satellite radiances, especially in oceanic/TC environments (Cardinali 2009; Aberson 2010; Ditchek et al. 2023)
- Satellite limitations: infrared radiances attenuated by clouds; microwave degraded by heavy precipitation; indirect measurements requiring forward operators, bias correction, cloud screening; weak sensitivity to lowest atmospheric layers

**S0 Advantages Over Dropsondes:**
- **Duration:** 2 hours continuous data vs. 2-10 minute dropsonde profiles
- **Observation density:** 2024 S0 flights collected ~6,300 observations per flight (3.5 Hz baseline); 2025 capability ~25,200 observations per flight (3.5 Hz); upgradeable to 100 Hz onboard for 75,600+ observations
- **Cost efficiency:** At $15,000/unit and 25,200 observations per flight, S0 provides:
  - 283x more observations per dollar at 500m and below vs. $1,000 dropsondes
  - 1,391x more observations per dollar below 100m
  - Equivalent cost per full-flight observations: $15K S0 vs. $76K in dropsondes
  - 162x better value for observations under 500m
  - 795x better value for observations under 100m
- **Coverage:** Superior inner-core sampling (r<100 km); sustained eyewall wind measurements (maximum 1-minute sustained wind estimates vs. instantaneous dropsonde readings)
- **Data quality:** Can resolve turbulence, coherent structures, air–sea exchange processes not captured by ballistic sondes; samples wind distribution over extended time vs. single point measurement

**Air-Deployable Design Selection:**
- Leverages existing Navy/Air Force aircraft (P-8, C-130, MH-60) for rapid, distant deployment
- Simplified logistics vs. S0-VTOL (no dedicated shipboard launch/recovery crews) and S0-LR (slow flight time ~8-12 hour endurance)
- Complements rather than replaces reusable variants for specific operational contexts
- Enables rapid deployment at great distances from fleet

### System Architecture & Capabilities

**Flight Profiles & Endurance:**
- Stepped-descent profiling: loitering ~10 minutes at prescribed altitudes (demonstrated 2024-2025)
- Spiral ascent/descent profiles: ~4 m/s ascent, ~6 m/s descent rates
- 2-hour endurance demonstrated (2025), with credible path for extension via propulsion/energy improvements
- Ascent rates: approximately 4 m/s
- Descent rates: approximately 6 m/s

**Data Rates & Transmission:**
- Baseline: 3.5 Hz (2024); upgradeable to 100 Hz raw onboard
- Onboard processing transmits reduced products to manage telemetry bandwidth
- Demonstrated robustness: drag coefficient calculation consistent across 100 Hz, 10 Hz, and 1 Hz downsampled data (0.15–0.36% differences), enabling 1 Hz telemetry without meaningful loss
- High-frequency data (100 Hz) capable for advanced computations but 1 Hz sufficient for critical parameters like CD

## Products & Capabilities Described

### S0 UAS (Air-Deployable, Expendable Variant)

**Status:** TRL 9 in Category 5 hurricanes (as of 2024-2025 operations)

**Operational Deployment History:**
- 2024: 19 S0 deployed from NOAA WP-3D during hurricane season
- 2025: 23 S0 deployed
- Storms sampled: Hurricanes Ernesto, Francine, Helene, Milton (2024); additional missions in 2025

**Base Sensing Suite (Target Accuracies & Response Times):**
| Parameter | Accuracy | Response Time | Validation Source |
|-----------|----------|---------------|-------------------|
| Pressure | 0.4 hPa | 0.01s | Dropsondes, towers, ocean arrays |
| Temperature | 0.1°C | 0.5s | Dropsondes, towers, ocean arrays |
| Humidity | 2% | 0.3s | Dropsondes, towers, ocean arrays |
| 3D Winds | 0.2 m/s | 0.01s | Dropsondes, towers, TDR |
| Sea Surface Temperature | 0.3°C | N/A | Floating buoys, ocean arrays |
| Wave Height (Hs) | 3% | N/A | Floating buoys, ocean arrays |
| Mean Squared Slope (MSS) | 10% | N/A | Floating buoys, ocean arrays |

**Phase I Validation Results:**

*ARM SGP Tower Comparison (2021):*
- 10 S0 flights over 3 days at Lamont, Oklahoma
- Mean wind speed differences within ±0.50 m/s for all components
- Successfully resolved boundary-layer turbulence variance and vertical velocity distribution
- Tower instruments: 60 m instrumented tower with 3D sonic anemometer, temperature, humidity sensors; complemented by radiosondes, remote sensors, surface-based instrumentation

*P-3 TDR Comparison (2024):*
- Excellent agreement at 500 m altitude (lowest TDR capability)
- Consistent performance across Hurricanes Ernesto, Francine, Helene, Milton
- Validates robustness in extreme conditions
- TDR operates within ~50 km of aircraft with 2 km horizontal resolution and 0.5 km vertical resolution

*Dropsonde Comparison (March 20, 2024 clear-air test):*
- 9 total dropsondes (Vaisala and Streamsondes) within <5 km spatial and 20-minute temporal window
- Humidity agreement across profile
- Temperature: dropsonde reading colder than Streamsondes; S0 within ~0.9°C of streamsondes at lower altitudes (acceptable for time-separated measurement)
- Wind means show good agreement; S0 samples wind distribution over extended time vs. single dropsonde point
- S0 spent 50 minutes at 830 hPa and 22 minutes at 950 hPa during stepped descent
- Descent rate approximately 3.5 m/s

**Advanced Measurements (Phase I Development → Phase II Operations):**

1. **Turbulent Flux Estimation & Drag Coefficient (CD):**
   - Automated onboard algorithm developed and tested
   - 2024 results show consistency with published CBLAST experiment values (Black et al. 2007)
   - Calculations from 3.5 Hz data below 500 m across multiple storms
   - Momentum flux, turbulent kinetic energy (TKE)
   - Temperature/humidity variances
   - Applicability demonstrated across diverse TC conditions (inner core, eyewall, environment)

2. **Wave Height & Mean Squared Slope (via Kalman Filter on radar data):**
   - Phase I developed Kalman filter framework for estimating Hs and MSS from radar
   - Target accuracies (SASCWATCH): Hs <3%, MSS <10%
   - Sensor noise analysis: for <50 cm radar noise at 50 Hz sampling, target accuracies achievable
   - 40 km track length analysis demonstrates feasibility
   - Analysis assumes 50 m/s ground speed, 50 Hz sampling rate, 10 m true Hs, 0.05 rad (2.9°) true MSS, 12 s period
   - Phase II will validate filter across wider parameter space

**Sampling Frequency Robustness (Critical for Telemetry):**
From land-based flight data analysis (100 Hz, 10 Hz, 1 Hz comparison):
| Frequency | u* | CD | % Difference from 100 Hz |
|-----------|----|----|--------------------------|
| 100 Hz | 0.5979 | 0.0523 | baseline |
| 10 Hz | 0.6023 | 0.0531 | 0.15% |
| 1 Hz | 0.6756 | 0.0542 | 0.36% |

*Implication:* 1 Hz telemetry sufficient for CD calculation without meaningful loss; enables real-time transmission of reduced products.

**Operational Data Collection Examples (2024 Hurricane Helene Mission):**
- Two S0 collected approximately double total observations as all dropsondes deployed
- Hurricane Helene 09/26/2024: 2024 S0 averaged 6,300 observations per flight at 2 Hz sampling
- 2025 capability: 25,200 observations per flight (3.5 Hz)

### S0-VTOL (Vertical Takeoff/Landing)
- Reusable variant for short-range shipboard operations
- Reduces per-unit cost further through reusability
- Integrated launch/recovery platform option (Option phase)

### S0-LR (Long-Range)
- Land-launched reusable variant with >12-hour flight time for extended missions
- Slower flight speed compared to air-deployed variant
- Suitable for land-based or extended-range maritime operations

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Reconnaissance & Intensity Forecasting
- Inner-core sampling (r<100 km) with higher spatial density than dropsondes
- Eyewall wind measurements (sustained over minutes vs. instantaneous dropsonde readings)
- Maximum 1-minute sustained wind estimation at altitude (vs. instantaneous dropsonde readings)
- Boundary-layer thermodynamic profiling for operational forecast model initialization
- Stepped-descent and spiral profiling patterns operationally demonstrated (2024-2025 hurricane seasons)
- Environmental flow characterization for improved track prediction

### Secondary/Emerging Applications
- Polar lows and rapidly evolving maritime storms
- Arctic operations (cold-weather/icing enhancements planned for Phase II)
- Air-sea interaction studies (drag coefficient, momentum flux, wind-wave coupling, surface roughness investigation)
-