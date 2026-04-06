# Applying Advanced Human Engineering Methods to Mission Planning for Multi-Manned or Unmanned Air Vehicles

## Document Metadata
- **Type:** Phase 1 SBIR Proposal
- **Client/Agency:** U.S. Navy (SBIR Program)
- **Program/Solicitation:** Navy SBIR Topic N141-019; Proposal N141-019-0144
- **Date:** January 6, 2014 (Revision 2)
- **BST Products/Systems Referenced:** Tablet-based ground control stations (GCS); autopilot systems; Android mobile data visualization tools
- **Key Personnel:** Scott Scheff (HF Designworks, PI); Jack Elston (BlackSwift Technologies); Lowell Staveland; Michael Nico; UEDG subcontractor team

## Executive Summary
HF Designworks and BlackSwift Technologies propose to develop a human-factors-informed mission planning tool for multi-manned and unmanned aircraft that addresses current fragmentation in mission planning systems. The tool will leverage advanced human engineering methods to reduce planning time, workload, and errors while improving operator situation awareness. Phase 1 will establish requirements, algorithms, and interface designs for naval aircraft (F-18, Global Hawk, U-2); Phase 2 will develop and test a functional prototype with mission replanning and rehearsal capabilities.

## Technical Approach

### Overall Strategy
- **User-centered iterative design process** incorporating end-user feedback throughout development
- **Task flow analysis** to identify bottlenecks and automation opportunities
- **Development of three reference mission scenarios** (F-18 strike, Global Hawk surveillance, U-2 reconnaissance) to drive requirements
- **Supervisory control human-automation integration architecture** enabling communication and task delegation between operator, aircraft, and mission planning systems
- **Adaptive automation** framework that dynamically allocates tasks between human and automated systems based on operator/environmental conditions
- **Graphical, integrated information displays** (not separate data screens) to enhance situation awareness and reduce workload

### Key Technical Components

**Algorithms to be developed:**
- Location identification and management
- Background data querying and storage
- Data export/reporting (to PowerPoint, etc.)
- Detect and Avoid (DAA) conflict management
- Weather integration
- Physical obstacle avoidance (mountains, buildings)
- Range calculations
- Aircraft capability/performance modeling
- Payload capability/performance modeling

**Interface approach:**
- Initial development on desktop PC for Phase 1
- Migration to tablet platforms evaluated in Phase 1, implemented in Phase 2
- Standard keyboard/mouse/joystick controls transitioning to multi-modal inputs
- Integration with NATO STANAG 4586 standardized communication protocols

### Phase 1 Deliverables
- Performance evaluation of existing mission planning tools
- Three detailed mission scenarios with task flows and choke point identification
- Tool architecture and requirements specification
- Preliminary algorithms for mission planning operations
- Low-fidelity review with subject matter experts (SMEs)
- Comprehensive Phase 1 report with initial designs and Phase 2 plan
- Test plan submitted to Institutional Review Board (IRB) for Phase 2 human testing

### Phase 1 Option
- Formal test plan development including scenarios, metrics, participant screeners, waiver documentation
- IRB submission and approval coordination (estimated ~2 months timeline)

### Phase 2 Scope (Outlined)
- Full algorithm and workflow integration into comprehensive mission planning tool
- User testing with military personnel based on Phase 1 test plan
- Critical Design Review (CDR) of final design
- Prototype tool validation demonstration
- Potential incorporation of replanning and rehearsal capabilities

## Products & Capabilities Described

### BlackSwift Technologies Systems
- **Custom autopilot solutions** for small UAS
- **Tablet-based ground control stations** (currently commercially available)
- **Mobile Android data visualization tools** for real-time mission data
- **Access to multiple UAS platforms** for Phase 2 field testing
- **Ground control station architecture expertise** and STANAG 4586 familiarity

### HF Designworks Capabilities
- **Human factors engineering and UI design** specialization
- **User-centered design process** with iterative evaluation
- **Two quadcopter UAVs** (one with autopilot, one simulator-capable) for testing
- **Access to UGVs** for multi-platform testing
- **Classified facility** in Boulder, CO (SECRET-level, TOP SECRET upgrade in progress)
- **DCAA-approved accounting system**

### UEDG Subcontractor
- User experience design and globalization services
- Commercialization strategy guidance
- Silicon Valley market expertise

## Use Cases & Applications

### Primary Mission Scenarios (Phase 1 Focus)
1. **F-18 Strike Mission** – Multi-task naval strike planning for manned jet aircraft
2. **Global Hawk Surveillance** – High-altitude, long-endurance reconnaissance mission planning
3. **U-2 Reconnaissance** – Pilot-controlled reconnaissance aircraft mission planning

### Broader Application Domains
- Multi-aircraft coordination (manned-unmanned teaming)
- UAS integration into National Airspace System (NAS)
- UAS mission replanning while airborne
- 1:N supervisory control scenarios
- UAS swarm coordination
- Border Patrol operations
- Police Department/emergency response
- Forestry/search-and-rescue land canvassing
- Military (all branches) tactical mission planning
- Integration with Joint Mission Planning System (JMPS)

## Key Results (Phase 1 Objectives, not yet executed)

This is a proposal; Phase 1 has not been completed. Stated objectives include:

1. Identify current workload and performance measures for mission planning
2. Review and evaluate existing mission planning tools/systems (particularly JMPS)
3. Develop three detailed mission planning scenarios with task flows
4. Identify performance factors for individuals, teams, and mixed teams
5. Develop algorithms for key mission planning functions (locations, DAA, weather, range, capability modeling)
6. Establish requirements and architecture for Phase 2 prototype development

## Notable Details

### Human Factors Innovation
- **Situation Awareness (SA) Focus:** Proposal emphasizes integration of information into unified displays rather than fragmented multi-screen presentations; cites Endsley's SA framework and evidence that separated displays increase workload and decrease awareness
- **Workload Management:** Addresses dual challenge of automation reducing workload while potentially degrading situation awareness if not properly designed
- **Trust in Automation:** Recognizes that unreliable automation erodes operator trust and proposes "negotiated" automation levels where operators develop expectations about task allocation
- **Adaptive Automation:** Proposes dynamic reallocation of tasks based on real-time operator/environmental conditions rather than fixed automation levels

### Competitive Positioning
- Leverages existing BST capabilities (tablet GCS, autopilot, visualization tools) as baseline
- Claims complementary team pairing (HF Designworks' human factors expertise + BlackSwift's UAS technical depth)
- Differentiates through user-centered iterative design vs. narrowly-scoped existing tools
- References proven track record in DARPA iWarrior (GPS visualization/playback), Insight (analyst tools), and military ground control stations

### Prior Related Work Referenced
- **NASA UAS in NAS Program** – Future NAS integration focus
- **DARPA iWarrior** (2010–present) – Web/Android mission visualization with historical GPS playback
- **DARPA Insight** (2013–present) – Analyst decision-support tools
- **Army Universal Ground Control Station (UGCS)** (2009–2011) – Multi-platform GCS GUI and checklist development
- **Royal Australian Air Force Wedgetail** (2007–2008) – Airborne early warning GUI workload evaluations
- **Distributed Team Workload Assessment Tool** (OSD, 2011) – Networked team performance measurement

### Commercialization Strategy
- Initial focus on Navy/Department of Defense markets
- Plans to identify strategic industry partner in Phase 1
- Leverages HF Designworks' history of cross-domain tool adaptation (e.g., heat maps developed for ground vehicles now applied to aerial UAS)
- Existing customer relationships include: U.S. Army, Air Force, Navy, DARPA, NASA, BAE, General Atomics, General Dynamics, McKesson, OSD
- Target follow-on markets: emergency response, remote vehicle operations (UGVs/UUVs), command & control systems

### Organization Details
- **HF Designworks:** Founded 2006, grown to ~10 employees + contractors; Boulder, CO headquarters
- **BlackSwift Technologies:** Also located Boulder, CO; NASA and University of Colorado support experience
- **Proposed Team Structure:** HF Designworks as prime; BlackSwift and UEDG as subcontractors
- **Clearances:** Scott Scheff (PI) holds DoD Top Secret clearance

### Schedule & Funding
- Phase 1: 6 months
- Phase 1 Option: 6 months (includes IRB approval)
- Phase 2: Prototype development and testing (timeline to be detailed)
- Proposal indicates budget constraints awareness; emphasizes focusing on requirements vs. over-prototyping

### Key Challenge Areas Addressed
1. **STANAG 4586 Compliance** – Standardized UAS control interfaces for interoperability
2. **Situation Awareness Deficiencies** – Multi-screen data fragmentation causing mental correlation overhead and accidents
3. **Workload Balancing** – Irregular task distribution creating high-stress/idle periods
4. **Aircraft Diversity** – Tool must generalize across manned and unmanned platforms with different control paradigms
5. **Mission Replanning** – Current systems (e.g., Global Hawk) cannot accept mid-mission replanning
6. **UAS Loss Rates** – Acknowledges UAS loss rate several times higher than manned aircraft; attributes ~67% to human-systems integration issues