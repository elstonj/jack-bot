# UAS Airborne Communications Extension for Emergency Response and Remote Field Operations

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- **Program/Solicitation:** Not specified (proposed as pilot or new solicitation pathway)
- **Date:** May 21, 2026
- **BST Products/Systems Referenced:** S3 VTOL UAS, S2 (predecessor), SwiftCore Flight Management System, SwiftPilot, SwiftTab, SwiftStation
- **Key Personnel:** Beck Cotter (last editor, August 2026)

## Executive Summary
Black Swift Technologies proposes to configure two S3 VTOL aircraft as rapidly deployable airborne communications relay nodes for NOAA emergency response and remote field operations. The effort would define a mission-specific communications architecture (selecting from VHF relay, MANET, satellite-backed hybrid, or cellular options), integrate the selected payload on two S3 systems, and validate coverage, service quality, endurance, and aircraft rotation through operationally representative testing. The solution addresses communications gaps when terrestrial infrastructure is damaged, congested, terrain-blocked, or absent during disasters and remote operations.

## Technical Approach

**System Architecture (Three Segments):**
1. **User-Access Segment:** Connects field radios or data devices to S3 payload using selected waveform
2. **Airborne Processing & Relay Segment:** Receives, routes, repeats, or gateways traffic; reports payload health, power, temperature, network status
3. **Backhaul & Enterprise Segment:** Optional transfer to incident command post, servers, common operating picture, or satellite/terrestrial networks

**Key Technical Decisions:**
- Payload and aircraft treated as integrated RF and energy system (antenna placement, power conversion, cooling, EMC compatibility)
- Orbit altitude/geometry optimized for line-of-sight, terrain masking, coverage footprint, interference, and link budgets
- Explicit degraded-mode behavior: loss of backhaul does not terminate local relay; payload faults trigger controlled restart or isolation; loss of aircraft command link invokes SwiftCore contingency behavior
- Independent aircraft command-and-control link kept separate from mission traffic to preserve flight safety
- Two-aircraft rotation model: one on-orbit, second provides relief, backup, and sustained operations

**Integration Approach:**
- Modular mission payload using SwiftCore Flight Management System interfaces
- Standardized mechanical, power, and data interface (heritage from S2 scientific payload integration)
- Ground controls expose only mission-necessary status and operator functions
- RF isolation and EMC verification between payload, navigation sensors, avionics, command link, and other equipment

## Products & Capabilities Described

### S3 VTOL UAS
- **What it is:** Vertical-takeoff-and-landing platform with fixed-wing efficiency; BST's longer-range, higher-payload mission aircraft
- **Published Specifications:**
  - Payload capacity: 2.7 kg (6 lb)
  - Maximum flight time: up to 110 minutes
  - Maximum range: 110 km
  - Ceiling: 20,000 ft MSL
  - Wind resistance: 30 knots
  - Launch/recovery: vertical without runway requirement
  - Transition: launches vertically, transitions to efficient fixed-wing flight
- **Proposed Use:** Carry mission-selected communications relay or access payload; one on-orbit, second for relief and backup
- **Actual Communications Mission Envelope:** To be established for integrated configuration (mass, balance, electrical, thermal, aerodynamic constraints)

### SwiftCore Flight Management System
- **What it is:** BST-developed avionics combining autonomous mission execution, aircraft command and monitoring, third-party payload interfaces
- **Capabilities:**
  - Real-time telemetry and control
  - Onboard data handling
  - Payload status visibility independent of command-and-control link
  - Autonomous mission execution
  - Loss-of-link contingency behavior
  - Payload power state management, restart, and isolation capabilities

### S2 (Predecessor Platform)
- **Payload Integration Heritage:** Carried radiometers, electro-optical and thermal imagers, atmospheric probes, trace-gas instruments, aerosol sensors
- **Deployment Experience:** Arctic, high-altitude, volcanic, and wildfire-related missions for NASA and NOAA
- **Standardized Interface:** Mechanical, power, and data interfaces enabling diverse payload integration

## Use Cases & Applications

**Primary Mission Context:**
- Emergency response during hurricanes, wildfires, oil spills, severe weather
- Remote field operations where terrestrial communications are absent, damaged, congested, or terrain-blocked
- Support to NOAA teams, FEMA, state/local emergency managers, firefighters, search-and-rescue personnel, interagency users

**Supported Communications Services (to be downselected):**
1. **VHF Relay** – Extension of land-mobile radio (e.g., firefighter coordination)
2. **MANET** – Mobile ad hoc network for interagency data connectivity
3. **MANET with TAK/COP** – Integration with Team Awareness Kit or common operating picture servers
4. **Satellite-Backed/Hybrid Relay** – Remote field personnel with hybrid radio and satellite backhaul
5. **Cellular Gateway** – 4G/5G service extension to ordinary cellular devices (Option 3, subject to carrier participation)
6. **Government-Furnished Radio** – Customer-specified radio systems

**Operational Scenarios:**
- Damaged or powered-down terrestrial infrastructure
- Congested public networks
- Mountainous or forested terrain blocking line-of-sight
- Satellite service unavailable or capacity-limited
- Geographic areas inaccessible to ground-based restoration equipment
- Heterogeneous user base (firefighters on VHF, teams on MANET, field personnel on hybrid, public on cellular)

## Base Scope & Tasking

**Task 1 — System Definition and Trade Study** (Due ARO + 3 months)
- Define NOAA/interagency mission, supported users, devices, traffic types, coverage area, duration, deployment time, terrain, orbit constraints, backhaul, frequencies, security, flight authorization, environmental conditions
- Characterize S3 constraints (mass, volume, power, cooling, antenna, EMC, ground interface)
- Compare VHF relay, MANET, MANET+TAK, satellite-backed, hybrid, cellular, and Government-furnished-radio alternatives against user interoperability, coverage, service quality, payload SWaP, backhaul, spectrum, FCC/carrier dependencies, cybersecurity, COMSEC/keying, acquisition, and sustainment
- Deliver system definition, architecture recommendation, design concept review

**Task 2 — Selected-Payload Integration** (Due ARO + 6 months)
- Procure and integrate selected payload sets, antennas, power conversion, cooling, cabling, network management, health/status monitoring, ground controls, backhaul interfaces on two S3 systems
- Address RF isolation and EMC between payload, navigation sensors, avionics, command link
- Complete integration and safety review before flight

**Task 3 — Bench and Ground Network Verification** (Due ARO + 8 months)
- Test connectivity, coverage at controlled ranges, throughput/latency/voice intelligibility, encryption/authentication, payload power and thermal behavior, EMI/EMC
- Test backhaul degradation/loss, payload restart, aircraft loss-of-link independence, data logging, emergency procedures
- Close critical discrepancies before flight-envelope expansion

**Task 4 — Flight Coverage and Persistence Demonstration** (Due ARO + 11 months)
- Progressive flight testing and one operationally representative demonstration over Customer-approved terrain
- Map coverage; measure service quality, payload and aircraft endurance, setup time, user connectivity, environmental effects
- Demonstrate relief by second aircraft; record service interruption, reconnection, handoff behavior during rotation
- Provide flight, payload, network, video data and after-action review

**Task 5 — Transition Package** (Due ARO + 12 months)
- Validated configuration, interface information, test data, coverage maps
- Spectrum and regulatory findings, cybersecurity architecture, operating/emergency procedures
- Training, maintenance and support assumptions, recommendations for broader deployment

## Optional Tasks

**Option 1 — Second Communications Mode** (6 months post-exercise)
- Add second nonduplicative waveform or service
- Interface updates, bench and flight testing, user-device verification
- Address independent, concurrent, or gateway operation

**Option 2 — TAK or Customer Common-Operating-Picture Integration** (5 months post-exercise)
- Integrate authorized position, message, sensor, incident-data exchange with Customer TAK or designated server
- Verify identity, access, data routing, latency, loss-of-backhaul behavior, user workflows
- Only if not already in base architecture

**Option 3 — Airborne 4G/5G Feasibility and Demonstration** (up to 12 months post-exercise)
- Define intended users, devices, licensed band, participating carrier or authorized operator
- Address network-core/subscriber approach, backhaul, interference controls, cybersecurity, spectrum authority, operating restrictions
- Feasibility review; if approved, integrate and demonstrate cellular payload
- **Caveat:** Universal public service and carrier interconnection not promised

## Hardware Deliverables

| Item | Scope | Configuration | Quantity | Due Date / Disposition |
|------|-------|---------------|----------|------------------------|
| 1 | Base | S3 systems configured for selected relay architecture | 2 | ARO + 11 mon.; Customer title |
| 2 | Base | Selected communications payload sets and installed antennas | 2 | ARO + 11 mon.; Customer title (unless furnished by Customer) |
| 3 | Base | Ground-control, network-management, charging, cases, support equipment | 1 set | ARO + 11 mon.; Customer title |
| 4 | Base | Development instrumentation and specialized RF/network test equipment | As required | Contractor-owned; not delivered unless separately identified |
| 5 | Options | Radio, server, network, or cellular equipment | TBD by option | At applicable option completion; disposition defined at exercise |

## Financial Estimate (ROM, Non-Binding)

| Scope | Scale | Estimate |
|-------|-------|----------|
| **Base** — Selected airborne communications architecture | 12 months / 2 S3 systems / 2 payload sets / 1 representative demo | **$0.90M** |
| **Option 1** — Second communications mode | One additional mode and representative testing | $0.25M |
| **Option 2** — TAK or Customer COP integration | One authorized server/interface and test event | $0.20M |
| **Option 3** — Airborne 4G/5G feasibility and demo | Feasibility gate, conditional integration, demonstration | $0.20M |
| **Maximum Potential Value** | Base plus all options | **$1.55M** |

**Cost Drivers for Re-estimation:**
- Government-furnished high-value radio
- Classified waveform
- Unusual spectrum requirement
- Permanent network infrastructure
- Extended operational deployment

## Key Results / Validation Approach

**Verification Pyramid** (Figure 1 in document):
- BST's aircraft, SwiftCore, and modular-payload experience inform a gated S3 integration and verification approach
- Heritage from S2 scientific payload deployments reduces execution risk
- Progressive flight testing from bench → ground network → flight coverage → operationally representative demonstration

**Service Quality Metrics to Be Demonstrated:**
- Coverage mapping and footprint
- Throughput and latency (for data modes) or voice intelligibility (for radio)
- Payload power consumption and thermal behavior
- Aircraft and communications endurance
- Setup time and deployment from austere staging
- User connectivity and ease of access
- Environmental effects (terrain, weather, interference)
- Service interruption, reconnection, and handoff behavior during aircraft rotation
- Failure modes and degraded-mode behavior (loss of backhaul, payload fault, loss of command link)

## Proposed Timeline & Resource Requirements

**Period of Performance:**
- Base effort: 12 months after receipt of order, interface information, and Government-furnished equipment
- Option 1: 6 months post-exercise
- Option 2: 5 months post-exercise
- Option 3: Up to 12 months post-exercise

**Critical Path Dependencies:**
- Timely Customer downselect of architecture
- NOAA identification of mission owner, representative users, test area
- Government-furnished spectrum authority, user devices, server/backhaul access
- COMSEC and keying when required
- Cybersecurity officials and safety reviews
- Flight and airspace approvals