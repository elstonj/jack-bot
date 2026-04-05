# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System

## Document Metadata
- Type: STTR Phase II Technical Proposal
- Client/Agency: Office of Naval Research (ONR)
- Program/Solicitation: Navy STTR N2-9533; Topic N25A-T025
- Date: 2026-02-25 (proposal submission)
- BST Products/Systems Referenced: S0 UAS (primary), S0-VTOL, S0-LR (long-range)
- Key Personnel: Jack Elston (Ph.D., Principal Investigator), Maciej Stachura (Ph.D.), Jun Zhang (Ph.D.), Joshua Wadler (Ph.D.), John Park (Ph.D.)

## Executive Summary
Black Swift Technologies proposes to transition the S0 expendable UAS from a NOAA-operational research system into a Navy-adoptable atmospheric profiling capability for hazardous weather. Phase II focuses on completing sensor calibration/validation, developing real-time turbulence and wave-state algorithms, enabling autonomous adaptive sampling, and demonstrating forecast improvements in Navy operational models. The S0 provides orders-of-magnitude improvements over traditional dropsondes in spatiotemporal data density at ~10x lower cost per effective vertical profile.

## Technical Approach

### Core System
The **S0 UAS** is an air-deployable, expendable small uncrewed aircraft designed for sustained profiling of the marine boundary layer and air-sea interface in extreme weather. Key capabilities:

- **Endurance**: 2+ hours of continuous operation (with extension pathway to exceed 12 hours via S0-LR variant)
- **Deployment**: Air-launched from Navy platforms (P-8 preferred) or NOAA/USAF aircraft (P-3, C-130J)
- **Cost**: ~$15,000 per unit (10x reduction vs. dropsonde cost per effective profile)
- **Operating Environment**: Currently qualified to TRL 9 in Category 5 hurricanes; Phase II extends to Arctic conditions (-65°F) and icing environments

### Sensing Suite
**Base measurements** (Phase I validated):
- **Pressure**: 0.4 hPa accuracy, 0.01s response time
- **Temperature**: 0.1°C accuracy, 0.5s response time
- **Humidity**: 2% accuracy, 0.3s response time
- **3D Winds**: 0.2 m/s accuracy, 0.01s response time

**Advanced measurements** (Phase II development):
- **Sea Surface Temperature**: 0.3°C accuracy
- **Wave Height (Hs)**: 3% accuracy via radar-based Kalman filter
- **Mean Squared Slope (MSS)**: 10% accuracy
- **Turbulence metrics**: Drag coefficient (C_D), momentum flux, turbulent kinetic energy, temperature/humidity variances—computed in real-time onboard

### Data Collection & Processing
- **Raw sampling rate**: Up to 100 Hz (wind, thermodynamic sensors)
- **Radar sampling**: 50 Hz (wave measurement)
- **Data transmission**: High-rate raw data compressed onboard using Temporal Multimodal Multivariate (TMM) Learner generative framework to produce "synthetic superobs" (mean-covariance pairs) that preserve statistical and physical relationships while reducing transmission load
- **Output format**: WMO-standard NetCDF with automated meteorological quality control

## Products & Capabilities Described

### S0 Unmanned Aircraft System
**What it is**: A small, expendable, air-deployable fixed-wing UAS with distributed sensor suite for atmospheric profiling in hazardous maritime environments.

**Operational context**: Flown operationally from NOAA WP-3D (P-3) in 2024 (19 units) and 2025 (23 units) into tropical cyclones; generates 3D wind profiles, thermodynamic fields, sea surface temperature, and wave height data.

**Performance vs. dropsondes**:
- Single S0 flight collects ~25,200 observations vs. ~333 observations per dropsonde
- For measurements below 500m altitude: S0 produces equivalent of 283 dropsondes in observation count; below 100m, equivalent of 1,391 dropsondes
- 2-hour loitering capability enables continuous observation of turbulence and coherent structures vs. instantaneous dropsonde measurements
- Can estimate maximum 1-minute sustained wind at altitude; dropsondes only provide instantaneous winds

**Coverage advantage**: Figure 2 comparison shows S0 provides much better spatial coverage in inner-core region (r < 100 km) than dropsonde trajectories; eyewall sampling extends far longer than ballistic descent.

### S0-VTOL (Option phase variant)
- Vertical takeoff/landing version for short-range shipboard operations
- Reusable platform reducing cost further than air-deployable S0

### S0-LR (Option phase variant)
- Long-range version with 12+ hour endurance
- Land-launched missions
- Still cheaper than repeated dropsonde deployments

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Profiling
- **2024-2025 NOAA hurricane operations**: Demonstrated in Hurricanes Ernesto, Francine, Helene, Milton
- **Boundary layer focus**: High-resolution measurements in marine boundary layer where air-sea momentum, heat, and moisture exchange governs storm intensity and structural evolution
- **Data assimilation**: Vertical profiles provide high-impact information per datum for numerical weather prediction
- **Eyewall sampling**: Extended loitering in strongest wind region captures wind structure that dropsonde cannot achieve

### Severe Weather Applications
- **Rapid intensification prediction**: Address observational deficit in data-sparse ocean basins
- **Storm structure analysis**: Derive estimates of drag coefficient, momentum flux, and wind-wave coupling
- **Forecast sensitivity**: Support targeted observation campaigns in dynamically sensitive regions

### Proposed Navy/Joint Operations
- **Integration with P-8 maritime patrol aircraft**: Rapid deployment to great distances from fleet
- **C-130J Hercules compatibility**: Current Air Force platform for tropical cyclone reconnaissance
- **Arctic/polar low monitoring**: Extended cold-weather capability for high-latitude operations
- **Rapid maritime storms**: Supports general maritime hazardous weather operations beyond hurricanes

## Key Results (Phase I Validation)

### Wind Measurement Validation
- **ARM SGP Tower (Oklahoma, 2021)**: 10 S0 flights over 3 days showed mean differences in wind speed within 0.50 m/s for all three wind components vs. 60m tower; S0 successfully reproduced boundary-layer turbulence variance and vertical velocity distribution
- **NOAA P-3 TDR Comparison (2024 hurricanes)**: S0 wind measurements at 0.5 and 1 km altitude showed very good agreement with tail Doppler radar across all four major storms sampled

### Thermodynamic Validation
- **Dropsonde Comparison (March 2024 clear-air test)**: S0 humidity agreed well across all altitudes; temperature within ~0.9°C of other sondes after accounting for time differences; mean u and v winds agreed well
- **Data density advantage**: 50+ minute loitering at specific altitudes vs. 2-10 minute dropsonde descent; enables characterization of vertical structure at fine resolution

### Drag Coefficient Algorithm (Turbulence)
- **Phase I result**: Computed C_D values from 2024 hurricane data using 3.5 Hz sampling; results consistent with Coupled Boundary Layer Air-Sea Transfer (CBLAST) experiment reference curve
- **Frequency sensitivity analysis**: Drag coefficient calculation showed remarkable consistency between 100 Hz, 10 Hz, and 1 Hz data, indicating 1 Hz transmission sufficient for C_D computation in tested cases (though noted caveat for high-wind hurricane conditions)
- **Onboard automation**: Successful implementation of automated algorithm on S0 demonstrated feasibility of real-time turbulence metric calculation

### Wave Height Algorithm (Radar-Based Kalman Filter)
- **Phase I analysis**: Derived error equations for significant wave height (H_s) and mean squared slope (MSS) based on sensor noise, track length, and sampling rate
- **Performance prediction**: Analysis shows S0 radar with <50 cm sensor noise can achieve target accuracies (H_s <3%, MSS <10%) for hurricane-typical wave states (H_s 10-20m, period ~12s, MSS 0.05-0.1 rad)
- **Sampling rate**: 50 Hz radar sampling confirmed as sufficient; increases beyond this provide minimal improvement

### Autonomous Adaptive Sampling (AI Framework)
- **Generative AI (TMM Learner)**: Successfully developed framework that maintains statistical and physical covariance structure while compressing high-rate data into synthetic superobs
- **Advanced uncertainty quantification**: Models multimodal TC data (e.g., gale vs. storm wind profiles in single grid cell) using mixture of multivariate PDFs; novel entropy metric quantifies partial information contributions
- **Information-theoretic planning (IT-RRT*)**: Adapted Rapidly-Exploring Random Tree algorithm for TC environments; evaluates utility function balancing entropy reduction against flight constraints (energy, wind shear, precipitation)
- **Simulation results**: STRAP-RRT* variant demonstrated 1-4% improvement in hurricane forecast model metrics (pressure, temperature, wind speed, relative humidity) vs. baseline minimum-distance sampling in Hurricane Harvey simulations (Table 5)

## Notable Details

### Operational Integration Achievements
- **Proven operational deployment**: 19 S0 units in 2024, 23 in 2025 from NOAA P-3
- **Existing interoperability**: Data compatible with modern data assimilation frameworks and experimental forecasting workflows
- **Stepped-descent profiling**: Demonstrated during 2024-2025 hurricane seasons with ~10-minute loitering at prescribed altitudes to resolve turbulence; routine spiral ascent/descent profiles at ~4 m/s (ascent) and ~6 m/s (descent)

### Comparative Advantage Over Traditional Systems
- **vs. Dropsondes**: 76-1,391x more observations per deployment depending on altitude focus; 10x lower cost per effective profile; sustained rather than instantaneous sampling; longer observation duration at boundary layer
- **vs. Satellite remote sensing**: In situ profiles provide higher forecast impact per observation than satellite radiances; directly observe boundary layer through clouds; not attenuated by heavy precipitation (unlike infrared/microwave satellite products); higher vertical resolution
- **vs. manned aircraft**: Eliminates crewed aircraft risk in extreme weather; lower operational cost; enables greater deployment density; compatible with existing Navy/Air Force aviation assets via air deployment

### Partnerships & Data Sources
- **NOAA**: Ongoing operational partnership with P-3 and G-IV for tropical cyclone reconnaissance; clear-air testing protocols established
- **Universities**: Phase I collaboration with Embry-Riddle Aeronautical University (ERAU), University of Miami (UM), Old Dominion University (ODU) for validation and algorithm development
- **ONR initiatives**: Integration with SASCWATCH (Study on Air-Sea Coupling with WAves, Turbulence, and Clouds at High winds) project; ocean array deployments for collocated validation

### Phase II Technical Objectives (Structured Approach)
1. **Calibration & Validation**: Complete flight-relevant characterization through ocean array overflights and land-based testing; incorporate NOAA/SASCWATCH opportunistic validation
2. **Turnkey System**: Automated pre-flight self-checks (<1 min), simplified mission input UI, human-on-the-loop autonomy, automated meteorological QC, sensor redundancy (dual humidity sensors for bias detection), standardized post-flight data packaging
3. **Real-Time Algorithms**: Transition turbulence and wave-state algorithms from offline analysis to onboard execution; compute C_D, momentum flux, TKE, variance metrics in real-time; validate Kalman filter for H_s/MSS across wider parameter space
4. **Forecast Integration**: Real-time data transfer to operational centers; validate Navy/DoD models; improve turbulence parameterizations; data assimilation optimization of sampling strategy
5. **Cold-Weather Upgrades**: Extend operations to Arctic region, icing conditions, -65°F temperatures (vs. current hurricane-centric design)
6. **Autonomous Adaptive Sampling**: Port TMM Learner and IT-RRT* algorithms from prototype to operational flight software (JSBSim/S0 stack); enable closed-loop adaptive sampling for turnkey capability
7. **Navy Integration**: Compatibility with C-130, P-8, MH-