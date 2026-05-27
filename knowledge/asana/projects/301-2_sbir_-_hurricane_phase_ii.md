# SBIR - Hurricane Phase II+

## Overview
- **Client/customer**: University of Miami (NOAA)
- **Dollar value**: $344,000 total funding to BST
- **Timeline**: Project completed and archived as of January 3, 2024
- **Status**: **ARCHIVED** — Project successfully completed with all deliverables finished (100% completion rate)
- **Team members involved**: Jack Elston (Owner), Josh Fromm, Dan Prendergast, Maciej Stachura, Ben Busby, Meredith O'hara Needham, Nate Straus
- **Risk signals**: None — project completed successfully

**Key Contacts:**
- **GPC (Government Point of Contact)**: Dr. Joseph Cione, NOAA/AOML/HRD Miami, FL — joe.cione@noaa.gov, Joseph.J.Cione@OSTP.eop.gov
- **UPC (University Point of Contact)**: Dr. Jun Zhang, University of Miami/CIMAS Miami, FL — Jun.Zhang@rsmas.miami.edu
- **Billing Contact**: Luis Quijada, lcq5@miami.edu
- **Field Operations Contact**: Nick Underwood (NOAA AOC)

---

## Key Deliverables & Milestones
- **Deliver Twelve Field-Ready S0 UAS** — Due: 2024-07-31 | **Completed: 2024-07-29** (2 days early)
- **Delivery of Two MHTP for use on Altius 600** — Due: 2024-04-30 | **Completed: 2024-08-17**
- **Conduct 2x Hurricane Field Study** — Due: 2024-11-30 | **Completed: 2024-08-17**

---

## Task Summary
- **Total tasks**: 425+ completed, 0 open (100% completion rate)
- **Primary assignees**:
  - **Jack Elston**: Led most technical flight operations, flight control algorithm troubleshooting, GCS/HDOB integration, wind estimation fixes, sensor QC, magnetometer calibration, MHTP development and hardware verification, avionics, tablet configuration
  - **Josh Fromm**: Project management, QC/final assembly coordination, weekly status updates, manufacturing coordination, housing installation, sealing, MHTP mechanical assembly, deployment tube and adhesive promoter investigations, GCS configuration (completed final "New GCS" task on 2024-01-31)
  - **Dan Prendergast**: Flight algorithm testing and validation, eyewall following algorithm development (completed 2024-02-27), center fix algorithm (completed 2024-06-05)
  - **Maciej Stachura**: Flight control algorithms, vertical wind bias correction, pitot tube diagnostics, code updates with wind tunnel calibrations and real-time wind estimation, MHTP firmware development and testing
  - **Ben Busby**: Flight operations, preflight checklist procedures, path planning optimization
  - **Meredith O'hara Needham**: Manufacturing (MHTP modules), shipping coordination, sensor management
  - **Nate Straus**: Manufacturing, packing/shipping logistics

- **Notable patterns**: 
  - Heavy focus on field deployment readiness with extensive testing, QC, and shipping coordination (July 2024)
  - Intensive flight operations and troubleshooting phase (August-October 2024) addressing wind estimation, GPS/altitude issues, flight termination logic
  - Strong emphasis on HDOB (Hurricane Data Operations) integration and scientist-facing interfaces
  - Multiple tasks related to RS421 sensor interface robustness and reliability
  - Detailed MHTP board development and validation workflow spanning 2023: sensor procurement, PCB QC, wind tunnel calibrations, magnetometer calibration, dynamic pressure testing, firmware updates, housing installation, sealing, and data integration verification

---

## Recent Activity
**Project Status**: Archived January 3, 2024. All work completed successfully.

**Final Phase Tasks Completed (January 2024)**:
- **New GCS (no VGA connector)** (Josh Fromm, Due: 2024-01-26, Completed: 2024-01-31) — Finalized ground control station configuration without VGA connector requirement
- **Avionics** (Jack Elston, completed 2024-01-30)
- **Deployment Tube** (Josh Fromm, completed 2024-01-17)
- **Tablet** (Jack Elston, completed 2024-07-16) — Minimum Viable configuration

**MHTP & Algorithm Deliverables (2023-2024)**:
- **Eyewall Following Algorithm** (Dan Prendergast, Due: 2024-02-16, Completed: 2024-02-27) — Two primary modules explored: "eyewall" and "inflow" modules, with UAS launched in hurricane eye and directed toward eyewall for evaluation
- **Center Fix Algorithm** (Dan Prendergast, Due: 2024-05-31, Completed: 2024-06-05)
- **Adhesive Promoter Investigation** (Josh Fromm, Due: 2024-02-16, Completed: 2024-02-01) — Minimum Viable task, focused on membrane adhesive solutions

**Earlier Project Milestones (2023)**:
- **March-April 2023**: Sensor ordering, mechanical component procurement, initial QC, code updates with wind tunnel calibrations and real-time wind estimation
- **April-May 2023**: Board testing, S2 test rig installation, dynamic pressure clog testing, sealing, serial number assignment
- **May 2023**: Sent to Area-I for initial integration
- **July-September 2023**: Data retrieval verification, magnetometer calibration completion, firmware orientation updates, completed 2023-09-21

**Final Deployment Phase (Aug-Oct 2024)**:
- **Late July 2024**: Shipped 12 S0 UAS units to NOAA AOC (ahead of schedule)
- **August 2024**: MHTP modules delivered, early hurricane field study operations began
- **September-October 2024**: Intensive troubleshooting of flight termination logic, HDOB date/time synchronization, wind direction estimation, GCS GPS anomalies, and engine enable problems

---

## Notes & Context

**Project Type**: SBIR Phase II Government Research Contract

**Products Delivered**: 
- S0 UAS systems (12 units delivered)
- Custom MHTP (hurricane research payload) for Altius 600 platform
- Scientist-facing web-based GUI for data review
- Eyewall following and center fix algorithm modules for autonomous hurricane reconnaissance
- Tablet-based field operations interface
- Ground Control Station (GCS) without VGA connector requirement

**Technical Focus**: Hurricane data collection and reconnaissance using specialized UAS with:
- Wind measurement capabilities (HDOB integration)
- Vertical wind estimation algorithms
- Autonomous mission planning for tropical cyclone research including eyewall following and center fix
- Real-time data transmission and GCS integration
- RS421 sensor interface for robust data transmission in harsh conditions
- Dynamic pressure measurement with raw sensor data logging for clog mitigation in precipitation

**Key Technical Achievements**:
- Successful HDOB integration with GCS and Area-I computer
- Wind estimation algorithm refinement including real-time capability and vertical wind bias correction
- Eyewall following and center fix algorithm development for autonomous reconnaissance in hurricane eye
- Robust flight termination logic and failsafe procedures
- Multi-system coordination (S0 UAS with P3 aircraft altitude separation protocols)
- Deployment tube and adhesive promoter solutions for payload integration
- MHTP board development with:
  - Magnetometer calibration procedure (over UART)
  - Dynamic pressure testing capability for clog detection
  - Firmware updates with correct sensor orientation defaults
  - Raw sensor data output for post-flight analysis and precipitation performance assessment
  - Data retrieval verification via Area-I computer interface
- RS421 interface robustness (final verification)

**Contractual & Support Framework**: 
- GPC (Dr. Cione) and UPC (Dr. Jun Zhang) serve as Subject Matter Experts for non-contractual technical questions
- Any technical disagreements or contractual changes must be directed to the Contracting Officer (CO)

**Field Deployment**: Successfully conducted hurricane field studies in partnership with NOAA Hurricane Research Division (HR