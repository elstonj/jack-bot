# Technical Narrative for STTR Phase II: Navy Hazardous Weather

## Document Metadata
- **Type:** STTR Phase II Technical Narrative / Proposal
- **Client/Agency:** U.S. Navy (Office of Naval Research)
- **Program/Solicitation:** Navy STTR Phase II, Hazardous Weather Topic
- **Date:** Submitted 2026-01-27 (modified through 2026-03-23)
- **BST Products/Systems Referenced:** S0 UAS, S0-VTOL, S0-LR (long-range variant), SwiftCore (embedded compute system)
- **Key Personnel:** 
  - Jack Elston, Ph.D. (Principal Investigator)
  - Maciej Stachura, Ph.D.
  - Jun Zhang, Ph.D.
  - Joshua Wadler, Ph.D.
  - John Park, Ph.D.
  - Beck Cotter (last editor)

## Executive Summary

Black Swift Technologies proposes a Phase II STTR effort to transition the S0 unmanned aircraft system from a NOAA-operational research platform into a fully Navy-integrated atmospheric profiling capability for hazardous maritime weather, including tropical cyclones and Arctic environments. The effort centers on completing sensor calibration and validation, maturing real-time onboard algorithms for turbulence and wave-state measurement, demonstrating forecast improvements through Navy operational models, and hardening the platform for cold-weather and icing conditions. Phase I successfully validated S0 core sensing capabilities, developed prototype turbulence and wave-height algorithms, and established AI-based autonomous sampling frameworks; Phase II will operationalize these capabilities and demonstrate measurable forecast impact.

## Technical Approach

### Phase I Foundation
Phase I (completed) established:
- **Sensor validation** comparing S0 wind, temperature, humidity, and pressure measurements against:
  - ARM Southern Great Plains 60m meteorological tower (mean wind differences <0.50 m/s)
  - NOAA P-3 Tail Doppler Radar (TDR) observations in 2024 hurricanes (Ernesto, Francine, Helene, Milton)
  - GPS dropsondes and streamsondes from NOAA missions
- **Advanced sensing prototypes**: onboard turbulent flux algorithms and radar-based Kalman filter for significant wave height (Hs) and mean squared slope (MSS) estimation
- **Autonomous sampling frameworks**: Temporal Multimodal Multivariate (TMM) Learner for generative data compression and Information-Theoretic Rapidly-Exploring Random Tree (IT-RRT*) path planning, demonstrating up to 4% improvement in TC minimum central pressure estimates in simulation

### Phase II Base Period Technical Objectives

**Objective 1: Calibration and Validation of S0 Base Sensing**
- Complete flight-relevant characterization of pressure, temperature, humidity, and 3D wind sensing
- Execute test matrix across four dedicated over-ocean validation events (annually, Base + Option phases)
- Establish error bounds and response time characterization under representative operating conditions
- Leverage NOAA P-3 clear-air testing and ONR SASCWATCH ocean arrays for opportunistic validation data

**Objective 2: Making the System Turnkey for DOW Missions**
- Automate pre-flight checks to <1 minute from boot-up with simplified mission-type selection
- Transition to human-on-the-loop autonomy where operator not required for nominal operation
- Implement automated meteorological data quality control (handling sensor failures, water bridging, high-bank maneuvers)
- Add sensor redundancy (second humidity sensor from different manufacturer) for bias detection
- Automate post-flight data packaging into WMO-standard NetCDF files

**Objective 3: Real-Time Turbulence Sensing and Wave-State Algorithms**
- Transition Phase I algorithms (drag coefficient CD, momentum flux, turbulent kinetic energy) from offline to real-time onboard execution
- Optimize radar-based Kalman filter for Hs and MSS estimation in heavy precipitation and cloud cover
- Refine data transmission strategy (Phase I showed CD calculation consistent at 1 Hz, 10 Hz, and 100 Hz frequencies)
- Target accuracy: Hs <3%, MSS <10%

**Objective 4: Demonstration of Forecast and Situational Awareness Improvements**
- Transfer quality-controlled S0 data in real time to Navy forecasters for situational awareness
- Evaluate Navy COAMPS-TC and other models' prediction of low-level boundary-layer structure using S0 observations
- Derive improved turbulence parameterizations for physics packages (e.g., Common Community Physics Package, CCPP)
- Conduct data assimilation studies using research models to assess impact on TC track and intensity forecast skill
- Optimize sampling strategy through real data assimilation feedback

**Objective 5: Severe Weather Enhancements for Cold and Icing Environments**
- Integrate internal PTC heaters in 3D-printed nose cone to maintain pressure port clarity in icing
- Apply anti-ice chemical coatings to wings, propeller, and tail structures
- Upgrade components rated only to -40°F to enable operation down to -65°F
- Target 2-hour endurance in icing conditions while maintaining meteorological and wave-state data reporting
- Plan validation in NASA Ice Research Tunnel (Option phase) and potential Air Force Arctic flight test opportunity

**Objective 6: Autonomous Adaptive Sampling**
- Advance from rule-based autonomy (center fixes, eyewall following) to closed-loop AI-guided adaptive sampling
- Implement machine-learning–based guidance to dynamically update flight paths maximizing information gain
- Leverage local wind information to minimize deviations and increase energy efficiency
- Target continued forecast error reduction over non-collection baselines across multiple cases

**Objective 7: Navy Integration and Path to Full Operational Capability**
- Adapt S0 for Navy Common Launch Tubes (CLT) compatibility
- Leverage existing P-3 certifications and ongoing C-130 integration for platforms including P-8 and MH-60
- Conduct initial Navy/Air Force demonstration flights during Base period
- Develop CONOPS, integration standards, and FOC-enabling capabilities (Option period)

## Products & Capabilities Described

### S0 Unmanned Aircraft System
**What it is:**
- Air-deployable, expendable unmanned aircraft designed for atmospheric profiling in extreme weather
- Current platform TRL-9, proven in Category-5 hurricanes and severe maritime environments
- Approximately 2-hour endurance (2024 operations); extended capability (>12 hours) projected for future variants

**Base Sensing Suite:**
- **3D winds** (accuracy 0.2 m/s, response time 0.01s)
- **Pressure** (accuracy 0.4 hPa, response time 0.01s)
- **Temperature** (accuracy 0.1°C, response time 0.5s)
- **Humidity** (accuracy 2%, response time 0.3s)
- **Sea Surface Temperature** (accuracy 0.3°C)
- **Wave Height** (accuracy 3%, via radar Kalman filter)
- **Mean Squared Slope** (accuracy 10%, via radar Kalman filter)

**Advanced Sensing (Phase II Development):**
- Drag coefficient (CD) calculation from turbulent flux algorithm
- Momentum flux and turbulent kinetic energy computation
- Real-time onboard algorithm execution (100 Hz wind data reduced to 1 Hz transmission without loss of CD accuracy in certain conditions)

**Deployment Variants Proposed:**
- **S0 Air-Deployed (primary for Navy):** Launched from P-3, P-8, C-130, enabling rapid long-range deployment
- **S0-VTOL:** Short-range shipboard operations variant
- **S0-LR (Long-Range):** Land-launched variant with >12-hour flight time

**Cost Comparison to Dropsondes:**
- Single S0 unit cost: ~$15,000 (reusable)
- Single dropsonde cost: ~$1,000 (expendable)
- 2024 S0 performance: ~6,300 observations per 2-hour mission
- 2025+ S0 projected: ~18,900 observations per mission (3x increase)
- For measurements below 500m: single S0 equivalent to 283 dropsondes; below 100m equivalent to 1,391 dropsondes

### SwiftCore / Onboard Compute System
Referenced as embedded domain capable of running Python-ported algorithms (from Phase I MATLAB prototypes). Designed for real-time execution of:
- Generative AI frameworks (TMM Learner)
- Wave-state Kalman filters
- Turbulence metrics computation
- Autonomous path planning (IT-RRT*)

## Use Cases & Applications

### Primary Operational Context: Tropical Cyclone Observations
- **2024 Season:** 19 S0 UAS deployed from NOAA WP-3D (P-3)
- **2025 Season:** 23 S0 UAS deployed
- **Measurement focus:** 3D winds, pressure, temperature, humidity, sea surface temperature, wave height at altitudes 10–1,500m
- **Strategic advantage over dropsondes:**
  - Continuous loitering (captured entire time-evolution, not just instantaneous profiles)
  - Stepped-descent profiling at prescribed altitudes (~10 min per level) to resolve marine boundary layer turbulence
  - Spiral ascent/descent capability (4 m/s ascent, 6 m/s descent rates)
  - Horizontal coverage: 2024 data shows S0 much denser coverage in eyewall (r<100 km) compared to dropsonde single-profile sampling

### Secondary Applications (Phase II Scope)
- **Cold maritime environments and polar lows:** Arctic operations down to -65°F with icing survivability
- **Rapidly evolving maritime storms:** Mid-latitude systems beyond tropical cyclones
- **Boundary-layer turbulence research:** Direct measurement of exchange coefficients, eddy diffusivities
- **Air-sea coupling studies:** Co-located momentum flux and wave-state observations to understand wind-wave alignment effects on surface roughness

### Navy-Specific Operational Scenarios
- Real-time situational awareness for force-deployment decisions
- Adaptive sampling guided by forecast sensitivity (AI-based path planning)
- Data assimilation support for Navy COAMPS-TC and other operational models
- Storm-relative measurements supporting Navy P-8, MH-60, C-130 missions

## Key Results (Phase I Validation Data)

### Wind Measurement Validation
- **ARM SGP Tower Comparison (March–April 2021):** Mean wind speed differences <0.50 m/s across U, V, W components over 10 flights; S0 accurately reproduced variance and vertical velocity distribution (boundary-layer turbulence resolved, not just mean flow)
- **NOAA P-3 TDR Comparison (2024 Hurricanes Ernesto, Francine, Helene, Milton):** S0 wind measurements at 0.5 km and 1 km altitudes showed good agreement with TDR across all four storms
- **Dropsonde Intercomparison (2024-03-20 Clear Air Test):**
  - S0 spent extended time at prescribed altitudes (830 hPa: 50 min; 950 hPa: 22 min; 985 hPa: final minutes)
  - Mean U/V wind components agreed well with dropsondes and streamsondes
  - Temperature: S0 lower-level readings ~0.9°C warmer than streamsondes (attributed to ~1-hour temporal offset, not systematic bias)
  - Humidity: good agreement across levels

### Thermodynamic Validation
- Pressure, temperature, humidity target accuracies established and validated
- Response times characterized (pressure 0.01s, temperature 0.5s, humidity 0.3s)

### Turbulence Algorithm Development
- **Drag Coefficient Calculation:** Developed onboard algorithm computing CD from turbulent flux components
  - 2024 hurricane data (all observations below 500m): CD estimates ranged 0.007–0.052, consistent with CBLAST experiment best-fit (Black et al. 2007)
  - Sampling frequency study (Table 4): CD calculation robust across 100 Hz, 10 Hz, 1 Hz data (variation <5%), enabling efficient data transmission
  - Over-land validation: CD values ~0.025–0.052, comparable to prior studies (Shao et al. 2022)

### Wave-State Algorithm Development
- **Significant Wave Height