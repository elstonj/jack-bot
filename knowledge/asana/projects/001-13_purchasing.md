_Asana snapshot as of 2026-10-31: 215 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active (ongoing purchasing workflow)
- **Dollar Value:** Not systematically tracked in custom fields; individual orders span from small consumables to thousands of dollars across multiple projects
- **Timeline:** Continuous operational project; orders span dates from Mar 2026 through Dec 2026
- **Key Pattern:** Centralized purchasing intake using Asana form; all 215 tasks are open with 0 completed, indicating this is a workflow system where task closure is not the primary tracking method

## Key Deliverables & Milestones
No traditional milestones. This is a **purchasing intake and tracking system**, not a project with deliverables. Tasks represent purchase orders by vendor and project.

## Task Summary

**Total Tasks:** 215 open, 0 completed

**Assignees:**
- **Meredith O'hara Needham:** ~50 tasks (mostly recent/active orders with near-term due dates)
- **Unassigned:** ~165 tasks (orders in various stages: placed, shipped, received, or in inventory)

**Order Status Breakdown** (from custom field):
- **Order Placed:** ~20 tasks
- **Order Placed in Inventory:** ~80 tasks (flagged for longer-term use or stock)
- **Order Shipped:** ~30 tasks
- **Order Received:** ~50 tasks
- **Not yet placed/pending:** ~35 tasks

**Tax Exempt:** Mixed; majority marked NO, with several "YES" for project-specific equipment (IDIQ Hurricane, S3, S0, Magnetometer)

## Recent Activity

**Upcoming/Near-term Orders (Oct–Nov 2026):**
- Multiple S3 parts (Jaw Stec, MKS servos, north american survival) due Oct 28–31
- S0 AD Switch Fix and related parts due Oct 30–Nov 1
- SOCOM Pope ii orders (Amazon, Aegis/Videology, MCMaster) due Oct–Nov
- IDIQ Hurricane parts (various vendors) due through Nov
- Shop supplies and equipment (digikey, mcmaster, aliexpress, protease) due Oct 24–30

**Recently Placed/Shipped (Sept–Oct):**
- S3 Remote ID Modules (shipped, due Oct 10)
- S3 Backup Regulators (shipped, multiple, due Sept–Oct)
- ByLight/Mustang Pt. 2 orders (mcmaster, mouser) shipped Aug–Sept
- Jawstec, sendcutsend, protolabs orders shipped July–Sept

**Large/Multi-project Orders with Missing Breakdown:**
- Several tasks marked "MULTIPLE PROJECT – PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" (Jaw Stec #69738, digikey #100222302, protease #6634-517, mcmaster multi-project). These flag allocation issues.

## Notes & Context

**System Design:**
- This is a **centralized purchasing tracker**, not a project. The form link in the project notes (https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594) is the intake mechanism; tasks are created from form submissions.
- Custom fields capture: Vendor, Requester, Due Date, Project to Bill, Tax Exempt status, Order Status
- No tasks are marked "completed" because completion is handled outside Asana (items arrive, are logged to inventory, invoiced, etc.)

**Key Requesters (frequency):**
- Joshua Fromm: ~80 tasks (highest volume; shop supplies, S0 IDIQ, S3 sales parts, multi-project)
- Sam: ~20 tasks (S3 fixes, S0 AD parts, hardware, Magnetometer)
- Alex: ~15 tasks (S0 VTOL, S3, Swiftstation, Magnetometer)
- Dan/Dan Prendergast: ~5 tasks (antennas, modules, equipment)
- Ethan/Ethan Domagala: ~10 tasks (ByLight/Mustang Pt. 2 hardware)
- Spencer, Nate, others: ~10 tasks (IRAD General, S0, consumables)

**Projects Most Represented:**
1. **[001-7] IRAD S3** – ~30 orders (regulator fixes, lasers, RF connectors, gimbals, hardware)
2. **[300-3] 2026 IDIQ (Hurricane)** – ~40 orders (Microhard, motors, tubing, composites, batteries, GCS parts)
3. **[451-1] INSTAAR S3 x2** – ~20 orders (servos, bearings, parts, sales inventory)
4. **Shop Supplies** – ~25 orders (soldering, tools, storage, shipping, consumables)
5. **[001-4] IRAD S0 VTOL** – ~15 orders (Jawstec, digikey, APC props, servocity)
6. **General Sales** – ~10 orders (inventory for resale)
7. **[550-1] Navy SBIR: Magnetometer** – ~8 orders (Bartington connectors, GetFPV, amazon)

**Risk Signals:**
- **Untracked Orders in Inventory:** ~80 tasks with status "Order Placed in Inventory" and due date 2026-12-29 appear to be stockpiled or long-term commitments; many have old "when should this be placed" dates (May–Aug 2026), suggesting actual placement occurred earlier but task was not updated.
- **Multi-project Orders Without Breakdown:** At least 5–7 orders lack clarity on which project to bill; requires follow-up.
- **Task Not Closed After Delivery:** Many tasks marked "Order Received" or "Order Shipped" remain open, creating ambiguity on true order status and completion.
- **High Volume, Low Visibility on Spend:** No centralized sum of purchase totals; individual order values are not consistently logged in custom fields.

**Process Improvement Opportunities:**
1. Establish a completion/closure workflow (e.g., close task when invoice received or item logged to inventory).
2. Add dollar amount custom field to all orders for spend tracking.
3. Clarify "Order Placed in Inventory" status—is this committed/on-order or physically received?
4. Require project breakdown for multi-project orders at task creation.
5. Archive old or completed orders to reduce list clutter.