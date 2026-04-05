# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System

## Document Metadata
- **Type:** STTR Phase II Technical Proposal
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR N2-9533; Topic N25A-T025
- **Date:** 2026-02-25 (proposal submission date)
- **BST Products/Systems Referenced:** S0 UAS (primary focus), S0-VTOL, S0-LR (long-range variant mentioned for Option phase)
- **Key Personnel:** 
  - Jack Elston, Ph.D. (Principal Investigator)
  - Maciej Stachura, Ph.D.
  - Jun Zhang, Ph.D.
  - Joshua Wadler, Ph.D.
  - John Park, Ph.D.
  - Beck Cotter (last editor)

## Executive Summary

Black Swift Technologies proposes a Phase II effort to transition the S0 unmanned aircraft system from a NOAA-operational research platform into a Navy-adoptable atmospheric profiling capability for hazardous weather conditions, particularly tropical cyclones, polar lows, and maritime storms. The proposal builds on Phase I validation work that demonstrated the S0's superior capability compared to traditional dropsonde systems, delivering 2+ hours of continuous boundary-layer observations at approximately $15,000 per unit—a 10x cost reduction per effective vertical profile. Phase II focuses on completing sensor calibration and validation, making the system operationally turnkey, transitioning advanced turbulence and wave-state algorithms to real-time onboard execution, demonstrating forecast improvements in Navy models, enabling Arctic operations, and establishing the path to full operational capability (FOC) across Navy platforms (P-8, C-130, MH-60).

## Technical Approach

### Core Problem Statement
Severe weather prediction depends critically on high-resolution observations of the lower atmosphere and air-sea interface, where momentum, heat, and moisture exchange govern storm intensity. Existing operational systems (dropsondes, radiosondes, satellite remote sensing) provide limited coverage in data-sparse ocean regions under hazardous conditions due to:
- **Dropsondes:** Single profile per deployment (~$1,000 each), limited by fixed aircraft flight tracks, ~2-10 minute descent times, sparse sampling density
- **Satellites:** Global coverage but limited penetration beneath clouds, especially in heavy precipitation; lower per-datum forecast impact
- **Radiosondes:** Fixed launch locations, coarse temporal resolution, poor representation of air-sea interface in high winds

### S0 System Value Proposition
The S0 directly addresses these gaps through:
- **Persistent sampling:** 2+ hours continuous data collection near air-sea interface (vs. 2-10 min for dropsondes)
- **High spatial/temporal density:** ~6,300 observations per flight in 2024 version; tripling for 2025+
- **Maneuverability:** Loiters at prescribed altitudes (~10 min per level for stepped-descent profiling), executes spiral profiles (ascent ~4 m/s, descent ~6 m/s)
- **Cost efficiency:** ~$15,000 per airframe; delivers equivalent observations to 76-1,391 dropsonde equivalents depending on altitude focus
- **Boundary-layer focus:** Can spend extended time in the marine boundary layer (MBL), where vertical gradients are strongest and forecast information content is highest
- **Reusable platforms:** S0-LR variant offers 12+ hour endurance for land-based operations; S0-VTOL enables short-range shipboard operations

### Phase I Achievements (Foundation for Phase II)

**1. Sensing Performance Validation:**
- Compared S0 wind measurements against 60m ARM SGP tower (Oklahoma, 2021): mean wind speed differences **< 0.50 m/s** across all three components over 10 flights across three days
- Validated vertical wind variance and turbulence capture against tower observations
- Compared against NOAA P-3 Tail Doppler Radar (TDR) in 2024 hurricanes (Ernesto, Francine, Helene, Milton): **very good agreement** at lowest TDR altitude (500 m)
- Compared against Vaisala dropsonde and Streamsonde data in clear-air tests: good agreement in temperature, humidity, and mean wind components

**2. Target Accuracy and Response Times (Table 2):**
| Quantity | Accuracy | Response Time | Validation Method |
|----------|----------|---------------|--------------------|
| Pressure | 0.4 hPa | 0.01s | Dropsondes, towers, ocean arrays |
| Humidity | 2% | 0.3s | Dropsondes, towers, ocean arrays |
| Temperature | 0.1°C | 0.5s | Dropsondes, towers, ocean arrays |
| 3D Winds | 0.2 m/s | 0.01s | Dropsondes, towers, TDR; dynamic wind tunnel |
| Sea Surface Temp | 0.3°C | N/A | Floating buoys, ocean arrays |
| Wave Height | 3% | N/A | Floating buoys, ocean arrays |
| Mean Squared Slope | 10% | N/A | Floating buoys, ocean arrays |

**3. Advanced Sensing Development:**

**Turbulence/Drag Coefficient Calculation:**
- Developed onboard algorithm to compute drag coefficient (C_D) from momentum flux measurements
- 2024 hurricane season results show calculated C_D values consistent with CBLAST experimental baseline
- Demonstrated frequency analysis: drag coefficient remains consistent across 100 Hz, 10 Hz, and 1 Hz data sampling rates for land-based flights
- Validated computational approach for real-time execution

**Wave Height and Mean Squared Slope Estimation:**
- Developed Kalman Filter framework for estimating Hs (Significant Wave Height) and MSS (Mean Squared Slope)
- Theoretical analysis shows S0 radar sensor (50 Hz sampling, <50 cm noise) capable of achieving **<3% Hs accuracy** and **<10% MSS accuracy** for 40 km track lengths
- Performance validated across assumed hurricane conditions (Hs 10-20 m, MSS 0.05-0.1 rad)

**4. Autonomous Adaptive Sampling Framework (AI-based):**
- Developed Temporal Multimodal Multivariate (TMM) Learner for generative compression of S0 data
  - Creates "synthetic superobs" (mean-covariance pairs) preserving ensemble probability distributions
  - Advanced uncertainty quantification using mixture of multivariate PDFs; captures multimodal TC phenomena (gale vs. storm winds)
  - Contextual awareness: distinguishes transient noise from sustained meteorological changes
- Adapted Information-Theoretic RRT* (IT-RRT*) path planning algorithm for TC environments
  - Dynamically grows tree of feasible flight segments balancing information gain against flight constraints (energy, wind shear, precipitation)
  - Aligns trajectories with local wind flows to extend coverage and endurance
- Phase I simulation validation (STRAP-RRT* variant): demonstrated **3-4% improvement** in atmospheric observation quality vs. baseline Minimum Distance Method
  - Tested in Hurricane Harvey scenario with data assimilation into forecast models
  - TMM Learner integration reduces epistemic uncertainty, enabling tractable real-time embedded hardware execution

**5. Operational Context:**
- 19 S0 UAS operated from NOAA WP-3D (P-3) in 2024 hurricane season; 23 in 2025
- Successfully demonstrated capability in Category 5 hurricanes (TRL 9)
- Data integration into NOAA operational workflows
- Partnership with Embry-Riddle Aeronautical University (ERAU), University of Miami (UM), and Old Dominion University (ODU)

### Phase II Technical Objectives (7 main areas)

**Objective 1: Calibration and Validation of S0 Base Sensing**
- Complete flight-relevant characterization of pressure, temperature, humidity, 3D winds
- Execute dedicated STTR over-ocean validation events each year of Base and Option phases (4 total)
- Land-based flight testing of S0 upgrades; comparison against local meteorological towers
- Leverage opportunistic NOAA P-3 missions and ONR SASCWATCH ocean array deployments
- Establish statistically defensible error bounds under representative operating conditions

**Objective 2: Making the System Turnkey for DOW (Department of the Navy/Department of War) Missions**
- System improvements: storage capability, rapid code updates, operational labeling/switches
- Automated pre-flight self-checks with simple operator feedback; goal: <1 minute pre-flight time with intuitive mission selection
- Mission autonomy: simplified user input with human-on-the-loop control; autonomous nominal operation with operator override capability
- Meteorological data quality control (QC): transition from manual post-flight processing to real-time automated NetCDF production
  - Address complex errors (water bridging, high-bank maneuver artifacts)
  - Add sensor redundancy (second humidity sensor from different manufacturer) for automatic bias detection
- Post-flight met data packaging: ensure WMO standard netCDF format compliance with Navy/Air Force requirements; eliminate manual input steps

**Objective 3: Real-Time Turbulence Sensing and Wave-State Algorithms**
- Transition Phase I algorithm prototypes from offline analysis to onboard real-time execution
- Turbulence metrics computed onboard in real-time: drag coefficient (C_D), momentum flux, turbulent kinetic energy, temperature and humidity variances
- Radar-based Kalman filter for Hs and MSS estimation refined, tuned, and validated using high-frequency (up to 100 Hz) wind and radar data
- Processed products transmitted instead of raw high-rate data (bandwidth constraint management)

**Objective 4: Forecast and Situational Awareness Improvements**
- Real-time data transfer to operational centers for situational awareness
- Evaluation of Navy and other operational models' performance in forecasting near-surface and boundary-layer structures
- S0 data analysis for turbulence parameterization validation and model improvement
- Optimization of S0 sampling strategy through data assimilation studies

**Objective 5: Severe Weather Enhancements for Cold and Icing Environments**
- Current design: optimized for Category 5 hurricanes (heavy precipitation, extreme winds)
- Planned upgrades: Enable Arctic region operations with icing conditions and temperatures down to -65°F
- Design modifications for cold-weather survival and sensor performance in extreme cold

**Objective 6: Autonomous Adaptive Sampling**
- Advance from current rule-based autonomy (center fixes, eyewall following) to closed-loop adaptive sampling using onboard AI
- Integration of TMM Learner and IT-RRT* planning into JSBSim/S0 flight software stack for operational execution
- Enable turnkey system capability through intelligent mission planning

**Objective 7: Navy Integration and Path to Full Operational Capability (FOC)**
- Integration tasks for DOD launch platforms: C-130 (Air Force), P-8 (Navy), MH-60 (Navy)
- Ship-based and land-based deployment variants
- Data format compatibility for Navy DOW-based operational models
- Establishment of operational procedures and logistics for sustained Navy operations

## Products & Capabilities Described

### S0 Unmanned Aircraft System (Primary Product)

**Physical Characteristics:**
- Air-deployable small uncrewed aircraft (expendable or recoverable variant)
- Current endurance: 2 hours demonstrated in 2025 missions with credible path to further extension
- Design optimized for rapid deployment from Navy and Air Force aircraft (P-8, C-130)
- Capable of autonomous flight management with reduced operator burden

**Sensor Suite (Base):**
- 3D wind measurement system (dual/triple-axis)
- Pressure sensor
- Temperature sensor
- Humidity sensor
- Radar altimeter (50 Hz, <50 cm noise target)
- GPS for positioning and data geolocation
- High-rate data acquisition (100 Hz capability; real-time transmission rates TBD)

**Advanced Sensors (Phase II additions):**
- Secondary humidity sensor (redundancy for QC)
- Turbulence calculation algorithms onboard
- Wave-state estimation (Hs, MSS) capability

**Performance Claims (from Phase I validation and Phase II targets):**
- Wind measurement accuracy: 0.2 m/s; response time 0.01s
- Pressure accuracy: 0.4 hPa; response time 0.01s