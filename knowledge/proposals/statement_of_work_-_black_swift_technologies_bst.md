# Statement of Work - Black Swift Technologies (BST)
## Improving NOAA Forecasts by Advancing the Capabilities of UAS to Sample Tropical Cyclones from the Ocean Surface to the Stratosphere

## Document Metadata
- **Type:** Statement of Work (SOW) / Project Proposal
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration) - Office of Marine and Aviation Operations (OMAO)
- **Program/Solicitation:** NOAA-OMAO funding proposal
- **Date:** Created May 15, 2025; Modified May 16, 2025
- **Status:** Pending
- **BST Products/Systems Referenced:** S0 (small uncrewed aircraft system, 1.58 kg)
- **Key Personnel:** Beck Cotter (last editor)

## Executive Summary
Black Swift Technologies proposes to advance its S0 small uncrewed aircraft system (sUAS) toward operational readiness (Readiness Level 9) for routine deployment from NOAA's WP-3D (P-3) aircraft to sample tropical cyclones from the planetary boundary layer to the stratosphere. The project will implement hardware/payload improvements, optimize operational efficiency, enhance meteorological instrumentation, and support hurricane field deployments to enable NOAA forecasters and operational centers to access critical in-storm measurements from regions too dangerous for crewed aircraft.

## Technical Approach

### Hardware and Payload Improvements
- Implement moving baseline RTK GPS for improved heading accuracy, GPS velocities, and positions for more reliable wind data
- Develop data buffering and re-transmission capability for periods of lost P-3 communication
- Configure downward-pointing laser altitude sensor for optimal performance in rain conditions to measure sea surface characteristics in eyewall and rainband regions
- Install onboard video system for real-time imagery and recording

### Operational Efficiency Optimization
- Customize firmware, communications, and user interface to increase S0 autonomy, reducing need for dedicated Black Swift pilot onboard P-3
- Enhance battery endurance by potentially up to 30 additional minutes
- Implement manufacturability improvements to reduce cost and increase reliability
- Modify S0 and deployment system for external launch via Cartridge Actuated Device (CAD), eliminating need for P-3 depressurization
- Update data reporting to airOPS with fields: laser altitude, radio signal quality, time since last communication
- Develop USB-based firmware update system integrated into launch tube interface
- Create automated quality-control software for real-time netCDF data file generation

### Meteorological Instrument Enhancement
- Conduct wind tunnel testing to characterize and correct for wing effects on multi-hole pressure probe wind measurements
- Ensure meteorological data reporting at minimum 10 Hz frequency
- Implement laser-altitude-based flight control to maintain consistent altitude above sea surface, especially below 50m

### Project Coordination and Deployment
- Coordinate with NOAA contractors (including Skyfora)
- Complete sensor calibration missions
- Participate in hurricane field deployments
- Enable real-time data delivery to NOAA operational centers (NHC, EMC)
- Support AWIPS II near-real-time visualization and AirOPS situational awareness updates
- Provide post-analysis support including flux calculations

## Products & Capabilities Described

### BST S0 sUAS
- **What it is:** Small uncrewed aircraft system weighing 1.58 kg (~3 pounds), designed for deployment from manned aircraft (P-3) into tropical cyclones
- **Current status:** Previously successfully deployed in Hurricanes Tammy (2023), Ernesto, Francine, Helene, and Milton (2024)
- **Proposed improvements:** Moving baseline RTK GPS, data buffering/re-transmission, rain-capable laser altimeter, onboard video, extended-endurance battery, CAD launch compatibility, increased autonomy via firmware/UI updates, laser-altitude-based flight control
- **Key specifications:**
  - Meteorological data reporting: minimum 10 Hz
  - Altitude control capability: can maintain consistent height via laser readings, particularly below 50m
  - Communication: two-way radio link to P-3 in real-time
  - Deployment: From P-3 aircraft; proposed CAD external launch compatibility
  - Endurance: Current endurance to be extended by up to 30 minutes

### Data Systems and Integration
- Real-time data streaming to NOAA operational centers (EMC and NHC)
- Automated quality-control and netCDF data file generation
- Integration with P-3's airOPS situational awareness software
- Integration with AWIPS II forecasting system
- USB firmware update capability via launch tube interface

## Use Cases & Applications

### Primary Mission
- **Tropical Cyclone Sampling:** Routine deployment into hurricanes to sample critical low-level measurements (planetary boundary layer / PBL) region
- **High-Risk Region Access:** Collect data from regions too dangerous for crewed aircraft, specifically:
  - Eyewall regions
  - Rainband areas
  - Low-level turbulence zones
  - Sea surface characteristics in heavy precipitation

### Operational Integration
- Support NOAA forecast operations during hurricane season
- Provide real-time data to forecasters, emergency managers, and operational modeling centers
- Enable improved tropical cyclone forecasting and prediction models

## Key Results
Not applicable—this is a prospective SOW describing planned work rather than a report of completed results.

## Notable Details

### Operational Context
- NOAA has been developing S0 deployment from WP-3D (P-3) aircraft since 2018
- Project goal is to transition S0 from experimental/developmental to **routine operational status (Readiness Level 9)**
- Recent successful deployments establish proven capability in real hurricanes

### Key Capability Advances
- **Autonomy:** Proposed autonomy enhancements would allow P-3 flight pattern adaptation without dedicated BST pilot onboard, reducing crew burden
- **Data Access:** Real-time data streaming to operational centers (NHC, EMC) represents critical advancement for operational forecasting integration
- **Manufacturability:** Cost reduction and reliability improvements suggest pathway to sustained operational deployment
- **Deployment Method:** CAD external launch eliminates need for cabin depressurization, simplifying operational procedures for AVAPS operator

### Contractor Coordination
- Partnership with Skyfora for UxS-related tasks and services
- Integration with existing NOAA systems: airOPS, AWIPS II, NHC/EMC data systems

### Wind Measurement Validation
- Wind tunnel testing specifically designed to characterize and correct for aerodynamic effects of S0 wing on multi-hole pressure probe, ensuring accuracy in high-wind tropical cyclone conditions