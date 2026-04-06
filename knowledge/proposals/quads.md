# SMM UAS (Soil Moisture Mapping Unmanned Aerial System)

## Document Metadata
- Type: Capability briefing / project progress presentation
- Client/Agency: NASA
- Program/Solicitation: 2012 NASA SBIR, Soil Moisture topic (Phase I)
- Date: Created 2013-09-02; Modified 2015-05-26
- BST Products/Systems Referenced: Tempest airframe, SwiftPilot Pro, SuperSwift, LDCR (Low-cost Data acquisition unit for radiometer), S-series platforms
- Key Personnel: Maciej Stachura (PI, BST), Prof. Al Gasiewski (Scientific Payload Lead, CET)

## Executive Summary
BST proposed developing a low-cost, science-grade unmanned aerial system (UAS) for soil moisture and ocean salinity mapping using passive microwave radiometry. The system integrates a Tempest airframe with the SwiftPilot Pro autopilot to enable terrain-following flight at 15-30m AGL with an L-band radiometer, targeting deployment as a calibration/validation platform for NASA's SMAP satellite mission and other Earth science applications.

## Technical Approach

**Core Integration Strategy:**
- Integration of existing airframe (Tempest), autopilot (SwiftPilot Pro), and sensor technologies into a cohesive soil moisture mapping platform
- Passive microwave radiometer in L-band frequency to map volumetric soil moisture content
- Terrain-following low-altitude flight capability (~15m AGL) using laser altimeter
- Data logging at 2M samples/sec supporting high-speed sensor data rates

**Key Technical Developments (Phase I):**
1. **SwiftPilot Pro Autopilot:** Science-grade autopilot system with:
   - GPS RTK (Real-Time Kinematic positioning)
   - Integrated payload computer
   - Modular payload bus for rapid multi-sensor integration
   - On-board SDK for advanced flight planning algorithms
   - Derived from original SwiftPilot, but expanded for broader science applications

2. **High Speed Data Acquisition Unit (LDCR):** 
   - Custom-built to handle LDCR sensor data rate requirements (810 MB/s)
   - No existing commercial solutions available for small UAS
   - Designed to fit size, weight, power (SWaP) constraints of small UAS
   - MicroSD card array for low-cost storage
   - Design completed in Phase I; debugging/testing to follow

3. **Flight Path Planning Algorithm:** Developed for autonomous mission execution

4. **Auxiliary Sensors:** Laser altimeter, thermal, red, and NIR sensors specified and procured

5. **Avionics Integration:** All interfaces between autopilot, sensors, and LDCR designed; 3D CAD modeling of all components completed

## Products & Capabilities Described

### SwiftPilot Pro
- **What it is:** Science-grade autopilot system for small UAS at consumer price point
- **Key features:** GPS RTK, integrated payload computer, modular payload bus, on-board SDK
- **Phase I status:** Prototype designed, built, undergoing testing
- **Applications:** Soil moisture mapping, ocean salinity mapping, general science missions

### Tempest Airframe
- **What it is:** Small UAS airframe platform
- **Phase I status:** Purchased and modeled in 3D CAD
- **Configuration:** Can be paired with SwiftPilot Pro and L-band radiometer payload
- **Capabilities:** Hand-launch, land on unimproved surfaces

### SuperSwift
- **What it is:** Commercial evolution/modified configuration of Tempest platform
- **Design features:** Pusher configuration with removable nose cone payload bay
- **Applications:** Ocean salinity mapping, larger antenna accommodation
- **Phase II goal:** Production-ready commercial system

### Tempest 2X
- **What it is:** Larger variant of Tempest airframe
- **Purpose:** Accommodate larger P-band antenna for extended frequency capabilities

### LDCR (High Speed Data Acquisition Unit)
- **Data rate handling:** 810 MB/s sensor data
- **Storage:** MicroSD card array (low-cost approach)
- **SWaP optimization:** Designed for small UAS constraints
- **Phase I status:** Design complete; board assembly/testing underway

### L-Band Radiometer
- **Specifications:** 15m sensor footprint
- **Measurement capability:** Volumetric soil moisture content to 5-20cm depth at ~15m resolution
- **Data logging:** 2M samples/sec
- **Surface measurement:** Temperature to ±0.1°C accuracy, elevation to 1cm accuracy
- **Passive microwave approach:** No active illumination, energy-efficient

## Use Cases & Applications

### Primary Mission: Soil Moisture Mapping
- **Target application:** Calibration/validation platform for NASA SMAP (Soil Moisture Active Passive) satellite
- **Agricultural use:** Extension service deployment for crop productivity optimization
- **Test sites identified:**
  - University of Nebraska-Lincoln (UNL) - in situ soil moisture probes for validation
  - Canton, Oklahoma - in situ soil moisture probes
  - Pawnee National Grasslands, CO - FAA COA in place for early verification
- **Flight envelope:** 15-30m AGL, terrain-following capability

### Secondary Mission: Ocean Salinity Mapping
- **Sensor:** L-band radiometer (same as soil moisture mission)
- **Platform:** SuperSwift airframe
- **Application:** Measure ocean surface salinity near coastal features
- **Deployment:** Greenland field campaign (summer 2016 targeted) to measure salinity near glaciers
- **Scientific value:** Understand freshwater input from glacial melt affecting ocean circulation

### NASA Mission Support
- Provide localized, high-resolution data for comparison with SMAP and Aquarius satellites
- Small-scale validation of satellite-derived soil moisture products

## Project Goals & Phase II Development Plan

**Phase I Deliverables/Status:**
- SwiftPilot Pro prototype designed, built, testing underway
- LDCR data acquisition board design complete; debugging/testing to follow
- 3D CAD integration of all components complete
- Auxiliary sensors specified and purchased
- Flight path planning algorithm developed
- Tempest airframe purchased and modeled

**Phase II Objectives (Three Field Campaigns):**

1. **Campaign 1 (Late Summer 2014):** 
   - Preliminary soil moisture mission using Phase I prototype
   - Flight testing in Canton, Oklahoma

2. **Campaign 2 (May 2015):**
   - Full SMM campaign with improvements and modified aircraft
   - Flight test SuperSwift commercial design at SMAP calibration site in California
   - Incorporate P-band antenna

3. **Campaign 3 (Summer 2016):**
   - Ocean salinity mapping mission
   - Greenland deployment for Arctic Ocean surface salinity measurement near coastal glaciers

**End Goal:** Tested systems ready for commercial sales and NASA science missions

## Notable Details

### Competitive Advantages
- **Novel integration:** Tight integration of passive microwave radiometer with small UAS avionics and airframe for low-altitude precision mapping
- **Cost reduction:** Science-grade autopilot at consumer prices; low-cost data acquisition via microSD arrays
- **Autonomous capability:** Terrain-following flight and modular payload bus enable broad applicability
- **No existing solutions:** High-speed data acquisition for small UAS was unprecedented; BST built custom solution

### Institutional Partnerships
- Prof. Al Gasiewski (CET - likely Center for Environmental Technology or similar) as Scientific Payload Lead
- University of Nebraska-Lincoln test site collaboration
- University of Oklahoma early discussions for validation

### Regulatory Progress
- FAA Certificates of Authorization (COA) obtained for Pawnee National Grasslands, CO test area
- COA submitted for UNL test site
- COA accepted for Canton, Oklahoma test site

### Technical Distinctions
- Hand-launch and unimproved surface landing capability enables remote deployment
- Passive microwave (no active transmission) approach suitable for science applications
- High-precision positioning (RTK-GPS) and surface elevation measurement (1cm accuracy) integrated into system

### Science Applications Beyond NASA
- Agricultural extension services for crop management optimization
- Federal agency deployment for environmental monitoring
- Potential broader Earth science platform due to modular payload architecture

---

**Note:** This presentation spans 2013-2015, showing progression from Phase I concept through Phase II planning. The document demonstrates iterative development with multiple test site collaborations and evolving system configurations (Tempest → SuperSwift → Tempest 2X).