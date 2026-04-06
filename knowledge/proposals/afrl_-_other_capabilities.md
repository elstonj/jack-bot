# AFRL - Other Capabilities

## Document Metadata
- Type: Capability brief / presentation
- Client/Agency: Air Force Research Laboratory (AFRL)
- Program/Solicitation: Not specified
- Date: October 23, 2023
- BST Products/Systems Referenced: S2 (fixed-wing UAS), E2 (multi-rotor UAS), S2 VTOL, SwiftCore (Flight Management System), SwiftFlow 3D wind probe
- Key Personnel: Jack Elston (last editor)

## Executive Summary
Black Swift Technologies presented its UAS capabilities to AFRL, emphasizing the S2 fixed-wing platform and E2 multi-rotor variant for soil moisture mapping and other ISR/monitoring applications. The document highlights BST's modular payload architecture, field-tested sensor integration across multiple domains (atmospheric, volcanic, wildfire, coastal monitoring), and advanced autonomy/avionics solutions.

## Technical Approach

### S2 Fixed-Wing Platform
- Rugged, modular fixed-wing UAS originally designed for atmospheric and volcano research
- Field-swappable payload nose cone with common power, data, and mechanical interfaces (no specialized tools required)
- Controlled by SwiftCore FMS (mature, scalable Flight Management System)
- Payload capacity: multiple sensor configurations (single, dual, or triple)
- Operates in extreme conditions: -20°C temperatures, altitudes up to 14,000 ft

### S2 VTOL Configuration
- Solar panels on wings for extended endurance (4-6 hours per flight)
- Machine vision-based automated landing (no pre-planning required)
- Terrain-aware flight planning using onboard elevation models
- Wind-aware flight planning for energy harvesting
- Rugged ingress protection rated for -40°F to 120°F operations

### E2 Multi-Rotor Platform
- Originally designed for autonomous infrastructure inspection; adapted for ISR missions
- Proprietary carbon fiber and polyamide 12 airframe
- Max takeoff weight: 25 lbs
- 35-minute nominal flight duration
- 6.5 lb max payload capacity
- Forward-mounted payload for full field-of-view
- 900 MHz telemetry frequency
- Flight ceiling: 14,000 ft
- Max winds endured: 30 mph
- Built for rugged field conditions and inclement weather

## Products & Capabilities Described

### Soil Moisture Mapping Package
- **What it is:** Integrated L-band radiometer package in S2 payload nose cone; unique UAS sensor package not commercially available elsewhere
- **Capabilities:**
  - Patented radiometer technology penetrates vegetation
  - Measures soil moisture up to 10 cm below ground surface
  - Accuracy within 3% of true volumetric soil moisture
  - Moisture maps at up to 5m resolution
  - Mapping rate: 1 km² per hour (up to 600-1,200 acres per day)
  - Additional data products: orthomosaic maps, NDVI maps, thermal maps
- **Recent deployment:** May 2022 USGS soil site for wildfire mitigation; mapped 8 km² in 1.5 days

### SwiftCore Flight Management System
- Mature, scalable FMS for S2 control
- Integration with advanced avionics

### Advanced Avionics Solutions
- **Improved Autonomy:**
  - AI and machine vision-based systems
  - GPS-denied navigation
  - ADS-B integration
  - Real-time semantic segmentation (demonstrated in NASA-funded project)
  - Automated emergency landing plan generation
- **Improved Reliability:**
  - ML predictive maintenance
  - Web-based user portal for flight analysis and maintenance recommendations
- **Advanced Sensors:**
  - SwiftFlow 3D wind probe
  - Heated pitot
  - Rain mitigation for air data

## Use Cases & Applications

### Soil Moisture Monitoring
- Wildfire mitigation planning
- Runway assessment (unimproved runways)
- Quick-scan capability with complementary E2 for higher resolution

### Atmospheric Research
- High-altitude, high-latitude studies (Greenland operations at -20°C, up to 14,000 ft)
- Water vapor analysis
- Trace gas measurements: CO₂, SO₂, CH₄, H₂S

### Volcanic Monitoring
- Plume monitoring with specialized gas sensors
- Nephelometer for volcanic particle size/distribution assessment

### Wildfire Monitoring
- Nighttime in situ measurements of wildfire plumes
- Remote measurement of wildfire properties
- Research-quality measurements of CO₂, CO, aerosol, RH, pressure, temperature

### Coastline Monitoring
- Thermal and hyperspectral payload combinations
- Multispectral camera arrays for Landsat-8 OLI and S-NPP VIIRS instrument calibration

### Infrastructure Inspection
- Autonomous inspection missions (E2's original application)
- Adaptable for ISR missions

## Notable Details

### Complementary Platform Strategy
- S2 (fixed-wing): broader coverage area
- E2 (multi-rotor): higher resolution data
- Designed to work together for comprehensive surveys

### Unique Capabilities
- BST's soil moisture radiometer is described as unique—unavailable from competitors
- Machine vision-based automated landing eliminates need for pre-planned landing zones
- Modular payload system enables rapid field swaps without specialized tools

### Operational Flexibility
- S2 VTOL capable of month-long automatic campaigns with solar charging
- Terrain-aware and wind-aware autonomy for rugged environments
- Proven track record from Arctic to Tropics

### Advanced Autonomy Demonstrations
- NASA-funded project demonstrated real-time semantic segmentation and emergency landing planning
- Web-based maintenance portal and ML predictive maintenance represent modern fleet management approach