# Mustang Project - Effort 1: Week One Summary

## Document Metadata
- **Type:** Project Status Report / Weekly Summary
- **Client/Agency:** ByLight (BST acting as consulting party)
- **Program/Solicitation:** Mustang Project - Effort 1
- **Date:** 10 October 2025
- **BST Products/Systems Referenced:** S2 avionics, CAN-based flight control system
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
Black Swift Technologies received a ByLight aircraft and car launch system on October 1, 2025 for integration and testing. BST identified multiple structural and aerodynamic issues including shipping damage, inadequate vertical tail stability, and thrust line misalignment. Over week one, BST replaced avionics with their S2 system, modified V-tail geometry for stability, performed motor and propeller upgrades, and conducted captive drive tests up to 65 mph. A test flight plan has been developed for the following week.

## Technical Approach
BST's consulting approach focused on:
1. **Systems Integration:** Complete removal of ByLight avionics and installation of BST S2 avionics (CAN-based protocol for surface actuation)
2. **Aerodynamic Modification:** Increased V-tail incidence angle from 24° to 36° to achieve safe vertical tail volume coefficient
3. **Propulsion Upgrade:** Swapped original motor with BST's standard 6S aircraft motor and higher-thrust folding propeller
4. **Launch System Integration:** Mounted car launcher to SUV with captive drive testing protocol
5. **Sensor Optimization:** Repositioned GPS (fuselage top mount) and pitot tube (nose mount) for better performance across flight orientations

## Products & Capabilities Described

### S2 Avionics
- **What it is:** BST's flight control system using CAN protocol for surface actuation
- **Configuration for Mustang:** Two stacks of actuator boards (4 total boards) - forward stack controls aileron/wing surfaces, aft stack controls ruddervator/tail surfaces
- **Capabilities:** Handles autopilot, radio communications, ESC control, GPS/airspeed sensor integration, and surface actuation with programmable deflection limits
- **Surface Control Authority:** ±20° ruddervator deflection, +20°/-15° aileron deflection

### Propulsion System
- **Original:** Deemed inefficient
- **Replacement:** BST's common 6S brushless motor with folding propeller offering higher thrust

## Use Cases & Applications
- **Aircraft Type:** Small UAS designed for rapid deployment via car-launched system
- **Mission Profile:** Vertical lift-off capability with car launch at highway speeds (65+ mph)
- **Operational Environment:** Appears designed for rapid field deployment with vehicle-mounted launch system

## Key Findings

### Structural Issues Identified
- Minor shipping damage to fuselage and wing surfaces (duct-taped damage on right wing top surface)
- Left wing shows propagating crack underneath skin running from trailing edge to leading edge, approximately halfway from fuselage to wingtip
- Right ruddervator has damaged servo linkage requiring repair
- No wing/tail locking mechanisms to secure control surfaces in place
- Shoddy surface finish with frequent holes, chips, and scratches
- **Material Composition:** Fiberglass/composite fuselage with plaster shell layer; aluminum friction-fit wing and tail spars

### Aerodynamic Analysis & Remediation
**Initial Stability Metrics (Problematic):**
- Stability margin: 0.28 (ideal: 0.05–0.15) — overdamped in pitch
- Horizontal tail volume coefficient: 1.1 (ideal: 0.3–0.6) — higher than any aircraft BST has flown
- Vertical tail volume coefficient: 0.016 (ideal: 0.02–0.05) — **problematic, causes Dutch roll instability**

**Dutch Roll Issue:** Identified as likely cause of previous launch failures (not autopilot as initially suspected)

**Remediation:** V-tail geometry modification increased incidence angle from 24° to 36°, bringing vertical tail volume coefficient into safe range while reducing pitch overdamping to acceptable levels

### Launch System & Captive Testing
- Car launcher mounted to SUV roof using four U-bolts
- Captive drive tests conducted at 40 mph and 65 mph with aircraft powered and secured
- Aircraft visibly generated lift starting at approximately 60 mph
- Vertical pull force on launch mechanism observed at 65 mph
- GPS and airspeed values confirmed during testing

## Notable Details

### Missing Information at Intake
- No battery (received separately 10/3)
- No radio handset
- No ground station setup
- No documentation on wiring, autopilot specifications, battery specifications, or payload weight
- Aircraft lacked visible serial numbers or identification markings, complicating inventory management

### BST Modifications & Improvements
- Bypassed original power board
- Integrated camera (type/specs not detailed)
- Repaired servo control horns (possible shipping damage)
- Replaced ineffective pitot tube with nose-mounted configuration
- Brought up second fuselage due to thrust offset issue (details not elaborated)

### Testing Status
Flight testing planned for early the following week; captive testing phase successfully completed with no aircraft release