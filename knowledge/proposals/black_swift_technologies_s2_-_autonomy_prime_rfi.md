# Black Swift Technologies S2 - Autonomy Prime RFI

## Document Metadata
- **Type:** RFI Response / Capability Briefing (Google Slides presentation)
- **Client/Agency:** Department of Defense (Autonomy Prime program)
- **Program/Solicitation:** Autonomy Prime RFI
- **Date:** October 23, 2023
- **BST Products/Systems Referenced:** S2 (CTOL and VTOL variants), SwiftCore Flight Management System, SwiftTab User Interface, SwiftFlow 3D wind probe
- **Key Personnel:** Jack Elston, Ph.D. (presenter; elstonj@blackswifttech.com)

## Executive Summary
Black Swift Technologies proposes leveraging its S2 sUAS platform—available in both CTOL (TRL-9) and VTOL (TRL-4) configurations—to serve as a modular open architecture UAS testbed for the Autonomy Prime program. BST suggests a Phase III SBIR contract pathway to rapidly develop the S2 VTOL into a low-cost, mission-capable platform meeting Autonomy Prime requirements while avoiding competitive procurement delays.

## Technical Approach

**Two-Path Solution:**
1. **S2 CTOL (TRL-9, in production since 2019):** Mature, FAA-certified, proven platform; $39,900 unit cost plus $18,000 launcher
2. **S2 VTOL (TRL-4, planned Q2 2023 production):** Under development; target cost <$50,000; includes machine vision-based automated landing and persistent monitoring capabilities

**SwiftCore Flight Management System:**
- Proprietary, distributed avionics architecture using networked nodes on a robust CAN bus
- Not Dronecode-based; estimated to outperform open-source autopilot solutions in certain control and estimation schemes
- Enables redundancy, field maintenance, part lifetime tracking, expandability, and third-party component integration
- Supports GPS-denied navigation, ADSB integration, and advanced fault detection

**Open Architecture Design:**
- Modular, field-swappable payload nose cone (8 in. diameter × 25 in. length, 5 lbs capacity)
- 50 W power and open data/control interface
- Open SDK for ground and onboard control
- Compatible with sensor-directed mission control and advanced flight planning algorithms

**Advanced Capabilities:**
- AI/machine vision for semantic segmentation and real-time emergency landing plan generation (NASA-demonstrated)
- Terrain-aware and wind-aware flight planning with energy harvesting
- Machine learning-based predictive maintenance
- On-board vision-based automated landing system (no pre-planned landing sites required)

## Products & Capabilities Described

### S2 UAS Platform

| Specification | CTOL | VTOL |
|---|---|---|
| **Weight** | 20.5 lbs | 28 lbs |
| **Wingspan** | 10 ft | 13 ft |
| **Flight Time** | 2 hours | 1.5 hours (with payload) |
| **Flight Ceiling** | 14,000 ft | 14,000 ft |
| **Max Winds Endured** | 30 mph | 30 mph |
| **TRL** | 9 | 4 |
| **Cost (unit)** | $39,900 | <$50,000 (target) |
| **FAA Certification** | COA Certified | None (in pipeline) |
| **NASA Certification** | AWS certified | In pipeline |
| **Production Status** | In production since 2019 | Planned Q2 2023 |

**Command & Control:**
- Direct link via ISM frequencies to 20 miles
- Iridium satellite option for extended range/backup
- Waterproof Samsung tablet interface

**Payload Sensor Examples:**
- RGB, NDVI, thermal imaging
- L-band soil moisture radiometer
- Multi-spectral camera arrays
- Hyperspectral sensors
- Gas analyzers (CO₂, SO₂, CH₄, H₂S)
- Nephelometer (volcanic particle distribution)
- 3D LiDAR

### SwiftCore Flight Management System
- Distributed avionics architecture with CAN bus
- Proprietary control schemes
- Open protocol support (interoperable with standard systems but with performance advantages)
- Fault detection using electronic centralized aircraft monitor-like system

### SwiftTab User Interface
- Proprietary, intuitive GUI focused on mission data gathering
- Built-in safety fault trees and failure identification
- Stand-alone simulator with fault injection capability for operator training

### Advanced Sensors & Subsystems
- **SwiftFlow 3D Wind Probe:** On-board wind measurement
- **Heated Pitot Tube:** Rain mitigation for air data accuracy
- **Machine Vision Landing System:** Real-time semantic segmentation and autonomous emergency landing plan generation

## Use Cases & Applications

**Demonstrated/Historical Missions:**
- High-altitude, high-latitude atmospheric research in Greenland (−20°C temperatures, 14,000 ft altitude) measuring water vapor
- Airborne trace gas measurements (CO₂, SO₂, CH₄, H₂S) and generation of orthomosaics, thermal, and 3D data products
- Volcano plume monitoring with multi-gas sensors and nephelometer
- Coastline monitoring using thermal and hyperspectral payloads for Landsat-8 OLI and S-NPP VIIRS instrument calibration
- Nighttime in situ wildfire plume measurements and remote wildfire property assessment (CO₂, CO, aerosol, RH, pressure, temperature)
- Soil moisture mapping (up to 600 acres per flight) using L-band radiometer

**Operational Environments:**
- Arctic operations
- Tropical volcanoes
- Wildfire zones
- Hurricane research (mentioned in company background)
- Tornado research (mentioned in company background)

**S2 VTOL Persistent Monitoring Enhancements:**
- Solar panel-equipped wings for 4–6 hour endurance with ground recharging
- Month-long autonomous monitoring campaigns
- Machine vision automated landing ("land anywhere" without pre-planned sites)
- Terrain-aware flight planning for rugged/low-altitude operations
- Wind-aware flight planning with energy harvesting
- Rugged ingress protection (−40°F to 120°F operation)

## Key Results & Track Record

**SBIR/STTR Success:**
- Total of 17 SBIR Phase I awards across USDA, NASA, NOAA, and USAF
- Seven Phase II awards accepted (NASA, NOAA, USAF)
- Multiple awards referenced but exact count stated as "11 SBIR awards, including five Phase II efforts" (slight discrepancy in text)

**Operational Heritage:**
- 2,500+ legal flight hours accumulated
- 150+ FAA-approved flight operations
- 7 NASA flight safety reviews passed
- 20+ major scientific deployments
- 100+ technical publications
- Approval from NOAA and DOE as operator

**Company Financials (as of 2023 RFI):**
- 2020 revenues: $1.7 million
- 2021 revenues (estimated): $2.0 million
- Clean capital table; no prior equity raises
- First equity capital raise planned in 2021 (document date suggests this may have occurred)

**Platform Heritage:**
- S2 CTOL: Reliable platform flown by NASA, NOAA, USGS in extreme environments since 2019 production
- S2 VTOL: Built on proven CTOL heritage

**Certifications & Approvals:**
- **FAA:** S2 CTOL certified under COA; S2 VTOL awaiting certification
- **NASA:** S2 CTOL has NASA Armstrong Airworthiness Statement (AWS); S2 VTOL in pipeline
- **NOAA:** S2 CTOL approved platform; S2 VTOL status not explicitly stated
- **USAF/DOD:** Currently in use; system meets airworthiness and security requirements

## Notable Details

**Competitive Positioning:**
- BST is one of only a few companies worldwide capable of designing modular UAS systems "from the ground up" with vertically integrated avionics, firmware, airframes, and payload interfaces
- SwiftCore avionics is a proprietary alternative to Dronecode-based systems, with claimed performance advantages in control and estimation schemes
- Founders hold PhDs in UAS-related research (founded 2011)

**Acquisition Strategy:**
- **Phase III SBIR Sole Source Option:** RFI response highlights SBA policy allowing government to go sole source to prior SBIR/STTR winners for Phase III efforts derived from previous awards. BST proposes leveraging this pathway to accelerate Autonomy Prime development with reduced competition and faster timeline.

**Manufacturing & Scalability:**
- Final assembly and QC performed at BST; components sourced from certified manufacturers/distributors
- Partnerships with specialized companies for scaling support and maintenance
- Target scaling to 100 units per month

**Go-To-Market Strategy (as of 2023):**
- Increase sales revenue through LiDAR and digital mapping applications (S2, E2 platforms)
- Grow soil moisture management package sales
- Expand DOD sales across S2, E2, and S0 platforms
- Scale production capacity

**Design Philosophy:**
- Systems designed for easy transport (all components fit in hard cases; can be checked baggage on commercial flights)
- Rapid deployment capability (aircraft in air within 15 minutes of arrival at site)
- Remote operations focus, supporting demanding field conditions

**User Endorsement:**
- Quote from Daniel Hesselius, Director of Flight Operations, University of Colorado Boulder: "I have not come across an autopilot that can handle fixed-wing aircraft as well as Black Swift." (quoted twice in presentation, suggesting importance to BST's messaging)

---

**Note on Document Completeness:** The final slide contains incomplete notes ("What is the payload capacity of the VTOL version? Need to say something about frequencies."), indicating this was a working draft or interim version. Payload capacity for VTOL is not explicitly stated; frequencies are mentioned generically as "ISM frequencies" for the 20-mile direct link.