# 2016_NASA_CCRPP___Volcano___Q1_Interim_Report

## Document Metadata
- Type: SBIR Phase III/CCRPP Quarterly Demonstration Report #1
- Client/Agency: NASA (contract 80NSSC22CA192); also NOAA Weather Program Office (matching funds)
- Program/Solicitation: NASA SBIR CCRPP (Collaborative Commercialization and Research Partnership Program); Topic 2022-1-1118
- Date: November 2022
- BST Products/Systems Referenced: S2, S0, E2, SwiftCore (firmware), SwiftTab (app), SwiftStation (ground control station), AeroPod (implied)
- Key Personnel: Jack Elston (PI/Principal Investigator), Maciej Stachura (Lead Engineer)

## Executive Summary
Black Swift Technologies is executing a Phase III SBIR contract to develop ruggedized UAS capabilities for scientific data gathering in harsh environments, focusing on automation and wind-aware flight planning. The project builds on successful Phase II-e volcano observation missions and receives matching funds from NOAA for hurricane sampling and soil moisture mapping. Key technical objectives include intelligent wind-aware flight planning, improved mission planning for terrain/communications, enhanced user interface for scientific data management, and improved manufacturability of the S2-VTOL variant.

## Technical Approach

**Core Philosophy:** Automate capabilities that were previously manual and expertise-dependent, enabling routine global operations in challenging environments without highly specialized teams.

**Key Technical Objectives:**

1. **Intelligent Flight in Strong Winds**: Implement real-time environmental assessment combined with predictive modeling to inform automated flight path changes that minimize energy usage. Uses decision tree regression machine learning on 300+ S2 flights. Improvements needed to account for vertical air velocity (angle-of-attack) rather than GPS-derived climb rates, and integration of wind forecasts for pre-flight planning.

2. **User Interface Improvements**: Update SwiftTab application to provide flexible, interchangeable payload telemetry display and control via XML-based or tablet UI components for common operating picture.

3. **Advanced Mission Planning**: Automated processes for terrain and communication limitation planning, building on wind-aware planning methodology.

4. **Improved S2-VTOL Manufacturability**: Simplify construction and reduce cost of the vertical takeoff/landing variant that enables operations in strong winds and obstacle-dense areas.

## Products & Capabilities Described

### S2 (Fixed-wing UAS)
- **Description**: Primary research platform for long-range, high-altitude scientific operations
- **Configuration for Phase III**: 
  - Heated pitot tube (upgraded from Phase II-e prototype to production PCB with thermistor feedback and duty-cycle heating control)
  - ADS-B receiver integrated with avionics for manned aircraft detection
  - Iridium satellite communications backup system (custom board/firmware between radio and autopilot)
  - RTK GPS capability
  - Tail boom-mounted antenna for satellite modem
- **Used for**: Volcano observations (Makushin, Alaska deployment Sept 2021), soil moisture mapping, atmospheric measurements
- **Performance note**: 4 successful missions at Makushin but 2-3 turned back due to wind or power constraints (20-mile ingress problematic in high winds)
- **Payloads carried**: Trace gas payload (CO₂, SO₂ measurement), thermal/optical camera payload with georeferencing, atmospheric sensors (pressure, temperature, humidity)

### S0 (Tube-launched single-use UAS)
- **Description**: Low-cost, purpose-built platform for deployment from manned aircraft (NOAA P3 "Hurricane Hunter")
- **Configuration**: 
  - Fits in ~5" OD × 37" long tube with spring-loaded wings
  - Full suite of atmospheric sensors: pressure, temperature, RH, sea surface temperature
  - Custom 5-hole pitot probe for 3D wind measurement
  - 400MHz communication system
  - Compact autopilot and sensor suite
- **Range**: Up to 150 nautical miles from P3
- **Used for**: Hurricane boundary layer sampling from NOAA P3 aircraft
- **Status**: Two prototypes successfully tested May 2022 (safe separation, deployment, level flight transition, sensor functionality validated); full-duration flight testing planned Spring 2023
- **Under development**: Waterproof multi-hole probe tip using thin nylon membrane with DWR coating for heavy precipitation operation

### E2 (Multirotor)
- **Description**: Multi-rotor platform for soil moisture measurements
- **Configuration**: Carries passive L-band microwave radiometer
- **Resolution/Coverage**: 10-20 m resolution over several square kilometers
- **Used for**: NOAA SPLASH soil moisture mapping campaign (4 deployments May-October 2022 at Avery site and other locations)

### S2-VTOL (Vertical Takeoff/Landing variant)
- **Status**: Prototype tested during Phase II-e, in development for Phase III production
- **Advantage**: Can launch/land in strong winds, obstacle-dense areas without runway
- **Objective**: Simplify manufacturing, reduce cost, expand operational envelope
- **Customer**: NOAA group (one of three CCRPP investor groups)

### SwiftCore (Firmware)
- Real-time wind-aware flight path optimization implemented here
- Automated mission generation capabilities
- Integrates satellite/Iridium communications failover logic
- Controls heated pitot tube via CAN bus (1000 μs = off, 1500 μs = auto, 2000 μs = on)

### SwiftTab (Ground Control Station Application)
- Python-based GUI for real-time telemetry display
- Displays ADS-B aircraft detection
- Being upgraded for flexible, payload-agnostic data display
- Supports mission planning with wind/terrain/communications awareness

### SwiftStation (Ground Control Station Hardware)
- Modular antenna stand constructed for Alaska campaign
- Supports multiple antenna types including directional FCC-licensed antenna
- Waterproof containers for precipitation operation
- Improved range and ease of setup/adjustment

### Specialized Payloads

**Trace Gas Payload**:
- Measures atmospheric trace gases (CO₂, SO₂)
- Reconstructed from Phase II-e prototype with improved cable routing
- Assembly labor: 40 hours; PI firmware setup/testing: 16 hours; calibration/testing: 16 hours
- Uses Python GUI for real-time telemetry in flight

**Thermal/Optical Payload**:
- Dual camera system (RGB + thermal)
- Aircraft-triggered synchronized capture with georeferencing
- Additional battery for extended mission time
- Bench-tested for camera settings, trigger verification, photo georeferencing

**Multi-hole Probe (MHP)**:
- Custom 5-hole pitot for 3D wind measurement (5 measurements for angle-of-attack, angle-of-sideslip)
- Standard version: measures pressure ports
- Hurricane variant: waterproof design with DWR-coated nylon membrane covering ports (in development, requires wind tunnel recalibration)
- Used on S0 for hurricane work and planned for S2 wind estimation improvements

**Backup Satellite Communications (Iridium)**:
- Custom PCB and firmware
- Sits between command/control radio and autopilot (aircraft) or between radio and GCS single-board computer
- Seamless fallover: waits for 10 seconds or half the lost-comm timeout (whichever is shorter), then transmits down-sampled data over Iridium
- Queries IMEI to auto-determine correct SIM phone number
- Modifies RSSI header (sets to 0) to signal radio loss but Iridium connection maintained
- Adjusts retry timeouts on detected RSSI=0 to accommodate 4+ second round-trip latency
- Suspends telemetry transmission when command is being sent over satellite link
- Recent updates: new PCB spin for component shortages, completely redesigned mounts for aircraft and ground station for dust protection and better RF conditions for modems

## Use Cases & Applications

### Volcano Monitoring
- **Makushin Volcano, Alaska (Sept 2021)**: 4 missions with S2; provided only visual observations of target volcano that calendar year; complex terrain navigation, BVLOS operations, strong winds/downdrafts that exceeded aircraft capability and even some manned aircraft
- **Challenges addressed**: Long flight planning preparation (months), frequent in-flight wind observation feeding into custom software for battery margin calculation, required highly knowledgeable specialized team
- **Goal**: Automate these capabilities for routine worldwide operations
- **NASA customers**: Tropospheric Chemistry Program, Applied Sciences Air Quality Program, CALIPSO, Aura, CATS, OCO-2/3, Earth Ventures programs; JPL and NASA Ames volcanic/wildfire observation programs

### Hurricane Boundary Layer Characterization (NOAA WPO)
- **Platform**: S0 tube-launched from NOAA P3
- **Objective**: Complement existing data coverage within tropical cyclone boundary layer; improve intensity forecasts through advancements in boundary-layer process understanding
- **Data delivery**: Real-time to National Hurricane Center (NHC), Environmental Modeling Center (EMC), Hurricane Research Division (HRD)
- **Science**: Physical processes in boundary layer to be incorporated into operational forecast models
- **Status**: Two prototype flights May 2022 successful; full-duration testing Spring 2023 planned

### Soil Moisture Mapping (NOAA WPO SPLASH)
- **Platforms**: S2 and E2
- **Sensor**: Passive L-band microwave radiometer for 5-20 cm depth soil moisture
- **Resolution/Scale**: 10-20 m resolution over several km²
- **Data use**: Evaluate forcings for National Water Model, support development of Unified Forecast System (UFS) and Rapid Refresh Forecast System (RRFS), inform process-level understanding of surface energy budget and atmospheric boundary layer
- **Deployment**: 4 campaigns May-October 2022 covering Avery site and other locations; generated RGB, thermal, NDVI, and volumetric soil moisture datasets

### Other Potential Applications
- Wildfire monitoring and support (hazardous particulates, severe turbulence)
- Air quality monitoring (pollution, toxic releases, dust storms, smoke)
- Calibration missions for satellite data (ASTER, MODIS, AIRS, OMI)
- Ground-based observations (S0 VTOL variant for atmospheric measurements)
- Commercial multi-hole probe sensor market

## Key Results (Phase III Q1 Interim)

### Completed/In Progress:
- **NASA Phase III deliverables**: S2 (S/N S20015) constructed and QC tested; all quality control values and component serial numbers recorded; flight-tested with launch system and full manual control options
- **NOAA WPO soil moisture**: Year 1 deliverables completed; four successful field deployments with rich datasets
- **NOAA WPO hurricane sampling**: Year 1 deliverables completed; two prototype S0 aircraft successfully tested for separation, deployment, level flight transition, and sensor functionality from P3
- **Intelligent wind flight**: Machine learning regression model (10-level decision tree) built from 300+ S2 flights; tested against training data with very good performance; field-validated at Makushin showing model weakness in high-downdraft regions

### Milestones Scheduled (from Table 1):
- Q2 2022: Two S0 (calibration), S2 (soil moisture)
- Q3 2022: Six S0 (hurricane), S2 (remote sensing/trace gas), two S0 VTOL (ground obs)
- Q1 2023: Two multi-hole turbulence probes for Altius integration
- Q2 2023: Six video S0 (calibration), eight multi-hole probes for Altius
- Q3 2023: Six video S0 (calibration)

### S0 Hurricane Testing Results (May 2022):
- Mass model drop: successful safe separation from P3
- Two functional prototype flights: successful deployment, safe separation, level flight transition, meteorological data recording
- Identified need for waterproof multi-hole probe for heavy precipitation; prototype design developed (nylon membrane with DWR coating)
- Full-duration flight testing with sensor data analysis planned Spring 2023

### Soil Moisture Campaign Results:
- Four successful deployments covering multiple sites
- Generated RGB imagery, thermal imagery, NDVI calculations, volumetric soil moisture values
- Demonstrated 10-20 m resolution capability over several-km² areas

### Wind Flight Planning Insights:
- Makushin mission analysis revealed power usage prediction errors in downdraft regions
- Current model uses GPS-derived climb rate; planned improvement: