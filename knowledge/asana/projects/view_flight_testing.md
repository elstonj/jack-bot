# Flight Testing

## Overview
- **Client/customer**: Not apparent from task data
- **Dollar value**: Not specified in available data
- **Timeline**: Active project with validation flights scheduled for April 7-9, 2026
- **Status**: Active - high completion rate (97%) with critical validation phase imminent
- **Team members involved**: Dan Prendergast (validation flights), Nate Straus (primary flight operations), Maciej Stachura (fixes/testing), Jack Elston, Sam Hild, Alex Lomis, Meredith O'hara Needham
- **Risk signals**: 
  - All 4 open tasks assigned exclusively to Dan Prendergast
  - Four consecutive validation/functional flights scheduled over 3 days (April 7-9, 2026)
  - Potential single-point-of-failure risk for critical validation phase

## Key Deliverables & Milestones
- **Validation Flight #1**: April 8, 2026 (Dan Prendergast)
- **Functional Flight Test**: April 8, 2026 (Dan Prendergast) 
- **Validation Flight #2**: April 8, 2026 (Dan Prendergast)
- **Validation Flight #3**: April 9, 2026 (Dan Prendergast)

## Task Summary
- **Total tasks**: 4 open, 135 completed (97% completion rate)
- **Assignee breakdown (open tasks)**:
  - Dan Prendergast: 4 tasks (100% of open work)
- **Assignee breakdown (completed, most active)**:
  - Nate Straus: majority of completed tasks across all phases
  - Dan Prendergast: soil moisture testing, training flights, validation prep
  - Maciej Stachura: fixes and specialized testing
  - Jack Elston, Sam Hild, Alex Lomis: specialized test roles
  - Meredith O'hara Needham: logistics support
  - Unassigned: ~8 completed tasks
- **Notable patterns**: 
  - Systematic testing progression: development flights → QC flights → specialized sensor testing → validation phase
  - Heavy use of aircraft serial numbers (S-series, FW-series, E-series platforms)
  - Standardized testing templates with consistent note patterns
  - Most tasks completed without explicit due dates; validation phase has tight deadlines

## Recent Activity
- **October 21, 2025** (latest): S00001 and S10020 fixes testing (Maciej Stachura), S10019 Lost Comms Fix completed
- **July-August 2025**: VTOL merge fixes validation (S10005/S10011, FW1/FW2 QC flights - Nate Straus)
- **May 2025**: Equipment organization completed (torx tools for field kit), E20006 Soil Moisture RevD Test, S20009 training flights
- **Spring 2025**: Dronetag/RID compliance testing, sensor integration (E20006/E20009 new sensors), soil moisture data collection
- **Winter 2024-2025**: VTOL controller integration (S10020), dronetag firmware compatibility testing, RID compliance
- **Transition point**: Testing evolved from development/QC phase through specialized sensor work to final validation readiness

## Notes & Context

### Aircraft Fleet
- **S-series**: S10005, S10011, S10019, S10020, S00001, S20009, S20018
- **FW-series**: FW0001, FW0002 (fixed-wing platforms with VTOL testing)
- **E-series**: E20006, E20009, E20013 (sensor/specialized platforms, heavy soil moisture focus)

### Testing Categories & Specializations
- **Development & QC flights**: Initial validation of platforms and systems
- **Sensor testing**: Magnetometer calibration, NDVI, thermal, radiometer (soil moisture program)
- **VTOL operations**: Control mixer updates, firmware validation on S10020 and FW-series
- **Communication systems**: 900 MHz testing (S10019), Lost Comms fixes
- **Remote ID (RID) & dronetag compliance**: Multiple platforms tested and validated
- **Environmental testing**: Rain testing (S10019), hover tests
- **Specialized sensors**: Airspeed indicator clog detection (S10005, FW-series), soil moisture meters

### Technical Issues & Resolutions
- **Firmware incompatibility**: AutoPilot 2030 cannot accept dronetag in certain configurations (noted on S10011, FW0002) — firmware updates required
- **VTOL control updates**: Significant rework of control mixer on FW-series (completed June 2025)
- **Lost Comms fixes**: Systematic testing and resolution (S10019, latest October 2025)
- **Magnetometer calibration**: Questions flagged on mag cal updates and trigger address changes

### Soil Moisture Program
- **Active platforms**: E20006, E20009 (with specialized radiometer/thermal/NDVI sensors)
- **Data collection approach**: NDVI, thermal, raw radiometer data collection paired with physical soil measurements and integrity checks
- **Testing progression**: Initial test (Oct 2024) → SMM training (Sept 2024) → multiple revisions (RevD validated May 2025)
- **Equipment requirements**: Soil moisture meter, cone penetrometer

### Operations & Logistics
- **Field kit organization**: Completed May 2025 with full equipment categorization and torx tool integration
- **Support activities**: U-Haul van rental for multi-day operations (November 2024)
- **Process maturity**: Standardized testing templates with systematic notation (removing non-applicable sections after task creation)

### Validation Phase Context
- April 2026 marks transition to formal validation flights
- Single assignee (Dan Prendergast) for all validation work suggests either confidence in readiness or potential bottleneck risk
- Four sequential flight events (3 validation flights + 1 functional test) over 2 days indicates compressed schedule; weather or aircraft issues could cascade
- 97% historical completion rate suggests strong execution, but validation phase represents new complexity tier