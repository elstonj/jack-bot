# #commercial-sales

## Overview

The #commercial-sales channel is Black Swift Technologies' hub for customer orders, project delivery, and sales execution. It tracks aircraft systems (E2, S2, S3, S0, S0-VTOL), payload integrations, customer relationships, and the complete lifecycle from quotes through delivery and support. The channel shows active engagement with university research programs, government agencies (NASA, NOAA), and international customers, with discussion spanning technical specifications, shipping logistics, quality control, and troubleshooting.

**Key Participants:**
- Jack Elston (leadership, customer relationships, technical decisions)
- Joshua Fromm (manufacturing, technical implementation, battery/avionics work)
- Melissa Phillips (shipping/logistics coordination)
- Maciej Tromba (payload/camera work, customer communication)
- Danny Troke (QC, testing, batteries)
- Meredith Needham (shipping, logistics, quote coordination, invoice tracking)
- Nate (assembly, QC flights, payload prep, GCS builds, quotes)
- Paige Smith (sales coordination, customer communication)
- Beck Cotter (customer outreach, email coordination)
- Ben Busby (team member)
- Dan Prendergast (project coordination, customer requests)
- Dan H (CU - external customer, E2 battery interest)

**Activity Level:** High-volume channel with 4,700+ messages spanning multiple years of operations (2020-2026). Consistent daily activity with multiple concurrent projects and customer interactions. Recent activity as of April 30, 2026.

---

## Key Decisions

### Aircraft Configuration & Production Decisions

**E2/S1/S2 Production Capacity (March 2016)**
- Decision to pursue federal sales requires 10 aircraft/month production capacity
- E2: Feasible for internal production
- S1: Challenging, requires assessment as design locks in
- S2: Most difficult due to long lead items and hand labor; would require Lee or shop support
- Resolution: Identified Maxamps bottleneck (new welder purchased); air tank sourcing may need specialty fabrication; contract manufacturing considered for scaling

**S2 End-of-Life Decision (2024-2025)**
- S2 designated as end-of-life product but continuing customer support
- Last S2 batteries allocated to existing customers; production ceased
- Focus shifting to S3 production

**S3 Production Scaling (2025)**
- Two S3 systems ordered by INSTAAR (June 1, 2025 deadline)
- UMES S3 training planned for late May with funding deadline 5/31/2025
- S3 becoming primary aircraft platform replacing S2
- **UMES S3 Order (April 2026):** 3 S3 battery packs and 2 S2 battery packs included in order; Joshua Fromm requesting clarification on S2 battery pack inclusion since S2 is end-of-life (April 29, 2026)

**E2 Tilted Rotor Configuration (August 2022)**
- E2-13: Keep untilted rotors initially, parts ordered for future conversion
- E2-14 and company E2: Convert to tilted rotors
- Decision to defer on some units due to parts availability

**ADS-B Feature Discontinuation (August 2022)**
- S2-17 (unsold): Original ADS-B model discontinued
- Cost to redesign: $2,000+ with significant rebuild required
- Decision: Do not offer ADS-B feature unless customer specifically requests and accepts redesign cost

**S0-VTOL Landing Transition Issues (2025)**
- Multiple prototype flights (goal: 10 successful flights before customer delivery)
- Issues under investigation regarding landing transition stability
- Remote ID integration required per COA requirements

**NASA S2 Iridium Retrofit Decision (April 2026)**
- Customer (NASA) requested estimate for adding Iridium components to S20009 and associated ground stations
- Jack Elston decision: Advise against addition due to component obsolescence from third parties and significant engineering burden
- Recommendation: Politely decline unless customer insists; if they do insist, may cannibalize parts from existing BST setup but flagged as "huge headache"
- Reasoning: Iridium capability is a legacy/one-off feature reviving obsolete components; not worth production effort

**E2 Battery Allocation for EMASS Project (April 2026)**
- Jack Elston proposed offering one of BST's nicest E2 batteries to Dan Prendergast's group (NASA/EMASS project)
- Rationale: Company has excess E2 batteries; no major flight campaigns planned for E2 (previously needed for Crested Butte SMM operations); would save manufacturing time
- Pricing: Not full price, discounted to recover some costs while primarily saving internal labor
- Dan Prendergast requested keeping 4 E2 batteries reserved until after EMASS completion (April 21, 2026)
- Maciej Tromba approved proposal (April 2026)

**Used E2 Battery Pricing Decision (April 30, 2026)**
- Customer Dan H (CU) interested in purchasing used E2 battery pack
- Maciej Tromba seeking guidance on discount vs. new pack ($3,699)
- Rationale for discount: Significant labor savings from not building new unit
- No final pricing decision documented yet (pending response)

### Service Repair Pricing & Quoting Standards (April 2026)

**S20004 Flap Servo Replacement Quote (April 24, 2026)**
- Nate developing quote for S20004 flap servo replacement including:
  - MD89MW servo motors x2 @ $104.99 each
  - Servo pockets (Jawstec) x2 @ $20 per pocket
  - Beefy clevis x2 @ $20 per linkage
  - Labor: Quote in hours rather than dollar amount (to be calculated by Meredith)
- **Standard labor rate established by Jack Elston: $125/hour**
- Joshua Fromm guidance: Quote component parts ($20 for pockets and linkages) and labor hours separately; let Meredith handle final pricing compilation

### Gimbal & Camera Decisions

**Gimbal Lens Compatibility Testing (January 2021-2022)**
- Multiple lens testing required: 16mm, 20mm, 35mm, 50mm, 85mm f/1.8
- 85mm f/1.8 heavy lens (484g) causes balance issues; requires 200g ballast repositioning
- Smaller lenses cause vibration issues
- Zoom lenses incompatible with gimbal
- Decision: Create setup chart for customers on weight placement for different lenses
- Ballast movement: 200g between pitch and roll positions depending on lens

**Thermal/Photogrammetry Lens FOV Matching (2024)**
- Selected FLIR Vue Pro R with 45° FOV (13mm lens)
- Paired with Sony 20mm lens for photogrammetry to match narrower FLIR FOV
- Sony 16mm = 73°, Sony 20mm = 61° selected for consistency

### Payload & Sensor Decisions

**TeAx Thermal Camera Frame Skip Setting (2022)**
- Original: ~1.1 FPS skip-8-frames mode to overcome WiFi download limitations
- Attempted: Single-capture mode with A5100 trigger board (~3 fps every frame with GPS tags)
- Camera's FFC (flat field correction) causes frame drops (5 of 2000 triggers)
- Decision: Extended trigger pulse from 200ms to 300ms to prevent FFC conflicts
- Single image captures chosen as solution for better Pix4d compatibility

**TeAx Frame Rate Optimization (2021)**
- Current frame size: 2 minutes of video = 400MB (45-minute download time)
- Decision: Reduce frame rate from 8.33Hz to ~4Hz if FOV/flight height/overlap calculations support
- Frame skip easily adjustable via USB program

**Trisonica Sphere Alignment Solution (2022)**
- Current: Only marked with 'N' - requires manual alignment on each flight
- Decision: Need machined or 3D-printed alignment solution (requires screws, not quick-connect)
- Noted: Setup requires removal for storage between flights

**Micasense Altum Camera Resolution (2024)**
- Channels 2 and 5 had exposure