# ERDC Multiple Uncrewed Aerial Systems Applications

## Document Metadata
- Type: Request for Information (RFI) Response
- Client/Agency: U.S. Army Engineer Research and Development Center (ERDC), Environmental Laboratory (EL)
- Program/Solicitation: ERDC Multiple Uncrewed Aerial Systems RFI
- Date: Submitted 2024 (document created 2024-07-31, modified 2024-08-05)
- BST Products/Systems Referenced: S0 (VTOL and Air-Delivered variants), S2, S3, SwiftCore FMS, Ground Control System (GCS)
- Key Personnel: Jack Elston, Ph.D. (Founder and CEO, Technical POC)

## Executive Summary
Black Swift Technologies responds to ERDC's RFI for multiple uncrewed aerial systems by offering a portfolio of specialized electric VTOL and fixed-wing UAS (S0, S2, S3 models) built on the proprietary SwiftCore Flight Management System. BST emphasizes ruggedized design for extreme environmental conditions, modular payloads, autonomous swarming capabilities, and proven federal agency adoption (NOAA, USGS, NASA, USAF, DoD).

## Technical Approach
BST's technical foundation centers on:
- **SwiftCore™ FMS**: Proprietary flight management system including autopilot, ground station, user interface, and support electronics; enables modular customization and multi-UAS/swarming control
- **Quality assurance**: NDAA and ASDA compliant; proprietary avionics (not open-source) providing guaranteed supply and robustness
- **Modular architecture**: Field-swappable payload nose cones; components replaceable/reconfigurable within 30 minutes
- **Open systems approach**: Integration of government-developed platform-agnostic collaborative plugins; third-party sensor integration capability
- **Autonomous capabilities**: Terrain-aware navigation, computer vision for ATR, GPS-denied navigation, autonomous launch/landing in mountainous terrain
- **Integration with military command systems**: Mission data transmitted to Android Team Awareness Kit (ATAK)

## Products & Capabilities Described

### S0 UAS (Two Variants)

**S0-VTOL Configuration:**
- Wing span: 62"; Length: 40"
- Empty weight: 5.2 lbs; Max gross weight: 5.7 lbs
- Payload capacity: 0.5 lbs
- Max speed: 100 kts; Cruise: 37 kts
- Max altitude: 15,000 ft
- Max range: 53 miles
- Max endurance: 75 minutes
- Rate of climb: 3,000 ft/min
- Glide ratio: 14.3:1
- Power: 1155 kV Brushless (x3); 148.0 Wh Li-Ion battery
- Designed for low-cost swarm solutions, economical construction and operation
- Approved for use by NOAA and USAF; used by multiple federal agencies

**S0-AD (Air-Delivered) Configuration:**
- Wing span: 32"; Length: 32.5"
- Empty weight: 2.50 lbs; Max gross weight: 2.75 lbs
- Payload capacity: 0.25 lbs
- Max speed: 60 kts; Cruise: 46 kts
- Max altitude: 10,000 ft
- Max range: 97 miles
- Max endurance: 110 minutes
- Rate of climb: 3,000 ft/min
- Power: 1950 kV Brushless; 106.4 Wh Li-Ion battery
- Designed for tube launch from aircraft (e.g., C-130); enables mass deployment

### S2 UAS

- Wing span: 120.6"; Length: 73.4"
- Empty weight: 13.5 lbs; Max gross weight: 18.5 lbs
- Payload capacity: 5 lbs (accommodates multiple configurable sensors)
- Max speed: 48 kts; Cruise: 37 kts
- Max altitude: 10,000 ft
- Max range: 63 miles
- Max endurance: 90 minutes (potential 3+ hours with rechargeable battery; 8+ hours with hybrid fuel-powered generator)
- Rate of climb: 950 ft/min
- Glide ratio: 14.3:1
- Power: 465 kV Brushless; 302 Wh Li-Ion battery
- Operates in headwinds >25 kts, crosswinds >5 kts, tailwinds up to 5 kts
- Flight tested in extreme temperatures (46°C/115°F); heated sensors adaptable to -51°C/-60°F
- Proven in high-altitude mountainous regions with damaging particulates
- Demonstrated 20+ nautical mile operations in 50 kt winds and icing conditions
- Specialized design for USACE and Army Combat Engineers requirements

**S2 Applicability Summary:**
- High-endurance range with 80 nautical miles operational range potential
- Multi-payload flexibility with field-swappable nose cone
- Rugged, reliable design for extreme conditions
- Autonomous launch/recovery in diverse environments (land, maritime, water recovery potential)
- Modular components replaceable within 30 minutes
- Open systems for government-developed collaborative plugins
- Supports multi-air vehicle control

### S3 VTOL UAS

- Built on proven S2 design and SwiftCore FMS
- VTOL (vertical take-off/landing) capability improving portability and operations in rugged terrain
- Modular payload system (similar to S2) for quick mission conversion
- User-friendly autonomous operation with terrain-aware navigation
- Onboard computer vision capability
- Advanced autonomous development underway including:
  - Computer vision system for automatic target recognition (ATR)
  - Real-time video/sensor analysis for threat identification (unauthorized personnel/vehicles)
  - Preventative maintenance automation
  - Automatic landing capability
  - GPS-denied navigation
- Integration with ATAK for command and control
- Reduces operator workload and programmatic risk

## Use Cases & Applications

### 1. **Extreme Environmental Monitoring / Volcano Observation**
- S2 demonstrated 20+ nautical mile operations in 50 kt winds and icing conditions observing volcanoes in Alaska with USGS
- Engineered for high-altitude flights with strong winds and damaging particulates

### 2. **Hurricane Data Collection (NOAA)**
- S0-AD air-deployed from NOAA P3 hurricane hunter
- Provides wind, pressure, temperature, and video data collection
- 20-unit delivery to NOAA for 2024 hurricane season
- Development contract for 2025 season includes multi-UAS swarming and automatic path planning in hurricanes
- Mission flown into Tropical Storm Tammy (late 2023, off Barbados coast)
- Capacity to scale to orders of 100+ units

### 3. **Multi-UAS Swarm Operations for Wildfire Wind Monitoring (NASA SBIR)**
- Coordinated team of S0 UAS for atmospheric forecasting around wildfires
- Two UAS demonstrated in 2023; planned expansion to 6-UAS team
- Autonomous guidance to highest-uncertainty sampling locations
- Data used by National Center for Atmospheric Research (NCAR) for 12-hour weather forecasting
- Data shared via ATAK to firefighting teams and command centers
- Supports safety for both manned aviation and ground-based firefighting

### 4. **RF Emitter Localization and Tracking (NSF/Air Force)**
- Mesh-networked S0 UAS team for autonomous RF source detection
- Autonomous path planning optimizing localization while maintaining mesh communications
- Tested with WiFi (2.4GHz) and 433MHz emitters
- Field experiments achieved ~20m localization accuracy
- UAS automatically reconfigured as relay when emitter outside primary comm range
- Demonstrated system portability across different small fixed-wing UAS types

### 5. **Soil Integrity/Runway Assessment (AFWERX SBIR Phase II with AFRL)**
- S2 equipped with commercial soil moisture sensor for runway integrity assessment
- Supports C-130 aircraft operations on unimproved/dirt runways
- Multi-UAS swarm extension (coordination with NASA) for vastly increased coverage and reduced collection times
- TRL 9 maturity (operational experience with USGS, NOAA, NASA)
- Wildfire application focus; potential Army Corps of Engineers extension for trafficability assessment in remote/disadvantaged locations

### 6. **Advanced Cooperative Control / Swarming (AFWERX/AFRL)**
- S0 UAS intended as low-cost platform enabling hierarchical control and advanced cooperative autonomy
- Supports multi-domain command and control for battlespace operations
- Air-deployable from C-130 or ground-launched
- Enables "unpredictability and mass" through large numbers of inexpensive systems
- Reduced operator overhead through advanced autonomy for complex multi-UAS tasks

### 7. **Perimeter Security and Surveillance (S3 Application)**
- Computer vision-based automatic target recognition
- Real-time threat detection (unauthorized personnel/vehicles)
- Integrated with ATAK for tactical information sharing

## Key Results & Demonstrated Capabilities

- **Proven federal adoption**: Contracts with NASA, DoD, NOAA, USGS, USAF
- **Extreme condition performance**: Flight-tested in 50 kt winds, icing conditions, extreme temperatures (-60°F to 115°F)
- **Swarming maturity**: Multiple successful coordinated multi-UAS deployments
- **Rapid scaling**: Delivered 20 S0-AD units to NOAA in 2024; capacity for 100+ unit orders
- **Data integration**: Mission data transmission and integration with ATAK demonstrated
- **Research partnerships**: Collaboration with Creare LLC, Orbital Micro Systems, Anduril Industries, NCAR

### Publications from RF Localization Work:
- https://onlinelibrary.wiley.com/doi/abs/10.1002/rob.21666
- https://arc.aiaa.org/doi/epdf/10.2514/1.51591

## Notable Details

- **Founded**: 2011 in Boulder, CO
- **CAGE Code**: 6PGF9; **UEI**: C2J3K9NRE3L3
- **Company structure**: Small business specializing in next-generation small UAS platforms
- **Proprietary advantage**: Owns and controls SwiftCore FMS and avionics (not reliant on open-source)
- **Supply chain**: Guarantees quality, robustness, and supply of critical components; NDAA/ASDA compliant
- **2025 Program**: NOAA contract for multi-UAS hurricane operations with automatic path planning (significant expansion from 2023-2024 single-aircraft operations)
- **Modular design philosophy**: 30-minute field reconfiguration of components
- **Open architecture**: Supports government-developed collaborative plugins and third-party sensor integration
- **Upcoming engagement**: Virtual Technology Review with ERDC scheduled for 12 August 2024

**Document quality note**: This is a substantive RFI response with detailed technical specifications, proven operational history, and clear articulation of BST's competitive advantages (proprietary avionics, swarming expertise, extreme-condition performance, federal agency relationships).