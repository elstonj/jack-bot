# SBIR Phase I Interim Report: S0 UAS Air-Deployed Boundary Layer Observation System

## Document Metadata
- **Type:** SBIR Phase I Interim Report
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA)
- **Program/Solicitation:** NOAA SBIR 18-1-10
- **Contract Number:** 1305M218CNRMW0059
- **Date:** November 14, 2018
- **BST Products/Systems Referenced:** S0 UAS (primary focus), S1, S2, SwiftCore (SwiftPilot autopilot, SwiftTab UI, SwiftStation ground station), Multi Hole Probe (MHP), Penguin BE platform
- **Key Personnel:** Dr. Jack Elston (Principal Investigator/Project Manager), Dr. Maciej Stachura, Josh Fromm

## Executive Summary
Black Swift Technologies is developing the S0, a low-cost, air-deployed unmanned aircraft system designed to sample boundary layer kinematics and thermodynamics in tropical cyclones and severe storms. This interim report documents Phase I progress (67% complete as of November 2018) toward producing an aircraft priced near $5,000 per unit with 2-hour endurance, capable of measuring 3D winds, temperature, humidity, pressure, sea surface temperature, and altitude while integrating with NOAA's AVAPS telemetry system.

## Technical Approach

### Design Philosophy
The S0 is purpose-built for air deployment from NOAA P-3 Orion aircraft via modified AXBT (air-expendable bathythermograph) drop tubes. Key design drivers:
- **Extreme weight reduction** (target 2.5 lbs GTOW, achieved 2.25 lbs in production design) to enable simple, single-moving-part deployment
- **Single folding wing** mechanism using torsion spring for deployment
- **Consolidated avionics** using BST's proprietary SwiftCore ecosystem to eliminate third-party autopilot/air data probe integration
- **In-house manufacturing** (3D printing for tail and avionics tray) to reduce cost and improve repeatability
- **Modular sensor approach** enabling quick integration of new instruments

### Deployment Configuration
- Aircraft packed in 4.61" ID × 36" long G10/FR4 tube fitting standard AXBT chute liners (5.25" nominal ID)
- Parachute in rear of tube slows descent
- Aircraft released by gravity, wing pivots to locked flight position
- No pre-deployment warm-up required; performs unpowered glide until GPS acquisition
- SwiftPilot autopilot stabilizes from any initial orientation

### Airframe Specifications
| Component | Specification |
|-----------|---------------|
| **Wing** | MH32 airfoil, 30.5" span, 4.5" chord, spread tow 160GSM carbon fiber with foam fill, dual full-span flaperons, Hoerner wingtips |
| **Empennage** | Entirely 3D printed (PA2200 nylon), NACA 0010 airfoil, all-moving horizontal surface, no rudder |
| **Fuselage** | 1-ply Kevlar tube, 2" ID × 2.03" OD, 29" long (RF-transparent for internal component mounting) |
| **Propulsion** | KDE 2306XF-2550 motor, 7×4 folding propeller |
| **Performance** | Cruise speed 35 knots, dash speed 58 knots, 2-hour endurance, cruise power 60W |

### Avionics & Electronics
**SwiftCore Integration:**
- SwiftPilot modular autopilot (flight-tested to recover from inverted flight, stalls, flat spins, spiral dives, high-speed vertical dives)
- Custom combined avionics PCB with pressure sensors, temperature/humidity interface, laser altimeter interface, GPS, magnetometer
- Full flight regime capable; terrain-following capability down to <15m using laser altimeter
- Battery: 3S3P Li-ion (Sanyo NCR18650GA), 111.6 Wh

## Products & Capabilities Described

### S0 UAS
**What it is:** Purpose-built, expendable, air-deployed small UAS for lower boundary layer meteorological sampling in severe weather.

**Proposed use in this contract:** 
- Primary platform for NOAA tropical cyclone and severe convection research
- Increases observation frequency (currently single-digit flights per storm → multiple deployments per mission)
- Reduces per-aircraft cost to enable routine operations

**Specifications/Performance Claims:**
- Unit cost target: ~$5,000
- Maximum gross takeoff weight: 2.25 lbs
- Endurance: 2 hours nominal cruise
- Airframe ruggedness: designed to survive extreme turbulence and precipitation
- Deployment tube compatible with standard P-3 Orion AXBT chutes

### SwiftCore Flight Management System
**Components:**
- **SwiftPilot:** Modular autopilot with full flight envelope authority
- **SwiftTab:** User interface for mission programming (target: COTS tablet/laptop with Bluetooth/WiFi)
- **SwiftStation:** Ground station software
- **Proprietary MHP:** 3D-printed multi-hole probe for 3D wind measurement (10× cheaper than Aeroprobe, 4× lighter)

**Capabilities:**
- In-house wind measurement with 0.5 m/s horizontal, 1 m/s vertical accuracy
- Reduced cost vs. commercial solutions (Aeroprobe)
- Improved vertical wind component accuracy vs. autopilot estimates
- Traceable wind measurement methodology (vs. "black box" autopilot filtering)

### Sensor Suite
1. **Multi Hole Probe (MHP):** 5 dynamic pressure + static pressure ports for 3D wind
2. **Vaisala RD94 Radiosonde:** Temperature, humidity (integrated on S0)
3. **Laser Altimeter:** Range measurement to water surface (100m range)
4. **Infrared Thermometer:** Sea surface temperature measurement
5. **Pressure/Temperature/Humidity Board:** Integrated sensor conditioning

### AVAPS Integration
- Custom radio receiver + decoding box (sourced through NCAR) receives and parses sonde telemetry
- JSON message format for easy parsing by ground computer
- Enables real-time data streaming to P-3 during flight
- Solution developed to replace unavailable full AVAPS rack

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Intensity Forecasting
- Sample lower boundary layer kinematics and thermodynamics during hurricane/cyclone intercepts
- Improve forecast accuracy through increased observation density (temporal and spatial sampling)
- Targeted in situ measurements of wind, pressure, temperature, humidity, sea surface conditions
- Multiple deployments per storm enable gradient measurements

### Secondary Missions Mentioned
- Supercell thunderstorm penetration (rear flank downdraft, outflow boundary observations)
- Mountainous region operations
- Volcanic plume monitoring
- Formation flight for instantaneous gradient measurements

## Key Results (Phase I Progress)

### Completed Work (as of November 2018)
1. **Aircraft Development:**
   - Functional prototype constructed (1.94 lbs, cardboard fuselage for cost-effective iteration)
   - Production airframe design finalized (2.25 lbs)
   - All major components manufactured: 3D-printed tail, carbon fiber wing, Kevlar fuselage
   - Deployment tube design finalized (4.94" OD G10/FR4 tube, 36" long)
   - Parachute deployment mechanism designed (based on AXBT methodology)

2. **Avionics & Electronics:**
   - SwiftPilot autopilot core schematic completed
   - Sensor interface schematic completed (pressure sensors, GPS, magnetometer)
   - Sensor selection finalized after wind tunnel validation
   - PCB design underway (final layout pending battery management & mechanical details)

3. **Sensor Validation:**
   - BST MHP validated in wind tunnel against industry-standard Aeroprobe
   - Angular error <1° for both sensors
   - Velocity measurement accuracy confirmed at 0.5 m/s
   - New pressure sensor suite selected after evaluating initial options
   - Comprehensive test procedures documented for pressure, temperature, humidity, wind, ocean temperature, altitude

4. **AVAPS Integration:**
   - Workaround solution implemented: radio receiver + NCAR-provided decoding box
   - JSON telemetry format verified
   - System ready for ground and flight testing

5. **Mission Planning:**
   - Identified terrain following, vertical profiling, grid coverage capabilities
   - Target: simple COTS interface for operator mission programming

### Budget & Schedule
- **Cumulative costs incurred:** $79,915.30 (as of Nov. 16, 2018)
- **Physical completion:** 67%
- **Remaining Phase I tasks:** Autonomous prototype flight testing, AVAPS transmission validation, mission planning interface finalization, Phase II planning & risk mitigation

## Notable Details

### Competitive Advantages & Innovation
1. **Cost reduction:** Target $5,000/unit vs. existing platforms (Aerosonde, Coyote ~$13k)
2. **Custom MHP:** 10× cheaper, 4× lighter than Aeroprobe standard
3. **Integrated avionics:** SwiftCore ecosystem eliminates expensive third-party autopilot/sensor integration
4. **Simplified deployment:** Single moving part (folding wing) reduces complexity, weight, failure modes
5. **RF transparency:** Kevlar fuselage allows internal mounting, improves aerodynamics
6. **3D manufacturing:** Repeatable production of complex shapes (tail, avionics tray) reduces assembly labor

### Key Partnerships & Resources
- **InterMet Systems:** Sensor calibration expertise, sonde heritage
- **University of Colorado (CU) & NOAA ATDD:** Wind tunnel validation of MHP
- **NCAR:** Sonde telemetry decoding solution, safety mechanism consultation
- **Vaisala:** Temperature/humidity sensor specifications, dropsonde integration
- **AOC (Aircraft Operations Center likely):** Deployment tube launching methodology
- **Terry Hock (NCAR):** Safety case development for airborne launches

### Regulatory/Operational Constraints Addressed
- Fits existing AXBT chute liners (P-3 Orion compatibility)
- Parachute deployment for controlled descent
- Water-resistant fuselage design for water landing
- SwiftPilot full-envelope recovery capability (inverted flight, stalls, spins) for safe mid-air activation
- Thorough pre-deployment testing procedures (airframe waterproofing spray test, bench avionics testing, sensor calibration in controlled chambers)

### Technical Milestones Remaining (Phase I)
1. Autonomous flight of cardboard prototype (validating aerodynamics & SwiftPilot control)
2. AVAPS data transmission testing via sonde radio link
3. Mission planning interface design & user testing
4. Sensor integration & validation in environmental chamber (pressure, temperature, RH testing per ISA conditions table)
5. Wind tunnel testing of final airframe with mounted MHP
6. Flight testing of fully integrated sensor suite
7. Phase II risk assessment & mitigation planning

### Design Maturity Notes
- Prototype weight (1.94 lbs) below production design (2.25 lbs), indicating margin
- Airframe design ready for manufacturing
- Avionics PCB design nearing completion (awaiting final layout)
- Sensor suite proven in components; system integration underway
- Testing procedures detailed and grounded in established standards (NIST traceability, wind tunnel methodology, atmospheric chamber protocols)