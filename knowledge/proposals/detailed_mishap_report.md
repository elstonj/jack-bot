# Detailed Mishap Report

## Document Metadata
- Type: Incident report / mishap investigation
- Client/Agency: NASA / JPL (Jet Propulsion Laboratory)
- Program/Solicitation: SoOp (Signals of Opportunity) - Fraser Experimental Forest snow water equivalent characterization
- Date: 2018-05-22
- BST Products/Systems Referenced: BST aircraft (two variants), p-band radiometer payload system
- Key Personnel: Jack Elston (author), Simon Yueh (JPL PI), Xiaolan, Maciej

## Executive Summary
During a third scheduled flight operation at Fraser Experimental Forest (elevation ~10,000 MSL) to characterize snow water equivalent using a p-band radiometer, a BST aircraft suffered a mishap when trim adjustments during flight resulted in an unrecoverable dive, causing the aircraft to contact multiple trees. The aircraft sustained moderate damage (fractured right wing spar, damaged nose and scaffolding) while payload equipment (SDR, LNA) remained largely intact. All procedures were followed and the incident was properly reported.

## Technical Approach

### Mission Context
- Location: Fraser Experimental Forest, mountainous forested terrain at ~10,000 MSL
- Payload: p-band radiometer for signals of opportunity snow water equivalent measurement
- Aircraft: Two variants of BST aircraft available; second aircraft selected for its lighter weight and improved construction, enabling steeper climb-out angles
- Launch/Recovery: Conducted from forest service road with tall trees on both sides and potential mountain wind shear
- Planned Operations: Three flights scheduled at 6:00, 9:00, and 12:00

### Flight Profile and Incident Sequence

**First Flight (6:30, successful):**
- Initial payload issues caused slight delay
- Successful launch and recovery using first aircraft
- Determined that second, lighter aircraft would be safer for subsequent flights

**Second Flight (9:00, incident flight):**
- Successful launch in autonomous mode
- During mapping mission: nose-down behavior observed during turns, within safe margins but indicative of trim/CG issue
- Suspected cause: elevator trim state (CG had been measured pre-flight; components secured and checked)
- Decision: Adjust trim settings during straight-level flight near end of mission at ~120m AGL
  - Rationale: Better handling needed for tight landing with little margin for error; altitude provided safety margin for manual intervention if needed
- Trim command execution: Aircraft began to dive and gain speed
- Pilot intervention attempt: Unable to slow descent despite manual control input
- Autopilot mode reinstatement: Aircraft could only slightly slow descent before contacting trees

### Root Cause Analysis (from flight logs)

1. Aircraft had been using nearly full up elevator deflection to maintain level flight before trim adjustment
2. Resetting trim condition zeroed the control loop integrators, causing the dive
3. Aircraft was slowly recovering but recovery time uncertain
4. Manual pilot throws available were slightly less than autopilot maximum deflection—insufficient to arrest descent
5. Direct line of sight being lost periodically through trees, making continued manual control problematic
6. Decision to return to autonomous mode was optimal given circumstances

## Products & Capabilities Described

### BST Aircraft (two variants)
- **General Characteristics:**
  - 10' wing span
  - Equipped with detachable nose section
  - Autonomous and manual control modes
  - Capable of operations from constrained locations (forest service roads)
  
- **First Variant (Flight 1):**
  - Standard construction
  - Heavier than second variant
  - Shallower climb-out angle
  
- **Second Variant (Flight 2 incident aircraft):**
  - Lighter weight due to improved construction techniques
  - Steeper climb-out angle capability
  - Better suited for confined launching areas
  - Design improvements under development post-incident

### Payload System (p-band radiometer)
- Mounted in internal scaffolding structure
- Components: SDR (Software Defined Radio), LNA (Low Noise Amplifier), antenna
- Detachable nose design houses payload scaffolding
- Designed for signals of opportunity snow water equivalent characterization

## Use Cases & Applications

**Snow Water Equivalent Characterization:**
- Partnership with Simon Yueh (JPL)
- Fraser Experimental Forest study site in mountainous terrain
- P-band radiometer using signals of opportunity methodology
- High-altitude operations in challenging terrain (10,000 MSL, forested mountains)

## Damage Assessment

**Aircraft Damage:**
- Right wing: Fractured spar (major structural damage)
- Left wing: Minor damage only
- Fuselage: Intact with several internal brackets broken loose
- Both tail sections: Survived intact
- Detachable nose: Requires replacement
- Payload scaffolding: Requires replacement

**Payload Equipment Damage:**
- SDR: Unharmed
- LNA: Unharmed
- Antenna: Damaged (likely due to weight and forward position)

**Overall Assessment:** Damage to JPL equipment and aircraft determined to be "relatively minor" despite tree contact at flight speed

## Recovery and Follow-up

- Last known location noted and used for recovery
- Field team (Jack Elston, Maciej) recovered aircraft safely
- No immediate safety hazards found (battery in safe condition)
- All components collected; no items left behind
- Post-flight discussion conducted
- Incident summary sent to JPL via official "Close Call / Mishap Reporting Reference Sheet"
- Full incident analysis completed same afternoon

## Corrective Actions Undertaken

**Design Changes (implemented in latest aircraft version for future flights):**

1. **Structural Rigidity:** 
   - Much more rigid outer structure to prevent damage from handling and transport
   - Addresses pre-existing trim damage from transit/use that went undetected in pre-flight

2. **Protection:** 
   - Redesigned protective case for surface protection during transit

3. **Control System Updates:**
   - Increased maximum elevator deflection limits
   - **Critical change:** Manual control limits now set equal to autopilot limits (previously, manual limits set to pilot preference for comfort, creating mismatch that prevented adequate manual intervention)

## Notable Details

- All Flight Test Plan (FTP) procedures followed, including emergency procedures and incident reporting
- Official mishap reporting completed same day
- Armstrong review anticipated
- High-altitude mountainous operations present unique challenges (wind shear, terrain, density altitude effects on aircraft performance)
- Control system architecture consideration: pilot comfort vs. emergency capability trade-off identified and corrected