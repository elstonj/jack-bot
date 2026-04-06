# Black Swift Technologies Statement of Work (SOW) July 1 2023 – June 30 2024

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration) - Office of Atmospheric Research (OAR) and Office of Marine and Aviation Operations (OMAO); Hurricane Research Division of the Atlantic Oceanographic Meteorological Lab (AOML)
- Program/Solicitation: NOAA tropical cyclone research advancement; WP-3D hurricane sUAS deployment program
- Date: 14 July 2023 (effective 1 July 2023 – 30 June 2024, with Year 2 extending to 30 June 2025)
- BST Products/Systems Referenced: S0 sUAS platform (primary), partnerships with Area-I Altius 600
- Key Personnel: Dr. Joseph Cione (GPC, NOAA/AOML/HRD), Dr. Jun Zhang (UPC, University of Miami/CIMAS), Meredith Needham (document editor)

## Executive Summary
This SOW contracts Black Swift Technologies to design, build, test, and deliver fully-integrated meteorological/oceanographic (METOC) payload-equipped small unmanned aircraft systems (sUAS) for tropical cyclone research. The project builds on successful hurricane deployments (2014-2022) by expanding sUAS duration, communication range, and data reliability, with goals of achieving multi-hour flight duration, 150 nm command & control range, and continuous real-time data transmission to support NOAA operational hurricane intensity models and boundary layer research.

## Technical Approach

**Core Mission Concept:**
- Air-deployable sUAS launched from NOAA WP-3D aircraft via free-fall chute into hurricane environments
- Autonomous flight execution with pre-programmed mission profiles
- Real-time telemetry and payload data transmission to WP-3D up to 150 nm range
- Expendable/unrecoverable platform designed for severely turbulent TC conditions

**Key Technical Requirements:**
- Multi-hour endurance (minimum 1.25 hours demonstrated)
- Radio line-of-sight C2 link with 150 nm range capability; maximum 1-minute telemetry loss tolerance
- Launch envelope: minimum 5,000'–15,000' altitude (preferred 3,500'–16,000'), at 210–250 KIAS aircraft speed
- Autonomous operation with user-selectable mission profiles pre-deployment
- Emergency flight termination capability
- Integration with NOAA real-time data systems (AirOPS, WMO HDOBS formatting, WMO/NHOP Vortex Data Message compliance)
- Payload data transmission to maximum extent possible within bandwidth limitations

**Design & Testing Phases:**
- Preliminary Design Review (PDR) to establish allocated baseline
- Critical Design Review (CDR) at subsystem and system level before fabrication
- Calibration Missions (CM): clear-air, low-wind test flights to validate P-3/sUAS range, endurance, payload performance, and safety compliance before storm deployment
- Hurricane environment capability demonstration: survival and flight maintenance in wind speeds >65 knots with heavy rain and severe turbulence

## Products & Capabilities Described

### Black Swift Technologies S0 sUAS Platform
- **What it is:** A small unmanned aircraft system designed for air deployment from WP-3D and rapid atmospheric sampling in hurricane boundary layers
- **Specifications & Performance Claims:**
  - Multi-hour endurance (≥1.25 hours demonstrated with payload)
  - 150 nm command & control range
  - Deployable from 5,000'–15,000' altitude (preferred 3,500'–16,000')
  - Autonomous flight capability with pre-programmed profiles
  - Capable of sustained flight in hurricane conditions (>65 knot winds)
- **Payload Integration:** Fully integrated METOC sensor package (see below)
- **Quantities to Deliver:** 20 total S0 platforms across 2-year project (16 with full METOC payload + integration support)
  - 4 platforms delivered by 21 Feb 2024
  - 12 platforms delivered by 31 July 2024

### METOC (Meteorological/Oceanographic) Payload
**Core Sensor Package:**
- **Pressure, Temperature, Humidity (PTH) Sensor:** NCAR NRD41 dropwindsonde package for collecting and transmitting pressure, temperature, and humidity data; also provides wind components (horizontal and vertical) via integration with sUAS autopilot data
- **Infrared (IR) Sensor:** Downward-looking for Sea Surface Temperature (SST) and cloud-top measurement; Government recommendation: Melexis InfraRed Thermometer (PN: MLX90614); telemetry ingested and transmitted by NRD41 via existing auxiliary data input
- **Altimeter:** Viable laser or radar altimeter for accurate vertical platform position above surface
- **Multi-Hole Turbulence Probe (MHTP):** 
  - Designed, tested, and integrated to measure 3D wind components (u, v, w)
  - Minimum 5 Hz sampling frequency
  - 2 MHTP platforms to be built for integration on Area-I Altius 600 sUAS (delivery 31 April 2024)
- **Video/Image Capability:** Short burst video and/or still image capture explored; loss of other METOC payload data during video/image capture is acceptable if necessary

**Performance Validation Tolerances (Post-Flight Analysis Guidance):**
- Geographic Position: Aircraft ±3 nm; storm surface center ±6 nm; flight level ±6 nm
- Wind Direction: Surface ±10°; flight level (>20 kt winds) ±5°
- Wind Speed: Surface ±10 kt; flight level ±4 kt
- Pressure Height: Surface ±2 mb; flight level ≤500 mb ±10 m; >500 mb ±20 m
- Temperature: Sea surface ±1°C; flight level ±1°C
- Dew-Point Temperature: 20°C to +40°C ±1°C; <20°C ±3°C
- Absolute Altitude: ±10 m
- 3D Wind Data: Minimum 5 Hz resolution from MHTP
- Video/Image: Clear capture and transfer to P-3 demonstrated

### Flight Control Station (FCS)
- Ground-based system for sUAS command & control and telemetry reception
- Rack-installed radio and computer equipment, antennas, power/data cables
- To be installed on WP-3D in AOC-compliant configuration
- Contractor to propose mechanical, electrical, and data integration solutions reviewed at PDR
- Primary link aircraft antenna to be provided by contractor per AOC specifications

## Use Cases & Applications

**Primary Mission:** Tropical cyclone (hurricane) boundary layer research and measurement
- **Specific Applications:**
  - Measure surface air/sea interaction processes to improve hurricane intensity prediction models
  - Target areas of storms that manned aircraft cannot safely sample
  - Collect critical boundary layer data in extreme wind conditions

**Historical Context & Precedent:**
- Successful deployments into Hurricanes Edouard (2014), Maria (2017), Michael (2018), and Ian (2022)
- Hurricane Michael (October 2018): Recorded 183 mph wind gust at 2,000 feet above ocean
- Hurricane Ian (September 28, 2022): ALTUIS 600 set records for sUAS endurance in TC (102 min), communication distance to P-3 (135 nmi), and recorded wind speed (215 mph)

**Operational Use:**
- Real-time delivery of sUAS METOC data to National Hurricane Center (NHC) and Environmental Modeling Center (EMC) operational centers
- Data integration with NOAA's WP-3D onboard KARMA (situational awareness visualization system)
- Conformance to WMO HDOBS and WMO/NHOP Vortex Data Message (VDM) standards for operational integration

**Field Deployment Schedule (FY2023-2025):**
- Up to two 3-day clear-air calibration missions
- Up to two 5-day in-storm hurricane deployments per year (2023, 2024)
- Deployment locations: Avon Park, FL, other Government-selected sites, or over water warning areas
- Conducted during Atlantic hurricane season (Sep–Nov)

## Key Results (Historical Basis for Current Work)

**Previous Mission Success Record:**
- **2014-2016 Program:** Airborne-launched sUAS successfully deployed from NOAA WP-3D inside Category 3 Hurricane eye; demonstrated viability of air-deployment CONOPS
- **2017 Major Hurricane Maria:** Six sUAS deployed successfully
- **October 2018, Hurricane Michael:** sUAS recorded record-setting 183 mph wind gust at 2,000 feet altitude
- **September 28, 2022, Category 5 Hurricane Ian (ALTUIS 600):**
  - 102-minute endurance (sUAS endurance record in TC environment)
  - 135 nm communication distance to deployment P-3 (communication distance record)
  - 215 mph recorded wind speed (wind speed record)

**Scientific Value:**
- Data collection from boundary layer regions previously under-sampled
- Critical inputs to improving NOAA operational TC intensity models
- Demonstrated proof-of-concept for expendable, targeted sUAS as force-multiplier for manned research aircraft

## Notable Details

**Project Goals & Advancement Objectives:**
1. Measurable increase in sUAS flight duration (target: multi-hour capability)
2. Enhanced communication robustness and continuous range of operation (target: 150 nm)
3. Improved payload data reliability and capability (3D turbulence measurements, video)
4. Advancement to higher technical maturity level for routine operational deployment
5. Routine collection of valuable METOC data in TC boundary layer environment

**Government-Provided Support:**
- Validation using Government-launched dropwindsondes and remote systems
- NOAA AOC provides mechanical/electrical/data integration specifications for FCS and antenna
- Dr. Joseph Cione (GPC) and Dr. Jun Zhang (UPC) available for technical SME guidance

**Partnerships:**
- **Area-I Altius 600:** Complementary platform; BST to build and help integrate 2 MHTP for Altius 600 deployments (residual NRE included)
- **NCAR:** Existing integration of Melexis IR sensor and NRD41 dropwindsonde package analyzed by NCAR

**Real-Time Data Integration Requirements:**
- AirOPS data management system compatibility
- WMO HDOBS formatting conversion
- WMO/NHOP compliant Vortex Data Message (VDM) generation
- KARMA onboard visualization system integration

**Cost & Resource Allocation:**
- **Total Project Budget (2023–2025):** $390K
  - Year 1 (1 July 2023–30 June 2024): $260K
    - $110K NRE; $20K Area-I MHTP; $18K travel; $112K sUAS hardware
  - Year 2 (1 July 2024–30 June 2025): $130K
    - $12K travel; $112K sUAS hardware; $6K project documentation
- **Hardware Breakdown:**
  - 16 BST S0 sUAS platforms with integrated METOC payload: $224K
  - 2 MHTP for Altius 600: $20K
  - Engineering support (payload integration, automation, real-time data, video): $110K
  - Travel & in-field support (calibration missions, 4 hurricane deployments): $30K
  - Documentation: $6K

**Deliverable Timeline:**
- 31 July 2023: Coordination & analysis from March 2023 Florida sensor calibration/integration missions
- 1 Sep–30 Nov 2023: Two 5-day hurricane field deployments with real-time HDOBS data to NHC/EMC
- 21 Feb 2024: 4 S0 platforms delivered
- 1–21 March 2024: Payload calibration/TC lessons learned missions
- 31 April 2024: 2 MHTP for Altius 600 delivered
- 31 July 2024: 12 additional S0 platforms delivered
- 1 Aug–30 Nov 