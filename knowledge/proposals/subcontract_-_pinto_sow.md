# Subcontract - Pinto SOW (Phase I NASA SBIR Wildfire)

## Document Metadata
- Type: Subcontract Statement of Work / NASA Phase I SBIR Proposal
- Client/Agency: NASA (SBIR program)
- Program/Solicitation: NASA Phase I SBIR - Wildfire Topic
- Date: Created 2023-02-28, Modified 2023-03-13, Due 2023-03-10
- BST Products/Systems Referenced: Black Swift Technologies UAS (uncrewed aircraft system); unspecified model capable of measuring atmospheric turbulence
- Key Personnel: Jack Elston (BST, last editor); James Pinto, Joe Grim, Kate Fossell (NCAR PI and key personnel)

## Executive Summary
Black Swift Technologies leads a Phase I NASA SBIR partnership with NCAR/RAL and Colorado's Center of Excellence for Advanced Technology Aerial Firefighting to assess the potential for collecting and assimilating BST UAS observations to improve low-level wind and turbulence forecasts in wildland fire regions. The pilot study will determine how UAS-derived data assimilation can enhance safety and effectiveness of mixed crewed/uncrewed aerial wildland firefighting operations in complex terrain.

## Technical Approach
- **Data Collection**: BST will deploy UAS near active wildland fires to collect observations in the lowest 1 km of the atmosphere
- **Data Assimilation**: NCAR will process observations and perform assimilation experiments using Ensemble Kalman Filter (EnKF) implemented in the Data Assimilation Research Testbed (DART), tailored for UAS observations
- **Validation Strategy**: Two-phase approach—first, offline ensemble simulations using historical wildfire events (e.g., Calwood Fire) to identify optimal sampling strategies; second, Observing System Experiments (OSEs) using actual UAS flight data from summer/fall 2023 on 1-2 high-risk fire days
- **Turbulence Measurement**: BST UAS will directly measure atmospheric turbulence for model validation in potential Phase II work

## Products & Capabilities Described

### Black Swift Technologies UAS
- **What it is**: Uncrewed aircraft system capable of collecting atmospheric observations and measuring turbulence
- **Proposed Use**: Deploy in wildland fire regions to collect targeted observations of low-level winds and turbulence; provide data for EnKF assimilation to improve wind/turbulence forecasts
- **Specifications/Performance Claims**: 
  - Can collect observations in lowest 1 km of atmosphere (critical for low-altitude flight operations)
  - Capable of direct atmospheric turbulence measurement
  - Can be deployed with flexible sampling strategies (profiling locations, cadence, spacing)

## Use Cases & Applications

### Wildland Firefighting Operations
- Supporting safe mixed crewed/uncrewed aerial assets in complex terrain during active fires
- Wind and turbulence forecasting for flight planning and airspace management in fire regions
- UAS Traffic Management (UTM)-like systems for coordinated aerial firefighting

### Specific Operational Scenarios
- High-risk fire days in foothills of Boulder County, Colorado
- Regions with complex terrain where meso-gamma-scale wind variations create hazards
- Areas requiring UAS detailed boundary mapping and hot spot identification

### Wind/Turbulence Phenomena of Interest
- Terrain-driven drainage winds and flow reversals (e.g., canyon effects in Saguache Canyon)
- Wind speed shifts and sudden increases associated with meso-gamma-scale variations
- Vertical velocity distributions and thermal intensity for airframe performance prediction
- Critical vertical velocity thresholds for flight safety

## Key Results (Historical Context)
The proposal cites prior NCAR research (Jensen et al. 2021, 2022) demonstrating:
- Targeted UAS observations in lowest 1 km of atmosphere significantly improved analysis and prediction of terrain-driven wind variations and thunderstorm initiation in complex terrain
- UAS Data Assimilation improved flow regime representation and local stability estimates
- Improved flow predictions translated to better vertical velocity and turbulence predictions (via LES)
- Example: Saguache Canyon case showed UAS DA captured flow reversal around 08:30 UTC and wind evolution through 11:30 MDT, with improvement extending 3.5+ hours into forecast period
- UAS DA reduced overly-peaked turbulence distributions and better captured broadening of turbulence distribution observed in nature

## NCAR Tasking (as subcontractor)

1. Provide guidance on UAS sampling strategies (profiling locations, cadence, spacing) based on offline high-resolution ensemble simulations for previous wildfire events
2. Process UAS observations for data assimilation using EnKF framework
3. Perform Observing System Experiments for 1-2 high-risk fire days in foothills of Boulder County
4. Assess impact of UAS DA on 3D winds and provide summary report with Phase II requirements if invited

## Notable Details

- **Partnership Structure**: BST (lead), NCAR/RAL (data assimilation and analysis), Colorado CoE for Advanced Technology Aerial Firefighting (operational liaison and deployment coordination)
- **Budget**: $33,500 for Phase I
- **Temporal Window**: UAS data collection planned for summer and fall 2023; OSEs on 1-2 high-risk fire days
- **Key Gap Addressed**: Lack of accurate low-level wind field estimates and 3-12 hour forecasts for wildland fire regions—critical for safe mixed-asset aerial operations
- **Technical Prerequisite**: Leverages several years of prior NCAR UAS DA system development; well-established EnKF framework with published validation
- **Operational Flexibility**: Study does not require actual wildfire occurrence; conditions conducive to wildfire growth sufficient for proof-of-concept validation
- **Future Direction**: Phase II would develop real-time capability and BST turbulence measurements for model validation