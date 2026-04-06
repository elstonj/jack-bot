# Atmospheric Sounding UAS - Task 02 Phase II Status Report

## Document Metadata
- Type: Phase II Status Report (presentation format)
- Client/Agency: U.S. Air Force
- Program/Solicitation: SBIR; Contract FA8730-20-C-0021
- Date: Submitted April 2020 (created 2020-04-10, last modified 2021-03-18)
- BST Products/Systems Referenced: S0 UAS (prototype atmospheric sounding aircraft)
- Key Personnel: Dr. Jack Elston (Principal Investigator)

## Executive Summary
This report documents Phase II progress on developing an atmospheric sounding unmanned aircraft system (S0) for U.S. Air Force and commercial weather research applications. Task 01 (requirements finalization) was completed at 100%. Task 02 (prototype design and initial testing) was 90% complete, with manufacturing delays pushing first prototype flight beyond the contract milestone, mitigated by aerodynamic analysis, design completion, and surrogate flight data collection.

## Technical Approach

### Task 01: Requirements Finalization
BST conducted comprehensive requirements review with AF end-users and commercial customers across multiple dimensions:

**Altitude Performance:**
- AF minimum requirement: 10,000 feet (covering most Army missions)
- Commercial requests: mostly 10,000 feet, some up to 15,000 feet
- Specialized research requests: up to 100,000-120,000 feet

**Flight Duration:**
- AF requirement: 40 minutes minimum (prioritizing data speed/fidelity balance)
- Commercial: 1 hour typical; upper range 90 minutes to 4 hours

**Deployment & Launch:**
- AF: Hand launch by weather operator (AF, Army, or SOF)
- Commercial: Hand launch acceptable; some Arctic/remote research requested balloon tube-launch from altitude

**Data Parameters:**
- AF priority: Wind speed/direction, temperature, dewpoint, pressure
- Commercial: Temperature, pressure, relative humidity, 2D/3D wind profiles
- Extended capabilities explored: cloud cover, precipitation, water/ice content, aerosols, trace gases (including methane, SO₂, NOx), soil moisture, sea ice, ozone, CBRNE detection, turbulent kinetic energy (TKE), turbulence intensity

**Data Downlink:**
- AF: Post-recovery data collection acceptable if processing <15 minutes
- Commercial: Mix of post-recovery and real-time data requirements

**Recovery:**
- AF: ~10 feet recovery accuracy
- Commercial: One researcher specified ship-based deployment/retrieval

**Data Format:**
- AF: Integration with AF standard desktop, upload to AF Data Center
- Commercial: Text files, BUFR, GRIB, netCDF formats required for weather model integration

**Autonomy:**
- AF: Desired ("set height and parameters, let system go")
- Commercial: Desired with frequent requests for autopilot override capability

### Task 02: Prototype Design & Development

**Manufacturing Mitigation Strategy:**
Due to manufacturing delays delaying first prototype flight beyond milestone, BST implemented workarounds:
- Completed aerodynamic analysis to validate flight characteristics
- Completed first prototype aircraft and avionics/payload designs
- Procured parts from manufacturers
- Used surrogate flight data from previous aircraft with similar sensors
- Converted data to new format tools
- Submitted data to AF Technical Monitor for evaluation

**Airframe Design:**
- Fuselage: 1/16" wall Phenolic Linen, 1.81" OD
- Span: 54 inches
- Length: 36 inches (nose to tail, subject to battery sizing changes)
- Estimated weight: 1.6 kg
- Tail design: NACA-0010 airfoil, entirely 3D printed with full moving surfaces for tail landing
- Tail features: Field swappable (3 screws + wire-to-wire connector, no reprogramming needed), sealed against dust/dirt ingress, pivot point for tail landing
- Servos: MKS DS450 (direct drive)
- Wing: COTS modified with quick-detach (insert from top, slide forward to latch); combination electrical/mechanical latching; fully field replaceable
- Motors: T-Motor F40 Pro III with APC 8x4E propeller
- ESC: Castle DMR 30/40

**Payload/Sensor Design:**
- 5-hole air sampling sensor integrated into nose cone
- Short plumbing runs from nose cone back to avionics board (minimize errors)
- Vertical/tail landing designed to reduce cone damage
- Clogged ports cleanable with stainless steel wire
- Vaisala RSS421 sensor mounted on fuselage side ahead of wing/props for clean airflow
  - Measures: Relative humidity, temperature, pressure
  - Custom interface board for avionics integration
  - Retains factory calibration and self-cleaning features
  - Field replaceable unit
  - Optional protective cover available
  - Shelf life TBD

**Autopilot/Avionics:**
- Integrated charger
- LED-based full UI
- USB programmable flight patterns
- Heated pressure sensor chamber
- Connections for: GPS antenna, radio antenna (optional), laser (optional), scientific payload
- Minimizes external components
- Makes vehicle fully autonomous/stand-alone

### Task 03: In Progress (20% complete)

**Wind Tunnel Testing:**
- Probe calibration using wind tunnel with comprehensive coverage:
  - 900 probe positions
  - ±15° angle of attack (α) & angle of sideslip (β) at 1° intervals
  - >1,000 measurements per position
  - ~10⁶ total measurements
  - 3-hour total runtime
- Completed assessment and calibration of probe
- 9th order polynomial fit provides good results
- Computed cα, cβ, cq coefficients
- Developed automated code for future tunnel data analysis

**Wind Tunnel Results:**
- Cross-validation errors:
  - α: 0.10°
  - β: 0.25°
  - True airspeed (TAS): 0.06 m/s
- Accurate fit with minimal lag during α & β transitions
- Outstanding issues: No tunnel static pressure measurement; probe tip translation in tunnel
- Continuing calibration work with NOAA

**Flight Testing Plans:**
- Approved for operations at DOE Southern Great Plains site (60-m triangular tower)
- Site has 2x daily balloon launches, sonic anemometer, meteorological reference sensors
- 5-day test window planned
- Flight patterns: Various upwind of tower to evaluate biases
- Comparison metrics: Wind speed, wind direction, temperature, pressure, humidity; turbulence capture across scales
- Flights coordinated with radiosonde launches for consistency evaluation
- Partnership with University of Nebraska-Lincoln (Dr. Houston):
  - Combined Mesonet and Tracker near-surface platform for close-proximity intercomparison
  - Profiling rotary-wing UAS (DJI M600P) for additional intercomparison (separately funded UNL research)

## Products & Capabilities Described

### S0 UAS (Atmospheric Sounding Aircraft)
- **What it is:** Small unmanned aircraft designed for autonomous atmospheric profiling and meteorological data collection
- **Design approach:** Tail-landing capable fixed-wing aircraft with integrated sensors and autonomous flight planning
- **Key specifications:**
  - Weight: 1.6 kg
  - Span: 54"
  - Length: 36" (variable with battery)
  - Altitude capability: 10,000+ feet (AF requirement); expandable to 100,000+ feet (research)
  - Flight duration: 40+ minutes (AF requirement); 1+ hour (commercial typical)
  - Launch: Hand launch (standard); balloon tube-launch from altitude (optional for remote operations)
  - Recovery: Tail landing with minimal recovery area (~10 feet)
  - Autonomy: Programmable flight patterns via USB; autopilot override capability

- **Sensor payload:**
  - 5-hole wind probe (integrated nose cone)
  - Vaisala RSS421 (temperature, pressure, relative humidity)
  - Future capabilities: Additional instrumentation slots
  
- **Data output formats:** NetCDF, BUFR, GRIB, text files compatible with weather models and AF data systems

- **Operational advantages:**
  - Field-swappable components (tail, wing, sensors) requiring no reprogramming
  - Sealed against environmental contamination
  - Integrated on-board charger and UI
  - Data collection on recovery or real-time downlink (architecture supports both)

## Use Cases & Applications

### Air Force Applications
- Army tactical weather support (wind, temperature, pressure profiling)
- Special Operations Forces (SOF) meteorological intelligence
- Rapid atmospheric sounding for time-sensitive decision support
- Integration with AF standard data systems and AF Data Center

### Commercial/Research Applications
- Weather research and forecast model validation
- Arctic research operations (with altitude tube-launch capability)
- Hurricane/severe weather monitoring
- Atmospheric turbulence characterization
- Cloud microphysics research (water/ice content)
- Atmospheric chemistry (ozone, SO₂, NOx, methane detection)
- Environmental monitoring (soil moisture, sea ice properties, snow cover)
- Ship-based deployment for maritime research
- CBRNE detection applications
- Surface energy transport studies

## Key Results

### Task 01 Results (100% Complete)
- Comprehensive specifications finalized incorporating AF and commercial requirements
- AF acceptance of requirements documentation
- Customer agreement that specifications meet operational needs
- Extended capability set identified for Phase III potential

### Task 02 Results (90% Complete)
- First prototype aircraft: Design complete, parts ordered
- First prototype avionics/payload: Design complete
- Aerodynamic analysis validated flight characteristics meet design requirements
- Surrogate flight data collected using previous aircraft with similar sensor suite
  - Data converted to NetCDF format
  - Submitted to AF Technical Monitor for evaluation
  - Compared favorably with standard balloon-sonde data from DOE ARM facility

### Task 03 Results (20% Complete - In Progress)

**Wind Tunnel Calibration Completed:**
- Comprehensive probe calibration dataset (~10⁶ measurements)
- Polynomial fit model with excellent accuracy:
  - Angle of attack error: ±0.10°
  - Angle of sideslip error: ±0.25°
  - True airspeed error: ±0.06 m/s
- Minimal lag in transition responses

**Flight Testing Logistics Arranged:**
- DOE Southern Great Plains site approved for operations
- UNL partnership established for ground-truth intercomparison
- Test plan: 5-day evaluation window with multiple flight patterns
- Coordination with twice-daily radiosondes for validation

## Notable Details

### Design Features
- **Tail-landing capability:** Enables recovery in austere environments; reduces vehicle damage
- **Full field replaceability:** Tail, wing, and major sensors swappable without reprogramming—critical for extended remote operations
- **Compact, lightweight design:** 1.6 kg enables diverse launch methods including hand and tube-launch
- **Sealed environmental design:** Dust/dirt-sealed components support desert, Arctic, and other harsh operations

### Technical Innovation
- 3D-printed tail structure with full moving surfaces for tail-landing capability
- Integrated 5-hole probe in nose cone with minimal line runs to reduce measurement error
- Custom interface boards allowing Vaisala commercial sensors to integrate with proprietary avionics
- Automated wind tunnel data analysis tools developed for future calibrations

### Intercomparison Strategy
- Leveraging DOE ARM facility radiosonde launches for direct comparison
- Multi-platform approach: Aircraft, sonic anemometer, mesonet, and rotary-wing UAS enabling turbulence scale assessment
- Partnership with Dr. Houston (UNL) provides established calibration methodology from prior field campaigns

### Schedule Management
- Manufacturing delays acknowledged early in status report
- Clear communication to AF Technical Monitor with mitigation plan
- Surrogate data approach demonstrates technical credibility while awaiting first prototype

### Data Integration
- Designed for seamless integration into operational AF systems
- Support for multiple meteorological data standards (text, BUFR, GRIB, netCDF)
- Real-time or post-recovery data collection options

### Capability Expansion Path
- Extended altitude capability (100,000+ feet) identified as potential Phase III enhancement
- Modular sensor architecture supporting future payload additions
- Autonomous override and manual control balancing efficiency with operational flexibility