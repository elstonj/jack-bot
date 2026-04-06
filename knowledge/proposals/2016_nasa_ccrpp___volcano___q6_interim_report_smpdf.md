# 2016 NASA CCRPP Volcano Q6 Interim Report

## Document Metadata
- Type: Quarterly Demonstration Report (Q6)
- Client/Agency: NASA (Contract through NASA Shared Services Center)
- Program/Solicitation: SBIR CCRPP (Commercialization/Collaboration Research Pilot Project); Contract Number 80NSSC22CA192; Original Topic 2022-1-1118
- Date: February 2023
- BST Products/Systems Referenced: S0, S2, S2-VTOL (later called S3), SwiftCore (firmware), SwiftTab (app)
- Key Personnel: Jack Elston (PI/Offeror), Maciej Stachura (Lead Engineer)

## Executive Summary
This Q6 report documents Black Swift Technologies' progress on developing ruggedized UAS for scientific data gathering in harsh environments. Building on successful Phase II-e work (including Alaska volcano missions), BST is advancing automation capabilities for extreme environment operations through intelligent flight algorithms, improved user interfaces, manufacturability enhancements to the S2-VTOL, and expanded operational deployments with NOAA for hurricane sampling and soil moisture mapping.

## Technical Approach
BST's approach centers on automation and intelligence to enable routine operations in challenging atmospheric environments:

1. **Intelligent Wind-Aware Flight Planning**: Real-time environmental assessment combined with predictive models to adjust flight paths, minimize energy usage, and handle lateral/vertical wind exceeding S2 capabilities

2. **Terrain and Communications-Aware Mission Planning**: Automated processes for flight planning and control accounting for rugged terrain and communication system limitations

3. **Simplified Manufacturing**: Updated S2-VTOL design (renamed S3) to reduce construction complexity and overall price while maintaining VTOL capability for launch/landing in strong winds

4. **Flexible Payload Management**: Enhanced SwiftTab app to display telemetry from interchangeable payloads and manage flexible payload control requirements

## Products & Capabilities Described

### S0 Aircraft (Small UAS)
- Small fixed-wing aircraft designed for hurricane and environmental sampling missions
- Equipped with Multi-hole Probe (MHP) sensor for real-time wind speed/direction measurement at 100 Hz
- Operational range: ~70 miles (target 150 nmi with updates)
- Features rechargeable battery system, CAN bus servo control, waterproof pressure port membranes
- Recent improvements: 6-cell 21700 battery pack (5% greater endurance), CAN-to-PWM conversion board, enhanced manufacturability with improved wire routing and assembly features
- 2024 hurricane season deployment: 16 operational S0 systems planned for NOAA WPO

### S2 Aircraft
- Larger terrain-aware fixed-wing aircraft used for volcano monitoring and soil moisture mapping missions
- Successfully completed operational missions to Makushin Volcano, Alaska with USGS/NASA
- Limitations noted: Extended ingress consuming too much propulsion power (20-mile flights), wind (lateral/vertical) exceeding aircraft capabilities
- Equipped with multiple specialized scientific payloads
- Planned updates with intelligent flight algorithms and terrain/communications awareness

### S2-VTOL / S3 Aircraft
- Vertical takeoff/landing variant of S2, prototype tested during Phase II-e
- Primary advantage: Launch/landing in strong winds from small/obstacle-dense areas, greatly expanding operational envelope
- Current focus: Simplified design for manufacturability and cost reduction
- Target: Functional prototype by Q1 2024; planned for volcano observations in Chile Q2 2024

### SwiftCore Firmware
- Flight control and autopilot software for BST aircraft
- Improvements implemented: Enhanced wind-aware flight planning, terrain/communications-aware algorithms, hurricane flight control modes
- Supports multiple flight patterns: eyewall tracking, inflow, center fix (for hurricane operations)
- 100 Hz sensor data processing with sliding-window averaging for noise mitigation

### SwiftTab Application
- Ground control station/mission planning software
- Updates: Unified configuration file structure, custom payload telemetry display (up to 8 channels), payload command capability, generic status display, custom pre-flight checklists, custom mapping and plotting (geographic and time-series)
- Supports diverse payload configurations without requiring multiple software packages

### Specialized Payloads
- **Multi-hole Probe (MHP)**: 5-port sensor measuring wind speed/direction in real-time; critical for hurricane eyewall tracking
- **Soil Moisture Radiometer (Rev. D)**: Simplified design using digital correlation via ADALM Pluto board; accepts dual commercial patch antennas; self-calibrating
- **Thermal/Photogrammetry Package**: Combines visual and thermal imaging for volcano mapping; produces 3D maps and orthomosaics with thermal data overlay
- **Trace Gas Sensors**: CO₂ measurement capability (precision improvements in progress)
- **Video Equipment**: Integrated on S0 for calibration missions

## Use Cases & Applications

### NASA Applications
- **Volcanic Ash Aviation Hazards**: Improved atmospheric model validation for volcanic ash forecasting
- **Air Quality Monitoring**: Support for Tropospheric Chemistry Program, CALIPSO, Aura, CATS, OCO-2/3, Earth Ventures missions
- **Wildfire Smoke Monitoring**: Operations in hazardous particulates and severe turbulence
- **Calibration Missions**: Satellite calibration/validation (ASTER, MODIS, AIRS, OMI)

### NOAA Applications
1. **Hurricane Sampling (WPO)**: 
   - Eyewall tracking missions collecting wind, pressure, temperature, humidity, sea surface temperature below 5,000 ft
   - Inflow pattern missions spiraling inward to measure hurricane inflow at different altitudes
   - Center fix missions to locate precise hurricane center via minimum wind speed and wind direction shift
   - 2023 season deployment with 6 S0 aircraft; 2024 season expansion to 16 aircraft

2. **Soil Moisture Mapping (SPLASH Campaign)**:
   - Radiometer-based mapping at Crested Butte and Pepperwood test sites
   - Year 1 deliverables completed; continuing with Air Force funding

### USGS Applications
- Volcano observation campaigns: Makushin (Alaska) operational missions; Chile deployment Q2 2024
- 5 flights to summit with two different thermal/gas payloads completed during reporting period
- Christoph Kern, Angie Diefenbach, Jonathan Stock (USGS advisors) involved in planning/execution

### Commercial/Industrial Applications
- **Oil & Gas Methane Detection**: Demonstration completed with producer showing sub-facility level emission resolution over entire facility; continuing commercialization efforts
- **Wildfire Monitoring/Support**: Operational capability in hazardous particulate environments

## Key Results (Reports/Achievements)

### Technical Accomplishments Completed
1. All Phase III NASA deliverables completed
2. Year 1 deliverables for both NOAA WPO missions (hurricane sampling, soil moisture) completed
3. Initiated intelligent flight planning through winds
4. S0 deployment tube system redesigned: Rechargeable lithium battery integration, single-piece aluminum latch, improved power switch, safety pin housing
5. S0 airframe improvements: New 6-cell battery pack design, CAN bus servo control implementation, pressure port adhesion testing with 3M 94 primer
6. S0 manufacturability enhancements: Increased drainage holes in 3D structures, wire routing channels, latching connector upgrades, stringers in horizontal tail, ballast weight pockets
7. S0 firmware range optimization: Data rate reduction through engineering data filtering while prioritizing science data
8. S0 external interface integration: HDOBS and AirOps data ingestion/dissemination improvements

### Hurricane Flight Controller Development
Three independent eyewall tracking algorithms developed and tested in simulation:

1. **Alignment Controller with Offset**: 
   - Aligns aircraft heading to wind direction at periodic intervals (typically 100-150 sec)
   - Relies on eyewall wind speeds exceeding aircraft airspeed
   - Mean error: ~3,486 meters in test trajectory

2. **Left-Right Eyewall Controller**:
   - Alternating left/right turns triggered by decreasing wind trend detection
   - Parallel low-frequency alignment loop prevents heading deviation
   - Best overall performance in simulated hurricane dataset
   - Mean error: ~1,203 meters in test trajectory

3. **Gradients Controller**:
   - Measures tangential wind gradients to differentiate radial vs. tangential wind variation
   - Accounts for wind variability along eyewall arc
   - Subtracts tangential gradients from cross-eyewall measurements

**Simulation Results**:
- 729 parameter sets evaluated across 5 altitudes (30m-2000m) over 120-minute simulations
- Left-Right Controller demonstrated best performance
- Error increases at low altitudes (hurricane inflow) and high altitudes (outflow); optimal performance at ~1,000-1,200m
- Parameters tunable per altitude but may not generalize across different hurricanes
- Future work: UI elements on SwiftCore Tablet for in-mission parameter adjustment

### Inflow and Center Fix Controllers
- **Inflow Controller**: Develops spiral pattern from outside eyewall inward; similar to eyewall trackers but drives initial intercept
- **Center Fix Controller**: Implements "Figure 4" pattern scaled to S0 performance (40 knots vs. P-3's 100 knots); 120-degree waypoint rotation about estimated center; algorithm complete, simulation/flight testing planned

### Soil Moisture Radiometer (Rev. D)
- Simplified frontend design removing analog correlation
- Digital correlation via ADALM Pluto 1 board enabling faster iteration and intelligent noise rejection
- Self-calibrating design addressing recalibration issues from prior campaigns
- Accepts commercially-sourced dual patch antennas (more robust than custom designs)
- Design evolved from Rev C2

### Software/UI Improvements
- Unified configuration file architecture consolidating: custom scripts, payload packet structures (rx/tx for 8 channels), serial/CAN interfaces, pre-flight checklists, mapping setup, plotting configuration
- Generic payload status display in custom UI windows
- Support for diverse "Applications" configurations: methane mapping, soil moisture, volcano trace gas/photogrammetry, hurricane sampling

### Manufacturability/Design Updates for S2-VTOL (S3)
- S3 simulator updates in progress
- Propulsion system refinements ongoing
- Control system advancements underway
- Target: Functional prototype Q1 2024

## Notable Details

1. **Phase II-e Success Validation**: S2 achieved only visual observations of target volcano during calendar year of deployment; however, revealed automation requirements—flight planning required months of preparation, in-mission monitoring of wind data critical for battery margin management

2. **Customer/Investor Base**: Three entities investing in CCRPP—NASA Ames and two NOAA groups (WPO divisions)—all requiring operations in rugged terrain, precipitation, and/or strong winds

3. **Simulation Infrastructure**: BST developed dual simulation approaches:
   - Python-based Hurricane Trajectory Simulator (kinematic, rapid parameter evaluation)
   - X-Plane physics-based extensions (high-fidelity dynamics with actual flight control software)

4. **Competitive Advantage**: Small UAS capable of operations in airspaces too hazardous for crewed aircraft; S2-VTOL enables launch/landing where conventional aircraft cannot; automated mission execution suitable for routine global deployments

5. **Data Quality Impact**: Improved atmospheric models reduce uncertainty in warnings for volcanic ash aviation hazards, pollution alerts, toxic releases, dust storms, and wildfire smoke—direct safety implications

6. **International Operations**: Planned Chile deployment Q2 2024 with USGS; algorithms for automated terrain/communications planning to reduce setup time in unfamiliar locations

7. **Production Readiness**: 
   - 2 S0 aircraft + new ground station for NOAA delivery March 2024
   - 14 additional S0 aircraft for NOAA delivery June 2024
   - 4 S0 systems for March 2024 clear air testing
   - Total 16 operational S0 systems for 2024 hurricane season

8. **Multi-hole Probe Sensor**: Commercial market potential identified for this BST-developed sensor; referenced as deliverable for Altius integration (10 probes total: 2 by Q1 2023, 8 by Q2 2023)

9. **Clear Air Testing Schedule**: March 2024 campaign planned to validate design updates, test intelligent flight algorithms, perform thorough range testing (5,000' and 500' altitudes), test max winds/center fix/inflow controllers, validate wave height and thermal measurement accuracy, test precipitation performance

10. **Partnerships**: Active collaboration with