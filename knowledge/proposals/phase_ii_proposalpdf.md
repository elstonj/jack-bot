# Soil Moisture Mapping sUAS Phase II Proposal

## Document Metadata
- Type: SBIR Phase II Proposal
- Client/Agency: NASA (SBIR Program)
- Program/Solicitation: NASA SBIR S3.05 subtopic (Earth Science); Proposal number S3.05-8971
- Date: Submitted November 2013 (document modified date); Phase II contract period ~22.5 months
- BST Products/Systems Referenced: SuperSwift sUAS, Tempest sUAS, SwiftPilot Pro autopilot, L-band Discrete Correlator Radiometer (LDCR)
- Key Personnel: Jack Elston (PI, electrical engineer), Brian Argrow, Eric Frew, Maciej Stachura, Jason Roadman, Adam Houston, Jamie Lahowetz; Prof. Albin Gasiewski (CU/CET, radiometer development); Prof. Mahta Moghaddam (soil moisture validation)

## Executive Summary

Black Swift Technologies proposes the Phase II development of the SuperSwift small unmanned aircraft system (sUAS) equipped with a passive microwave radiometer for full-coverage soil moisture mapping over 400-acre areas per flight. The system integrates a custom L-band radiometer with tightly controlled flight at 15-30m altitude above ground level to enable ~5cm depth soil moisture measurements at 15m resolution. Phase II work will complete and flight-test the Phase I prototype, design and construct two commercial-grade SuperSwift aircraft, conduct validation deployments at California instrumented test sites, and adapt a prototype for Arctic ocean surface salinity mapping.

## Technical Approach

### Primary System Architecture
- **Airframe Evolution**: Transitioning from single-engine Tempest prototype (modified with non-conductive fuselage/empennage) to twin-engine SuperSwift design with removable nose cone housing entire sensor payload
- **Propulsion**: Electric propulsion (batteries in wings) for simplified operation and cold-weather capability; 1-hour endurance with 70km range capability
- **Flight Control**: SwiftPilot Pro autopilot system (Linux-based payload computer with CAN bus interface) with custom avionics designed specifically for scientific missions
- **Positioning/Altitude Control**: Dual GPS/GLONASS receiver with post-processing accuracy <10cm in all three axes; real-time ~50cm uncertainty; laser altimeter for terrain-following at 15m AGL with advanced altitude-hold algorithms
- **Flight Planning**: Tablet-based user interface with automated "Zamboni" (serpentine) mission generation based on sensor footprint and desired coverage overlap

### Sensor Payload Integration
- **L-band Discrete Correlator Radiometer (LDCR)**: Passive microwave radiometer originally developed by Prof. Albin Gasiewski under NASA NESSF Award NNX12AO08H; capable of measuring brightness temperature for soil moisture retrieval
- **Antenna**: Coaxial-collinear antenna array elements designed in Phase I; integrated into removable nose cone to eliminate near-field interactions with fuselage
- **Supporting Sensors**: 
  - NDVI board measuring red (550-700nm) and near-infrared (700-1300nm) from nadir and zenith, plus surface and cloud-bottom infrared (10μm) temperature
  - 8 thermistor channels for ground/subsurface temperature validation
  - Laser altimeter for precise altitude above ground level

### Data Acquisition & Processing
- **Phase I Logger**: 1000 samples/sec on 10 channels (8 thermistors, 1 microwave measurement, 1 housekeeping) via A/D converter with digital serial link to autopilot at 50Hz; data logged to SD card
- **Phase II High-Speed Logger**: FPGA-based system capable of 180 mega-samples per second (MS/s) on two microwave channels, requiring 720MB/s total data rate with 36 microSD card array at 720MHz clock speed (4x oversampling); claimed to be only unit of this performance in sUAS size/weight category
- **RFI Mitigation**: High data rate enables FFT and kurtosis-based radio frequency interference algorithms developed by CU Center for Environmental Technology (CET)
- **Post-Processing Software**: Custom suite combining radiometer, thermistor, NDVI, thermal, laser, GPS, and IMU data to produce georeferenced soil moisture maps in standard open file formats

## Products & Capabilities Described

### SuperSwift sUAS
**What it is**: Next-generation soil moisture mapping platform evolved from Tempest, featuring removable nose cone payload module, twin electric engines, and integrated SwiftPilot Pro avionics

**Specifications**:
- Airframe weight: 5kg (no payload)
- Wingspan: 3.2m
- Endurance: 1 hour
- Range: Up to 70km
- Cruise speed: 18 m/s
- Minimum turn diameter: 66m (45° bank angle)
- Altitude capability: 15-30m AGL (terrain-following) for soil moisture missions
- Sensor footprint: 15m resolution
- Coverage per flight: 400 acres
- Flight time for 14.3km mission path: 13.2 minutes (well within 60-minute endurance of Tempest prototype)

**Key Innovations**:
- Modular removable nose cone enabling rapid sensor payload exchange for multi-mission use
- Twin-motor electric design simplifies integration vs. Phase I single-engine modifications
- SwiftPilot Pro autopilot with SDK for payload integration and autonomous data-driven flight planning
- Simplified operator interface with automated mission planning from area/footprint inputs

### SwiftPilot Pro Autopilot
**What it is**: Custom avionics system developed in parallel with soil moisture SBIR, featuring autopilot board, wireless command/control link, ground station, and tablet-based user interface

**Capabilities**:
- CAN bus interface and Linux-based payload computer for rapid new payload integration
- Software Development Kit (SDK) for custom mission scripting beyond waypoint-following
- Dual GPS/GLONASS raw data logging enabling post-processed positioning <10cm (better than competitors using GPS alone)
- Real-time ~50cm position uncertainty for flight control
- Advanced algorithm support for sensor-data-driven flight planning (e.g., adaptive sampling based on observed soil moisture)
- "Simplified mapping interface" for area-based mission generation with automatic line spacing/overlap calculation
- Tablet interface with visualization of flight progress

**Market Positioning**: BST reports early commitments from university engineering/research groups, agricultural researchers, atmospheric scientists, Arctic researchers, and commercial entities

### L-band Discrete Correlator Radiometer (LDCR)
**What it is**: Passive microwave sensor measuring L-band brightness temperature for soil moisture retrieval; integrates with specialized antenna array and supporting electronics

**Performance Claims**:
- Soil moisture mapping to ~5cm depth at 15m resolution
- Full coverage of 400 acres per flight
- Requires precise altitude control (15-30m AGL) for accurate measurements
- Dual-antenna configuration supporting RFI mitigation via high-speed data acquisition

### Auxiliary Subsystems Developed in Phase I
1. **Data Acquisition Board**: A/D converter, 8-channel thermistor logging, serial autopilot interface, SD card storage
2. **Power Board**: Voltage/current regulation for LDCR and thermistors
3. **Connector Boards**: Power combining and impedance matching for antenna array elements
4. **NDVI/Thermal Sensor Board**: Six-sensor configuration (red, NIR nadir/zenith, surface/cloud IR temperature) with sky-correction capability; based on AMSR-E and SMAP correction procedures
5. **High-Rate Data Logger Prototype**: FPGA-based 180MS/s unit (detailed in Phase II objectives)

## Use Cases & Applications

### Primary: Soil Moisture Mapping
- **Local-scale calibration/validation**: On-demand high-resolution measurements to validate and calibrate satellite soil moisture products (SMAP, Aquarius)
- **Watershed management**: High-resolution local-scale measurements at critical watershed scales to assess soil absorption capacity
- **Flood prediction**: Soil moisture estimates for absorption capacity assessment supporting flood forecasting
- **Drought assessment**: Targeted measurements in drought-affected areas
- **Agricultural productivity**: Extension service deployment for farm productivity improvement through detailed soil moisture mapping

### Secondary: Ocean Surface Salinity Mapping
- **Coastal/estuarine salinity**: Augmenting low-resolution Aquarius satellite data with high-resolution measurements near coastlines, estuaries, glacial outlet zones, and salinity gradient regions
- **Arctic glacier outflow mapping**: Proposed Greenland deployment to map freshwater discharge patterns near glacier grounding lines (Petermann Glacier, Jakobshavn Isbrae) supporting basal lubrication studies
- **Performance claims**: Capability of 0.3-5 ppt salinity measurement in estuarine outflow regions, ~1 ppt in polar coastal waters

### Tertiary: Broader Earth Observation
- Document emphasizes removable nose cone design positioning SuperSwift for use in additional Earth observing missions including cryospheric and hydrological science beyond soil moisture
- SwiftPilot Pro features designed for "range of scientific missions" suggesting multi-purpose platform potential

## Technical Objectives (Phase II)

1. **Completion and ground testing of Phase I prototype** (Tempest-based system with LDCR)
   - Install actual antenna elements (vs. Phase I mockups)
   - Validate NDVI and thermal sensors in lab
   - Conduct ground testing with stationary operations over instrumented plots
   - Verify data logging and processing software end-to-end

2. **Flight testing of Tempest prototype** at Canton, OK instrumented site
   - 300m × 500m test area with 21 in situ capacitive soil moisture probes at 4cm, 13cm, 30cm depths
   - 14.3 km serpentine flight path over 13.2 minute duration
   - Validate radiometer, NDVI system, terrain-following algorithms, system integration
   - Compare aircraft measurements to in situ sensors

3. **Design and construction of two SuperSwift aircraft** incorporating Phase I lessons
   - Modified removable nose cone housing soil moisture payload
   - Twin-engine electric configuration
   - Integrated SwiftPilot Pro avionics
   - High-rate (180MS/s) data logger in first aircraft
   - Real-time RFI mitigation processing board (designed by CET team)

4. **Ground testing of SuperSwift systems**
   - Test both new subsystems (high-rate logger, real-time processor)
   - Comparison flights with Phase I prototype to verify performance parity

5. **Deployment to California instrumented test sites** (2-week campaign)
   - SoilSCAPE network within 36km × 36km SMAP satellite footprint
   - 120-150 in situ capacitive soil moisture sensors
   - Dual SuperSwift operations for redundancy and mission serialization
   - Validation against ground sensors, comparison to SMAP data (if operational by deployment date)
   - Assessment of commercial readiness and field operability

6. **Refinement toward commercial product**
   - System modifications based on deployment feedback
   - Completion of data sheets and capability documents
   - Commercial analysis software with MATLAB/Octave compatibility
   - User manuals, operational checklists, FAA COA documentation templates/consulting services

7. **Arctic salinity mission preparation**
   - Modify SuperSwift for cold-weather operations
   - Development of mission requirements and implementation of necessary changes
   - Ground testing in temperature-controlled chambers and Colorado winter conditions
   - Static testing over artificial pools with predetermined salinity
   - Strong case development for Phase II-X or post-Phase II funding for Greenland field campaign
   - Collaboration discussions with Aquarius mission chief scientist Dr. Gary Lagerloef

## Key Results (Phase I Summary)

The document reports Phase I achievements beyond original statement of work:

- **Airworthy prototype constructed**: Tempest airframe modified with non-conductive fuselage/empennage and integrated LDCR radiometer, albeit with integration challenges identified for Phase II resolution
- **Auxiliary boards designed and prototyped**: Data acquisition board, power board, connector boards built and tested; NDVI/thermal sensor board designed and built but still requiring validation
- **High-speed data logger prototyped**: Initial FPGA-based unit designed for Phase II implementation
- **Antenna design completed**: Coaxial-collinear antenna elements designed, impedance/pattern/efficiency analyzed via HFSS simulation, ordered but arrived after Phase I end (Phase II will integrate)
- **SwiftPilot Pro avionics developed