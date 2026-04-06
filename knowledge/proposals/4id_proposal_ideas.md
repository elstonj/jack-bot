# 4ID Proposal Ideas

## Document Metadata
- Type: Internal proposal/brainstorm document
- Client/Agency: U.S. Army (4th Infantry Division)
- Program/Solicitation: 4ID Autonomous Systems Experiment
- Date: Created 2025-09-02; Modified 2025-09-05
- BST Products/Systems Referenced: S0 VTOL, S3
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
Black Swift Technologies outlined two proposal concepts for 4th Infantry Division involving UAS-mounted electromagnetic spectrum (EMS) sensing capabilities: (1) airborne collection and analysis of enemy EM signatures for intelligence and force protection, and (2) company-level electronic patrol using multi-UAS RF detection and collaborative localization to identify infiltrating aircraft and ground-based radio emitters.

## Technical Approach

### Proposal 1: UAS-Mounted EMS Analysis
- **Core Concept**: Single UAS equipped with wideband RF receiver conducts extended surveillance of known enemy positions
- **Data Collection**: Collects wideband RF data over time and across different times of day; data recorded in flight and analyzed post-processing
- **Operational Mode**: Low-/no-comm operation with GPS-jamming/spoofing resilience
- **Analysis Goals**: Extract EM signatures to identify unit type, specific unit ID, location, physical arrangement, and current activities
- **Dual-Use Applications**: Enemy intelligence for operations planning; friendly unit characterization for force protection and decoy development

### Proposal 2: Company-level Electronic Patrol
- **Core Concept**: Multiple UAS with wideband RF receivers conduct collaborative patrol using signal detection, classification, and source localization
- **Collaborative Detection**: When one aircraft detects and classifies a signal of concern, a second aircraft is cued to approach and fly a complementary pattern to localize the signal source
- **Network Integration**: Target information (type, location, signal band, signal strength) transmitted over tactical data network
- **Search Strategy**: Area coverage ~100 sq km per aircraft at 40 knots, 500' AGL

## Products & Capabilities Described

### S0 VTOL
- **Use in Context**: Proposed as primary platform for Proposal 2 (2× S0 VTOL for collaborative patrol)
- **Specifications**:
  - Weight: < 20 lbs
  - Payload Capacity: > 3.5 lbs
  - Cruise Speed: > 40 knots
  - Dash Speed: > 80 knots
  - Endurance: > 2 hours
  - Wingspan: < 7 ft

### S3
- **Use in Context**: Alternative platform for Proposal 1 (single-aircraft EMS collection)
- **Specifications**: Same as S0 VTOL (meets identical requirements)

### RF Payload (Unspecified)
- Wideband receiver capability (frequency range: X kHz to Y GHz—specific range not filled in)
- Antenna integration
- Signal processing and classification capability
- Onboard or post-processing analysis capability

## Use Cases & Applications

1. **Enemy Unit Intelligence Gathering**
   - Pattern-of-life EM intelligence collection on enemy military formations
   - Unit type identification
   - Specific unit ID and location determination
   - Physical arrangement characterization
   - Current activity assessment

2. **Force Protection**
   - Friendly unit EM characterization for defensive measures
   - Decoy operation development

3. **Area Security/Intrusion Detection**
   - Company or Battalion-level area of operations monitoring (~100 sq km)
   - Detection and localization of infiltrating aircraft and ground units
   - Target systems: Ground-based radios (squad comms, WiFi, Bluetooth) and aircraft-based radios (drone control/telemetry, VHF/UHF)

## Tactical/Organizational Placement
- Proposal 1: Battalion through Division level
- Proposal 2: Battalion or Company level

## Requirements Summary

### Common Aircraft Requirements (Both Proposals)
- Weight: < 20 lbs
- Payload: > 3.5 lbs
- Cruise Speed: > 40 knots
- Dash Speed: > 80 knots
- Endurance: > 2 hours
- Wingspan: < 7 ft

### Proposal 1 Specific Requirements
- Wideband RF receiver
- NGC2 network integration (discovery, broadcasting, meshing, tasking)
- Hardened radio (256-bit encryption, frequency hopping/shifting)
- Low-/no-comm operation capability
- GPS-denied navigation

### Proposal 2 Specific Sensor Requirements
- Line of bearing to RF source (20-second emission window)
- RF source localization via flight pattern (20-second emission window)
- RF source classification (e.g., "DJI drone," "FRS radio")
- Ability to close distance to weak RF sources
- Collaborative multi-UAS source localization

### Proposal 2 Specific Network Requirements
- NGC2 integration (discovery, broadcasting, meshing, tasking)
- Hardened radio (256-bit encryption, frequency hopping/shifting)
- GPS-denied return-to-base (RTB)

## Notable Details

### Assessment Notes
- **Proposal 1**: Marked as Unique Capability = High, Operational Impact = Med/High, Feasibility = Low (noted concerns: time to research/integrate, area of expertise)
- **Proposal 2**: Referenced need for "full list of labels" for RF source classification

### Talking Points
- Intuitive drone platform
- Electronic warfare capabilities executed at company level
- Discoverable and reporting node on NGC2 network

### Status
Document location indicates this project is in "Completed/Inactive/Unsubmitted Projects," suggesting these proposals were not pursued or were shelved.