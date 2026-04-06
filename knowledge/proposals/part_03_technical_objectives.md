# NASA SBIR Phase II Proposal: SuperSwift XT Volcanic Profiling System

## Document Metadata
- Type: SBIR Phase II Proposal (Technical Objectives section)
- Client/Agency: NASA
- Program/Solicitation: NASA 2016 SBIR
- Date: 2016-12-02 to 2016-12-09 (created/modified)
- BST Products/Systems Referenced: SuperSwift XT, SwiftCore Flight Management System, SwiftPilot, SwiftTab ground control station
- Key Personnel: David Pieri (referenced for mass spectrometer development)

## Executive Summary
Black Swift Technologies proposes to develop the SuperSwift XT, a commercially viable turn-key small UAS system capable of routine autonomous flights into harsh volcanic environments to measure trace gases, particulate sizing and density, pressure, temperature, humidity, 3D wind, and collect EO/thermal imagery. Phase II will build on Phase I design work by integrating sensors, enhancing the airframe for high-altitude and turbulent conditions, developing mission-specific flight planning software, and validating the system through three-stage flight testing culminating in volcanic deployment.

## Technical Approach

### Four Primary Phase II Objectives:

1. **Volcanic Profiling Payload** - Mechanical, electrical, and data integration of multi-sensor package using SwiftPilot modular payload bus with on-board Linux computer (SwiftCore FMS) for data logging, timing, and telemetry. Modular design allows field payload swaps. Includes provision for future mass spectrometer integration (candidate sensors under development).

2. **SuperSwift XT Airframe Development** - Finalize and validate Phase I design improvements to enable:
   - Motor protection from particulates with adequate thermal cooling
   - Redundant airspeed measurement (payload as backup if primary pilot clogs)
   - High-altitude endurance (power system and battery validation)
   - Required climb performance for terrain-following flight
   - Enhanced controllability in strong turbulence
   - Launch/landing capability in mountainous, unimproved terrain

3. **Flight Planning Software** - Add volcanic profiling mission profiles to SwiftTab (Android tablet-based ground control station). Automatic flight plan generation for five mission types identified in Phase I. Similar to existing terrain-mapping auto-planning feature. Modular architecture allows future mission profile expansion.

4. **Flight Testing & Validation** - Three-stage testing program:
   - **Pawnee National Grasslands** (local): Airframe design validation, payload calibration, rapid iteration
   - **San Luis Valley** (high altitude/mountainous): High-altitude operations (up to 14 kft), turbulence handling, difficult terrain launch/landing
   - **Turrialba, Costa Rica** (volcanic deployment): System validation in actual volcanic plume environment

## Products & Capabilities Described

### SuperSwift XT
- Small fixed-wing UAS with hand-launch capability
- Equipped with laser altimeter for terrain-relative altitude control (±15m AGL)
- Autonomous flight control with terrain-following capability
- Designed for deployment from mountainous, unimproved terrain
- High-altitude operation to 14,000 feet
- Turbulence-resistant design

### SwiftCore Flight Management System
- On-board Linux computer for data gathering and logging
- Integrated timing and telemetry tagging
- Extensible architecture for sensor integration

### SwiftPilot
- Modular payload bus for sensor control and data acquisition
- Power and data interfaces for multiple sensors

### SwiftTab Ground Control Station
- Android tablet-based interface with gesture recognition
- Automatic flight plan generation for terrain mapping and profiling missions
- Mission parameter setting for volcanic operations

### Volcanic Profiling Payload Package
Integrates:
- Trace gas measurement sensors
- Particulate sizing and density instruments
- Pressure, temperature, humidity sensors
- 3D wind measurement capability
- Electro-optical (EO) camera
- Thermal imaging camera
- Forward video

## Use Cases & Applications

### Primary Use Case: Volcanic Plume Profiling
- Autonomous in-situ data collection from volcanic plumes
- Five distinct profiling mission types (specific types not detailed in this section)
- High-altitude mountainous deployment
- Corrosive particle environment (volcanic ash)
- Scientific campaign support for NASA Airborne Sciences

### Secondary/Future Applications
- Wildfire environment monitoring (explicitly noted as natural next step)
- Other harsh environment missions requiring ruggedized fixed-wing platforms
- Terrain mapping (existing capability)

## Notable Details

### BST Expertise Referenced
- Prior NASA SBIR work: Soil moisture mapping radiometer integration
- NOAA atmospheric sampling missions
- Multiangular visible/infrared remote sensing projects
- On-board data logging heritage: Developed system storing L-band radiometric data at 240MB/s with lightweight, reliable design
- Existing SwiftCore product for commercial terrain mapping surveys

### Key Technical Challenges Addressed
- Ash/particulate protection of motor and sensors
- Airspeed measurement redundancy in ash-laden environment
- Endurance at altitude with weight constraints
- Control authority in turbulence
- High-altitude terrain-following flight planning
- Rapid deployment capability for scientists/operators

### Distinguishing Features
- Modular payload architecture for rapid sensor integration and field swaps
- Automatic mission planning reduces setup time
- Hand-launch capability for remote deployment
- Simple, intuitive user interface for non-specialist operators
- Significantly lower cost than larger UAS or manned aircraft
- Integrated laser altimeter with low-altitude hold control (±15 m)

### Testing Philosophy
- Incremental validation at each stage
- Design improvements validated through flight testing before deployment
- Pawnee site enables rapid iteration and high-cadence testing
- San Luis Valley provides realistic environment before volcanic deployment