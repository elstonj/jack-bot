# NOAA SBIR 2018-1 Questions and Answers #4

## Document Metadata
- Type: Q&A clarification document
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration)
- Program/Solicitation: SBIR 2018-1 (Small Business Innovation Research)
- Date: November 17, 2017
- BST Products/Systems Referenced: None directly mentioned
- Key Personnel: None named

## Executive Summary
This is a NOAA SBIR 2018-1 Q&A clarification document addressing questions from potential proposers regarding eligibility requirements, export controls, and technical specifications for eight different subtopics (8.1.1, 8.1.3, 8.2.5, 8.2.6, 8.2.9, and 8.2.13). The document provides official guidance on regulatory compliance and detailed technical requirements for various oceanographic and atmospheric sensing applications.

## Key Topics Addressed

### Eligibility & Compliance Questions
- **NGO Eligibility**: Non-Governmental Organizations may not apply unless they meet Section 1.5 requirements; can participate as subcontractors
- **Foreign National Work**: Work must be completed on U.S. soil with E-Verify verification; foreign nationals cannot access export-controlled technology without proper authorization
- **Export Controls**: FAR 52.222-54 and 1330-52.235-70 clauses apply; contractors must establish export compliance procedures covering all employees and non-NOAA facilities

### Subtopic 8.1.1 - Air Balloon/Platform for GPS Payloads
- No restrictions on gas type (helium, hydrogen, etc.) as long as safe and functional
- Tethered balloon platforms acceptable, especially for Phase I
- Recoverable GPS payload is desirable feature
- Requirements for altitude achievability and future expectations discussion

### Subtopic 8.1.3 - Air Sensor Calibrator
- Adaptation of existing technology (e.g., NIST patents) acceptable but requires:
  - Research license from patent holder
  - Assessment against "level of innovation" evaluation criteria
- Does not need to be instrument-specific

### Subtopic 8.2.5 - Mooring Beacon System
- **Primary Function**: Locate moorings for recovery using GPS
- **Surfacing Detection**: Beacon detects when subsurface mooring is accidentally disconnected and surfaces (via conductivity or light sensor)
- **Communication**: Should use existing infrastructure (cell phone or satellite); beacon selects appropriate network based on location
- **Data Scope**: Beacon transmits location only; other mooring instruments maintain their own data archives
- **Power Management**: Surfacing detection function in standby while underwater to preserve battery

### Subtopic 8.2.6 - Visibility Sensors
- Current generation visibility sensors use significant power
- Infer visibility during reduced visibility conditions from nearest sensor (5-10 mile range)
- Link to technical report provided: https://tidesandcurrents.noaa.gov/publications/Technical_Report_NOS_CO-OPS_055.pdf
- Term "nephelometers" not commonly used by CO-OPS

### Subtopic 8.2.9 - Seabed Imaging Vehicle
- **Sea State Capability**: Must operate in 1-2 foot (non-breaking) waves while maintaining course and speed against tidal currents and wind from potentially different directions
- **Survey Objective**: Mapping scour areas in seagrass meadows
- **Operating Depth**: Often ~2 feet in seagrass areas
- **Current Method**: Survey-grade GPS with bathymetry transects across scour areas; measures maximum depth, volume, and boundaries
- **Sensor**: Currently Garmin GPSmap 168 with NMEA depth string
- **Position Accuracy**: Real-Time Kinematic (RTK) GPS not feasible due to offshore distance requirements
- **Example Dataset**: Available upon request

### Subtopic 8.2.13 - Continuous Atmospheric UAS/Vehicle
- **Endurance**: 1-4 hours (minimum acceptable depends partly on cost/unit)
- **Definition of "Continuous"**: Not just minutes duration
- **Disposability**: Yes, vehicle is meant to be expendable/disposable
- **Operating Environment**: Hurricane conditions, 5-100 m/s wind speeds
- **Required Payload**: 
  - Atmospheric pressure
  - Temperature
  - Humidity
  - Wind speed and direction (2 Hz minimum, 10+ Hz desired)
- **Desired Additional Payload**:
  - Laser altimeter
  - Downward-looking IR sensor (ocean surface temperature)
- **Physical Constraints**: Must fit existing launch tube dimensions:
  - GPS dropsonde: 2.75" diameter × 16.063" length
  - GPS drop tube: 3" diameter × 17.625" length
  - AXBT: 4.86" diameter × 36" length
  - AXBT drop tube: 5.25" diameter × 38" length
  - ~0.25" clearance required for P-3 tubes

## Notable Details
- All questions must be routed through the Contracting Officer (CO) to ensure fair competition and uniform information distribution to all potential offerors
- Deadline for questions: December 5, 2017 at 2:00 PM Eastern
- Document reflects typical NOAA oceanographic and atmospheric monitoring needs with emphasis on practical operational constraints
- Strong emphasis on leveraging existing infrastructure and platforms rather than developing new ground systems