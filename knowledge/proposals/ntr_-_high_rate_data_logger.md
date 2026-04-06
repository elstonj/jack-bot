# High Data Rate Compact Data Logger

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Goddard Space Flight Center
- Program/Solicitation: NASA SBIR Phase II (Contract NNX14CG09C); WBS 939869.03.06.02, Program S3.05-8971
- Date: Submitted 2016-04-06/07 (Development completed 03/01/2016)
- BST Products/Systems Referenced: SwiftPilot autopilot, S3 (Soil Moisture Mapping sUAS)
- Key Personnel: Jack Elston (lead innovator, PCB Assembly/OS/Firmware), Maciej Stachura (overall design), Subramanyam Ramya (PCB Design/FPGA firmware)

## Executive Summary
Black Swift developed a compact, lightweight high-rate data logger capable of sampling at 60 megasamples per second (MS/s), designed to fit within small unmanned aircraft systems. The logger was specifically engineered to capture data from a passive L-band microwave radiometer and auxiliary sensors for soil moisture mapping missions, integrating with the SwiftPilot autopilot system to provide geolocation and vehicle state data.

## Technical Approach

**System Architecture:**
- **Analog/RF Board**: Interfaces with instruments and auxiliary sensors; conditions analog signals
- **A/D Board**: Contains LTC2143-14 dual analog-to-digital converter (14-bit, 80 MS/s per channel)
- **FPGA Processing**: Spartan-6 based EFM-02 FPGA module with programmable DSP capability
- **Data Storage**: Pico ITX single-board computer (VIA EPIA-P910-10Q) with onboard solid-state drive (SSD)
- **Integration**: Microcontroller collects auxiliary data from internal thermistors and CAN packets from SwiftPilot autopilot, interleaves data for FPGA logging with timestamps
- **Interface**: USB 3.0 connection between FPGA and ITX board

**Development Timeline:**
- September 2014: Initial conceptual design
- October 2014: Detailed design, data rate analysis, component selection
- October 2014: First prototype PCB design and circuit build
- February 2015: ITX board OS and application design
- April 2015: FPGA-based FFT testing on input signals
- July 2015: Software verification with various hard drive options
- March 2016: Full integrated system test completed

## Products & Capabilities Described

**High Rate Data Logger:**
- **Sampling Rate**: 60 megasamples per second (effectively dual-channel 80 MS/s ADC supporting this rate)
- **Resolution**: 14-bit analog-to-digital conversion
- **Size/Weight**: Compact and lightweight—designed to fit within sUAS payload constraints
- **FPGA Capability**: Spartan-6 FPGA enables real-time DSP algorithms (e.g., FFT) and future signal processing enhancements
- **Storage**: Solid-state drive with timestamped data logging
- **State Integration**: CAN interface to SwiftPilot autopilot for synchronized auxiliary data (vehicle attitude, position, timing)

**SwiftPilot Autopilot Integration:**
- Provides CAN bus data packets containing vehicle state and auxiliary flight data
- Enables precise geolocation and correlation of sensor data with aircraft position/orientation

## Use Cases & Applications

**Primary Application:**
- Soil Moisture Mapping via passive L-band microwave radiometer in small UAS
  - Collects high-rate data from two L-band antennas (requiring RFI mitigation algorithm development)
  - Logs temperature data from 2 antenna thermistors and 6 internal LDCR (likely "L-band Differential Radiometer" or similar) thermistors
  - Enables soil moisture measurement depth of 5–20 cm with 15 m spatial resolution

**NDVI Sensor Support:**
- Document notes development of NDVI (Normalized Difference Vegetation Index) sensor as complementary capability

**Broader Market Potential:**
- Growing UAS civil market ($2.4 billion annual sales projected by 2020, per AUVSI)
- Applicable to any advanced sUAS sensing system requiring high-rate, compact data acquisition
- Follow-on commercialization opportunities beyond radiometry

## Key Features & Competitive Advantages

**Novel Elements:**
- Combination of 60 MS/s sampling rate with small size/weight/power profile not found in alternatives
- FPGA in processing chain enables instantaneous FFT and other signal processing without external compute
- Integrated CAN interface to autopilot for seamless sensor-vehicle data correlation

**State of Development:**
- Prototype design and production model status
- "Used in Current Work" (soil moisture mapping sUAS operations)
- Technology Readiness Level: Substantial Advancement in the Art

## Notable Details

- **RFI Mitigation**: High sampling rate specifically required to implement and test radio frequency interference mitigation algorithms on radiometer data
- **Microcontroller Firmware**: Dedicated microcontroller manages auxiliary sensor polling and CAN arbitration/interleaving before FPGA logging
- **No Patents Listed**: Patent status section left blank; technology disclosed to others January 2015
- **Team Contributions**:
  - Jack Elston: PCB assembly, OS/application development, microcontroller firmware
  - Maciej Stachura: System-level design and integration
  - Subramanyam Ramya: PCB layout, FPGA firmware/RTL design
- **Supporting Documentation**: NTR includes circuit drawing, block diagram, and prototype photographs from final report (referenced but not reproduced in this document)