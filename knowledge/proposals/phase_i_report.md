# Aircraft Selection and Requirements Analysis Report

## Document Metadata
- **Type:** Requirements analysis and aircraft selection report
- **Client/Agency:** SPEC Inc (Stratton Park Engineering)
- **Program/Solicitation:** Not specified
- **Date:** September 7, 2016
- **BST Products/Systems Referenced:** SwiftPilot autopilot, SwiftTab user interface
- **Key Personnel:** Nick Krause (SPEC Inc - CAD/mechanical validation)

## Executive Summary
This report presents Black Swift Technologies' analysis of airframe and systems selection for a payload-carrying UAS mission planned for Arctic operations in Ny Alesund, Svalbard. BST evaluated four candidate airframes and recommended the Penguin B from UAV Factory, along with the SwiftPilot autopilot and supporting avionics and communications systems, to meet mission requirements for high-altitude (15 kft), long-duration (2 hour) operations with up to 9 kg payload in icing-prone conditions.

## Technical Approach

### Airframe Selection Process
BST evaluated four airframes against mission requirements:
1. **Penguin B (UAV Factory)** - Selected
2. TBM UAV-4 (Troy Built Models) - Rejected (lower quality/reliability)
3. Cryowing - Rejected (non-COTS, sourcing/parts challenges; under consideration as for-hire service through Andoya Space Center)
4. Arcturus Jump 15 - Rejected (tractor configuration blocks sensor airflow)

**Tiger Shark UAS** was also reviewed but deemed beyond BST's operational capability; BST recommended client contact Navmar Applied Science Corporation if preferred.

### Penguin B Selection Rationale
- **Maximum payload capacity:** 11.5 kg total (fuel + payload)
- **Fuel capacity:** 3000 cc standard tank = 2.3 kg
- **Usable payload:** 9.2 kg with full fuel tank (0.2 kg margin above 9 kg requirement)
- **Fuel type:** 98 octane (readily available in Europe)
- **Mechanical validation:** Nick Krause (SPEC Inc) performed Solidworks CAD analysis confirming payload volume, center-of-gravity within spec, and sensor inlet port integration feasibility

### Propulsion System
**Engine Requirements Met:**
- No maintenance required during 10-20 hour initial testing phase (service interval considerably >20 hours per UAV Factory)
- Arctic-rated operation at temperatures below -20°C (extensively tested in Arctic regions)
- 15 kft density altitude capability (achievable with Electronic Fuel Injection [EFI] upgrade; 10 kft without)

**Engine Details:**
- Fuel consumption: 450 g/hour nominal at MTOW; range 200-700 g/hour depending on density altitude
- EFI system and Electronic Control Unit (ECU) supplied by Currawong Engineering (CE367B model)
- Interfacing: RS232 connection for throttle command from autopilot; optional engine diagnostics downlink possible

### Performance Specifications
- **Maximum climb rate (at MTOW):** 1.2 m/s (236 fpm)
- **Cruise speed:** 43 kts
- **Endurance capability:** Worst case (700 g/hr at 15 kft) requires 1.4 kg fuel for 2-hour mission; full 3000cc tank enables 3.3 hours worst-case or 5.1 hours nominal flight time
- **Wind capability:** 15 kts sustained (within design envelope; not limiting)
- **Note:** SPEC Inc required to verify climb/descent rates meet sensor mission requirements (rates not provided in this report)

## Products & Capabilities Described

### SwiftPilot Autopilot
**Specifications & Features:**
- Fixed-wing autopilot control with up to 128 actuator interfaces (only 7 needed for Penguin B)
- Capable of operating gas-powered vehicles
- Can execute ascent/descent while maintaining orbit maneuvers
- Telemetry output: 20 Hz onboard, at least 1 Hz available externally
- Payload data downlinking capability (tagged with autopilot telemetry)
- Command uplink capability from Ground Control Station (GCS)
- Waypoint-based flight plan execution with graphical interface (SwiftTab)

**Comparison to Alternative (Piccolo Autopilot):**
- SwiftPilot preferred due to lower training/operational cost
- Both systems meet core requirements
- Piccolo requires significant NRE for implementation; uses Microhard Nano n920 radio (60+ mile range, -108 dBm sensitivity)
- Piccolo integrates directly with Currawong CE367B ECU

### SwiftTab (Ground Control Station Interface)
- Allows graphic boundary definition for flight planning (e.g., balloon operation avoidance)
- Provides waypoint-based mission planning
- Receives autopilot telemetry and payload data

### Communications System: Xeta9m-T Radio (XetaWave)
**Specifications:**
- Manufacturer: XetaWave (Boulder, Colorado)
- Frequency: 900 MHz (recommended for Ny Alesund operations; 2.4 GHz restricted; 900 MHz typical for Europe requires special approval, obtainable through Andoya Space Center)
- Power output: 1 W standard; 3 W boost option available (harder to license)
- Receiver sensitivity: -110 dBm at 57 kbps (MSK modulation)
- Published range: 70+ miles (verified for 20 miles Svalbard link analysis)
- Software-defined radio with modulation flexibility
- Local manufacturer support from XetaWave

**Radio Analysis for Svalbard (20 nm requirement):**
- Link budget analysis using Radio Mobile Online tool
- 6.12 dB fade margin (note: low margin requiring real-world testing validation)
- Antenna: 2.1 dBi omnidirectional
- Critical requirement: Maintain line-of-sight with terrain in Svalbard

**Sensitivity vs. Throughput Trade (Xeta9m-T):**
| Sensitivity (dBm) | Modulation | Throughput (kbps) |
|---|---|---|
| -110 | MSK | 57 |
| -107 | MSK | 114 |
| -106 | MSK | 153 |
| -103 | MSK | 229 |
| -99 | BPSK | 530 |
| -98 | 2FSK | 663 |
| -97 | QPSK | 1061 |
| -95 | QPSK | 1768 |
| -90 | 8PSK | 2651 |
| -86 | 16QAM | 3535 |
| -81 | 32QAM | 4419 |

**Payload Radio Challenges:**
- SPEC Inc requested SSH (3 sessions) and FTP client capability
- Bandwidth requirements not provided in report
- BST recommends payload data downlink via SwiftPilot/Piccolo payload channel over 900 MHz rather than separate SSH/FTP radio due to:
  - Robustness and data tagging with autopilot telemetry
  - Reduced RF interference and system complexity
- Alternative (if dedicated payload radio required): 433 MHz or 5.8 GHz, but both inadequate (insufficient bandwidth and range respectively)

### Power System for Payload
**Total System Mass:** 0.7 kg

**Alternator: S676-300F-01 (Sullivan Unmanned Vehicle)**
- Dimensions: 76 mm diameter × 21 mm thickness
- Power output: 120 W @ 2500 RPM to 475 W @ 7500 RPM
- Mass: 350 g

**Voltage Regulator: SREGS-350U-01 (Sullivan Unmanned Vehicle)**
- Max output: 350 W
- Voltage: 20-30 VDC, 13A (factory set to 24 VDC)
- Backup battery capable: 24-32 VDC
- Dimensions: 139 mm × 48 mm × 48 mm
- Mass: 350 g
- Temperature range: -20°C to 55°C ambient

**Power Delivery:**
- Designed to meet SPEC Inc requirement of 200-300 W continuous payload power
- 300 W capacity selected for minimal weight penalty vs. lower-capacity systems
- Note: Penguin B manufacturer standard options only 80-100 W; external system required

## Use Cases & Applications

### Mission Profile (Ny Alesund, Svalbard)
- **Duration:** 2 hours flight time (takeoff to landing)
- **Altitude:** 0-15 kft density altitude capability
- **Payload:** Up to 9 kg (SPEC Inc sensor package)
- **Launch/Recovery:** "Soccer Field" adjacent to airport at Ny Alesund
- **Environmental conditions:** Arctic temperatures (-20°C and below), potential icing conditions
- **Operational constraint:** Avoid balloon operations (1.5 nm exclusion radius)

### Environmental/Science Operations
- High-latitude Arctic atmospheric sampling
- Operations in icing-prone conditions
- Extended endurance requirements for scientific measurement

## Key Results

### Icing Analysis and Recommendations
**Icing Types and Temperature Ranges:**
| Type | Temperature (°C) | Characteristics |
|---|---|---|
| Clear | 2 to -10 | Worst form; changes airfoil shape; stall risk |
| Mixed | -10 to -15 | Clear + rime combination |
| Rime | -15 to -20 | Forms when droplets freeze immediately; less airflow disturbance |

**Key Finding:** No reliable method currently exists for icing detection/mitigation on small UAS despite significant DoD/other investments.

**BST Recommended Icing Risk Mitigation Strategy:**
1. Use airport weather service and other sources to forecast and avoid/minimize icing areas
2. Heated pitot tube (provided by UAV Factory) to maintain airspeed measurement
3. Onboard Outside Air Temperature (OAT) sensor with ground monitoring (or ground-based visual observation) to avoid clouds below 5°C
4. ECU engine performance downlink with real-time monitoring for performance degradation
5. Escalating response protocol if icing encountered:
   - Primary: Fly reciprocal path out of icing environment
   - Secondary: Climb or descend to safer altitude
   - Tertiary: Return home immediately and land

**Critical Conclusion:** No guaranteed icing avoidance exists; field team must weigh aircraft risk vs. scientific data value with available information.

### Avoidance/Prevention Assessment
- Icing prevention systems (heated surfaces, anti-ice chemicals, special coatings) **not feasible** on Penguin B due to SWAP constraints
- Fault detection algorithms for ice buildup on aerodynamic surfaces possible but would constitute new R&D requiring validation before operational use
- Lessons learned from Navy small UAS operations incorporated into recommended CONOPS

### Flight Duration Validation
**Worst-case scenario analysis (700 g/hour at 15 kft density altitude):**
- 1.4 kg fuel required for 2-hour mission → 10.1 kg payload capacity (exceeds 9 kg requirement with margin)
- Full tank (2.3 kg fuel) → 3.3 hour worst-case flight time or 5.1 hour nominal flight time

### Radio Range Validation
- 20-mile requirement for Svalbard verified through Radio Mobile Online analysis
- 6.12 dB fade margin adequate but tight; **requires real-world testing validation**
- Terrain line-of-sight maintenance critical in operational area

## Notable Details

### Coordination with External Organizations
- **Andoya Space Center:** BST discussing Cryowing for-hire operations; awaiting pricing/schedule for summer Svalbard integration/flights
- **XetaWave:** Local Boulder-based radio manufacturer with ongoing support relationship with BST
- **UAV Factory:** Validation support provided for Penguin B propulsion and performance specs
- **Currawong Engineering:** ECU/EFI system supplier; direct Piccolo autopilot integration capability

### Design Approach Rationale
- **COTS preference:** Penguin B selected for commercial availability and parts sourcing vs. Cryowing research platform
- **Quality/reliability emphasis:** TBM UAV-4 rejected despite lower cost due to mission complexity and sensor risk
- **System integration:**