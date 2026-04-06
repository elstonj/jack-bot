# LDCR sUAS Soil Moisture Sensor Status Update

## Document Metadata
- Type: Technical status update / progress report
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR Phase II (Soil Moisture)
- Date: July 23, 2015
- BST Products/Systems Referenced: LDCR (L-band Downwelling Brightness Temperature Correlator Radiometer), Tempest sUAS platform, MiCo antennas
- Key Personnel: Eryan Dai, Albin J. Gasiewski (University of Colorado), Maciej Stachura (Black Swift Technologies)

## Executive Summary
This quarterly progress report documents technical work on the LDCR soil moisture sensor payload integrated on Black Swift's Tempest sUAS platform. The update covers thermal characterization of the radiometer receiving system, electromagnetic interference mitigation efforts (particularly from onboard altimeter laser), and experimental data analysis from ground testing over wet grass fields.

## Technical Approach

**System Architecture:**
- LDCR uses lobe differential correlation architecture with two patch antennas pointing in nadir and zenith directions
- Output DC voltage is proportional to antenna temperature difference between upward- and downward-looking beams
- Measured gain: 0.45 mV/K for Build01 system

**Thermal Monitoring:**
- Six thermistors installed on receiving system monitoring: reference terminations, channel 2 isolator, local oscillator, channel 2 IF filter, and correlator chip
- Two additional thermistors on MiCo antenna pairs to measure thermal noise from ohmic losses
- 16-channel ADC board with 2.667V reference voltage to maximize conversion range
- Thermal measurements show 6σ variation of 0.3K (σ = 0.05K), matching analytical predictions
- Temperature control capability: ~47K difference achievable via heated channel 2 TEC and cooled channel 1 TEC for calibration

**EMI Mitigation:**
- Tested interference from 900MHz transmitting antenna (nearby, close to L-band MiCo antennas): negligible impact
- Identified altimeter laser as source of quasi-periodic oscillation in LDCR output through systematic testing (removing GPS antenna, 900MHz transmitter, altimeter in sequence)
- Two hypotheses for laser coupling: (1) high-current pulse driving laser, or (2) L-band radiation from laser
- Spectrum analysis with 1.4GHz probe antenna showed no detectable radiation signature
- Planned mitigation: decouple power supply lines of altimeter

## Products & Capabilities Described

### LDCR (L-band Downwelling Brightness Temperature Correlator Radiometer)
- **What it is:** L-band passive microwave radiometer for soil moisture sensing using differential correlation architecture
- **Integration:** Payload on Tempest sUAS platform
- **Performance specifications:**
  - Gain: 0.45 mV/K (Build01 with standard coaxial cables)
  - Effective gain with Tempest integration: 0.23 mV/K (accounting for -0.5dB insertion loss in cables and 17.8dB main-to-backlobe ratio)
  - Thermal stability: 0.05K standard deviation in thermal measurements
  - Calibration capability: ±47K temperature control via dual TECs

### MiCo Antennas
- Dual patch antennas (upper and lower pairs) with nadir and zenith pointing capability
- Main-to-backlobe ratio: 17.8dB (measured over wet grass field)
- Operating frequency: L-band (~1.4 GHz implied)
- Thermal noise characteristics measurable via antenna thermistors

### Tempest sUAS Platform
- Integrated payload platform carrying LDCR receiver, MiCo antennas, 900MHz transmitter, altimeter laser, navigation board, batteries
- Compact integration presenting EMI challenges requiring mitigation

## Use Cases & Applications

**Primary Application:**
- Soil moisture retrieval via passive L-band microwave radiometry
- Nadir and zenith brightness temperature correlation approach

**Test Scenarios:**
- Ground testing over wet grass field (July 2, 2015) yielding estimated antenna temperature measurements of ~87K
- Chamber testing for EMI characterization
- Thermal calibration range testing

## Key Results

**Thermal Characterization:**
- Thermal monitoring system validated with measured noise (0.05K σ) matching analytical predictions
- Demonstrated temperature measurement stability across 8 channels
- Identified temperature-dependent gain drift requiring thermal compensation

**EMI Analysis:**
- 900MHz transmitter interference: negligible (no detectable impact in 5-minute tests)
- Altimeter laser interference: confirmed as source of quasi-periodic oscillation with period and magnitude consistent across measurements
- Hypothesis narrowed to power supply coupling rather than radiation

**Ground Testing Results:**
- Antenna temperature over wet grass field: ~87K (from July 2 test)
- Insertion loss measured: -0.5dB (standard coaxial cables)
- System gain reduced from 0.45 to 0.23 mV/K with Tempest integration due to cable losses and antenna patterns

## Notable Details

- Document represents Quarter 5 deliverable from Phase II SBIR contract
- Collaboration between University of Colorado ECE Department and Black Swift Technologies
- Detailed instrumentation approach with 16-channel ADC enabling comprehensive thermal monitoring and diagnostics
- Systematic troubleshooting methodology for EMI (methodical hypothesis testing by isolating components)
- Planned improvement: upgrade to semi-rigid, lower-loss cables to restore radiometer gain closer to 0.45 mV/K specification
- Data logging and analysis capability demonstrates mature sensor integration and test infrastructure
- Thermal stability achieved appears suitable for operational deployment