# DOI RFI Response - Black Swift Technologies

## Document Metadata
- **Type:** Request for Information (RFI) Response
- **Client/Agency:** Department of Interior (DOI)
- **Program/Solicitation:** Notice ID DOIRFBO240032 - "Demonstration of Uncrewed Aircraft Systems (UAS)"
- **Date:** September 6, 2024
- **BST Products/Systems Referenced:** S0 UAS, E2 UAS, S2 UAS, SwiftCore Flight Management System, SwiftTab, SwiftStation, SwiftPilot
- **Key Personnel:** Jack Elston (last editor), Beck Cotter (referenced in comments)

---

## Executive Summary

Black Swift Technologies proposes to demonstrate four core UAS platforms and systems for Department of Interior applications: the S0 (small, economical VTOL/air-deployed), E2 (medium multirotor for inspection and mapping), S2 (specialized fixed-wing for extreme conditions), and SwiftCore Flight Management System (proprietary avionics and control suite). These systems have been proven across NASA, NOAA, USGS, DOD, and USAF contracts, with demonstrated capabilities in wildfire monitoring, hurricane tracking, volcano observation, methane detection, and soil moisture mapping.

---

## Technical Approach

BST's technical approach centers on building complete, vertically-integrated UAS solutions from avionics through aircraft design to payload integration and field operations. Rather than relying on open-source/low-quality components, BST designs and manufactures critical systems in-house, ensuring NDAA and ASDA compliance, supply chain control, and rapid customization to mission needs.

**Core Technical Strategy:**
- **Proprietary SwiftCore FMS** as foundation for all platforms: SwiftPilot autopilot, SwiftTab operator interface, SwiftStation ground station
- **Modular, field-swappable payload architecture** enabling rapid mission adaptation
- **Distributed avionics** (networked nodes on robust bus) enabling redundancy, automated diagnostics, easy field maintenance
- **Sensor-based autonomous control** minimizing operator workload while optimizing sensor data quality
- **Data-centric flight management** with real-time telemetry and precise payload management
- **Advanced machine learning and estimation/control schemes** that outperform Dronecode alternatives, particularly in high-wind environments

---

## Products & Capabilities Described

### **S0 UAS** (Small, Economical VTOL/Air-Deployed)

**Characteristics:**
- **Two configurations:**
  - **S0-VTOL:** 62" wing span, 40" length, 5.2 lbs empty weight, 0.5 lbs payload
    - Max speed 100 kts, cruise 37 kts, endurance 75 min, range 53 miles, max altitude 15,000 ft
    - 3x 1155 kV brushless motors, 148 Wh Li-Ion
  - **S0-AD (Air-Deployed):** 32" wing span, 32.5" length, 2.5 lbs empty weight, 0.25 lbs payload
    - Max speed 60 kts, cruise 46 kts, endurance 110 min, range 97 miles, max altitude 10,000 ft
    - 1x 1950 kV brushless motor, 106.4 Wh Li-Ion

**Key Capabilities:**
- Autonomous flight in extreme atmospheric conditions
- Small size, light weight enable deployment from aircraft, ships, ground vehicles
- Ruggedized for harsh weather (high winds, rain, snow)
- Long endurance enables large area coverage
- Currently approved for NOAA and USAF use

**Applications/Use Cases:**
1. **UAS Swarm for Wind Monitoring (NASA SBIR):** Coordinated multi-UAS operations for improved wildfire forecasting. Two S0s demonstrated in 2023, data provided to National Center for Atmospheric Research for 12-hour forecasts. Goal: 6-UAS team. Data shared via ATAK for wildfire community use.

2. **NOAA Hurricane Tracking:** Air-deployed S0-AD for in-hurricane flights from NOAA P3 hurricane hunter
   - Collects wind, pressure, temperature, video data
   - Up to 2-hour flight times with multiple sensors
   - 20 systems delivered to NOAA for 2024 season; capacity to scale to 100+
   - 2025 contract in development for multi-UAS capability with cooperative path planning

3. **AFWERX SBIR - Advanced Inter-Aircraft Communications:** S0 as low-cost swarming platform
   - Enables cooperative control and hierarchical command/control
   - Air-deployable from C-130 or ground-launched
   - Supports advanced autonomy with reduced operator overhead for large UAS groups

---

### **E2 UAS** (Medium Multirotor)

**Characteristics:**
- 28.276" fuselage, 25 lbs max takeoff weight, 6.5 lbs max payload
- 4x 360 kV motors, 42,000 mAh Li-Ion (6S)
- Flight ceiling 14,000 ft, range 12 miles, flight time 35 min nominal, flight speed 22 mph
- Max winds endured 25 mph
- Forward-mounted payload for full field-of-view
- Proprietary carbon fiber and polyamide 12 construction
- Easily swappable payload and battery systems

**Key Capabilities:**
- Inspection with high-resolution imagery and lidar
- Soil moisture mapping
- Operates in harsh conditions with advanced gimbal systems
- Intuitive control suitable for minimal-training operators

**Applications/Use Cases:**
1. **Wind Turbine Inspections (with Alerion):** Custom payload via open API for high-resolution images, lidar, video of turbine blades; damage/defect identification

2. **Solar Panel Mirror Inspections (with NREL):** High-resolution camera gimbal for heliostat inspection; misalignment and defect detection

3. **Soil Moisture Mapping (USGS, Pepperwood Preserve, NOAA SPLASH):**
   - Three campaigns (May 2022, Aug 2022, May 2023) capturing seasonal variations
   - Equipped with optical, near-infrared, thermal cameras, L-band radiometer
   - Captures 13,000-30,000 images per flight with brightness temperatures converted to volumetric soil moisture
   - Supporting NASA extension into UAS swarm for vastly increased coverage

---

### **S2 UAS** (Specialized Fixed-Wing for Extreme Conditions)

**Characteristics:**
- 120.6" wing span, 73.4" length, 13.5 lbs empty weight, 5 lbs max payload
- 1x 465 kV brushless motor, 302 Wh Li-Ion
- Max speed 48 kts, cruise 37 kts, endurance 90 min, range 63 miles, max altitude 10,000 ft
- Glide ratio 14.3:1, stall speed 23 kts
- Fiberglass and carbon fiber construction
- Modular, field-swappable payload system
- Built with SwiftCore FMS for advanced flight management

**Key Capabilities:**
- Exceptional resilience in extreme conditions (winds >50 kts, icing, precipitation, damaging particulates)
- Long endurance for large-area coverage
- BVLOS operations capability
- Real-time telemetry and precise payload management
- Capable of flying 25+ miles and climbing 7,000 ft altitude in extreme conditions

**Applications/Use Cases:**

1. **Methane/CO2 Emission Detection:**
   - Advanced laser spectrometer sensor for detecting methane leaks in oil/gas infrastructure
   - Responds to regulatory scrutiny and environmental concerns
   - Advantages over traditional detection methods

2. **Trace Gas Observations (Cal Tech, JPL, Costa Rica):**
   - E2 and S2 adapted for precipitation survivability
   - High-altitude flights on Turralbá and Rincón Viejo volcanoes
   - CO2 concentration measurements over hidden vents

3. **Soil Moisture & Soil Integrity Mapping:**
   - Same payload as E2 but with longer flight time and faster ground speed for large areas
   - Agricultural fields, watersheds
   - **AFRL AFWERX Phase II SBIR:** Mapping soil integrity for C-130 operations on dirt runways
   - TRL 9: Operated with USGS, NOAA, NASA for field campaigns

4. **Wildfire Observations (NOAA NIGHTFOX Campaign):**
   - Nighttime operations with thermal cameras and radiometers
   - High-resolution data on fire intensity, spread, atmospheric conditions
   - Improves fire behavior models and response strategies

5. **BVLOS Volcano Observations (USGS Makushin Volcano, Alaska):**
   - 2021-2023 missions demonstrating BVLOS capability
   - August 2023: Direct measurement of SO₂ and H₂S from summit
   - First UAS-based detection of volcanic gases at Makushin
   - Operated in extreme conditions: winds >50 kts, icing, 25+ mile range, 7,000 ft climb
   - Large orthomosaic photogrammetry of summit
   - Potential for routine, safe hazardous volcano monitoring

---

### **SwiftCore Flight Management System**

**Components:**

1. **SwiftPilot Avionics Control Board**
   - Size: 6.7cm × 4.0cm × 1.8cm, Weight: 50g
   - 9 DOF IMU, 10 Hz GPS, 1 kHz altitude update
   - Gumstix Overo processor (1 GHz Cortex-A8)
   - Interfaces: CAN, UART, I2C, SPI, USB, Ethernet
   - Industry-leading sensor-based control minimizing operator workload

2. **SwiftTab Operator Interface**
   - Android-based tablet with gesture/multi-touch interface
   - Real-time telemetry
   - Mission planning, payload, autopilot, aircraft control
   - Intuitive design abstracting clutter while providing essential information
   - Integrates with modular payload systems for real-time mission adjustments

3. **SwiftStation Ground Station**
   - Size: 15cm × 30cm × 35cm, Weight: 0.9 kg
   - Tripod-mounted with 900 MHz and GPS antennas
   - Links SwiftTab to SwiftPilot, enabling fully autonomous flight
   - Multiple data link options for connectivity maintenance
   - Capable of functioning as RTK base station (centimeter-level accuracy for navigation and payload data tagging)

**Key Capabilities:**

1. **Predictive Maintenance:**
   - Real-time diagnostics and predictive analytics
   - Continuous monitoring of critical components
   - Early detection of wear/potential failures (e.g., propulsion degradation)
   - Detection of subtle anomalies in power distribution
   - Extends service intervals, reduces downtime

2. **Safe-to-Land Autonomy:**
   - Machine learning algorithms for hazard recognition
   - Onboard sensor data assessment of environmental conditions
   - Autonomous landing zone identification and selection
   - Real-time processing (once per second)
   - Tested on S2 platform; currently low TRL, target for commercial inclusion within next year

3. **Cooperative Control / Swarming:**
   - NSF and USAF-funded project using Black Swift UAS for RF emission localization/tracking
   - Autonomous path planning for swarm optimization
   - Mesh network communications relay capability
   - Field-tested RF source localization to ~20m accuracy with two UAS tracking WiFi (2.4 GHz) and 433 MHz emitters
   - Demonstrated portability to different small fixed-wing UAS types

4. **Advanced Autonomy:**
   - Fully autonomous flights in harshest conditions
   - Sensor-based control autonomously modifying flight path based on sensor inputs
   - Proprietary estimation and control schemes exceeding Dronecode performance, especially in high-wind environments
   - Not a "Dronecode clone"; supports multiple protocols with open interfaces while maintaining independent innovation
   - Distributed avionics architecture (networked nodes) enabling redundancy, field maintenance, automated part lifetime tracking, expandability, third-party integration

---

## Use Cases & Applications Summary

| Application | UAS Platform(s