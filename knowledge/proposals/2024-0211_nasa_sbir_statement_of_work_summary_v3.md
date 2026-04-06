# Assimilation of Uncrewed Aircraft System Observations to Improve Low-level Wind Guidance to Support Wildland Firefighting

## Document Metadata
- Type: NASA SBIR Phase II Proposal - Statement of Work Summary
- Client/Agency: NASA (Small Business Innovation Research program)
- Program/Solicitation: NASA 2023 SBIR, Wildfire topic, Phase II
- Date: Submitted 31 January 2024 (document created 23 Jan 2024, last modified 27 Mar 2024)
- BST Products/Systems Referenced: UAS platforms (unspecified models, but implied S-series or similar)
- Key Personnel: 
  - BST: Jack Elston (PI), Maciej Stachura (PI)
  - NCAR: James Pinto (PI), Matt Wilson, Arnaud Dumont
  - Partners: Colorado Center of Excellence for Advanced Technology Aerial Firefighting, NCAR/RAL, CalFire, Department of the Interior

## Executive Summary
Black Swift Technologies will lead a partnership with NCAR and Colorado's Center of Excellence to demonstrate how targeted UAS observations can improve short-term predictions of low-level winds during wildland fires. The project will develop and optimize an Ensemble Sensitivity Analysis (ESA) technique to identify optimal UAS deployment locations, validate the approach through observing system simulation experiments, and conduct real-world field deployments in Colorado and California to demonstrate technology transfer to incident commanders.

## Technical Approach

### Ensemble Sensitivity Analysis (ESA) Technique
- Identifies geographic areas where environmental variables (surface pressure, low-level stability, wind shear) are strongly correlated with low-level winds in a region of interest
- Correlates prior atmospheric state (e.g., surface pressure 3 hours before forecast) with response variables (e.g., 90th percentile 10-m wind gusts)
- Uses 40-member ensemble forecasts to generate sensitivity fields
- Identifies regions of "enhanced sensitivity" where UAS observations would have maximum impact on wind predictions

### Observing System Simulation Experiments (OSSE)
- Uses "nature run" (digital twin atmosphere) from WRF 40-member ensemble as testbed
- Three data assimilation experiments compared:
  1. **CONV**: Conventional observations only (baseline)
  2. **CONV+UAS**: Conventional + ESA-targeted UAS observations
  3. **CONV+UAS_untargeted**: Conventional + randomly-selected UAS observations
- Synthetic UAS profiles drawn from nature run and assimilated into NCAR's Model Prediction Across Scales (MPAS) using Ensemble Kalman Filter (EnKF)
- Uses different dynamical core (MPAS vs. WRF) to avoid "identical twin" problem

### Data Assimilation & Forecasting
- Ensemble Kalman Filter (EnKF) for data assimilation
- Testing on operational models: RRFS ensemble DA system, HRRR
- Optimization of ESA with weighted average contributions from multiple predictor fields
- Real-world Observing System Experiments (OSE) using actual UAS observations

### Field Deployment Strategy
- Deploy BST UAS fleet based on ESA/OSSE guidance
- Coordinate with Colorado Center of Excellence and CalFire
- Collect observations during conditions conducive to fire growth or during actual wildland fires
- Near real-time data ingestion and wind guidance dissemination to incident commanders

## Products & Capabilities Described

### Black Swift Technologies UAS Platforms
- **What**: Uncrewed aircraft systems capable of profiling atmospheric conditions
- **Use Case**: Targeted deployment to collect vertical profiles of wind, temperature, and humidity in wildfire-threatened areas
- **Deployment Strategy**: Strategic placement based on ESA sensitivity analysis to maximize impact on forecasts
- **Key Capability**: Flexibility to fly multiple profiling missions across regions of enhanced sensitivity

### NCAR/RAL Tools & Models
- **Ensemble Sensitivity Analysis (ESA)**: Technique to identify optimal observation locations
- **Model Prediction Across Scales (MPAS)**: Dynamical core for data assimilation experiments
- **Ensemble Kalman Filter (EnKF)**: Data assimilation methodology
- **WRF Ensemble**: Used to generate nature runs for testing

## Use Cases & Applications

### Primary Use Case: Wildland Fire Prediction & Response Support
- **Mission**: Improve 12-hour low-level wind forecasts over wildfire-threatened areas
- **Key Need Identified**: Wildland firefighting managers require accurate predictions of how low-level wind fields will evolve over the next 12 hours for operational planning
- **Application Areas**: Colorado Front Range (Calwood fire example) and California
- **End Users**: Incident commanders, wildland firefighting managers, CalFire, Department of the Interior

### Specific Test Events
- **Calwood Fire (Colorado)**: Used as historical case study example; fire erupted on a day conditions were primed for explosive development, burned 10,000+ acres in wildland-urban interface
- **Colorado deployment**: Coordinated with Colorado Center of Excellence during elevated wildland fire danger
- **California deployment**: Prescribed burn or wildfire event in conjunction with NASA group, Department of Interior, and CalFire

## Key Objectives & Proposed Outcomes

1. **Develop ESA optimization**: Increase set of predictors (surface pressure, mountain-top stability, low-level wind shear) to identify optimal UAS deployment regions
2. **Validate through OSSE**: Demonstrate value of ESA-targeted UAS observations vs. random or conventional-only approaches
3. **Field demonstration**: Conduct real-world UAS deployments in Colorado and California
4. **Impact assessment**: Quantify improvement in low-level wind analysis and prediction accuracy
5. **Technology transfer**: Demonstrate near-real-time data ingestion and wind guidance dissemination to incident commanders
6. **Operational integration**: Test ESA technique on operational high-resolution ensemble forecast systems (RRFS, HRRR)

## NCAR Tasks (as contracted partner)
- Develop nature run for Calwood fire OSSE
- Improve ESA technique with expanded predictor set
- Guide BST deployments using ESA/OSSE results
- Assess impact of actual UAS observations via Observing System Experiments (OSE)
- Configure OSE data assimilation for California demonstration
- Streamline data workflow for near real-time UAS observation ingestion and incident commander product dissemination

## Notable Details

### Budget & Duration
- Proposed Phase II Budget: $211,461
- Submission Deadline: 31 January 2024

### Partnership Structure
- **BST Role**: Lead contractor, UAS platform operations, field deployment execution
- **NCAR/RAL Role**: Techniques development, data assimilation experiments, modeling, forecasting, product dissemination
- **CoE & CalFire Role**: Coordination, operational input, incident commander feedback
- **DOI & CalFire (CA)**: Participation in California demonstration

### Key Technical Advantages
- ESA technique built on Phase I NASA SBIR work (Hill et al. 2016)
- Addresses identified operational gap: 12-hour low-level wind guidance for fire planning
- OSSE methodology eliminates model-matching bias by using different dynamical cores
- Emphasis on near real-time operational integration and incident commander support

### Phase I Foundation
- ESA technique previously implemented and tested
- 40-member WRF ensemble already developed
- Operational relationships established with wildfire management stakeholders
- Calwood fire case used to validate Phase I approach

### Competitive/Unique Elements
- Targeted, adaptive UAS deployment strategy (vs. random or fixed patterns)
- Integration of ensemble forecasting with adaptive observing systems
- Demonstrated real-world application pathway through CalFire and DOI coordination
- Transfer of academic technique (ESA) to operational wildfire management