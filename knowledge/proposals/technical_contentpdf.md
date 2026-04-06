# NOAA SBIR Phase I Proposal: S0 UAS Development for Tropical Cyclone Sampling

## Document Metadata
- **Type:** SBIR Phase I Proposal
- **Client/Agency:** NOAA
- **Program/Solicitation:** NOAA SBIR (specific topic number not stated in document)
- **Date:** January 31, 2018 (submission date)
- **BST Products/Systems Referenced:** S0 (proposed), S1, S2, SwiftCore (SwiftPilot, SwiftTab, SwiftStation), Multi Hole Probe (MHP)
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator, CEO/co-founder)
  - Dr. Maciej Stachura (Chief Technology Officer, Flight Authorization Expert)
  - Mark Benoit (InterMet, Sensor Interface and AVAPS Integration)
  - Joshua Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposes to develop the S0, a low-cost, air-deployable UAS designed to sample the lower boundary layer of tropical cyclones and severe storms. The system will provide 3D wind measurements, thermodynamic data (temperature, humidity, pressure), sea surface temperature, and altitude measurements, with a target unit cost of ~$5,000 to enable more frequent storm sampling missions for NOAA. The S0 leverages BST's expertise from the Coyote platform while reducing complexity, weight, and cost through purpose-built design and consolidated avionics.

## Technical Approach

### Airframe Design
- **Target GTOW:** 2.5 lbs (significantly lower than Coyote at 13 lbs)
- **Design philosophy:** Simplified single-piece swiveling wing, reduced complexity to minimize manufacturing and part costs
- **Construction approach:**
  - Wing: Carbon fiber molded skin with closed-cell foam core
  - Tail: 3D printed (for consistency and rapid iteration)
  - Fuselage: Kevlar tube (RF-transparent for internal antenna housing)
  - Propeller: Pusher configuration (rear-mounted to provide undisturbed airstream to nose-mounted sensors)

### Cruise Performance
- **Cruise speed:** 35 knots
- **Dash speed:** 60 knots
- **Stall speed:** 26 knots
- **Endurance target:** 2 hours
- **Wing airfoil:** MH-43
- **Tail airfoils:** NACA0010
- **Aspect ratio:** 6.9

### Air Deployment System
- Aircraft stows in 4.61" ID deployment tube, 36" long (fits in standard AXBT drop tube)
- Single torsion spring for wing deployment (only moving part during deployment phase)
- No warm-up required; aircraft performs unpowered glide until GPS acquisition
- Designed to survive rough handling and strong gusts in storm environments

### Avionics & Electronics
- **SwiftPilot modular autopilot system:** To be consolidated into single custom PCB for S0
- Full flight regime autopilot (recovery from inverted flight, stalls, flat spins, spiral dives, high-speed vertical dives)
- Integrated power regulation, GPS, IMU, static pressure, servo/motor outputs
- Direct interfaces to laser altimeter, AVAPS radio, and sensor board
- Can power on mid-flight and stabilize from any initial orientation

### Sensing Suite
- **3D Wind:** BST Multi Hole Probe (MHP) with 5 dynamic pressure sensors + static pressure
  - 1.0 kHz data capture capability
  - 3D printed probe design (10x lower cost than Aeroprobe, 4x less mass)
  - Previously validated against Aeroprobe with <1° angular error
- **Temperature:** iMet sensor (target accuracy: ±0.7°C, <2 sec response time)
- **Humidity:** iMet sensor (target: ±5%, <5 sec response time)
- **Pressure:** Static pressure transducers (target: ±2.5 Pa, <1 sec response time)
- **Sea surface temperature:** Thermal IR sensor—Everest MODEL 3800LM (target: ±0.5°C, <1 sec response time)
- **Height above water:** Laser altimeter—LW20 (target: ±10 cm range to 100m)

### Mass Budget (Current Design: 2.1 lbs)
| Component | Mass (g) |
|-----------|----------|
| Battery (3S3P 18650GA, 112Wh) | 402 |
| Kevlar Fuselage | 72 |
| MHP | 13 |
| Motor (KDE1806XF-2350) | 22 |
| Wiring/connectors | 40 |
| Speed Controller (KDEXF-UAS20LV) | 16 |
| Propeller (6x4E Folding) | 18 |
| Servos (HS5065MG) | 36 |
| Tail/Motor 3D Print | 52 |
| Wing skin | 102 |
| Wing foam core | 50 |
| Wing mount | 15 |
| Wing deployment spring | 45 |
| Avionics/sensor board | 20 |
| Temperature + humidity | 4 |
| Laser altimeter | 20 |
| IR thermometer | 14 |
| **Total** | **941 g (2.1 lbs)** |

Maximum GTOW margin: 2.5 lbs allows 0.4 lb buffer for design maturation.

### Integration with NOAA Systems
- AVAPS integration: 400 MHz transmitter for one-way telemetry streaming to P3
- Data streaming via AVAPS system to aircraft
- Mission pre-programming via COTS short-range, high-bandwidth communications (Bluetooth or WiFi) using laptop, tablet, or phone
- Programming possible on ground or in-flight from P3

## Products & Capabilities Described

### S0 UAS
- **What it is:** New purpose-built, air-deployable fixed-wing UAS specifically designed for tropical cyclone boundary layer sampling
- **How it was proposed to be used:** Dropped from NOAA P3 aircraft to sample lower boundary layer conditions during hurricane/storm operations
- **Specifications:**
  - 2.5 lb GTOW
  - 2-hour endurance at 35 kt cruise
  - Integrated meteorological sensor suite
  - Deploys from sonobuoy drop tube via AXBT
  - Seals for reliable operation in most weather (except icing)
  - Can float and transmit data if mission allows
  - Durable construction for rough handling and strong gusts

### SwiftCore Flight Management System
- Comprises: SwiftPilot autopilot, SwiftTab user interface, SwiftStation ground station
- **Capability:** Modular avionics architecture enabling rapid sensor integration and control algorithm modification
- **Application:** Core flight control and management for S0

### Multi Hole Probe (MHP)
- **What it is:** BST-developed 3D-printed probe for accurate 3D wind measurement
- **Performance:** 
  - Accuracy: 0.5 m/s horizontal, 1 m/s vertical components
  - Comparable performance to Aeroprobe (validated wind tunnel testing <1° angular error)
  - 10x lower cost than Aeroprobe
  - 4x less mass than lightest Aeroprobe
- **Application:** Primary wind sensing component for S0

### InterMet Subsystems (via Subcontractor)
- Humidity/temperature/pressure calibration systems
- Expertise in radiosonde sensor design
- AVAPS radio module design/integration support

## Use Cases & Applications

### Primary Mission
- **Tropical cyclone intensity forecasting:** Targeted observations of hurricane lower boundary layer to improve forecast models and intensity predictions
- **In situ measurements:** Gathering kinematic and thermodynamic data at multiple points per storm to improve temporal and spatial sampling
- **Lower boundary layer observations:** Specifically the near-surface region critical to understanding storm dynamics and sea surface interaction

### Specific Measurement Objectives
- 3D wind field characterization in tropical cyclones
- Temperature and humidity profiles
- Sea surface temperature and height variations
- Pressure field mapping
- Formation flight capability (future) for instantaneous gradient measurements

### Operational Context
- Air deployment from NOAA P3 aircraft operating in/near hurricanes
- Multiple aircraft per storm (increasing frequency from "single digit" to systematic multi-point sampling)
- Operations in "difficult atmospheric conditions commonly encountered in convective storms"

### Future/Phase II Applications (Planned)
- High altitude testing (up to 14,000 ft in Colorado, expecting 30,000 ft operational ceiling)
- Extreme weather flight testing (heavy precipitation, strong winds/gusts)
- Intelligent sampling algorithms (sensor-driven autonomous navigation)
- Energy harvesting for extended flight time

## Phase I Technical Objectives

1. **Cost target:** Keep unit price near $5,000 to enable routine operations
2. **Sensing:** Accurate 3D winds (MHP) + temperature, humidity, pressure
3. **Additional sensing:** Laser altimeter + thermal IR for sea surface characterization
4. **Endurance:** 2-hour cruise flight capability
5. **AVAPS integration:** Stream data back to P3 aircraft
6. **Mission interface:** Simple user interface for in-air pre-programming
7. **Phase II enabler:** Develop foundation for intelligent sampling and energy harvesting

## Phase I Work Plan (6-month duration)

### C1: S0 Airframe Development & Deployment
- Build and flight-test prototype based on aerodynamic design
- Design and test deployment mechanism (single torsion spring)
- Design deployable composite S0 based on prototype
- Test mature composite aircraft
- **Testing location:** Pawnee National Grasslands, northeastern Colorado
- **Manufacturing capacity:** 4 units/day (long-term); expandable via manufacturing partners

**Key tasks:**
- Prototype construction using modern production techniques
- Flight testing for aerodynamic validation, speed, endurance, range
- Deployment mechanism design for AXBT tube compatibility
- Rapid build-test-iterate cycle (inspired by S2 development success)

### C2: Avionics & Sensing Electronics
- Consolidate SwiftPilot into single custom PCB for S0 (eliminating modularity overhead)
- Integrate: IMU, static pressure, GPS, servo/motor outputs, laser altimeter interface, AVAPS radio, sensor board interface
- Develop and test MHP circuit board (modify existing BST design)
- Develop sensor board with interfaces to: 5 dynamic pressure sensors, static pressure, IR thermometer, iMet sensor suite
- PCB design at BST offices; manufacturing at Advanced Assembly (Colorado-based)

### C3: Sensor Calibration & Validation
- **Temperature/humidity/pressure:** Calibration at InterMet facilities using their established systems
- **MHP wind measurement:** Wind tunnel testing at University of Colorado
  - Validate integrated MHP performance on S0 airframe
  - Expand on past work comparing BST MHP to Aeroprobe
  - Ensure accuracy maintained when mounted on aircraft
- **Laser altimeter:** Flight testing over water, validate 100m range
- **IR thermometer:** Lab testing against calibrated reference, water trials
- **Integrated sensor suite:** Full flight testing to validate all instruments reporting and recording correctly
- **5-week timeline** for calibration/validation tasks

### C4: AVAPS Integration
- Hardware procurement/development for 400 MHz transmitter
- Integration with avionics board (add to PCB layout, firmware interface)
- Software development for radio interface (leveraging modular SwiftCore architecture)
- Test plan for performance, data streaming, range validation
- **Partnership:** Leverage established relationship with NCAR MIST Sonde team (experienced with AVAPS systems)

### C5: Mission Planning
- Develop simple-to-use system for pre-programming flight paths and sampling missions
- Enable operator programming via intuitive COTS interface (eliminates need for dedicated ground station)
- Allow pre-mission programming on ground OR in-air shortly before deployment
- Coordinate with Technical Monitor on CONOPS specifics
- Current mission planning options available: terrain following, vertical profiling, grid coverage
- Result: System sufficient to enable S0 flight operations

## Notable Details

### Unique BST Capabilities Leveraged
1. **Certified in-house autopilot** (SwiftPilot) with full flight regime recovery capabilities
2. **Propri