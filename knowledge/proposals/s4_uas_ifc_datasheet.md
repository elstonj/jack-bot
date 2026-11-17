# S4 UAS IFC Datasheet

## Document Metadata
- **Type:** Technical datasheet / Interim Flight Clearance (IFC) document
- **Client/Agency:** DIU (Defense Innovation Unit) / NAVAIR
- **Program/Solicitation:** DIU/NAVAIR LC-ISR (Low Cost ISR) Gauntlet
- **Date:** November 16, 2026 (Rev. 0 Draft; released 11/20/2026)
- **BST Products/Systems Referenced:** S4 UAS, SwiftCore Flight Management System (SwiftPilot, SwiftCore autopilot 3.3.0), SwiftStation GCS, SwiftTab 3.3.0, S2 (reference platform), S0-AD (heritage platform)
- **Key Personnel:** Jack Elston (last editor)
- **Partners:** KrateoSky (co-preparation), Lisenby/DSKinetic (wing manufacturer), NextVision (gimbal), Teledyne FLIR, ModalAI, CoVar, Microhard, Amprius, u-blox

## Executive Summary
The S4 is a battery-electric long-endurance UAS designed for the DIU Low Cost ISR Gauntlet competition. With a 40 lb maximum takeoff weight, 177-inch high-aspect-ratio wing, and 12-hour design endurance objective (9 hours with current battery cells), the S4 combines proven SwiftCore autopilot technology with dual brushless motors, stabilized EO/IR payload, and multiple datalink options for autonomous surveillance missions. The system features autonomous belly-landing recovery and is derived from BST's S2 and S0-AD heritage platforms.

## Technical Approach

### Aircraft Design & Performance
- **Configuration:** Twin-motor, high-aspect-ratio sailplane-style design; battery-electric propulsion
- **Wing:** 177-inch (4.5 m) wingspan, 25:1 aspect ratio, ~8.7 ft² area; composite construction by Lisenby/DSKinetic, laid up for 40 lb GTOW with maneuver margin
- **Fuselage:** Approximately 75 inches length (final CAD TBC)
- **Empty Weight:** ~15.5 lb (7.0 kg) without battery or payload
- **Maximum Takeoff Weight:** 40.0 lb (18.1 kg)
- **Design Endurance:** 12 hours (loiter ~41 kt, sea level ISA, with Amprius SiCore 500 Wh/kg cells); ~9 hours with currently available 400 Wh/kg cells. Final value from early-2027 flight test.

### Propulsion
- **Motors:** 2 × brushless outrunner motors (400 Kv-class), one per wing pylon, controlled by ESCs commanded by SwiftPilot autopilot
- **Propellers:** 2 × 17×13 in RFM folding propellers (Soaring USA), 2-blade, fold on belly landing for impact protection
- **Power Source:** 2 × 6S8P Li-ion packs in parallel (Amprius SA03 cells), 20.4 V nominal, 3,865 Wh total; 3.79 kW continuous capability (1C discharge)
- **Propulsion Power:** ~340 W at loiter
- **Avionics Power:** ~13.5 W nominal (flight-critical systems, servos, C2/backup C2, Remote ID, strobe; includes conversion losses)
- **Payload Power:** Baseline ~16 W nominal / 45 W peak; up to 50 W allocated
- **Power Losses:** ~3.5 W DC-DC conversion (88% regulator efficiency) plus wiring/ESC losses

### Flight Management & Avionics
- **Autopilot/Flight Controller:** BST SwiftCore Flight Management System
  - **Hardware:** SwiftPilot Core Board 1 (STM32H743 processor, u-blox ZED-F9P multi-band GNSS, RM3100 magnetometer, MS5611 static + MS4515DO differential pressure) + Core Board 2 (dual ICM-20948 IMUs, Microhard P400 radio, IMU heater)
  - **Same stack as:** S0-AD (NOAA/SOCOM heritage); S2 power board
  - **Firmware:** SwiftCore autopilot 3.3.0 (released Nov 2026), FreeRTOS on STM32H743; Gauntlet build version frozen
  - **Power Board:** BST S2 power board (switched 5 V / 12 V rail, Ethernet/UART/MIPI interfaces)

- **GPS/INS:** u-blox ZED-F9P multi-band GNSS (GPS/GLONASS/Galileo/BeiDou, L1/L2) with external active antenna; extended Kalman filter fusion of dual IMUs, magnetometer, air data, and GNSS

- **Remote ID:** Dronetag Mini (ASTM F3411 broadcast via Bluetooth + network Remote ID via LTE-M)

### Command & Control / Datalinks
**Primary C2 Link Options:**
- **Microhard P400-C2S:** 410-480 MHz frequency-hopping spread-spectrum (FHSS), 2 W, 56-115 kbps planned (345 kbps max); heritage from S0-AD (demonstrated 400 km ground link, 215 nm air-to-ground in licensed narrowband)
- **Alternate:** Same P400 in licensed 12.5 kHz narrowband mode (9.6 kbps) with fixed channel assignment

**Secondary C2 Link (Beyond-LoS Backup):**
- **Iridium 9603N SBD:** 1616-1626.5 MHz L-band, 2.4 kbps; automatic fallback when primary lost; supports loiter, return, land, terminate commands; carrier board refresh required (S2 parts obsolete)

**Payload Video (FMV Configuration):**
- **Microhard pMDDL2280-SWP:** 2.2-2.8 GHz, 2×2 MIMO, >40 Mbps; up to 6 W transmit power (planned 1 W or less)

**Frequency Status:** No JF-12 waivers held; requires DoD frequency assignment for 400 MHz hopping; payload video frequency assignment required.

### Ground Control Station
- **Hardware:** BST SwiftStation (embedded Linux, OpenWrt-based; integrated P400 and pMDDL2280 ground radios; internal UPS battery) on tripod mast; optional auto-tracking antenna; optional rugged laptop (Panasonic Toughbook class)
- **GCS Software:** SwiftCore gcsDaemon 3.3 (multi-aircraft, multi-radio support), SwiftTab 3.3.0 operator interface, TAK/CoT output
- **Tablet Interface:** Rugged Android tablet with SwiftTab 3.3.0; local Wi-Fi (2.4/5 GHz) to SwiftStation (<30 m); SwiftStation relays to aircraft over P400 (no direct air-vehicle link); wired Ethernet/USB tether backup available
- **Manual Control (Flight Test Backup):** Futaba 2.4 GHz FASSTest transmitter; autonomous via SwiftTab, joystick mode available through SwiftTab over C2 link

### Launch & Recovery
- **Launch:** Pneumatic rail launcher scaled from S2 for 40 lb class (in development); target exit speed 22 m/s (43 kt), minimum 1.3× clean stall speed at MTOW (TBC); rail length ~5-6 m; fallback vehicle-top cradle (2025-26 test-bed proven)
- **Recovery:** Autonomous belly landing (no parachute or net); abrasion-resistant composite belly skid; folding propellers; autonomous approach with flaps, motors stopped, props folded; landing on grass/dirt lanes ~500×100 ft (150×30 m), clear of obstacles; manual R/C backup during flight test

### Center of Gravity
- **Design CG:** 30-35% MAC (MAC ~7 in / 0.18 m); final limits from Lisenby wing aero data
- **Procedure:** Set by battery position; weighed in flight configuration before each flight; recorded on weight-and-balance sheet

## Products & Capabilities Described

### SwiftCore Flight Management System
- Modular, proven autopilot stack (S0-AD, S2 heritage)
- Dual-core IMU redundancy, multi-constellation GNSS, integrated C2 radio
- Safe Sandbox isolation of non-critical functions (payloads) from flight-critical control
- Supports autonomous navigation, loiter, return-to-home, forced landing modes
- Lost-link and lost-GNSS emergency procedures available

### SwiftStation Ground Data Terminal
- Integrated dual-radio platform (P400 and pMDDL2280)
- Multi-aircraft, multi-radio command and control daemon
- UPS battery for field operations
- Optional auto-tracking antenna for extended range
- TAK/CoT integration for military networks

### SwiftTab Operator Interface
- Mission planning, lost-com and landing plan setup
- Joystick/manual control modes over C2 link
- Runs on rugged Android tablets
- Multi-aircraft capable (via gcsDaemon)

## Use Cases & Applications

The S4 is positioned for the **DIU Low Cost ISR (LC-ISR) Gauntlet** competition, designed for:
- **Long-endurance surveillance:** 9-12 hour loiter over operational area
- **Full-motion video (FMV):** Stabilized EO/IR gimbal with 20× optical zoom and tracking/geolock
- **Automated target recognition (ATR):** ModalAI + Teledyne FLIR + CoVar ACES integration (alternative payload)
- **Atmospheric/weather sensing:** Optional pressure, temperature, humidity, wind measurements from autopilot air-data solution
- **Autonomous operations:** No pilot required after launch; fully autonomous navigation, loiter, landing
- **Extended range:** Dual-datalink redundancy (Microhard + Iridium) for beyond-LoS operations

## Key Results / Status

This is a **pre-flight datasheet** (Rev. 0 Draft as of 11/20/2026) for a system in development:

- **Configuration Status:** Final dimensions and performance specs marked "TBC" (to be confirmed) pending early-2027 flight test
- **No Service Bulletins Issued:** New configuration; no waivers requested
- **Flight Termination:** Autopilot function on C2 link (no independent FTS); can add independent FTS receiver if range requires it
- **Documentation in Preparation:** NATOPS-equivalent Operator's Manual, emergency procedures checklists, SwiftCore 3.3 operator guides, launcher operations manual
- **Frequency Status:** No spectrum waivers held; will require range/DoD frequency assignments for 410-480 MHz hopping and 2.2-2.8 GHz payload video before operation

## Notable Details

### Heritage & Proven Technology
- SwiftCore stack derived from **S0-AD** (NOAA / SOCOM operations)
- Wing design influenced by **S2** platform experience
- Microhard P400 radio already demonstrated 400 km ground link and 215 nm air-to-ground in S0-AD testing
- Launcher design scaled from operational S2 system

### Advanced Battery Performance
- **Amprius SA03 cells:** Silicon-anode Li-ion, 11.84 Ah per cell; 500 Wh/kg (SiCore variant) or 400 Wh/kg (current availability)
- Dual 6S8P parallel configuration provides redundancy and high continuous discharge (3.79 kW @ 1C)
- Exceeds typical endurance targets for the class

### Payload Flexibility
- **Baseline (FMV):** NextVision DragonEye2 (145 g) with 2-axis stabilization, 1280×720 EO, 640×480 LWIR, tracking/geolock
- **ATR Alternative:** Teledyne FLIR Hadron 640R (56 g) + ModalAI VOXL 2 compute (16 g, QRB5165, 15 TOPS) running CoVar ACES
- Payload bay isolated from flight-critical systems via Safe Sandbox
- Switched power rails support up to 50 W payload allocation

### Regulatory Considerations
- **Remote ID:** FAA-approved Dronetag Mini (broadcast + network); no traditional transponder required
- **Lithium Battery Safety:** Amprius SA03 cells exempt from review per NAVSEA S9310-AQ-SAF Rev. 3 ¶4-2.2, but require notification
- **Flight Termination:** Autopilot-based (not independent FTS), acceptable under RCC 323-99; independent receiver can be added if needed

### DIU Gauntlet Competition Context
- **Single-aircraft GCS model** for Gauntlet (no swarming configuration)
- **Low-cost emphasis:** Autonomous operations, minimal ground crew
- **Demonstrated vs. novel:** Most subsystems (autopilot, radios, launchers) derived from operational heritage; primary development effort on wing integration and endurance optimization

### Outstanding Items (Pre-Flight Datasheet Notes)
- Final wing CAD (length TBC)
- Launcher test for 22 m/s exit speed validation
- Endurance flight test (early 2027) to confirm 9-12 h targets
- Motor/ESC/propeller final part numbers
- Frequency assignments (DoD 410-480 MHz, payload 2.2-2.8 GHz)
- Iridium carrier board refresh parts
- Optional auto-tracking antenna & laptop models
- Remote Controller / Futaba transmitter battery specs
- AI functionality integration (noted in footnote [a] as requiring documentation)