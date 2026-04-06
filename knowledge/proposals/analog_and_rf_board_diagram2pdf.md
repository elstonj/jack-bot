# Analog and RF Board Diagram

## Document Metadata
- Type: Technical schematic/diagram
- Program/Solicitation: NASA SBIR Phase II - Soil Moisture
- Date: Created/Modified October 25, 2014
- BST Products/Systems Referenced: Not explicitly named (component-level design document)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This is a technical schematic diagram showing the analog and RF board architecture for a soil moisture measurement instrument developed under a NASA SBIR Phase II contract. The document displays the interconnection between RF frontend, ADC components, microcontroller, and timing/control systems.

## Technical Approach
The board architecture includes:
- **RF Frontend**: SMA/F connectors with 5-10cm traces, 50-ohm impedance matching
- **ADC Chain**: Dual ADC configuration:
  - High-speed ADC (LTC2143-14) operating at 80 MS/s
  - Secondary ADC with 32 kS/s sampling rate (16-bit)
- **Signal Path**: 16-bit digital data bus from ADC to microcontroller
- **Timing/Control**: Dedicated timing and control subsystem (marked TBD) synchronized to 50Hz clock
- **Power Management**: 3.3V supply with separate power control subsystem (TBD)
- **Navigation Interface**: CAN BUS connection to navigation microcontroller
- **Sampling Rate**: Primary system operates at 1 kS/s with 50Hz synchronization

## Products & Capabilities Described
This appears to be an internal component diagram rather than a product-level specification. No named BST products are explicitly referenced.

## Use Cases & Applications
- Soil moisture measurement (identified in program title)
- NASA remote sensing application

## Notable Details
- Document is a quarter 2 deliverable from Phase II of a NASA SBIR contract
- Indicates multi-stage ADC architecture suggesting need for both high-speed RF sampling and lower-rate precision measurements
- CAN BUS integration suggests integration with larger system or vehicle platform
- Multiple TBD elements indicate this may be a preliminary or in-progress design document