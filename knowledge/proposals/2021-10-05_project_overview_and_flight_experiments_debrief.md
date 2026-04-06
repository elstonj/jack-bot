# Makushin Mission Debrief: Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: Project overview and flight experiments debrief (presentation)
- Client/Agency: USGS (U.S. Geological Survey); NASA Armstrong Flight Research Center
- Program/Solicitation: Phase II SBIR (Small Business Innovation Research) for volcano monitoring
- Date: 2021-10-05 (presentation date; missions flown September 2021)
- BST Products/Systems Referenced: S2 UAS, SwiftCore FMS, SwiftPilot 4.0 (in development), VTOL S2 (in development)
- Key Personnel: C. Kern (last editor)

## Executive Summary
Black Swift Technologies deployed its S2 fixed-wing UAS to Makushin Volcano in Alaska in September 2021 as part of a Phase II SBIR effort for volcano monitoring in harsh environments. The mission tested the S2's capability to operate in extreme conditions (>50kt winds, >1600 ft/min downdrafts, near-freezing temperatures) with modular sensor payloads for trace gas measurement and photogrammetry. While four flights were completed with two reaching the summit, challenging wind conditions and downdrafts limited full mission objectives, though all flights demonstrated the S2's autonomous safety systems and data collection capabilities.

## Technical Approach

**Mission Design:**
- Operated from Dutch Harbor Airport, Alaska
- Required COA (Certificate of Authorization), waiver, and TFR (Temporary Flight Restriction) coordination
- Fully autonomous BVLOS (Beyond Visual Line of Sight) operations with no string of observers required
- Redundant communication link with real-time backhaul to internet
- Sensor-directed flight control

**Autonomous Safety Systems:**
- ADS-B integration for manned traffic awareness (displays speed, altitude, registration)
- Automatic mission abort when dangerous conditions detected (high headwinds >50kts + downdrafts)
- Automatic terrain avoidance and climb-back capabilities
- Real-time telemetry monitoring

**Flight Planning:**
- Wind estimation protocols with go/no-go decision criteria (<20kts for launches/ingress/egress)
- Terrain and airspace analysis
- Dedicated radio link with satellite backup capability
- NASA MTS (Mission Traffic System) integration

## Products & Capabilities Described

### S2 UAS Fixed-Wing System
**Specifications:**
- Max takeoff weight: 20.5 lbs
- Wingspan: 10 ft
- Flight ceiling: 14,000 ft
- Max endurance: 90 min (with max payload)
- Range: 63 miles (with max payload)
- Cruise speed: 42 mph
- Wind capability: 30 mph max (documented in tests; demonstrated >30kts wind resistance)

**Payload Capabilities:**
- Nose cone: 8 inch diameter × 25 inch length
- Payload capacity: 5 lbs
- Power available: 50 W total
- Geotagging accuracy: <1m in all directions
- Modular, field-swappable payload system (no specialized tools required)
- Supports single, dual, or triple sensor configurations

**Payload Configurations Deployed:**

1. **Trace Gas Payload** (Total mass: 9,495g)
   - Licor 850 CO2/H2O analyzer (1,300g)
   - Ocean Optics spectrometer (265g)
   - City Tech H2S sensor (17g)
   - City Tech SO2 sensor (17g)
   - Support electronics, wiring, mechanicals (698g)
   - Focus: atmospheric trace gas measurements for volcanic characterization

2. **Photogrammetry/Thermal Payload** (Total mass: 9,317g)
   - Sony a5100 EO camera (24MP) (289g)
   - FLIR Vue Pro-R thermal camera (640×480)
   - Extra ¾ propulsion battery for extended flight time
   - Scaffold, actuators, supply boards, servo (total mechanical: 530g)
   - Focus: summit imaging and thermal mapping

**Unique Capability:**
- Soil moisture measurement package with radiometer integrated into S2 payload nose cone described as "not available anywhere else"

### SwiftCore FMS
- Mature, scalable Flight Management System
- Controls S2 platform
- Enables sensor-directed flight control

### Technologies Under Development
- **VTOL S2:** Vertical takeoff/landing variant with increased flight time and climb power
- **SwiftPilot 4.0:** Advanced mission planning software with onboard DEMs (Digital Elevation Models), terrain-aware path planning, energy/wind-aware routing, real-time terrain and hazard mapping

## Use Cases & Applications

**Primary Mission:** Volcano monitoring with focus on:
- Summit imaging and thermal mapping
- Trace gas characterization (SO2, H2S, CO2)
- Photogrammetry for detailed 3D mapping
- Volcanic plume sampling (future objective)

**Operating Conditions Tested:**
- Extreme winds (>50kts headwinds encountered)
- Strong downdrafts (up to 2,000 fpm documented)
- Precipitation and clouds
- Near-freezing temperatures (never exceeded <5°C)
- High humidity (>80%)
- High-altitude terrain (Makushin summit operations)

**Future Application Areas Identified:**
- Wildland firefighting
- Additional volcano observations
- Operations in extreme environments generally

## Key Results

**Flight Summary (September 2021):**

| Flight | Date | Duration | Max Wind | Outcome | Notes |
|--------|------|----------|----------|---------|-------|
| #1 | 2021-09-10 | 61.5 min | <20kts launch | Success | Strong downdrafts, higher power usage than modeled |
| #2 | 2021-09-11 | 74.7 min | >50kts | Automatic abort | Excessive headwind and downdraft at 1.5km from summit; S2 autonomously turned back |
| #3 | 2021-09-14 | 75.4 min | <20kts launch | Success | **Successful completion of full 1 km² map** with EO and thermal of summit |
| #4 | 2021-09-14 | 33.8 min | <20kts launch | Automatic abort | Trace gas payload flight; encountered 2,000 fpm downdraft, S2 turned back at 1,000 ft AGL |

**Data Collection Results:**
- EO/thermal photogrammetry: Complete 1 km² summit map successfully acquired (Flight #3)
- Trace gas measurements: Sensors performed nominally and measured background atmosphere composition
- Volcanic gas characterization: Unsuccessful—could not characterize volcanic gases; spectrometer did not detect SO2
- Reason: Challenging wind/downdraft conditions prevented full summit sampling during trace gas payload flights

**Autonomous Safety Performance:**
- All flights landed safely with adequate battery reserves (6.3-10.5Ah remaining vs. 2.8Ah minimum)
- S2 automatically detected and responded to dangerous conditions (>50kts headwind, excessive downdraft) with safe return-to-home
- Automatic terrain avoidance maintained minimum 1,000 ft AGL during downdraft encounter
- Zero loss of aircraft

## Notable Details

**Operational Achievements:**
- Demonstrated BVLOS operations without string of observers or special ground equipment
- Successful integration of NASA MTS and ADS-B for traffic awareness in restricted airspace
- Operations in TFR (Temporary Flight Restriction) area with COA approval
- Real-time redundant communications with internet backhaul
- Platform stability in extreme conditions (>50kt winds, extreme downdrafts)

**Mission Limitations Identified:**
- Insufficient climb power to overcome strong downdrafts and high altitude headwinds
- Limited flight time prevented full mission objectives on days with adverse winds
- Trace gas payload deployment constrained by wind/downdraft conditions
- Cannot flight through clouds in TFR areas (regulatory constraint)
- Current ADS-B broadcast from UAS not visible to manned aircraft (unidirectional awareness only)

**Commercialization & Funding Opportunities:**
- NASA CCRPP (Climate Change Research Program) match opportunity: $500K-$2.5M match available
- NOAA offering $480K match
- Match can fund new deployments or R&D in extreme environment operations (wildland firefighting, additional volcano observations)
- Application deadline: Early January 2022

**Publication & Outreach:**
- 2021 AIAA RM (AIAA Rocky Mountain) presentation
- 2021 AGU (American Geophysical Union) presentation
- November UAS Colorado Meetup
- NASA and USGS press releases planned
- YouTube video documentation of flights available

**Prior Relevant Experience:**
- 2019 volcanic sampling missions at Hawaii eruption sites (Armstrong Flight Research Center)
- 8 successful flights conducted 2019-08-05 to 2019-08-09
- Prior NOAA partnerships with S2 EO/thermal photogrammetry payloads

**Development Roadmap:**
- VTOL S2: Increased flight time, climb power, closer-proximity operations
- SwiftPilot 4.0: Terrain-aware planning, energy-optimized routing, real-time hazard mapping
- Focus on enabling operations in clouds, at lower altitudes near volcanic summits, with enhanced endurance