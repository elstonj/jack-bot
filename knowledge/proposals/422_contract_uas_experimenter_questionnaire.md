# NASA Contract UAS Science Investigator Questionnaire - Volcano Sampling sUAS

## Document Metadata
- Type: Questionnaire/Technical specifications form
- Client/Agency: NASA Goddard Space Flight Center, Wallops Flight Facility, Code 830 Aircraft Office
- Program/Solicitation: 2016 NASA SBIR (Volcano topic, Phase I)
- Date: December 6-9, 2016
- BST Products/Systems Referenced: S2 sUAS (implied), SMM Power Board v1.0
- Key Personnel: Jack Elston (Principal Investigator and Lead Technical POC, Black Swift Technologies)

## Executive Summary
This questionnaire documents the specifications and operational requirements for a customized volcano sensing payload to be integrated on a small UAS. The system comprises seven simultaneous sensors measuring optical/thermal imagery, meteorological parameters (pressure, temperature, humidity, 3D winds), trace gases, and particle characteristics, designed for low-altitude volcanic monitoring operations.

## Technical Approach
The payload integrates seven different sensors running simultaneously with time-tagging by the autopilot for post-processing synchronization. The system features:
- Independent power source (isolated from UAS power)
- Custom BST SMM Power Board v1.0 for power distribution
- Real-time data storage on SD card
- Lightweight optical window configuration for multi-spectral imaging
- Dedicated autopilot telemetry and control via Digi XTend radio link (1W, 902-928 MHz ISM band)

## Products & Capabilities Described

### S2 sUAS (implied platform)
- Small unmanned aerial system serving as platform
- Previously flown for Soil Moisture Mapping (SMM) mission
- Electric propulsion with two Maxamps LiPo battery packs (11000 mAh 5-cell and 4000 mAh 3-cell)
- Supports V-tail configuration with integrated avionics

### SMM Power Board v1.0
- Custom power supply board manufactured by Black Swift Technologies
- Integrated into payload for independent power distribution
- Isolated from UAS primary power system

### Volcano Sensing Payload
**Measurements:** EO/Thermal photos, EO video, pressure, temperature, humidity, 3D winds, trace gases, particle size and velocity

**Sensors:**
1. **Pitot-Static Port** - Starboard wing, forward-facing on aircraft axis
2. **3D Winds Sensor** - Nose-mounted, forward-facing; integrated with temperature and relative humidity sensors
3. **Nephelometer** - Nose-mounted, forward-facing on aircraft axis
4. **Trace Gas Sensor** - Nose-mounted, forward-facing on aircraft axis
5. **EO Camera System** - Multiple optical windows (0.46", 0.64" forward-facing in nose)
6. **LWIR Thermal Camera** - 1.58" optical window, nose-mounted, downward-facing
7. **Additional EO Window** - 1" x 1" downward-facing in fuselage

### Laser System
- **Type:** Class 1M (eye-safe classification)
- **Wavelength:** 850 nm
- **Output Power:** 11 mW continuous, 14 W peak
- **Status:** Authorized for U.S. operation; will not be operated outside U.S.
- **Pulse Parameters:** Pulse width and rep rate TBD

### Radio Frequency Systems
1. **Autopilot Telemetry/Control:** Digi XTend transceiver, 1W, 902-928 MHz ISM band
   - Antenna: 8.62" length, 0.66" diameter, mounted 30° off vertical in starboard V-tail
   
2. **Radio Control Link:** 2.4 GHz band, 100 mW
   - Antenna: 8.5" wire antenna, longitudinal orientation, mounted 4" below wing
   
3. **GPS Antenna:** 1575.42 MHz
   - 1.0" x 1.0" patch antenna, upward-facing on fuselage top

### Power System
- **Primary Batteries:** 
  - Maxamps LiPo 11000 5-cell (primary)
  - Maxamps LiPo 4000 3-cell (secondary/backup)
- **Battery Type:** Lithium Polymer
- **Recharge Time:** 1 hour battery-only requirement between flights

## Use Cases & Applications

### Primary Use Case: Volcano Monitoring
- **Mission Name:** Volcano Sampling sUAS
- **Application:** In-situ measurement of volcanic emissions and atmospheric conditions during volcanic activity
- **Measurements:** Capture volcanic gas composition (SO₂, CO₂, etc.), particle size/velocity profiles, thermal signatures, and meteorological conditions simultaneously

### Flight Operations Profile
- **Altitude:** Below 400 feet AGL
- **Airspeed:** Nominal 39 knots (range 29-58 knots)
- **Flight Attitudes:** Pitch -15° to +25°, Roll ±45°
- **Duration:** Nominally multiple flights per day with 1-hour battery recharge between flights
- **Conditions:** Daytime, visual flight rules only
- **Pre-flight Setup:** 15 minutes required for instrument preparation
- **Post-flight:** Immediate power-down capability; data stored on SD card during flight

## Key Installation Details

### Environmental Tolerances
- **Temperature Range:** -20°C to +50°C
- **Humidity Range:** 0% to 100% (no desiccant requirements)
- **Vibration:** Not specified (N/A)

### Power Architecture
- Experiment has independent power source
- Complete isolation from UAS primary power system
- No shared circuit protection between experimenter equipment and aircraft power
- No in-flight warm-up time required; instruments powered prior to takeoff

### Avionics Integration
- Time-tagging of all sensor data by autopilot for post-processing synchronization
- Ground control station required for mission planning and monitoring
- Autonomous flight pattern execution capability

## Notable Details

1. **Prior Flight History:** This payload configuration was derived from or builds upon the Soil Moisture Mapping (SMM) sUAS previously flown by BST, indicating iterative capability development.

2. **Hazmat Compliance:** 
   - Class 1M laser authorization obtained (fully compliant for U.S. operation)
   - Lithium polymer battery MSDS documentation attached
   - RF equipment within FCC unlicensed ISM band (no FCC authorization required)
   - No hazardous materials, cryogens, or radioactive materials

3. **Design Maturity:** Questionnaire indicates mature system with minimal support requirements:
   - No design or fabrication support required from NASA
   - No in-flight calibration maneuvers needed
   - Plug-and-play integration with ground control station

4. **Data Handling:** Real-time SD card storage enables immediate data access post-flight without tethered telemetry requirements.

5. **Compact Integration:** Multiple sensors housed in confined nose and fuselage space with carefully positioned optical windows and antenna arrays, demonstrating sophisticated payload integration capability.