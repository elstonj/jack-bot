# Virtual Redundancy for Safety Assurance in the Presence of Sensor Failures

## Document Metadata
- Type: Budget Justification (SBIR Phase I Subcontract)
- Client/Agency: U.S. Army (via Barron Associates as prime contractor)
- Program/Solicitation: Army Phase I SBIR (subcontract through Barron Associates)
- Date: December 16, 2014
- BST Products/Systems Referenced: Tempest vehicle, BlackSwift autopilot board, Virtual Sensor Toolkit
- Key Personnel: Jack Elston (last editor, implied Principal Investigator)

## Executive Summary
Black Swift Technologies proposed a 320-hour effort to apply a Virtual Sensor Toolkit to the Tempest vehicle to develop virtual redundancy capabilities that would provide safety assurance when physical sensors fail. The work spans two years and includes sensor selection, dynamics modeling, virtual sensor implementation, testing, and real-time deployment on BST's autopilot hardware.

## Technical Approach
The project follows a structured methodology:

1. **Sensor Selection & Failure Analysis** (16 hours): Identify which flight control system sensors would benefit most from virtual redundancy by evaluating failure susceptibility, impact on system stability/performance, and incorporating Barron Associates' input.

2. **Vehicle Dynamics Modeling** (60 hours): Construct a dynamics model suitable for the virtual sensor system, primarily by restructuring existing Tempest simulation models to conform to the Virtual Sensor Toolkit's interface specification. May include model simplifications for computational efficiency.

3. **Noise Modeling** (20 hours): Develop models of process noise and measurement noise for the vehicle dynamics, leveraging toolkit tools and analysis of simulation/experimental data.

4. **Virtual Sensor Implementation** (20 hours): Generate the virtual sensor system implementation using the toolkit's automation capabilities.

5. **Toolkit Feedback** (40 hours): Provide recommendations for improvements to Virtual Sensor Toolkit software and documentation based on operational experience.

6. **Testing & Validation** (86 hours): Support testing of the implemented virtual sensor system, deliver implementation and flight data to Barron Associates, and conduct hardware-in-the-loop simulation exercises.

7. **Real-Time Porting** (40 hours): Port the virtual sensor implementation to a BlackSwift autopilot board for operational deployment.

8. **Program Management** (20 hours): Provide technical documentation supporting Barron Associates' interim and final reports to NASA.

## Products & Capabilities Described

**Virtual Sensor Toolkit**
- A software framework developed (likely by Barron Associates or collaboratively) for rapid virtual sensor system development
- Provides interface specifications for dynamics models
- Includes tools for noise model development
- Offers high degree of implementation automation
- Documented software with improvement recommendations from BST's experience

**Tempest Vehicle**
- BST's unmanned air system serving as the test platform
- Has an existing simulation model for redundancy architecture analysis
- Equipped with flight control systems dependent on multiple sensors
- Generates flight data for validation and noise model development

**BlackSwift Autopilot Board**
- Hardware platform for real-time virtual sensor implementation
- Capable of executing virtual sensor algorithms in operational flight control loops

## Use Cases & Applications

**Primary Application**: Flight safety and system resilience for unmanned aerial vehicles through virtual sensor redundancy, addressing scenarios where physical sensors are susceptible to failure. The focus is on sensors critical to closed-loop flight stability and performance.

**Operational Context**: Intended to enhance autonomous vehicle safety by providing fallback sensor capability when primary sensors fail, improving mission reliability for operations where sensor failures could be catastrophic.

## Effort Breakdown

| Phase | Hours | Year 1 | Year 2 |
|-------|-------|--------|--------|
| Sensor Selection & Modeling | 156 | 128 | 28 |
| Virtual Sensor Development | 40 | 0 | 40 |
| Toolkit Feedback | 40 | 0 | 40 |
| Testing & Validation | 84 | 0 | 84 |
| Real-Time Implementation | 80 | 0 | 80 |
| Program Management | 20 | 0 | 20 |
| **Total** | **320** | **64** | **256** |

## Notable Details

- **Subcontract Structure**: BST was the subcontractor to Barron Associates (prime), suggesting this was part of a larger Army SBIR effort with reporting to NASA (as referenced in documentation requirements)
- **Proprietary Labor Rates**: Document notes labor rates were proprietary and disclosed to U.S. Government only upon request
- **Leverage of Existing Assets**: Project leveraged BST's existing Tempest simulation and flight data rather than building from scratch
- **Integration Focus**: Strong emphasis on porting validated simulation-based virtual sensors to operational autopilot hardware (real-time constraint)
- **Year 1-2 Distribution**: Heavily back-loaded to Year 2 (80% of effort), with Year 1 focused on foundational modeling and selection tasks, Year 2 on implementation, testing, and deployment