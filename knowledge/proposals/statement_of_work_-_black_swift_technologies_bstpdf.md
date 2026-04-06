# Statement of Work - Black Swift Technologies (BST): Improving NOAA Forecasts by Advancing UAS Capabilities for Tropical Cyclone Sampling

## Document Metadata
- **Type:** Statement of Work (SOW) / Proposal
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration), specifically NOAA-OMAO (Office of Marine and Aviation Operations)
- **Program/Solicitation:** NOAA funding (pending approval as of document date)
- **Date:** 2025-05-22 (submission/creation date)
- **BST Products/Systems Referenced:** S0 (small Uncrewed Aircraft System)
- **Key Personnel:** Beck Cotter (last editor)

## Executive Summary
Black Swift Technologies proposes to advance the S0 small uncrewed aircraft system toward operational readiness (Readiness Level 9) for routine deployment from NOAA's WP-3D (P-3) aircraft to collect critical meteorological measurements in tropical cyclones, particularly in the planetary boundary layer that is too dangerous for crewed operations. The project focuses on hardware improvements, operational optimization, instrument enhancements, and field deployment support to enable real-time data delivery to NOAA operational forecast centers during hurricane missions.

## Technical Approach

### Hardware & Payload Improvements
- **Moving baseline RTK GPS:** Implementation for improved heading accuracy, GPS velocities, and position measurements to enable more reliable wind data
- **Data buffering/re-transmission capability:** System to buffer and re-transmit data recorded during communication loss with the P-3
- **Rain-optimized laser altimeter:** Configuration of downward-pointing laser altitude sensor for operation in heavy precipitation (eyewall, rainbands)
- **Onboard video system:** Real-time imaging and recording of environmental conditions

### Operational Efficiency Optimization
- **Increased autonomy:** Firmware, communications, and user interface customization to enable P-3 crew flight pattern adaptation without onboard BST pilot
- **Extended battery endurance:** Potential 30-minute additional flight time through battery improvements
- **Manufacturability improvements:** Cost reduction and reliability enhancements
- **Cartridge Actuated Device (CAD) launch compatibility:** External launch capability eliminating P-3 depressurization requirement
- **Data reporting enhancements:** Integration of laser altitude, radio signal quality, and communication status into P-3's airOPS situational awareness software
- **USB firmware update system:** In-launch-tube firmware updates without aircraft removal
- **Automated data quality control:** Real-time quality-controlled netCDF file generation

### Meteorological Instrument Enhancement
- **Wind tunnel testing:** Characterization of S0 wing effects on multi-hole pressure probe wind measurements for accurate high-wind data
- **10 Hz reporting frequency:** Minimum data reporting rate for wind and meteorological variables
- **Laser-based altitude maintenance:** Autonomous flight capability to maintain consistent height above sea surface, particularly below 50m

## Products & Capabilities Described

### BST S0 Small Uncrewed Aircraft System
**What it is:**
- 1.58 kg (~3 pound) sUAS designed for deployment from NOAA P-3 aircraft
- Equipped with multi-hole pressure probe for wind measurement and laser altimeter
- Capable of operating in extreme weather conditions

**Current Use & Deployment History:**
- Deployed from P-3 to sample turbulence in planetary boundary layer (PBL) during tropical cyclones
- Successfully deployed in Hurricanes Tammy (2023), Ernesto, Francine, Helene, and Milton (2024)
- NOAA has been working toward TC deployment since 2018

**Proposed Improvements in This Project:**
- Integration with moving baseline RTK GPS
- Data buffering during communication gaps
- Rain-capable laser altimeter
- Onboard video
- Extended battery (up to 30 additional minutes)
- CAD launch compatibility
- Enhanced autonomy for crew operations
- Laser-based altitude hold functionality
- 10 Hz meteorological data reporting

**Performance Specifications:**
- Wind measurement capability requiring wing-effect characterization
- Multi-hole pressure probe sensor suite
- Two-way radio communication with P-3
- Real-time data transmission capability

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Sampling
- **Application:** Collection of critical meteorological measurements in hurricanes/tropical cyclones from ocean surface to stratosphere
- **Specific Focus:** Planetary boundary layer (PBL) sampling—the low-level region too dangerous for crewed aircraft
- **Data Utilization:** Support for NOAA forecasters, emergency managers, and operational modeling centers
- **Operational Centers Served:** National Hurricane Center (NHC), Environmental Modeling Center (EMC)

### Environmental Targets
- Eyewall sampling (heavy precipitation)
- Rainband sampling
- Sea surface characteristics observation in extreme weather
- Turbulence characterization in critical low-level regions

### Previous Operational Deployments
- Hurricane Tammy (2023)
- Hurricanes Ernesto, Francine, Helene, Milton (2024)

## Key Operational Requirements Addressed

### Real-Time Data Integration
- Real-time data streaming to P-3 via two-way radio
- Real-time data delivery to NOAA operational forecast centers (EMC, NHC)
- Near-real-time visualization via AWIPS II
- Real-time situational awareness updates on P-3 via airOPS

### Data Quality & Format
- Automated quality control processing
- Real-time netCDF file generation
- Post-analysis support including flux calculations
- Standardized data reporting fields

### Operational Crew Integration
- Simplified deployment (CAD launch eliminates depressurization)
- AVAPS operator integration
- Reduced pilot workload through increased autonomy
- Compatible with existing P-3 operational workflows

## Deliverables

**Hardware:**
- Improved S0 sUAS with integrated RTK GPS, data buffering, rain-capable laser altimeter, onboard video, extended endurance battery, manufacturability improvements, and CAD launch compatibility

**Software & Firmware:**
- Updated firmware and communication protocols supporting increased autonomy
- Firmware user interface documentation
- USB firmware update system (integrated into launch tube)
- Automated software for real-time quality control and netCDF data file generation
- Wind tunnel testing documentation

**Operational Capabilities:**
- S0 platforms reporting meteorological data at minimum 10 Hz
- Platforms capable of laser-based altitude maintenance
- Real-time data streams to NOAA operational centers
- Integration with airOPS situational awareness tool

**Field Support:**
- Successful deployment and operation during designated field missions
- Technical support throughout project period
- Platform integration, testing, deployment, and data verification assistance

**Program Advancement:**
- Contribution to S0 achievement of Readiness Level 9 (operational status)

## Notable Details

### Strategic Partnerships
- Coordination with NOAA contractors including Skyfora for UxS-related tasks
- Integration with NOAA P-3 aircraft operations and crew workflows

### Key Competitive Advantages
- Only platform proven to operate reliably in tropical cyclone conditions (successful deployments in five hurricanes)
- Ultra-lightweight design (1.58 kg) allows deployment from existing operational aircraft without modification
- Capability to access planetary boundary layer inaccessible to crewed aircraft

### Operational Readiness Goals
- Progression toward Readiness Level 9 (full operational deployment)
- Evolution from experimental/developmental status to routine operational use
- Integration into standard NOAA hurricane reconnaissance operations

### Technical Challenges Being Addressed
- Wind measurement accuracy in extreme conditions (wing effect characterization through wind tunnel testing)
- Communication reliability in high-interference environments (data buffering during dropouts)
- Accurate sea surface measurement in heavy precipitation (rain-optimized laser altimeter)
- Operational complexity reduction (CAD launch, increased autonomy, automated QC)