# A High Resolution Soil Moisture Mapping Unmanned Aircraft System

## Document Metadata
- Type: USDA SBIR Proposal - Equipment Documentation (Field 11)
- Client/Agency: USDA
- Program/Solicitation: USDA SBIR (topic not specified)
- Date: 2018-09-25 to 2018-10-25
- BST Products/Systems Referenced: S2, SwiftCore™, SwiftPilot™, SwiftStation™, SwiftTab™
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This document describes Black Swift Technologies' S2 unmanned aircraft system customized for high-resolution soil moisture mapping using an L-band radiometer payload. The S2 has been specially designed with electromagnetic interference mitigation and optimized payload integration to enable soil moisture measurements at higher spatial and temporal resolution than satellite-based remote sensing, providing agricultural and hydrological insights at root-depth scale.

## Technical Approach
**System Architecture:**
- S2 airframe extensively modified to house L-band antenna and radiometer payload with exact volume matching
- Critical design changes implemented to mitigate electromagnetic interference (essential for measurement accuracy and repeatability)
- Integration of SwiftCore™ flight management system for autonomous and remote operations
- Payload power budget: 50W available, 1.3W used by soil moisture payload

**Flight Management System (SwiftCore™):**
- Comprises SwiftPilot™ (autopilot), SwiftStation™ (ground station), and SwiftTab™ (mobile UI)
- SwiftPilot™: dual 168 MHz Cortex-M4 processors with FPU for autonomous operation; optional 1 GHz Cortex-A8 payload processor
- Modular CAN-bus architecture for flexible payload integration
- SwiftStation™: portable tripod-mounted ground station (<1.5 kg), standard 3dBi 900 MHz dipole and GPS antenna
- SwiftTab™: Android-based interface with gesture controls for field operations
- 10 Hz telemetry update rate via 900 MHz real-time radio link
- Capabilities: autonomous flight planning, pre-defined banking/spirals, real-time data analysis, intervention capability

## Products & Capabilities Described

**S2 UAS (Soil Moisture Mapping Configuration)**
- **Design Purpose:** Customized to house L-band radiometer payload with optimized volume matching
- **Specifications:**
  - MTOW: 7.3 kg / MGTOW: 9.0 kg
  - Wingspan: 3.0 m
  - Fuselage length: 187 cm (excluding air intake nozzle)
  - Propulsion: Electric, propeller-driven
  - IP42 ingress protection rating
  - Launch: Pneumatic or car launch
  
- **Performance:**
  - Flight ceiling: 6,000 m AMSL
  - Cruise speed: 19.0 m/s
  - Stall speed: 12.0 m/s
  - Max stable wind: 15 m/s
  - Endurance: 120 min max / 90 min nominal
  - Max range: 110 km (60 nm) max / 92 km (50 nm) nominal
  - Area coverage: <1,100 acres per mission
  - Take-off/landing corridor: 200 m × 15 m
  - Attitude capability: ±45° roll, ±20° pitch

- **Payload Capacity:**
  - Nominal payload mass: 5.0 kg
  - Available payload power: 50 W
  - Payload mass capacity: 3.5 kg
  - Nose cone: 20.3 cm diameter, 63.2 cm length
  - Geotagging accuracy: <4 m (all directions)
  - Downlink data rate: 9,600 bps (serial)
  - Data storage: SD card

**SwiftCore™ Flight Management System**
- NASA-approved system used on major scientific missions
- NOAA deployments documented
- Designed for complex aerial network operations
- Features real-time telemetry, autonomous-to-landing capability, and field-based decision support

**L-band Radiometer Payload**
- Revision 2 build mentioned with flight testing
- Designed specifically for soil moisture measurement
- Payload power consumption: 1.3 W (well within 50 W budget)
- L-band antenna sized to match S2 payload volume

## Use Cases & Applications
- **Agricultural Soil Monitoring:** Root-depth soil drainage and moisture retention diagnostics
- **End Users:** Government agencies, agronomists, crop consultants, farmers
- **Capability Advantage:** Provides spatial and temporal resolution previously unobtainable through satellite-based remote sensing

## Key Technical Achievements
- Electromagnetic interference mitigation design validated through flight testing with new launcher
- Successful integration of L-band radiometer into S2 platform
- 3D CAD models and Revision 2 prototype documented with flight test data

## Notable Details
- Document explicitly answers equipment justification questions: only the 2 aircraft systems listed in budget; no additional equipment required
- Emphasis on American-made equipment compliance for SBIR funding
- SwiftCore™ founding team has significant experience with complex aerial network design
- System enables both autonomous and human-in-the-loop operations with gesture-based controls for harsh field conditions
- Real-time telemetry at 10 Hz enables immediate preliminary analysis and mission decision-making