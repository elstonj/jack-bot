# 2025 Multi-UAS Proposal

## Document Metadata
- Type: Proposal
- Client/Agency: NOAA (Joe Cione, NOAA Federal)
- Program/Solicitation: NOAA/WPO Hurricane operations (2020 Hurricane Project context)
- Date: Created 2024-01-24; Modified 2024-08-22
- BST Products/Systems Referenced: S0 UAS, SwiftCore (Flight Management System), ground station, tablet-based user interface, radio systems
- Key Personnel: Joe Cione (NOAA Federal, last editor)

## Executive Summary
Black Swift Technologies proposes to develop multi-UAS command and control capabilities enabling simultaneous operation of two or more S0 aircraft from a single ground station and operator. The system will maintain existing S0 architecture and communications range (150 nautical miles) while reducing operator overhead through automation similar to AVAPS dropsonde deployment paradigms. Development and testing will occur over 12 months with a budget of $120,000.

## Technical Approach
- **Single operator/single ground station control**: Develop mechanisms to operate multiple S0 vehicles simultaneously from one location, following the operational model of AVAPS dropsondes where an aircraft voice officer (AVO) sets initial conditions and can deploy multiple uncrewed aircraft sequentially
- **Flight pattern modifications**: Enable in-flight changes to flight patterns and desired altitudes with minimal operator overhead due to infrequent adjustment needs
- **Radio system expansion**: Upgrade ground station with additional radios (maintaining same cable interfaces and antenna systems within P3 platform) to support multi-vehicle operations while preserving 150 nautical mile communication range
- **SwiftCore upgrades**: Modify the SwiftCore Flight Management System to enable multi-vehicle coordination and control
- **Simulation environment**: Update BST simulation tools to support multi-UAS mission development and testing

## Products & Capabilities Described

### S0 UAS
- Operational unmanned aircraft successfully deployed into tropical storms during 2024 season
- Proposed use: Primary platform for multi-vehicle simultaneous hurricane observations
- Capability baseline: Individual aircraft operates with 150+ nautical mile range via radio link

### SwiftCore (Flight Management System)
- Current system manages individual S0 flights
- Proposed enhancement: Multi-UAS command architecture to coordinate two or more simultaneous vehicles from single ground station
- Maintains tablet-based user interface

### Ground Station
- Currently supports single S0 operation
- Proposed modification: Installation of additional radios to manage multiple simultaneous aircraft while maintaining 150 nmi communication range
- Maintains existing P3 cable interfaces and antenna systems

## Use Cases & Applications
- **Hurricane sampling**: Primary application—simultaneous targeted observations from multiple locations within tropical storms
- **Multi-point data collection**: Ability to observe different regions or altitudes within a storm simultaneously
- **Sequential deployment**: Initial AVAPS-style model where operator sets conditions and deploys aircraft sequentially, then manages them collectively
- **Scalability pathway**: System designed to expand from 2 aircraft to larger numbers (testing with up to 4 vehicles)

## Testing & Evaluation Plan
- **Simulation testing**: Updated BST simulation environment for multi-UAS mission development and validation
- **Local facility testing**: Demonstration of dual aircraft simultaneous flights with SwiftCore at BST flight facility to reduce overhead
- **Radio configuration testing**: Various configurations evaluated to support 150+ nmi range with up to 4 simultaneous vehicles
- **Potential P3 integration**: If clear air testing funding becomes available separately, testing could be incorporated into P3 flights
- **Avionics firmware**: Updates required for flight testing implementation

## Project Budget & Timeline
- **Duration**: 12 months
- **Budget breakdown**:
  - SwiftCore FMS updates: $42,000
  - Multi-UAS simulation development: $26,000
  - Avionics firmware updates: $22,000
  - Local flight testing (10 days): $15,000
  - Hardware (additional radios, development boards): $7,000
  - Overhead/project management: $8,000
  - **Total: $120,000**
- **Deliverables**: Monthly progress updates and final presentation demonstrating objectives achieved

## Notable Details
- **Risk mitigation**: Proposal prioritizes reuse of existing S0, ground station, and user interface to reduce cost and programmatic risk
- **Operational simplification**: Designed to minimize operator workload despite controlling multiple vehicles—single operator, single ground station
- **Platform integration**: Hardware and communications architecture designed to integrate with existing P3 aircraft installation
- **Incremental development**: Phase 1 focuses on dual-vehicle operation with intentional scalability to 4+ vehicles
- **NOAA partnership**: Directly supports NOAA WPO hurricane observation mission; builds on successful 2024 S0 seasonal deployments