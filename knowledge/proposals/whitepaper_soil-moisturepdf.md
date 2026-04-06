# Soil Moisture Mapping with Uncrewed Aircraft Systems (UAS)

## Document Metadata
- Type: White paper
- Client/Agency: Army (prepared for 2025 ACM-UAS Summit)
- Program/Solicitation: NASA SBIR program (mentioned for LDCR sensor development)
- Date: May 2, 2025
- BST Products/Systems Referenced: S2 UAS, SwiftCore (Flight Management System), SwiftPilot, SwiftStation, SwiftTab, LDCR (Lobe Differencing Correlation Radiometer)
- Key Personnel: Jack Elston (CEO), Maciej Stachura (CTO)

## Executive Summary
Black Swift Technologies, in partnership with the Center for Environmental Technology (CET), has developed a soil moisture mapping UAS system based on the S2 fixed-wing platform equipped with a passive L-band microwave radiometer (LDCR). The system provides high-resolution soil moisture data at depths of 5-10 cm with up to 15m spatial resolution, enabling applications in agriculture, emergency response, wildfire management, and military runway integrity assessment across areas of up to 600 acres per flight.

## Technical Approach
The system integrates three core elements:

**Sensor Technology:**
- Lobe Differencing Correlation Radiometer (LDCR) operating at 1.4 GHz
- Passive L-band microwave radiometry (not affected by clouds, lower vegetation sensitivity)
- Measures brightness temperature of ground and vegetation, fitted to dielectric characteristic models to estimate volumetric soil moisture (VSM)
- Coupled with multispectral instruments for visible, thermal, and near-infrared data capture
- Provides elevation, thermal imagery, NDVI (normalized difference vegetation index), and soil type information

**Airframe & Integration:**
- Electrically powered S2 airframe designed to minimize electromagnetic interference with antenna performance
- Shielded electronics to eliminate interference in LDCR circuit and antenna
- Custom inertial navigation solution integrated into SwiftCore avionics
- Modular payload architecture with large nose cone volume for field-swappable instruments
- RTK (real-time kinematic) GPS for georeferencing, further corrected at ground station

**Flight Capabilities:**
- Low-altitude, terrain-following flight capability (15m-30m AGL optimal for soil moisture)
- Can operate at 30-120m AGL depending on mission
- Fully autonomous takeoff with advanced landing algorithm for robust belly landings using laser landing system
- Operating ceiling up to 6,096m (20,000 ft) for NASA science missions
- Coverage: up to 600 acres per flight
- Can operate in temperatures near -20°C

## Products & Capabilities Described

**Black Swift S2 UAS:**
- Fixed-wing electric aircraft designed around payload requirements
- Payload-centric design with large nose cone for integration flexibility
- Modular field-swappable payload system with standard data and power interfaces
- Passed NASA rigorous flight safety review
- Operational ceiling: up to 20,000 ft
- Primary aircraft for soil moisture mapping missions

**SwiftCore Flight Management System:**
- Entire system made in USA and designed in-house by BST
- Comprised of: SwiftPilot (autopilot), SwiftStation (ground station), SwiftTab (user interface), and support electronics
- Used and approved by NASA, deployed by NOAA, growing commercial use

**SwiftPilot Autopilot:**
- Two dedicated 168 MHz Cortex-M4 CPUs with floating-point units
- One optional 1 GHz Cortex-A8 processor for customer payloads
- Modularized CAN-bus architecture for virtually unlimited peripheral/payload connectivity options
- One of the smallest and most powerful commercially available autopilots
- Enables fully autonomous flight from launch to landing

**SwiftTab User Interface:**
- Runs on handheld Android tablets and smartphones
- Intuitive flight planning: operators can program aircraft in minutes
- Mid-flight flight plan modifications and uploads
- Gesture-based controls for minimal training requirements
- Geo-referenced data import capability

**SwiftStation Ground Station:**
- Tripod-mounted, portable, customizable platform
- Incorporates 900 MHz and GPS antennas
- Expandable via custom modules
- Multiple radio options available
- Seamlessly integrates with X-Plane Pro Flight Simulator

**LDCR Sensor:**
- Passive L-band radiometer measuring soil moisture at 1.4 GHz
- Penetration depth: 5-10 cm below ground surface
- Measurement resolution: up to 5m spatial resolution
- Functional under dense canopy crops
- Provides volumetric water content (VWC) estimates

## Use Cases & Applications

**Wildfire Susceptibility & Prevention:**
- Maps soil moisture and live fuel moisture (LFM) in near real-time
- Identifies threshold-like impacts on fire ignition probability, fire size, and flammability
- Assists with pre-fire situational awareness in nearly real-time for western US wildfire-prone landscapes (particularly California)
- Demonstrates improved fire danger accuracy and more effective land management response

**Precision Agriculture:**
- Water conservation through variable rate irrigation systems based on soil moisture data
- Reduces fertilizer application based on exact soil water content, lowering ecological impacts of runoff
- Can be deployed by agricultural extension service offices to improve crop productivity
- Works with university-level agriculture research groups and commercial entities
- Early problem diagnosis and crop health improvement prediction

**Runway Integrity Assessment (Military):**
- Evaluates soil strength for unconventional/unimproved airfield operations
- Maps soil moisture distribution to determine load-bearing capacity for forward air base operations
- Assesses soil composition, depth, density, and quality at 5m resolution
- Alternative to traditional dynamic cone penetrometer (DCP) manual ground surveys (eliminates time delays and safety risks in hot zones)
- Identifies areas suitable for off-road movement and operations in unstable terrain (rivers, wetlands, coastal regions, thunderstorm-prone areas)

**Hydrologic Modeling & Flash Flood Prediction:**
- Demonstrated in NASA-funded research mapping soil moisture in North Texas and Oklahoma flood-affected regions
- Provides alerts and warnings for areas susceptible to flash flooding
- Supports FEMA in understanding flash flood vulnerability
- Improves flood event predictions in vulnerable watersheds

**Atmospheric Research Applications (Historical S2 Deployments):**
- High-altitude, high-latitude atmospheric research (Greenland ice sheet water vapor analysis at 4,267m altitude, -20°C temperatures)
- Wildfire plume monitoring with CO2, CO, aerosol, humidity, pressure, temperature measurements; remote fire property measurements
- Volcano plume monitoring (gases, particle size distribution, ashfall measurement accuracy)
- Airborne CO2 monitoring in volcanic regions for ecosystem response studies
- Landsat-8 and S-NPP VIIRS instrument calibration
- Airborne greenhouse gas measurements (CO2, SO2, CH4, H2S)
- Snow Water Equivalent (SWE) measurement in mountainous environments using P-band reflective signals
- Coastline monitoring with thermal and hyperspectral payloads

## Key Results
- Flights conducted by University of Colorado at Boulder at multiple test sites including Canton, Oklahoma Soilscape Site and Irrigation Research Foundation (IRF) in Yuma, Colorado
- Preliminary mission results correlate with in situ probes
- Strong correlation demonstrated across different soil types, validating the UAS solution
- Example flight data generated maps showing: flight trajectories, land cover type, soil type, and volumetric water content (VWC)

## Notable Details

**Partnership & Development:**
- Collaboration with Center for Environmental Technology (CET) on soil moisture mapping system
- LDCR sensor developed and tested under NASA SBIR program
- Active field campaigns: four major scientific campaigns in atmospheric science and remote sensing

**Company Background:**
- Black Swift Technologies based in Boulder, Colorado; operational since 2011
- All systems built on proprietary SwiftCore flight management system
- Unlike competitors using open-source avionics, BST controls design of all critical components including electronics for avionics and ground systems, software, mechanical assembly, and QC processes
- Combined expertise in avionics and engineering consulting
- Supplied to NASA, NOAA, universities, government entities, and commercial customers

**Competitive Advantages:**
- Modular architecture allowing rapid instrument integration and accommodation of next-generation payloads
- End-to-end avionics (in-house design and USA manufacturing)
- Passive microwave technology unaffected by clouds
- High revisit frequency relative to satellite systems
- Autonomy and redundancy designed for routine, safe data collection
- Field-swappable payload system reducing customer costs

**Data Products Delivered:**
- Actionable spatial and temporal resolution data on soil drainage and moisture retention dynamics
- Real-time or near real-time capability for decision-making in operational environments
- Multiple data product formats: orthomosaic, thermal, 3D data products, multispectral imagery