# MS8607-02BA01 PTH Fusion Sensor Datasheet

## Document Metadata
- **Type:** Component datasheet/technical specification
- **Manufacturer:** Measurement Specialties (MEAS)
- **Part Number:** MS8607-02BA01
- **Date:** August 25, 2014 (Preliminary)
- **Document Code:** DA8607-02BA01_000
- **BST Context:** Found in Black Swift Technologies NASA 2016 SBIR Volcano Phase I project files; likely evaluated as potential sensor component for environmental monitoring applications

## Executive Summary
The MS8607 is a compact, integrated environmental sensor module combining pressure, temperature, and humidity (PTH) measurement in a single 5×3×1 mm QFN package. Designed for low-power applications requiring high accuracy across a wide operational range, this fully factory-calibrated sensor communicates via I2C interface and is optimized for portable and embedded systems.

## Technical Approach & Sensor Design
The MS8607 employs a dual-sensor architecture:
- **Pressure & Temperature:** Piezoresistive MEMS sensor measuring 10–2000 mbar and -40 to +85°C
- **Relative Humidity:** Capacitive-type humidity sensor measuring 0–100% RH
- **Signal Processing:** Dual ΔΣ (delta-sigma) ADC integrated circuits convert analog outputs to digital values (24-bit for P/T, 12–16-bit for RH depending on configuration)
- **Calibration:** Fully factory-calibrated with coefficients stored in on-chip PROM (112 bits total across two separate memories: P&T and RH)

## Products & Capabilities Described

### MS8607-02BA01 Sensor Module

**Physical Specifications:**
- Package: QFN, 5×3×1 mm³
- Supply voltage: 1.5–3.6 V (nominal 3.0 V)
- I2C interface: 400 kHz clock, two distinct I2C addresses (0x76 for P/T, 0x40 for RH)
- Pin configuration: VDD (1), GND (3), SDA (7), SCL (8); pins 2, 4, 5, 6 are NC

**Pressure Performance:**
- Operating range: 10–2000 mbar (extended from 300–1200 mbar nominal)
- Absolute accuracy @25°C (300–1200 mbar): ±2 mbar
- Highest resolution: 0.016 mbar
- Long-term stability: ±1 mbar/year
- Response time: <5 ms
- Oversampling ratio (OSR) options: 256–8192 for resolution/speed trade-offs

**Temperature Performance:**
- Operating range: -40 to +85°C
- Absolute accuracy @25°C: ±1°C
- Resolution: 0.01°C
- Long-term stability: ±0.5°C/year
- Response time: <5 ms

**Relative Humidity Performance:**
- Operating range: 0–100% RH (raw output extends -6 to 118% RH with clamping)
- Absolute accuracy @25°C (20–80% RH): ±3% RH
- Resolution: 0.04% RH (highest mode, OSR=4096)
- Response time: ~5 seconds (at 63% recovery, 33–75% RH step, 3 m/s airflow)
- On-chip heater: Optional (~5.5 mW, provides 0.5–1.5°C rise) for diagnostics

**Power Consumption:**
- Supply current (P/T conversion @1 Hz): 0.63–20.09 µA depending on OSR
- Supply current (RH conversion @1 Hz): 0.78–6.22 µA depending on OSR
- Peak current (P/T conversion): 1.25 mA
- Peak current (RH conversion): 0.45 mA
- Standby current: 0.03–0.24 µA @25°C

**ADC Specifications:**
- P&T ADC output: 24-bit
- RH ADC output: 12–16-bit (depending on OSR setting)
- Conversion time: 0.54–17.2 ms (P/T); 2.08–15.89 ms (RH) depending on OSR

**Environmental Robustness:**
- ESD protection: ±2 kV (Human Body Model)
- Maximum soldering temperature: 250°C (40 sec max)
- Storage temperature: -20 to +85°C
- Latch-up protection: JEDEC standard, ±100 mA
- Reflow soldering recovery time: 5 days minimum (66% recovery)

## Calibration & Software Compensation

The sensor includes:
- **Factory calibration coefficients (C1–C6):** Stored in P&T PROM for pressure sensitivity, offset, temperature coefficients
- **RH calibration data:** Stored in separate RH PROM with factory-defined values
- **CRC-4 error checking:** Both PROM memories include 4-bit CRC for data integrity verification (C code implementations provided)
- **Temperature-compensated pressure calculation:** First-order compensation standard; second-order compensation recommended for enhanced accuracy over temperature, especially at low temperatures (<20°C and <-15°C)
- **RH calculation:** Linear formula with ±6 to 118% RH output range clamping

## I2C Communication Protocol

**Two distinct I2C address schemes:**
1. **Pressure & Temperature (I2C address 0x76):**
   - Commands: Reset, PROM read, D1/D2 conversion, ADC read
   - Configurable OSR (256–8192) for resolution/speed trade-off
   - 24-bit data output

2. **Relative Humidity (I2C address 0x40):**
   - Commands: Reset, user register read/write, RH measure (Hold/No-Hold modes), PROM read
   - Configurable OSR (256–4096) via user register bits 0 & 7
   - Optional on-chip heater enable (bit 2)
   - Battery state monitoring (bit 6: VDD threshold 2.25 V)
   - Measurement resolution: 4 levels (256, 1024, 2048, 4096 OSR)
   - 16-bit data output with 2 status bits

**Hold Master vs. No-Hold Master modes:** Allow I2C bus sharing with the sensor either blocking the SCL line during measurement or the MCU polling for measurement completion.

## Use Cases & Applications (from datasheet context)

The MS8607 is designed for:
- **Smart phones and tablets:** Environmental sensing and altitude estimation
- **HVAC systems:** Climate control monitoring
- **Weather stations:** Environmental data logging
- **Portable environmental monitoring:** Compact form factor and low power ideal for battery-powered devices
- **Industrial PTH sensing:** Ruggedized design and wide operating range

**BST relevance (inferred):** The sensor was evaluated for integration into BST's environmental monitoring systems, particularly for volcano monitoring applications (based on file location in NASA SBIR Volcano Phase I deliverables). The compact size, low power consumption, wide pressure range (10–2000 mbar covers high-altitude operation), and integrated sensor fusion align with airborne environmental measurement platforms.

## Notable Technical Details

1. **MEMS technology:** Leverages proven MEMS fabrication and Measurement Specialties' decade+ experience in high-volume sensor module production

2. **Flexible integration:** I2C bus allows multiple sensor addressing; supports PCB or flexible cable interconnection

3. **Assembly considerations:**
   - Vacuum pick-and-place compatible
   - No pressure hysteresis due to low-stress assembly
   - Requires Class 10,000 cleanroom or particle protection during assembly
   - Mandatory 220–470 nF decoupling capacitor on VDD for accuracy
   - "No-clean" solder paste recommended to avoid sensor damage during cleaning

4. **Supply voltage sensitivity:** Maximum error with supply voltage variation (VDD 1.5–3.6 V): ±0.5 mbar (P), ±0.3°C (T), ±0.25% RH

5. **Hysteresis & recovery:** Reflow soldering impact up to ±2 mbar (pressure) with 5-day recovery period; long-term stability excellent (±1 mbar/year for pressure, ±0.5°C/year for temperature)

6. **Ordering:** Available as MS860702BA01-50 in Tape & Reel packaging

---

**Note:** This is a component datasheet, not a Black Swift Technologies proposal or report. It documents a sensor component that BST engineers likely evaluated for potential integration into environmental monitoring payloads, particularly for the NASA Volcano SBIR project. No BST-specific technical approach, results, or proprietary information is contained in this document.