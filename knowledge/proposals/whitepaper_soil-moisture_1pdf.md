# Soil Moisture Mapping with Uncrewed Aircraft Systems (UAS)

## Document Metadata
- Type: White Paper
- Client/Agency: General audience (prospective customers in agriculture, emergency management, defense, federal agencies)
- Program/Solicitation: Soil Moisture RFQ
- Date: 2024 (created/modified October 25, 2024)
- BST Products/Systems Referenced: S2 UAS, SwiftCore (Flight Management System), SwiftPilot, SwiftTab, SwiftStation, LDCR (Lobe Differencing Correlation Radiometer)
- Key Personnel: Dr. Jack Elston (CEO), Dr. Maciej Stachura (CTO)

## Executive Summary
Black Swift Technologies, partnering with the Center for Environmental Technology (CET), has developed a soil moisture mapping UAS solution built around the S2 fixed-wing platform equipped with a passive L-band microwave radiometer (LDCR). The system provides high-resolution soil moisture data at depths up to 5-10 cm with 5-15m spatial resolution over areas up to 600 acres per flight, enabling applications in precision agriculture, wildfire risk assessment, runway integrity evaluation, and hydrologic modeling.

## Technical Approach

**Core System Architecture:**
- **Airframe:** Black Swift S2 fixed-wing UAS, electrically powered with design optimized to minimize electromagnetic interference on antenna performance
- **Primary Sensor:** Lobe Differencing Correlation Radiometer (LDCR)—a passive L-band (1.4 GHz) microwave radiometer developed under NASA SBIR program
  - Measures brightness temperature of ground and vegetation
- **Flight Management System:** SwiftCore, consisting of SwiftPilot (autopilot), SwiftStation (ground station), and SwiftTab (user interface)
- **Navigation:** Custom inertial navigation solution with RTK (real-time kinematic) GPS for georeferencing; capable of terrain-following flight at low altitudes (15-30m AGL)
- **Secondary Sensors:** Multispectral instruments for visible, thermal, and near-infrared data collection
- **Data Processing:** Brightness temperature fitted to dielectric ground models to estimate volumetric soil moisture (VSM); data further corrected using ground station

**Key Technical Characteristics:**
- Fully autonomous take-off and belly landing with laser landing system
- Operates at altitudes from low-level (15-30m AGL) to 6,096m (20,000 ft)
- All-electric propulsion with shielded electronics to prevent RF interference
- Modular, field-swappable payload architecture via standard data/power interface
- Capable of terrain-following flight and autonomous operations in unimproved areas

## Products & Capabilities Described

### Black Swift S2 UAS
- **What it is:** Purpose-built fixed-wing unmanned aircraft designed around scientific payload requirements
- **Use in this context:** Primary platform for soil moisture mapping via integrated LDCR and multispectral sensors
- **Key specifications:**
  - Fully autonomous operations (launch to landing)
  - Coverage: Up to 600 acres per flight
  - Flight altitude: 15-30m AGL for soil moisture missions (up to 20,000 ft capability)
  - Soil moisture measurement depth: 5-10 cm below ground
  - Spatial resolution: 5-15m for soil moisture; up to 5m resolution possible
  - Payload-centric design with large nose cone volume for sensor integration
  - Designed to accommodate diverse scientific instruments
- **Performance:** Passed NASA flight safety review; used in multiple major scientific field campaigns

### SwiftCore Flight Management System
- **What it is:** Proprietary autopilot and ground control system designed entirely by BST
- **Components:**
  - **SwiftPilot:** Advanced autopilot with dual 168 MHz Cortex-M4 CPUs and optional 1 GHz Cortex-A8 payload processor; modularized CAN-bus architecture supporting UART, I2C, SPI, Ethernet, USB connectivity
  - **SwiftStation:** Tripod-mounted ground station with 900MHz and GPS antennas; expandable via custom modules; integrates with X-Plane Pro Flight Simulator
  - **SwiftTab:** Handheld Android tablet/smartphone interface with gesture-based controls; allows mid-flight mission modification; intuitive flight planning in minutes
- **Advantages:** Entirely USA-manufactured; designed from ground up by BST (not open-source); guarantees quality, robustness, and supply control

### Lobe Differencing Correlation Radiometer (LDCR)
- **What it is:** Passive L-band (1.4 GHz) microwave radiometer payload
- **Key capability:** Measures brightness temperature unaffected by cloud cover and with lower vegetation sensitivity compared to other remote sensing approaches
- **Use:** Coupled with multispectral instruments to provide soil moisture down to 5cm depth, vegetation indices (NDVI), thermal data, and soil type mapping

## Use Cases & Applications

### Wildfire Susceptibility / Fire Risk Management
- Real-time soil moisture and live fuel moisture (LFM) mapping to assess wildfire ignition probability, fire size potential, and flammability
- Demonstrates threshold-like relationship between LFM and fire behavior
- Enables pre-fire situational awareness for land managers and first responders in fire-prone regions (California, western US)
- Provides near-real-time decision-making capability vs. hours/days with traditional methods

### Precision Agriculture
- High-resolution soil moisture maps to inform variable rate irrigation and reduce water usage
- Optimize nutrient/fertilizer application based on soil water content, reducing fertilizer runoff
- Early problem diagnosis, crop health monitoring
- Demonstrated collaboration with university agriculture research groups and commercial entities
- Support to agricultural extension services for farmer decision support

### Runway Integrity Assessment (Military/DoD Application)
- Evaluates soil integrity for unconventional airfield operations and off-road movement
- Identifies soil strength to determine vehicle load capacity
- Replaces time-consuming manual dynamic cone penetrometer (DCP) measurements
- Provides comprehensive spatial coverage (~5m resolution) vs. discrete point measurements
- Applicable to unimproved runways, hot zones, and terrain in/around rivers, wetlands, coastal regions

### Hydrologic Modeling / Flash Flood Prediction
- Demonstrated in NASA-funded research over North Texas and Oklahoma (severe flooding regions)
- Supports FEMA vulnerability assessment for flash flood-prone watersheds
- Provides soil drainage and moisture retention data at root depths for improved flood forecasting
- Enables alerts and warnings for susceptible areas

### Environmental Monitoring (General)
- Large-area ecological studies
- Crop damage assessment
- Land management applications
- Earth science research platform

## Key Results (from Validation Testing)

**Flight Validation:**
- Actual flight missions conducted over test sites including:
  - Canton, Oklahoma Soilscape Site
  - Irrigation Research Foundation (IRF) in Yuma, Colorado
  - University of Colorado Boulder collaborative flights
- **Preliminary findings:** Volumetric water content (VWC) measurements correlate well with in situ probes and show strong correlation across different soil types
- Maps generated demonstrate flight trajectory, land cover type, soil type, and volumetric water content data products

**Atmospheric/Science Missions (S2 Platform):**
Document lists diverse successful deployments:
- High-altitude research in Greenland (-20°C, altitudes to 4,267m) measuring water vapor over ice sheets
- Nighttime wildfire plume sampling (CO₂, CO, aerosol, RH, pressure, temperature) with multispectral wildfire mapping
- Volcano plume monitoring (gases, particle size via nephelometer, 3D wind patterns)
- Airborne CO₂ monitoring in volcanic regions
- Landsat-8/S-NPP instrument calibration with NASA Goddard
- Airborne measurements: CO₂, SO₂, CH₄, H₂S with orthomosaic/thermal/3D data products
- P-band snow water equivalent (SWE) measurement
- Thermal/hyperspectral coastal monitoring

## Notable Details

**Partnership & Collaboration:**
- Works with Center for Environmental Technology (CET) on soil moisture sensor development
- SBIR program development (NASA funding for LDCR technology)
- University collaborations (University of Colorado Boulder, agriculture research groups)
- Federal agency deployments: NASA, NOAA
- Commercial integrators and end-user sales

**Competitive Advantages:**
- Proprietary SwiftCore avionics fully designed and manufactured in USA (unlike open-source competitors)
- Modular architecture enables rapid payload integration without purchasing extra expensive instruments
- Passive L-band radiometer unaffected by cloud cover (advantage over active systems)
- Tight integration of sensor, avionics, and airframe for precise low-altitude flight control
- Demonstrated reliability across extreme environments (cold, high altitude, volcanic, wildfire)
- Field-swappable payload capability enabling multi-mission deployment

**Company Background:**
- Based in Boulder, CO; operating since 2011
- Leadership: Dr. Jack Elston (CEO; Ph.D. on complex UAS networks and supercell sampling), Dr. Maciej Stachura (CTO; M.S./Ph.D. aerospace engineering; 300+ flight experiments including VORTEX2)
- Unique coupling of avionics expertise with consulting services

**Customer Contact:**
Link provided for quotes: link.bst.aero/kB50