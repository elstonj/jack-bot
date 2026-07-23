# #sbir-volcano

## Overview
This channel is primarily used for coordinating Black Swift Technologies' SBIR (Small Business Innovation Research) projects focused on volcanic monitoring using unmanned aircraft systems. The main projects involve deploying S2 and S3 aircraft with specialized sensor payloads to study volcanic emissions and activity, with NASA oversight and collaboration with USGS scientists.

Key participants include:
- **Jack Elston** (Project lead, technical decisions, circuit design, documentation, flight logistics)
- **Joshua Fromm** (Payload development, technical integration, diagnostics, aircraft inventory tracking)
- **Danny Troke** (Flight operations, equipment)
- **Maciej Smolka** (Regulatory, reporting, flight planning, translation support)
- **Dan Prendergast** (Flight planning software, technical development, logistics, contracting inquiries, documentation, S3 operator's manual, data collection patterns, site selection analysis)
- **Meredith Needham** (Administrative support, travel coordination)
- **Ethan Domagala** (Flight operations support)
- **Nate** (Remote ID/registration support)
- **Alex Lomis** (Team member, availability flexible)

The channel covers activities from 2020 through July 2026, with high activity during deployment periods and report deadlines.

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

**Export & Regulatory (April 2026)**
- Determined that S3 falls under "Temporary Export Exception" as a "Tool of the Trade" - no export license required for Mexico deployment
- Required documentation identified: Letter of justification, proof of ownership, FAA registration, proof of USGS contract
- Carnet needed to avoid import fees (1-2 day turnaround)
- FAA Remote ID registration obtained: 20686S30001

**Mexico Deployment Personnel & Timeline (April 2026)**
- Decision made to defer Mexico deployment from planned April 19-27 window to later date (decision finalized by April 16, 2026)
- Reason: S3 aircraft requiring repairs; issue to be resolved and testing completed by Friday April 18 required before proceeding
- Deferral allows proper S3 testing and validation rather than proceeding with incomplete aircraft readiness

**Gas Payload Isolation Circuit Design (April 18, 2026)**
- **Opto-isolator Configuration**: Determined that single-side isolated optocoupler (SparkFun OPT3001) insufficient for simultaneous TX/RX isolation; requires dual configuration
- **Solution Selection**: Decided to use ADUM1201 magnetic isolator instead of dual optocoupler boards - simpler approach with better high-speed capability
- **Rationale**: ADUM1201 selected for superior baud rate support; will be positioned near high-power lines with expected robust noise immunity
- **Potential Secondary Application**: Discussed possible future application of magnetic isolators on CAN lines to motor and pivot servo to mitigate noise, though impact may be limited

**Operating Manual Documentation (April 28, 2026)**
- **Decision**: Jack Elston initiated development of operating manual as required for flight permissions
- **Approach**: Overleaf document shared with team members for collaborative editing and refinement
- **Content Generation** (May 19, 2026): Jack Elston confirmed manual contains "AI fill in the gaps" content but assessed as "accurate enough"
- **Compliance Expectation**: Jack Elston indicated that AFAC (Mexican authorities) unlikely to scrutinize manual extensively

**C-130 Integration & S0/S0-AD Procurement (June 13, 2026)**
- **Clarification needed on funding**: Jack Elston questioned whether client is paying for S0-AD aircraft, deployment, or both
- **C-130 Setup Work**: Acknowledged additional work required to configure aircraft for integration with C-130 cargo aircraft and establish handoff procedures
- **S0 Aircraft Spares**: Decision to procure extra S0 aircraft units; inventory tracking confirms procurement on schedule

**S0 Aircraft Inventory Status (June 14, 2026)**
- Confirmed S0 aircraft delivery numbers accurate in Asana project management system
- Projected total inventory of approximately 37 S0 aircraft units on track to be delivered
- No inventory shortage issues identified

**Photogrammetry Payload Conversion for Popocatépetl (July 1, 2026)**
- Joshua Fromm inquiry regarding required modifications to photogrammetry payload originally used in Kentucky deployment for volcano mission application
- Gas payload parts on order with projected arrival and conversion completion before end of July 2026
- Plan includes test flight before full deployment

**Photogrammetry Payload/System Performance Validation (July 2, 2026)**
- Jack Elston confirmed that photogrammetry payload system "worked quite well" - assessment indicates readiness for Popocatépetl deployment

**Takeoff/Landing Location Selection for Popocatépetl (July 16-17, 2026)**
- **Issue**: Three candidate takeoff/landing sites identified, with analysis of southernmost location's proximity to crater
- **Constraints**: Paso de Cortés confirmed as end of public access - may be required as operational base
- **Options**: Jack Elston recalled that the closer location (presumably the southernmost site) was discussed as an option but Paso de Cortés may be necessary operational constraint
- **Status**: Decision finalized - operations will likely proceed from Paso de Cortés as the designated takeoff/landing location
- **Reference tool**: Google Earth project created documenting candidate locations

**Popocatépetl Flight Planning Parameters (July 20, 2026)**
- **Altitude Profile Decision**: Selected level flight at 120m AGL above highest volcano point (5,380m elevation) over terrain-following approach
- **Rationale for Level Flight**: Reduces mission complexity from 85 waypoints/90km (terrain-following) to 34 waypoints/39km (level); maintains communication line-of-sight on far side of crater; avoids excessive climbing/descending in challenging terrain and wind environments at altitude where S3 may struggle to maintain required climb rates
- **Approved Parameters**: 80% overlap in both directions maintained
- **Performance Consideration**: S3 will operate above 100 km/h true airspeed at that altitude

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

**Kentucky Deployment**
- **Status**: Completed; photogrammetry payload successfully validated and confirmed functional
- **Significance**: Photogrammetry payload being adapted for Popocatépetl mission; performance confirmation indicates readiness for conversion

**Popocatépetl Volcano