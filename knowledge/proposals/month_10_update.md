# VTOL Project Update

## Document Metadata
- Type: Project status update presentation
- Client/Agency: Creare
- Program/Solicitation: 2019 VTOL Autopilot
- Date: March 2020
- BST Products/Systems Referenced: Double Eagle (VTOL platform)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This Month 10 update documents progress on a VTOL autopilot project for Creare, including completed navigation controller implementations, flight testing fixes, and schedule adjustments due to travel restrictions. The project remains on track for completion by end of May 2020.

## Technical Approach
- Implemented mixed reduced state and full state controller for VTOL navigation
- Fixed navigation state machine with p-value correction (0.4) to address tracking issues
- Enhanced waypoint-based flight planning with orbit and hover transition capabilities
- Developed mapping logic and improved landing approach procedures
- Implemented wind-aware path selection for return-to-land operations

## Products & Capabilities Described

### Double Eagle (VTOL Platform)
- Vertical takeoff and landing capable aircraft
- Supports autonomous flight phases: takeoff, forward transition, orbit, waypoint navigation, hover transitions, return-to-landing, and automated landing
- Being upgraded/integrated with new avionics suite
- Capable of parachute deployment systems
- Testing envelope includes flight in higher wind conditions

## Use Cases & Applications
- Autonomous VTOL flight operations with complex flight plans
- Multi-waypoint navigation with orbital patterns
- Autonomous landing procedures
- Wind-aware return-to-base operations
- Small prototype testing for higher wind conditions

## Schedule Status (as of March 2020)
- **Week 1 (by next Monday):** Ship old Double Eagle; integrate avionics into new Double Eagle; small prototype high-wind test
- **Week 2:** Double Eagle ground/hover tests; repeated small prototype tests
- **Week 3:** Double Eagle parachute testing; timeline discussion
- **Week 4:** Double Eagle full flight envelope testing
- **Overall:** Testing completion targeted for end of April; project completion by end of May 2020
- **Note:** Final test demo relocated to Colorado due to travel restrictions (likely COVID-related, given March 2020 date)

## Notable Details
- Smooth transitions achieved between multiple flight plans (mapping, square orbit, landing)
- 3D UI visualization implemented for flight planning and monitoring
- Project showed sufficient progress to maintain end-of-May completion despite logistical disruptions