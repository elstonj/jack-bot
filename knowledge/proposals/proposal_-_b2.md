# The Soil Moisture Mapping sUAS

## Document Metadata
- Type: SBIR/STTR Civilian Commercial Readiness Pilot Program (CCRPP) Application (Form B2)
- Client/Agency: NASA (primary), with matching investments from University of Colorado, University of Maryland Eastern Shore, and NASA MALIBU
- Program/Solicitation: NASA SBIR/STTR CCRPP; underlying work from Soil Moisture Mapping sUAS SBIR (Phase II and Phase II-E)
- Date: March 30, 2017
- BST Products/Systems Referenced: SuperSwift sUAS, L-band radiometer, SwiftTrainer, SwiftPilot autopilot, SwiftStation ground control station
- Key Personnel: Dr. Maciej Stachura, Dr. Jack Elston, Bradley Cheetham (COO), Prof. Gasiewski (referenced), Dr. Miguel O. Román (NASA GSFC)

## Executive Summary
Black Swift Technologies proposes to commercialize two core technologies from its Soil Moisture Mapping sUAS SBIR project: the SuperSwift sUAS airframe and an L-band radiometer payload. The CCRPP work will focus on improving manufacturability of both systems and integrating new payloads for NASA MALIBU and NOAA FIREX missions. Total matching investments of $177,157 from NASA MALIBU, University of Colorado, and University of Maryland Eastern Shore will be combined with CCRPP funds to accelerate technology maturation and market entry by Q3 2018.

## Technical Approach

### SuperSwift sUAS Manufacturability
BST proposes a three-aircraft build program to improve manufacturing processes and tooling:

1. **Fuselage**: Streamline internal design and construction of assembly jigs to ensure tolerances for rapid part replacement. Goal is to outsource composite fuselage production to Northwind Composites.

2. **Tail Design**: Redesigned aerodynamically in Phase II-E for improved stability and ease of manual flight. CCRPP work includes creating composite molds, interior redesign for single bonding operation, and assembly jigs.

3. **Wing Design**: Replace current foam-core design with hollow-core design outsourced to composite suppliers. New design will reduce weight, manufacturing time, and improve quality/repeatability. Includes composite molds and assembly jigs.

4. **Car Launch System**: Modify University of Colorado's Tempest car launcher design with automated servo-controlled release mechanism. More reliable at cold temperatures (<40°F) than existing bungee catapult; tested 30+ times without incident.

### L-band Radiometer Design (3rd Revision)
The radiometer is a lobe-differencing correlating radiometer that will undergo design revision for manufacturability:

1. **Functional Design**: Address manual work, wiring, and calibration requirements of current design; include critical design review.

2. **Board-Level Design**: Circuit board schematic, layout, materials selection, and mechanical dimensions optimized for easy airframe integration via Colorado Engineering Inc (CEI).

3. **Board Testing**: Extensive validation of new design to verify readiness for direct integration without additional manual work.

4. **Integration & Lab Test**: Install radiometer with antennas and other electronics in SuperSwift before flight testing.

5. **Finalized Design**: Incorporate results from testing to produce design ready for production manufacture.

**Supporting Components** (already mature from Phase II):
- Four-element antenna array: printed circuit board patterns (sourced from Advanced Circuits)
- NDVI/Thermal Sensors: three-channel sensor (red, near-infrared, longwave infrared) with upward/downward facing elements
- Data Logger: balun circuit board, FPGA board (collects radiometer data, thermistors, autopilot telemetry, NDVI/thermal data at 240MB/s via USB 3.0), Linux single board computer, 1TB SSD storage

### Payload Integration for New Applications

**MALIBU Integration** (NASA GSFC funded):
- Current MALIBU payload: 12 multispectral cameras + incident light sensor moving from Tempest to SuperSwift (addresses EMI issues identified in previous deployments)
- New MALIBU payload: Replace Tetracam-based system with MAPIR Kernel camera array featuring doubled resolution, reduced weight, 10x increased capture rate, automatic geo-tagging

**FIREX Integration** (University of Colorado/NOAA):
- In situ payload: CO₂, CO, aerosol, relative humidity, temperature, pressure, wind measurements (multi-hole probe)
- Remote sensing payload: fire radiative power, fire perimeter, ambient RH/T/p/wind measurements
- Combined into UAS Observation System (UASOS) for test flights and nighttime fire plume sampling strategy development

## Products & Capabilities Described

### SuperSwift sUAS
- **What it is**: Small unmanned aircraft system designed specifically to carry the L-band radiometer and antenna; modular payload bay with removable nose cone for scientific payloads; built-in electromagnetic interference (EMI) shielding
- **Evolution**: Evolved from Tempest aircraft (external radiometer antennas, significant EMI issues) to SuperSwift (integrated payload nose cone with dedicated radiometer, internal EMI shielding)
- **Key specifications/capabilities**:
  - Robust, simple to use
  - Operates from unimproved areas
  - Payload modularity allows adaptation to multiple missions
  - Simplified operation reduces ongoing operational costs
  - Designed for scientific-grade measurements
  - Can field-swap payloads between MALIBU multispectral and soil moisture radiometer
  - Current design demonstrates capability; CCRPP work improves manufacturability and reduces cost

### L-band Radiometer
- **What it is**: Core sensor for generating soil moisture maps; lobe-differencing correlating radiometer measuring at L-band frequencies
- **Measurement capability**: Soil moisture measurements at ~15-meter resolution (compared to ~40 km resolution of satellite-based SMAP)
- **Current limitations**: Requires significant manual work, testing, and tuning before installation; major hurdle to cost reduction and manufacturing rate
- **Proposed improvements**: Third revision design with focus on manufacturability and reduced post-processing requirements

### SwiftTrainer
- **What it is**: Smaller, lower-cost sUAS designed for training purposes
- **Use in this context**: To be delivered to University of Maryland Eastern Shore (UMES) in summer 2017 to prepare their team for soil moisture mapping flights with SuperSwift in 2018

### SwiftPilot Autopilot
- Autopilot avionics package previously commercialized by BST; provides control and sensor fusion capabilities

### SwiftStation Ground Control Station
- Tablet software-based ground control station for aircraft operations

## Use Cases & Applications

### 1. Satellite Calibration and Validation
- **Primary customers**: NASA, CEOS-Space agencies (ESA, NOAA, USGS, EUMETSAT)
- **Specific missions supported**: JPSS-1, GOES-R, Sentinel 2a/b, Sentinel 3a/b, Landsat-8, MSG-3, SMAP, Aquarius, SMOS
- **NASA MALIBU Project**: Funded investor and customer; planning regular operations through summer 2018 and beyond; committed to acquire and fly SuperSwift for multispectral imaging validation
- **Value proposition**: Provides reference measurements at finer spatial resolution than satellites; supports CEOS Working Group on Calibration and Validation framework

### 2. Precision Agriculture
- **Target application**: Optimize water usage while maintaining crop yields; support variable-rate irrigation
- **Key demonstration site**: Irrigation Research Foundation (IRF) in Colorado
  - Demonstrated 15% water savings while maintaining crop yields
  - Direct control of irrigation system allows comparison of different techniques
- **Project Drought (University of Colorado)**: 
  - Second-year project at IRF test site
  - Uses SMM sUAS to gather soil moisture maps for variable-rate irrigation guidance
  - Addresses SMAP mission goals of assisting crop productivity
- **UMES Variable Rate Irrigation Project**:
  - Planned flights in late spring 2018
  - UMES identified as potential owner/operator given aviation training heritage
  - SwiftTrainer delivery in summer 2017 for team training
- **Other interested organizations**: Oklahoma State University, St. Louis University, University of Bristol, Colorado State University, Monash University (Australia), National Geospatial-Intelligence Agency
- **Market potential**: 41 soil moisture networks worldwide representing 1,400+ sites; potential addressable market >$14 million for system sales at $100,000/unit (1 system per 10 sites)

### 3. Wildland Firefighting/Fire Monitoring
- **NOAA FIREX Project**: University of Colorado investment for SuperSwift integration with fire monitoring payloads
- **Capabilities**: In situ and remote sensing measurements of CO, CO₂, aerosol, relative humidity, temperature, pressure, winds
- **Application**: Nighttime fire plume sampling and remote fire observation
- **Project timeline**: Initial demo flights Q2 2018; production aircraft ready for sustained deployment Q2 2019
- **Market expansion**: Opens new capability segment for SuperSwift; aligns with NOAA interests; potential expanded funding through end of FIREX (2019)

### 4. Flash Flood Prediction Support
- **Historical precedent**: 2007 NASA-funded research at CU Center for Environmental Technology mapped soil moisture in flood-affected North Texas/Oklahoma using P-3 aircraft Polarimetric Scanning Radiometer
- **Data assimilation application**: Soil moisture data input to rainfall-runoff models to calculate rainfall thresholds for flooding; informs FEMA alerts and warnings
- **CCRPP advantage**: SMM sUAS enables expanded data collection at fraction of P-3 operating cost
- **Deployment requests**: BST was contacted about deploying system during 2017 landslide events in Grand Junction, Colorado and Washington

## Key Results (for reports)
This is a proposal document, not a report with results. However, it documents the following accomplishments and demonstrations from prior work:

**Phase II and Phase II-E Achievements**:
- Demonstrated SuperSwift aircraft capability and specifications
- Two successful MALIBU field campaigns with prototype aircraft proving value of platform
- Project Drought experiments showing 15%+ water savings with soil moisture data
- 30+ successful tests of car launcher system without incident
- Successfully completed six NASA Airworthiness Flight Safety Review Boards (AFSRB) and Flight Readiness Review Boards (FRRB)

**Planned CCRPP Flight Testing** (10 deployments):
1. MALIBU payload testing at farm site (Q3 2017)
2. Project Drought deployment (summer 2017)
3. UMES flight training (unspecified)
4. Additional deployments through Q2 2019 (details partially cut off in document)

## Notable Details

### Customer/Investor Base
- **Total matching funds committed**: $177,157
  - NASA MALIBU (SuperSwift Integration): $49,604
  - NASA MALIBU (New payload design/integration): $41,073
  - University of Colorado (Project Drought): $49,090
  - UMES (Training/variable rate integration): $15,000
  - University of Colorado (NOAA FIREX): $22,390

### Market Analysis
- **Addressable markets**: Satellite cal/val, precision agriculture, wildland firefighting
- **Market size estimates**: 
  - Civil UAS market projected $1.8-2.4 billion through 2020
  - Precision agriculture identified as largest sUAS market segment with 2.2 million farms in US
  - In situ soil moisture network: 41 networks, 1,400+ sites globally
- **Competitive advantages**:
  - First mover in L-band radiometer on sUAS for soil moisture mapping
  - SuperSwift modularity enables rapid payload swapping
  - Simplified operations reduce total cost of ownership
  - EMI shielding and integrated payload design unique to SuperSwift
  - BST expertise: 140+ FAA Certificates of Authorization (CoA) between Dr. Stachura and Dr. Elston; hundreds of UAS deployments
- **Competition**: No direct sUAS competitors; satellite missions (SMAP, Aquarius, SMOS) are complementary; manned aircraft (AirMOSS) more expensive; in-situ sampling techniques provide comparison/calibration data

### Financial Status (as of 2016)
- **FY 2016 Revenue**: $676,397
  - Billable Expense Income: $348,581