# SwiftCore Flight Management System

## Document Metadata
- Type: Product datasheet/capability brief
- Client/Agency: DARPA (Albatross program, subcontractor to BAE)
- Program/Solicitation: DARPA Albatross (BAE subcontract RFP)
- Date: 2024 (created/modified December 10, 2024)
- BST Products/Systems Referenced: SwiftCore FMS, SwiftPilot, SwiftTab, SwiftStation
- Key Personnel: Daniel Hesselius (quoted, Director of Flight Operations at University of Colorado)

## Executive Summary
SwiftCore is Black Swift Technologies' proprietary end-to-end Flight Management System designed for autonomous UAS operations in remote and austere environments. The system integrates hardware (SwiftPilot autopilot, SwiftTab tablet interface, SwiftStation ground station) with field-proven autonomous flight capabilities and has been deployed by NASA, NOAA, and USGS for scientific research missions in extreme conditions.

## Technical Approach
SwiftCore is designed as a modular, distributed avionics architecture consisting of networked nodes connected through a robust bus. This enables redundancy, field maintenance, automated part lifetime tracking, expandability, and third-party integration. The system differs from Dronecode-based alternatives with proprietary estimation and control schemes that claim superior performance.

## Products & Capabilities Described

### SwiftPilot Control Board
- Size: 6.7cm x 4.0cm x 1.8cm
- Weight: 50 grams
- 9 DOF IMU with 10 Hz GPS and 1kHz altitude update
- Processor: Gumstix Overo (1 GHz Cortex-A8)
- Interfaces: CAN, UART, I2C, SPI, USB, Ethernet
- Capability: Industry-leading sensor-based autonomous control that minimizes operator workload; performs fully autonomous flights in harsh conditions; modifies flight path based on sensor inputs

### SwiftTab
- Platform: Android-based tablet
- Interface: Gesture and multi-touch controls
- Function: Mission planning, autopilot control, aircraft and payload function management
- Capability: Intuitive, user-focused interface designed to abstract away clutter while providing useful information; minimal training required

### SwiftStation
- Size: 15cm x 30cm x 35cm
- Weight: 0.9 kg
- Components: 900MHz and GPS antennas, tripod-mounted
- Capability: Links SwiftTab to SwiftPilot autopilot; enables fully autonomous flight from launch to landing; can switch between multiple data links to maintain connectivity
- Customizable: Multiple radio solutions available; expandable via custom modules

## Use Cases & Applications
- Scientific research missions in demanding environments (Greenland, tropical volcanoes)
- Arctic operations (20+ major deployments)
- Hurricane sampling
- Wildfire monitoring
- Tornado observation
- Volcano monitoring
- Agricultural soil moisture measurement
- Trace gas detection (oil & gas industry)

## Notable Details

### Operational Track Record
- Founded: 2011
- 2,500+ legal flight hours
- 150+ FAA-approved UAS flight operations
- 7 NASA flight safety reviews
- 20+ major deployments in extreme environments
- Currently deployed by NASA, NOAA, USGS

### Company Viability
- Profitable revenue growth since 2016
- 2023 Revenue: $1.7 million
- 2024 YTD Revenue: $2.0 million
- 11 SBIR awards (five Phase II efforts)
- $7 million in funding from NASA, NOAA, USGS
- Leadership: CEO/CTO hold PhDs in UAS research with 100+ publications

### Competitive Advantages
- In-house development of avionics, control systems, payload interfaces, payloads, aircraft designs, user interfaces, and ground stations (not Dronecode-dependent)
- Open interfaces supporting multiple protocols while avoiding single-system shortcomings
- Distributed architecture vs. centralized competitors

### Commercialization & Scalability
- Single-unit cost: $8,000
- Partnerships with certified manufacturers/distributors for components
- Only final assembly and QC performed at BST to simplify scaling
- Contacts established with specialized companies for support and maintenance scaling
- Current customers: Federal agencies and commercial partners in agriculture and energy sectors