# UAS Airborne Communications Extension for Emergency Response and Remote Field Operations

## Document Metadata
- **Type:** White Paper / Capability Proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- **Program/Solicitation:** NOAA IDIQ (1305M226D0012); SBIR Phase III eligibility noted (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); NOAA Broad Agency Announcement (open through 30 September 2026)
- **Date:** August 17, 2026
- **BST Products/Systems Referenced:** S3 VTOL UAS, S2 UAS, SwiftCore Flight Management System, SwiftPilot, SwiftTab, ground-station software, fleet-management software
- **Key Personnel:** Cory Dixon (last editor)

## Executive Summary

BST proposes to deploy a mission-selected airborne communications relay or access payload aboard two S3 VTOL aircraft to restore voice and data connectivity for NOAA and interagency responders when terrestrial infrastructure is damaged, congested, blocked by terrain, or disrupted by disaster. One S3 would maintain orbit over the operational area while a second aircraft provides relief, backup, and sustained operations. The effort combines systems definition, architecture trade study, payload integration, ground and flight verification, and operationally representative demonstration to deliver a rapidly deployable capability that extends reach and reduces dependence on ground infrastructure.

## Technical Approach

**System Definition and Architecture Selection:**
- Characterize supported users, devices, coverage area, flight authorization, environmental conditions, and success metrics with NOAA/interagency stakeholders
- Compare candidate architectures: VHF relay, MANET (Mobile Ad Hoc Network), MANET with TAK (Team Awareness Kit) or other common operating picture, satellite-backed or hybrid relay, airborne cellular (4G/5G), and Government-furnished-radio alternatives
- Trade against user interoperability, coverage, service quality, payload size-weight-power (SWaP), backhaul requirements, spectrum/FCC dependencies, cybersecurity, COMSEC/encryption, acquisition availability, and sustainment
- Conduct design concept review before detailed integration

**Payload Integration:**
- Procure and integrate selected payload (radio/relay system), antennas, power conversion, cooling, cabling, network management, payload health/status monitoring, and ground controls on two S3 systems
- Address RF isolation and electromagnetic compatibility (EMC) between payload, navigation sensors, avionics, independent aircraft command-and-control link, and other equipment
- Complete integration and safety review before flight

**Verification Approach:**
- Bench and ground network verification: test connectivity, coverage at controlled ranges, throughput/latency or voice intelligibility, encryption/authentication, payload power/thermal behavior, EMI/EMC, backhaul degradation, payload restart, loss-of-link independence, data logging, and emergency procedures
- Progressive flight testing over Customer-approved terrain; operationally representative demonstration
- Map coverage; measure service quality, payload and aircraft endurance, setup time, user connectivity, environmental effects
- Demonstrate aircraft relief/rotation and document service interruption, reconnection, or handoff behavior

**Operational Architecture:**
Three logical segments:
1. **User-access segment:** Connects field radios or data devices to S3 payload using selected waveform
2. **Airborne processing and relay segment:** Receives, routes, repeats, or gateways traffic; reports payload health, power state, temperature, network status to operator
3. **Backhaul and enterprise segment:** Transfers traffic to incident command post, Customer server, common operating picture, or approved satellite/terrestrial network (as required by mission)

**Aircraft and Payload Integration:**
- Treat S3 and payload as one RF and energy system
- Select antenna locations and operating frequencies to provide required field coverage while controlling coupling with navigation sensors, avionics, other radios, and aircraft command link
- Choose orbit altitude/geometry to balance line of sight, terrain masking, coverage footprint, interference, regulatory limits, energy use, and link budgets
- Separate mission payload from aircraft flight-safety systems: payload can be powered, monitored, restarted, or isolated without disrupting flight-critical functions

**Aircraft Rotation Concept:**
- First S3 launches vertically from austere site, transitions to fixed-wing flight, establishes approved orbit, begins service
- Monitor coverage, throughput/latency or voice quality, payload power/temperature, aircraft energy state, link health throughout mission
- Second S3 launches when first aircraft approaches recovery limit, establishes service before first returns for vertical recovery
- Characterize service interruption, reconnection, or handoff during rotation (does not assume seamless continuity)

## Products & Capabilities Described

### S3 VTOL UAS
- **What it is:** Vertical takeoff-and-landing unmanned aircraft with fixed-wing efficiency
- **Key specifications:**
  - 2.7 kg payload capacity
  - Up to 110 minutes flight time
  - 110 km maximum range
  - 20,000 ft MSL ceiling
  - 30-knot wind resistance
  - Payload mass, balance, electrical, thermal, and aerodynamic constraints to be managed for communications mission
- **Use in this proposal:** Primary platform for airborne relay; launches and recovers vertically without runway; transitions to efficient fixed-wing orbit; communications payload size, antenna installation, and orbit duration optimized for relay endurance
- **Advantages cited:** Combines VTOL with range and endurance of fixed-wing; can operate from austere staging sites; enables rapid positioning and repositioning as incident changes

### S2 UAS
- **What it is:** Predecessor to S3; established platform with deep payload-integration heritage
- **Use:** Historical reference for payload-integration experience
- **Heritage:** Has carried radiometers, electro-optical/thermal imagers, atmospheric probes, trace-gas instruments, aerosol sensors in Arctic, high-altitude, volcanic, and wildfire environments for NASA and NOAA

### SwiftCore Flight Management System
- **What it is:** Autonomous mission-execution, aircraft command-and-control, and third-party payload-interface platform developed and integrated by BST
- **Key functions:**
  - Autonomous mission execution
  - Real-time telemetry and control
  - Onboard data handling
  - Third-party payload interfaces
  - Aircraft command-and-control link (independent from mission payload)
  - Payload status, orbit commands, power state, link health, aircraft condition visibility
- **Use in this proposal:** Manages aircraft flight safety, navigation, telemetry, recovery; maintains separation between mission payload and flight-critical functions; enables payload to be powered, monitored, restarted, or isolated without disrupting flight safety

### SwiftPilot, SwiftTab, Ground-Station Software
- Referenced as pre-existing proprietary BST systems that may be incorporated into deliverables; specific details not provided in proposal

## Use Cases & Applications

**Primary Emergency Response Missions:**
- Hurricane operations (personnel coordination, observations, imagery, warnings, logistics)
- Wildfire response (FEMA, state/local emergency managers, firefighters coordination)
- Oil spills (data, operational support, observations)
- Severe weather (warnings, observations, common operating picture)
- Search-and-rescue operations

**Communications Failure Scenarios Addressed:**
- Terrestrial infrastructure damaged or without power
- Public cellular networks congested
- Mountainous or forested terrain blocking line-of-sight links
- Satellite service unavailable, capacity-limited, or unsuitable for all users
- Specialized radios unable to serve public carrying standard devices
- Ground-deployed equipment constrained by access, terrain, damaged roads, or time to position

**Supported User Types:**
- NOAA field teams (aircraft, vessels, field sites, incident command posts, remote observing locations)
- FEMA personnel
- State and local emergency managers
- Firefighters
- Search-and-rescue personnel
- Interagency responders
- Members of public (cellular-device users)

**Service Objectives:**
- Personnel coordination
- Command and control
- Observations and data exchange
- Imagery and warnings
- Logistics
- Common operating picture updates
- Voice and data connectivity in remote or disrupted areas

## Deliverables

**Data Deliverables (Table 1 referenced but not detailed):**
- System definition and trade study report
- Design concept review documentation
- Integration and safety review documentation
- Bench and ground network verification test data
- Flight coverage maps
- Service quality measurements (throughput, latency, voice intelligibility)
- Payload and aircraft endurance data
- Environmental effect analysis
- After-action review with flight, payload, network, and video data
- Spectrum and regulatory findings
- Cybersecurity architecture documentation
- Operating and emergency procedures
- Training materials
- Maintenance and support assumptions
- Transition package with recommendations for broader NOAA/interagency deployment

**Hardware Deliverables (Table 2 referenced but not detailed):**
- Two S3 VTOL systems configured with selected communications payload
- Associated ground equipment
- Network management equipment

## Optional Enhancements

**Option 1 — Second Communications Mode (6 months):**
- Add second nonduplicative communications service to base configuration
- Complete interface updates, bench and flight testing, user-device verification
- Provide operational recommendation on independent, concurrent, or gateway operation

**Option 2 — TAK or Customer Common-Operating-Picture Integration (5 months):**
- Integrate authorized position, message, sensor, or incident-data exchange with Government-furnished TAK environment or designated server
- Verify identity, access, data routing, latency, loss-of-backhaul behavior, representative user workflows
- Exercise only if base architecture does not already include interface

**Option 3 — Airborne 4G/5G Feasibility and Demonstration (up to 12 months):**
- Define intended users, devices, licensed band, participating carrier/authorized network operator
- Define network-core approach, subscriber approach, backhaul, interference controls, cybersecurity, spectrum authority, operating restrictions
- Conduct feasibility review and seek Customer written go decision
- Integrate and demonstrate cellular payload
- Note: Universal public service and carrier interconnection not promised

## Key Results

**Not a report with results.** This is a proposal for work to be performed. No experimental results, field data, or validation outcomes are provided. Document explicitly notes (Figure 1 caption) that "The evidence supports the development method and reduces execution risk; it does not imply that the proposed communications relay is already integrated or qualified."

## Timing and Resource Requirements

**Period of Performance:**
- Base effort: 12 months after receipt of order, required interface information, and any Government-furnished equipment
- Option 1: 6 months after base architecture stable
- Option 2: 5 months after base architecture stable
- Option 3: Up to 12 months after exercise
- Schedule dependent on: timely downselect, spectrum authority, COMSEC/keying receipt, airspace/flight approvals, cybersecurity decisions, carrier involvement, test-range support, weather, equipment availability

**Government-Furnished Resources Required:**
- Mission ownership identification and representative users
- Test area designation
- User radios, devices, and communications requirements
- Backhaul access and requirements
- Spectrum authority and frequencies
- TAK or other server access (if applicable)
- COMSEC and keying when required
- Cybersecurity officials and reviews
- Flight and airspace approvals
- Test-range support
- Network/backhaul access
- Operational participants
- Carrier involvement (for cellular option)
- Any Government-furnished equipment

## Notable Details

**Vertical Integration and Risk Reduction:**
- BST develops aircraft, avionics, flight-control system, payload interfaces, user interfaces, and ground stations in-house (U.S.-based)
- Vertical integration critical for relay aircraft: payload status, orbit commands, power state, link health, and aircraft condition must be visible without compromising independent command-and-control link
- S2 heritage demonstrates ability to integrate specialized payloads and deploy outside conventional test ranges (Arctic, high-altitude, volcanic, wildfire environments for NASA and NOAA)

**Intellectual Property and Licensing:**
- Deliverables incorporate pre-existing BST proprietary systems: airframes, SwiftCore, SwiftPilot, SwiftTab, ground-station software, fleet-management software, simulation assets, operator-interface software, alert-management logic, fleet-orchestration methods, atmospheric wind-estimation, autonomy functions, interfaces, models, manufacturing know-how
- Data rights in software, designs, algorithms, technical data, and improvements to be defined in agreement
- Third-party radio, TAK component, carrier system, and encryption rights subject to their applicable licenses
- No third-party source-code rights assumed

**Acquisition Pathways:**
- Existing NOAA IDIQ vehicle available: 1305M226D0012