# Disclosure of Technical Data Assertions - DARPA Albatross

## Document Metadata
- Type: Regulatory compliance form (Technical data disclosure for FAR/DFARS compliance)
- Client/Agency: DARPA
- Program/Solicitation: DARPA Albatross (BAA subcontract RFP from BAE Systems)
- Date: Not explicitly stated (document created/modified 2024-12-10)
- BST Products/Systems Referenced: SwiftCore FMS (SwiftPilot, SwiftTab, SwiftStation), SwiftFlow probe, UAS Simulation Environment, web-based communications/planning tools
- Key Personnel: Dr. Jack Elston (CEO, Black Swift Technologies, LLC)

## Executive Summary
This document is a compliance filing disclosing technical data and intellectual property assertions for a DARPA Albatross program response. BST identifies both noncommercial items (a UAS simulation environment) and commercial items (SwiftCore avionics suite components) that will be delivered under potential government contracts, asserting restrictions based on prior SBIR funding and private development.

## Technical Approach
BST's approach centers on its proprietary SwiftCore Flight Management System, developed with partial private funding and prior NASA SBIR support. The company proposes to leverage existing, mature avionics and control systems rather than developing new solutions from scratch. Commercial items are presented as previously developed components that can be integrated into the proposed effort.

## Products & Capabilities Described

### SwiftCore Flight Management System
**Components:**
- **SwiftPilot Autopilot Controller**
  - Dimensions: 6.7cm × 4.0cm × 1.8cm
  - Weight: 50 grams
  - 9 DOF IMU, 10 Hz GPS, 1kHz altitude update
  - Processor: Gumstix Overo (1 GHz Cortex-A8)
  - Interfaces: CAN, UART, I2C, SPI, USB, Ethernet
  - Provides industry-leading sensor-based autonomous control
  - Capable of fully autonomous flight in harsh conditions
  
- **SwiftTab**
  - Android-based tablet platform
  - Gesture and multi-touch interface
  - Real-time telemetry display
  - Mission planning and control of autopilot, aircraft, and payload functions
  
- **SwiftStation Ground Station**
  - Dimensions: 15cm × 30cm × 35cm
  - Weight: 0.9 kg
  - Tripod-mounted with 900MHz and GPS antennas
  - Switches between multiple data links for connectivity
  - Customizable with multiple radio solutions
  
- **Application-Specific Sensor Integrations**
  - Modular architecture for payload customization

### SwiftFlow™ 3D Wind Probe
- **Type:** Multi-hole probe for wind velocity and atmospheric measurement
- **Specifications:**
  - Weight: 144g (probe) + 37g (GNSS)
  - Size: 0.515m × 0.051m × 0.04m (probe); 0.016m × 0.054m × 0.054m (GNSS)
  - Data frequency: 100 Hz
  - Operating temperature: -20°C to 60°C
  - Input voltage: 5 to 8.4V
  - Data interface: 5V TTL UART (921600 baud)
  
- **Measured Parameters:**
  - Barometric pressure (10-1200 hPa, ±1.5 hPa)
  - Differential pressures (side/center port)
  - Air temperature (-40 to 85°C, ±0.3°C)
  - Relative humidity (0-100%, ±3%)
  - Rotation rates, accelerations, magnetic field (3-axis)
  - Wind velocity, airspeed, altitude, angle-of-attack, side-slip
  - GPS position (±2.5m horizontal/vertical) and velocity (±0.05 m/s)
  
- **Design:** Integrated 3D multi-hole probe with magnetometer and IMU; designed specifically for UAS deployments and operation in precipitation

### UAS Simulation Environment
- Ingests NCAR weather data
- Simulates UAS flight for testing soaring algorithms
- Developed under NASA SBIR with open-source software
- Proposed as noncommercial item with SBIR data restrictions

### Web-Based Communications & Planning Tools
- Terrain and wind-aware mission planning
- Previously developed with partial private funding

## Intellectual Property Assertions

### Noncommercial Items (Asserted as SBIR Data)
- **UAS Simulation Environment with Weather Server**
  - Asserted Rights: SBIR Data
  - Basis: Developed under NASA SBIR, utilizing open-sourced software
  - Person Asserting: Dr. Jack Elston, CEO

### Commercial Items (Asserted as SBIR Data with Prior Private Development)
All of the following are asserted with restrictions based on prior development outside this contract:

1. **SwiftPilot Autopilot with 3D wind sensing and atmospheric sensing**
   - Asserted Rights: Rights in SBIR data
   - Basis: Developed prior to project; developed partially at private expense
   
2. **SwiftStation Control Station for SwiftPilot**
   - Asserted Rights: Rights in SBIR data
   - Basis: Developed prior to project; developed partially at private expense
   
3. **SwiftTab UI for controlling UAS with SwiftPilot**
   - Asserted Rights: Rights in SBIR data
   - Basis: Developed prior to project; developed partially at private expense
   
4. **SwiftFlow 5-hole probe for 3D wind measurement in precipitation**
   - Asserted Rights: Rights in SBIR data
   - Basis: Developed prior to project; developed partially at private expense
   
5. **Web-based communications, terrain and wind-aware planning**
   - Asserted Rights: Rights in SBIR data
   - Basis: Developed prior to project; developed partially at private expense

## Use Cases & Applications
The document references SwiftCore usage by:
- **Federal Agencies:** NASA, NOAA, USGS for scientific research in demanding environments (Greenland, tropical volcano operations)
- **Commercial Applications:** Soil moisture measurement, trace gas detection for agriculture and oil & gas industries
- **Requirements Met:** Airworthiness and security requirements for government agencies

## Operational Characteristics Noted
- Designed for remote operations in austere environments
- Minimal training required due to intuitive gesture-based controls
- Capable of handling topographically diverse geography
- Distributed avionics architecture enabling redundancy, field maintenance, automated part lifetime tracking, and expandability
- Interoperable with standard protocols while offering superior performance to Dronecode alternatives in certain estimation and control schemes
- Quote: "I have not come across an autopilot that can handle fixed-wing aircraft as well as Black Swift." — Daniel Hesselius, Director of Flight Operations, University of Colorado, Boulder

## Notable Details
- BST develops proprietary avionics, control systems, payload interfaces, payloads, aircraft designs, user interfaces, and ground stations in-house
- SwiftCore is described as "one of the very few distributed avionics systems"
- The company uses "tightly integrated" 3D multi-hole probe technology with fusion algorithms for wind vector solutions
- All commercial components are asserted as previously developed (prior to this project) with partial private funding, thus retaining restrictions under SBIR data rights provisions
- Government rights progression: Commercial items initially restricted under SBIR data rights; GPR (Government Purpose Rights) restrictions typically limited to 5-year periods per DFARS 252.227-7013/7014