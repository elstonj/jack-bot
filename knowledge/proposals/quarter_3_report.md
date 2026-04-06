# Soil Moisture Mapping sUAS Phase II Quarter 3 Report

## Document Metadata
- **Type:** Technical progress report (Phase II interim report)
- **Client/Agency:** NASA (Soil Moisture Active/Passive mission validation)
- **Program/Solicitation:** NASA SBIR Phase II, Contract Number NNX14CG09C
- **Date:** January 2015 (Q3 report covering period through December 2014)
- **BST Products/Systems Referenced:** SuperSwift (development), Tempest (operational platform), LDCR (Lobe Differencing Correlation Radiometer)
- **Key Personnel:** Maciej Stachura (lead), Jack Elston (avionics/electronics), Cory (aerodynamic design), CET team (data analysis), Eryan Dai, A.J. Gasiewski (antenna design)

## Executive Summary
This Phase II quarterly report documents BST's progress on developing a soil moisture mapping unmanned aerial system (UAS) platform. The focus was completing flight permission processes (NASA AFSRB/FRRB reviews and FAA COA), advancing the SuperSwift aircraft design through detailed propulsion analysis, developing a high-rate data logger for LDCR sensor integration, refining antenna tuning techniques, and continuing ground-based LDCR experiments. The project experienced a 6.5-month delay in first flight testing, with revised schedule targeting February 2015 field deployment in Canton, Oklahoma.

## Technical Approach

### Overall Program Structure
BST is developing two parallel systems:

1. **Tempest Platform (operational):** Existing airframe being used for initial field testing and certification
2. **SuperSwift Platform (prototype):** New lightweight aircraft design optimized for soil moisture mapping mission with extended endurance

### Key Technical Work Streams

**Flight Certification (Completed Q3):**
- Conducted NASA Airworthiness and Flight Safety Review Board (AFSRB) and Flight Readiness Review Board (FRRB) at NASA Ames on December 16, 2014
- Delivered risk assessment, airworthiness document, FAA Certificate of Authorization (COA), emergency/lost-link/lost-communications procedures, flight checklists, and system manual
- Obtained FAA N-number (N676CU) for Tempest aircraft—new requirement for all UAS operating in National Airspace System (NAS)
- FAA COA passed Air Traffic Control (ATC) safety check; expected issuance February 2015
- NASA "No Objection" letter expected January 29, 2015

**SuperSwift Propulsion System Optimization:**
- Conducted comprehensive analysis of 1,280,421 motor-propeller-battery combinations
- Analysis matrix: 3,027 motors × 141 propellers × 3 battery voltage options
- Objective: maximize flight endurance at 6,000 ft altitude
- Optimization performed using MATLAB script modeling Battery-Motor-Propeller-ESC system
- **Selected Configuration:**
  - Motor: Scorpion Power Systems M-4015-340Kv (353g)
  - Propeller: APC 12×12E (85g)
  - Battery: 5-cell lithium ion (~18V at full throttle)
  - **Predicted Performance:** >2 hours flight time at 6,000 ft altitude
  - No gearbox employed (avoided added losses, weight, cost, reliability concerns)
  - Operating point: 16.2 m/s flight speed, ~75W power consumption

**SuperSwift Airframe Design (Complete):**
- Total prototype weight: 3,389g (7.47 lbs)
- Wing: Center + outer wings using MH70 airfoil, 40" span, 10" chord, EPP foam construction
- Fuselage: Fiberglass (development); future commercial version will use fiberglass for wings as well
- Removable nose cone: Fiberglass for sensor payload integration
- Tail: NACA0009 empennage with carbon fiber boom
- Control surfaces: 4 servos (2 aileron, 2 ruddervator—mixed control)
- Manufacturing partners: Flying Foam (wing cutting), Ability Composites (fuselage/nose cone molds)
- First two prototypes scheduled for build in February 2015

**High-Rate Data Logger System:**
- **Purpose:** Collect sensor data from dual L-band antennas, 8 thermistors (2 on antennas, 6 in LDCR), autopilot telemetry
- **Architecture:** Multi-board stacked system (Analog/RF board → ADC Digital board → FPGA/USB3 board → Pico-ITX host computer)

*Analog/RF Board:*
- Interfaces to LDCR signal with amplification and balun for single-ended to differential conversion
- 10 thermistor inputs + analog correlator data
- Microcontroller interleaves data at 1 kHz serial rate

*ADC Digital Board:*
- LTC2143-14 ADC: 14-bit, 60 MSPS, dual-channel simultaneous sampling
- STM32F405 ARM Cortex-M4 microcontroller (168 MHz, 4 USARTs, 2 CAN bus interfaces)
- Interfaces: UART (from Analog/RF), 2× CAN (autopilot data, power control), JTAG programming
- SI510 crystal oscillator: 80 MHz, ≤18ps period jitter
- Board size: 100mm × 72mm × 1mm

*FPGA/USB3 Interface:*
- EFM-02 board with Spartan-6 FPGA (XC6SLX45-3FGG484I)
- Cypress FX3 USB3.0 device controller (CYUSB3014)
- VHDL implementation in Xilinx ISE 14.7
- ADC-SPI interface for configuration
- ADC parallel data capture at 80 MHz, buffered to 100 MHz for USB3.0 transfer
- Block transfers: fixed 8 kB size for throughput/latency optimization
- Data format: Channel A (14-bit) + Channel B (14-bit) + 2 overflow flags + zero padding = 32-bit packets

*Host Computer:*
- VIA EPIA-P910-10Q Pico-ITX board with USB3.0 host controller
- USB3.0 portable SSD: 1TB capacity, ≥320 MB/s write speed, 380 MB/s measured throughput

**MiCo Antenna Frequency Tuning:**
- **Problem:** Integrated antenna frequency drift after installation in airframe
- **Solution:** Dielectric tuning pieces placed over antenna elements
- **Method:** Analytical modeling of effective dielectric constant changes
- Tuning piece design parameters: dielectric constant 2.52 (Dow Corning 3140 RTV), variable width (0–14mm) and thickness (0–2.4mm)
- Theoretical shift frequency relationship: Δf ≈ –14 MHz per unit change in εeff
- **Achieved accuracy:** 11 MHz measured frequency shift vs. 14 MHz predicted (3 MHz error), enabling real-time tuning post-integration
- Tuning pieces: 2mm width × 290mm length × 0.7mm thickness mounted on antenna elements

**Ground-Based LDCR Testing (Build01):**
- Improved experimental apparatus: mounting fixture on long pole with fulcrums to stabilize unit and minimize human absorber effects
- Electronic level meter ensures horizontal orientation and consistent sensor height
- Noise reduction: 6σ voltage variation 0.008V (fixture) vs. 0.01V (hand-held), representing ~20% improvement
- Calculated system temperature calibration constant (Ta): 2.96K (fixture) vs. 3.7K (hand-held), 15% above theoretical (2.57K) vs. 44% above

## Products & Capabilities Described

### SuperSwift UAS
**What it is:** Lightweight, long-endurance unmanned aircraft platform designed specifically for soil moisture mapping

**Key Specifications:**
- Total weight: 7.47 lbs (3,389g)
- Flight endurance: >2 hours at 6,000 ft
- Propulsion: Scorpion M-4015-340Kv motor + APC 12×12E propeller + 5S LiPo battery
- Control: 4-channel servo control (ailerons + ruddervator)
- Payload: Removable fiberglass nose cone for sensor integration
- Airframe: Composite/fiberglass construction with carbon fiber spars/boom

**Proposed Use:** LDCR sensor carrier for soil moisture mapping at centimeter-scale resolution over areas up to 0.6 km² per flight hour

**Performance Claims:** 
- Cruise speed: 16.2 m/s
- Cruise power: ~75W
- Endurance: >2 hours on 11 Ah battery

### Tempest UAS
**What it is:** Existing BST platform, lightweight electric aircraft

**Use in Program:** Operational test platform for initial field deployment and certification prior to SuperSwift availability

**Status:** Completed NASA AFSRB/FRRB reviews, FAA COA submitted, N-number N676CU registered

### LDCR (Lobe Differencing Correlation Radiometer)
**What it is:** Passive L-band (1.4 GHz) radiometer measuring soil moisture via brightness temperature

**Sensor Specifications:**
- Frequency: 1.4135 GHz (within SMAP 1400–1427 MHz band)
- Measurement depth: ~5–10 cm soil penetration
- Antenna: 2×2 microstrip colinear array
- Each element: 5-segment microstrip patch
- Radiation pattern: Broad nadir/zenith beams with horizon nulls

**Capabilities:**
- Spatial resolution: ~15 m at typical flight altitude
- Coverage area: 0.6 km² in one hour flight
- Validation measurement for NASA SMAP mission
- Precision agriculture and evapotranspiration studies

**Components Described:**
- Dual L-band antenna (nadir + zenith looking)
- 8 thermistors (antenna temperature compensation + LDCR internal compensation)
- Correlator electronics (analog + digital processing)
- Lobe differencing: queries brightness difference between nadir and zenith to isolate soil moisture signal

### High-Rate Data Logger System
**What it is:** Custom-designed telemetry and data acquisition system for high-speed LDCR signal capture and geo-referencing

**Capabilities:**
- **Dual-channel ADC:** 14-bit resolution, 60 MSPS per channel, simultaneous sampling
- **Sampling rate:** 80 MHz per channel
- **Storage:** USB3.0 SSD, sustained write >320 MB/s
- **Flight endurance:** ≥1 hour data logging at full resolution
- **Data multiplexing:** LDCR baseband signals + thermistor data + autopilot telemetry (position, altitude, attitude, airspeed)
- **Time synchronization:** ±100 µs precision via ADC reference clock
- **RFI mitigation:** High sampling rate enables post-processing algorithms for radio frequency interference rejection

**Technical Achievement:** First prototype design completed; functional testing planned for January–February 2015

## Use Cases & Applications

### Primary Mission: SMAP Validation
- Soil moisture validation at spatial scales (15 m) finer than SMAP products (5–40 km)
- Sub-watershed scale coverage (~1 km²) for water resource management
- Diurnal sampling at arbitrary times vs. SMAP's fixed overpass times

### Secondary Applications Mentioned
- **Precision Agriculture:** Site-specific irrigation management
- **Hydrological Studies:** Evapotranspiration and boundary layer heat transport research
- **Flood Prediction:** Antecedent soil moisture conditions
- **Arctic Ocean Salinity Mission:** Planned in Phase II (December 2015–February 2016), requires hardware/software modifications to SuperSwift for saline environment operation

### Deployment Locations
- **Canton, Oklahoma (Feb. 2015):** First field deployment, test operational procedures
- **California SMAP Validation Site (Aug. 2015):** Primary validation deployment
- **Arctic (Jan.–Feb. 2016):** Planned salinity measurement extension

## Key Results

### Flight Certification Progress