# #commercial-sales

## Overview

The #commercial-sales channel is Black Swift Technologies' hub for customer orders, project delivery, and sales execution. It tracks aircraft systems (E2, S2, S3, S0, S0-VTOL), payload integrations, customer relationships, and the complete lifecycle from quotes through delivery and support. The channel shows active engagement with university research programs, government agencies (NASA, NOAA), and international customers, with discussion spanning technical specifications, shipping logistics, quality control, and troubleshooting.

**Key Participants:**
- Jack Elston (leadership, customer relationships, technical decisions)
- Joshua Fromm (manufacturing, technical implementation, battery/avionics work)
- Melissa Phillips (shipping/logistics coordination)
- Maciej Tromba (payload/camera work, customer communication)
- Danny Troke (QC, testing, batteries)
- Meredith Needham (shipping, logistics)
- Nate (assembly, QC flights, payload prep, GCS builds)
- Paige Smith (sales coordination, customer communication)
- Beck Cotter (customer outreach, email coordination)
- Ben Busby (team member)
- Dan Prendergast (project coordination, customer requests)

**Activity Level:** High-volume channel with 4,701+ messages spanning multiple years of operations (2020-2026). Consistent daily activity with multiple concurrent projects and customer interactions.

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
- Channels 2 and 5 had exposure saturation issues post-firmware update
- Camera sent back to Micasense multiple times for diagnosis
- Final resolution: Internal circuit board replaced, fan replaced, full recalibration done
- Issues not reproducible on ground testing; uncertain if fully resolved

**MHP (Modular Hovering Payload) Production Plan (2021)**
- Production plan: 5 aeropods + 5 regular MHP units
- Allocation: 1-NASA, 2-L3 Harris, 1-S1 project, 1-BST internal, balance for S2 integrations

**NASA Langley S2 MHP Power Configuration (2021)**
- Option 1: Self-powered with 2-hour battery
- Option 2: Aircraft-powered via wing (requires left wing for power cable/wingtip drilling)
- Team leaning toward Option 2

### International Shipping Policy

**Large Item International Shipping (May 2022)**
- Customers arrange and pay for their own shipping provider for large items (larger than MHP)
- Company coordinates with whatever provider customer uses
- Exception: Oier/Alerion maintains existing established process (no batteries involved)

### Probe Design Decisions

**MHP Sensor Probe Design (July 2016)**
- Decision: Stick with smaller/older tip style (proven design with wind tunnel data)
- Joshua Fromm advocated for larger carbon tube due to: increased length needed, current tube too small for hoses/causes static port clogs, brittle at step-down, time-consuming potting
- Concerns about manufacturing precision without proper equipment
- Resolution: Order housing from external supplier (MM Solutions to machine tubes properly)
- Later decision (October 2021): Order 2 more avionics bays once Joshua satisfied with arrangement

### GCS & Tablet Decisions

**Tablet Updates (2024)**
- Update to Tab Active 5 (WiFi) for S2 deliveries
- New PingRX Pro ADS-B selected (old one unavailable)

**GCS Production (2024)**
- Building 3 additional GCS units (Nate assigned)
- Allocation: Barbados 1, ERAU 1 (second unit), ADONIS 1, Oklahoma likely needs 2-3
- No Xtend GCS available; would need to build one for potential S1 customer

### Composite Sourcing Strategy

**Multi-Vendor