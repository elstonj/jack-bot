# RICO SUAVE: Research In Coordination with Operations Small Uncrewed Air Vehicle Experiment

## Document Metadata
- Type: Experiment module overview / scientific research plan
- Client/Agency: NOAA / National Hurricane Center (NHC)
- Program/Solicitation: 2024 Hurricane Field Program (HFP), Mature Stage Science
- Date: 2025-03-05 (last edited)
- BST Products/Systems Referenced: Black Swift Technologies S0
- Key Personnel: Joseph Cione (PI), Josh Wadler (ERAU, Co-PI), Jun Zhang, Mikal Montgomery; Co-Investigators include NOAA, NCAR, University of Miami, Mississippi State, UAH researchers

## Executive Summary
RICO SUAVE is a NOAA-led experiment deploying small uncrewed aircraft systems (sUAS) from a P-3 aircraft into mature hurricane environments to collect high-resolution atmospheric and oceanographic observations in regions too dangerous for crewed flight. The experiment aims to improve hurricane track and intensity forecasts by gathering detailed boundary-layer thermodynamic, kinematic, and turbulence measurements, while providing real-time situational awareness data to the National Hurricane Center.

## Technical Approach
The experiment deploys two sUAS platforms from a NOAA P-3 aircraft operating at different altitudes to capture complementary observations:

1. **Coordinated Sampling Strategy**: sUAS deployed into specific hurricane regions (eyewall, inflow layer, eye) with P-3 flying concurrent higher-altitude patterns to provide comparative validation data via dropsondes, streamSondes, AXBT, and SFMR measurements.

2. **Six Modular Flight Patterns**:
   - **P-3 Pattern #1 (Eyewall Circumnavigation)**: sUAS makes azimuthal eyewall orbits at multiple altitudes; P-3 maximizes eyewall penetrations with collocated expendables
   - **P-3 Pattern #2 (Inflow)**: sUAS released upshear-left; P-3 flies parallel paths at higher altitude with dropsondes deployed every 30° azimuth to study downdraft effects
   - **P-3 Pattern #3 (Inflow-Layer Turbulence)**: Stepped-descent sUAS with P-3 conducting zig-zag pattern to measure eddy viscosity vertical profile at hurricane-force winds
   - **P-3 Pattern #4 (Center Fix/Eye Loiter/Eye-Eyewall)**: sUAS performs low-level center fixes and eye-eyewall interface sampling
   - **P-3 Pattern #5 (Video Capture)**: Single sUAS equipped with full-motion video (FMV); P-3 maintains ≤20 nm range for continuous video link
   - **P-3 Pattern #6 (Saildrone Overflight)**: Synchronized sUAS and P-3 overflights of autonomous saildrone for air-sea interface measurements

3. **Real-Time Data Pipeline**: sUAS High-Density Observations (HDOBs) streamed to NHC and Environmental Modeling Center (EMC) with estimates of Radius of Maximum Wind (RMW) and maximum sustained wind (Vmax) at multiple altitudes; integration with AirOPS P-3 situational awareness visualization tool.

## Products & Capabilities Described

### Black Swift Technologies S0
- **Description**: Compact electric sUAS designed for hurricane operations
- **Specifications**: 
  - Gross weight: 3 lbs
  - Wingspan: 3 ft
  - Endurance: ~1.5 hours (recently tested)
  - Range: Similar to Area-I Altius 600 (expected ~190 nm in clear air)
- **Sensor Suite**:
  - PTHU (Pressure, Temperature, Relative Humidity) measurements
  - Remotely sensed sea surface temperature (SST)
  - Wave height measurement using laser
  - Wind velocity and atmospheric turbulence measurements
- **Proposed Use**: Deployed into hurricane eyewall, boundary-layer inflow regions, and eye-eyewall interfaces to collect continuous, long-duration (hours-scale) observations at scales impossible for crewed aircraft

### Area-I Altius 600 (comparative platform)
- **Specifications**: 8.3 ft wingspan, 25-27 lbs, 3-4 hour endurance, 190 nm range
- **2023 Upgrade**: Multi-hole pressure port probe for turbulent wind measurement
- **Advantage over Dropsondes**: Continuous (~5 Hz) observations over hours vs. minutes; ability to target and loiter in specific storm regions horizontally and vertically

## Use Cases & Applications

**Hurricane Intensity and Track Forecasting**:
- Real-time RMW and Vmax estimates to improve NHC operational situational awareness
- Low-altitude boundary-layer sampling in regions otherwise inaccessible to crewed reconnaissance
- Data assimilation calibration by sampling same storm at varying intensity categories (1-5)

**Boundary Layer Physics**:
- 360-degree azimuthal depictions of hurricane boundary-layer structure at multiple altitudes
- Vertical profile of eddy viscosity at hurricane-force winds (fills critical parameterization gap)
- Understanding turbulent heat, moisture, and momentum exchanges at air-sea and eye-eyewall interfaces
- Downdraft analysis in principal rainbands to determine intensity modification mechanisms

**Coupled Air-Sea Interactions**:
- Saildrone collocated sampling: coordinated atmospheric boundary-layer and upper-ocean observations
- Sea surface temperature and wave height in storm environment
- Enhanced data assimilation inputs combining autonomous vehicles (sUAS + saildrone)

**Model Evaluation & Improvement**:
- Post-storm analysis comparing sUAS observations with HWRF and HAFS forecast/analysis fields
- Testing observing system experiments (OSEs) to quantify sUAS impact and optimize deployment strategies
- Improving parameterizations in NOAA hurricane prediction models (HWRF, HAFS) based on high-resolution boundary-layer measurements

## Key Hypotheses Being Tested

1. 360-degree RMW and Vmax depictions at multiple altitudes achievable through strategic sUAS eyewall orbits synchronized with wind direction
2. Accurate TC thermodynamic/kinematic inflow-layer (100-1500 m) characterization possible via coordinated dropsonde-sUAS deployments
3. Turbulence vertical profile derivation feasible using specifically-designed P-3/sUAS flight patterns
4. Eye loitering, TC center fixes, and eye-eyewall sampling operationally possible with sUAS

## Notable Details

**Real-Time Operational Integration**: Unlike research-only platforms, RICO SUAVE explicitly targets near-real-time NHC/EMC delivery of observations to immediately improve situational awareness and forecast inputs.

**Cross-Platform Coordination**: Experiment designed to operate in conjunction with 11+ other Mature Stage modules (Boundary Layer & Air-Sea Interactions, CHAOS, Eye-Eyewall Mixing, Gravity Wave, Convective Burst, Rainband Survey, Surface Wind, Significant Wave Height, Diurnal Cycle, Synoptic Flow, satellite validation modules).

**Analysis Infrastructure**: Leverages existing working groups focused on boundary-layer turbulence/thermodynamics and observing system experiments; plans OSE/OSSE studies using Nature Run to quantify impact and optimize sUAS resource allocation.

**Comparative Validation Strategy**: All sUAS measurements co-located with simultaneous P-3 flight-level, radar, dropsonde, streamSonde, AXBT, and SFMR data to enable rigorous validation and model comparison.

**Safety-Critical Mission**: Explicitly designed to access storm regions too hazardous for crewed operations (high-wind eyewall, eye-eyewall interfaces), advancing both operational forecasting and fundamental hurricane science.