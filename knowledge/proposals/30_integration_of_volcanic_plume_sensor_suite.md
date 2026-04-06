# Integration of Volcanic Plume Sensor Suite

## Document Metadata
- Type: SBIR Phase I Final Report (section 3.0)
- Client/Agency: NASA
- Program/Solicitation: 2016 NASA SBIR, Volcano topic
- Date: September 10, 2016 (report date); Phase I work completed by October 21, 2016
- BST Products/Systems Referenced: SuperSwift XT, SwiftCore FMS, SwiftPilot, Multi-Hole Probe (MHP), payload tray system
- Key Personnel: Jack Elston (PI), Dr. Argrow, Dr. Wardell, Dr. Dixon, Dr. Stachura

## Executive Summary
Black Swift Technologies completed Phase I work integrating a multi-sensor payload suite into the SuperSwift XT for volcanic plume sampling missions. The work included development of a novel lightweight multi-hole probe (MHP) for 3D wind measurement, a comprehensive sensor trade study resulting in two payload configurations, detailed interface design for eight sensors, and complete CAD assembly design with CFD validation of nose cone modifications. The finalized system maintains aircraft center of gravity, fits within 5-lb payload limits, and achieves a gross takeoff weight of 14.6 lbs (below the SuperSwift XT maximum of ~15.5 lbs).

## Technical Approach

### Multi-Hole Probe (MHP) Development
- **Design Philosophy**: Developed a lightweight, lower-cost alternative to commercial MHPs using 3D printing and custom PCB sensors
- **Sensor Configuration**: 5 dynamic pressure ports (pointing forward + 4 offset at 45°) + 4 static pressure ports
- **Manufacturing**: Initial ABS plastic prototype failed due to clogged ports; revised design used acrylic with 29-micron layers allowing 0.3mm minimum wall thickness
- **Electronics**: 
  - i2c multiplexer for sequential reads from five differential pressure sensors
  - CAN bus to USB serial interface (115,200 baud ASCII format)
  - Output: Time [ms], Static P [Pa], Dynamic P [Pa], four Differential P measurements [Pa], Board Temp [°C]
- **Calibration Method**: Multi-point calibration (5 airspeeds: 10-30 m/s; pitch/yaw: ±20° in 9-point grid) generating lookup tables for velocity calculation per Telionis (2009) and Johansen (2001) methods
- **Validation**: Incompressible flow airspeed calculation using formula: V = √(2(Pt - Ps)/ρ) for Mach < 0.2
- **Wind Tunnel Testing**: Validated against Aeroprobe multi-hole probe at matching test points

### Sensor Trade Study and Configuration Selection
Two payload configurations developed based on:
- 5-lb payload weight limit
- Physical space constraints (multiple sensors require direct airflow access)
- Scientific mission requirements

**Configuration 1 (Primary for Phase II)**:
- PTH: iMet-XF (Pressure, Temperature, Humidity)
- Forward Video: COTS FPV camera (3.7V, 0.9W)
- 3D Winds: BST Multi-Hole Probe (5V, 0.5W)
- Thermal IR Video: FLIR Vue Pro R (5V, 2.2W)
- EO Camera: MapIR Survey2 (5.2V, 10W)
- Nephelometer: MSE mini LDV (12V, 20W)
- Gas Sensors: iMet miniGAS for CO₂, SO₂, CH₄, H₂S (12V, 3W)

**Configuration 2 (Follow-on)**:
- Mass Spectrometer: Transpector XPR3 from INFICON Inc.
- Vacuum Pump: *Suitable commercial pump not identified during Phase I*; JPL contact recommended pursuing turbo-molecular drag pump from Creare

### Sensor Interface Design
- **Power Budget**: Total 36.7W from available 50W; 12V and 5V supplied to payload tray
- **Data Architecture**: SwiftPilot with Linux Gumstix board as central hub
- **Payload CAN Bus**: Custom BST CAN interface boards for sensor integration
- **Camera Trigger System**: Camera Interface board converts autopilot commands to camera-specific signals; each image tagged with trigger time, position (lat/lon/altitude), and orientation (roll/pitch/yaw) to SD card
- **Forward Video**: Start/stop control on launch/landing; timing logged for synchronization
- **MHP + PTH**: Route through iMET-XF combined board, then via Generic Interface board (serial-to-CAN) to autopilot for time-synchronization and SD card logging
- **USB Sensors** (Nephelometer, miniGAS): Direct Gumstix USB connection with autopilot-provided time tags and telemetry; support for USB initialization commands in Phase II

### Payload Assembly Design
- **Structural Design**: Laser-cut 2D+ wood/composite frame with four carbon fiber rods for mounting in SuperSwift XT airframe
  - Payload tray mass: 219g
  - Design allows field reconfiguration and future commercialization conversion to machined composites
- **Sensor Placement Constraints**:
  - Maintain aircraft center of gravity (verified in Solidworks)
  - Provide uninterrupted airflow access for MHP, trace gas, PTH, Nephelometer, mass spectrometer
  - Unobstructed forward video view
  - EO and Thermal cameras mounted for nadir (downward) viewing
  - All sensors mountable, accessible, serviceable
  - MHP positioned away from nose cone for accurate 3D wind measurement via 3D printed support piece
  
### Nose Cone Modification
- **CFD Analysis**: Validated modified nose cone inlet ports at cruise speed
- **Port Configuration**: Separate inlets for PTH, MHP, trace gas, nephelometer, and cameras
- **Solid Model**: Complete assembly modeled for CFD to assess flow effects on MHP wind measurements

## Products & Capabilities Described

### SuperSwift XT Aircraft
- **Payload Capacity**: 3-5 lbs optimal range; maximum GTOW ~15.5 lbs
- **Power Availability**: 50W from 12V and 5V rails to payload tray
- **Field Reconfigurability**: Modular payload system allows rapid swaps
- **Prior Scientific Missions**: 
  - Soil Moisture Mapping radiometer
  - MALIBU (Multi AngLe Imaging Bidirectional Reflectance Distribution Function) payload
  - Both approved under NASA Certificates of Authorization (COAs)

### SwiftCore FMS (Flight Management System)
- Integrated avionics with CAN bus architecture
- Autopilot with Linux companion computer
- Payload data logging to SD card with time/position/orientation tagging
- Extensible to multiple sensor interfaces (CAN, serial, USB, Ethernet)

### SwiftPilot Avionics
- Linux Gumstix board for payload control
- CAN interface boards (Camera Interface, Generic Interface) plug directly to payload bus
- Handles sensor initialization, data capture, telemetry synchronization

### Multi-Hole Probe (MHP) - Novel Development
- **Advantages**: Lower cost and lighter weight than commercial alternatives (Aeroprobe)
- **Measurement Capability**: Full 3D velocity vector (airspeed, pitch, yaw)
- **Rapid Prototyping**: 3D-printable design allows platform-specific modifications
- **Particulate Resilience**: Probe geometry can be modified to better handle volcanic particulates

## Use Cases & Applications

### Primary Mission: Volcanic Plume Sampling
- Real-time in-situ sampling of volcanic gases (CO₂, SO₂, CH₄, H₂S)
- Measurement of plume dynamics via 3D wind field
- Thermal signature mapping via FLIR imagery
- Optical documentation via forward and nadir EO cameras
- Particulate characterization via nephelometer
- Atmospheric state (PTH) measurement for context
- Mass spectrometry option for detailed chemical composition (Phase II)

### Scientific Data Integration
- All measurements geo-located and time-synchronized
- Sensor data cross-referenced with aircraft position and attitude
- Enables spatial correlation of chemical, thermal, and aerosol measurements

## Key Results (Phase I Completion)

### MHP Development
- **Prototype Completion**: Finalized 3D-printed acrylic case design with six pressure ports integrated
- **Wind Tunnel Testing Completed**: Validated against commercial Aeroprobe sensor
- **Firmware Implementation**: Dual PCB integration with i2c multiplexing and CAN-to-USB serial interface
- **Cost/Weight Achievement**: Successful demonstration of lower-cost, lighter alternative to commercial MHPs
- **Manufacturing Path**: Post-processing (acetone polishing) validated for surface smoothness; metal printing evaluated as option

### Payload Configuration Finalization
- **Configuration 1 Mass Breakdown**:
  - Aircraft (wing, fuselage, battery, nose): 4857g (10.71 lbs)
  - Sensors: 1747g (3.85 lbs)
  - **Total GTOW**: 6604g (14.6 lbs) — *within 15.5 lb maximum*
  - Center of gravity verified within safe envelope

### Sensor Trade Study Results
- Evaluated multiple sensor suites for scientific return optimization
- Selected eight sensors spanning three measurement domains (atmospheric, thermal, optical)
- Identified vacuum pump as limiting constraint for mass spectrometer integration in Phase II

### Design Completion
- Complete 3D CAD assembly of SuperSwift XT with integrated payload
- Nose cone modifications designed and CFD-validated
- Payload tray laser-cut design ready for manufacture
- All sensor mounting, wiring, and connector integration documented

### Interface Architecture Validation
- Demonstrated modular payload system extensibility across multiple standard interfaces
- Confirmed power budget feasibility (36.7W vs. 50W available)
- Established time-synchronization protocol across heterogeneous sensor types

## Notable Details

### Technical Achievements
- **First Multi-Hole Probe Development**: BST developed novel MHP in-house, partnering with iMET to integrate into their standard PTH package offering for future commercial use
- **Modular Design Philosophy**: Laser-cut 2D+ approach enables rapid prototyping with wood/composites, scalable to machined composites for commercialization
- **CFD-Validated Design**: Nose cone and inlet flow validated to eliminate adverse effects on wind measurement accuracy

### Partnership/Collaboration Strategy
- **iMET Collaboration**: Integrating BST MHP into iMET-XF board for combined wind/PTH measurement
- **JPL/NASA Partnership**: Ongoing investigation into turbo-molecular drag pump from Creare (previously flown by JPL) for Phase II mass spectrometer implementation
- **Sensor Manufacturer Coordination**: Direct contact with all sensor manufacturers to obtain accurate CAD models and interface specifications

### Phase II Readiness
- Payload tray ready for laser-cutting order
- Mass spectrometer integration pending vacuum pump identification (target: JPL turbo-molecular pump)
- USB interface initialization protocols with nephelometer and miniGAS sensor companies planned
- All structural and aerodynamic design validation complete

### Operational Considerations
- SuperSwift XT carries NASA COA approval based on prior MALIBU and soil moisture payload flights
- Field reconfigurability supports rapid payload swaps between Configuration 1 and 2, or future sensor integration
- Modular CAN bus architecture designed to remain functional as sensor technology evolves (avoiding obsolescence)

### Document Status
Report dated September 10, 2016, with final technical activities logged through October 21, 2016. This represents completion of Phase I deliverables. The project is now transitioned to Phase II (planned activities not detailed in this section).