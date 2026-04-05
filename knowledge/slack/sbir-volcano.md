# #sbir-volcano

## Overview
This channel is primarily used for coordinating Black Swift Technologies' SBIR (Small Business Innovation Research) projects focused on volcanic monitoring using unmanned aircraft systems. The main projects involve deploying S2 and S3 aircraft with specialized sensor payloads to study volcanic emissions and activity, with NASA oversight and collaboration with USGS scientists.

Key participants include:
- **Jack Elston** (Project lead, technical decisions)
- **Joshua Fromm** (Payload development, technical integration)
- **Danny Troke** (Flight operations, equipment)
- **Maciej Smolka** (Regulatory, reporting)
- **Dan Prendergast** (Flight planning software, technical development)

The channel covers activities from 2020 through early 2024, with high activity during deployment periods and report deadlines.

## Key Decisions

**Mission Parameters & Equipment (2020-2021)**
- Switched from 1 sq km to 1km x 0.5km mapping area to fit S2 mission profile
- Selected S2-9 as primary aircraft (75g lighter than S2-3)
- Approved dual payload approach: photogrammetry payload vs. gas detection payload
- Set payload door operation range 1500-2000 with neutral at closed position
- Determined total payload replacement cost at ~$20,200

**Radio/Communications (2021)**
- Reduced radio transmit power to 23dBm for FCC Part 15 compliance
- Selected 1W transmit power with 14dBi yagi antenna configuration
- Decided on standalone 2.4GHz video system instead of dual data/video feed

**Propulsion System (2022-2023)**
- Selected 15x10E propeller over 14x12E based on 26-29% better power efficiency in cruise
- Switched to new battery configuration enabling missions old setup couldn't complete

**Aircraft Selection for High-Altitude Missions (2024)**
- Decided to focus on S3 as primary aircraft for Mexico deployment due to S2 altitude/performance limitations at 19,500-20,000 ft

## Projects & Initiatives

**Makushin Volcano Monitoring (Alaska)**
- **Status**: Multiple successful deployments completed (2021, 2022, 2023)
- **Key Achievement**: First successful detection and measurement of volcanic plume downwind of summit using trace gas sensors
- **Capabilities**: Operations in 30+ knot winds, beyond USGS helicopter limits (20 knots)
- **Location**: Dutch Harbor, Alaska
- **Partners**: USGS, Alaska Volcano Observatory, NASA

**CRATER Mission (Costa Rica)**
- **Status**: Completed May 2024
- **Objective**: NASA crew training and science data collection at Rincon de la Vieja volcano
- **Results**: 6 flights completed, NASA personnel trained, science objectives met
- **Restrictions**: Operations limited to west side of ridge until NASA crew qualified

**Popocatépetl Volcano (Mexico)**
- **Status**: Planning phase for deployment (target February 2025)
- **Significance**: SO2 output 10-50x higher than Makushin
- **Aircraft**: S3 selected due to high-altitude requirements (19,500-20,000 ft)
- **Partners**: CENAPRED (Mexican institution), AFAC, AV3 for flight approvals

**NASA CCRPP (Climate Change Response Program)**
- **Status**: Multiple quarterly reports completed through Q8 (final report August 2024)
- **Funding**: Requires 1:1 matching funds from non-NASA projects
- **Components**: Hurricane sampling, soil moisture, wind measurement, UI improvements, terrain mapping

## Action Items & Commitments

**Ongoing/Recent**
- Dan Prendergast: Follow up on wire payment confirmation for S3 registration (Mexico mission)
- CENAPRED coordination: Request overflight permits from AFAC as government-to-government approach
- Export Classification for S3 still pending as of April 2024
- Equipment manifest finalization for Mexico deployment with carnet documentation

**Historical Major Items (Completed)**
- NASA SBIR quarterly reports (Q1-Q8) - All completed on schedule
- Equipment shipping to Alaska deployments via ACE Air Cargo
- Regulatory approvals: COA updates, TFR approvals, FAA experimental licenses
- Gas sensor calibration with custom gas mixes and USGS coordination

## Client & External References

**Government Partners**
- **NASA**: Mark Sumich (primary contact), Michael Stewart, Matt (Ames), Laura Iraci (trace gas group)
- **USGS**: Christoph (spectrometer calibration, mission planning), Angie (Mexico coordination)
- **Alaska DOT**: Ryan (COA approvals, TFR coordination)
- **CENAPRED**: Mexican government institution for volcano monitoring
- **AFAC**: Mexican aviation authority

**Service Providers**
- **AV3 (Mexico)**: Joe (joe@av3aerovisual.com) - Flight approvals and operations
- **ACE Air Cargo**: Alaska shipping logistics ($220-4500 per shipment)
- **Dutch Harbor Airport**: Dale (airport manager)
- **Robin Campion**: Mexico City contact for equipment delivery

**Academic Collaborators**
- **UCR (University of Costa Rica)**: Andres - required $5000 payment for official participation
- **Alaska Volcano Observatory**: Volcanic activity monitoring and alerts

## Recurring Topics & Themes

**Regulatory Challenges**
- Continuous COA (Certificate of Authorization) updates and approvals
- FCC compliance issues with radio systems and experimental licenses
- Export classification requirements for international deployments
- TFR (Temporary Flight Restriction) coordination for sensitive areas

**Equipment Reliability & Logistics**
- Shipping challenges to remote locations (Alaska, Costa Rica, Mexico)
- Battery shipping restrictions (cannot be checked luggage)
- Equipment calibration timing and gas supply management
- Weather-related operational windows and limitations

**Technical Integration Issues**
- Radio system compliance and power management
- Payload weight optimization and center of gravity calculations
- Sensor calibration procedures and timing
- Communication system reliability at extended ranges

**Report Cycles**
- Quarterly NASA SBIR reports with specific section assignments
- Technical documentation for regulatory compliance
- Mission debrief presentations and lessons learned

## Important Resources

**Mission Planning & Documentation**
- Mission Planner presentation: https://docs.google.com/presentation/d/16_C6tUXqQ8RBh-Q6dcd8R2v-7iZCQ1PHek0etKsyocY/edit
- NASA CCRPP reports in Overleaf (multiple project links)
- Asana project for Alaska deployment: https://app.asana.com/0/1204876610650984/1204876610650984
- Real-time mission tracking: https://airbornescience.nasa.gov/tracker/#map/FA3TNAPYAY

**Technical References**
- FAA CAPS system for COA access
- DigiKey parts and specifications for iridium antenna systems
- Pololu heated pitot switch specifications and power consumption data
- McMaster-Carr parts for pressure gauges and mechanical components

**Media Coverage**
- DroneLife article about volcano monitoring project
- NASA blog post about volcanic laboratory flights at Rincon de la Vieja

## Recent Activity

**Mexico Mission Planning (2024)**
- S3 aircraft preparation for high-altitude Popocatépetl deployment
- Export classification and regulatory approvals in progress
- Equipment shipping coordination with customs documentation
- CENAPRED partnership development for government-to-government permit requests

**Costa Rica Mission Completion (May 2024)**
- Successfully completed CRATER mission with NASA crew training
- 6 flights completed despite challenging weather conditions
- NASA personnel now qualified for independent operations
- Mission documented with media team coverage

**Technical Development**
- Continued development of heated pitot systems for high-altitude operations
- Battery pack optimization for extended range missions
- Mission planning software improvements with validation features
- Gas sensor payload refinements based on field experience

The channel shows consistent activity around deployment periods, report deadlines, and technical development milestones, with strong collaboration between BST team members and external partners.