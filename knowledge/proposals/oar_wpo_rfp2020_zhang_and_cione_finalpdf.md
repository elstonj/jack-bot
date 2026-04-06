# Employing Small Unmanned Aircraft Systems to Improve Situational Awareness and Operational Physical Routines Used to Predict Tropical Cyclone Structure and Intensity

## Document Metadata
- **Type:** Research proposal
- **Client/Agency:** NOAA/OAR (Office of Oceanic and Atmospheric Research)
- **Program/Solicitation:** NOAA-OAR-WPO-2021-2006592 (Weather Program Office Research Competition)
- **Date:** 2021 (submitted for August 1, 2021 – July 31, 2023 project period)
- **BST Products/Systems Referenced:** Black Swift Technologies S0 sUAS
- **Key Personnel:** 
  - Dr. Jun A. Zhang (PI, University of Miami)
  - Dr. Joseph J. Cione (Co-PI, NOAA/AOML/Hurricane Research Division)
  - Mark Rogers, AOC/OMAO/NOAA (collaborator)
  - Brian C. Zachry, NHC/NCEP/NOAA (collaborator)
  - Avichal Mehra, EMC/NCEP/NOAA (collaborator)

## Executive Summary
This proposal seeks $598,355 over two years to evaluate and assess the benefits of using NOAA P-3 aircraft-deployed small unmanned aircraft systems (sUAS) to improve operational situational awareness for tropical cyclones and enhance physical routines in NOAA's forecast models to predict TC structure and intensity change. The work builds on previous successful deployments in hurricanes Edouard (2014), Maria (2017), and Michael (2018), advancing sUAS technology from readiness level ~7-8 toward operational transition (RL9) while providing critical boundary-layer observations currently unavailable due to safety constraints on manned aircraft.

## Technical Approach

### Core Objectives
1. Significantly enhance observations within the tropical cyclone planetary boundary layer (PBL) below 500m altitude
2. Derive mean and turbulence structures of the TC PBL at different storm intensities
3. Identify and quantify model uncertainties related to TC structure
4. Use enhanced sUAS observations to improve physics in NOAA's coupled TC operational forecast systems (HWRF, HAFS)
5. Provide real-time sUAS data to NOAA operational forecast centers (NHC, EMC, HRD)
6. Advance sUAS technology toward operational transition (RL9)

### Four Main Technical Activities

**4.1 Analysis of Existing sUAS Data (2014-2018)**
- Compute turbulent momentum fluxes (τ) from nine historical sUAS flights
- Estimate vertical eddy diffusivity (K) parameterization from observations
- Compare observed turbulence metrics to those from manned NOAA P-3 flights
- Calibrate K values for use in HWRF and HAFS PBL schemes

**4.2 Evaluate TC Mean Structure in HWRF**
- Compare HWRF model output to sUAS observations for temperature, dewpoint, moisture, and wind
- Assess model performance within low-level atmospheric boundary layer
- Identify systematic biases in model TC structure forecasts using normalized radial coordinates
- Compare air-sea thermal contrast between models and observations

**4.3 Evaluate and Improve Boundary Layer Parameterizations in HWRF**
- Assess performance of non-local PBL schemes (GFS scheme, hybrid EDMF scheme)
- Develop new parameterizations of vertical eddy diffusivity using sUAS observations
- Evaluate PBL height parameterization using critical Richardson number approach
- Transition improvements from HWRF to other operational models (HAFS)

**4.4 Conduct Field Experiments to Collect Targeted Observations**
- Deploy three sUAS platforms during 2021-2022 hurricane seasons:
  - Area-I Altius 600 (~25 lbs, 1.5-5h flight duration) – 2021 CAT testing
  - Black Swift Technologies S0 (~2.5 lbs, 1.5-5h flight duration) – 2022 CAT and field deployment
  - Barron Associates Wingsonde (~8.8 lbs, 1.5-5h flight duration) – 2022 CAT and field deployment
- Execute two primary flight modules:
  - **Eyewall module:** Launch from hurricane eye, circumnavigate eyewall at radius of maximum wind (RMW)
  - **Inflow module:** Launch outside storm core, fly radially inward to eyewall for pattern flights
- Deploy sUAS up to 150 nautical miles from NOAA P-3 deployment aircraft
- Conduct 3 multi-day hurricane field deployments in 2022 (August-October)
- Perform collocated dropsonde releases from WP-3D aircraft with sUAS flights
- Provide near-real-time data to NHC and EMC during operations

## Products & Capabilities Described

### Black Swift Technologies S0
- **What it is:** Small unmanned aircraft system, ~2.5 lbs weight, designed for extreme hurricane environments
- **Proposed use:** Air-deployed from NOAA P-3 aircraft to sample tropical cyclone planetary boundary layer at altitudes below 500m, particularly in high-wind eyewall regions
- **Status/Readiness Level:** Expected to be RL 6-7 at project start; RL 8-9 by project completion
- **Capabilities:**
  - Flight duration: 1.5-5 hours depending on platform, environmental conditions, and flight profile
  - Can operate in extreme turbulence within hurricane PBL
  - Can be deployed up to 150 nautical miles from deployment aircraft
  - Will be equipped with multi-hole turbulence probe (MHTP) for measurements
  - Equipped with laser or radar altimeter
- **Key integration:** Will undergo Clear Air Tests (CAT) in Year 1 (by Jan 31, 2022); delivery of 8 field-ready units by July 1, 2022

### Related Platforms Under Development
- **Area-I Altius 600:** 25 lbs, RL 7 as of November 2020, will carry integrated MHTP with laser/radar altimeter; four integrated units to be delivered by July 1, 2022
- **Barron Associates Wingsonde:** 8.8 lbs, designed to measure conditions in extreme turbulent hurricane environments

## Use Cases & Applications

### Primary Application: Tropical Cyclone Intensity Forecasting
- **Boundary Layer Data Collection:** Enhanced, high-resolution observations of temperature, moisture, and wind below 500m altitude in tropical cyclones—currently a critical data void
- **Air-Sea Interaction Studies:** Measure processes at the air-sea boundary where energy and momentum are exchanged; critical to understanding TC intensity change
- **Operational Forecasting Support:** Real-time data provision to NHC forecasters and emergency managers for situational awareness during landfalling hurricanes
- **Model Improvement:** Use observations to constrain and improve physics parameterizations in HWRF and HAFS operational models

### Historical Test Cases
- **Hurricane Edouard (2014):** Two sUAS missions; Flight 1 reached 55.5 m/s max wind at 27-minute duration; Flight 2 inflow mission 38.8 m/s max wind at 68-minute duration (longest flight)
- **Hurricane Maria (2017):** Six flights; highest recorded sUAS wind speed 69.5 m/s; achieved glider flights (6-7 minute duration each) at ~46-47 m/s winds
- **Hurricane Michael (2018):** One sUAS mission recording strongest wind speed 87 m/s at 641m altitude (13.5-minute duration); lowest controlled flight altitude achieved: 110m

### Projected Field Operations (2022)
- Up to 3 multi-day hurricane field deployments during August-November 2022
- Planned deployment areas: Atlantic tropical waters, East Pacific, Gulf of Mexico, Caribbean Sea
- Multiple sUAS missions per deployment (targeting 2 per platform)

## Key Results (From Historical Data Analysis)

### Turbulence Measurements
- **Data Volume:** 256.5 minutes of PBL data collected across nine historical sUAS flights, primarily at altitudes below 1km
- **Turbulence Flux Analysis:** Preliminary analysis of turbulent momentum flux (τ) estimates from sUAS flights shows reasonable agreement with estimates from manned P-3 aircraft
  - Figure 2a comparison shows sUAS operating at higher wind speeds (up to 87 m/s) compared to most P-3 flights (max ~64 m/s)
  - Figure 2b (normalized by U²) shows similar trends: τ decreases with height in hurricane boundary layer for both sUAS and P-3 measurements
  
### Model Evaluation Results
- **HWRF Performance:** Comparison of sUAS observations with HWRF forecasts for Hurricane Maria (Flight 4, 23 Sept 2017, ~1 hour before flight):
  - Strong correlation between observed and simulated temperatures and dewpoint temperatures
  - **Systematic Cold/Dry Bias:** HWRF conditions are consistently 1-2°C cooler and drier than sUAS observations
  - Bias shows minimal dependence on height within 300-1400m altitude range
  - Similar model biases identified in idealized HWRF simulations compared to dropsonde composites (Zhang et al. 2020)
  - Bias implications: affects representation of air-sea fluxes, PBL stability, and hurricane intensity change prediction accuracy
- **Validation:** Dropsonde profiles from same Maria flight confirmed sUAS observations were accurate; model bias is real

## Notable Details

### Readiness Level Advancement
- Previous Coyote sUAS work (2014-2018) advanced technology readiness level to RL 7-8
- Goal: approach operational transition at/near RL 9 by project completion
- Three new platforms specifically designed to NOAA TC requirements: S0, Wingsonde, Altius 600

### Data Provision and Operational Integration
- Near-real-time data delivery to NHC, EMC, and HRD during field operations
- Integration into Advanced Weather Interactive Processing System-2 (AWIPS2) visualization architecture for operational use
- Data archiving in ASCII (or binary) format; will be made publicly available
- Operational HWRF forecast data archived with NOAA collaborators; interested users can request access

### Partnerships and Coordination
- **NOAA Internal Collaborators:** NHC, EMC, HRD, AOC/OMAO, AOML
- **Private Sector:** Black Swift Technologies (S0), Area-I (Altius 600), Barron Associates (Wingsonde)—all under existing NOAA contracts
- **External Academic Partner:** Dr. Dongxiao Zhang (NOAA PMEL) conducting complementary research on unmanned ocean assets (Saildrone, Ocean Glider) in hurricanes; planned logistical coordination for 2022 field operations
- **UxS Program Coordination:** Dr. Sippel (AOML) leading complementary project on impacts of sUAS observations on TC operational forecasts using HWRF/data assimilation with EMC

### Budget and Resources
- **Total Budget:** $598,355 over 2 years
  - Year 1: $299,182 (University of Miami $288,415 + NOAA HRD $10,767 field travel)
  - Year 2: $299,173 (University of Miami $288,176 + NOAA HRD $10,997 field travel)
- **Computing Resources:** Access to NOAA Jet supercomputer (no additional cost) and University of Miami PC-cluster systems
- **Aircraft Resources (In-Kind):** Up to 75 hours of NOAA HRD flight hours over 2 years
  - Year 1: ~15 hours for Clear Air Tests (3 CATs × 5h each, one to validate MHTP on Altius 600)
  - Year 2: ~60 hours for in-storm missions (6 missions × 8-10h each, 2 per sUAS platform)

### Program Priorities Addressed
- **Primary:** WPO Research Obs-2 and Obs-3 (innovative observing technologies for extreme events)
- **Secondary:** Obs-4 and Obs-9

### Technical Novelty
- **First quantitative turbulent flux estimates in high-wind hurricane eyewall:** Previous CBLAST measurements were in tropical-storm-force