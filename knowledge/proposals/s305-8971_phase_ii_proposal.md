# S3.05-8971 Phase II Proposal: Soil Moisture Mapping sUAS

## Document Metadata
- **Type**: SBIR Phase II Proposal
- **Client/Agency**: NASA
- **Program/Solicitation**: NASA SBIR Topic S3.05 (Earth Science); Soil Moisture Mapping
- **Date**: Submitted 2013 (document created 2013-05-28)
- **BST Products/Systems Referenced**: SuperSwift sUAS, SwiftPilot Pro autopilot, Tempest airframe, LDCR (L-band radiometer), data acquisition boards, NDVI/thermal sensor board
- **Key Personnel**: Jack Elston (Electrical Engineer), Prof. Albin Gasiewski (CU/CET, radiometer developer), Eryan Dai (graduate student), Dr. Mahta Moghaddam (advisor, in situ validation), Dr. Gary Lagerloef (Aquarius mission collaboration)

---

## Executive Summary

Black Swift Technologies proposes to develop, test, and validate the SuperSwift small unmanned aircraft system (sUAS) equipped with a passive L-band microwave radiometer for operational soil moisture mapping. Building on Phase I prototyping work using the Tempest airframe, Phase II will culminate in a commercially viable system capable of mapping soil moisture at ~5cm depth with 15m resolution over 400 acres per flight, operating at 15-30m above ground level. The system integrates custom avionics (SwiftPilot Pro), novel high-speed data logging, and auxiliary sensors for temperature and vegetation index measurement, enabling rapid deployments for NASA missions and broader civilian applications.

---

## Technical Approach

### System Architecture
- **Platform**: Modified Tempest airframe redesigned as **SuperSwift** with dual electric motors and removable nose cone payload module
- **Sensor**: L-band Dual-Channel Radiometer (LDCR) developed by Prof. Gasiewski under NASA NESSF Award
- **Flight Parameters**: 
  - Altitude: 15-30m AGL (maintained via laser altimeter and precision terrain-following)
  - Airspeed: 18 m/s
  - Endurance: 60+ minutes
  - Wingspan: 3.2m
  - Airframe weight: 5 kg (dry)
  - Coverage: ~400 acres per mission

### Key Technical Innovations

**1. Modular Removable Nose Cone Payload Architecture**
- Entire soil moisture sensing package housed in removable nose cone
- Enables quick payload swap for other Earth observing missions
- Simplifies field testing, calibration, and maintenance
- Twin-motor design (vs. single motor) allows this configuration

**2. SwiftPilot Pro Autopilot System**
- Purpose-built for scientific missions with strict state estimate requirements
- Features:
  - High-accuracy GPS/GLONASS with post-processed position uncertainty <10cm (all three axes)
  - Real-time position solutions ~50cm uncertainty
  - CAN bus interface for modular payload integration
  - Linux-based payload computer with software development kit (SDK)
  - Tablet-based user interface with automated mapping mission planning
  - Terrain-following with laser altimeter for precise low-altitude flight
  - Dual GNSS constellation logging for post-processing

**3. Advanced Data Acquisition Systems**
- **Phase I unit**: 1000 samples/sec, 10 channels (8 thermistors, 1 microwave, 1 housekeeping)
- **Phase II high-speed logger** (SuperSwift 1):
  - 180 mega-samples/sec (MS/s) on LDCR channels
  - 36 microSD card array written by FPGA at 720 MHz clock
  - AD9643-210 ADC with 210 MS/s sampling rate
  - Total data rate: 720 MB/s
  - Claimed to be only unit in this weight/size class capable of this performance
  - Enables FFT and kurtosis-based RFI mitigation algorithms

**4. Real-Time Processing Unit** (SuperSwift 2)
- Performs on-board data processing and RFI mitigation
- Provides immediate feedback to operators
- Enables flight re-routing based on real-time soil moisture observations

**5. Auxiliary Sensor Suite**
- **NDVI/Thermal Sensor Board**: Six sensors measuring:
  - Red (550-700 nm) and NIR (700-1300 nm) from nadir and zenith
  - Surface and cloud-bottom infrared temperature (10 μm)
  - Provides sky-corrected NDVI and soil temperature estimates
  - Required for correcting microwave brightness signal per SMAP/AMSR-E algorithms
- **Laser Altimeter**: Precision altitude control for terrain following

**6. LDCR Antenna Design**
- Coaxial-collinear antenna elements analyzed for impedance, pattern, and efficiency
- Connector/power-combining boards for impedance matching
- ~5cm soil depth penetration capability

### Regulatory & Operational Approach
- FAA Certificate of Authorization (COA) strategy leveraging BST's regulatory expertise
- NASA Airworthiness and Flight Safety Review (AFSR) compliance pathway
- Concept of Operations (CONOPS) documentation for safe NAS operation

---

## Products & Capabilities Described

### SuperSwift sUAS
**What it is**: Next-generation soil moisture mapping platform based on Tempest airframe redesign; primary BST deliverable for this SBIR.

**Design improvements over Phase I Tempest prototype**:
- Twin electric motors (vs. single) to accommodate nose cone payload module
- Removable nose cone houses entire sensor package
- Simplified manufacturing and field maintenance
- Propulsion batteries relocated to wings
- Robust airframe proven in severe weather (Vortex 2 campaign)

**Specifications**:
- Wingspan: 3.2m
- Dry weight: 5kg
- Powered endurance: ~60 minutes
- Range: ~70km
- Cruise speed: 18 m/s
- Terrain-following altitude capability: 15-30m AGL
- Coverage per mission: ~400 acres

**Proposed uses**: Primary soil moisture mapping; secondary applications include sea surface salinity, cryospheric science, hydrological monitoring

**Performance claims for soil moisture mapping**:
- Soil moisture depth: ~5cm
- Spatial resolution: 15m
- Measurement accuracy: Against SMAP and Aquarius satellites
- On-demand local-scale measurements complementing satellite data
- Useful for calibration validation of SMAP satellite (~2014 launch timeframe mentioned)

---

### SwiftPilot Pro Autopilot
**What it is**: Advanced avionics system designed from science mission requirements; commercial product developed in parallel with SBIR work.

**Capabilities**:
- Fully autonomous mission execution with custom payload integration
- Post-processed GPS/GLONASS fusion: <10cm uncertainty in 3D
- Real-time RTK-capable positioning: ~50cm uncertainty
- CAN bus payload interface
- Modular payload computer with Linux OS and SDK
- Automated mission planning interface (tablet-based)
- Terrain-following and altitude-hold algorithms
- Raw GNSS constellation logging

**Commercial Status**: Already has commitments from university research groups, agricultural researchers, atmospheric scientists, Arctic researchers, and other commercial entities. Marketed as separate commercial product beyond SBIR.

---

### LDCR (L-Band Dual-Channel Radiometer)
**What it is**: Passive microwave radiometer originally developed by Prof. Albin Gasiewski (NASA NESSF Award NNX12AO08H); core sensor for soil moisture and salinity measurement.

**Technical approach in Phase II**:
- Two units modified/constructed for Phase II (total of 3+ units available from Phase I)
- Redesigned for compact nose-cone integration via stacked PCB layout
- Lightweight housing to reduce airframe weight
- Custom antenna system (coaxial-collinear elements)

**Measured parameters**:
- L-band brightness temperature (primary)
- Soil moisture (via Jackson algorithm)
- Surface salinity (secondary application): 0.3-5 ppt in estuarine regions; ~1 ppt in polar waters

**Measurement depth**: ~5cm for soil moisture

---

### NDVI/Thermal Sensor Board
**What it is**: Six-sensor auxiliary board providing vegetation and temperature corrections to radiometer data.

**Specifications**:
- Red (550-700 nm): nadir + zenith
- NIR (700-1300 nm): nadir + zenith
- Surface infrared (10 μm)
- Cloud-bottom infrared (10 μm)

**Purpose**: Compute sky-corrected NDVI and surface temperature for input to soil moisture extraction algorithms (following SMAP/AMSR-E methodologies)

**Status**: Designed and built in Phase I; validation required in Phase II

---

### Data Acquisition Systems
**Phase I Unit**:
- 1000 samples/sec on 10 channels
- 8-bit ADC channels for thermistors
- Microwave signal channel
- Housekeeping channel
- SD card logging
- Software-verified to meet mission requirements

**Phase II High-Speed Logger** (SuperSwift 1):
- 180 MS/s (180 million samples/second)
- 16-bit ADC
- 36 microSD card array
- FPGA-based
- Total throughput: 720 MB/s
- Enables RFI mitigation via FFT and kurtosis algorithms

**Phase II Real-Time Processing Unit** (SuperSwift 2):
- Processes radiometer data on-board
- Mitigates radio frequency interference
- Provides real-time soil moisture estimates
- Design to be completed during Phase II

---

## Use Cases & Applications

### Primary: Soil Moisture Mapping
**Scientific Missions**:
- Local-scale calibration/validation for SMAP L-band satellite (2014 launch)
- High-resolution complement to global SMAP coverage
- Watershed-scale water management assessments
- Flood prediction via soil absorption capacity
- Drought monitoring in targeted regions

**Test Sites (Proposed)**:
- **Canton, Oklahoma** (instrumented field): 300m × 500m with 21 in situ capacitive probes at 4, 13, and 30cm depths; part of SoilSCAPE network
- **California (Sacramento region)**: Larger SoilSCAPE site with 120+ sensors; within 36km × 36km SMAP footprint for concurrent validation
- **Greeley, Colorado**: Agricultural field service plot
- **Northwestern Kansas**: Private farm

### Secondary: Ocean Surface Salinity Mapping
**Application**: Augment Aquarius satellite data near coastlines with high-resolution measurements

**Target Regions**:
- Glacier outflow zones (e.g., Greenland coast)
- Estuarine mixing regions
- Coastal zones with spatial salinity variability
- Areas with freshwater discharge

**Proposed Campaign**: ROSES/Phase II-X campaign to Greenland mapping near-coast salinity in glacier outflow regions (e.g., Petermann Glacier, Jakobshavn Isbrae); focus on basal lubrication studies. Collaboration discussions held with Dr. Gary Lagerloef (Aquarius mission chief scientist).

**Performance Claims for Salinity**:
- Estuarine regions: 0.3-5 ppt measurement range
- Polar coastal waters: ~1 ppt

### Tertiary Applications (Enablement)
- **Agricultural productivity**: Extension service offices
- **Wildfire prediction**: Wildfire danger assessment
- **Disaster management**: Flooding potential assessment
- **Cryospheric science**: Cold-weather capable system under development
- **Hydrological science**: General Earth observing platform

### Market Position
Claimed as "**only commercial system** capable of mapping soil moisture content at critical depths in a low cost, easy to operate package."

---

## Key Results (Phase I Accomplishments)

### Hardware Development Completed
1. **Tempest airframe prototype**: Integrated with LDCR radiometer (with fuselage modifications)
2. **Antenna system**: LDCR coaxial-collinear antenna elements designed, analyzed, and ordered
3. **Data acquisition board**: Designed, built, tested; SD card logging verified at 1 kS/s
4. **Power supply board**: Designed, built, tested; voltage/current levels verified
5. **Connector/matching boards**: Antenna power combining and impedance matching
6. **