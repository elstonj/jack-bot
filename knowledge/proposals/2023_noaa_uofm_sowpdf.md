# 2023 NOAA UofM SOW

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: NOAA Office of Atmospheric Research (OAR), NOAA Office of Marine and Aviation Operations (OMAO), Hurricane Research Division of Atlantic Oceanographic Meteorological Lab (AOML)
- Program/Solicitation: Tropical cyclone research advancement support; University of Miami/CIMAS collaboration
- Date: July 1, 2023 – June 30, 2024 (with extensions through 2025)
- BST Products/Systems Referenced: S0 sUAS platform (primary), S2 and S3 referenced in historical context
- Key Personnel: Dr. Joseph Cione (NOAA/AOML, Government Point of Contact); Dr. Jun Zhang (University of Miami/CIMAS, University Point of Contact)

## Executive Summary

NOAA contracted Black Swift Technologies to design, build, test, and deliver fully-integrated METOC (meteorological/oceanographic) payload-equipped small Unmanned Aircraft Systems (sUAS) capable of being air-deployed from NOAA WP-3D hurricane research aircraft to collect critical data from the hurricane boundary layer in severe storm environments. The program spans 2023–2025 and builds on successful historical deployments (Hurricanes Edouard 2014, Maria 2017, Michael 2018, Ian 2022) to advance sUAS operational capability and data reliability.

## Technical Approach

**Core Concept:** Air-deployable, expendable sUAS launched from WP-3D via freefall chute at flight altitudes of 5,000–15,000 feet (preferred 3,500–16,000 feet). Aircraft speed: designed for 250 KIAS, demonstrating reliable launch at 210 KIAS.

**Flight Duration & Range:**
- Minimum 1.25-hour flight duration with integrated payload
- Command & Control (C2) line-of-sight link with 150 NM range capability
- Maximum C2 telemetry loss tolerance: 1 minute
- Autonomous pre-programmed flight profiles (user-selectable prior to launch)
- Emergency flight termination capability

**Key Technical Requirements:**
- Autonomous flight execution without pilot input during mission
- Survival in hurricane environment (winds >65 knots, heavy rain, severe atmospheric turbulence)
- Continuous METOC data collection and transmission simultaneously with C2 maintenance
- Integration into NOAA P-3 Flight Control Station (FCS)—rack-mounted on aircraft
- Platform designated unrecoverable/expendable

## Products & Capabilities Described

### S0 sUAS Platform
- **What it is:** Black Swift Technologies small unmanned aircraft system designed for hurricane research
- **Specifications:** 
  - Launch envelope: 5,000–15,000 feet (minimum acceptable); 3,500–16,000 feet (preferred)
  - Flight duration: ≥1.25 hours with payload
  - C2 range: 150 NM line-of-sight
  - Deployable from WP-3D via freefall chute and launch tube/release mechanism
  - Designed for autonomous operation; capable of emergency termination
- **Payload Integration:** Full METOC package with PTH sensors, IR sensor, laser/radar altimeter, turbulence probe, video/image capture
- **Historical context:** S2 and S3 platforms used in earlier deployments (Hurricanes Edouard, Maria, Michael); S0 is current operational version

### Multi-Hole Turbulence Probe (MHTP)
- **What it is:** Integrated sensor package for three-dimensional wind measurement
- **Specifications:** Measures u, v, w wind components at ≥5 Hz frequency
- **Integration:** Two units to be built for Area-I's Altius 600 sUAS platform; capability development under this SOW
- **Cost:** $20K for design, build, and integration support

### Integrated METOC Payload
Components:
1. **PTH Sensor Array:** NCAR NRD41 dropsonde package measuring pressure, temperature, humidity; provides horizontal and vertical wind components via autopilot data fusion
2. **Downward-Looking IR Sensor:** Collects sea surface temperature (SST) and cloud top data; Government recommendation is Melexis InfraRed Thermometer (MLX90614); IR telemetry transmitted via NRD41 auxiliary input
3. **Laser/Radar Altimeter:** Enhanced vertical platform positioning above surface (accuracy requirement: ±10m)
4. **Video/Image Capture:** Short-burst video and still image capability (optional; payload data loss acceptable during capture periods)
5. **Data Format Conversion:** All data converted to WMO HDOBS protocol and WMO/NHOP-compliant Vortex Data Message (VDM) format for operational centers (NHC, EMC)

### Flight Control Station (FCS)
- Rack-mounted ground station for P-3 aircraft
- Rack-installed radio and computer equipment
- Radio antennas
- Power and data cables
- Antenna for primary C2 link (NOAA AOC to provide integration specifications)
- Real-time data visualization integration with NOAA AOC's KARMA (Situational Awareness) system

## Use Cases & Applications

**Primary Mission:** Hurricane boundary layer research and operational intensity forecasting support

**Specific Applications:**
1. **Tropical Cyclone Intensity Research:** Measure surface air/sea interaction processes critical to hurricane intensity prediction models
2. **High-Risk Sampling:** Deploy into areas of severe storm (record wind speeds >100 knots) that manned aircraft cannot safely sample
3. **Boundary Layer Characterization:** Collect 3D wind, temperature, humidity, pressure, and SST data in the hurricane eye and eyewall
4. **Operational Support:** Provide real-time METOC data to NOAA National Hurricane Center (NHC) and Environmental Modeling Center (EMC) during hurricane season (September–November)
5. **Severe Storm Environments:** Designed for operation in winds >65 knots with heavy rain and severe atmospheric turbulence

**Deployment Schedule (2023–2025):**
- Up to 2 three-day clear-air calibration missions (low wind, clear conditions)
- Up to 4 five-day in-storm hurricane deployments (2023 and 2024 seasons)

## Key Results & Deliverables

### Historical Performance (Prior to this SOW)
- **Hurricane Edouard (2014):** First successful air-deployed sUAS launch from WP-3D
- **Hurricane Maria (2017):** 6 additional sUAS deployed
- **Hurricane Michael (2018):** Recorded 183 mph wind gust at ~2,000 feet above ocean surface
- **Hurricane Ian (September 28, 2022):** ALTIUS 600 platform (via Area-I, not BST) set three records:
  - sUAS endurance in TC: 102 minutes
  - C2 communication distance to P-3: 135 NMI
  - Wind speed recorded: 215 mph

### Contractual Deliverables (2023–2025)

**July–December 2023:**
- Coordination with existing NOAA contractor BST on sUAS tasks (by July 31, 2023)
- BST completion of sensor calibration/integration mission analysis from Florida March 2023 flights (by July 31, 2023)
- Up to 2 five-day hurricane field deployments using BST S0 platform (Sep 1–Nov 30, 2023)
- Real-time HDOBS sUAS TC data provision to NHC and EMC (Sep 1–Nov 30, 2023)
- Delivery of 4 BST S0 platforms with integrated payloads (by Feb 21, 2024)

**January–June 2024:**
- Payload calibration and TC lessons-learned missions using BST S0 platform (Mar 1–21, 2024)
- Establishment of 2024 hurricane field plan layouts for sUAS platforms with GPC/UPC (Feb 1–Apr 30, 2024)
- Delivery of 2 Multi-Hole Turbulence Probes for Altius 600 (by Mar 31, 2024)
- Delivery of 12 additional BST S0 platforms (by Jul 31, 2024)

**July 2024–April 2025:**
- Up to 2 five-day hurricane field deployments using BST S0 platform (Aug 1–Nov 30, 2024)
- End-of-project technical report and operational transition assessment review (by Apr 31, 2025)

### Total Deliverables
- **20 sUAS platforms:** 16 S0 platforms fully integrated with METOC payload + participation in 4 additional deployments
- **2 Multi-Hole Turbulence Probes:** For Altius 600 integration
- **Flight Control Station:** Integrated onto WP-3D
- **All payload data:** WMO HDOBS and VDM format conversion

## METOC Validation Tolerances

Performance guidance for post-flight test analysis:

| Parameter | Requirement |
|-----------|-------------|
| **Geographic Position** | Aircraft: ±3 NM; Storm center (surface/flight level): ±6 NM |
| **Wind Direction** | Surface: ±10°; Flight level (>20 kt): ±5° |
| **Wind Speed** | Surface: ±10 kt; Flight level: ±4 kt |
| **Pressure Height** | Surface: ±2 mb; ≤500 mb: ±10 m; >500 mb: ±20 m |
| **Temperature** | Sea surface & flight level: ±1°C |
| **Dew-Point** | -20 to +40°C: ±1°C; <-20°C: ±3°C |
| **Absolute Altitude** | ±10 m |
| **Turbulence Data** | 5 Hz minimum resolution (u, v, w components) |
| **Video/Image** | Clear transfer demonstrated to P-3 |

## Financial Summary

**Total Project Cost (2023–2025):** $390,000

**Budget Breakdown:**
- **Hardware:** $244,000
  - 16 BST S0 sUAS platforms with integrated METOC payload: $224,000
  - 2 Multi-Hole Turbulence Probes (build & integration): $20,000
- **Non-Recurring Engineering & Program Support:** $116,000
  - S0 payload integration, flight performance, full automation, NOAA data integration (AirOPS, HDOBS, VDM), video/image integration: $110,000
  - Project documentation: $6,000
- **Travel & In-Field Support:** $30,000
  - 1 clear-air calibration flight mission ('24): $6,000
  - 4 in-storm hurricane deployments ('23/'24): $24,000

**Funding Distribution:**
- **Year 1 (Jul 2023–Jun 2024):** $260,000 available
  - NRE: $110,000 | Area-I MHT: $20,000 | Travel: $18,000 | sUAS: $112,000
- **Year 2 (Jul 2024–Jun 2025):** $130,000 available
  - Travel: $12,000 | sUAS: $112,000 | Project doc: $6,000

## Notable Details

**Historical Context & Justification:**
- Program builds on 9 years of successful air-deployed sUAS research (2014–2023)
- NOAA's WP-3D hurricane research aircraft proven capable of deploying and recovering data from sUAS
- Platforms designated as "expendable/unrecoverable" technology, reducing operational risk to manned aircraft
- Concept of operations (CONOPS) validated through successful missions in four hurricanes

**Technical Maturity Goals:**
- Advance sUAS capability from developmental to routine operational use
- Increase flight duration, communication robustness, payload reliability
- Achieve continuous range operation at 150 NM (up from prior 135 NM record)
- Demonstrate sustained operation in extreme conditions (>65 kt winds, heavy precipitation, severe turbulence)

**Integration & Operational Requirements:**
- Full integration with NOAA P-3 onboard systems (KARMA situational awareness