# 2018 NOAA Phase II Hurricane UAS Proposal

## Document Metadata
- **Type:** SBIR Phase II Proposal
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration)
- **Program/Solicitation:** NOAA SBIR Phase II, Proposal Number: SBIR-2018-082013
- **Date:** Submitted February 2019 (based on file modification date of March 1, 2021)
- **BST Products/Systems Referenced:** S0 (S/zero), RD-41 sonde, SwiftCore, SwiftPilot autopilot, SwiftTab UI, SwiftStation ground station, S2, Penguin BE, Coyote UAS
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator)
  - Dr. Maciej Stachura (Lead Engineer)
  - Josh Fromm (Aircraft Design and Integration)

## Executive Summary
Black Swift Technologies proposes development and flight validation of the S0, a low-cost, air-deployable UAS designed specifically for boundary layer observations in hurricanes. The S0 will measure 3D winds, temperature, humidity, pressure, sea surface temperature, and aircraft altitude while achieving 1-2 hours endurance and costing approximately $5,000 per unit to enable multiple deployments per storm. The system integrates the proven RD-41 sonde with custom BST avionics and uses AVAPS for data transmission, mirroring existing NOAA operational procedures.

## Technical Approach

### Core Architecture
- **Air-deployed tube-launched UAS** designed to fit within existing NOAA P3 drop tubes (similar to sonobuoy/AXBT deployment)
- **Target GTOW:** 2.5 lbs (significantly lighter than Coyote at 13 lbs)
- **Single swiveling wing** design for simplicity and manufacturability
- **Design philosophy:** Purpose-built for hurricane observation only (not ISR or other missions), reducing complexity and cost compared to Aerosonde/Coyote platforms

### Sensing Suite
1. **RD-41 Sonde Core** (Vaisala): Pressure, temperature, humidity integration
2. **Multi-Hole Probe (MHP)** (custom BST design): 3D wind measurement with 5-hole configuration
   - CFD-validated, wind-tunnel tested design
   - Integrated directly into fuselage nose
   - Plan to address water droplet bridging risk via heating, widening holes, or drainage
3. **Laser Altimeter:** Aircraft-to-sea-surface distance measurement (previously flown on other BST aircraft)
4. **Thermal IR Sensor:** Sea surface temperature measurement
5. **Custom Avionics Board:** Purpose-built control and sensor interface based on SwiftCore platform

### Avionics & Flight Control
- **Autopilot:** Custom BST SwiftPilot system with integrated autopilot, ESC (Electronic Speed Controller), servo control
- **Propulsion:** Single motor with swiveling propeller
- **Battery:** Sized to optimize endurance/weight trade
- **User Interface Panel:** Waterproof external panel with USB programming port, status LEDs, charge port
- **Firmware:** Modified SwiftCore firmware for new avionics board, external interfaces, and automated release detection

### Communications & Data Transmission
- **System:** AVAPS (Atmospheric Vertical Atmospheric Profiling System) - one-way radio link from S0 to P3
- **Innovation:** GPS removed from sonde; autopilot emulates GPS packets and inserts additional sensor data into alternate message frames
- **Advantage:** No post-deployment command/control link needed; downstream hardware requires only post-processing software changes, not hardware modifications
- **Antenna:** Integrated into 3D-printed tail section; vertically polarized during flight

### Automated Guidance Algorithm
- **Autonomy Level:** Fully autonomous navigation post-release; no operator intervention possible post-deployment
- **Phase I Demonstration:** Used simulated hurricane data from NCAR (George Bryan) combined with on-board atmospheric sensors to achieve automated eyewall location in high-fidelity simulations
- **Navigation Basis:** Primarily pressure-based control strategy (gradient descent to eyewall edge); wind acts as passive controller pushing aircraft toward eyewall
- **Phase II Goals:** 
  - Validate simulation data against actual Coyote observations
  - Expand algorithm using additional sensor parameters (wind, humidity, temperature)
  - Conduct Monte Carlo simulations targeting 99% success rate for eyewall navigation from nearby drop zones

## Products & Capabilities Described

### S0 UAS
**What it is:** Lightweight, air-deployable, tube-launched fixed-wing UAS optimized for hurricane boundary layer sampling

**Specifications (target):**
- Maximum Gross Takeoff Weight: 2.5 lbs
- Endurance: 1-2 hours cruise at 5,500' MSL elevation
- Target achieved: 60+ minutes demonstrated in Phase I
- Phase II goal: 90 minutes at design weight
- Airfoil: MH32 (tested, aerodynamic polish ongoing)
- Single-piece composite wing
- 3D-printed tail section

**Sensor Accuracy Requirements:**
- Air temperature: ±0.1°C accuracy, 0.5 sec response time
- Humidity: ±2% accuracy, 0.3-10 sec response time
- Pressure: ±0.4 hPa accuracy, <0.1 sec response time
- 3D wind velocity: ±0.5 m/s horizontal, ±1 m/s vertical, <1 sec response time
- Sea surface temperature: ±0.5°C, <1 sec response time
- Altitude: ±10 cm measurement accuracy

**Deployment Mechanism:**
- Fits within NOAA P3 sonobuoy tube (~3" diameter constraint)
- Parachute system for safe descent before aircraft motor start
- Mechanical release system for deployment
- Rugged enough to survive drop-test conditions

**Target Cost:** $5,000 per unit (order of magnitude reduction vs. Coyote/Aerosonde)

### RD-41 Sonde Integration
- Vaisala sonde core adapted for aircraft mounting
- Maintains proven sensor reliability and characterization
- Pod-mounted design allows swappable sonde units
- Protected cap design (matching dropwindsonde practice)

### Multi-Hole Probe (MHP)
- 5-hole design for 3D wind sensing
- Integrated into aircraft nose
- 3D-printed probe case and pressure barbs
- ~10x lower cost than Aeroprobe equivalent
- ~4x lighter than lightest Aeroprobe option
- Water droplet bridging risk mitigation strategies under development

### SwiftCore Flight Management System
- SwiftPilot autopilot: Modular, certified, BST-developed
- SwiftTab UI: Tablet-based mission planning interface
- SwiftStation: Ground station software
- Custom-built for this platform (not commercial COTS)

## Use Cases & Applications

### Primary Mission: Hurricane Boundary Layer Sampling
- **Objective:** Improve tropical cyclone intensity forecasts through targeted in situ measurements
- **Target Altitude:** Lower boundary layer (near sea surface)
- **Target Location:** Eyewall region (high-wind, low-pressure core)
- **Operational Concept:** Mimics existing dropwindsonde operations; designed to integrate seamlessly into current NOAA hurricane reconnaissance procedures
- **Key Advantage:** Multiple S0s per storm (vs. single-digit Coyote flights) enables enhanced temporal/spatial sampling

### Secondary Applications (mentioned as future potential):
- Formation flight testing (instantaneous atmospheric gradient measurements)
- Land-based severe convective storm sampling (BST historical expertise)
- Volcano plume monitoring (referenced as BST prior experience)
- Mountainous terrain operations (referenced as BST prior experience)

### Environmental Conditions:
- Severe turbulence in hurricane boundary layer
- Heavy precipitation and water ingestion risk
- High wind speeds (near hurricane force)
- Sea surface operations (corrosion environment)
- Extreme thermal environment

## Key Results (Phase I Accomplishments)

### Prototype Development & Flight Testing
- Successfully built and flew multiple S0 prototypes
- Demonstrated 60+ minute autonomous flight times at full weight
- Achieved stable autonomous flight in turbulent conditions
- Demonstrated automatic control loop tracking capability
- Multiple successful local test flights near BST (Colorado area)

### Component Integration
- **RD-41 Sonde:** Successfully integrated into aircraft pod; secured Vaisala supply commitment
- **Multi-Hole Probe:** CFD analysis completed; wind tunnel testing validated frequency response for angle-of-attack/sideslip measurements; flight testing of initial design completed
- **AVAPS Integration:** Demonstrated successful data transmission via GPS packet emulation technique; method validated for streaming additional sensor data
- **Autopilot:** Custom avionics designed integrating MHP sensors, sonde interface, AVAPS radio; demonstrated reliable autonomous operation

### Automated Guidance Algorithm
- **Simulation Architecture:** Built integration between BST aircraft simulator and NCAR hurricane weather models
- **Proof of Concept:** Demonstrated automatic eyewall location using pressure-based guidance in 3 hours of simulated storm data
- **Algorithm Basis:** Pressure gradient descent; wind passive control; tested with local sensor measurements only

### Design Validation
- Prototype confirmed ability to fit within deployment tube
- Wing swivel deployment mechanism designed in 3D CAD
- Antenna characterization completed (RF measurements in anechoic chamber)
- RD-41 sensor integration validated
- Aerodynamic baseline established (MH32 airfoil performance confirmed)

### Risk Mitigation Achievements
- Addressed communications reliability (switched from two-way command/control to one-way AVAPS)
- Addressed sensor reliability (chose proven RD-41 core instead of iMet sensors based on Coyote experience feedback)
- Addressed autonomous navigation (developed and validated simulation-based guidance algorithm)

## Notable Details

### Competitive Advantages vs. Aerosonde/Coyote
1. **Cost:** Target $5,000 vs. much higher existing platform costs (order of magnitude reduction claimed)
2. **Simplicity:** Single swiveling wing vs. complex deployable tail/fin systems
3. **Weight:** 2.5 lbs vs. 13 lbs (Coyote) – allows smaller deployment mechanism
4. **Specialization:** Purpose-built for hurricane sampling only (vs. general ISR platforms)
5. **Integration:** In-house avionics, autopilot, MHP, ground station (vs. reliance on third-party components)

### Manufacturing & Commercialization Focus
- Extensive use of 3D printing for rapid iteration and cost reduction
- Composite wing construction using production molds (manufacturing planned at Northwind Composites)
- Custom cable assembly design in progress to reduce cost and lead time
- Build procedures and QC processes under development for Phase II completion
- Partnership with Vaisala for RD-41 sonde supply

### Key Partnerships & Resources
- **NOAA AOC (Aircraft Operations Center):** Coordination for P3 integration and flight permissions
- **NCAR (National Center for Atmospheric Research):** George Bryan providing hurricane simulation data and meteorological guidance
- **Vaisala:** RD-41 sonde supply commitment
- **Northwind Composites:** Wing production
- **University of Colorado:** Prior collaboration on MHP validation

### Operational Integration
- **CONOPS:** Designed to match existing dropwindsonde operations (reduce operator workload)
- **Ground Station:** Leverage existing AVAPS ground stations at NOAA facilities
- **Data Format:** Post-processing software adaptation only (no AVAPS hardware modifications)
- **Flight Planning:** Tablet-based UI to integrate P3 radar/reflectivity data for initial flight plan creation

### Phase II Specific Objectives
1. **Design Refinement:** Aerodynamic optimization (target 90-min endurance), wing/tail design finalization, antenna integration
2. **Electronics:** Production avionics PCB manufacture, firmware development, sensor integration and calibration
3. **Algorithm Development:** Validation against real Coyote data, Monte Carlo simulations (99% success target), robust guidance algorithm
4. **Deployment Systems:** Tube design finalization, parachute system, mechanical release testing, AOC requirement compliance
5. **Flight Testing:** Local iterative testing, severe weather Colorado tests, launch tube deployment tests, P3 integration flights
6. **Documentation:** CONOPS document, system specification, build procedures, QC processes

### Budget & Schedule
- **Phase II Duration:** 24 months (June 2019 – August 2021