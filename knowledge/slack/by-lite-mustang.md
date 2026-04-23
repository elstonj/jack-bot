# #by-lite-mustang

## Overview

This channel tracks the development and flight testing of the **By Light Mustang aircraft**, a customer contract for the U.S. Air Force testing at Yuma. The project uses a two-phase approach: first flying the original Mustang to demonstrate its limitations for the 400km range mission, then developing the new Chilli airframe to meet full mission specs (400km range at 30m/s cruise with 4kg payload).

**Key Participants:**
- Maciej (project lead, flight operations, task oversight)
- Ethan Domagala (design, measurements, avionics integration)
- Dan Prendergast (flight test coordination)
- Jack Elston (backup pilot, vehicle support, approvals)
- Nate (aircraft assembly, launch support)
- Bryan Sparling (ByLight pilot/contact)
- Beck Cotter (program management, SOW coordination)
- Dan H., Terry Tate, Spencer (contractors/specialists)
- Alex Lomis (components/inventory, battery design)

**Activity Level:** High, covering October 2025 through April 2026, with regular flight tests, design iterations, and scope management updates. Recent activity (April 20, 2026) shows ongoing task management and resource allocation discussions.

## Key Decisions

**October 2025 – Contract Execution & Strategy**
- Two-phase approach approved: Mustang flights to prove inadequacy, then Chilli development
- Chilli airframe selected with Czech A37 commercial wings (from Soaring USA)
- COTS components prioritized per contract requirements
- KDE 4215-465Kv motors selected (dual motors for Chilli) over Vertiq due to stock and voltage compatibility concerns
- TBS Lucid ESCs chosen with KISS telemetry (lacks position-hold but proven reliable)
- RFM folding props selected to minimize damage on belly landings

**October-November 2025 – Design Pivots**
- V-tail angle increased from 36° to 35-40° using 3D-printed shims to fix stability margin issues
- Fuselage tube material changed from 4.25" carbon fiber (out of stock) to 4.5" fiberglass rocketry tube from Wildman Rockets (more durable on impact)
- Elevator servo selection and pitot static sensor decisions made during assembly phase

**November-December 2025 – Prop & Configuration Optimization**
- 17x13 props selected as best performer for 30-40lb weight range after testing 15x13, 14x14, 14x12, and 15x13 variants
- New fuselage design by Ethan finalized after flight testing showed 18% power reduction vs. old design

**December 2025 – Customer Engagement**
- Dec 8: Additional funding approved by Air Force customer; Yuma test site, March window confirmed
- Dec 17: ByLight (Mel) approved proceeding with Ethan's 3D-printed fuselage design instead of new design, with EchoPilot integration planned

**January-March 2026 – Phase 2 Planning**
- Two follow-on phases quoted to ByLight:
  - **Phase 1:** Complete red Chilli airframe (Trillium integration, 400km battery, paint, flight test) – $34K
  - **Phase 2:** Build Chilli #2 with CF tube and SwiftPilot integration – $31K
- Spencer contracted to design improved wing with 16% performance gain; new wing design finalized April earliest with IP transfer to ByLight

**April 2026 – New Program Initiative (M2/HALO)**
- New scope added: HALO project rebranded as **M2**
- SOW signed and filed (April 7, 2026)
- ADS-B units procurement decision: BST to procure and provide (added to Scope 2)
- Additional 40 hours of engineering at Sam's rate added to Scope 2

**April 17, 2026 – Battery Configuration & GTOW Confirmation**
- Battery design finalized with three configuration options (2-pack primary, optional 3rd pack)
- Decision: Confirm all configs below 40lbs GTOW before parts ordering
- Battery parts ordered (April 17) from SCS and Jawstec suppliers
- Weekly email updates to ByLight implemented (Fridays) replacing Signal messages for better tracking

## Projects & Initiatives

### Mustang 1.0 (Original Aircraft) – COMPLETED
- **Status:** Flight testing completed, shipped to ByLight for static display
- **Specs:** 5400-5717g AUW, single KDE 4215 motor, 6S 518.4Wh battery
- **Key Results:** 
  - 31.8 minutes tethered flight, proved flyable but inadequate for 400km/4kg payload mission
  - Demonstrated need for new airframe design
  - Shipped to ByLight at 4038 Gillespie St, Fayetteville, NC for SOF week display

### Chilli/MS2-4 Prototype (Primary Aircraft) – IN FLIGHT TESTING
- **Status:** Red fiberglass fuselage airframe active, multiple flight tests completed through December 2025
- **Configuration:**
  - Wings: Commercial Chilli A37 from Soaring USA
  - Fuselage: 4.5" fiberglass rocketry tube (red, Wildman Rockets)
  - Motors: 2x KDE 4215-465Kv
  - Props: Currently testing 17x13 RFM folding props (best performer)
  - ESC: TBS Lucid with KISS telemetry
  - Avionics: 2030 autopilot, S2 power board, 3-to-1 CAN boards
  - Weight: Testing at 25, 30, 35 lbs (3-5 ballast plates)
- **Recent Flight Data (Dec 2025):**
  - Old fuselage: 590W at 30m/s
  - New fuselage (Ethan design): 480W at 30m/s (18% improvement)
  - At 27m/s: 335W, projecting 13 hours flight time / 1200km range as S0
  - 19 m/s stall speed (clean config)
  - Elevator incidence: 1.8° relative to wing (acceptable)
  - Aero efficiency: 30% better than previous at 27m/s, 20% better at 30m/s
- **Next Milestones:** 400km flight test at Sod Farm, Trillium mass model integration, battery scaling for 3.7+ hour flights

### Battery Design & Pack Integration – IN PROGRESS
- **Status:** Design finalized as of April 17, 2026; parts ordered from SCS and Jawstec
- **Specs:**
  - **Pack Configuration:** 2-pack primary design (950Wh capacity each, ~2.8-3kg per pack)
  - **Secondary Option:** 3-pack config with 3rd pack in gimbal space, or alternative placement in forward payload bay
  - **Performance:** 2-pack sufficient for 4-hour endurance target; 3rd pack provides additional capacity
  - **Energy Density:** ~315 Wh/kg (80-85% cells, 15-20% non-cell pack weight—inefficiency due to ByLight fuselage form factor constraints)
- **Constraints:** 
  - Tail spar must be removed to access batteries (charge-in-place option planned as alternative)
  - Tight fit in fuselage; may require selective material grinding
  - Non-permanent tail attachment design required
- **GTOW Target:** All configs must remain below 40lbs (wing load constraint)
- **Contact:** george.kusaba@amprius.com (Amprius SA03 Pouch cells supplier)

### Chilli #2 (New Frame Build) – PLANNED
- **Scope:** Build second airframe with CF tube fuselage (instead of fiberglass), SwiftPilot integration
- **Status:** In planning phase, quoted $31K
- **Target:** Two demo-able Chilli aircraft ready for customer by March 2026
- **Component Needs (as of April 7, 2026):** 
  - 10 additional actuator boards
  -