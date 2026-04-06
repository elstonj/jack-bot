# Uncrewed Aircraft System Data Assimilation for Improved Wildland Fire Fighting Decision Support

## Document Metadata
- Type: Project overview presentation (SBIR Phase I)
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Topic A3.02-1718
- Contract Number: 80NSSC23PB371
- Date: August 22, 2023
- BST Products/Systems Referenced: S2, S0, SwiftCore, SwiftTab, SwiftFlow 3D wind probe
- Key Personnel: Jack Elston (PI, elstonj@bst.aero), James Pinto (UCAR subcontractor, pinto@ucar.edu), Ed Kase (TABA Vendor, ed.kase@ekaseconsulting.com)

## Executive Summary
Black Swift Technologies proposes to develop and demonstrate uncrewed aircraft system (UAS) data assimilation capabilities to improve wildland firefighting decision support. The project will utilize BST's S0 weather-sensing platform to collect real-time wind and turbulence data near active wildfires, assimilate these measurements into predictive models using ensemble Kalman filter techniques, and integrate resulting forecasts into existing wildfire asset management systems.

## Technical Approach

### Data Assimilation Framework
- Ensemble Kalman Filter (EnKF) framework for assimilating UAS observations
- Ensemble sensitivity analysis to identify optimal UAS sampling locations
- Observing System Experiments (OSEs) to assess added value of UAS measurements
- High-resolution ensemble simulations of previous wildland fires (Calwood Fire, Fourmile Canyon Fire)
- Model configuration using 1 km grid spacing on inner domain with multiphysics/time-lagged ensemble approach
- Assessment of model uncertainty in RH (relative humidity) and winds

### UAS Operations
- Deployment of up to 3 S0 platforms simultaneously for weather data collection
- Autonomous mission tasking via standardized interface developed during Phase I
- Flight operations on 1-2 high-risk fire days to collect pressure, temperature, humidity, and wind measurements
- Low-level winds analysis focusing on lower atmospheric conditions
- Integration with UTM (Unmanned Aircraft Traffic Management) systems for safe operation near crewed aircraft

### System Integration
- Development of interfaces for safe UAS operation in wildfire vicinity
- Integration with existing wildfire asset management platforms (e.g., ATAK/CivTAK)
- Open interfaces and data standards compliance for scalability
- Interfaces to feed improved weather/wind forecasts to traffic management and fire weather forecasters

## Products & Capabilities Described

### S0 UAS (Small, Deployable Platform)
**What it is:** Low-cost, modular, electric fixed-wing UAS designed for atmospheric sampling and rapid deployment
- **Specifications:**
  - Max takeoff weight: 4 lbs
  - Wingspan: 54.6 inches
  - Flight ceiling: 15,000 ft
  - Max winds endured: 50 mph
  - Flight time: 90 minutes nominal
  - Cruise speed: 40 mph / Dash speed: 100 mph
  - Climb rate: 2,000 ft/min
  - Communication range: Up to 100 miles
  - Launch options: Vertical takeoff/landing or tube-launched
  - Payload capacity: 100 grams
  - Sensor options: EO/IR cameras, trace gas sampling, atmospheric profiling sensors

**Proposed use in wildfire context:** 
- Collection of real-time wind, turbulence, pressure, temperature, and humidity data in the vicinity of active wildfires
- Autonomous profiling missions to gather data at optimal locations identified through ensemble sensitivity analysis
- Multiple simultaneous operations (up to 3 platforms) for spatial coverage

**Validation record:**
- Tested against measurement towers: 12 flights at SGP (5.8 hours flight time) validated against 60m towers in up to 40 mph winds
- Air-deployed variant validated against dropsondes in hurricane sampling (comparable pressure, temperature, humidity data)
- Proven performance in extreme atmospheric conditions

### S2 UAS (Larger Platform)
**What it is:** Rugged, workhorse fixed-wing UAS for longer-duration missions
- **Specifications:**
  - Max takeoff weight: 20.5 lbs
  - Wingspan: 10 ft
  - Flight ceiling: 15,000 ft
  - Max winds: 30 mph
  - Flight time: 90 minutes with max payload
  - Range: 63 miles with max payload
  - Cruise speed: 42 mph
  - Payload capacity: 5 lbs
  - Payload nosecone: 8 in diameter x 25 in length
  - Power available: 50 W total
  - Geotagging accuracy: Typically <1m in all directions

**Referenced use:** While the wildfire project focuses on S0, the presentation notes that S2 has been utilized for fire weather prediction (swapping between gas composition and EO/IR imaging payloads) as part of previous NOAA efforts (NightFox)

### SwiftCore Flight Management System
**What it is:** End-to-end, distributed avionics system developed in-house by BST
- Key features:
  - Distributed networked architecture with redundancy
  - Proprietary hardware flight controller that outperforms open-source Ardupilot alternatives
  - Built-in fault monitoring system
  - Automated part lifetime tracking
  - Field maintenance simplicity
  - Expandability and third-party component integration
- Referenced as mature and field-proven for both S0 and S2 platforms

### SwiftTab User Interface
**What it is:** Proprietary, tablet-based GUI for mission control and monitoring
- Key features:
  - Mission-focused design reducing operator workload
  - Safety systems including centralized aircraft monitoring with fault trees
  - Stand-alone simulator with fault injection for training
  - Support for multiple error level display and handling

### SwiftFlow 3D Wind Probe
Advanced airdata sensor for accurate wind measurement in precipitation and extreme conditions

## Use Cases & Applications

### Primary Wildfire Application
**Problem addressed:** Wildland firefighting operations, especially at night, suffer from lack of situational information limited to field reports and coarse satellite overpasses. This dearth of data impacts both safety of crewed operations and accuracy of predictive models.

**Proposed solution:** Autonomous UAS deployment to gather high-resolution wind and turbulence data in the lower atmosphere near active fires, with data assimilation into predictive models and distribution to firefighting assets.

**Test cases identified:**
- Calwood Fire (Boulder County, Colorado) - expanded to 5,000 acres in 5 hours due to high winds and low relative humidity
- Fourmile Canyon Fire (previous event)
- Future flights on 1-2 high-risk fire days in Boulder County foothills

### Broader Applications
As noted in Task 5 (market exploration), the developed technologies address multiple NASA and government markets:
- NSF applications
- DOE (Department of Energy) applications
- NOAA applications
- USGS applications
- UTM system developers and commercial UAS companies
- State and local government fire management
- Supplemental weather data providers

## Key Objectives & Tasks

### Phase I Work Plan (5 Tasks)

**Task 1: UAS Sampling Strategies Development**
- Analyze two previous wildland fire events (Calwood Fire, Fourmile Canyon Fire)
- Employ ensemble sensitivity analysis to identify points of greatest uncertainty in fire predictions
- Determine optimal locations, cadence, and spacing for UAS weather measurements
- Develop standardized interface for autonomous UAS mission tasking
- Generate model configuration using 1 km grid spacing with multiphysics/time-lagged ensemble approach

**Task 2: Multi-UAS Integration into Wildfire Space**
- Research UTM-like integration methods for operating 3 S0 UAS simultaneously in wildfire operations
- Determine necessary interfaces and permissions for safe co-operation with crewed aircraft
- Explore current research and methods (e.g., NASA's STEReO project)
- Do NOT plan to fully solve UTM integration in Phase I, but explore methods and current state of research

**Task 3: Gathering and Assimilating UAS Measurements**
- Conduct 2 S0 flights on high-risk fire days to collect low-level winds analysis data
- Collect pressure, temperature, humidity, and wind measurements
- Assimilate data using Ensemble Kalman Filter framework
- Compare UAS DA (data assimilated) predictions against non-DA predictions and independent truth data (e.g., AWOS)

**Task 4: Researching UAS Integration into Wildfire Operations**
- Generate overview and assessment of current data dissemination methods in wildfire response
- Identify limitations of existing platforms (e.g., ATAK, CivTAK) regarding environmental data display
- Work with Colorado Center of Excellence to develop methods for displaying 3D winds and prediction data in asset management platforms
- Explore real or simulated wind/prediction data integration with systems like ATAK

**Task 5: Exploring Commercial Potential and Product Viability**
- Conduct market research on addressable NASA markets for wildfire-focused UAS technologies
- Identify governmental and commercial applications
- Identify potential Phase II and III funding sources
- Explore partnerships with UTM developers, commercial UAS companies, state/local governments, supplemental weather data providers

## Notable Details

### Company Background & Relevant History
Black Swift has demonstrated extensive experience operating unmanned systems in challenging conditions:
- **2012:** Pathfinding mission for USGS demonstrating BVLOS observations of Makushin volcano in harsh Aleutian Islands (>50kt winds, >1600 ft/min downdrafts, precipitation, clouds, near freezing)
- **2013:** USAF Phase I and II to develop UAS for rapid wind profiles up to 15,000 ft AGL in >40 mph winds
- **2015:** Three-month campaign in Greenland with custom payload, missions to 14,000 ft in -20°C conditions
- **2016:** Development of E2 multi-rotor UAS for infrastructure inspection
- **2017:** Initial NOAA SBIR (>$1M) to develop tube-launched, air-deployed UAS for hurricane observations
- **2018:** S2 initial sales with $1M in system/payload sales to date; machine vision safe-to-land system demonstration; pathfinding volcano observations
- **2019:** Initial NASA SBIR for soil moisture mapping (over $2M awarded); S1 photogrammetry platform
- **2020:** NASA SBIR for advanced ML techniques for UAS predictive maintenance
- **2021:** SwiftCore FMS development with modular, redundant architecture

### Competitive Advantages
- **In-house development:** BST develops own avionics, control systems, payload interfaces, aircraft designs, user interfaces, and ground stations (not reliant on Dronecode/Ardupilot clones)
- **Superior control and estimation schemes:** SwiftCore flight controller outperforms open-source alternatives in fixed-wing aircraft handling
- **Distributed avionics architecture:** Unique networked approach enabling redundancy and field maintainability
- **Extreme weather design:** Proven track record in harsh conditions (volcanic environments, arctic operations, hurricane sampling, high altitude/cold operations)
- **Modular payload system:** Field-swappable payloads without specialized tools enabling rapid mission reconfiguration
- **Machine vision and ML capabilities:** Demonstrated semantic segmentation, GPS-denied navigation, predictive maintenance systems
- **Proven BVLOS operations:** Multiple demonstrated BVLOS missions in extreme conditions

### Standardization & Interoperability
- Open command and control protocols supporting third-party integration
- Interoperable with systems like ATAK (Area Tactical Operations Center)
- Compliance with established data standards for scalability
- While proprietary systems, BST maintains open interfaces to support ecosystem integration

### Risk Mitigation & Safety Focus
- Safety-centric design philosophy built into SwiftCore with fault monitoring systems
- Redundant communication links demonstrated (Makushin volcano operations)
- Emergency automated landing capabilities (vision-based)
- Real-time internet backhaul demonstrated
- Extensive testing and validation against reference systems (towers, dropsondes, AWOS)

### Subcontractor Partnership
- UCAR (University Corporation for Atmospheric Research) partnership with James Pinto for data assimilation expertise, bringing advanced meteorological modeling capability to the project