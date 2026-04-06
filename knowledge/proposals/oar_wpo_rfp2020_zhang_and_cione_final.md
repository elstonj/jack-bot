# Employing Small Unmanned Aircraft Systems to Improve Situational Awareness and Operational Physical Routines Used to Predict Tropical Cyclone Structure and Intensity

## Document Metadata
- **Type:** Research Proposal
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration), Office of Oceanic and Atmospheric Research (OAR), Weather Program Office (WPO)
- **Program/Solicitation:** NOAA Funding Opportunity NOAA-OAR-WPO-2021-2006592; Competition Area: Observations
- **Date:** Submitted 2020 (for 2021-2023 funding period)
- **Principal Investigator:** Dr. Jun A. Zhang, University of Miami
- **Co-Principal Investigator:** Dr. Joseph J. Cione, Hurricane Research Division, AOML/NOAA
- **Project Period:** August 1, 2021 – July 31, 2023 (2 years)
- **Total Budget:** $598,355 (Year 1: $299,182; Year 2: $299,173)
- **BST Products Referenced:** S0 (small unmanned aircraft system)
- **Key Personnel:** Dr. Jun Zhang, Dr. Joseph Cione, Dr. Brian C. Zachry (NHC), Dr. Avichal Mehra (EMC), Mark Rogers (AOC/OMAO)

## Executive Summary

This proposal evaluates the use of NOAA P-3 aircraft-deployed small unmanned aircraft systems (sUAS) to improve observational coverage within the tropical cyclone planetary boundary layer (PBL)—a critical data-sparse region below 500 meters altitude. By enhancing in-situ measurements of temperature, moisture, wind, and turbulence in this region, the project aims to improve NOAA's operational hurricane intensity forecasts through better understanding of boundary-layer physics and advanced data assimilation, potentially transitioning sUAS technology from research readiness level 7-8 to operational readiness (RL 9).

## Technical Approach

### Data Analysis and Compilation
- Analysis of existing sUAS data collected during nine missions in three Major Hurricanes (Edouard 2014, Maria 2017, Michael 2018) totaling 256.5 minutes of boundary layer observations
- Derivation of turbulent momentum flux (τ) and vertical eddy diffusivity (K) from sUAS observations
- Comparison of observations with existing dropsonde and manned aircraft data

### Model Evaluation
- Retrospective HWRF (Hurricane Weather Research and Forecast) model forecasts compared against sUAS observations
- Evaluation of mean TC structure, particularly thermodynamic conditions (air temperature, dewpoint) at various altitude levels
- Assessment of model biases in boundary layer representation
- Identification of PBL height parameterization errors using critical Richardson number approach

### Physics Improvement
- Development of improved vertical eddy diffusivity parameterizations based on observed turbulence data
- Calibration of PBL schemes in HWRF using observational constraints
- Planned application of findings to HAFS (Hurricane Analysis and Forecast System) and other operational models

### Field Operations
- Deployment of three sUAS platforms through NOAA P-3 aircraft:
  - **Black Swift Technologies S0** (primary focus for this analysis)
  - Area-I Altius 600
  - Barron Associates Wingsonde
- Two primary flight modules: "eyewall" (circumnavigation of eyewall at radius of maximum wind) and "inflow" (radial inflow from outer core)
- Coordinated dropsonde deployment to provide collocated measurements
- Real-time data delivery to NHC, EMC, and HRD

## Products & Capabilities Described

### Black Swift Technologies S0
- **Weight:** ~2.5 lbs
- **Endurance:** 1.5–5 hours (depending on configuration and conditions)
- **Deployment Range:** Up to 150 nautical miles from deployment aircraft
- **Capabilities:** Temperature, moisture, wind measurements at low altitude (100–1000m); can measure turbulence in extreme hurricane conditions
- **Status as of proposal:** Readiness Level 6–7; expected to reach RL 9 by end of project
- **Advantages:** Upgrade over previous Coyote sUAS; significantly lighter and more flexible platform
- **Design Context:** SBIR Phase II project designed specifically to meet NOAA tropical cyclone requirements

### Existing Coyote sUAS (Baseline for Comparison)
- **Past Performance:** Successfully deployed 9 times into Hurricanes Edouard, Maria, and Michael (2014–2018)
- **Achievements:** Set records for low-altitude flight (~110 m) and maximum sustained wind measurement (87 m/s at 641 m altitude)
- **Current Status:** RL 7–8
- **Data Quality:** Turbulence momentum flux measurements comparable to NOAA P-3 data from previous studies

## Use Cases & Applications

### Primary Use Case: Hurricane Intensity Forecasting
- Enhanced boundary layer observations to improve HWRF intensity predictions
- Focus on the air-sea boundary region where energy/momentum exchange occurs and affects landfall wind severity
- Targeted data collection during major hurricane seasons (August–October) in Atlantic, East Pacific, Gulf of Mexico, and Caribbean

### Specific Mission Types
1. **Eyewall Module:** Measure radial extent and vertical structure of maximum winds; circumnavigate at radius of maximum wind (RMW)
2. **Inflow Module:** Measure turbulence fluxes and mean properties during radial inflow from outer core to eyewall

### Operational Impact
- Real-time data provision to National Hurricane Center for improved situational awareness and public forecast decisions
- Support for emergency managers and life-safety decision-making
- Data assimilation into HWRF and next-generation UFS

## Key Technical Findings (From Historical Data)

### Existing sUAS Data (2014–2018)
- **Data Volume:** 256.5 minutes total at altitudes primarily below 1 km; longest flight: 68 minutes
- **Environmental Range:** Wind speeds 27.0–87.0 m/s across nine missions
- **Altitude Coverage:** Minimum controlled flight altitude: 110 m

### Model Bias Identification (Hurricane Maria Case Study)
- HWRF consistently simulates boundary layer air temperatures **1–2°C cooler and drier** than sUAS observations
- Bias shows minimal height dependence across sampled layer (300–1400 m)
- Similar biases identified in idealized HWRF simulations vs. dropsonde composites
- Implications for air-sea flux calculations, PBL stability, and intensity prediction

### Turbulence Measurements
- sUAS-derived momentum flux estimates compare favorably with historical NOAA P-3 data from CBLAST experiment and Allen/Hugo hurricane flights
- Nondimensional momentum flux (||τ||/U²) vs. height shows consistent decreasing trend with both sUAS and P-3 data
- Demonstrates feasibility of capturing high-wind turbulence statistics from small platforms

## Project Deliverables & Timeline (Selected Key Milestones)

### Year 1 (2021)
- Sensor calibration and integration for BST S0 and Barron Wingsonde: December 1, 2021
- Clear Air Tests (CATs) for both sUAS platforms: January–February 2022
- Analysis of mean boundary layer structure from existing data: February 28, 2022
- Quality-controlled sUAS data provision to EMC/HRD for data assimilation: January 31, 2022
- Turbulence parameter derivation: April 30, 2022
- Peer-reviewed publication: May 31, 2022

### Year 2 (2022–2023)
- Field-ready delivery of 8 BST S0 systems and Barron Wingsonde units: July 1, 2022
- Multi-day hurricane field deployments: August–November 2022 (up to 3 deployments)
- Real-time operational sUAS data delivery: August–November 2022
- Post-processing and analysis of 2022 field data: January 31, 2023
- HWRF model comparisons (mean structure): February 28, 2023
- Turbulence structure validation: March 31, 2023
- Physics improvement implementation: June 30, 2023
- End-of-project technical report and operational transition assessment: July 31, 2023

## Notable Details

### Operational Readiness Advancement
- Previous sUAS work (Coyote) advanced technology to RL 7–8; this project targets transition to operational RL 9
- BST S0 and other new platforms expected to progress from RL 6–7 to RL 9 over project duration

### Collaborative Framework
- Coordination with NOAA National Hurricane Center (NHC), Environmental Modeling Center (EMC), Hurricane Research Division (HRD), and Aircraft Operations Center (AOC)
- Synergy with parallel NOAA UxS-funded data assimilation project (led by Dr. Sippel) that will evaluate sUAS impacts on HWRF
- Coordination with complementary NOAA PMEL project using Saildrone and Ocean Gliders to sample surface layer and upper ocean

### Data Assimilation Synergy
- Separate NOAA UxS funding (not in this proposal) addresses data assimilation development at HRD/EMC
- This proposal focuses on model physics evaluation and improvement

### Computing Resources
- Access to NOAA Jet supercomputer at no additional cost
- University of Miami PC-cluster systems available

### Data Management
- sUAS field data archived by NOAA HRD as part of Annual Hurricane Field Program (public availability)
- Model output stored in NetCDF format, made publicly available after publication
- Operational HWRF data available through NOAA/EMC with access via NOAA collaborators

### Previous Field Success
- Nine sUAS missions flown 2014–2018 into Major Hurricanes with no loss of aircraft
- Near-real-time data successfully delivered to NHC and incorporated into public forecasts
- Established operational viability of CONOP (concept of operations) using P-3 as deployment platform

### Boundary Layer Physics Focus
- Targets critical knowledge gap: detailed observations in lowest 500m of tropical cyclones extremely limited due to safety constraints
- Emphasis on both kinematic (wind, inflow angle) and thermodynamic (temperature, moisture, turbulence) measurements
- Particular interest in air-sea interaction processes crucial to intensity change