# Wildfire Observation & Management with UAS

## Document Metadata
- Type: White paper
- Client/Agency: Not specified (general marketing/capability document)
- Program/Solicitation: References NASA SBIR, NOAA NightFOX program
- Date: December 20, 2022 (created); April 8, 2022 (modified)
- BST Products/Systems Referenced: S2 UAS, S2-VTOL, SwiftCore, SwiftTab, SwiftPilot, SwiftStation, Multi-Hole Probe, L-band radiometer
- Key Personnel: Jack Elston (CEO), Maciej Stachura (CTO)

## Executive Summary
Black Swift Technologies proposes comprehensive UAS capabilities for wildfire observation, management, and emissions characterization. The document outlines how BST's S2-VTOL platform, integrated with specialized sensor suites and autonomous flight capabilities, can provide fire managers with real-time environmental data, air quality monitoring, and fire behavior intelligence while addressing airspace integration challenges through downwind operations and software integration with existing firefighting command systems.

## Technical Approach
BST leverages its S2-VTOL (vertical takeoff and landing fixed-wing UAS) as the core platform, equipped with modular, field-swappable sensor payloads. Key technical elements include:

**Platform Capabilities:**
- VTOL fixed-wing hybrid design enabling rapid deployment with minimal runway requirements
- Multi-hour endurance despite compact size
- Proven operation in extreme conditions (high winds, remote locations, difficult terrain)
- Full BVLOS (Beyond Visual Line of Sight) certification from FAA and NASA

**Autonomous Flight & Data Collection:**
- Sensor reactive sampling: Automated flight pattern generation based on real-time sensor measurements
- Machine vision-based terrain awareness for flight path optimization in mountainous environments
- Automated failure detection and mitigation via Electronic Centralized Aircraft Monitor System (ECAMS)
- Support for multi-aircraft coordinated operations from single operator interface

**Airspace Integration Strategy:**
- Initial focus on downwind missions to avoid interference with active firefighting operations
- Integration with existing wildfire management software (Android Team Awareness Kit/ATAK) through BST's SwiftTab interface
- Provision of airspace management data and situational awareness to incident commanders

## Products & Capabilities Described

### S2 / S2-VTOL UAS
- **What it is:** Vertical takeoff and landing fixed-wing unmanned aircraft system designed for earth observation in extreme conditions
- **Proposed use:** Primary platform for wildfire characterization, emissions monitoring, and operational surveillance
- **Specifications/Performance:**
  - Multi-hour endurance
  - Operates in very strong winds (demonstrated in Alaska volcano missions)
  - Rapid deployment capability
  - Modular payload architecture supporting sensor swapping
  - BVLOS certified by FAA, NASA; certified by NOAA and DOE

### SwiftCore Flight Management System
- **What it is:** Modular, open-interface avionics solution with custom autopilot and control algorithms
- **Proposed use:** Enables fully autonomous flight from launch to landing; supports sensor-reactive sampling and multi-aircraft coordination
- **Specifications/Performance:**
  - Designed specifically for UAS research and operations in difficult environments
  - Contains multiple safety features and custom control algorithms for strong wind operations
  - ECAMS (Electronic Centralized Aircraft Monitor System) provides Level 2 and Level 3 failure warnings with automated mitigation options
  - Supports unlimited connectivity options (UART, I2C, SPI, CAN, Ethernet, USB, GPIO)

### SwiftPilot Autopilot
- **What it is:** High-performance autopilot system for autonomous UAS flight
- **Specifications/Performance:**
  - One of the smallest and most powerful autopilots commercially available
  - Dual 168 MHz Cortex-M4 CPUs with FPU (core processors)
  - Optional 1 GHz Cortex-A8 processor for payload use
  - Modularized CAN-bus hardware architecture

### SwiftTab User Interface
- **What it is:** Android-based ground station software for flight planning, control, and multi-aircraft management
- **Proposed use:** Flight planning and modification; data display (real-time weather, wind, trace gas concentration, particle distribution); multi-aircraft status monitoring; airspace management visualization
- **Specifications/Performance:**
  - Runs on Android tablets and smartphones
  - Mid-flight flight plan modification capability
  - Gesture-based controls for minimal training requirement
  - Displays manned and unmanned traffic
  - Color-coded failure status display (Level 2 cautions in yellow, Level 3 warnings in red)
  - Designed to integrate with ATAK (Android Team Awareness Kit) with custom modules for wildfire-specific data display

### SwiftStation Ground Station
- **What it is:** Tripod-mounted portable ground station
- **Specifications/Performance:**
  - 900 MHz and GPS antennas
  - Expandable via custom modules
  - Multiple radio options available
  - Integrates with X-Plane Pro Flight Simulator

### Sensor Payloads

**Pre-Fire Characterization:**
- L-band radiometer for soil moisture mapping (NASA SBIR developed; operates under dense canopy)
- Hyperspectral and multispectral remote sensing for vegetation mapping
- High-resolution orthomosaics via aerial imagery
- Digital Elevation Models (photogrammetry and LiDAR)
- Canopy height measurements (LiDAR + high-resolution orthomosaics)

**During-Fire Monitoring:**
- Infrared (IR) and thermal imaging for fire outline, boundaries, and active fire surveillance
- Electro-optical (EO) imaging
- Multi-Hole Probe for real-time wind measurement
- Atmospheric thermodynamics sensors (temperature, humidity, pressure)
- Trace gas measurement sensors (specialized for fire emissions characterization)
- Particulate sizing and distribution sensors
- Communications relay capability

**Post-Fire Assessment:**
- Surveyor-grade orthomosaics for infrastructure and building impact assessment
- LiDAR-based canopy height and burn extent determination
- Soil moisture mapping for flash flood/landslide risk identification
- Infrared/thermal/EO imaging for search and rescue operations
- Downwind particulate and contaminant measurements for community safety assessment

### Multi-Hole Probe
- Wind velocity measurement device for real-time atmospheric wind data
- Also provides atmospheric thermodynamics (temperature, humidity, pressure)

## Use Cases & Applications

### Pre-Fire Operations
- Soil moisture mapping for areas susceptible to flash flooding and landslides post-fire
- Vegetation characterization and fuel load assessment
- Burn condition evaluation (dryness, fuel load, species composition) for controlled burn planning and pre-fire hazard assessment

### Active Fire Surveillance
- Nighttime fire observations (demonstrated through NOAA NightFOX program)
- Fire perimeter and burn boundary identification
- Fire radiative power assessment
- Combustion efficiency characterization
- Close-in, in situ fire plume emissions sampling
- Remote fire observation measurements directly over fire
- Downwind air quality monitoring without interfering with active firefighting operations
- Hazardous emissions characterization (mercury, lead, other toxins) to inform firefighter and public safety

### Post-Fire Assessment
- Fire impact surveying and damage assessment
- Burn extent determination
- Soil stability and flood risk assessment
- Search and rescue operations in burn zones

### Fire Behavior Modeling & Forecasting
- Real-time wind and thermodynamic data for improved fire weather forecasting
- Smoke and emissions characterization for air quality models
- Data refinement for fire behavior prediction models

## Key Results / Demonstrated Capabilities

**Operational Experience:**
- BVLOS flights collecting photogrammetric images and trace gas measurements over Makushin Volcano (2,036 meters) from 25 km base of operations
- Successful operations in harsh, nomadic scientific field campaign environments
- Proven partnership with NASA and NOAA for demanding atmospheric research missions

**NightFOX Program:**
- Collaborative effort with CIRES, University of Colorado Boulder, NOAA UAS Program Office
- Characterizes nighttime combustion efficiency, smoke, fire perimeter, and fire radiative power at high spatial resolution
- Specifically designed to inform and test fire weather forecasting improvements
- Demonstrates viability of UAS for wildfire missions despite airspace constraints

**Autonomous Sampling Demonstrations:**
- Machine vision-based terrain awareness in mountainous terrain (Costa Rica CO2 plume sampling missions)
- Automated flight path generation for optimal data gathering in complex topography
- Sensor-reactive sampling algorithms that automate characterization of thermodynamic properties, trace gas, and particulate content

## Notable Details

**Competitive Advantages:**
- Only manufacturer moving beyond proof-of-concept to real-world operational scenarios
- End-to-end proprietary avionics stack (SwiftCore, SwiftPilot) designed specifically for demanding UAS research
- Proven track record with NASA, NOAA, DOE, and USGS
- Modular, future-proof payload architecture enabling sensor upgrades without platform redesign
- Sensor-reactive autonomous flight reduces operator overhead and enables multi-aircraft operations

**Regulatory & Integration Strategy:**
- FAA and NASA BVLOS certification already achieved
- NOAA and DOE operational certification obtained
- Addresses airspace interference concerns by initially focusing on downwind operations
- Works with Center of Excellence for Advanced Technology Aerial Firefighting (CoFireTech)
- Integrating with existing wildfire management tools (ATAK) rather than requiring new custom systems
- Pursuing integration with commercial wildfire management software providers

**Key Personnel Expertise:**
- Jack Elston (CEO): Ph.D. from CU Boulder in complex meshed network UAS and tornadic supercell sampling; technical lead on all BST avionics and SwiftCore FMS development
- Maciej Stachura (CTO): M.S. and Ph.D. in aerospace engineering from CU Boulder; 300+ flight experiments experience; involved in VORTEX2 campaign (first-ever intercept of tornadic supercell)

**Company Background:**
- Founded 2011, Boulder, Colorado
- Recognized for delivering reliable, robust, highly accurate UAS for demanding atmospheric environments
- Global operations for specialized atmospheric research including wildfire, volcano, tornado, and hurricane missions

**Data Accessibility & Decision Support:**
- Emphasis on providing incident commanders and team members with actionable intelligence beyond standard EO/IR imagery
- Focus on metrics relevant to firefighter safety and community protection
- Real-time data dissemination to common operating picture (COP) software packages
- Automated failure mitigation prioritization when multiple system failures occur simultaneously