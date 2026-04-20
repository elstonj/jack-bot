# Flight Testing

## Overview
- **Client/customer**: Not apparent from task data
- **Dollar value**: Not specified in available data
- **Timeline**: Active project with validation flights scheduled for April 21-23, 2026
- **Status**: Active - critical validation phase underway (4 open tasks, all validation/functional flights)
- **Team members involved**: Dan Prendergast (validation flights - exclusive owner of open work), Nate Straus (flight operations), Maciej Stachura (fixes/testing), Jack Elston, Sam Hild, Alex Lomis, Meredith O'hara Needham
- **Risk signals**: 
  - **Single point of failure**: All 4 open tasks assigned exclusively to Dan Prendergast for validation phase
  - **Compressed schedule**: 4 sequential validation/functional flights over 3 days (April 21-23, 2026) — **dates have shifted 5 days later than previous snapshot**
  - **Minimal buffer**: Back-to-back flights with limited contingency time for weather, aircraft issues, or rework
  - **No completed tasks**: Validation phase tasks remain outstanding as of this snapshot

## Key Deliverables & Milestones
- **Functional Flight Test**: April 21, 2026 (Dan Prendergast)
- **Validation Flight #1**: April 21, 2026 (Dan Prendergast)
- **Validation Flight #2**: April 22, 2026 (Dan Prendergast)
- **Validation Flight #3**: April 23, 2026 (Dan Prendergast)

## Task Summary
- **Total tasks**: 4 open, 135+ completed (97% historical completion rate through prior phases)
- **Assignee breakdown (open tasks)**:
  - Dan Prendergast: 4 tasks (100% of open work)
- **Notable patterns**: 
  - All validation work concentrated on single person
  - Systematic testing progression completed through prior phases (development → QC → sensor testing → validation readiness)
  - Standardized flight test format repeated for all 4 validation events
  - **Updated**: Task due dates have shifted 5 days later (was April 16-17, now April 21-23)

## Recent Activity
- **Current**: 4 validation/functional flight tasks due April 21-23, 2026 (imminent, ~6 months out)
- **Change from last snapshot**: All validation flight due dates postponed by 5 days — suggests either schedule adjustment, weather contingency, or resource availability shift
- **Prior activity** (from existing knowledge):
  - October 21, 2025: S00001 and S10020 fixes testing; S10019 Lost Comms Fix completed
  - July-August 2025: VTOL merge fixes validation
  - May 2025: Field kit organization, sensor testing prep
  - Spring-Winter 2024-2025: Development, QC, and specialized sensor testing phases

## Notes & Context

### Aircraft Fleet
- **S-series**: S10005, S10011, S10019, S10020, S00001, S20009, S20018
- **FW-series**: FW0001, FW0002 (fixed-wing platforms with VTOL testing)
- **E-series**: E20006, E20009, E20013 (sensor/specialized platforms)

### Testing Categories & Specializations
- **Development & QC flights**: Initial validation of platforms and systems
- **Sensor testing**: Magnetometer calibration, NDVI, thermal, radiometer (soil moisture program)
- **VTOL operations**: Control mixer updates, firmware validation
- **Communication systems**: 900 MHz testing, Lost Comms fixes
- **Remote ID (RID) & dronetag compliance**: Multiple platforms tested and validated
- **Environmental testing**: Rain testing, hover tests
- **Specialized sensors**: Airspeed indicator clog detection, soil moisture meters

### Technical Issues & Resolutions
- **Firmware incompatibility**: AutoPilot 2030 dronetag configuration issues (S10011, FW0002) — firmware updates required
- **VTOL control updates**: Significant rework of control mixer on FW-series (completed June 2025)
- **Lost Comms fixes**: Systematic testing and resolution completed (S10019, October 2025)
- **Magnetometer calibration**: Technical questions on updates and trigger address changes

### Soil Moisture Program
- **Active platforms**: E20006, E20009 (radiometer/thermal/NDVI sensors)
- **Data collection**: NDVI, thermal, raw radiometer data paired with physical soil measurements
- **Status**: RevD validated May 2025; ready for validation phase

### Validation Phase Risk Assessment
- **Readiness**: 97% historical task completion through prior phases suggests thorough preparation
- **Concentration risk**: Dan Prendergast is sole executor for all 4 validation events; no backup assignees identified
- **Schedule**: 3-day window (April 21-23) with back-to-back flights leaves minimal margin for weather delays, mechanical issues, or data rework
- **Timeline shift**: 5-day postponement from original April 16-17 dates may indicate resource constraints or intentional buffer addition
- **Recommendation**: Confirm contingency dates, cross-train backup personnel, and establish clear weather abort criteria before April 21