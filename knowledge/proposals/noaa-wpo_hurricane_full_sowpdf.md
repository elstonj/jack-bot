# NOAA/Black Swift Technologies Statement of Work (SOW) FY21-24

## Document Metadata
- Type: Statement of Work (SOW) / Contract specification
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration) - Office of Atmospheric Research (OAR) and Office of Marine and Aviation Operations (OMAO)
- Program/Solicitation: Tropical cyclone research advancement; air-deployed sUAS for hurricane boundary layer research
- Date: 19 October 2021 / 5 November 2021 (draft)
- BST Products/Systems Referenced: Black Swift Technologies S0 sUAS (16 units)
- Key Personnel: 
  - Dr. Joseph Cione (NOAA/AOML/HRD - Government Point of Contact)
  - Dr. Jun Zhang (University of Miami/CIMAS - University Point of Contact)
  - Jack Elston (BST - last editor)

## Executive Summary
This SOW establishes a multi-year contract (FY21-24) for Black Swift Technologies to design, build, test, and deliver 16 fully integrated, air-deployable small unmanned aircraft systems (sUAS) equipped with meteorological/oceanographic (METOC) payloads for deployment from NOAA's WP-3D aircraft into tropical cyclones. The program builds on successful prior missions (Hurricanes Edouard 2014, Maria 2017, Michael 2018) and aims to advance sUAS duration, communication robustness, and data reliability to enable routine collection of critical boundary layer data in severe storm environments.

## Technical Approach

### Core Concept
- **Air-deployment method**: sUAS launched from NOAA WP-3D aircraft using pressurized launch tube and release mechanism
- **Launch envelope**: Minimum 5,000'-15,000' altitude; preferred 3,500'-16,000'; design for 250 KIAS aircraft speed, minimum demonstrated 210 KIAS
- **Command & Control (C2)**: Radio line-of-sight link with 150 nm range capability between WP-3D and sUAS
- **Expendable/unrecoverable**: Designed as expendable technology for use in severe turbulent tropical cyclone environments

### Key Performance Requirements
- **Flight duration**: Minimum 1.5 hours with payload installed
- **Operational environment**: Survive and maintain flight in hurricane conditions with one-minute averaged wind speeds exceeding 65 knots, heavy rain, and severe atmospheric turbulence
- **Data continuity**: Maximum C2 telemetry loss shall not exceed 1 minute
- **Autonomous flight**: Capable of executing at least 3 pre-programmed flight profiles without pilot input; user-selectable prior to launch
- **Flight control modes**: Heading and altitude override capability; emergency flight termination capability

## Products & Capabilities Described

### Black Swift Technologies S0 sUAS
**What it is**: A multi-hour duration, air-deployable small unmanned aircraft system designed for hurricane research operations.

**Specifications and capabilities**:
- 16 units total to be delivered across the contract period
- Minimum 1.5 hour endurance with integrated payload
- Autonomous flight execution with pre-programmed profiles
- Radio C2 link with 150 nm range
- Deployable from WP-3D aircraft via pressurized launch tube
- Capable of operating in 65+ knot winds with heavy rain and severe turbulence
- Short burst video capability (with payload data pause if necessary)
- Flight control station (FCS) installed on WP-3D in rack configuration
- Primary and satellite C2 link capability with aircraft antenna systems

### Integrated Payload Components

**METOC Payload** (per system requirement 4.1.1-4.1.2):
- **PTH sensors**: Pressure, temperature, humidity data collection from NCAR NRD41 dropwindsonde package
- **Wind measurement**: Horizontal and vertical wind components derived from PTH sensor and sUAS autopilot data
- **Infrared (IR) sensor**: Downward-looking sensor for sea surface temperature (SST) and cloud top data collection; Government-recommended Melexis IR Thermometer (PN: MLX90614)
- **Altimeter**: Viable laser or radar altimeter for accurate vertical platform position assessment above surface
- **Turbulence probe**: Three-dimensional wind component measurement (u, v, w) at 5 Hz or greater frequency
- **Multi-Hole Turbulence Probe (MHTP)**: Designed by Area-I's Altius 600 for integration; 10 units specified in deliverables (separate from S0 units)

**Data transmission and integration**:
- Payload data transmitted via C2 link to maximum bandwidth extent possible
- Real-time data ingest into NOAA AOC's P-3 onboard situational awareness visualization system (KARMA)
- WMO HDOBS data formatting compliance
- WMO/NHOP compliant Vortex Data Message (VDM) generation capability
- Data validation tolerances specified for wind, pressure, temperature, humidity, altitude, and positioning

## Use Cases & Applications

### Primary Mission
**Tropical cyclone boundary layer research**: Deployment into active hurricanes to collect critical meteorological and oceanographic data in the hurricane boundary layer environment—areas that manned aircraft cannot safely sample.

### Historical Context & Precedent
- **Hurricane Edouard (2014)**: First successful air-deployed sUAS from NOAA WP-3D inside Category 3 hurricane eye
- **Hurricane Maria (2017)**: Six (6) sUAS deployed
- **Hurricane Michael (2018)**: Single sUAS recorded 183 mph wind gust at 2,000 feet above ocean surface

### Specific Research Goals
- Improve understanding of surface air/sea interaction processes impacting hurricane intensity models
- Advance situational awareness regarding tropical cyclone (TC) intensity change prediction
- Enable routine collection of valuable meteorological and oceanographic data within TC boundary layer environment
- Transition capability from research prototype to operational readiness

## Test & Evaluation Approach

### Preliminary Design Review (PDR)
- Technical assessment to establish allocated baseline before detailed design work
- Scheduled on or before 31 Jan 2022 with close coordination with GPC, UPC, and NOAA Aircraft Operational Center staff

### Critical Design Review (CDR)
- Multi-disciplined technical review to ensure system can proceed to fabrication, demonstration, and test
- Meeting stated performance requirements within cost, schedule, and risk parameters
- Multiple CDRs may be held for key Configuration Items and subsystems
- Primary CDR scheduled on or before 31 Mar 2022; potential secondary CDR by 31 Mar 2023

### Separation/Dummy Missions (DM)
- Two (2) mass and shape equivalent sUAS units to evaluate clean separation from WP-3D and flight configuration transition
- Minimal critical equipment to assess separation phase viability
- May include deployable flight surfaces
- Video recording from external cameras or chase aircraft

### Calibration Missions (CM)
- Clear air, low-wind environment test flights evaluating all operational aspects anticipated in storm environment
- Confirmation of P-3 to sUAS range capability
- sUAS endurance verification
- Payload performance validation
- Array of safety-oriented tests ensuring NOAA compliance
- Scheduled testing windows: 17-31 May 2022 and 31 May 2023 (if needed)

### METOC Validation Tolerances
- **Geographic Position**: Aircraft within 3 nm; storm surface/flight level center within 6 nm
- **Wind Direction**: Surface within 10°; flight level (>20 kt) within 5°
- **Wind Speed**: Surface within 10 kt; flight level within 4 kt
- **Pressure Height**: Surface within 2 mb; flight level ≤500 mb within 10 m; >500 mb within 20 m
- **Temperature**: Sea surface and flight level within 1°C
- **Dew-Point Temperature**: 20°C to +40°C within 1°C; <20°C within 3°C
- **Absolute Altitude**: Within 10 m
- **Video**: Clear capture and transfer to P-3 demonstrated

## Project Deliverables Timeline (2021-2023)

### FY2022 Deliverables
- **31 Aug 2021**: Coordinate with BST on sUAS tasks
- **31 Jan 2022**: Conduct S0 PDR with GPC, UPC, NOAA AOC staff
- **28 Feb 2022**: Complete NRE tasks (payload integration, safety, automation, KARMA integration, WMO HDOBS requirements)
- **31 Mar 2022**: Conduct S0 CDR
- **30 April 2022**: Deliver 2 field-ready S0 sUAS with full payload (laser altimeter, MHTP)
- **17-31 May 2022**: Conduct S0 P-3/sUAS Calibration and Dummy Missions
- **31 July 2022**: Deliver 6 field-ready S0 sUAS with full payload
- **1 Aug - 30 Nov 2022**: Conduct hurricane field deployment (in-storm operations)

### FY2023 Deliverables
- **28 Feb 2023**: Complete NRE tasks from 2022 lessons learned; generate WMO/NHOP VDM for 2023 season
- **31 Mar 2023**: Complete Area-I Altius 600 MHTP design and build; conduct potential CDR#2
- **31 Mar 2023**: Deliver 2 MHTPs to Area-I for Altius 600 integration
- **30 April 2023**: Deliver 2 field-ready, MHTP-equipped S0s with video capability
- **31 May 2023**: Conduct potential second sUAS CM for operational readiness
- **31 May 2023**: Contribute to Area-I Altius 600 P-3/sUAS MHTP Calibration Mission
- **30 June 2023**: Deliver 8 MHTPs to Area-I for Altius 600 integration
- **31 July 2023**: Deliver 6 field-ready, MHTP-equipped S0s with video capability
- **1 Aug - 30 Nov 2023**: Conduct hurricane field deployment

## Key Results / Performance Data
No results documented; this is a proposal/SOW for future work rather than a completed project report.

## Cost Summary

### Hardware
- **16 Black Swift Technologies S0 sUAS platforms** with integrated payloads (PTH sensors, IR sensor, laser altimeter OR video camera): **$160K**
- **10 Multi-Hole Turbulence Probes (MHTP)** for Area-I Altius 600: **$80K**

### Non-Recurring Engineering (NRE) & Program Support
- **Engineering support**: S0 payload integration, flight performance enhancement, full automation, NOAA real-time data requirements (KARMA, WMO HDOBS, WMO/NHOP VDM), video camera integration, Area-I MHTP NRE: **$161K**
- **Project Documentation**: **$15K**

### Travel & In-Field Support
- **(2) Clear-air calibration S0 sUAS flights** (2022, 2023): **$20K**
- **(1) Clear-air calibration Area-I MHTP flight** (2022): **$10K**
- **(3) In-storm hurricane S0 deployments** (2x 2022, 1x 2023): **$30K**

**Total 2021-23 Project Cost: $476K**
- Year 1 (FY2021) available: $150K
- Year 2 (FY2022) available: $251K
- Year 3 (FY2023) available: $75K

## Notable Details

### Partnerships & Integration Points
- **NCAR NRD41 dropwindsonde package**: PTH sensor source; auxiliary data input for IR sensor telemetry
- **Area-I (Altius 600)**: Separate sUAS platform; BST contracted to design, build, and deliver 10 MHTPs for Area-I integration during 2022-2023
- **NOAA Aircraft Operational Center (AOC)**: Provides mechanical, electrical, power, and data integration requirements for FCS and antenna systems
- **University of Miami/CIMAS**: Technical oversight via Dr. Jun Zhang (UPC)