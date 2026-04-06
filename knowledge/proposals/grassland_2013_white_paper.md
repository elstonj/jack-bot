# 2013 Grassland Testing Avionics Package

## Document Metadata
- Type: White paper / technical proposal
- Client/Agency: Internal BST project
- Program/Solicitation: 2013 Grassland Campaign
- Date: May 2-3, 2013
- BST Products/Systems Referenced: SwiftPilot, Robovero board, Overo flight computer, Tempest
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This white paper proposes construction of a comprehensive avionics data logging and sensor integration system for the 2013 Grassland campaign to enable accurate wind measurements and state estimation studies. The system will interface multiple sensors (multi-hole probe, MIST sonde, autopilots, pressure sensors, magnetometers) through a central Robovero platform and log synchronized data for future algorithm development.

## Technical Approach
- **Sensor Integration Hub**: Robovero board outfitted with custom firmware to serve as central interface for multi-hole probe, MIST sonde, and autopilot data
- **Data Logging**: Overo-based flight computer polls Robovero for sensor readings, records data with system timestamps to onboard SD card for post-flight analysis
- **Sensor Networks**: 
  - Tempest equipped with pressure sensor array to investigate wind direction sensing without dedicated probe
  - Magnetometer network to investigate state estimation improvement and analyze aircraft-induced magnetic field effects
- **Autopilot Comparison**: Installation of SwiftPilot alongside Piccolo autopilot to compare state estimation algorithms, sensor suites, and wind measurements

## Products & Capabilities Described

**SwiftPilot**
- BST-developed autopilot system
- Proposed use: Side-by-side comparison with Piccolo autopilot for state estimation accuracy
- Enables comparison of raw sensor measurements between autopilot systems

**Robovero Board**
- Sensor interface/logging platform
- Custom firmware development for synchronized multi-sensor data acquisition
- Maintains centralized sensor measurement coordination

**Overo Flight Computer**
- Flight control and data logging processor
- Polls Robovero platform for sensor readings
- Logs timestamped data to SD card storage

**Tempest Platform**
- Aircraft equipped with pressure sensor array
- Experimental platform for alternative wind direction sensing investigation

## Use Cases & Applications
- **Wind Measurement Accuracy**: Development of improved state estimation algorithms to compensate for small UAS sensor limitations (drift, bias)
- **Meteorological In Situ Measurements**: Data collection to inform design of future atmospheric measurement systems
- **VORTEX2 Validation**: Comparison of Piccolo wind estimates with multi-hole probe measurements to validate wind data quality from previous VORTEX2 campaign
- **Sensor Fusion Research**: Investigation of magnetometer integration for improved state estimation

## Notable Details
- **Problem Statement**: Small UAS face inherent trade-offs between weight, payload size, cost, and sensor accuracy; this project generates data to develop algorithmic compensation
- **Data Availability**: Collected dataset intended for future research and algorithm development by broader team
- **Multi-Platform Approach**: Synchronization of data from multiple sensor types and autopilot systems enables comparative analysis
- **Hardware Integration**: Custom firmware development on Robovero required; interface board possibly needed for expanded sensor count
- **Real-time Guarantees**: Emphasis on maintaining real-time data acquisition guarantees despite multiple sensor streams