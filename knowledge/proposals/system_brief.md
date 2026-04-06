# Soil Moisture Mapping UAS System Brief

## Document Metadata
- Type: System brief / capability proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II (Soil Moisture topic)
- Date: Created 2014-02-24; Modified 2014-02-26
- BST Products/Systems Referenced: SuperSwift sUAS, LDCR (L-band Digital Correlator Radiometer)
- Key Personnel: Dr. Maciej Stachura (BST), Prof. Al Gasiewkski (collaborator, University of Colorado)

## Executive Summary
Black Swift Technologies proposes a soil moisture mapping UAS system integrating a passive microwave radiometer (LDCR) with the SuperSwift small unmanned aircraft to enable full-coverage soil moisture measurements over 400 acres per flight at 15m resolution down to ~5cm soil depth. The system operates at low altitude (15-30m AGL) and includes two planned Phase II field deployments in Oklahoma and California, with additional development for Arctic ocean salinity mapping applications.

## Technical Approach

### Aircraft Platform
- **SuperSwift sUAS**: 3.2m wingspan, 6kg weight (with LDCR payload), 1-hour flight endurance, cruise speed 18 m/s
- Designed for precise low-altitude flight control required for soil moisture sensing
- Regulatory knowledge applied to enable FAA-compliant operation in national airspace

### LDCR Instrument (L-band Passive Microwave Radiometer)
- L-band antenna array (1400-1427 MHz passive EESS band) specifically designed for small UAS integration
- Coaxial-collinear antenna elements with impedance matching and connector boards
- **Receiver specifications**:
  - Bandwidth: 27 MHz minimum (standard), up to 100 MHz (low electromagnetic emissions conditions)
  - Intrinsic sensitivity: ~1-1.5% volumetric soil moisture (VSM) accuracy
  - Depth of penetration: ~5cm direct measurement
  - Spatial resolution: 15m
  - Coverage: 400 acres per flight

### Supporting Subsystems
1. **Data acquisition board**: Logs 8 thermistors + 2 radiometer signals via A/D converter (1kS/s) and digital link to autopilot (50Hz), stores to SD card
2. **Antenna array connector boards**: Power combining and impedance matching for LDCR elements
3. **Multispectral sensor board**: Measures red (550-700nm) and near-infrared (700-1300nm) from nadir and zenith; surface and cloud-base infrared (10μm) temperature for microwave brightness signal correction

## Products & Capabilities Described

### SuperSwift sUAS
- **What it is**: Small unmanned aircraft system with 3.2m wingspan, 6kg total weight with LDCR
- **Proposed use**: Platform for integrated soil moisture mapping via low-altitude flight control
- **Specifications**: 1-hour endurance, 18 m/s cruise speed, capable of 15-30m AGL operations
- **Advantages**: Tight integration of sensor with avionics and airframe; regulatory knowledge incorporated

### LDCR (L-band Passive Microwave Radiometer)
- **What it is**: Passive L-band radiometer with integrated antenna array for microwave remote sensing
- **Soil moisture mapping use**: Direct measurement of volumetric soil moisture to ~5cm depth at 15m resolution
- **Performance claims**: 
  - 1-1.5% VSM intrinsic sensitivity under ideal conditions
  - 5-10% VSM accuracy required and achievable for agricultural applications (low vegetation, low roughness, known soil types)
  - Can exceed required accuracy by factor of 3-10 under optimal conditions
  - 400-acre coverage per flight
- **Limitations**: Only directly senses top ~5cm; deeper levels (30-50cm needed for irrigation) would require dynamic modeling or P-band observations

## Use Cases & Applications

### Primary: Agricultural Soil Moisture Mapping
- Enables irrigation management decisions requiring 5-10 levels of dryness specification
- Ideal for agricultural areas with low vegetation and known soil types
- Dynamic modeling approach proposed to estimate deeper soil moisture (30-50cm) from regular L-band observations

### Secondary: Arctic Ocean Salinity Mapping
- **Modified system for cold-weather operations** in Greenland
- **Application**: Map glacier outflow surface salinity off Greenland coast and estuarine salinity
- **Performance**: Capable of ~0.3-5 ppt salinity measurement in estuarine regions; ~1 ppt in polar coastal waters
- **Purpose**: Augment Aquarius satellite data near coastal areas with high-resolution UAS measurements
- **Scientific focus**: Study freshwater outflow patterns to support basal lubrication research at glacier grounding lines (Petermann Glacier, Jakobshavn Isbrae)
- **Collaboration potential**: Discussions with Dr. Gary Lagerloef (Aquarius mission chief scientist) indicate encouraging prospects

## Planned Field Testing Activities

### Phase II Deployment 1: Canton, Oklahoma (Year 1)
- **Test site**: 300m x 500m instrumented area
- **In situ sensors**: 21 capacitive soil moisture probes at 4cm, 13cm, and 30cm depths
- **Validation**: Part of SoilSCAPE network; data used for NASA AirMOSS EV-1 and SMAP satellite validation
- **Flight plan**: "Zamboni" pattern with 15m spacing between flight lines; 14.3km total path distance; ~13.2 minutes flight time
- **Minimum turn diameter**: 75m orbits

### Phase II Deployment 2: California (Late Spring 2015)
- **Duration**: Two-week deployment
- **Test sites**: SoilSCAPE network sites near Sacramento
- **Coverage area**: Within 36km x 36km SMAP satellite footprint
- **In situ sensors**: 120 existing capacitive sensors, expanding to 150 total
- **Purpose**: Demonstrate, assess, and validate SuperSwift system performance at larger scale

### Arctic Salinity Mission Development (Phase II)
- **Cold-weather modification**: Develop requirements and implement changes for Greenland operations
- **Ground testing**: Temperature-controlled chamber tests (2016 winter, Colorado mountains)
- **Static tests**: Operation over small artificial pools with predetermined salinity
- **Future field campaign**: Late summer 2016+ in Greenland (pending post-Phase II funding)
- **Goals**: Verify operational capability; determine freshwater outflow patterns; support glacier basal lubrication research

## Key Results
Not applicable—this is a proposal/system brief, not a completed report. The document describes planned activities in Phase II, not results.

## Notable Details

- **Phase status**: System in prototype phase awaiting Phase II funding (2-year duration)
- **Commercial goal**: Phase II intended to result in commercially available UAS
- **Depth penetration limitation**: L-band cannot directly measure below ~5cm; P-band observations mentioned as alternative for deeper soil moisture
- **Regulatory expertise**: BST's "strong working knowledge of the regulatory environment surrounding sUAS" highlighted as advantage for FAA approval path
- **Multi-purpose platform**: Single system adaptable to both agriculture (soil moisture) and oceanographic (salinity) applications via payload and operational modifications
- **Collaborative partnerships**: University of Colorado (Prof. Al Gasiewkski), NASA AirMOSS and SMAP projects (validation), SoilSCAPE network (test sites), Aquarius mission (potential Arctic collaboration)
- **Integration approach**: "Tight integration of sensor with sUAS avionics and airframe" emphasized as enabling precise low-altitude flight control