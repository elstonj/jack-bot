# Week Four Summary: Mustang Project - Effort 1

## Document Metadata
- Type: Weekly progress report
- Client/Agency: By Light (ByLight)
- Program/Solicitation: Mustang Project - Effort 1
- Date: 31 October 2025
- BST Products/Systems Referenced: Chilli (COTS platform being modified), dual motor design, custom fuselage/empennage design
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is developing a modified aircraft platform based on the SoaringUSA Chilli GPS (Double Carbon version) for ByLight to meet specific mission requirements. Week Four focused on completing the dual motor mounting design, progressing the Chilli build-up with servo installation, and initiating CAD design of a custom lighter, more durable fuselage/empennage to replace the stock airframe while retaining the wings.

## Technical Approach

### Dual Motor Design
- **Configuration**: Twin rotors mounted symmetrically along center wing, separated by 2 feet (aligned with inner flap servo pocket for alignment reference)
- **Motor Pylon**: MJF 3D-printed component bonded permanently to wing surface; houses wiring and serves as structural hard point without modifying wing structure
- **Motor Pod**: Bolt-on assembly (uses plastic screws for breakaway capability during rough landings) containing:
  - Brushless motor
  - Electronic speed controller (ESC) with heat-sinking and free-stream cooling
  - 5V regulator
  - Telemetry-capable actuator board
  - 3-in-1 actuator board
  - All contained within carbon fiber tube
  - Components mounted on damped, isolated tray to protect from high-vibration environment

### Performance Specifications
- Target cruise speed: 30 m/s
- Continuous power requirement: 400-500W combined (both motors)
- Motor control via telemetry actuator board with CAN bus communication
- RPM and critical performance metrics telemetry-capable

### Chilli COTS Platform Selection
- Aircraft: SoaringUSA Chilli GPS (Double Carbon version)
- Wingspan: 15.25 feet (chosen for range efficiency and wing loading stability)
- Mission requirement: 400 km range
- Components retained from COTS: Wings (deemed excellent for mission)
- Components being replaced: Fuselage and empennage (custom design in progress)

## Products & Capabilities Described

### Chilli Aircraft (Modified COTS)
- **What it is**: Consumer off-the-shelf sailplane platform serving as development/prototyping vehicle
- **Usage in project**: Base airframe for extended-range mission with dual-motor propulsion
- **Current status**: Wing servos and linkages installed and tested; elevator servo installed; rudder servo pocket created

### Custom Fuselage/Empennage Design
- **Design approach**: Two carbon fiber tubes—one as main fuselage body, one as tail boom
- **Key features**:
  - Outer carbon fiber tube shell slides entirely off internal core for easy access to avionics, firmware updates, and CG adjustment
  - Single main internal core houses avionics and batteries
  - Emphasis on light weight, structural strength, and rapid adjustability
  - Designed to accommodate future modifications as mission requirements evolve
- **Current maturity**: Intermediate CAD phase; noted as requiring refinement based on real flight data

## Use Cases & Applications
- **Mission type**: Long-endurance flight (400 km range requirement)
- **Flight profile**: Cruise at 30 m/s with climb and dash capability
- **Operational requirements**: Support for multiple payloads (specific payloads not detailed in this report)

## Key Results/Progress
- **Completed**: Dual motor mounting design finalized; all motor components ordered (delivery expected ~Thursday of following week)
- **In progress**: Bench-top testing and wiring preparation; Chilli servo installation and integration
- **Upcoming**: Flight test of Chilli Double Carbon to gather real flight data for battery capacity calculations and fuselage design refinement

## Notable Details
- BST operators providing direct feedback to inform design iterations
- Plastic screws on motor pods designed to break away during rough landings, protecting costlier wing structure
- Motor selection based on propeller manufacturer analysis tools and previous experience
- New fuselage design prioritizes internal modular structure allowing easy access and reconfiguration
- Specific avionics and payload selections still pending (noted as "to be determined")
- Next week's report (Week 5) expected to show more refined fuselage concept
- Future design priorities: finalizing avionics, finalizing both payloads, designing secure wing attachment mechanism