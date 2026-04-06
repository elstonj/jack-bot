# 2QSCC4 Soil Moisture Front End

## Document Metadata
- Type: Technical schematic/PCB design file
- Client/Agency: U.S. Air Force (AFWERX)
- Program/Solicitation: SBIR Phase II - Soil Moisture Mapping (2022.4)
- Date: 2/8/2024
- BST Products/Systems Referenced: MiCo Antenna Elements, ADALM-Pluto interface
- Key Personnel: Eryan Dai (Engineer)

## Executive Summary
This is a PCB schematic and board layout document for the RF front-end electronics of BST's soil moisture mapping system. The design includes dual RF signal chains with amplifiers, filtering, and hybrid coupler topology for antenna coupling, designed to interface with ADALM-Pluto software-defined radio modules.

## Technical Approach
The front-end implements a dual-channel RF architecture with the following key components:

**Signal Path:**
- Two independent RF input/output chains (RFIN1/RFOUT pairs)
- RF amplifiers using PMA2-63LN+ modules (U5A, U5B, U6A, U6B)
- Input impedance matching using 49.9Ω resistors (R1, R2)
- Bandpass filtering via CBP-1314R5AK1+ components (U3A-U4B) - dual channels with extensive ground planes

**RF Components:**
- Matching networks with small inductors (L1-L6: 12nH, 44nH)
- Low-loss capacitors (C1-C14: ranging from 0.9pF to 150pF at 25-50V ratings)
- 0 and 180° hybrid coupler topology for sum/delta outputs
- Isolators using 11305-10 components (U7A-U8B) to prevent reflections

**Power & Thermal Management:**
- 12V and 5V power supplies (VCC1)
- Thermistor monitoring circuits (PIAT101-PIAT204, COAT1, COAT2) for temperature compensation of RF attenuators (ThermalATT1, ThermalATT2)
- Adjustable current (Iadj1) for amplifier biasing

**Integration:**
- SMA connectors (J1-J4) for RF I/O and ADALM-Pluto interfaces
- Board designed for integration with MiCo Antenna Elements

## Products & Capabilities Described

### MiCo Antenna Elements
- Microwave coherent antenna system used with this RF front-end
- Receives RF signals from two output ports of the front-end electronics

### ADALM-Pluto Interface
- Software-defined radio platform receiving processed RF signals
- Two connection points (J3, J4) for transmitting sum and delta channel outputs
- Enables flexible signal processing for soil moisture measurement

## Use Cases & Applications
- **Soil Moisture Mapping:** Primary application for AFWERX Phase II program
- Defense/agricultural sensing for remote soil characterization

## Key Results
N/A - This is a design/schematic document, not a results report. It represents the implementation phase of the Phase II SBIR effort.

## Notable Details
- **Revision Control:** Document marked "RevD" indicating multiple design iterations
- **Dual-Channel Design:** Redundant signal chains suggest robust, differential measurement approach typical of coherent radar systems
- **Thermal Compensation:** Integrated thermistor monitoring suggests performance degradation with temperature is a known concern requiring active compensation
- **Hybrid Coupler Topology:** Sum/delta output configuration is consistent with interferometric or polarimetric radar measurement techniques
- **High-Performance Components:** Use of amplifiers, filters, and isolators indicates high-frequency operation likely in X/Ku band for soil penetration and resolution
- **File Location:** Stored in Active Projects indicating ongoing Phase II effort as of Feb 2024