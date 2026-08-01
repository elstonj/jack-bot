# #operations

## Overview
The operations channel serves as Black Swift Technologies' central hub for coordinating day-to-day activities, project status updates, facility management, shipping/logistics, procurement, financial tracking, and administrative matters. It functions as a working operations log where decisions are documented, action items assigned, and resources tracked.

**Key participants:** Jack Elston (leadership), Joshua Fromm (hardware/shop lead), Meredith Needham (finance/admin), Parker Vollmer (systems/compliance), Dan Prendergast (soil moisture/research), Maciej Suwinski (VTOL/flight ops), Sam Hild (firmware/electrical), Alex Lomis (mechanical/VTOL), Nate (aircraft builds), James Hannon (project management), Ben Busby (flight operations/QA), Beck Cotter (project coordination), Paige Smith (admin), Ethan Domagala (project coordination), Kareem (team member), and numerous other engineers and support staff.

**Activity level:** High-volume channel with 3,430+ messages spanning from July 2020 through July 2026. Activity increased significantly starting in mid-2023 with more structured project management and formalized coordination processes. Continues through July 2026 with project refinements, flight operations coordination, NOAA testing, demo/flight scheduling, and ongoing operational management. Most recent activity (July 31, 2026) reflects DFM group visit planning, infrastructure improvements, and equipment optimization discussions.

---

## Key Decisions

### Office & Facilities
- **July 20, 2020:** Completed office relocation. Jack Elston coordinated with landlord. New facility includes solder station, vacuum dust management system, and industrial curtain dividers for clean/dirty room separation (divider delayed ~1 month due to COVID).
- **May 16-17, 2023:** New office lighting installation scheduled and executed.
- **August 2023:** Alex installed garage door seal for improved weatherproofing.
- **June 11, 2026:** Ben Busby addressing sprinkler valve maintenance at facility.

### Personnel & Management
- **June 2, 2023:** James Hannon hired as new Project Manager to address task overload and process improvements.
- **June 6, 2023:** Jack Elston issued formal travel policy requiring Rippling approval for any leave longer than one day, citing multiple simultaneous absences by S1/S0 build team in May causing project delays.
- **May 21, 2026:** Jack Elston implementing reminder system for PTO requests in Rippling, tracking current requests (Jack, Meredith, Nate confirmed; Alex anticipated for birthday).
- **June 3, 2026:** Jack Elston presented draft organizational chart for team review and refinement. Beck Cotter assigned to coordinate feedback on job descriptions via Slack/email. Career path discussions directed to Jack Elston.
- **June 15, 2026:** Kareem returning to work at 12:00 PM. Jack Elston soliciting input on task assignment options: S0 components assembly, ground station completion, or slide project work. Division of labor coordination initiated with relevant team members regarding wildfire video project completion.
- **July 27, 2026:** Beck Cotter now tracking S0 shipment and logistics status (transitioned from Joshua Fromm). Jack Elston assigned to create login access for Beck.

### Equipment Procurement & Infrastructure
- **December 2023:** Drill press acquisition decision pending. Joshua Fromm researching floor-mounted options (Nova 58000 Voyager, Grizzly models) with ~$500+ budget needed for tooling. Jack Elston requested spreadsheet comparison for budget approval.
- **April 2023:** End-of-week cleanup task list implemented with color-coded tool inventory checks assigned to shop manager. Clipboard-based tracking without formal records (Jack Elston assigned responsibility).
- **Lab equipment (2024):** JBC HDE Heavy-Duty soldering station recommended for production line work. 26AWG PTFE wire identified as correct specification for 2.00mm clickmate crimps (not ETFE).
- **May 28, 2026:** Inquiry regarding availability of Gateworks boards for S0 ground stations for IDIQ contract (Joshua Fromm inquiry to Jack Elston).
- **June 9, 2026:** Joshua Fromm checking on status of Gateworks package received from DigiKey; following up with Ben Busby for tracking information.
- **June 12, 2026:** BST Steam Deck ordered and tracked via UPS. Ben Busby reports expedited shipping arriving Monday (June 17, 2026), faster than originally stated delivery timeline.
- **July 31, 2026:** Jack Elston acquired new computing infrastructure for two purposes: (1) git server replacement, (2) external workstation to reduce laptop battery drain. Jack Elston's test scores: 806.0 and 390.6 on OnShape CAD compatibility check. Team running CAD performance benchmarks across devices (Joshua Fromm, Maciej, Alex Lomis, Dan Prendergast comparing OnShape check scores). Discussion of hardware optimization for CAD work; noted potential limitations in GPU/graphics performance on some machines.

### Lithium Battery Shipping (April 2022 - ongoing)
**Major compliance discovery:** E2 and S2 batteries cannot be shipped internationally without hazmat certification. Multiple carriers (UPS, DHL) rejected shipments.

**Requirements established:**
- IATA hazmat training course (16 hours, ~$1,100-$209 through Hazmat University) - required before international shipment
- UPS dangerous goods contract (domestic only)
- UN-certified packaging and commercial invoices
- Minimum 2-week international shipping timelines

**Solution:** Bill Nickerson coordinated with ProCargo (Houston) to handle hazmat packaging and documentation. Joshua Fromm documented comprehensive lithium shipping checklist including discharge procedures, taping, packing, labeling, and record-keeping. Operating limitation: domestic-only ground shipping initially; international shipments require specialized freight handlers.

**Cost implications:** Extremely high ($1,225-$1,340 for 5x E2 batteries to Costa Rica via DHL without insurance). April 2022 Costa Rica mission required significant logistics planning due to battery shipping constraints.

**May-June 2026 Mexico/Import Coordination:** Dan Prendergast identified historical correspondence regarding battery shipments to Mexico. Discovery that ECCN (Export Control Classification Number) was not obtained for batteries; Mexico import was processed as permanent import rather than temporary export. Dan coordinating with customs broker Javi to clarify procedures. Jack Elston deferred response pending additional information (May 27, 2026).

**June 30, 2026 - Battery Import Authorization:** Dan Prendergast requested permission from Jack Elston to sign power of attorney document from Robert Correia (Aeronet/customs broker) to facilitate return of BST battery into the US. Jack Elston approved authorization (June 30, 2026).

### Remote ID (RID) Implementation
- **November 20, 2023:** S1 RID accepted by FAA and became selectable in FAA database (RID000001894). Expanded to S0, S3, and other aircraft platforms through testing protocols established by Jack Elston and team.

### Project Numbering System (September 2023)
- **September 18, 2023:** Meredith Needham finalized customer/project numbering system with specific codes: 200=NASA, 300=NOAA, 350=USGA, 400=Air Force, 450=CU Boulder, 500=Department of Agriculture. Applied to Asana, QuickBooks, and Toggl for consistent tracking.

### Industrial Plan & Asana Portfolio Restructuring (July 23-24, 2026)
- **July 23, 2026:** Decision to implement Industrial Plan tasks in Asana with new portfolio structure. Four new Views created for each pillar of Industrial Plan (separate from current "Active Projects" and "Business Operations" views). Beck Cotter advocated for separate IP project rather than folding tasks into existing projects to accommodate IP items that don't fit naturally into current projects. Linking via Projects or Dependencies to be used for items that naturally connect to existing projects.
- **July 23, 2026:** New project code assigned: [001-24] IRAD Albatross (Maciej Suwinski requesting code for new Albatross project). Meredith Needham assigned project ID and added to Toggl.
- **July 24, 2026:** Maciej Suwinski created