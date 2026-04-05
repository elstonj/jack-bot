# EXTiC White Paper: Black Swift Technologies

## Document Metadata
- **Type:** White Paper / Proposal
- **Client/Agency:** Department of Defense (DoD)
- **Program/Solicitation:** EXTiC 26-1 (Experimentation: Transforming in Contact)
- **Date:** 2026-01-12
- **BST Products/Systems Referenced:** S0 VTOL, SwiftCore Flight Management System
- **Key Personnel:** Jack Elston (last editor)

---

## Executive Summary

BST proposes the S0 VTOL uncrewed aircraft system as a demonstration-ready ISR and sensing-extension capability for the EXTiC 26-1 experimentation event. The S0 VTOL is a 5.7-lb fixed-wing VTOL platform designed for operations in high-wind, austere, and contested environments, capable of rapid deployment, persistent airborne presence, and low logistical burden. The system provides critical ISR capabilities that support the detection-to-response mission thread while maintaining resilience under environmental and operational stress.

---

## Technical Approach

**Core Design Philosophy:**
- Fixed-wing VTOL architecture combining vertical takeoff/landing flexibility with efficient cruise performance
- Originally developed for scientific/environmental missions (wildfire monitoring, volcanic gas sampling, atmospheric profiling), with design characteristics directly applicable to defense ISR
- Purpose-built for extreme conditions rather than optimized for benign environments

**Key Performance Characteristics:**
- Weight: ~5.7 lbs (highly portable)
- Cruise speed: Exceeding 85 knots
- Endurance: ~1 hour (depending on configuration)
- Launch/recovery: No runway, launch rails, or recovery equipment required; operates from austere/confined sites with small teams
- Flight envelope: Designed for high-wind and turbulent operations, providing greater environmental margin than typical small multirotor systems

**Operational Architecture:**
- Fully autonomous flight from launch through recovery with supervisory control paradigm
- Tablet-based mission planning interface for rapid area-of-interest definition and flight pattern configuration
- Electronic centralized aircraft monitoring (ECAM) with continuous health/navigation/sensor status evaluation
- Fault detection with severity categorization and autonomous mitigation response if operator input unavailable

---

## Products & Capabilities Described

### S0 VTOL Uncrewed Aircraft System

**What It Is:**
A lightweight, fixed-wing VTOL uncrewed aircraft system combining vertical takeoff/landing capability with fixed-wing cruise efficiency. TRL 7 mature system with fully functional aircraft and ground control station available for demonstration.

**Proposed Use in EXTiC:**
- Primary role: Airborne ISR and target custody asset responding to detection cues
- Rapid launch from austere locations in response to threat detection
- Establishment of positive identification (PID) and sustained target tracking
- Persistence in high-wind/turbulent environments where other ISR assets degrade
- Integration node for layered sensing architecture

**Technical Specifications:**
- Weight: 5.7 lbs
- Dash speed: 85+ knots
- Endurance: ~1 hour
- Environmental tolerance: Designed for strong/variable winds, turbulence, complex terrain, particulate-laden environments
- Integrated onboard environmental sensing suite (wind, temperature, pressure, humidity)

**Key Differentiators:**
- VTOL eliminates infrastructure dependencies (runways, launch equipment)
- Fixed-wing efficiency enables larger area coverage and longer loiter times vs. multirotors
- Environmental sensing capabilities provide operational context (sensor interpretation, flight optimization)
- Proven operational heritage in government-sponsored and scientific missions

---

### SwiftCore Flight Management System

**What It Is:**
BST's proprietary end-to-end avionics solution encompassing onboard autopilot, mission planning software, ground control station, and sensor interfaces. Designed from inception for autonomous operations in challenging atmospheric/operational conditions.

**Key Capabilities:**
- Fully autonomous mission execution with operator supervisory control
- Tablet-based mission planning interface for rapid reconfiguration
- Electronic centralized aircraft monitoring (ECAM) with fault detection/prioritization/mitigation
- Autonomous fault response if operator unavailable within specified time window
- Modular, open-architecture design with well-defined interfaces for third-party payloads/sensors/mission software
- Standard electrical and data interfaces reducing vendor lock-in

**Operational Heritage:**
- Proven in field operations supporting scientific, environmental, and government-sponsored missions
- Demonstrated in strong winds, turbulence, remote/austere environments
- Multiple platforms and mission types validated
- Tested in government-sponsored research campaigns and operational demonstrations

**Integration Design Philosophy:**
- Intentionally open interfaces supporting rapid reconfiguration without airframe/core avionics redesign
- Self-contained communications and control architecture minimizing external dependencies
- Modular payload architecture enabling incremental additions without system destabilization

---

## Use Cases & Applications

**Primary EXTiC Alignment: ISR and Target Custody**
- Rapid response to detection cues from radar, passive sensors, or other tripwire systems
- Airborne PID and tracking of low-altitude threats
- Sustained custody through maneuver, terrain masking, environmental complexity
- Data handoff to C2 systems for fusion with other sensors
- Evaluation of how persistent airborne ISR absorbs environmental/operational stress

**Secondary Alignment: Detection and Early Warning**
- Extension of detection coverage beyond line-of-sight/field-of-view limitations of ground-based sensors
- Investigation of uncertain areas; confirmation/refutation of detections
- Addressing gaps in sensor coverage in complex terrain
- Assessment of airborne sensing extensions' impact on detection timelines and false alarm reduction

**Secondary Alignment: Resilience and Sustainment**
- Deployment from austere locations without fixed infrastructure
- High-wind/turbulence tolerance increasing mission availability under adverse conditions
- Autonomous operation and fault mitigation supporting continued operation/safe recovery under degraded states
- Graceful degradation pathways under electronic/navigation attack

**Broader Scientific/Environmental Heritage** (demonstrating design robustness):
- Wildfire monitoring
- Volcanic gas sampling
- Atmospheric profiling
- Environmental observation in extreme conditions

---

## EXTiC 26-1 Demonstration Concept

**Proposed Mission Role:**
- Downstream ISR asset operating after initial detection
- Scoped to: rapid response, situational awareness establishment, persistent coverage, C2 data handoff
- Explicitly excludes engagement/defeat actions

**Representative Scenario Phases:**

1. **Cueing and Launch:** Receipt of detection cue; VTOL launch from confined/unimproved site
2. **Transit and Repositioning:** High-speed transit to area of interest; demonstration of terrain coverage impractical for multirotors
3. **ISR Establishment and Custody:** Loiter/patrol pattern establishment; maintenance through environmental disturbances
4. **Integration and Handoff:** Data product display locally and integration into broader C2 environment; sensor fusion with other systems
5. **Stress and Degradation:** Introduction of environmental/operational stressors (wind, navigation degradation, communications constraints); observation of system behavior and mission impact
6. **Recovery:** VTOL recovery with minimal ground footprint

**Proposed Evaluation Metrics:**
- Response Time: Detection cue to airborne ISR presence
- Persistence: Continuous coverage duration vs. multirotor systems
- Environmental Tolerance: Stable flight/sensing in high-wind/turbulent environments
- Operator Workload: Interaction levels during nominal/off-nominal conditions
- Integration Effectiveness: Data ingestion into C2; contribution to common operating picture
- Degraded Operations: System behavior and mission impact under degraded navigation/communications

**Experimentation Value:**
- Low-risk, high-value evaluation of lightweight fixed-wing VTOL ISR class
- Assessment of complement to existing detection, EW, defeat systems
- Evaluation of gap reduction between detection and response
- Identification of integration priorities and future development pathways

---

## Integration, Communications, and Connectivity

**Ground Segment:**
- Portable, self-contained ground control station with integrated battery power
- No external power, fixed infrastructure, or specialized facilities required
- Tablet-based interface for mission planning, flight monitoring, system health display, data recording
- All core functions available locally enabling operation in connectivity-limited environments

**Communications Architecture:**
- Organic point-to-point radio data link (part of system)
- Supports command/control, telemetry, sensor data exchange
- Does not require IP-based networking for essential flight/data functions
- Intentionally simple and robust, minimizing external network dependencies
- Well-suited to scenarios with constrained, intermittent, or deliberately stressed network conditions

**Data Products and Interfaces:**
- Environmental measurements, aircraft state, mission metadata displayed at ground station and recorded
- Well-defined APIs for sharing data with external systems when connectivity available
- Interface-based approach enabling integration with C2, data fusion, visualization tools without core flight system modification

**Growth Path:**
- Future integration of digital data link (DDL) for live video dissemination identified as growth area
- Not required for EXTiC 26-1 but represents logical extension informed by experimentation
- Current demonstrated capabilities separated from future enhancements

**Integration Risk Mitigation:**
- Self-contained communications/control architecture minimizes risk to overall experiment
- Simplicity, modularity, transparency in integration strategy
- Meaningful integration touchpoints without undue burden on event infrastructure

---

## Technology Readiness and Operational History

**TRL Assessment:** TRL 7
- Fully functional system-level demonstrations in operationally relevant environments
- Aircraft, avionics, ground control station, communications architecture all fully functional
- Available for live demonstration without laboratory-only components or developmental subsystems

**Operational Heritage:**
- BST's extensive history designing/deploying uncrewed aircraft in demanding environmental conditions
- Platforms derived from same design philosophy as S0 VTOL used in U.S. Government agency, academic, and commercial missions
- Operations include: strong/variable winds, turbulent boundary layers, complex terrain, austere/limited-infrastructure locations

**S0 VTOL-Specific Development:**
- Originally developed to meet atmospheric observation mission requirements
- Wildfire monitoring, volcanic gas sampling, environmental profiling missions
- Missions required reliable autonomous flight, precise navigation/control, robust system behavior in environments where conventional small UAS degrade

**System Maturity:**
- Mature, integrated system with known performance characteristics, documented limitations, established operating procedures
- Not a prototype assembled for this submission
- Enables experimentation focus on mission-thread integration and system-of-systems behavior rather than basic platform viability

---

## Risks, Limitations, and Experimentation Opportunities

**Known Limitations and Experimentation Value:**

1. **Navigation Dependency:**
   - Reliance on conventional satellite-based (GPS) navigation for nominal operations
   - Includes fault monitoring and defined behaviors for degraded navigation quality
   - Does not claim assured performance under all forms of electronic attack/GPS denial
   - **Experimentation opportunity:** Characterize navigation degradation effects on mission execution, operator workload, ISR continuity; identify system-of-systems mitigation strategies

2. **Communications Bandwidth:**
   - Current point-to-point radio link optimized for robustness/simplicity vs. high-bandwidth dissemination
   - Limits real-time transmission of rich data products (live video)
   - Ensures reliable command/control and telemetry under constrained conditions
   - **Experimentation opportunity:** Inform trade studies on expanded connectivity, data prioritization, external network integration

3. **Environmental Stressors:**
   - High winds, turbulence, dust, thermal activity can affect operations
   - System explicitly designed to operate in such conditions
   - **Experimentation opportunity:** Evaluate availability, persistence, graceful degradation; observe system behavior as conditions deteriorate; inform mission resilience and operator decision-making understanding

**Experimentation Perspective:**
These limitations framed as enablers rather than detractors—exposing known seams and trade spaces allows EXTiC participants to understand S0 VTOL complement to other capabilities, identify high-benefit integration approaches, and design mission threads accommodating real-world system behavior vs. idealized assumptions.

---

## Notable Details

**Competitive and Integration Positioning:**
- Intentionally scoped to complement detection, C2, defeat systems rather than serve as all-encompassing solution
- Modular, open-architecture design allows adaptation to evolving mission needs without redesign
- Low logistical footprint (5.7 lbs, self-contained power, no infrastructure) suitable for austere/expeditionary contexts
- Explicitly excludes engagement/defeat actions, maintaining clear integration boundaries

**Organization Details:**
- Black Swift Technologies LLC
- Location: 2840 Wilderness Pl Ste D, Boulder, CO 80301
- Contact: 720-638-9656

**Organizational Strengths Emphasized:**
- Extensive experience operating uncrewed aircraft in challenging environments