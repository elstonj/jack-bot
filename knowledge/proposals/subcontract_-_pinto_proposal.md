# Subcontract - Pinto Proposal

## Document Metadata
- Type: NASA Phase I SBIR Proposal with NCAR Subcontract Letter of Commitment
- Client/Agency: NASA (via NSF sponsorship)
- Program/Solicitation: NASA Phase I SBIR; NCAR Proposal #2023-0278
- Date: March 8-13, 2023 (submitted March 10, 2023)
- BST Products/Systems Referenced: Uncrewed Aircraft Systems (UAS)
- Key Personnel: Dr. Jack Elston (BST); Dr. James Pinto (NCAR PI); Nathan Aderhold (NCAR Budget Analyst II)

## Executive Summary
This proposal describes a Phase I SBIR project to assess the potential for collecting and assimilating targeted UAS observations to improve representation of low-level winds and turbulence in regions affected by active wildland fires. Black Swift Technologies will lead a partnership with Colorado's Center of Excellence for Advanced Technology Aerial Firefighting and NCAR/RAL to collect UAS observations near wildfires and conduct data assimilation experiments to enhance decision support for mixed crewed/uncrewed aerial firefighting operations.

## Technical Approach

**Overall Strategy:**
- Collect targeted UAS observations in the lowest 1 km of the atmosphere near wildland fires
- Perform data quality assessments at NCAR
- Conduct data assimilation experiments using Ensemble Kalman Filter (EnKF) methodology via the Data Assimilation Research Testbed (DART)
- Execute Observing System Experiments (OSEs) to assess skill improvements
- Develop wind and turbulence prediction products for firefighting operations

**Key Technical Elements:**
- Use ensemble predictions to guide UAS deployment strategies
- Perform ensemble sensitivity analyses (ESA) on two previous wildland fire events to identify areas of greatest uncertainty in wind forecasts
- Conduct data denial experiments (OSEs) on 1-2 actual or high-risk fire days during summer/fall 2023
- Employ WRF (Weather Research and Forecasting) model with LES (Large Eddy Simulation) nesting
- Focus on terrain-driven winds, thunderstorm outflows, and thunderstorm initiation detection
- Assess 3D wind field improvements and turbulence intensity prediction

**Timeline (6 months):**
- Months 1-2: Provide UAS sampling strategy guidance (profiling locations, cadence, spacing)
- Months 3-4: Process UAS observations for data assimilation
- Months 4-5: Perform Observing System Experiments
- Months 5-6: Analyze UAS DA impact on 3D winds and prepare summary report

## Products & Capabilities Described

### Black Swift Technologies - UAS
- **What it is:** Uncrewed aircraft systems capable of collecting atmospheric observations in complex terrain
- **Proposed use:** Deploy in vicinity of active wildfires or in high-risk foothills areas to collect wind/turbulence data; operate either outside Temporary Flight Restrictions (TFRs) or on days with complex wind patterns
- **Context:** Part of mixed (crewed and uncrewed) aerial assets for wildfire firefighting operations

### NCAR Systems
- **Data Assimilation Research Testbed (DART):** Framework for EnKF data assimilation
- **WRF-LES modeling:** High-resolution atmospheric simulation with nested scales
- **UAS Data Assimilation System:** Developed over prior years; capable of assimilating low-altitude UAS observations
- **Ensemble prediction and sensitivity analysis tools:** For deployment planning

## Use Cases & Applications

**Primary Application:**
- Wildland fire monitoring and management in complex terrain
- Decision support for safe operation of mixed crewed/uncrewed aerial firefighting assets
- Airspace management for multiple aerial assets during active wildfires

**Specific Scenarios Described:**
1. **Low-level wind prediction:** Capture terrain-driven wind reversals and sudden wind shifts critical to flight planning
2. **Turbulence forecasting:** Predict updrafts/downdrafts affecting flight safety and efficiency
3. **Site examples:** Saguache Canyon (San Luis Valley, Colorado); Boulder County foothills

**Operational Benefits:**
- Improved accuracy of wind and turbulence guidance near wildfires
- Enhanced efficiency and safety of firefighting flight operations
- Better detection of sub-optimal or hazardous flight conditions
- Real-time capability development for Phase II

## Key Results (from Prior NCAR Work Referenced)

**Evidence of Concept Feasibility:**
- Prior NCAR studies (Jensen et al. 2021, 2022) demonstrated that UAS observations in lowest 1 km of atmosphere significantly improved analysis and prediction of:
  - Meso-gamma-scale terrain-driven wind variations
  - Thunderstorm outflows and initiation
  - Low-altitude flow regimes and atmospheric stability

**Saguache Canyon Case Study (July 19, 2018):**
- UAS DA cycling 06:00-08:00 UTC showed improved wind prediction performance
- With UAS assimilation: WRF correctly captured flow reversal from northwesterly to southeasterly winds around 08:30 UTC
- Without UAS assimilation (NoDA): Winds remained northwesterly throughout, missing critical reversal
- Improved wind predictions persisted 3.5+ hours into forecast period
- Vertical velocity distribution (turbulence proxy) better captured amplitude and spread of observed values with UAS DA

## Notable Details

**Partnership Structure:**
- **Lead:** Black Swift Technologies LLC (Boulder, CO)
- **Partners:** 
  - NCAR/RAL (Research Applications Laboratory) at University Corporation for Atmospheric Research (UCAR)
  - Colorado's Center of Excellence for Advanced Technology Aerial Firefighting
- **BST Role:** Collect UAS observations and coordinate with CoE on critical wind criteria for firefighting
- **NCAR Role:** Data quality assessment, data assimilation experiments, guidance on sampling strategies

**Budget (NCAR Subcontract):**
- Total requested: $33,580
- Period: July 1, 2023 - December 31, 2023 (6 months)
- Personnel: Project Scientist III (5% effort); Associate Scientist IV (6% effort); Project Scientist I (13% effort)
- NCAR Indirect Cost Rate (FY 2023): 56.9%
- UCAR Management Fee: 5% of MTDC

**Principal Investigator Credentials:**
Dr. James Pinto (NCAR/RAL) - Science Deputy of Aviation Applications Program with:
- BS Agronomy/Meteorology (Cornell, 1990)
- MS Meteorology (Penn State, 1993)
- PhD Astrophysical, Planetary & Atmospheric Science (University of Colorado, 1997)
- Experience in boundary layer/cloud physics, NWP, aviation hazard products, UAS atmospheric studies
- Prior leadership on micro-weather prediction for UAS during 2018 LAPSE-RATE field experiment

**Competitive Advantage/Innovation:**
- Addresses critical gap in UTS (UAS Traffic Management) systems: lack of observations of winds/turbulence in fire regions
- Combines BST's UAS capability with NCAR's established UAS data assimilation system
- Focuses on lowest 1 km of atmosphere where observations are typically absent but critical for flight operations
- Demonstrates real-world applicability through actual fire season deployments vs. simulation only

**Phase II Pathway:**
- Phase I will identify tasks required to develop real-time capability for Phase II
- Contingency: OSEs can be performed on high-risk fire days if actual deployment opportunity unavailable