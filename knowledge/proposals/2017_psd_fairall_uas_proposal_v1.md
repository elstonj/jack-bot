# 2017 PSD_Fairall_UAS_Proposal_V1

## Document Metadata
- Type: Project proposal / funding application
- Client/Agency: NOAA Physical Sciences Division (PSD); submitted to NOAA UAS office
- Program/Solicitation: NOAA UAS evaluation program (RFP objectives listed)
- Date: April 3, 2017 (created); modified September 1, 2021
- BST Products/Systems Referenced: Multi-Hole Pressure (MHP) probe; BST control systems
- Key Personnel: Dr. Jack Elston (Black Swift Technologies, CEO); Dr. Christopher Fairall (PI, NOAA PSD); Dr. Gijs de Boer (Co-I, CIRES)

## Executive Summary
This proposal seeks to develop, test, and deploy "miniFlux," an integrated sensor package for small unmanned aerial systems (sUAS) capable of measuring turbulent fluxes of heat, moisture, and momentum—critical measurements currently unavailable to NOAA. The project combines sensors from NCAR, University of Colorado, and Black Swift Technologies into a lightweight, operationally-deployable package to advance technology readiness from TRL 4/5 to TRL 7/8 over 16 months (May 2017–September 2018).

## Technical Approach

### System Design
miniFlux integrates five core sensor components:
1. **NCAR AVAPS dropsonde sensor suite** – thermodynamic measurements (pressure, temperature, humidity)
2. **CU DataHawk fine-wire temperature sensor** – fast thermodynamic response
3. **VectorNav VN-300 Inertial Navigation System (INS)** – high-precision attitude and motion tracking (~$3,200)
4. **Black Swift Technologies Multi-Hole Pressure (MHP) probe** – three-component wind estimation
5. **Thermopile surface temperature sensor** – surface skin temperature

### Development Phases
1. **Development & Integration (RL2→RL3):** Electronic design, sensor interfacing, power management, housing design; data acquisition system with 10–100 Hz logging capability; robust to -40 to +50°C operation; electromagnetic interference mitigation.

2. **Testing & Evaluation (RL3→RL6):** 
   - Wind tunnel calibration of BST MHP probe (University of Colorado wind tunnel)
   - Laboratory calibration of thermopile and fine-wire sensors (NCAR environmental chambers)
   - Surface-based field testing against tower-mounted instrumentation (sonic anemometer, open-path water vapor sensor, slow PTH, IRT)
   - Airborne testing on CU Pilatus aircraft in Colorado across varied environmental conditions

3. **Demonstration (RL6→RL8):**
   - Deployment on NOAA-operated UAS (targeting Puma; deployment contingent on available platforms and missions)
   - Operational campaign flights in field environments (proposed locations: DOE ARM SGP facility in Oklahoma, Oliktok Point, Alaska)
   - ~30 flight hours total (distributed across CU and NOAA aircraft) to generate sufficient statistics

### Data Management
- Embedded microcomputer system for coordinated sensor polling and data logging
- Data ingest and processing to NetCDF format with initial quality control
- High-frequency logging (10–100 Hz) synchronized between MHP and INS units

## Products & Capabilities Described

### Black Swift Technologies Multi-Hole Pressure (MHP) Probe
- **Current State:** RL 5 (prototype developed and flight-tested on BST aircraft)
- **Application:** Three-component wind velocity estimation from differential pressure measurements
- **Proposed Development:** Wind tunnel calibration to establish response curves across platform flight speed ranges and orientations; generation of calibration constants for field deployment
- **Advantage:** Compact, lightweight alternative to traditional sonic anemometers; suitable for small UAS with limited payload capacity

### Integrated miniFlux System
- **Scale:** Similar footprint to CU Pilatus wing pod (aircraft wingspan 3.2 m)
- **Deployment Flexibility:** Designed for deployment across multiple sUAS platforms (Puma, Manta, ScanEagle, Latitude HQ-60, Coyote); modular sensors allow reconfiguration for aircraft-launched systems
- **Performance Claims:** System will meet NOAA Program Observation Requirements Document (PORD) and OAR Observational User Requirements Document (OURD) standards for:
  - Vertical profiles of temperature, dew point, humidity, pressure, wind speed/direction
  - Surface temperature (land and sea)
  - Turbulent flux derivation (heat, moisture, momentum)

## Use Cases & Applications

1. **Arctic Operations:** Low-altitude sampling of surface layer over evolving sea ice where atmospheric stratification limits manned aircraft; boundary layer characterization for climate modeling
2. **Hurricane Monitoring:** Integration potential with P-3-launched Coyote UAS for evaluating turbulent surface fluxes in storm environments inaccessible to manned aircraft
3. **Atmospheric Rivers:** Sampling difficult-to-reach precipitation systems
4. **Model Evaluation:** Spatial flux variability assessment (model grid scales: kilometers) without deploying hundreds of towers or ships
5. **Routine Meteorological Support:** "Deployments of opportunity" on existing UAS missions to provide critical atmospheric data

### Observing Requirements Addressed
- **PORD (2013):** Temperature, dew point, humidity, pressure, wind profiles (PSD, AOML, ARL, NSSL, PMEL); surface temperature (PSD, AOML, ARL, PMEL)
- **OURD Supplemental (2016):** 
  - Climate (CLI) goal: air temperature profiles, pressure profiles, land skin temperature, sea surface temperature, water vapor, wind profiles
  - Weather-Ready Nation (WRN) goal: boundary layer temperature, land surface temperature, boundary layer wind profiles
- **NWS Requirements:** Storm Prediction Center, National Hurricane Center, Aviation Weather Program, Marine Weather Program, Surface Weather Program

## Project Milestones & Timeline

| Milestone | Target Date | Readiness Level Advance |
|-----------|------------|----------------------|
| Prototype system design, sensor integration, data acquisition system functional | 7/15/2017 | RL2→RL3 |
| Initial airborne testing on CU aircraft | 8/30/2017 | — |
| Wind tunnel calibration of MHP, lab evaluation of sensors | 10/1/2017 | RL3→RL4 |
| Field surface-based testing vs. traditional sensors | 11/1/2017 | RL4→RL5 |
| Continuous airborne testing on CU aircraft (varied conditions) | 3/31/2018 | RL5→RL6 |
| Deployment on NOAA aircraft in operational setting | 6/30/2018 | RL6→RL7 |
| Final system deployment on NOAA aircraft | 9/30/2018 | RL7→RL8 |

## Key Technical Team & Roles

- **Dr. Jack Elston (Black Swift Technologies):** Integration of BST MHP probe into miniFlux; in-kind contribution
- **Dr. Gijs de Boer (CIRES):** Technical lead; oversees testing protocols, flight coordination, deployment planning
- **Mr. David Costa & Mr. Paul Johnston (CIRES):** Data acquisition system development; overall integration and testing
- **Dr. Dale Lawrence & Dr. Brian Argrow (CU-Boulder):** Guidance on fast temperature/wind sensing; local test flight coordination (in-kind CU support)
- **Dr. Holger Vömel & Mr. Terry Hock (NCAR):** Thermodynamic sensor integration, shielding, data logging, housing design (in-kind NCAR support)
- **Mr. Emeil Hall & Dr. Allison McComiskey (CIRES/NOAA GMD):** Thermopile sensor calibration protocol development
- **Dr. Christopher Fairall (NOAA PSD, PI):** Overall project coordination; expert in turbulent flux measurement (in-kind PSD support)

## Comparative Technology Assessment

### Advantages of miniFlux/UAS Approach vs. Alternatives
- **vs. Tower-based systems:** Cannot evaluate spatial variability of fluxes; miniFlux enables sampling across different surface types in single flight
- **vs. Ship-based observations:** Eliminates large research vessel expense; direct access to open ocean with compact platform
- **vs. Manned aircraft:** Can fly lower in stratified environments (Arctic, storms); safer for remote/dangerous operations; more flexible flight patterns
- **vs. Commercial sensors:** Individual components available commercially, but integration fills critical gap—ensures co-location of wind/thermodynamic measurements, proper physical/logging alignment of INS and MHP probe

### Technology Maturity
- **Individual components:** All at RL 9 (NCAR AVAPS operationally deployed on NASA Global Hawk; VectorNav VN-300 widely used by industry; fine-wire/thermopile sensors deployed on thousands of DataHawk flights)
- **Integrated system:** Currently RL 2; project advances to RL 8
- **BST MHP probe:** Currently RL 5 (prototype flown on BST aircraft); advancement needed through calibration and integration validation

## Notable Details

### Budget & Duration
- **Total Budget:** $255k over two fiscal years (FY17–FY18)
- **Period of Performance:** May 1, 2017 – September 30, 2018 (16 months)
- **Most Expensive Component:** VectorNav VN-300 INS (~$3,200); overall equipment costs modest; largest risk is underestimation of labor/travel costs

### Project Management
- Bi-weekly team meetings (broader group); more frequent smaller subgroup discussions as needed
- Broad team with overlapping expertise mitigates personnel departure risk
- **Redundancy:** Budgeted for three complete miniFlux packages to allow for damage during testing without project impact
- **Platform Access:** CU team manages airspace access via existing Certificates of Authorization (COAs) and blanket low-altitude COA; NOAA AOC manages flight permissions for NOAA UAS

### Field Testing Locations
- **Initial testing:** Colorado (CU aircraft)
- **Primary evaluation site:** NOAA ARL proposed UAS sensor evaluation center (contingency: DOE ARM SGP site in Oklahoma)
- **Operational deployment:** Proposed sites include ARM SGP and Oliktok Point, Alaska

### Risk Mitigation
- **Platform failure:** Well-tested platforms (T-Twistor, Talon) within manual pilot control range; three complete systems budgeted
- **Equipment procurement delays:** Equipment generally inexpensive with well-understood pricing; rated "remote" likelihood
- **ARL test site unavailability:** Fallback to ARM SGP (de Boer has extensive ARM background)
- **Cost overruns:** Rated as "remote" likelihood; potential "notable" impact if salary/travel support inadequate

### Expected Deliverables
1. Written project plan
2. NEPA (National Environmental Policy Act) analysis
3. Testing technical report (post-lab/initial field testing)
4. Operator manual with calibration/operational procedures
5. Testing and evaluation datasets (public release)
6. Monthly project status reports
7. Annual progress reports
8. Final project report

## Science Traceability
- **NOAA OAR Mission:** "Conduct research to understand and predict the Earth system" and "develop technology to improve NOAA science"
- **Key Science Gap:** Turbulent exchange of energy (heat, moisture, momentum) poorly constrained in models; requires detailed measurements across varied environments
- **Operational Impact:** Addresses requirements across multiple NOAA line offices (AOML, ARL, NSSL, PMEL) and NWS programs; enables assessment of surface fluxes in previously inaccessible regions (Arctic, hurricanes)

---

## Document Status Notes
- Document contains several incomplete sections marked with bracketed editorial notes (e.g., "[h]," "[i]," "[m]")—appears to be a working draft with placeholders for budget breakdown and personnel expertise details
- Risk matrix table (Table 2) identifies 6 numbered risks; narrative mitigation strategies provided for each
- Schedule chart (Table 1) displays FY17 tasks (blue) and FY18 tasks (orange) across 16-month timeline
- Readiness Level Worksheet included showing component-level RL advancement from RL 2/5/6 (start) to RL 5/7/8 (end) across platforms, payloads, observing systems, and observing strategies