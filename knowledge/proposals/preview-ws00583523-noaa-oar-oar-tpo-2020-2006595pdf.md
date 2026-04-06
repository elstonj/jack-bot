# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- **Type:** SBIR Phase II Proposal
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA) – Office of Oceanic and Atmospheric Research (OAR)
- **Program/Solicitation:** NOAA SBIR FY 2020 Phase II (NOAA-OAR-OAR-TPO-2020-2006595)
- **Date:** October 14, 2020 (submitted)
- **Proposed Period of Performance:** April 1, 2021 – March 31, 2023
- **BST Products/Systems Referenced:** S1, S2, S2 XT, E2, SwiftCore FMS (Flight Management System), SwiftPilot, SwiftTab, SwiftStation, Multi-Hole Probe (MHP)
- **Key Personnel:** Dr. Jack S. Elston (CEO & Principal Investigator), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposes to develop a Diverse-Source Global Positioning System (DS-GPS) to enable beyond-visual-line-of-sight (BVLOS) UAS operations by providing accurate position information in GPS-denied environments. The system integrates computer vision, machine learning, inertial sensors, air-data sensors, and signals of opportunity to maintain navigation capability when GPS is jammed, spoofed, or fails. This technology addresses a critical gap identified in FAA/UTM regulations for safe BVLOS operations and will unlock commercial applications in coastal mapping, pipeline inspection, power line inspection, and railroad track monitoring.

## Technical Approach

### Core Technology
The proposed DS-GPS system provides position information through multiple redundant sources without relying on GNSS (Global Navigation Satellite System) constellations:

**Key Components:**
1. **GPS Monitoring & Degradation Detection** – Real-time detection of GPS jamming, spoofing, or hardware failure; monitoring solution integrity and quality metrics
2. **Visual Odometry** – Computer vision-based optical flow analysis to measure platform motion and relative position changes
3. **Simultaneous Localization and Mapping (SLAM)** – Building and maintaining maps of the environment while simultaneously localizing the aircraft within it
4. **Signals of Opportunity** – Exploitation of available electromagnetic signals (WiFi, cellular, television broadcasts, etc.) for positioning when GPS unavailable
5. **Sensor Fusion** – Integration of vision, inertial measurement unit (IMU), air-data sensors, magnetometer, and signals of opportunity into coherent navigation solution

### Phase I Accomplishments
- Designed optical flow algorithms for motion estimation
- Developed absolute positioning algorithms
- Created plan for GPS degradation detection
- Assessed available navigation signals

### Phase II Technical Objectives
1. **GPS Monitoring** – Implement robust GPS quality assessment and jam/spoof detection
2. **Dense Training Data Generation** – Create dataset for machine learning model training via flight testing
3. **Visual Odometry** – Refine optical flow techniques for accurate motion measurement
4. **SLAM Implementation** – Develop and test map-based localization
5. **Signals of Opportunity** – Integrate multiple signal sources for position augmentation
6. **Sensor Fusion** – Combine all sensor inputs into unified, high-confidence navigation output

### Hardware Module
The final product will be a small, standalone hardware module sized to fit on various UAS platforms, leveraging commercial-off-the-shelf (COTS) technology where possible to keep costs affordable.

## Products & Capabilities Described

### Black Swift UAS Systems
**S1 (Survey Platform)**
- Advanced fully autonomous survey and mapping platform
- Ready-to-fly, hand-launch capable with autonomous belly landing
- Used for surveying, land management, crop damage assessment, ecological studies

**S2 (Scientific Payload Platform)**
- Purpose-built for flying scientific payloads in demanding atmospheric environments
- High altitude, corrosive particulates, strong turbulence capable
- Larger payload capacity, longer endurance, higher ceiling, greater range than vector wing airframes
- Autonomous launch, flight, and landing in mountainous regions

**S2 XT**
- Ruggedized version for extreme environments

**E2 (Infrastructure Inspection)**
- Designed and manufactured entirely in USA for structural/industrial inspections
- Advanced navigation technology for precise inspections in extreme conditions
- Computer vision and machine learning capable
- Completely autonomous flight capability

**SwiftCore Flight Management System (FMS)**
- Advanced end-to-end avionics solution
- Controls, communicates, and commands UAS for fully autonomous flight
- Approved/used by NASA, NOAA deployments, and commercial users
- Components: SwiftPilot (autopilot), SwiftTab (tablet interface), SwiftStation (ground station)
- Minimizes operator workload while improving data quality through autonomous flight path modifications

**Multi-Hole Probe (MHP)**
- Wind velocity measurement device integrating differential pressure, magnetometer, and IMU
- Provides full wind vector solution
- Captures airspeed, altitude, angle-of-attack, side-slip, ambient temperature, relative humidity

### DS-GPS System (Proposed)
- **Purpose:** Enable BVLOS operations through GPS-denied navigation
- **Design Philosophy:** Small, modular, integrate-able into various platforms; leverage COTS where possible
- **Key Capability:** Maintain accurate position information when GPS unavailable (jamming, spoofing, failure)
- **Integration:** Works with SwiftCore FMS to enhance aircraft autonomy and safety
- **Regulatory Compliance:** Designed to meet FAA/UTM BVLOS performance requirements for navigation, communications, intent sharing, aircraft avoidance, and FAA connectivity

## Use Cases & Applications

### Government Applications
**NOAA Coastal Mapping**
- Conduct 3D survey of entire U.S. coastline (95,000 miles) in one summer for yearly repeats
- Cost analysis comparing BVLOS vs. line-of-sight operations
- **BVLOS Advantage:** BST S2 BVLOS could accomplish mission with 4 aircraft, 4 teams of 2, ~$850K cost vs. 50 aircraft/50 teams or 16-17 flights/day for LOS operations

### Commercial Applications
1. **Pipeline Inspection**
   - Partnership with Institute of Arctic and Alpine Research (University of Colorado) to develop methane detection sensor over tundra
   - Current LOS approach requires frequent ground station repositioning; BVLOS enables continuous long-distance monitoring
   - Highest cost is labor hours; BVLOS dramatically reduces operational inefficiency

2. **Powerline Inspection**
   - Currently conducted primarily by manned helicopters flying low over lines
   - Proposed small UAS BVLOS approach offers safety advantages
   - DS-GPS system provides machine vision-based powerline tracking for backup navigation (machine vision tuned to track powerline back to launch site if GPS lost)

3. **Railroad Track Inspection**
   - BNSF Railways/Rockwell Collins demonstration showed feasibility but required visual observers strung along flight path
   - Labor-intensive due to FAA requirement for visual oversight; DS-GPS technology would enable safe BVLOS operations under UTM guidelines without observer requirement

### Market Segments
- Infrastructure inspections (pipelines, powerlines, railroad tracks)
- Environmental monitoring and remote sensing
- Atmospheric observations
- Precision agriculture
- Aerial photography
- Disaster risk management
- Mining and mineral exploration
- Insurance assessment

## Market Analysis

### Market Size & Growth
- **Global UAS Market (2018):** $20.71 billion → projected $52.30 billion by 2025 (CAGR: 14.15%)
- **Commercial UAS Market:** Projected to exceed $17 billion by 2024
- **UAS Shipments:** Projected 805,000 units by 2021 (CAGR: 51%)
- **Environmental Monitoring Market:** Expected to reach $19.56 billion by 2021 (CAGR: 13.38%)
- **Remote Sensing Services:** $10.68 billion (2017) → $21.62 billion by 2022 (CAGR: 15.14%); UAS segment highest CAGR
- **Drone Services Market:** $705.3 million (2016) → $18,022.7 million by 2022 (CAGR: 71.62%)

### Target Addressable Market (TAM)
- BST's TAM estimated at hundreds of units by 2021
- Primary markets: government (NOAA, NASA) and commercial infrastructure/environmental monitoring users

## Technical Specifications & Performance Claims

### Coastal Mapping Example
**Aircraft Performance:**
- **DJI M600:** 15-minute time of flight with payload; 5 m/s mapping speed
- **BST S2 VTOL:** 90-minute TOF with payload; 20 m/s mapping speed

**Operational Efficiency:**
- **DJI M600 LOS:** 16-17 flights/day required; full battery per mission
- **BST S2 LOS:** 4-5 flights/day (setup/teardown intensive)
- **BST S2 BVLOS:** 5 flights/day (dramatically more efficient)

**Mission Scaling (95,000 miles coastline, 90 flight days available):**
- LOS operations: 50 aircraft + 50 teams required
- DJI BVLOS: 25 aircraft + reduced teams (still significant)
- BST S2 BVLOS: 4 aircraft + 4 teams → ~$850K total cost

### Payload Capability
- Combined photogrammetry + LIDAR payload approximately $20,000
- GPS RTK capable

## Key Results & Achievements

### Phase I Completion (Prior Work)
- Successfully demonstrated feasibility of using computer vision techniques with inertial and air-data sensors for navigation
- Developed optical flow algorithms and absolute positioning algorithms
- Created GPS degradation detection plan
- Assessed available navigation signals for exploitation

### Company Performance
- **Founded:** 2011
- **Current Employees:** 8 (as of proposal submission, SBC data shows 7 employees)
- **Recent Revenue:** $1.5M (previous year $1.225M); $275K growth year-over-year
- **Previous SBIR Success:**
  - Completed Phase II: "Soil Moisture Mapping sUAS" (NNX14CG09C) → $719,314 additional investment; commercialized soil moisture radiometer and S2 UAS; 2 aircraft to NOAA, 1 to NASA
  - Ongoing Phase II: "Ruggedized UAS for Scientific Data Gathering in Harsh Environments" (NNX16CP42P) → Multi-hole probe developed (10 units delivered); second generation funded by commercial sales
  - Phase I SBIR machine vision technology commercialized for underwater photogrammetry → $46,088 in sales with significant ongoing opportunity

## Notable Details

### Competitive Advantages
1. **Vertical Integration:** BST owns entire system (hardware, firmware, software, airframe, sensors) enabling maximum accuracy/efficiency
2. **In-House Expertise:** Core subject matter expertise enables quick evolution to emerging needs
3. **First-Mover Strategy:** Early FAA approval acquisition creates barrier to entry
4. **FAA Experience:** BST actively involved with FAA since 2008; offering COA/waiver application services since 2013
5. **Commercialization Track Record:** Proven ability to commercialize SBIR technology with subsequent government and commercial sales

### IP Strategy
- Protection via **trade secrets** rather than patents
- Rationale: Patents inform market of technology details and create defense obligations
- Sensitive material shared with customers under NDA

### Post-Award Commercialization Plans
- Phase II funding focuses on FAA approval and demonstration using NOAA operational scenario
- Post-Phase II commercialization financed by:
  - Company resources enabled by commercial sales
  - Offered as value-added feature on BST UAS
  - Standalone sales to other UAS manufacturers
- Early support service: offer to write grant applications for customers (fee-based)

### Development Barrier to Entry
- 2-5 years of development effort required
- >$1M estimated cost
- Creates significant competitive moat for first mover

### Regulatory Approach
- Fully grounded in UTM rules
- Performance authorization strategy: FAA case-by-case evaluation leading to standard operational packages and streamlined approvals
- Addresses FAA requirements: navigation, communications, intent sharing, aircraft avoidance, FAA connectivity

### Funding Request
- **Requested Amount:** $395,730.81 