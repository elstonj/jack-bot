# HR0011SB20254XL-01: ALIAS Missionized Autonomy for Emergency Services - SBIR XL

## Document Metadata
- Type: DARPA SBIR XL Topic Announcement
- Client/Agency: DARPA (Defense Advanced Research Projects Agency)
- Program/Solicitation: ALIAS (Aircrew Labor In-Cockpit Automation System) / ALIAS-Texas initiative; Topic HR0011SB20254XL-01
- Date: 2025 (FY25 solicitation)
- Technology Areas: Air Platform | Battlespace | Sensors
- Modernization Priorities: Human-Machine Interfaces | Integrated Sensing and Cyber | Trusted AI and Autonomy
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This SBIR XL solicitation seeks proposals for developing autonomy applications that enhance autonomous/optionally piloted UH-60 and S-76 helicopters for emergency services, with initial focus on wildfire suppression. Proposers must integrate with DARPA ALIAS and Sikorsky's MATRIX autonomy system using the provided SDK, develop functional prototypes tested in simulation (AFSIM) and live flight tests, and demonstrate capability across multiple mission scenarios including water drops, cargo sling loads, medical evacuations, reconnaissance, and crew shuttles.

## Technical Approach
- **Autonomy Development Framework**: Leverage DARPA ALIAS air vehicle autonomy program and Sikorsky MATRIX Government Purpose Rights Software Development Kit to develop third-party autonomy applications ("plugins") that integrate with the ALIAS/MATRIX autonomy stack
- **Simulation Environment**: Advanced Framework for Simulation, Integration, and Modeling (AFSIM) environment representing terrain, wind, vegetation, and fire dynamics with real-time sensor interface conformance
- **Integration Requirements**: Applications must integrate with high-fidelity Generic Helicopter Model for training, testing, and evaluation; demonstrate seamless integration with ALIAS/MATRIX autonomy system
- **Real-World Validation**: Transition from simulation to live flight testing using S-76 and UH-60 optionally piloted helicopters; concurrent control of multiple ALIAS-enabled aircraft
- **Development Focus**: Real-time decision-making, integrated sensing for situational awareness, advanced communication technologies for coordination with ground and air units

## Products & Capabilities Described

### DARPA ALIAS (Aircrew Labor In-Cockpit Automation System)
- DARPA's established air vehicle autonomy program providing autonomy foundation
- Serves as the autonomy stack onto which third-party applications plug in
- Government Purpose Rights software development kit provided to offerors

### Sikorsky MATRIX Autonomy System
- Autonomy system deployed on S-76 and UH-60 helicopters
- Integrates with ALIAS to enable optionally piloted vehicle (OPV) operations
- Provides foundation for mission-specific autonomy application integration
- Supports concurrent/collaborative multi-vehicle operations

### UH-60 & S-76 Helicopters (Optionally Piloted Variants)
- Primary air platforms for autonomy application testing and demonstration
- Capable of supporting sustained concurrent/collaborative multi-vehicle wildland firefighting operations
- Will undergo live flight testing with autonomy applications

### AFSIM (Advanced Framework for Simulation, Integration, and Modeling)
- High-fidelity simulation environment for autonomy app development and testing
- Models terrain, wind, vegetation, and fire dynamics
- Supports conformant sensor interfaces for real-time interaction
- Generic Helicopter Model integration capability

## Use Cases & Applications

### Primary Mission: Wildland Firefighting
- **Water or Retardant Drops**: Automated drop planning and execution using buckets or fixed tanks; wind and terrain-aware routing
- **Reconnaissance**: Autonomous route or area reconnaissance using EO/IR sensors; tagging points of interest; time-stamped reporting
- **Cargo Sling Loads**: Autonomous management of load stability, airspeed, and landing zone approach
- **Crew Shuttles**: Personnel transport between mission staging areas; dynamic route and manifest updates based on C2 tasking or weather

### Emergency Services Missions
- **Medical Evacuations**: Autonomous or semi-autonomous medical evacuation operations
- **Rooftop Personnel Recovery**: Recovery of injured personnel from rooftops in urban environments using autonomous landing, hover, or hoist operations under emergency conditions
- **Search and Rescue (SAR)**: Multi-domain mission profiles combining SAR with logistics delivery

### Multi-Aircraft Scenarios (Phase II Option)
- **Coordinated Wildfire Suppression**: Reconnaissance and suppression aircraft operating together to identify firelines, relay targets, and coordinate drops
- **ISR-Driven Multi-Aircraft Coordination**: Distributed autonomous team coordination without centralized ground control
- **Cross-Domain Mission Profiles**: Simultaneous fire suppression and reconnaissance; SAR with logistics delivery

## Demonstration Requirements

### Phase II Capstone Scenario Examples (Proposers select scope):
1. Single Aircraft: Fixed Burn Fire Suppression with automated drop planning over fixed area
2. Single Aircraft: Rooftop Personnel Recovery (autonomous landing/hover-hoist)
3. Multi-Aircraft: Coordinated Wildfire Suppression (recon + suppression coordination)
4. Single Aircraft: Cargo Sling Load with autonomous load management
5. Single Aircraft: Reconnaissance with EO/IR sensors
6. Single Aircraft: Crew Shuttle with dynamic routing
7. At least one government-organized simulation exercise participation
8. At least one flight demonstration event

### Phase II Option (12-month) Multi-Aircraft Expansion:
- Training, tactics, and procedures (TTPs) for tasking, mission monitoring, and dynamic reallocation
- Airspace integration procedures for mixed civil/military/disaster response operations
- Validation of ISR-driven multi-aircraft coordination TTPs without centralized ground control
- Tactical autonomy behaviors for denied/degraded/contested environments
- Distributed autonomous team response TTPs
- End-user collaboration for mission-specific SOPs and CONOPS
- Cross-domain mission profile testing

## Solicitation Structure

### Phase I
- **Direct-to-Phase II (DP2) Only**: No traditional Phase I; proposals must demonstrate existing technical maturity and feasibility
- **Required Demonstration**: Preliminary results, app prototypes, or prior autonomy work
- **Deliverables**: Clear articulation of integration ability with Generic Helicopter Model; transition path to Phase II; documentation of existing modeling and simulation environments supporting rapid autonomy app development

### Phase II
- **Duration**: 12-month Period of Performance (with optional 12-month expansion)
- **Deliverables**:
  - Functional prototype of mission app integrated with ALIAS/MATRIX autonomy stack
  - Performance demonstration in simulation and live flight test (S-76, UH-60)
  - Scenario-based evaluation with key app functionality validation
  - Participation in at least one simulation exercise and one flight demonstration event
- **Phase II Option**: Multi-aircraft scenario development, TTP refinement, airspace integration procedures

## Phase III Commercial & Military Applications
- **Commercial**: Rapid response to wildfires and natural disasters
- **Military**: Autonomous surveillance and reconnaissance in austere environments
- **Broad Applications**: AI app development, aircraft-sensor-app integration, mission-based testing across various domains

## Notable Details
- **ITAR Controlled**: Technology restricted under International Traffic in Arms Regulation (22 CFR Parts 120-130) and potentially Export Administration Regulation (15 CFR Parts 730-774); foreign national participation must be disclosed and may be restricted
- **ALIAS-Texas Initiative**: Program named in references as Texas A&M System-led 59.8M autonomous helicopter wildfire response initiative
- **Related Reference**: DARPA announced ALIAS-Texas testbed for assessing autonomous/semi-autonomous aircraft in wildland firefighting through simulated and live test environments
- **Key Innovation Focus**: Development of autonomy applications for "optionally piloted" operations—systems that can operate fully autonomously or with human oversight depending on mission phase/complexity
- **Competitive Advantage**: Integration with established ALIAS and MATRIX systems; access to high-fidelity AFSIM simulation environment; pathways to live flight testing with actual UH-60 and S-76 helicopters
- **Multi-Domain Approach**: Supports engineering, testing, and training across AI app development, aircraft-sensor-app integration, and mission-based evaluation
- **Operational Realism**: Strong emphasis on operationally realistic scenarios, field validation, and end-user collaboration (emergency services coordination)

---

**Assessment**: This is a substantive solicitation document outlining DARPA's strategic focus on autonomous helicopter applications for emergency services. It directly invites third-party autonomy app development rather than asking for full system solutions, positioning BST or other contractors as developers of specific mission capabilities integrated onto established ALIAS/MATRIX platforms. The emphasis on simulation-to-flight transition and multi-vehicle coordination indicates maturity-focused development with clear path to operational deployment.