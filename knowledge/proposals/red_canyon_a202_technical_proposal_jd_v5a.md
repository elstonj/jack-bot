# Red Canyon Software FLAVA SBIR Phase I Proposal

## Document Metadata
- **Type:** SBIR Phase I Technical Proposal
- **Client/Agency:** NASA (Small Business Innovation Research program)
- **Program/Solicitation:** SBIR Topic #A2.02
- **Date:** 2016-01-29
- **BST Products/Systems Referenced:** Black Swift autopilot hardware platform, Black Swift sensor board
- **Key Personnel:** Jay David (JD) Marks (PI, Red Canyon); Steven Wichman-Wishstar (Redefine Technologies); Black Swift engineer (unnamed); Red Canyon SW Engineer (unnamed/Alec mentioned as intern)

## Executive Summary
Red Canyon Software proposes FLAVA (Four Layered Aerial Vehicle Architecture), a standardized software architecture with open-source interfaces for UAVs to reduce development costs and timelines. The proposal demonstrates feasibility of a four-layer architecture using NASA open-source tools (CoreFlight Executive for operations layer, OSAL for OS abstraction, PLEXIL for plan execution) that would enable modular development of mission-specific components and hardware independence. This addresses NASA's need to reduce UAV software development costs currently absorbed mission-by-mission.

## Technical Approach

### Layered Architecture Model
FLAVA implements a four-layer stack based on OSI networking model principles:

1. **Planning Layer (PL):** Develops high-level mission plans as sequences of activities (e.g., "take off," "fly to location XYZ," "acquire sensor data"). Plans are airframe-agnostic.

2. **Plan Execution Layer (PEL):** Translates activities into detailed operational commands specific to individual airframes. Contains Activity Execution Blocks (AEB) with airframe-specific knowledge. Interfaces with PL via Planning Layer Interface (PLI) and with OL via Plan Execution Layer Interface (PELI).

3. **Operational Layer (OL):** Executes mission-level capabilities (guidance/navigation/control, takeoff, landing, collision avoidance, communications, environmental controls) through modular applications. Uses CoreFlight Executive (cFE) as standardized infrastructure providing inter-process communication (IPC), timing, event notification, and data services. Interfaces with hardware via OS Abstraction Interface (OSAI) and Hardware Abstraction Interface (HAI).

4. **Physical Subsystems Layer (PSL):** Hardware components (sensors, actuators, motors, science instruments, transmitters). Includes communication busses (RS232, I2C, SPI, CAN, USB, RS422) and drivers that translate functional instructions to hardware-specific signals.

### Key Technology Selections

**CoreFlight Executive (cFE):** NASA GSFC open-source software framework providing standardized infrastructure for OL. Current aerospace flight heritage. Goals: platform/project-independent reusable software infrastructure and standardized product-line approach for development.

**OSAL (Operating System Abstraction Layer):** NASA GSFC open-source OS abstraction layer. Currently supports Linux, VxWorks, RTEMS, and ARINC653. Enables developers to swap/upgrade operating systems without rewriting application code.

**PLEXIL (Plan Execution Interchange Language):** NASA Ames/JPL/Carnegie Mellon open-source plan execution suite. Originally developed for Mars rover control. Supports branches, loops, time/event-driven activities, concurrent operations, sequences, and temporal constraints.

### Standardized Interface Strategy
Layer separation with well-defined interfaces allows:
- Hardware/software components developed independently of specific missions
- Commercial manufacturers to develop mission-independent products
- Distributed system implementation (Planning Layer can reside on ground or airframe)
- Hardware component upgrades requiring only driver modifications
- Reuse of previously flown components without re-verification

## Products & Capabilities Described

### Black Swift Hardware Platform
- **Autopilot hardware processor board:** Will host PEL and OL during demonstration
- **Sensor board:** Will host PSL during demonstration
- **Role in proposal:** Demonstration/test platform; provides hardware expertise and driver development support
- **Value to proposal:** Commercial UAV autopilot manufacturer providing real-world hardware context

### Software Infrastructure Components (not BST products, but integrated with BST hardware)
- **CoreFlight Executive:** OL infrastructure
- **OSAL:** OS abstraction interface between OL and PSL
- **PLEXIL:** PEL functionality and plan execution
- **Ubuntu Linux:** Development platform
- **GIT:** Configuration management

## Use Cases & Applications

### Phase I Demonstration Mission
- Proof-of-concept demonstration of FLAVA architecture using Black Swift hardware
- Canned mission plan transmitted via standardized interface
- Not fully specified in this proposal draft

### Proposed NASA Applications
- Future unmanned vehicle missions across NASA directorates
- Specific target engagement planned: Aeronautics Research Mission Directorate (ARMD), JPL Mars Rover and MSL Teams, JPL AI Group

### Broader Commercial Applications
- Commercial unmanned aerial vehicles (DJI, 3DRobotics-level applications)
- Unmanned robotic vehicles
- Unmanned underwater vehicles
- Unmanned rovers
- Dynamic onboard re-planning for autonomous systems if Planning Layer is resident on vehicle
- Modular software components marketable independent of hardware configuration

## Phase I Technical Objectives

1. Determine technical feasibility of meeting UAV mission requirements through four-layer architecture
2. Define "Load Plan" communication protocol between Planning and Plan Execution Layers
3. Define inter-process communication protocol for "execute activity" and "activity execution results" between PEL and OL
4. Define initial Hardware Abstraction Interface framework between OL and PSL
5. Demonstrate feasibility of cFE as OL infrastructure
6. Demonstrate feasibility of OSAL as OS abstraction
7. Demonstrate feasibility of PLEXIL as plan execution component in PEL

## Phase I Work Plan

### Deliverables
- Requirements documentation
- Design descriptions
- Prototype Plan Interface code
- Prototype Hardware Abstraction Interface code
- Prototype PLEXIL configuration
- Proof-of-concept demonstration
- Final comprehensive report
- Two interim bi-monthly status reports
- Kickoff and wrap-up meeting presentations

### Major Tasks
1. Define demonstration mission and required components
2. Set up software development environment (3 Ubuntu Linux workstations, Eclipse IDE, GIT)
3. Develop Plan→PEL interface
4. Configure PLEXIL activity blocks and socket/UDP interfaces
5. Configure OSAL and cFE on development workstation
6. Define and develop OL applications
7. Define HAI APIs for PSL interface
8. Develop PSL drivers for HAI
9. Create test plan
10. Execute proof-of-concept demonstration

### Phase I Team & Hours
- **Jay David Marks** (Red Canyon): PI and Senior Software Engineer, FLAVA design/development—### hours (unfilled)
- **Red Canyon SW Engineer** (unnamed/Alec?): Software Engineer, FLAVA development—### hours (unfilled)
- **Steve Wishstar** (Redefine Technologies): Senior Space Systems Engineer, HAI and driver development—120 hours
- **Black Swift Engineer** (unnamed): Hardware expertise and driver development—120 hours

**Subcontracting:** ~30% of Phase I work to Black Swift Technologies and Redefine Technologies; 193 total subcontractor hours budgeted.

### Phase I Timeline
Six-month project with tasks distributed across 6 months (specific months labeled 1-6 in task schedule). Definition and setup months 1-2; development months 2-5; testing and demonstration months 4-6.

## Key Findings & Expected Results (Phase I)

### Expected Outcome
- Technology Readiness Level (TRL) 4 at end of Phase I: "technology validated in lab environment"
- Proof-of-concept demonstration showing architecture feasibility
- Validated protocol definitions for layer interfaces

### Phase II Potential Objectives (Follow-on Work)
- Develop and demonstrate system in relevant environment with tighter operational requirements
- Survey real-time operating systems (RTEMS, VxWorks, Red Hat Real Time Kernel)
- Replace FSW simulation with full open-source CoreFlight Software suite
- Develop IPC mechanisms using VML global variables
- Potential CASPER integration for modified code development

## Notable Details

### Problem Being Addressed
Current UAV development model requires custom architecture per hardware configuration and custom software per mission. High software development, upgrade, and maintenance costs prevent many potential NASA science missions from being funded. Time and cost are "severely reducing the number of scientific missions."

### Key Innovation Claims
- **Flexibility:** Change mission hardware or requirements with reduced time/cost investment
- **Reusability:** Library-based mission configuration rather than bespoke development
- **Commercial viability:** Standardized interfaces enable commercial manufacturers to develop mission-independent products without platform customization
- **Cost reduction:** Eliminates need for custom development per mission; enables component reuse; reduces verification overhead

### Competitive Advantages Over Current State
- Software apps developed independent of specific missions
- Common infrastructure for all app interfaces
- Hardware upgrades require only driver modifications
- Standardized interfaces enable commercial market participation
- Distributed system capability (Planning Layer on ground or airframe)

### Industry Support
Letters of commitment obtained from:
- Sierra Nevada Corporation
- ADSYS Controls
Both expressing support for technical objectives and willingness to collaborate in Phase I/II.

### Subcontractor Expertise
- **Black Swift Technologies (Boulder, CO):** Commercial UAV autopilot manufacturer; 100+ publications; provides demonstration hardware and driver/HAI development support
- **Redefine Technologies (Boulder, CO):** Specializes in TRL advancement, spacecraft design, embedded programming, reconfigurable avionics, advanced systems design; provides HAI and driver support

### Open Source Strategy
All major infrastructure components are open-source (cFE, OSAL, PLEXIL) to enable industry-wide adoption without proprietary restrictions. Explicitly avoids vendor lock-in common in current autopilot providers.

### Documentation Status
This proposal is a draft with substantial incomplete sections (marked with ### for unfilled numbers, multiple editorial notes, unresolved naming conventions for Black Swift hardware, and numbered personnel assignments). The document contains extensive editorial annotations suggesting ongoing refinement and coordination needed before submission.