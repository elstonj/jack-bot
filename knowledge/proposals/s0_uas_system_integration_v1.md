# S0 UAS System Integration

## Document Metadata
- Type: Proposal / System Integration Document
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration), 53rd Weather Reconnaissance Squadron
- Program/Solicitation: NOAA WP-3D Orion Integration; Proposed WC-130J Integration
- Date: October 20, 2025
- BST Products/Systems Referenced: S0 UAS, SwiftCore avionics
- Key Personnel: Jack Elston (last editor)

## Executive Summary
The Black Swift S0 is a compact, air-deployable uncrewed aircraft system designed for extreme atmospheric operations (hurricanes, severe convection, marine boundary layer studies). Weighing approximately 3 pounds with under-2-foot wingspan, it launches through existing AXBT-style freefall chutes on NOAA P-3 and WC-130J aircraft without airframe modifications. During 2024, the S0 successfully deployed multiple times from the NOAA P-3 during Hurricane Milton, collecting over 20 hours of low-level meteorological data including wind gusts up to 209 knots, validating the air-launch and recovery concept as the first reusable, powered UAS from a hurricane reconnaissance aircraft.

## Technical Approach

### S0 UAS Design
- **Dimensions & Weight**: ~3 pounds; wingspan just under 2 feet
- **Launch System**: Deploys through existing AXBT-style freefall chutes on P-3 and WC-130J without aircraft modification
- **Stabilization**: Autonomous parachute deployment pre-separation, then transition to powered flight
- **Avionics**: SwiftCore-based precision control with onboard data processing
- **Telemetry**: Secure long-range communications exceeding 190 nautical miles line-of-sight
- **Autonomy**: Autonomous control validated in turbulent hurricane environments; lost-comms programming maintains 3,000 feet AGL ceiling with pre-planned mission profiles

### P-3 Integration Approach
- **Deployment**: Uses existing freefall chute (identical to AXBT system); S0 packaged in sealed canister matching AXBT tube size, shape, and weight
- **No Aircraft Modification**: Passes cleanly through standard NOAA fiberglass sleeve insert; fiberglass construction prevents contact with aircraft structure
- **Radio System**: Microhard P400 transceiver operating at 430/431 MHz narrowband (12.5 kHz bandwidth), 2-watt transmit power
- **Antenna**: Reuses existing 430 MHz antenna on P-3 (pre-approved infrastructure)
- **Ground Station**: 1U ruggedized, flight-qualified unit; powered from aircraft 110 VAC 60 Hz bus with internal battery backup
- **Interfaces**: Encrypted Wi-Fi control via ruggedized Android tablet; USB data access; Ethernet for AirOps integration

### WC-130J Integration Approach
- **Deployment**: Identical to P-3, using paratroop-door freefall chute with matching dimensions to P-3 system
- **Antenna**: 430 MHz removable panel-mounted antenna (frequency-agile system can shift bands if needed)
- **Ground Station**: Self-contained, portable, battery-powered (8 hours continuous operation); internal rechargeable battery with AC charging; can incorporate Mini-Circuits ZVBP-435-S+ bandpass filter inline
- **Installation**: Connects to removable panel-mounted antenna via single coaxial cable; minimal permanent aircraft modifications
- **Power Independence**: Does not require aircraft electrical system

## Products & Capabilities Described

### S0 UAS
- **Purpose**: Compact, air-deployable UAS for extreme atmospheric environments
- **Deployment Concept**: Launched through existing AXBT freefall chutes; autonomous parachute stabilization followed by powered flight transition
- **Control & Avionics**: SwiftCore-based onboard systems with precision control, data processing, and secure telemetry
- **Communications**: 190+ nautical miles line-of-sight range; Microhard P400 radio (430/431 MHz narrowband)
- **Mission Profile**: Low-altitude sampling with extended loiter; continuous 3D wind and thermodynamic measurements
- **Data Collection**: HDOB (High-Density Observation) formatted outputs compatible with NOAA networks
- **Lost-Comms Behavior**: Autonomous continuation of preplanned mission at ≤3,000 feet AGL until link restoration or mission completion

### SwiftCore Avionics
- Provides precision control, onboard data processing, and secure long-range telemetry backbone for S0 system

## Use Cases & Applications

### Hurricane Reconnaissance & Sampling
- **Hurricane Milton Operations (2024)**: Multiple successful P-3 deployments collecting 20+ hours of low-level meteorological data
- **Data Collected**: Wind gusts up to 209 knots; continuous 3D wind measurements; thermodynamic data
- **Application**: Storm intensity research, model assimilation, augmentation of traditional sonde data
- **Advantage**: Reusable, powered UAS provides continuous low-altitude measurements vs. expendable instruments

### Marine Boundary Layer Studies
- Extended loiter capability enables detailed atmospheric profiling

### Severe Convection Operations
- Compact design and air-launch approach suitable for intense weather environments

## Key Results

### Hurricane Milton 2024 Campaign
- Multiple successful deployments from NOAA P-3
- Over 20 hours of low-level meteorological data collection
- Wind gust measurements up to 209 knots
- Validated autonomous control and stable communications in turbulent conditions
- Confirmed clean release and recovery cycle
- First successful reusable, powered UAS launched from hurricane reconnaissance aircraft
- Results confirmed capability to augment sonde data with continuous, three-dimensional measurements critical for storm research

### Integration Validation
- 190 nautical miles line-of-sight communications demonstrated (exceeded design expectations)
- Clean electromagnetic coexistence with AVAPS and AXBT systems confirmed
- No aircraft structural modifications or airworthiness compliance issues identified
- Crew workflow compatibility verified with existing AXBT procedures

## AVAPS Interference Mitigation

### Problem Identified
Elevated noise on AVAPS receive chain during S0 telemetry transmissions (430–431 MHz band) despite narrowband operation within approved allocations; harmonic content and intermodulation coupling into sensitive AVAPS receiver front end.

### Multi-Stage Mitigation Solution Implemented (P-3)

**Stage 1 - Ground Station**: Mini-Circuits ZVBP-435-S+ bandpass filter inline with S0 ground station
- Sharply defined passband at 435 MHz with steep roll-off
- Attenuates out-of-band emissions before RF propagation

**Stage 2 - Signal Conditioning**: Mini-Circuits ZX60-14LN-S+ low-noise amplifier (LNA) on aircraft chassis
- Strengthens filtered signal path
- Compensates for insertion losses
- Maintains high signal-to-noise ratio

**Stage 3 - AVAPS Isolation**: Custom Lark Engineering filter (P/N 3C404-T6-3AA) integrated directly into AVAPS chassis
- Dedicated isolation barrier between AVAPS receiver and external telemetry signals
- Tuned to block residual harmonics from 430 MHz transmissions
- Preserves AVAPS sonde receive band sensitivity

### Results
- Successfully mitigated cross-system noise
- Simultaneous AVAPS and S0 operations achieved without interference or data degradation
- Full operational flexibility maintained

### Alternative Approaches for WC-130J

**Operational Deconfliction** (simplest):
- Time-separate AVAPS dropsonde releases from S0 telemetry windows
- Limited concurrent operation feasible but with measurable sonde receive quality degradation (elevated noise, intermittent packet loss)

**Frequency & Antenna Planning**:
- Retune Microhard P400 to alternate frequencies for improved RF deconfliction from AVAPS band
- Select antenna centered on chosen telemetry frequency
- Lower S0 TX power when link margin allows
- Maximize physical separation between telemetry and AVAPS cabling
- Use cross-polarization or pattern nulling if mechanically practical

**Replicate P-3 RF Stack** (recommended for full flexibility):
- In-chassis bandpass filter near radio
- Optional inline filter (e.g., ZVBP-435-S+) in ground station
- AVAPS chassis filter comparable to custom Lark unit
- Preserves operational flexibility while leveraging proven P-3 configuration
- Lowest certification risk

## Ground Station Details

### P-3 Configuration (1U Enclosure)
- **Power**: Aircraft 110 VAC 60 Hz bus with internal battery backup for brief interruptions
- **Front Panel**: Single power switch, status indicator LED, multi-function diagnostic LED, externally accessible USB drive for flight logs/telemetry
- **Rear Panel Connectivity**: GPS antenna, radio antenna, Ethernet ports
- **Networking**: AirOps integration via Ethernet; HDOB data uplink to NOAA networks; encrypted Wi-Fi module for wireless control
- **Control Interface**: Ruggedized Android tablet for command/control, telemetry monitoring, mission status
- **Operational Flexibility**: Supports monitoring and commanding from any P-3 cabin seat; enables future multi-UAS deployments
- **Ruggedization**: Vibration isolation mounts, shielded connectors, EMI compliance

### WC-130J Configuration (Portable)
- **Power**: Internal rechargeable battery system (8-hour continuous operation capability)
- **Charging**: Standard AC input during preflight staging
- **Battery Management**: Integrated circuitry with automatic switchover and over-discharge/thermal protection
- **Installation**: Mounts to removable interior panel near paratroop-door freefall chute
- **Antenna Connection**: Single coaxial cable to removable panel-mounted antenna; impedance and gain profile matches P-3 430 MHz configuration
- **Filtering**: Can incorporate Mini-Circuits ZVBP-435-S+ bandpass filter inline for source-level RF isolation
- **Interoperability**: Same electrical and communication standards as P-3 system
- **Configuration Flexibility**: Rapid installation/removal between missions without permanent aircraft modifications

## Situational Awareness Integration

### AirOps Network Integration
- S0 ground station fully integrated with NOAA AirOps via IWG1 data protocol ("IWG strings")
- **Ingestion**: Subscribes to existing IWG multicast feed within P-3 cabin network
- **Broadcasting**: Transmits standardized aircraft state information including GPS position, pressure altitude, true airspeed, heading, time-synchronized environmental data
- **Data Synchronization**: Aligns S0 telemetry with aircraft flight and mission parameters for accurate georeferencing and timestamping
- **HDOB Compatibility**: Automatic generation and uplink of HDOB-formatted messages
- **Operational Benefit**: Mission directors and flight scientists obtain unified view of aircraft and UAS operations; S0 position, health, and sampling data appear alongside other NOAA airborne instruments
- **Coordination Advantage**: Improves coordination, situational awareness, and real-time decision-making during multi-platform missions

## Deployment Procedures

### Standard Launch Sequence (Timeline)
- **T-2 minutes**: Aircraft transitions to target altitude, maintains level unaccelerated flight
- **T-60 seconds**: 
  - Cabin depressurized around freefall chute
  - Chute door status verified
  - Safety cap removed
  - S0 canister inserted into fiberglass sleeve
  - Physical seating confirmed
- **T-10 seconds**: System transitions from standby to armed mode
- **T-0**: Crew command "drop drop drop" initiates release
- **Release to Parachute Deployment**: <0.5 seconds
- **Descent & Stabilization**: 10-12 seconds
- **Sensor Confirmation & Wing Deployment**: Onboard sensors confirm stable orientation, trigger parachute release and wing deployment
- **Transition to Powered Flight**: Autonomous
- **Total Sequence**: Less than 30 seconds from arming to stable powered flight

### Crew Coordination
- Flight Director (FD): Altitude callouts, countdown, launch command
- Pilot (P): Depressurization, cabin preparation, chute door verification, launch area clearance
- Navigator (NAV): GO call verification
- AVAPS Operator (AVAPS): S0 physical preparation, safety cap removal, canister seating, arming verification, launch execution
- S0 Operator/Mission Specialist (AVO): Mission configuration, telemetry verification, lost-comms waypoints