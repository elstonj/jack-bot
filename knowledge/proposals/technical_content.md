# NOAA SBIR Phase I Proposal: Air-Deployed UAS for Turbulent Storm Environments

## Document Metadata
- Type: SBIR Phase I Proposal
- Client/Agency: NOAA
- Program/Solicitation: NOAA SBIR 2018, Subtopic 8.2.13
- Date: Submitted January 28, 2018 (created); last modified February 19, 2019
- BST Products/Systems Referenced: S0 (proposed), S2, SwiftCore (SwiftPilot, SwiftTab, SwiftStation), Multi Hole Probe (MHP), Tempest, Coyote
- Key Personnel: Dr. Jack S. Elston (PI, CEO/co-founder), Dr. Maciej Stachura (CTO), Mark Benoit (InterMet, sensor interface), Joshua Fromm (aircraft design)

## Executive Summary
Black Swift Technologies proposes development and flight validation of the S0, a low-cost, air-deployed unmanned aircraft system (UAS) designed to sample the lower atmospheric boundary layer in tropical and extratropical storm environments. The S0 will be deployed from NOAA P-3 aircraft using existing GPS dropsonde or AXBT sonobuoy launch tubes, measure 3D winds and thermodynamic parameters continuously for 2-4 hours at altitudes below 1 km, and transmit data via the one-way AVAPS (Advanced Vertical Atmospheric Profiling System) system. The innovation is achieving an order-of-magnitude cost reduction (~$5,000/unit) compared to existing platforms while maintaining performance through purpose-built design and integrated electronics.

## Technical Approach

### System Design Philosophy
- **Single-piece wing design** with torsion spring deployment mechanism to minimize complexity, weight, and cost
- **Integrated avionics and electronics** consolidating autopilot, sensors, and interfaces onto two circuit boards (avionics board and sensor board)
- **Purpose-built airframe** focused on minimizing weight and manufacturing complexity rather than multi-mission capability
- **Modular sensor integration** leveraging BST's existing SwiftCore avionics ecosystem

### Airframe Specifications (S0 Prototype)
- **Maximum Gross Takeoff Weight (GTOW):** 2.5 lbs target; prototype 2.1 lbs
- **Dimensions:** Stowed in 4.61" ID tube, 36" long (fits AXBT deployment tube with 0.25" clearance)
- **Wing design:** MH-43 airfoil, carbon fiber molded skin with closed-cell foam core, aspect ratio 6.9
- **Fuselage:** Kevlar tube (RF-transparent for internal GPS/comms antennas)
- **Tail:** 3D printed components (NACA0010 airfoil)
- **Cruise speed:** 35 knots; dash speed 60 knots; stall speed 26 knots
- **Propulsion:** KDE1806XF-2350 motor with folding 6x4E propeller
- **Power:** 3S3P 18650 battery pack (112 Wh, 402g)

### Flight Performance
- **Endurance:** 2 hours cruise flight (design goal); minimum 1 hour acceptable depending on cost/unit
- **Altitude:** Designed for operation below 1 km, with capability to operate below 500m
- **Deployment:** Unpowered glide until GPS acquisition; no warm-up required; autopilot stabilizes from any initial orientation
- **Wind environment:** Designed for hurricane-scale wind speeds (5-100 m/s); vertical wind speeds typically ±1 m/s (rarely up to ±20 m/s in extreme updrafts/downdrafts)

### Autonomous Operations
- **One-way communications:** Post-deployment uses only AVAPS receive link (~200 nmi range); no real-time telemetry control
- **Onboard AI/autonomy:** SwiftPilot autopilot performs autonomous flight operations based on pre-programmed mission
- **Mission pre-programming:** Via short-range comms (Bluetooth/WiFi) to laptop, tablet, or phone before or during P-3 flight
- **Data logging:** Onboard hard drive/logger to prevent data loss if AVAPS range drops temporarily

## Products & Capabilities Described

### S0 UAS (Proposed)
**What it is:** A low-cost, disposable, air-deployed fixed-wing unmanned aircraft system purpose-built for atmospheric sampling in severe weather.

**Proposed use:** Deployed from NOAA P-3 aircraft during tropical cyclone, extratropical, and polar storm missions to sample lower boundary layer (below 1 km) for extended periods (2+ hours).

**Key specifications:**
- Weight: 2.1-2.5 lbs
- Cost target: ~$5,000/unit (order of magnitude less than Coyote at ~$50,000+)
- Endurance: 2 hours
- Deployment mechanism: Sonobuoy/AXBT launch tube compatible
- Intended as **disposable/expendable** (air-deployed, not recovered)

### SwiftCore Flight Management System
**Components:** SwiftPilot autopilot, SwiftTab user interface, SwiftStation ground station

**Use in S0 context:**
- Core autopilot will be integrated into modified PCB (consolidation of SwiftPilot into single S0-specific board)
- Provides IMU, static pressure, GPS, servo/motor control
- Capable of full-regime flight control including recovery from inverted flight, stalls, flat spins, spiral dives
- Powers terrain-following capability using laser altimeter (tested to below 15m)
- Features modular radio interface for integration with multiple communication systems

**Notable capabilities:**
- Successfully powered on mid-flight and acquired GPS in flight tests
- Proven in multiple atmospheric science campaigns for NOAA and NASA
- SwiftTab user interface allows simple mission planning without dedicated ground station

### Multi Hole Probe (MHP)
**What it is:** BST-developed 3D-printed wind measurement probe for measuring 3D wind velocity.

**Specifications:**
- Diameter: 2" (matches S0 fuselage)
- 5 dynamic pressure sensors + 1 static pressure sensor
- Data capture rate: 1.0 kHz (downsampled as needed)
- Short, semi-flexible tubing for fast response time
- Cost: ~$500-600 (10x cheaper than Aeroprobe; 4x lighter)
- Mass: 13g
- Integrated electronics housing in 3D-printed body

**Performance validation:**
- Wind tunnel tested against Aeroprobe (industry leader)
- Angular error <1° across range of angles of attack and sideslip
- Velocity accuracy: ±0.5 m/s horizontal components

**Use in S0:** Integrated directly into nose/fuselage as primary 3D wind sensor; electronics consolidated into sensor board.

### Sensor Suite (Integrated)
**Required sensors** (2 Hz minimum; 10 Hz desired data rate):
- Multi Hole Probe (3D wind)
- Temperature sensor (iMet): target accuracy ±0.7°C, <2 sec response time
- Humidity sensor (iMet): target accuracy ±5%, <5 sec response time
- Pressure sensor: target accuracy ±2.5 Pa, <1 sec response time

**Additional sensors (desired):**
- Laser altimeter (LW20): 100m range, ±10cm accuracy, measures aircraft height above sea surface
- Infrared thermometer (Everest MODEL 3800LM): measures sea surface temperature, target ±0.5°C, <1 sec response time

### S2 UAS
**Referenced as:** Predecessor/proof of concept for BST's UAS development capability

**Specifications:**
- 10-foot wingspan
- Max payload: 5 lbs
- Scientific mission platform

**Historical payloads:** L-band radiometer (soil moisture), multispectral camera (Landsat calibration), volcanic plume sensors, P-band radiometer (snow), thermal/hyperspectral packages

**Relevance to S0:** Demonstrates BST's ability to design custom UAS, integrate payloads, and operate in difficult environments (volcanic plumes, etc.). Design tools (XFLR5) and manufacturing expertise directly applied to S0.

### AVAPS Integration
**System:** Advanced Vertical Atmospheric Profiling System (one-way data retrieval system used by NOAA for GPS dropsondes)

**Use in S0:**
- Streams sensor data from S0 back to P-3 via 400 MHz transmitter
- ~200 nmi range capability
- Hardware: Will either procure existing AVAPS interface module or design custom 400 MHz radio module (with InterMet support)
- Software: Firmware added to avionics board to interface with radio; modular radio interface leveraged from SwiftCore heritage

## Use Cases & Applications

### Primary Mission: Hurricane/Tropical Cyclone Sampling
- **Flight profiles:**
  1. Circumnavigate hurricane eyewall: Deploy in calm eye, fly counterclockwise with high-wind region
  2. Spiral inflow: Follow storm currents spiraling into core toward eye/eyewall
- **Historical examples:** Aerosonde flights (2005 Ophelia, 2007 Noel); Coyote flights (Hurricane Edouard, Hurricane Maria)
- **Desired sampling:** Lower boundary layer (below 500-1000m) where ocean-atmosphere energy transfer occurs
- **Improvements over current methods:** 
  - Coyote dropsondes: sparse, instantaneous measurements
  - GPS dropsondes: <500m Doppler wind coverage, sparse temperature/moisture
  - P-3 onboard radar: limited to highest altitudes
  - S0: continuous, extended-duration profiling in lowest layer

### Extratropical and Polar Storm Systems
- Same boundary layer sampling approach applied to non-tropical storms
- Critical for improving forecasting across storm types

### Formation Flight / Gradient Measurement
- Proposed innovation: multiple S0 deployed simultaneously to measure instantaneous atmospheric gradients (Phase II goal, not Phase I)

### Scientific Research Applications (from BST history)
- **Severe convective storms:** Rear-flank downdraft sampling, outflow boundary dynamics (prior Tempest/CoCoNUE work)
- **Boundary layer transitions:** Early-morning convective boundary layer development
- **Arctic operations:** Cold/stable boundary layer characterization
- **Volcanic plume monitoring:** Integration capability demonstrated with S2
- **Wind energy:** Boundary layer profiling for resource assessment

## Key Results (Reports/Validation)

### Phase I Work Plan Outputs (Proposed)
Phase I is a 6-month development effort structured in five work categories:

**C1: S0 Airframe Development & Deployment**
- Prototype construction and flight testing
- Deployment mechanism design/testing
- Composite S0 design and testing
- Expected outcome: Flight-tested S0 design ready for AVAPS integration and storm trials
- Manufacturing capacity: 4 units/day at BST facilities

**C2: Avionics and Sensing Electronics**
- Consolidation of SwiftPilot into S0-specific PCB
- MHP integration and modified design for S0
- Sensor board design (5 dynamic pressure sensors, IR thermometer interface, iMet interface, avionics interface)
- Flight testing to validate autopilot performance equivalence
- Expected outcome: Two consolidated circuit boards ready for integration

**C3: Sensor Calibration and Validation**
- Thermodynamic sensor calibration at InterMet facilities
- Wind tunnel validation of MHP integrated on S0 airframe (comparing to past Aeroprobe benchmarks)
- Flight testing over water for laser altimeter and IR thermometer
- Fully integrated sensor suite validation
- Potential validation near lidar profilers/instrumented towers during Phase II
- Expected outcome: Documented sensor accuracy meeting targets (see Technical Approach section)

**C4: AVAPS Integration**
- Hardware procurement/design of 400 MHz AVAPS interface module
- Integration with S0 avionics board
- Firmware development for radio interface
- Test plan for performance, data streaming, range
- Expected outcome: S0 with functional AVAPS telemetry link

**C5: Mission Planning**
- User interface development for flight path planning
- COTS interface (laptop, tablet, phone) for mission pre-programming
- Options: terrain following, vertical profiling, grid coverage, custom patterns
- Expected outcome: Simple operational planning tool for storm deployment

### Target Sensor Accuracies (Phase I validation goals)