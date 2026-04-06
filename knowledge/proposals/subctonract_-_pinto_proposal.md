# Subcontract - Pinto Proposal

## Document Metadata
- Type: SBIR Phase I Proposal (with subcontract commitment letter and budget justification)
- Client/Agency: NASA (National Aeronautics and Space Administration)
- Program/Solicitation: NASA SBIR Phase I; 2023 Wildfire Topic
- Date: Submitted March 9-10, 2023
- BST Products/Systems Referenced: Uncrewed Aircraft Systems (UAS) for atmospheric data collection
- Key Personnel: Dr. Jack Elston (Black Swift Technologies), Dr. James Pinto (NCAR PI), Dr. Aaron Jensen (referenced in prior work)

## Executive Summary
This NASA SBIR Phase I proposal, led by Black Swift Technologies in partnership with the National Center for Atmospheric Research (NCAR) and Colorado's Center of Excellence for Advanced Technology Aerial Firefighting, aims to assess the potential for collecting and assimilating UAS observations to improve representation of low-level winds and turbulence near active wildland fires. The work will use data assimilation techniques (Ensemble Kalman Filter) to demonstrate how targeted UAS observations can enhance wind and turbulence forecasts critical to safe mixed crewed/uncrewed aircraft operations during wildfire suppression.

## Technical Approach

**Data Collection & Observation Strategy:**
- BST will conduct UAS flights in summer and fall of 2023, collecting atmospheric observations near wildland fires
- Flights will occur either outside Temporary Flight Restriction (TFR) areas during active fires or on high-risk wind pattern days in Colorado foothills
- Target observation areas: lowest 1 km of atmosphere with focus on profiling locations, cadence, and spacing

**Data Assimilation Framework:**
- NCAR will employ Ensemble Kalman Filter (EnKF) data assimilation using the Data Assimilation Research Testbed (DART)
- Processing pipeline: UAS observations → quality assessment → assimilation into EnKF system
- Observing System Experiments (OSEs) to quantify impact of UAS data on wind/turbulence analysis and prediction

**Numerical Modeling:**
- Weather Research and Forecasting (WRF) model with Large-Eddy Simulation (LES) nesting capability
- High-resolution ensemble simulations for pre-deployment planning
- Ensemble Sensitivity Analysis (ESA) to identify areas where UAS observations would have greatest forecast impact
- WRF-LES capable of 100 m grid spacing for detailed turbulence representation

**Prior Validation Data:**
- Prior work (Jensen et al. 2021, 2022) demonstrated capability using coordinated UAS fleets
- Case study: Saguache Canyon, July 19, 2018 showed UAS DA improved wind reversal prediction and turbulence intensity forecasting
- Study showed improved forecast skill extending 3.5+ hours into prediction period

## Products & Capabilities Described

**Black Swift Technologies:**
- Operates uncrewed aircraft systems capable of collecting targeted atmospheric observations
- Coordinates with Center of Excellence for Advanced Technology Aerial Firefighting for deployment logistics
- Provides quality-controlled UAS observation data to NCAR

**NCAR's UAS Data Assimilation System:**
- Ensemble-based DA capability developed over prior 2+ years
- Integration with WRF/LES for high-resolution wind and turbulence analysis
- EnKF framework implementation via DART software
- Real-time WRF-LES simulation capability (demonstrated during 2018 LAPSE-RATE field campaign)

## Use Cases & Applications

**Primary Application:** Wildland fire fighting decision support through improved wind and turbulence guidance

**Specific Scenarios:**
- Prediction of sudden wind shifts critical to flight planning (demonstrated 8:30 UTC wind reversal case)
- Detection of meso-gamma-scale wind variations in complex terrain near fire perimeters
- Forecast of atmospheric stability and turbulence intensity affecting aircraft energy consumption and safety
- Flight planning for mapping fire extent and hot spots
- Safety guidance for both large crewed aircraft and smaller UAS in regions with strong updrafts/downdrafts
- Coordination of mixed crewed and uncrewed aircraft operations in constrained airspace near fires

**Geographic Focus:** Colorado foothills, potential deployment in Boulder County or similar complex terrain areas

## NCAR Tasking & Timeline

**Month 1-2:** Provide UAS sampling strategy guidance based on offline ensemble simulations and ESA studies for previous wildland fires (e.g., Calwood Fire)

**Month 3-4:** Process UAS observations for data assimilation using EnKF framework

**Month 4-5:** Perform Observing System Experiments (OSEs) for 1-2 high-risk fire days in Boulder County foothills

**Month 5-6:** Analyze impact of UAS DA on 3D winds; prepare summary report describing tasks needed for Phase II real-time capability development

## Budget & Personnel

**Total NCAR Subcontract Value:** $33,580 (Firm Fixed Price)
**Performance Period:** July 1, 2023 – December 31, 2023

**Staffing:**
- Project Scientist III (Dr. James Pinto): 5% effort (~$151,869 annual salary), project oversight and leadership
- Associate Scientist IV: 6% effort (~$120,360 annual salary), DA system configuration/testing on supercomputer
- Project Scientist I: 13% effort (~$110,266 annual salary), UAS observation analysis and turbulence prediction impact assessment

**Budget Breakdown:**
- Salaries & Benefits: $19,364
- Computing Service Center costs: $1,599 (RAL $7.75/hr, MMM $6.50/hr)
- Indirect Costs (56.90% NCAR rate): $11,018
- UCAR Management Fee (5%): $1,599

**Key Details:**
- 54.5% fringe benefits rate applied (vacation, sick leave, holidays, standard benefits)
- 4% salary escalation included annually
- Costs subject to NSF cognizant audit agency approval
- NSF negotiated indirect cost rate agreement dated December 12, 2022

## Key Research Results/Prior Demonstrations

**Case Study Validation (Saguache Canyon, CO - July 19, 2018):**

Wind Prediction Improvement:
- Without UAS DA: Winds remained northwesterly throughout morning (incorrect)
- With UAS DA: Captured abrupt wind transition to southeasterly at ~8:30 UTC (correct)
- Improved wind speed evolution prediction from 08:00-11:30 UTC with accuracy extending 3.5+ hours into forecast period

Turbulence Representation:
- UAS DA improved vertical velocity distribution (proxy for turbulence) amplitude and spread
- Better captured broadening of vertical velocity distribution during late morning hours
- WRF-LES nested within UAS DA runs showed enhanced skill in predicting turbulence intensity timing and intensity changes

**Published Validation:**
- Jensen et al. (2021): "Assimilation of a Coordinated Fleet of Uncrewed Aircraft System Observations in Complex Terrain: EnKF System Design and Preliminary Assessment" - *Mon. Wea. Rev.* 149, 1459–1480
- Jensen et al. (2022): "Assimilation of a Coordinated Fleet of Uncrewed Aircraft System Observations in Complex Terrain: Observing System Experiments" - *Mon. Wea. Rev.* 150, 2737-2763
- Pinto et al. (2021): Real-time WRF-LES operations during 2018 LAPSE-RATE field campaign, *Earth System Science Data*, 13, 697-711

## Notable Details

**Partnership Structure:**
- Black Swift Technologies (lead contractor)
- NCAR/Research Applications Laboratory (data assimilation and modeling expertise)
- University Corporation for Atmospheric Research (UCAR) administers subcontract through UEI# YEZEE8W5JKA3
- Colorado Center of Excellence for Advanced Technology Aerial Firefighting (field deployment support)

**Prior Experience:**
- NCAR team led micro-weather prediction system development for 2018 LAPSE-RATE field campaign (San Luis Valley, CO)
- Currently leading fog prediction improvement study using weather-sensing UAS at large airport
- Dr. Pinto serves as Science Deputy for NCAR's Aviation Applications Program (4 years)

**Competitive Advantages Addressed:**
- Addresses critical gap in UTM (UAS Traffic Management) systems: lack of wind/turbulence observations in fire regions
- Targets meso-gamma-scale phenomena (sub-kilometer) typically missed by operational networks
- Demonstrates value of targeted adaptive sampling in complex terrain
- Provides actionable guidance for flight planning in hazardous environments

**Key Client Requirements:**
- Safe operation of mixed crewed/uncrewed aircraft during wildland fire suppression
- Identification of hazardous wind and turbulence conditions
- Real-time capability development pathway for Phase II (if awarded)
- Demonstration of forecast improvement metrics applicable to operational decision support