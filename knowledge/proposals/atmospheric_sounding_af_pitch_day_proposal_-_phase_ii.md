# Atmospheric Sounding AF Pitch Day Proposal - Phase II

## Document Metadata
- **Type:** SBIR Phase II Proposal
- **Client/Agency:** U.S. Air Force
- **Program/Solicitation:** AF192-005 (SBIR Topic); Proposal Number F2-12711
- **Date:** Submitted 2019 (created October 7, 2019)
- **BST Products/Systems Referenced:** S0 UAS (modified atmospheric sounding variant), S0-AD (air-deployed version), Multi-hole Probe (MHP)
- **Key Personnel:** Dr. Jack Elston (PI, CEO), Josh Fromm (Lead Engineer), Dr. Maciej Stachura (Aerospace Engineer)

## Executive Summary
Black Swift Technologies proposes to develop a hand-launched, purpose-built unmanned aircraft system (S0) for rapid atmospheric profiling to support Air Force weather operations, Army, and Special Operations Forces. The system would provide vertical wind profiles up to 15,000 feet in under 20 minutes with autonomous operation, precision landing within 10 feet, and high-wind tolerance (30+ mph), while maintaining a target cost of approximately $5,000 per unit and compatibility with existing Air Force data systems.

## Technical Approach

### Problem Statement
Current atmospheric data collection relies on balloon-borne soundings and dropsondes, which provide limited spatial-temporal density and are not recoverable. Satellite systems (ASTER, MODIS, AIRS, OMI) suffer from low spatial resolution and infrequent measurement cycles. A need exists for targeted, repeatable, recoverable in situ measurements that can be quickly deployed by small teams in remote locations.

### Proposed Solution
BST proposes to adapt the S0-AD (originally designed for hurricane sampling) into a ground-deployed atmospheric sounding platform with the following key modifications:

1. **Airframe Design:** Modified wings and tail optimized for hand-launch, fast climb rate (~4 m/s or 787 ft/min), and precision deep-stall landing (vertical descent, landing within 10 feet). Design analysis conducted using XFRL5 vortex lattice method during Phase I.

2. **Flight Characteristics:** 
   - Cruise speed: 35-40 mph
   - Cruise angle-of-attack: 1.5° (zero elevator deflection)
   - Efficient CL/CD across broader speed range
   - Endurance: 60 minutes flight time
   - Target climb performance: reach 15,000 ft AGL in under 20 minutes

3. **Onboard Algorithms:** Novel control algorithms for accurate profiling at fast climb rates, maintaining consistent angle-of-attack and zero sideslip to maximize 3D wind estimation accuracy. Aircraft will maintain set angle-of-attack during climb phase.

4. **Autonomy & Communications:** Dual-mode operation—fully autonomous with no wireless communications (for stealth/denied-area operations), or real-time wind data downlink to ground operator. Two-mode capability adds Air Force exclusivity to commercial version.

5. **Data Integration:** Automated data formatting and transmission compatible with Air Force standard desktop systems and Air Force Data Centers. Support for text file, BUFR, GRIB, and netCDF formats for weather model ingestion.

## Products & Capabilities Described

### S0 UAS (Modified Atmospheric Sounding Variant)
- **What it is:** Hand-launched, fixed-wing UAS purpose-built for atmospheric profiling; adaptation of BST's commercial S0-AD platform
- **Proposed uses:** Tactical upper air measurement to support Air Force Weather, Army, and Special Operations Forces operations; rapid wind field characterization for precision operations (e.g., airborne drops)
- **Key specifications:**
  - Weight: 2 lbs
  - Wingspan: 31 inches
  - Cruise time: 60 minutes
  - Launch type: Hand-launch (modified from S0-AD's air deployment)
  - Communications range: 100 miles (one-way)
  - Setup/deployment time: <5 minutes by single operator
  - Landing precision: 10-foot radius
  - Target cost: ~$5,000 per unit

### Multi-hole Probe (MHP)
- **What it is:** BST-designed and manufactured sensor instrument for measuring 3D wind velocity, pressure, temperature, and humidity. Uses 3D printing to reduce cost by 10x compared to traditional instruments; originally developed under NASA SBIR.
- **Integration:** Core sensing component of S0; provides real-time wind data at 100 Hz sampling rate
- **MHP Specifications:**
  - Weight: 1.8 oz (50 g)
  - Cost: $2,000
  - Wind velocity resolution: 0.03 m/s
  - Wind velocity accuracy: 0.29 m/s
  - Temperature range: -40° to 85°C
  - Temperature accuracy: ±0.3°C
  - Pressure resolution: 0.012 mbar
  - Pressure accuracy: 1.5 mbar
  - Relative humidity range: 0-100% RH
  - Humidity accuracy: ±1.3% RH
- **Market validation:** 9 units sold to date (NOAA, NCAR, University of Colorado Boulder, others) with ~$9,000 revenue in past 12 months, achieved with minimal marketing effort

### S0-AD (Air-Deployed Variant)
- **What it is:** Commercial predecessor platform designed for air deployment from manned aircraft into hurricanes
- **Current use:** NOAA hurricane sampling; BST has contract to deliver 5 units through mid-2021
- **Status:** Intended as replacement for Navy Coyote UAS for NOAA hurricane research

### SwiftTab Ground Station Software
- **What it is:** User interface running on ruggedized Android tablet for mission planning, real-time telemetry, and data download
- **Capabilities:** Simplified scripting for complex atmospheric sampling patterns; data visualization consistent with weather balloon output; modeled on existing BST ground control systems

## Use Cases & Applications

### Primary Mission (Air Force)
- **Tactical upper air measurements** for Air Force Weather supporting Army and Special Operations Forces (SOF) operations
- **Precision drop operations:** Rapid wind field knowledge enabling accurate airborne insertions
- **Boundary layer characterization** for military operations in unfamiliar terrain
- **Speed of intelligence:** Fast data collection and processing (<15 minutes post-landing) to support nowcasting and tactical decision-making

### Secondary Military/Government Applications
- **Air Defense Artillery, Armor, Aviation, Chemical, Engineer, Field Artillery operations:** All have validated weather/environmental data requirements
- **ISR missions:** Platform capable of carrying alternative sensor payloads (atmospheric monitoring, environmental sensing, intelligence gathering)
- **Special Operations Forces:** Rapid deployment requiring minimal setup time and personnel

### Non-Defense Research & Commercial Applications
- **Severe weather research:** Supercell thunderstorm characterization; tornado sampling
- **Arctic operations:** Remote, harsh-environment atmospheric profiling (mentioned as high-altitude/remote research requirement)
- **Hurricane research:** NOAA partnership for continued validation and operational deployment
- **Cloud physics research:** Potential payloads for cloud water content, precipitation measurement
- **Atmospheric chemistry:** Gas sensors, chemical/biological detection payloads
- **Environmental monitoring:** Methane detection, air quality sensing, aerosol characterization
- **Hydrological research:** Soil moisture, snow cover depth measurement
- **Maritime applications:** Sea surface temperature, sea ice properties observation
- **High-altitude research:** Ozone, SO₂, NOₓ measurement; aerosol characterization (requested up to 100,000-120,000 ft altitude by some researchers)

## Key Results (Phase I Findings)

### Aerodynamic Analysis (XFRL5)
- Pitching moment coefficient reaches zero at 1.5° angle-of-attack (aircraft's natural cruise condition with no elevator deflection)
- CL/CD maximum occurs at cruise condition, with flat efficiency curve allowing speed range of 35-40 mph without significant endurance loss
- Flow analysis and lift distributions confirmed stable design with negative tail lift at cruise

### Flight Testing
- Two test flights completed in challenging conditions (5 kt sustained winds, gusts to 13 kt)
- Aircraft demonstrated qualitative flying characteristics aligned with design expectations
- Prototype platform ready for Phase II sensor integration and performance validation testing

### Customer Discovery
- **Federal Government contacts:** 58 attempted, 5 reached (5 by phone, 0 by email, 0 in person)
- **Federal organizations:** 9 contacted, 4 reached
- **USAF organizations:** 2 contacted, 1 reached (Major Andrew Travis, Hanscom AFB)
- **Interviews conducted:** Meteorology groups, commercial entities, research institutions
- **Requirement consensus:** Altitude 10,000-15,000 ft; flight duration ~1 hour; 10-ft recovery accuracy; hand-launch feasibility; autonomous operation preferred

### Stakeholder Support
- **MOU received** from Bruce A. Lambert, DAF Chief Engineer, Weather Systems Branch, Air Force Life Cycle Management Center (Hanscom AFB), supporting technology as potential tactical upper air measurement tool for unfunded ACC/A5W requirement
- **Letters of support** from NOAA, NASA, NCAR, and academic researchers (Dr. Greg Blumberg, NASA GSFC; Dr. Ahmed Fadl, NASA Wallops; Larry Cornman, NCAR)

## Phase II Technical Objectives & Key Results

### Objective 1: Validate Operational Performance
1. **Flight Endurance Testing:** Demonstrate climbs/descents equivalent to 15,000 ft ascent in under 20 minutes (4 m/s climb rate) while maintaining Part 107 waiver compliance
2. **Precision Autoland Validation:** 10 consecutive fully autonomous landings with maximum error ≤10 ft, documenting average error
3. **High-Wind Operations:** 3 successful sampling missions in winds exceeding 30 mph with full autonomous flight and no aircraft damage

### Objective 2: Validate Meteorological Sensing Accuracy
1. **3D Wind Estimation Accuracy:** Validate wind measurements against tower and weather balloon overflight on 5 separate days with target accuracies:
   - Lateral wind: ±2° heading, ±0.3 m/s speed
   - Vertical wind: ±0.4 m/s
2. **Secondary Sensor Validation:** Confirm pressure, temperature, humidity measurement accuracy:
   - Temperature: ±0.3°C RMS
   - Pressure: ±1.5 hPa RMS
   - Humidity: ±1.3% RMS

### Objective 3: Validate Ground Systems & Data Handling
1. **Operator Training & Setup:** Non-BST personnel (UNL operators) complete 5 missions with setup time <5 minutes per mission
2. **Real-Time Telemetry:** Full science data downlink over complete profile; communications validated to 15,000 ft overhead altitude; emergency procedures and fault trees established
3. **Air Force Data Format Generation:** 5 sampling flights on separate days generating BUFR-format data files meeting Air Force standards within 5 minutes of landing

## Phase II Work Plan

### Task 1: Design and Manufacture Ground-Deployed S0 Airframe
- Base design on tube-deployed S0-AD variant to minimize risk and leverage existing manufacturing
- Continued aerodynamic refinement using vortex lattice methods
- Focus on field maintenance, operational simplicity, and compact transport configuration for Air Force operations
- **Deliverables:** Detailed aerodynamic assessment report; flight-test-ready airframe

### Task 2: Design and Manufacture S0 Avionics, Sensors, and Radio Configuration
- Adapt tube-deployed S0 avionics with modifications for:
  - Swappable radio systems (AVAPS, iMet base station, ISM 900 MHz, cellular, fully autonomous mode)
  - Hard-wired device interface for parameters, flight plans, diagnostics, firmware updates, data download (browser-based, no proprietary software required)
  - Real-time and post-flight data transmission capability
- Maintain MHP sensor as core measurement instrument
- **Deliverables:** Detailed design report; flight data files in Air Force format for validation

### Task 3: Design and Manufacture Ground System & User Interface
- Develop SwiftTab module for ruggedized Android tablet
- Capabilities: Mission planning, near-real-time telemetry, data download, atmospheric sampling pattern scripting
- Data visualization consistent with weather balloon output
- **Deliverables:** Hardware and software components built and tested at BST facility

### Task 4: Flight Testing and Validation in Relevant Environment
- Multi-condition flight testing (various altitudes