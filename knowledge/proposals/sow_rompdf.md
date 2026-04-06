# SOW_ROM: DARPA Albatross Program

## Document Metadata
- Type: Statement of Work (SOW) / Draft
- Client/Agency: DARPA
- Program/Solicitation: DARPA Albatross
- Date: 2024-11-07 (document created/modified date)
- BST Products/Systems Referenced: s-UAS (small uncrewed aircraft systems), Black Swift Flight Range
- Key Personnel: Beck Cotter (last editor)
- Status: Draft (appears to be internal/subcontractor planning document)

## Executive Summary
This SOW outlines Black Swift Technologies' subcontractor role in DARPA's Albatross program, a 24-month effort to develop autonomous aircraft soaring capabilities that harness wind energy to reduce power demand and extend range/endurance. The work focuses on developing mission planning tools, flight sensing systems, control solutions, and providing small UAS platforms for real-world flight testing across multiple operational environments.

## Technical Approach

**Program Philosophy:**
- NOT a dedicated airframe design effort
- Focuses on integrating planning tools, additional sensors, and control solutions onto existing or quickly-assembled small UAS
- Autonomous soaring defined as independent active harnessing of energy from atmospheric flow fields to reduce onboard power and enable increased range/endurance
- Weather forecast-informed mission planning + real-time onboard sensing of dynamic wind conditions

**Four Major Technical Work Areas:**

1. **Preflight Planning Perk (PF2P)**
   - Identify and integrate data sources (terrain, land cover, weather, solar, oceanic forecasts)
   - Predict harvestable energy per geologic feature type incorporating UAV performance
   - Design and implement user interface approach
   - Provide baseline ground station and Android map-based UI for ground control
   - Export functionality for in-flight mission use

2. **Sensing and Harnessing Control System (SHCS)**
   - Sensors and processing for soaring-relevant information detection
   - Real-time flow condition detection subsystem
   - Integration with PF2P to balance energy harvesting against higher-level mission objectives
   - Potential soaring location detection
   - Obstacle avoidance subsystem for flight safety
   - Real-time flight safety approaches

3. **Soaring Platform (s-UAS Fleet)**
   - Select appropriate small UAS for test events, practice test events, and flight tests
   - Procure, build, adapt, or modify s-UAS platforms
   - Provide both baseline and Albatross-enabled configurations for metrics evaluation
   - Meet government specifications including MAV link interface compatibility
   - Provide flight safety certification documentation for US government test ranges

4. **Integration, Test, and Evaluation**
   - Component integration before test events
   - Simulation-based integration testing
   - Test event readiness reviews per safety requirements
   - Manage logistics and execution of multiple flight tests
   - Evaluate system performance against program metrics

## Products & Capabilities Described

**Black Swift s-UAS Fleet:**
- Small uncrewed aircraft systems for autonomous soaring demonstrations
- Baseline and Albatross-enhanced configurations
- Must meet government MAV link interface standards
- Selected for multiple operational environments

**Black Swift Flight Range:**
- Located in Boulder, Colorado
- Used for system checkout milestone (6 months MAC)

## Use Cases & Applications

**Operational Domains for Testing:**
- Desert environments (Fort Irwin, California; Yuma Proving Ground, Arizona)
- Marine environments (San Clemente Island; Pacific Missile Range Facility, Hawaii; Roosevelt Roads, Puerto Rico)
- High-altitude/remote (Kodiak, Alaska; Vandenberg Space Force Base, California)
- International (south of Agadir, Morocco)

**Mission Types:**
- Extended range flight through wind energy harvesting
- Increased endurance through autonomous soaring
- Operations across varied terrain and weather conditions

## Program Schedule & Milestones

**24-Month Period of Performance:**
- **Month 1 (MAC):** Kickoff (Burlington, MA) - 2 people, 2 days
- **Month 6 (MAC):** System Checkout at Black Swift Flight Range (Boulder, CO) - 2 people, 3 days
- **Months 8, 12, 14, 16, 20, 22:** Pre-test Events (Fort Irwin, Yuma, San Clemente Island, Vandenberg) - 2 people, 7 days each
- **Month 12, 18, 24 (MAC):** Test Events - 2 people, 12 days (CONUS locations); 10 people, 12 days (OCONUS locations)
  - **Month 12:** Fort Irwin, Yuma
  - **Month 18:** Hawaii, San Clemente Island, Puerto Rico
  - **Month 24:** Vandenberg, Kodiak (Alaska), Morocco

**Go/No-Go Decision:** System checkout at month 6 is go/no-go decision point for continuing with full project.

## Deliverables

| Item | Deliverable | Due Date |
|------|-------------|----------|
| A001 | Presentation Materials | 24 hours prior to presentation |
| A002 | Technical and Financial Status Reports | Monthly (5th of each month) |
| A003 | Test Plan and Review Inputs | Months 6, 12, 18, 24 MAC |
| A004 | Test Reports | Months 12, 18, 24 MAC |
| A005 | Software Data Package | Months 12, 18, 24 MAC |
| A006 | Final Report | Month 24 MAC |

All deliverables provided with minimum Government Purpose Rights (GPR).

## Notable Details

- Document marked "BAE SYSTEMS PROPRIETARY" - suggests this is a subcontractor SOW where Black Swift operates under BAE Systems as prime contractor
- Spiral/incremental development approach with regular test events every 2 months
- Extensive travel requirements across multiple US government test ranges (military installations, ranges, proving grounds)
- Emphasis on flight safety certification and government range approval processes
- Strong integration focus between forecasting (PF2P) and real-time control (SHCS) systems
- Baseline capability documentation required to measure improvement from Albatross enhancements
- Performance metrics evaluation planned at each test cycle