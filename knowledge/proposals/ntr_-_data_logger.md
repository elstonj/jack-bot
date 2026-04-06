# NTR - Data Logger

## Document Metadata
- Type: New Technology Report (NTR)
- Client/Agency: NASA Goddard Space Flight Center
- Program/Solicitation: NASA 2012 SBIR Phase I; WBS 939869.03.06.01 (S3.05-8971 Soil Moisture Mapping sUAS)
- Contract Number: NNX13CG33P
- Date: Submitted 2014-06-06
- BST Products/Systems Referenced: sUAS (small Unmanned Aircraft System) platform
- Key Personnel: Jack Elston (Company Tech Rep, PCB Assembly/Firmware), Maciej Stachura (Overall Design), Eric McIntyre (PCB Design, University of Colorado)
- NASA COTR: Geoff Bland

## Executive Summary
Black Swift Technologies developed a high data rate compact data logger capable of sampling at 180 mega-samples per second (MS/s) using a microSD card array, designed to fit within the size, weight, and power constraints of small UAS platforms. This represents a substantial advancement over comparable systems, which typically achieve only 0.2 MS/s at similar scales.

## Technical Approach
- **Architecture**: Array of 36 microSD cards written sequentially by an FPGA
- **FPGA Specifications**: 720 MHz clock speed (4x the desired 180 MS/s rate)
- **ADC**: AD9643-210 with 210 MS/s sampling rate
- **Data Rate**: 810 MB/s with 16-bit ADC channels
- **Development Strategy**: Built and tested a lower-rate single microSD card prototype at ~1 kS/s to verify core concepts before scaling to full-rate array system
- **Data Recovery**: Sequential writes to card array with data recreation in post-processing

## Products & Capabilities Described

### High Data Rate Compact Data Logger
- **What it is**: Miniaturized, lightweight data logging system using microSD card arrays
- **Proposed Use**: Primary application is logging high-rate samples from microwave radiometer systems aboard sUAS
- **Specifications**:
  - Sample rate: 180 MS/s (up to 210 MS/s capability)
  - Data rate: 810 MB/s
  - Resolution: 16-bit ADC channels
  - Storage medium: 36 microSD cards in array
  - Size/weight optimized for sUAS integration

## Use Cases & Applications
- **Primary**: Microwave radiometer data collection on small UAS platforms
- **Secondary/Market**: General sUAS sensor data logging; represents enabler for advanced sensing systems in UAS
- **Market Context**: Positioned for growing civil UAS market (projected $2.4B annual sales by 2020 per AUVSI)

## Development Timeline
- **04/03/2013**: Initial discussion and conceptual design
- **04/15/2013**: Detailed design, data rate analysis, component selection
- **07/01/2013**: Lower-rate prototype design and circuit build initiated
- **11/05/2013**: Lower-rate prototype build completed
- **11/12/2013**: Firmware written and operational testing completed on lower-rate unit

## Notable Details
- **Key Innovation**: Achieves 180 MS/s sampling rate at sUAS-compatible scale—900x improvement over comparable systems (0.2 MS/s typical)
- **Approach Rationale**: Uses low-cost, readily available microSD cards rather than expensive high-speed storage solutions
- **Development Stage**: Prototype (lower-rate single card version complete and tested; full 36-card array at 180 MS/s still requires design completion and testing)
- **Technology Readiness**: Classified as "Substantial Advancement in the Art" with prototype-level development
- **Patent Status**: No patents filed or applied for at time of NTR submission
- **Supporting Documentation**: Circuit drawings and prototype photos attached to final report