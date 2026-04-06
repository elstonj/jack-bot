# Iridium Supplies Detail

## Document Metadata
- Type: Budget justification / procurement detail documentation
- Client/Agency: NASA
- Program/Solicitation: 2016 SBIR Phase III - Volcano Monitoring
- Date: June 2020
- BST Products/Systems Referenced: Iridium communication system (V1.0)
- Key Personnel: Frank Strazzabosco (MicroFirm Engineering), Jack Elston (BST), Thinh Nguyen (Summit Assembly)

## Executive Summary
This document is a detailed breakdown of component costs and procurement invoices for the Iridium V1.0 communication system developed for BST's NASA SBIR volcano monitoring project. It covers PCB assembly, parts sourcing from multiple vendors (DigiKey, Mouser, NextPCB, Maxtena), and associated labor during June 2020.

## Technical Approach
The Iridium system was developed as a modular communication interface board (V1.0) with the following approach:
- PCB design and fabrication through multiple vendors (MicroFirm Engineering, Circuits West, NextPCB)
- Surface-mount assembly coordination with Summit Assembly
- Component sourcing from major electronics distributors
- Integration with antenna and mounting hardware

## Products & Capabilities Described

### Iridium V1.0 System
- **What it is**: A satellite communication interface board designed for remote data transmission
- **Components**: 
  - Custom PCB (4-layer, 3.55" × 1.89", manufactured to IPC-A-600 Class II spec)
  - STM32F405RGT6 microcontroller (32-bit, 1MB flash)
  - Multiple voltage regulators and buck converters
  - SIM card connector for Iridium satellite modem integration
  - Various resistors, capacitors, inductors, and signal conditioning electronics
  - IMU sensors (ICM-20689 inertial measurement units)
  - Flash memory (SST25VF020B-80-4I-SAE, 2M × 256K × 8)

### Bill of Materials Summary
- **Interface Board**: 3 units @ $500 each = $1,500
  - PCB assembly labor: $450 (2 boards × $225)
  - Stencil and setup: $200
- **Enclosure/Mount**: 2 units @ $100 each = $200
- **Antenna**: 2 units @ $50 each = $100 (Maxtena 25mm passive antenna, Maxtena P.O. 1016)
- **Tripod**: 1 unit @ $120 = $120
- **Total Identified Hardware**: $1,920

### Detailed Procurement Costs (June 2020)
**MicroFirm Engineering (7/1/2020 Invoice #2963)**
- Labor: 41 hours @ $100/hr = $4,100
- Parts from Digikey: $89.87
- Parts from Mouser: $103.06 + $13.01 + $17.43 + $188.45 = $321.95
- Parts from NextPCB: $178.80 + $111.80 = $290.60
- Parts from Amazon: $16.78
- Shipping/handling: $27.28
- **Total MicroFirm Invoice: $4,846.50**

**Component Procurement Detail**

From DigiKey (Invoice 74119169, 6/4/2020, $89.87):
- STMicroelectronics STM32F405RGT6 MCU (2 units)
- Passive components: resistors (various ohm values), capacitors (0.022µF to 330µF), inductors
- Signal conditioning: NXP NTS0102GD translators, Kyocera 16MHz crystal
- Supporting ICs for power management

From Mouser (Multiple invoices totaling $321.95):
- Passive components: resistors, capacitors, inductors, ferrite beads
- Power management: TPS62135RGXR buck converters, AP2210K LDO regulators, LT3757AEDD switching regulators
- Analog/Mixed-signal: TDK InvenSense ICM-20689 IMU (7 units @ $6.17 each)
- Connectors: Molex headers, Hirose connectors, Micro USB type B, Micro SD connectors
- Diodes and TVS/ESD suppressors
- Memory: Microchip SST25VF020B flash memory

From NextPCB (Two invoices):
- PCB P-E19254ASY7: 10 units, 9.14×4.83mm, $150.40 + freight/fees = $178.80
- PCB P-E19254ASY8: 10 units, 2.16×12.98mm, $86.30 + freight/fees = $111.80

From Maxtena (P.O. 1016):
- Iridium passive antenna, 25mm: $75.00

## Use Cases & Applications
- **Primary Application**: Volcano monitoring via satellite communication
- **Capability**: Remote data transmission from unattended high-altitude platforms via Iridium satellite network
- **Environment**: High-altitude, harsh environmental deployment (volcano monitoring context suggests extreme conditions)

## Key Results/Project Status
- Phase III NASA SBIR project (2016 program, execution in 2020)
- System reached hardware realization and assembly stage (June 2020)
- Multiple board variants fabricated (10+ units of two PCB designs)
- Parallel development of related systems (MHP modifications mentioned in time records)

## Notable Details

### Vendor Coordination
- Frank Strazzabosco (MicroFirm Engineering) acted as primary procurement coordinator and designer
- Summit Assembly (contact: Thinh Nguyen) handled PCB assembly in Denver
- Multiple suppliers leveraged for cost optimization and lead time management
- NextPCB used for international PCB manufacturing

### Development Timeline (June 2020)
- 6/2-6/4: Board finalization, quote management, parts ordering
- 6/5-6/26: Modifications, parts procurement, assembly coordination, power supply debugging
- 41 hours of engineering labor across the month for Iridium and MHP projects

### Technical Specifications Observed
- Standard 3.3V and 5V power rails with multiple regulators
- Micro SIM card interface for satellite modem
- IMU integration (motion/orientation sensing)
- Comprehensive ESD and signal integrity protection
- Industrial-grade component selection (primarily automotive/industrial rated)

### Cost Structure
- Labor dominated total cost (~$4,100 of ~$6,000+ total)
- PCB fabrication and assembly: ~$750-800 per board
- Component BOM approximately $1,200-1,500 per unit
- Antenna and mechanical hardware: ~$170-200 per unit
- Project demonstrates typical small-satellite/remote-sensing instrument cost profile