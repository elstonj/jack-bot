# S0 UAS Specification Document

## Document Metadata
- Type: Specification Document
- Client/Agency: U.S. Air Force (557th Weather Wing)
- Program/Solicitation: SBIR Phase II; Contract Number FA8730-20-C-0021
- Date: January 16, 2020
- BST Products/Systems Referenced: S0 UAS, S0-AD (Air Deployed)
- Key Personnel: Jack Elston (document author/last editor)

## Executive Summary
Black Swift Technologies proposes to develop the S0 UAS, a purpose-built unmanned aircraft system designed specifically for atmospheric sounding and meteorological measurements. The system modifies BST's existing S0-AD (air-deployed) platform with optimized airframe design, advanced wind measurement algorithms, and standardized data formatting to meet U.S. Air Force requirements for rapid vertical atmospheric profiling, particularly to support precision operations like cargo drops.

## Technical Approach

**Airframe Modifications:**
- Redesigned wing and tail configuration optimized for hand-launch, increased endurance, and rapid vertical climb
- Novel tail design enabling deep-stall landing capability for near-vertical descent and precision landing in difficult terrain
- Aerodynamic design informed by computational flow analysis (Cp distributions, wing/tail lift profiles)

**Flight Control & Measurement:**
- Onboard algorithms enabling rapid vertical profiling while maintaining accurate 3D wind estimation
- Aircraft flies at set angle of attack during climb with zero sideslip condition to maximize wind estimation accuracy
- Utilizes onboard MHP (Multi-Hole Probe) sensor for wind velocity measurements
- Novel flight control approach not previously available in commercial atmospheric sounding platforms

**Data Systems:**
- Dual operational modes: (1) fully autonomous with no wireless communications, (2) secure real-time wind data downlink to operator
- Data formatting compatible with existing Air Force systems and command/control interfaces
- Open interface specifications and SDK provided for third-party software development
- Android tablet-based ground control station for commercial variant

## Products & Capabilities Described

### S0 UAS
- **What it is:** Hand-launched unmanned aircraft designed for vertical atmospheric profiling and meteorological data collection
- **Key specifications:**
  - Maximum altitude: 4,572 m (15,000 ft)
  - Climb rate: ~4 m/s (787 ft/min) to 15,000 ft in 20 minutes
  - Wind tolerance: Capable of operations in winds exceeding 26 knots (30 mph)
  - Packed dimensions: Sum of three linear dimensions ≤157 cm (62 inches)
  - Packed weight: ≤4.5 kg (10 lbs)
  - Autoland accuracy: ±3 m (10 ft) precision landing with no damage

**Sensors:**
- 5-hole probe with PTH (pressure, temperature, humidity) sensors
- Field-replaceable sensor suite
- Measurements in standardized formats: BUFR, GRIB, netCDF, weather balloon format (txt)

**Performance Characteristics:**
- Hand-launch capable
- Setup/takedown: Toolless assembly and disassembly; <5 minutes total mission prep and breakdown
- Preflight checklist: <5 minutes
- Real-time telemetry: Encrypted ISM point-to-point radio downlink to ground station and Android tablet
- Communications range: Effective up to 4,572 m overhead
- USB data download interface (non-wireless variant)

## Use Cases & Applications

1. **Primary: U.S. Air Force Weather Support**
   - Rapid wind field characterization for precision cargo drops and military operations
   - Support to 557th Weather Wing and Army operations (50% of AF weather activity)
   - Operational support for Air Defense Artillery, Aviation, Field Artillery, Engineering, and other Army branches

2. **Scientific/Commercial:**
   - Weather forecasting and atmospheric modeling
   - Atmospheric/environmental monitoring
   - Intelligence, Surveillance & Reconnaissance (ISR) with alternative payloads

3. **Operational Context:**
   - Fills gap between satellite remote sensing (limited spatial resolution, low overpass frequency), balloon soundings (single-time snapshot), dropsondes (single-use), and ground-based radar/lidar (limited altitude coverage)
   - Enables repeatable, targeted in situ measurements with recoverable platform and sensor reuse

## Measurement Requirements & Validation

**Wind Estimation Accuracy (validated vs. tower and weather balloon):**
- Lateral wind: ±1° heading, ±0.3 m/s speed
- Vertical wind: ±0.4 m/s during climb; ±0.1 m/s using specific horizontal flight pattern
- Validation: 5 days of comparative missions with co-located meteorological tower and balloon soundings

**Meteorological Sensor Accuracy:**
- Temperature: ±0.3°C RMS
- Pressure: ±1.5 hPa RMS
- Relative Humidity: ±1.3% RMS

## Test & Validation Goals

**Proficiency Demonstration:**
- Non-BST personnel to complete 5 successive missions (preflight, hand launch, data collection, autoland) without issues

**Vehicle Performance Validation:**
- Real-time telemetry: Continuous science data downlink; communications verified to 15,000 ft overhead; emergency procedures and fault trees documented
- Autoland: 5 consecutive landings with error ≤3 m, no damage, aircraft operational afterward
- Endurance: Demonstrate 5 climb/descent cycles meeting 4 m/s climb rate to 15,000 ft requirement

**Data Product Retrieval:**
- Validation through both encrypted real-time link and post-flight wired interface
- Onboard sensor accuracy verified against on-site meteorological instrumentation (tower-mounted)
- Aircraft flown past tower sensors at mission climb rate to account for sensor lag

**Operability:**
- Trained non-BST operator performs 5 missions with setup time <5 minutes per mission

## Notable Details

- **Supply Chain & Manufacturing:** Autopilot designed and manufactured in the USA; alternate suppliers specified for major components
- **Competitive Advantage:** Sensor-reactive control algorithms allowing sampling focused on areas of interest—capability unavailable from existing atmospheric sounding technology
- **Market Strategy:** Production design prioritizes high production numbers to keep costs low and ensure Air Force availability; commercial variant distributed through standard channels with different data formats and interfaces than military version
- **Unique Design Features:**
  - Deep-stall landing capability enables near-vertical descent and precision landing in difficult terrain
  - Constant angle-of-attack and zero-sideslip flight during climb maximizes wind measurement accuracy
  - Onboard algorithms compute wind estimates in real time
- **Field Operability:** Mission setup without additional equipment (buttons and onboard feedback); Android tablet UI for commercial variants; USB charging and data download
- **Security:** Non-wireless option available with no software installation requirement; wireless variant uses encrypted radio links; Android application digitally signed; commercial tablet stripped to minimal apps
- **Documentation & Integration:** Data products formatted for direct assimilation into existing Air Force models and meteorological systems; open interface specifications provided for third-party integration