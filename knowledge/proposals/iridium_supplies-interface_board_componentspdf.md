# Iridium Supplies - Interface Board Components

## Document Metadata
- **Type:** Invoice and procurement records (budget justification supporting documents)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2016 SBIR Phase III - Volcano Monitoring
- **Date:** June-July 2020
- **BST Products/Systems Referenced:** Iridium communications system, MHP (Multi-Hop Power?) modifications
- **Key Personnel:** Jack Elston (BST), Frank Strazzabosco (MicroFirm Engineering), Thinh Nguyen (Summit Assembly)

## Executive Summary
This document comprises purchase invoices and labor records for electronic components and PCB fabrication related to Iridium satellite communication interface boards and power supply modifications for a NASA SBIR Phase III volcano monitoring project. The work involved MHP board modifications, Iridium interface design, and assembly of interface and power supply circuit boards through June-July 2020.

## Technical Approach
- **MicroFirm Engineering** provided 41 hours of labor (at $100/hr) over June 2020 for:
  - Iridium board design finalization with connector additions
  - MHP board modifications and BOM (bill of materials) cleanup
  - PCB quoting and Gerber file generation
  - Power supply board troubleshooting and modifications
  - Parts sourcing and assembly coordination with Summit Assembly

- **PCB Fabrication:** Two custom PCBs ordered from NextPCB (China):
  - PCB P-E19254ASY7: 9.14 × 4.83 mm (10 units at $15.04 each)
  - PCB P-E19254ASY8: 2.16 × 12.98 mm (10 units at $8.63 each)

## Products & Capabilities Described

**Iridium Interface Board**
- Custom PCB interface for Iridium satellite communications
- Added connector to existing Iridium design
- Design finalized and sent for manufacturing quotes in early June 2020

**MHP (Multi-Hop Power?) System**
- Power supply board modifications including diode additions
- 3.3V supply reconfiguration
- 10 units of modified boards packaged and sent to Summit Assembly for assembly

## Components Procured
Parts ordered from Digi-Key, Mouser Electronics, Amazon, and NextPCB (totaling ~$4,846.50 including labor):

**Microcontrollers & ICs:**
- STMicroelectronics STM32F405RGT6 (32-bit MCU, 1MB Flash)
- Various voltage regulators (TPS62135RGXR, TPS621351RGXR, AP2210K-5.0TRG1)
- Level translators, MOSFETs, diodes, and Schottky rectifiers
- SIM card connector (SIM NANO hinged 6-pin with switch)

**Passive Components:**
- Ceramic capacitors (0.022µF to 47µF, various voltages)
- Resistors (ranging 2Ω to 374kΩ)
- Inductors (1-10µH)
- Crystal oscillator (16.0 MHz)
- Ferrite beads, zener diodes

**Connectors & Interface:**
- Molex connectors (6-position, 40-circuit board-to-board, Ultrafit 3.5mm)
- Hirose 1.25mm headers
- Micro USB Type B connector
- Micro SD card connector

**Assembly & Miscellaneous:**
- SIM card cutter tool (Amazon)
- Fasteners (5mm Phillips screws)

## Use Cases & Applications
- **Volcano Monitoring:** Integration with Iridium satellite communications for remote data transmission from volcanic monitoring sites
- **Remote Communications:** Multi-hop power system enabling extended field operation via satellite link
- **Data Collection Platform:** Interface boards supporting integrated sensor and communication systems for NASA volcano observation missions

## Notable Details

**Key Timeline:**
- June 2-19: Design, modification, and PCB quoting phase
- June 18-19: Parts packaging and shipment to Summit Assembly
- June 22-25: Prototyping and testing phase (diode modifications to power supply boards)
- July 2: Final PCB manufacturing orders placed with NextPCB

**Supply Chain:**
- Primary component sourcing from Digi-Key ($89.87), Mouser Electronics ($103.06 + $13.01 + $188.45), and Amazon ($16.78)
- PCB fabrication contracted to NextPCB (Shenzhen, China) totaling $290.60 for 20 boards
- Assembly coordination through Summit Assembly (Denver, CO) managed by Thinh Nguyen
- Engineering support from MicroFirm Engineering (Erie, CO)

**Component Selections Indicate:**
- 32-bit embedded processing capability (STM32F405)
- Battery/low-power operation focus (buck regulators, voltage management)
- Satellite modem integration (SIM card interface for Iridium module)
- Multi-board architecture (separate interface and power supply designs)

This represents Phase III development work transitioning from concept to prototype hardware for volcano monitoring via Iridium satellite communications.