# Contract UAS Questionnaire

## Document Metadata
- Type: Regulatory questionnaire / compliance documentation
- Client/Agency: NASA (implied from folder structure)
- Program/Solicitation: 2016 SBIR Phase I - Volcano Monitoring
- Date: 2016-12-06 to 2016-12-09
- BST Products/Systems Referenced: SuperSwift (S2), SwiftPilot Pro autopilot, SwiftStation, SwiftTab
- Key Personnel: Jack Elston (last editor), Maciej Stachura (UAS owner contact)

## Executive Summary
This is a comprehensive regulatory questionnaire completed by Black Swift Technologies for NASA's approval to conduct volcano monitoring flights using the SuperSwift UAS. The document details aircraft specifications, systems architecture, operational procedures, safety measures, and crew qualifications for a Phase I SBIR project involving payload integration and autonomous flight operations.

## Technical Approach
BST proposed to operate the SuperSwift, a small composite aircraft equipped with the SwiftPilot Pro autopilot system, to conduct autonomous sampling flights near volcanic sites. The system uses a hybrid control architecture with:
- Primary autonomous control via SwiftPilot Pro autopilot
- Secondary manual override via 2.4 GHz radio control handset
- Ground control station (GCS) with tablet interface for mission planning and monitoring
- Dual communication links (900 MHz ISM for autopilot/telemetry, 2.4 GHz for manual control)
- Hand-launched operations with autonomous landing capability

## Products & Capabilities Described

### SuperSwift (S2)
- **Configuration**: Fully composite, molded fiberglass airframe
- **Dimensions**: Length 73.6", wingspan 120.6", tail height 8.2"
- **Weight**: Maximum gross takeoff weight (GTOW) 15 lbs; zero fuel weight 10 lbs; payload capacity 5 lbs
- **Performance**:
  - Maximum speed: 48 kts
  - Cruise speed: 39 kts
  - Maximum endurance: 1.5 hours
  - Maximum range: 58.5 nm
  - Rate of climb: 950 ft/min
  - Rate of descent: 810 ft/min
  - Maximum glide slope: 15 degrees
  - Maximum altitude capability: 400' AGL (mission-limited)
- **Propulsion**: Electric motor (SII-4020-420kV, 1500W continuous, 0-30A current draw)
- **Power**: On-board battery monitoring with auto-cutoff; 15-minute power reserve margin maintained
- **Landing**: Belly landing on underside of fuselage (no landing gear)
- **Designed for**: Scientific payloads up to 5 lbs with easy access and rapid integration

### SwiftPilot Pro Autopilot
- Commercial COTS autopilot product from BST
- Allows dual control interfaces: manual handset and ground control station (GCS)
- Supports both autonomous and manual flight modes with switchable control authority
- Implements automated emergency responses:
  - Lost communications: Returns to designated waypoint, then aerodynamic termination after 5 minutes
  - GPS loss: Banks aircraft at fixed angle, holds altitude
  - Motor failure: Maintains airspeed while descending
- Parameter-based flight envelope protection (48 kts max airspeed, ±45° roll, +25°/-15° pitch limits)
- Uses CAN bus for servo control board communication and payload integration
- Employs X-Plane software-in-the-loop (SIL) simulation for validation

### SwiftStation (Ground Control Station)
- Communication relay between aircraft and tablet
- Dual power: A/C plug or 6-hour battery backup
- Enables heartbeat monitoring (1 Hz) of aircraft connection status

### SwiftTab (Tablet Interface)
- Android-based user interface
- Provides geo-referenced map view with real-time telemetry
- Allows waypoint creation/modification and mission plan changes via touch interface
- Displays aircraft attitude (±0.5° accuracy in roll, pitch, yaw)
- Color-coded indication of successful/pending command transmission
- Run time: >12 hours from internal batteries

### Radio Systems
- **Primary link**: Digi Xtend frequency-hopping, spread-spectrum (FHSS) radios
  - Frequency: 902-928 MHz ISM band
  - Power: 1W maximum
  - Data rate: 115.2 kbps
  - Encryption: Optional 256-bit AES
  - Link margin: ~30 dB at 5-mile maximum distance
- **Secondary/Manual link**: 2.4 GHz spread-spectrum radio control system (redundant)

### Avionics Architecture
- Gumstix on-board computer for data logging
- CAN payload bus for auxiliary sensor integration (8 sensor ports documented)
- Sensor inputs: GPS, static pressure (for altitude), motor current
- Autopilot outputs: PWM signals to servo control boards via CAN
- Real-time attitude and position telemetry to ground station

## Use Cases & Applications

### Volcano Monitoring Mission
- **Primary objective**: Deploy scientific sensors near volcanic sites for atmospheric and gas sampling
- **Payload configuration**: Custom scaffolding designed for 5 lbs of instruments including:
  - EO (electro-optical) camera
  - Thermal camera
  - Forward video
  - MHP (Met Probe) + PTH (pressure/temperature/humidity) sensors
  - Nephelometer (particle scattering measurement)
  - Trace gas sampling inlet
- **Operational area**: Remote volcanic sites (example area ~8 miles from nearest town)
- **Flight profile**: 
  - Daytime VFR operations only
  - Maximum wind condition: 20 kts
  - Autonomous waypoint-based sampling patterns
  - 400' AGL maximum altitude
  - Visual line-of-sight maintained by observer

### Specific Experiment Ports
Six dedicated payload integration points on SuperSwift:
1. Bottom-mounted cameras (EO, thermal)
2. Forward-looking video and sensors (nose cone)
3. Top-mounted atmospheric sampling probes
4. Distributed inlet ports for gas sampling

## Key Results
This questionnaire is regulatory documentation rather than a results report. However, it demonstrates:
- **Proven platform**: PIC had 10+ previous SuperSwift flights with 5+ hours flight time
- **System maturity**: SwiftPilot Pro has been used in "several different airframes covered under a number of FAA COAs"
- **No historical failures**: No system failures, accidents, or major modifications reported for this specific aircraft
- **Simulation validation**: Full mission profile validated using software-in-the-loop X-Plane simulation

## Notable Details

### Safety & Redundancy Measures
- **Dual control modes**: Autopilot + independent manual RC handset backup
- **Geo-fence**: Automated boundary enforcement prevents exceeding COA limits
- **Lost link procedure**: Automatic return-to-home with 5-minute timeout before aerodynamic termination
- **Power monitoring**: Battery voltage monitor with auto-motor cutoff when depleted
- **Manual override**: Handset can immediately take control in any flight phase
- **Emergency termination**: Quick engine disable via manual handset or interface

### Regulatory Compliance
- Operating under FAA Section 333 exemption (mentioned in document)
- Class E airspace operations (VFR)
- NOTAM issued 24 hours prior to flights
- No transponder required (small UAS exemption)
- No formal flight plan filing required
- Observer trained in FAR Part 91.113 right-of-way rules

### Quality Assurance & Configuration Management
- Using Subversion + Trac for version control and change tracking
- In process of implementing FAA DO-178 certified QA procedures
- Unit testing and hardware-in-the-loop (HIL) simulation for verification
- Software version matching enforcement between ground and aircraft
- Pre-flight configuration file validation

### Crew & Training
- **PIC requirements**: Private Pilot Certificate minimum, current Class 2 medical, 3 takeoff/landing events in prior 90 days
- **Manual pilot**: Current RC flying experience with similar airframe
- **Observer**: Class 2 medical, trained in FAR 91.113, visual scan techniques, proper radio phraseology
- **Team size**: 4-person flight crew (all ground-based except PIC during flight)

### Operational Procedures
- Hand-launch by PIC
- Manual pilot flies from takeoff through initial climb
- Transition to autonomous mode after qualitative state verification
- Autonomous sampling mission execution
- Manual pilot retakes control for descent and landing
- Autonomous belly landing to designated area
- Post-flight data download via laptop from on-board SD card

### Ground Support Equipment
- SwiftStation (GCS relay and communications hub)
- SwiftTab (tablet running control software)
- Manual handset (RC control backup)
- Minimal support requirements; no generators or specialized launch equipment

### Unique Constraints & Limitations
- Maximum operating wind: 20 kts
- VFR-only conditions (3 SM visibility minimum, 900' cloud ceiling)
- No icing capability or cold-weather operation
- No anti-collision lights
- Limited to single aircraft operations in area
- 400' AGL altitude limit (COA restriction)
- No flight recovery/parachute system
- Belly landing only (no conventional runway required)

### Distance to Hazards
- Nearest town (Nunn, CO): 8 miles
- Nearest major city (Fort Collins, CO): 22 miles (outside glide range)
- Nearest highway (US-85): 7.5 miles
- Nearest major highway (I-25): 17.5 miles

---

**Document Quality Note**: This is a thorough, complete regulatory questionnaire with detailed responses across all sections. The document includes references to attached files (flight test plan, emergency procedures, checklists, manual) that provide additional implementation details. The questionnaire demonstrates mature operational procedures and comprehensive system understanding appropriate for NASA SBIR Phase I volcano monitoring work.