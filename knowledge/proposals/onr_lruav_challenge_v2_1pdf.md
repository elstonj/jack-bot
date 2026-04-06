# ONR Long-Range UAV Challenge v2

## Document Metadata
- Type: Solicitation / Challenge RFP
- Client/Agency: Office of Naval Research (ONR)
- Program/Solicitation: ONR Long-Range UAV (LRUAV) Challenge; awarded through One Nation Innovation OTA
- Date: 2025 (document created/modified August 2025)
- BST Products/Systems Referenced: None explicitly named (this is a solicitation document, not a BST proposal)
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
ONR is soliciting industry proposals to develop a long-endurance, low-cost unmanned aerial vehicle for distributed maritime operations and sea denial missions. The effort seeks a compact, attritable platform capable of persistent surveillance and targeting in contested maritime zones, to be delivered through five integrated prototyping phases culminating in 12 mission-ready systems plus technical documentation.

## Technical Requirements & Specifications

### Performance Targets (T) and Objectives (O)
- **Cost per unit:** T: $75,000 | O: $50,000 (excluding payloads)
- **Range:** T: 1,800 | O: 2,400 nautical miles
- **Payload capacity:** T: 15 | O: 30 lbs
- **Cruise speed:** T: 70 | O: 120 knots
- **Dash speed:** T: 110 | O: 150 knots
- **Max Takeoff Weight:** T: 120 | O: 100 lbs
- **Endurance:** Configurable for loiter, sprint, or extended range/duration missions
- **Deployment:** Flexible launch and recovery from distributed locations

### Avionics & Architecture Requirements
- **Flight control:** ArduPilot-based
- **Avionics architecture:** Modular, open architecture frameworks (FACE, OMS compliance)
- **Payload interfaces:** Standard electrical, mechanical, and data interfaces; tool-less payload swaps
- **Communications:** Mesh networking radios, software-defined radios, satcom capability; AES-256 or better encryption
- **Compliance:** NDAA-compliant components; full ICDs required; cybersecurity documentation mandatory

## Five-Phase Development Approach

1. **System Conceptualization and Architecture** – Define operational requirements, architecture, and CONOPS with government labs
2. **Platform Realization** – Design, fabricate, and integrate 3 prototype UAVs meeting all thresholds
3. **Mission Enablement** – Integrate payloads, comms systems, and fully operational Ground Control Station
4. **Test and Experimentation** – Conduct system-level flight and performance testing across maritime scenarios
5. **Manufacturing Scale-Up Analysis** – Deliver cost model and feasibility report for future production

## Deliverables

- (3) prototype UAV test platforms
- (12) fully mission-integrated UAVs
- Ground Control Station + Communications Suite
- Technical documentation: Interface Control Documents (ICDs), maintenance manuals, training materials, Technical Data Package (TDP)

## Use Cases & Applications

- Maritime domain awareness
- Intelligence, Surveillance, Reconnaissance (ISR) in denied/semi-permissive environments
- Over-the-horizon targeting support
- Sea denial operations
- Critical sea lane monitoring
- Real-time ISR for Joint Forces
- Electronic warfare support

## Operational Context

- **Problem addressed:** Existing long-range UAVs are too large, too expensive to field at scale, or insufficiently adaptable for diverse mission profiles
- **Strategic goal:** Enable Navy and Joint Forces to monitor contested maritime zones, extend surveillance and targeting into denied environments, and conduct persistent operations across broad theaters
- **Deployment model:** Distributed, scalable fielding with flexible launch/recovery options

## Integration & Interoperability Expectations

- Modular payload integration (EO/IR, SIGINT sensors)
- Seamless integration with existing government command and control systems
- GCS must be intuitive and tactically relevant
- Standard interfaces for future upgrades and rapid payload swaps
- Support for multiple communication links (mesh, SDR, satcom)

## Proposal Submission Requirements

- Maximum 10 pages (12pt Arial), plus separate cover page
- Must include:
  - Technical overview of proposed UAV system and architecture
  - Rough Order of Magnitude (ROM) cost estimate for prototype phases
  - Proposed schedule and development milestones
  - Relevant past performance or case studies
  - Integration and modularity approach with government systems
  - IP and data rights strategy
- One or more awards may be made based on technical merit and mission alignment

## Funding Vehicle

- One Nation Innovation OTA (Other Transactional Agreement)
- One Nation Innovation is a 501(c)(3) non-profit intermediary for rapid government acquisition
- Initial award may be augmented with additional prototype or production awards pending successful performance and mission validation

## Notable Details

- **Attritable design philosophy:** Cost structure and performance targets suggest expendable/attritable platforms suitable for distributed operations
- **Modular architecture focus:** Heavy emphasis on open standards (FACE, OMS) and tool-less payload integration indicates government's desire for rapid capability insertion
- **Cybersecurity emphasis:** NDAA compliance, encryption standards, and security documentation are mandatory
- **Scalability:** Progression from 3 prototypes to 12 mission-integrated systems indicates scaling and manufacturing readiness as key evaluation factors
- **ArduPilot mandate:** Specification of ArduPilot-based flight control suggests preference for open-source, proven autopilot systems