# Assimilation of Uncrewed Aircraft System Observations to Improve Low-level Wind Guidance to Support Wildland Firefighting

## Document Metadata
- Type: NASA Phase II SBIR Proposal with NCAR commitment letter
- Client/Agency: NASA (SBIR Program)
- Program/Solicitation: NASA Phase II SBIR (follows Phase I effort)
- Date: January 25, 2024 (submission/commitment date)
- BST Products/Systems Referenced: BST UAS platforms (unspecified model designations)
- Key Personnel: 
  - BST: Dr. Jack Elston (PI), Maciej Stachura (PI)
  - NCAR: Dr. James Pinto (PI), Dr. Matthew Wilson (Co-PI), Dr. Arnaud Dumont (Other Personnel)

## Executive Summary
This Phase II SBIR proposal demonstrates how Black Swift Technologies' UAS platforms, integrated with NCAR's Ensemble Sensitivity Analysis (ESA) and data assimilation techniques, can improve short-term low-level wind predictions in wildland fire regions. The partnership will develop ESA-guided UAS deployment strategies, conduct observing system experiments, and demonstrate real-time wind guidance dissemination to incident commanders in Colorado and California wildfire operations.

## Technical Approach

**Core Strategy:**
- Leverage Phase I ESA technique to identify optimal locations for UAS deployment to maximize impact on low-level wind prediction skill
- Conduct Observing System Simulation Experiments (OSSE) using synthetic observations drawn from a "nature run" (WRF 40-member ensemble)
- Perform three comparison data assimilation experiments:
  - CONV: Conventional observations only
  - CONV+UAS: Conventional + ESA-targeted UAS observations
  - CONV+UAS_untargeted: Conventional + randomly-selected UAS observations (control)
- Use Ensemble Kalman Filter (EnKF) for data assimilation
- Deploy BST UAS in real field operations (Colorado and California) based on OSSE guidance
- Conduct Observing System Experiments (OSE) with actual UAS data to assess real-world impact
- Develop near-real-time workflow for ingest and dissemination of wind guidance products

**Technical Details:**
- Nature run selected from WRF 40-member ensemble based on evaluation against surface observations (10-m winds, temperature, relative humidity)
- Synthetic UAS profiles assimilated into NCAR's Model Prediction Across Scales (MPAS) model (different dynamical core than WRF to avoid "identical twin" problem)
- ESA technique correlates surface pressure, mountain-top stability, and low-level wind shear (3 hours prior) with 90th percentile ensemble mean 10-m wind gusts at target time
- Field case study: Calwood fire (Front Range, Colorado) with predicted wind gusts up to 16 m/s
- Operational evaluation on RRFS (Rapid Refresh Forecast System) ensemble DA output and HRRR (High-Resolution Rapid Refresh) model
- Integration with Tactical Assault Kit (TAK) decision support display system for wildland fire operations

## Products & Capabilities Described

**Black Swift Technologies UAS Platforms**
- What: Fleet of weather-sensing UAS capable of vertical profiling missions
- Deployment: Guided by ESA-derived sensitivity maps to collect targeted atmospheric observations during high fire-danger conditions or active wildfires
- Capability: Flexible multi-transect profiling across regions of enhanced sensitivity (demonstrated as north-south and west-east transect lines)
- Data: Atmospheric profiles (pressure, temperature, humidity, winds) for assimilation into forecast models

**NCAR Ensemble Sensitivity Analysis (ESA)**
- What: Statistical technique relating environmental variables to forecast response variables
- Enhancement: Phase II includes optimization of ESA using weighted-average contributions from multiple predictors (surface pressure, mountain-top stability, low-level wind shear)
- Application: Determines where and when UAS observations will have greatest impact on low-level wind predictions
- Output: Spatial sensitivity maps showing regions of enhanced correlation with target wind field

**Data Assimilation System**
- EnKF implementation within MPAS model for assimilating UAS observations
- Generates analysis fields and short-term wind forecasts with and without UAS data
- Enables quantification of forecast improvement from targeted UAS observations

**Operational Integration**
- Near-real-time dissemination of NCAR wind predictions to incident commanders
- Data workflow optimization for TAK system (handheld wildland fire field operations display)
- Internet protocol configuration for product ingest by operational fire management systems

## Use Cases & Applications

**Primary Application: Wildland Firefighting Decision Support**
- Short-term (12-hour) low-level wind field prediction for fire planning
- Critical weather information identified by wildland firefighting managers during Phase I
- Application areas: Colorado Front Range and California

**Specific Field Deployments:**
- Colorado: Planned deployment coordinated with Colorado Center of Excellence (CoE) for Advanced Technology Aerial Firefighting
- California: Demonstration with Department of Interior and Cal Fire on prescribed burn or wildfire event
- Real-case deployments during elevated fire danger conditions or active wildfires

**Model Systems Evaluated:**
- RRFS (Rapid Refresh Forecast System) ensemble DA system
- HRRR (High-Resolution Rapid Refresh)
- WRF (Weather Research and Forecasting model) 1-km ensemble

**Case Study:**
- Calwood fire (October 2020, Front Range Colorado): Demonstrated ESA effectiveness by identifying regions where UAS profiles would improve wind gust predictions; fire charred >10,000 acres at wildland-urban interface

## NCAR Task Breakdown & Budget

**NCAR Budget: $211,461 total (2-year Phase II)**
- Year 1: $93,077
- Year 2: $118,384

**Personnel Effort:**
- Dr. James Pinto (PI, AAP Science Deputy Director): 10% Year 1, 7.5% Year 2 (~$24,511 cumulative salary)
- Dr. Matthew Wilson (Co-PI, Postdoc Fellow I): 30% Year 1, 25% Year 2 (~$37,898 cumulative salary)
- Dr. Arnaud Dumont (Other Personnel, AAP Engineering Deputy Director): 7.5% Year 2 only (~$10,741)

**Key NCAR Tasks:**
1. Develop nature run for Calwood fire event using WRF ensemble
2. Improve ESA technique with expanded predictor set
3. Use ESA/OSSE results to guide BST field deployments (Colorado)
4. Assess real UAS observation impact via OSE with/without DA
5. Configure OSE and analyze UAS impact for California demonstration mission
6. Streamline data workflow for real-time UAS observation ingest and wind guidance dissemination to incident commanders

**Costs:**
- Salaries and fringe: $116,357
- Travel (domestic, AMS conference, Year 2): $5,333
- Computing services (CSC at $7.48/hr, 1,431 total hours): $10,704
- Indirect costs (56.7% of MTDC): $68,998
- UCAR management fee (5%): $10,069

## Key Results (from Phase I - Baseline)

**Phase I Accomplishments:**
- Implemented ESA technique to identify areas where environmental variables correlate with low-level winds
- Developed WRF 40-member ensemble for fire-prone regions
- Demonstrated spatial sensitivity maps showing where UAS profiles would provide greatest forecasting benefit
- Calwood fire case study: ESA identified peak sensitivity regions south-southwest of existing UAS profiling sites

## Notable Details

**Partnership Structure:**
- Lead: Black Swift Technologies LLC
- Co-investigators: NCAR/Research Applications Laboratory, Colorado Center of Excellence for Advanced Technology Aerial Firefighting, Cal Fire, Department of Interior
- NCAR funding administered through University Corporation for Atmospheric Research (UCAR); contact: Anna Thomas, fedaward@ucar.edu

**Key Technical Advantages:**
- Use of different dynamical core (MPAS) for DA system eliminates "identical twin" problem inherent in synthetic observation experiments
- Combination of OSSE (theoretical) and OSE (real-world) experiments to validate approach
- Direct operational relevance: results feed into incident commander decision-support tools (TAK system)
- Addresses critical gap identified by firefighting managers: 12-hour low-level wind forecast skill

**Technology Transfer Path:**
- Real-time demonstration of UAS DA impact during actual wildland fire
- Product integration with existing wildland fire operational decision support systems
- Peer-reviewed publications (NCAR team has strong publication record in UAS assimilation)

**Research Pedigree:**
- Builds on LAPSE-RATE and TORUS field campaigns (UAS profiling experiments)
- NCAR team expertise in fog prediction with weather-sensing UAS (parallel project with airports)
- Dr. Pinto: extensive boundary layer/cloud physics and NWP background; led micro-weather system development for 2018 LAPSE-RATE experiment
- Dr. Wilson: recent PhD in UAS data assimilation; TORUS storm-scale forecast experience

**Budget Justification Details:**
- 4% annual salary escalation included
- Fringe benefits: 56% (vacation, sick leave, holidays, standard benefits)
- Computing CSC rate reflects actual NCAR HPC resource usage
- 2-year effort with minimal Year 1 travel (focus on OSSE development); AMS conference presentation in Year 2