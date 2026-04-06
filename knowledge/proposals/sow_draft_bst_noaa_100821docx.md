# NOAA/Black Swift Technologies Statement of Work (SOW) FY21-24

## Document Metadata
- Type: Statement of Work (SOW) / Draft Contract
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration) - Office of Atmospheric Research (OAR), Hurricane Research Division, Atlantic Oceanographic Meteorological Lab (AOML)
- Program/Solicitation: Tropical Cyclone Research / Hurricane Boundary Layer Research; NOAA WP-3D Air-Deployed sUAS Program
- Date: 8 October 2021 (Draft)
- BST Products/Systems Referenced: S0 (small Unmanned Aircraft System)
- Key Personnel: Dr. Joseph Cione (NOAA/AOML/HRD - Government Point of Contact); Dr. Jun Zhang (University of Miami/CIMAS - University Point of Contact); Jack Elston (BST - last editor)

## Executive Summary
This SOW outlines a multi-year agreement (FY21-24) between NOAA and Black Swift Technologies to design, build, test, and deliver air-deployed small unmanned aircraft systems (sUAS) equipped with meteorological and oceanographic (METOC) payloads for tropical cyclone research. The project aims to advance hurricane boundary layer understanding by deploying 16 fully-integrated S0 sUAS platforms from NOAA WP-3D aircraft, with focus on multi-hour endurance, 150 nm command and control range, and reliable data collection in severe storm environments.

## Technical Approach

**Core Concept of Operations (CONOP):**
- Air-launch of small UAS from NOAA WP-3D aircraft in-flight using pneumatic free-fall chute deployment
- Target areas of hurricanes inaccessible to manned aircraft
- Collect boundary layer meteorological and oceanographic data during TC operations
- Expendable/unrecoverable platform designed for severe turbulent environments

**System Architecture:**
- **Launch System:** Pressurized launch tube and release mechanism for WP-3D cabin deployment
- **Command & Control:** Radio line-of-sight C2 link between sUAS and WP-3D with 150 nm range capability
- **Flight Control Station (FCS):** Rack-mounted equipment (radio, computer, antennas, power/data cables) installed on WP-3D
- **Data Management:** Real-time telemetry transmission with maximum 1-minute C2 loss tolerance
- **Autopilot:** Autonomous pre-programmed flight profile execution with pilot override capability for heading/altitude and emergency termination

**Payload Integration:**
- Vaisala NRD41 dropwindsonde PTH sensor package (pressure, temperature, humidity)
- Downward-looking infrared (IR) sensor (recommended: Melexis MLX90614) for sea surface temperature (SST) and cloud top measurement
- Laser or radar altimeter for accurate vertical position assessment above surface
- Multi-hole turbulence probe (MHTP) for three-dimensional wind measurement (u, v, w components) at ≥5Hz frequency
- Data transmission via C2 link with conversion to WMO HDOBS formatting for NOAA situational awareness visualization (KARMA)

**Flight Performance Requirements:**
- **Launch envelope:** Preferred 3,500-16,000 ft altitude; minimum acceptable 5,000-15,000 ft
- **Launch speed:** Designed for 250 KIAS; reliable at 210 KIAS
- **Flight duration:** Minimum 1.5 hours with full payload installed
- **Storm environment survivability:** Capable of surviving and maintaining flight in hurricanes with sustained wind speeds >65 knots, heavy rain, and severe atmospheric turbulence

## Products & Capabilities Described

**Black Swift Technologies S0 sUAS:**
- **Definition:** Small unmanned aircraft system designed for air-deployment from manned aircraft
- **Proposed Use:** Tropical cyclone boundary layer research platform; expendable remote sampler for hurricane intensity and surface interaction studies
- **Specifications:**
  - Deployable from NOAA WP-3D via pneumatic launch
  - Multi-hour endurance (≥1.5 hours with payload)
  - 150 nm command and control range
  - Autonomous flight with 3+ pre-programmed profiles
  - Real-time C2 and payload data transmission
  - Survives extreme wind (>65 kt), heavy precipitation, severe turbulence
  - Carries integrated METOC payload (PTH sensors, IR sensor, altimeter, turbulence probe)
- **Delivery Commitment:** 16 fully-integrated, field-ready platforms over FY21-24
- **Cost:** $160K for 16 platforms with integrated payload

**Multi-Hole Turbulence Probe (MHTP):**
- **Definition:** Specialized measurement probe for high-frequency 3D wind component characterization
- **Proposed Use:** Integration on both BST S0 platforms and Area-I's Altius 600 sUAS
- **Specifications:**
  - Measures u, v, w wind components
  - Sampling frequency: ≥5Hz
  - Full engineering design, testing, and build required
- **Delivery Commitment:** 10 MHTPs total (2 for initial S0 integration, 8 additional for Altius 600)
- **Cost:** $80K for 10 units

**Flight Control Station (FCS):**
- Custom WP-3D rack-mounted ground station
- Radio, computer, antenna systems for C2 link management
- Integration with NOAA AOC mechanical/electrical specifications
- Designed to support real-time data receipt and situational awareness

## Use Cases & Applications

**Primary Mission:** Tropical Cyclone (Hurricane) Boundary Layer Research
- **Specific Applications:**
  - Air-deployed reconnaissance into hurricane eye and boundary layer regions
  - Surface air/sea interaction process measurement
  - Hurricane intensity model improvement
  - Wind speed and direction profiling at storm center
  - Sea surface temperature mapping in storm environment
  - Pressure and humidity sampling in TC boundary layer

**Historical Context (Successfully Demonstrated):**
- Hurricane Edouard (2014): First successful deployment from WP-3D in Category 3 hurricane eye
- Hurricane Maria (2017): 6 sUAS deployed
- Hurricane Michael (2018): Recorded 183 mph wind gust at 2,000 ft altitude

**Target Storm Environments:**
- Major hurricanes (Category 3+ equivalent)
- Severe atmospheric turbulence conditions
- Heavy precipitation environments
- Wind speeds exceeding 65 knots sustained

## Key Results (from Background)

**Historical Performance Data:**
- **Hurricane Michael (October 2018):** Record-setting wind measurement of 183 mph gust at 2,000 ft above ocean surface
- **Operational Viability:** Successfully demonstrated that air-deployed sUAS concept is viable for TC research
- **Data Value:** Collected data shown to be critical for improving surface air/sea interaction process understanding and tropical cyclone intensity prediction models

**Proven Capability Gaps Addressed:**
- Prior systems had limited duration, communication robustness, and payload reliability
- Current effort focuses on measurable increases in endurance, communication range (150 nm), and data reliability

## Testing & Validation Requirements

**Pre-Deployment Testing Pipeline:**

1. **Preliminary Design Review (PDR)** (by 31 Jan 2022)
   - Contractor design assessment with GPC, UPC, and NOAA AOC
   - Validates technical approach and allocated baseline

2. **Separation/Launch Testing**
   - Two (2) mass and shape-equivalent dummy sUAS for launch viability assessment
   - NOAA AOC conducts free-fall deployment tests with video documentation
   - Validates clean separation and flight configuration transition

3. **Calibration Missions (CM)** (2 per year - May 2022, May 2023 windows)
   - Clear air, low-wind environment test flights
   - Validation of: P-3 to sUAS range, sUAS endurance, payload performance, safety compliance
   - Uses government dropwindsondes for METOC data cross-validation
   - **Mandatory prerequisite** before any operational TC deployment

4. **Critical Design Review (CDR)** (by 31 Mar 2022, possible CDR#2 by 31 Mar 2023)
   - Multi-disciplinary technical review
   - Confirms readiness for fabrication, demonstration, and testing
   - Validates ability to meet performance requirements within cost/schedule/risk

**METOC Sensor Performance Tolerances (Post-Flight Guidance):**
- Geographic Position: Aircraft ±3 nm; Storm center ±6 nm
- Wind Direction: Surface ±10°; Flight level (>20 kt) ±5°
- Wind Speed: Surface ±10 kt; Flight level ±4 kt
- Pressure Height: Surface ±2 mb; Flight level (≤500 mb) ±10 m; (>500 mb) ±20 m
- Temperature: Sea surface ±1°C; Flight level ±1°C
- Dew-Point: 20-40°C ±1°C; <20°C ±3°C
- Absolute Altitude: ±10 m

## Notable Details

**Partnership Structure:**
- **BST Role:** Hardware development, payload integration, flight testing, field deployment support, NOAA data requirement compliance (KARMA, WMO HDOBS)
- **Area-I Role:** Multi-hole turbulence probe design/build for Altius 600 platform; coordinate with BST on dual-platform deployment
- **NOAA Roles:** AOC provides aircraft, test facility (Avon Park FL), pilot operations; AOML/HRD provides scientific guidance (Dr. Cione)
- **University of Miami:** CIMAS provides co-technical point (Dr. Zhang)

**Program Schedule (2021-2024 Phased Approach):**
- **Phase 1 (Jan-Apr 2022):** PDR completion; 2 field-ready S0 delivery; launch/separation testing
- **Phase 2 (May 2022):** Calibration missions (clear air); dummy launch tests
- **Phase 3 (Aug-Nov 2022):** First hurricane season field deployment; 8 total S0s delivered by July
- **Phase 4 (2023):** Lessons-learned improvements; possible CDR#2; second season deployment; 8 additional S0s delivered

**Operational Support Requirements:**
- **Travel & Field Support Commitment:** Four 3-5 day deployments (2 clear-air, 2 in-storm) across 2022-2023 seasons
- **Budget:** $484K total for 2021-23 period
  - Hardware (16 S0 + 10 MHTP): $240K
  - NRE/Program Support: $130K
  - Field Travel/In-Storm Support: $114K

**Data Integration Requirements:**
- Real-time telemetry to NOAA P-3 KARMA visualization system
- WMO HDOBS data formatting compliance
- Post-flight mission performance reporting

**Safety & Regulatory Considerations:**
- Expendable/unrecoverable platform designation (no recovery requirement)
- Emergency flight termination capability required
- AOC safety compliance for WP-3D integration
- Severe storm environment certification (>65 kt sustained winds)

**Competitive Advantages Highlighted:**
- Only proven air-deployable sUAS platform with demonstrated hurricane deployment history (3 major hurricane missions, 2014-2018)
- Proven 150+ nm range capability (inferred from operational requirement)
- Integration with government standardized METOC sensors (NCAR NRD41)
- Real-time command and control in extreme environments

This SOW represents a significant expansion of NOAA's TC research capability, moving from proof-of-concept (3 prior missions) to routine operational sUAS-based hurricane boundary layer sampling.