# SBIR 2018-1 Questions and Answers #7

## Document Metadata
- Type: Q&A clarification document
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration)
- Program/Solicitation: SBIR 2018-1
- Date: December 22, 2017
- BST Products/Systems Referenced: None directly mentioned
- Key Personnel: Not identified in this document

## Executive Summary
This is an official NOAA SBIR 2018-1 Q&A document clarifying requirements and acceptability criteria across multiple subtopics (8.2.1 through 8.3.5). The document addresses technical specifications, cost targets, acceptable solutions, and data requirements for various ocean observing, atmospheric sensing, and marine resource protection technologies. This document marks the final round of questions ("NO FURTHER QUESTIONS PERTAINING TO THE SOLICITATION AND ITS SUBTOPICS ARE PERMITTED").

## Key Subtopics & NOAA Requirements

### Subtopic 8.2.1: Phytoplankton Detection Device
- **Requirement**: Portable, hand-carried device to identify and characterize phytoplankton species in coastal/inland waters
- **Portability**: Hand-carry capability; robust enough for moving platforms (boats) or stationary deployment (piers)
- **Performance**: Must acquire statistically representative data within minutes
- **Scope**: Phase I must include instrument system design; market research alone insufficient
- **Data Support**: NESDIS/STAR has no phytoplankton imagery archive; proposers must establish partnerships with research institutions
- **Species Focus**: Common algal species in coastal/inland waters (to be determined in Phase I)

### Subtopic 8.2.5: Low-Cost Mooring Beacon
- **Reference System**: Xeos Kilo (~$3,000 plus satellite subscription)
- **Function**: Transmit location data only (latitude/longitude), not oceanographic data
- **Deployment**: Waterproof to 500m depth; attached to instrument package without subsurface expression
- **Operational Life**: 6-8 month deployments
- **Transmission Schedule**: Minimal data transmission recommended; 1-2 times daily sufficient for mooring rescue operations (backup to 2-3 times daily if needed)
- **Cost Target**: Lower than current $3,000 baseline; focus on reducing device cost and satellite transmission costs
- **Use Case**: Directing rescue/recovery operations for adrift or stranded moorings

### Subtopic 8.2.6: Fog Detection Sensor for Navigation
- **Mounting**: Shore/coastal structures near navigation channels (not buoy-mounted as originally conceived, though buoy deployment now "tantalizing" and being explored)
- **Detection Methods**: Images/grayscale analysis suggested but not required; seeking innovative alternatives
- **Performance Goals**: 5-10 nautical mile detection range (minimum 5nm, maximum 10nm)
- **Data Transmission**: GOES, Iridium, or ipmodem every 18 minutes (three 6-minute bundles averaged/compressed)
- **Reporting Frequency**: Every 18 minutes; automated IP polling nightly (midnight-4am) for gap-filling
- **Environmental Challenges**: Surface spray, ice, snow, salt, dirt, sand, bird activity are constant problems; cannot be fully avoided while meeting maritime commerce support mission
- **Design Priority**: Innovative, simpler, less costly (initial and recurring), reduced maintenance/servicing, significantly less power consumption
- **Height**: Depends on detection capability and local requirements; 25-foot height typical for pilot eye level

### Subtopic 8.2.7: Autonomous Vehicle for Gulf Dead Zone Mapping
- **Primary Vehicle Concept**: Gliders mentioned extensively but not exclusively required
- **Alternative Solutions**: Long-endurance waterproof drones with submersible payloads acceptable if they "effectively enhance our mapping and monitoring capabilities through the NGOMEX Dead Zone"
- **Acceptance Criteria**: Vehicle must resolve challenge of mapping dead zone "effectively and cost-efficiently"
- **Flexibility**: NOAA open to solutions beyond gliders

### Subtopic 8.2.9: Integrated Data Logger (Depth/Position)
- **Cost Target**: Under $20,000 (reference point: survey-grade GPS now available for under $1,000)
- **Data Integration**: Combine depth measurements from acoustic depth sounder with GPS position data
- **Logging Frequency**: 1 second or less
- **Output Format**: Must be ingestible by ESRI ArcGIS; comma-delimited file acceptable
- **Current Workflow**: NMEA string extraction from depth sounder + GPS position combined with Pathfinder software conversion to GIS shapefile
- **Requirement**: Single integrated record per observation (one depth/position pair per record in decimal degrees)
- **Use**: Create volume estimates for mapping applications

### Subtopic 8.2.11: Renewable Energy for NOAA Buoys
- **Technology Focus**: Ocean-powered energy sources (wave energy conversion devices acceptable)
- **Example Power Level**: ~10W sufficient for some instrumentation
- **Reference Systems**: 
  - Standard NDBC buoy (www.ndbc.noaa.gov) for power requirements
  - Self-Contained Ocean Observing Payload (SCOOP) system for smaller buoy platforms
- **Drifting Buoy Applications**: Yes, would benefit from compact wave energy; could recharge batteries and extend operation
- **Acceptance**: All innovative renewable energy technologies welcome; not limited to wave energy

### Subtopic 8.2.12: Low-Cost Weather Observing Systems
- **Cost Philosophy**: "The cheaper the better"; NOAA has many expensive systems (weather radars, satellites); new systems measured in millions/year will face challenges without extraordinary evidence of beneficial impact
- **Platform Flexibility**: Land, water, air-based all suitable; satellite/radar applications also eligible
- **Data Transmission**: Sub-hourly time scale ideal (weather prediction moving toward hourly data assimilation); more than once per hour target
- **Data Types Needed**:
  - State-of-system observations (for data assimilation)
  - New insights into atmospheric/environmental processes
  - Data gaps: observations below cloud decks (especially over oceans); soil state; snow pack depth/coverage
  - Sanity checks on other data sources (e.g., remote temperature data for anchoring satellite radiance data)
- **Data Volume**: NOAA handles hundreds of GB of satellite data/day; pre-processing/averaging expected (e.g., average over minute or tens of minutes rather than tenth-of-second sampling)
- **Wave Height Data**: Specifically noted as useful; no current operational shipboard wave measurement equipment exists; need for inexpensive, easily installable systems
- **Hybrid Approaches**: Wave energy-powered weather systems being considered favorably ("bit beyond strict wording of solicitation, but personally... relevant enough to consider")

### Subtopic 8.3.2: Marine Mammal/Protected Species Protection in Aquaculture
- **Primary Animals of Concern**: Marine mammals and free-swimming protected species whose native range coincides with aquaculture:
  - Whales (various species)
  - Dolphins
  - Seals
  - Otters
  - Sea turtles
- **Problem Types**: Animals living/migrating near farm gear or actively feeding on crop
- **Aquaculture Types**: All marine aquaculture (finfish, shellfish, seaweed), coastal and offshore
- **Gear Types**: Submerged vertical lines or other gear posing entanglement risk
- **Scope**: Focused on aquaculture gear (not capture fisheries, though relevant literature may inform solutions)

### Subtopic 8.3.4: Advanced Warning Visualization for Non-Scientists
- **Integration**: Collaborate with current NWS warning generation system (not replace it)
- **Current Gap**: System provides lat/lon numbers for polygons but lacks hazard tracking tool; treats hazards as points rather than areas
- **Needed Capability**: Tool to track specific hazards (e.g., hurricane rain bands, winter storm snow bands, hail, tornadoes) with location-specific threat information
- **Target Audience**: "Non-scientists" = those without meteorology degrees (e.g., TV weather personnel, emergency managers, general public)
- **Data Source**: Radar as primary data source likely
- **Flexibility**: System can track meteorologist-defined features; doesn't need to directly match particular attributes
- **Delivery Format**: Online application/website primary priority, but offline hardware option (weather radio-like with interactive display/touchscreen) could have utility in connectivity-limited areas
- **Update Frequency**: 
  - Slowly progressing events (hurricanes, winter storms): every 10-15 minutes
  - Rapidly moving events (severe thunderstorms, tornadoes): at least every 4-5 minutes (radar-like frequency)
- **Data Volume**: Real-time transmission important for life-threatening hazards

### Subtopic 8.3.5: Plant-Based Feeds for Aquaculture
- **Species Priority**: NOAA has not identified priority species or initial targets
- **Feed Types**: Macroalgae/seaweed-based finfish feeds qualify
- **Phase I Testing**: Live fish testing NOT required as part of Phase I effort

## Notable Details

1. **Final Q&A Round**: Document explicitly states no further questions permitted, indicating this was the final clarification opportunity before proposal submission

2. **Cost Consciousness**: Strong theme across multiple subtopics emphasizing cost reduction and affordable solutions (mooring beacons at $3K target, data logger under $20K, general preference for "cheap" observing systems)

3. **Flexibility on Solutions**: Multiple subtopics show NOAA openness to alternative technical approaches beyond those explicitly mentioned (e.g., accepting drones instead of gliders for dead zone mapping, accepting buoy-mounted fog sensors despite shore-based original conception)

4. **Data Integration Emphasis**: Several subtopics stress need for integrated, GIS-compatible data rather than separate streams

5. **Real-time Data Value**: Recognition that real-time data can improve field operations (e.g., mooring rescue logistics) but balanced against cost constraints

6. **Partnership Expectations**: Subtopic 8.2.1 explicitly requires proposers to establish partnerships with research institutions for data/resources

7. **Environmental Robustness**: Subtopic 8.2.6 acknowledges harsh marine environment challenges (spray, ice, salt, bird activity) as unavoidable constraints

8. **Data Assimilation Focus**: Weather/oceanographic subtopics emphasize importance of filling data gaps for assimilation into forecasting models

---

**Note**: This document contains no direct references to Black Swift Technologies or its products. It is a NOAA SBIR clarification document potentially relevant to BST if the company was considering proposals under any of these subtopics.