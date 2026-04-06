# Crested Butte SMM (SPLASH) Project Proposal

## Document Metadata
- **Type:** Research proposal
- **Client/Agency:** NOAA Weather Program Office (NOAA-OAR-WPO-2021-2006592)
- **Program/Solicitation:** FY2021 NOAA OAR Weather Program Office
- **Date:** Submitted November 2020 (field dates: August 2021 – July 2023)
- **BST Products/Systems Referenced:** S2 UAS with L-band radiometer payload
- **Key Personnel:** 
  - Jack Elston (CEO/Founder, Black Swift Technologies) – Co-Investigator
  - Gijs de Boer (Lead Investigator, CU/CIRES)
  - Allen B. White (Co-PI, NOAA PSL)
  - Additional team: Darren Jackson, James Pinto, Rob Cifelli, Janet Intrieri, Mimi Hughes, Kelly Mahoney, Sara Morris, William Currier, Jackson Osborn, Anders Jensen

## Executive Summary
This proposal funds deployment of a fleet of uncrewed aerial systems (UAS), including Black Swift Technologies' S2 platform, during the SPLASH field campaign in Colorado's East River Basin to provide observations of surface properties (soil moisture, snow cover, vegetation, surface energy budget) and lower atmosphere characteristics (temperature, pressure, humidity, winds, turbulence). These observations will support improved weather and water prediction in complex terrain, be distributed in near-real-time to operational forecast offices, and be assimilated into NOAA prediction tools.

## Technical Approach

### Core Strategy
The proposal uses a multi-platform, multi-sensor observing system deployed during the SPLASH and concurrent SAIL (Surface-Atmosphere Integrated field Laboratory) campaigns in Colorado's East River Basin to:
1. Characterize land-atmosphere interactions and surface properties in complex terrain
2. Evaluate and improve NOAA prediction tools (UFS, RRFS, National Water Model)
3. Demonstrate the value of UAS-derived observations for operational weather and water forecasting
4. Assimilate UAS data into high-resolution numerical models to assess forecast skill improvement

### Specific Technical Activities

**Task 1 – UAS-based surface properties mapping:**
- Black Swift Technologies S2 deployed with L-band radiometer (Lobe Differencing Correlation Radiometer – LDCR) for soil moisture mapping
- Four 1-week mapping missions annually during spring melt period
- Data processing and delivery to Colorado Basin River Forecast Center (CBRFC)

**Task 2 – Data quality evaluation and operational product development:**
- Statistical evaluation of UAS measurements via comparison with surface-based in-situ sensors
- Quality control workflows for real-time data distribution to NWS operational partners
- Uncertainty characterization for assimilation into forecast models

**Task 3 – Data assimilation studies:**
- High-resolution WRF model (grid spacing <1 km) with nested domains
- NCAR Data Assimilation Research Testbed (DART) using Ensemble Adjustment Kalman Filter (EAKF)
- Assessment of UAS observation impacts on convective initiation, drainage flows, and hydrometeorology

**Task 4 – Surface energy budget and land surface model evaluation:**
- Integration of UAS observations with DOE ARM mobile facility data and NOAA surface flux stations
- Evaluation of Noah and Noah-MP land surface models in UFS
- Analysis of surface energy budget partitioning impacts on snowpack simulation

**Task 5 – Planetary boundary layer observations and model evaluation:**
- Development of research-quality dataset from UAS profiling (T, q, winds)
- Evaluation of UFS and RRFS boundary layer parameterizations over complex terrain
- Support for wind energy applications in mountainous terrain

## Products & Capabilities Described

### Black Swift Technologies S2 UAS
- **What it is:** Commercially-available fixed-wing platform with flexible payload system
- **Proposed use:** Deployment with L-band radiometer for soil moisture and snow cover mapping over East River Basin
- **Capabilities in this context:**
  - Soil moisture observations via LDCR sensor
  - Snow cover mapping
  - NDVI (vegetation) measurements
  - Atmospheric measurements (pressure, temperature, humidity, winds)
  - Extended flight duration (referenced as RL7 class system)
- **Status/Readiness:** Described as "commercially-available" but notes that "further dataflow development and evaluation is required to advance its readiness level"
- **Specifications:** Fixed-wing platform with flexible payload architecture
- **Note:** Deployment of S2 would be directly funded by this proposal

### Co-deployed UAS Systems (for context)
- **RAAVEN (RL7):** 2.3 m fixed-wing with miniFlux sensor suite (T, q, winds, turbulence, turbulent fluxes)
- **HELiX (RL6):** Hexacopter with pyranometers (albedo), multispectral camera, PTH sensors

## Use Cases & Applications

### Primary Application: Colorado River Basin Water and Weather Prediction
- **Geographic focus:** East River Basin, Colorado (complex mountain terrain in headwaters of Colorado River)
- **Specific targets:**
  - Spring snowmelt prediction in mountain headwater regions
  - Streamflow forecasting for Colorado River Basin (water supply for southwestern US)
  - Improved initialization of National Water Model
  - Convective precipitation and lightning prediction over mountains
  - Wind energy resource assessment in complex terrain
  - Avalanche and flood hazard mitigation

### Operational Forecasting Support
- **Colorado Basin River Forecast Center (CBRFC):** Near-real-time data on soil moisture, surface properties, evaporative demand, snowpack
- **Grand Junction Weather Forecast Office (WFO GJT):** Boundary layer observations, cloud properties, precipitation data for daily forecasting

### Model Evaluation and Improvement Applications
- **National Water Model (NWM):** Evaluate atmospheric forcing, land-atmosphere exchange
- **Unified Forecast System (UFS):** Boundary layer parameterizations, land surface model (Noah, Noah-MP) performance, snow representation
- **Rapid Refresh Forecast System (RRFS):** Boundary layer physics, convection parameterization
- **Fire prediction:** Wind and boundary layer characterization relevant to fire potential
- **Wind renewable energy:** Assessment of diurnal wind regimes and cold-air drainage flows

## Key Results
Document is a proposal; no actual field results are presented. However, references previous successful work:
- Jensen et al. (2020) demonstrated that assimilation of UAS observations from coordinated fleet into high-resolution WRF improved forecast skill in drainage flow and convection initiation prediction in San Luis Valley, Colorado
- Prior RAAVEN deployments and miniFlux sensor use in other NOAA campaigns provide proof-of-concept

## Notable Details

### Partnerships & Co-deployment
- **University of Colorado Boulder (CIRES):** Primary institution, operates RAAVEN and HELiX UAS
- **NOAA Physical Sciences Laboratory (PSL):** Co-PI institution, financial and personnel support
- **NCAR Research Applications Laboratory:** Data assimilation and modeling support
- **US Department of Energy (DOE):** Concurrent SAIL campaign with Atmospheric Radiation Measurement (ARM) mobile facility deployment
- **National Center for Atmospheric Research (NCAR):** Modeling infrastructure

### Budget
- **Total (2 years):** $599,889
  - University of Colorado direct costs: $480,131
  - CU indirect costs: $70,118
  - NOAA PSL hosting: $49,640
- **Annual breakdown:** ~$300k/year

### Operational Transition Potential
Document highlights existing pathways for operational transition:
- **S2 platform:** "Familiar to NOAA through activities conducted by other laboratories and being considered for operational transition for boundary layer observation"
- **Existing transition discussions:** NOAA's OMAO (Office of Marine and Aviation Operations) considering integration under developing NOAA UxS (uncrewed systems) program
- **miniFlux sensor suite:** Joint NOAA PSL/CU development with active transition plan for deployment on NOAA-operated platforms

### Community Engagement & Stakeholder Alignment
- Direct coordination with NWS offices (CBRFC, GJT WFO) with signed collaboration letters
- Alignment with Western Water Assessment Colorado River Basin State of the Science Report (Lukas et al., 2020)
- Support for NOAA Snow Workshop priorities and Precipitation Prediction Grand Challenge objectives
- Public outreach planned: community open house, school district engagement (Summer Experience program), intern mentorship (CIRES RECCS program, NOAA Hollings program)

### Data Management
- Near-real-time data processing (same-day availability target)
- NetCDF format for standard archiving
- Long-term storage at NOAA PSL servers and public archival at NCEI with DOI assignment within 1 year
- Data papers planned for Earth System Science Data (ESSD) journal
- PI has track record with data publication (guest editor for LAPSE-RATE and EUREC4A data special issues)

### Diversity and Inclusion Commitment
- Team composition: gender balance goal (6 males, 4 females, 1 TBD in core team)
- Inclusion of underrepresented participants and international team members
- Coordination with CIRES Director of Diversity and Inclusion (Susan Sullivan)
- Targeted recruitment of underrepresented populations for internships