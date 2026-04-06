# 2019-07-14 Volcano Project Overview

## Document Metadata
- Type: Project Overview Presentation
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II (NNX16CP42P)
- Date: July 14, 2019
- BST Products/Systems Referenced: S2 (fixed-wing UAS), SwiftStation, SwiftPilot, SwiftCore, SwiftTab
- Key Personnel: Jack Elston (last editor), Dr. Dave Pieri (JPL Technical Monitor)

## Executive Summary
This presentation documents BST's volcano monitoring mission capabilities using the S2 UAS platform, specifically for scientific data gathering at Makushin volcano in Alaska. The project builds on previous successful volcano deployments in Costa Rica (ELEVATE) and Hawaii, and proposes a comprehensive mission combining trace gas measurements, terrain modeling, and thermal imagery in a harsh, remote environment requiring BVLOS operations.

## Technical Approach

### System Architecture
- **Primary Aircraft**: S2 fixed-wing UAS with electric propulsion, purpose-built for scientific payloads in demanding environments
- **Ground Station**: SwiftStation with SwiftPilot autopilot system, SwiftTab tablet interface
- **Communications**: Primary 900 MHz radio link with Iridium satellite backup for BVLOS operations
- **Launcher**: Pneumatic catapult system (145 PSI firing pressure, 1300 PSI tank burst pressure, >100 validation firings)

### Mission Design
**Flight Operations:**
- Visual line-of-sight (LOS) and BVLOS capability with FAA SWIM feed integration
- Real-time telemetry through Iridium backup communications
- Terrain-aware flight planning using digital elevation models (DEMs)
- Gas flux estimation via lateral plume traverses at 400' AGL or lower
- Mapping missions up to 1 sq km at 400' AGL depending on battery margin
- Applied for Part 107 BVLOS Waiver; primary plan is NASA Certificate of Authorization (COA)

**Air Traffic Coordination:**
- Contact list coordination with local Dutch Harbor operators
- Live telemetry available to airport if desired
- Phone briefings with local operators before/after missions
- Proposed COA area maintains LOS radio link while avoiding 3 NM restricted circle around airport

### Flight Endurance Analysis
- **Cruise Power**: 353W (VTOL)
- **Takeoff/Landing Power**: 2400W
- **Battery Capacity**: 610Wh (10% reserve withheld)
- **Payload Average Power**: 30W
- **Makushin Mission Profile**: 28 km one-way range, 2400 m altitude gain, up to 17 m/s crosswind
- **Predicted Mapping Capability**: 0.7 sq km at 80% battery utilization with 5 lb payload
- **Flight Time**: 90 minutes nominal at 6,000 ft density altitude

## Products & Capabilities Described

### S2 Aircraft Specifications
- **Configuration**: Fixed-wing electric UAS, pneumatic rail launch with belly landing
- **Dimensions**: 3.0 m (10 ft) wingspan
- **Maximum Gross Takeoff Weight**: 9.5 kg (21 lbs)
- **Payload Capacity**: 
  - Max weight: 2.3 kg (5 lbs)
  - Nose cone: 20.3 cm (8 in) diameter, 63.2 cm (24.9 in) length
  - Power available: 50 W total
- **Performance**:
  - Stall speed: 12 m/s (24 kts)
  - Cruise speed: 19 m/s (37 kts)
  - Flight ceiling: 4,500 m (15,000 ft)
  - Maximum wind endurance: 15 m/s (30 kts)
  - Range: 101 km (55 nm) nominal
  - Load ratings: -1.5G to +3.8G sustained; -4.2G to +6.2G gust
- **Environmental**: IP42 ingress protection
- **Downlink Data Rate**: 9,500 bps serial stream
- **Fleet**: Two aircraft deployed
  - S20003 (FA3TNAPYAY): 76 flights, 18 hours
  - S20009 (FA3XLE9TFX): 2 flights, 0.8 hours

### SwiftPilot Autopilot System
- U.S. design and manufacture
- CAN bus distributed architecture for servos and off-board sensors
- Electronic Centralized Aircraft Monitor (ECAM) system with Level 2 (user discretion) and Level 3 (automatic) failure protocols
- Geo-fencing capability
- Lost-link procedures: automatic return to lost-link waypoint, then autonomous landing
- Manual control redundancy via tablet interface independent from autopilot
- Laser altimeter-based flare prior to impact
- Software version tracking via Git

### Payload Integration System
- **Firmware Status** (as of July 14, 2019):
  - Licor CO2/H2O sensor: ~80% complete
  - Trace gas sensors (SO2, H2S): I2C interface integration
  - MAPIR camera: triggering and geotagging ~90% complete
  - MHP wind sensor: onboard data serial stream ~80% complete
  - Spectrometer (FLAME-S): data acquisition and file formatting 80% complete, abbreviated downlink 30% complete
  - Payload power control via CAN bus with tablet UI
  - Payload door control via CAN bus

### Communication Systems

**Primary 900 MHz Radio Link:**
- Custom receiver Yagi antenna (17.1 dBi gain)
- Tested range: 20 km useable communications with <30% packet loss
- Video intermittent at 30 km depending on orientation

**ADS-B Integration:**
- Ping Rx module with custom CAN interface drivers
- On-board alerting of manned aircraft detection and location
- New system specifically designed for this mission

**Iridium Satellite Backup:**
- Designed for minimal integration effort with current autopilot
- Allows fallback if primary 900 MHz link fails
- Hardware, SIM, and custom board already in hand
- Firmware implementation underway (target: end of July testing)

**Heated Pitot Tube:**
- New system designed and built for icing mitigation
- PTC heating element
- Temperature performance: 85°C at 20°C ambient, 41°C at -7°C ambient
- Maximum power consumption: 3.72 W at 5V
- On/Off control via pitot board with fusing for protection

## Payload & Instruments

| Sensor | Measurement | Weight (g) | Max Power (W) |
|--------|-------------|-----------|---------------|
| BST 5-Hole Probe | 3D winds, pressure, temperature, RH | 50 | 0.5 |
| LiCor 850 | CO2 and water vapor (trace) | 1,300 | 4.6 |
| City Tech SO2 | Sulfur dioxide (0-200 ppm) | 17 | 0.1 |
| City Tech H2S | Hydrogen sulfide (0-100 ppm) | 17 | 0.1 |
| MapIR Kernel | Downward-facing still camera | 62 | 4 |
| FPV Video | Forward-facing video camera | 75 | 6 |
| Ocean Optics FLAME-S | Spectrometer | 265 | 1.25 |
| **TOTAL** | | **1,786 g** | **16.55 W** |

**Payload Integration Notes:**
- Multi-hole probe mounted on top for wind measurements (proven design from previous Hawaii mission)
- Static air inlets/outlets for trace gas sensors (same ports tested on previous volcano payload)
- Tightly integrated GPS and time-tagging for all measurements
- Real-time ground visualization of measurement values
- Wing-mounted FPV video housing with custom receiver Yagi, 30° above horizon view, 1080p60 onboard recording

## Use Cases & Applications

### Previous Deployments
1. **ELEVATE (Costa Rica)**: High-resolution CO2 monitoring above forested vents on active volcano
   - Multiple flights successfully showing CO2 signature
   - Time series plots showing CO2 concentration spikes near vents
   - Flight tracks colorized by CO2 concentration

2. **Phase II SBIR - Hawaii Deployment**: Fissure 8 eruption (2018)
   - Integrated particulate and trace gas measurements with orthomosaic
   - Generated thermal orthomosaic, RGB orthomosaic, elevation data
   - Hot spot detection in areas not visible in RGB imagery
   - Vent identification and characterization
   - 3D wind field mapping

3. **Additional BST Flight Experience**:
   - 8 different missions under NASA AFSRB/FRRB with S2
   - Soil moisture mapping (multiple sites)
   - Landsat calibration (multiple sites)
   - Snow/water equivalent mapping

### Makushin Volcano, Alaska Mission (Proposed)

**Location**: Dutch Harbor/Unalaska, Alaska
- Port of Dutch Harbor as reference point
- Possible takeoff/landing sites: DUT Airport gravel lot (helicopter operations) and Fort Schwatka (2 miles from runway, pending landowner permission)
- Remote location with minimal population density

**Scientific Objectives**:
1. **Volcanic Gas Measurements**:
   - Characterize water vapor (H2O), carbon dioxide (CO2), sulfur dioxide (SO2), and hydrogen sulfide (H2S) relative abundances
   - Determine total SO2 emission rate
   - Calculate emission rates of all primary volatile species
   - Constrain environmental factors: wind speed/direction, relative humidity, temperature, pressure

2. **High-Resolution Terrain Modeling**:
   - Characterize vent geometry, size, and distribution at complex summit topography
   - Create high-resolution baseline data for future deformation measurements
   - Support improved hazardous flow modeling
   - Enable improved geologic mapping
   - Improve infrasound interpretation
   - Understand lahar (volcanic mudflow) potential
   - Quantify ice/snow budget

**Flight Profiles**:
- **Gas Flux Mapping**: Lateral traverses underneath plume at 400' AGL or lower, visually and instrument-guided plume location, terrain-aware via DEMs
- **Terrain Mapping**: Up to 1 sq km coverage at 400' AGL (depending on available battery margin)

**Pilot-in-Command Experience**:
- Over 700 missions with fixed-wing UAS at BST
- Over 500 missions under University COAs
- Team has flown 8 different missions under NASA AFSRB/FRRB with S2

## Safety & Risk Management

### Comprehensive Hazard Analysis
BST identified 15 primary hazards with likelihood/consequence scoring:

**Critical/Catastrophic Risks (Hazards 4, 5, 10):**
1. **Mid-Air Collision**: NOTAM issuance, airport/operator contact, FAA SWIM monitoring, lower altitude operations in remote area
2. **Loss of Command & Control Link**: Pre-programmed lost-link procedures (return to lost-link waypoint, auto-landing), Iridium backup for telemetry/control, manual override via LOS
3. **Lost GPS**: GPS health pre-flight validation, cabling maintenance, manual pilot override if LOS, flare-before-impact using laser altimeter if BVLOS

**Major Risks (Hazards 1, 2, 3, 6, 7, 8, 11, 13, 14, 15):**
- Battery fire mitigation: manufacturer-spec charging, cell-balancing charger with auto fault detection, fire extinguisher on site
- Autopilot loss of control: pre-flight checklists, system testing, manual control link independent of autopilot
- Loss of vehicle electrical power: backup power system, battery voltage pre-flight validation
- Ground station power loss: manual handset control fallback, battery backups available
- Handset power loss: autopilot tablet interface manual control, autonomous landing
- Aircraft crash with fire: ground crew fire extinguisher for immediate mitigation
- Engine out: battery pre-flight checks, flight timers + real-time voltage tracking, routine motor health maintenance
- Structural failure: