# Temporary White Paper: Te-UAS/GV Operating Picture and Safe Flight Systems

## Document Metadata
- Type: White paper / SBIR proposal framework document
- Client/Agency: Department of Defense
- Program/Solicitation: SBIR (Small Business Innovation Research)
- Date: 2021-09-20
- BST Products/Systems Referenced: Te-UAS (Tactical micro-Unmanned Aerial System), GV (Ground Vehicle)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This document outlines design goals for creating sensor configurations and software algorithms to generate a common operating picture and enable safe autonomous flight of a small UAS (Te-UAS) while a ground vehicle (GV) is in motion. BST proposes using machine-vision sensing fused with standard onboard UAS sensors to enable autonomous path planning and obstacle avoidance in urban, suburban, and rural environments.

## Technical Approach
- **Primary method**: Machine-vision sensing integrated with standard onboard sensors (TRL 6 or greater)
- **Application**: Autonomous navigation and path computation for Te-UAS operating from a moving ground vehicle
- **Basis**: Leverages BST's existing capabilities developed through prior machine-vision projects for commercial UAS safety and performance
- **Key constraints**: 
  - Te-UAS must operate safely while GV travels up to 45 mph
  - All sensors must be currently procurable and feasible to mount on designated platforms
  - No fixed sensor count requirement; cost optimization expected

## Products & Capabilities Described

### Te-UAS (Tactical micro-Unmanned Aerial System)
- Small tactical UAS platform
- Must operate safely while launched/recovered from a moving ground vehicle
- Requires real-time autonomous navigation in varied environments

### Common Operating Picture (COP) Software
- Must tolerate and/or exclude poor quality data (temporal or spatial degradation)
- Requires cyber resiliency
- Must be scalable for additional sensor modalities
- Fuses machine-vision data with standard UAS onboard sensors

## Use Cases & Applications
- **Urban environments**: Autonomous UAS operations in city settings
- **Suburban environments**: Mixed density operations
- **Rural environments**: Open area operations
- **Mobile platform operations**: GV-launched UAS providing persistent awareness while vehicle is in motion (speeds up to 45 mph)

## Document Structure/Proposal Framework
This white paper provides the template/guidance for SBIR proposal response, covering required sections:
1. Problem or Need Statement
2. State of Technology
3. Proposed Approach
4. Risks and Mitigation
5. Prior Work
6. Success Metrics

## Notable Details
- **Prior work**: BST has conducted multiple projects and internal R&D (iR&D) on machine-vision-based safety and performance improvements for commercial UAS
- **Technology readiness**: Focus on TRL 6+ technologies, emphasizing near-term implementability
- **Cost consideration**: Explicit acknowledgment that proposals must balance capability with cost-effectiveness
- **Performance requirement**: Specific operational constraint of 45 mph GV speed establishes technical baseline
- **Defense relevance**: Framed as addressing Department of Defense tactical needs for mobile UAS operations

## Assessment
This is a preliminary white paper establishing the problem statement and approach framework for an SBIR proposal response. It is relatively brief and does not contain detailed technical specifications, performance data, or complete statement of work—those would be developed in the full proposal submission. The document confirms BST's existing expertise in machine-vision UAS applications and indicates intent to apply that capability to the specific challenge of GV-integrated operations.