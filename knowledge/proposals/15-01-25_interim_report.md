# High-Rate Data Logger Interim Report

## Document Metadata
- **Type**: Interim Report (SBIR Phase II)
- **Client/Agency**: NASA
- **Program/Solicitation**: 2012 SBIR - Soil Moisture
- **Date**: January 25, 2015 (report period ending)
- **BST Products/Systems Referenced**: SwiftPilot Pro, LDCR (L-band radiometer), SuperSwift (platform)
- **Key Personnel**: Not named in document

## Executive Summary
This interim report documents the design and development of a high-rate data logger for collecting microwave radiometer data and ancillary sensor measurements from the LDCR (L-band radiometer) instrument. The system was redesigned mid-project to reduce data rate requirements from 720 MB/s to 210 MB/s, simplifying the architecture from a 36-card microSD array to a single USB 3.0 SSD. The logger successfully integrated custom Analog/RF conditioning board, ADC digital board with FPGA, and Pico-ITX host computer.

## Technical Approach

### System Architecture
The high-rate data logger employs a modular three-board design:

1. **Analog/RF Board**: Conditions signals from LDCR antenna and thermistors
   - Adds gain and performs balun circuit conversion (single-ended to differential)
   - Performs analog correlation at 32 kS/s (averaged to 1 kS/s)
   - Interfaces with 10 thermistors (5 on LDCR, 2 on antenna, reference)
   - Receives 50 Hz digital nav data from SwiftPilot Pro via UART at 1 kHz

2. **ADC Digital Board**: Data acquisition and telemetry aggregation
   - LTC2143-14 dual-channel ADC: 14-bit, 60 MSPS simultaneous sampling
   - STM32F405 ARM Cortex-M4 microcontroller (168 MHz, 4 USARTs, 2 CAN interfaces)
   - Receives analog signal from Analog/RF board through 50Ω-terminated SMA connectors
   - Aggregates autopilot state, NDVI data, power board status, and correlator/thermistor data

3. **FPGA/USB Interface**: Data streaming and storage
   - Spartan-6 FPGA (XC6SLX45-3FGG484I) on EFM-02 board
   - Cypress FX3 USB 3.0 controller (CYUSB3014)
   - Outputs data at 210 MB/s to USB 3.0

4. **Host/Storage**: VIA EPIA-P910-10Q Pico-ITX board with USB 3.0 SSD
   - USB 3.0 portable SSD (SSD2GO Pocket): write speed 394 MB/s, 1 TB capacity
   - Simple Linux write operations to disk

### Key Technical Details

**ADC Sampling**:
- Clock: 80 MHz from SI510 differential LVDS oscillator (18ps peak-peak jitter)
- ADC configured via SPI for full-rate CMOS output, binary data format
- 30 IO pins receive 14-bit data from both channels + 2 overflow flags
- Data appended with 2 zeros to form 32-bit frames written to FIFO at 80 MHz

**Data Aggregation**:
- Microcontroller interleaves data at different rates:
  - Correlator data: 1 kHz
  - Thermistor data: 50 Hz
  - Autopilot/NDVI data: 50 Hz
  - Power data: <1 Hz
- All data timestamped with 100 µs precision based on ADC reference clock

**FPGA Programming**:
- Implemented in VHDL using Xilinx ISE Design Suite 14.7
- Two state machines manage USB data transfers:
  - SM_GPIF_to_Fifo: Moves data between FX-3 and FPGA FIFOs
  - SM_Fifo_to_Wishbone: Translates streamed USB data to address-oriented Wishbone bus cycles
- Fixed 8 KB block size for data transfers to balance throughput and latency
- Asynchronous FIFOs allow independent GPIF PCLK and syscon.clk frequencies

**USB 3.0 Interface**:
- Cypress FX3 configured with dual sockets (Socket 0/Thread 0 for H2P, Socket 2/Thread 2 for P2H)
- Watermark thresholds set at 8 KB to manage FIFO status
- Data transfers streamed with UDK3 protocol headers for post-transfer address resolution

### Physical Design
- ADC Digital Board: 100 mm × 72 mm, 1 mm thickness
- Board stacked with EFM-02 FPGA module and Pico-ITX host via Q-Strip connectors
- Power requirement: 5V, 300mA supplied by EFM-02

## Products & Capabilities Described

### LDCR (L-band Radiometer)
- Dual L-band antenna channels generating analog signals
- Equipped with 2 thermistors for temperature compensation
- Subject to radio frequency interference (RFI) requiring mitigation algorithms
- Operates with LDCR Reference Radiometer (LDCR) for correlation validation

### SwiftPilot Pro
- Provides autopilot state (50 Hz, 30 bytes)
- Delivers NDVI down-looking data (50 Hz, 21 bytes)
- Delivers NDVI up-looking data (50 Hz, 21 bytes)
- Includes laser altimeter above-ground elevation data
- Connected via CAN bus interface to ADC digital board

### High-Rate Data Logger System
- **Purpose**: Collect LDCR microwave data and auxiliary measurements for soil moisture retrieval
- **Sample Rate**: 60 MSPS (14-bit) on two channels
- **Storage Rate**: 210 MB/s sustained write
- **Storage Capacity**: 756 GB per 1-hour flight
- **Key Advantage**: Significant reduction from original 720 MB/s, 2.6 TB/hour requirement

## Use Cases & Applications

- **Soil Moisture Remote Sensing**: Primary application for LDCR instrument deployment
- **SuperSwift Platform Operations**: Data logger designed for integration with SuperSwift aircraft
- **RFI Mitigation Testing**: High sampling rate enables digital RFI detection/removal algorithm validation
- **Extended Flight Operations**: 1-hour sortie capability with single SSD storage

## Key Results

### Design Evolution & Simplification
- **Original Design**: 36 microSD cards in parallel array, 720 MB/s write requirement, 2.6 TB/hour
- **Revised Design**: Single USB 3.0 SSD, 210 MB/s write requirement, 756 GB/hour
- **Justification**: Third Nyquist zone sampling reduced data rate by 70%; eliminated 31.7W power draw from multiple microSD cards; simplified parallel write complexity

### Board Development Status
- **ADC Digital Board V1.0**: PCB fabricated with LTC2143 ADC and STM32F405 microcontroller
- **FPGA Design**: VHDL implementation complete, downloadable via USB 3.0
- **Validation**: Data logging from dummy ADC counter verified via binary viewer software
- **SSD Performance**: Write speeds tested to 394 MB/s, exceeding 210 MB/s requirement (safety margin: 1.88×)

### Interface Performance
- **USB 3.0 Theoretical**: 625 MB/s (sufficient headroom for 210 MB/s data stream)
- **Timestamp Precision**: 100 µs synchronization across all data sources
- **ADC Jitter**: 18 ps peak-to-peak from clock oscillator

## Notable Details

1. **Risk Reduction**: Team explicitly identified high-rate data logging as potential project bottleneck; redesign addressed this by adopting commercial-grade SSD with proven throughput

2. **Flexibility**: Quick SSD swapping between flights eliminates need to read data from multiple microSD cards in field

3. **Protocol Implementation**: UDK3 protocol headers embedded in USB stream enable post-processing separation of heterogeneous data sources (analog, telemetry, correlation)

4. **Thermal Monitoring**: 8 analog thermistor inputs (5 LDCR, 2 antenna, 1 reference) enable temperature-dependent calibration corrections

5. **Redundancy**: Analog correlator data sampled for validation against digital correlator performance

6. **Timing Synchronization**: All data timestamped relative to ADC master clock for precise geo-location of soil moisture measurements

7. **Power Efficiency**: Shift from multiple microSD cards to single SSD significantly reduces payload power budget, enabling longer flight durations or larger instrument payload

8. **Standards-Based Components**: LTC2143 ADC, STM32F4 microcontroller, Cypress FX3 controller selected for availability, documented performance, and cost-effectiveness

---

**Document Quality Note**: This is a substantive technical interim report with detailed engineering specifications, board schematics, and design justification. Includes system block diagrams, PCB photos, state machine descriptions, and quantified performance metrics. Represents mid-Phase-II progress on NASA SBIR soil moisture instrument development.