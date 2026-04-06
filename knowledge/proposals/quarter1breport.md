# Quarter 1b Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- Type: Interim Report (Phase II progress report)
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II, Contract Number NNX14CG09C
- Date: July 2014
- BST Products/Systems Referenced: Tempest UAS, SuperSwift, SwiftPilot Pro autopilot, LDCR (L-band Digital Correlator Radiometer)
- Key Personnel: Maciej Stachura (lead), Eryan (antenna/RF work), Jack (avionics/sensors), Al (filters), CET team (software/analysis)

## Executive Summary
Black Swift Technologies reports progress on Phase II development of a soil moisture mapping sUAS system using an L-band radiometer payload. The team has completed ground testing of the LDCR microwave receiver instrument, built and tested coaxial-collinear (CoCo) antennas for aircraft integration, and begun integration onto a Tempest UAS platform. Flight certification delays have pushed the initial field deployment from August to an anticipated October-September timeframe, but the team has restructured the work plan to maintain overall Phase II schedule through March 2015.

## Technical Approach
- **Instrument Development**: Modified LDCR receiver unit with noise reduction through LC filters on power input, IF gain amplifiers between receiver and analog correlator, and low-pass filter (1.5ms time constant) plus video amplifier at correlator output to optimize A/D converter input levels
- **Antenna Design**: Transitioned from initial microstrip patch antennas (99% efficiency, negligible mutual coupling) to lighter, more compact coaxial-collinear (CoCo) antennas with ~-20 dB mutual coupling between vertical pair (reducing sensitivity ~10%)
- **Platform Integration**: Payload integration into Tempest UAS with SwiftPilot Pro autopilot for data tagging and telemetry; custom foam mounting for antenna spacing precision; CNC foam cuts designed for improved fit
- **Data Acquisition**: 1000 sample/sec data logger with SD card storage; post-processing software written to extract both LDCR measurements and NDVI/thermal sensor data formatted for radiometer analysis
- **Flight Certification Path**: FAA COA submitted through NASA; extensive documentation prepared (operational procedures, test plan, checklists, payload integration, range safety) for NASA flight safety review

## Products & Capabilities Described

### LDCR (L-band Digital Correlator Radiometer)
- Custom-built microwave receiver measuring brightness temperature at L-band frequencies
- Ground test unit: measured noise σm = 9K (6x initial simulation of 1.5K, primarily from correlator board)
- Instrument sensitivity: ~0.33 mV/K (verified in field testing)
- Critical modifications: custom power board with filtering, IF gain amplifiers, analog correlator with low-pass filter and video amplifier
- Field test results: successfully distinguished brightness differences between upright and inverted positions; brightness difference of 225K measured over pond
- Performance: adequate for initial flight deployment per team assessment

### Tempest UAS
- Primary test aircraft platform for Phase II
- Equipped with SwiftPilot Pro autopilot capable of sensor payload data tagging
- CoCo antennas mounted in fuselage with custom foam mounts for precise spacing (5.304 cm vertical separation)
- NDVI/Thermal sensor boards integrated and tested successfully

### SwiftPilot Pro Autopilot
- Tested with NDVI sensors and data logging board
- Successfully tags sensor payload data with telemetry packets
- Compatible with post-processing software for extracting and formatting data

### SuperSwift
- Next-generation removable-nose aircraft under development
- Three designs under evaluation: twin-engine tractor, single-engine pusher, twin-engine canard
- Twin-engine tractor design modeled and simulated in X-Plane
- Planned to carry two modified LDCR units on integrated power/correlator board
- Nose cone design with removable payload interface

### NDVI/Thermal Sensor Boards
- New sensor boards received and integrated with avionics
- Eight units built/ordered total for: ground test unit, initial Tempest prototype, and two SuperSwift aircraft
- Successfully tested with SwiftPilot Pro autopilot and data logging

### CoCo (Coaxial-Collinear) Antennas
- Lightweight, inexpensive antenna pair designed for UAS integration
- Simulated and measured performance: ~-20 dB mutual coupling between upper/lower antennas
- Reduces sensitivity by approximately 10% compared to patch antennas
- More compact and lighter than microstrip patch antennas
- Fabricated with connector boards and 5.304 cm vertical separation
- Under consideration for New Technology Report filing

## Use Cases & Applications
- **Soil Moisture Mapping**: Primary application; measurements over agricultural and water surfaces
- **Field Deployment Site**: Canton, Oklahoma (planned for August 2014, delayed to October)
- **Ground Testing**: Measurements over grass fields and water ponds to validate performance

## Key Results (Reports & Findings)

### Instrument Testing Achievements
- LDCR noise traced and mitigated from 54K (6x simulated) to acceptable levels through hardware modifications
- Voltage range expanded via video amplifier to match data logger A/D converter specifications
- Ground test unit verified operation of: modified LDCR with gain/filtering, analog correlator with low-pass filter and video amp, 1000 sample/sec data logger, power board

### Antenna Performance
- **Microstrip Patch Antennas**: 99% ohmic efficiency, negligible mutual coupling between up/down facing antennas, highly predictable
- **CoCo Antennas**: Mutual coupling of ~-20 dB resulting in ~10% sensitivity reduction; lightweight and compact; performance validates design for UAS integration

### Data Processing
- Post-processing software written and tested for field deployment use
- Successfully extracts LDCR measurements and sensor data from SD card logger
- Formats data directly for radiometer analysis software

## Notable Details

### Schedule Management
- Initial Phase II deployment scheduled for August 1-7, 2014 anticipated to slip 1-2 months due to flight certification delays
- Team restructured work plan to maintain overall Phase II completion by March 31, 2015
- Flexible schedule allows parallel development of SuperSwift system (tasks 2.1-2.8) while awaiting flight certification
- Post-deployment analysis tasks (1.11, 1.12) can be repositioned in schedule without impacting Phase II objectives

### Flight Certification Status
- FAA Certificate of Authorization (COA) submitted through NASA (submitted as of report date, July 2014)
- Complete documentation package prepared: system description, operational procedures, test plan, checklists, payload integration details, range safety procedures
- NASA flight safety review process ongoing with expectations of 1-2 month delays

### Technical Innovations
- Custom power management and filtering solutions for noise reduction in LDCR unit
- CoCo antenna design submitted for New Technology Report
- SuperSwift airframe design submitted for New Technology Report

### Team Coordination
- Integration work distributed across multiple subsystems: RF/antennas (Eryan), power/correlator boards (Jack), avionics/software (CET team), aircraft integration (Maciej)
- All major subsystems tested and verified to work together as integrated ground test unit before planned flight deployment