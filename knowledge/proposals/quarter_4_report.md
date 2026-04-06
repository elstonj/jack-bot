# Quarter 4 Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- Type: Interim quarterly progress report (Phase II, Quarter 4)
- Client/Agency: NASA
- Program/Solicitation: SBIR Phase II; Contract Number NNX14CG09C
- Date: April 2015
- BST Products/Systems Referenced: Tempest (sUAS), SuperSwift (sUAS), LDCR (Lobe Differential Correlation Radiometer), SwiftPilot Pro, MiCo antennas, High Rate Data Logger, FPGA systems
- Key Personnel: Maciej Stachura (primary contact, stachura@blackswifttech.com)

## Executive Summary

Black Swift Technologies completed Q4 work on the NASA-funded Soil Moisture Mapping (SMM) sUAS project, advancing two aircraft platforms toward deployment. The Tempest sUAS received FAA Certificate of Authorization (COA 2014-CSA-200) for Canton, Oklahoma flights and was integrated with the complete SMM instrument payload. The SuperSwift sUAS underwent detailed mechanical design refinement with emphasis on tool-less field assembly and payload swapping, and scaffolding prototypes were constructed and tested. A high-rate data logger system was engineered to simultaneously capture L-band radiometer data at 80 MHz with precision timestamping and on-board FFT processing for soil moisture inversion.

## Technical Approach

**Overall Strategy:** BST pursued parallel development of two sUAS platforms—Tempest for initial Canton, OK deployment and SuperSwift for a larger second deployment in California. Work focused on:
1. FAA flight certification for both aircraft
2. Mechanical design optimization for field operability and payload flexibility
3. Advanced data acquisition electronics to handle high-speed LDCR sampler output
4. Integration and ground testing of complete avionic and instrument systems

**Key Technical Decisions:**
- Separated composite nose cone from payload structure to enable tool-less payload swapping and access
- Adopted 2D laser-cut scaffolding (⅛" spruce prototypes, eventual fiberglass production) for cost-effective manufacturability and rapid payload reconfiguration
- Increased SuperSwift propeller diameter from 12" to 14" to improve climb performance (220 → 950 ft/min at 6,000 ft) despite modest flight time reduction (126 → 109 min)
- Modified LDCR receiving board with 90° hybrid to accommodate MiCo (microstrip collinear) antenna arrays replacing patch antennas
- Designed removable tail boom assembly with hexagonal carbon rod (easier orientation control) and pogo pin electrical connectors

## Products & Capabilities Described

### **Tempest sUAS**
- Status: Flight-ready for Canton, OK deployment
- Integration: Complete SMM payload (LDCR, high-rate data logger, antenna arrays, thermistor network) integrated into airframe
- Certification: FAA COA 2014-CSA-200 obtained
- Avionics: SwiftPilot Pro autopilot (transmits telemetry at 900 MHz including NDVI data at 50 Hz)
- Ground testing: Completed with both mass model and actual LDCR payload; identified minor sensitivity and RFI issues under investigation

### **SuperSwift sUAS**
- Status: Detailed design and scaffolding prototypes completed; composite nose cone and fuselage manufacturing to begin Q5
- Design Specifications:
  - Fuselage diameter increased to 8" (from 7.45") to accommodate larger payload volume
  - Propeller: 14" diameter
  - Hand-launchable with 3"-wide grip point below motor
  - Flight endurance: ~109 minutes predicted
  - Climb performance: 950 ft/min at 6,000 ft altitude
- Mechanical Features:
  - Tool-less nose cone attachment (aeroshell design)
  - Payload tray: removable via two thumb screws; designed for lab bench integration
  - Tail boom: pogo pin connectors eliminate manual electrical wiring
  - All internal scaffolding: 2D parts for rapid manufacturing scaling
- FAA Registration: N869BS and N598SW (two aircraft for California deployment)
- Material: Composite nose cone and fuselage (7781 E-glass + Loctite EF 9899 Aero foam, 0.01" thickness) from Ability Composites (local radome specialist)

### **LDCR (Lobe Differential Correlation Radiometer)**
- Instrument Purpose: L-band passive microwave radiometer for soil moisture measurement
- Operating Configuration (SMM): Two MiCo antenna pairs (nadir/zenith) with 90° hybrid modification
- Channels: 2 independent receiving channels with thermoelectric coolers (TECs)
- Temperature Monitoring: 5 thermistors on receiving board (TEC ch1, TEC ch2, isolator, local oscillator, IF filter) + 2 additional planned for antenna arrays
- Calibration Modes: 4 selectable via switches (reference-reference, reference-nadir, zenith-reference, zenith-nadir)
- TEC Behavior Characterized: Voltage-temperature relationship mapped; diodes added to protect against reverse polarity during heating mode
- Test Results: Antenna temperatures measured at 53 K (over water), 59 K (saturated grass), 170 K (dry grass)

### **High-Rate Data Logger**
- Purpose: Simultaneous capture of LDCR samples, thermistor data, autopilot telemetry with microsecond-precision timestamping
- Hardware Components:
  - **ADC Board:** 14-bit, 60 MSPS dual-channel simultaneous-sampling ADC (high-speed sampling of LDCR analog signal)
  - **Microcontroller:** STM32F405XX with dual CAN bus, 6 UART interfaces; interleaves Analog/RF board data (1 kHz) and correlator redundancy
  - **FPGA:** USB 3.0 device controller; 40+ I/O pins; implements UART-to-storage interface and FFT processing
  - **Processor:** Pico ITX board with two USB 3.0 host controllers
  - **Storage:** 1 TB SSD with 320+ MB/s throughput, USB 3.0 interface
- Data Rate Achieved: 247 MB/s logged to SSD (measured via UDK3 Performance Monitor)
- Synchronization: 100 μs timestamp precision via 80 MHz ADC reference clock (26-bit timestamp register for 1-hour flights)
- Data Format: Three parallel streams logged with 2-bit prefixes (ADC: "10", UART: "01", Timestamp: "11")
- Processing Priority: UART data (1 kHz) > Timestamp (every 100 μs) > ADC (continuous 80 MHz)

### **FFT Processing for Digital Correlator**
- Implementation: Xilinx LogiCORE IP FFT (Cooley-Tukey algorithm)
- Specifications:
  - 65,536-point (2^16) FFT per channel
  - 14-bit fixed-point precision
  - Dual-channel radix-2 burst I/O
  - Latency: 6,556.38 μs (processes ~1 ms of data)
  - Hardware: 24 DSP slices, 860 9k BRAMs
- Method: Computes cross-spectral density (CSD) of two antenna channels for soil moisture correlation (differs from NASA SMAP filter-bank approach but validated with SMAP hardware designer Jeff Piepmeier)
- Verification: 8-bit 8-point FFT simulation validated against Octave results

### **Antenna Systems**
- **MiCo (Microstrip Collinear) Antennas:** Paired arrays with ¼ wavelength vertical separation; combined with 90° hybrid to produce nadir/zenith beams equivalent to patch antenna configuration; radiation efficiency ~95.6% (simulated)
- **Foam Block Assembly:** Dedicated payload tray section isolates antenna electronics from other RF/electronic sources

## Use Cases & Applications

**Primary Mission:** Soil moisture mapping via passive microwave radiometry
- Brightness temperature measurement over vegetation and soil
- Water content estimation from dielectric property variations
- Multi-temporal mapping capability via repeated small-UAS flights

**Specific Deployments:**
1. **Canton, Oklahoma (Q4/Q5 2015):** Tempest sUAS to conduct pilot soil moisture measurement flights under FAA COA
2. **California (Q5+):** SuperSwift sUAS deployment with expanded mapping capability; two aircraft enable broader area coverage

**Test Scenarios Completed:**
- Ground truth measurements over water (53 K antenna temperature)
- Saturated green grass (59 K; post-snow melt condition)
- Dry green grass (170 K; representative vegetation)

## Key Results

### Flight Certification
- **Tempest:** FAA COA 2014-CSA-200 issued for Canton, OK site operations
- **SuperSwift:** Section 333 exemption filed; automatic nationwide COA eligibility under conditions (flights <200 ft, aircraft <55 lbs, daytime VFR, visual line-of-sight, Sport Pilot minimum, distance restrictions from airports/heliports)

### SuperSwift Design Validation
- Scaffolding prototypes (laser-cut ⅛" spruce) successfully assembled and confirmed 3D CAD viability
- Removable payload tray design verified to accommodate LDCR, data logger, analog correlator, power with minimal integration effort
- Tail boom assembly with pogo pin connectors tested for long-term viability (ongoing in Q5)
- Composite nose cone prototype (5" diameter) manufactured by Ability Composites; RF interference test completed with no L-band disruption detected

### High-Rate Data Logger Integration
- Achieved 247 MB/s sustained data logging to SSD (exceeds 320 MB/s throughput capability of SSD, indicating no bottleneck)
- FPGA UART interface successfully looped-back test data to verify bidirectional communication
- ADC tested with constant DC voltage inputs (0.6 V, 0.8 V, 1.0 V) and verified digital output accuracy
- Trace length matched and cross-talk minimization applied to ADC Digital board layout

### LDCR Performance
- Ground test unit gain characterized at 0.45 mV/K
- Temperature sensitivity (ΔTRMS) established for quantitative radiometer performance modeling
- Thermoelectric cooler characterization complete; heating requires ~0.6–0.7 V lower supply than cooling to same ΔT
- 5 thermistors successfully installed on receiving board; 2 additional thermistors for antenna arrays pending installation

### Tempest Flight Integration Issues Identified (Under Investigation)
1. **RFI:** Short segments of non-Gaussian noise detected in LDCR output; hypothesis: 900 MHz telemetry radio interference
2. **Sensitivity Loss:** Observed sensitivity ~50% of patch antenna baseline; expected only 20–30% reduction; cause under investigation
3. **Assessment:** Neither issue expected to prevent Canton, OK flight testing or compromise soil moisture measurement validity

## Notable Details

### Design Philosophy & Manufacturability
- **Tool-less Assembly Goal:** All major components (nose cone, payload tray, tail boom, wings) attachable/removable without specialized tools or procedures
- **Scalability:** 2D scaffolding and composite shells sourced from local providers capable of delivering 10s per month; laser-cut custom parts available for <$100
- **Future Ecosystem:** Planned publication of payload tray outer dimensions and weight/CG limits with CAD templates to enable third-party payload development

### FAA Regulatory Strategy
- Proactive filing of Section 333 exemption prior to Q4 completion, enabling immediate nationwide commercial UAS operations post-approval
- Automatic COA under Section 333 conditions eliminates per-flight COA requests for subsequent California deployment
- Sport Pilot certificate requirement (lower barrier than commercial pilot) acceptable for operations

### Competitive Advantage
- Custom FPGA-based data logger combines high-speed ADC sampling, real-time FFT computation, and USB 3.0 logging in single integrated system
- Payload modularity (removable tray, standardized CG envelope) enables rapid reconfiguration for future payloads beyond soil moisture (NDVI, methane, other radiometric sensors)
- Consultation with NASA SMAP hardware architect (Jeff Piepmeier) validates FFT-based correlator approach despite deviation from SMAP filter-bank topology

### Vendor Partnerships