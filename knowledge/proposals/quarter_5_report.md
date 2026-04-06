# Quarter 5 Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- Type: SBIR Phase II Interim Report
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II; Contract Number NNX14CG09C
- Date: July 2015
- BST Products/Systems Referenced: SuperSwift aircraft, Tempest avionics, LDCR (L-band Differential Correlation Radiometer), MiCo antennas
- Key Personnel: Jack Elston (last editor), M. Stachura (contact)

## Executive Summary
This Phase II quarterly report documents BST's progress on developing a small unmanned aircraft system (sUAS) for soil moisture mapping. Work in Q5 focused on completing the SuperSwift aircraft wing and nose cone design, developing a high-rate data logging system, mitigating electromagnetic interference on the LDCR radiometer, and conducting ground testing with the integrated system ahead of planned flight tests.

## Technical Approach

### SuperSwift Aircraft Design
- **Wing Structure**: Foam core (2.2 lbs surfboard foam, 100 PSI compressive strength) encased in fiberglass using wet layup construction
- **Design Loads**: Limit loads of -1.5G to +3.8G with gust loads from -4.2G to +6.2G, plus 1.5 factor of safety; designed to handle ultimate 10G load factor
- **Spar**: Straight carbon fiber tube (0.375" inner diameter, 0.459" outer diameter) spanning entire wing; joined to fuselage with 24" carbon rod (0.375" diameter)
- **Spar Location**: 30% chord of root
- **Skin**: Style 120 fiberglass; control surfaces covered with 1 ply 1.7oz Kevlar cloth
- **Cap Strips**: Carbon fiber strips (0.5" x 0.042") bonded above/below fuselage for additional strength; balsa wood strips applied on top and sanded to maintain airfoil shape
- **Weight Target**: Wing design total mass 1,621g (3.57 lbs), below 3.9 lbs Tempest constraint
- **Prototypes**: First prototype wings being completed by Northwind Composites; designed with intentional overbuilding for first prototype flyability with planned weight reduction

### Nose Cone
- Two layers of fiberglass with 3M foam core for stiffness
- Outer rim (1") at opening: 7 layers of fiberglass without foam for drilling/hardpoint attachment durability
- Mold completed; first cone built with minor design modifications for manufacturability

### High-Rate Data Logger System
- **Processor**: VIA EPIA P910 Pico ITX board
- **OS**: Customized Gentoo Linux on USB flash drive (206 MB, 5-second boot time)
- **Storage**: SATA III SSD (achieved ~270 MB/s sequential write speed with 128K block size); meets 220 MB/s bandwidth requirement
- **USB 3.0 SSD**: Initially tested but insufficient bandwidth on ITX platform (chip/driver limitation); external USB 3.0 drives underperformed compared to desktop testing
- **ADC Interface**: STM32F4 chip programmed to implement two CAN buses (NDVI, thermal, power control, autopilot) and UART interface; currently generates test packets with random data for FPGA throughput testing
- **ADC Sampling**: LTC2412 ADC on board; planned direct sampling of analog lines in next revision
- **Test Setup**: Full integration test planned next quarter with STM32F4, LTC2412 ADC, FPGA, and ITX boards

### LDCR (L-band Differential Correlation Radiometer) Integration
- **Architecture**: Lobe differential correlation design with dual patch antennas (nadir and zenith pointing)
- **Thermal Monitoring**: Six thermistors installed on receiving system (reference terminations, channel 2 isolator, local oscillator, channel 2 IF filter, correlator chip) plus two on MiCo antenna pairs
- **Thermal Performance**: 6σ variation measured at 0.3K, σ variation 0.05K (matches analytical prediction)
- **TEC Capability**: Heated channel 2 TEC and cooled channel 1 TEC supply ~47K temperature difference for calibration
- **Gain (Build01)**: Measured at 0.45 mV/K with lab setup; decreased to 0.23 mV/K in flight unit due to coaxial cable insertion loss (-0.5dB) and back side lobe ratio (17.8dB main-to-back)
- **ADC Reference**: 2.667V supply for maximum range utilization and TEC voltage avoidance of saturation
- **16-Channel ADC Mapping**: 
  - Channels 0-7, 9-11: LDCR DC voltages, thermal measurements, battery monitoring
  - Channel 8: External ADC reference voltage
  - Channels 13-15: Constant 2.3V source for coupled noise reduction

### EMI Mitigation
- **900 MHz Transmitter Interference**: Noise spikes at 5 Hz (aircraft transmission rate); mitigated through discrete component filtering and ferrite beads on all RF cabling; verified eliminated in anechoic chamber testing
- **Altimeter Laser Interference**: Quasi-periodic oscillation discovered in full system testing; source confirmed as laser altimeter high-current pulses (not L-band radiation); solution: decouple power supply lines

## Products & Capabilities Described

### SuperSwift Aircraft
- Small unmanned aircraft designed for soil moisture mapping
- Carries LDCR radiometer payload
- First prototypes under construction with overbuilt design for safety margin
- Planned weight reduction before Phase II conclusion
- Integration with Tempest avionics platform

### Tempest Avionics System
- Flight management and data logging system
- Includes 900 MHz telemetry radio (5 Hz transmission rate)
- Navigation board integration
- All systems programmed and verified through ground testing

### LDCR Radiometer
- L-band passive radiometer for soil moisture measurement
- Dual antenna configuration (nadir/zenith MiCo antennas)
- Receives signal from two channels with separate TEC control
- Correlator-based brightness temperature measurement
- Down-looking antenna capable of detecting brightness temperature range 230K-310K (tested)

### MiCo Antennas
- Microwave correlator antennas for L-band reception
- Main-to-back side lobe ratio: 17.8 dB (in flight configuration)
- Temperature-sensitive due to ohmic losses requiring thermal compensation

## Use Cases & Applications

### Primary Mission: Soil Moisture Mapping
- Small UAS platform for high-resolution soil moisture measurement
- Designed for remote sensing in agriculture and hydrological applications

### Test Site
- Soilscape test site in Oklahoma (associated with Prof. Moghaddam, USC)
- Ground truth validation planned using in situ sensors

### Ground Testing Configuration
- Car-mounted test rig: aircraft held at constant 34.5" height above ground
- Tested over mixed terrain: dry soil, mud patches, shallow puddles
- Capability to conduct quasi-mapping patterns and north-south passes
- Video camera synchronization (1 fps) for ground truth documentation

## Key Results

### SuperSwift Wing Design
- Weight analysis complete: 1,621g total mass for wing assembly
- Structural design validated for required load factors with 1.5 factor of safety
- First prototype in final manufacturing stages (expected delivery ~2 weeks from report)
- Design successfully balances weight constraints with structural requirements

### Data Logger Development
- SATA III interface identified as solution for required 220 MB/s write bandwidth
- Achieved ~270 MB/s sequential write speed with optimized block size
- Pico ITX board with customized Linux OS functional and tested
- SSD performance verified and suitable for high-rate instrument data logging

### LDCR System Performance
- Thermal measurement system stable and accurate (0.05K σ variation)
- EMI mitigation successful: 900 MHz interference completely eliminated through filtering
- Altimeter laser interference source identified and solution developed
- System ready for flight test pending final EMI fixes

### Ground Test Results (July 20, 2015 data)
- Brightness temperature range: 230K to 310K over test area
- Hard-packed dry roadbed correctly identified as hottest location (~310K) corresponding to brighter feature in spatial plot
- Down-looking antenna functioning as expected
- Clear qualitative agreement between radiometer and video imagery
- Up-looking antenna had SMA cable issue (replaced) during test

## Notable Details

### Manufacturing & Partnerships
- Flying Foam: Foam core cutting
- Northwind Composites: Wing assembly and fiberglass layup
- Avnet: Electronics and component sourcing

### Technical Challenges & Solutions
- **Data Logger Bandwidth**: USB 3.0 chipset limitation on ITX platform; solved by switching to SATA III interface
- **Thermal Monitoring**: Noise susceptibility on thermistor lines from 900 MHz telemetry; solved with extra filtering
- **EMI Environment**: Both transmitter and laser caused measurable interference; anechoic chamber used for isolation and verification
- **Cable Performance**: Insertion loss and side lobe ratio significantly reduced gain in flight configuration (0.45 mV/K → 0.23 mV/K); semi-rigid cables with lower loss planned for improvement

### Regulatory & Data Rights
- SBIR data protected under contract NNX14CG09C with 4-year restriction on government disclosure
- Standard SBIR data rights notice applied

### Test Plan Disruptions
- Initial flight test postponed due to Oklahoma flooding that disabled in situ sensors at Soilscape test site
- Temporary substitution of car-based ground mapping campaign to continue validation work
- Flight tests rescheduled pending restoration of test site sensor network

### System Readiness Status
- Tempest avionics fully programmed and verified
- Aircraft structure nearly complete (wings in fabrication)
- LDCR radiometer system cleared for flight after EMI mitigation verification
- All subsystems integrated and tested individually; full system integration test next quarter