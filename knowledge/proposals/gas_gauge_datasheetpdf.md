# Gas Gauge Datasheet (bq40z80)

## Document Metadata
- Type: Technical datasheet (product specification)
- Client/Agency: Texas Instruments (TI) / general commercial distribution
- Program/Solicitation: Not applicable (product datasheet)
- Date: June 2018 (revised November 2018)
- BST Products/Systems Referenced: None. This is a commercial off-the-shelf (COTS) component datasheet, not a BST document.
- Key Personnel: None named (Texas Instruments document)

## Executive Summary
This is a technical datasheet for the Texas Instruments bq40z80 battery pack manager IC, a fully integrated single-chip solution for gas gauging, protection, and authentication in 2-series to 7-series Li-Ion and Li-Polymer battery packs. The device incorporates patented Impedance Track™ technology for accurate charge measurement and supports comprehensive safety protection features, cell balancing, and SMBus communications.

## Important Note
**This document appears to be a commercial component datasheet from Texas Instruments, not a Black Swift Technologies proposal, report, or capability document.** It was found in BST's file structure under "NASA/2017 SBIR/Internal Intelligence/Phase II/Deliverables/NTR/Battery Board/" and likely represents a COTS component that BST evaluated or incorporated into battery management electronics for a NASA project. The document itself contains no BST branding, references, or proprietary information.

## Technical Approach
The bq40z80 provides:
- **Gas Gauging:** Impedance Track algorithm measures available capacity by integrating charge/discharge current, compensates for temperature and state-of-charge effects, estimates self-discharge
- **Current Measurement:** Delta-sigma integrating ADC measures voltage drop across 1-3 mΩ sense resistor (SRP/SRN inputs)
- **Voltage Measurement:** Individual cell voltages (VC1-VC7) measured via 16-bit ADC with scaling factors (0.2 LSB for cell voltages, 0.0286 LSB for pack voltage)
- **Cell Balancing:** Internal bypass switches (up to 10 mA per cell) or external FET control for cells 1-6; cell 7 uses external balancing via CB7EN pin
- **Protection:** Software-based 1st and 2nd level safety protections against overvoltage, undervoltage, overcurrent, short-circuit, overload, overtemperature
- **Authentication:** ECC (Elliptic Curve Cryptography) or SHA-1 with secure memory for key storage
- **Communication:** SMBus v1.1 interface (10-400 kHz, MASTER/SLAVE modes), supports SBS commands and packet error checking (PEC)

## Products & Capabilities Described

### bq40z80 Battery Pack Manager IC

**What it is:**
- 32-lead VQFN package (4.0 × 4.0 mm)
- Single-chip battery management IC supporting 2-7 series Li-Ion/Li-Polymer cells
- Fully integrated: includes oscillators, ADCs, references, FET drivers, cell balancing

**Key Specifications:**
- **Supply Voltage:** 2.2-32 V
- **Supply Current (NORMAL mode):** 663 µA typical
- **Supply Current (SLEEP mode):** 96 µA typical
- **Supply Current (SHUTDOWN mode):** 1.4 µA
- **Operating Temperature:** –40°C to 85°C
- **Internal 1.8V LDO:** Regulated voltage 1.6-2.0 V, 20 mA output current limit
- **Cell Voltage Measurement:** 0-5 V input range per cell, 16-bit resolution, ±8.5 LSB INL
- **Pack Voltage Measurement:** 0-32 V, scaling factor 0.0286 LSB
- **Current Measurement Range:** ±100 mV (or ±200 mV with RSNS=1), 250 ms conversion time
- **ADC Conversion Time:** 1.95-31.25 ms (configurable), effective resolution 9-15 bits
- **Cell Balancing:** Internal RCB ~200 Ω, external control up to 7 cells
- **Temperature Sensors:** 4 external (NTC thermistor) + 1 internal, 18 kΩ pullup
- **SMBus Frequency:** 10-100 kHz standard, 40-400 kHz XL mode
- **Oscillators:** 16.78 MHz HFO (±3.5% over –40 to 85°C), 262 kHz LFO (±2.5%)

**Protection Features:**
- **Primary (1st Level):** Cell overvoltage, undervoltage, overcurrent (charge/discharge), overload, short-circuit (charge/discharge), overtemperature (charge/discharge), undertemperature (charge/discharge), precharge timeout, overcharge protection
- **Secondary (2nd Level):** Permanent failure detection for overvoltage, undertemperature, FET overtemperature, Qmax/impedance imbalance, capacity degradation, cell balancing failure, open cell connections, thermistor failures, etc. Can drive external fuse via FUSE pin to permanently disable pack

**FET Drivers:**
- **CHG (N-CH):** Charge FET gate drive, output 10.5-12.5 V above BAT (at high voltage)
- **DSG (N-CH):** Discharge FET gate drive, output 10.5-12.5 V above PACK
- **PCHG (P-CH):** Precharge FET gate drive, output 6-8 V (VCC – VPCHG)
- **Rise/Fall times:** 200-500 µs rise, 40-300 µs fall (DSG), 40-200 µs fall (CHG/PCHG)

**Multifunction Pins:**
- 8 configurable pins (12, 13, 15, 16, 17, 20, 21, 22) can be assigned as:
  - Thermistor inputs (TS3, TS4)
  - ADC inputs (ADCIN1, ADCIN2)
  - LED controls (LEDCNTLA/B/C) with 22.5 mA sink capability
  - GPIO (input/output, various voltage levels)
  - System present detection (PRES)
  - Emergency shutdown (SHUTDN)
  - Display button (DISP)
  - Pre-discharge control (PDSG)
  - Cell 7 voltage sense divider enable (VC7EN)
  - Cell 7 external balancing (CB7EN)

**Authentication:**
- EC-KCDSA signature generation: 375 ms signing time
- Supports up to 20,000 authentication operations
- Current during auth: 1350 µA (NORMAL + AUTH mode)

**Data Logging:**
- Lifetime data updated every 10 hours: max/min cell voltages, max delta voltage, max currents, max power, max/min temperatures, FET temperature, safety event counts, charge termination counts, Qmax/Ra update counts, shutdown event counts, cell balancing time per cell

**Charge Control:**
- JEITA temperature range support with configurable sub-ranges
- Adaptive charging current based on cell voltage
- Voltage-based cell balancing during charging
- Reports charging voltage/current to smart charger via SMBus
- Charge suspend/inhibit for out-of-range temperatures
- Supports TURBO Mode 2.0 / Intel Dynamic Battery Power Technology (DBPTv2)

**LED Display:**
- 3-, 4-, or 5-segment LED display support
- Shows remaining capacity or permanent fault (PF) error code
- 124 Hz refresh rate

**IATA Support:**
- Special commands and procedures for air transport compliance

## Use Cases & Applications
- Industrial appliances and robots
- Handheld garden and power tools
- Battery-powered vacuums
- Energy storage systems and UPS
- Smart battery packs with embedded gauging and protection
- Systems requiring cell balancing and comprehensive monitoring

## Key Technical Data

### Electrical Characteristics (Summary)
| Parameter | Value |
|-----------|-------|
| Cell Voltage Scaling | 0.2 LSB/V |
| Pack Voltage Scaling | 0.0286 LSB/V |
| Coulomb Counter Resolution | ±5.2 to ±22.3 LSB (16-bit) |
| Current OCD Threshold | ±50 to ±100 mV (programmable) |
| SCC Threshold | 22.2-200 mV (programmable) |
| Temperature Drift | ±80 PPM/°C (references) |
| High-Frequency Oscillator | 16.78 MHz ±3.5% |
| Low-Frequency Oscillator | 262 kHz ±2.5% |
| Flash Endurance | 1,000 cycles (instruction), 20,000 cycles (data) |

### Thermal Performance
- Junction-to-ambient thermal resistance: 47.4 °C/W (QFN-32)
- Junction-to-board: 14.7 °C/W
- Operating temperature: –40°C to 85°C

## Notable Details
- **Fully Integrated:** No external oscillators, references, or major support components required
- **Compact Package:** 32-lead QFN minimizes PCB area and cost
- **Impedance Track™ Patent:** TI proprietary algorithm for accurate capacity measurement even with aging batteries
- **Configurable Protection:** All protection thresholds and timing can be programmed via data flash
- **Cell Balancing:** Supports both internal bypass (up to 10 mA) and external FET control for higher currents
- **Diagnostic Black Box:** Lifetime data logging enables post-failure analysis
- **Multiple Temperature Sensors:** Up to 4 external + 1 internal for comprehensive thermal monitoring
- **SMBus Master/Slave:** Can communicate bidirectionally with host systems or act as master to chargers
- **ECC Authentication:** 163-bit cryptographic key system for genuine pack identification
- **TURBO Mode 2.0/DBPTv2:** Enables dynamic power management in Intel-based systems

### Configuration Example (7-Series Pack)
The datasheet provides a simplified schematic showing a complete 7-series configuration with:
- 7 cell voltage dividers (VC1-VC6 direct sense, VC7 via external divider)
- 2 external thermistors (TS1, TS2) + internal sensor
- Cell balancing for cell 7 via external NFET
- SMBus interface to host
- 3 LED segments for charge indication
- System present (PRES) detection
- Precharge circuit (PCHG FET)
- Charge/discharge FETs (CHG, DSG)
- Optional external fuse drive (FUSE)

---

**Assessment:** This is a standard TI component datasheet with no BST proprietary content. Its presence in BST's NASA SBIR file suggests the bq40z80 was evaluated as a COTS solution for battery management electronics, possibly for the AeroPod platform or other airborne systems requiring long-duration operation and comprehensive battery monitoring.