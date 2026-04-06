# S0 UAS Phase II Interim Report

## Document Metadata
- Type: SBIR Phase II Interim Report
- Client/Agency: National Oceanic and Atmospheric Administration (NOAA)
- Program/Solicitation: NOAA SBIR Phase II
- Contract Number: 1305M219CNRMW0030 (Phase II); 1305M218CNRMW0059 (referenced)
- Date: August 23, 2019
- BST Products/Systems Referenced: S0 UAS, S2 UAS, SwiftTab UI, SwiftCore autopilot
- Key Personnel: Dr. Jack Elston (Principal Investigator/Project Manager), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Mechanical Engineer)

## Executive Summary
This interim report documents Q1 progress on the NOAA SBIR Phase II contract for developing the S0, a low-cost, air-deployed unmanned aircraft system (UAS) designed for boundary layer observations in tropical storms and hurricanes. The project aims to create a purpose-built platform that costs approximately $5,000 per unit while maintaining 1-2 hours of endurance and comprehensive meteorological sensing capabilities. As of August 23, 2019, the project is 20% physically complete with $78,915.61 in cumulative costs incurred.

## Technical Approach

### S0 UAS Design Philosophy
The S0 represents a significant cost reduction compared to existing platforms (Coyote, Aerosonde, Altius at ~$35,000) while maintaining measurement quality. Key design innovations include:

- **Airframe**: Single swiveling wing design with fixed 3D-printed rear horizontal stabilizer to reduce complexity and deployment failure risk
- **Weight target**: Less than 2.5 lbs gross takeoff weight (GTOW)
- **Design basis**: Purpose-built for air deployment from P-3 aircraft (from AXBT tube or dropsonde tube)
- **Operational constraint**: Designed to mimic radio dropsonde operations to fit existing NOAA CONOPS

### Sensing Architecture
The S0 integrates BST's proprietary autopilot, ground station, and sensor suite:
- Multi-hole probe (MHP) for 3D wind measurement
- Temperature, humidity, pressure sensors (leveraging RD-41 dropsonde technology)
- Laser altimeter for height above water measurement
- Thermal IR sensor for sea surface temperature (SST)
- GPS-based position and velocity
- Real-time data streaming via AVAPS integration

### Autopilot & Control
- BST's certified autopilot provides autonomous flight control
- Unscented Kalman Filter (UKF) fuses multi-hole probe data with onboard accelerometer and gyroscope data
- Intelligent autonomous sampling: aircraft can make navigation decisions based on atmospheric sensor data
- Sophisticated hurricane mapping scheme developed in Phase I enables eyewall-autonomous navigation

### Multi-Hole Probe Development
- New dynamic pressure sensors with minimal drift (no zeroing required in-flight)
- Wind tunnel calibration with University of Colorado showing consistent manufacturing
- Individual calibration planned to be unnecessary, reducing per-unit cost
- Rigid body motion correction algorithm removes aircraft rotation effects on probe tip velocity (induced alpha/beta angles up to 2 degrees)
- Updated UKF now processes 100 Hz of sensor data, with onboard capability for 1 kHz processing

## Products & Capabilities Described

### S0 UAS
**What it is**: A purpose-built, air-deployable fixed-wing UAS optimized for meteorological observation in severe weather environments.

**Proposed use**: 
- Deployment from P-3 aircraft in tropical cyclones and hurricanes
- Boundary layer and sea surface observations
- Multiple flights per storm (enabling expanded temporal/spatial sampling vs. dropsondes)
- Autonomous navigation to storm features

**Specifications and Performance Targets**:
| Specification | Target | Verification Type |
|---|---|---|
| GTOW | <2.5 lbs | Test |
| Endurance | 2 hours at sea level | Flight test |
| Wind capability | Up to 160 mph | Simulation |
| Precipitation | Heavy precipitation capable | Test + flight |
| Deployment | AXBT tube compatible | Demonstration |
| Cost per unit | <$5,000 | Analysis |
| Cruise endurance | 1-2 hours | Flight test |

### Sensor Performance Targets
- **Air temperature**: ±0.7°C with <2 sec response time
- **Humidity**: ±5% with <5 sec response time
- **Pressure**: ±2.5 Pa with <1 sec response time
- **3D wind**: 0.5 m/s (horizontal), 1 m/s (vertical) with <1 sec response time
- **Ocean temperature**: ±0.5°C with <1 sec response time
- **Altitude above water**: ±10 cm
- **Shelf life**: ≥1 year before refurbishment

### Integration Interfaces
- AVAPS data streaming (real-time data transmission to P-3)
- GPS interface compatible with NCAR sonde
- Tablet-based UI (Android, ruggedized) for preflight setup (<15 min target)
- Serial and Ethernet backup interfaces for mission planning

## Use Cases & Applications

### Primary Application
**Tropical Cyclone Intensity Forecasting**: Air-deployed missions from NOAA's P-3 Hurricane Hunters
- Lower boundary layer observations within storm eyewalls
- Sea surface interaction measurements for air-sea coupling research
- Multiple flights per storm (vs. traditional single-use dropsondes at $800/unit)

### Secondary Applications (Implied)
- Formation flight for instantaneous atmospheric gradient measurement
- Severe convective storm observation (supercell penetration)
- Volcanic vent atmospheric sampling (evidenced by S2 flight data from Hawaii)
- General boundary layer profiling in turbulent environments

### Operational Concept
Designed to mirror NOAA dropsonde operations:
- Simple preflight setup (15 min target on tablet UI)
- Integration with existing P-3 onboard systems
- Minimal crew training required
- Real-time data streaming to forecasters

## Key Results (Phase I/Interim Phase II Activities)

### Completed Tasks (Q1 Phase II)
1. **Kickoff Meeting** (Aug 2019): Review of Phase I lessons learned, requirements update, risk assessment with technical monitor Joe Cione and NOAA/NASA stakeholders
   
2. **Requirements Document Finalization**: Formal verification matrix established with 20 system requirements across airframe, avionics, and sensors

3. **Test Site Validation**: 
   - Boulder aeromodeler's field (water overflight capability for laser/SST testing)
   - Sod farm near Longmont, CO (deployment mechanism and swivel wing testing)
   - Florida permissions being pursued for P-3 deployment tests

4. **Risk Review**: 18 identified risks with mitigation strategies covering:
   - Programmatic risks (weight, endurance, cost)
   - Operational risks (pitot tube clogging, premature launch, inclement weather)
   - Technical risks (sensor placement, precipitation effects, AVAPS integration)

### Wind Sensing Advances
**S2 Flight Data Analysis (Hawaii, 2019-08-08)**:
- New dynamic pressure sensors demonstrate near-zero offset at bootup (enabling no-zeroing operations)
- Rigid body motion correction successfully quantifies and removes aircraft rotation effects
- Improved UKF with accelerometer integration validates wind field consistency across flight legs
- Measured wind field (7.8 mph @ 93°) matches ground truth

**Wind Tunnel Calibration** (U of Colorado):
- Alpha and beta pressure sweeps show excellent agreement
- Consistent manufacturing tolerances across probes suggest no individual calibration needed per unit
- Cost-saving implication for S0 production

### Multi-Hole Probe Hardware
- New sensor board under iterative firmware development
- Hand-integrated sensors into Phase I probe for initial evaluation flights
- Flight testing underway to refine probe design

## Budget Status

**Contract Budget**: $399,578.08 (including 10% fee)
- Direct Labor: $196,700 (3 personnel × 1,000+ hrs @ $50/hr)
- Materials/Supplies: $42,138.55
- Travel: $3,329.98
- Indirect Costs (overhead 35% + G&A 15%): $121,084.27

**Expended to Date** (as of 08/23/19): $78,915.61
**Physical Completion**: 20%

### Planned Personnel Hours (Full Phase II)
- Dr. Jack Elston (PI): 1,517 hours
- Dr. Maciej Stachura (Lead Engineer): 1,136 hours
- Josh Fromm (Mechanical Engineer): 1,281 hours

## Notable Details

### Commercial Viability
- Reviewer feedback noted "very high likelihood of commercialization"
- $5,000 price point positioned between dropsondes ($800) and existing sUAS platforms ($35,000)
- Cost optimization work planned via design-for-manufacturing (DFM) techniques
- Recognized as cost-prohibitive for "full operational use and large purchases" (per reviewer weakness)

### Risk Mitigation Strategy
High-priority risks address:
- **Pitot clogging in heavy precipitation** (Very High likelihood, High consequence): Multi-hole probe provides 5 independent pressure points; GPS speed backup available
- **Inclement weather operations** (Moderate likelihood, Very High consequence): Aircraft designed for 160 mph winds and heavy precipitation
- **Premature tube launch** (Very High likelihood, Very High consequence): Aircraft will not interfere with manned aircraft after deployment

### Technical Team Expertise
- Long history building platforms for severe convective storm observation (Tempest, VORTEX2)
- Proven 3D wind measurement from UAS
- Custom autopilot and ground station development capability
- No external third-party autopilot or air data probe integration required

### Partnerships & Collaboration
- NOAA Aeronautical Operations Center (AOC) for P-3 integration and CONOPS validation
- University of Colorado for wind tunnel calibration
- NCAR for AVAPS interface specifications
- iMet Sensor for sensor placement expertise

### Design Constraints & Trade-offs
- **Weight**: 2.5 lb limit leaves only 0.4 lb design margin
- **Deployment complexity**: Air-deployment requirement increases airframe design complexity despite goal of simplicity
- **Sensor placement**: Multi-hole probe placement and aircraft flow effects critical to measurement accuracy
- **Unproven components over water**: IR SST sensor and laser altimeter both marked as unproven over ocean surfaces (fallback options identified)

### Phase II Remaining Work
Planned activities include:
- Aerodynamic optimization (target 90 min endurance at 5,500 ft MSL)
- Wing swivel mechanism prototype and testing
- Antenna integration and RF testing
- CONOPS document development
- Tablet UI implementation for preflight
- Tube and parachute system design
- Iterative flight testing at Boulder-area sites and Florida AOC facility