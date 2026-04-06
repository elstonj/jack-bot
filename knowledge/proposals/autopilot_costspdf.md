# Autopilot Costs

## Document Metadata
- Type: Budget justification / cost documentation (Price listing and invoices)
- Client/Agency: NASA (inferred from file path)
- Program/Solicitation: 2023 SBIR Phase II - Wildfire
- Date: November–December 2023
- BST Products/Systems Referenced: Autopilot systems (ap_psns, ap_core, deployment tube, connectors)
- Key Personnel: Frank Strazzabosco (MicroFirm Engineering, procurement contact)

## Executive Summary
This document is a collection of cost breakdowns, invoices, and purchase orders for Black Swift Technologies autopilot hardware components assembled in late 2023. It provides detailed per-unit costs for autopilot PCB assemblies (ap_psns v0.32, ap_core v28, deployment tube v01) and itemizes component purchases from multiple suppliers for the build of approximately 30 autopilot board sets.

## Products & Capabilities Described

### Autopilot Systems (Hardware Components)

**ap_psns v0.32 (Autopilot Power/Sensor Node)**
- Per-unit cost: $571.86
  - Raw PCB: $188.04
  - Parts: $58.82
  - Assembly: $325.00
- Assembly labor: $1,375–$1,675 per lot (10 units, 5-day turnaround)

**ap_core v28 (Autopilot Core)**
- Per-unit cost: $1,027.69
  - Raw PCB: $286.25
  - Parts: $216.44
  - Assembly: $525.00
- Assembly labor: $1,320–$1,620 per lot (10 units, 5-day turnaround)

**Deployment Tube v01**
- Per-unit cost: $249.31
  - Raw PCB: $41.68
  - Parts: $27.63
  - Assembly: $180.00

**Connectors**
- aircraft_connector V1 (Deployment Tube Edge Connector): $17.48
- tube_connector v01 (Launch Tube Connector): $15.42
- USB Connector v01: $87.71

## Technical Components & Specifications

The autopilot systems use high-reliability aerospace-grade components:

**Power Management & Battery Monitoring:**
- MAX17320G20+ (2–4 cell fuel gauge)
- LT4356IDE-1TRPBF (surge stopper)
- LTC3611EWP (10A, 32V synchronous buck converter)
- MAX3051EKA (CAN interface IC)
- TPS62143RGTR (buck regulator, 5V 2A)
- Various LDO voltage regulators

**Sensing & Telemetry:**
- MS5611-BT (pressure sensor) — qty 57 units ordered
- PNI Sen-Z Magnetometer (Z-axis) — qty 5 units ordered @ $6.40 ea.
- u-blox NEO-M8P-0 GNSS/GPS module (qty 28) — $124.19 ea., precision GNSS receiver

**Processing & Control:**
- STM32H743VIT6 (32-bit microcontroller, 2MB flash, 100LQFP)
- LTC2954IDDB-1 (push-button on/off controller)
- INA180A3 (current sense amplifier)
- NTS0102GT (bidirectional voltage translator)
- Various MOSFET, diode, and switching components

**Memory & Data:**
- SST25VF020B (2M NOR flash, 80MHz)
- Microchip Technology storage
- microSD push/push connectors

**Inductive & Filter Components:**
- Bourns 2.2µH power inductors (multiple units)
- Murata/Pulse power inductors (47nH–1µH range)
- Extensive capacitor arrays (tantalum, ceramic MLCC in 0.01–100µF range)
- Current sense resistors (0.2–50Ω precision)

**Connector & Interface:**
- Molex CLIKMATE headers/housings (2–8 position)
- Samtec headers (20-position)
- USB 3.1 receptacle connectors
- SMA slide switch
- LED indicators (red, blue, yellow)

## Use Cases & Applications
- Wildfire monitoring payload (NASA SBIR context)
- Autonomous small UAS autopilot system
- Environmental sensor data collection platform

## Notable Details

**Procurement Strategy:**
- Distributed component sourcing: Mouser, Digi-Key, Ideas PCB (HK), PNI Sensor, Synzen, JLCPCB, PCBWay, Circuits West
- Board assembly outsourced to Summit Assembly (Denver, CO)
- Lead times managed for ~30-unit production batch (November–December 2023 cycle)

**Cost Structure for 30-Unit Build:**
- Material costs (parts + PCB): ~$362–$560 per unit (depending on board)
- Assembly labor: ~$325–$525 per unit
- **Total per-unit cost (ap_core): ~$1,028**
- Bulk component orders from Mouser totaled $6,532.14 (single large order, 30 Nov 2023)
- Digi-Key order: $1,197.20
- Ideas PCB (bare boards): $487.20 for 30 pcs (core v29)
- Circuits West (antenna PCB): $570.00 for 40 boards

**Quality/Compliance:**
- RoHS3 compliant components specified
- REACH compliance noted on several components
- Tg=180 PCB material (thermal grade)
- HASL finish, green solder mask, white silk screen

**Supply Chain Visibility:**
- Component sourcing shows precision navigation/GPS focus (u-blox M8P is RTK-capable receiver)
- Magnetometer inclusion suggests attitude/orientation sensing capability
- Power management emphasis (fuel gauge, surge protection, multiple voltage rails) indicates battery-powered platform

---

**Assessment:** This document provides granular cost and bill-of-materials documentation for a mature autopilot system entering production phase. The ~$1,000–$1,200 per-unit cost (including assembly) for the core autopilot suggests a high-reliability, instrumented platform suitable for scientific mission payloads.