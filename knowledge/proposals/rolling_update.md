# VTOL Project Update

## Document Metadata
- Type: Status/Progress presentation
- Client/Agency: Creare (partnership/collaboration)
- Program/Solicitation: 2019 VTOL Autopilot project
- Date: Created 2020-04-06; Last modified 2020-09-11
- BST Products/Systems Referenced: Double Eagle VTOL platform
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This rolling update documents progress on a VTOL autopilot development project, focusing on controller improvements, saturation algorithm rewrites, and flight test results. Key work includes fixes to prototype stability, implementation of a new heading controller, and refinement of transition behavior between hover and forward flight modes.

## Technical Approach

**Saturation Code Redesign:**
- Original issue: High speed/thrust commands and low speed/thrust commands both causing saturation problems
- Solution: Rewrote saturation code to be more generic, with a desaturation algorithm that:
  - Desaturates thrust commands where possible
  - Equalizes saturation across channels when desaturation isn't sufficient
  - Example given: Tr_max = 5, Tr_min = 3 constraint
- Flight test result: New saturation code showed "much better" performance with less oscillation

**Heading Controller Reformulation:**
- Previous design: Used yaw command for heading control
- New design: Changed to heading rate command approach
- Flight tested with positive results

## Products & Capabilities Described

**Double Eagle VTOL Platform:**
- Multi-rotor VTOL capable of hover and forward flight transitions
- Recent hardware updates: New wings installed on test vehicle
- Performance characteristics measured:
  - Hover power: 264W
  - Forward flight power: 187W
  - Airspeed and altitude control: "very good"
  - Pitch response: smooth
  - Rotor performance: clean and unsaturated

## Use Cases & Applications
- VTOL hover and transition flight testing
- Multi-mode flight control (hover to forward flight transitions)

## Key Results
- Saturation algorithm flight test: Reduced oscillation, improved control behavior
- Heading controller reformulation: Successful flight test
- Airspeed/altitude performance: Excellent
- Rotor control: Clean operation without saturation

## Known Issues & Outstanding Work
- Larger than desired altitude drops during transition back to hover (both autonomous and manual modes)
- A few minor transition bugs remaining
- Hardware fit issue: Trailing edge spar with aluminum piece doesn't fit on two outboard wings (machining tolerance issue); fix identified but not yet implemented
- Rotor saturation issues previously addressed but appear resolved in latest iteration

## Notable Details
- This is an inactive/completed project (per file location)
- Represents collaborative work with Creare on autopilot development
- Demonstrates iterative flight test and refinement cycle
- Focus on control stability and power efficiency in hover/transition operations