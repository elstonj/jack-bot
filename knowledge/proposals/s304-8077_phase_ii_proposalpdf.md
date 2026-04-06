# S3.04-8077 Phase II Proposal

## Document Metadata
- Type: NASA SBIR Phase II Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR S3.04 Subtopic (Airborne Science)
- Date: 2016
- BST Products/Systems Referenced: SuperSwift XT, SuperSwift, SwiftCore Flight Management System (FMS), SwiftPilot (autopilot), SwiftTab (operator interface), Multi-Hole Probe (MHP), SwiftTrainer
- Key Personnel: Jack Elston (PI), Dr. Wardell (science lead), David Pieri (NASA technical monitor), Jorge Andres Diaz (subcontractor)

## Executive Summary
Black Swift Technologies proposes the development of the SuperSwift XT, a ruggedized small unmanned aircraft system (sUAS) specifically designed to collect in situ scientific data from volcanic plumes and other harsh atmospheric environments. Built on the proven SuperSwift airframe and SwiftCore FMS, the system will integrate a comprehensive sensor suite to measure volcanic gases (SO₂, CO₂, H₂S, CH₄), ash particulates, atmospheric parameters (pressure, temperature, humidity, 3D winds), and imagery. Phase II will complete mechanical and electrical integration, build and test the aircraft, develop flight planning software for volcanic profiling missions, and conduct extensive field validation.

## Technical Approach

**Core Strategy:**
- Enhance the commercially-available SuperSwift airframe with modifications for harsh environment operations
- Integrate proven SwiftCore FMS with enhanced flight planning capabilities
- Develop and integrate a purpose-built volcanic plume sensor suite
- Conduct extensive flight testing at three test sites (two in Colorado, one at an active volcano)
- Emphasize "test early, test often" agile development philosophy
- Achieve flight certification through NASA Airworthiness Flight Safety Review Boards (AFSRB) and Flight Readiness Review Boards (FRRB)

**Key Design Philosophy:**
The SuperSwift XT maintains the modular, field-swappable payload design that was central to the original SuperSwift, enabling quick sensor suite changes in the field and future adaptation to other scientific missions.

## Products & Capabilities Described

### SuperSwift XT (Enhanced Airframe)
**What it is:** Modified fixed-wing sUAS evolved from the commercialized SuperSwift platform, specifically hardened for volcanic plume measurement and other harsh environments.

**Proposed capabilities:**
- Maximum altitude: 20,000 ft MSL
- Flight time: 70+ minutes (single battery) to 120+ minutes (dual battery)
- Climb angle: 37-44° depending on battery configuration
- Gross takeoff weight: 13.7-15.5 lbs
- Hand-launchable design
- Sustained thrust-to-weight ratio >1.0 up to 8 kft density altitude (critical for hand-launch at high elevations)

**Design modifications:**
- **Propulsion system redesign:** New motor providing thrust-to-weight ratio of 1.4 at sea level (vs. original 0.5), enabling sustained flight at 20 kft and improved climb performance
- **Dual battery capability:** Custom battery trays and fuselage modifications accommodate second 6-cell 9,000 mAh HV LiPo battery pack for extended range
- **Increased control authority:** Control surface sizing increased (ailerons +29%, flaps +32%, ruddervators +59%) for better performance in turbulent conditions
- **Environmental protection:** Sealed access panels with gaskets; larger pitot-static tube to prevent blockage from water droplets and particulates; custom motor cowl with integrated cooling fins; aerodynamic shells protecting exposed components; ash protection coverings
- **Modular payload bay:** Removable nose cone with standardized power/data/mechanical interfaces allowing rapid field swaps of different sensor suites

### SwiftCore Flight Management System (FMS)
**What it is:** Proven autopilot and avionics suite specifically designed for scientific missions, consisting of SwiftPilot (autopilot) and SwiftTab (operator interface).

**Capabilities:**
- On-board Linux computer for data logging and sensor control
- Modular payload bus for instrument integration
- Extensible architecture for rapid sensor integration
- Previously demonstrated 240 MB/s data logging capability for radiometric data
- Strong heritage in NASA science missions

**Phase II enhancements planned:**
- Add automatic mission profile generation for five volcanic plume profiling scenarios
- Implement terrain-following flight capability for mountainous regions
- Enhanced flight planning tools for scientists to generate optimal flight patterns
- Support for autonomous low-altitude terrain following

### Volcanic Profiling Sensor Suite
**Selected sensors (8 primary + optional mass spectrometer):**

1. **Multi-Hole Probe (MHP)** - BST-designed
   - Measures 3D wind velocity (angle of attack, sideslip angle)
   - Novel design using 3D printing for cost reduction and easy modification
   - Wind tunnel tested; outperformed commercial Aeroprobe sensor across tested angles
   - Lighter and lower cost than existing commercial solutions
   - Plans for commercialization with sensor manufacturer iMET

2. **Trace Gas Sensor (iMET)**
   - Measures CO₂, SO₂, CH₄, H₂S
   - Captures major and minor volcanic gas species

3. **Nephelometer**
   - Measures particle concentration, velocity, and sizing
   - Provides ash particle characterization

4. **Atmospheric Sensors**
   - Pressure transducer
   - Temperature sensor
   - Humidity sensor

5. **Imaging Systems**
   - Downward-looking EO (electro-optical) camera for ground/vent imagery
   - Thermal camera
   - Forward-facing video camera for situational awareness

6. **Ash Sampling Capability**
   - Physical ash sample collection

**Payload integration:**
- All sensors integrated into removable nose cone
- Electrical and data integration plan developed in Phase I
- CFD validation conducted on nose cone airflow
- Common power/data interface for seamless integration with SwiftCore FMS

**Optional upgrade:**
- Mass spectrometer payload module (alternative nose cone configuration) pending identification of lighter/smaller sensor variant

## Use Cases & Applications

### Primary Mission: Volcanic Plume Monitoring
Five mission profile types identified in Phase I:

1. **Volumetric Sampling**
   - Max altitude: 19,300 ft MSL
   - Time of flight: 75 min
   - Max range: 10.4 km
   - Climb slope: 14°
   - Purpose: Comprehensive 3D sampling of plume composition

2. **Cylindrical Profiling**
   - Max altitude: 19,800 ft MSL
   - TOF: 34 min
   - Max range: 7.6 km
   - Climb slope: 14°
   - Purpose: Vertical plume structure characterization

3. **Long Distance Gradient**
   - Max altitude: 19,300 ft MSL
   - TOF: 74 min
   - Max range: 37.3 km
   - Climb slope: 14°
   - Purpose: Downwind plume transport monitoring

4. **Vent Contouring**
   - Max altitude: 17,850 ft MSL
   - TOF: 14 min
   - Max range: 7.4 km
   - Climb slope: 31°
   - Purpose: High-resolution local source characterization

5. **Terrain Mapping**
   - Max altitude: 14,500 ft MSL
   - TOF: 90 min
   - Max range: 5.0 km
   - Climb slope: 31°
   - Purpose: Baseline topographic and environmental data

### Test Volcano Sites
- **Turrialba, Costa Rica** (height: 10,958 ft)
- **Popocatépetl, Mexico** (height: 17,802 ft)

### Phase II Test Sites
1. **Pawnee National Grasslands, Colorado** - initial flight testing (NASA approval already exists from prior missions)
2. **Mountainous Colorado location** - terrain following and CONOPS validation (tall mountain with thousands of feet elevation change)
3. **Active volcano site** - real-world system validation and scientific data collection

### Broader Applications Beyond Volcanic Monitoring
The modular payload design enables use for:
- Wildfire smoke hazard characterization
- Toxic release monitoring
- Dust storm analysis
- Air quality research
- Atmospheric chemistry studies
- Model validation for dispersion forecasting

## Key Results from Phase I

### CONOPS and Sensor Selection
- Defined five mission profile types based on volcanic monitoring requirements
- Conducted comprehensive sensor trade study
- Selected 8-sensor primary suite plus optional mass spectrometer
- Validated sensor selection against payload weight/CG constraints

### SuperSwift XT Design Development
- Analyzed SuperSwift airframe performance against mission requirements
- Identified necessary modifications to propulsion system, mechanical design, and environmental protection
- Designed enhanced propulsion system (new motor + dual battery capability) with detailed performance predictions
- Designed environmental hardening features (sealed access, protected motor, improved pitot-static)
- Increased control surface areas for improved turbulence handling
- Created detailed CAD models of all components and assemblies
- Demonstrated feasibility of achieving all performance objectives

### Volcanic Plume Sensor Suite Development
- **Multi-Hole Probe:** Designed, built, and wind tunnel tested novel MHP
  - 3D printed construction reduces cost and enables easy modification
  - Performance exceeded commercial Aeroprobe across tested angles
  - Firmware developed and validated
- **Payload Integration:** 
  - All sensors integrated in CAD models
  - Mechanical mounting designed and validated against weight/CG
  - Electrical and data integration architecture developed
  - CFD analysis completed on nose cone airflow
  - Nose cone and mechanical components ready for manufacturing

### Flight Certification
- Identified three Phase II test sites
- Prepared complete NASA documentation for Airworthiness Flight Safety Review Board and Flight Readiness Review Board for Pawnee National Grasslands site
- Documentation ready for submission at Phase II commencement to minimize certification delays
- Demonstrated experience with NASA review processes (6 successful board completions in prior 2 years)

## Notable Details

### BST's Commercial Track Record and Infrastructure
- Self-funded since founding in 2011 through commercial sales, consulting, development contracts, and non-equity grants
- **Previous NASA SBIR success:** Soil moisture mapping sUAS project (currently Phase II-E) has achieved $240,000 non-NASA investment for commercialization
- **Commercial products in market:**
  - **SuperSwift** - proven platform from soil moisture mapping SBIR; actively used in MALIBU (Multi AngLe Imaging Bidirectional Reflectance Distribution Function) project with two completed flight campaigns
  - **SwiftTrainer** - independently verified as top-performing 3D photogrammetry sUAS for surveys and orthomosaics
  - **SwiftCore FMS** - marketed commercially; provides tracking accuracy and sensor timing integration exceeding all competitive systems
- **Commercialization partnerships:** Working with Goddard Space Flight Center on MALIBU commercialization; planning to work with iMET on multi-hole probe sensor commercialization

### Scientific and Operational Context
- **Aviation safety imperative:** ~33,000 new passenger/freighter aircraft will be added globally over next 20 years; 4.5% annual growth in air travel increases volcanic ash encounter risk
- **Data gap:** Volcanic ash transport and dispersion (VATD) models lack in situ validation data; satellite ash thickness and density "are largely unvalidated" (JPL volcanologist Dave Pieri); nine Volcanic Ash Advisory Centers (VAACs) worldwide rely on unvalidated models
- **Unique capability:** Small sUAS can access airspace impossible for manned aircraft; significantly lower cost than larger UAS or manned platforms for high-risk, high-value applications
- **Scientific value:** System will enable rapid response data collection (particle size-frequency distribution, vertical ash concentration distribution, SO₂ flux) immediately after eruption—data previously unobtainable
- **Broader societal impact:** Improved VATD model validation directly supports aviation safety, pollution alerts, wildfire smoke monitoring, and toxic release forecasting

### Technical Innovation Highlights
- **Multi-hole probe:** Novel lightweight, low-cost 3D-printable design outperforming expensive commercial alternatives
- **Modular payload architecture:** Enables rapid field swapping of sensor suites and future adaptation to other scientific missions
- **Flight management system integration:** SwiftCore FMS designed specifically for scientific missions (vs. commercial autopilots), enabling