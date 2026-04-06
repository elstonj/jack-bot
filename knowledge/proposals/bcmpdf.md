# Battery Management Controller Schematic (bcm.sch)

## Document Metadata
- Type: Electronic schematic (circuit design)
- Program/Solicitation: NASA 2017 SBIR Phase II
- Date: 2020-03-25
- BST Systems Referenced: Battery Management System (BMS)
- Key Personnel: Chris (git user)
- Project Status: Completed/Inactive

## Executive Summary
This is a detailed schematic for a Battery Management Controller (BCM) board designed to manage and monitor lithium-ion battery packs. The circuit integrates a BQ40Z80 fuel gauge IC, STM32F103 microcontroller, CAN bus communication, and comprehensive safety protection for battery packs up to 6 cells (32V nominal).

## Technical Approach
The BCM employs a modular, safety-first architecture:
- **Battery monitoring**: TI BQ40Z80 fuel gauge IC for voltage, current, and state-of-charge tracking
- **Microcontroller**: STM32F103T6U6 for local control and external communication
- **Communication protocols**: CAN bus (with MAX3051 transceiver) and SMBus for external interfaces
- **Protection**: ESD protection on all signal inputs; freewheel clamping diodes; soft latch power switch (3-second disconnect); MOSFETs with gate isolation resistors for parallel operation
- **Sensing**: 4 thermocouples for temperature monitoring; current sensing via sense resistors (G_RSENSE)
- **Power conditioning**: 3.3V and 5V regulated outputs; up to 45V input support with voltage regulation

## Products & Capabilities Described

### Battery Management System (BMS/BCM)
- **Max voltage**: 32V (6-cell configuration)
- **Max capacity**: 29 Ah
- **Max charge rate**: 4A
- **Charge input**: Up to 36V via Anderson PowerPole connectors
- **Communication**: CAN bus + SMBus
- **Temperature monitoring**: 4 thermocouples (TS1-TS4) with 10kΩ sensing network
- **State-of-charge display**: LED indicators (LEDA, LEDB, LEDC) for visual SoC feedback
- **Power management**: Soft power switch with 3-second disconnect; minimal quiescent drain in low microamp range

### Key ICs
- **BQ40Z80NET** (U7): Fuel gauge with integrated FET protection; manages charge/discharge, cell balancing, and safety functions
- **STM32F103T6U6** (U6): 32-bit ARM Cortex-M3 microcontroller for BMS logic and communication
- **MAX3051EKA** (U5): CAN bus transceiver
- **MIC5319** (U4): 3.3V LDO regulator (500mA output)
- **LT3065IDD-5PBF** (U2): 5V linear regulator with adjustable current limiting
- **LTC6995HS6-1** (U8): Precision timer/oscillator
- **24LC64T** (U10): 64-bit EEPROM for data storage

## Protection & Safety Features
- **ESD protection**: Capacitors C5, C6, C14, C15; PESD1CAN-U TVS diodes on CAN lines
- **Short-circuit protection**: Series resistors R4, R5 in sense lines; STPS10H60SFY Schottky diodes for reverse current blocking
- **Thermal management**: Q1 and Q2 MOSFET thermally designed; separate thermal compensation networks
- **Power switch**: SLS (soft latch switch) with low quiescent current; optional high-side switching via MAX1614
- **Fuse/disconnect**: DFLT27A-7 electronic fuse; programmable shutdown via SHDN pin

## Connectors & External Interfaces
- **Anderson PowerPole (PP)**: Battery input/output (BAT+, BAT-)
- **SMBus (4-pin)**: TS1-TS4 thermocouple inputs
- **CAN connector**: CANH/CANL for external device communication
- **JTAG connector**: 10-pin TC2050 for in-circuit debugging
- **SPI/SWD**: STM32 programming interface
- **LED display connector**: 3-pin for external SoC display board

## Notable Technical Details
- **Parallel MOSFET support**: Circuit includes gate isolation resistor best practices for paralleling FETs (Q1-Q4, Q9-Q20)
- **Terminating resistor option**: CAN-specific 120Ω termination switchable
- **LED control**: Independent PWM control for three LED channels (LEDCNTLA/B/C) enabling tri-color or graduated SoC display
- **Voltage rails**: Separate 5V_SLS rail for soft latch power control; 3v3 and 5V rails for logic
- **Clock**: 8MHz crystal oscillator for precise timing

## Context
This BCM board appears to be a deliverable from a NASA SBIR Phase II program on internal intelligence systems. It represents BST's battery management and monitoring capability suitable for autonomous platforms requiring reliable, intelligent power distribution and fuel gauging in challenging environments.