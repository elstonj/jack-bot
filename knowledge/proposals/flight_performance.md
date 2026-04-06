# Flight Performance Assessment - SMM sUAS

## Document Metadata
- Type: Final Report (excerpt)
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR Phase II - Soil Moisture
- Date: 2015 (deployment); Report finalized ~2017
- BST Products/Systems Referenced: SwiftPilot Pro autopilot, SMM sUAS (Soil Moisture Mapping small Unmanned Aircraft System)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This report section documents flight testing results from a Canton, OK deployment of Black Swift's Soil Moisture Mapping (SMM) sUAS system. Testing assessed the performance of the aircraft, SwiftPilot Pro autopilot, support equipment, and soil moisture sensor. The system demonstrated acceptable altitude tracking (0.78 m standard deviation) and waypoint tracking (0.74 m standard deviation) performance despite operational constraints and wind conditions, though several system improvements were identified for future commercial viability.

## Technical Approach
- **Flight Testing Framework**: Multiple mapping missions conducted on 2015-09-08 and 2015-09-09 with instrumented data collection on altitude, airspeed, and GPS ground speed
- **Altitude Control**: Longitudinal controller assessed against commanded altitude during straight mapping segments; no tuning performed on longitudinal loops
- **Waypoint Tracking**: Lateral controller performance analyzed by calculating minimum (normal) distance from actual flight path to desired waypoint lines; control parameters tuned during early flights to improve performance
- **Constraint**: Laser altimeter disabled due to electromagnetic interference with the LDCR (Low-frequency, Dual-polarization, Calibrated Radiometer) instrument caused by proximity to semi-rigid SMA cables; minimum safe flight altitude increased to 30 m (from planned 15 m) without laser feedback

## Products & Capabilities Described

### SwiftPilot Pro Autopilot
- Autopilot system controlling both longitudinal and lateral aircraft control
- **Longitudinal controller**: Manages altitude tracking
- **Lateral controller**: Manages waypoint/path tracking; parameters tuned in-flight for performance optimization
- Performance adequate for soil moisture mapping operations despite loss of laser altimeter input

### SMM sUAS (Soil Moisture Mapping small UAS)
- Complete unmanned aircraft system for soil moisture mapping
- Integrated payload: LDCR (Low-frequency, Dual-polarization, Calibrated Radiometer) soil moisture sensor
- Concept of operations tested and validated
- Issues identified for transition to reliable, commercially viable platform

## Use Cases & Applications
- **Soil Moisture Mapping**: Primary mission; aircraft designed to acquire soil moisture data over designated mapping areas
- **Operational Deployment**: Canton, OK test site with 5 total mapping missions across two flight days

## Key Results

### Altitude Tracking Performance
| Flight | Average Error | Standard Deviation | Maximum Error |
|--------|----------------|-------------------|----------------|
| 2015-09-08 Flt. 1 Map 1 | 0.16 m | 0.75 m | 3.95 m |
| 2015-09-08 Flt. 2 Map 1 | -0.15 m | 1.14 m | 5.15 m |
| 2015-09-08 Flt. 2 Map 2 | 0.02 m | 0.91 m | 2.50 m |
| 2015-09-09 Flt. 1 Map 1 | -0.36 m | 0.56 m | 1.88 m |
| 2015-09-09 Flt. 1 Map 2 | -0.22 m | 0.54 m | 2.08 m |

**Summary**: Average standard deviation of 0.78 m across all mapping missions; deemed sufficient for soil moisture mapping where distance-to-ground measurement (not altitude hold precision) is critical.

### Waypoint Tracking Performance
| Flight | Average Error | Standard Deviation | Maximum Error | Wind Speed |
|--------|----------------|-------------------|----------------|------------|
| 2015-09-08 Flt. 1 Map 1 | 0.38 m | 1.28 m | 5.59 m | 4.9 m/s |
| 2015-09-08 Flt. 2 Map 1 | 0.46 m | 1.14 m | 4.66 m | 4.8 m/s |
| 2015-09-08 Flt. 2 Map 2 | 0.52 m | 0.78 m | 2.84 m | 4.8 m/s |
| 2015-09-09 Flt. 1 Map 1 | 0.18 m | 0.75 m | 2.86 m | 3.8 m/s |
| 2015-09-09 Flt. 1 Map 2 | 0.12 m | 0.74 m | 2.35 m | 3.8 m/s |

**Summary**: Best standard deviation of 0.74 m achieved in final mission; exceeded accuracy of on-board GPS alone; achieved despite wind speeds constituting 21% of aircraft cruise speed (3.8-4.9 m/s wind in optimal flights).

## Notable Details

### Critical Issues Identified
- **Laser Altimeter Interference**: Electromagnetic interference between laser altimeter and LDCR sensor; proximity of laser to semi-rigid SMA antenna cables was root cause; relocation infeasible due to space and center-of-gravity constraints
- **Operational Workaround**: Laser disabled for Canton deployment; minimum altitude increased to 30 m (from 15 m) to maintain safe operations without laser feedback
- **Future Solution**: Laser altimeter integration required for next system iteration to enable planned 15 m mission altitude

### System Validation
- In-flight tuning of lateral controller proved effective; standard deviation improved across sequential missions
- No longitudinal controller tuning performed; indicates potential for further performance gains
- System demonstrated adequate stability and control authority in 3.8-4.9 m/s wind conditions
- Overall system "worked well enough" to complete required flight tests and data collection

### Commercial Viability Pathway
Document identifies need to address system issues to transition SMM sUAS to "safe, reliable, and commercially viable platform" status.