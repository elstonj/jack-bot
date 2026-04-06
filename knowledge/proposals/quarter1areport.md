# Soil Moisture Mapping sUAS Phase II Interim Report

## Document Metadata
- **Type:** Phase II Interim Report (SBIR)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase II, Soil Moisture Mapping sUAS
- **Contract Number:** NNX14CG09C
- **Date:** May 2014
- **BST Products/Systems Referenced:** Tempest UAS, SwiftPilot Pro autopilot
- **Key Personnel:** Jack Elston (last editor); stachura@blackswifttech.com (contact)
- **BST Address:** 3080 Valmont Rd Ste 259, Boulder, CO 80301-2152

## Executive Summary
This interim report documents the first 6 weeks of Phase II work on a soil moisture mapping system for sUAS deployment. BST is developing an L-band radiometer payload (LDCR) integrated with NDVI/thermal sensors on the Tempest aircraft for initial deployment in August 2014 at a test site in Canton, Oklahoma. The team is on schedule despite minor delays in LDCR development due to noise mitigation issues, with flight certification proceeding through NASA and FAA channels.

## Technical Approach

### LDCR (Lobe Differencing Correlating Radiometer) Development
- **Design:** Quadrature phased two-channel upper sideband receiver with electronically selectable hot and cold calibration terminations using Peltier thermoelectric cooling (TEC) chips
- **Specifications:**
  - Two USB channels, center frequency 1440 MHz, bandwidth 130 MHz
  - IF signals: center frequency 225 MHz, bandwidth 80 MHz
  - Dimensions: 235 x 82 x 20 mm
  - Four amplifier stages at 22 dB gain each
  - Isolator with ~1 dB loss, mixer with -7 dB conversion efficiency
  - Total measured gain: 70.9 dB
  - Output noise power spectral density: -50 dBm in 100 kHz bandwidth
  - Total noise output power: -21 dBm
  - System noise temperature: assumed ~290 K (room temperature)

### Antenna Design (Two Types)

**L-Band Microstrip Patch Antenna (Ground Test Unit):**
- Frequency: 1413 MHz (air-dielectric)
- Configuration: Two identical back-to-back antennas (vertical orientation)
- Patch material: Copper; Ground plane: Aluminum
- Key dimensions:
  - Patch length (square): 93.5 mm
  - Ground plane length (square): 235.0 mm
  - Gap between ground plane and patch: 6.4 mm
  - Probe insert distance: 27.3 mm
- Bandwidth: 50 MHz for VSWR <1.2 (-10 dB reflection loss)
- Radome: 2" thick blue building insulation foam (causes ~2 MHz frequency pull)
- Measured scattering parameters at 1.4135 GHz: S11=-29 dB, S22=-26 dB, S12=-46 dB

**Microstrip Colinear (MiCo) Antenna Array (Aircraft Integration):**
- 2x2 rectangular L-band antenna array for Tempest integration
- Four elements: each a 5-segment microstrip collinear antenna with omnidirectional radiation pattern
- Axis oriented along aircraft roll axis
- Separation: Half-wave horizontal, quarter-wave vertical (67 mm = 6.6% of wavelength, adjusted for mutual coupling compensation)
- Uses 90° quadrature hybrid coupler for 2x2 Butler matrix
- Result: Distinct upward and downward lobes, with main lobe 14 dB larger than back lobe
- Compensation network under design to null back lobe

### LDCR Downconverter Performance Testing
- Proper downconversion of 1413 MHz sine wave observed in both channels
- Output spectrum shows bandpass signal with center frequency ~225 MHz, 10 dB bandwidth ~101 MHz (174-275 MHz)
- LO tone at 1185 MHz observed at -46 dBm power (to be filtered by Butterworth 2-pole low-pass filter)
- EMI/RFI mitigation measures implemented: decoupling capacitors (0.1 µF and 22 µF in parallel), series inductors (1 µH), shielded twisted triple wires for DC supply, 0.1 µF capacitors on TEC pins

## Products & Capabilities Described

### Tempest UAS
- Primary aircraft platform for soil moisture mapping mission
- Equipped with SwiftPilot Pro autopilot
- Integrates LDCR radiometer payload, NDVI/thermal sensors, power and data logging systems
- Capable of executing 11.1 km flight paths over test sites with light to moderate winds
- Flight simulation tested in X-Plane with autopilot software-in-the-loop

### SwiftPilot Pro Autopilot
- CAN bus interface for receiving sensor data packets
- Tested integration with NDVI/thermal sensor board
- Controls aircraft for autonomous mission flight

### NDVI/Thermal Sensor Board
- Prototype complete
- Includes photodiodes with Red band filters, NIR filters, and thermal sensor
- Converts Red, NIR, and thermal measurements to CAN bus data packets
- Revision ordered (expected 2 weeks from report date) with improvements: easier mounting, electrical fixes, white color to reduce thermal loading from sunlight

### Power and Data Logging Boards
- Power board: Tested and modified per LDCR requirements; ready for aircraft and ground test unit deployment
- Data logging board: Tested and ready for both aircraft and ground configurations
- Combo board (power + logging): Designed but assessment ongoing for necessity in August deployment

## Use Cases & Applications

### Primary Mission
**Soil Moisture Mapping via Radiometry**
- Location: Canton, Oklahoma test site
- Collaboration with Prof. Mahta Moghaddam
- L-band radiometer measures soil moisture through brightness temperature correlation
- Coordinated with existing soil moisture monitoring stations in the field
- August 2014 planned initial deployment

### Flight Characteristics
- Flight path length: 11.1 km
- Flight profile: Autonomous via SwiftPilot Pro
- Environmental conditions: Tested for light to moderate wind conditions
- Integration of multiple sensor types (L-band radiometer, NDVI optical, thermal IR) for comprehensive ground characterization

## Key Results

### LDCR Development Status
- Board provides expected functions of filtering, downconversion, and amplification
- Identified and mitigating LO signal leakage through LC filtering and power supply isolation
- One week behind schedule due to unforeseen noise issues, but buffer in schedule prevents overall project delay
- Successfully measured gain of 70.9 dB, matching theoretical expectations

### Antenna Validation
- L-band patch antennas fabricated and tested with expected performance
- MiCo antenna array simulated showing proper lobe formation (nadir/zenith beams)
- Mutual coupling addressed through spacing adjustment (67 mm) achieving 14 dB main-to-back lobe ratio
- Design moving toward manufacturing phase

### System Integration Progress
- NDVI/thermal sensor board prototype complete and tested
- Power management boards tested and modified per requirements
- Data logging functional
- Software tested for sensor data sampling and CAN bus communication

## Notable Details

### Flight Certification Status
- NASA flight request filed; initial questionnaires mostly complete
- Technical interchange meeting with airworthiness personnel scheduled for June 4, 2014
- FAA COA paperwork completed; COA anticipated in early July 2014
- Flight certification identified as major potential delay risk; contingency plans in place for schedule recovery if delayed

### Revised Work Plan (Key Milestones)
- Initial Prototype Deployment: April 18 – August 31, 2014
- Instrument testing completion: May 27, 2014
- CoCo antenna completion: June 11, 2014
- Ground testing of integrated system: May 27 – July 25, 2014
- AFSR Review Panel: July 8-15, 2014
- Final preparation: July 16-31, 2014
- Deployment in Canton, OK: August 1-7, 2014

### Technical Challenges Addressed
- **LDCR Noise:** Unforeseen noise issues identified and mitigated through component isolation, filtering, and power supply management
- **Mutual Coupling:** Antenna spacing optimized (quarter wavelength adjusted to 67 mm) to minimize back lobe
- **EMI/RFI:** Multi-pronged approach including decoupling, shielding, and planned in-band/out-of-band RFI leakage testing
- **LO Leakage:** Butterworth filter implementation planned for IF stage

### Competitive/Unique Aspects
- Dual antenna approach: ground test unit with microstrip patches, aircraft with advanced MiCo 2x2 array using quadrature hybrid couplers
- Integration of L-band radiometry with NDVI and thermal sensors for multi-parameter soil characterization
- Autonomous mission capability via SwiftPilot Pro with software-in-the-loop simulation validation

### Program Structure
- Phase I completed (prototype design/analysis)
- Phase II focuses on hardware development and initial field validation
- Structured development with clear milestones tied to August 2014 field deployment
- Collaboration with academic partner (Prof. Moghaddam, likely University of Michigan) for science validation