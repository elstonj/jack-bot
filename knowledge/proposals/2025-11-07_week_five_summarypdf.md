# Week Five Summary - Mustang Project (Effort 1)

## Document Metadata
- Type: Weekly progress report
- Client/Agency: ByLight (via contract/partnership)
- Program/Solicitation: Mustang Project - Effort 1
- Date: 7 November 2025
- BST Products/Systems Referenced: Chilli airframe, GPS Module, custom fuselage design
- Key Personnel: Ethan Domagala (last editor)

## Executive Summary
Black Swift Technologies is building a custom unmanned aircraft for ByLight based on a Chilli Double Carbon COTS airframe with a dual-motor design. Week Five focused on completing the Chilli vehicle build and refining the new fuselage design, particularly addressing center of gravity (CG) concerns related to battery placement and munitions payload. A flight test is tentatively scheduled for Tuesday, 11 November 2025, to gather power consumption data that will inform final battery specifications.

## Technical Approach

### Chilli Vehicle Build
- CAD design of dual-motor configuration completed
- All materials ordered and expedited; delivery received 7 November 2025 (two-day delay due to supplier error)
- Motor pylons wired and epoxied to middle wing joiner surface on 7 November; curing for Week 6 assembly
- Remainder of airframe and avionics ready for flight

### New Fuselage Design
- Fuselage tube inner diameter (ID) scaled from 4 inches to 4.25 inches to accommodate battery
- Wing attachment points designed with 3D-printed middle "pylon" for aerodynamic efficiency
- Main wing attachment via two M5 to 5/16-18" thread adapter standoffs threaded into bulkhead sections with hex inserts
- Wire routing through wing pylon to motors and GPS module to be completed in future iterations
- Fuselage structure maintains initial design with optimized payload/internal placement

## Products & Capabilities Described

### Chilli Airframe (COTS)
- Consumer off-the-shelf Double Carbon design
- Dual-motor configuration
- Platform for Mustang project integration

### Custom Fuselage Design
- Cylindrical aluminum tube construction (4.25" ID)
- Designed to house battery pack, Hawkeye munitions payload, and avionics
- Incorporates GPS module mount on wing pylon
- Modular battery placement strategy to manage CG

### Battery System
- **Selected Cell:** Amprius SA112 21700 battery
  - Energy density: 315 Wh/kg
  - Reliability and durability focus
- **Current Configuration:** 96 cells total arranged in 6 sections of 16 cylindrical cells each
  - Estimated capacity: 2112 Wh
  - Weight: ~7 kg
  - Length: ~18 inches
- **Battery Placement Strategy:** Three-section distribution
  - 4 sections aft of wings
  - 1 section forward (to counterbalance munitions payload)
  - 1 section between wing pylon bulkheads
  - Each section has lattice structure attached to cell terminals
- **Estimated Range:** 400 km
- **Target CG:** 105 mm aft of leading edge
- **Possible Future Reduction:** Back to 4" diameter housing (13 Amprius SA112 per section) pending flight test data

### GPS Module
- BST-manufactured GPS module
- Housed in 3D-printed wing pylon for flush mounting

## Use Cases & Applications

**Munitions Delivery Mission**
- Payload: Hawkeye munitions (mounted forward in fuselage)
- Range requirement: 400 km
- Mission profile requires careful CG management due to dense forward payload

## Key Results / Progress

1. **Chilli Airframe:** Dual-motor CAD complete; physical assembly 90% complete as of Week 5; epoxy curing on motor pylons
2. **Battery Design:** Refined from single aft-mounted package to three-section distributed configuration to address CG concerns
3. **Fuselage Scaling Decision:** ID increased from 4" to 4.25" to accommodate battery pack
4. **Flight Test Plan:** Tentatively scheduled for 11 November 2025 to measure actual power draw and refine battery requirements

## Notable Details

- **CG Challenge:** The combination of a massive battery capacity (2112 Wh) and dense munitions payload in the front required distributing the battery into three sections rather than a single aft-mounted unit
- **Battery Cell Selection Rationale:** Cylindrical Amprius cells chosen for precise fuselage fit, reducing overall weight vs. alternative battery form factors
- **Weight Optimization:** Current battery design at 7 kg; potential further reduction if flight test data supports smaller capacity
- **Design Iteration Approach:** Initial flight tests on Chilli setup will identify weak points and inform final fuselage design refinements
- **Manufacturing Consideration:** Wing pylon to be 3D-printed for improved aerodynamic efficiency vs. traditional mounting
- **Schedule Impact:** Supplier shipping delay pushed motor pylon completion to Week 6; flight test still planned for Week 6 pending weather
- **Next Steps:** Avionics wiring diagrams, refined internal systems layout, and characterization flights in Week 6