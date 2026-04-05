# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System

## Document Metadata
- **Type:** STTR Phase II Technical Proposal
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR N2-9533; Topic N25A-T025
- **Date:** 2026-02-25 (proposal submission)
- **BST Products/Systems Referenced:** S0 UAS, S0-VTOL, S0-LR (long-range)
- **Key Personnel:** Jack Elston (Ph.D., Principal Investigator), Maciej Stachura (Ph.D.), Jun Zhang (Ph.D.), Joshua Wadler (Ph.D.), John Park (Ph.D.)

## Executive Summary
Black Swift Technologies proposes to transition the S0 unmanned aircraft system from a NOAA-operational research platform into a Navy-adoptable atmospheric profiling capability for hazardous weather observation. The Phase II effort will complete sensor calibration and validation, advance real-time turbulence and wave-state algorithms for onboard execution, demonstrate measurable forecast improvements in Navy operational models, and prepare the system for integration into Navy platforms (P-8, MH-60, C-130) to provide persistent boundary-layer observations during tropical cyclones, polar lows, and rapidly evolving maritime storms.

## Technical Approach

### Core Mission Concept
The S0 addresses a critical observational gap in marine boundary-layer data collection by providing:
- Continuous atmospheric profiling near the air-sea interface (vs. one-time profiles from dropsondes)
- Air-deployable expendable design compatible with Navy P-8 and Air Force C-130 platforms
- 2+ hours of sustained data collection at ~$15,000 per unit (10x cost reduction vs. dropsonde-equivalent observations)
- Superior spatiotemporal coverage: 2024 data showed S0 collecting ~2x the observations of all dropsondes on the same mission
- High-resolution boundary-layer data critical for tropical cyclone intensity forecasting and data assimilation

### Phase II Technical Objectives (7 main areas)

**Objective 1: Calibration and Validation of S0 Base Sensing**
- Complete flight-relevant characterization of pressure (0.4 hPa accuracy, 0.01s response), temperature (0.1°C, 0.5s), humidity (2%, 0.3s), 3D winds (0.2 m/s, 0.01s)
- Execute test matrix across four dedicated over-ocean validation events (Base and Option periods)
- Leverage NOAA spring clear-air testing, SASCWATCH ocean arrays, and existing meteorological towers
- Phase I validation already demonstrated:
  - Wind agreement within 0.50 m/s vs. ARM SGP 60m tower across 10 flights
  - Excellent agreement with P-3 Tail Doppler Radar (TDR) across 2024 hurricane data
  - Strong correlation with Vaisala dropsondes and NOAA streamsondes in collocated flights

**Objective 2: Making the System Turnkey for DOW Missions**
- System improvements for long-term storage, rapid code updates, operational labeling
- Automated pre-flight self-checks to reduce setup time to <1 minute from boot-up
- Mission autonomy: simplified user input with human-on-the-loop control for nominal operations
- Meteorological data quality control (QC): automated detection and flagging of sensor biases (e.g., water bridging), sensor redundancy via dual humidity sensors
- Post-flight automated packaging into WMO-standard NetCDF format without manual input

**Objective 3: Real-Time Turbulence Sensing and Wave-State Algorithms**
- Transition Phase I algorithms from offline analysis to real-time onboard execution
- Turbulence metrics onboard: drag coefficient (CD), momentum flux, turbulent kinetic energy, temperature and humidity variances
- Wave-state algorithm: Kalman filter estimation of Significant Wave Height (Hs <3% accuracy) and Mean Squared Slope (MSS <10%)
- Data compression: transmit only processed products to overcome realistic communication constraints
- Phase I demonstrated drag coefficient consistency across 100 Hz, 10 Hz, and 1 Hz sampling, indicating feasibility of computationally efficient onboard processing
- Wave height analysis showed current S0 radar sensor (50 cm noise) sufficient to meet SASCWATCH accuracy targets

**Objective 4: Forecast and Situational Awareness Improvements**
- Real-time data transfer to operational centers for situational awareness
- Evaluate Navy model performance in forecasting near-surface and boundary-layer structures
- Analyze S0 data to validate and improve turbulence parameterizations
- Optimize sampling strategy through data assimilation; Phase I STRAP-RRT* simulations showed 3-4% improvement in pressure, temperature, wind speed forecasts vs. baseline methods

**Objective 5: Severe Weather Enhancements for Cold and Icing Environments**
- Extend operational envelope beyond Category 5 hurricanes (current design)
- Enable Arctic operations: temperatures down to -65°F, icing conditions
- Design upgrades for extreme cold and precipitation environments

**Objective 6: Autonomous Adaptive Sampling**
- Advance from rule-based autonomy (center fixes, eyewall following) to closed-loop adaptive sampling using onboard AI
- Integration of Generative AI framework (Temporal Multimodal Multivariate Learner) for:
  - Synthetic superobs generation: create compact mean-covariance pairs representing probability distributions
  - Advanced uncertainty quantification using mixture of multivariate PDFs to capture multimodal TC phenomena
  - Information-Theoretic RRT* path planning to balance information gain against flight constraints (energy, wind shear, precipitation)
- Real-time embedded execution on S0 flight computer via Python porting

**Objective 7: Navy Integration and Path to Full Operational Capability**
- Integration into Navy launch platforms: C-130 (Air Force), P-8 (Navy), MH-60 (Navy), shipboard and land-based versions
- Data format compatibility with DOW-based operational models
- Establish operational procedures and training materials for Navy personnel

## Products & Capabilities Described

### S0 UAS (Primary System)
**What it is:**
- Small, air-deployable unmanned aircraft system designed for atmospheric profiling in extreme weather
- Expendable design (~$15,000 unit cost); air-dropped from Navy/NOAA platforms
- Currently TRL 9 in Category 5 hurricanes (validated in 2024-2025 NOAA operations)

**Current capabilities (validated):**
- 2-hour endurance with potential for extension
- Spiral ascent/descent profiles (4 m/s ascent, 6 m/s descent rates)
- Stepped-descent profiling (loitering ~10 min per altitude)
- Sensor suite: pressure, temperature, humidity, 3D winds, sea surface temperature (via IR), wave height (via 50 Hz radar)
- 3.5 Hz base telemetry rate (expandable to 100 Hz raw sensor data)
- Continuous atmospheric evolution data (vs. ballistic sondes)

**Proposed enhancements in Phase II:**
- Real-time turbulence and wave-state algorithm execution onboard
- Dual humidity sensor redundancy for automated bias detection
- Expanded operational envelope (cold-weather/icing)
- Autonomous adaptive sampling with AI path planning

**Performance data (2024 NOAA missions):**
- 19 S0 deployed from NOAA P-3 (2024), 23 in 2025
- Single S0 flight produced ~25,200 observations (2024 sensors) vs. ~333 observations from a single dropsonde
- Under 500m altitude: S0 produces 23,609 observations vs. 83 from dropsonde
- Under 100m altitude: S0 produces 23,185 observations vs. 17 from dropsonde (1,391x equivalent dropsonde cost)
- Time-based comparison: single S0 flight ~120 min vs. dropsonde ~2.8 min per profile

### S0-VTOL (Option Phase)
- Vertical takeoff/landing variant for short-range shipboard operations
- Re-usable (lower operational cost than expendable)

### S0-LR (Option Phase)
- Long-range variant for land-launched missions
- Endurance >12 hours
- Re-usable; further reduces per-mission cost

## Use Cases & Applications

### Primary Mission: Tropical Cyclone (TC) Intensity Forecasting
- Addressed observational void in marine boundary layer (0-500m altitude)
- High-impact location: eyewall and inner-core regions (r<100 km)
- Advantages over dropsondes:
  - Better inner-core coverage: S0 samples entire region; dropsonde samples only below flight track
  - Extended sampling in strongest wind regions (eyewall)
  - Resolves turbulence and coherent structures over extended period
  - Can extract maximum 1-minute sustained wind at given altitude (vs. instantaneous dropsonde measurements)

### Secondary Missions (Phase II scope):
- **Polar lows:** Rapid maritime storm evolution in high-latitude regions
- **Arctic operations:** Extended to -65°F temperatures with icing conditions
- **Ship-based deployments (Option):** S0-VTOL for vessel operations
- **Land-based campaigns (Option):** S0-LR for sustained observation of coastal/inland severe weather

### Forecast Impact Evidence:
- Dropsonde assimilation proven to improve TC track forecasts (Aberson 2010, Ditchek et al. 2023)
- In-situ vertical profiles produce disproportionately large forecast error reductions per observation (Cardinali 2009)
- UAS predecessor system (lower capability than S0) provided ~100x more thermodynamic data than dropsondes, comparable wind observations to TDR (Cione et al. 2020)
- Phase I STRAP-RRT* adaptive sampling simulations showed 3-4% improvement in forecast fields

## Key Results from Phase I

### Validation Against Reference Systems

**Wind Measurements vs. ARM SGP Tower (2021):**
- 10 S0 flights across 3 days
- Mean wind speed differences: <0.50 m/s for all three components
- S0 reproduced variance and distribution of vertical velocity, demonstrating turbulence resolution

**Wind Measurements vs. P-3 TDR (2024 Hurricanes Ernesto, Francine, Helene, Milton):**
- Excellent agreement across all storm regions
- Demonstrated robustness of S0 measurements in extreme conditions

**Thermodynamic Profiles vs. Dropsondes (Clear-air, March 2024):**
- Humidity agreement "pretty well across the board"
- Temperature within ~0.9°C of streamsondes (accounting for time lag)
- U and V wind means agree well
- S0 advantage: extended loitering allows high-resolution boundary-layer sampling vs. single profile

### Advanced Sensing Algorithm Development

**Turbulence/Drag Coefficient (CD) Algorithm:**
- Developed onboard automated algorithm for real-time execution
- 2024 hurricane data (3.5 Hz): drag coefficient calculations from all data below 500m across multiple storms
- Frequency sensitivity analysis: remarkable consistency between 100 Hz, 10 Hz, 1 Hz sampling for CD calculation
- Results consistent with CBLAST experiment data across wind speed bins
- Enables real-time transmission of processed metrics rather than high-rate raw data

**Wave Height Algorithm (Kalman Filter):**
- Developed framework for Significant Wave Height (Hs) and Mean Squared Slope (MSS) estimation
- Error analysis under various assumptions (10m wave height, 0.05 rad MSS, 50 m/s ground speed, 50 Hz sampling)
- Results: current S0 radar sensor noise (<50 cm) achieves both Hs <3% and MSS <10% accuracy targets
- Phase II focus: validation with floating buoys and ocean arrays

### Autonomous Adaptive Sampling Framework

**Generative AI (Temporal Multimodal Multivariate Learner):**
- Replaces destructive averaging with ensemble distribution reconstruction
- Creates "synthetic superobs" (mean-covariance pairs) for compact data representation
- Advanced uncertainty quantification using mixture of multivariate PDFs
- Contextual awareness via recurrent neural units to distinguish noise from sustained changes

**Information-Theoretic Path Planning (IT-RRT*)