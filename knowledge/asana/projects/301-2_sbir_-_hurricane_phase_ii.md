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
  - **Jack Elston**: Led most technical flight operations, flight control algorithm troubleshooting, GCS/HDOB integration, wind estimation fixes, sensor QC, magnetometer calibration, MHTP development and hardware verification
  - **Josh Fromm**: Project management, QC/final assembly coordination, weekly status updates, manufacturing coordination, housing installation, sealing, MHTP mechanical assembly
  - **Dan Prendergast**: Flight algorithm testing and validation, eyewall following algorithm development
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

**MHTP Deliverable Timeline (2023)**:
- **March-April 2023**: Sensor ordering, mechanical component procurement, initial QC, code updates with wind tunnel calibrations and real-time wind estimation
- **April-May 2023**: Board testing, S2 test rig installation, dynamic pressure clog testing, sealing, serial number assignment
- **May 2023**: Sent to Area-I for initial integration
- **July-September 2023**: Data retrieval verification, magnetometer calibration completion, firmware orientation updates, completed 2023-09-21

**Final project phase (Aug-Oct 2024)** focused on hurricane field operations and system validation:
- **Late July 2024**: Shipped 12 S0 UAS units to NOAA AOC (ahead of schedule)
- **August 2024**: MHTP modules delivered, early hurricane field study operations began
- **September-October 2024**: Intensive troubleshooting of:
  - Flight termination logic (9/11 flight issue resolved 9/20)
  - HDOB date/time synchronization
  - Wind direction estimation and vertical wind bias correction
  - GCS GPS anomalies and altitude calculation
  - Engine enable problems
- **Project closure**: January 3, 2024 status update marked completion of all work

---

## Notes & Context

**Project Type**: SBIR Phase II Government Research Contract

**Products Developed**: 
- S0 UAS systems (12 units delivered)
- Custom MHTP (hurricane research payload) for Altius 600 platform
- Scientist-facing web-based GUI for data review
- Eyewall following algorithm module for autonomous hurricane reconnaissance

**Technical Focus**: Hurricane data collection and reconnaissance using specialized UAS with:
- Wind measurement capabilities (HDOB integration)
- Vertical wind estimation algorithms
- Autonomous mission planning for tropical cyclone research including eyewall following
- Real-time data transmission and GCS integration
- RS421 sensor interface for robust data transmission in harsh conditions
- Dynamic pressure measurement with raw sensor data logging for clog mitigation in precipitation

**Key Technical Achievements**:
- Successful HDOB integration with GCS and Area-I computer
- Wind estimation algorithm refinement including real-time capability and vertical wind bias correction
- Eyewall following algorithm development for autonomous reconnaissance in hurricane eye
- Robust flight termination logic and failsafe procedures
- Multi-system coordination (S0 UAS with P3 aircraft altitude separation protocols)
- Tablet-based field operations interface
- MHTP board development with:
  - Magnetometer calibration procedure (over UART)
  - Dynamic pressure testing capability for clog detection
  - Firmware updates with correct sensor orientation defaults
  - Raw sensor data output for post-flight analysis and precipitation performance assessment
  - Data retrieval verification via Area-I computer interface
- RS421 interface robustness (final verification task)

**Contractual Notes**: 
- GPC (Dr. Cione) and UPC (Dr. Jun Zhang) serve as Subject Matter Experts for non-contractual technical questions
- Any technical disagreements or contractual changes must be directed to the Contracting Officer (CO)

**Field Deployment**: Successfully conducted hurricane field studies in partnership with NOAA Hurricane Research Division (HRD) and National Hurricane Center (NHC), with units staged at NOAA Atlantic Oceanographic and Meteorological Laboratory (AOML) in Miami.

---

## Related Opportunities & Initiatives (as of May 2026)

**NASA RFI - Hurricane ET (Environmental Tracking)**
- **Recommendation**: NASA contacts and Dr. Joe Cione (NOAA/project GPC) recommended BST investigate this opportunity (Alex Lomis, 4/17/26)
- **RFI Link**: https://sam.gov/workspace/contract/opp/d7e641e7fc4d4dfbbd2f5cd62f17758f/view
- **Status**: Flagged for team evaluation
- **Relevance**: Direct extension of Hurricane Phase II+ technical capabilities

**Navy STTR**
- **Status**: Submitted with invoice (Meredith Needham, 4/17/26)
- **Current Priority**: **HIGH** — Jack Elston confirmed priority over SBIR Magnetometer (5/8/26, reconfirmed 5/11/26): *"the navy sttr has priority, the SBIR is mostly on schedule"*

**SBIR Magnetometer (Navy)**
- **Status**: Kicked off April 21, 2026 (Maciej, 4/21/26)
- **Technical Lead**: Designated team member with support from others (Maciej, 4/22/26)
- **Key Deliverables**: 
  - FWA