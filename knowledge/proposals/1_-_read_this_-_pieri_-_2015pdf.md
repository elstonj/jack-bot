# Unmanned Aerial Mass Spectrometer Systems for In-Situ Volcanic Plume Analysis

## Document Metadata
- **Type:** Peer-reviewed research article (Journal of the American Society for Mass Spectrometry)
- **Client/Agency:** NASA (multiple centers); Universidad de Costa Rica
- **Program/Solicitation:** NASA Earth Science missions; referenced as supporting materials for NASA 2016 SBIR Phase I Volcano proposal
- **Date:** Published online January 15, 2015; received October 10, 2014
- **BST Products/Systems Referenced:** None directly (this is not a BST document; it is supporting research material)
- **Key Personnel:** Jorge Andres Diaz (Universidad de Costa Rica/GasLab), David Pieri (JPL, PI), Kenneth Wright (INFICON), Paul Sorensen & Robert Kline-Shoder (CREARE LLC), and 13+ others across NASA centers and international institutions

## Executive Summary
This paper describes the development of integrated UAS-mounted mass spectrometer (UAS-MS) systems for in-situ volcanic gas analysis without risking scientist lives. Two UAS-MS configurations were developed—one for mid-sized UAVs (SIERRA) using the Transpector MPH mass spectrometer, and one for small UAVs (VECTOR WING, Helikite) using the miniature Transpector XPR3. Field deployments at Turrialba, Miravalles, and Solfatara volcanoes demonstrated capability for real-time 3D chemical mapping and calibration/validation of satellite remote sensing data.

## Technical Approach

### Core System Architecture
Two integrated UAS-MS payload designs were developed to match different UAV platform capabilities:

1. **UAS-MS-MPH Configuration** (for mid-sized UAVs like SIERRA)
   - Targets platforms with 20–50 kg payload capacity
   - Volume optimized for SIERRA nose compartment
   - Includes MiniGas auxiliary sensor package mounted on side of nose

2. **UAS-MS-XPR3 Configuration** (for small UAVs)
   - Targets platforms with 3–5 kg payload capacity
   - Designed for VECTOR WING 500 and Helikite aerostats
   - Same MiniGas integration approach

### Mass Analyzer Selection
Two INFICON commercial mass spectrometers were selected:

**Transpector MPH (High Performance)**
- Quadrupole analyzer with 6 × 125 mm rods
- Mass range: 1–100 Da
- Scan rate: 10 Hz full spectra (1 ms dwell)
- Max operating pressure: 0.5 mTorr
- Sensitivity: 91 × 10⁻³ A/Torr
- Dynamic range: Nine decades
- LOD: Sub-PPM
- Dimensions: 12.1 × 11.5 × 17 cm
- Mass: 1.4 kg (36% reduction from previous generation)
- Power: 20–30 W typical
- Communication: Ethernet with built-in web server
- Key features: Field-replaceable filament assembly, ion source, EM/FC detector; advanced high-resolution electrometer; RoHS-compliant electronics

**Transpector XPR3 (Miniature)**
- Quadrupole with 18 mm rods
- Mass range: 1–100 Da
- Scan rate: 1 Hz full spectra (8 ms dwell)
- Max operating pressure: 20 mTorr (can operate at higher pressures)
- Sensitivity: 94 × 10⁻³ A/Torr
- Dynamic range: Six decades
- LOD: PPM level
- Dimensions: 14.3 × 12.4 × 17.5 cm
- Mass: 2.3 kg (being re-engineered to ~1 kg)
- Communication: Serial (RS-232/RS-485)
- Key features: Off-axis micro-channel plate electron multiplier for mTorr operation; dual electron energy (40 or 70 eV); two ion chambers for both total and partial pressure measurement

### Vacuum System (Custom-Designed)

**High-Vacuum Subsystem: Miniature Turbo Molecular Drag Pump (MDP)**
- Developer: CREARE LLC
- Mass: 150 g
- Dimensions: 8.4 cm long × 3.4 cm I.D.
- Operating speed: 200,000 rpm
- Power consumption: ~1.5 W at 1 Torr discharge
- Volumetric flow rate: >5 L/s
- Compression ratio (N₂, O₂): >10⁷
- Design life: >1 year; demonstrated 4+ months continuous operation
- Heritage: Similar technology used in NASA's Sample Analysis at Mars (SAM) instrument on Mars Science Laboratory Curiosity Rover

**Low-Vacuum Subsystem: Miniature Scroll Pump**
- Developer: CREARE LLC (under DHS funding)
- Mass: <250 g
- Power consumption: <5 W
- Reduces mass 2–5× and volume 2–3× vs. commercial units through MS-optimized design

**Sample Delivery Subsystem:**
- Small KNF diaphragm pump (KNF 83.3) draws sample gas continuously
- Chamber maintained at constant pressure using critical orifices and flow controllers
- MS inlet samples orthogonally through critical orifice for rapid response
- Second critical orifice for direct sample analysis
- Third pump (KNF 84.4) backs scroll pump

### Complementary Sensor Suite (MiniGas Payload)
Integrated auxiliary instruments:
- SO₂ electrochemical sensor
- H₂S electrochemical sensor
- CO₂ non-dispersive near-infrared sensor
- Temperature sensor
- Pressure sensor
- Relative humidity sensor
- GPS receiver (geo-referencing)
- On-board data storage
- Telemetry system
- Single-board computer (Fit PC3) for data acquisition, storage, and transmission

### Calibration & Validation Approach
- Laboratory pre-deployment calibration using compact sample delivery system with flow/pressure control
- Three NIST-traceable certified calibration gas cylinders (zero-test-span calibration)
- Comparison with simultaneous satellite remote sensing data (ASTER, OMI)
- Integration with ground-based monitoring networks (seismometers, tiltmeters, in-ground gas monitors, MiniDOAS, UV/IR/FTIR cameras)

## Products & Capabilities Described

### Mass Spectrometer Systems
1. **Transpector MPH**
   - Purpose: Core analytical instrument for bulk and trace gas analysis in UAV-MS-MPH payload
   - Application: Mid-sized UAV deployment (20–50 kg capacity)
   - Performance claims: Sub-PPM LOD, 9-decade dynamic range, fast scan (10 Hz), field-replaceable components for harsh environments, improved electronics over previous generations
   - Specifications: See technical approach section above

2. **Transpector XPR3**
   - Purpose: Miniaturized core analytical instrument for small UAV/aerostat deployment
   - Application: Small UAV and tethered aerostat platforms (3–5 kg capacity)
   - Performance claims: PPM-level LOD, operates up to 20 mTorr, designed for integration with small turbo pump, miniaturized footprint
   - Specifications: See technical approach section above

### Miniature Turbo Molecular Pump (MDP)
- Purpose: Provides high-vacuum environment required by mass spectrometers
- Application: Core component of UAS-MS vacuum systems
- Performance claims: World's smallest turbo molecular pump of its kind; proven reliability on Mars Science Laboratory SAM instrument; >10⁷ compression ratio; design life >1 year
- Specifications: 150 g, 8.4 cm long, 3.4 cm I.D., 200,000 rpm nominal, ~1.5 W power

### Miniature Scroll Pump
- Purpose: Roughing (low-vacuum) pump to back the turbo molecular pump
- Application: Reduced-mass, low-power vacuum system for portable applications
- Performance claims: 2–5× mass reduction, 2–3× volume reduction vs. commercial alternatives
- Specifications: <250 g, <5 W power consumption

### MiniGas Auxiliary Payload
- Purpose: Complementary meteorological and chemical measurements
- Application: Integrated with both UAS-MS-MPH and UAS-MS-XPR3 configurations
- Performance claims: Real-time 3D gas concentration mapping; simultaneous measurement of SO₂, H₂S, CO₂, temperature, pressure, humidity, and position
- Specifications: Multiple sensors (electrochemical, non-dispersive IR), GPS, telemetry, embedded PC control

## UAV Platforms Referenced

Three different unmanned platforms were targeted for integration:

1. **SIERRA UAS (NASA Ames Research Center)**
   - Type: Fixed-wing, carbon composite, ~250 kg
   - Endurance: 8–12 hours
   - Range: Up to 965 km
   - Payload capacity: Up to 45 kg
   - On-board power: 1.5 kW
   - Cruise speed: 100 km/h
   - Engine: Single 28-kW pusher configuration (unobstructed nose sampling)
   - Operational altitude: Suitable for volcanic plume sampling
   - Role: Carry UAS-MS-MPH system for mid-altitude systematic plume mapping

2. **VECTOR WING 500 (Universidad de Costa Rica)**
   - Type: Unmanned flying wing, 3.3 m wingspan
   - Endurance: 30 minutes
   - Payload capacity: 4.5 kg
   - Max altitude: 4,500 m ASL
   - Airspeed: 10–30 m/s (typical cruise 18 m/s)
   - Autopilot: Waypoint-guided
   - Predecessor (VECTOR WING 100): 1 kg payload, 45 min endurance, flight-tested 20+ times at Turrialba before/after 2010 eruption
   - Role: Carry UAS-MS-XPR3 system; demonstrates repeated deployment capability

3. **Allsopp Helikite Aerostat (NASA GSFC-WFF, JPL)**
   - Type: Hybrid balloon/kite using buoyancy and aerodynamic lift
   - Volume: 11–16 cubic meters (helium-lifted)
   - Wind tolerance: Up to 64.3 km/h (18 m/s)
   - Power: Battery-based (minimizes tethered winch complexity)
   - Advantage: Stable platform for stationary plume sampling
   - Role: Carry miniaturized MS package for vertical profiling and persistent monitoring

## Use Cases & Applications

### Primary Application: Volcanic Plume Monitoring
**Turrialba Volcano, Costa Rica**
- First UAS-MS deployments: March 2013–October 2014
- Ground deployments: 2003–2006 (AVEMS on manned WB-57 aircraft and Cessna 206)
- Airborne test flights: December 9, 2013 (tethered balloon) and January 23, 2013 (VECTOR WING 100)
- Key achievement: 3D SO₂ concentration mapping showing plume penetration from 3,200–3,550 m AMSL with 350 m thickness; max concentrations 6.7 and 12.5 ppmv SO₂ correlating well with ASTER satellite remote sensing

**Miravalles Volcano, Costa Rica**
- Las Hornillas fumarolic site field testing
- Measurements: CO₂ ~75%, H₂S 168 ppmv, SO₂ 24 ppmv

**Solfatara Volcano, Naples, Italy**
- Bocca Grande fumarole: CO₂ ~86%, H₂S 66 ppmv, SO₂ 13 ppmv
- Bocca Nuova fumarole: CO₂ ~76%, H₂S 68 ppmv, SO₂ 11 ppmv

### Scientific Objectives
1. Detect early warning volcanic hazard indicators through gas emission changes (molecules 1–100 Da