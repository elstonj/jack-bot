# Costa Rica After Action Report

## Document Metadata
- Type: Interim After Action Report
- Client/Agency: NASA
- Program/Solicitation: Contract Number 80NSSC25CA052
- Date: 2025-05-19 (submitted); document modified 2025-05-29
- BST Products/Systems Referenced: S2, E2, S0, SwiftTab, SwiftCore, Log Parse website
- Key Personnel: Jack Elston (last editor), Daniel Prendergast (referenced for support site improvements)

## Executive Summary
This interim after action report documents a NASA-funded data collection mission over Costa Rica volcanoes using Black Swift Technologies aircraft. The report focuses on lessons learned and provides detailed recommendations for improving BST's deployment toolkits, operator training materials, support documentation, and log analysis capabilities based on operational experience.

## Technical Approach
The mission involved deploying BST aircraft (S2, E2, and S0 models) for data collection over volcanic sites in Costa Rica. While technical mission details are not extensively documented in this interim report, the recommendations section reveals the operational workflow: pre-flight planning using SwiftTab, flight operations via tablet and handset control systems, real-time monitoring, and post-flight log analysis through the Log Parse website.

## Products & Capabilities Described

### S2 (Primary Aircraft)
- Multi-sensor platform with servo-based control surfaces
- Equipped with quick-release (QR) button systems for wing and tail assembly
- Supports multiple payload configurations (photogrammetry, gas sensors)
- Features SwiftTab control interface
- Specifications: Multiple servo types, 900 MHz antenna communication, tail joiner tube construction
- Identified spare parts needs: servos, servo arms, antennas, tail tubes, control cables, connectors

### E2
- Aircraft with propeller-based propulsion
- Spare prop set identified as critical component

### S0
- Equipped with live video capability for route planning and wind profile assessment pre-launch
- Starlink integration capability noted

### SwiftTab
- Tablet-based flight control and monitoring interface
- Contains pre-takeoff checklist tab
- Displays caution (yellow) and warning (red) threshold values for flight parameters
- Supports multiple operating modes

### Log Parse Website
- Post-flight data analysis and visualization tool
- Current bugs: only displays one flight per day
- Capabilities: flight summary info, graphs/charts, flight trajectory visualization
- Can upload and parse BIN flight log files
- Allows entry of pilot-in-command (PIC) and flight summary metadata
- Downloads available in netCDF format

### Control Systems Architecture
- Primary: Waypoint autopilot mode
- Secondary: Augmented (semi-autonomous) mode
- Tertiary: Full manual control via handset radio
- Ground Control Station datalink
- Handset radio backup datalink

### Flight Control Sensors
- Pitot tube (airspeed)
- GPS (position)
- Magnetometers (heading)
- Laser altimeter (altitude)

## Use Cases & Applications
- **Volcanic crater monitoring and documentation** over Costa Rica
- **Photogrammetry data collection** for 3D mapping of crater features
- **Gas payload sampling** (atmospheric composition analysis near volcanic vents)
- **Scientific data collection** requiring extended endurance and precise positioning

## Key Results (for reports)
Document is explicitly labeled as "Interim Report" with substantive results section not included. The report focuses on operational lessons learned rather than scientific findings.

## Notable Details

### Deployment Toolkit Recommendations
BST recommends creating standardized deployment kits to improve operational readiness and reduce field troubleshooting:

**General Equipment Kit:**
- Multiple USB charging adapters and cables (USB-C, USB-A, proprietary barrel connectors for GCS and handset)
- AC and car power adapters
- Kapton tape, Blenderm tape, adhesives, basic tools (screwdrivers, X-acto knife)
- Soldering iron (USB-C powered) and rosin core solder
- S0 with live video feed for pre-flight planning
- Starlink terminal

**Aircraft-Specific Spares:**
- S2: servo sets, servo arms, 900 MHz antennas, tail joiner tubes, wing/tail QR button repair kits, specialized tool kit with Torx drivers and MHP hex bits, spare cable connectors, crimpers (Anderson and 2mm Clik-mate), wire assortment
- Recommendation to standardize all S2 fasteners to Torx to reduce tool complexity
- E2: spare propeller set

**Payload-Specific Kits:**
- Photogrammetry: SD cards (64 MB+, non-micro), USB cables, lens cleaning wipes
- Gas Payload: calibration tubing/valves, spectrometer stoppers, spare thumb drives

### Operator Training Documentation
Recommends comprehensive Pilot's Operating Handbook including:
- **Checklists**: Admin/Logistics, Preflight Inspection, Pre-startup, Pre-takeoff
- **Emergency Procedures**: Contingency procedures and caution/warning threshold reference tables
- **Systems Descriptions**: Control systems (tablet vs. handset, operating modes), datalinks (GCS, handset radio), flight control (sensors, autopilot, CAN bus, servos), propulsion/electrical, launcher
- **Standard Procedures**: Indexed from support website
- **Performance Charts**: Obstacle avoidance climb/descent profiles, battery usage (recommendation to build from empirical data), endurance and range charts
- **Briefing Templates**: Mission brief (for multi-disciplinary teams) and Flight Ops brief (detailed coordination)

### Support Documentation Gaps
- Log Parse functionality not documented on support site (how to upload files, use analysis features)
- Missing S2-specific documentation page
- Unclear organization of emergency/contingency procedures

### Log Parse Software Bugs
- Critical bug: system only displays one flight per day (example: S20015 aircraft had flights on May 16 and May 19 but only one visible per day)
- Missing data fields: takeoff time, landing time, flight duration in summary info

### Process Improvements Noted
- Documentation should be mirrored to wiki with PDF download capability
- Log Parse UI is intuitive but needs on-site instruction documentation (lower priority, future task)
- Opportunity to collect empirical battery consumption data by payload type
- Recommendation to expand Log Parse functionality documentation as new features are implemented

**Document Status:** This is an interim report with recommendations section completed but substantive operational results and findings section not yet included.