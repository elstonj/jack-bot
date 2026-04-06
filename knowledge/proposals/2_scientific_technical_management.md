# NASA ROSES A.59 FireSense Technology Proposal: Pre-Fire Soil & Live Fuel Moisture Mapping

## Document Metadata
- **Type**: NASA grant proposal (S/T/M section - Scientific/Technical/Management)
- **Client/Agency**: NASA (ROSES 2024, Program Element A.59 - Wildland FireSense)
- **Program/Solicitation**: NASA ROSES 2024 A.59 Wildland FireSense Technology
- **Date**: Submitted March 2024 (document created March 7, modified March 29, 2024)
- **Status**: Completed/Inactive/Unsubmitted (appears in "Attic")
- **BST Products/Systems Referenced**: 
  - L-band soil moisture radiometer UAS (fixed-wing and multirotor versions)
  - Multi-UAS autonomy and swarm coordination system
  - Edge computing/onboard processing platform
  - Terrain-aware flight planning and terrain-following capabilities
- **Key Personnel from BST**:
  - Jack Elston, PI - UAS chief designer, project lead
  - Maciej Stachura, Co-I - Multi-aircraft UAS design and flight operations expert

## Executive Summary
Black Swift Technologies proposes to develop an operational pre-fire decision support system using L-band radiometer-equipped UAS to generate near-real-time, high-resolution soil moisture and live fuel moisture (LFM) maps for wildfire management. The system will coordinate up to 8 small UAS (fixed-wing and multirotor) operated by a single pilot, guided by NASA satellite data (UAVSAR P-band in Year 1, NISAR in subsequent years), with onboard processing enabling rapid data delivery to fire management partners at the Pepperwood Preserve in California and potentially broader regions.

## Technical Approach

### Core System Architecture
- **Multi-tiered data fusion**: High-resolution UAS L-band radiometer data (down to 2m resolution) combined with wider-area satellite data (UAVSAR 20×60 km in Y1, NISAR 6-day global revisit in Y2+)
- **Operational model**: 8 UAS flown by single operator from single ground station; enables coverage of 3,200+ acres (Pepperwood) in one day at high resolution
- **Platform mix**: Multirotor for high-resolution, low-altitude mapping (15m AGL for 5m resolution) in mountainous/vegetated terrain; fixed-wing for efficiency and area coverage (18 m/s vs 3 m/s)

### Key Technical Innovations

**1. Onboard L-Band Brightness Temperature Calculation**
- New digital correlator with FPGA board for real-time coherence matrix calculation
- Self-calibration and gain fluctuation immunity
- Eliminates multi-hour post-processing; enables near-real-time soil moisture products onboard each UAS
- Allows self-checking and intelligent re-tasking of individual aircraft

**2. Multi-UAS Autonomy & Swarm Operations**
- Automated mapping flight plans with terrain-based planning
- Active terrain tracking and avoidance
- Automated pre-flight checks and sensor setup
- Enable single operator to fly 2 UAS (Y1), 4 UAS (Y2), 8 UAS (Y3)
- Requires FAA and NASA approval for multiple simultaneous operations

**3. Intelligence Tasking & Data Fusion**
- Radar retrieval algorithm (originally developed for SMAP SAR) adapted for P-band UAVSAR and NISAR
- Uses "data cube" lookup table approach (dielectric constant, surface roughness, vegetation water content axes)
- Wide-area satellite soil moisture maps used to identify high-risk areas and task UAS swarm
- Fusion of multi-scale data: 2m resolution UAS, 20m UAVSAR, 200m NISAR

**4. Live Fuel Moisture Derivation**
- Soil moisture converted to LFM through empirically-derived relationships (developed at Pepperwood)
- Strong correlation between root-zone soil moisture and plant live fuel demonstrated
- High-correlation calibration developed for chaparral species (chamise) and oak species

## Products & Capabilities Described

### 1. L-Band Soil Moisture Radiometer UAS
- **What it is**: Passive L-band radiometer payload on fixed-wing and multirotor platforms; originally developed under NASA SBIR
- **Current status**: Operationalized after SBIR; 100+ flights for USGS, NOAA, universities, commercial partners
- **Proposed improvements**:
  - Fixed-wing version: 2.2 kg, <50W power
  - Multirotor version: 1.5 kg, <50W power
  - Both include thermal and NDVI sensors
  - New digital correlator and FPGA-based real-time processing
- **Performance**: 
  - Resolution: down to 2m (multirotor at 15m AGL)
  - Can measure through sparse tree canopy (slower integration time of multirotor advantageous)
  - Field validation showing strong agreement with in-situ measurements (Figure 9)

### 2. Multi-UAS Swarm Operations System
- **Scalable single-operator control**: Ground station UI/comms for managing 2→4→8 UAS
- **Flight safety infrastructure**: Enables FAA/NASA permissions progression (2 → 4 → 8 per year)
- **Terrain-aware autonomy**: Automated flight planning and active altitude tracking for mountainous terrain
- **Data management**: Distributed processing reduces operational overhead vs. centralized processing

### 3. Real-Time Data Processing Pipeline
- Edge computing capability (onsite calculation with no connectivity)
- L-band brightness temperature calculation onboard
- Near-real-time soil moisture product generation
- Future capability: sensor/model-directed flight control

### 4. Live Fuel Moisture Mapping System
- Integrated tool to convert soil moisture to LFM maps
- Species-specific relationships for chaparral and forest ecosystems
- Format compatible with existing wildfire management systems
- Delivery <30 minutes from landing (Y3 goal)

## Use Cases & Applications

### Primary Use Case: Pre-Fire Prescribed Burn Planning
- **Location**: Pepperwood Preserve, Sonoma County, CA (3,200-acre instrumented site)
- **Application**: Support decision-making for controlled burns by providing real-time soil moisture/LFM data
- **Timeline**: Coordinate with existing prescribed burns at Pepperwood (Year 3+)
- **Partners**: Pepperwood Preserve (NGO focused on fire resilience), CalFire, USGS California Water Science Center

### Secondary Use Cases
- **Fire risk assessment**: Input to fire danger rating systems for region-wide wildfire risk
- **Active fire response**: Initial mapping for response to ignition sources
- **Post-fire monitoring**: NISAR disturbance product to identify fire perimeters (Y3 exploration)
- **Scalability**: System designed for eventual expansion to other California and western US fire-prone regions

### Operational Integration
- Real-time delivery to burn boss and land management personnel
- Data format and resolution informed by Pepperwood/CalFire feedback
- Stakeholder engagement to ensure actionability and utility

## Key Results (from Pilot Work)

### Previous USGS-Funded Pilot (2021-2023)
- **4 field deployments** at Pepperwood with iterative technology refinement
- **900+ ground validation measurements** of soil moisture via mobile TDR
- **Major hardware/software improvements** implemented based on field experience:
  - Slope correction algorithm for steep terrain
  - Thermal electronics expansion for high-temperature stability
  - Thermal calibration technique upgrade
  - Development of multirotor variant for slower flight/longer integration
  
### Key Findings
- **Strong soil moisture-LFM correlation** demonstrated (Figure 4)
- **L-band UAS soil moisture maps** validated against in-situ sensors with good agreement even through moderate forest canopy (Figure 9)
- **Multi-species validation**: Chaparral (chamise) and oak species sampled
- **Pilot study evidence**: Critical observation gap in fuel moisture data can be overcome via UAS-based L-band radiometry

### Historical Context
- Original L-band radiometer developed under NASA SBIR (listed as SBIR success story)
- 100+ operational flights across USGS, NOAA, university, and commercial missions
- Recent deployment in NOAA SPLASH campaign for watershed studies

## Notable Details

### Risk Mitigation Strategy
**Risk 1 - Data Quality in Difficult Terrain**
- Mitigation: 4 previous deployments with proven iterative improvements; team capability demonstrated

**Risk 2 - FAA/NASA Multi-UAS Permissions**
- Mitigation: Dr. Stachura's PhD work on cooperative UAS swarms; 100+ FAA COAs issued; lead on NASA flight readiness reviews; step-up approach (2→4→8 UAS/year) to establish precedent

**Risk 3 - Utility for Fire Management**
- Mitigation: Pepperwood as team member providing real-time feedback; CalFire connections for broader community relevance; data format/quality/resolution co-developed with users

### Team Composition & Expertise
- **Jack Elston (BST, PI)**: UAS chief designer; involved since 2013 with soil moisture radiometer; leads flight campaigns and onboard algorithm integration
- **Maciej Stachura (BST, Co-I)**: Multi-aircraft UAS design, FAA/NASA flight certification expert
- **Seungbum Kim (JPL, Co-I)**: 15-year microwave radiometry/radar specialist; SMAP/NISAR algorithm lead; provides UAVSAR P-band and NISAR processing
- **Michelle Stern (USGS, Science PI)**: Hydrologist; PhD on soil moisture/LFM at multiple scales; leads LFM conversion and validation
- **Ryan Ferrell (Pepperwood, Co-I)**: Research Scientist; leads ground sampling and logistical coordination; primary interface to fire management community
- **Eryan Dai (Orbital Micro Systems, Co-I)**: L-band radiometer design expert; leads data processing pipeline improvements and onboard processing development

### Technology Readiness Levels (Entry → Exit)
- Live fuel moisture mapping: TRL 5 → 6
- L-band radiometer with onboard processing: TRL 4 → 7
- Multi-UAS autonomy: TRL 3 → 7
- P-band UAVSAR soil moisture mapping: TRL 5 → 6
- NISAR soil moisture mapping: TRL 7 → 8
- **Overall system: TRL 3 → 6**

### Program Alignment
Addresses multiple RFP requirements:
1. **Multiple vantage points + coordinated observations**: UAS swarm guided by satellite data
2. **Next-generation platforms**: L-band radiometer on small UAS with improved autonomy
3. **Computational challenges**: Onboard/edge computing for real-time products
4. **Mass/power constraints**: Instrument package <2.2 kg, <50W for small platforms
5. **Pre-fire topic focus**: Soil moisture/hydrology and fuel moisture directly addressed; supports fire risk assessment and prescribed burn planning

### Stakeholder Engagement
- **Primary partner**: Pepperwood Preserve (3,200-acre instrumented site with 40 monitoring stations)
- **Data support**: Strong in-situ validation infrastructure (15-min to hourly soil moisture/temperature to 1m depth or bedrock)
- **End-user integration**: CalFire and local burn boss feedback incorporated into product design and delivery
- **Future scalability**: System designed to expand beyond Pepperwood to broader California/western US fire-prone regions

### Deployment Schedule (9 Total Flight Campaigns)
- **Year 1** (3 campaigns): Retire high-risk items; prove LFM mapping, onsite soil moisture calculation, 2-UAS operations
- **Year 2** (3 campaigns): NISAR integration, 4-UAS operations, terrain-based planning, onboard brightness calculation
- **Year 3** (3 campaigns): Full 8-UAS system (single operator), real-time data delivery, integration with controlled burn operations

### ESTO Reporting & Documentation Requirements
- Project plan and quad chart within 15 days of award
- Quarterly technical reports
- Annual interim (6 months) and full reviews (12 months+)
- Final report at completion
- Annual presentations at Earth Science Technology Forum