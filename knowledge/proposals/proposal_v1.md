# Advancing the Readiness Level of Soil Moisture Sensing from Unmanned Aircraft

## Document Metadata
- **Type:** Research proposal (NOAA funding application)
- **Client/Agency:** NOAA Office of Atmospheric Research (OAR), Water and Air Quality (OWAQ) Program
- **Program/Solicitation:** NOAA-OAR-OWAQ-2019-2005820, "Snowpack and Soil Moisture Observations and Data Assimilation to Improve the National Water Model (NWM)"
- **Date:** Submitted January 2019 (created 2019-01-07; modified 2019-02-13)
- **BST Products/Systems Referenced:** S2 (Super Swift) fixed-wing sUAS, SwiftCore Flight Management System, SwiftPilot autopilot, SwiftStation ground station, SwiftTab user interface, S2-SMM (Soil Moisture Mapping) system
- **Key Personnel:** 
  - Principal Investigator: Dr. Gijs de Boer (NOAA/CIRES)
  - Co-PIs: Dr. Mimi Hughes (NOAA/CIRES), Darren Jackson (NOAA/CIRES)
  - BST Subcontractor: Dr. Jack Elston (BST CEO)
  - Federal Collaborators: Dr. Kelly Mahoney, Dr. Robert Zamora, Dr. Michael Cosh (USDA)

## Executive Summary
This proposal seeks NOAA funding to advance the Readiness Level (RL) of the Black Swift Technologies S2-SMM (Soil Moisture Mapping) system—a small unmanned aircraft system equipped with an L-band radiometer for high-resolution soil moisture sensing. The project will conduct five field deployments to two locations (Russian River Valley, California and southern Arizona) to validate the system against in situ measurements, improve data processing automation, and integrate the S2 platform into NOAA operations. Success will advance the system from RL5 to RL7 and support eventual operational use for the National Water Model.

## Technical Approach

### S2 Platform Integration
The S2-SMM integrates a Lobe Differencing Correlation Radiometer (LDCR)—developed under NASA and University of Colorado funding—into the BST Super Swift fixed-wing electric small UAS. Key technical specifications:
- **Radiometer Sensitivity:** Better than ~1 K for 5 msec integration time, resulting in ~3-5% volumetric soil moisture accuracy at ~15 meter spatial resolution
- **Calibration:** Uses downwelling sky temperature as a reference (unique approach)
- **Integration:** LDCR housed in self-contained nose cone (22" length × 8" diameter)
- **Ancillary Sensors:** Onboard NDVI and thermal infrared imaging for vegetation water content and surface temperature corrections

### Flight Operations and Control
The S2 platform is a fixed-wing, modular, high-endurance autonomous aircraft designed for NASA science missions:
- **Propulsion:** Electric, propeller-driven
- **Flight Ceiling:** 6,000 m AMSL
- **Endurance:** 120 min maximum (90 min nominal)
- **Max Range:** 110 km maximum (92 km nominal)
- **MTOW:** 7.3 kg (MGTOW 9.0 kg)
- **Cruise Speed:** 19.0 m/s
- **Max Stable Wind Speed:** 15 m/s
- **Payload Capacity:** 3.5 kg; 50 W available power
- **Geotagging Accuracy:** <4 m (all directions)
- **Launch/Landing:** Bungee or ramp launch; autonomous belly landing with laser-guided terrain-following system
- **Take-Off/Landing Corridor:** 200 m × 15 m

### Flight Management System (SwiftCore)
The SwiftCore flight management system comprises three integrated components:
- **SwiftPilot™:** Miniaturized autopilot with dual 168 MHz Cortex-M4 CPUs and optional 1 GHz Cortex-A8 payload processor; modular CAN-bus architecture for versatile payload integration
- **SwiftStation™:** Portable tripod-mountable ground station (1.8 kg) with customizable 900 MHz dipole antenna, GPS, and user-specific sensor payload integration
- **SwiftTab™:** Android-based user interface (smartphones/tablets) for flight planning, modification, autonomous operation, real-time telemetry, and intervention

**Avionics Features:**
- Telemetry update rate: 10 Hz
- Data/control via 900 MHz real-time radio
- SD card data storage
- 9600 bps downlink data rate
- Gesture-based controls for harsh field conditions
- Autonomous take-off and landing with advanced landing algorithm
- Real-time terrain following with optional canopy following

### Measurement and Processing Approach
**Field Validation Strategy:**
- Five one-week field deployments across two regions during different seasons (wet, dry, transitional)
- Comparison against NOAA PSD long-term in situ soil moisture networks
- High-resolution spatial surveys using portable FieldScout TDR350 sensors (0.1% VWC resolution, ±3% accuracy)
- Data collection over operationally-useful 1-2 km² areas

**Data Processing Workflow Improvement:**
- Current status: Multiple manual processing steps required
- Proposed: Serialize and optimize processing steps for immediate post-flight automated workflow
- Output format: User-specified files (e.g., NetCDF) with high-resolution user-gridded, terrain-compensated georegistered maps
- Corrections integrated: NDVI vegetation, thermal, and soil type corrections
- Development of Python visualization tool for map perusal and statistical analysis

## Products & Capabilities Described

### S2-SMM (Soil Moisture Mapping System)
**What it is:** A fully integrated sUAS platform combining a L-band Lobe Differencing Correlation Radiometer (LDCR) with the BST Super Swift airframe, designed for high-resolution microwave-based soil moisture remote sensing.

**Proposed use in this context:**
- Advancement of technology readiness level through field validation
- Demonstration in operational NOAA environment
- Evaluation against in situ networks in California and Arizona
- Support for National Water Model initialization and validation

**Key specifications and performance claims:**
- Soil moisture measurement accuracy: 3-5% volumetric
- Spatial resolution: ~15 m kriged to custom user grid
- Measurement time: ~2-hour sorties
- RMS error vs. in situ probes: 3-5% volumetric soil moisture
- Unique capabilities: Cold sky calibration reference, advanced EMI shielding, RFI mitigation via digital correlation processor

**Current Readiness Level:** RL5 (prototype deployed and initial comparisons completed)
**Target Readiness Level:** RL7 (by end of project)

### SwiftCore Flight Management System
**What it is:** Integrated avionics control and command system comprising SwiftPilot, SwiftStation, and SwiftTab, designed for ease of use and accurate flight tracking.

**Proposed use:** Flight planning, autonomous operation, real-time telemetry, intervention capabilities for S2-SMM deployments

**Technical capabilities:**
- Autonomous take-off and landing
- Real-time wind condition adaptation
- Laser altimeter-guided terrain-following operations
- Support for complex science missions and survey applications

### S2 Platform
**What it is:** Fixed-wing, modular, high-endurance electric sUAS designed for NASA science missions including satellite calibration and validation.

**Proposed use:** Primary airframe for soil moisture mapping payload

**Prior mission experience referenced:**
- Soil moisture mapping with radiometer
- 12-band multispectral camera system calibration
- Snow-water equivalent radiometry
- Volcano sampling (active plume operations)
- NOAA wildfire applications
- Atmospheric sampling campaigns (San Luis Valley, Colorado)
- Arctic deployments
- High-altitude operations (up to 6,000 m AMSL)

## Use Cases & Applications

### Primary Use Case: National Water Model Support
- Provide high-resolution (10s of meters) soil moisture measurements over model grid scales (1-10 km²)
- Address gaps in spatial coverage between point in situ measurements (detailed but limited spatial extent) and satellite measurements (broader coverage but coarser resolution)
- Inform sub-grid scale variability questions and representativeness of point measurements
- Enable frequent resampling in regions of interest to evaluate NWM parameterizations across seasonal cycles
- Support identification of model performance issues related to high-impact flooding events

### Research Applications
- Understanding sub-grid scale soil moisture variability and hydrometeorological process impacts
- Evaluation of NWM parameterizations
- Improvement of model initialization and validation data
- Assessment of key physical processes governing model performance

### Operational Applications (Near-Real-Time)
- **Weather and River Forecast Offices:** Regular surveys of soil moisture over flood-prone regions (~2-3 km²)
- **Rapid Response:** Post-storm deployment for high-resolution monitoring of soil moisture changes due to precipitation
- **Decision Support:** Observational confirmation of NWM output in regions of importance, increasing forecast confidence

### Eventual Operational Use (Not in Current Scope)
- Assimilation of high-resolution S2-SMM measurements into the National Water Model (future step)

## Test Sites and Deployment Locations

**California (Russian River Watershed):**
- Four sites in North Central California: Middletown, Redwood Valley East, Lake Sonoma, Potter Valley West
- Region characterization: Large seasonal precipitation cycles, diverse soil types
- Deployment timing: December 2019 (wet season), April 2020 (transitional), July 2020 (dry season)

**Arizona:**
- Two sites near Elgin and Canelo, Arizona
- In situ sensors: Soil moisture/temperature at multiple depths (5, 10, 20, 30, 50, 100 cm), air temperature, relative humidity, precipitation
- Deployment timing: May 2020 (dry), August 2020 (wet season)

**Ground Truth Reference:**
- NOAA Physical Sciences Division long-term in situ soil moisture networks
- Portable FieldScout TDR350 sensors deployed during field campaigns for high-resolution spatial surveys
- Soil characterization via USDA Web Soil Survey and UC Davis SoilWeb interface

## Key Results (Not Yet Available)
This is a proposal for future work with anticipated field deployments beginning December 2019. Results section includes anticipated outcomes and success metrics:

**Anticipated Milestones:**
- Acquisition of final flight approvals (December 2019)
- Successful completion of first field deployment (December 2019)
- Development of transition plan (February 2020)
- Successful completion of additional field deployments (August 2020)
- Presentation of comparison study to scientific community (January 2021)
- Public dissemination of quality-controlled datasets (August 2021)
- Publication of comparison study (August 2021)

**Success Metrics for RL Advancement:**
- **RL5→RL6:** Deployment to range of operational environments (Russian River and Arizona regions), measurements over operationally-useful 1-2 km² areas, quantified via instrument uptime %, flight hours, manual intervention requirements, flights completed under varied weather
- **RL6→RL7:** Automated data processing workflow reducing manual intervention, quantified via time-to-processed-data and labor hours reduction
- **RL7→RL8:** NOAA OMAO AOC declaration of S2 as airworthy NOAA platform, personnel training completion

## Notable Details

### EMI/RFI Mitigation
The proposal emphasizes unique technical approaches:
- Special attention to electromagnetic interference (EMI) shielding integration
- Advanced statistical signal processing for radio frequency interference (RFI) mitigation in digital correlating processor
- These attributes claimed to set S2-SMM apart from other available sUAS soil moisture systems

### Prior Related Research
The team has extensive experience with UAS-based atmospheric and hydrological measurements:
- **miniFlux Project:** Development of sensor suite for turbulent flux measurement from UAS (RL3→RL8 advancement), including Arctic Ocean deployment (October 2018)
- **ERASMUS Project:** Two unmanned aircraft systems deployed to Arctic Alaska for atmospheric/surface measurements; datasets publicly available through DOE ARM archive
- **LAPSE-RATE Campaign:** Multi-team community UAS campaign with 50 platforms, ~1300 flights, ~260 flight hours in six days (July 2018)—characterized as largest U