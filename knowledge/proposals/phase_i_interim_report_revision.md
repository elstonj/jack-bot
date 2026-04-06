# Advanced Technologies for Coordinated In-Situ Atmospheric Sensing (CAPS) - Phase I Interim Report

## Document Metadata
- **Type:** Phase I SBIR Interim Report
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR 2014, Contract Number NNX14CP21P
- **Date:** July 2014 (Report Date: 04/10/14; Modified 12/09/14)
- **BST Products/Systems Referenced:** Apollo UAS (unmanned aircraft), CAPS (Coordinated Atmospheric Profiling System)
- **Key Personnel:** Jack Elston (lead), Brian Argrow, Leuschke, Lawrence, Stachura

## Executive Summary

Black Swift Technologies is developing the Coordinated Atmospheric Profiling System (CAPS), a multi-aircraft UAS platform for in situ atmospheric sensing of temperature, pressure, humidity, and 3D winds. The system addresses NASA's need for improved understanding of atmospheric boundary layer processes across multiple spatial scales. CAPS is designed as a cost-effective ($15,000 per airframe target), reliable, and operationally simple system that enables coordinated volumetric atmospheric sampling—a significant advancement over existing single-aircraft or prototype systems currently used by NASA.

## Technical Approach

CAPS is built on the RSI Apollo reference airframe design, modified specifically for atmospheric sensing and multi-aircraft coordination. The technical approach integrates five key components:

1. **Apollo UAS Airframe:** A modular, hand-launchable fixed-wing aircraft with tool-free component attachment
2. **Atmospheric Sensor Suite:** Pressure, temperature, humidity, and 3D wind measurement systems
3. **Inter-Aircraft Mesh Network:** Radio-based communication for coordinated operations
4. **Autopilot System:** Commercial-grade autopilot with coordination algorithm support via SDK
5. **User Interface:** Android-based tablet interface for mission planning and real-time data visualization

The design philosophy emphasizes **modularity** (swappable payloads, wings, motors, tails) to enable use across multiple NASA Earth Observing missions, and **operational simplicity** to minimize training and logistics barriers.

## Products & Capabilities Described

### Apollo UAS (Unmanned Aircraft)

**Description:**
Tailless, composite construction fixed-wing aircraft based on forward-swept wing design. Modular construction with four interchangeable fuselage modules (main, battery, thrust, payload) plus three-piece wing and detachable tail.

**Specifications & Performance:**
- **Wing Options:** 54-inch (base), 72-inch, or 102-inch span configurations
- **Max Payload:** 0.25–1.0 kg (depending on wing/motor selection)
- **Payload Volume:** Minimum 500 cm²
- **Endurance:** ~70–75 minutes at sea level (54-in config); 64 minutes at 10,000 ft
  - 30 minutes on-station capability + 25 min transit + 15 min ingress/egress/landing
- **Cruise Speed:** ~12 m/s (sea level), 14 m/s (10,000 ft) for maximum endurance
- **Max Speed:** ~41 m/s (sea level), 45 m/s (10,000 ft)
- **Service Ceiling:** Exceeds 10,000 ft requirement
- **Max Weight:** 2.97 kg (6.0 lbs)
- **Wing Loading:** 75.6 N/m² (25.3 oz/in²)
- **Hand Launch Capability:** Yes
- **Landing Speed:** 10 m/s (deep stall or simplified landing method)
- **Airframe Lifespan:** ~100 launches/landings on unimproved surfaces
- **Wind Capability:** Sustained 10 m/s winds, gusts to 20 m/s
- **Weather Resistance:** Water-resistant for light rain operation

**Aerodynamic Design:**
- Custom airfoils: RSI9822 (root, blend of MH60 & S5020), RSI1022 (tip)
- Forward-swept wing for improved spanwise efficiency and favorable CG positioning for forward payloads
- Tailless design reduces parts count and ground handling damage
- Static margin: 5% (sufficient for remote pilot control and efficient autopilot operation)
- L/D max ~10.4 at α ~7.5°
- Two COTS metal gear servos with embedded rotary drive system for elevon control (minimizes drag and damage)

**Power System (Current Design):**
- Hacker A30-14L 800Kv brushless motor
- APC 12×6 propeller
- Total power package: 450 watts
- Battery: 5,000 mAhr 4-cell lithium pack (adjustable 3,000–10,000 mAhr range)
- Field-replaceable battery and motor modules

**Modular Payload Interface:**
- Removable nose cone with standardized mechanical, electrical, and data interfaces
- CAN bus, Ethernet, and DC power connections to autopilot
- Blind-mating waterproof connectors
- Supports custom payload development by third parties

**Operations:**
- Single operator can deploy up to 5 aircraft
- 5-minute maximum interval between successive aircraft launches
- Automatic recovery after defined flight time
- Tool-free component swaps for field operations

### Atmospheric Sensor Suite

**Pressure Measurement:**
- Resolution: 0.1 mb
- Precision: 0.5 mb
- Selected sensor: Measurement Specialties MS 5611 (8 msec time constant, 100 Hz update rate, 0.012 mb resolution)
- Status: 80% complete; awaiting iMet sensor system information for potential Phase II upgrade

**Temperature Measurement:**
- Resolution: 0.1 K
- Precision: 0.2 K
- Approach: Thin-film RTD (Resistance Temperature Detector) for fast response (~0.15 sec or faster)
- Can be post-calibrated against slower radiosonde-grade thermistors for accuracy
- Status: Evaluation in progress; current selection meets accuracy but falls short of desired 6 Hz sampling frequency

**Humidity Measurement:**
- Resolution: 1%
- Precision: 2%
- Challenge identified: No low-cost, UAS-compatible sensors with sub-second time constants currently available
- Current approach: Smaller thermistor beads; humidity sensing remains the "difficult" element
- Potential future: Campbell Scientific KH20 hygrometer (100 Hz capable but oversized/costly for small UAS)

**3D Wind Sensing (High-Accuracy Approach):**
Requires three measurements: vehicle attitude, vehicle velocity, and relative wind vector

- **Vehicle Velocity:** GPS-based (uBlox 7 series, ~0.1 m/s accuracy at 30 m/s)
  - Mitigations for improvement: differential GPS via pseudolite, ground-station corrections, Kalman filter fusion with accelerometer data
  
- **Vehicle Attitude:** Gyro-integrated with low-pass correction from magnetometer and accelerometer
  - Expected accuracy: >1 degree
  - Coupled with 30 m/s airspeed → ~0.5 m/s relative wind accuracy
  
- **Relative Wind Vector Measurement:** Multi-hole probe approach selected
  - Target accuracy: 0.1 m/s (0.2 knots)
  - Method: Differential pressure sensing from multi-hole probe tip on nose cone
  - Probe design: CNC-machined custom unit (smaller than commercial Aeroprobe OTF at ~$5–7K each)
  - Sensor options evaluated:
    - Silicon Microstructures SM9541: ±10 cm water range, 14-bit, 500 Hz, $16 each
    - Measurement Specialties MS 4525DO: ±1 psi range, 14-bit, 2 kHz, $30 each
    - Freescale MPXV7002: ±2.5 kPa, ~0.13 Pa resolution (with conditioning), $10 each
  - Probe includes water trap and drain for operation in precipitation
  - Quick-removal design for field cleaning/back-flushing
  - Wind tunnel calibration feasible due to small size

**Alternative Wind Sensing Approaches Evaluated (not selected for Phase I):**
- Circle/arc motion averaging (low bandwidth, large spatial scale)
- Hot wire anemometry (fragile wires, frequent recalibration, maintenance burden)
- Sonic anemometers (too large for small UAS, fragile in landing)
- Particle velocimetry (not yet mature)

**Geolocation Accuracy:**
- Target: <3 m error in all three axes (x, y, z)

**Data Collection Cadence (Requirements):**
- Temperature: 100 Hz
- Humidity: 0.1 Hz
- Pressure: 100 Hz
- 3D wind: 10 Hz
- At cruise speed 20 m/s, this provides ~10 m spatial resolution

### Inter-Aircraft Coordination System

**Mesh Network:**
- Topology: Multi-hop mesh supporting up to 10 nodes
- Range: Up to 10 km per link
- Bandwidth: 115 kb/s per aircraft
- Status: 46% complete (design phase)
- Validation approach: Link budget analysis, range testing, ground testing of 10 radios in multi-hop scenarios

**Coordination Algorithms:**
- **Collision Avoidance:** Enforced vehicle separation of 2× minimum turn radius
- **Sampling Methodologies (User-Selectable):**
  1. Horizontal gradient sampling (side-by-side formation)
  2. Vertical gradient sampling (stacked formation)
  3. Helical/volumetric sampling (coordinated spiral patterns)
- Status: Algorithms selected from prior validated work; SDK implementation 60–90% complete (behind schedule)
- Capability: Add/remove vehicles during mission with automatic system re-optimization

**Autopilot System:**
- Commercial-grade autopilot with embedded computing
- **Path Following Accuracy:** <3 m horizontal, <10 m vertical (in calm conditions)
- **Emergency Procedures:** Lost-link return-to-known-waypoint with aerodynamic termination after 5 minutes
- **GPS Outage Contingency:** Designed and validated
- **SDK (Software Development Kit):**
  - Rapid development environment for new coordination schemes
  - Open interface for sensor integration
  - Originally planned as highly flexible; Phase I scope reduced to ensure completion, with extended functionality deferred to Phase II
  - Status: 60–90% complete; simplification needed to avoid schedule impact

### User Interface

**Platform:** Android-based tablet interface

**Functional Capabilities:**
- Command and control of up to 5 UA by single operator
- Individual vehicle control (specific commands to individual aircraft)
- Mission-level commands to vehicle groups
- Automatic atmospheric sampling mission generation
- Real-time telemetry display from 5 vehicles simultaneously
- Near-real-time payload data visualization (PTH = pressure, temperature, humidity)
- Situational awareness layer displaying 88D radar products (WSR-88D—Weather Surveillance Radar-1988 Doppler)

**Status:** Simulation-level validation in progress; real-time 88D data integration pending

## Use Cases & Applications

### Primary NASA Missions
1. **Weather Observations:** Atmospheric boundary layer (ABL) thermodynamics, local weather phenomena
2. **Atmospheric Composition:** Complement to NASA's ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) and JPL's HyspIRI (Hyperspectral Infrared Imager)
3. **Replacement for Dragon Eye UAS:** Direct upgrade path with enhanced functionality and lower cost

### Scientific Phenomena Targeted
- **Stable Boundary Layers:** Quiescent, stratified atmospheric conditions (mid-latitude and arctic)
- **Convective Boundary Layers:** Unstable, actively mixing conditions
- **Severe Convective Storms:** High-wind, severe instability environments (per BST's prior experience)
- **Orographic Effects:** Wind flow over terrain
- **Wind Energy Generation:** Resource assessment and characterization
- **Vertical Atmospheric Gradients:** Temperature, humidity, and wind structure
- **Volumetric Sampling:** Multi-point simultaneous measurement of atmospheric properties across space

### Advantages Over Prior Systems
- **Prior Research Systems:** DataHawk, SUMO, M2AV, Tempest, NexSTAR—prototype platforms with:
  