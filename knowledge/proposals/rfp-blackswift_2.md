# Virtual Redundancy for Safety Assurance in the Presence of Sensor Failures

## Document Metadata
- Type: Request for Proposal (RFP)
- Client/Agency: Barron Associates, Inc. (prime contractor); NASA (ultimate client)
- Program/Solicitation: RFP #P14-53-01; appears to be SBIR Phase II
- Date: December 12, 2014 (issued); Deadline: December 16, 2014
- BST Products/Systems Referenced: Tempest vehicle, Black Swift autopilot board, Virtual Sensor Toolkit
- Key Personnel: Jack Elston (last editor); Alec Bateman (Barron Associates technical contact)

## Executive Summary
This RFP requests Black Swift Technologies to develop a virtual sensor implementation for the Tempest UAV using a Virtual Sensor Toolkit, providing redundancy for flight control system sensors in the event of failures. The work spans 24 months with a Phase II effort ceiling of $40,000 and includes hardware-in-the-loop testing and real-time implementation on BST autopilot hardware.

## Technical Approach

The project follows a structured five-task approach:

**Task 1: Virtual Sensor Development**
- Apply Virtual Sensor Toolkit to develop virtual sensor for Tempest vehicle
- Identify subset of flight control system sensors where virtual redundancy provides greatest benefit
- Selection criteria: sensor failure susceptibility, impact on closed-loop system stability/performance, Barron Associates input
- Identify anticipated failure modes for selected sensors
- Construct vehicle dynamics model conforming to toolkit interface specifications (may include simplifications for computational efficiency)
- Develop process noise and measurement noise models using toolkit tools and empirical data
- Generate virtual sensor implementation using toolkit automation

**Task 2: Toolkit Feedback**
- Provide recommendations for Virtual Sensor Toolkit software and documentation improvements based on implementation experience

**Task 3: Testing Support**
- Deliver virtual sensor implementation to Barron Associates
- Provide Tempest flight data for testing

**Task 4: Real-Time Implementation**
- Port virtual sensor implementation to Black Swift autopilot board
- Execute hardware-in-the-loop simulation testing

**Task 5: Program Management**
- Provide technical documentation to support Barron Associates' interim and final reports to NASA

## Products & Capabilities Described

**Tempest Vehicle**
- UAV platform for which virtual sensor system is being developed
- Has flight control system with multiple sensors subject to failure
- Existing simulation model available for adaptation

**Virtual Sensor Toolkit**
- Software toolkit for developing virtual sensor implementations
- Provides interface specifications for dynamics models
- Includes tools for noise model development
- Enables automated implementation generation from defined inputs
- Requires documentation improvements (feedback expected)

**Black Swift Autopilot Board**
- Real-time autopilot hardware platform capable of running virtual sensor algorithms
- Target platform for final hardware-in-the-loop testing and deployment

## Use Cases & Applications

- **Flight Control System Redundancy**: Providing virtual sensor redundancy for critical flight control sensors to maintain stability and performance in the event of sensor failures
- **Safety Assurance**: Ensuring aircraft safety when physical sensors fail through model-based virtual sensor estimation

## Work Effort Distribution
- Year 1: 20% of effort
- Year 2: 80% of effort
- Total Phase II: $40,000 (Firm Fixed Price)
- Period of Performance: 24 months, estimated start May 1, 2015
- Travel: None expected

## Notable Details

- This is a subcontract to Barron Associates under an apparent NASA SBIR Phase II program
- The Virtual Sensor Toolkit is a proprietary BST or partner tool being actively developed and improved
- BST has existing Tempest flight data available
- The work emphasizes both algorithm development and real-time implementation capability
- Hardware-in-the-loop testing validates the virtual sensor performance before potential flight testing
- Cost proposal required with detailed labor, equipment breakdowns by contract year
- 180-day proposal validity period required