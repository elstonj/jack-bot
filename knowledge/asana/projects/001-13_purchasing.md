_Asana snapshot as of 2026-10-28: 207 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active - high-volume purchasing workflow
- **Dollar Value:** Not explicitly tracked in custom fields; appears to span multiple projects with individual orders ranging from small shop supplies to significant component purchases
- **Timeline:** Orders span from past due (Feb 2025) through Oct 2026, with heaviest concentration in Oct 2026
- **Risk Signals:** 
  - **207 open tasks, 0 completed** — indicates poor task closure hygiene; many orders marked "Order Placed," "Order Received," "Order Shipped," or "Order Placed in Inventory" remain open
  - Multiple past-due orders (dating back to Feb 2025, Aug 2026) still marked open
  - Heavy assignment skew: most tasks assigned to Meredith O'hara Needham; many unassigned

## Key Deliverables & Milestones
This is a **purchasing intake and tracking project**, not a traditional deliverables project. Key patterns:

- **Projects with highest order volume:**
  - [001-7] IRAD S3 — ~20 orders (antennas, laser, backup regulators, gimbal parts, hardware)
  - [300-3] 2026 IDIQ (Hurricane) — ~18 orders (tubes, servos, batteries, GCS parts, composites)
  - [451-1] INSTAAR S3 x2 — ~15 orders (MKS servos, PCBs, remote ID modules, bearings)
  - [600-01] SOCOM Pope ii — ~10 orders (Amazon, McMaster, foam toppers, electronics)
  - Shop Supplies (General) — ~25 orders (digikey, McMaster, Amazon, hand tools, workspace equipment)

- **Common vendors:** McMaster, Jawstec, Digikey, Amazon, Protolabs, Sendcutsend, Mouser, Horizon Hobby, Sparkfun

## Task Summary

| Metric | Count |
|--------|-------|
| **Total Open Tasks** | 207 |
| **Total Completed Tasks** | 0 |
| **Assigned to Meredith O'hara Needham** | ~90 tasks |
| **Unassigned** | ~117 tasks |

**Order Status Breakdown (inferred from "Status" custom field):**
- Order Placed: ~80 tasks
- Order Shipped: ~35 tasks
- Order Received: ~50 tasks
- Order Placed in Inventory: ~40 tasks
- (No status recorded): ~2 tasks

**Key Requesters:**
- Joshua Fromm (heavy user — ~70 orders across multiple projects)
- Alex / Alex Lomis (~20 orders)
- Sam (~10 orders, mostly S3/S0 parts and backups)
- Dan / Dan Prendergast (~5 orders)
- Spencer (~3 orders)
- Ethan / Ethan Domagala (~10 orders, ByLight/Mustang project focus)
- Others: Nate, Jack Elston, Kareem Ahmed

**Tax Exempt Status:** ~60% of orders are tax-exempt (YES), suggesting research/government funding eligibility.

## Recent Activity

**Approaching/Past-Due Deadlines (Oct 2026):**
- Oct 8: Microhard 10x p900 and 100x p400 (Jack Elston, Hurricane project)
- Oct 10: S3 Laser, Soldering Supplies
- Oct 11: PSKN3 antenna (StepGlobal), jawstec for SOCOM Pope, protolabs for SOCOM-Pope
- Oct 14–24: Heavy cluster of shop supplies and multi-project orders (McMaster, Digikey, Aliexpress, Protocase, Powerwerx)
- Oct 23: Dean connectors, Hiawatha Hobbies, Digikey for various projects (all Joshua Fromm, S3/S0 projects)
- Oct 29: McMaster (Alex, IRAD S3), MKS servos (Joshua, INSTAAR S3)

**Status Drift:** Many tasks marked "Order Placed," "Order Shipped," or "Order Received" remain OPEN, suggesting **no workflow to close tasks post-fulfillment**. Orders from Aug–Sep 2026 are still open despite "Order Received" or "Order Shipped" status.

**Historical Past-Due:**
- Feb 2025: McMaster for [039-1] S2 Oklahoma (due date Feb 24, 2025 — nearly a year overdue)
- Multiple Aug 2026 orders still marked open with "Order Placed in Inventory" status

## Notes & Context

### Process Issues
1. **No Task Closure Workflow:** 207 open tasks with 0 completed indicates that fulfilled orders are not being closed. This makes the project backlog difficult to triage and masks completion rates.
2. **Asana Submission Form Required:** Project notes reference a form (https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594) and state "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE" — suggests orphaned tasks may be auto-purged, yet 207 remain open.
3. **Dual Tracking:** Some orders tracked by both project (e.g., [001-7] IRAD S3) and by requester name, indicating potential for duplication or missed consolidation.

### Custom Fields in Use
- **Project** (required): Maps to BST project codes or generic categories (Shop Supplies, General Sales, MULTIPLE PROJECT)
- **Status:** Order Placed, Order Shipped, Order Received, Order Placed in Inventory (inferred via workflow, not closed in Asana)
- **Tax Exempt?:** YES/NO
- **Requires Approval?:** YES/NO (mostly NO; one ADS-B order for [001-7] marked YES)
- **Name of requester:** Free text; inconsistent capitalization

### Multi-Project / Unclear Billing
~15 orders marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — these lack clear project assignment and require manual follow-up.

### Recommended Actions
1. **Implement task closure:** Define a "fulfilled" or "received and closed" workflow to reduce open-task noise.
2. **Consolidate multi-project orders:** Clarify which projects should be billed before closing.
3. **Archive aged orders:** Feb 2025 McMaster task should be archived or escalated if truly outstanding.
4. **Assign unassigned tasks:** ~117 unassigned tasks should be routed or consolidated with Meredith.