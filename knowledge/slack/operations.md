# #operations

## Overview
The operations channel serves as Black Swift Technologies' central hub for coordinating day-to-day activities, project status updates, facility management, shipping/logistics, procurement, financial tracking, and administrative matters. It functions as a working operations log where decisions are documented, action items assigned, and resources tracked.

**Key participants:** Jack Elston (leadership), Joshua Fromm (hardware/shop lead), Meredith Needham (finance/admin), Parker Vollmer (systems/compliance), Dan Prendergast (soil moisture/research), Maciej Suwinski (VTOL/flight ops), Sam Hild (firmware/electrical), Alex Lomis (mechanical/VTOL), Nate (aircraft builds), James Hannon (project management), Ben Busby (flight operations/QA), Beck Cotter (project coordination), Paige Smith (admin), and numerous other engineers and support staff.

**Activity level:** High-volume channel with 3,430+ messages across multiple batches spanning from July 2020 through April 2026. Activity increased significantly starting in mid-2023 with more structured project management and formalized coordination processes. Recent activity (April 2026) includes AI assistant integration and ongoing project refinements.

---

## Key Decisions

### Office & Facilities
- **July 20, 2020:** Completed office relocation. Jack Elston coordinated with landlord. New facility includes solder station, vacuum dust management system, and industrial curtain dividers for clean/dirty room separation (divider delayed ~1 month due to COVID).
- **May 16-17, 2023:** New office lighting installation scheduled and executed.
- **August 2023:** Alex installed garage door seal for improved weatherproofing.

### Personnel & Management
- **June 2, 2023:** James Hannon hired as new Project Manager to address task overload and process improvements.
- **June 6, 2023:** Jack Elston issued formal travel policy requiring Rippling approval for any leave longer than one day, citing multiple simultaneous absences by S1/S0 build team in May causing project delays.

### Equipment Procurement
- **December 2023:** Drill press acquisition decision pending. Joshua Fromm researching floor-mounted options (Nova 58000 Voyager, Grizzly models) with ~$500+ budget needed for tooling. Jack Elston requested spreadsheet comparison for budget approval.
- **April 2023:** End-of-week cleanup task list implemented with color-coded tool inventory checks assigned to shop manager. Clipboard-based tracking without formal records (Jack Elston assigned responsibility).
- **Lab equipment (2024):** JBC HDE Heavy-Duty soldering station recommended for production line work. 26AWG PTFE wire identified as correct specification for 2.00mm clickmate crimps (not ETFE).

### Lithium Battery Shipping (April 2022 - ongoing)
**Major compliance discovery:** E2 and S2 batteries cannot be shipped internationally without hazmat certification. Multiple carriers (UPS, DHL) rejected shipments.

**Requirements established:**
- IATA hazmat training course (16 hours, ~$1,100-$209 through Hazmat University) - required before international shipment
- UPS dangerous goods contract (domestic only)
- UN-certified packaging and commercial invoices
- Minimum 2-week international shipping timelines

**Solution:** Bill Nickerson coordinated with ProCargo (Houston) to handle hazmat packaging and documentation. Joshua Fromm documented comprehensive lithium shipping checklist including discharge procedures, taping, packing, labeling, and record-keeping. Operating limitation: domestic-only ground shipping initially; international shipments require specialized freight handlers.

**Cost implications:** Extremely high ($1,225-$1,340 for 5x E2 batteries to Costa Rica via DHL without insurance). April 2022 Costa Rica mission required significant logistics planning due to battery shipping constraints.

### Remote ID (RID) Implementation
- **November 20, 2023:** S1 RID accepted by FAA and became selectable in FAA database (RID000001894). Expanded to S0, S3, and other aircraft platforms through testing protocols established by Jack Elston and team.

### Project Numbering System (September 2023)
- **September 18, 2023:** Meredith Needham finalized customer/project numbering system with specific codes: 200=NASA, 300=NOAA, 350=USGA, 400=Air Force, 450=CU Boulder, 500=Department of Agriculture. Applied to Asana, QuickBooks, and Toggl for consistent tracking.

### Asana Project Management System
- **August 2023:** Significant effort to implement Asana with proper numbering conventions. Parker Vollmer led cleanup and structure development. Generic vs. project-specific task categorization issues identified and resolved. Later transitioned to portfolio structure: Active Projects, Internal Projects, Business Operations.

### Shipping Protocol & Insurance (April-May 2023)
- **Critical gap identified:** Packages must be scanned by shipper at pickup/dropoff for insurance coverage to activate. UPS pickup drivers were not scanning packages. Decision to require high-value declaration with signature and obtain drop-off receipts for all shipments.
- **Freight provider selection (June 2023):** Oak Harbor Freight selected over UPS Freight ($438 vs. $2,200 quote for Phase 1 tooling shipment). Parker Vollmer investigating insurance coverage for freight provider option.

### Financial/Accounting
- **March 2023:** Tax-exempt status coordination established with vendors. Joshua Fromm provides vendor lists; Karen contacts with tax-exempt certificate from DigiKey link.
- **Ongoing:** Credit card monitoring and fraud detection protocols maintained. Josh Fromm's card cancelled after unauthorized WordPress.com charges ($40/month for bst.aero migration). Home Depot account unauthorized login investigated and cleared (Karen confirmed legitimate access Nov 2).
- **August 2023:** DigiKey account password set to BSTOct11!; account locked requiring tech support intervention.

### Vendor Management
- **2023-2024:** Parker Vollmer organizing vendor list for procurement software evaluation. Goal: understand vendor roles, projects supported, and active status. Separate tracking needed from accounting system vendor list.
- **Multiple vendor program setups:** Murray State, Notre Dame, and others onboarded with W9 collection and contract setup handled by Meredith Needham.

### International Export & Customs (2024)
- **Decision:** Licensed customs brokers specializing in scientific equipment identified as necessary for international shipments. Joshua Fromm researching freight forwarders for batteries, scientific instruments, drones. Process requires understanding country-specific requirements, deposits, and fees.
- **Export documentation:** ECCN classification requests from CU Boulder for S2 aircraft in compliance process.
- **S2 shipment from NASA Ames:** Richard Kolyer shipment postponed to January 2024 (only aircraft and ground station shipping; launcher retrofitting with safety updates continues separately).

### AI Assistant Development (April 2026)
- **April 6, 2026:** Jack Elston implementing "Jack Bot" AI assistant that reads #operations channel history to provide task summaries and refine outputs based on team feedback.
- **April 16-17, 2026:** Beta testing underway with team feedback. Initial bugs identified:
  - Deadline calculation errors (showing past due dates as "2 days away" and incorrectly flagging completed projects like ADONIS final report)
  - Task relevance issues (marking UMEX-owned tasks as BST responsibilities)
  - Personality too critical/harsh per Paige Smith feedback
- **April 19, 2026:** Jack Elston fixed deadline calculation bugs and improved comment picking. Preserved personality trait (team found "mean" tone helpful/appropriate). Continuing refinement cycle.

### Project Status & Scheduling
- **April 17, 2026:** Mexico flight operations moved to Fall 2026. Navy project tasks completed. (Maciej Suwinski)
- **April 8, 2026:** Maciej Suwinski and Alex Lomis planning last-minute travel for flight testing conclusion (850pm Frontier flight possibility, decision pending test completion).

---

## Projects & Initiatives

### Aircraft & Platform Development

#### S0-VTOL
- **Status (Oct 2024-Jan 2025):** Voltage issue fixed and flight tested successfully. Servo control issues resolved. Hub updates completed. Motor imbalance fix in progress. **50-flight test plan underway** for delivery validation.
- **Earlier (2023):** Multiple flight test iterations identifying pivoter failures and hub