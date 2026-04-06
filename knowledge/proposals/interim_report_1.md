# S0 UAS: Air Deployed Solution for Boundary Layer Observations in Turbulent Environments – Interim Report

## Document Metadata
- **Type:** SBIR Phase I Interim Report
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA)
- **Program/Solicitation:** SBIR Phase I, Topic 18-1-10
- **Contract Number:** 1305M218CNRMW0059
- **Date:** September 18, 2018
- **BST Products/Systems Referenced:** S0 (primary), S1, S2, SwiftCore (SwiftPilot, SwiftTab, SwiftStation), Multi Hole Probe (MHP)
- **Key Personnel:** Dr. Jack Elston (Principal Investigator/Project Manager), Dr. Maciej Stachura, Josh Fromm

## Executive Summary

Black Swift Technologies proposes the development and flight validation of the S0, a low-cost, air-deployed unmanned aircraft system (UAS) designed to sample kinematics and thermodynamics of the lower boundary layer in tropical cyclones and other severe weather. Building on BST's heritage with the Aerosonde and Coyote platforms, the S0 aims to achieve an order-of-magnitude cost reduction (targeting ~$5,000 per unit) while maintaining high measurement quality and 2-hour endurance, enabling expanded storm observations and improved tropical cyclone intensity forecasts.

## Technical Approach

### Core Design Philosophy
- **Simplicity-driven architecture:** Single deployable wing using a torsion spring mechanism; minimal moving parts to reduce cost, weight, and complexity
- **Purpose-built for air deployment:** Designed to fit within a 4.61" ID deployment tube (36" long) compatible with standard AXBT drop tubes
- **Weight optimization:** Target maximum gross takeoff weight (GTOW) of 2.5 lbs (vs. Coyote at 13 lbs), achieved through:
  - Custom-designed avionics consolidation (SwiftPilot-based)
  - In-house multi-hole probe (MHP) for wind measurement (~10x lower cost and 4x lighter than Aeroprobe)
  - Integrated thermodynamic and kinematic sensing suite
  - Minimal third-party integrations

### Airframe Design
- **Wing:** 31" × 4.5" planform; MH32 airfoil selected (8.7% thickness) for efficiency, durability, and manufacturability
  - Polars demonstrate suitability for hurricane environments and dynamic soaring capability
  - Wing loading: 103 g/dm² (33.8 oz/ft²)
  - Stall speed: ~12 m/s; cruise speed: 18 m/s
  - Construction: Carbon fiber molded skin with closed-cell foam core for rigidity and durability
- **Fuselage:** Kevlar tube (2" × 24", 72g) selected for RF transparency to enable internal GPS and comms antenna housing
- **Tail:** Fixed, non-deployable design (horizontal: 4.5" × 3"; vertical: 2.75" × 2.5")
  - Static margin: 0.09 (within "good" range of 0.05–0.15)
  - Horizontal tail volume coefficient: 0.39 (within 0.3–0.6 range)
  - Vertical tail volume coefficient: 0.029 (within 0.02–0.05 range)
- **Propulsion:** KDE2306XF-2550 motor with APC 6×4 propeller; thrust-to-weight ratio of 0.81; predicted 10A draw at 18 m/s cruise; ~60+ minutes endurance at sea level; max dash speed 40 m/s (90 mph)

### Avionics & Flight Management
- **Core System:** SwiftCore flight management system
  - SwiftPilot modular autopilot (consolidated into single PCB for S0)
  - SwiftTab user interface
  - SwiftStation ground station
- **PCB Consolidation:** Custom avionics board designed to integrate autopilot, sensor interfaces, and communications in minimal footprint (~20g)
- **Control Architecture:** Pre-programmed flight path with autopilot autonomy; manual teleoperation capability maintained
- **Communications:** 
  - Primary: AVAPS data streaming interface to P-3 aircraft
  - Secondary: COTS short-range, high-bandwidth comms (Bluetooth/WiFi) for pre-flight mission programming via laptop, tablet, or phone

### Sensor Suite & Measurement Package
- **3D Wind Measurement:** BST-developed Multi Hole Probe (MHP)
  - Uses 3D printing for probe, case, and pressure barbs
  - Provides pressure measurements at 5 locations for redundancy
  - ~10× lower cost and 4× lighter mass than commercial alternatives (Aeroprobe)
  - Response time: <1 second
  - Accuracy: 0.5 m/s (horizontal components), 1 m/s (vertical)
- **Thermodynamic Sensors:**
  - Air temperature: ±0.7°C (response <2 sec)
  - Relative humidity: ±5% (response <5 sec)
  - Pressure: ±2.5 Pa (response <1 sec)
- **Oceanographic Sensors:**
  - Laser altimeter (LW20): Aircraft-to-sea-surface measurement ±10 cm
  - Thermal IR sensor: Sea surface temperature ±0.5°C (response <1 sec)
- **Total sensor mass budget:** ~38g (temperature/humidity: 4g, laser altimeter: 20g, SST: 14g, MHP: ~13g)

### Calibration & Validation Strategy
- **Partner:** InterMet Systems (heritage in sonde sensor design and Coyote platform experience)
- **Approach:** Multi-facility validation over 5-week span
  - InterMet facilities for thermodynamic sensor calibration
  - University of Colorado wind tunnel for MHP accuracy validation
  - BST bench testing for integration and data analysis
- **Traceability:** Characterized MHP provides traceable wind measurement without "black box" autopilot filtering

## Products & Capabilities Described

### S0 UAS
- **Purpose:** Air-deployed platform for lower boundary layer observations in severe weather (hurricanes, supercells, etc.)
- **Physical Configuration:**
  - Deployable from standard AXBT tube; stored configuration: 4.61" OD × 36" long
  - Single-wing deployment with torsion spring mechanism
  - Fixed tail configuration
  - GTOW: 2.5 lbs; Mass: 926g predicted
- **Performance:**
  - Endurance: 2 hours at sea level (design goal: 60+ minutes confirmed)
  - Cruise speed: 18 m/s; max dash: 40 m/s
  - Design capability: Flight in up to 160 mph winds, heavy precipitation
  - Deployment/recovery: Air-deployed from manned aircraft; parachute recovery implied for ocean operations
- **Sensor Integration:** Consolidated payload bay accommodating MHP, thermodynamic suite, laser altimeter, thermal IR sensor
- **Cost Target:** <$5,000 per unit for production (Phase I focus on design; Phase II will validate cost)
- **Operational Concept:**
  - Pre-programmed before deployment or in-flight via Bluetooth/WiFi from aircraft
  - Autonomous navigation along programmed path
  - Continuous data streaming via AVAPS interface to host P-3 aircraft
  - Manual takeover capability for emergency control

### SwiftCore Flight Management System
- **Components:**
  - SwiftPilot: Modular autopilot with customizable hardware/firmware
  - SwiftTab: User interface for mission planning and system configuration
  - SwiftStation: Ground station for monitoring and command
- **Application to S0:** SwiftPilot consolidated into single custom PCB; enables rapid integration of new sensors, flight patterns, and control algorithms without third-party dependencies

### Multi Hole Probe (MHP)
- **Innovation:** 3D-printed probe design with improved sensors; ~10× cost reduction vs. Aeroprobe; ~4× mass reduction
- **Measurement:** 5-point pressure array for 3D wind velocity estimation with <1 second response
- **Qualification:** Developed and verified with University of Colorado and NOAA; published comparison against third-party solutions

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Boundary Layer Observations
- **Objective:** Improve tropical cyclone intensity forecasts through targeted in situ measurements of lower boundary layer winds, thermodynamics, and sea surface characteristics
- **Challenge Addressed:** Current platforms (Aerosonde, Coyote) are single-use or high-cost, limiting sampling to single-digit flights per storm; S0 aims to enable 10–20+ flights per storm for enhanced temporal/spatial sampling
- **Data Products:**
  - 3D wind profiles (horizontal and vertical velocity)
  - Air temperature, humidity, pressure (vertical structure)
  - Sea surface temperature and aircraft altitude for gradient estimation
- **Deployment Method:** Air-deployed from NOAA P-3 aircraft via AXBT tube during hurricane reconnaissance missions

### Secondary Applications (Mentioned in Heritage & Future Potential)
- **Severe Convective Storm Penetration:** BST PI has flown supercell rear-flank downdrafts and outflow boundaries; S0 applicable for rapid, multiple-pass sampling
- **Atmospheric Gradient Measurement:** Reduced cost enables formation flight concepts for instantaneous spatial gradient estimation
- **Extended Weather Observations:** Low cost permits broader operational use across NOAA research missions

## Key Results (Phase I to Date)

### Completed Tasks
1. **Kickoff meetings:** NOAA Silver Spring (BST overview) and Boulder (with technical monitor Joe Cione and multi-agency stakeholders: NOAA, NASA, NCAR)
2. **Requirements documentation:** Formal capture of solicitation requirements and project objectives
3. **Risk assessment:** Programmatic and operational risk identification with mitigation strategies (18 technical risks documented with likelihood/consequence matrix)
4. **R/C prototype development & flight test:**
   - Foam-core wing prototype with cardboard tube fuselage
   - Initial propulsion: KDE2304XF-2350 + APC 6×3 propeller (thrust-to-weight 0.51) – underpowered
   - Validation flight at 6,100' density altitude in Colorado
   - Second iteration: KDE2306XF-2550 + APC 6×4 propeller (thrust-to-weight 0.81) – validated flight characteristics with excess power
5. **Airfoil selection & wing design:**
   - MH32 selected over AG25 (thinner, more efficient but MH32 better for manufacturability and stall behavior)
   - Wing dimensions optimized to 31" × 4.5" to fit tube constraint
   - Aerodynamic parameters calculated and verified within design ranges
6. **Avionics PCB block diagram:** Initial design completed; integration from SwiftCore modular framework to reduce development time
7. **Mass budget:** Predicted 926g total mass with 0.4 lbs margin against 2.5 lbs GTOW target

### Financial Status (as of 9/18/2018)
- **Total cumulative costs:** $39,957.65
- **Physical completion:** 34%
- **Budget allocation:**
  - Direct labor: $15,066.96 (157.56 hrs Dr. Elston, 70.03 hrs Dr. Stachura, 73.75 hrs J. Fromm at $50/hr)
  - Travel: $1,333.60 (kickoff meeting)
  - Materials & supplies: $4,545.97
  - Subcontracts: $5,000.00 (InterMet partnership for sensor calibration)
  - Overhead/G&A: $10,378.61 (35% overhead, 5% G&A)
  - Fee: $3,632.51 (10%)

### No Issues Reported
- Risk mitigation strategies in place; schedule on track
- No current impediments to performance or cost

## Notable Details

### Competitive Advantages & Technical Innovation
1. **Cost Leadership:** Target $5,000 per unit vs. $130,000+ for Coyote/Aerosonde; 10× reduction in MHP cost
2. **In-House Ecosystem:** Consolidated autopilot (SwiftPilot), ground station, and sensor design eliminates third-party