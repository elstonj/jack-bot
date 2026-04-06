# Soil Moisture Concepts of Employment

## Document Metadata
- Type: Concepts of Employment / Operational Requirements Document
- Client/Agency: U.S. Air Force (AFWERX)
- Program/Solicitation: DOD Air Force AFWERX Business Development
- Date: Created 2025-01-14; Modified 2025-01-27
- BST Products/Systems Referenced: Soil Moisture Measurement (SMM) system; UAS-mounted soil moisture sensor suite
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
This document outlines Black Swift Technologies' proposed Soil Moisture Measurement (SMM) system for three Air Force operational concepts: unimproved runway integrity assessment, base civil engineering projects, and ground trafficability assessment. The SMM system uses UAS-mounted remote sensing (NDVI, IR thermal, and L-band radiometer) to replace manual cone penetrometer measurements, reducing personnel exposure to threat in contested environments while providing spatially distributed soil integrity mapping.

## Technical Approach

### Sensor Suite
The SMM system comprises three integrated sensors:
- **NDVI (Normalized Difference Vegetation Index)**: Measures health and quantity of vegetation
- **IR Thermal**: Measures ground surface temperature (degrees Celsius)
- **LDCR (Lobe Differencing Correlating Radiometer)**: Measures brightness temperature (L-band energy, degrees Kelvin)

**Processing**: Onboard processing calculates both soil moisture maps and soil integrity maps from sensor data.

**Platform Flexibility**: System can be mounted on multirotor or fixed-wing UAS.

**Technical Basis**: Approach leverages established research showing correlation between soil moisture and soil integrity, and demonstrated capability of space-based and aircraft-mounted radiometers to measure soil moisture remotely.

## Products & Capabilities Described

### Soil Moisture Measurement (SMM) System
- **What it is**: UAS-mounted remote sensing system for real-time soil integrity and soil moisture assessment
- **Key advantage over current method**: Provides spatially distributed measurements across entire runway/route rather than point measurements; reduces personnel exposure to threat
- **Proposed platforms**: Multirotor or fixed-wing UAS
- **Output**: Soil moisture maps and soil integrity maps

## Use Cases & Applications

### 1. Unimproved Runway Integrity Assessment
**Current approach**: Air Force Special Tactics Teams (contested) or Civil Engineering units (uncontested) use cone penetrometer to measure soil integrity at multiple points across prospective runway.
- Drop weight on rod driven 36 inches into ground
- Measure blows per inch, convert to California Bearing Ratio (CBR) or Cone Penetration Index (CPI)
- Takes ~5 minutes per measurement point
- Exact number of measurements required unknown

**Contested scenario**: Team covertly inserted to austere location (e.g., dry lake bed in hostile territory); provides own security during insertion and assessment; reports results via radio/SATCOM after measurement; exfiltrates on first available aircraft.

**Uncontested scenario**: Typically humanitarian relief after natural disaster; performed by civil engineering units with administrative/logistical infrastructure support; results reported via telephone or email.

**Problem addressed**: Current approach time-consuming and exposes servicemembers to enemy threat in contested environments.

**Proposed SMM advantage**: Remote measurement from UAS reduces personnel exposure; provides comprehensive coverage across runway surface rather than point samples.

### 2. Base Civil Engineering Projects
Document outlines this use case but content incomplete/underdeveloped (template structure provided without substantive detail).

### 3. Ground Trafficability Assessment
**Mission**: Assess soil conditions along routes for vehicle convoy transit to prevent vehicles becoming stuck in mud/soft soil/waterlogged areas.

**Current challenges**: Lack of real-time soil stability data forces convoys to take longer alternative routes or use trial-and-error navigation, risking delays, mechanical strain, delays, vulnerability to ambush/exposure.

**Proposed solution**: UAS-mounted SMM system performs on-call measurement of soil integrity along ground routes using fixed-wing unmanned platform; provides soil integrity maps across width and length of prospective route.

**Problem addressed**: Enables predictive terrain assessment before transit; reduces risk of vehicles becoming stuck.

## Key Results
None provided. Document is a prospective concepts paper, not a report of completed work or testing.

## Notable Details

### Current System Limitations
- **Cone penetrometer**: Purely mechanical; low maintenance (corrosion prevention only); no batteries/electronics; but time-consuming and personnel-intensive
- **Point vs. distributed measurement**: Current approach yields only point measurements at discrete locations; exact number required for certification unknown
- **Personnel exposure**: Both contested and uncontested scenarios require personnel on the ground; contested operations expose Special Tactics Teams to enemy threat during insertion, assessment, and exfiltration

### Soil Types and Accuracy Specifications
Document indicates uncertainty in specifications:
- Soil types: "All natural soil types? Not rock?" (unknown whether rock surfaces supported)
- Soil integrity accuracy: "???" (not specified)
- Soil moisture accuracy: Listed in specification tables but values not filled in

### Operational Flexibility
- Works in both contested (covert insertion) and uncontested (humanitarian relief) scenarios
- Applicable to different operational personnel: Air Force Special Tactics Teams vs. Civil Engineering units
- Compatible with existing military communication infrastructure (radio, SATCOM, digital, telephone, email)

### Document Status
Document is incomplete/draft stage. Three major use cases outlined but:
- "Base Civil Engineering Projects" section is template-only (section headers with no content)
- "Ground Trafficability" section has significant placeholder text ("Ipsum lorem...")
- "System Analysis" sections across all use cases are unfilled
- Many specification fields marked unknown or incomplete ("???")
- Operational policies and constraints consistently marked "Unknown"

This appears to be a work-in-progress concepts document being developed for Air Force AFWERX to structure requirements and operational employment for the SMM system across multiple use cases.