# UAS Integration Overview

## Document Metadata
- **Type:** Technical integration report
- **Client/Agency:** NOAA/OAR/ARL/ATDD (Air Resources Laboratory, Atmospheric Turbulence and Diffusion Division)
- **Program/Solicitation:** Not specified
- **Date:** August 23, 2017
- **BST Products/Systems Referenced:** SwiftCore FMS, SwiftPilot autopilot, SwiftStation ground station, SwiftTab tablet
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
Black Swift Technologies integrated its SwiftPilot autopilot system into a Penguin BE small unmanned aircraft system (sUAS) for NOAA, enabling autonomous flight control with 5 NM communications range at 5,000 feet AGL. The document details the complete integration process including avionics wiring, payload mounting, quality control procedures, and initial flight test attempts with lessons learned and subsequent aircraft modifications.

## Technical Approach

### Autopilot Integration
- **Avionics Stack:** SwiftPilot autopilot with SwiftStation ground control station running on tablet
- **Power Distribution:** Custom BST Power Supply Board with Anderson Power Pole 75 connectors (rated 120A burst) for modularity; independent Li-Fe battery for autopilot; 5V regulator supplying avionics, 900MHz radio, receiver, and actuator boards
- **Control Architecture:** Futaba T14SG/R7008SB radio control system (after initial Spektrum DX9 replacement) mapped to 9 channels controlling throttle, ailerons, elevator/ruddervator, flaps, landing gear, and auto/manual mode
- **Communications:** 900 MHz XTend radio with quarter-wave omnidirectional antenna on aircraft (0 dBi gain, TNC connector) and 6 dBi ground station antenna on tripod with 15-foot cable
- **Avionics Mounting:** Fiberglass plates on multiple levels with standoffs in fuselage behind battery; 900 MHz radio mounted below landing gear with 6.5-inch copper grounding plate

### Payload Integration
- **Mount Design:** Custom vertical mount redesigned from original University of Tennessee design to fit within fuselage constraints
- **Payload Components:**
  - Intel NUC computer
  - Pika L Hyperspectral Camera
  - Ellipse2-N INS (Inertial Navigation System)
  - TeAx ThermalCapture Fusion Camera
  - GPS antenna
  - SSD storage
- **Power:** 12.0 VDC from onboard regulator (100W max continuous); combined payload draws ~24W
- **GPS Integration:** TeAx camera configured to receive GPS data via autopilot serial line; autopilot also controls camera triggering via ON/OFF detection
- **Shielding:** Extensive payload shielding added to mitigate GPS interference from mission equipment (added ~0.5 lbs)

## Products & Capabilities Described

### SwiftPilot Autopilot System
- Airborne autopilot unit mounted in aircraft fuselage
- Ground station tablet for flight path, altitude, and airspeed control
- Range: 5+ nautical miles at 5,000 feet AGL
- Frequency: 900 MHz
- Capable of fully manual radio control or fully autonomous operation via incremental engagement

### SwiftStation Ground Control Station
- Tablet-based interface
- Provides GPS lock verification
- Battery monitoring and calibration
- Four PWM channels for payload control (e.g., camera triggering)
- Auto/Manual mode switching capability

### SwiftTab
- Tablet component of ground station system
- Used for flight plan and waypoint management

### SwiftCore FMS (Flight Management System)
- Referenced as the integrated navigation/autopilot architecture
- Supports attitude control loops (roll, pitch, rudder)
- Supports thermal energy control (TEC) loops for airspeed and altitude hold
- Navigation with look-ahead and tracking capability

## Use Cases & Applications

**NOAA Atmospheric Research Mission:**
- Automatic control of Penguin BE for atmospheric sampling and data collection
- Equipped with hyperspectral and thermal imaging payloads for environmental monitoring
- Autonomous waypoint-based flight planning with manual override capability
- Scientific instrument in-flight control via ground station (4 PWM channels)

## Key Results

### Quality Control
- **Aircraft Mass:** 19.32 kg (within 21.5 kg limit)
- **Center of Gravity:** Within specification, set to 110 mm from root leading edge
- **Surface Deflections:** All control surfaces passed deflection tests within tolerance
  - Ailerons: ±20° (±2° tolerance)
  - Flaps: 30° down (2° tolerance)
  - Ruddervators: ±25° (±2° tolerance)
- **Autopilot/Avionics Checks:** All passed, including battery reading, GPS lock, antenna verification, and surface direction confirmation

### Communications Testing
- **Ground Testing:** Full 360° rotation test at 5 miles with NLOS obstructions showed adequate performance
- **Air Testing:** Line-of-sight communication verified in air at 5 miles

### Throttle/Takeoff Performance
- Full power testing at 8,260 feet MSL achieved airspeed >20 m/s (required for takeoff)
- Takeoff run: 14 seconds, 148 meters (486 feet) at full throttle—significantly longer than 30m specification
- Power draw: >1,400W during full power test
- Finding: Higher pitch propeller investigation needed for high-altitude performance

### Initial Flight Test Attempt (August 28, 2017)
**Issues Encountered:**
1. **Wheel Friction Problem:** Aircraft wheels had insufficient friction on runway; addressed by tightening wheel bolts
2. **RC System Deficiency:** Spektrum DX9 transmitter/receiver system failed—only 276 meters range at full power despite passing low-power range tests. Identified as manufacturing defect.

**Response & Modifications Made:**
1. **Transmitter Replacement:** Spektrum DX9 replaced with Futaba 14SG with R7008SB receiver (S.BUS2)
2. **Brakes Addition:** Xicoy 100mm electric brakes with Pro-Drive controller added to main landing gear, replacing stock roller-blade wheels; provides full modulation control from handset
3. **Pitot Probe Replacement:** Original probe damaged; replaced with unheated spare (noted: heated probe weighs more and requires CG recheck)
4. **Motor/Propeller Upgrade:** Replaced A60-5S with A60-6XS motor and changed from APC 20×15E to 20.5×14E propeller
   - Old: 5,355 RPM, 8.38 lbs thrust, 65.3A, 1,580W
   - New: 6,200 RPM, 12.57 lbs thrust, 70.5A, 1,660W
5. **Smaller Pitch Propeller:** Procured APC 20×13E as contingency option

## Notable Details

- **Aircraft Base Platform:** Penguin BE from UAV Factory—2.7 kW electric motor, 100W power distribution unit, 4-servo V-tail, swappable universal payload mount
- **Training Component:** NOAA personnel received integration training and simulation training at BST Boulder facility; on-site training planned during follow-on flight tests
- **Incremental Flight Testing Approach:** Flight test cards designed for progressive engagement of autopilot—manual control first, then attitude loops, TEC loops, navigation/limits, then range validation
- **Test Limitations:** Initial testing at 8,240-8,640 feet MSL altitude in remote southern Colorado location; future testing planned at Front Range location for smaller runway requirements
- **High Altitude Challenges:** Extended takeoff distance and power requirements at elevation; future testing site selection prioritized for smaller runway compatibility
- **Quality Issues Lessons Learned:** Low-power RC range tests inadequate for validating full-power performance; future systems should avoid Spektrum equipment in favor of Futaba or equivalent
- **GPS Interference:** Mission payload caused unacceptable GPS degradation; solved through extensive shielding at cost of ~0.5 lbs added weight
- **Payload Camera Integration:** TeAx ThermalCapture configured with autopilot GPS feed and trigger control; detailed configuration screenshots provided

---

**Status:** Project integration completed; QC passed; first flight test attempt resulted in equipment defects requiring modifications; revised aircraft ready for follow-on flight testing with upgraded transmitter, brakes, motor, and propeller.