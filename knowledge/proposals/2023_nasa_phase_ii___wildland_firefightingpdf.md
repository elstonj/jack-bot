# UAS Data Assimilation for Improved Wildland Firefighting Decision Support

## Document Metadata
- Type: NASA Phase II SBIR Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II (Proposal Number: A3.02-1718)
- Date: 2023
- BST Products/Systems Referenced: S0 VTOL, S1 UAS, SwiftTab user interface, SwiftCore
- Key Personnel: Jack Elston (last editor)

## Executive Summary
Black Swift Technologies proposes a Phase II effort to develop an operationalized system for collecting atmospheric observations via uncrewed aircraft systems (UAS) and assimilating them into weather models to improve low-level wind and turbulence forecasts for wildland firefighting operations. Building on Phase I feasibility work demonstrating the value of targeted UAS observations and data assimilation near the Calwood Fire in Colorado, Phase II will create end-to-end operational tools, software integrations with Team Awareness Kit (TAK), and refined aircraft systems to support safe aerial firefighting operations in data-sparse mountainous terrain.

## Technical Approach

### Core Innovation
Use ensemble-based meteorological techniques (Ensemble Sensitivity Analysis) to identify optimal locations for gap-filling UAS observations that will have the greatest impact on short-term wind and turbulence forecasts in areas affected by wildland fires. Data collected by atmospheric-sensing S0 and S1 VTOL aircraft will be assimilated using NCAR's Ensemble Kalman Filter (EnKF) approach to generate refined 4D wind and turbulence grids that can be broadcast to incident commanders via Team Awareness Kit (TAK) displays.

### Phase I Achievements (Foundation for Phase II)

**Objective 1 - Ensemble Sensitivity Analysis (ESA) Validation:**
- Created 40-member ensemble forecast at 1km resolution over Rocky Mountains using Calwood Fire (October 2020) as case study
- Used NOAA NWS High Resolution Rapid Refresh (HRRR) model for initial/boundary conditions
- ESA successfully identified areas of heightened sensitivity where targeted observations would have maximum forecast impact
- Method demonstrated ability to identify regions where lower sea-level pressures correlated with higher wind speeds over fire region

**Objective 2 - UAS Flight Operations & Data Assimilation Demonstration:**
- October 13, 2023 flights: Modified S1 UAS with S0 nose collected atmospheric profiling data (pressure, temperature, humidity, dew point, 3D winds) in spirals from 30m to 120m AGL
  - Four flights over 4-hour period with minimal downtime between battery swaps
  - Data successfully converted to WMO-standard NetCDF and PREPBUFR formats for model ingestion
  - Validated climb/descent rate of 2.0 m/s provided optimal data density with low sensor variance
  
- January 5, 2024 flights: Coordinated dual-UAS operations (S0 and modified S1) spaced 15km apart north of Boulder
  - Demonstrated simultaneous dispersed UAS operations
  - Data assimilation using EnKF showed 50% reduction in bias and 30% reduction in RMSE for 10m u-wind component
  - Modified wind field from northerly to east-northeasterly near Boulder Airport (90-degree shift) — operationally critical for firefighting
  - Smaller improvements in v-wind component; relative humidity dry bias notably reduced
  - Demonstrated self-validation technique using GPS ground speed to estimate bulk winds via fixed-altitude orbits and sine-wave fitting to speed vs. ground course

**Objective 3 - Interoperability & Airspace Access:**
- Established partnerships with: NASA FireSense, ACERO, Colorado Center of Excellence (CoE), National Interagency Fire Center (NIFC), CAL FIRE, Boulder County Parks and Open Space
- Formal letters of support from CoE and CAL FIRE for continued collaboration
- Identified key safety requirements: NASA Airworthiness Review (AFSRB/FRRB) and possible Commercial Aviation Services (CAS) review; track record of flight safety critical
- Operating outside Temporary Flight Restrictions (TFRs) identified as practical pathway (TFR boundaries smaller than relevant weather systems)
- Alternative: early morning operations or direct coordination with fire teams using VFR radio
- Determined most valuable data outputs: improved weather forecasting (especially wind shifts) and low-altitude 3D winds for safety of water bombers; secondary value in live video for post-fire operations/SAR

**Objective 4 - S0 VTOL Design Improvements for Rugged Operations:**
- Precipitation & Particulate Resistant 3D Wind Sensor: porous PTFE material prevents tap clogging in rain, ash, smoke
- Primary Propulsion: new motors/propellers selected via bench testing for full-flight hover capability with enhanced efficiency
- Ruggedized Pitching Motor Mounts: linear-actuator based design for full-range tilting on two primary motors enabling true VTOL
- High Capacity Battery: 30% increase in usable capacity with only 20g (3%) weight increase
- Shifted Wing Location: new mount to accommodate battery and propulsion changes
- Tail Motor Configuration: three-motor tricopter configuration with fixed tail motor
- Improved Landing Accuracy: SF20c Laser with integrated housing for non-GPS-dependent landing
- Updated User Interface: improved waterproofing and usability
- CAN-Based Controls: CAN protocol less susceptible to interference than PWM
- Updated Sonde Mount: redesigned for reduced weight and payload swap capability
- Live Video Transmission System: digital HD video system capable of transmitting over 5km (alternate payload)

### Data Dissemination Infrastructure
- Team Awareness Kit (TAK) identified as standard wildfire asset management tool; COTAK (Colorado version) and WFTAK (national version) also used
- Two proposed data pathways to TAK:
  1. **Direct S0-to-TAK**: Ground station communicates directly to TAK instance (no internet required)
  2. **Cloud-based**: S0 ground station sends data via cellular/satellite to NCAR for model ingestion, then processed data distributed to multiple TAK instances
- CoE's field-deployable server and mesh network enables intermediate option for local TAK distribution
- TAK features utilized: 3D maps/overlays for terrain and heat maps, Import Manager for automatic data refresh, open-source architecture supporting custom plugins
- Plan to develop all-in-one TAK plugin for S0 integration combining aircraft flight information and wind forecast maps

## Products & Capabilities Described

### S0 VTOL (Vertical Takeoff & Landing Aircraft)
**What it is:** Rugged, fixed-wing uncrewed aircraft with true VTOL hover capability (tiltrotor configuration with three-motor tricopter design), enhanced from original Phase I version with multiple design improvements for extreme environments.

**Atmospheric Sensing Payload:**
- 3D wind measurement via five-hole probe with precipitation/particulate-resistant porous PTFE design
- Pressure, temperature, humidity (PTH) measurement
- Dew point calculation
- High-frequency wind estimation with self-validation via GPS ground speed analysis

**Proposed Use in Wildfire Context:**
- Gap-filling observations in data-sparse mountainous terrain to improve low-level wind forecasts
- Can be deployed in complex terrain where crewed aircraft cannot safely operate
- Persistent monitoring capability when operating multiple aircraft
- Alternative payload: live HD video transmission system (5km range) for post-fire damage assessment and search/rescue
- Endurance sufficient for extended monitoring operations with battery swapping (demonstrated 4-hour+ continuous sampling with dual aircraft)

**Specifications/Capabilities:**
- Operating altitude: 30m-120m AGL (demonstrated in Phase I)
- Full VTOL hover capability (new in Phase II design)
- Flight time sufficient for atmospheric profiling missions with turnover time <30min between flights
- Data output formats: WMO-standard NetCDF and PREPBUFR for direct model ingestion
- Range/endurance superior to multi-rotor alternatives while maintaining runway-independent operations
- Ruggedized for rain, ash, smoke, extreme atmospheric turbulence

### S1 UAS
**What it is:** Predecessor aircraft to S0, can be modified with S0 nose for equivalent data collection capability.

**Proposed Use:** Demonstrated in Phase I testing as part of multi-platform operations; Phase II plans focus on S0 VTOL as primary platform.

### SwiftTab User Interface
**What it is:** BST-developed ground control station software designed with safety as priority, minimizing operator overhead by simplifying displayed information to only what is needed.

**Proposed Use:** Extended during Phase II for data exchange compatibility with Team Awareness Kit (TAK); custom plugin development to reduce application fragmentation and improve usability during multi-UAS operations.

### Data Assimilation Research Testbed (NCAR's DART)
**What it is:** NCAR's Ensemble Kalman Filter implementation available in DART.

**Proposed Use:** Assimilates UAS observations into HRRR model ensemble to generate refined analyses and short-term forecasts of wind, turbulence, and atmospheric fields; demonstrated 50% bias reduction and 30% RMSE reduction in Phase I testing.

## Use Cases & Applications

### Primary: Wildland Firefighting Operations
1. **Prescribed Burns:** Demonstration flights during controlled burns in Boulder County and other fire agency partnerships to validate methods and gather flight hours
2. **Active Wildfire Response:** Operating outside TFR boundaries to collect data that supports incident commander decision-making without direct interference with manned aircraft
3. **Night Operations:** Enhanced wind/turbulence forecasts enabling safer nighttime aerial firefighting operations (less crowded airspace, easier coordination)

### Secondary Applications (Mentioned as Extensible)
1. **Package Delivery:** UAS delivery in remote mountainous areas where weather variability and sparse data pose significant risk
2. **Advanced Air Mobility (AAM):** Low-altitude flights in mountainous terrain or urban corridors benefiting from enhanced weather forecasting and dynamic route planning
3. **General Aviation Safety:** Wind/turbulence information broadcast to all airspace users via UTM systems

### Specific Case Studies
- **Calwood Fire (October 2020, Boulder CO):** High-impact event with extreme fire behavior, complex terrain, limited observations, proximity to structures. Used retrospectively to develop and validate ESA methodology.
- **October 13, 2023 Test Operations:** Boulder County test flights validating data collection, conversion, and cycling procedures
- **January 5, 2024 Test Operations:** Dual-UAS coordinated sampling north of Boulder demonstrating real data assimilation impact

## Key Phase I Results

### Ensemble Sensitivity Analysis Validation
- ESA successfully identified forecast-sensitive regions for targeted observation collection
- Negative sensitivity areas (lower sea-level pressure → higher winds) more reliably targeted for UAS sampling
- Demonstrated feasibility for operational implementation in HRRR model framework

### Wind Data Improvements from Assimilation
- **10m u-wind component:** 50% bias reduction, 30% RMSE reduction
- **10m v-wind component:** smaller but consistent improvements
- **2m relative humidity:** dry bias notably reduced
- **Geographic impact:** Strongest improvement near Boulder Airport and western foothills; limited impact in complex higher terrain 36km away (indicates need for additional UAS observations)

### Data Quality & Validation Techniques
- Self-validation method using GPS ground speed demonstrated high agreement with instrumented meteorological towers (DOE Southern Great Plains site at 25m and 60m heights)
- WMO-standard data format conversion successful; NCAR verified PREPBUFR formatting
- Climb/descent rate optimization: 2.0 m/s provided highest data density with lowest variance

### Operational Feasibility Demonstrations
- Four-hour continuous operations via battery swapping with minimal downtime
- Dual-UAS synchronized sampling across 15km separated locations successfully executed
- Software tools for data conversion from flight logs to meteorological standards proven functional and repeatable

## Notable Details

### Partnerships & Stakeholder Engagement
- **NCAR/RAL:** Data assimilation expertise; Ensemble Kalman Filter implementation; model guidance integration
- **Colorado Center of Excellence for Advanced Technology Aerial Fireﬁghting (CoE):** Airspace access, local burns, TAK system expertise, COTAK implementation knowledge
- **NASA FireSense:** Integration with Earth science research and operational fire agencies
- **CAL FIRE:** Formal letters of support; feedback on technology adoption criteria (flight safety track record as priority)
- **National Interagency Fire Center (NIFC):** Operational insights on data needs and coordination requirements
- **Boulder County Parks and Open Space:** Access to local prescribed burn operations

### Competitive Advantages Over State-of-the-Art
1. **Superior to