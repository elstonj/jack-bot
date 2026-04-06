# Trace Gas Supplies - Budget Justification Detail

## Document Metadata
- Type: Budget justification / itemized cost breakdown
- Client/Agency: NOAA Earth System Research Laboratory (ESRL) and NOAA/ATDD
- Program/Solicitation: NASA 2016 SBIR Phase III (Volcano monitoring)
- Date: Multiple invoices from June 2019 – October 2020; document compiled 2022
- BST Products/Systems Referenced: S2 aircraft, S2 Payload Development Kit, Actuator Board, GNSS board, Kevlar Nose Cone
- Key Personnel: Joshua Fromm, Jack Elston (BST); Ru-Shan Gao (NOAA ESRL), Edward Dumas (NOAA/ATDD)

## Executive Summary
This document itemizes the gas payload components and supporting hardware for a volcano monitoring system integrated into the BST S2 aircraft platform. The bill of materials totals $3,138.00 and includes commercial gas detection sensors (H2S and SO2), BST avionics boards, payload integration hardware, and structural components sourced from multiple vendors between 2019 and 2020.

## Technical Approach
The payload integrates:
- **Gas Detection Sensors**: City Tech T3H (H2S, 0-100 ppm, 4-20mA output) and City Tech T3ST/F (SO2, 0-100 ppm, 4-20mA output) mounted with aspiration fixtures
- **BST Avionics**: Actuator Board (PWM servo/motor control), GNSS board (positioning and magnetometry)
- **Data Acquisition**: NDC PR33-10 current loop receiver (16-bit ADS1115 I2C module) for reading 4-20mA sensor outputs
- **Structural Integration**: S2 Payload Development Kit components (3D-printed scaffold, carbon fiber plates, quick-release attachment assemblies) plus custom mounting hardware
- **Airframe**: Kevlar nose cone for aerodynamic integration

## Products & Capabilities Described

### BST Actuator Board
- Cost: $128 per unit (2 purchased at $72 budgeted cost)
- Function: Add-on board for controlling servos or motors via PWM
- Application: Payload actuation and control

### BST GNSS Board (GNSS-MAG v06)
- Cost: $535 per unit (1 purchased at $400 budgeted cost)
- Function: GNSS positioning with integrated magnetometer; Quick-Click connector housings
- Application: Aircraft navigation and orientation reference

### S2 Payload Development Kit
- Cost: $672 from vendor (components itemized separately at $300-$150 each)
- Contents: 3D-printed ring, carbon fiber plate, quick-release attachment assemblies, carbon fiber rods
- Purpose: Modular payload integration framework for S2 aircraft

### S2 Nose Cone - Kevlar
- Cost: $533 (budgeted at $428)
- Material: Full kevlar construction
- Application: Aerodynamic enclosure for S2 airframe

### Custom Payload Integration Services
- Cost: 10 hours of custom engineering at $174/hour = $1,740
- Work: Design and construction of payload mounts for S2 and E2 aircraft

## Use Cases & Applications
- **Volcano Monitoring**: Measurement of volcanic gas emissions (H2S and SO2) using airborne platform
- **Atmospheric Sampling**: Integration of gas sensors into S2 aircraft for remote sensing missions
- **NOAA Coordination**: Partnership with NOAA ESRL and NOAA/ATDD for environmental monitoring applications

## Key Bill of Materials Details

| Component | Qty | Unit Cost | Source/Notes |
|-----------|-----|-----------|--------------|
| City Tech T3H (H2S 0-100 ppm) | 1 | $541 | McNeill International, S/N 38622797-020 |
| City Tech T3ST/F (SO2 0-100 ppm) | 1 | $541 | McNeill International, S/N 38830116-020 |
| BST Actuator Board | 2 | $128 ea. | Sells for $128, budgeted at $72 |
| BST GNSS Board | 1 | $535 | Sells for $535, budgeted at $400 |
| S2 Payload Dev Kit | 1 | $672 | Includes scaffold, carbon plates, attachments |
| S2 Kevlar Nose Cone | 1 | $533 | Full kevlar construction |
| NDC Current Loop Reader | 1 | $62 | 4-channel 4-20mA receiver with 16-bit ADS1115 |
| Custom Engineering (10 hrs) | 10 | $174/hr | S2 and E2 payload mount design |
| Mounting Hardware/Tubing | 1 | $125 | McMaster-Carr assorted fittings and hardware |
| City Tech Air Fittings | 1 | $90 | Aspiration mounting collars and fixtures |

## Notable Details
- **Vendor Diversity**: Components sourced from BST, McNeill International (gas sensors), National Control Devices (electronics), and McMaster-Carr (hardware)
- **Lead Times**: Gas sensors have 3-week manufacturing lead time plus delivery (made-to-order in England)
- **Warranty**: 12-month warranty on gas detection sensors; non-refundable/non-cancellable orders
- **Current Loop Architecture**: Standardized 4-20mA sensor output through I2C data acquisition module enables integration with BST avionics
- **Budget vs. Actual**: Several BST components carry higher actual selling prices than budgeted (e.g., GNSS board $535 vs. $400 budgeted; Actuator Board $128 vs. $72 budgeted), suggesting cost-sharing or negotiated pricing for SBIR Phase III
- **Document Classification**: This is a Phase III proposal budget item, indicating advancement beyond earlier prototype work toward a deliverable system for NOAA