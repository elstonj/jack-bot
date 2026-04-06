# 15-04-23 Interim Report: High-Rate Data Logger for Soil Moisture Measurement System

## Document Metadata
- Type: SBIR Interim Report
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR (Soil Moisture topic)
- Date: April 2015 (submitted/created April 14, 2015; last modified November 9, 2015)
- BST Products/Systems Referenced: SwiftPilot Pro, LDCR (L-band Downconversion Receiver)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This interim report documents the design and development of a high-rate data logger system for BST's soil moisture measurement instrument. The logger collects simultaneous data from dual L-band microwave antennas, multiple thermistors, and autopilot telemetry at high sampling rates to enable RFI (radio frequency interference) mitigation algorithm testing and validation. The system achieved 247 MB/s logging throughput to solid-state storage.

## Technical Approach

### System Architecture
The high-rate data logger integrates four main subsystems:
1. **Analog/RF Board**: Conditions LDCR signals (amplification, single-ended to differential conversion via balun circuit); interfaces 10 thermistors; includes analog correlator for redundancy checking
2. **ADC Digital Board**: Dual-channel 14-bit, 60 MSPS simultaneous-sampling ADC (LTC2143); STM32F405 microcontroller; FPGA with USB 3.0 device controller
3. **Storage System**: Pico ITX board with two USB 3.0 host controllers; 1TB SSD with 320+ MB/s throughput
4. **Data Integration**: FPGA-based timestamp synchronization and data multiplexing

### Data Collection & Synchronization
- **LDCR dual-channel data**: 60 MSPS sampling from ADC, continuously logged
- **Thermistor data**: 10 channels sampled via Analog/RF board microcontroller at 1 kHz
- **Autopilot telemetry**: SwiftPilot Pro auxiliary data (including NDVI) at 50 Hz via CAN bus
- **Timestamp precision**: 100 microsecond resolution relative to 80 MHz ADC clock reference
- **Data identification**: 2-bit prefixes identify data type (ADC="10", UART/thermistor="01", timestamp="11")

### Key Design Decisions
- **Priority queuing**: UART telemetry (1 kHz) > timestamp updates (100 µs) > ADC data (continuous)
- **Trace routing optimization**: Equal-length analog traces from SMA connectors to ADC inputs to minimize signal delay; vias added for ground plane connection
- **FPGA FFT processing**: 65,536-point Radix-2 FFT IP core (14-bit fixed-point precision) for computing cross-spectral density (CSD) of dual channels; output logged alongside primary data for post-processing verification

## Products & Capabilities Described

### SwiftPilot Pro
- Autopilot system providing auxiliary telemetry data
- Supplies digital telemetry and NDVI (Normalized Difference Vegetation Index) measurements at 50 Hz
- Data transmitted via CAN bus interface to ADC digital board

### LDCR (L-band Downconversion Receiver)
- Dual L-band microwave antennas with attached thermistors (2) and internal thermistors (6)
- Produces single-ended analog signals conditioned by Analog/RF board
- Designed for soil moisture measurement via microwave remote sensing
- Requires high-rate sampling for RFI mitigation algorithm development

### High-Rate Data Logger System
- **Sampling capacity**: 247 MB/s sustained throughput (verified via Cesys UDK3 Performance Monitor)
- **Logging duration**: 1+ hour per flight
- **ADC specs**: LTC2143 dual-channel, 14-bit, 60 MSPS, simultaneous sampling
- **Microcontroller**: STM32F405 with 6 UART/USART interfaces (up to 10.5 Mbit/s capability)
- **FPGA**: USB 3.0 device controller; >40 I/O pins; supports UART-to-FPGA interface and FFT processing
- **Timestamp register**: 26-bit (sufficient for 36 million increments across 1-hour mission)

## Use Cases & Applications

### Primary Application
Soil moisture mapping via airborne L-band microwave remote sensing, with emphasis on:
- RFI mitigation algorithm development and testing
- Dual-channel correlation analysis for measurement validation
- High-fidelity data collection for algorithm refinement

### Phase III Potential
- NASA applications: Soil moisture monitoring for hydrological studies
- Commercial applications: Agricultural remote sensing, water resource management, climate/weather modeling support

## Key Results

### Validation & Testing Completed

1. **STM32F405 UART Programming**: Successfully configured UART4 to receive 1 kHz telemetry from Analog/RF board microcontroller; combined with CAN messages and transmitted via USART1 to FPGA

2. **FPGA UART Interface**: Implemented library-based UART protocol with state machine; loopback verification confirmed full functionality

3. **Synchronized Data Logging**: ADC data, UART telemetry, and 100 µs-precision timestamps successfully logged to single binary file with priority-based FIFO arbitration

4. **ADC Validation**: 
   - SPI-based test patterns (all 1s, all 0s, alternating) verified correct configuration
   - DC voltage input testing at 0.6V, 0.8V, 1.0V confirmed analog signal processing

5. **High-Speed Data Logging**: Achieved **247 MB/s** sustained throughput over USB 3.0 with 8 kB transfer blocks (verified using Cesys UDK3 Performance Monitor tool)

6. **PCB Layout Optimization**: Improved signal integrity through equal-length analog traces, cross-talk reduction, and enhanced ground plane connections

7. **FFT Implementation**:
   - 65,536-point dual-channel FFT IP core (14-bit fixed-point, Radix-2 Cooley-Tukey algorithm)
   - Latency: 6556.380 µs per 1 ms data block
   - Resource utilization: 24 DSP slices, 860 × 9k BRAMs
   - Verified against MATLAB Octave reference implementations
   - Output logged alongside raw ADC data for CSD (cross-spectral density) computation and post-processing verification

## Notable Details

- **Dual-channel correlator redundancy**: Both digital and analog correlators implemented; digital output compared against analog for validation
- **Real-time Linux customization**: Pico ITX board kernel drivers modified for USB 3.0 bandwidth optimization; fast boot initialization
- **Complex data synchronization**: Handled asynchronous data streams (60 MSPS ADC, 1 kHz thermistor, 50 Hz telemetry) with unified 100 µs timestamp reference
- **Adaptive logging priority**: Design intelligently prioritizes limited USB/storage bandwidth by queuing UART (low-rate, critical telemetry) before FFT outputs before raw ADC data
- **Modular FPGA architecture**: Wishbone interface between modules enables scalable addition of DSP functions (FFT included)