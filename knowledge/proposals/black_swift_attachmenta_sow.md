# Statement of Work for Black Swift Technologies – Creare SBIR Project

## Document Metadata
- **Type:** Statement of Work (SOW)
- **Client/Agency:** Creare (prime contractor); NOAA (end user for aerosol sensor)
- **Program/Solicitation:** SBIR Project – "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- **Date:** January 21, 2019
- **BST Products/Systems Referenced:** Black Swift Autopilot (flight control algorithms), Ground Controller/Ground Station
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
Black Swift Technologies was contracted by Creare to develop and integrate autonomous flight control algorithms for a Quad-Biplane unmanned aircraft system designed for vertical takeoff and landing (VTOL) operations from naval vessels. BST's work encompassed autopilot algorithm customization, precision landing capability integration, ground control station implementation, avionics integration support, and comprehensive flight testing including BVLOS operations.

## Technical Approach

### Autopilot Algorithm Development
- Adapt existing Black Swift autopilot flight control algorithms for Quad-Biplane multi-rotor application
- Customize attitude control algorithms (originally developed for high-stability flight control of multi-rotors) to enable stable flight across multiple flight modes
- Develop "outer loop" controller to achieve mission objectives (flight trajectory, altitude, etc.) in mission execution loop
- Inner loop provides stable flight control commands
- Approach designed to leverage existing software and minimize implementation effort

### Precision Landing Algorithm
- Integrate Creare's Landing Location Detection software (visual identification of shipboard landing target coordinates)
- Fine-tune Quad-Biplane flight path using relative coordinates from detection algorithm
- **Accuracy target:** 0.1 m in no-wind conditions for shipboard landings

### Ground Control Station
- Integrate Quad-Biplane algorithms into ground flight controller system
- Features include: mission planning, flight monitoring, autonomous mission execution

### Avionics & Integration
- Identify and integrate suitable avionics and radios for Quad-Biplane, Black Swift Autopilot, and NOAA aerosol sensor instrument
- Provide autopilot hardware and ground station hardware to Creare for integration

### Flight Testing Strategy
- **Local testing (Boulder, CO):** Compliance with 14 CFR Part 107; request waivers for operation above 400 feet (within line of sight); September-October 2019
- **BVLOS testing (Griffiss UAS Test Site, Rome, NY):** Beyond Visual Line of Sight operations; October 2019 – February 2020
- Demonstrate all flight modes including precision landings on moving platform (simulating shipboard operations)
- Creare to provide guidance based on their experience with drone operations from moving platforms

## Products & Capabilities Described

### Black Swift Autopilot
- **What it is:** Autonomous flight control system with customizable attitude control algorithms
- **Proposed use:** Primary flight control for Quad-Biplane VTOL aircraft
- **Capabilities:** Support for multiple flight modes (vertical hover, transition, horizontal flight, precision landing)

### Ground Controller/Ground Station
- **What it is:** Operator interface and mission management software/hardware system
- **Proposed use:** Mission planning, flight monitoring, autonomous flight execution for Quad-Biplane operations

## Use Cases & Applications
- **Primary mission:** Shipboard VTOL operations (naval vessel deck operations)
- **Instrument payload:** NOAA aerosol sensor
- **Operating environment:** Maritime conditions with moving platform landing requirement
- **Regulatory context:** Beyond Visual Line of Sight (BVLOS) operations with need for waiver coordination

## Schedule & Milestones
- **First-generation flight controller delivery:** August 30, 2019
- **Local flight testing:** September-October 2019
- **BVLOS testing at Griffiss:** October 2019 – February 2020
- **Monthly progress reporting:** Due by 20th of each month

## Deliverables
1. Monthly progress reports (due 20th of each month)
2. Autopilot firmware (flight planning, autonomous flight control, precision landing)
3. Autopilot hardware and firmware
4. Ground controller hardware and software

## Notable Details
- BST responsible for technical progress planning, expense monitoring, and participation in joint project meetings
- Partnership with Creare (prime) leveraging their moving-platform drone experience
- Integration of third-party sensor (NOAA aerosol instrument) requiring coordinated avionics/radio selection
- Regulatory coordination with Griffiss UAS Test Site for BVLOS waiver approval
- Emphasis on precision landing capability (0.1 m accuracy) as critical for shipboard operations
- Project demonstrates BST's ability to customize autopilot systems for specialized applications beyond standard fixed-wing platforms