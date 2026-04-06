# Supplemental Budget and Other Information

## Document Metadata
- **Type**: Budget documentation, vendor quotes, and project planning materials
- **Client/Agency**: NOAA (National Oceanic and Atmospheric Administration)
- **Program/Solicitation**: 2018 SBIR Phase I
- **Date**: January 31, 2018
- **BST Products/Systems Referenced**: S0 (aircraft platform), SwiftPilot (flight control interface), AVAPS (atmospheric measurement system)
- **Key Personnel**: Jack Elston (BST contact, elstonj@blackswifttech.com, 720-638-9656)

## Executive Summary
This document collection contains budget justifications, cost estimates, and vendor information supporting a NOAA SBIR Phase I proposal. It includes task-level labor hour budgets for S0 aircraft development, avionics design, sensor integration, and AVAPS system integration, along with supporting vendor quotes for PCB assembly, components, and services.

## Document Contents & Technical Details

### Project Budget Structure
The main budget document outlines labor allocation across seven major task categories:

**Task Categories & Labor Hours (by person):**
- **Task 1.00 - Preliminary Tasks**: Kickoff meetings, requirements review, risk review, project management
  - Lead roles: Jack (5-20 hrs), Maciej (5 hrs), Josh (5-13 hrs)

- **Task 2.00 - S0 Aircraft Development**: Prototype build/testing, deployment mechanism, composite aircraft design
  - Hours: Build prototype (40-60 hrs), Flight test (5 hrs), Deployment mechanism (10-40 hrs), Composite design (5-40 hrs)

- **Task 3.00 - Avionics and Sensing Electronics**: PCB design, firmware development, production board design
  - PCB design prototype (60 hrs), Firmware for combined board (40 hrs), Production board design (20 hrs)

- **Task 4.00 - Sensor Calibration and Validation**: Bench testing (10-120 hrs), wind tunnel testing (10-40 hrs), flight testing (10 hrs)

- **Task 5.00 - AVAPS Integration**: Hardware procurement/development, SwiftPilot interface to AVAPS, ground testing
  - Hardware: 40-60 hrs, Interface development: 20 hrs, Ground testing: 10 hrs

- **Task 6.00 - Mission Planning**: Mission plan loading on P3 aircraft, mission simulation capability, intelligent sampling specification

- **Task 7.00 - System Specification**: Documentation and final reporting (10-40 hrs)

### iMET Budget Justification
Detailed subcontractor labor for iMET (CU - University of Colorado) at $110/hour:
- Biweekly meetings: 13 hrs = $1,430
- Sensor integration with multi-hole probe: 8 hrs conceptualization = $880
- Calibration methodology development: 40 hrs conceptualization + 40 hrs procedures + 80 hrs test fixtures = $13,200
- Transmit interface design: 16 hrs research + 4 hrs specifications + 40 hrs transmitter design = $2,200
- **Total iMET cost**: $241 hours = $26,510

### Black Swift Technologies 2017 Financial Summary
Snapshot as of January 31, 2018:
- **Total Income**: $753,049.07
  - Billable expenses: $470,585.20
  - Sales of services: $220,064.55
  - Product sales: $86,886.27
- **Cost of Goods Sold**: $185,630.09
- **Gross Profit**: $567,418.98
- **Operating Expenses**: $445,225.59 (59.2% of income)
  - General/Administrative: $266,004.25 (35.3%)
  - Overhead (rent, utilities, insurance): $43,542.25 (5.8%)
  - IRAD Hardware: $33,058.13
  - Payroll: $69,785.96
  - Taxes: $32,835.00
- **Net Income**: $122,193.68

### Vendor Quotes & Component Specifications

**PCB Assembly (Advanced Assembly - Quote Q68219-A, April 18, 2017)**
- Product: AP Pro Core v03 revision board
- Configuration: 4-layer PCB, green mask, HASL finish, RoHS compliant, SMT + THT assembly
- Component count: 95 SMT + 1 THT, 41 signal lines
- Assembly: 5-day turn time, quantity 10
- NRE (setup): $385.00
- **Unit Price**: $4,676.67 per assembly

**3D Printed Components (Shapeways quotes, Jan 31, 2018)**
- Tail piece (S0 aircraft component): 
  - Nylon plastic: $62.80
  - Aluminum: $939.57
- Shell (fuselage section):
  - Strong & Flexible Plastic: $13.56-$14.56
  - Aluminum: $126.64
- Tube (structural element):
  - Strong & Flexible Plastic: $12.96-$13.96
  - Aluminum: similar pricing

**Lithium-ion Battery Packs (CMEC - Jan 31, 2018)**
Common configurations for small aircraft applications:
- 6S4P (25.2V, 14Ah, 40A continuous): €235
- 6S6P (25.2V, 21Ah, 60A continuous): €330
- 10S6P (42V, 21Ah, 60A continuous): €550
- 10S9P (42V, 38.2Ah, 135A continuous, NCR20700B cells): €920

**Electronic Components**
- HS-5065MG servo (Hitec): $33.99 (24.99-30.55 oz/in torque, 0.11-0.14 sec/60°)
- KDE1806XF-2350 brushless motor: $25.95 (770g+ thrust on 5" propeller, 4S voltage)
- KDEXF-UAS20LV 20A+ ESC: $40.95 (2S-6S LiPo compatible, regenerative braking)
- LightWare LW20 laser rangefinder: $329.00 (100m range, I2C/serial, IP67 sealed)
- E+E EE03 humidity/temperature module: Starting $96.00 (±3% RH accuracy, -40 to +85°C range)

**Structural Materials**
- Round Kevlar tubing (2.000 x 2.030 x 72 inches): $230.99 (for aircraft frame)

### Travel & Per Diem Planning
- Hotel search for Silver Spring, Maryland (June 4-5, 2018)
  - Hampton Inn: $126/night
  - DoubleTree by Hilton: $147-159/night
- Montgomery County, Maryland per diem (2018):
  - Lodging: $201-253/month depending on season
  - Meals & Incidentals: $69/day ($64 meals only)
  - Incidentals: $5/day

## Notable Details

1. **Aircraft Development Focus**: Heavy emphasis on S0 composite aircraft development with significant hours allocated to prototype fabrication (40-60 hrs), flight testing, and design iterations.

2. **Integration with AVAPS**: SwiftPilot interface development for integration with NOAA's Automated Vertical Atmospheric Profiling System—suggesting deployment on NOAA research aircraft (P3 Orion referenced).

3. **Sensor Suite Philosophy**: Comprehensive approach including bench calibration, wind tunnel validation, and flight testing before deployment.

4. **Cost-Effective Component Strategy**: Mix of commercial off-the-shelf (COTS) components (servos, motors, ESCs, batteries) with custom PCB design and 3D-printed structural elements.

5. **Subcontractor Integration**: University of Colorado (iMET) providing sensor integration and calibration expertise at $110/hour rate.

6. **Budget Efficiency**: Relatively small team (4-5 named personnel) managing multi-domain technical tasks spanning airframe, avionics, firmware, and sensor integration.

This appears to be a well-organized SBIR Phase I effort focused on developing an autonomous small aircraft platform for atmospheric science applications, with particular emphasis on sensor integration and NOAA system compatibility.