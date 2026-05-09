# DAF_26.BZ_PH I_R1_v2.pdf

## Document Metadata
- Type: SBIR Phase I Proposal Submission Instructions & Topic Index
- Client/Agency: Department of the Air Force (DAF), Department of War (DoW)
- Program/Solicitation: DoW 2026 SBIR BAA Release 1
- Date: 2026-05-08 (document version 2)
- Key Personnel: Beck Cotter (last editor), Daniel J. Brewer (AF SBIR/STTR Contracting Officer)
- BST Products/Systems Referenced: None mentioned in this document

## Executive Summary
This document provides comprehensive submission instructions for Phase I proposals in response to the Department of Air Force's 2026 Small Business Innovation Research (SBIR) Broad Agency Announcement (BAA). It includes detailed requirements for proposal format (7 volumes), evaluation criteria, compliance procedures, and five specific Phase I research topics focused on autonomous systems and electronic warfare capabilities.

## Document Structure & Content

### Phase I Proposal Format Requirements
Proposals must include seven volumes:
- **Volume 1:** Cover Sheet with technical abstract (non-proprietary)
- **Volume 2:** Technical Volume (10-point font, 1-inch margins, maximum page limits per topic)
- **Volume 3:** Cost Volume with itemized breakdown
- **Volume 4:** Company Commercialization Report
- **Volume 5:** Supporting Documents
- **Volume 6:** Fraud, Waste, and Abuse Training certification
- **Volume 7:** Disclosures of Foreign Affiliations or Relationships to Foreign Countries

### Key Submission Requirements
- Minimum 2/3 of Phase I research/analytical effort must be performed by the awardee (measured by direct + indirect costs, excluding profit)
- All R/R&D work must be performed in US unless rare exceptions approved in writing
- Proposals submitted electronically via Defense SBIR/STTR Innovation Portal (DSIP)
- CMMC Level 2 (Self) requirement for all topics listed
- ITAR/EAR export control restrictions apply to all five topics
- Foreign nationals must be disclosed with countries of origin, visa/work permit type, and SOW tasks

### Evaluation & Award Details
- DAF will conduct security risk assessment based on foreign affiliations disclosure
- Evaluation criteria include technical merit, feasibility, and commercialization potential
- Multiple awards anticipated per topic; each evaluated independently
- Timeline: ~90 calendar days from solicitation close to final selections
- Small businesses with venture capital/hedge fund/private equity ownership eligible

---

## Phase I Research Topics

### Topic 1: DAF26BZ01-NV003
**Title:** Low-Cost Modular Payload Vehicle for Agile Electronic Warfare Swarms with Ground Launch Capability

**Award Maximum:** $275,000 | **Duration:** 6 months | **Technical Volume Limit:** 20 pages

**Technology Priority Area:** Integrated Sensing and Cyber

**Objective:** Develop a low-cost small unmanned aircraft system (sUAS), Group 3 and below, with modular payload accommodation and ground launch capability for electronic warfare (EW) applications in swarms (3-10 units).

**Key Performance Parameters:**
- Minimum 5 lbs payload capacity
- Minimum 45 minutes endurance with 5 lb payload
- Minimum 100 km operational range
- Compatible with readily available ground launch systems (pneumatic launcher, rail system)
- Deployable and operational within 5 minutes of arrival

**Technical Approach:**
- Develop standardized payload interface for rapid integration/swapping
- Either modify existing commercially available sUAS or develop new platform
- Optimize for low cost, ease of use, reliability
- Design for low-to-medium swarm operations

**Phase I Deliverables:**
- Detailed specifications for payload interface, power system, communication system, control system
- Feasibility demonstration for rapid payload integration and payload agnosticism
- Preliminary designs and performance simulations
- Component selection rationale
- Ground launch integration plan
- Documentation addressing integration challenges

**Phase II Goals:**
- Develop and integrate prototype modular payload vehicle
- Demonstrate rapid payload integration/swapping
- Achieve specific cost target per unit (to be determined)
- Demonstrate all stated KPPs
- User-friendly control interface
- Integration with representative ground launch system
- Evaluate impact of ground launch on performance/reliability

**Phase III Dual-Use Applications:**
- Environmental monitoring platforms
- Logistics and supply chain delivery
- Infrastructure inspection platforms
- First responder situational awareness
- Disaster relief communications and EW capabilities

---

### Topic 2: DAF26BZ01-NV006
**Title:** Intelligent Threat Aware Autonomy (ITA2)

**Award Maximum:** $300,000 | **Duration:** 6 months | **Technical Volume Limit:** 20 pages

**Technology Priority Area:** Trusted AI and Autonomy

**Objective:** Develop autonomous systems capable of:
1. Weapon Engagement Zone (WEZ) modeling and representation
2. WEZ avoidance through dynamic path planning for Autonomous Collaborative Platforms (ACPs)
3. Advanced weaponeering to optimize weapon usage for target capture/neutralization
4. Mutual support for multiple ACPs cooperating in adversarial situations

**Technical Approach:**
- Focus on sense-think-act behaviors beyond sensing
- Develop WEZ models considering weapon range, vehicle movement, threat trajectories
- Create real-time path planning algorithms for safe navigation through dynamic WEZs
- Optimize weapon assignment to targets considering movement and mission context
- Enable coordinated movement and collaborative weapon engagement among multiple ACPs
- Vehicle control via desired aim-points/waypoint plans in 3D space
- Interface with existing vehicle control technologies (normal acceleration, roll-rate, throttle commands out of scope)
- Address uncertainty in own-ship states, target states, operations boundaries, communication delays, environmental disturbances (wind)

**Phase I Deliverables:**
- Initial development of proposed solutions to one or more design challenges
- Alternate solutions and identification of most promising approaches
- Desktop simulation analysis in representative aircraft platforms (kinematic or dynamic)
- Feasibility studies of proposed approaches
- Identification of Air Force customer/stakeholder applications
- Phase II technology development plan
- No government-furnished data/equipment required

**Phase II Goals:**
- Expand design details and experimental test plans
- Higher fidelity desktop simulation with representative platforms
- Realistic use cases exercising ITA2 functionality
- Demonstrate benefits vs. current state-of-art (circumnavigation, pure-pursuit)
- Real-time functionality evaluation in software/hardware integration laboratory
- Cost/schedule permitting: port code to flight processors and initial flight demonstrations with surrogate sUAS
- Technology transfer plan for Air Force programs

**Phase III Applications:**
- Counter unmanned aerial system (C-UAS) defense
- Cruise missile defense
- High-value airborne asset defense
- High-speed threat interception
- Suppression/destruction of enemy air defenses (SEAD/DEAD)
- Combat air patrol
- Applicable to Group 5 systems particularly
- Support to manned platforms
- Pre-mission planning and wargaming

---

### Topic 3: DAF26BZ01-NV008
**Title:** Runtime Assured Autonomy (RTAA)

**Award Maximum:** $300,000 | **Duration:** 6 months | **Technical Volume Limit:** 20 pages

**Technology Priority Area:** Trusted AI and Autonomy

**Objective:** Develop innovative Runtime Assured Autonomy (RTAA) systems that protect individual platforms and fleets against undiscovered design errors in autonomy functions. Focus on use cases where RTAA determines if autonomy is generating infeasible, incorrect, and/or non-optimal solutions (paths, task allocation) affecting mission progress and effectiveness.

**Key Technical Challenges:**
- Autonomy approaches are complex and nondeterministic, difficult to certify for airworthiness
- AI/autonomy capabilities rapidly evolving with continuous updates
- Need for runtime monitoring and mitigation without full pre-certification

**Two Main RTAA Functions:**

1. **Fault Detection & Isolation:**
   - Monitor if autonomy is correctly producing Courses of Action (COAs) and commands
   - Detect faults indirectly through effects on platform safety, performance, mission effectiveness
   - Determine correct behavior through nominal functional/performance requirements, sanity checks, rubrics, rule sets
   - Focus primarily on autonomy performance in delivering correct/optimal COAs

2. **Mitigation Response:**
   - Activate recovery/reversionary protocols when autonomy design errors detected
   - Command vehicle to failsafe loiter point
   - Clear functional states and restart autonomy
   - Last resort: return-to-base or ditch procedures
   - Switch to simpler reversionary autonomy functions

**Two Functional Levels:**

1. **Platform/Fleet Safety:**
   - Monitor flight envelope (angle of attack, angular rates, g-loading)
   - Verify flight corridor/airspace compliance
   - Validate path commands against vehicle maneuvering capabilities
   - Deactivate advanced autonomy if safety violations detected

2. **Autonomy Function Performance:**
   - Verify correct COA generation (safe, optimal, deconflicted paths)
   - Monitor asset allocation and role reassignment
   - Verify replanning for environmental/threat changes
   - Maximize mission effectiveness

**Phase I Deliverables:**
- Feasibility study of proposed solutions
- Architecture and approach initial design ideas
- Identification of technical challenges, risks, design requirements
- Functional design of architecture, interface requirements, communication pathways, sensor suite requirements
- Use cases covering range of autonomy design faults causing incorrect COA generation
- Contingency scenarios (platform hardware faults, pop-up threats, mission changes)
- Fault detection/isolation strategies (formal methods, heuristic mechanisms)
- Recovery procedures under various scenarios/contexts
- Risk assessment
- Desktop simulation studies in lower-order design analysis
- Phase II technology development plan
- No government-furnished data required

**Mission Scenarios for Use Cases:**
- ISR, patrol, supply delivery, high-value escort
- Weapon engagement/deployment, enemy suppression
- Contested operations: high-risk zones, no-fly zones, natural/urban terrain with red team assets

**Phase II Goals:**
- Mature architecture design, align with Air Force Autonomy-Government Reference Architecture (A-GRA)
- Higher fidelity desktop simulation with representative platforms
- Realistic use cases for RTAA fault detection and mitigation
- Real-time functionality and integration laboratory testing
- Capstone demonstrations of recovery processes effectiveness
- Technology readiness level maturation
- Repeat capstone experiments from desktop simulations
- Government-furnished data/equipment possible (simulation models, lab equipment)
- Technology transfer plan for Air Force programs

**Phase III Applications:**
- Direct Air Force customer support via AFWERX STRATFI/TACFI programs
- AFRL directorates, Autonomy Prime programs
- Agility Prime for air mobility with autonomy
- Current/future air wings with autonomy-driven platforms
- 412th Test Wing at Edwards AFB autonomous flight tests
- Urban/Advanced Air Mobility (UAM/AAM): eVTOL/hVTOL applications
- Medical evacuation, resupply/distribution, patrol, search & rescue
- Law enforcement, civil air patrol, firefighting, disaster relief
- Border patrol, infrastructure inspections, environmental services, agriculture
- Ground vehicles, self-driving cars, autonomous transportation
- Industrial systems, medical devices, robotic applications
- Any systems requiring assured intelligent autonomy

**Commercialization Opportunities:**
- License developed code
- Manufacture avionics subsystems
- Support DoD and civilian platforms
- Critical for operations over densely populated areas
- Enable rapid fielding of autonomy functions with reduced certification burden

---

### Topic 4: DAF26BZ01-NV500
**Title:** Autonomous Space Cargo Network (ASCN): AI-Driven Logistics Automation and Digital Twin Integration for Space Mobility

**Award Maximum:** $75,000 | **Duration:** 3 months | **Technical Volume Limit:** 10 pages

(Topic described in index only; full description not included in provided document text)

---

### Topic 5: DAF26BZ01-NV501
**Title:** Commercial-Derived Insights for Novel Tactical Surveillance, Reconnaissance, and Tracking (TacSRT) Capabilities

**Award Maximum:** $175,000 | **Duration:** 3 months | **Technical Volume Limit:** 5 pages

(Topic described in index only; full description not included in provided document text)

---

## Notable Details & Compliance Information

### Export Control & Security
- All topics restricted under ITAR (22 CFR Parts 120-130) or EAR (15 CFR Parts 730-774)
- Foreign nationals must be fully disclosed with work permit