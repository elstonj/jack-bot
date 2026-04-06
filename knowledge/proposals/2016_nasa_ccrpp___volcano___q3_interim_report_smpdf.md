# 2016_NASA_CCRPP___Volcano___Q3_Interim_Report

## Document Metadata
- Type: Quarterly Demonstration Report (Q3 Interim Report)
- Client/Agency: NASA (CCRPP - Collaborative Capability Research & Prototyping Program)
- Program/Solicitation: SBIR Phase III, Topic 2022-1-1118; Contract Number: 80NSSC22CA192
- Date: May 2023 (submitted as Q3 report)
- BST Products/Systems Referenced: S2, S0, S2 VTOL, SwiftCore, SwiftTab, SwiftPilot, E2
- Key Personnel: Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
This quarterly report documents Q3 progress on a NASA-funded SBIR project to develop a ruggedized uncrewed aircraft system (UAS) for scientific data gathering in harsh environments. BST continued development of autonomous flight capabilities for extreme weather operations, supporting simultaneous NOAA hurricane sampling and soil moisture mapping missions, while advancing terrain-aware mission planning and user interface improvements for flexible payload management across multiple science applications.

## Technical Approach
The project improves upon Phase II-e work that successfully demonstrated the S2 aircraft on volcano observation missions in Alaska. The current phase (Phase III via CCRPP) focuses on four key technical objectives:

1. **Intelligent flight in strong winds**: Implementing real-time wind assessment and predictive models to minimize energy usage through wind-aware flight path adjustments in SwiftCore firmware
2. **User interface improvements**: Developing flexible SwiftTab application software to support interchangeable payloads with common operating picture and telemetry display
3. **Advanced mission planning**: Automating flight path planning that accounts for terrain, communication line-of-sight limitations, and battery optimization
4. **Improved S2 VTOL manufacturability**: Simplifying construction and reducing costs of the vertical takeoff/landing variant for strong wind operations

The work leverages customer/investor matching funds from NASA Ames, NOAA Weather and Prediction Operations (WPO), and USGS to validate developments in operational field campaigns.

## Products & Capabilities Described

### S2 Aircraft
- Terrain-aware fixed-wing UAS demonstrated on Makushin Volcano (Alaska) missions
- Capable of beyond visual line of sight (BVLOS) operations in complex terrain and extreme winds
- Recent 4-mission deployment showed wind and power management limitations requiring solutions
- Status: Production improvements underway; S2 VTOL variant in development

### S2 VTOL Variant
- Vertical takeoff/landing capability enables launch/landing from small or obstacle-dense areas
- Prototype tested during Phase II-e; improves operational envelope for strong wind environments
- Planned improvements: simplified construction, reduced manufacturing cost

### S0 Aircraft (Small UAS)
- Tube-deployed system for deployment from NOAA P3 research aircraft
- Currently in production for 2023 hurricane season (8 units ordered)
- Specifications: ~80+ minute flight duration, 10-25+ nmi communication range
- Equipped with: improved autopilot, multi-hole pitot (MHP) probe for wind measurement
- Sensor suite: Vaisala RSS421 atmospheric sonde, temperature/humidity/pressure/wind sensors
- Clear air testing (March 2023): 3 successful flights validating deployment, atmospheric measurement

### S0 Atmospheric Sensing Capabilities (Post-Phase II-e)
- 3D wind measurement (lateral and vertical) with Kolmogorov spectral analysis capability
- Temperature/relative humidity profiling with ±1°C accuracy (±20% RH initially, corrected to near-dropsondes)
- Precipitation-tolerant design with multi-hole probe and deflector for RSS421 sonde protection
- Sea surface and laser altimeter data capability
- Comparison with dropsonde data shows competitive performance; exceeds dropsondes in turbulence measurement

### E2 Aircraft
- Used for NOAA soil moisture mapping missions
- Fixed-wing platform for radiometric surveys

### SwiftCore Firmware
- Aircraft autopilot control system
- Planned enhancement: wind-aware intelligent flight algorithms for energy-optimized routing

### SwiftTab/SwiftPilot Software
- Ground control and mission planning application
- Current limitations: largely manual waypoint/altitude selection; limited terrain/airspace avoidance
- Planned upgrades: terrain-following collection patterns, LoS communication optimization, battery usage estimation, automated flight parameter calculation

### Radiometric Payload (Soil Moisture)
- L-band brightness temperature measurement (15m footprint)
- Redesigned warm/cold source (non-thermal-gradient based) reduces weight, power, and instrument noise
- Validation: Two flights (April 2023) over paired test sites with 200+ ground-truth soil moisture measurements per flight
- Performance: Excellent visual agreement with in situ data; UAS readings slightly wet on upper end due to water body overlap; ±3% agreement on moisture change between flights

## Use Cases & Applications

### NOAA WPO Hurricane Sampling
- Deployment from NOAA P3 during active hurricane season
- Objectives: Atmospheric data collection in severe conditions
- System: 8 S0 aircraft being produced
- March 2023 clear air testing achieved: 3 successful deployments, 80+ minute endurance, sea surface data, atmospheric profiling
- Challenges addressed: GPS antenna integration, static pressure calibration, AVAPS RF interference mitigation
- Future: 2023 hurricane season planned as first operational deployment in actual hurricanes

### NOAA WPO Soil Moisture Mapping
- Regional soil moisture mapping with radiometric L-band measurements
- Completed Year 1 deliverables
- March-summer 2023: 3 planned flights (2 completed by report date)
- Target: SPLASH campaign study area
- Ground validation: 200+ in situ probe measurements per flight at 3.5cm depth
- Performance validation: April 2023 flights showed corrected humidity bias and excellent spatial agreement with in situ data

### NASA Volcano Observation
- Phase II-e demonstrated visual observations of Makushin Volcano (Alaska) during period when satellite data unavailable
- Payload: thermal imaging, 3D mapping, spectral analysis capabilities
- Current role: Reference application for future Earth Science missions
- Planned applications: CALIPSO, Aura, CATS, OCO-2/3 field campaign support; Tropospheric Chemistry Program

### Wildfire/Air Quality Monitoring (Potential)
- Ability to operate in environments with severe particulates and turbulence
- Support for dispersion model validation
- Ash hazard and smoke impact assessment

### Atmospheric Model Validation
- Vertical profile measurement of wind, temperature, humidity for model input/validation
- Particular value for volcanic ash aviati hazards, pollution alerts, toxic releases, dust storms
- Advantage over satellites: independent of cloud cover, at higher spatial/temporal resolution

## Key Results

### S0 Hurricane Sampling - Clear Air Testing (March 2023)

**Flight 1 (23 March)**:
- Partial success: GPS altitude initialization failure
- Corrective action: GPS altitude fallback and static pressure validation implemented in firmware
- Issue identified: Reduced AVAPS RF performance due to S0 out-of-band noise (requires further filter/amplifier investigation)

**Flight 2 (24 March)**: 
- 80+ minute endurance achieved
- Successful mission profile: square pattern descent from 5000ft to 10-15m altitude
- Sea surface and laser altimeter data collected
- Atmospheric profiling: Temperature profile matches dropsondes well; humidity corrected for sensor heating bias (5°C)
- Range test failure: Maximum ~15-25 nmi datalink range instead of required 150 nmi (requires RF settings investigation)
- Battery monitoring failure around 55 minutes

**Flight 3 (26 March)**:
- 60-minute flight duration
- GPS antenna ground plane failure at low altitude (corrected in autopilot hardware revision)
- Temperature bias: ~1°C warm bias noted (source under investigation)
- Humidity data: Corrected for sensor heating; spikes identified as sensor-side failures (returning -999 invalid values)
- Wind measurements: Multi-hole probe validation completed; aircraft accurately tracks 3D wind vs. dropsonde measurements
- Turbulence/wind structure: Kolmogorov frequency spectrum shows expected -5/3 slope; small 1Hz aircraft motion corrections needed

**Production Updates Planned**:
- Integrated GPS antenna (increased performance, compact, lower cost)
- Reduced autopilot size/weight (~1 inch PCB length reduction)
- USB-C integrated interface
- Improved MHP fabric with higher hydrostatic head (AATCC 127) for precipitation tolerance
- RSS421 deflector design optimization for airflow without water ingestion

### NOAA Soil Moisture Mapping (April 2023)

**New Radiometer Design**:
- Warm/cold source redesigned (non-thermal-gradient method)
- Result: Increased thermal separation between channels, reduced weight, reduced power consumption

**Flight Validation**:
- Two flights (7 April and 11 April): Similar soil moisture, different air temperatures—excellent test of radiometer compensation
- L-band brightness temperatures: Reasonable values with correct water signatures
- Soil moisture map comparison with in situ: Visual agreement excellent on both days
- UAS vs. in situ quantitative comparison: Centered near 1:1 line; slight wet bias on upper end (water body overlap explained)
- Moisture change between days: ±3% agreement on change maps; consistent drying trend (bottom areas), wetting in top-right
- Conclusion: "Very encouraging" results validating hardware updates have resolved prior drift/offset issues

### Mission Planning Development (Design Phase)

**Segment-Based Approach**:
- Collection segment: Terrain-following patterns optimized for data collection
- Transit segment: Battery/LoS communication optimized

**Collection Pattern Algorithm**:
- Converts operator-defined start/end point lines to dense waypoint sets
- Adds terrain model for constant altitude above ground level (AGL)
- Ensures aircraft flight capability compliance

**Planned Capabilities**:
- Automated terrain and airspace avoidance
- Battery usage estimation along route
- Line-of-sight communication loss prediction
- Wind-aware altitude/airspeed optimization
- Estimated flight parameters (time enroute, battery remaining) at mission planning stage

### User Interface/SwiftTab Application Framework (Design Complete)

**Payload Application Architecture (XML-Based)**:
- Modular definition enabling flexible, interchangeable payloads
- Components: Payload Layout, Sensor Parameters, Mapping Inputs, Pre/Post-Flight Checklist, Scripts, Payload Struct Definition, Custom Plotting

**Data Management Features**:
- Serial interface flexibility: BST protocol, UBlox/NMEA GPS, MAVLINK, payload passthrough, hardware-in-the-loop
- Sensor parameter configuration (focal length, trigger mode, etc.)
- Payload channel-to-autopilot actuator mapping
- Pre/post-flight checklists with manual/automated/user-validation items
- Automated multi-sensor mission planning (separate patterns per sensor or unified optimized pattern)
- Custom telemetry plotting with time-series and geo-referenced (heat map/scatter/wind barb) visualization

**Implementation Status**: Design complete; implementation beginning with soil moisture mapping as first application

## Notable Details

### Technical Partnerships & Stakeholder Network
- **NASA Ames**: Primary customer; airborne science program integration
- **NOAA WPO**: Two parallel programs (hurricane sampling, soil moisture); matching fund investment
- **USGS**: Technical advisors on volcano work (Christoph Kern, Angie Diefenbach); operational partner on Makushin missions
- **JPL/Dave Pieri**: Volcano observation technical input
- **NCAR**: Atmospheric data processing consultation (humidity correction methodology)
- **DOE/Southern Great Plains Site**: Reference data for wind turbulence validation

### Atmospheric Measurement Quality Achievements
- S0 wind measurements now competitive with/exceed dropsondes in capturing high-frequency turbulence
- Humidity correction methodology (fixed dewpoint assumption for sensor heating) brings data into agreement with reference dropsondes
- Temperature accuracy: ±1°C with minor remaining bias requiring investigation
- Spectra analysis validates physical wind structure capture

### Radar/Communication Challenges Identified
- S0 datalink range (15-25 nmi achieved) significantly below 150 nmi target—RF settings/configuration requires investigation
- AVAPS/S0 RF interference on 400MHz band—inadequate filtering/amplification in legacy AVAPS system
- Solutions under investigation but ongoing challenge for multi-platform operations

### Production Ramp-Up Status