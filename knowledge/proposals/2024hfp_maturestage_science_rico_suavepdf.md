# 2024 NOAA/AOML/HRD Hurricane Field Program - APHEX: RICO SUAVE Mature Stage Experiment

## Document Metadata
- Type: Science Description / Experiment Overview
- Client/Agency: NOAA/AOML (Atlantic Oceanographic and Meteorological Laboratory), National Hurricane Center (NHC)
- Program/Solicitation: 2024 NOAA/AOML/HRD (Hurricane Research Division) Hurricane Field Program - APHEX (Atlantic Hurricane and Tropical Storm Surge Program Experiment)
- Date: 2024
- BST Products/Systems Referenced: Black Swift Technologies S0
- Key Personnel: Joseph Cione (PI), Josh Wadler (ERAU, Co-I), Jun Zhang, Mikal Montgomery; Co-Investigators include researchers from NOAA, NCAR, University of Miami, University of Alabama in Huntsville, Mississippi State University

## Executive Summary
RICO SUAVE (Research In Coordination with Operations Small Uncrewed Air Vehicle Experiment) leverages NOAA's P-3 aircraft to deploy small uncrewed aircraft systems (sUAS) into hurricane environments unsafe for crewed operations. The experiment aims to improve understanding of tropical cyclone (TC) track and intensity through detailed observations of boundary-layer thermodynamics, wind fields, and air-sea interactions, ultimately enhancing operational forecasts and numerical model physics.

## Technical Approach
The experiment employs two complementary sUAS platforms deployed from the P-3 aircraft:

**Primary Platform - Area-I Altius 600:**
- Electric-powered sUAS with 3-4 hour endurance, 190 nautical mile range
- 8.3 ft wingspan, 25-27 lbs gross weight
- Measures pressure, temperature, relative humidity (PTHU), remotely sensed sea surface temperature
- 2023 upgrade: multi-hole pressure port probe for turbulent wind measurements
- Vaisala RD41 meteorological payload (identical to GPS dropwindsonde)
- Continuous measurements at ~5 Hz for hours-long sampling
- Advantages over dropsondes: targeted horizontal/vertical coverage, sustained observation duration enabling turbulence-scale process analysis

**Secondary Platform - Black Swift Technologies S0:**
- Smaller sUAS (3 lbs, 3 ft wingspan)
- ~1.5 hour endurance (range tests ongoing, expected similar to Altius)
- Measures PTHU, remotely sensed sea surface temperature, wave height (via laser)
- Wind velocity and atmospheric turbulence measurements available
- Real-time data transmission capability

**Complementary Observations:**
- P-3 deployed dropsondes, streamSondes, AXBTs (Airborne eXpendable BathyThermographs)
- Coordinated saildrone (ocean surface autonomous vehicle) overflights for coupled air-sea measurements
- Flight-level, TDR (Tail Doppler Radar), CRL (Compact Radar Lidar), and SFMR (Stepped Frequency Microwave Radiometer) observations from P-3

**Flight Patterns (6 modules):**
1. **Eyewall Circumnavigation:** sUAS high-density observations (HDOBs) of radius of maximum wind (RMW) and maximum sustained wind (Vmax) at multiple altitudes/azimuths
2. **Inflow Layer:** sUAS deployment from upshear-left quadrant; P-3 follows at higher altitude with dropsondes every 30° azimuth; targets downdraft effects and boundary-layer structure
3. **Inflow-Layer Turbulence:** "Zig-zag" P-3 pattern allowing sUAS descent profiling; 7 dropsondes for eddy viscosity profile derivation at hurricane-force winds
4. **Center Fix/Eye-Eyewall Sampling:** sUAS loitering in eye and sampling eye-eyewall interface
5. **Video Capture:** Single sUAS equipped with video; released in eye, proceeds to eyewall; P-3 maintains <20 nm range for full motion video (FMV) downlink
6. **Saildrone Overflight:** sUAS and P-3 coordinate passes over saildrone location; option for circumnavigation with second saildrone pass if battery permits

## Products & Capabilities Described

### Black Swift Technologies S0
- **What it is:** Small uncrewed aircraft system designed for hurricane research
- **Specifications:**
  - Weight: 3 lbs
  - Wingspan: 3 ft
  - Endurance: ~1.5 hours
  - Range: Expected similar to Altius 600 (~190 nm); range tests ongoing
- **Proposed Use:** Deploy alongside Area-I Altius 600 to measure atmospheric and oceanographic parameters in hurricane boundary layer and inflow regions
- **Sensor Suite:**
  - PTHU (pressure, temperature, relative humidity)
  - Remotely sensed sea surface temperature
  - Laser-based wave height measurement
  - Wind velocity and atmospheric turbulence measurements
- **Advantages:** Smaller footprint than Altius; complements larger platform; capable of sustained turbulence sampling and detailed vertical profiling
- **Real-Time Capability:** Data available to NHC and EMC in near-real time for operational situational awareness

### Area-I Altius 600 (included for comparison/context)
- Primary sUAS platform; mature system with demonstrated hurricane deployment history
- Longer endurance (3-4 h) enables extended sampling missions
- Enables detailed thermodynamic boundary-layer and kinematic inflow sampling

## Use Cases & Applications

**Primary Use Cases:**
1. **Hurricane Intensity Forecasting:** Improve NWS/NHC operational forecasts of tropical cyclone track and intensity change through enhanced boundary-layer observations
2. **Eyewall Sampling:** Characterize high-wind-speed eyewall structure and wind field (RMW, Vmax) at multiple altitudes and azimuthal positions—impossible to obtain via crewed operations
3. **Boundary-Layer Thermodynamics and Kinematics:** Detailed sampling of inflow layer (100-1500 m altitude) thermodynamic and kinematic structure, including downdraft effects
4. **Turbulence Characterization:** Derive vertical profiles of eddy viscosity at hurricane-force wind speeds to improve PBL (planetary boundary layer) parameterizations
5. **Eye-Eyewall Interface:** Observe thermodynamic and kinematic structure at eye-eyewall boundary; evaluate SST response and mixing processes
6. **Air-Sea Coupling:** Collocated sUAS and saildrone observations to characterize coupled atmosphere-ocean interactions and validate coupled data assimilation approaches
7. **Video Documentation:** Capture visual conditions in lower atmosphere during TC—novel observational capability for forecaster awareness

**Specific Hurricane Conditions:** Designed for Categories 1–5 hurricanes; preference for sampling storms across multiple intensity categories for data assimilation calibration

## Key Results
Document is a science description/experiment design for 2024 HFP; no results reported. However, it references prior publications establishing feasibility:
- Cione et al. (2020): "Eye of the Storm" paper documenting earlier UAS hurricane operations
- Cione et al. (2016): Coyote UAS observations in Hurricane Edouard (2014)
- Wadler et al. (2021): Thermodynamic downdraft characteristics in TC simulations
- Chen et al. (2021, 2022): LES evaluation of PBL parameterizations in hurricane conditions

## Notable Details

**Operational Integration:**
- All sUAS data available in AirOPS (AOC's P-3 situational awareness visualization tool)
- Real-time HDOBs provided to NHC for operational forecaster support
- Estimates of RMW, Vmax reported in near-real time to NHC and EMC
- Post-mission analysis compared with HWRF (Hurricane WRF) and HAFS (High-Resolution All-Scale Forecast System) model outputs

**Research Integration:**
- Two active working groups analyzing sUAS data: (1) boundary-layer turbulence/thermodynamics; (2) observing system experiments (OSEs)
- Observing System Simulation Experiments (OSSEs) planned to optimize sUAS resource deployment and quantify impact on forecasts
- Multi-model comparison (HWRF, HAFS, CM1) to evaluate small-scale boundary-layer features and processes

**Interdisciplinary Coordination:**
- RICO SUAVE designed to fly in conjunction with 11 other APHEX Mature Stage experiments/modules (Boundary Layer and Air-Sea Interactions, CHAOS, Eye-Eyewall Mixing, Gravity Wave, Convective Burst Structure, Rainband Complex Survey, Surface Wind Speed, Significant Wave Height Validation, TC Diurnal Cycle, Synoptic Flow, NESDIS satellite validation modules)
- Multi-institutional collaboration: NOAA (HRD, ARL), NCAR, Embry-Riddle Aeronautical University, University of Miami, University of Alabama in Huntsville, Mississippi State University

**Data Assimilation Focus:**
- Emphasis on evaluating sUAS data for future integration into NOAA hurricane prediction models
- Strong connection between observational analysis and operational forecast improvement
- Post-storm observing system experiments to assess sUAS impact on model performance

**Technical Gaps Addressed:**
- Sparse sampling of near-surface TC boundary layer in high-wind-speed eyewall and inflow regions
- Limited observational coverage of turbulent exchanges of heat, moisture, momentum at air-sea interface
- Gap in eddy viscosity profiles at hurricane-force wind speeds
- Lack of detailed eye-eyewall interface observations
- Limited coupled atmosphere-ocean observations in TC environment