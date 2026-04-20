# #sbir-volcano

## Overview
This channel is primarily used for coordinating Black Swift Technologies' SBIR (Small Business Innovation Research) projects focused on volcanic monitoring using unmanned aircraft systems. The main projects involve deploying S2 and S3 aircraft with specialized sensor payloads to study volcanic emissions and activity, with NASA oversight and collaboration with USGS scientists.

Key participants include:
- **Jack Elston** (Project lead, technical decisions, circuit design)
- **Joshua Fromm** (Payload development, technical integration, diagnostics)
- **Danny Troke** (Flight operations, equipment)
- **Maciej Smolka** (Regulatory, reporting, flight planning)
- **Dan Prendergast** (Flight planning software, technical development, logistics)
- **Meredith Needham** (Administrative support, travel coordination)
- **Ethan Domagala** (Flight operations support)
- **Nate** (Remote ID/registration support)
- **Alex Lomis** (Team member, availability flexible)

The channel covers activities from 2020 through April 2026, with high activity during deployment periods and report deadlines.

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
- Packing list and travel details partially arranged but not fully executed due to postponement

**Gas Payload Isolation Circuit Design (April 18, 2026)**
- **Opto-isolator Configuration**: Determined that single-side isolated optocoupler (SparkFun OPT3001) insufficient for simultaneous TX/RX isolation; requires dual configuration
- **Solution Selection**: Decided to use ADUM1201 magnetic isolator instead of dual optocoupler boards - simpler approach with better high-speed capability
- **Rationale**: ADUM1201 selected for superior baud rate support; will be positioned near high-power lines with expected robust noise immunity
- **Potential Secondary Application**: Discussed possible future application of magnetic isolators on CAN lines to motor and pivot servo to mitigate noise, though impact may be limited (noise likely capacitively coupled requiring choke near transceiver instead)

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
- **Status**: Deployment deferred from April 19-27, 2026 to later date; S3 aircraft repairs ongoing
- **Significance**: SO2 output 10-50x higher than Makushin
- **Aircraft**: S3 (Registration 20686S30001) selected due to high-altitude requirements (18,000-20,000 ft)
- **Mission Parameters (As of April 13, 2026)**:
  - Launch height: 3,650 m (~12,000 ft)
  - Mapping altitude: 5,500 m (18,000 ft) with 200m clearance over volcano summit
  - Estimated climb time: 13 minutes to altitude
  - Transit time to summit: 5.6 minutes
  - Mapping mission duration: 40 minutes (75% overlap)
  - Total mission duration: ~1 hour under power plus 15 minutes power-off descent
  - Max range: ~10 km, may require directional antenna (yagi) or terrain-based approach
  - Optimizations planned: Climb-orbit radius 500+ meters to preserve battery; possible on-site terrain analysis for LOS verification
- **Partners**: CENAPRED (Mexican institution), AFAC, AV3 for flight approvals
- **Key Issue**: Written permission from Mexican authorities not secured as of April 13, 2026; decision on proceeding deferred to April 15 at 4pm
- **Payload Status** (as of April 18, 2026): 
  - Trace gas payload communication issue identified April 17; root cause determined to be single-side isolated optocoupler requiring dual configuration or replacement
  - Solution: ADUM1201 magnetic isolator ordered/identified for implementation
  - Photogrammetry payload confirmed operational
  - Pitot system configured without drain (taped)

**S10022 Aircraft Testing (April 2026)**
- **Status**: Multiple test flights completed week of April 13-14, 2026
- **Purpose**: Validation flights and data analysis to support confidence in aircraft systems
- **Activities**: 
  - Multiple flights at Sod Farm location
  - High-altitude hover tests at multiple elevation points (Boulder at 5,600 ft, Caribou TH at ~10,000 ft, intermediate point)
  - Analysis of performance parameters for extrapolation to higher altitudes
  - Flight data collection (corrupt SD card issue resolved April 13)
- **Status**: Windy conditions limited flight opportunities; tactical planning adjusted based on weather windows

**S1-22 Aircraft Testing (April 2026)**
- **Status**: Ready for flight operations but wind conditions challenging for testing

**S3 Design Improvement Initiative (April 18, 2026)**
- **Status**: In-progress
- **Focus**: Development of new S3 design generation
- **Priority**: Jack Elston recommending focus shift to new design rather than incremental fixes to current optocoupler setup (April 18)

**NASA CCRPP (Climate Change Response Program)**
- **Status**: Multiple quarterly reports completed through Q8 (final report August 2024)
- **Funding**: Requires 1:1 matching funds from non-NASA projects
- **Components**: Hurricane sampling, soil moisture, wind measurement, UI improvements, terrain mapping

## Action Items & Commitments

**Immediate/In Progress (April 18, 2026)**

**Gas Payload Isolation Circuit Design**
- **Jack Elston**: Verify wiring diagram and finalize ADUM1201 