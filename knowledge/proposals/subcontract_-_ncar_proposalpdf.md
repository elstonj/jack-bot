# UAS In Situ EDR to Support Safety Assurance for UAS Operations

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal with NCAR Subcontract Letter of Commitment
- **Client/Agency:** NASA (SBIR Fiscal Year 2021 General Solicitation)
- **Program/Solicitation:** NASA SBIR FY2021; NCAR Proposal #2021-0150
- **Date:** January 5, 2021
- **BST Products/Systems Referenced:** Fixed-wing small UAS (sUAS) platforms; flight data systems with multi-hole probe (MHP) capability
- **Key Personnel (NCAR):** Dr. James Pinto (PI), Dr. Larry Cornman, Dr. Gregory Meymaris
- **Key Personnel (BST):** Dr. Jack Elston (recipient of commitment letter)

## Executive Summary
Black Swift Technologies proposed to collaborate with NCAR to adapt NCAR's in situ Eddy Dissipation Rate (EDR) turbulence detection algorithm for deployment on small fixed-wing UAS platforms. This Phase I effort aims to develop a proof-of-concept real-time turbulence detection and reporting system that will enhance safety and operational efficiency of commercial sUAS operating in the lowest 120 meters of the atmosphere, where turbulence hazards are currently poorly characterized and largely unmeasured.

## Technical Approach

### Core Algorithm Adaptation
- **Algorithm Foundation:** NCAR's in situ EDR software based on the vertical wind measurement technique (Sharman et al. 2014), derived from Kolmogorov's inertial subrange theory (1941)
- **Theoretical Basis:** EDR (energy dissipation rate) describes turbulence state independent of aircraft type; uses structure functions related to velocity differences across spatial displacements
- **Current Implementation:** Algorithm uses three variations—onboard vertical wind calculation, true airspeed (TAS), and inverse algorithms using aircraft response models. NCAR uses the wind-based method; FLYHT's TAMDAR system uses the TAS variant

### NCAR Phase I Tasks
1. Establish onboard sensor requirements, data rates, computational capabilities, and transmission requirements for computing and transmitting EDR from UAS to ground station (or ADS-B out if available)
2. Determine processor speed and storage specifications for EDR add-on capability versus integration into existing flight monitoring systems
3. Compare EDR derived from high-rate flight data against high-rate wind data from multi-hole probe (MHP) to validate accuracy
4. Collaborate with BST to define end-to-end capability requirements, including new software package or circuit board for onboard EDR computation and dissemination
5. Explore requirements and document techniques for extending EDR calculations to multirotor UAS (flights adjacent to instrumented tower; coincident flights with instrumented fixed-wing UAS)
6. Support status briefings and regular reporting

### Required Input Data
- True airspeed (TAS)
- Altitude
- Dynamic pressure
- Linear accelerations
- Angular rates and accelerations
- Angle of attack and angle of sideslip
- High-rate 3D wind field measurements (from multi-hole probe)

## Products & Capabilities Described

### NCAR In Situ EDR Turbulence Detection Algorithm
- **What it is:** A C software library for aircraft systems (avionics, electronic flight bags) that estimates atmospheric turbulence intensity from in-flight measurements; can be integrated onboard or on ground
- **Current deployment:** Transport aircraft, FLYHT's TAMDAR system
- **Proposed adaptation:** Integration onto fixed-wing sUAS platforms
- **Extensibility:** Algorithm is "readily extensible to a range of fixed-wing UAS platforms"; follow-on work could extend to multirotor aircraft and possibly UAM eVTOL vehicles
- **Key advantage:** EDR measurements are independent of aircraft type, enabling direct validation of NWP models and uniform turbulence guidance products

### Quality Control Capabilities
- NCAR has developed onboard and ground-based quality control algorithms that can flag spurious reports and identify vehicles experiencing ongoing problems

### Proposed End-to-End System
- Onboard EDR computation
- Real-time transmission to ground station or cell towers
- Simultaneous reporting of power consumption, altitude, location, temperature, and derived wind speed
- Internet of Things (IoT) capability to broadcast turbulence conditions to nearby UAS

## Use Cases & Applications

### Primary Mission: UAS Traffic Management (UTM) Safety
- Support safe and efficient operation of small commercial UAS
- Provide accurate and complete depiction of current and future weather hazards within operations regions
- Enable real-time in-flight decision making for sUAS operators

### Key UAS Operational Considerations
1. **GEO-fencing:** Will turbulence intensity be severe enough to cause UAS to deviate from geofenced flight corridors?
2. **Operating Range Impact:** Will persistent turbulence significantly degrade operating range due to excessive power consumption needed to maintain altitude and corridor?

### Broader Applications
- **Aviation Safety:** Inform crewed low-altitude flight operations
- **Boundary Layer Research:** Unprecedented spatio-temporal coverage of turbulence intensities in lower atmosphere
- **Model Validation:** Evaluate and improve turbulence guidance products (e.g., NCAR/NOAA's Graphical Turbulence Guidance—GTG); assess realism of boundary layer turbulence predictions in mesoscale and microscale models
- **Operational Meteorology:** Support weather hazard products for aviation planning

### Operational Context
Commercial sUAS primarily operate within lowest 120 meters of atmosphere, where:
- Turbulence is highly variable in space and time
- Characteristics strongly tied to diurnal cycle
- Variability influenced by surface roughness, heat and moisture fluxes, wind shear, static stability
- Current observations are scarce (limited to tall towers with sonic anemometers, Doppler lidars at wind farms, subset of surface mesonet stations)

## Budget & Resource Allocation

**Total NCAR Subcontract:** $37,070 (Firm Fixed Price)
**Period of Performance:** June 1, 2021 – November 30, 2021

### Labor Breakdown
- **Dr. James Pinto (Project Scientist III, PI):** 5% effort (~$2,975) – project oversight, budget/personnel management, data analysis, EDR measurement evaluation
- **Dr. Larry Cornman (Project Scientist III):** 10% effort (~$5,808) – scientific guidance on algorithm implementation, high-rate data analysis tools, quality control development, multirotor UAS implementation planning
- **Dr. Gregory Meymaris (Software Engineer III):** 10% effort (~$5,102) – algorithm adaptation for UAS environment, Interface Control Document (ICD) development, data requirements specification

### Cost Breakdown
- **Salaries and Benefits:** $21,452
- **Indirect Costs (56.6% rate):** $12,142
- **Computing Service Center:** $1,711 ($7.67/hr)
- **UCAR Management Fee (5%):** $1,765

## Notable Details

### NCAR Expertise & Credentials
- **Dr. Pinto:** Science Deputy, Aviation Application Program, NCAR (2017-present); extensive experience in boundary layer and cloud physics, numerical weather prediction, weather hazard products for aviation; led micro-weather prediction system development for 2018 LAPSE-RATE field experiment; co-authored multiple 2020 publications on UAS in operational meteorology
- **Dr. Cornman:** Project Scientist III with 35+ years experience; recognized technical expert in remote and in situ turbulence detection; recipient of Aviation Week Laurels (1998, 1990), NASA "Turning Goals into Reality" award (2003), "Scientific American 50 – Research Leader in Aerospace" (2004)
- **Dr. Meymaris:** Primary software engineer and algorithm developer for NCAR In Situ EDR Algorithm; significant contributor to RTCA DO-370 Guidelines for EDR Algorithm Performance (2018); extensive publication record on turbulence detection

### Algorithm Pedigree
- Original NCAR accelerometer method (Cornman et al. 1995)
- Updated version using vertical winds (Sharman et al. 2014) – current deployment standard
- FLYHT TAMDAR system implementation (Daniels 2002) – operational validation on commercial aircraft
- NCAR has comprehensive C library with quality control and on-board processing capabilities ready for adaptation

### Proposed Phase II Work (Contingent on Phase I Success)
- Install algorithm on multiple fixed-wing UAS; conduct calibration/validation flights adjacent to CAL/VAL tower
- Develop methods for extending EDR to multirotor UAS and possibly UAM eVTOL vehicles
- Develop and implement onboard quality control methods
- Develop turbulence guidance products specifically designed for low-altitude sUAS operations

### Contingency Notes
- UCAR/NCAR participation contingent upon mutually agreed-upon terms and conditions
- Fixed-firm price contract limits scope creep; any tasking alterations require mutual agreement
- Work performed to support sponsor "as resources allow"
- Contract administration handled by Ms. Amy Smith, UCAR Contracts Manager (fedaward@ucar.edu)