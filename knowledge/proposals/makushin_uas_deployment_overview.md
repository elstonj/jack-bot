# Makushin UAS Deployment Overview

## Document Metadata
- Type: Mission Planning / Operations Plan
- Client/Agency: USGS (U.S. Geological Survey), in partnership with NASA and Black Swift Technologies
- Program/Solicitation: USGS Volcano Monitoring Program
- Date: October 17, 2019
- BST Products/Systems Referenced: S2 UAS, SwiftPilot Pro autopilot, SwiftTab UI, SwiftStation GCS
- Key Personnel: Jack Elston (Pilot in Command, BST), Christoph Kern (USGS), Angie Diefenbach (USGS), Jonathan Stock (USGS), Matt Fladeland, Maciej Stachura (Observer), Andy Dietrick

## Executive Summary
This document outlines Black Swift Technologies' plan to demonstrate autonomous volcano observation capabilities using the S2 UAS at Makushin Volcano in Alaska. The mission combines real-time gas composition measurement and emission rate calculation with photogrammetry survey, showcasing how the S2 could support volcanic monitoring during future eruption events. The operation involves Beyond Visual Line of Sight (BVLOS) flight with continuous real-time data telemetry to enable adaptive mission execution based on field conditions.

## Technical Approach

### Mission Concept
- Deploy S2 UAS for ~25 km flight from takeoff site near Unalaska, AK to Makushin Volcano summit (6,000 ft altitude)
- Approach via Makushin Valley, transitioning to BVLOS as distance increases
- Conduct adaptive observation segment based on real-time meteorological and gas plume data
- Return to base following same general flight path
- Real-time video feed and gas sensor data telemetered to base station informs flight adjustments

### Flight Profile (Based on Prior Helicopter Mission Template)
1. **Approach**: Climb from sea level to ~6,000 ft over ~25 km, following Makushin Valley
2. **Gas Measurement Phase**: 
   - Multiple traverses below visible plume at ~3,000-4,000 ft
   - Circular patterns flown at plume altitude (~4,000 ft) for in-situ composition measurement
   - Measurements inform SO₂ emission rates and relative composition (CO₂, SO₂, H₂S, H₂O)
3. **Photogrammetry Phase**: Lawnmower pattern over summit at ~7,000 ft with nadir-facing camera, or flown as separate mission
4. **Return**: Climb to cruise and return to base

### Key Operational Characteristics
- **Operating Altitude**: Maximum 400 ft AGL per COA, though mission planning documents reference higher altitudes (up to 7,000 ft for photogrammetry)
- **Cruise Speed**: 37 kts nominal, 39 kts cruise, max 48 kts
- **Endurance**: 1.5 hours maximum
- **Range**: 58.5 nm maximum
- **Wind Limitation**: 20 kts maximum operational wind speed
- **Visibility Requirements**: 3 statute miles minimum, 900 ft cloud ceiling minimum

## Products & Capabilities Described

### S2 UAS (Black Swift Technologies)
**What it is:**
- Commercial off-the-shelf (COTS), fixed-wing electric UAS
- Developed under NASA SBIR program
- Fully composite airframe with electric propulsion
- Designed for rapid deployment and scientific payload integration

**Specifications:**
- **Engine**: KDE4215XF motor, max 1500 W continuous, 0-40A draw
- **Dimensions**: [measurements in table reference, specific values in original]
- **Maximum GTOW**: 18.5 lbs (including up to 5 lb payload)
- **Payload Capacity**: Up to 5 lbs with modular, swappable payload tray
- **Airspeed**: 48 kts max, 39 kts cruise, 29-48 kts operational range
- **Altitude Performance**: 950 ft/min climb rate, 810 ft/min descent rate, 15° glide slope
- **Endurance**: 1.5 hours maximum
- **Maximum Range**: 58.5 nm
- **Structural Design**: Limit loads -1.5G to +3.8G, gust loads -4.2G to +6.2G, 1.5 factor of safety applied
- **Vne**: 80 kts

**Operational History (This Specific Aircraft)**
- 40 flights completed
- 22 hours total flight time
- All repairs/modifications tracked with QC flight test using mass model

**Use in This Context:**
- Autonomous flight of 25 km distance to volcano with real-time data relay
- Carries USGS-developed custom volcanic gas sampling and photogrammetry payloads
- Demonstrates BVLOS autonomous operations capability for scientific missions
- Payload tray designed and built by BST to accommodate volcanic sampling package

### SwiftPilot Pro Autopilot
**What it is:**
- COTS autopilot system developed by Black Swift Technologies
- Proven system used across multiple FAA COAs with various airframes

**Capabilities:**
- Autonomous waypoint navigation with real-time flight plan modification
- GPS-based positioning and heading control via PID control loops
- Lost-link procedures: return to designated waypoint, then slow spiral descent after 5 minutes
- GPS outage handling: 20° bank hold with altitude hold to reacquire signal; if lost-link occurs during GPS outage, automatic aerodynamic descent
- Motor failure handling: maintains airspeed while descending, notifies operator
- Servo failure detection: relies on PIC observation of control degradation
- Pitch limits: -15° to +25°; Roll limits: ±45°; Max airspeed parameter: 48 kts
- Fully autonomous landing capability (belly landing, no landing gear)

**Communication:**
- CAN bus interface to servo control boards for control surface commands
- Separate R/C receiver backup link (2.4 GHz) for manual control override
- Receiver arbitrates between autopilot and manual control

### SwiftTab User Interface (v3.0.0)
**Platform:** Samsung Galaxy Tab Active2 Android tablet

**Capabilities:**
- Geo-referenced map display for spatial awareness
- Real-time telemetry subset display (critical flight parameters)
- Waypoint creation and assignment via touch interface
- Waypoint pattern modification via gesture commands
- Color-coded waypoint status (red for local-only modifications)
- Airspeed, altitude, tracked waypoint, and turn rate controls via popup windows
- Manual/autonomous mode indicator
- Real-time flight plan modification capability
- Warning displays: GPS loss/degradation, low battery, low signal strength, altitude/airspeed out of range, engine disabled

### SwiftStation Ground Control Station
**Components:**
- Radio relay unit (communication bridge between aircraft and tablet)
- Dual power: A/C plug + 6-hour battery backup
- Allows tablet WiFi connection to aircraft telemetry

### Ground Support Equipment
- **Launch System**: Pneumatic catapult (max 145 PSI), validated through >50 firings
- **Manual Handset**: COTS R/C transmitter (2.4 GHz), 6+ hour battery life, audible low-battery warning
- **Communication Radios**: Digi Xtend frequency-hopping spread spectrum (FHSS) in 902-928 MHz ISM band, max 1W output, 115.2 Kbps data rate, 256-bit AES encryption available, ~30 dB link margin at 5 miles

## Use Cases & Applications

### Primary Application: Volcanic Gas and Emissions Monitoring
**Specific Use Case - Makushin Volcano, Alaska:**
- **Gas Composition Measurement**: 
  - DOAS (Differential Optical Absorption Spectroscopy) spectrometer for SO₂ measurement (upward-looking during plume traverses)
  - In-situ sensors for relative composition: CO₂, SO₂, H₂S, H₂O
  - Enables SO₂ emission rate calculation (example: ~200 t/d measured on reference helicopter mission)

- **Plume Characterization**:
  - Wind speed and direction measurement via GPS tracking of neutral circles
  - Plume altitude determination
  - Plume trajectory analysis

- **Photogrammetry Survey**:
  - High-resolution nadir-facing camera for summit mapping
  - Can be integrated into gas measurement flight or flown separately

### Broader Mission Goals
- Demonstrate autonomous volcano observation capability for future eruption response
- Test complete workflow: flight planning, permissions, adaptive in-flight execution based on real-time data
- Show how autonomous UAS can support volcanic unrest monitoring

### Environmental Challenges Addressed
- **Complex Summit Topography**: Multiple degassing sources, steep terrain
- **High Wind Conditions**: 15+ knot winds common; plume follows topography down flanks; UAS must fly low to maintain measurement capability
- **Remote Location**: 25 km from base station requires BVLOS capability; telemetry relay infrastructure planned (Mount Ballyhoo repeater location identified)

## Key Results
This document is a pre-mission planning document, not a results report. However, it references:
- **Reference Helicopter Mission (20 August 2019)**: 
  - SO₂ measurement: ~200 t/d emission rate
  - Plume was blown northward; pilot was directed adaptively to follow
  - Multiple traverses flown at different altitudes to characterize plume structure
  - In-situ data collected from circles inside plume

## Notable Details

### Safety and Airspace Coordination
- **Airfield**: Dutch Harbor Airport (DUT), Unalaska, Alaska
  - Low traffic volume
  - Main operators: Grant Aviation (1-5 flights/day, King Air/Navajo), PenAir (2 flights/day, SAAB 2000), ACE Air (twice daily cargo, Beechcraft 1900)
  - Also: LifeMed medevac (KingAir), Maritime Helicopters (Long Ranger), USCG (HH-65 Dolphin, Jayhawk, C-130), NOAA marine survey, civilian Cessnas
  - CTAF: 122.6 MHz; also monitor 129.5 (Dutch Weather)
  - Common arrivals: left base runway 13, right base runway 31
  
- **Deconfliction Strategy**:
  - Proposed takeoff/landing site: northeast of DUT, just west of FAA radar domes
  - Site is within visual line of sight of volcano from base (terrain profile verified)
  - Real-time telemetry enables base-station awareness of meteorological conditions and adaptive decision-making
  - Manual pilot backup system allows immediate takeover if needed
  - No transponder or anti-collision lights on S2
  - Observer scans airspace with naked eye; notifies PIC of manned aircraft; PIC initiates immediate landing if conflict detected

### Regulatory Compliance
- **FAA Part 107 Compliance**: 
  - Aircraft <55 lbs ✓
  - Daylight operations ✓
  - Max 400 ft AGL (with BVLOS waiver for observation segment)
  - 100 mph max ground speed ✓
  - Right-of-way to manned aircraft ✓
  - 3 miles visibility / 500 ft cloud separation ✓
  - Class G airspace ✓

- **BVLOS Waiver**: Required for approach and observation segments; full permissions process outlined
- **COA (Certificate of Authorization)**: NASA Armstrong approval required

### Crew Qualifications
- **Pilot in Command**: Jack Elston (BST)
  - FAA Remote Pilot License
  - Current Class 3 Medical Certificate
  - 20+ years unmanned aircraft operations (since 2001)
  - ~1000 hours operations across 20 platforms, 5 autopilot systems
  - Experience in challenging environments: tornado chasing, arctic operations

- **Observer**: Maciej Stachura
  - FAA Private Pilot License
  - Current Class 3 Medical Certificate
  - Fully cross-trained to assume pilot role
  - Full redundancy in crew capability

### Software and Configuration Management
- **Autopilot Software**: Majority developed by BST
  - Low-level libraries from board support packages for processors
  - GCS and operator interface software: BST-developed, runs on COTS OS
  - UML design and diagramming used
  -