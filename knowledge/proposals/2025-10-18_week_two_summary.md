# Week Two Summary - Mustang Project Effort 1

## Document Metadata
- Type: Progress/Status Report
- Client/Agency: ByLight (consulting engagement)
- Program/Solicitation: Mustang Project - Effort 1
- Date: 18 October 2025
- BST Products/Systems Referenced: Mustang UAS (aircraft under development/testing)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies is serving as a consulting party to ByLight to diagnose and resolve flight stability issues with the Mustang aircraft. After a crash in Week One due to yaw instability, BST implemented modifications to the tail geometry and motor offset alignment. The redesigned aircraft successfully flew on October 14, 2025 for approximately 24 minutes, though power consumption data revealed the aircraft will fall significantly short of the 400 km range requirement.

## Technical Approach

### Tail Adjustment
- Diagnosed initial tail angle at 132 degrees (24° increase from horizontal) as insufficient for yaw stability
- Ran stability simulations to identify optimal tail angle range of 35-40 degrees for adequate stability margin and yaw damping
- Designed and implemented modification increasing tail angle from 24° to 36° (12° increase)
- Construction: carbon fiber forward spar, 3D printed PLA airfoil spacer, bent rear spar
- Result: Achieved target 36° angle with sufficient stability margin for flight

### Motor Offset Correction
- Root cause: Yaw moment generated during high throttle periods, amplified by rear motor placement and clockwise propeller rotation
- Testing method: Confining rig restricting aircraft to Z-axis movement while throttle was stepped up
- Iterative adjustment: Motor offset 0.017 inches (approximately 0.98 degrees) to the left to create straight thrust vector and minimize yaw generation
- Additional modifications: Lengthened aileron servo horns for full surface deflection; repositioned RC receiver antennas outside fuselage to improve signal reception

### Structural Testing
- Wing support test at center of lift to evaluate deflection at target 30 lbs weight
- Tested up to 3G loading (90 lbs total load at 30 lbs aircraft weight)
- Deflection remained acceptable up to 3G; noted potential aileron lock-up concern at inboard position; recommended moving ailerons outboard to reduce flex

## Products & Capabilities Described

### Mustang UAS
- Fixed-wing unmanned aircraft system under development/testing
- Configuration: Rear-mounted motor, swept-wing design with vertical tail surfaces
- Launch method: Car-launch capable
- Current specifications from test flight:
  - Cruise altitude: 300' AGL / 5,250' MSL
  - Tested airspeed range: 25-29 m/s
  - Stall speed (current configuration): ~21 m/s
  - Battery capacity: 518.4 Wh (single pack)
  - Flight endurance achieved: 24 minutes
  - Structural capability: 3G loading at design weight
  - Controllability: Good control performance post-tuning

## Use Cases & Applications
- Long-endurance mission aircraft (target 400 km range)
- Payload-carrying capable aircraft (payload weight significant but not specified in this report)
- Operations requiring extended surveillance/monitoring duration

## Key Results

### Test Flight Performance (October 14, 2025)
- **Flight Duration:** 24 minutes
- **Launch Method:** Car launch successful
- **Control Performance:** Good after tuning; roll/pitch RMS error, maximum error, and delay performance comparable to other BST fixed-wing UAS
- **Airspeed Testing:** Successfully tested 25 m/s, 27 m/s, and 29 m/s for endurance optimization

### Power Consumption & Range Analysis
- Average power draw measured at three speeds; values consistent with earlier European test flight (slightly elevated due to higher elevation test site)
- **Calculated Range:** 132-141 km on single 518.4 Wh battery (lower value at 29 m/s cruise, higher at 25 m/s)
- **Critical Findings:**
  - Aircraft will **not achieve 400 km minimum range requirement** even with single battery
  - Doubling battery capacity will **not double range** due to increased power draw at heavier weight
  - Payload weight (unspecified but noted as "significant") will further increase power draw and reduce range
  - At target 30 lbs weight, stall speed increases to ~32 m/s, requiring cruise at ≥39 m/s, which further reduces efficiency

## Notable Details

### Stability Improvements Achieved
- Week One crash attributed to yaw instability during high-throttle launch phase
- Dual modifications (tail geometry + motor offset) successfully eliminated yaw instability
- Aircraft demonstrated safe launch characteristics and good controllability post-modification

### Performance Gap Identified
- A significant mismatch exists between current aircraft capability and mission requirements
- The detailed power analysis suggests fundamental limitations of current design approach for 400 km range mission
- Document does not propose solutions to range shortfall (analysis only)

### Engineering Quality
- Comprehensive iterative testing approach (simulation → CAD design → physical modification → flight test)
- Structural testing conducted to validate design at target weight
- Control loop tuning and performance validation performed pre-flight