# October Interim Report: Soil Moisture Mapping sUAS Phase II-E

## Document Metadata
- **Type:** NASA SBIR Phase II-E Interim Report
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase II-E, Contract Number NNX14CG09C
- **Date:** October 2016
- **BST Products/Systems Referenced:** S2 (SuperSwift), Tempest
- **Key Personnel:** Maciej Stachura (contact: stachura@blackswifttech.com)

## Executive Summary
This interim report documents progress on Phase II-E of the NASA SBIR Soil Moisture Mapping sUAS project. Work focused on integrating an L-band radiometer antenna, upgrading FPGA logging software to 80 MS/s sampling rates, designing and implementing comprehensive EMI shielding for the S2 aircraft, conducting baseline EMI testing, and initiating flight certification for car-launch operations. The project addresses the need for a fully radio-quiet aircraft platform capable of precise soil moisture measurements via L-band radiometry.

## Technical Approach

### L-band Antenna Integration
- Antenna integrated, tuned, and tested with new payload scaffolding and fiberglass nose cone
- Antenna tuning techniques developed in Phase II applied successfully
- New reinforced payload tray with carbon fiber tubes designed for stiffness and ease of removal
- Antenna center frequency measured at 1.42 GHz (6.5 MHz higher than target of 1.4135 GHz)
- Return loss: ~35 dB at center frequency
- Tuning foam overlay can lower center frequency by 5 MHz; final tuning deferred until full assembly including wings

### FPGA High-Rate Data Logging
- Upgraded sampling rate from original 60 MS/s to 80 MS/s
- Data throughput at 80 MS/s: 305 MB/s through USB 3.0 interface
- Addressed data acquisition gaps caused by 16 MB contiguous block limits on CESYS FPGA board
- Improved guard band performance: at 80 MS/s, guard band of ±11.5 MHz on low-frequency side (vs. ±1.5 MHz at 60 MS/s) for bandwidth 200-240 MHz, reducing RFI effects
- Data structure: 32-bit samples with 2 header bits (data type: time, ADC, or UART)
  - ADC data: 30 bits (15 bits per channel: 14 data + 1 overflow)
  - Timestamp: 26-bit counter derived from ADC clock (increments every 8192 ADC clock cycles = 102.4 µs/0.1024 ms)
  - Overflow period: ~1 hour 54 minutes (exceeds maximum expected flight time)
  - 8192 (2^13) samples per timestamp for FFT spectral analysis compatibility
- Remaining tasks: on-board cross-spectral density (CSD) computation via FFT; add low-frequency digital data stream (autopilot nav, thermistors, NDVI/Thermal boards) time-tagged with radiometer data

### EMI Shielding Design & Implementation
**Design Philosophy:** Shield and ground all electronics, cabling, and actuators with maximum gap sizes ≤1/8 L-band wavelength (≈1 inch)

**Priority Areas (in order):**
1. Sensor package: radiometer, balun board, FPGA, Linux computer board, SSD, payload battery, wiring
2. Propulsion system: battery, ESC, motor, interconnecting wiring
3. Avionics package: autopilot, radio board, RC transmitter board, actuator boards, power distribution board
4. Servo wiring

**Sensor Package Shielding:**
- New technique: thin brass sheet cases (replacing costly machined aluminum) that are cut, bent, drilled, and soldered
- "Shoebox" style design: layered cases with hanging lids; each upper layer sits on previous with shoebox lid from next layer
- First prototype hand-built for design validation; finalizing 3D CAD for machine shop fabrication
- Assembly via soldering rig maintains straight, vertical walls and RF sealing with copper tape
- Weight reduction: ~1 lb saved from Phase II design
- Three cases for radiometer system with final top lid; all other electronics use base layer plus shoebox lid
- Currently evaluating screws or pressure-fit snap designs to replace soldering for easier disassembly
- Integrated prototypes shown fitting (tightly) inside S2 nose cone; vertical height optimization ongoing

**Propulsion System Shielding:**
- Copper mesh design with cowling around motor
- Fiberglass cowling with copper mesh glued inside, connected to ground
- Motor opening sized <1" in all dimensions to prevent L-band noise escape
- ESC and battery compartment covered in copper mesh
- Manufacturing plan: molded fiberglass part using fuselage/nose cone techniques

**Other Electronics Shielding:**
- Avionics boards to receive smaller brass shoebox-style cases
- Servo wiring also to be shielded

## EMI Testing Results

**Test 1: Sensor Shielding Effectiveness (50Ω terminations, no antenna)**
- **Without shielding:** Non-Gaussian signal with sinusoidal noise at ~0.2 MHz in both channels; evidence of external/UAS-generated noise pickup
- **With brass shielding:** Non-Gaussian signal completely removed; sinusoidal noise eliminated
- Conclusion: Shielding effectively eliminates circuit susceptibility to external signals

**Test 2: Aircraft Systems Effect (50Ω terminations, systems on vs. off)**
- Conditions: 900 MHz transmitter active, motor spinning at ~20% throttle (worst-case scenario)
- Result: Raw signal and FFT nearly identical between systems-on and systems-off cases
- Conclusion: Aircraft systems have negligible effect on radiometer electronics with new shielding
- Note: Out-of-band noise slightly higher in Channel 1 than Channel 2; source under investigation (not external)

**Test 3: Antenna-Connected Baseline (with antenna)**
- Result: ADC saturation at ±1V for all subsystem configurations (motor, transmitter, etc. individually activated)
- Issue: Comparison between cases impossible due to signal clipping
- Investigation ongoing: possible solutions include reducing gain or isolating USB 3.0 cable effects
- Plan: Replace USB 3.0 cable with sealed Linux single-board computer in brass case

## Products & Capabilities Described

### S2 (SuperSwift)
- **What it is:** Small unmanned aircraft system (sUAS) for precision soil moisture mapping via L-band radiometry
- **Capabilities addressed in this phase:**
  - Carries large payload volume (unmatched by comparable aircraft with similar wingspan)
  - Compatible with L-band radiometer antenna and high-rate data logging systems
  - Being retrofitted with comprehensive EMI shielding to operate as "radio quiet" platform
  - Supports multiple launch modes: hand-launch, car-launch (newly certified)
  - Existing launch pin design compatible with car launcher system
  - Avionics include autopilot capable of autonomous operations (preflight checks, airspeed-triggered release)
  - Motor/ESC can operate at low throttle (~20%) for testing
- **Specifications/Performance:**
  - Fiberglass fuselage, nose cone, and (planned) motor cowling
  - New reinforced payload tray with carbon fiber tubes
  - New lighter fiberglass nose cone (lower cost than previous design)
  - Integrated with: L-band antenna, FPGA radiometer board, balun board, Linux computer, SSD, payload battery, autopilot, 900 MHz transmitter, servo actuators

### Tempest
- **What it is:** Companion sUAS platform (likely earlier generation or sister system to S2)
- **Use in this project:** Car launcher testing/validation by University of Colorado; 10 successful launches with no failures

## Use Cases & Applications

### Primary Mission
- **Soil Moisture Mapping:** L-band radiometric remote sensing to measure soil moisture content
- **Key requirement:** "Radio quiet" operation to avoid self-interference and environmental RFI—driving entire EMI mitigation effort

### Testing/Certification
- **Pawnee National Grasslands (planned November testing):** Flight validation of certified car-launch capability in realistic operational environment

## Key Results

### Successfully Completed
1. **L-band antenna integration and tuning** with new scaffolding/nose cone; no compatibility issues with carbon fiber payload tray or fiberglass nose cone
2. **FPGA sampling upgrade** to 80 MS/s with improved RFI guard band (±11.5 MHz vs. ±1.5 MHz)
3. **EMI shielding design and prototype fabrication** for sensor package achieving ~1 lb weight reduction
4. **Baseline EMI characterization** of S2 with new shielding demonstrating noise elimination at 0.2 MHz and aircraft systems having negligible effect on radiometer circuits
5. **Flight certification addendum submitted** to AFSRB for car-launch capability

### In Progress / Pending
1. **Antenna tuning finalization** (after full assembly including wings)
2. **FPGA design refinements:**
   - On-board cross-spectral density (CSD) computation
   - Integration of low-frequency digital data streams (autopilot, thermistors, NDVI/Thermal boards)
3. **Motor cowling development** (3D CAD finalized; mold and fiberglass part manufacturing pending)
4. **Antenna-connected EMI baseline testing** (ADC saturation issue requires resolution)
5. **Flight testing in Pawnee National Grasslands** (planned November 2016)

### Outstanding Issues
- ADC saturation (±1V) when antenna connected during systems testing; gain reduction and/or USB cable isolation strategies under evaluation
- Out-of-band noise discrepancy between Channel 1 and Channel 2 (source unknown)
- Sensor package case vertical height optimization needed for easier aircraft integration
- Case assembly methodology refinement (soldering vs. screws/pressure-fit)

## Notable Details

### Partnerships & Collaboration
- **University of Colorado:** Developing car launcher in parallel with BST; conducted 10 successful Tempest car launches as proof of concept
- **NASA TM (Technical Monitor):** Working with BST to refine EMI shielding design
- **CET (presumably consulting firm):** Participated in SuperSwift EMI design review

### Design Philosophy & Innovation
- **Brass shoebox design:** Cost-effective, lightweight alternative to machined aluminum for RF shielding; enables rapid fabrication via machine shop
- **Copper mesh motor cowling:** Balances EMI mitigation with operational practicality (fiberglass + glued mesh vs. fully shielded enclosure)
- **Car launcher:** Simpler, more repeatable than hand-launch; superior to bungee launcher (no cold-temperature limitations, lower user risk)

### Competitive Advantages Highlighted
- S2 payload capacity unmatched by comparable aircraft with similar wingspan
- Rapid prototyping capability for shielding designs (hand-built first articles, then CAD → machine shop fabrication)
- Interdisciplinary integration (RF, avionics, mechanical design, flight operations)

### Technical Insights
- L-band wavelength constraint (1" maximum gap) is driving force for shielding design
- FPGA 16 MB block limit creates unavoidable "quiet periods" in high-rate sampling; mitigated by accepting 80 MS/s with gaps over continuous 60 MS/s
- FFT block size (8192 samples = 2^13) optimized for spectral analysis capabilities
- Environmental EMI testing (rather than purely anechoic) chosen to validate real-world shielding performance