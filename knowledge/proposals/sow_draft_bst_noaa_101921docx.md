# NOAA/Black Swift Technologies Statement of Work (SOW) FY21-24

## Document Metadata
- Type: Statement of Work (Draft)
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration) - Office of Atmospheric Research (OAR), Hurricane Research Division, Atlantic Oceanographic Meteorological Lab (AOML)
- Program/Solicitation: Tropical cyclone research advancement; air-deployable sUAS for hurricane boundary layer research
- Date: 19 October 2021 (draft); modified January 7, 2022
- BST Products/Systems Referenced: Black Swift Technologies S0 sUAS (16 units planned)
- Key Personnel: Dr. Joseph Cione (NOAA/AOML/HRD - Government Point of Contact), Dr. Jun Zhang (University of Miami/CIMAS - University Point of Contact), Jack Elston (BST - last document editor)

## Executive Summary
This SOW establishes a multi-year contract (FY21-24) between NOAA and Black Swift Technologies to design, build, test, and deliver 16 fully-integrated meteorological/oceanographic (METOC) payload-equipped small unmanned aircraft systems (sUAS) for deployment from NOAA WP-3D aircraft into tropical cyclones. The project builds on previous successful deployments into Hurricanes Edouard (2014), Maria (2017), and Michael (2018), aiming to advance sUAS duration, communication robustness, and data reliability to enable routine operational collection of boundary layer data within hurricane environments.

## Technical Approach

**Core Concept of Operations (CONOPS):**
- Air-deployed, expendable sUAS launched from NOAA WP-3D manned research aircraft
- Launched via free fall chute using air pressure-activated mechanism
- Designed for autonomous operation in severe tropical cyclone environments
- Multi-hour duration flight with continuous command & control link to parent aircraft

**Launch System:**
- Design and build launch tube and release mechanism for WP-3D cabin deployment
- Launch altitude envelope: minimum acceptable 5,000-15,000 ft; preferred 3,500-16,000 ft
- Designed for 250 knots indicated airspeed (KIAS); demonstrate reliable launch at 210 KIAS

**Flight Autonomy & Control:**
- Capable of autonomously executing one of at least three pre-programmed flight profiles without pilot input
- Pilot ability to switch to heading/altitude override mode during flight
- Emergency flight termination capability
- Radio line-of-sight C2 link with 150 nautical mile range capability
- Maximum C2 telemetry loss not to exceed 1 minute duration

**Payload Integration:**
- Pressure-Temperature-Humidity (PTH) sensors from NCAR NRD41 dropwindsonde package for environmental wind measurement (horizontal and vertical components)
- Downward-looking Infrared (IR) sensor (Melexis MLX90614 recommended) for sea surface temperature (SST) and cloud top data
- Laser or radar altimeter for accurate vertical platform positioning
- Multi-hole turbulence probe (MHTP) designed to measure 3D wind components (u,v,w) at ≥5 Hz
- Video capability (short burst format)
- Real-time data transmission via C2 link
- Data conversion to WMO HDOBS formatting and WMO/NHOP compliant Vortex Data Message (VDM) format

**Flight Control Station (FCS):**
- Ground-based command and control system with rack-installed radio and computer equipment
- Antenna systems for primary and satellite C2 link
- Designed for integration on WP-3D with AOC specifications for mechanical, electrical, and data integration
- Integration with NOAA's KARMA (P-3 onboard situational awareness visualization system)

**Performance Requirements:**
- Minimum 1.5-hour flight duration with payload installed
- Capability to survive and maintain flight in hurricane environment with one-minute averaged wind speeds >65 knots, heavy rain, and severe atmospheric turbulence
- Demonstrated operation across multiple pre-deployment calibration and dummy missions

## Products & Capabilities Described

### Black Swift Technologies S0 sUAS
- **Definition:** Small unmanned aircraft system equipped with integrated METOC payload
- **Quantity:** 16 units to be delivered across project timeline
- **Key Specifications:**
  - Deployable from NOAA WP-3D via air-pressure-actuated free fall chute
  - Multi-hour endurance (≥1.5 hours with payload)
  - 150 NM command & control range
  - Autonomous flight with pilot override capability
  - Designed for tropical cyclone environments with extreme turbulence and precipitation
- **Payload Integration:** Fully integrated PTH sensors, IR camera, laser altimeter, turbulence probe, video capability
- **Cost:** $160K for 16 platforms with fully integrated payloads

### Multi-Hole Turbulence Probe (MHTP)
- **Definition:** 3D wind measurement probe designed for measuring turbulence characteristics
- **Capability:** Measures u, v, w wind components at frequencies ≥5 Hz
- **Integration:** Designed for both BST S0 sUAS and Area-I Altius 600 sUAS platforms
- **Quantity:** 10 MHTPs for Area-I Altius 600; delivered in phases (2 by March 31, 2023; 8 by June 30, 2023)
- **Cost:** $80K for 10 MHTP units

### Flight Control Station (FCS)
- **Definition:** Ground-based command and control infrastructure
- **Components:** Rack-installed radio and computer equipment, primary and satellite C2 antennas, power/data cables, integration with KARMA visualization system
- **Integration:** Designed for WP-3D aircraft installation per AOC specifications
- **Cost:** Included within engineering support budget

## Use Cases & Applications

**Primary Mission: Hurricane Boundary Layer Research**
- Deploying from NOAA WP-3D into tropical cyclone environments to measure boundary layer properties
- Targeted sampling of storm regions inaccessible to manned aircraft
- Advance understanding of air/sea interaction processes affecting hurricane intensity

**Specific Historical Success Cases:**
- Hurricane Edouard (2014): First successful sUAS deployment from WP-3D inside Category 3 hurricane eye
- Hurricane Maria (2017): Six sUAS deployed
- Hurricane Michael (2018): sUAS recorded 183 mph wind gust at ~2,000 feet above ocean surface

**Planned 2022-2023 Operations:**
- Two (2) clear-air calibration/dummy missions (2022 and 2023)
- Tropical cyclone field deployments: August 1 - November 30, 2022 and 2023
- Calibration window: May 17-31, 2022 and as needed in 2023

**Supporting Research:**
- Validation against government-launched dropwindsondes and other remote systems
- METOC data collection for operational model improvement (hurricane intensity prediction)
- Contribution to NOAA situational awareness and operational decision-making

## Key Results (Applicable Sections)

No results are provided in this draft SOW. This document establishes requirements and timelines for future execution. However, historical context notes:

**Previous Success Metrics (2014-2018):**
- Successful deployment and recovery operations in three major hurricanes
- Record wind measurement of 183 mph at ~2,000 feet altitude (Hurricane Michael, 2018)
- Validation that air-deployed sUAS CONOPS is operationally viable
- Critical data collection addressing previously under-sampled storm boundary layer region

## Performance Validation Criteria

**METOC Sensor Package Tolerances (Guidance for Post-Flight Analysis):**

| Parameter | Requirement | Tolerance |
|-----------|-------------|-----------|
| **Geographic Position** | | |
| Aircraft position | | ±3 nm |
| Storm surface center (wind/pressure) | | ±6 nm |
| Flight level storm center (wind/pressure) | | ±6 nm |
| **Wind Direction** | | |
| Surface | | ±10° |
| Flight level (winds >20 kt) | | ±5° |
| **Wind Speed** | | |
| Surface | | ±10 knots |
| Flight level | | ±4 knots |
| **Pressure Height** | | |
| Surface | | ±2 mb |
| Flight level ≤500 mb | | ±10 m |
| Flight level >500 mb | | ±20 m |
| **Temperature** | | |
| Sea surface | | ±1°C |
| Flight level | | ±1°C |
| **Dew-Point Temperature** | | |
| 20°C to +40°C | | ±1°C |
| <20°C | | ±3°C |
| **Absolute Altitude** | | ±10 m |
| **Video** | Clear capture and transfer to P-3 | TBD duration |

## Notable Details

**Partnership & Integration Points:**
- Collaboration with Area-I (supplier of Altius 600 sUAS platform for separate but related turbulence probe development)
- Integration with NCAR's NRD41 dropwindsonde package and sensors
- Melexis IR thermometer (MLX90614) as specified sensor for SST measurement
- Integration with NOAA's KARMA real-time visualization system and WMO data standards (HDOBS, VDM)

**Project Timeline Highlights (2021-2023):**
- S0 PDR: January 31, 2022
- S0 CDR: March 31, 2022
- Initial 2-unit delivery: April 30, 2022
- 2022 calibration missions: May 17-31, 2022
- 2022 hurricane deployment: August 1 - November 30, 2022
- 6-unit delivery: July 31, 2022
- 2023 final 6-unit delivery: July 31, 2023
- 2023 hurricane deployment: August 1 - November 30, 2023

**Cost Breakdown (FY21-24 Total: $476K):**
- Hardware (16 S0 sUAS + 10 MHTP): $240K
- NRE & Program Support: $176K (payload integration, automation, data requirements, MHTP design/build)
- Travel & In-Field Support: $60K (4 calibration missions + 3 in-storm deployments)
- Distributed across 3 fiscal years: $150K (Year 1), $251K (Year 2), $75K (Year 3)

**Operational Requirements Addressed:**
- Real-time data delivery to NOAA operational systems (KARMA integration)
- WMO-compliant data formatting for operational meteorological use
- Safety of operation certification for extreme tropical cyclone environment
- Autonomous flight capability for areas of storm inaccessible to manned aircraft
- Expendable/unrecoverable system design philosophy for cost-effective deployment

**Testing & Validation Gates:**
- Preliminary Design Review (PDR) and Critical Design Review (CDR) with government oversight
- Mass-equivalent dummy missions for separation/launch viability verification
- Clear-air calibration missions before any hurricane deployment
- Post-mission performance reporting and validation against government reference systems