# Autonomous Wildfire Detection and Monitoring System

## Document Metadata
- **Type:** NOAA SBIR Phase I Technical Narrative (Proposal)
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration)
- **Program/Solicitation:** NOAA-OAR-TPO-2025-0001, Topic 9.1 (Extreme Events and Cascading Hazards)
- **Date:** January 3, 2025 (submitted)
- **Proposed Duration:** 6 months
- **Requested Amount:** $189,460
- **BST Products/Systems Referenced:** S3 UAS, NightFOX payload
- **Key Personnel:** 
  - Dr. Maciej Stachura (Principal Investigator, CTO)
  - Dr. Jack Elston (CEO)
  - Dr. Kyle Hilburn (Data integration expert, CIRA partnership)
  - Dr. Troy Thornberry (NightFOX payload expertise)
  - Joey Taylor (NOAA payload team member)
  - Beck Cotter (Proposal Specialist/Project Manager)

## Executive Summary
Black Swift Technologies proposes to develop an autonomous uncrewed aircraft system (UAS) for real-time wildfire detection and management by enhancing the S3 UAS platform with advanced sensors and software for persistent monitoring of fire perimeters, hotspot detection, and integration with wildfire prediction models (WRF-SFIRE) and operational tools (WFTAK). Phase I focuses on UAS optimization for extreme conditions, sensor integration, data pipeline development, and experimental planning to prepare for Phase II demonstrations.

## Technical Approach

### Primary Challenge Addressed
Current wildfire detection methods fall short due to:
- **Satellite systems (MODIS/VIIRS):** Low resolution, long revisit times (24+ hours), miss early-stage fires
- **Ground-based systems (ALERTWildfire):** Line-of-sight limitations, extensive infrastructure requirements, unsuitable for remote areas
- **Commercial UAS platforms:** Short flight durations, limited payload capacity

### Core Solution: S3 UAS Platform
The S3 UAS is a vertical takeoff and landing (VTOL) platform with:
- **Twin-motor setup** for enhanced speed and maneuverability
- **Extended flight endurance** optimized for complex terrain and wildfire conditions
- **Robust navigation** for stable flight in high winds (80+ knots) and complex terrain
- **Advanced sensor integration** including the NightFOX multi-spectral, infrared, and thermal imaging payload

### Phase I Technical Objectives

**1. S3 UAS Optimization**
- Enhance propulsion system for longer endurance
- Integrate advanced navigation algorithms for stability in high winds and complex terrain
- Stress testing for environmental resilience (target: 80 kt winds, 50°C temperatures)
- Validation through programmable digital load testing and software-in-the-loop simulations

**2. Real-Time Data Integration with WRF-SFIRE**
- Design data pipelines to feed UAS-derived fire data into the WRF-SFIRE two-way coupled fire-atmosphere prediction model
- Develop preprocessing algorithms for multi-spectral and thermal data
- Achieve near-real-time data ingestion compatible with model input requirements
- Use archived NightFOX data during Phase I for preliminary model testing

**3. WFTAK (Wildland Fire Team Awareness Kit) Integration**
- Create software interface for real-time transmission of fire perimeter and hotspot data
- Deliver actionable insights to first responders and wildfire management teams
- Design software architecture and establish stakeholder requirements through consultation

**4. Demonstration Planning & Validation**
- Plan flight scenarios for Phase II field testing
- Secure permissions from stakeholders (Colorado Center of Excellence for Advanced Technology Aerial Firefighting)
- Design experimental protocols to assess UAS data impact on model accuracy
- Phase I focuses on planning; direct flight testing is out of scope

**5. Quantifying Model Improvement**
- Design experiments to evaluate impact of UAS-derived data on fire behavior, intensity, and spread predictions
- Develop validation metrics for forecast accuracy improvements

### Key Technical Questions to Answer
- What data quantity, format, and rate is necessary for running operational wildfire models?
- What changes must be implemented to the S3 UAS for mission success with minimal operator oversight?
- What quantitative improvement in forecasting can be expected from high-resolution UAS hotspots and fire-perimeter measurements?

## Products & Capabilities Described

### S3 UAS
**What it is:**
- Advanced VTOL uncrewed aircraft system designed for extreme environmental monitoring
- Twin-motor configuration for enhanced maneuverability and speed
- Optimized for extended endurance missions in harsh conditions

**Proposed use in this project:**
- Primary platform for autonomous wildfire detection and real-time data collection
- Equipped with high-resolution multi-spectral and thermal imaging
- Deployed for fire perimeter mapping, hotspot detection, and atmospheric data collection
- Designed to operate in high-wind, high-temperature environments typical of wildfires

**Specifications/Performance Claims:**
- Capable of operating in 80+ knot winds (stressed design condition)
- Can withstand temperatures up to 50°C
- Extended flight endurance (specific duration not provided in Phase I proposal)
- VTOL capability enabling rapid deployment without runway requirements
- Compatible with NOAA NightFOX payload

### NightFOX Payload
**What it is:**
- NOAA-developed advanced remote sensing system featuring multi-spectral, infrared, and thermal imaging
- Originally developed during the FIREX-AQ (Fire Influence on Regional to Global Environments and Air Quality) campaign
- Provides high-resolution fire radiative power measurements and fire characterization data

**Proposed use:**
- Primary sensor suite for the S3 UAS wildfire system
- Delivers high-fidelity data for fire detection, perimeter mapping, and fire behavior analysis
- Data feeds into WRF-SFIRE model and WFTAK operational tools

**Capabilities:**
- Multi-spectral imaging for fire detection and characterization
- Thermal imaging for hotspot and fire radiative power measurement
- Superior resolution compared to satellite systems (VIIRS comparison shown: NightFOX delivers ~10x finer spatial detail)
- Previously deployed from NOAA Twin Otter aircraft; now being adapted for UAS integration

**Historical context:**
- First wildfire flight in 2019 over controlled burn in partnership with Boulder County
- Successfully demonstrated in FIREX-AQ campaign for fire monitoring applications
- Proven capability to detect ignition points and monitor fire dynamics with high accuracy

## Use Cases & Applications

### Primary Use Case: Wildfire Management Operations
- **Real-time fire perimeter tracking** for incident command teams
- **Hotspot identification** for targeting suppression resources
- **Data-driven decision support** for evacuation and containment strategies
- **Integration with operational tools** (WFTAK) for first responder situational awareness

### Wildfire Model Enhancement
- **Input for WRF-SFIRE model:** High-resolution UAS data improves fire behavior prediction accuracy
- **Data-sparse region monitoring:** Critical capability in remote or complex terrain where other systems fail
- **Wind field characterization:** UAS data improves low-level wind predictions critical to fire spread modeling

### Secondary/Future Applications Mentioned
- **Advanced Air Mobility (AAM)** in mountainous areas and urban corridors
- **NASA Earth Science programs** (3D-Winds mission)
- **Environmental observation and weather forecasting**
- **Cooperative control/teaming and BVLOS (Beyond Visual Line of Sight) operations**

### Specific Mission Context
- Recent Los Angeles wildfires highlighted critical need: grounded air traffic due to high winds and safety concerns created gaps in observational capabilities
- Proposal explicitly targets improvement of situational awareness during extreme fire events

## Key Results (N/A - Phase I Proposal)
This is a Phase I proposal; no results are available. However, the document specifies anticipated Phase I deliverables:

**Month 3 Milestones:**
- Completed validated design simulations and algorithm testing for UAS platform

**Month 4 Milestones:**
- Sensor calibration and successful data transmission testing

**Month 6 Milestones:**
- Functional data pipeline prototype for WRF-SFIRE integration
- Validation plan for Phase II demonstrations
- Secured permissions from stakeholders
- Completed demonstration protocols
- WFTAK interface prototype
- Draft training materials for first responders

**Phase II Expected Results (mentioned):**
- Live flight demonstrations with integrated system
- Quantitative validation of forecast improvements
- Operational deployment readiness
- Commercial path identified and partnerships established

## Notable Details

### Market Opportunity
- Global wildfire detection technology market: **$2.72 billion in 2024**
- Projected CAGR: **10.4% from 2025-2034**
- Primary markets: Government agencies (USDA, USFS), forestry services, utility companies, insurance firms, rural communities

### Competitive Advantages
The S3 UAS combines strengths of competing solutions while addressing their limitations:
- **vs. Satellites (Planet Labs, ICEYE):** Higher resolution, real-time delivery vs. broad but coarse coverage
- **vs. Ground networks (ALERTWildfire):** No line-of-sight limitations, accessible to remote areas vs. fixed infrastructure
- **vs. Commercial UAS (DJI):** Extended endurance, sophisticated sensors, operational integration vs. short flight duration

### Stakeholder Partnerships
- **Colorado Center of Excellence for Advanced Technology Aerial Firefighting:** Letter of support attached; provides access to firefighting expertise and potential demonstration sites
- **USGS:** Previous partnership on live-fuel moisture mapping work
- **Boulder County:** Provides testing sites and open space; hosted first NightFOX flight in 2019
- **CIRA (Cooperative Institute for Research in the Atmosphere):** Subcontract for Dr. Kyle Hilburn's expertise in data integration and WRF-SFIRE modeling
- **NOAA:** No-cost partnership providing access to wildfire expertise and NightFOX sensor suite

### Facilities
- **BST Boulder Headquarters:** State-of-the-art facility with dedicated UAS integration lab, sensor calibration workspaces, software/hardware resources for real-time data processing
- Access to diverse testing environments in Colorado (complex terrain, varied weather conditions)

### Technical Risk Mitigation Strategy
**Three main risks identified with mitigation plans:**

1. **Integration Challenges (UAS + Payload)**
   - Mitigation: Iterative integration testing, bench tests for power compatibility, vibration-isolated mounts, structural testing

2. **Data Pipeline Compatibility with WRF-SFIRE**
   - Mitigation: Design/prototype pipeline using archived datasets, NOAA feedback loops, track latency and format accuracy metrics

3. **Stakeholder Coordination for Demonstrations**
   - Mitigation: Early engagement with stakeholders, detailed demonstration plans, regular updates and collaborative meetings

### Personnel Qualifications

**Dr. Maciej Stachura (PI/CTO):**
- Expert in control systems and environmental sensing
- Published work on volcanic monitoring UAS design and communication-aware information gathering
- Leading propulsion system analysis and sensor calibration efforts

**Dr. Jack Elston (CEO):**
- Background in UAS development and atmospheric research
- Published work on hurricane measurement systems and energy-efficient UAS flight planning
- Overall project strategy and NOAA coordination

**Dr. Kyle Hilburn:**
- Expert in remote sensing, data assimilation, and predictive environmental modeling
- Extensive experience integrating multi-sensor data into weather and fire models
- Leading real-time data pipeline development for WRF-SFIRE

**Dr. Troy Thornberry:**
- Principal Investigator of original NOAA NightFOX project
- Expert in instrument hardware, data reduction, mission planning
- Experience with interagency coordination for small UAS wildfire deployment

### Alignment with NOAA Initiatives
- **Fire Weather Testbed:** Project supports NOAA's advanced sensing and predictive technology initiatives
- **FIREX-AQ Campaign:** Builds directly on FIREX-AQ insights about multi-spectral sensing effectiveness
- **Weather-Ready Nation Program:** Supports NOAA's mission to build resilience against natural disasters

### Commercialization Strategy (Phase II/III)
- Direct sales to government agencies and forestry services
- Service contracts for ongoing wildfire monitoring operations
- Data subscription models for real-time fire information feeds
- Leverage existing partnerships and distribution channels

---

## Summary
This NOAA SBIR Phase I proposal demonstrates Black Swift Technologies' comprehensive approach to closing critical gaps in wildfire detection and response. By integrating the proven NightFOX sensor payload with the advanced S3 UAS platform, coupled with real-time data pipelines into operational models