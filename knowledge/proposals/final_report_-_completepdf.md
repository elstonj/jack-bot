# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- Type: NASA SBIR Phase II Final Report
- Client/Agency: NASA JPL (Jet Propulsion Laboratory)
- Program/Solicitation: NASA SBIR 2016-II, Topic S3.04 Unmanned Aircraft and Sounding Rocket Technologies
- Contract Number: NNX17CP13C
- Date: August 2019 (submitted); work performed 2017-2019
- BST Products/Systems Referenced: S2 XT (SuperSwift XT), SwiftCore FMS, SwiftPilot autopilot, SwiftTab operator interface, Multi-hole probe (MHP)
- Key Personnel: Jack Elston (PI), Dr. Dixon, Dr. Stachura, Dr. Diaz, Dr. Wardell

## Executive Summary
Black Swift Technologies successfully developed the S2 XT (SuperSwift XT), a ruggedized unmanned aircraft system designed for scientific data collection in harsh volcanic environments. This Phase II effort created a commercially viable, turn-key system capable of measuring trace gases, particulates, atmospheric parameters, and imagery in volcanic plumes through flights up to 20,000 ft MSL. The system was validated through field deployments in Hawaii and successfully demonstrated the simultaneous collection of multiple data types previously unobtainable from a single platform.

## Technical Approach

**Core Innovation:** Modified the SuperSwift airframe (from NASA-funded Phase I work) into the S2 XT variant with:
- Expanded operational ceiling to 20,000 ft MSL
- Enhanced durability for harsh environments (volcanic dust, high turbulence, strong winds)
- Field-swappable modular payload system with protected sensor integration
- Custom multi-hole probe (MHP) for 3D wind measurement
- Integrated data logging and sensor management system

**Technical Strategy:**
- Iterative "test early, test often" development philosophy
- Ground testing of individual systems before integration
- Progressive flight testing: Pawnee National Grasslands (PNG) for basic validation → San Luis Valley (SLV) for high-altitude/mountainous terrain → Turrialba volcano (Costa Rica) for operational deployment
- Comprehensive design for manufacturability (DFM) optimization for commercialization

## Products & Capabilities Described

### S2 XT (SuperSwift XT) Aircraft
- **What it is:** Fixed-wing small UAS (sUAS) with hand-launch capability, <2.5 kg sub-payload capacity
- **Specifications:**
  - Maximum altitude: 20,000 ft MSL (expanded from standard SuperSwift)
  - Endurance: Long-duration flights (specific duration not quantified in report)
  - Wind tolerance: Designed for high-altitude, high-turbulence environments
  - Airframe hardening: Modified to keep out volcanic dust and particulates; IP63 rating gaskets/seals
  - Motor cowl: Custom design to cool motor and protect against particulates
  - Construction: Two complete airframes built and tested
- **Notable features:** 
  - Modular nose cone payload bay with field-swappable capability
  - Autonomous terrain-following capability for mountainous areas
  - Integrated avionics bay with SwiftCore FMS

### SwiftCore Flight Management System (FMS)
- **What it is:** On-board autopilot and avionics system
- **Components:** SwiftPilot (autopilot) + SwiftTab (operator interface tablet UI)
- **Enhancements in Phase II:** 
  - Automatic mission planning for volcanic plume profiling
  - Terrain avoidance algorithms
  - Custom flight pattern generation (5 candidate patterns identified for volcanic operations)
  - Gesture-based interface for intuitive mission creation/modification
  - Integrated sensor initialization and data logging

### Scientific Payload Suite
**Sensors integrated into <2.5 kg package:**
- **Trace Gas Measurement:**
  - SO₂ (sulfur dioxide)
  - CO₂ (carbon dioxide)
  - H₂S (hydrogen sulfide)
  - CH₄ (methane)
- **Particulate Measurement:**
  - Particle size distribution and density assessment
  - Ash sampling cassettes for lab analysis
- **Atmospheric Parameters:**
  - Pressure
  - Temperature
  - Humidity (PTH - Pitot-Static-Humidity sensor)
  - 3D winds (via custom Multi-Hole Probe)
- **Remote Sensing:**
  - Electro-optical (EO) imagery
  - Thermal imagery
  - Forward video feed

### Custom Multi-Hole Probe (MHP)
- **What it is:** BST-designed wind measurement instrument for 3D air velocity estimation
- **Advantages over commercial alternatives:** Lighter weight, lower cost than existing commercial solutions
- **Development:** Designed in Phase I, wind tunnel tested and validated in Phase II
- **Integration:** Mounted in nose cone; CFD analysis optimized placement to account for fuselage effects
- **Commercialization:** Planned partnership with iMet to integrate MHP into their XF sensor suite expansion ports

### Pitot-Static-Humidity (PTH) Probe
- Custom design for harsh environment durability
- Wind tunnel verification and testing completed
- Provides atmospheric pressure and humidity measurements

## Use Cases & Applications

**Primary Mission (Volcanic Plume Profiling):**
- In-situ measurement of volcanic gas composition (SO₂, CO₂, H₂S, CH₄)
- Particulate characterization (ash size, concentration, density profiles)
- 3D wind field mapping within plume
- Thermal and visual documentation
- Sample collection for laboratory analysis

**Specific Deployments:**
- **Fissure 8 (Hawaii, 2018):** Background trace gas measurements; comprehensive study including gas concentrations, particulate distribution, 3D winds, thermodynamic values, orthomosaic imagery, thermal mapping, sample collection, and 3D terrain models
- **Planned Turrialba Volcano (Costa Rica):** Full system operational validation; one of first approved Beyond Visual Line of Sight (BVLOS) flights on volcano in U.S.

**Related Applications:**
- Wildfire smoke monitoring (actively used by NOAA)
- Volcanic Ash Advisory Center (VAAC) model validation and input
- Volcanic Ash Transport and Dispersion (VATD) model improvement
- Aviation safety (ash hazard characterization)

**Scientific Objectives Addressed:**
1. Improve understanding of volcanic emission chemistry and physics
2. Enhance volcanic eruption prediction capabilities
3. Calibrate and validate remote sensing methods (satellites: ASTER, MODIS, AIRS, OMI)

## Key Results

**Phase II Accomplishments:**

*Airframe Development:*
- Designed, tested, and assembled two complete S2 XT airframes
- Successfully modified S2 UAS for volcanic environment (dust/particulate sealing)
- Expanded operational altitude capability to 20,000 ft MSL
- Validated aerodynamic performance in mountainous terrain

*Sensor Integration:*
- Developed first-of-its-kind sub-2.5 kg atmospheric sampling payload
- Mechanically and electrically integrated complete sensor suite
- Achieved data synchronization and proper timestamping across all instruments
- Validated sensor interfaces through lab and flight testing

*Flight Testing Results:*
- **Pawnee National Grasslands flights:** Validated basic airframe performance, aerodynamic behavior empty and at full payload weight, UI/control system functionality, sensor performance
- **San Luis Valley flights:** Demonstrated high-altitude operations (up to 14,000 ft), terrain-following capability, flight pattern generation/execution, sensor package validation in mountainous terrain
- **Hawaii deployment (Fissure 8):** Successfully collected:
  - Trace gas concentration measurements
  - Particulate size and distribution data
  - Three-dimensional wind field data
  - Atmospheric thermodynamic values
  - RGB orthomosaic imagery
  - Thermal maps
  - Atmospheric samples for lab analysis
  - 3D terrain models of fissure and surrounding lava flow

*Software Development:*
- Modified SwiftTab UI for easy creation of sampling missions
- Developed data analysis software for in-flight validation
- Created data management plan for field campaigns
- Implemented automatic mission planning with volcanic-specific flight patterns

*Unique Innovation Validated:*
- Demonstrated simultaneous collection of multimodal data (gases, particulates, imagery, wind, thermodynamics) providing insights not previously possible from single platform

## Financial & Contractual Details
- **Total cumulative costs:** $723,117.00 (as of August 30, 2019)
- **Physical completion:** 100%
- **Contract duration:** 24 months (approximately 2017-2019)

## Notable Details

**Phase II-E Extension & Future Plans:**
- Successfully negotiated Phase II-E extension with USGS and private company investment
- Planned upgrades: VTOL (Vertical Take-Off and Landing) capabilities for S2 XT
- Additional volcano sampling payload development
- Long-distance data link creation
- Planned USGS deployment to Makushin volcano (Aleutian Islands)

**Commercial Partnerships & Mission Infusion:**
- **USGS:** Integration into Makushin volcano campaign
- **NOAA:** Active use of S2 XT improvements for wildfire monitoring flights
- **iMet:** Partnership to commercialize MHP technology as part of XF sensor suite
- **IAVCEI:** Potential participation in calibration campaign

**Regulatory & Operational Achievements:**
- Secured FAA and NASA flight approvals (AFSRB and FRRB clearances)
- Demonstrated capability across six successful NASA flight safety review boards in two years
- First approved BVLOS flight on volcano in US (planned)
- First commercial operator to secure permission for flights in National Parks (Great Sand Dunes NP survey flights conducted)
- International deployment capability (Costa Rica operational approvals secured)

**Competitive Advantages Demonstrated:**
- Purpose-built design specifically for harsh environment scientific missions (vs. commercial COTS platforms)
- Rugged airframe with extended flight envelope compared to Dragon Eye and Vector Wing systems
- Higher payload capacity, longer endurance, higher ceiling than comparable systems
- Modular field-swappable payload architecture enabling rapid sensor reconfiguration
- Direct control over FMS architecture enabling custom scientific mission planning tools
- Lighter, lower-cost custom MHP vs. existing commercial wind measurement solutions

**Team Expertise:**
- Dr. Elston (PI): Program leadership, scientific mission integration
- Dr. Stachura: Flight safety, certification, aircraft systems
- Dr. Dixon: Autopilot and state estimation algorithms, aerodynamic analysis
- Dr. Diaz: Volcano science, international collaboration
- Dr. Wardell: Data analysis software, sensor integration

**Risk Management:**
- Iterative testing at each phase (test early, test often philosophy)
- Escalating flight test locations (flat grassland → high-altitude terrain → active volcano)
- Multiple backup test sites identified (Turrialba and Volcanoes National Park)
- Comprehensive ground testing before flight integration

**Document Quality Note:** This is a comprehensive, well-structured Phase II final report with detailed technical accomplishments, supporting appendices referenced but not fully included in provided text. The document demonstrates substantial progress from Phase I concept through validated operational system capable of deployment at actual volcanic sites.