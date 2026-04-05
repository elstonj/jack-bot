# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions (Navy STTR Phase I Final Report)

## Document Metadata
- **Type:** STTR Phase I Final Report
- **Client/Agency:** U.S. Navy, Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR Topic N25A-T025
- **Contract Number:** N6833525C0270
- **Date:** January 7, 2026
- **Period of Performance:** July 7, 2025 – January 6, 2026
- **BST Products/Systems Referenced:** S0 (small uncrewed aircraft system / sUAS)
- **Key Personnel:** Jack Elston (CEO/PI), Maciej Stachura (Prepared By), Meredith Needham (Last Editor)
- **TPOC:** Dr. Joshua Cossuth (ONR)

## Executive Summary

This Phase I effort assessed the feasibility of adapting the Black Swift Technologies S0 small uncrewed aircraft system as an expendable, air-deployed profiler for high-resolution atmospheric observations in hazardous maritime weather, including tropical cyclones and polar environments. The investigation combined comparative analysis, sensor validation, and engineering maturation using data from multiple tropical cyclone deployments (Hurricanes Ernesto, Helene, Milton; Tropical Storm Imelda). Results confirm that the S0 provides a significant advancement over traditional profiling systems: a single S0 mission returns more than 25,000 observations—orders of magnitude greater than a typical dropsonde—while enabling targeted, sustained sampling and resolving fine-scale turbulence and air-sea exchange processes not observable with legacy instruments. Recommended action: Phase II should focus on final qualification of the Common Launch Tube (CLT)-compatible deployment system, comprehensive icing validation, and full-scale demonstrations from Navy platforms.

## Technical Approach

### Overall Strategy
Phase I executed a disciplined, end-to-end evaluation of the S0 as an expendable, air-deployed platform for hazardous-weather atmospheric and ocean-surface profiling. Work addressed known limitations of legacy dropsonde-based systems (sparse temporal coverage, lack of spatial control, inability to resolve turbulence and air-sea exchange in the marine atmospheric boundary layer [MABL]).

### Four Primary Tasks

**Task B.1: Background Review and Comparative Analysis**
- Quantitative comparative analysis of S0 versus existing operational systems (NCAR/Vaisala dropsondes, radiosondes, Tail Doppler Radar, prior-generation sUAS)
- Evaluation based on: cost, observation density, spatial and temporal coverage, operational constraints
- Direct comparison of S0 flight data with concurrent dropsonde deployments
- Identification of critical parameters not observable with legacy expendables (vertical velocity, turbulence spectra, air-sea fluxes, wave properties)
- Quantification of cost-data trade space

**Task B.2: S0 Data Analysis and Enhancements**
- Validated physical sensing architecture and quantified key sources of measurement uncertainty
- Atmospheric Layer Comparison Experiments using 60 m instrumented meteorological tower at DOE Southern Great Plains (SGP) site
- Comparisons with GPS dropsondes and NOAA P-3 Tail Doppler Radar during ~50 operational deployments in hurricanes through Cat 5
- Focus on extreme cold and aircraft icing as the only hazard regime not yet flown
- Development of approach for (1) keeping sensing core operating, (2) keeping ice off aircraft structure
- Implementation of dual-GPS heading estimation to improve wind accuracy (reduced horizontal wind uncertainty from >1 m s⁻¹ to ~0.2 m s⁻¹)
- Specification development for accuracy, response time, and measurement frequency for all measured quantities

**Task B.3: Turbulence and Wave Height Measurements**
- Leveraged high-frequency (100 Hz) 3D wind data from nose-mounted multi-hole probe for momentum flux, turbulent kinetic energy, and 10 m neutral drag coefficient (C_DN) computation
- Analytical models applied to adjust measured mean winds to standard 10 m height and neutral stability boundary layer
- Validation via comparison with Coupled Boundary Layer Air-Sea Transfer (CBLAST) experiment data and repeat flights over land
- Radar-based Significant Wave Height (H_s) and Mean Squared Slope (MSS) estimation to overcome laser altimeter limitations in heavy precipitation
- Framework development for onboard Kalman Filter in spectral domain to model ocean surface as Fourier series and estimate wave spectra and properties in real-time

**Task B.4: Automatic Sampling**
- Examined classical automated sampling currently in use on S0
- Development of next-generation machine learning-based strategies
- Two-level onboard modeling: open-loop system based on preprogrammed tropical cyclone forecasting model rules, and closed-loop system with higher autonomy using surrogate ML models for self-learning and adaptive real-time updating
- Dimensionality reduction for AI using Temporal Multimodal Multivariate (TMM) Learners for compact latent representations
- Closed-loop architecture with three principal feedback loops: Data Loop (raw sensor data and generative compression), Control Loop (utility-driven path planning and execution), Learning Loop (assimilated observations for model retraining)

## Products & Capabilities Described

### S0 Small Uncrewed Aircraft System

**What It Is:**
The S0 is a small, expendable uncrewed aircraft system designed for hazardous weather operations, particularly in tropical cyclones and extreme environments. It serves as a high-endurance profiling platform capable of sustained in-situ observations.

**Specifications & Performance (2024-2025 versions):**
- **Flight Endurance:** Greater than 2 hours (2024 version: ~90 min; 2025 version: ~120 min)
- **Communication Range:** Exceeding 200 nautical miles
- **Data Collection:** 25,200+ observations per mission (2025 version; 2024 version: ~6,300 observations)
- **Sampling Rate:** Up to 100 Hz for 3D wind data (primary wind measurements at 3.5-10 Hz nominal)
- **Operational Wind Capability:** Demonstrated survival and data collection in Category 5 hurricanes
- **World Record:** Highest wind speed recorded by uncrewed aircraft (Guinness World Record)
- **Descent Rate:** ~3.3–3.5 m/s

**Primary Sensors:**
- **Atmospheric Measurements:**
  - Pressure (target accuracy: 0.4 hPa, response: 0.01 s)
  - Temperature (target accuracy: 0.1°C, response: 0.5 s)
  - Humidity (target accuracy: 2%, response: 0.3 s)
  - 3D Winds via multi-hole probe (target accuracy: 0.2 m/s, response: 0.01 s)
  
- **Ocean/Surface Measurements:**
  - Radar altimeter (newly integrated in 2025) for sea-surface height and wave characterization
  - Sea Surface Temperature (target accuracy: 0.3°C)
  - Wave Height capability via radar (target accuracy: <3% error for H_s, <10% error for MSS)

- **Guidance/Navigation:**
  - Dual-GPS heading estimation (reduced heading uncertainty from ~4° to 0.5°, yielding wind error reduction)
  - INS integration

**Proposed Enhancements for Phase II:**
- Radar-based Significant Wave Height and Mean Squared Slope measurement refinement
- Ice protection system: heating elements in nose for multi-hole probe, chemical ice repellent on aircraft body (to be validated in NASA Glenn Ice Research Tunnel)
- CLT (Common Launch Tube) compatible deployment system (pressure-based, non-pyrotechnic)
- Onboard Kalman filtering for wave spectral estimation
- Extended battery capability for longer endurance

**How Proposed for Use:**
- Air-deployed expendable profiler from manned Navy aircraft (P-3, P-8, or other platforms)
- High-resolution MABL characterization during tropical cyclones and polar operations
- Sustained sampling capability to improve weather forecast initialization and accuracy
- Autonomous guidance modes for minimal operator intervention

**Unique Capabilities:**
- Only known platform with waterproof, small form-factor 5-hole probe suitable for high-frequency turbulence measurement in extreme weather
- Ability to resolve fine-scale turbulence structure and air-sea exchange processes (demonstrated ~4× increase in wind variance between 100–50 m altitude)
- Direct computation of momentum flux and air-sea exchange coefficients (C_D, C_H, C_E) in real-time
- Targeted spatial sampling (can cover ~300 km horizontal range) vs. single-point dropsondes
- Extended temporal residence over regions of interest ("virtual tower" capability)

## Use Cases & Applications

### Primary Use Cases

**1. Tropical Cyclone Observation and Forecasting**
- **Application:** Real-time MABL profiling during hurricane operations
- **Benefit:** Improve initialization of Navy hurricane forecast models with high-density, high-frequency observations below 500 m altitude where forecast uncertainty is greatest
- **Validation Data:** Operational deployments in Hurricanes Ernesto, Helene, Milton (2024); Hurricanes in 2025 season; Tropical Storm Imelda (Sept 29, 2025)
- **Performance:** Single S0 mission collects ~2× the observations of all dropsondes deployed in a single P-3 mission; provides 10–1,391× more observations than dropsondes for low-altitude (<500 m, <100 m) regions depending on measurement type and time-based comparison
- **Specific Value:** Can estimate 1-minute sustained wind maxima at given altitude (dropsondes only provide instantaneous winds); eyewall-following capability enables accurate radius of maximum wind determination (recent NOAA data showed RMW errors up to 20% without UAS data)

**2. Marine Atmospheric Boundary Layer (MABL) Characterization**
- **Application:** High-resolution turbulence and flux measurements over water
- **Benefit:** Direct measurement of turbulent kinetic energy, momentum flux, and drag coefficients (C_DN) not available from dropsondes
- **Demonstrated Capability:** Derived C_DN values fall within physically consistent ranges comparable to historical CBLAST aircraft measurements; successfully computed drag coefficients across multiple storm-relative locations and wind speeds (2024 hurricane data); demonstrated consistency of drag coefficient calculation across 100 Hz, 10 Hz, and 1 Hz sampling frequencies
- **Application:** Feed improved air-sea interaction parameterizations into Navy weather models

**3. Ocean Surface State Monitoring**
- **Application:** Significant Wave Height (H_s) and Mean Squared Slope (MSS) measurement during extreme weather
- **Benefit:** Simultaneous atmospheric and ocean surface observations for air-sea coupling research and Navy force protection planning
- **Validation Status:** Error analysis and simulations completed; expected accuracies H_s <3%, MSS <10% with appropriate integration lengths (40+ km track); Phase II to include Kalman filter implementation and validation against buoy/ocean array data

**4. Polar and Arctic Operations**
- **Application:** Hazardous weather observations in extreme cold environments
- **Status:** Development of cold-weather and icing mitigation approach during Phase I; full operational validation planned for Phase II (NASA Glenn Ice Research Tunnel testing)
- **Relevance:** Addresses Navy operational planning needs in polar regions where weather characterization remains critical

**5. Autonomous Hazardous-Weather Sampling**
- **Application:** "Fire and forget" deployment with onboard AI-driven path planning
- **Benefit:** Minimal operator training and oversight; aircraft autonomously plans trajectories to optimally inform weather models
- **Current Operational Modes (Legacy):**
  - **Eyewall Following:** Locates and tracks eyewall; determines radius of maximum winds
  - **Center Fix:** Autonomous navigation to storm center via heading control and wind trend detection
  - **Inflow Sampling:** Constant-offset spiral inbound toward eye to measure storm inflow strength
  - **Virtual Tower:** Matches wind speed to remain stationary over fixed ocean locations (demonstrated 2025 with SASCWATCH project)
- **Future (Phase II):** Next-generation ML-based sampling strategies with self-learning capability via closed-loop feedback

## Key Results

### Comparative Analysis Results

**S0 vs. Dropsonde Data Coverage & Density**

*Horizontal Distribution:*
- S0 demonstrates much better spatial coverage in hurricane inner core (r < 100 km) compared to dropsondes
- Dropsonde: vertical profile below crewed aircraft only
- S0: