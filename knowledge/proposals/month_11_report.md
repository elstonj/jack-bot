# Autonomous Quad-Biplane Flight Controller - Month 11 Interim Report

## Document Metadata
- Type: Interim Report (Month 11)
- Client/Agency: Creare (subcontractor); NOAA (end user for aerosol sensor)
- Program/Solicitation: SBIR Project "A Compact and Agile Fixed-Wing UTAS for VTOL Shipboard Operations"
- Contract Number: S649
- Date: 2020-04-20
- BST Products/Systems Referenced: Black Swift Autopilot, Ground Flight Controller System
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing an autonomous flight controller for Creare's Quad-Biplane UTAS platform, a fixed-wing aircraft capable of VTOL operations for shipboard deployment. By Month 11, BST had completed major avionics and power board designs and was conducting initial structural/electrical testing and prototype flight trials, with schedule adjustments made due to COVID-19 delays.

## Technical Approach

### Autopilot Algorithm Development
- Adapting BST's existing autopilot flight control algorithms for the Quad-Biplane application
- Customizing attitude control algorithms developed for multi-rotor platforms for high-stability flight control
- Supporting multiple flight modes: vertical hovering (takeoff), transition to horizontal flight, horizontal flight, and precision landing
- "Outer loop" controller architecture to achieve mission trajectory and altitude objectives while setting control targets for stable flight algorithms
- Leveraging existing BST software to minimize implementation effort

### Precision Landing System
- Integrating Creare's Landing Location Detection software (visual identification of shipboard landing target coordinates)
- Precision landing accuracy target: **0.1 m in no-wind conditions**
- Relative coordinate inputs to autopilot to fine-tune flight path

### Ground Control System
- Integration of Quad-Biplane algorithms into ground flight controller system
- Operator features: mission planning, monitoring, and autonomous mission profile execution

### Hardware Integration
- Identifying and integrating suitable avionics and radios compatible with Black Swift Autopilot, Creare's Quad-Biplane, and NOAA aerosol sensor instrument
- Providing autopilot hardware and ground station hardware to Creare

## Products & Capabilities Described

### Black Swift Autopilot
- **What it is:** Autonomous flight control system with customizable attitude control and mission execution algorithms
- **Use in project:** Core control system for Quad-Biplane; adapted from existing multi-rotor control algorithms
- **Flight modes supported:** Vertical hover, transition, horizontal flight, precision landing

### Ground Flight Controller System
- **What it is:** Ground-based mission planning and monitoring interface
- **Features:** Mission planning, real-time flight monitoring, autonomous mission execution
- **Enhanced in Month 11:** Tablet UI improvements including real-time plotting of all control loops for rapid field tuning

### Avionics Layout
- Design completed; specific board designs documented (see Technical Approach section)

### Power Board
- Design completed for Quad-Biplane electrical power distribution

### GNSS Board
- Design completed for GPS/navigation system

## Use Cases & Applications
- **Primary Mission:** Shipboard-based VTOL operations (launch and landing on moving platforms)
- **Payload:** NOAA aerosol sensor instrument
- **Operational Requirements:** Beyond Visual Line of Sight (BVLOS) capable; operation above 400 feet altitude; precision landing on moving shipboard platforms

## Work Completed (Month 11)

### Testing Activities
1. **Strapped-down structural/electrical test** of the "Double Eagle" platform
   - Validated structural integrity and electrical systems prior to flight testing
   - Issue discovered: ESC (Electronic Speed Controller) error codes after test, possibly caused by excessively fast rotor spinup (corrected for slower startup)
   - ESC monitoring showed normal current, voltage, and temperature profiles during test
   - Error code: "Motor Anomaly" - abnormal motor behavior/lost synchronization

2. **Continued small prototype flight testing**
   - Recent flights conducted in high wind conditions
   - Control tuning observations: aircraft under-responsive in body yaw control; over-responsive to airspeed error in pitch
   - Real-time control loop plotting (new UI feature) enabling rapid field tuning

### Software/UI Improvements
- Enhanced tablet UI with real-time plotting of all control loops for accelerated tuning in field
- Codebase improvements moving system toward production version

### Schedule Updates
- **Reason for revision:** COVID-19 shutdown caused downtime; proposed 1-month extension to original schedule
- **Current status:** BST has permission for two-person flight test teams at BST Sod Farm site; revised schedule expected to hold

## Testing Plan (Remaining)
- Local flight testing at Boulder, CO location (14 CFR Part 107 compliance with altitude waiver requests)
- Flight test campaign at Griffiss UAS Test Site, Rome, NY for BVLOS testing
- Flight test demonstrations required:
  - All flight mode operations
  - Precision landings on moving platform (simulating shipboard operations)
  - Creare providing guidance based on prior experience with drone operations from moving platforms

## Notable Details
- Partnership with Creare as prime contractor; BST in subcontractor role
- NOAA as end-user agency (aerosol sensor payload)
- Griffiss UAS Test Site coordination for BVLOS clearance
- Document classification: Contains company confidential and proprietary information; restricted use