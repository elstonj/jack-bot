# Black Swift Technologies Statement of Work – NOAA Hurricane Research (SOW_BST_JULY2023)

## Document Metadata
- **Type:** Statement of Work (SOW)
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration) – Office of Atmospheric Research (OAR) and Office of Marine and Aviation Operations (OMAO); specifically Hurricane Research Division of Atlantic Oceanographic Meteorological Lab (AOML)
- **Program/Solicitation:** NOAA sUAS Hurricane Research Program; NOAA WP-3D air-deployed sUAS operations
- **Date:** July 1, 2023 – June 30, 2024 (with deliverables extending to April 2025)
- **BST Products/Systems Referenced:** 
  - S0 sUAS platform (primary platform for this contract)
  - Multi-Hole Turbulence Probe (MHTP) integration
- **Key Personnel:**
  - Dr. Joseph Cione (NOAA/AOML/HRD) – Government Point of Contact (GPC)
  - Dr. Jun Zhang (University of Miami/CIMAS) – University Point of Contact (UPC)
  - Black Swift Technologies (existing contractor for coordination and platform delivery)

## Executive Summary

This SOW establishes a contract between NOAA and Black Swift Technologies to design, build, test, and deploy fully-integrated meteorological/oceanographic (METOC) payload-equipped small unmanned aircraft systems (sUAS) for tropical cyclone research. Over 12-24 months, BST will deliver 20 air-deployable sUAS platforms capable of 1.25+ hour endurance, autonomous operation, 150 nm command and control range, and deployment from a NOAA WP-3D aircraft to sample critical hurricane boundary layer data that manned aircraft cannot safely access. The work builds on successful prior deployments into Hurricanes Edouard (2014), Maria (2017), Michael (2018), and Ian (2022).

## Technical Approach

### Air-Deployment Concept
- sUAS are launched from NOAA WP-3D aircraft via free-fall chute deployment
- Launch tube and release mechanism to be designed and integrated for cabin-mounted deployment
- Designed for launch at 250 KIAS (knots indicated airspeed); minimum reliable launch at 210 KIAS
- **Launch altitude envelope:** Minimum acceptable 5,000'–15,000'; preferred 3,500'–16,000'
- sUAS designated as unrecoverable/expendable technology for operations in severe storm environments

### Command & Control (C2) System
- **Range requirement:** 150 nautical miles (nm) between WP-3D and sUAS
- Radio line-of-sight C2 link with continuous command and control capability
- **Maximum telemetry loss tolerance:** No more than 1-minute duration
- Payload data transmitted to maximum bandwidth possible
- Flight Control Station (FCS) to be rack-mounted on WP-3D per NOAA Aircraft Operations Center (AOC) specifications
- Aircraft antenna provided by contractor; NOAA AOC provides integration requirements

### Flight Autonomy
- sUAS capable of autonomously executing pre-programmed flight profiles without pilot input
- Mission flight profiles user-selectable prior to launch (defined by GPC/UPC)
- Emergency flight termination capability required; independent flight termination system not required

### Endurance & Performance
- **Minimum demonstrated flight duration:** 1.25 hours with payload installed
- Data extrapolation permitted if actual flight demonstration is less than 1.25 hours
- Must operate reliably in severely turbulent tropical cyclone environments with extreme wind speeds (65+ knots), heavy rain, and severe atmospheric turbulence

### METOC Payload Integration
The sUAS carries an integrated meteorological/oceanographic sensor package:

**Pressure, Temperature, Humidity (PTH):**
- Integrates NCAR NRD41 dropwindsonde PTH sensor package
- Collects and transmits pressure, temperature, humidity data
- Autopilot data combined with PTH sensors to derive horizontal and vertical wind components

**Infrared (IR) Sensor:**
- Downward-looking IR sensor for Sea Surface Temperature (SST) and cloud-top data collection
- IR telemetry ingested and transmitted via research dropsonde NRD41 using existing auxiliary data input
- Government recommendation: Melexis InfraRed Thermometer (MLX90614); alternatives considered
- NCAR has analyzed and integrated this sensor on dropwindsondes

**Altitude Measurement:**
- Viable laser or radar altimeter to be integrated for accurate vertical platform positioning above surface

**Multi-Hole Turbulence Probe (MHTP):**
- Contractor to design, test, and fully integrate probe to measure three-dimensional wind components (u, v, w)
- **Minimum measurement frequency:** 5 Hz or greater
- Two (2) MHTP units to be built for integration on Area-I's Altius 600 sUAS

**Optional Video/Imaging:**
- Explore incorporation of short burst video capability and/or still image capture
- Loss of other METOC payload data acceptable during video/image capture if necessary

### Data Integration & Formatting
- Real-time data delivery to NOAA's operational centers (NHC, EMC)
- Integration with AOC's P-3 onboard situational awareness visualization system (KARMA)
- Conversion of sUAS data output to World Meteorological Organization (WMO) HDOBS data formatting protocols
- Generation of WMO/NHOP-compliant Vortex Data Message (VDM) where applicable
- All necessary engineering for real-time data delivery and operational integration

### Testing & Validation Framework

**Preliminary Design Review (PDR):**
- Technical assessment establishing allocated baseline before detailed design work begins
- First government opportunity to closely observe contractor's hardware and software design

**Critical Design Review (CDR):**
- Multi-disciplined technical review to confirm system can proceed to fabrication, demonstration, and test
- Confirms ability to meet stated performance requirements within cost, schedule, and risk
- Multiple CDRs may be held for key configuration items and subsystems, culminating in system-level CDR

**Calibration Missions (CM):**
- Clear air, low-wind environment test flights evaluating all aspects of sUAS operation
- Must be completed before any sUAS proceeds to tropical cyclone environment deployment
- Include confirmation of P-3 to sUAS range, sUAS endurance, payload performance, and safety compliance with NOAA requirements
- Up to two (2) successful CMs required as contracted deliverables

## Products & Capabilities Described

### Black Swift Technologies S0 sUAS Platform
**What it is:**
- Small unmanned aircraft system designed for air deployment from manned aircraft (NOAA WP-3D)
- Expendable platform for operation in extreme weather environments
- Fully autonomous capable with integrated multi-sensor METOC payload

**Proposed use in this context:**
- Primary platform for NOAA's tropical cyclone boundary layer research
- Air-launched into hurricane environments to collect real-time meteorological and oceanographic data
- Targeted, expendable resource to sample areas manned aircraft cannot safely access

**Key specifications:**
- **Endurance:** Minimum 1.25 hours with payload
- **Command & Control Range:** 150 nm from deployment aircraft
- **Launch capability:** 5,000'–15,000' at 250 KIAS (210 KIAS minimum reliable)
- **Environmental survivability:** Designed for winds >65 knots, heavy rain, severe atmospheric turbulence
- **Autonomy:** Pre-programmed autonomous flight profiles without pilot input
- **Payload capacity:** Fully integrated METOC sensor suite (PTH, IR, altimeter, MHTP, video/imaging)
- **Data transmission:** Continuous C2 and payload telemetry with <1-minute loss tolerance
- **Deployment:** Free-fall chute launch with launch tube and release mechanism from WP-3D cabin

**Delivery schedule:**
- Four (4) platforms by February 21, 2024
- Twelve (12) platforms by July 31, 2024
- **Total contract:** 20 fully-integrated, flight-ready S0 sUAS platforms with payloads

### Multi-Hole Turbulence Probe (MHTP)
**What it is:**
- Integrated sensor package for measuring three-dimensional wind components (u, v, w)
- High-frequency measurement capability (5 Hz minimum)

**Proposed use:**
- Integration on Area-I's Altius 600 sUAS platform
- Provides enhanced wind measurement resolution for turbulence characterization in hurricane environment

**Specifications:**
- **Minimum measurement frequency:** 5 Hz
- **Data resolution:** 5 Hz minimum
- **Delivery:** Two (2) MHTP units by April 31, 2024

### Flight Control Station (FCS)
**What it is:**
- Ground-based command and control and telemetry reception system
- Rack-mounted configuration for WP-3D aircraft installation

**Components:**
- Rack-installed radio and computer equipment
- Radio antennas
- Power and data cables
- Contractor-proposed antenna solution for primary link

**Integration requirements:**
- Mechanical, electrical power, and data integration per NOAA AOC specifications
- Solution reviewed and approved at PDR

## Use Cases & Applications

### Primary Mission: Tropical Cyclone (Hurricane) Research
- **Boundary layer characterization:** Collection of critical meteorological data from hurricane boundary layer where manned aircraft cannot safely operate
- **Surface air/sea interaction processes:** Measurement of conditions impacting hurricane intensity models
- **Situational awareness:** Enhanced observation of under-sampled critical storm regions
- **Operational model improvement:** Data to advance NOAA's tropical cyclone intensity change prediction models

### Demonstrated Historical Missions
- **Hurricane Edouard (2014):** First successful sUAS deployment into Category 3 hurricane from NOAA WP-3D
- **Hurricane Maria (2017):** Six (6) sUAS deployed
- **Hurricane Michael (2018):** sUAS recorded record-setting 183 mph wind gust at 2,000 feet above ocean surface
- **Hurricane Ian (September 28, 2022):** Area-I ALTIUS 600 deployment set records:
  - sUAS endurance: 102 minutes in tropical cyclone environment
  - Communication distance: 135 nm to deployment P-3
  - Recorded wind speed: 215 mph

### Proposed 2023-2024 Deployment Schedule
- **Up to two (2) three-day clear air deployments** (calibration missions) per season
- **Up to two (2) five-day in-storm hurricane deployments** per season
- Timing: September 1 – November 30, 2023 and August 1 – November 30, 2024
- Real-time HDOBS data transmission to National Hurricane Center (NHC) and Environmental Modeling Center (EMC)

## Performance Requirements & Validation

### METOC Sensor Package Validation Tolerances
These serve as guidance for post-flight test analysis:

| Parameter | Accuracy Requirement |
|-----------|----------------------|
| **Geographic Position** | |
| Aircraft position | Within 3 nm |
| Storm surface center (wind/pressure) | Within 6 nm |
| Flight-level storm center (wind/pressure) | Within 6 nm |
| **Wind Direction** | |
| Surface | Within 10° |
| Flight level (winds >20 kt) | Within 5° |
| **Wind Speed** | |
| Surface | Within 10 kt |
| Flight level | Within 4 kt |
| **Pressure Height** | |
| Surface | Within 2 mb |
| Flight level ≤500 mb | Within 10 m |
| Flight level >500 mb | Within 20 m |
| **Temperature** | |
| Sea surface | Within 1°C |
| Flight level | Within 1°C |
| **Dew-Point Temperature** | |
| 20°C to +40°C | Within 1°C |
| <20°C | Within 3°C |
| **Absolute Altitude** | Within 10 m |
| **Video/Image Capture** | Clear video/image with minimum duration TBD |
| **3D Wind Data (MHTP)** | 5 Hz minimum resolution |

### Hurricane Environment Survivability Requirement
- Demonstrated capability to survive and maintain flight in hurricane environment where:
  - One-minute averaged wind speeds exceed 65 knots
  - Heavy rain present
  - Severe atmospheric turbul