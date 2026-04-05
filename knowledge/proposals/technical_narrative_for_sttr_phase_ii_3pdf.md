# Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System

## Document Metadata
- **Type:** STTR Phase II Technical Proposal
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR N2-9533; Topic N25A-T025
- **Date:** 2026-02-25 (draft)
- **BST Products/Systems Referenced:** S0 UAS, S0-VTOL, S0-LR (long-range variant)
- **Key Personnel:** Jack Elston (Principal Investigator, Ph.D.), Maciej Stachura (Ph.D.), Jun Zhang (Ph.D.), Joshua Wadler (Ph.D.), John Park (Ph.D.)

## Executive Summary
Black Swift Technologies proposes to transition the S0 unmanned aircraft system (UAS) from a research platform into a Navy-operationalized atmospheric profiling capability for hazardous weather observation. The S0, already operational in Category 5 hurricanes with NOAA, will be enhanced through Phase II to provide persistent, cost-effective boundary-layer measurements (winds, pressure, temperature, humidity, sea surface temperature, wave state) while addressing Navy operational requirements for deployment, autonomy, data quality control, and forecast integration. The proposal builds on Phase I validation demonstrating that two S0 aircraft collect approximately double the observations of all deployed dropsondes while providing 10× cost reduction per effective profile.

## Technical Approach

### Core Mission
Air-deployed expendable UAS launched from Navy aircraft (P-8, C-130, MH-60) to provide vertical atmospheric profiling and air-sea interface measurements in severe weather conditions. The S0 enables sustained, adaptive sampling near the marine boundary layer—a critical data gap where traditional dropsondes provide limited information content.

### Key Technical Advances Over Current Systems
1. **Persistent Sampling vs. Ballistic Descent:** Unlike dropsondes (single profiles, ~5 min duration), S0 conducts continuous 2-hour missions with stepped-descent profiling, spiral ascents/descents, and loitering at prescribed altitudes for ~10 minutes to resolve boundary-layer turbulence.

2. **Spatial Coverage:** Figure 2 data shows S0 achieves vastly superior horizontal coverage in storm inner core (r<100 km) compared to dropsonde-only missions; can spend prolonged time in eyewall region capturing maximum 1-minute sustained wind estimates vs. instantaneous dropsonde measurements.

3. **Data Density:** Single S0 flight generates ~25,200 observations of a thermodynamic variable; equivalent to 76–1,391 dropsondes depending on altitude focus (500m and below = 283 equivalent sondes; 100m and below = 1,391 equivalent sondes at $1,000/sonde cost).

4. **Cost Structure:** Single S0 unit cost ~$15,000; provides 10× reduction in cost per effective vertical profile vs. dropsondes while capturing orders-of-magnitude improvements in spatiotemporal data density.

## Products & Capabilities Described

### S0 UAS (Primary System)
**What it is:**
- Small, air-deployable unmanned aircraft system (TRL 9 in Category 5 hurricanes)
- Expendable design for hazardous environments
- 2-hour endurance (2024 version); credible path to extension beyond 12 hours via incremental improvements

**Sensor Suite:**
- **Base Sensing:** 3D winds, pressure, temperature, humidity, sea surface temperature
- **Advanced Sensors:** Onboard radar for wave measurement; high-rate wind/thermodynamic probes (up to 100 Hz sampling)

**Target Measurement Accuracies & Response Times (Table 2):**
- Pressure: 0.4 hPa (0.01s response)
- Temperature: 0.1°C (0.5s response)
- Humidity: 2% (0.3s response)
- 3D Winds: 0.2 m/s (0.01s response)
- Sea Surface Temperature: 0.3°C
- Wave Height: 3% accuracy
- Mean Squared Slope: 10% accuracy

**Operational Modes Demonstrated:**
- Stepped-descent profiling (loiter at altitude ~10 min)
- Spiral ascent/descent (ascent rate ~4 m/s; descent ~6 m/s)
- Eyewall-following autonomous patterns
- Adaptive, information-theoretic path planning (Phase I development)

### S0-VTOL
- Vertical takeoff/landing variant for short-range shipboard operations
- Reusable platform to reduce cost further than expendable air-deployed variant

### S0-LR (Long-Range)
- Land-launched variant with >12-hour endurance
- Suitable for extended over-ocean missions
- Reusable design; lower per-mission cost than expendable S0

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Observation
- **Deployment:** Launched from NOAA WP-3D (P-3), USAF C-130J Hercules, and planned Navy P-8
- **Proven Operations:** 19 S0 missions in 2024 hurricane season; 23 in 2025, operating in hurricanes Ernesto, Francine, Helene, Milton
- **Data Collected:** 3D winds, pressure, temperature, humidity, SST, wave height in extreme conditions
- **Advantage:** Fills critical observational gap in marine boundary layer (0–500 m altitude) where air-sea momentum/heat/moisture exchange governs storm intensity evolution

### Secondary Mission (Phase II Option): Arctic/Polar Operations
- Cold-weather and icing environment capability
- Temperature range down to –65°F
- Addresses ONR requirement for polar low and maritime storm observation

### Navy-Specific Applications
- **Real-time Situational Awareness:** Data transmitted to operational centers during missions
- **Forecast Model Improvement:** Data assimilation into Navy operational models (e.g., high-resolution numerical weather prediction systems)
- **Air-Sea Interaction Research:** Collocated turbulent flux and wave-state measurements validate/improve boundary-layer parameterizations

## Key Results (Phase I Validation)

### Wind Measurement Validation
- **ARM SGP Tower (Lamont, OK) Comparison (March–April 2021):** 10 S0 flights over 3 days
  - Mean wind speed differences: <0.50 m/s for all three components vs. 60m tower
  - S0 reproduced variance and vertical velocity distribution, demonstrating turbulence resolution beyond mean flow
  
- **P-3 Tail Doppler Radar (TDR) Comparison (2024 Hurricanes Ernesto, Francine, Helene, Milton):**
  - Very good agreement at 0.5–1 km altitude
  - Confirms S0 robustness across all storm regions (Figure 10)

- **Dropsonde Comparison (2024-03-20 Clear Air Test):**
  - S0 trajectory vs. 9 collocated dropsondes (<5 km spatial separation, <20 min temporal window)
  - Humidity agreement good across altitude range
  - Wind means agree well; individual histograms at 605m MSL show S0 captures full wind distribution vs. single-point dropsonde measurement

### Turbulence & Drag Coefficient (CD) Results
- **Phase I Algorithm Development:** Onboard algorithm to compute drag coefficient from momentum flux measurements
- **2024 Hurricane Data Analysis (Figure 11):**
  - CD calculated at storm-relative locations; values consistent with Coupled Boundary Layer Air-Sea Transfer (CBLAST) empirical relationships
  - Analysis based on 3.5 Hz S0 data below 500m altitude across multiple storm regions
  
- **Sampling Frequency Sensitivity (Land-based 100 Hz Data, Table 3–4):**
  - Remarkably consistent CD values across 100 Hz, 10 Hz, and 1 Hz data
  - Suggests 1 Hz data transmission sufficient for CD calculation in lower-wind regimes; implications for real-time data streaming in operational settings

### Wave Height Algorithm Development
- **Goal:** Significant Wave Height (Hs <3%) and Mean Squared Slope (MSS <10%) from S0 radar
- **Phase I Results (Figure 12):**
  - Kalman filter framework validated using synthetic data
  - Target accuracies achievable with sensor noise <50 cm on radar altimeter
  - Enables colocation of momentum flux (drag coefficient) with wave-state for air-sea coupling studies

### AI-Based Autonomous Sampling (Phase I Foundation)
- **Generative AI Framework:**
  - Temporal Multimodal Multivariate (TMM) Learner compresses high-rate data into synthetic "superobs" (mean-covariance pairs) preserving underlying probability distribution
  - Advanced uncertainty quantification using mixture of multivariate PDFs to capture multimodal TC environments (e.g., gale vs. storm wind regions)
  - Contextual awareness via recurrent neural units to distinguish noise from sustained meteorological change

- **Information-Theoretic Path Planning (IT-RRT*):**
  - Incrementally grows tree of dynamically feasible flight segments
  - Balances predicted information gain (entropy reduction) vs. flight constraints (energy, wind shear, precipitation)
  - Aligns trajectories with local wind flows to extend endurance and coverage range

- **Phase I Simulation Results (Table 5):**
  - STRAP-RRT* planning in Hurricane Harvey simulation: 3–4% improvement in atmospheric field estimation (pressure, temperature, wind speed, relative humidity) over baseline Minimum Distance Method
  - Integration of TMM Learner further improves multimodal TC forecasting accuracy

## Phase II Technical Objectives

### Objective 1: Calibration & Validation of S0 Base Sensing
- Execute dedicated over-ocean validation flights against existing ocean arrays (4 test events across Base and Option phases)
- Land-based validation against meteorological towers
- Leverage NOAA P-3 and ONR SASCWATCH mission opportunities for opportunistic calibration data
- Establish statistically defensible error bounds under operational conditions

### Objective 2: Making System Turnkey for DOW (Department of Defense) Missions
- **System Improvements:** Long-term storage capability, rapid code updates, operational labeling/switches
- **Pre-flight Automation:** <1 min pre-flight self-checks with simplified UI (mission type selection); green-light to launch authorization
- **Mission Autonomy:** Simplified user input with human-on-the-loop control (operator not required for nominal ops)
- **Meteorological Data QC:** Transition to fully automated real-time quality control; detect and flag sensor biases (e.g., water bridging) via sensor redundancy (dual humidity sensors from different manufacturers)
- **Post-flight Packaging:** WMO standard NetCDF delivery matching Navy/Air Force user requirements; remove manual input steps

### Objective 3: Real-Time Turbulence Sensing & Wave-State Algorithms
- Transition Phase I algorithms from offline to onboard real-time execution
- Compute turbulence metrics (CD, momentum flux, TKE, T/q variances) onboard at high frequency (up to 100 Hz)
- Real-time radar-based Kalman filter for Hs and MSS estimation
- Compress and stream only processed products due to data transmission constraints

### Objective 4: Forecast & Situational Awareness Improvements
- Real-time data transfer to operational centers
- Evaluate Navy model performance in forecasting near-surface and boundary-layer structures
- Validate/improve turbulence parameterizations in operational models
- Optimize S0 sampling strategy via data assimilation feedback loops

### Objective 5: Severe Weather Enhancements (Cold/Icing)
- Upgrade from current hurricane-optimized design (Category 5, heavy precipitation) to Arctic capability
- Operating temperatures down to –65°F
- Icing condition tolerance
- Enable polar low and maritime storm observation over ice-covered regions

### Objective 6: Autonomous Adaptive Sampling
- Advance from current rule-based autonomy (center fixes, eyewall following) to closed-loop adaptive sampling
- Integrate onboard AI (TMM Learner + IT-RRT* planning) into JSBSim/S0 flight software stack
- Port Phase I algorithms to Python for embedded execution
- Enable turnkey autonomous operation with minimal operator burden

### Objective 7: Navy Integration & Path to Full Operational Capability (FOC)
- Integration into launch platforms: C-130 (