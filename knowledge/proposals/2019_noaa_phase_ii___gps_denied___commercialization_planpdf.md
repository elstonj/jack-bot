# 2019 NOAA Phase II GPS-Denied Navigation Commercialization Plan

## Document Metadata
- **Type:** Commercialization Plan (SBIR Phase II proposal supporting document)
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration)
- **Program/Solicitation:** NOAA SBIR Phase II; Proposal Number: NOAA-OAR-OAR-TPO-20200695
- **Date:** 2019 (submitted for 2020 SBIR cycle)
- **BST Products/Systems Referenced:** S1, S2, E2, SwiftCore FMS, Multi-Hole Probe (MHP)
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
Black Swift Technologies proposes to develop a diverse-source global positioning system (DS-GPS) navigation module that enables beyond-visual-line-of-sight (BVLOS) UAS operations using computer vision, inertial sensors, and air-data sensors instead of relying on GNSS constellations. This technology would be integrated with BST's SwiftCore Flight Management System to enable longer-range, more efficient UAS missions for coastal mapping, infrastructure inspection, environmental monitoring, and other applications currently constrained by line-of-sight regulations. The commercialization plan demonstrates significant cost and time savings for government and commercial operations.

## Technical Approach
The DS-GPS module combines:
- **Computer vision techniques** for robust navigation
- **Inertial measurement units (IMU)** 
- **Air-data sensors**
- **Fusion algorithms** to generate navigation solutions independent of GNSS

The system is designed as a standalone hardware module small enough to fit multiple UAS platforms while leveraging commercial off-the-shelf (COTS) technology where possible to maintain affordability. BST emphasizes vertical integration, controlling hardware, firmware, software, airframe, and sensors in-house to maximize accuracy and efficiency.

**Key differentiator:** Unlike DOD GPS-denied systems (not commercially available), BST plans to seek FAA approvals to demonstrate the capability and offer grant-writing services to customers for regulatory compliance—a service competitors don't provide.

## Products & Capabilities Described

### **SwiftCore Flight Management System (FMS)**
- Advanced end-to-end avionics solution for autonomous UAS control and communication
- Proven in field by NASA, NOAA, and commercial users (CU, UTSI, etc.)
- Comprises: SwiftPilot autopilot, SwiftTab tablet interface, SwiftStation ground station, sensor integration
- Autonomously modifies flight path based on sensor inputs; minimizes operator workload
- Engineered for nomadic scientific campaigns in harsh environments (high-altitude, arctic, desert, strong turbulence, corrosive particulates)

### **S1 Aircraft**
- Advanced fully autonomous survey/mapping platform
- Ready-to-fly with all components included (aircraft, batteries, ground station, tripod, tablet, toolbox, carrying case, handset)
- Hand-launch capable; autonomous belly landing
- Used for surveying, land management, crop damage assessment, ecological studies

### **S2 Aircraft**
- Purpose-built for flying scientific payloads in demanding atmospheric environments
- Larger payload capacity than vector-wing airframes
- Longer endurance, higher ceiling, greater range
- Rugged airframe for autonomous launch/flight/landing in mountainous regions
- Time-of-flight (TOF) with payload: 90 minutes
- Mapping speed: 20 m/s

### **E2 Aircraft**
- Designed, manufactured, serviced entirely in USA
- Engineered for structural and industrial inspections
- Advanced navigation technology for precise, up-close infrastructure inspections in extreme conditions
- Leverages computer vision and machine learning for completely autonomous flight
- Real-time data delivery to operator

### **Multi-Hole Probe (MHP)**
- Tightly integrated wind velocity measurement device for small UAS
- Combines differential pressure, magnetometer, IMU with fusion algorithms
- Records airspeed, altitude, angle-of-attack, side-slip, ambient temperature, relative humidity
- Comprehensive wind environment and aircraft performance evaluation

## Use Cases & Applications

### **Government Applications (Primary Target)**
1. **NOAA Coastal Mapping:** 
   - 95,000-mile U.S. coastline survey in single summer
   - Photogrammetry + LIDAR with GPS RTK
   - Payload cost ~$20,000
   - **LOS limitation comparison:** DJI M600 (15 min TOF at 5 m/s) vs. S2 VTOL (90 min TOF at 20 m/s)
   - **Cost/personnel to map coastline in 90 days:**
     - DJI M600 LOS: 50 aircraft, 50 teams of 2, ~$10M
     - S2 LOS: 50 aircraft, 50 teams of 2, ~$10M
     - DJI M600 BVLOS: 16 aircraft, 8 teams of 2, ~$5M
     - **S2 BVLOS: 4 aircraft, 4 teams of 2, $850K** (most efficient)

### **Commercial Applications**
1. **Pipeline Inspection**
   - Methane detection over tundra (partnership with Institute of Arctic and Alpine Research, University of Colorado)
   - Currently inefficient due to ground station repositioning requirements
   - DS-GPS enables long-range missions; machine vision can track pipeline to home aircraft on GPS loss
   - Tested with oil and gas industry partners

2. **Powerline Inspection**
   - Currently done mainly by manned helicopters flying low
   - BVLOS UAS offers greater safety
   - Machine vision system can track powerlines for return home if GPS lost
   - Applies to pipelines and railroad tracks

3. **Railroad Track Inspection**
   - BNSF Railways/Rockwell Collins demonstrated BVLOS pilot-in-command operations
   - Current FAA requirement: visual observers strung along flight path for handover tracking and voice communication
   - Labor intensive; DS-GPS technology enables safe operation with reduced observer requirement
   - Would enable operations under UTM (UAS Traffic Management) guidelines

## Commercialization Strategy

### **Financing Model**
- SBIR Phase II funding for initial development and FAA approval work
- Company resources for post-Phase II commercialization enabled by commercial sales
- Offered as value-added feature on BST UAS and as standalone product to other UAS manufacturers

### **Marketing Plan**
- **Initial target:** Government (NOAA, NASA) with strong track record in safe operations and numerous relevant scientific efforts
- **FAA approval focus:** BST will lead effort to secure FAA approvals, providing first-mover advantage and reducing friction for future customer requests
- **Differentiation:** Offer grant-writing services for customers purchasing technology (unique service competitors don't provide)
- **FAA engagement history:** Involved since 2008 when FAA first required Certificates of Authorization (COAs); since 2013, BST has offered FAA application and waiver writing services

### **Track Record of Commercialization**
BST has demonstrated successful SBIR commercialization:
- **Soil Moisture Mapping sUAS (NNX14CG09C):** Led to additional $719,314 investment; S2 UAS sold to NOAA (2) and NASA (1)
- **Ruggedized UAS for Harsh Environments (NNX16CP42P):** Multi-hole probe instrument development; 10 units delivered; second generation funded by commercial sales
- **Machine vision for underwater photogrammetry:** $46,088 in Phase I SBIR commercialization (first Phase I commercialization success)

## Market Analysis

### **Global Market Context**
- Global UAS market: $20.71B (2018) → $52.30B (2025), CAGR 14.15%
- Commercial UAS market: Projected >$17B by 2024
- Commercial UAS shipments: 805,000 units by 2021 (CAGR 51%)
- Drone services market: $705.3M (2016) → $18,022.7M (2022), CAGR 71.62%

### **Target Market Segments**
- **Environmental Monitoring:** $19.56B by 2021 (CAGR 13.38%)
- **Remote Sensing Services:** $10.68B (2017) → $21.62B (2022), CAGR 15.14%
  - UAS segment projected highest CAGR
  - Applications: precision farming, 3D terrain modeling, damage assessment, geo-hazard mapping, mineral exploration
- **Drone services by industry:** Infrastructure, agriculture, entertainment, logistics, oil/gas, utility/power, security, search/rescue, mining, scientific research, insurance
- **BST's strongest presence:** Mapping/surveying, scientific research, environmental monitoring

### **TAM Estimate**
- BST Total Addressable Market (TAM): Hundreds of units by 2021
- Driven primarily by infrastructure inspections, environmental monitoring, atmospheric observations

## Competitive Landscape

### **Current Situation**
- Significant academic research exists on GPS-denied navigation (vision systems, signals of opportunity)
- **No commercially available COTS solution** currently on market
- Some DOD GPS-denied technologies exist but unavailable for commercial UAS

### **BST Competitive Advantages**
1. **Vertical Integration:** Internal ownership of entire system (hardware, firmware, software, airframe, sensors)
2. **Subject Matter Expertise:** In-house core competencies enable rapid evolution to emerging needs
3. **First-Mover Advantage:** Leading FAA approval efforts; providing barrier to entry
4. **Barrier to Entry:** Technology requires 2-5 years development at >$1M cost
5. **FAA Expertise:** Established relationships since 2008; offers regulatory writing services (unique differentiator)
6. **Service Value-Add:** Grant application writing for customers pursuing BVLOS approvals

## Innovation & Industry Impact

The DS-GPS module represents a paradigm shift enabling:
- **More reliable UAS operations** independent of GNSS constellation availability
- **Stepping stone to safe BVLOS operations** critical for wider NAS integration
- **New application categories:** Drone delivery, long-range pipeline inspection, remote environmental monitoring
- **Environmental benefit:** Energy companies can monitor infrastructure environmental impact more cost-effectively
- **Social benefit:** Autonomous delivery services particularly valuable during COVID-19 for social distancing compliance

## Key Business Metrics (at time of proposal)

- **Company founding:** 2011
- **Employees:** 8 (as of proposal)
- **Revenue:** $1.5M (prior year), up $275K from previous year
- **Growth trajectory:** Steady expansion documented in growth analysis chart

## Patent & IP Strategy

BST chose to protect intellectual property through **trade secrets** rather than patents. Rationale: Patents serve to inform the market about technical intricacies and put BST in position of needing to defend against infringement claims. Sensitive material discussed with potential customers under non-disclosure agreements.

## Notable Details

1. **Operational efficiency comparison:** BVLOS S2 operations for U.S. coastline mapping would require only 5 flights/day vs. 16-17 flights/day for competitors' platforms—"much more reasonable number" for operational teams

2. **Access challenges acknowledged:** Document notes that despite compelling economics, implementation faces real-world obstacles (limited coastal access, flight restrictions near populated areas)

3. **Proof of concept timing:** Phase II work to include FAA permission to fly BST aircraft BVLOS in pertinent area for NOAA operational activities

4. **Post-SBIR plan:** Commercialization financed by commercial sales; technology offered both integrated on BST platforms and as standalone to other UAS manufacturers

5. **Customer support model:** BST plans to differentiate by offering grant-writing services to customers seeking FAA approvals for their own BVLOS operations—revenue-generating service that competitors unlikely to provide

6. **Regulatory history:** BST's team "closely involved with FAA regulations since 2008"—establishes credibility for navigating GPS-denied navigation certification pathway