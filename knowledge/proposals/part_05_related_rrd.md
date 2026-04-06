# Part 05: Related R/R&D
## NASA 2016 SBIR Volcano Phase II Proposal

## Document Metadata
- Type: Proposal section (Related Research & Development)
- Client/Agency: NASA
- Program/Solicitation: NASA 2016 SBIR Phase II - Volcano Topic
- Date: Created 2016-12-02; Modified 2016-12-09
- BST Products/Systems Referenced: SwiftCore FMS, SwiftPilot, SwiftStation, SwiftTab, SuperSwift XT Volcanic Profiling System
- Key Personnel: Jack Elston (PI), Brian Argrow

## Executive Summary
This section surveys prior research into UAS-based volcanic emissions monitoring and documents Black Swift Technologies' and the PI's significant related R&D. BST developed the SwiftCore FMS avionics package for scientific sUAS missions, which forms the basis for the proposed SuperSwift XT Volcanic Profiling System. The PI has extensive experience designing and operating specialized sUAS for extreme atmospheric sampling, including pioneering work with the Tempest aircraft during VORTEX2 supercell intercepts.

## Technical Approach

### SwiftCore FMS & SuperSwift XT System
- **Components**: SwiftPilot autopilot, SwiftStation ground station, SwiftTab user interface software
- **SwiftPilot Features**:
  - High-accuracy GPS
  - Advanced mission planning tools
  - Modular sensor payload architecture
  - Linux single board computer for on-board sensor data processing and custom algorithm execution
  - Designed specifically for scientific missions vs. commercial applications
- **Development Basis**: SwiftCore FMS currently in use by university research groups and NASA Phase II SBIR soil moisture mapping project
- **Improvement Over Previous Systems**: SwiftPilot addressed limitations of Piccolo autopilot state estimation, particularly for wind measurement during aircraft maneuvers

### PI's Prior Experience: Tempest Aircraft & VORTEX2
- **Platform**: Highly modified off-the-shelf airframe with customized networked sUAS communication, command, and control architecture
- **Design Drivers**: Storm dynamics, FAA regulations, lessons learned from CoCoNUE experiment
- **Key Accomplishments**:
  1. First sUAS data collection near supercell (May 6, 2010)
  2. First sUAS sampling of supercell rear-flank downdraft (June 9, 2010)
  3. FAA coordination reducing notification time from 48 hours to 1 hour
- **Follow-on Work (AVIATE, 2013)**: Tempest equipped with Aeroprobe multi-hole probe for wind estimation validation using dual Doppler radar, balloon-borne sondes, and mobile mesonet

## Products & Capabilities Described

### SwiftCore FMS (In Use)
- **What it is**: Advanced avionics package for sUAS with emphasis on scientific field campaign performance
- **Current Use**: Multiple university research groups; NASA Phase II SBIR soil moisture mapping mission
- **Proposed Volcanic Application**: Forms the technical foundation for SuperSwift XT system

### SuperSwift XT Volcanic Profiling System (Proposed)
- **What it is**: sUAS platform purpose-designed for volcanic plume analysis
- **Capabilities**: Same SwiftCore FMS components plus specialized gas and ash sensing capabilities
- **Use Case**: In situ volcanic emissions sampling with high-precision atmospheric data collection
- **Competitive Advantage**: Enables rapid, adaptive sampling of volatile volcanic phenomena; supports multi-aircraft campaigns

### Tempest Unmanned Aircraft (Historical)
- **What it is**: First-of-its-kind sUAS specifically designed for supercell sampling
- **Performance**: Successfully collected data in extreme atmospheric conditions; validated RFD sampling concept
- **Lessons Applied**: Design informed current BST approach to extreme-environment sUAS

## Use Cases & Applications

### Volcanic Monitoring (Primary Focus)
- **Gas Species Sensing**: SO₂ (sulfur dioxide), CO₂, H₂S, CO, HCl, H₂, CH₄, HF, and trace metals
- **Scientific Objectives**:
  - Species/SO₂ ratio measurements to estimate fluxes of other volcanic gases
  - CO₂ flux measurement (uncommon previously; indicates magmatic degassing depth)
  - H₂S as plume marker in weakly degassing systems
  - CO:CO₂ ratio to determine oxidative environment and distinguish volcanic settings
  - SO₂ validation/calibration against satellite and remote sensing data
  
### Volcanic Ash Characterization
- **Background**: 2010 Eyjafjallajökull eruption impacted 100,000 flights and 8 million passengers
- **Application Need**: Validate volcanic ash transport and dispersion (VATD) models
- **Ash Safety Thresholds**: European Commission tiered system with >4000 μg m⁻³ no-fly limit, <200 μg m⁻³ unrestricted
- **Measurement Need**: Particle size distribution (<2 mm range; <4 μm respirable particles); proximal ash data for model validation

### Meteorological & Atmospheric Research
- **Prior PI Work**: Supercell thunderstorm dynamics (VORTEX2)
- **Data Needs**: Wind speed/direction, temperature, humidity within plume location for model inputs

## Key Results (From Related Research)

### Prior Research Landscape (Table 5.1 compiled research)
NASA centers (JPL, ARC, GSFC-WFF, KSC) and academic institutions (University of Costa Rica, MIT, Caltech) have pursued multi-instrument sUAS packages:
- MIT's Cooperative Autonomous Observing Systems group: plume characterization algorithms
- University of Costa Rica: vehicle-agnostic sensor development and miniaturization
- Various platforms: Global Hawk, Ikhana (HALE UAS); Dragon Eye, VANTAR, S9TWL, Swinglet CAM (micro/small UAS)

### VORTEX2 Achievements (2010)
- Demonstrated feasibility of sUAS in extreme atmospheric conditions
- Pioneered FAA coordination protocols for rapid sUAS deployment
- Proved RFD sampling capability
- Identified needs for next-generation design (improved instrumentation, endurance, multi-aircraft support)

### AVIATE Follow-on Study (2013)
- Tested Aeroprobe multi-hole probe on Tempest for improved wind estimation
- Validation via dual-Doppler radar, balloon sondes, mobile mesonet
- Identified SwiftPilot as needed solution for state estimation during maneuvering

## Notable Details

### Competitive/Unique Capabilities
1. **PI Expertise**: Recognized leader in extreme-environment sUAS design; published extensively on meteorological sUAS applications
2. **SwiftCore FMS Advantage**: Purpose-built for scientific missions (vs. commercial platforms); modular architecture enables complex sensor payloads
3. **Proven Operations**: VORTEX2 and AVIATE demonstrate ability to obtain FAA approval and operate safely in hazardous conditions

### Sensor/Chemical Focus
- Document provides detailed rationale for measuring specific gas species:
  - **SO₂**: Most widely monitored; enables flux estimates via remote sensing correlation; critical for volcanic hazard prediction
  - **CO₂**: Low magma solubility indicates deep degassing; less scrubbed in hydrothermal systems; aviation hazard in pooling areas
  - **H₂S**: Plume marker; sulfur aerosol formation relevant to ash aviation hazards
  - **Multi-species Approach**: Ratios (CO:CO₂, species:SO₂) reveal oxidative environment and magmatic characteristics

### Research Validation Strategy
- SuperSwift XT designed to calibrate/verify data from other sUAS, ground-based sensors, and satellites
- Fills gap in routine, proximal in situ characterization of volcanic emissions
- Provides direct input for volcanic ash transport and dispersion model validation

### Regulatory/Operational Heritage
- PI's FAA coordination experience (reduced notification time from 48 hrs to 1 hr) positions BST for rapid volcanic emergency response

---

**Document Quality Note**: This is a substantive, well-researched R&D section with 16 detailed references. Extensive tables of related NASA platforms and prior sUAS sensor configurations included. Demonstrates deep scientific context and positioning of BST technology within broader research ecosystem.