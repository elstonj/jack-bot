# Persistence Demo Final Report

## Document Metadata
- Type: Final Report
- Client/Agency: NASA (NOAA collaboration)
- Program/Solicitation: Contract Number 80NSSC25CA043
- Date: September 25, 2025
- BST Products/Systems Referenced: S2 UAS (multiple aircraft: S20003, S20009)
- Key Personnel: Paige Smith (last editor), demonstration team included representatives from NOAA, NASA, and US Forest Service

## Executive Summary

Black Swift Technologies demonstrated the operational feasibility of using the S2 fixed-wing UAS to provide persistent infrared monitoring of wildfires, detect unauthorized drones in restricted airspace, and maintain continuous overwatch through coordinated aircraft handover procedures. The project integrated NOAA's NightFOX multispectral payload with the S2 platform and validated both technical performance and operational utility across three demonstration objectives conducted in August 2025.

## Technical Approach

### NightFOX Wildfire Detection Payload Integration
- Mounted multispectral sensor suite on S2 UAS for high-resolution fire detection
- Validation flight conducted August 20, 2025 at Pawnee National Grasslands
- Demonstrated data collection at 400m and 800m AGL
- Flight coverage: 45 square kilometers in 50 minutes
- Data streams transmitted to ground station in near real-time via S2 datalink

### UAS Detection System Development
Three complementary sensor technologies integrated into S2 airframe:
1. **ADS-B Reception**: Commercial off-the-shelf receiver modified for S2 integration; tracks multiple simultaneous airborne and ground targets with position, altitude, velocity data
2. **Long-Range Remote ID Detection**: Custom Bluetooth 5.2 module (Nordic nRF52840) optimized for Remote ID packet detection; operational range 1-1.3 km (improvement over ground-based 400-1,000m limit)
3. **Software-Defined Radio Signal Interception**: Custom SDR platform detecting drone command/control signals and video transmission links on common frequencies (1.2 GHz, 2.4 GHz, 5.8 GHz)

### Persistent Operations Procedure
- Developed on-station handover protocol for continuous coverage
- Demonstration: Two sequential 30-minute S2 flights maintaining uninterrupted overwatch
- Procedure: Establish first aircraft in Operations Orbit (380' AGL) → Launch second aircraft to Standby Orbit (300' AGL) → Send first to Landing Orbit → Shift second to Operations Orbit
- Scalable to wildfire scenarios with altitude blocks, lateral separation, and time-based scheduling

## Products & Capabilities Described

### Black Swift S2 UAS
- **Configuration**: Fixed-wing, small, multi-sensor capable platform
- **Endurance**: Approximately 2 hours with NightFOX payload; extended with modular battery design
- **Maximum operational radius**: 30 km from takeoff/landing site (datalink limitation)
- **Payload capacity**: Demonstrated integration of NightFOX multispectral suite, Remote ID receiver, RF detector, ADS-B receiver simultaneously
- **Data transmission**: Near real-time video and sensor data to ground station via S2 Ground Station datalink
- **Integration capability**: Seamless data feed to Wildland Fire Team Awareness Kit (WFTAK) displays with standardized symbology

### NightFOX Wildfire Detection Payload
- **Spatial resolution**: ~25-meter pixel size (vs. 375m from NOAA VIIRS satellite)
- **Spectral bands**:
  - Visible: FLIR Duo R, 90° × 51° FOV, 1920 × 1080 pixels
  - SWIR (1.0-1.6 µm): Custom camera, 23° × 23° FOV, 64 × 64 pixels
  - Near IR (1.6 µm): Custom scanning scope, 1° FOV, ±30° scan across flight track
  - Mid IR (4 µm): Custom scanning scope, 1° FOV, ±30° scan across flight track
  - Thermal IR (7.5-13.5 µm): FLIR Duo R, 57° × 44° FOV, 160 × 120 pixels
- **Capabilities**: Fire radiative power measurement, fireline delineation, hotspot identification, combustion dynamics quantification
- **Prior validation**: Demonstrated on 2019 Rabbit Mountain prescribed burn and Granite Gulch Fire; VIIRS comparison validated superior spatial resolution and temporal responsiveness
- **Integration**: Data streams available as video in near real-time to operators via S2 Ground Station

### Airspace Awareness System
- **ADS-B Display**: Real-time target icons showing position (lat/lon), altitude AGL, speed, direction vectors, target classification
- **Remote ID Display**: Target classification distinguishing Forest Service assets from unauthorized drones
- **Data Processing**: All detected targets appear in standardized WFTAK interface with detection method, confidence level, time since last update
- **Communications Architecture**: Mesh network capability across multiple S2 aircraft; ground stations receive via cellular, satellite, or line-of-sight radio with automatic failover

## Use Cases & Applications

### Primary Wildfire Applications
1. **Fireline Monitoring**: Continuous tracking of fire front position, rate of spread, direction of movement; enables dynamic suppression planning, identifies control lines, escape routes, staging areas, structure protection priorities
2. **Fire Behavior Tracking**: Real-time hotspot and flare-up detection; multispectral data supports scientific analysis of combustion dynamics and tactical decision-making
3. **Unauthorized Drone Detection**: Proactive airspace management to prevent collision hazards; shifts from reactive aircraft grounding to early warning system

### Operational Scenarios Addressed
- **Critical Need Response**: Addresses 2025 wildfire season incidents (Palisades Fire collision, Park Fire, Fairview Fire, Bridge Fire, Manitoba wildfire)
- **Multi-Aircraft Coordination**: Persistent overwatch without interference with water/retardant drops, rotorcraft bucket operations
- **Smoke-Degraded Visibility**: Infrared sensing penetrates smoke obscuration; superior to ground or optical observation
- **Large Operations Area Monitoring**: Incident Command situational awareness across complex, dynamic airspace with multiple asset types

## Key Results (for reports)

### NightFOX Validation Flight (August 20, 2025, Pawnee National Grasslands)
- Successfully generated multispectral imagery at 400m and 800m AGL
- Covered 45 square kilometers in 50-minute flight
- All image products streamed as video in near real-time to operator
- Calibration verification confirmed proper sensor operation
- Demonstrated feasibility in wildfire-like environment

### UAS Detection System Demonstrations
- **ADS-B Collection**: S2 successfully tracked multiple ground-based and airborne targets simultaneously; position data accurately relayed to WFTAK displays
- **Remote ID Detection**: Effective detection range exceeding 1 kilometer under typical field conditions (Figure 6 validation with DJI Mavic drones)
- **RF Signal Detection**: Laboratory testing and flight demonstration confirmed ability to identify drone signals at distances exceeding 1 kilometer
- **TAK Integration**: All detection data successfully integrated into standard WFTAK displays with real-time updates and standardized symbology

### Persistence Demonstration (August 20, 2025, Sunny Slope Sod Farm)
- Two sequential 30-minute S2 flights executed on-station handover procedure
- Maintained continuous monitoring throughout handover
- Validated deconfliction protocols based on altitude, lateral separation, time-based scheduling
- Confirmed scalability to operational wildfire scenarios

### Operational Impact Assessment
- **Aviation Safety**: Prevents aircraft collisions (Palisades Fire incident: DJI Mini 3 punctured Super Scooper wing)
- **Suppression Effectiveness**: Reduces aircraft downtime from emergency groundings; enables continuous initial attack period monitoring
- **Cost-Effectiveness**: Prevented incidents save millions in aircraft replacement and operational delay costs

## Persistent Coverage Support Calculator Results

**Resource Requirements Framework** (for either NightFOX monitoring or rogue drone detection):

All three sensor types (NightFOX, Remote ID Receiver, RF Signal Detector) have ~1 sq km footprint with similar coverage patterns. Resource estimates vary by:
- **Revisit Time Objective**: Elapsed time between consecutive sensor scans of given location
- **Operations Area Size**: Incident-specific perimeter requiring coverage
- **Temporal Requirement**: Day-only vs. 24-hour operations (doubles operators if continuous)

**Key Assumptions**:
- Beyond Visual Line of Sight (BVLOS) authorization obtained
- Day-only operations (24-hour requires doubled staffing)
- Framework defines coverage by revisit time, not simultaneous area coverage
- Maximum 30 km distance: takeoff/landing site to operations area (datalink limitation)

**Scalability**:
- Single Aircraft: Localized airspace awareness for smaller incidents
- Multiple Aircraft: Distributed sensor network for large complex fires
- 20-30 equipped S2 aircraft could provide nationwide coverage for high-priority incidents

## Notable Details

### Historical Validation
- **2019 Rabbit Mountain Prescribed Burn**: NightFOX successfully collected fire radiative power measurements, validating ability to capture wildfire energy release rates from UAS platform
- **2019 Granite Gulch Fire**: VIIRS comparison confirmed NightFOX advantage in spatial resolution and temporal responsiveness

### Operational Safety Incidents Referenced
- **Palisades Fire, Los Angeles (January 9, 2025)**: DJI Mini 3 collided with Super Scooper aircraft, punctured wing, forced grounding. Incident Commander Anthony Marrone: "A small drone hit the wing... it put a hole in the wing... it's grounded now."
- **California Incidents (2024-2025)**: Park Fire, Fairview Fire, Bridge Fire—repeated aircraft groundings due to unauthorized drone operations
- **Manitoba Wildfire (May 2025)**: Unauthorized drones forced water bomber grounding for 6+ hours

### Integration Framework
- **WFTAK Integration**: Seamless data display with standardized icons, real-time updates
- **Air Attack Coordination**: Strict adherence to deconfliction protocols through established air attack channels
- **Incident Command Support**: Provides unprecedented situational awareness showing all authorized assets, unauthorized drone locations, safe corridors, real-time conflict assessment

### Competitive Advantages Highlighted
- Superior spatial resolution vs. satellite (25m vs. 375m pixels)
- Extended Remote ID detection range vs. ground-based systems (1-1.3 km vs. 400-1,000m)
- Multi-sensor integration (ADS-B + Remote ID + SDR) on single airborne platform
- Proactive vs. reactive airspace management paradigm
- Persistent endurance capability (up to 2 hours; extendable with procedure)

### Deployment Recommendations
- **Immediate Actions**: Pilot program on 2-3 high-risk incidents during season; training integration; stakeholder coordination
- **Scaling**: 20-30 S2 aircraft for nationwide high-priority incident coverage; regional maintenance support
- **Cost-Benefit**: Prevented aircraft collisions and avoided suppression delays justify system costs

### Technical Limitations/Constraints
- Datalink range limit: 30 km from takeoff/landing site
- Endurance: ~2 hours with NightFOX payload
- Remote ID detection realistic range: 1-1.3 km (theoretical up to 5 km)
- Day-only operation baseline (24-hour requires personnel doubling)