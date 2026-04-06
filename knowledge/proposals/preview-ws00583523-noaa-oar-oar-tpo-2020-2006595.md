# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: NOAA SBIR Phase II Proposal
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA), Office of Oceanic and Atmospheric Research (OAR)
- Program/Solicitation: NOAA-OAR-OAR-TPO-2020-2006595; FY 2020 Small Business Innovation Research Phase II
- Date: October 14, 2020 (submission); Period of Performance: April 1, 2021 – March 31, 2023
- BST Products/Systems Referenced: S1, S2, E2, SwiftCore FMS, Multi-Hole Probe (MHP), Diverse-Source Global Positioning System (DS-GPS)
- Key Personnel: Dr. Jack S. Elston (CEO & Principal Investigator), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposes to develop a Diverse-Source Global Positioning System (DS-GPS) that enables Beyond-Visual-Line-of-Sight (BVLOS) UAS operations by providing accurate position information in GPS-denied areas. The system combines camera-based visual odometry, inertial measurement, air-data sensors, and signals of opportunity with machine learning to replace GPS as the primary navigation source, critical for safe UAS operations under the emerging UAS Traffic Management (UTM) system. Phase II seeks $395,730.81 over 24 months to advance the prototype (demonstrated in Phase I) to a flight-proven commercial system.

## Technical Approach

### Core Technology
The DS-GPS augments standard GPS with an integrated sensor suite:
- **Computer vision system** using optical flow algorithms to estimate inertial velocity and absolute position from onboard camera imagery
- **Inertial Measurement Unit (IMU)** with pressure sensors for dead-reckoning and sensor fusion
- **Machine vision algorithms** to detect GPS degradation (jamming, spoofing, hardware failure) and seamlessly transition to vision-based navigation
- **Signals of opportunity** (e.g., software-defined radio) as tertiary position sources
- **Sensor fusion** framework to combine all sources into unified navigation solution

### Phase I Accomplishments
- Assembled prototype hardware: IMU board, Jetson TX2 embedded processor, machine vision camera
- Implemented and flight-tested inertial navigation with optical flow algorithms
- Demonstrated absolute position estimation using geotagged aerial imagery
- Evaluated GPS spoofing detection capabilities
- Generated trajectory estimates compared against GPS ground truth

### Phase II Objectives
1. **GPS Monitoring**: Develop robust GPS integrity checking to detect spoofing, jamming, and poor signal quality
2. **Dense Training Data Generation**: Collect and process high-resolution aerial imagery for machine learning model training
3. **Visual Odometry**: Refine optical flow and feature-tracking algorithms for accurate velocity estimation
4. **Simultaneous Localization and Mapping (SLAM)**: Implement loop-closure detection to correct drift in long-duration flights
5. **Signals of Opportunity**: Explore alternative navigation signals (cellular, WiFi, LTE, radar reflections)
6. **Sensor Fusion**: Integrate all sources with Kalman filtering for seamless GPS/vision transitions
7. **Flight Testing**: Validate system in realistic operational scenarios
8. **System Specification**: Define commercial product specifications and interface standards

## Products & Capabilities Described

### Black Swift S1
- Purpose: Fully autonomous survey and mapping platform
- Features: Hand-launch capable, autonomous landing, simple tablet-based interface
- Applications: Surveying, land management, crop damage assessment, ecological studies
- Integration: Will serve as testbed for DS-GPS development

### Black Swift S2
- Purpose: Fixed-wing scientific payload platform for demanding atmospheric environments
- Specifications: Large payload capacity, longer endurance, higher ceiling, greater range than vector-wing aircraft
- Capability: Autonomous launch/flight/landing in mountainous terrain
- Advantages for coastal mapping: 90-minute time-on-station vs. 15 minutes for DJI M600; 20 m/s mapping speed vs. 5 m/s
- Integration: Primary integration platform for DS-GPS system

### Black Swift E2
- Purpose: Structural and industrial inspection platform
- Features: Advanced autonomous navigation, computer vision-based obstacle avoidance, real-time situational awareness
- Manufacturing: Entirely US-designed and manufactured

### SwiftCore Flight Management System (FMS)
- Core avionics: Controls, communications, autonomous flight for all BST platforms
- Deployments: NASA missions, NOAA operations, international commercial/research users
- Components: SwiftPilot autopilot, SwiftTab tablet interface, SwiftStation ground station
- Key advantage: Minimizes operator workload while improving data quality through sensor-based autonomous path adaptation

### Multi-Hole Probe (MHP)
- Purpose: 3D wind velocity measurement for small UAS
- Sensors: Differential pressure, magnetometer, IMU with sensor fusion
- Measurements: Airspeed, altitude, angle-of-attack, side-slip, temperature, humidity
- Application: Atmospheric science wind characterization

### Diverse-Source Global Positioning System (DS-GPS)
- Form factor: Standalone hardware module (small enough for diverse UAS platforms)
- Output: GPS-compatible position/velocity data stream
- Integration: Works with BST SwiftCore FMS or third-party autopilots
- Operational mode: Seamless switchover from GPS to vision/signal-of-opportunity when GPS becomes unreliable
- Enabling capability: Supports continuous BVLOS operations without GPS

## Use Cases & Applications

### Government/NOAA Applications
1. **Coastal Mapping and Monitoring**
   - Mission: Complete 3D survey of entire U.S. coastline (95,000 miles)
   - Current constraint: LOS operations require 1-km repositioning; limited access to many coastlines
   - BVLOS advantage with DS-GPS: 4 teams of 2 aircraft could map entire coastline in 90 days for ~$850K (vs. $10M+ for LOS operations with 50 teams)
   - Payload: Photogrammetry + LiDAR (~$20K); GPS RTK

2. **Atmospheric Science Missions**
   - Historical BST use: Hurricane, tornado, wildfire, volcano monitoring
   - DS-GPS benefit: Extended range operations without losing position awareness

### Commercial Applications
1. **Pipeline Inspection**
   - Current partner: Institute of Arctic and Alpine Research (University of Colorado)
   - Development: Methane trace detection sensor for tundra
   - BVLOS advantage: Eliminates inefficient ground station repositioning; reduces labor costs
   - Commercial partners: Oil and gas industry

2. **Powerline Inspection**
   - Current approach: Manned helicopters flying low over lines (safety hazard)
   - UAS advantage: Safer, more cost-effective
   - DS-GPS benefit: Machine vision can track powerline back to home in GPS-loss event; supports BVLOS safety

3. **Railroad Track Inspection**
   - Historical demonstration: BNSF/Rockwell Collins BVLOS PIC operations
   - Current limitation: Requires visual observers strung along flight path (labor-intensive, economically marginal)
   - DS-GPS opportunity: Enable safe BVLOS railroad inspection under UTM guidelines without observers

4. **Infrastructure Monitoring**
   - Applications: Precision agriculture, 3D terrain modeling, damage assessment, geo-hazard mapping, mineral exploration
   - Market segment: Remote sensing and environmental monitoring

## Key Results (Phase I)

### Flight Test Achievements
- **Optical flow implementation**: Inertial navigation algorithms implemented on embedded hardware (Jetson TX2) and successfully flight-tested
- **Visual odometry**: Generated trajectory estimates from onboard camera imagery; validated against GPS ground truth after transformation and scaling correction
- **Point cloud mapping**: Created dense map point clouds from flight video
- **Real-time feature extraction**: Demonstrated live feature extraction and tracking in onboard camera feed
- **GPS spoofing detection**: Evaluated detection algorithms

### Technical Validation
- Phase I confirmed feasibility of computer vision + inertial sensor fusion approach
- Prototype hardware verified compatible with small UAS platforms
- Algorithms demonstrated viable for embedded execution (no external processing required)

## Notable Details

### Competitive Positioning
- **First-mover advantage**: No commercially-available COTS product currently exists for GPS-denied UAS navigation
- **Vertical integration**: BST owns entire technology stack (hardware, firmware, software, airframe, sensors), enabling optimization and rapid iteration
- **FAA relationship**: BST has worked with FAA since 2008 on Certificates of Authorization (COAs); offers grant-writing services for customer waiver requests—creates customer-facing competitive moat
- **Barrier to entry**: 2-5 years development, >$1M investment required to replicate

### Commercialization Track Record
- **Previous SBIR successes**: Completed 1 Phase II; actively working on 2 other Phase IIs
- **S2 commercialization**: Phase II completion led to sales to NOAA (2 aircraft) and NASA (1 aircraft)
- **Soil Moisture SBIR** (NNX14CG09C): Generated additional $719K post-Phase II investment from NASA and commercial sources
- **Multi-Hole Probe commercialization**: Delivered 10 units; second generation funded by commercial sales; reduced cost 10x through 3D printing
- **Machine vision underwater photogrammetry**: Commercial contract generated $46K+ in sales; significant growth potential
- **Revenue trajectory**: $1.5M in FY 2019, up $275K from prior year

### Market Opportunity
- **Global UAS market**: $20.71B (2018) → $52.30B (2025), CAGR 14.15%
- **Commercial UAS market**: >$17B by 2024
- **Commercial unit shipments**: 805K units projected by 2021 (CAGR 51%)
- **Environmental monitoring market**: $19.56B by 2021 (CAGR 13.38%)
- **Remote sensing services**: $10.68B (2017) → $21.62B (2022), CAGR 15.14%; UAS segment highest growth
- **Drone services market**: $705.3M (2016) → $18.0B (2022), CAGR 71.62%
- **BST TAM estimate**: Hundreds of units by 2021 (infrastructure inspection, environmental monitoring, remote sensing)

### Business Model
- **Phase II funding**: Government investment ($395.7K) to fund initial development and FAA approval pathways
- **Post-Phase II commercialization**: Financed through company commercial sales and customer revenue
- **Product strategy**: Standalone DS-GPS module sold as value-added feature on BST UAS and for licensing/integration with third-party manufacturers
- **Marketing strategy**: Service offering of FAA waiver application writing for customer purchases

### Company Status (as of October 2020)
- **Founded**: 2011
- **Location**: Boulder, Colorado
- **Employees**: 8 (company states 6 in SBC registration as of January 2019)
- **DUNS**: 078359543
- **EIN**: 45-4203799
- **Capitalization**: No VC/hedge fund/private equity ownership

### FAA/Regulatory Alignment
- Proposal explicitly grounded in UTM (UAS Traffic Management) regulatory framework
- DS-GPS addresses identified FAA performance requirements for BVLOS authorization:
  - Navigation accuracy
  - Position reporting to USS (UAS Service Supplier) in near real-time
  - Safe reaction to GPS denial events
  - Continued avoidance of other aircraft and ground hazards

### IP Strategy
- **Patent protection**: Not pursued; protected through trade secrets
- **Rationale**: Patents inform market of technical details; trade secret approach preferred to avoid defensive patent litigation