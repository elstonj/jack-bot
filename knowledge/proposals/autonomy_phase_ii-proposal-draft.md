# Autonomy Phase II Proposal – DRAFT

## Document Metadata
- **Type:** NASA Phase II SBIR proposal
- **Client/Agency:** NASA (Aeronautics Research Mission Directorate – ARMD; Convergent Aeronautics Solutions program)
- **Program/Solicitation:** NASA SBIR Phase II (autonomy-focused)
- **Date:** April 8–9, 2026 (draft status)
- **BST Products/Systems Referenced:** SwiftCore Flight Management System
- **Key Personnel:** Beck Cotter (last editor)
- **Status:** DRAFT – incomplete; template sections unfilled

## Executive Summary
Black Swift Technologies proposes to develop advanced autonomy capabilities built on the SwiftCore Flight Management System, a modular, NDAA-compliant avionics platform designed for rapid integration and testing of novel UAS control and coordination features. The innovation addresses NASA's need for reconfigurable, rapidly deployable autonomy solutions for research applications including BVLOS operations and multi-UAS coordination. SwiftCore's hierarchical, containerized architecture with embedded "safe sandbox" safety features enables accelerated innovation cycles while maintaining certification readiness.

## Technical Approach

**Core Innovation: SwiftCore Modular Architecture**
- Fully modular, hierarchical avionics system built around a **publisher-subscriber (pub/sub) message-based communication framework** with service discovery
- Hardware nodes (sensors, actuators, autopilots, flight computers) are **hot-swappable** and independently replaceable
- Standardized message types distributed over a **high-bandwidth, real-time communication bus**
- Individual embedded control layers (sensor-actuator interfaces through multi-vehicle coordination and ML-based vision/control) can be upgraded or replaced independently without system-wide modifications

**Embedded Containerization**
- Leverages embedded container strategies (referenced: Wind River embedded container solutions)
- Enables experimental modules (e.g., ML-based controllers) to run securely on dedicated compute nodes
- Supports rapid testing, validation, and deployment while simplifying certification overhead
- Independent validation of software configurations

**"Safe Sandbox" Concept**
- Monitors commands from external or experimental components
- Automatically overrides control if predefined safety thresholds are breached
- Reverts to certified, trusted avionics layers
- Critical for complex NASA missions (BVLOS, multi-UAS coordination)

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is:** An NDAA-compliant, flight-proven avionics platform with modular, hierarchical architecture
- **Key advantages over conventional monolithic UAS avionics:** Eliminates need for system-wide modifications and lengthy revalidation when adding/changing components; significantly reduces certification overhead
- **Proposed use in this context:** Foundation for Phase II autonomy research; enables rapid integration and testing of advanced autonomy features for NASA missions
- **Embedded control layers:** Ranges from direct sensor-actuator interfaces to complex multi-vehicle coordination and ML-based vision/control systems
- **Communication framework:** Open, message-based pub/sub model with service discovery

## Use Cases & Applications

**NASA Mission Scenarios:**
- Beyond Visual Line-of-Sight (BVLOS) flight operations
- Multi-UAS coordination and swarm operations
- Complex autonomous research missions aligned with NASA ARMD and Convergent Aeronautics Solutions (CAS) program objectives

**Existing BST Application Areas (referenced in facilities description):**
- Environmental monitoring
- Wildfire detection
- Hurricane observation
- Atmospheric profiling

## Key Results
No results section provided; this is a proposal, not a report. Technical Objectives and Work Plan sections are unfilled templates.

## Notable Details

**Competitive Positioning:**
- SwiftCore explicitly addresses NASA's stated need for "modular and rapidly reconfigurable solutions" (NASA CAS 2024)
- Directly responds to NASA ARMD challenges: rapid technology infusion, robust fault tolerance, streamlined integration
- Flight-proven system with NDAA compliance already established

**Facilities:**
- State-of-the-art facility in Boulder, Colorado
- Dedicated UAS integration lab with sensor calibration workspace
- Real-time data processing and mission planning capabilities
- Rapid iteration and platform adaptation capacity

**Document Status:**
This is a **DRAFT** with multiple unfilled template sections:
- Part 3: Technical Objectives (blank)
- Part 4: Work Plan (blank)
- Part 5: Related R/R&D (blank)
- Part 6: Key Personnel and Bibliography (blank)
- Part 7: Commercialization and Business Plan (blank)
- Part 9: Subcontractors and Consultants (blank)
- Part 10: Related Awards (blank)
- Budget section incomplete
- Briefing chart placeholder only

**Referenced Literature/Standards:**
- Elston 2011, Argrow 2015, Scharf 2024 (SwiftCore architecture references)
- Wind River 2024 (embedded container solutions)
- NASA CAS 2024, NASA ARMD 2024