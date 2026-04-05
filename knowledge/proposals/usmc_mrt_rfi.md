# USMC MRT RFI

## Document Metadata
- **Type:** Request for Information (RFI) with Response Template
- **Client/Agency:** U.S. Marine Corps (USMC); PEO (U&W), PMA-263
- **Program/Solicitation:** Marine Robotics Technology (MRT) UAS; Notice 243-26-024
- **Date:** April 13, 2026 (BST response submission date); RFI distributed prior
- **BST Products/Systems Referenced:** Black Swift S3 UAS
- **Key Personnel:** Jack Elston (BST contact)

---

## Executive Summary

The USMC PMA-263 issued an RFI seeking information on small Unmanned Aerial Systems (UAS) capable of supporting tactical Marine operations with specific emphasis on size, weight, endurance, autonomous operation in GNSS-denied environments, secure datalinks, and multi-payload integration. This document provides the detailed RFI parameters and response template that BST (and other vendors) were required to address, with a focus on the Black Swift S3 platform's capabilities against USMC requirements.

---

## Technical Approach & Key Requirements

### Air Vehicle Specifications (Required by USMC)
- **MGTOW (with payload):** < 20 lbs
- **Total System Weight:** < 75 lbs (including GCS, launch/recovery equipment, peripheral gear)
- **Payload Capacity:** > 3.75 lbs
- **Airspeed:** > 25 knots indicated airspeed (KIAS)
- **Endurance:** ≥ 2.5 hours (takeoff to landing)
- **Line-of-Sight Range:** ≥ 40 km
- **Propulsion:** Electric or hybrid-electric; non-petroleum-based (fuel cell, renewable preferred)
- **Launch/Recovery:** Vertical Takeoff and Landing (VTOL)
- **Wind Operating Limits:** Up to 25 KIAS
- **Precipitation Operating Limits:** Up to 0.75 inches/hour rainfall

### Communications & Security
- **Datalink Encryption:** AES 256-bit encryption using FIPS 140-3 validated cryptographic modules
- **Bandwidth Optimization:** Multiple frequency bands with fixed power output
- **Multi-INT Capability:** Simultaneous operation of multiple intelligence payloads
- **Network Compatibility:** TAK (Tactical Assault Kit) compatible; real-time ISR dissemination to USMC info systems
- **GNSS-Denied Operations:** Capability to operate without GPS using M-Code GPS, inertial navigation units (INU), computer vision, and/or visual-inertial odometry (VIO)

### Autonomy & Control
- **Flight Control:** Operator-in-the-loop (OITL) with semi-autonomous operation
- **Multi-AV Control:** Single GCS/operator capable of controlling two or more air vehicles
- **Personnel Requirements:** Maximum of two (2) operator/maintainer for deployment
- **GCS:** Man-portable, mobile, and network-enabled

### Baseline Payload
- **Configuration:** Dual-mode gimbaled EO/IR payload
  - EO: Ultra-High Definition (UHD)
  - IR: High Definition (HD)
  - Laser rangefinder
  - Laser designator

### Open Architecture & Growth
- **Payload Integration:** Open, modular architecture capable of supporting weapon payloads
- **Third-Party Integration:** Capability for integration of additional sensors and mission systems
- **Interoperability Standards:** STANAG 4586/4607/4609, ROS/ROS2, RAS-G IOP compatibility desired

### Technology Maturity
- **Required TRL:** 8 or higher (adequate maturity for immediate production, delivery, fielding, and deployment)

---

## Products & Capabilities Described

### Black Swift S3 UAS
- **Platform:** Electric VTOL tactical UAS
- **Application Context:** Proposed as a solution to USMC MRT RFI requirements for small tactical ISR platform
- **No specific performance claims** are quantified in this RFI document itself; this is a requirements/template document rather than a proposal with results

---

## RFI Response Structure (70+ Specific Questions)

The RFI requires respondents to address detailed technical questions organized in the following categories:

### Section 3A: System Characteristics & Performance Attributes (17 subsections)
1. **Size, Weight, Transportability** — MGTOW, system weight, transport packaging, case dimensions
2. **Launch, Recovery, Basing** — Supported methods, landing zone requirements, shipboard/maritime compatibility
3. **Propulsion and Power** — Power source(s), management approach, endurance tradeoffs
4. **Payload Capacity and Modularity** — Modular capability, multi-sensor support, simultaneous operations
5. **Sensor Capabilities** — EO, IR, LRF, LD; resolution; NIIRS performance; gimbal stabilization
6. **Command, Control, and Autonomy** — Autonomy modes, OITL/MITL, mission planning, multi-AV control
7. **Navigation and Guidance** — GNSS, M-Code GPS, inertial, vision-based; GNSS-denied performance
8. **Communications, Datalinks, and Networking** — Datalink types, encryption, spectrum agility, DDIL environment capability
9. **Ground Control Station (GCS)** — Portability, OS, interoperability, sensor/vehicle control, networked operation
10. **Mission Data Handling** — Data types, storage locations, security, integrity measures
11. **Performance Envelope** — Speed, endurance, range, altitude limits, operating envelope
12. **Environmental Operating Limits** — Temperature, wind, precipitation, saltwater tolerance, storage
13. **Acoustic and Signature Characteristics** — Noise, detectability
14. **Maintenance, Sustainment, and Logistics** — Operator-level maintenance, modular replacement, tooling, spare parts
15. **Manpower and Training** — Personnel requirements, training approach
16. **Software Assurance and Maturity** — SBOM, update approach, autonomy explainability, TRL
17. **Growth and Future Capability** — Open architecture, payload growth, integration roadmap

### Section 3B: Technical Approach, Implementation, and Operational Considerations (32 subsections)

**System Software and Navigation (3B.1–3B.6)**
- Operating systems (AV, companion computer, GCS); versions; SBOM availability
- Primary and backup PNT methods; GNSS constellation usage; sensor fusion
- GPS-denied navigation capability; visual-inertial odometry (VIO); SLAM performance; drift rates
- SAASM / M-Code GPS receiver details; keying/fill compatibility; timing holdover
- Flight modes supported (manual, assisted, waypoint, geofence, terrain-following, loiter, hover-and-stare, autonomous)
- Autonomy/AI functions; compute hardware; human-on/in-the-loop safeguards

**Launch, Recovery, and Safety (3B.7–3B.11)**
- Precision recovery capability; circular error probable (CEP) for landing accuracy
- Water landing capability; buoyancy; flotation time; corrosion protection; re-launch feasibility
- Launch/recovery equipment type, size, weight, power, setup/teardown time
- Safety features: lost link, lost GPS behaviors, return-to-home, auto-land, geofencing, flight termination, detect-and-avoid
- Personnel requirements for launch, recovery, ops, maintenance

**Mapping and Mission Planning (3B.12–3B.15)**
- Mapping software (Google, FalconView, open-source); DTED/DEM support; DoD standard mapping; disconnected ops
- GCS-AV datalink: waveform, frequency bands, bandwidth, encryption, anti-jam, autonomous mission execution capability
- Proprietary vs. standards-based waveform
- DoD COP / tactical network integration (TAK/ATAK, ROS/ROS2, RAS-G IOP, STANAG 4586/4609/4607)
- Multi-AV simultaneous control capability; bandwidth management; deconfliction

**Compliance and Security (3B.16–3B.23)**
- NDAA compliance (Sections 848, 889); TAA, BAA compliance; process documentation
- Mission data storage and protection; encryption at rest; access control; log integrity
- Interface Control Document (ICD) availability for avionics, payload, battery interfaces
- Payload inventory: EO/IR, SIGINT, LIDAR, comm relay, drop kits; TRL and availability dates
- Unique capabilities (deck ops, cold-weather kits, quiet propellers, confined-area VTOL)
- Third-party payload integration capability; successful past integrations
- Organic obstacle/threat detection and avoidance
- Swarm capability (current or in development); swarm size, comms, autonomy, heterogeneous platform compatibility

**Power and Endurance (3B.24–3B.25)**
- Battery rechargingmethod and time for maximum-endurance missions
- Battery certifications (UN 38.3, UL, NOSSA, S9310); thermal management; transport compliance

**Company Experience and Production (3B.26–3B.29)**
- Years of small UAS development experience; programs of record; airworthiness processes; production experience
- Units produced/fielded; customer base (USG, FMS, industry); operational hours
- Production lead times for 1–50, 51–100, 101–250, 251–500 units; supply chain constraints
- Maximum monthly production output under various capacity scenarios (1 line/1 shift through surge/overtime)

**Sustainment and Logistics (3B.30–3B.36)**
- Logistics support, spare parts, repair capability; sparing philosophy; turnaround times
- Field Service Representative (FSR) support for CONUS and OCONUS austere environments
- Personnel breakdown for launch, mission execution, recovery
- Operator qualification training time; syllabus/summary
- AV assembly time from field-packed state (2-person team)
- Field-level maintenance actions and estimated times
- Additive manufacturing (3D printing) feasibility for non-critical spares; example parts; technical/data-rights considerations

**Cost and Availability (3B.37–3B.42)**
- Full system composition (number of AVs, batteries, GCS, antennas, required gear)
- Unit cost per full system; CLIN-level cost breakdown; warranty terms
- Commercial availability; differences between commercial and government configurations
- CAGE code, UEI, NAICS business size, socio-economic categories (8(a), SDB, HUBZone, SDVOSB, WOSB)
- Foreign Ownership, Control, or Influence (FOCI); mitigation plans
- Government funding history (SBIR/STTR/OTA/BAA); data rights assertions
- Availability of operator/maintenance manuals, quick reference cards, training materials; formats; classification

**System Performance and Flight Envelope (3B.43–3B.46)**
- Max payload capacity, range, endurance, cruise speed, service ceiling, wind limits
- Precipitation and icing operating conditions
- Hybrid/ICE fuel type, consumption rates, hot-refuel capability
- Measured acoustic, RCS, and electromagnetic signatures

**Environmental & Regulatory Compliance (3B.47–3B.50)**
- Environmental qualifications (MIL-STD-810H, MIL-STD-461G, IP ratings)
- Shipboard and mobile vehicle operation; tested speeds, sea states, corrosion protection
- Airworthiness approvals (FAA Part 107 waivers, COAs, SORA levels)
- FAA Remote ID compliance; capability to disable Remote ID in denied areas when authorized

**Cybersecurity & Spectrum Assurance (3B.51–3B.53)**
- Cybersecurity posture: secure boot, code signing, STIG/CIS compliance, vulnerability disclosure program
- Lifecycle cybersecurity assessment and maintenance process
  - Vulnerability identification, disclosure, intake, triage, coordination
  - Patch development, validation, deployment (disconnected/austere environments)
  - Configuration management of fielded systems
  - Update cadence; operational impact considerations
- Spectrum authorizations (NTIA, FCC); multi-ship spectrum deconfliction

**Reliability, Maintainability, and Logistics (3B.54–3B.59)**
- Reliability and diagnostics: MTBF, BIT/