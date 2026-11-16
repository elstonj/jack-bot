_Asana snapshot as of 2026-11-16: 194 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview

- **Owner:** Meredith O'hara Needham
- **Team:** Whole BST team (submits purchase requests via form)
- **Status:** Active and heavily used
- **Timeline:** Ongoing operational purchasing system
- **Key Pattern:** This is BST's centralized purchasing request tracking project, not a traditional deliverable project

**Note:** This project serves as a **purchasing intake and tracking system**. It contains 194 open tasks representing pending, placed, received, or inventory-staged purchase orders across multiple internal projects and general shop supplies.

---

## Task Summary

- **Total Tasks:** 194 open, 0 completed
- **Assigned:** Meredith O'hara Needham (primary processor) handles most current approvals/placements; many older tasks unassigned
- **Task Distribution by Status:**
  - Order Placed: ~40 tasks
  - Order Shipped: ~8 tasks
  - Order Received: ~30 tasks
  - Order Placed in Inventory: ~100+ tasks
  - Pending placement: ~16 tasks

---

## Key Requesters & Projects

### Top Requesters
1. **Joshua Fromm** – ~80 tasks (S3 sales parts, IRAD S0 hurricane, shop supplies, multi-project orders)
2. **Alex / Alex Lomis** – ~20 tasks (S0 VTOL, Swiftstation GCS, Navy SBIR Magnetometer, SOCOM Pope ii)
3. **Spencer** – ~5 tasks (S3, IRAD flight testing, soil moisture)
4. **Sam** – ~20 tasks (S3 motor/regulator fixes, hurricane parts, remote ID modules)
5. **Dan / Dan Prendergast** – ~8 tasks (SOCOM S0-AD, general support, Pope ii)
6. **Ethan / Ethan Domagala** – ~8 tasks (Mustang Pt. 2, ByLight gimbal, shop supplies)
7. **Ali Sulehria** – 1 task (QC kit materials)

### Major Projects Billed
- **[001-7] IRAD S3** – ~25 orders (motors, regulators, RF components, composites)
- **[300-3] 2026 IDIQ (Hurricane)** – ~35 orders (S0 parts, tubes, batteries, servos, composites)
- **[451-1] INSTAAR S3 x2** – ~20 orders (S3 sales parts: servos, bearings, composites)
- **[001-4] IRAD S0 VTOL** – ~15 orders (Jawstec, Sendcutsend, protolabs, servocity)
- **[001-16] IRAD Swiftstation** – ~10 orders (GCS wiring, OpenUPS, Microhard)
- **[600-01] SOCOM Pope ii** – ~15 orders (mcmaster, Aegis/Videology, composites)
- **[001-23] SOCOM S0-AD** – ~5 orders (FLIR camera, protolabs)
- **[550-1] Navy SBIR: Magnetometer** – ~10 orders (Navy mag sensor, batteries, connectors)
- **Shop Supplies** – ~30 orders (McMaster, Amazon, Home Depot, safety supplies)
- **Future Sales** – ~15 orders (S3 manufacturing parts: protolabs, Digikey, ACP composites)
- **General Sales** – ~10 orders (various S3 components)

---

## Recent Activity

### Immediate Due Dates (November 2026)
- **Nov 13:** Dronetag DRI RID Module for S3 flight testing (Spencer, requires approval)
- **Nov 13:** Jawstec S3 parts; mcmaster for various projects; composite envisions S3
- **Nov 12:** FLIR Hadron 640R Camera for SOCOM S0-AD (Dan); cst sales S3; PTC motor grounding
- **Nov 11:** Composite envisions S3 (backorder); Sendcutsend; jawstec S3; mcmaster
- **Nov 15:** Protolabs S3 sales (#1858-331, already placed); digikey S3 parts; QC kit materials; ACP composites; instrumart
- **Nov 14:** Safety glasses restock; S3 motor grounding; hillside composites

### Status Patterns
- **Order Placed:** ~40 orders in transit, many placed Nov 3–13, 2026
- **Order Shipped:** 8 orders (jawstec, mcmaster, datapro, minibox, PTC, S3 motor grounding, protokase, jawstec multi-project)
- **Order Received:** ~30 orders (jawstec S3, Amazon, mcmaster, digikey, mks servos, dated late Aug–early Nov)
- **Order Placed in Inventory:** ~100+ long-tail orders (many dated Apr–Oct 2026, including S3 regulators, hurricane parts, shop equipment, ByLight gimbal parts)

### Aging Inventory Orders
Many "Order Placed in Inventory" tasks have due date **2027-01-04** or **2026-12-29** despite placement dates from April–October 2026. These appear to be items staged for future builds or held pending project scheduling.

---

## Notable Patterns & Risk Signals

### High-Volume Vendors
- **Jawstec** – ~15 orders (S3 parts, sales, multi-project, hurricane, SOCOM)
- **McMaster Carr** – ~15 orders (shop supplies, hardware, multi-project)
- **Mouser / Digikey** – ~10 orders (electronics, multi-project)
- **Amazon** – ~12 orders (shop supplies, S0 parts, S3, hurricane, Navy mag)
- **Protolabs** – ~5 orders (S3 sales, S0 VTOL, hurricane, SOCOM, S0 IDIQ)

### Incomplete Data
- Many tasks show **truncated project names** and **incomplete billing info** (e.g., "Future Sales (Provide extra info)," "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN").
- Several "MULTIPLE PROJECT" orders lack detail on cost allocation.
- Some vendor quotes show **no dollar amounts** in task notes.

### Tax Exempt Tracking
- **Tax Exempt: YES** – ~50 orders (mostly sales parts, composites, research components)
- **Tax Exempt: NO** – ~100+ orders (electronics, shop supplies, hardware)

### Approval Requirements
- Only **2 tasks marked "Requires Approval: Yes"**:
  1. Dronetag DRI RID Module (Spencer, due Nov 13, requires approval)
  2. ADS-B for S30002 (Sam, inventory, requires approval)
- Suggests most purchases are under $200 thresholds or pre-approved.

### Aging & Unassigned Tasks
- ~30 tasks remain **unassigned** (no owner listed), many with status "Order Received" or "Order Placed in Inventory" from Aug–Oct 2026.
- These may be awaiting closure or cost allocation confirmation.

### Risk: Stale Data
- Oldest tasks (e.g., "McMaster" for S2 Oklahoma, due **2025-02-24**) suggest Asana is not being used to close out completed purchases.
- Project notes direct users to **use a form or tasks will auto-delete**, but 0 completed tasks and 194 open indicate either:
  - Form submissions bypass Asana closure, or
  - Tasks are manually kept open for accounting/archival.

---

## Notes & Context

1. **Intake Mechanism:** The project notes reference a mandatory Asana form. Users who don't use it risk auto-deletion. This suggests purchasing requests are flowing in via form, but many old tasks remain open.

2. **Financial Tracking:** No visible total spend or budget cap in project-level data. Dollar amounts appear only in incomplete vendor quotes or task names (e.g., order numbers). Recommend establishing a summary dashboard or milestone for total purchasing spend per project.

3. **Backorder Items:** At least 2 orders explicitly marked backorder (e.g., composite envisions S3 backorder, due Nov 11).

4. **Vendor Relationships:** Heavy reliance on **Jawstec**, **Protolabs**, **Mouser**, **Digikey**, **McMaster** for recurring supply chain.

5. **Project Health:** No visible overdue tasks (all due dates are Nov 2026 or later, except one Feb 2025 McMaster order for archived S2 Oklahoma project). Most "Order Placed" tasks are recent (placed Nov 3–13).

6. **Inventory Strategy:** Significant use of "Order Placed in Inventory" status (100+ tasks) with future due dates suggests BST pre-stages components for multiple upcoming builds. Consider reconciling these against actual build schedules.