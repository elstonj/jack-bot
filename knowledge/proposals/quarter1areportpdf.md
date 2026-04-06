# Soil Moisture Mapping sUAS Phase II Interim Report

## Document Metadata
- **Type:** Phase II SBIR Interim Report
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase II, Contract Number NNX14CG09C
- **Date:** May 2014
- **BST Products/Systems Referenced:** Tempest UAS, SwiftPilot Pro autopilot
- **Key Personnel:** Jack Elston (last editor), contact email stachura@blackswifttech.com

## Executive Summary
Black Swift Technologies is executing a NASA Phase II SBIR contract to develop an unmanned aircraft system (UAS) capable of soil moisture mapping using an L-band radiometer payload. The interim report documents progress during the first 6 weeks of Phase II (as of May 2014), covering sensor development, aircraft integration, and preparations for an initial prototype deployment planned for August 2014 in Canton, Oklahoma.

## Technical Approach
The program focuses on integrating three key sensor systems onto the Tempest UAS:

1. **LDCR (Lobe Differencing Correlating Radiometer)** – An L-band microwave radiometer for measuring soil moisture
   - Quadrature phased two-channel upper sideband receiver
   - Center frequency: 1440 MHz with 130 MHz bandwidth per channel
   - IF output: 225 MHz center frequency, 80 MHz bandwidth
   - Includes electronically selectable hot/cold internal calibration terminations using Peltier TEC chips
   - Measured total system gain: 70.9 dB

2. **Antenna Systems** – Two complementary designs:
   - **L-Band Microstrip Patch Antennas** (ground test unit): Dual 1413-MHz air-dielectric patch antennas arranged vertically (upward/downward looking), 50 MHz bandwidth for VSWR < 1.2
   - **MiCo (Microstrip Collinear) Antenna Array** (aircraft integration): 2×2 rectangular array with four 5-segment omnidirectional collinear elements; arranged at half-wave horizontal and quarter-wave vertical separations to produce nadir/zenith-directed end-fire beams with 90° quadrature hybrid coupler

3. **Auxiliary Sensors:**
   - NDVI/Thermal sensor board for vegetation and temperature data
   - Power and data logging boards
   - Integration with SwiftPilot Pro autopilot via CAN bus

## Products & Capabilities Described

### Tempest UAS
- Unspecified, fully autonomous aircraft platform
- Software-in-the-loop simulation capability demonstrated in X-Plane
- Capable of 11.1 km flight paths in light-to-moderate winds
- Flight-certified path planned over test site in Oklahoma

### LDCR Radiometer Downconverter
- Dimensions: 235 × 82 × 20 mm
- Four amplifier stages (22 dB each), isolator (~1 dB loss), mixer (−7 dB conversion efficiency)
- Expected maximum gain: ~80 dB; measured system gain: 70.9 dB
- Measured output noise power spectral density: −50 dBm in 100 kHz bandwidth (−21 dBm total)
- LO leakage at 1185 MHz observed at −46 dBm (to be filtered with Butterworth 2-pole low-pass filter)
- RFI mitigation implemented: decoupling capacitors (0.1 µF and 22 µF), series inductors (1 µH), shielded twisted triple power supply wires

### L-Band Patch Antennas (Ground Test)
- **Frequency:** 1413 MHz tuned
- **Dimensions:** Patch 93.5 × 93.5 mm, ground plane 235 × 235 mm, gap 6.4 mm, probe distance 27.3 mm
- **Materials:** Copper patch, aluminum ground plane, 2″ blue building insulation foam radome
- **Performance:** Measured bandwidth 50 MHz for VSWR < 1.2 (−10 dB return loss); resonant frequency pull from radome ~2 MHz
- **Isolation (back-to-back):** S12 = −46 dB at all measured frequencies
- **Return losses (at 1.4135 GHz):** S11 = −29 dB, S22 = −26 dB

### MiCo Antenna Array (Aircraft-Integrated)
- Four omnidirectional collinear elements in 2×2 arrangement
- Each element: 5-segment microstrip collinear design
- Orientation: Omnidirectional axis aligned with aircraft roll axis
- Vertical spacing: 67 mm (14 mm above quarter-wavelength, 6.6% of wavelength increase for mutual coupling compensation)
- Quadrature hybrid coupler/Butler matrix forms distinct upward and downward-pointing lobes
- Main lobe-to-back lobe ratio: 14 dB (with mutual coupling compensation)
- Compensation network under design to null back lobe

### NDVI/Thermal Sensor Board
- Measures Red band, Near-Infrared (NIR), and thermal channels
- Interfaced via CAN bus to SwiftPilot Pro
- Prototype completed, revised version ordered for improved mounting and thermal properties (changed to white for thermal management)
- Software implemented for data sampling and CAN packet conversion

### Power and Data Logging Boards
- Power board: Modified for LDCR power requirements, tested and ready
- Logging board: Tested and ready for aircraft and ground use
- Combination board under consideration to reduce wiring and integration complexity

## Use Cases & Applications

### Primary Mission
**Soil Moisture Mapping** – Radiometric measurement of soil moisture at validation test site in Canton, Oklahoma using L-band microwave emission from soil

### Deployment Scenario
- Initial prototype deployment: August 2014 (Canton, OK)
- 11.1 km autonomous flight path
- Coordination with Prof. Mahta Moghaddam (soil moisture validation researcher)
- Cross-validation with ground-based soil moisture stations

## Key Results

### LDCR Functional Testing Results
- **Downconversion Performance:** Proper downconversion of 1413 MHz input signal confirmed in both channels
- **Noise Performance:** Output noise power spectral density −50 dBm in 100 kHz RBW (total −21 dBm) matches expected thermal noise floor
- **System Gain Verification:** Measured 70.9 dB gain validates design calculations; consistent with 4× 22 dB amplifiers minus isolator (−1 dB) and mixer (−7 dB) losses plus variable gain control (−9 dB additional loss)
- **LO Leakage:** Single LO tone at 1185 MHz observed at −46 dBm; mitigation via Butterworth filter implementation

### Antenna Development Results
- **Patch Antenna Validation:** Dual-antenna configuration (back-to-back isolation −46 dB) suitable for ground test LDCR verification
- **MiCo Array Simulation:** Quadrature hybrid coupler successfully produces dual nadir/zenith lobes; mutual coupling compensation achieved with 67 mm spacing (14 mm> λ/4) yielding 14 dB main-to-back lobe ratio

### Integration Progress
- NDVI board prototype complete and operational
- Power/logging systems tested and ready
- Flight simulation in X-Plane with autopilot software-in-the-loop completed successfully

## Notable Details

### Schedule Status
- **Overall Status:** On pace for August 2014 deployment with buffer for unforeseen delays
- **Current Delay:** One week behind schedule on LDCR work due to noise issues (does not impact overall timeline)
- **Critical Path Risk:** Flight certification (NASA airworthiness and FAA COA) is identified as major potential obstacle; contingency planning in place to advance post-deployment tasks if certification delays occur

### Flight Certification Progress
- **NASA:** Flight request filed; initial questionnaires mostly complete; first technical interchange meeting scheduled for June 4, 2014
- **FAA:** COA (Certificate of Airworthiness) paperwork completed; approval anticipated early July
- **Test Site:** Mapped flight area with planned path over Canton, OK test site

### Technical Challenges & Mitigation
1. **EMI/RFI Sensitivity:** Significant concern for LDCR downconverter; mitigation includes decoupling capacitors, inductors, shielded twisted-pair power lines, and planned in-band/out-of-band RFI testing
2. **Mutual Coupling (MiCo Antenna):** Addressed via spacing optimization (67 mm vs. theoretical 53 mm); compensation network with low loss and good matching under design

### Deliverables Completed
- Ground test LDCR unit design with dual patch antennas
- LDCR radiometer downconverter functional and tested
- NDVI/Thermal sensor board prototype
- Power and data logging boards (tested)
- MiCo antenna array design with simulated radiation patterns
- Aircraft integration plan and flight simulation

### Deliverables In Progress (as of May 2014)
- MiCo antenna fabrication and integration
- Final aircraft-sensor integration and checkout
- Ground system testing over Oklahoma test fields (30 June – 25 July planned)
- Flight certification documentation

### Coordination
- Partnering with Prof. Mahta Moghaddam (likely University of Michigan or USC) for soil moisture validation and test site coordination
- NASA and FAA regulatory coordination for flight authorization