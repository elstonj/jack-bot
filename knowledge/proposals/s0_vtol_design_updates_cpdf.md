# S0 VTOL Design Updates

## Document Metadata
- **Type:** Technical report (Phase I NTR Additional Documentation)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase I, Contract No. 80NSSC23PB371
- **Date:** 2024 (completed as of January 24, 2024)
- **BST Products/Systems Referenced:** S0 VTOL UAS
- **Key Personnel:** Elston J. (contact: elstonj@blackswifttech.com)

## Executive Summary
This document details comprehensive design modifications to Black Swift's S0 VTOL (vertical takeoff and landing) UAS to improve performance and reliability for wildland fire operations in rugged mountainous terrain. The redesigned aircraft incorporates tilting rotors for improved landing capability, enhanced weather resistance, increased battery capacity, and additional sensors—improving the MTOW from 2.2kg to 2.45kg while maintaining 90+ minute endurance.

## Technical Approach

### Design Philosophy
The redesign was motivated by deployment challenges in wildland fire operations:
- High winds and bulk gusts requiring increased power
- Restrictive landing zones in rough terrain
- Rapidly changing weather with precipitation and airborne ash
- Need for precision hover and landing operations

### Key Design Changes

**Tilting Rotor System (Pitch Control Motors)**
- Replaced fixed motor mounts with servo-based tilt mechanisms using linear actuators
- Selected HITEC HLS12-5050-6V linear actuator for low backlash and durability
- 105-degree motor sweep capability (5° past vertical to 10° past horizontal)
- Integrated, potted 40-amp brushless ESC within custom SLM-printed aluminum heatsink
- Enables vertical takeoff and landing without requiring flat surfaces

**Precipitation & Particulate Protection**
- Developed solution for five-hole pressure probe clogging from rain/ash ingestion
- Implemented porous PTFE film patches (0.1 µm rating, rated to 52,000 Pa forward pressure)
- Custom nose geometry machined to seat PTFE patches while preserving angular precision and avoiding diaphragm effects
- Tested in rain tunnel (13 m/s airspeed, 4 gal/min spraydown, 45-minute continuous exposure)
- Validated in field deployment during Tropical Storm Tammy (October 19)

**Battery System Upgrade**
- Previous: 4s3p arrangement of 18650 Li-Ion cells (133.2 Wh labeled capacity)
- New: 4s2p arrangement of high-current 21700 Li-Ion cells (148 Wh labeled capacity, +11%)
- Previous discharge rating: 15A continuous/25A burst per cell
- New discharge rating: 30A continuous/45A burst per cell
- Assembly weight: 680–700g (only 20g heavier than original 660g pack)
- Usable capacity under 18A load: 133.9 Wh (90% retention vs. 77% for previous design)
- Construction: Annealed copper bus bars, 3D-printed bulkheads, threaded rods for structure

**Primary Propulsion Motors**
- Previous: T-Motor F90 1500KV with 9×6 propeller
  - Peak thrust: 1.6kg (< 5 seconds sustainable)
  - Permanent damage risk at 1 minute full power
- New: T-Motor Cine66 1155KV with 10×7 propeller
  - Constant thrust: 1.75kg (indefinite)
  - 25% higher static efficiency
  - Thrust at fully depleted battery (2.8V/cell): 1.125kg (sufficient for vertical landing)
  - Trade-off: ~10% reduction in maximum airspeed due to lower KV

**Tail Rotor**
- Vertiq 23-14 all-in-one motor-ESC combo with 9×4.5 propeller
- Static thrust: 1.25kg at full charge, 0.75kg at depleted battery (~1/3 of front motors)
- Onboard closed-loop feedback for precise RPM/position control
- Propeller stowable to cruise position for reduced drag
- Total weight: 78g motor + 100g mount/hatch = 178g installed

**Wing Repositioning**
- Wings shifted upward to accommodate larger internal battery
- Redesigned wing-body blend with reduced fuselage cutouts
- Structural analysis: Stress calculations 3 orders of magnitude below ultimate stress of fiberglass fuselage
- Wing structural FEM: 9.9g maximum maneuver load (spar adds additional capacity)
- Aeroelastic stability analysis:
  - Flutter onset: 240 mph (p-k method), 249 mph (g method in ZAERO)
  - Sufficient for >100 mph dash speed and 165 mph max 25-year wind gusts in Colorado mountains

**Laser Altimeter**
- SF20c laser altimeter for high-accuracy altitude during takeoff/landing
- Weight: 17g
- Provides AGL measurement independent of GPS and altitude maps

**Control System Architecture**
- Migrated from PWM to CAN-based control for noise reduction and reliability
- Three small CAN-to-PWM actuator control boards:
  - One per wing (controls tilt actuator, ESC, aileron servo)
  - One in tail (controls tail motor and tail servos)
- CAN protocol more resistant to interference from current-carrying wires and 900 MHz radio

**Sonde Mount & Modular Payload**
- Redesigned for modular payload swapping
- RSS421 sensing element with improved intake for air flow
- Metallic foil coating to reduce solar heating effects
- Accepts alternative payloads (e.g., video transmission system)

**User Interface**
- Larger pushbutton for gloved operation
- 4-pin waterproof charging connector (replacing barrel jack)
- Communication antenna mounted to panel for easier assembly
- Status LED and power button

**Video Transmission System**
- Off-the-shelf HD system modified for extended range (tested to 4 km at 25 Mbps)
- Rear-facing camera for documenting motor tilt transitions
- Mounts to modular sonde point, swappable with atmospheric sensor
- Used for initial flight test documentation

## Products & Capabilities Described

### S0 VTOL UAS
- **Type:** Electric VTOL aircraft for atmospheric profiling
- **Original specs:** 90-minute endurance, 15,000 ft service ceiling, 2.2 kg MTOW
- **Updated specs:** 2.45 kg MTOW, 90+ minute endurance (maintained despite weight increase)
- **Propulsion:** Dual tilting front rotors + fixed tail rotor (tricopter configuration)
- **Sensor package:** Five-hole pressure probe (3D winds), atmospheric thermistor sonde (RSS421)
- **Optional payloads:** HD video transmission system
- **Control:** Autopilot with CAN-based actuator interface
- **Endurance capability:** Indefinite hover at optimal battery/motor pairing (improved from previous 5-second limitation)

## Use Cases & Applications

1. **Wildland Fire Operations**
   - Pre-fire and active fire atmospheric profiling
   - Deployment in rough mountain terrain
   - Real-time video for fire team situational awareness
   - 3D wind data for fire behavior modeling

2. **Tropical Storm Sampling**
   - Validated in Tropical Storm Tammy (October 2023)
   - Capability to sample through active rain while maintaining sensor accuracy

3. **Atmospheric Research**
   - 3D wind profiling
   - Vertical temperature profiles
   - Extended endurance for regional survey missions

## Key Results

### Testing & Validation Completed

**Five-Hole Probe Protection (PTFE)**
- Rain tunnel testing: Maximum airspeed 13 m/s, 4 gal/min spraydown (exceeds heavy rain conditions)
- Unprotected probe: Clogged and failed to recover after rain exposure
- PTFE-protected probe: Maintained functionality; no clogs after 45-minute continuous spraydown
- Field validation: Tropical Storm Tammy deployment confirmed pressure sensor functionality during active precipitation

**Tilting Motor Pod**
- Actuation reliability validated in testing
- Thermal performance: ESC temperature rise ≤15°C over ambient at 40A continuous load (5 minutes, no airflow)
- Linear actuator selected for backdrive resistance and durability

**Battery Pack**
- Constant-current 18A discharge test over 32 minutes
- Temperature: No location exceeded 122°F
- Depleted voltage: 2.8 V/cell after 32 minutes
- Usable capacity comparison:
  - Original pack: 103.4 Wh usable / 133.2 Wh labeled (77.6% retention)
  - New pack: 133.9 Wh usable / 148 Wh labeled (90.5% retention)

**Propulsion System**
- Primary motors: Static thrust ramp response tested across multiple motor-propeller combinations
- Cine66 selected for thermal endurance and hover efficiency
- Tail rotor: Propeller selection tested at full and depleted battery voltages
- Performance across entire battery voltage range characterized

**Structural Analysis**
- Fuselage integrity: Stress analysis showed 3 orders of magnitude margin below ultimate strength
- Wing capability: 9.9g maximum maneuver load (FEM, skin only)
- Aeroelastic stability: Flutter margin 100+ mph above design dash speed

### Performance Improvements
- **Hover capability:** Indefinite (vs. <5 seconds on previous motor)
- **Static efficiency:** 25% improvement during hover
- **Battery usable capacity:** 90.5% retention under load (vs. 77.6%)
- **Thermal management:** ESC temperature rise <15°C under full continuous load
- **Landing safety:** Able to land vertically on fully depleted battery at reduced thrust

## Notable Details

1. **Manufacturing Techniques**
   - SLM (selective laser melting) for complex aluminum heatsinks
   - 3D printing (MJF) for thin-walled structural components
   - Custom jigs developed for battery assembly precision

2. **Design Documentation**
   - Detailed assembly and QC guide written for battery pack to enable team manufacturing
   - Motor control transfer function characterized for controller design

3. **Component Integration**
   - All upgrades integrated within slight MTOW increase (2.2 kg → 2.45 kg)
   - Modular payload system reduces deployment overhead

4. **Operational Improvements**
   - CAN-based control eliminates PWM noise issues from previous design
   - Larger UI button enables operation with gloves
   - Waterproof charging connector improves field durability

5. **Test Articles**
   - New design test assembly (Figure 2) shows integrated tiltrotor configuration
   - All major subsystems (motor pods, battery, nose probe, tail motor) manufactured and tested independently before full integration

6. **Competitive Advantages Demonstrated**
   - Ability to operate in precipitation (storm sampling capability verified)
   - Vertical landing without prepared surfaces (enables rough terrain deployment)
   - Indefinite hover endurance (simplifies operator workload)
   - 4+ km video transmission range for real-time fire team support