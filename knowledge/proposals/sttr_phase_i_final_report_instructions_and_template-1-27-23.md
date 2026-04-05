# STTR Phase I Final Report: Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** STTR Phase I Final Report
- **Client/Agency:** U.S. Navy, Office of Naval Research (ONR)
- **Program/Solicitation:** STTR Topic N25A-T025
- **Contract Number:** N6833525C0270
- **Period of Performance:** July 7, 2025 – January 6, 2026
- **Date Submitted:** January 2026
- **BST Products/Systems Referenced:** S0 small uncrewed aircraft system (sUAS)
- **Key Personnel:** Jack Elston (CEO, PI), Maciej Stachura (Prepared by), David Richter (SASCWATCH project)
- **TPOC:** Dr. Joshua Cossuth (ONR)

---

## Executive Summary

Black Swift Technologies conducted a Phase I STTR program to assess the feasibility of adapting the **S0 small uncrewed aircraft system (sUAS)** as an expendable, air-deployed atmospheric profiler to address observational gaps in hazardous maritime weather, particularly tropical cyclones and polar environments. The investigation combined comparative analysis, sensor validation, and engineering maturation using data from multiple tropical cyclone deployments (Hurricanes Ernesto, Helene, Milton, and Tropical Storm Imelda). 

Results confirm that the S0 provides a significant advancement over traditional profiling systems, delivering orders of magnitude more observations than dropsondes (>25,000 observations per mission vs. ~333 for dropsondes), enabling targeted sustained sampling of the marine atmospheric boundary layer (MABL), and resolving fine-scale turbulence and air–sea exchange processes not observable with legacy instruments. Phase II should focus on calibration, icing validation, and full-scale demonstrations from Navy platforms.

---

## Technical Approach

### Task B.1: Background Review and Comparative Analysis
- Quantitative comparison of S0 against NCAR/Vaisala dropsondes, radiosondes, Tail Doppler Radar (TDR), and prior-generation sUAS
- Direct comparison of S0 flight data with concurrent dropsonde deployments
- Identification of critical parameters not observable with legacy expendables (vertical velocity, turbulence spectra, air–sea fluxes, wave properties)
- Cost–data trade-space analysis demonstrating substantially greater data return per mission

### Task B.2: S0 Data Analysis and Enhancements
- Uncertainty and response-time analysis for all measured quantities using specifications from Vaisala dropsondes and other instruments
- Atmospheric Layer Comparison Experiments using 60 m instrumented meteorological tower at DOE Southern Great Plains (SGP) site, Lamont, Oklahoma
- Validation through direct comparisons with GPS dropsondes and NOAA P-3 Tail Doppler Radar during operational deployments (nearly 50 flights in hurricanes, Cat 5)
- Hazardous air approach focused on extreme cold and aircraft icing
- **Key enhancement:** Implementation of dual-GPS heading baseline instead of magnetometers, reducing heading uncertainty from ~4° to 0.5° and horizontal wind error from >1 m/s to ~0.2 m/s

### Task B.3: Turbulence and Wave Height Measurements
- **Turbulence Modeling:** High-frequency (100 Hz) 3D wind data from nose-mounted multi-hole probe to compute momentum flux, turbulent kinetic energy, and 10 m neutral drag coefficient (CDN) using direct-covariance methods
- **Reduction to 10m:** Analytical models applied to adjust measured mean winds to standard 10 m height using equations dependent on surface friction velocity and von Karman constant
- **Validation:** Comparative experiments comparing S0-derived drag coefficients against CBLAST (Coupled Boundary Layer Air–Sea Transfer) experiment results
- **Radar-Based Wave Height Estimation:** Evaluation of radar altimeter accuracy for Significant Wave Height (Hs) and Mean Squared Slope (MSS) in heavy precipitation
- **Spectral Domain Kalman Filtering:** Framework developed for onboard Kalman Filter modeling ocean surface as Fourier series to estimate wave spectra real-time

### Task B.4: Automatic Sampling
- **Two-Level Onboard Modeling:** Open-loop system with preprogrammed rules from tropical cyclone forecasting models; closed-loop system with higher autonomy using surrogate ML models
- **Dimensionality Reduction:** Artificial intelligence incorporates dimensionality reduction using Temporal Multimodal Multivariate (TMM) Learners for compact latent representations
- **Closed-Loop Architecture:** Three principal feedback loops: Data Loop (sensor data → compression → uncertainty map), Control Loop (path planning → execution), Learning Loop (assimilation → model retraining)
- **Four Automated Sampling Modes Demonstrated:**
  - Eyewall Following: Finds and tracks eyewall at given altitude to determine radius of maximum winds (RMW)
  - Center Fix: Automated detection of hurricane center using wind speed trends
  - Inflow: Measures storm inflow at lower altitudes by maintaining constant offset from local wind direction
  - Virtual Tower: Matches speed with wind over ocean arrays for sustained fixed-location sampling

---

## Products & Capabilities Described

### S0 Small Uncrewed Aircraft System (sUAS)

**What it is:**
- Expendable, air-deployed atmospheric profiling platform designed for hazardous maritime weather operations
- Small, hand-launchable or air-droppable UAS with extended endurance and high-frequency sensing

**Measured Quantities and Target Accuracies:**
| Quantity | Accuracy | Response Time | Phase II Validation |
|----------|----------|----------------|-------------------|
| Pressure | 0.4 hPa | 0.01s | Compared with dropsondes, towers, ocean arrays |
| Humidity | 2% | 0.3s | Same as above |
| Temperature | 0.1°C | 0.5s | Same as above |
| 3D Winds | 0.2 m/s | 0.01s | Dropsondes, towers, TDR; dynamic wind tunnel |
| Sea Surface Temp | 0.3°C | N/A | Floating buoys, ocean arrays |
| Wave Height (Hs) | 3% | N/A | Ocean arrays |
| Mean Squared Slope (MSS) | 10% | N/A | Ocean arrays |

**Key Sensing Systems:**
- **Thermodynamic Package:** Pressure, temperature, humidity sensors (Vaisala sonde heritage)
- **Wind Measurement:** Multi-hole probe (5-hole) for 3D wind, 100 Hz sampling capability
- **Heading Determination:** Dual-GPS baseline (upgraded from magnetometer) for improved accuracy
- **Wave Sensing:** Radar altimeter for sea-surface height and wave characterization
- **Data Logging:** On-board processing for turbulence metrics, flux calculations, wave height estimation

**Proposed Use in Context:**
- Air-deployed from Navy manned aircraft (P-3, C-130, etc.) into hazardous weather environments
- Expendable platform (no recovery required) enabling higher sampling density than traditional dropsondes
- Sustained, targeted profiling missions lasting >2 hours with communication ranges >200 nautical miles
- Provides high-fidelity MABL observations to improve Navy situational awareness and forecast accuracy

**Performance Claims from Phase I:**
- Single S0 mission: >25,000 observations (vs. ~333 per dropsonde)
- Flight endurance: >2 hours (2024 versions) to >120 minutes (2025 versions planned)
- Communication range: >200 nautical miles
- Wind measurement uncertainty: ~0.2 m/s (with dual-GPS improvement)
- Operational capability demonstrated: Cat 5 hurricane conditions
- Data density in lower 100m: ~1,400x dropsonde equivalent based on observation count
- Unique measurements: Turbulence spectra, vertical velocity, momentum flux, wave spectra

---

## Use Cases & Applications

### Tropical Cyclone Operations
- **Eyewall Characterization:** Sustained sampling of maximum wind region; demonstrated 4x increase in wind variance between 100m and 50m altitude in tropical storm conditions
- **Radius of Maximum Winds (RMW) Determination:** Recent NOAA findings show RMW errors of up to 20% without UAS data; S0 provides direct measurement
- **Inflow Characterization:** Measurement of low-level inflow circulation at rates and resolutions impossible with dropsondes
- **Storm Evolution Monitoring:** Persistent boundary-layer sampling to understand intensity evolution and air–sea coupling

**Deployment History (Phase I Validation):**
- Hurricane Ernesto (2024)
- Hurricane Francine (2024)
- Hurricane Helene (2024)
- Hurricane Milton (2024)
- Tropical Storm Imelda (2025)
- ~50 operational flights conducted with NOAA P-3 through Cat 5 conditions
- World record wind speed measurements for UAS survivability

### Polar Environments
- **Cold/Icing Conditions:** Design approach focuses on sensor core operation and ice protection via heaters and chemical repellent
- **Planned Phase II Testing:** NASA Glenn Ice Research Tunnel validation of icing mitigation strategies
- **Arctic Maritime Operations:** MABL characterization in extreme cold environments (not yet flown but identified as primary development target)

### Air–Sea Exchange & Flux Estimation
- **Momentum Flux Calculation:** Direct computation using 100 Hz multi-hole probe data and boundary-layer theory
- **Drag Coefficient (CDN) Estimation:** Derived values match CBLAST historical aircraft-based measurements; enables validation of parameterizations in numerical weather prediction
- **Enthalpy Flux Measurement:** Capability demonstrated through temperature/humidity/wind integration

### Wave State Characterization
- **Significant Wave Height (Hs):** Radar altimeter-based measurement targeting <3% error
- **Mean Squared Slope (MSS):** Ocean surface roughness parameter targeting <10% error
- **Co-located Observations:** First capability to simultaneously measure atmospheric turbulence and sea state from single platform in severe weather
- **Navy Relevance:** Supports improved parameterizations for sea-state dependent drag; critical for aviation and maritime operations

### Hazardous Weather Situational Awareness
- **High-Resolution MABL Observations:** Data assimilation into Navy weather models to reduce forecast uncertainty
- **Boundary-Layer Structure Mapping:** Vertical gradients and fine-scale variability not resolvable by remote sensing or sparse in-situ networks
- **Real-Time Adaptive Sampling:** Autonomous guidance modes reduce operator workload and enable information-driven measurements

---

## Key Results

### Comparative Analysis Results

**S0 vs. Dropsonde Data Coverage:**
- Single S0 mission provides horizontal coverage across entire inner core region (r<100 km) of hurricane
- Dropsondes sample only vertical profile below release point; cannot sustain presence over high-wind regions
- In eyewall region: S0 samples strongest winds for extended period; dropondes provide only instantaneous snapshot
- S0 can estimate maximum 1-minute sustained wind at given altitude; dropsondes cannot

**Observation Quantity Comparison (Hurricane Helene, 2024 season):**
- Two S0 missions: ~12,600 total observations
- All dropsondes deployed from same P-3 mission: ~6,300 observations
- Data advantage scales with interest in low-altitude observations (500m and below, 100m and below)

**Cost-Data Trade Space (2025 S0 capability):**
| Scenario | Observation Count | Equivalent Dropsondes | Sonde Cost | Cost per Observation |
|----------|-------------------|----------------------|-----------|----------------------|
| Full Flight | 25,200 obs | 76 | $76K | $3.01/obs |
| Under 500m | 23,609 obs | 283 | $283K | $0.012/obs |
| Under 100m | 23,185 obs | 1,391 | $1.39M | $0.0006/obs |

**Unique Measurement Capability:**
- Tropical Storm Imelda (Sept 29, 2025): Demonstrated ~4x increase in wind standard deviation (turbulence intensity) between 100m and 50m altitude
- This fine-scale boundary-layer structure is unobservable with dropsondes (single-point vertical profilers)
- Only small UAS with sustained flight and high-frequency sampling can resolve such variability

### S0 