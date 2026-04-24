# #operations

## Overview
The operations channel serves as Black Swift Technologies' central hub for coordinating day-to-day activities, project status updates, facility management, shipping/logistics, procurement, financial tracking, and administrative matters. It functions as a working operations log where decisions are documented, action items assigned, and resources tracked.

**Key participants:** Jack Elston (leadership), Joshua Fromm (hardware/shop lead), Meredith Needham (finance/admin), Parker Vollmer (systems/compliance), Dan Prendergast (soil moisture/research), Maciej Suwinski (VTOL/flight ops), Sam Hild (firmware/electrical), Alex Lomis (mechanical/VTOL), Nate (aircraft builds), James Hannon (project management), Ben Busby (flight operations/QA), Beck Cotter (project coordination), Paige Smith (admin), and numerous other engineers and support staff.

**Activity level:** High-volume channel with 3,430+ messages across multiple batches spanning from July 2020 through April 2026. Activity increased significantly starting in mid-2023 with more structured project management and formalized coordination processes. Continues through April 2026 with project refinements, AI assistant integration refinements, NDAA compliance discussions, and operational coordination.

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

### NDAA Compliance (April 17, 2026)
**Status Assessment:**
- **S0-VTOL, S0-AD, E2:** Can be made NDAA compliant; self-certification process (no formal federal certification required)
- **S3:** No electronics with final assembly in China; mechanical components currently manufactured in China but can be sourced domestically at increased cost; compliant or can be made compliant
- **S0-AD:** Similar status to S3; electronic components need assessment; rotary latches contain electronics requiring review
- **E2:** Already sold one NDAA-compliant unit (RC receiver swapped). Self-certification process confirmed by Maciej Suwinski
- **Marketing guidance:** Avoid "NDAA Certified" terminology (no formal certification process exists). Use safer language like "NDAA Compliant" with supporting documentation (example provided: Google Doc with E2 compliance details)
- **Decision:** Team can market NDAA compliance on S3 and S0-AD per Maciej Suwinski's guidance; focus on eliminating Chinese-origin microelectronics and final assembly concerns
- **Responsibility:** Paige Smith coordinating marketing language and compliance documentation with input from Maciej, Joshua Fromm, and Alex Lomis

### AI Assistant Development (April 2026)
- **April 6, 2026:** Jack Elston implementing "Jack Bot" AI assistant that reads #operations channel history to provide task summaries and refine outputs based on team feedback.
- **April 16-17, 2026:** Beta testing underway
- **April