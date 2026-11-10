_Asana snapshot as of 2026-11-10: 179 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active — high-volume purchasing coordination project
- **Dollar Value:** Not aggregated in visible custom fields; individual orders tracked across multiple projects (IRAD variants, INSTAAR S3, Hurricane IDIQ, Navy SBIR Magnetometer, SOCOM Pope II, Shop Supplies, and others)
- **Timeline:** Ongoing; orders span from April 2026 through January 2027, with most active procurement Nov 2026–Dec 2026
- **Team Members:** Meredith O'hara Needham (assignee), plus requesters: Joshua Fromm, Alex, Jack Elston, Dan P., Dan Prendergast, Sam, Ethan, Spencer, Nate, Nathaniel Straus, Alex Lomis

## Key Observations

### Task Volume & Status
- **179 open tasks, 0 completed** — This is a **workflow project, not a delivery project.** Tasks represent purchase orders in various stages (placed, shipped, received, in inventory) rather than work items to be closed. The form submission process (`https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594`) generates tasks automatically, and they remain open for tracking/audit.

### Order Status Distribution
Tasks are organized by status custom field:
- **Order Placed** (~15 tasks) — Most recent; due dates Nov 2026
- **Order Shipped** (~3 tasks) — Transitional stage
- **Order Received** (~40 tasks) — Delivered but not yet closed
- **Order Placed in Inventory** (~115 tasks) — Received and stored; majority of backlog

### Key Projects Being Procured For
1. **[300-3] 2026 IDIQ (Hurricane)** — Heavy component purchases (Microhard, icare, mouser, digikey, protolabs, craftcloud, vertiq, bluebird servos)
2. **[001-7] IRAD S3** — Antenna, laser, regulators, remote ID modules, RF connectors
3. **[451-1] INSTAAR S3 x2** — Servos, bearings, remote ID, survival gear
4. **[001-4] IRAD S0 VTOL** — Protolabs, SendCutSend, Dronetag, IRLock, APC props
5. **[001-16] IRAD Swiftstation** — GCS wiring, FTDI, OpenUPS, Sparkfun
6. **[550-1] Navy SBIR: Magnetometer** — Bartington sensors, batteries, FPV components
7. **[600-01] SOCOM Pope II** — Hardware, Aegis/Videology, mattress toppers (field deployment kit?)
8. **[001-23] SOCOM S0-AD** — Jawstec, protolabs (Quote 6634-517)
9. **Shop Supplies** — Amazon, McMaster, Digikey, Home Depot (consumables, tools, storage)
10. **General Sales / Multiple Project** — Jawstec, SendCutSend, Digikey (components for inventory/resale)

### Primary Requesters & Patterns
- **Joshua Fromm** — ~90% of requests; drives procurement across all projects
- **Alex / Alex Lomis** — IRAD projects, SOCOM Pope II, Navy SBIR
- **Sam** — Fix/repair parts and component backups (S3 regulators, S0-AD fixes, dronecan boards)
- **Dan Prendergast / Ethan** — Shop supplies, field deployment equipment

### Vendor Concentration
- **Jawstec** — Most frequent single vendor (~20+ orders), specialized parts/machining
- **McMaster** — Hardware/fasteners (shop supplies, project-specific)
- **Amazon** — General supplies, shop inventory
- **Digikey, Mouser** — Electronics components
- **SendCutSend, Protolabs** — Fabrication services
- **Specialty vendors** — Servocity, MKS, Dronetag, Microhard, Vertiq, Rockwest, etc.

### Tax-Exempt Orders
Many orders marked "Tax Exempt?: YES" — indicates BST may have nonprofit or government contractor status; primarily on IRAD, Hurricane, and Navy SBIR projects.

### Notable Data Quality Issues
- **Multiple project entries** — Many tasks have "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" but lack itemized detail (e.g., jawstec #72163, batteryspace #506512, digikey #102698013)
- **Incomplete project fields** — Some tasks have truncated project names in custom field data
- **Old requested dates vs. due dates** — Tasks show "When should this order be placed?" dates from May–Oct 2026, but due dates often Nov–Dec 2026, suggesting orders were already placed or delayed
- **One anomalous due date** — McMaster task due 2025-02-24 ([039-1] S2 Oklahoma) is in the past and may be a data error or archived project

---

## Recent Activity

**Most Recent Orders (Nov 2026)**
- Sendcutsend, Amazon shop supplies, McMaster, Microhard (Hurricane parts), Eugene Hobbies, Jawstec, Batteryspace, Mouser (S0 IRAD), Kipper's Hobbies, McMaster (multi-project)

**Orders Transitioning to Shipment (Late Oct 2026)**
- Jawstec S3 parts (#71988), S0-AD radio fix, MMaster (#1105JELSTON), Digikey multi-project, Datapro, Minibox, MKS servos (S3)

**Received & In Inventory (Aug–Oct 2026)**
- Large backlog of older orders now in stock inventory status, spanning all projects

---

## Notes & Context

1. **Workflow Design**: This project uses Asana as an audit trail and status tracker for procurement, not a task management board. The form forces structure and prevents duplicate/malformed entries. Tasks should only be closed when the purchase is fully reconciled (received, invoiced, booked to correct cost center).

2. **Cost Tracking**: Dollar amounts are not visible in the task-level custom fields provided. Budget tracking likely happens in a separate finance system or in order notes (brief order descriptions are sometimes included but incomplete).

3. **Multi-Project Allocations**: ~15–20 orders reference multiple projects but lack line-item breakdown. Joshua Fromm (primary requester) should be asked to provide cost allocation details for accurate project accounting.

4. **Shipping/Delivery**: "Estimated Ship Date" field appears on some tasks (e.g., amazon for S0 mags, 2026-08-31) but is sparse. No delivery confirmation or receipt date tracking is visible.

5. **Approval Workflow**: Most orders marked "Requires Approval?: No" except one ADS-B item for S3 (marked "Yes"). No approval assignments visible; suggest reviewing approval rules if orders >$200 require sign-off.

6. **Stale Inventory Backlog**: ~115 orders in "Order Placed in Inventory" status with due dates ranging back to July 2026. These should be archived or closed out; they clutter active procurement visibility.

---

## Recommended Actions
- Clarify which "MULTIPLE PROJECT" orders need cost breakdowns and follow up with requesters
- Archive completed/received orders older than 30 days to reduce clutter
- Implement receipt/invoice-matching workflow to close tasks and trigger accounting reconciliation
- Add dollar amount roll-up to understand total pipeline spend by project
- Review one 2025 McMaster task (due date error?)