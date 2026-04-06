# Transitioning the Tropical Cyclone Air-Deployed sUAS CONOP to Operations

## Document Metadata
- Type: Research proposal / Transition plan
- Client/Agency: NOAA Office of Marine and Aviation Operations (OMAO)
- Program/Solicitation: NOAA Applications of Uncrewed Systems (UxS) Technology, 2021 RFP
- Date: Submitted 2021 (created/modified September 24, 2021)
- BST Products/Systems Referenced: Black Swift Technologies' S0 sUAS
- Key Personnel: 
  - Principal Investigator: Dr. Joseph J. Cione (NOAA/AOML/HRD)
  - Senior Investigators: Drs. Jun A. Zhang, Altug Aksoy, Joshua B. Wadler (NOAA/AOML)
  - Division Director: Dr. Frank D. Marks

## Executive Summary
This proposal seeks to transition small uncrewed aircraft systems (sUAS), including Black Swift Technologies' S0 platform, from research to operational use within NOAA's tropical cyclone forecasting and research missions. Over a three-year period (June 2021–May 2024), the project will deploy air-launched sUAS to collect high-resolution observations of the planetary boundary layer and sea surface in hurricane environments, enhance NOAA's operational forecast models (HWRF, HAFS), and deliver real-time data to the National Hurricane Center and Environmental Modeling Center for improved intensity forecasting and situational awareness.

## Technical Approach

### Core Concept of Operations (CONOP)
The project will conduct field experiments deploying three sUAS platforms into tropical cyclones using NOAA's WP-3D aircraft:
- **Area-I Altius 600**: 25 lbs, 1.5–4 hour flight duration
- **Black Swift Technologies S0**: ~3 lbs, 1.5–4 hour flight duration
- **Barron Associates Wingsonde**: 9 lbs, 1.5–4 hour flight duration

### Three Primary Flight Modules
1. **Eyewall Module**: Launch near hurricane center, circumnavigate at/near radius of maximum wind (RMW); measure maximum winds at various azimuths and heights
2. **Inflow Module**: Launch outside storm core, fly radially inward; measure turbulence fluxes and boundary layer properties
3. **Eye Loiter Module**: Remain within TC eye to monitor intensity and rapid intensification events

### Operational Range & Sampling
- Deployment ranges up to 190 nautical miles from parent aircraft
- Samples extreme turbulence in hurricane planetary boundary layer (PBL)
- Target altitudes: 100–1,400 m (emphasis on sub-500 m data collection)
- Can operate in high wind environments (observed wind speed up to 87 m/s at 641 m altitude in prior flights)

### Scientific Measurements & Instruments
**Instrumentation planned for integration:**
- Multi-hole turbulence probes (MHTPs) for eddy correlation measurements
- Laser and radar altimeters (advanced)
- Temperature, humidity, wind sensors
- Remote estimates of sea surface temperature (SST) via infrared (IR) measurements
- GPS dropsondes for complementary thermodynamic data

**Key observables:**
- Turbulent momentum, heat, and moisture fluxes (eddy correlation method)
- Turbulent kinetic energy (TKE)
- Boundary layer height
- Wind speed and direction profiles
- Temperature and dewpoint profiles
- Air-sea interaction parameters

## Products & Capabilities Described

### Black Swift Technologies S0
- **Description**: Small uncrewed aircraft system, ~3 lbs, designed for extreme wind/turbulence operation
- **Proposed Use**: Air-deployed from NOAA WP-3D into tropical cyclone boundary layers to collect high-resolution thermodynamic and kinematic observations
- **Status**: SBIR Phase II project; designed from scratch to meet NOAA tropical cyclone requirements
- **Expected Readiness Level**: RL 6–7 by spring 2022; approaching RL 9 (operational transition) by project completion
- **Deliverables**: 
  - 4 S0 sUAS platforms to be delivered by March 31, 2022
  - 6 additional field-ready S0 platforms by August 1, 2022
  - 4 more S0 platforms by August 1, 2023
  - Integration with multi-hole turbulence probes and advanced altimeters
  - Payload calibration missions planned April 2022, then multiple hurricane field deployments (2022, 2023)

### Data Products & Outputs
- Real-time sUAS data streams to NOAA/AOC's KARMA (Kyle's AAMPS Real-time Map App) situational awareness tool for P-3 crews
- Real-time data visualization integration into NWS operational AWIPS-II (Advanced Weather Interactive Processing System-2) for National Hurricane Center forecasters
- Quality-controlled datasets archived at NOAA/AOML for research and operational use
- Optimized data assimilation pathway for NOAA's operational HWRF and next-generation HAFS models

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Intensity Forecasting
The fundamental objective is to improve hurricane intensity forecasts by addressing a critical observational gap in the planetary boundary layer (PBL)—the region where momentum is exchanged with the ocean surface and where heat and moisture are extracted.

**Key Scientific Challenges Addressed:**
1. **Data Void Below 500 m**: Currently, GPS dropsondes are the primary source of below-500-m data, with only ~100 times more wind speed data than temperature/humidity observations (excluding Hurricane Maria 2017 sUAS data). Turbulence observations are even rarer.
2. **Boundary Layer Understanding**: The PBL is identified as critical to TC intensity change but routine thermodynamic observations remain elusive.
3. **Model Uncertainty**: Large uncertainties in track and intensity analyses from numerical weather prediction models are partially attributable to lack of in-situ PBL data.

### Operational Deliverables
1. **Enhanced TC Situational Awareness**: Real-time sUAS observations to NHC and EMC for forecaster decision-making
2. **Improved Model Physics**: Use sUAS observations to identify and correct HWRF model biases (shown example: HWRF cool/dry bias of 1–2°C in boundary layer during Hurricane Maria)
3. **Data Assimilation**: Optimize assimilation of sUAS observations into HWRF and HAFS operational models
4. **Turbulence Parameterization**: Calibrate and improve PBL turbulence parameterization schemes using observational eddy diffusivity estimates

### Previous Operational Impact (2014–2018)
Nine sUAS were deployed during:
- **Hurricane Edouard (2014)**: 2 flights
- **Hurricane Maria (2017)**: 6 flights
- **Hurricane Michael (2018)**: 1 flight

**Data collected**: 256.5 minutes of sUAS observations within hurricane PBL, primarily below 1 km altitude; longest flight 68 minutes; lowest controlled altitude 110 m; strongest measured wind 87 m/s at 641 m.

**Scientific findings**: Momentum flux measurements from sUAS compare favorably with prior P-3 crewed aircraft measurements, showing similar trends with height and reasonable magnitudes.

## Key Results (Historical Data & Analysis)

### Model Bias Identification (Hurricane Maria 2017)
Figure 2 in proposal shows HWRF model comparison with sUAS-observed (Coyote) temperature and dewpoint:
- HWRF exhibited a **cool bias of 1–2°C** and **dry bias** in the boundary layer (300–1,400 m altitude)
- Bias showed little dependence on height across the sampled boundary layer region
- Potential implications: underestimation of air-sea fluxes, altered lower boundary layer stability, degraded intensity change predictions

### Turbulence Observations
- Turbulent momentum flux magnitude estimates from sUAS flights (2017–2018) compared well with prior CBLAST and P-3 measurements
- Nondimensional momentum flux decreased with height, consistent with prior crewed aircraft observations
- First direct measurements of turbulence properties at multiple levels within hurricane eyewall and outer core regions

### Data Characteristics
- Flight patterns included "stepped descent" and "glider" configurations
- High wind speed operations validated (87 m/s at 641 m altitude)
- Extreme turbulence sampling capability demonstrated

## Notable Details

### Readiness Level (RL) Progression
The proposal establishes explicit RL targets:
- **Baseline**: S0 and Wingsonde SBIR projects design-phase; Altius 600 at ~RL 7 as of April 2021
- **End-of-Project Target**: All platforms approaching RL 9 (operational transition)
- **RL 6/7 Expectation**: S0 and Wingsonde platforms within RL 6–7 range by spring 2022

### Budget & Resource Commitment
- **Total Project Funding**: $2,129,315 (FY21–FY23)
  - FY21: $726,376
  - FY22: $926,535
  - FY23: $476,404
- **In-Kind Support**: $1,348,351 (NOAA labor, 90 P-3 flight hours valued at $941,671)
- **P-3 Flight Hour Commitment**: 135 total hours (90 from existing NOAA resources; only 45 h requested from RFP supplemental pool)

### Partnerships & Procurement
- **sUAS Contractors**: Area-I (Altius 600), Black Swift Technologies (S0), Barron Associates (Wingsonde)
- **NOAA Operating Centers**: 
  - Aircraft Operations Center (AOC) – real-time data visualization, KARMA integration
  - National Hurricane Center (NHC) – operational data reception, AWIPS-II integration
  - Environmental Modeling Center (EMC) – operational model integration, data assimilation
- **Related OMAO-Funded Effort**: Dr. Sippel's project focuses on sUAS data assimilation impacts; development at no cost to this project in FY21–22

### Competitive Advantage & Risk Mitigation
- **Multiple Platform Strategy**: Three different sUAS platforms tested to reduce single-point-of-failure risk and provide operational redundancy and cost-point flexibility
- **Existing Integration with NOAA**: All three platforms already under contract with NOAA; integration with established crewed P-3 infrastructure
- **Proven Concept**: Precedent from successful 2014–2018 missions with Coyote sUAS demonstrates technical feasibility and operational compatibility
- **Design-to-Requirements**: SBIR Phase II projects (S0, Wingsonde) specifically designed from scratch to meet NOAA TC requirements

### Data Management & Public Access
- All quality-controlled sUAS and crewed aircraft data archived at NOAA/AOML
- Public release within one year of collection
- Compliance with NOAA Data Management Planning Procedural Directive
- Model analysis and forecast datasets archived on NOAA HPC (Orion at Mississippi State)
- Code developments managed in public repositories for open sharing

### Timeline & Key Deliverables
**Calibration Phase (2021–2022)**:
- Payload integration and calibration for S0 and Wingsonde (by Dec 31, 2021)
- Multi-hole turbulence probe integration for Altius 600 (by July 1, 2022)
- Calibration missions for all platforms (April–July 2022)

**Operational Deployment Phase (2022–2023)**:
- Real-time data feeds to KARMA and AWIPS-II established for 2022 hurricane season
- 5-day hurricane field deployments for each platform (Aug–Nov 2022 and 2023)
- Real-time assimilation testing in operational models (FY23)

**Analysis & Transition (2023–2024)**:
- Model physics improvements based on boundary layer analysis
- Turbulence parameterization calibration
- Peer-review publications
- End-of-project technical report and operational transition assessment

### Personnel Expertise
**PI Dr. Joseph J. Cione**: NOAA Senior Scientist with 25+ years of experience; led first-ever UAS flights into tropical cyclones (2005 Tropical Storm Ophelia, 2007 Hurricane Noel); 2010 NOAA Bronze Medal, 2