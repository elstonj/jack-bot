# Q6 Report Vehicle Design Summary

## Document Metadata
- Type: Technical report / design summary
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR Phase II - Venus
- Date: Created 2021-03-01; Last modified 2021-08-13
- BST Products/Systems Referenced: Destiny aircraft (instrumented dynamic soaring testbed)
- Key Personnel: Jack Elston (last editor), Dirk Pflug (airfoil development)

## Executive Summary
Black Swift Technologies designed an aircraft capable of sustained flight on Venus via dynamic soaring, carrying a 20kg scientific payload. The design leverages proven Earth-based dynamic soaring principles adapted to Venus's atmospheric conditions, using variable camber airfoils and high aspect ratio wings to optimize performance across a range of possible trajectories.

## Technical Approach

**Core Strategy:**
- Dynamic soaring (DS) exploitation of Venus atmospheric velocity gradients to sustain flight without engine power
- Shift from high-speed DS (typical on Earth) to "break-even" DS strategy due to milder Venus velocity gradients
- Iterative design process pending trajectory optimization algorithms

**Key Design Features:**

1. **Airfoil Development (by Dirk Pflug):**
   - Variable camber design to widen performance envelope
   - Wide drag bucket achievable through camber range of -4° to +4°
   - Snap-flap technique: camber set as function of elevator deflection
   - Achieves minimal drag coefficient (~0.004) across CL range of 0.0-0.7

2. **Wing Design:**
   - Aspect ratio: 20:1 (compromise between aerodynamic performance and structural feasibility)
   - Best L/D: just over 60 with elliptical wing loading and mild washout
   - Wing loading: 13 kg/m² (Earth equivalent)
   - Stall speed: 18 m/s (without flaps), <14 m/s (with flaps)
   - Washed-out tips ensure benign root stall
   - Full trailing edge control surfaces (25% chord length)
   - Terminal velocity: 112 m/s
   - CAD design in Rhino 6

3. **Tail Configuration:**
   - T-tail layout for aerodynamic cleanliness
   - Keeps horizontal stabilizer clear of wing wake

## Design Assumptions

**Atmospheric/Flight Envelope:**
- Velocity gradient data provided by BST
- Atmospheric properties: density, kinematic viscosity, speed of sound (from BST)
- Estimated velocity range: 20-100 m/s (based on Destiny aircraft experience in mild conditions)
- Maximum acceleration: 20G (from Destiny data in break-even DS)
- Minimum wing section thickness: 10% (structural load management)

**Mass Budget:**
- Scientific payload: 20 kg
- Aircraft structure: 10 kg
- Total All-Up Weight (AUW): 30 kg

## Products & Capabilities Described

**Destiny Aircraft:**
- Instrumented dynamic soaring testbed used for baseline data
- Provided empirical performance data for mild velocity gradient conditions
- Informed assumptions for break-even DS trajectories and maximum acceleration limits

**Variable Camber System (Snap-Flap):**
- Electronically varied camber from -4° to +4°
- Coupled to elevator deflection for automatic optimization
- Enables aircraft to follow minimum drag bucket across wide CL range
- Maintains ~0.004 drag coefficient from CL 0.0-0.7

## Use Cases & Applications

- **Venus Atmospheric Sampling:** Scientific payload delivery and operation in Venus atmosphere while sustaining flight through dynamic soaring
- **Long-duration Mission:** Elimination of engine/fuel requirements enables indefinite loiter via energy extraction from atmospheric velocity gradients
- **Altitude Range Operations:** Design can accommodate vertically elongated DS circuits without exceeding terminal velocity (112 m/s)

## Design Characteristics Summary

| Parameter | Value |
|-----------|-------|
| Aspect Ratio | 20:1 |
| Best L/D | >60 |
| Wing Loading (Earth) | 13 kg/m² |
| Stall Speed (no flaps) | 18 m/s |
| Stall Speed (with flaps) | <14 m/s |
| Terminal Velocity | 112 m/s |
| Payload Mass | 20 kg |
| Structure Mass | 10 kg |
| Total AUW | 30 kg |
| Camber Range | -4° to +4° |
| Minimum Drag Coefficient | ~0.004 |
| Velocity Range Assumption | 20-100 m/s |
| Maximum Acceleration | 20G |

## Notable Details

1. **Design Iteration Status:** Noted as "reasonable first iteration" pending trajectory optimization algorithms; design expected to be revisited once final DS trajectory determined

2. **Scaling Capability:** Design scales down easily with minor airfoil modifications for lower Reynolds numbers; suggests potential for RC-scale testing

3. **Comparison to Earth DS Gliders:** Venus design allows higher wing loadings than typical RC dynamic soaring gliders (50-60 oz/sf) due to:
   - More dispersed velocity gradients on Venus
   - No launch/landing speed constraints
   - Ability to increase circuit turning radii to maintain optimal CL of 0.4
   - Benefits include reduced vehicle size and improved packaging

4. **Versatility Emphasis:** Design philosophy prioritized versatility to accommodate wide range of DS trajectories given uncertainty in final flight profile

5. **Deliverable Format:** 3D CAD files (Rhino 6 .3dm format) shared with team for further analysis