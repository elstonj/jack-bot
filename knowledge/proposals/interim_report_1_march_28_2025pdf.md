# Demonstrating Persistent IR Measurements Over Wildfires Using Small, Fixed Wing Uncrewed Aircraft – Interim Demonstration Report #1

## Document Metadata
- **Type:** Interim Demonstration Report (Phase III R/R&D project)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA contract 80NSSC25CA043
- **Date:** March 30, 2025
- **BST Products/Systems Referenced:** Black Swift S2 UAS
- **Key Personnel:** Jack Elston (BST), Maciej Stachura (BST), Matt Fladeland (NASA), William Wade (NASA), Joshua Schwarz (NOAA), Joey Taylor (NOAA), Chris Bolz (USFS), Sean Triplett (USFS), Eric Rhoden (USFS)

## Executive Summary
This interim report documents progress on a NASA-funded demonstration to validate 24-hour persistent infrared wildfire monitoring using Black Swift Technologies' S2 small unmanned aircraft equipped with NOAA's NightFOX sensor payloads. The project aims to overcome limitations of satellite-based systems (low spatial/temporal resolution, long revisit times) by demonstrating continuous coverage through seamless handoffs between multiple aircraft operating day and night. The demonstration is scheduled for May 2025 at Sunny Slope Sod Farm in Longmont, Colorado.

## Technical Approach

**Core Strategy:**
- Deploy multiple S2 UAS in rotation with seamless handoffs to eliminate data gaps and achieve 24-hour continuous coverage
- Equip at least two S2 aircraft with NOAA NightFOX payloads calibrated for high-resolution infrared imagery
- Configure S2 systems for FAA-compliant night flying operations
- Deploy calibration targets for ground-truth validation
- Collect geo-rectified IR imagery and telemetry for real-time and post-mission analysis
- Generate data products in formats compatible with USFS operational systems (shapefiles, GeoTIFFs, NetCDF)

**Flight Operations Methods:**
- Pre-mission checks and calibration at BST's Boulder, Colorado facilities
- Detailed flight plans with predetermined transects and orbits simulating fireline and hotspot monitoring
- Sequential UAS launches to maintain continuous coverage with timed handoffs
- Night operations adhering to FAA guidelines with visual observers and redundant safety systems
- IR imagery cross-referenced with deployed calibration targets for validation

**Data Strategy:**
- Real-time streaming where feasible; storage for post-analysis
- Pre-filtering onboard S2 embedded computers prioritizing 4 µm and 1.6 µm channels for downlink
- Support for near-real-time decision-making in wildfire management
- Integration with USFS platforms including ATAK (Android Tactical Awareness Kit) via WFTAK plugin

## Products & Capabilities Described

### Black Swift S2 UAS
- **Description:** Small, fixed-wing, cost-effective, modular platform designed for sustained operations and extreme environments
- **Proposed Use:** Primary airframe for persistent wildfire monitoring; capable of seamless multi-aircraft handoffs for continuous coverage
- **Specifications:**
  - Climb Rate: 950 ft/min
  - Cruise Speed: 48 KIAS
  - Endurance: 2 hours
  - Launch Method: Catapult
  - Recovery Method: Belly land
  - Operating Altitude: Up to 15,000 MSL
- **Key Features:** Already equipped for FAA-compliant nighttime operations; proven integration of hardware and software for extreme conditions; developed through partnership with NASA SBIR program
- **Track Record:** Years of research and operational experience; history of reliable performance in challenging environments (wildfire, hurricane, volcanic monitoring)

### NOAA NightFOX Payload
- **Description:** Field-proven remote sensing payload developed by NOAA for fire detection and characterization
- **Sensor Suite:**
  - FLIR camera (thermal infrared)
  - 1.6-micron SWIR (Short-Wave Infrared) camera
  - Synchronized scanning telescopes for fire radiative power (FRP) measurement
- **Proposed Use:** Mounted on S2 aircraft to provide on-demand, high-resolution infrared imaging for active-fire phase monitoring and post-event analysis
- **Performance Validation:** Recently validated during NOAA flight campaigns; undergoing maintenance and re-calibration for this demonstration
- **Data Channels:** 4 µm and 1.6 µm channels prioritized for downlink to support low-latency products

## Use Cases & Applications

**Primary Application:** Wildfire monitoring and management support
- **Continuous Perimeter Mapping:** Real-time monitoring of fire perimeter at ~1 km altitude above ground level (AGL)
- **Hotspot Detection:** Identification and tracking of active fire hotspots
- **Fire Intensity Assessment:** Fire radiative power measurements through FRP sensor capability
- **Post-Event Analysis:** High-resolution data for analyzing fire behavior after active suppression phase

**Operational Integration:**
- Near-real-time data delivery to USFS decision-makers during active wildfire events
- Integration with existing Forest Service operational dashboards and platforms (MTS, ATAK)
- Support for rapid turnaround in wildfire decision-making
- Complementary capability to satellite systems (MODIS, VIIRS) with higher spatial/temporal resolution

**Addressed Gaps:**
- Overcome satellite limitations: low spatial resolution, long revisit times (MODIS, VIIRS), inability to provide persistent coverage
- Enable proactive (vs. reactive) wildfire management
- Support improved fire-weather forecasting through continuous monitoring

## Key Results & Work Performed (Period Ending March 30, 2025)

**Kickoff Meeting (January 28, 2025):**
- Established formal collaboration with NASA Ames, NOAA, USFS, and BST
- Defined demonstration goals, deliverables, timeline, and payload configuration
- NOAA briefed on NightFOX sensor suite specifications
- USFS emphasized importance of near-real-time data delivery and compatibility with existing platforms (AFF trackers, GIS shapefiles)
- Scheduled demonstration for May 2025 with Flight Readiness Review 2-4 weeks prior (led by William Wade, NASA Ames)
- NOAA confirmed full team availability after March 2025

**Licensing & Coordination:**
- Identified USFS contacts: Chris Bolz and Sean Triplett for data coordination
- Initiated licensing process for WFTAK (Wildland Fire Team Awareness Kit) plugin for ATAK
- Began discussions on data delivery frequency, format, and interoperability (NetCDF, KMZ formats)
- Determined optimal data integration approaches with existing wildfire operational frameworks

**FAA Certificate of Waiver or Authorization (COA):**
- Completed and submitted COA request describing:
  - Operation purpose: research on UAS over active wildfires
  - Aircraft specifications and flight performance parameters
  - Operational area (Sunny Slope Sod Farm, Longmont, CO)
  - Flight safety protocols and contingency procedures
- Referenced BST's extensive compliance history and prior operational data
- COA currently under FAA review pending final site confirmation and payload integration testing

**USFS Collaboration & Demonstration Adaptation:**
- Confirmed altitude preference: ~1 km AGL for maximizing IR coverage
- Discussed perimeter mapping frequency and handoff cadence for continuous surveillance
- Gathered input on required data product formats (shapefiles, GeoTIFFs, NetCDF)
- Identified use cases for near-real-time integration with wildfire management dashboards
- BST committed to generating both raw and processed data in USFS-compatible formats
- Committed to exploring streaming downsampled data during flight for near-real-time use

**NOAA Payload Status:**
- Confirmed NightFOX payload availability for scheduled May 2025 demonstration
- Provided updates on recent performance validations during other NOAA campaigns
- Established joint timeline for sensor checkout, re-calibration, and S2 integration
- Agreed to test pre-filtering data onboard S2 embedded computers
- Strategy: prioritize 4 µm and 1.6 µm channels for downlink to optimize telemetry bandwidth vs. USFS low-latency product needs

**Upcoming Milestones:**
- Mid-April: Finalize system integration and ground tests
- Late April: Preliminary test flights and payload calibration at Sunny Slope Sod Farm
- 2 weeks before May demo: Complete NASA Flight Readiness Review
- May 2025: Conduct 24-hour demonstration with full partner coordination
- Within 90 days post-demo: Deliver geo-rectified imagery, aircraft state data, telemetry logs, full flight report
- Final report: Summarize operational findings, equipment list, recommendations for scaling to operational system

## Notable Details

**Competitive Advantages & Positioning:**
- BST uniquely positioned due to proven expertise in extreme-environment UAS operations and Earth science applications
- S2 platform culmination of years of research; specifically designed for reliable performance in extreme conditions
- In-house capability spanning autopilots to data processing software ensures seamless hardware-software integration
- Established partnerships with NASA, NOAA, USGS provide credibility and resource access

**Partnership Synergies:**
- NOAA partnership provides field-proven NightFOX payload (no development risk)
- NASA partnership includes technical oversight and Flight Readiness Review expertise
- USFS partnership ensures demonstration aligns with actual operational needs and future adoption potential
- Collaboration positions BST for scaling to operational system and future funding opportunities

**Test Site:**
- Sunny Slope Sod Farm, Longmont, Colorado: private farm offering secure, controlled environment
- Ideal for extended UAS operations with minimal logistical constraints
- Accessible for both daytime and nighttime mission testing

**Technical Innovations Highlighted:**
- Integration of night-flying capabilities into S2 for continuous monitoring (addresses critical safety/compliance/performance challenges)
- Seamless multi-aircraft handoff operational model for persistent coverage
- Onboard data pre-processing to optimize bandwidth (prioritizing key IR channels)
- Flexible data format outputs for interoperability with multiple stakeholder systems

**Operational Readiness:**
- S2 already FAA-compliant for nighttime operations (major de-risking factor)
- Calibration target deployment planned for scientific validation
- Visual observers and redundant safety systems in place for night operations