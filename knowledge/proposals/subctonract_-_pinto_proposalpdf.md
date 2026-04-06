# Subcontract - Pinto Proposal (NASA SBIR Phase I: Wildfire UAS Data Assimilation)

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal with NCAR subcontract commitment letter and budget justification
- **Client/Agency:** NASA (via NSF SBIR program)
- **Program/Solicitation:** NASA SBIR Phase I; NCAR Proposal #2023-0278
- **Date:** March 8, 2023 (commitment letter); June 9, 2023 (document date)
- **BST Products/Systems Referenced:** Uncrewed Aircraft Systems (UAS) for atmospheric observations
- **Key Personnel:** 
  - Dr. Jack Elston (Black Swift Technologies LLC, Principal contact)
  - Dr. James Pinto (NCAR Principal Investigator)
  - Nathan Aderhold (NCAR Budget Analyst)

## Executive Summary
Black Swift Technologies is leading a NASA SBIR Phase I project in partnership with NCAR and Colorado's Center of Excellence for Advanced Technology Aerial Firefighting to develop and demonstrate UAS-based data assimilation capabilities for improving low-level wind and turbulence forecasts in wildland fire regions. The project involves collecting targeted UAS observations near active wildfires, assimilating them using NCAR's Ensemble Kalman Filter (EnKF) system, and demonstrating how improved wind/turbulence predictions can enhance the safety and efficiency of mixed crewed-uncrewed aerial firefighting operations.

## Technical Approach

### Overall Strategy
- **Goal:** Conduct a pilot study assessing potential for collecting and assimilating targeted UAS observations to improve low-level winds and turbulence representation in wildfire regions
- **Timeline:** 6-month Phase I effort (July 1 – December 31, 2023)
- **Partnership Structure:** 
  - BST leads overall effort and coordinates UAS deployments
  - NCAR/RAL (Research Applications Laboratory) performs data assimilation experiments
  - Colorado Center of Excellence provides operational firefighting context and deployment guidance

### Data Assimilation System
- **Framework:** Ensemble Kalman Filter (EnKF) using NCAR's Data Assimilation Research Testbed (DART)
- **Model Integration:** Weather Research and Forecasting (WRF) model with Large-Eddy Simulation (LES) capability at 100 m grid spacing for high-resolution turbulence prediction
- **Ensemble Sensitivity Analysis (ESA):** Used to identify areas of greatest uncertainty in wind forecasts and inform UAS deployment strategies
- **Assimilation Technique:** Observing System Experiments (OSEs) using actual or high-risk fire day observations from summer/fall 2023

### Observation Collection
- UAS flights to be conducted:
  - Outside Temporary Flight Restriction (TFR) areas during active fires, OR
  - On days with strong/complex wind flow patterns in Colorado foothills
- Target: 1-2 actual wildfire days or high-risk fire days in Boulder County foothills
- Observation focus: Low-level (lowest 1 km of atmosphere) winds, temperature, pressure profiles
- Sampling strategy to be guided by ensemble predictions and ESA from previous fire events (e.g., Calwood Fire)

## Products & Capabilities Described

### BST Role & Capabilities
- **UAS Operations:** Deployment, flight planning, and real-time data collection in complex terrain near wildfires
- **Coordination:** Liaison between operational firefighting community and research team
- **Data Provision:** Quality-controlled UAS observation data for NCAR assimilation

### NCAR Systems & Capabilities

**Ensemble Kalman Filter (EnKF) Data Assimilation System:**
- Developed over prior years with demonstrated success in complex terrain applications
- Processes observations for DA using EnKF framework
- Performs ensemble-based sensitivity analysis to guide sampling strategies

**WRF-LES Modeling:**
- High-resolution nested simulations (outer domain 1 km grid spacing; inner LES domain 100 m)
- Integrated with data assimilation system
- Predicts both horizontal winds and vertical velocities (turbulence proxy)
- 3.5+ hour forecast skill demonstrated in prior studies

**Prior Research Validation:**
- Reference to Jensen et al. (2021, 2022) demonstrating coordinated UAS fleet observations improved wind and turbulence analysis/prediction in complex terrain
- Case study: San Luis Valley/Saguache Canyon (July 19, 2018) showing UAS DA improved:
  - Detection of abrupt wind reversals/flow transitions
  - Wind speed evolution prediction over 3.5+ hour forecast window
  - Turbulence intensity predictions via vertical velocity distributions

## Use Cases & Applications

### Primary Application: Wildland Firefighting Decision Support
- **Mission Type:** Mixed crewed-uncrewed aerial asset operations during active wildland fires
- **Key Hazard Identification:** 
  - Sudden wind shifts and speed ramps (dangerous for flight operations)
  - Terrain-driven wind flows and drainage winds
  - Thunderstorm outflows
  - Turbulence/updraft/downdraft intensities

### Operational Scenarios
1. **Flight Planning for UAS Mapping:** Terrain-relative wind/turbulence guidance for fire extent and hot-spot mapping missions requiring straight-level transects
2. **Crewed Aircraft Safety:** Identification of stronger updraft/downdraft regimes that pose structural/handling risks
3. **Ground Operations:** Wind and turbulence data for coordinating on-ground firefighting asset deployment in complex terrain
4. **UTM (UAS Traffic Management):** Incorporation of wind/turbulence data into airspace management systems for simultaneous crewed/uncrewed operations

### Geographic Context
- Focus region: Colorado foothills/complex terrain (demonstrated capability in San Luis Valley, applicable to Boulder County and similar environments)
- Applicability: Areas of complex terrain with limited existing meteorological observations

## NCAR Task Breakdown (Phase I)

**Months 1-2:** 
- Guidance on UAS sampling strategies (profiling locations, cadence, spacing)
- Offline high-resolution ensemble simulations for previous wildfire events
- Ensemble sensitivity analysis studies (e.g., Calwood Fire)

**Months 3-4:**
- Process UAS observations for data assimilation
- Data quality assessments

**Months 4-5:**
- Observing System Experiments (OSEs) for 1-2 high-risk fire days in Boulder County foothills
- Assess added skill from UAS measurements

**Months 5-6:**
- Analyze impact of UAS DA on 3D winds and turbulence
- Summary report including requirements for Phase II real-time operational capability

## Budget & Resource Allocation

### NCAR Subcontract Total: **$33,580** (Firm Fixed Price)
**Period of Performance:** July 1 – December 31, 2023 (6 months)

### Personnel (Total: $19,364 direct labor)
- **Project Scientist III (Dr. James Pinto, PI):** 5% effort (~$7,594 salary + benefits)
  - Role: Project oversight, budgeting, personnel management, reporting, consulting with BST, final report leadership
  
- **Associate Scientist IV:** 6% effort (~$7,222 salary + benefits)
  - Role: Configure, test, run UAS DA experiments on NCAR supercomputer; system installation on new computing platform (summer 2023)
  
- **Project Scientist I:** 13% effort (~$14,335 salary + benefits)
  - Role: Analyze UAS observations and model output; determine DA impact on wind/turbulence predictions; develop figures and report text

- **Fringe Benefits:** 54.50% of direct salaries ($6,830)

### Computing Services
- RAL Computing Service Center: $1,248 @ $7.75/hr (271 hours)
- MMM Computing Service Center: $351 @ $6.50/hr (54 hours)
- **Subtotal Computing:** $1,599

### Indirect Costs
- NCAR G&A (Onsite): 56.90% of MTDC = $11,018

### Management Fee
- UCAR Management Fee: 5.00% of (MTDC + Applied Indirect) = $1,599

### Excluded Costs
- No equipment costs
- No travel budgeted (local operations in Colorado)
- No participant/trainee support

## Key Results & Prior Research Foundation

### Published Prior Studies Demonstrating Capability
**Jensen et al. (2021)** - *Mon. Wea. Rev.*, 149, 1459–1480
- Title: "Assimilation of a Coordinated Fleet of Uncrewed Aircraft System Observations in Complex Terrain: EnKF System Design and Preliminary Assessment"
- Findings: Coordinated UAS observations significantly improved analysis/prediction of meso-gamma-scale winds and thunderstorm outflows in complex terrain

**Jensen et al. (2022)** - *Mon. Wea. Rev.*, 150, 2737-2763
- Title: "Assimilation of a Coordinated Fleet of Uncrewed Aircraft System Observations in Complex Terrain: Observing System Experiments"
- Findings: OSE demonstrations showing positive impact of UAS observations on wind and flow field predictions

**Pinto et al. (2021)** - *Earth System Science Data*, 13, 697-711
- Real-time WRF-LES simulations during 2018 LAPSE-RATE field experiment
- Demonstrated operational feasibility of real-time high-resolution modeling

### Demonstrated Capabilities from Case Study (San Luis Valley, July 19, 2018)
- **Wind Reversal Prediction:** UAS DA captured abrupt flow transition from NW to SE drainage winds that NoDA simulation missed
- **Forecast Skill:** Improved wind speed prediction extending 3.5+ hours into forecast period
- **Turbulence Prediction:** Enhanced vertical velocity distribution predictions using LES nested in DA system, capturing both amplitude and spreading of turbulent activity
- **Application:** These improvements directly support flight planning for operations requiring straight-level flight paths in terrain-complex environments

## Notable Details

### Partnership Structure
- **Lead:** Black Swift Technologies (SBIR Phase I prime contractor)
- **Technical Partner:** NCAR/Research Applications Laboratory (subcontractor, $33,580)
- **Operational Partner:** Colorado Center of Excellence for Advanced Technology Aerial Firefighting (provides deployment context, operational requirements, firefighting decision support expertise)
- **Institutional Support:** University Corporation for Atmospheric Research (UCAR) administers NCAR subcontract

### Competitive Advantages & Unique Capabilities
1. **Existing EnKF/DA System:** NCAR has operational UAS data assimilation framework already demonstrated in publications
2. **High-Resolution Modeling:** Capability for 100 m grid-spacing LES with ensemble predictions
3. **Complex Terrain Expertise:** Proven success in San Luis Valley studies; directly applicable to Colorado wildfire regions
4. **Operational Integration:** Partnership with firefighting operations center provides real-world context and validation
5. **Fleet Coordination Experience:** Prior work with coordinated multi-UAS observations (implicit in "fleet" references)

### Client Requirements Addressed
- **NASA SBIR Objective:** Demonstrate UAS observation value for improving operational decision support in wildland firefighting
- **Safety Requirement:** Identify hazardous wind/turbulence conditions for mixed crewed-uncrewed aerial operations
- **Operational Feasibility:** Pilot study using actual or representative fire day conditions; scalability to Phase II real-time capability
- **Decision Support Gap:** Fill lack of low-level wind/turbulence observations in traditional UTM system architectures

### Contingencies & Constraints
- NCAR participation contingent on "mutually agreed upon terms and conditions"
- Task timeline dependent on when BST performs flights and when quality-controlled data is provided
- Tasks to be "undertaken following mutually agreed upon approach(es)" and carried out "as resources allow"
- Budget not to exceed $33,580 total allocation to NCAR

### Administrative Details
- **NCAR Entity:** National Center for Atmospheric Research (part of UCAR)
- **UCAR UEI:** YEZEE8W5JKA3
- **Cognizant Agency:** National Science Foundation (NSF)
- **Approved Rates Referenced:** FY 2023 Provisional rates for G&A (56.90% onsite), Fringe Benefits (54.50%), Computing Services
- **Contacts:**
  - Anna Thomas, Manager UCAR Contracts: fedaward@ucar.edu, (303) 497-2005
  - Dr. James P