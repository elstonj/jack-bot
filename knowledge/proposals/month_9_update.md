# VTOL Project Update - Month 9

## Document Metadata
- Type: Progress report / Project update presentation
- Client/Agency: Creare (partnership/collaboration)
- Program/Solicitation: 2019 VTOL Autopilot
- Date: February 2020 (Month 9 update)
- BST Products/Systems Referenced: VTOL autopilot system, mini prototype
- Key Personnel: bhccreare (last editor)

## Executive Summary
This month 9 progress update reports on mechanical damage and repairs needed for the VTOL prototype, parachute system selection and specifications, and significant controller software improvements including a redesigned attitude control architecture that improved flight path performance.

## Technical Approach

### Mechanical Systems
- Motor canted at 6° using washers to improve yaw control authority in wind conditions
- Prototype experiencing component damage (props, motors, ESC) requiring replacement
- Recommendation to upgrade to full-span aluminum construction with thicker structural parts for durability

### Parachute System
- Selected Rocketman Chutes (model rocketry parachutes) as solution
- 20 ft parachute specification provides ~10 ft/s descent rate
- Estimated system weight: ~50 oz
- Estimated cost: ~$500, under 3 lbs total weight
- Solution expected imminently

### Control Architecture
Transitioning from prototype to production codebase with major controller redesign:

**Previous approach (Full State Attitude Control):**
- Controlled all attitude states simultaneously
- Artificially reduced control authority, resulting in curved flight paths

**New Mixed Approach:**
- **Thrust vector ("Tilt") controller:** Reduced state control
- **Yaw controller:** Reduced state control  
- **Remaining axes:** Full state attitude control
- Reduced attitude state control technique providing improved control authority and straighter flight paths

### Software Updates
- Quaternion attitude control re-implemented
- State machine updates
- Multiple small code fixes
- Transitioning from prototype to production codebase

## Key Results
- Motor cant adjustment (6°) significantly improved yaw control performance in wind
- New mixed control architecture eliminated "curvy path" problem from previous full-state implementation
- Parachute system solution identified and ready for integration

## Notable Details
- Collaborative project with Creare
- Focus on improving control authority and flight stability
- Hardware iteration cycle with component replacements ongoing
- Moving toward production-ready implementation of autopilot system