# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- Type: Phase I SBIR Proposal
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Subtopic A2.02 (Enabling Aircraft Autonomy); ProSAMS Proposal Number A2.02-1017
- Date: 2025-04-08
- BST Products/Systems Referenced: SwiftCore Flight Management System, S2 UAS
- Key Personnel: Dr. Jack Elston (PI), Dr. Maciej Stachura, Ben Busby

## Executive Summary
BlackSwift Technologies proposes SwiftCore, a modular and hierarchical avionics platform for UAS that addresses limitations of traditional monolithic flight control systems. The system uses independent, intelligent hardware nodes connected via an open, message-based communication framework with embedded containers and a "safe sandbox" for secure testing of experimental modules. This approach enables hot-swappable components, easier technology integration, and support for machine learning and multi-vehicle coordination capabilities required by NASA's autonomy requirements.

## Technical Approach

**SwiftCore Architecture:**
- Layered, hierarchical design with independent, intelligent hardware nodes
- Open, message-based communication framework (enabling interoperability)
- Five functional layers:
  1. Direct sensor/actuator access
  2. Control loop commanding
  3. Basic state sensing and navigation
  4. Applied machine learning and vision processing
  5. Multi-vehicle coordination
- Embedded containers for modularity and secure, reliable testing of experimental modules
- "Safe sandbox" concept: overrides unsafe commands during experimental testing to maintain safety
- Hot-swappable component design for easier technology integration

**Phase 1 Technical Objectives:**
- Define and validate the layered architecture
- Adapt and refine SwiftCore for the proposed approach
- Develop the safe sandbox capability
- Demonstrate ML-enabled control loop tuning

**Work Plan:**
- Define architectural layers
- Refine SwiftCore implementation
- Develop safe sandbox functionality
- Implement and demonstrate ML-based tuning
- Testing and validation at each step

## Products & Capabilities Described

**SwiftCore Flight Management System**
- What it is: A modular, hierarchical avionics platform designed for UAS flight control and management
- Proposed use: Baseline system for integrating autonomous decision-making, machine learning, multi-vehicle coordination, and experimental control modes while maintaining safety and reliability
- Key differentiators: True modularity (vs. tightly coupled architectures), embedded containerization, safe sandbox for secure experimental testing
- Architecture: Layered design with independent nodes, open message-based communication

**S2 UAS**
- Mentioned as existing BST asset that will be available for development and testing activities

## Use Cases & Applications

- **NASA Autonomy Requirements**: Addresses barriers in cognition, decision-making, communication, fault tolerance, and validation for autonomous aircraft systems
- **NDAA Compliance**: System designed to support NASA requirements for NDAA-compliant systems
- **Machine Learning Integration**: ML-enabled control loop tuning and vision processing capabilities
- **GPS-Denied Navigation**: Builds on previous research in GPS-denied environments
- **Multi-Vehicle Coordination**: Layered architecture supports coordinated multi-UAS operations
- **Government and Commercial Markets**: System has potential applications in both sectors

## Notable Details

- **Competitive Advantage**: SwiftCore's true modularity with embedded containers and safe sandbox concept differentiates it from existing monolithic avionics systems
- **Prior Experience**: Proposal builds upon previous NASA and NOAA-funded projects involving machine learning, machine vision, and GPS-denied navigation
- **Facilities**: BlackSwift Technologies operates a UAS development and testing facility in Boulder, CO
- **Planned Acquisitions**: Phase 1 will acquire a new NDAA-compliant ML-enabled single board computer for integration
- **Flight History**: SwiftCore has been flight-tested in previous NASA and NOAA missions, indicating operational maturity
- **Economic Benefits**: Proposal emphasizes potential for reduced costs and improved efficiency in autonomous UAS operations