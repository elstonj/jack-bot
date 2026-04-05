# Week Seven Summary - Mustang Project Effort 1

## Document Metadata
- Type: Project Status Report / Weekly Summary
- Client/Agency: ByLight (apparent client/partner)
- Program/Solicitation: Mustang Project - Effort 1
- Date: 21 November 2025
- BST Products/Systems Referenced: Mustang 2 aircraft (formerly "Chilli"), SwiftCore autopilot
- Key Personnel: Maciej Stachura (last editor), BST Engineers (unnamed)

## Executive Summary
Black Swift Technologies completed Week 7 of the Mustang Project by conducting real flight tests with the Mustang 2 aircraft under increased weight conditions and advancing fuselage design for the Mustang 2.1 variant. Engineers developed an incremental mass adjustment system, collected power and efficiency metrics across multiple weighted flight configurations, and completed design review and procurement of 3D-printed fuselage components.

## Technical Approach

### Weight Testing Configuration
- Designed modular steel plate weight system (1990g/4.4lbs per plate) mounted above aircraft center of gravity
- Rubber feet (4 per corner) and central bolts provide secure mounting to wing surface
- Prioritized speed of manufacturing and reliability over aerodynamic optimization
- Achieved full assembly and first flight within 24 hours of design conception

### Flight Testing Protocol
- Conducted flights in rapid succession with incrementally increasing weight
- Maximum tested weight: 13.497kg (29.76lbs) with 3 additional steel plates
- Speed limitation: 25 m/s due to weight and unoptimized propeller configuration
- Collected data on total power usage, throttle settings, and effective efficiency
- Effective efficiency calculation: L/D × ηmotor × ηprop × ηESC

### Fuselage Design (Mustang 2.1)
- New design approved with emphasis on cost-effective manufacturing methods
- Primary construction method: 3D-printed components
- Components ordered: 3 bulkheads, avionics bay, wing pylon attachment
- Prototyping approach: Sequential assembly → avionics integration → weight approximation testing → battery optimization iteration

### Propulsion Optimization
- Current wing designed for optimal cruise at ~20 m/s; performs sub-optimally at 30 m/s
- Trailing edge composed of 3 surfaces allowing for 1-3° reflex adjustment to improve L/D at higher speeds
- Propeller optimization identified as critical for efficiency improvement at 30 m/s
- Next testing phase: evaluate different propeller pitch/size configurations
- Final week (Week 9): implement autopilot code changes to accommodate reflex adjustments

## Products & Capabilities Described

### Mustang 2 Aircraft
- Uncrewed aircraft capable of sustained flight with variable payload weights
- Current configuration: glider-derived wing with modifiable trailing edge reflex
- Motor, ESC (electronic speed controller), and propeller systems
- SwiftCore autopilot integration for control and data logging
- Power consumption measurement capability across flight envelope

### SwiftCore Autopilot
- Flight control and automation system
- Code-modifiable for wing reflex adjustments
- Data logging of throttle, power, and performance metrics

## Use Cases & Applications
- Payload delivery/monitoring missions with variable weight requirements
- Extended endurance flight operations
- High-speed (30 m/s) aircraft performance in operational conditions
- Integration of Trillium camera payload with full actuation capability

## Key Results

### Flight Test Data (Week 7)
- Successfully completed weighted flights with 29.76 lbs total aircraft weight
- Identified efficiency degradation at 30 m/s as critical limitation
- Root causes identified: L/D drop-off and propeller efficiency (ηprop) at higher speeds
- Maximum safe speed with current configuration: 25 m/s

### Design Review Outcomes
- New fuselage design approved and cleared for procurement/manufacturing
- 3D-printed component manufacturing initiated
- Wiring routing and avionics bay layout finalized to accommodate Trillium payload actuator range
- General wiring schematic completed for construction reference

## Notable Details

- **Iterative Battery Optimization**: Process acknowledged as self-referential (battery weight affects performance, affecting required battery capacity); engineers will iteratively converge on optimal cell count
- **Propeller-Wing Trade-off**: Wing redesign in progress; reflex adjustment capability allows tuning without complete redesign
- **Rapid Prototyping Success**: 24-hour design-to-flight turnaround demonstrates BST's agile engineering capability
- **Payload Integration**: Fuselage design specifically accommodates Trillium camera with full actuation range—indicating photographic/imaging mission capability
- **Next Phases**: Continue weight testing to 35-40 lbs; propeller optimization testing; Week 9 autopilot code updates for wing reflex; battery capacity determination