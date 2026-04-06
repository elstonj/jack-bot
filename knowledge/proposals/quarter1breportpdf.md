# Quarter 1b Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- Type: Phase II Interim Report
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II (Contract Number NNX14CG09C)
- Date: July 2014
- BST Products/Systems Referenced: Tempest UAS, SuperSwift (in development), LDCR (L-band Dicke Radiometer), SwiftPilot Pro autopilot, NDVI/Thermal sensors, CoCo antennas
- Key Personnel: Maciej Stachura (lead contact, stachura@blackswifttech.com), Eryan (antenna/RF work), Jack (NDVI/integration), CET team (data analysis/processing), Al (filters)

## Executive Summary
This interim report documents progress in the second six weeks of Phase II development of an L-band microwave radiometer payload for soil moisture mapping on an unmanned aircraft system. The team completed ground testing of the LDCR instrument, developed and tested compact CoCo antennas as replacements for microstrip patch antennas, integrated sensors with the Tempest UAS avionics, and prepared FAA Certificates of Authorization (COA). A 1-2 month delay in initial flight deployment is anticipated due to FAA flight certification processes, but the schedule has been structured to accommodate this delay.

## Technical Approach

### LDCR Instrument Development
- Conducted extensive RF testing on the L-band Dicke Radiometer (LDCR) microwave receiver unit
- Identified and mitigated excessive noise (6x higher than simulated) traced to the analog correlator board through:
  - LC filter addition to input power voltage
  - IF gain amplifiers placed between LDCR output and analog correlator
  - Low-pass filter at analog correlator output (1.5 ms time constant)
  - Video amplifier (ADA 4528-2, 20 dB gain) between filter and A/D converter
- Output scaling with video amp to accommodate 16-bit A/D converters on data logger
- Analog correlator output voltage proportional to difference between upward and downward brightness temperatures (Tup - Tdown)

### Antenna Development
**Microstrip Patch Antennas (Ground Test):**
- Two oppositely-directed (nadir and zenith) coaxial-fed microstrip patch antennas
- Centered at 1413.5 MHz
- ~99% ohmic efficiency
- Negligible mutual coupling between upward/downward facing elements
- Ground tested over grass and water

**CoCo (Coaxial-Collinear) Antennas (Aircraft Use):**
- More compact and lightweight than microstrip patch antennas
- Two pairs with 5.304 cm vertical separation
- Designed specifically for UAS integration
- Measured ~-20 dB mutual coupling between upper/lower antennas (reducing sensitivity by ~10%)
- Lightweight and inexpensive; fabricated and tested
- Mounted in fuselage with foam protection for precise spacing

### System Integration
- Integrated LDCR payload with Tempest UAS avionics
- SwiftPilot Pro autopilot successfully tags sensor payload data with telemetry packets
- Processing software written to extract LDCR and NDVI measurements from SD card data logger
- Data formatted for radiometer analysis software
- CoCo antennas mounted in fuselage; precision-cut CNC foam mount ordered for SuperSwift variants

## Products & Capabilities Described

### LDCR (L-band Dicke Radiometer)
- Microwave receiver instrument for soil moisture measurement via brightness temperature
- Measured sensitivity: ~0.33 mV/K
- Measured noise: ~9K (6x higher than simulated 1.5K, mitigated through design modifications)
- Brightness temperature difference measurement capability: ~225K (demonstrated over water pond at 1m altitude)
- Ground test unit successfully verified operation of modified LDCR, correlator, data logger, and power board

### Tempest UAS
- Serves as initial test platform for LDCR payload
- Integrates with SwiftPilot Pro autopilot
- NDVI/Thermal sensor boards integrated and functioning

### SuperSwift (in development)
- Next-generation aircraft design being developed for enhanced payload capacity
- Three designs under evaluation:
  - Twin-engine tractor (modeled and simulated in X-Plane)
  - Single-engine pusher
  - Twin-engine canard
- Planned features: removable nose cone for payload, 2 modified LDCR units, high-speed data logger, real-time processing unit
- Target completion: March 31, 2015

### SwiftPilot Pro Autopilot
- Successfully tested with NDVI sensors and data logging board
- Tags sensor payload data with telemetry packets
- Compatible with processing software for data extraction

### NDVI/Thermal Sensors
- Newly designed boards (arrived and integrated)
- 8 units built for: ground test unit, initial Tempest aircraft prototype, and two SuperSwift aircraft
- Successfully integrated with avionics

## Use Cases & Applications

- **Soil Moisture Mapping:** Primary application using L-band microwave radiometry to measure soil moisture via brightness temperature
- **Agricultural/Environmental Monitoring:** Over grass fields and water bodies
- **UAS-Based Remote Sensing:** Compact, lightweight payload suitable for small unmanned aircraft

## Key Results

### Ground Testing Results
- Field tests conducted over grass fields and water (small ponds)
- Measurements taken with instrument right-side up and inverted to compare sky vs. ground/water brightness
- Brightness temperature difference from pond test: ~225K at 1m altitude above surface
- Instrument sensitivity: ~0.33 mV/K
- Measured noise: ~9K (6σ ≈ 30 mV)
- Simulated noise: ~1.5K
- Excess noise factor: 6x (traced to analog correlator, successfully mitigated)
- Results confirm prototype unit adequate for initial flight deployment

### Antenna Performance
**Microstrip Patch Antennas:**
- Simulation vs. measurement: excellent agreement
- Efficiency: ~99%
- Mutual coupling: negligible

**CoCo Antennas:**
- Measured mutual coupling: ~-20 dB
- Sensitivity reduction from coupling: ~10%
- Design ready for aircraft integration
- New Technology Report filed

### Schedule Status
- Overall Phase II approximately on schedule with 1-2 month delay anticipated in flight certification
- Most instrument development (1.4: Instrument Testing) 100% complete
- Sensor/avionics integration (1.5) 93% complete
- CoCo antenna completion (1.6) 88% complete
- Ground system testing (1.7) 72% complete
- Flight certification (1.8) only 20% complete (primary schedule risk)
- Initial deployment (1.10) and post-flight analysis (1.11, 1.12) not yet started

### Schedule Flexibility
Work plan allows up to 2-month deployment delay by advancing parallel SuperSwift development tasks, including:
- Integrated power/correlator board design and testing
- Second and third LDCR builds
- High-speed data logger design and build
- Real-time processing unit
- SuperSwift airframe construction and sensor integration

## Notable Details

### Technical Achievements
- Successfully diagnosed and resolved excessive noise in LDCR correlator through iterative RF testing and design modifications
- Developed compact, lightweight CoCo antenna design specifically optimized for UAS integration
- Achieved near-theoretical performance with 99% efficient microstrip patch antennas
- Integrated multiple sensors (LDCR, NDVI, thermal) with autopilot and data logging

### Project Management
- Detailed work breakdown structure (WBS) with task-level tracking
- Clear identification of schedule risks (flight certification delay)
- Proactive schedule recovery plan leveraging parallel development of SuperSwift system
- Flexible task sequencing to maintain overall project timeline despite certification delays

### Regulatory/Compliance
- FAA Certificate of Authorization (COA) submitted to NASA for FAA submission
- Extensive documentation completed: system descriptions, operational procedures, test plan, checklists, payload integration details, range safety procedures
- NASA flight safety review process underway
- AFSR (Air Force Safety Review) paperwork in progress (50% complete as of report date)

### CoCo Antenna Innovation
- Design targeted for New Technology Report submission
- Represents significant improvement in UAS radiometer antenna technology (compact, lightweight, efficient, inexpensive)
- Mutual coupling characteristics well-understood through simulation and measurement

### SuperSwift Development
- Advanced design work proceeding in parallel with Tempest flight testing
- X-Plane simulation used for airframe evaluation
- Twin-engine tractor design selected for further development; alternative designs (pusher, canard) under evaluation
- Planned capability: 2 LDCR units (vs. 1 in Tempest), high-speed data logger, real-time processing