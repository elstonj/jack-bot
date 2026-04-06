# S3.05-8971 Phase II Proposal: Soil Moisture Mapping sUAS

## Document Metadata
- **Type:** NASA SBIR Phase II Proposal
- **Client/Agency:** NASA (Earth Science Technology Office, subtopic S3.05)
- **Program/Solicitation:** NASA SBIR 2012; Topic S3.05 (Earth Observing Instruments)
- **Date:** 2012 (Phase II proposal submission)
- **BST Products/Systems Referenced:** SuperSwift sUAS, Tempest (predecessor airframe), SwiftPilot Pro autopilot, LDCR (L-band Dual-polarization Correlation Radiometer)
- **Key Personnel:** 
  - Black Swift Technologies team (company leadership not explicitly named in excerpt)
  - Prof. Albin Gasiewski (radiometer developer, CU/CET)
  - Dr. Mahta Moghaddam (California test site coordination)
  - Dr. Gary Lagerloef (Aquarius mission chief scientist, collaboration discussions)
  - Geoff Bland (NASA Project Manager)

## Executive Summary
Black Swift Technologies proposes continued development of the SuperSwift sUAS platform integrating a passive L-band microwave radiometer to provide full-coverage soil moisture measurements over 400 acres per flight at 15m resolution and ~5cm depth penetration. Phase II will complete prototype validation, construct two production SuperSwift aircraft, conduct two field deployments (Oklahoma and California test sites), and prepare an Arctic variant for ocean surface salinity mapping missions.

## Technical Approach

### System Architecture
The proposed system combines three integrated elements:

1. **Airframe:** Modified Tempest platform (originally designed for severe weather research including VORTEX2 tornado sampling)
   - Phase I used stock Tempest with modifications for antenna integration
   - Phase II introduces SuperSwift variant: twin-motor electric propulsion (vs. single motor), removable nose cone housing entire sensor payload, 5 kg airframe weight, 3.2 m wingspan
   - Electric propulsion simplifies operations and enables cold-weather capability
   - Can operate from unimproved surfaces

2. **Sensor Payload (Removable Nose Cone Module):**
   - L-band Dual-polarization Correlation Radiometer (LDCR) developed by Prof. Gasiewski under NASA NESSF Award NNX12AO08H
   - Measures brightness temperature at L-band frequencies for soil moisture extraction
   - NDVI/thermal sensor board: measures red (550-700 nm) and near-infrared (700-1300 nm) reflectance from nadir and zenith; surface and cloud-base infrared temperature (10 μm); provides sky-corrected NDVI and soil temperature corrections per AMSR-E and SMAP algorithms
   - Eight thermistors for temperature measurement
   - Laser altimeter for precise altitude control and terrain following
   - High-speed data acquisition: Phase I prototype logs at 1000 samples/sec across 10 channels (8 thermistors, 1 microwave, 1 housekeeping). Phase II will implement FPGA-based logger capable of 180 MS/s (mega samples/sec) on 16-bit ADC for RFI mitigation—using 36 microSD card array, described as state-of-the-art for sUAS class (current commercial systems max 0.2 MS/s).

3. **Avionics System (SwiftPilot Pro):**
   - Custom-developed autopilot specifically designed for scientific missions
   - Advanced dual-constellation GPS receiver (GPS + GLONASS raw data logging) with post-processed positioning accuracy <10cm in all three axes; real-time solution ~50cm uncertainty
   - CAN bus interface and Linux-based payload computer with SDK for rapid payload integration
   - Simplified tablet-based user interface with automated mission planning: user selects mapping region, interface auto-generates serpentine sampling path based on altitude AGL, sensor FOV, and desired overlap
   - Advanced altitude hold algorithms using laser altimetry for low-altitude (15m AGL) terrain-following precision
   - SDK enables scripted autonomous missions beyond simple waypoint-following; allows flight plan modification in-flight based on sensor data

### Operational Parameters
- **Flight Altitude:** 15-30m above ground level (AGL) required for 5cm depth penetration and ~15m spatial resolution
- **Coverage:** ~400 acres per flight
- **Endurance:** 60 minutes (Tempest); 1 hour sustained flight with SuperSwift
- **Range:** Up to 70 km
- **Cruise Speed:** 18 m/s (Tempest)
- **Turn Radius:** Minimum 66m (Tempest with 45° max bank angle); flight plans designed with 75m orbit diameters
- **Precision Flight Control:** Terrain-following with laser altimeter, precise GPS-based positioning, autonomous serpentine pattern execution

### Integration Challenges Addressed in Phase II
- **Phase I Lessons Learned:** Stock Tempest required extensive modification to remove conducting materials from rear fuselage and empennage (radiometer antenna requirements); external antenna placement; complex control linkage manufacturing; deeply integrated payload difficult to remove for testing
- **Phase II Solution:** Modified fuselage design with removable nose cone, twin-motor configuration on wings, separable sensor suite enabling modular payload swapping and field testing/replacement

### Novel Technologies Developed (Phase I + II)
1. **Lightweight NDVI/Thermal Sensor Board:** Custom design addressing Phase I discovery that NDVI and surface temperature are required corrections for soil moisture retrieval
2. **High-Rate Data Acquisition System:** 180 MS/s capability exceeds commercial sUAS-compatible solutions; enables FFT and kurtosis-based RFI mitigation algorithms for operation near populated areas
3. **Real-Time Processing Board (Phase II addition):** CET-led design for in-flight RFI mitigation and data processing, enabling adaptive flight path modification and immediate feedback
4. **SwiftPilot Pro Avionics:** Dual-constellation GPS with raw data logging, CAN bus payload architecture, payload SDK, simplified mission planning interface

## Products & Capabilities Described

### SuperSwift sUAS Platform
**What it is:** Modular sUAS platform with removable sensor nose cone, designed for Earth observation missions, featuring precision low-altitude flight control and flexible payload integration.

**Soil Moisture Mapping Configuration:**
- Full system integration: radiometer + NDVI/thermal sensors + high-rate data logger + avionics + airframe
- Delivers georeferenced soil moisture maps at 15m resolution, ~5cm depth
- Coverage: 400 acres per sortie
- Flight altitude: 15m AGL minimum
- Endurance: 1 hour
- Two aircraft constructed for redundancy and serial long-duration missions

**Key Specifications:**
- Airframe weight: 5 kg (airframe alone)
- Wingspan: 3.2 m
- Electric propulsion (twin motors in SuperSwift variant)
- Field-repairable/modular design for field operations

**Modular Architecture:**
- Removable nose cone housing all sensors and high-speed data logger
- Interface definition facilitates third-party payload development
- Quick sensor module exchange in field
- Supports upgrade, testing, calibration, and validation cycles

**Use Cases Beyond Soil Moisture:**
- Ocean surface salinity mapping (L-band radiometer suitable for ~0.3-5 ppt accuracy in estuaries, ~1 ppt in polar waters)
- Cryospheric and hydrological science missions
- Any Earth observation mission compatible with modular nose cone payload

### L-Band Dual-Polarization Correlation Radiometer (LDCR)
**What it is:** Passive microwave radiometer developed by Prof. Albin Gasiewski; measures L-band brightness temperature.

**Soil Moisture Application:**
- Brightness temperature converted to soil moisture using Jackson soil moisture extraction algorithm (validated on ESTAR/Washita'92 mission)
- Sensitive to ~5cm soil depth
- Optimal frequency for soil moisture penetration

**Ocean Salinity Application:**
- Capable of measuring sea surface salinity to 0.3-5 ppt in estuarine outflow zones
- ~1 ppt accuracy in polar coastal waters
- Complements Aquarius satellite data, particularly near coastlines, estuaries, glacial outlets

### SwiftPilot Pro Autopilot
**What it is:** Custom-developed autopilot/flight control system with groundstation and tablet UI, designed for scientific missions.

**Key Capabilities:**
- Simplified mission interface: user selects mapping region, system auto-generates serpentine flight paths with uniform sampling
- GPS positioning: dual-constellation (GPS+GLONASS) receiver with <10cm post-processed accuracy, ~50cm real-time
- CAN bus payload interface with Linux payload computer
- SDK for payload software development and mission scripting
- Modular payload logging architecture: central time/position correlation across multiple independent sensors
- Advanced altitude hold using laser altimeter for low-altitude precision flight
- Adaptive mission execution: flight plan can be modified in-flight based on sensor data
- Tablet-based user interface for mission monitoring and parameter adjustment

**Specifications:**
- Autonomous waypoint execution capability
- Advanced flight control suitable for difficult environments
- Integration with multiple sensor types simultaneously

### Auxiliary Sensor Boards (Phase I Designs, Phase II Integration)
1. **Data Acquisition Board (DAQ):** 
   - 8-channel analog input (thermistors) at 1 kS/s via A/D converter
   - 2 radiometer signal channels (microwave measurements)
   - Serial link to autopilot at 50 Hz
   - SD card logging for post-flight processing
   - Phase II upgrade: FPGA-based 180 MS/s sampling at 16-bit resolution on 36 microSD card array (720 MHz clock, 720 MB/s data rate)

2. **NDVI/Thermal Sensor Board:**
   - Red sensors (550-700 nm): 2 units (nadir + zenith)
   - Near-infrared sensors (700-1300 nm): 2 units (nadir + zenith)
   - Infrared temperature sensor (10 μm): 2 units (surface + cloud bottom)
   - Sky-corrected NDVI calculation
   - Surface temperature estimation for soil moisture algorithm correction
   - Design validated against AMSR-E and SMAP correction procedures

3. **Power Supply Board:** Custom voltage/current regulation for radiometer and thermistors

4. **Antenna Connector Boards:** Power combining and impedance matching for antenna array elements

5. **Coaxial-Collinear Antenna Elements:** L-band antenna array designed, analyzed for impedance/pattern/efficiency; externally mounted on Tempest (Phase I integration challenge; moved to removable nose cone in SuperSwift)

6. **Real-Time Processing Board (Phase II):** CET-developed; performs RFI mitigation and data processing in-flight from high-rate sampled data

### Data Products & Analysis Software
- Georeferenced soil moisture maps in standard open file formats
- Compatible with MATLAB and Octave for end-user processing
- Post-flight analysis software suite combining radiometer + thermistor + NDVI + thermal + GPS + IMU + laser altimeter data
- Validation against in situ soil moisture probes and satellite data (SMAP)

## Use Cases & Applications

### Primary Mission: Soil Moisture Mapping
**Test Sites:**
- **Canton, Oklahoma (Phase II Year 1):** 300m × 500m instrumented field with 21 in situ capacitive soil moisture probes at 4cm, 13cm, and 30cm depths; part of SoilSCAPE network (validates AirMOSS and SMAP); 1-week deployment planned
  - Flight path: 14.3 km serpentine route with 15m line spacing, 13.2 minutes flight time
  - Direct validation against in situ sensors
  - System verification for concept of operations, ground systems, operability

- **California (near Sacramento, Phase II Year 2):** 36 km × 36 km area within SMAP satellite footprint; SoilSCAPE network with 120-150 in situ capacitive probes; 2-week deployment
  - Larger scale demonstration of commercial capability
  - Comparison with SMAP satellite data (expected operational by deployment time)
  - Simultaneous in situ, sUAS, and satellite measurement comparison at three spatial scales
  - System refinement and commercialization assessment

### Agricultural Applications
- Productivity improvement through on-demand soil moisture monitoring
- Integration with agricultural extension service offices
- Local-scale measurements complement