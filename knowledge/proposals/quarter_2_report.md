# Quarter 2 Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- **Type:** NASA SBIR Phase II Interim Report (Q2)
- **Client/Agency:** NASA (contract number NNX14CG09C)
- **Program/Solicitation:** NASA SBIR Phase II - Soil Moisture Mapping sUAS
- **Date:** October 2014
- **BST Products/Systems Referenced:** Tempest UAS, SuperSwift (under development), LDCR (Lobe Differencing Correlation Radiometer), SwiftPilot Pro
- **Key Personnel:** Maciej Stachura (lead contact), Cory (aerodynamic design), Jack (power/correlator board), team at CET (Center for Environmental Technology)

---

## Executive Summary

Black Swift Technologies reports significant progress on Phase II development of an L-band microwave radiometer system for airborne soil moisture mapping. Key accomplishments include detailed analysis and optimization of a 2x2 microstrip colinear antenna array for the LDCR, ground testing of the LDCR Build01 portable sensor unit, and near-completion of aerodynamic and mechanical design for the SuperSwift aircraft platform. The team continues working toward securing flight permission from NASA Ames and the FAA, with deployment planned for winter 2014-2015 in Oklahoma.

---

## Technical Approach

### Overall Mission Architecture
- **Platform:** SuperSwift UAS (electric-powered pusher configuration, V-tail design)
- **Payload:** Lobe Differencing Correlation Radiometer (LDCR) for passive microwave soil moisture measurement
- **Operating Frequency:** 1.4135 GHz (L-band SMAP frequency band: 1400-1427 MHz)
- **Payload Capacity:** 3 lbs nominal, up to 5 lbs maximum
- **Flight Duration:** 90 minutes
- **Soil Penetration Depth:** ~5-10 cm under most conditions

### Antenna System Design
The core technical work focused on optimizing a 2x2 microstrip collinear (MiCo) antenna array:

**2x1 Subarray Architecture:**
- Two radiating elements, each a 5-segment microstrip collinear patch antenna
- Half-wavelength horizontal separation with 0° 3-dB coupler
- Operating center frequency: 1.4135 GHz
- Substrate: Rogers 4003C duroid (εr = 3.55, thickness 1.534 mm)
- Measured input return loss validated HFSS simulation results
- Omnidirectional individual element patterns produce null at horizon when paired

**2x2 Array Configuration:**
- Two subarray pairs stacked with styrofoam separation blocks
- ±90° quadrature phase shift between upper and lower pairs
- Quarter-wavelength vertical separation provides 90° phase shift for LDCR receiver channels
- Initial frequency pull of 20 MHz due to mutual coupling and proximity; compensated via design modifications (Table 3):
  - Operating center frequency shifted to 1.4335 GHz pre-modification
  - Short matching line length: 4 mm → 4.2 mm
  - Section lengths: 59.12 mm → 57.94 mm

**Optimization Work:**
- Tested vertical separation distances of 53.5–67.5 mm
- Optimal separation: 55.5 mm (2.5 mm larger than quarter-wavelength) for maximum main-to-back lobe ratio
- Best achieved main-to-back lobe ratio: 19.6 dB at 55.5 mm separation (Table 4)
- Simulated end-fire radiation patterns in nadir and zenith directions; ~20–47 dB rejection of horizontal radiation
- Developed frequency tuning method using dielectric loading (thin silicon RTV strips, εr = 3.6) to avoid aerodynamic drag penalty

**Integration into Tempest Fuselage:**
- 2x2 array adhered to fuselage exterior with styrofoam separation blocks
- Measured resonant frequency 9.5 MHz higher than simulation; attributed to board material tolerances (~2 MHz) and other factors under investigation
- Final return loss > -18.5 dB across working band with tuning

---

## Products & Capabilities Described

### SuperSwift UAS (Primary Platform)
**Status:** Design phase (Q2), construction to begin November 1, 2014

**Specifications:**
- **Configuration:** Electric-powered pusher with V-tail
- **Empty weight:** 7.5 lbs
- **Gross takeoff weight:** 10.5 lbs (with 3 lb soil moisture payload)
- **Wing area:** 1,100 in² (9.24 in mean aerodynamic chord)
- **Span:** 120 in
- **Wing loading:** 22 oz/ft²
- **Stall speed:** 33.5 ft/s at 6,000 ft altitude
- **Airfoil:** MH 70 (11.08% thickness-to-chord ratio, max CL ≈ 1.5, low pitching moment Cm ≈ -0.05)
- **Tail design:** NACA 0009 V-tail with 1° positive incidence
- **Static margin:** 21% (CG at 2.0 in from wing leading edge)
- **Motor:** Scorpion Precision Industry SII-4025-440KV (440 RPM/V, 0.025 Ω internal resistance, 1.1 A zero-torque current)
- **Propeller:** APC Thin Electric 12×12 inch
- **Cruise power consumption:** 71.5 W (83.4% efficiency)
- **Flight time:** 87 minutes predicted at 6,000 ft with 5-cell 11,000 mAh LiPo battery
- **Hand-launchable:** Yes (pusher configuration keeps nose clear and propeller safe from operator)

**Removable Nose Cone:**
- Fiberglass construction (similar to Tempest)
- Houses entire soil moisture mapping payload
- Weight and balance chart provided for payload integration guidance (Figure 22)
- Enables rapid payload swaps for different scientific missions

**Design Tools & Validation:**
- In-house developed spreadsheets (proven on multiple successful airframes)
- AVL (MIT vortex lattice model analysis)
- XFLR5 (low Reynolds number airfoil and wing analysis)
- X-Plane flight simulation with blade element theory
- SwiftPilot Pro software-in-the-loop for autonomous flight control validation

**Construction Plan:**
- Initial prototype: foam wings and fuselage (verify aerodynamics and payload mounting)
- Subsequent versions: composite construction (reduced weight, increased robustness)

### LDCR Build01 (Ground Test Unit)
**Configuration:**
- Portable, single-person operation
- Two L-band microstrip patch antennas (nadir and zenith looking)
- ZFL-1000LN+ amplifiers (two units)
- AD5391 correlator board
- Two NDVI sensor boards (10 cm from antennas)
  - Each with thermal IR, near-IR, and visible red sensors
  - One up-looking, one down-looking
- GPS antenna and navigation microcomputer
- Antennas encased in blue builder's foam (protects and isolates from nearby dielectrics)
- Peltier thermoelectric cooler/heater chips on terminating resistors for absolute thermal reference

**Operating Modes:**
- **Antenna mode:** Direct antenna-to-antenna differencing (Antenna Ch2 - Antenna Ch1)
- **Computer control mode:** PIN diode switching allows four measurement configurations:
  - Mode 0: Reference Ch2 - Reference Ch1 (zero differential, noise baseline)
  - Mode 1: Reference Ch2 - Antenna Ch1
  - Mode 2: Antenna Ch2 - Reference Ch1
  - Mode 3: Antenna Ch2 - Antenna Ch1

**Performance Metrics (Q2 Testing):**
- **Sensitivity (ΔT):** 3.7 K measured (6σ variation range: 0.01 V)
- **Theoretical ΔT (from noise analysis):** 2.57 K (assuming 500 K noise temperature per channel, 27 MHz bandwidth, 1.5 ms RC time constant)
- **Measured vs. theoretical discrepancy:** 44% higher than predicted (attributed to additional correlator circuitry noise, under investigation)
- **Bandwidth:** 27 MHz per channel
- **Integration time constant:** 1.5 ms
- **Output sensitivity:** G = 4.5×10⁻⁴ V/K (measured in indoor environment)
- **Brightness temperature assumptions (field test):** Zenith 5 K, nadir 200 K
- **Measured voltage change on inversion:** 0.17 V (matches theoretical prediction of 0.1755 V)

**Field Test Results:**
- Output DC voltage stability confirmed over grass field at 1–1.3 m height
- Good agreement between measured and theoretical output voltage
- Data collection validated with SD card recording capability

**Planned Improvements (Q3+):**
- Mechanical stabilization fixture with pole and fulcrum (eliminate orientation wavering)
- LN₂ cold calibration target for end-to-end sensor calibration
- Increased sample rate to 32 kS/s with 32× data averaging and 0.1 ms RC time constant
- Investigation of PIN diode switch crosstalk on output signal
- Construction of 4 additional complete LDCR units (one per SuperSwift, ground test unit, spare)

### LDCR Carrier (Version 2)
- **Material:** Machined aluminum
- **Weight reduction:** Factor of 3 lighter than Version 1
- **Function:** RF shielding for sensitive components in flight configuration
- **Status:** Design complete, fabrication planned for Q3

### High Rate Data Logger System
**Requirements (revised in Q2):**
- **Sampling:** 60 MS/s (third Nyquist zone sampling, down from original 180 MS/s requirement)
- **Resolution:** 14-bit dual channels
- **Net data rate:** 210 MB/s (down from 720 MB/s)
- **Storage per 1-hour sortie:** 756 GB (down from 2.6 TB)
- **Data inputs:**
  1. Two analog channels from LDCR (processed and amplified)
  2. Eight analog thermistor inputs (5 on LDCR, 2 on antenna, 1 reference)
  3. 50 Hz digital navigation data from autopilot (includes NDVI/thermal measurements and laser altimeter elevation)

**System Architecture:**
- **Analog/RF Board:** Signal conditioning, gain amplification, balun circuit for ADC, analog correlation (32 kS/s sampled, averaged to 1 kS/s)
- **A/D Board:** LTC2143-14 14-bit, 80 MS/s dual ADC
- **FPGA Module:** Spartan-6 based EFM-02 (Cesys)
- **Processor:** VIA EPIA-P910-10Q Pico ITX board (acts as USB host)
- **Storage:** Single SSD (SSD2GO Pocket, tested to 394 MB/s write speed)
- **Interface:** USB 3.0 (625 MB/s max theoretical)

**Data Products:**
1. Processed analog LDCR data at 60 MS/s (primary radiometer signal)
2. 50 Hz telemetry (autopilot, digitized thermistor, altitude)
3. 1 kS/s analog correlated data (lower rate processing)
4. All synchronized with common timestamp, separated post-flight via existing software

**Design Rationale:**
- Simplified from original concept (36 microSD card array reduced to single SSD)
- Reduced complexity and risk
- Rapid SSD swap between sorties vs. reading 11+ microSD cards
- USB 3.0 write speed (625 MB/s) sufficient for 210 MB/s radiometer data requirement
- FPGA handles data movement from ADC to USB; Linux on Pico-ITX handles SSD writing

---

## Use Cases & Applications

### Soil Moisture Mapping
- **Primary application:** Airborne passive microwave radiometry for soil moisture estimation
- **Frequency band:**