# Statement of Work - Black Swift Technologies: Improving NOAA Forecasts by Advancing UAS Capabilities for Tropical Cyclone Sampling

## Document Metadata
- **Type:** Statement of Work (SOW) / Project Proposal
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration) - Office of Marine and Aviation Operations (OMAO)
- **Program/Solicitation:** NOAA-OMAO funding proposal (pending)
- **Date:** Submitted May 16, 2025
- **BST Products/Systems Referenced:** S0 (small UAS)
- **Key Personnel:** Beck Cotter (last editor)

## Executive Summary
Black Swift Technologies proposes to advance the S0 small uncrewed aircraft system (sUAS) toward operational readiness (Readiness Level 9) for routine deployment from NOAA's WP-3D hurricane research aircraft to sample tropical cyclones. The project focuses on hardware improvements, operational efficiency enhancements, meteorological instrument upgrades, and field deployment support to enable the S0 to collect critical low-level wind and atmospheric data from the planetary boundary layer—regions too dangerous for crewed aircraft. The S0 has already been successfully deployed in five hurricanes (Tammy 2023; Ernesto, Francine, Helene, Milton 2024) and this effort aims to mature the platform for routine operational use by NOAA forecasters and modeling centers.

## Technical Approach

### Hardware and Payload Improvements
- **Moving Baseline RTK GPS:** Implement for improved heading accuracy, GPS velocities, and positions to provide more reliable wind data
- **Data Buffering/Re-transmission:** Develop capability for S0 to buffer and re-transmit data during periods of lost communication with the P-3
- **Rain-capable Laser Altimeter:** Configure downward-pointing laser altitude sensor for optimal operation in heavy precipitation (eyewall, rainbands) to accurately observe sea surface characteristics
- **Onboard Video System:** Install for real-time image capture and recording of environmental conditions during missions

### Operational Efficiency Optimization
- **Increased Autonomy:** Customize firmware, communications, and user interface to enable P-3 crew to adapt S0 flight patterns without requiring a dedicated Black Swift pilot onboard
- **Extended Endurance:** Improve battery to potentially add up to 30 additional minutes of flight time
- **Manufacturability Improvements:** Reduce cost and increase platform reliability
- **Cartridge Actuated Device (CAD) Launch:** Modify S0 and deployment system for external launch, eliminating need for P-3 depressurization and simplifying operations
- **Data Reporting Integration:** Update S0 data output to include laser altitude, radio signal quality, and time since last communication for display on P-3's airOPS situational awareness software
- **Firmware Update System:** Develop USB-based firmware update capability integrated into launch tube, preventing need to remove aircraft for updates
- **Automated Data Quality Control:** Create software to automate quality control of meteorological data files and generate real-time, quality-controlled netCDF data files

### Meteorological Instrument Enhancement
- **Wind Tunnel Testing:** Conduct testing to characterize and account for S0 wing effects on wind measurements from multi-hole pressure probe, ensuring accurate high-wind measurements
- **High-Frequency Data Reporting:** Ensure S0 reports wind and meteorological variables at minimum 10 Hz frequency
- **Laser Altitude-Based Flight:** Implement functionality for S0 to maintain consistent height above sea surface based on laser readings, especially below 50m altitude

## Products & Capabilities Described

### BST S0 sUAS
- **What it is:** A 1.58 kg (~3 pound) small uncrewed aircraft system designed for deployment from crewed aircraft
- **Current use:** Deployed from NOAA's WP-3D (P-3) aircraft to sample turbulence in the planetary boundary layer (PBL) of tropical cyclones—regions too dangerous for crewed aircraft
- **Operational history:** Successfully deployed in Hurricanes Tammy (2023), Ernesto, Francine, Helene, and Milton (2024)
- **Proposed enhancements:** The entire SOW describes improvements to move the S0 to Readiness Level 9 (operational status), including hardware upgrades (RTK GPS, rain-capable laser altimeter, video system), extended battery endurance, increased autonomy, improved wind measurement accuracy via wing characterization and 10 Hz data reporting, and laser-altitude-based flight control
- **Operational integration:** Will transmit real-time data back to P-3 via two-way radio and provide data streams to NOAA operational forecast centers (EMC and NHC) with automated quality control

## Use Cases & Applications

### Primary Application: Tropical Cyclone Sampling
- **Mission:** Collect critical meteorological measurements in tropical cyclones from ocean surface to stratosphere
- **Specific focus:** Sampling turbulence in the planetary boundary layer (PBL) and low-level wind structure
- **Deployment platform:** NOAA's WP-3D hurricane research aircraft
- **End users:** NOAA forecasters, emergency managers, and operational modeling centers (specifically NHC—National Hurricane Center; EMC—Environmental Modeling Center)
- **Operational context:** Enable routine data collection to advance forecast accuracy and support hurricane response operations

### Data Utilization
- Real-time data visualization via AWIPS II
- Situational awareness updates on NOAA P-3 via airOPS
- Post-mission flux calculations and data analysis

## Key Deliverables

1. Improved BST S0 hardware incorporating:
   - Moving baseline RTK GPS
   - Data buffering/re-transmission capability
   - Rain-capable laser altimeter
   - Onboard video system
   - Extended endurance battery
   - Improved manufacturability features
   - CAD launch compatibility

2. Updated firmware, communication protocols, and user interface documentation supporting increased autonomy

3. Functional USB firmware update system integrated into launch tube interface

4. Automated software for real-time quality control and generation of netCDF data files

5. Wind tunnel testing documentation characterizing wing effects on wind measurements

6. S0 platforms configured for 10 Hz minimum meteorological data reporting

7. S0 platforms capable of maintaining altitude based on laser readings

8. Successful deployment and operation during designated field missions

9. Real-time data streams delivered to NOAA operational centers (NHC, EMC)

10. Technical support and expertise throughout project for integration, testing, deployment, and data verification

11. Advancement of S0 toward Readiness Level 9 operational status

## Notable Details

### Operational Integration Requirements
- **Real-time data transmission:** Two-way radio link back to P-3
- **Data dissemination:** Real-time sUAS data to NOAA operational forecast centers
- **Quality control automation:** Real-time generation of quality-controlled netCDF files
- **Situational awareness:** Integration with P-3 airOPS display system including new data fields (laser altitude, radio signal quality, time since last communication)

### Partners and Coordination
- **Skyfora:** NOAA contractor for UxS-related tasks and services
- Coordination with NOAA for sensor calibration missions and field deployment support

### Technical Performance Targets
- Minimum 10 Hz meteorological data frequency
- Altitude maintenance capability below 50m via laser reference
- RTK GPS for improved positioning accuracy and wind calculation
- Data buffering during communication loss periods
- Video documentation capability for environmental observations

### Path to Operational Status
The project explicitly frames its objectives as advancing the S0 from current status toward **Readiness Level 9** (full operational capability), building on five successful hurricane deployments to establish routine operational use by NOAA forecasters and modeling centers.