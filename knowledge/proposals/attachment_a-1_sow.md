# Statement of Work (SOW) - Black Swift Technologies FY21-24

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration) - Office of Atmospheric Research (OAR) and Office of Marine and Aviation Operations (OMAO)
- Program/Solicitation: Hurricane Research Division project; NOAA/AOML/HRD tropical cyclone research advancement
- Date: 9 November 2021
- BST Products/Systems Referenced: S0 sUAS (small Unmanned Aircraft System)
- Key Personnel: Dr. Joseph Cione (NOAA/AOML/HRD - Government Point of Contact); Dr. Jun Zhang (University of Miami/CIMAS - University Point of Contact); Jack Elston (BST - last editor)

## Executive Summary
This SOW formalizes a multi-year (FY21-24) agreement between Black Swift Technologies and NOAA to design, build, test, and deliver fully-integrated meteorological/oceanographic (METOC) payload-equipped sUAS platforms for tropical cyclone research. The project builds on successful deployments into Hurricanes Edouard (2014), Maria (2017), and Michael (2018), aiming to expand sUAS duration, communication robustness, and data reliability to enable routine measurement of critical hurricane boundary layer phenomena currently under-sampled by manned aircraft.

## Technical Approach

**System Concept:**
- Air-deployable small Unmanned Aircraft Systems launched from NOAA WP-3D aircraft using pneumatic free-fall chute deployment
- Multi-hour endurance platforms capable of autonomous operation in severe hurricane conditions
- Continuous command and control (C2) link with 150 nautical mile range capability
- Real-time meteorological and oceanographic data transmission to WP-3D during flight

**Key Technical Requirements:**
1. **Launch System**: Pneumatic launch tube and release mechanism for cabin deployment from WP-3D
2. **Launch Envelope**: Minimum acceptable 5,000-15,000 feet; preferred 3,500-16,000 feet
3. **Aircraft Speed**: Designed for 250 KIAS; demonstrated capability at 210 KIAS minimum
4. **Flight Duration**: Minimum 1.5 hours with full payload installed
5. **Command & Control**: 150 nm range capability; maximum C2 telemetry loss not to exceed 1 minute
6. **Flight Automation**: Autonomous execution of at least 3 pre-programmed flight profiles with in-flight mode override capability
7. **Environmental Capability**: Survive and maintain flight in hurricane-force winds (>65 knots one-minute average) with heavy rain and severe turbulence
8. **Expendable Design**: Platform treated as unrecoverable/expendable technology

## Products & Capabilities Described

### S0 sUAS (Black Swift Technologies)
**What it is**: Small unmanned aircraft system equipped with integrated METOC payload, designed for air deployment from manned research aircraft.

**Integration & Payload**:
- **Pressure/Temperature/Humidity (PTH)**: NCAR NRD41 dropwindsonde package sensors for P, T, H measurement and wind calculation
- **Infrared Sensor**: Downward-looking for sea surface temperature (SST) and cloud top measurement (recommended: Melexis InfraRed Thermometer PN MLX90614)
- **Altitude Measurement**: Laser or radar altimeter for precise vertical position above surface
- **3D Wind/Turbulence Probe**: Contractor-designed turbulence probe measuring u, v, w wind components at 5Hz or greater frequency
- **Video Capability**: Short burst video capture capability for selected units
- **Data Transmission**: All payload data transmitted via C2 link; data formatted to WMO HDOBS protocols and WMO/NHOP compliant Vortex Data Message (VDM) format

**Specifications/Performance**:
- Delivery quantity: 16 total S0 platforms over project timeline
- Phased delivery: 2 units (April 2022), 6 units (July 2022), 6 units (July 2023), plus 2 additional MHTP-equipped units (April 2023)
- Flight duration: ≥1.5 hours with payload
- Wind capability: Designed to operate in >65 knot sustained winds

### Multi-Hole Turbulence Probe (MHTP)
**What it is**: Specialized probe designed for integration on Altius 600 sUAS (Area-I partnership) for advanced 3D wind and turbulence measurement.

**BST's Role**: Design, build, and deliver 10 MHTPs total
- 2 MHTPs by 31 March 2023
- 8 MHTPs by 30 June 2023

**Capability**: Measures three-dimensional wind components at high frequency (≥5Hz)

### Flight Control Station (FCS)
**What it is**: Ground-based command and control system integrated on NOAA WP-3D aircraft.

**Components**:
- Rack-installed radio and computer equipment
- Radio antennas (primary and satellite C2 link)
- Power and data cables
- Integration with NOAA AOC specifications
- Interface with NOAA's KARMA (Kinetic Analysis and Real-time Management of Atmospheric) situational awareness visualization system

## Use Cases & Applications

**Primary Application**: Tropical cyclone (hurricane) boundary layer research and atmospheric observation

**Specific Missions**:
1. **Calibration Missions (CM)**: Clear air, low-wind test flights evaluating all sUAS operation aspects prior to storm deployment
   - Confirmation of P-3 to sUAS range capability
   - sUAS endurance verification
   - Payload performance validation
   - Safety compliance testing
   - Scheduled: up to 2 per season (May 2022, May 2023)

2. **Dummy Missions (DM)**: Mass and shape equivalent test units to verify clean separation and flight configuration transition from WP-3D launch
   - Two (2) mass-equivalent dummy units
   - External camera or chase aircraft video documentation
   - Precedes operational unit testing

3. **In-Storm Hurricane Deployments**: Real-world operations in tropical cyclone environment during Atlantic hurricane season
   - Scheduled windows: Aug 1 - Nov 30, 2022; Aug 1 - Nov 30, 2023
   - Planned deployment scenarios: 2 five-day in-storm deployments in 2022; 1 five-day in-storm deployment in 2023

**Historical Context**: Platform builds on successful deployments into:
- Hurricane Edouard (2014) - first successful air-deployed sUAS
- Hurricane Maria (2017) - 6 sUAS deployed
- Hurricane Michael (2018) - sUAS recorded 183 mph wind gust at ~2,000 feet AGL

**Data Application**: Supports NOAA's improved tropical cyclone intensity prediction models and situational awareness; targets previously under-sampled hurricane boundary layer phenomena

## Test & Evaluation Requirements

**METOC Sensor Validation Tolerances**:
- **Geographic Position**: Aircraft position ±3 nm; storm center (surface/flight level) ±6 nm
- **Wind Direction**: Surface ±10°; flight level (>20 kt) ±5°
- **Wind Speed**: Surface ±10 kt; flight level ±4 kt
- **Pressure Height**: Surface ±2 mb; flight level ≤500 mb ±10 m; >500 mb ±20 m
- **Temperature**: Sea surface ±1°C; flight level ±1°C
- **Dew-Point Temperature**: 20°C to +40°C ±1°C; <20°C ±3°C
- **Absolute Altitude**: ±10 m
- **Video Capture**: Clear video capture and transfer to P-3; minimum duration TBD

**Review Gates**:
- **Preliminary Design Review (PDR)**: On or before 31 January 2022
  - Establishes allocated baseline before detailed design
  - First opportunity for Government to review hardware/software design
- **Critical Design Review (CDR)**: On or before 31 March 2022
  - Multi-disciplined technical review for fabrication readiness
  - Potential CDR #2: on or before 31 March 2023
  - May conduct subsystem-level CDRs culminating in system-level CDR

**Government Validation**: NOAA will use Government-launched dropwindsondes and remote systems to validate sUAS measurements

## Project Deliverables Timeline (FY21-24)

### 2021-2022
- Coordination completion: 31 August 2021
- S0 PDR: 31 January 2022
- NRE completion (payload integration, safety, automation, KARMA, WMO formatting): 28 February 2022
- S0 CDR: 31 March 2022
- Deliver 2 field-ready S0 sUAS with payload, laser altimeter, MHTP: 30 April 2022
- Dummy Missions and Calibration Missions: 17-31 May 2022
- Deliver 6 field-ready S0 sUAS with payload: 31 July 2022
- Hurricane field deployment: 1 August - 30 November 2022

### 2022-2023
- Lessons-learned NRE and VDM generation: 28 February 2023
- Area-I Altius 600 MHTP design and build completion: 31 March 2023
- Deliver 2 MHTPs to Area-I: 31 March 2023
- Optional CDR #2: 31 March 2023
- Deliver 2 field-ready, MHTP-equipped S0s with video: 30 April 2023
- Optional second Calibration Mission: 31 May 2023
- Area-I Altius 600 MHTP Calibration Mission support: 31 May 2023
- Deliver 8 MHTPs to Area-I: 30 June 2023
- Deliver 6 field-ready, MHTP-equipped S0s with video: 31 July 2023
- Hurricane field deployment: 1 August - 30 November 2023

## Financial Summary (FY21-23)

**Hardware Costs**:
- 16 BST S0 sUAS platforms (full METOC payload integration): $160,000
- 10 Multi-Hole Turbulence Probes (Area-I Altius 600 integration): $80,000

**Non-Recurring Engineering & Program Support**:
- S0 payload integration, flight enhancement, automation, KARMA integration, WMO HDOBS/VDM compliance, video integration, MHTP NRE: $161,000
- Project Documentation: $15,000

**Travel & Field Support**:
- 2 Clear-Air S0 Calibration Flights (2022, 2023): $20,000
- 1 Clear-Air Area-I MHTP Flight (2022): $10,000
- 3 In-Storm Hurricane Deployments (2 in 2022, 1 in 2023): $30,000

**Total Project Cost (FY21-23)**: $476,000
- Year 1 Available: $150,000
- Year 2 Available: $251,000
- Year 3 Available: $75,000

## Notable Details

**Partnership**: Collaboration with Area-I for integration of BST-developed Multi-Hole Turbulence Probes on Area-I's Altius 600 sUAS platform

**Data Standards Compliance**: 
- WMO HDOBS (High-Density Observation) data formatting protocols
- WMO/NHOP (Vortex Data Message) compliant output generation
- Integration with NOAA AOC's KARMA situational awareness system

**Safety & Operational Compliance**:
- Full safety of operation engineering required
- Real-time data delivery requirements per NOAA/AOC specifications
- Mechanical, electrical, and data integration per AOC standards for WP-3D aircraft integration

**Expendable Platform Concept**: Explicit design assumption that sUAS are unrecoverable/expendable, enabling deployment into extremely hazardous hurricane environments that manned aircraft cannot safely sample

**Previous Success Validation**: Hurricane Michael deployment validated record extreme wind measurement (183 mph at ~2,000 ft AGL