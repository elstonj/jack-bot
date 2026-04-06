# S3.04-8077 Phase I Proposal: A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** 2016 NASA SBIR (Volcano topic)
- **Date:** Submitted January 14, 2016
- **BST Products/Systems Referenced:** SuperSwift XT (proposed), SuperSwift (base airframe), SwiftCore FMS (SwiftPilot autopilot, SwiftStation ground station, SwiftTab UI), Multi-hole probe (PTH/wind measurement)
- **Key Personnel:** Dr. Jack S. Elston (PI, CEO/President), Dr. Cory Dixon (Director of Engineering), Dr. Maciej Stachura (CTO), Prof. Brian Argrow (CU Boulder, Senior Personnel), Dr. Lois J. Wardell (Arapahoe SciTech, Senior Personnel)

## Executive Summary
Black Swift Technologies proposes development of the SuperSwift XT, a ruggedized small unmanned aircraft system (sUAS) purpose-built for sampling volcanic ash clouds and other harsh atmospheric environments. The system integrates the proven SuperSwift airframe and SwiftCore Flight Management System with a field-swappable sensor suite for measuring trace gases (SO₂, CO₂, H₂S, CH₄), particulates (particle size distribution), and atmospheric parameters (temperature, pressure, humidity, 3D winds). Phase I will design and specify the platform; Phase II will build and flight-test the prototype.

## Technical Approach

**Core Platform:**
- Based on commercially available SuperSwift fixed-wing airframe and SwiftCore FMS (proven in field operations)
- Hand-launchable sUAS with modular payload architecture
- Modular nose cone design with standardized power/data/mechanical interfaces for rapid field payload swaps

**Key Modifications for Harsh Environment Operation:**
1. **Propulsion System:** Improvements to battery, motor, and propeller to sustain flight at 20,000 ft MSL
2. **Airframe Modifications:**
   - Aerodynamic redesign for efficient flight at high altitude and in strong turbulence
   - Custom motor cowling and seals to protect against ash and particulate contamination
   - Improved nose cone seals at all interface points
3. **Sensor Suite Integration:**
   - Trace gas measurement: MiniGAS multi-sensor and Transpector XPR3 mass spectrometer with vacuum pump
   - Particulate measurement: Dragon-miniGAS baseline (expandable to other sensors)
   - Atmospheric measurement: Multi-hole pressure probe (PTH + 3D wind from dynamic pressure sensors) + iMet-1 radiosonde integration
   - External scoop modification to nose cone for proper sensor airflow (validated via CFD)
   - Internal custom scaffold for mounting sensors and supporting electronics

**Validation Methods:**
- CFD analysis of airframe and scoop designs
- Wind tunnel testing of 3D-printed scaled models at University of Colorado's RECUV facility
- Thrust performance and propeller characterization throughout flight envelope
- Design leverages BST's existing analysis software developed under prior Phase II SBIR (soil moisture radiometer)

## Products & Capabilities Described

### SuperSwift XT (Proposed)
**What it is:** A ruggedized sUAS variant of the commercial SuperSwift airframe, modified specifically for harsh environment scientific sampling.

**Specifications/Performance Claims:**
- Ceiling: Up to 20,000 ft MSL (enhanced from base SuperSwift)
- Endurance: Not explicitly stated, but larger payload capacity than Dragon Eye with longer endurance/higher ceiling/longer range than Vector Wing
- Hand-launchable
- Field-swappable payload system (key feature: clean enclosure, rapid deployment without specialized tools)
- Capable of sustained flight through high-altitude winds, turbulence, and damaging particulates

**Use in This Context:**
Primary platform for in situ volcanic plume sampling; secondary applications to wildfire smoke, smog, gas clouds.

### SuperSwift (Base Airframe)
Already proven in field; originally designed to carry NASA soil moisture mapping radiometer; subsequently expanded to hyperspectral/visual cameras, infrared sensors, scanning lidar.

### SwiftCore Flight Management System
**Components:**
- SwiftPilot autopilot (high accuracy GPS, advanced mission planning, modular sensor payload architecture, Linux single-board computer for sensor data processing and custom algorithms)
- SwiftStation ground station
- SwiftTab tablet user interface

**Capabilities:**
- Near real-time data telemetry to ground station
- Sensor control during operations
- Expandable sensor interface architecture

**Prior Use:** Currently used in BST's NASA Phase II SBIR for soil moisture mapping; proven reliability and power/data modularity.

### Multi-Hole Probe / Atmospheric Sensor Suite
**Components:**
- Multi-hole probe with 5 dynamic pressure sensors (for 3D wind measurement)
- iMet-1 radiosonde core (temperature, pressure, humidity)
- Nose cone-mounted scoop for proper airflow
- All integrated into field-swappable nose cone

**Performance:** Provides PTH and 3D wind measurements; airflow validated through CFD and wind tunnel testing.

## Use Cases & Applications

### Primary Use Case
**Volcanic Ash Plume Sampling:**
- Measure particle size distribution, ash cloud height/thickness, spatial (horizontal/vertical) and temporal variability of ash concentration
- Measure SO₂ flux and trace gas composition
- Support Volcanic Ash Transport and Dispersion (VATD) model calibration and validation
- Improve predictive modeling for aviation safety (volcanic ash hazards to aircraft)
- Enable rapid post-eruption response (deploy within minutes, transmit reliable data)
- Safer than manned aircraft or ground-based measurement; reduces researcher exposure to dangerous phenomena

### Secondary Applications
- Wildfire smoke characterization
- Smog/air quality monitoring
- Gas cloud sampling
- Multi-aircraft coordinated operations for spatial/temporal coverage

### Test Site (Phase II)
San Luis Valley, Alamosa County, Colorado: 
- Elevation range 7,500–14,000+ ft (testing high-altitude capability)
- Mountainous terrain for altitude/airflow testing
- FAA CoA already obtained by BST (reduces approval delays)

## Key Results
**Phase I Deliverables (Design/Specification Phase):**
1. Requirements document for system design
2. Design report detailing SuperSwift XT airframe modifications
3. Sensor analysis, selection, and integration specification
4. 3D CAD design of modified nose cone (with CFD validation)
5. NASA Flight Safety Review Board (AFSRB) and Flight Readiness Review Board (FRRB) supporting materials + FAA approval documentation outline
6. System specification document detailing CONOPS, ruggedization modifications, and sensor integration
7. Risk management and Phase II implementation plan
8. Final Phase I report

**Phase II Objectives (to be executed if funded):**
- Manufacture, assemble, and integrate complete prototype SuperSwift XT
- Flight test in hazardous conditions (high altitude, strong winds, ash)
- Collect and validate PTH, wind, particulate, and trace gas data
- Demonstrate VATD model calibration capability
- Support multi-UAS coordinated operations

## Notable Details

### Competitive Advantages Over Existing Platforms
- **vs. Multi-rotor sUAS:** Superior endurance and operational range; can characterize large-scale atmospheric structures
- **vs. Existing fixed-wing sUAS (Dragon Eye, Vector Wing):** Larger payload capacity (than Dragon Eye); longer endurance, higher ceiling, longer range (than Vector Wing); purpose-built for harsh environments (vs. general-purpose airframes)
- **vs. HALE/Medium-sized UAS:** Lower cost, faster deployment, attrition-acceptable for high-risk missions

### Key Competitive Capability: Field-Swappable Payload System
- Modular nose cone design with standardized power/data/mechanical interfaces
- Clean sensor enclosure eliminates contamination
- Enables rapid payload swap in field without specialized tools
- Extends utility beyond volcano monitoring to multiple atmospheric science missions
- Leverages proven design from original (NASA-funded) SuperSwift airframe

### Team Expertise
- **Dr. Jack Elston:** CEO/PI; Ph.D. work on tornado-sampling sUAS (VORTEX2); first sUAS intercept of supercell thunderstorm; 300+ flight experiments; 100+ FAA CoA applications
- **Prof. Brian Argrow (CU Boulder):** Aerospace engineering; sUAS design expert; RECUV co-founder; experience with severe storm sampling (supercells, gust fronts); wind tunnel/CFD facilities
- **Dr. Lois Wardell (Arapahoe SciTech):** Geochemistry/volcanology background; 15+ years scientific research; experience with UAS sensor integration and remote field operations; prior NASA SBIR (guided dropsonde for volcanic ash)
- **Dr. Cory Dixon:** Director of Engineering, BST; Ph.D. aerospace engineering; 11+ UAS systems; 4 years DoD contractor experience with SBIR management
- **Dr. Maciej Stachura:** CTO, BST; 300+ flight experiments; 150+ FAA CoAs; NASA AFSRB/FRRB lead; VORTEX2 participant

### Prior Related Work (BST/Team)
- **VORTEX2 (2010):** Developed Tempest sUAS for supercell sampling; first sUAS supercell intercept and rear-flank downdraft sampling; collaborated with FAA to reduce notification time from 48 hours to 1 hour
- **AVIATE (2013):** Aeroprobe multi-hole probe integration for improved wind estimation; dual Doppler radar validation
- **SwiftCore FMS Development:** Advanced autopilot system overcoming Piccolo limitations for maneuvering wind measurement
- **Soil Moisture Phase II SBIR (ongoing):** SuperSwift airframe and SwiftCore FMS validation in field science campaigns

### Project Structure & Partnerships
- **Prime Contractor:** Black Swift Technologies LLC (Boulder, CO)
- **Subcontractors:**
  - University of Colorado Boulder / RECUV (Prof. Brian Argrow): Sensor evaluation, airframe design validation, wind tunnel/CFD testing
  - Arapahoe SciTech LLC (Dr. Lois Wardell): Volcanic plume sensor expertise, field operations guidance
- **Facilities:** BST 6,700 sq. ft. facility (prototyping, simulation, avionics testing); outsourced composite manufacturing to Ability Composites and Northwind Composites
- **External Resources:** CU RECUV wind tunnel facility for scaled-model testing

### Commercialization Plan (Mentioned)
- Post-Phase II: Transition to commercial product for both government and commercial entities
- Offer SuperSwift XT platform + field-swappable payload options
- Phase II testing results will inform operator training and safety documentation
- Emphasis on manufacturability during Phase I design to enable Phase III scaling and competitive pricing

### Budget & Timeline
- **Phase I Duration:** 6 months
- **Subcontract to CU:** $84,150 (amount noted for Arapahoe SciTech not explicitly stated in this excerpt)

---

**Document Quality Note:** This is a comprehensive, well-structured Phase I proposal with clear technical objectives, detailed work plan (section 4.0), relevant prior work citations, and qualified personnel. The proposal demonstrates strong continuity between BST's prior sUAS work (VORTEX2, AVIATE) and this new volcanic sampling application, leveraging existing platforms (SuperSwift, SwiftCore) to reduce development risk.