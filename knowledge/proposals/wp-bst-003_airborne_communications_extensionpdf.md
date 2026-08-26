# UAS Airborne Communications Extension for Emergency Response and Remote Field Operations

## Document Metadata
- Type: White paper / capability proposal
- Client/Agency: NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- Program/Solicitation: NOAA IDIQ vehicle (1305M226D0012); SBIR Phase III pathway (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); NOAA Broad Agency Announcement (open through 30 September 2026)
- Date: August 17, 2026
- BST Products/Systems Referenced: S3 VTOL UAS, S2, SwiftCore Flight Management System, SwiftPilot, SwiftTab
- Key Personnel: Cory Dixon (last editor)

## Executive Summary
Black Swift Technologies proposes to integrate a mission-selected communications relay or access payload aboard two S3 VTOL aircraft to provide rapidly deployable airborne communications capability for NOAA field teams and emergency responders. One aircraft would maintain orbit over the supported area while a second provides relief, backup, and sustained operations. The effort includes systems definition, architecture selection, integration, ground and flight verification, and transition documentation to restore communications in remote or disaster-disrupted areas where terrestrial infrastructure is damaged, congested, blocked by terrain, or absent.

## Technical Approach

**Architecture Selection Process:**
- Customer and BST conduct joint systems definition and trade study comparing candidate approaches: VHF relay, mobile ad hoc networks (MANET), satellite-backed or hybrid relay, cellular, and Government-furnished-radio alternatives
- Trade study evaluates: user interoperability, coverage, service quality, payload size/weight/power (SWaP), backhaul availability, spectrum dependencies, FCC and carrier requirements, cybersecurity, encryption/COMSEC, keying, acquisition, and sustainment
- Formal downselect leads to detailed integration

**Integration & Verification:**
- Selected payload sets, antennas, power conversion, cooling, cabling, and network management integrated on two S3 systems
- RF isolation and electromagnetic compatibility (EMC) verified between payload, navigation sensors, avionics, aircraft command-and-control link, and other equipment
- Bench and ground network verification tests: connectivity, coverage at controlled ranges, throughput and latency or voice intelligibility, encryption/authentication, payload power and thermal behavior, EMI/EMC, backhaul degradation, payload restart independence, loss-of-link behavior
- Progressive flight testing over operationally representative terrain with two-aircraft rotation demonstration

**System Separation:**
- Communications payload operates as modular mission payload carried by S3
- SwiftCore and aircraft command-and-control link remain responsible for flight safety, navigation, telemetry, and recovery
- This separation keeps mission traffic independent from flight-critical functions; payload can be powered, monitored, restarted, or isolated without disrupting flight operations

**Technical Integration Considerations:**
- Aircraft and payload treated as one RF and energy system
- Radio, antenna, mount, cable, power-conversion, cooling, and network components configured within S3 mass, balance, electrical, thermal, and aerodynamic constraints
- Antenna locations and operating frequencies selected to provide required field coverage while controlling coupling with navigation sensors, avionics, other radios, and command link
- Orbit altitude and geometry chosen to balance line-of-sight, terrain masking, coverage footprint, interference, regulatory limits, energy use, and link budgets
- Service interruption, reconnection, or handoff behavior characterized rather than assuming seamless continuity

## Products & Capabilities Described

**S3 VTOL UAS:**
- Vertical takeoff and landing capability (no runway required)
- Transitions to efficient fixed-wing flight
- **Specifications:**
  - 2.7 kg (6 lb) payload capacity
  - Up to 110 minutes maximum flight time
  - 110 km maximum range
  - 20,000 ft MSL ceiling
  - 30-knot wind resistance
  - Actual communications mission envelope to be established for integrated configuration
- Preferred for communications mission due to payload size/antenna installation capability, orbit duration, and austere-site launch/recovery
- Deep payload-integration heritage: has supported radiometers, electro-optical and thermal imagers, atmospheric probes, trace-gas instruments, aerosol sensors

**S2 (Predecessor):**
- Has carried varied scientific payloads for NASA and NOAA
- Demonstrated operations in Arctic, high-altitude, volcanic, and wildfire-related environments
- Establishes integration and deployment heritage relevant to S3

**SwiftCore Flight Management System:**
- Provides autonomous mission execution, aircraft command and monitoring, interfaces for third-party payloads
- Delivers real-time telemetry and control, onboard data handling
- Vertical integration with aircraft enables visibility of payload status, orbit commands, power state, link health, and aircraft condition without compromising independent command-and-control link
- Enables payload monitoring and control independent of flight-critical functions

**Ground Station & Support Software:**
- Includes SwiftPilot (pilot interface), SwiftTab (operator interface)
- Centralized fleet-management software
- Ground-control and network-management equipment
- Payload health/status monitoring
- Authorized server or backhaul interfaces

## Use Cases & Applications

**Primary Mission:**
Emergency response and remote field operations where terrestrial communications are damaged, disrupted, congested, or blocked by terrain.

**Supported Scenarios:**
- Hurricanes, wildfires, oil spills, severe weather, and other emergencies
- Operations supporting NOAA, FEMA, state and local emergency managers, firefighters, search-and-rescue personnel, and interagency users
- Personnel coordination, command and control, observations, imagery, warnings, logistics, and common-operating-picture updates

**User Groups & Services:**
- Firefighters (VHF land-mobile radio dependency)
- Customer field teams (MANET data and common operating picture connectivity)
- Remote field personnel (hybrid radio and satellite backhaul)
- General public (ordinary cellular devices)
- Interagency responders and incident command posts

**Coverage:**
- Rapidly repositionable airborne node raises communications line-of-sight
- Can reposition as incident changes
- Supports austere staging locations without runway dependency

## Base Scope & Deliverables

**Task 1 — System Definition and Trade Study** (Due ARO + 3 months)
- Define primary NOAA/interagency mission, supported users and devices, coverage area, flight authorization, environmental conditions, measurable success criteria
- Characterize S3 payload constraints (mass, volume, power, cooling, antenna, electromagnetic, ground-interface)
- Compare candidate approaches against user interoperability, coverage, service quality, payload SWaP, backhaul, spectrum, FCC/carrier dependencies, cybersecurity, encryption/COMSEC, keying, acquisition, sustainment
- Deliver system definition, recommended base architecture, design concept review

**Task 2 — Selected-Payload Integration** (Due ARO + 6 months)
- Procure and integrate selected payload sets, antennas, power conversion, cooling, cabling, network management, payload health/status monitoring, ground controls, authorized server/backhaul interfaces on two S3 systems
- Address RF isolation and EMC between payload, navigation sensors, avionics, aircraft command link, other equipment
- Complete integration and safety review before flight

**Task 3 — Bench and Ground Network Verification** (Due ARO + 8 months)
- Verify radio and network performance using representative devices
- Test connectivity, coverage at controlled ranges, throughput/latency or voice intelligibility, encryption/authentication, payload power/thermal behavior, EMI/EMC, backhaul degradation/loss, payload restart, aircraft loss-of-link independence, data logging, emergency procedures

**Task 4 — Flight Coverage and Persistence Demonstration** (Due ARO + 11 months)
- Progressive flight testing and operationally representative demonstration over Customer-approved terrain
- Map coverage; measure service quality, payload and aircraft endurance, setup time, user connectivity, environmental effects
- Demonstrate relief by second aircraft
- Record service interruption, reconnection, handoff behavior during rotation
- Provide flight, payload, network, and video data with after-action review

**Task 5 — Transition Package** (Due ARO + 12 months)
- Deliver validated configuration, interface information, test data, coverage maps, spectrum and regulatory findings, cybersecurity architecture, operating and emergency procedures, training, maintenance and support assumptions, deployment recommendations

**Hardware Deliverables:**
- 2x S3 systems configured for selected relay architecture (Customer title)
- 2x Selected communications payload sets and installed antennas (Customer title unless Customer-furnished)
- 1 set ground-control, network-management, charging, cases, support equipment (Customer title)

**Option Tasks:**
- **Option 1 (Task 7)** — Second Communications Mode: Add nonduplicative service; update interfaces, conduct bench and flight testing, verify user-device compatibility, provide operational recommendation on independent/concurrent/gateway operation (Est. 6 months, $0.25M)
- **Option 2 (Task 8)** — TAK or Customer COP Integration: Integrate authorized position, message, sensor, incident-data exchange with Government-furnished TAK environment or designated server; verify identity, access, data routing, latency, loss-of-backhaul behavior, user workflows (Est. 5 months, $0.20M)
- **Option 3 (Task 9)** — Airborne 4G/5G Feasibility and Demonstration: Define intended users/devices, licensed band, carrier/network operator, network-core/subscriber approach, backhaul, interference controls, cybersecurity, spectrum authority; conduct feasibility review; if approved, integrate and demonstrate cellular payload (Est. 12 months, $0.20M)

## Rough Order of Magnitude (ROM) Estimate

| Scope | Estimate |
|-------|----------|
| Base — Selected airborne communications architecture (12 months / 2 S3 systems / 2 payload sets / 1 representative demo) | $0.90M |
| Option 1 — Second communications mode | $0.25M |
| Option 2 — TAK or Customer COP integration | $0.20M |
| Option 3 — Airborne 4G/5G Feasibility gate, conditional integration, and demonstration | $0.20M |
| **Maximum potential value (Base plus all options)** | **$1.55M** |

Note: Third-party radio, carrier, COMSEC, spectrum, server, and range costs may require adjustment after architecture downselect.

## Notable Details

**Risk Reduction & Heritage:**
- BST develops aircraft, avionics, flight-control systems, payload interfaces, user interfaces, and ground stations in the United States (vertical integration)
- S3 payload-integration heritage includes radiometers, electro-optical/thermal imagers, atmospheric probes, trace-gas instruments, aerosol sensors
- S2 predecessor deployed in Arctic, high-altitude, volcanic, and wildfire environments for NASA and NOAA, demonstrating ability to integrate specialized payloads and deploy outside conventional test ranges

**Operational Concept Highlights:**
- Customer designates operating area, supported users, service objective, approved devices, available backhaul, spectrum, security conditions, and flight constraints
- Two-aircraft rotation supports continuous service: first aircraft orbits while second provides relief, backup, and rotation capability
- Separation of mission payload from flight-critical functions ensures payload issues do not compromise aircraft safety or control

**Government-Furnished Requirements:**
- Mission owner, representative users, test area, devices, communications and backhaul requirements, frequencies, success priorities
- Spectrum authority, user radios and devices, TAK or server access, COMSEC and keying
- Cybersecurity officials, flight and airspace approvals, test-range support, network/backhaul access
- Operational participants and carrier involvement (for cellular option)
- Timely downselect, safety, spectrum, cyber, and option decisions required to maintain schedule

**Intellectual Property:**
- Deliverables may incorporate BST pre-existing proprietary assets: airframes, SwiftCore, SwiftPilot, SwiftTab, ground-station software, centralized fleet-management software, simulation assets, operator-interface software, alert-management logic, fleet-orchestration methods, atmospheric wind-estimation methods, autonomy functions, interfaces, models, manufacturing know-how
- Data rights in software, designs, algorithms, technical data, improvements to be defined in agreement
- Third-party radio, TAK, carrier, encryption, and Government-furnished equipment remain subject to applicable licenses; no third-party source-code rights assumed

**Acquisition Pathway:**
- SBIR Phase III sole-source award eligible via 15 U.S.C. § 638(r) based on existing SBIR data rights lineage (S0 program)
- Existing