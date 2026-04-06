# BST Statement of Work for UMiami (NOAA Hurricane Research)

## Document Metadata
- **Type:** Statement of Work (SOW)
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration) / University of Miami (CIMAS)
- **Program/Solicitation:** NOAA Office of Atmospheric Research (OAR) / Hurricane Research Division (HRD) at Atlantic Oceanographic and Meteorological Lab (AOML)
- **Date:** July 12, 2023 – June 30, 2024 (contract period); Document dated July 13, 2023
- **BST Products/Systems Referenced:** S0 sUAS platform (primary), S3 mentioned in context
- **Key Personnel:** 
  - Dr. Joseph Cione (Government Point of Contact/GPC) – NOAA/AOML/HRD
  - Dr. Jun Zhang (University Point of Contact/UPC) – University of Miami/CIMAS
  - Black Swift Technologies as primary contractor

## Executive Summary
This SOW establishes a contract for Black Swift Technologies to design, build, test, and deliver fully-integrated meteorological/oceanographic (METOC) payload-equipped small unmanned aircraft systems (sUAS) for NOAA's tropical cyclone research. Over the contract period, BST will deliver 20 S0 sUAS platforms capable of being air-deployed from NOAA's WP-3D aircraft into hurricanes, equipped with advanced sensors for measuring wind, pressure, temperature, humidity, sea surface temperature, and turbulence data, with a minimum 1.25-hour flight duration and 150 nautical mile command-and-control range.

## Technical Approach

**System Architecture:**
- Development and integration of BST's S0 sUAS platform (small unmanned aircraft system)
- Air-deployable from NOAA WP-3D aircraft via free-fall chute with custom launch tube and release mechanism
- Autonomous flight execution of pre-programmed mission profiles
- Radio line-of-sight command-and-control (C2) link with 150 NM range capability
- Maximum C2 telemetry loss tolerance: 1 minute duration
- Platform classified as unrecoverable/expendable technology

**Launch Parameters:**
- Minimum acceptable launch altitude: 5,000–15,000 feet
- Preferred launch altitude: 3,500–16,000 feet
- Designed for launch at 250 KIAS aircraft speed; demonstrated reliable launch at 210 KIAS
- Aircraft speed during deployment: 210–250 knots

**Flight Performance:**
- Minimum 1.25-hour flight duration with payload installed
- Capability to survive and maintain flight in hurricane conditions with one-minute averaged wind speeds exceeding 65 knots, heavy rain, and severe atmospheric turbulence
- Autonomous flight without pilot input during mission execution
- Emergency flight termination capability

**Communication & Data Management:**
- Radio line-of-sight C2 link to WP-3D
- Maximum payload data transmission to bandwidth limits
- Real-time data delivery to NOAA's situational awareness visualization system (KARMA)
- WMO HDOBS data format conversion for operational centers
- Potential WMO/NHOP-compliant Vortex Data Message (VDM) generation

## Products & Capabilities Described

### BST S0 sUAS Platform
- **What it is:** A small unmanned aircraft system designed for air deployment from manned aircraft into severe weather environments
- **Configuration:** 16 platforms delivered under this contract (with plan for 20 total), fully integrated with METOC payload
- **Performance Specs:**
  - Flight duration: Minimum 1.25 hours with payload
  - C2 range: 150 NM
  - Launch altitude envelope: 5,000–15,000 feet (minimum acceptable); 3,500–16,000 feet (preferred)
  - Designed for deployment speeds: 250 KIAS (design point); 210 KIAS (demonstrated)
  - Payload capacity: Supports integrated METOC package
  - Autonomous execution of pre-programmed flight profiles
  - Capable of operating in hurricane-force conditions (65+ knots sustained winds)

### Integrated METOC Payload
- **Pressure-Temperature-Humidity (PTH) Sensors:**
  - Source: NCAR NRD41 dropsonde package
  - Data collected: Pressure, temperature, humidity
  - Wind calculation: PTH sensor combined with sUAS autopilot data provides horizontal and vertical wind components

- **Infrared (IR) Sensor:**
  - Downward-looking orientation
  - Application: Sea surface temperature (SST) and cloud top data collection
  - Recommended sensor: Melexis Infrared Thermometer (MLX90614); alternatives considered
  - Data transmission: Via NRD41 research dropsonde utilizing auxiliary data input
  - Integration: NCAR has analyzed and integrated on dropsonde

- **Altimetry:**
  - Laser or radar altimeter (viable option to be integrated)
  - Purpose: More accurate assessment of vertical platform position above surface
  - Accuracy requirement: Within 10 meters absolute altitude

- **Multi-Hole Turbulence Probe (MHTP):**
  - Measures three-dimensional wind components (u, v, w)
  - Frequency: 5 Hz minimum
  - Two (2) MHTP units to be built and integrated for use on Area-I's Altius 600 sUAS
  - Data format: High-resolution three-dimensional wind data

- **Video/Image Capture (Exploratory):**
  - Short burst video capability and/or still image capture
  - Integration: During capture periods, loss of other METOC payload data is acceptable if necessary
  - Requirement: Clear video/image capture and transfer to P-3 demonstrated

### Flight Control Station (FCS)
- **Components:**
  - Rack-installed radio and computer equipment
  - Radio antennas
  - Power and data cables
- **Configuration:** Ground-station system for sUAS command, control, and telemetry reception
- **Installation:** To be installed on NOAA WP-3D aircraft in acceptable rack configuration per NOAA AOC specifications
- **Integration Requirements:** Contractor to propose mechanical, electrical, power, and data integration solutions for PDR review
- **Antenna Requirements:** Contractor to provide primary link aircraft antenna per NOAA AOC specifications

## Use Cases & Applications

### Primary Mission: Tropical Cyclone (Hurricane) Research
- **Scientific Objective:** Advance understanding of hurricane boundary layer processes and air/sea interactions affecting hurricane intensity
- **Operational Application:** Safely collect meteorological and oceanographic data from critical storm areas not safely accessible to manned aircraft
- **Data Use:** 
  - Improve NOAA's operational models for tropical cyclone intensity change prediction
  - Better situational awareness of storm structure and intensity
  - Real-time data delivery to National Hurricane Center (NHC) and Environmental Modeling Center (EMC) operational centers

### Deployment Scenarios
- Air-deployment from NOAA WP-3D aircraft into active hurricanes
- Expendable platform design allows safe deployment into extreme conditions
- Target areas of storm currently under-sampled by traditional methods
- Autonomous missions for targeted, danger-prone storm regions

### Historical Context (Background)
- 2014: First successful launch of air-deployed sUAS inside Category 3 hurricane eye
- 2017: Six sUAS deployed into Major Hurricane Maria
- October 2018: sUAS deployed into Hurricane Michael; recorded 183 mph wind gust at ~2,000 feet above ocean
- September 28, 2022: Area-I ALTIUS 600 deployed into Category 5 Hurricane Ian; set records for:
  - Endurance in TC environment: 102 minutes
  - Communication distance to P-3: 135 NM
  - Wind speed recording: 215 mph

## Key Requirements & Performance Standards

### METOC Validation Tolerances (Post-Flight Analysis Guidance)

| Parameter | Condition | Tolerance |
|-----------|-----------|-----------|
| **Geographic Position** | Aircraft position | Within 3 NM |
| | Storm surface center | Within 6 NM |
| | Flight level storm center | Within 6 NM |
| **Wind Direction** | Surface | Within 10° |
| | Flight level (winds > 20 knots) | Within 5° |
| **Wind Speed** | Surface | Within 10 knots |
| | Flight level | Within 4 knots |
| **Pressure Height** | Surface | Within 2 mb |
| | Flight level ≤ 500 mb | Within 10 m |
| | Flight level > 500 mb | Within 20 m |
| **Temperature** | Sea surface | Within 1°C |
| | Flight level | Within 1°C |
| **Dew-Point Temperature** | -20°C to +40°C | Within 1°C |
| | < -20°C | Within 3°C |
| **Absolute Altitude** | — | Within 10 m |

### Testing & Validation

**Calibration Missions (CM):**
- Up to two (2) successful test flights to be conducted
- Launch from NOAA WP-3D at Avon Park, FL, or government-selected sites over water
- Validation against government-launched dropwindsondes and other remote systems
- Test coverage: P-3 to sUAS range confirmation, sUAS endurance, payload performance, safety compliance
- Validation of wind speed, wind direction, temperature, humidity, pressure performance
- Requirement: Satisfactory CM must be completed before storm deployment

**Preliminary Design Review (PDR):**
- Technical assessment to establish allocated baseline
- Conducted before detailed design work
- First opportunity for government to observe contractor's hardware and software design

**Critical Design Review (CDR):**
- Multi-disciplined technical review for fabrication, demonstration, and test readiness
- Verification of performance requirements within cost, schedule, and risk
- Multiple CDRs may be held for key configuration items and subsystems
- System-level CDR culminates process

## Project Deliverables & Timeline

### FY2023 Deliverables (July 1, 2023 – June 30, 2024)

| Milestone | Target Date |
|-----------|-------------|
| Coordinate with BST on sUAS tasks | July 31, 2023 |
| BST complete sensor calibration analysis from March 2023 Florida missions | July 31, 2023 |
| Up to two (2) 5-day hurricane field deployments using S0 platform | Sept 1 – Nov 30, 2023 |
| Deliver real-time HDOBS sUAS TC data to NHC and EMC | Sept 1 – Nov 30, 2023 |
| Delivery of four (4) BST S0 platforms | Feb 21, 2024 |
| Conduct payload calibration/TC lessons-learned missions | March 1–21, 2024 |
| Establish 2024 Hurricane Field Plan layouts with GPC and UPC | Feb 1 – April 30, 2024 |
| Delivery of two (2) MHTP units for Altius 600 | March 31, 2024 |

### FY2024 Deliverables (July 1, 2024 – June 30, 2025)

| Milestone | Target Date |
|-----------|-------------|
| Delivery of twelve (12) BST S0 platforms | July 31, 2024 |
| Up to two (2) 5-day hurricane field deployments using S0 platform | Aug 1 – Nov 30, 2024 |
| End-of-project technical report and operational transition assessment | April 31, 2025 |

## Budget & Cost Breakdown

**Total Contract Value (2023–2025): $390,000**

### FY2023 (July 1, 2023 – June 30, 2024): $260,000
- Non-Recurring Engineering (NRE): $110,000
  - S0 payload integration
  - Flight performance enhancement
  - Full automation
  - NOAA real-time data requirements (AirOPS, WMO HDOBS formatting, WMO/NHOP VDM)
  - Video/image camera integration
  - Area-I Altius 600 MHTP residual NRE
- Project Documentation: $6,000
- sUAS Hardware: $112,000
  - 16 BST S0 platforms with