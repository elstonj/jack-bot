# Cooperative Wind Sensing SBIR Phase I: System Design - Apollo UAS Report

## Document Metadata
- Type: SBIR Phase I Final Report
- Client/Agency: NASA
- Program/Solicitation: NASA 2014 SBIR (Cooperative Wind Sensing topic)
- Date: December 2014 (created 12/12/2014, modified 12/19/2014)
- BST Products/Systems Referenced: Apollo UAS (airframe), CAPS (Cooperative Atmospheric Profiling System)
- Key Personnel: 
  - Prof. Brian Argrow (University of Colorado) - aerodynamic analysis and design modifications
  - Prof. Lawrence (University of Colorado) - inclement weather modifications
  - Coby Leuschke (Rocketship Systems Inc.) - payload bay design and modifications
  - CGLusky (editor/likely BST PI)

## Executive Summary

This Phase I report documents the detailed assessment and design modifications of the Apollo aircraft (a forward-swept flying wing from Rocketship Systems) as the platform for the Cooperative Atmospheric Profiling System (CAPS). BST conducted aerodynamic analysis, designed weather-resistant modifications, and developed modular payload bay interfaces to enable the Apollo to operate as a robust, portable atmospheric sensing platform capable of autonomous launch/landing, deployment in adverse weather, and rapid payload swapping in field conditions.

## Technical Approach

### Aerodynamic Analysis & Performance Validation
- **Method**: Full Navier-Stokes CFD simulations using CD Adapco Star CCM+ flow solver
- **Scope**: Analyzed two wing configurations (54-inch and 102-inch span) across range of angles of attack through deep stall
- **Analysis**: 
  - Derived coefficient of lift (CL) and drag (CD) from CFD at nominal flight speed of 25 m/s
  - Performed standard unaccelerated flight performance analysis using battery-powered sUAS formulation (Traub 2011)
  - Included simple battery model with actual battery parameters (5000 mAh, 16.8 V)
  - Calculated endurance, stall speeds, rate of climb, power required

### Inclement Weather Modifications
- **Sealing approach**: Static facial O-ring seals compressed between module interfaces using draw latches/straps
  - O-ring specification: 0.100" nominal diameter medium-density neoprene cord in 0.125" wide × 0.080" deep gland
  - Design based on standard mechanical compression sealing techniques
- **Thermal management**: Aluminum and conductive thermoplastic heat sinks; IP67-rated vents with waterproof/breathable membranes; removable plugs for extreme cold
- **Water ingress prevention**: Water trap in pneumatic pitot-static system with manual drain valve
- **Wind capability analysis**: Reviewed existing RECUV NexStar UAS flight data from 30 Sep 2009 thunderstorm intercept (winds 20-25 m/s) to inform design

### Modular Payload Bay Design
- **Approach**: Modified Apollo nose cone with standardized mechanical and electrical interfaces
- **Two payload configurations developed**:
  1. **MHP (Meteorological Measurement Pod)**: Optimized for 2-inch diameter aluminum dome wind sensor; >3000 cm³ volume
  2. **Volcanic Observation**: 8" × 4" × 3" (20 × 10 × 7.5 cm) module for atmospheric gas and particulate sensors

**Mechanical Interface**:
- CNC-machined thermoplastic bulkhead with O-ring facial seal, carbon fiber reinforcement pins, draw latch mechanism
- Tool-free assembly/disassembly

**Electrical Interface**:
- Molex EXtreme Ten60Power modular connector on custom PCB
- Configuration: 2 power blades (60 amps each) + 15 signal pins (5 amps each)
- Modular design allows rapid reconfiguration for different payloads

**Center of Gravity Management**:
- Rail system for longitudinal battery repositioning to accommodate different payload weights without ballast

## Products & Capabilities Described

### Apollo UAS Aircraft
**Design basis**: Forward-swept flying wing from Rocketship Systems; extensively tested "Nurf" scale prototype proven rugged in wind gusts >13 m/s

**Functional Requirements Addressed**:
- Rugged autonomous launch/flight/landing capability
- Hand launch portability
- Safe landing on unimproved sites with rapid battery exchange
- Modular payload bay with quick-swap capability
- Complete transport in ruggedized boxes

**Technical Specifications Validated**:
- **54-inch wing configuration**:
  - Wing planform area: 0.353 m² (547 in²)
  - Aspect ratio: 4.9
  - Mean aerodynamic chord: 0.280 m (11.0 in)
  - Reynolds number: 2.14 × 10⁵
  - Wing loading: 75.6 N/m² (25.3 oz/ft²) at 2.97 kg max weight
  - Stall speed: 11.2 m/s (sea level), 13.0 m/s (10,000 ft)
  - Maximum speed: 36 m/s (81 mph) sea level, 40 m/s (90 mph) @ 10,000 ft
  - Maximum endurance: 1.2 hours @ sea level, 1.0 hour @ 10,000 ft
  - Rate of climb @ 30 m/s, 10,000 ft: 11 m/s

- **102-inch wing configuration**:
  - Wing planform area: 0.724 m² (1122 in²)
  - Aspect ratio: 10.2
  - Mean aerodynamic chord: 0.257 m
  - Reynolds number: 2.11 × 10⁵
  - Wing loading: 36.9 N/m² (12.3 oz/ft²) at 2.97 kg max weight
  - Stall speed: 7.9 m/s (sea level), 9.2 m/s (10,000 ft)
  - Maximum speed: 30 m/s (67 mph) sea level, 33 m/s (74 mph) @ 10,000 ft
  - **Maximum endurance: 2.6 hours @ sea level, 2.3 hours @ 10,000 ft** (exceeds 1-hour requirement by 2.3×)
  - Rate of climb @ 30 m/s, 10,000 ft: 6 m/s
  - Zero-lift drag coefficient (CD₀): 0.025

- **General Performance**:
  - Maximum available power: 315 W (70% of 450 W battery pack)
  - Lift-to-drag ratio: 10.8 @ 54-in wing (α=7.5°), 15.4 @ 102-in wing (α=6.0°)
  - Excess speed capability: Both configurations exceed 10 m/s wind requirement by >20 m/s
  - Service ceiling capability: Verified to exceed 10,000 ft requirement; 102-in exceeds 14,000 ft volcanic mission requirement

**Requirements Met**:
- Lifespan: 100+ launches/landings on unimproved surfaces
- Landing speed: 10 m/s through deep stall or simplified landing method
- Sustained wind operation: 10 m/s with positive ground speed (5 m/s minimum) in adverse winds
- Water resistance: Light rain with O-ring seals; potential for heavy rain with design refinement
- Assembly: Tool-free, modular construction
- Launch: Bungee (hand-launch option available)
- Recovery: Belly land
- Maintenance: Field-replaceable propellers and modules

### CAPS Modular Payload System
**Payload bay specifications**:
- Minimum volume: 500 cm³ (exceeded in both configurations)
- Maximum payload mass: 0.5 kg (testing phase), 1.0 kg (volcanic mission)
- MHP payload volume: >3000 cm³
- Volcanic payload: 8" × 4" × 3" (exceeds requirement)
- Operating ceiling support: 13,000 ft (future refinement to 14,000+ ft for volcanic missions)
- Power supply: Independent 9V DC batteries for sensor packages
- Ambient operating temperature: 10-25°C

## Use Cases & Applications

### Primary Mission: Cooperative Wind Sensing
- Autonomous atmospheric profiling for wind structure measurement
- Deployment in adverse weather conditions (thunderstorms, Arctic operations)
- Cooperative multi-platform atmospheric observations

### Volcanic Observation Mission
**Sensors considered for deployment**:
- **Current (tested on Dragon Eye platform)**:
  - SO2 sensors: City Technology Ltd sensors (5, 20, 50 ppmv ranges); 4-20 mA standard outputs; ~1 year useful life
  - Infrared thermal camera: FLIR Indigo TIR (50 mK sensitivity, 8-12 μm uncalibrated)
  - Panchromatic visible + low-light visible cameras (manufacturer TBD)
  - Deciliter-volume air sample collector (one-time trigger)
  - Micro-temperature, pressure, humidity sensors
  - Independent aircraft avionics/GPS

- **Future deployment instruments**:
  - **Nephelometer** (IDI Corp., Ithaca, NY): NASA SBIR-sponsored; dual laser (1.33 & 1.55 μm) forward-looking; discriminates liquid vs. solid aerosol size distributions; ash vs. ice particulates; successfully flown on aerostat to 11,000 ft at Turrialba Volcano
  - **CO2 sensors** (multiple options):
    - OEM sensor: ~10 ppmv sensitivity, 0-3000 ppmv range; flown on University of Costa Rica UAVs to 13,000 ft
    - Makel Engineering experimental sensor: 1 ppm sensitivity, 0-1000 ppmv range, ~425°C internal operating temperature; suitable for direct volcanic fumarole insertion
    - JPL laser CO2 sensor: 500g mass

**Mission Constraints**:
- Payload mass: <500g (current), <1000g (volcanic)
- Volume: 8" × 4" × 3" (volcanic payload form factor)
- Operating ceiling: 13,000 ft ASL (current), target 14,000 ft
- Ambient temperature: 10-25°C
- Power: Independent 9V DC

### Field Operations Advantages
- Highly portable with minimal ground support equipment
- Easy deployable/recoverable (rugged, can land virtually anywhere)
- Single science operator can launch/control/land with minimal UAS training
- Operations in adverse weather conditions
- Rapid payload exchange in field for mission flexibility
- Battery-powered endurance: 2.3+ hours enabling extended mission coverage

## Key Results Obtained

### Aerodynamic & Performance Analysis
1. **CFD-derived performance validated**:
   - 102-inch wing configuration exceeds all performance requirements with significant margin
   - 54-inch configuration meets minimum requirements at sea level, marginal at altitude
   - Both configurations verified aerodynamically capable of autonomous hand launch and automatic landing

2. **Service Ceiling Verification**:
   - Rate of climb analysis confirms both configurations exceed 10,000 ft minimum requirement
   - 102-inch configuration supports volcanic mission ceiling of 14,000+ ft

3. **Wind Capability Confirmation**:
   - Performance margin of >20 m/s speed excess over 10 m/s sustained wind requirement
   - Verified through comparison with documented RECUV NexStar flight performance in 20-25 m/s gusts

4. **Endurance Achievement**:
   - 102-inch: 2.6 hours @ sea level, 2.3 hours @ 10,000 ft (2.3× requirement)
   - 54-inch: 1.2 hours @ sea level, 1.0 hour @ 10,000 ft (meets requirement)
   - Battery model includes realistic energy state modeling for continuous inflight assessment

### Weather-Resistant Design Development
1. **O-ring seal specifications established**:
   - Facial seal with 0.100" neoprene cord in 0.125" × 0.080" gland
   - Draw latch compression mechanism proven in static testing