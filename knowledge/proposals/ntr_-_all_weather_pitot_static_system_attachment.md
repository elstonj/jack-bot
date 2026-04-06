# All Weather Pitot Static System

## Document Metadata
- Type: Technical attachment/deliverable (Phase I SBIR)
- Client/Agency: NASA
- Program/Solicitation: 2022 NASA SBIR, Extreme Environments Topic
- Date: 2023-01-24
- BST Products/Systems Referenced: S2 (aircraft platform)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This document presents CAD designs, circuit board schematics, and rain tunnel test results for an all-weather pitot static system developed under NASA SBIR Phase I funding. The system successfully demonstrated superior performance compared to conventional pitot tubes in heavy precipitation conditions, operating continuously without failure where standard systems failed within 1-2 minutes.

## Technical Approach
The all-weather pitot static system uses:
- **3D printed construction**: aluminum for the main housing and plastic components
- **Integrated heating elements** within the housing to prevent icing and water accumulation
- **Drain hole design** to shed accumulated moisture
- **Compact, integrated architecture** optimized for underwing pod installation
- **Multi-sensor electronics**: dynamic pressure sensors, static pressure sensors, temperature sensors (for housing thermal monitoring), and onboard microprocessor for sensor interface, data acquisition, and heater control management
- **Short form factor design** relative to conventional pitot tubes

## Products & Capabilities Described

### All Weather Pitot Static System
- **What it is**: An integrated pitot-static measurement system designed for operation in extreme weather conditions (heavy rain, icing environments)
- **Key innovation**: Heated, sealed design with active moisture management vs. conventional open-tube pitot designs
- **Integration capability**: Demonstrated installation in S2 wing pod configuration
- **Sensors**: Dynamic pressure, static pressure, and temperature measurement with integrated microprocessor for signal conditioning and heater control

## Use Cases & Applications
- **Extreme environment flight operations**: Arctic and polar operations implied by "Extreme Environments" SBIR topic
- **All-weather autonomous flight**: Systems requiring continuous airspeed measurement in precipitation
- **Small UAS operations**: Integration with S2 suggests suitability for small aircraft platforms

## Key Results

### Rain Tunnel Testing
**Clear Air Baseline (Figure 4)**:
- All-weather system produced airspeed measurements comparable to conventional, flight-tested pitot tube
- Short integrated design does not compromise measurement accuracy in non-precipitation conditions

**Standard Pitot Tube in Heavy Rain (Figure 5)**:
- Failed after 1 minute 20 seconds (180s mark)
- Water accumulation blocked the pitot opening, preventing valid airspeed measurement

**All-Weather System in Heavy Rain (Figure 6)**:
- Operated continuously through medium and heavy precipitation without failure
- No degradation in airspeed reading
- Successfully demonstrated rain tolerance exceeding conventional systems by 4-5x operating duration minimum

## Notable Details
- The system uses active heating control via onboard microprocessor—not passive thermal management
- 3D printing (both metal and plastic) enables integrated geometry not possible with traditional machined pitot tubes
- Design includes flight-testable form factor (wing pod integration with S2)
- Comparison testing conducted in controlled rain tunnel environment at BST facility