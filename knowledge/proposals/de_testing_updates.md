# DE Testing Updates

## Document Metadata
- Type: Presentation/Technical Update
- Client/Agency: Creare
- Program/Solicitation: 2019 VTOL Autopilot project
- Date: Created 2020-09-27, Modified 2020-10-20
- BST Products/Systems Referenced: Double Eagle (VTOL platform)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This presentation documents testing updates for a VTOL autopilot project with Creare, focusing on transition flight testing with the Double Eagle platform and troubleshooting of roll control saturation issues discovered during both full-scale and prototype aircraft testing.

## Technical Approach
Testing conducted in two phases:
1. **Full-scale Double Eagle transitions**: 7 transition flights to evaluate forward flight performance
2. **Small prototype iterations**: 9 flights dedicated to debugging roll control issues
3. **Control tuning**: Adjustments to elevon trim tabs to resolve saturation problems

## Products & Capabilities Described

**Double Eagle VTOL Platform:**
- Mass: 20.3 kg (with 2 batteries)
- Hover Power requirement: 2618W
- Forward Power @ 13 m/s: 1240W
- Identified inefficiency in forward flight due to maxed-out roll control authority

## Technical Issues & Solutions

**Roll Control Saturation Problem:**
- Initial issue: Forward roll control saturation in full autopilot mode, creating very narrow flight envelope
- Root causes identified:
  - Saturation in control channels during full automation
  - Rotor 3 saturation contributing to roll control issues
  - With elevons neutral: positive roll torque saturation
- Solution implemented: Elevon trim tab deflection (~5° up) eliminated saturation
- Result: Reduced rotor command spread, better control authority, improved tracking and orbit performance without oscillation

## Key Results
- Saturation effects demonstrated: decent tracking/orbit capability when saturated eliminated; oscillatory behavior observed with saturation present
- Elevon trim tab adjustment proved effective in expanding usable flight envelope
- Small prototype testing proved valuable for rapid iteration on control issues before full-scale validation

## Notable Details
- Inefficiency in Double Eagle forward flight attributed to control saturation rather than aerodynamic design
- Issue resolution required relatively minor hardware modification (trim tab deflection)
- Testing methodology: rapid iteration on small prototype followed by validation on full-scale platform