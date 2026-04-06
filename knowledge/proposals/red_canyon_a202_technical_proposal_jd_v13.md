# Red Canyon Software, Inc. SBIR Phase I Proposal: Four Layered Aerial Vehicle Architecture (FLAVA)

## Document Metadata
- **Type:** SBIR Phase I Technical Proposal
- **Client/Agency:** NASA (Small Business Innovation Research program)
- **Program/Solicitation:** Topic #A2.02-8303
- **Date:** January 31, 2016
- **BST Products/Systems Referenced:** Black Swift autopilot hardware platform, SwiftCore Flight Management System
- **Key Personnel:** Jay David Marks (Red Canyon, PI), Alec Forsman (Red Canyon), Jack Elston (Black Swift Technologies), Steven Wichman-Wishstar (Redefine Technologies)

## Executive Summary

Red Canyon Software proposes FLAVA, a four-layered open-source software architecture for unmanned aerial vehicles (UAVs) that uses standardized interfaces to reduce development costs and increase reliability across missions. Drawing parallels to the OSI model's success with the internet, FLAVA separates mission planning, plan execution, operations, and physical subsystems into distinct layers with defined interfaces, enabling software components to be reused across different airframes and missions rather than developed custom for each platform. The Phase I effort will demonstrate technical feasibility using NASA open-source components (CoreFlight Executive, OSAL, PLEXIL) integrated with Black Swift Technologies' autopilot hardware.

## Technical Approach

FLAVA implements a four-layer architecture based on the OSI model principles:

### Architecture Layers

1. **Planning Layer (PL):** Constructs high-level mission plans defining sequential activities (e.g., "take off," "fly to Location A," "acquire sensor data") independent of specific airframes. Plans are transmitted via the Planning Layer Interface (PLI) to enable remote planning and reuse across platforms.

2. **Plan Execution Layer (PEL):** Acts as translator between PL activities and OL operational commands. Contains Activity Execution Blocks (AEB) with airframe-specific knowledge, converting abstract activities into detailed command sequences. Will be implemented using NASA's PLEXIL (Plan Execution Interchange Language), which supports branching, loops, concurrent activities, and temporal constraints.

3. **Operations Layer (OL):** Handles mission-level capabilities including guidance/navigation/control (GN&C), takeoff, collision avoidance, landing, science observations, and communications. Implements individual functional "Apps" (separate software modules) that interface through a common infrastructure. Uses CoreFlight Executive (cFE) as the software bus providing inter-process communication (IPC), timing, event notification, and data services. The OS Abstraction Interface (OSAI) using GSFC's OSAL allows replacement of operating systems (Linux during development, custom OS for flight). The Hardware Abstraction Interface (HAI) provides standard APIs for accessing physical hardware without implementation details.

4. **Physical Subsystems Layer (PSL):** Contains all physical hardware (sensors, actuators, motors, science instruments, transmitters, receivers) and communication buses (RS232, I2C, SPI, CAN, USB, RS422). Software drivers translate functional instructions into hardware-specific signals and commands.

### Key Interface Standards
- **PLI:** Standardizes plan transfer between ground station and airframe
- **PELI (Plan Execution Layer Interface):** Standardizes status/command flow between PEL and OL
- **OLI (Operations Layer Interface):** Standardizes OL component interactions
- **HAI:** Abstracts hardware details from OL Apps

### Open Source Technology Stack
- **CoreFlight Executive (cFE):** NASA's GSFC-developed platform providing reusable software infrastructure with aerospace flight heritage
- **OSAL:** OS abstraction supporting Linux, VxWorks, RTEMS, ARINC653
- **PLEXIL:** NASA Ames/JPL/Carnegie Mellon collaborative effort for plan execution
- **Development Platform:** Ubuntu Linux; demonstration on Black Swift autopilot hardware

## Products & Capabilities Described

### Black Swift Technologies Autopilot Hardware Platform
- **Purpose:** Serves as demonstration platform for FLAVA implementation
- **Role in Project:** Hosts PEL and OL on processor board; PSL on sensor board. Black Swift provides hardware interface documentation, driver development support, and HAI consultation.
- **Specifications:** Not detailed in proposal, but characterized as "highly capable" with "SwiftCore Flight Management System" anchoring avionics capabilities

### CoreFlight Executive (cFE)
- **What it is:** Application development and run-time environment providing Software Bus (messaging), Time, Event, Executive, and Table services
- **How used:** As OL infrastructure replacing proprietary autopilot frameworks, enabling Apps to interface through common mechanisms
- **Claim:** Currently has aerospace flight heritage demonstrating reliability for flight missions

### OSAL (OS Abstraction Layer)
- **What it is:** Small software library isolating embedded software from real-time OS through standardized APIs
- **How used:** Provides OSAI layer enabling OS replacement/upgrade (Linux development → flight OS)
- **Supported OSs:** Linux, VxWorks, RTEMS, ARINC653

### PLEXIL (Plan Execution Interchange Language)
- **What it is:** Compact, semantically clear, deterministic plan execution language supporting branches, loops, time/event-driven activities, concurrent operations, sequences, and temporal constraints
- **How used:** Implements PEL functionality; communicates with OL via UDP interface
- **Heritage:** NASA Ames/JPL/Carnegie Mellon development; flight-proven on Mars rovers, planetary habitat control, drilling equipment, ISS operations

## Use Cases & Applications

### NASA Applications
- Future unmanned vehicle missions (any spacecraft, rover, or aerial platform)
- Mars Rover operations (target engagement with JPL Mars Rover and MSL teams)
- AI/autonomous system development (target engagement with JPL AI Group)
- Aeronautics research missions (target engagement with NASA ARMD)
- Dynamic replanning autonomous missions (enabled by on-board Planning Layer)

### Non-NASA/Commercial Applications
- Commercial unmanned aerial vehicles (UAVs)
- Unmanned robotic vehicles (ground-based)
- Unmanned underwater vehicles (UUVs)
- Unmanned rovers
- Science missions reducing cost and development timeline

### Demonstration Mission
Phase I will define and execute a single demonstration mission using Black Swift hardware and a canned mission plan, validating the architecture's ability to execute planning, execution, operations, and physical subsystem functions in an integrated manner.

## Technical Objectives (Phase I Validation Goals)

1. Demonstrate all planning activity capability within PL
2. Demonstrate all plan execution operations within PEL
3. Demonstrate all operations functions within OL
4. Demonstrate containment of physical hardware operations within PSL
5. Demonstrate remote mission plan transfer through common interface
6. Demonstrate plan execution and status via standardized PEL/OL interface
7. Define initial HAI framework between OL and PSL
8. Demonstrate feasibility of cFE as OL infrastructure
9. Demonstrate feasibility of OSAL as OS abstraction
10. Demonstrate feasibility of PLEXIL as PEL execution component

## Work Plan & Deliverables

### Phase I Structure (6 months)

**Four-Phase Execution:**
1. Requirements and Design
2. Development
3. Integration
4. Demonstration

**Key Deliverables:**
- Requirements and design documents
- Functional and detailed design documents
- Prototype Planning Interface code
- Prototype HAI code
- Prototype PLEXIL configuration
- Proof-of-concept demonstration
- Final comprehensive report
- Two bi-monthly interim status reports
- Kickoff and wrap-up meeting presentations

**Team Composition:**
- Jay David Marks (Red Canyon, PI): Principal Investigator, Senior Software Engineer, FLAVA design/development
- Alec Forsman (Red Canyon): Software Engineer, FLAVA development
- Steve Wichman-Wishstar (Redefine Technologies): Senior Space Systems Engineer, HAI and driver development (120 hours)
- Black Swift electrical engineer: Hardware platform and driver development (120 hours)
- Estimated hours for key personnel partially redacted in document

**Facilities:** Red Canyon Denver office and Black Swift Boulder office; no government facilities required

**Subcontractors (30% of Phase I work):**
- **Black Swift Technologies (Boulder, CO):** UAV autopilot hardware/software expertise, 100+ publications, provides demonstration hardware and HAI support
- **Redefine Technologies (Boulder, CO):** Engineering firm specializing in TRL advancement, spacecraft design, embedded programming, reconfigurable avionics; provides HAI and driver support

## Phase II Objectives (TRL Target: 4 at end of Phase I)

- Develop and demonstrate system in relevant environment using operational airframe
- Define and document Planning Interface formally
- Develop or obtain ground station planning software utilizing PLI
- Define mission and associated activities
- Configure PLEXIL for mission execution with fault response logic
- Develop/acquire and integrate functional Apps for demonstration
- Acquire and configure demonstration airframe with necessary hardware subsystems

## Key Results & Technical Findings

*This is a proposal document, not a completed project report. No results are available.*

## Notable Details

### Competitive Advantages Over Current State of the Art
- **Current industry model:** Custom architectures per hardware configuration; mission-by-mission software development (e.g., DJI, 3D Robotics, Predator each require unique software)
- **FLAVA advantages:**
  - Software components developed independent of specific missions
  - All apps interface through common infrastructure
  - Hardware upgrades require only driver modification
  - Reusable component libraries reduce verification time/cost
  - Commercial manufacturers can develop mission-independent components
  - Standardized interfaces enable one consolidated marketplace vs. fragmented per-platform markets

### Cost/Schedule Benefits Claimed
- Significantly reduced software development, upgrade, and maintenance costs
- Enables missions currently cost/time-prohibitive
- Faster mission launch through component reuse
- Reduced certification costs (single certification vs. per-airframe customization)
- Commercial hardware and software developers can provide products at lower costs

### Regulatory/Market Context
- FAA increasingly regulating UAV operations in commercial airspace
- Pressure for components certifiable once for reuse across multiple airframes
- Commercial UAV market explosion anticipated; need for common framework like internet's OSI model

### Related Prior Work (Program History)
- Red Canyon: 16 years developing spacecraft for NASA; Phase I & II SBIR with JPL (mentioned in comments); I-SPAREX autonomous spacecraft control Phase II (NNX13CA26P); AFRL Phase I & II work (mentioned in comments)
- Jack Elston (Black Swift): Ph.D. on complex meshed UAS networks and control algorithms for tornado sampling; Tempest sUAS design (first UAV intercept of tornadic supercell, VORTEX2 project); NSF Postdoctoral Fellowship on in-situ atmospheric thermodynamics with sUAS; led international comparison of four prolific sUAS platforms; 100+ publications; COA application and flight experiment expertise
- Steven Wichman-Wishstar: Autonomous spacecraft models for CASPER/ASPEN; Spacecraft Command Language (SCL) for Three Corner Satellite (3CS); master's from Stanford Aeronautics/Astronautics
- Alec Forsman: Undergraduate research on CubeSats, UAV agriculture applications; pursuing master's in Aerospace Engineering at University of Colorado

### Document Status
This is a draft proposal with editorial comments from review team embedded. Numerous sections have budget hours, subcontractor commitments, and related project details marked for confirmation before final submission. Document indicates this was a completed proposal (located in "Completed/Inactive/Unsubmitted Projects" folder), suggesting it may not have been awarded or was shelved prior to submission.

### Key Differentiators from Existing Autopilot Frameworks
- Open-source stack (cFE, OSAL, PLEXIL) vs. proprietary frameworks (ArduPilot, DJI)
- Components developed for one platform become interchangeable across all platforms supporting FLAVA
- Layered architecture enables distributed systems (PL on ground, or on-board for autonomous missions)
- NASA technology integration (proven components with flight heritage)