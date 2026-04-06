# Statement of Work: Virtual Redundancy for Safety Assurance in the Presence of Sensor Failures

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: NASA (via Barron Associates, prime contractor)
- Program/Solicitation: SBIR Phase I subcontract under Barron Associates
- Date: 2014-12-16
- BST Products/Systems Referenced: Tempest vehicle, Black Swift autopilot board, Virtual Sensor Toolkit
- Key Personnel: Jack Elston (last editor)

## Executive Summary
Black Swift Technologies proposes to develop and implement virtual sensor redundancy for the Tempest vehicle to improve safety assurance in the presence of sensor failures. The work involves applying BST's Virtual Sensor Toolkit to identify critical sensors, develop dynamics models and noise characterization, implement virtual sensors, and port the implementation to BST's autopilot hardware for real-time operation.

## Technical Approach

### Task 1: Virtual Sensor Toolkit Application
- Identify subset of Tempest flight control sensors benefiting most from virtual redundancy, considering sensor failure susceptibility, impact on system stability/performance, and Barron Associates input
- Identify anticipated failure modes for selected sensors
- Construct vehicle dynamics model conforming to Virtual Sensor Toolkit interface specifications, including model simplifications for computational efficiency
- Develop process noise and measurement noise models using toolkit-provided tools based on simulation and experimental data
- Generate virtual sensor implementation using toolkit automation

### Task 2: Toolkit Feedback
- Provide recommendations for Virtual Sensor Toolkit software and documentation improvements based on implementation experience

### Task 3: Testing Support
- Deliver virtual sensor implementation to Barron Associates
- Provide Tempest flight data to support testing

### Task 4: Real-Time Implementation
- Port virtual sensor implementation to Black Swift autopilot board
- Execute hardware-in-the-loop simulation testing

### Task 5: Program Management
- Document technical work for interim and final reports to NASA

## Products & Capabilities Described

**Virtual Sensor Toolkit**
- BST-developed software tool for automated virtual sensor implementation
- Provides interface specifications for dynamics models
- Includes tools for process/measurement noise model development
- Automates implementation generation from input models

**Tempest Vehicle**
- BST unmanned aircraft platform
- Flight control system with multiple sensors
- Existing simulation model available for adaptation

**Black Swift Autopilot Board**
- Real-time capable autopilot hardware
- Target platform for porting virtual sensor implementation
- Supports hardware-in-the-loop simulation

## Use Cases & Applications
- Aircraft sensor fault tolerance and safety assurance
- Closed-loop system stability maintenance during sensor failures
- Virtual redundancy as alternative to hardware redundancy

## Deliverables

**Year 1**
- Documentation to support interim reports

**Year 2**
- Documentation to support interim reports
- Tempest Flight Data
- Tempest Dynamic Model
- Documentation to support final report

## Notable Details
- Work is subcontracted through Barron Associates (prime) to NASA
- Leverages existing Tempest simulation models and flight data
- Virtual Sensor Toolkit appears to be a reusable BST technology platform applied to new vehicle/mission
- 2-year project timeline
- Emphasizes computational efficiency of vehicle dynamics models for real-time autopilot implementation