_Asana snapshot as of 2026-11-13: 192 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview

- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Timeline:** Ongoing operational purchasing function; tasks span from historical dates (May 2026) through future dates (Jan 2027)
- **Status:** Active — 192 open tasks, 0 completed. **This indicates a process issue:** tasks are not being closed after orders are fulfilled or received. Many tasks show "Order Received" or "Order Shipped" status but remain open in Asana.
- **Notable Pattern:** Heavy use of custom fields (Tax Exempt status, Requires Approval, Order Status) but poor task closure discipline. Many orders from mid-2026 and earlier remain open despite completion indicators.

## Key Context

This is BST's **centralized purchasing/procurement project**. All purchase requests from the engineering team flow through this project via a form (linked in project notes). Requesters include Josh Fromm, Sam, Dan, Alex, Ali Sulehria, Jack Elston, and others across multiple projects.

**Process Issue:** The project shows extensive backlog of closed/received orders that have not been marked complete in Asana. This creates noise and obscures actual open work.

## Task Summary

- **Total Open Tasks:** 192
- **Total Completed:** 0
- **Primary Assignee:** Meredith O'hara Needham (manages majority of active/pending orders)
- **Unassigned Tasks:** ~130+ orders marked as "Order Received," "Order Shipped," or "Order Placed in Inventory" — these should likely be closed

### Order Status Breakdown (from custom field "Status"):
- **Order Placed:** ~15 tasks
- **Order Shipped:** ~8 tasks  
- **Order Received:** ~40+ tasks
- **Order Placed in Inventory:** ~90+ tasks
- **Pending/No Status:** ~40 tasks requiring action

### Top Requesters (by volume):
- **Joshua Fromm:** ~100+ orders (S3 sales, S0 hurricane/IDIQ, general supplies)
- **Alex:** ~20+ orders (S0 VTOL, Swiftstation, Magnetometer, Pope ii)
- **Sam:** ~15+ orders (S3 fixes, S0 AD fixes, various component fixes)
- **Dan/Dan Prendergast:** ~5 orders (SOCOM, RemoteID modules, support)
- **Others (Ali, Jack, Spencer, Ethan, Nate):** ~10 orders each

## Key Projects Being Purchased For

Orders span across multiple BST projects:
- **[001-7] IRAD S3** — significant composite, motor, antenna, regulator orders
- **[300-3] 2026 IDIQ (Hurricane)** — S0 platform parts, hurricane-specific components
- **[451-1] INSTAAR S3 x2** — S3 sales/production components (servos, bearings, parts)
- **[001-4] IRAD S0 VTOL** — VTOL platform parts
- **[001-16] IRAD Swiftstation** — GCS and antenna components
- **[600-01] SOCOM Pope ii** — newer project with recent orders
- **[001-23] SOCOM S0-AD** — FLIR cameras, fixes
- **[550-1] Navy SBIR: Magnetometer** — sensor components
- **Shop Supplies** — consumables, tools, hardware (recurring)
- **General Sales** — inventory for product sales

## Recent Activity & Risk Signals

### Approaching Deadlines (Nov 2026):
- Multiple orders due Nov 11–14, 2026 (most already "Order Placed" or beyond)
  - Composite materials for S3 (backordered)
  - ACP composites, Hillside composites for S3 sales
  - Safety glasses restock
  - S3 motor grounding
  - McMaster multi-project order
  - FLIR Hadron camera for SOCOM

### Orders Long Overdue with No Closure:
- **McMaster order (#0903JELSTON)** — Due Sep 6, 2026, status "Order Received" — **UNASSIGNED, NEVER CLOSED**
- **GetFPV (#1001507386)** — Due Sep 4, 2026, "Order Received" — **UNASSIGNED, NEVER CLOSED**
- **Amazon for S0 mags** — Due Sep 3, 2026, "Order Received" — **UNASSIGNED, NEVER CLOSED**
- **3dr (#5804)** — Due Aug 30, 2026, "Order Received" — **UNASSIGNED, NEVER CLOSED**
- Many others from July–August 2026 in same state

### Orders in "Placed in Inventory" Status (Due Jan 2027, Dec 2029):
~90 tasks marked "Order Placed in Inventory" with due dates in late 2026–2027. These appear to be stocked/backlog items. **None are closed.**

## Notes & Context

1. **Form-Based Intake:** All new requests must use the Asana form or tasks auto-delete (per project notes). Form captures:
   - Vendor/order description
   - Requester name
   - Desired order date
   - Project to bill
   - Tax exempt status
   - Approval requirement (>$200)

2. **Frequent Vendors:** DigiKey, McMaster-Carr, Mouser, JawsTec, Amazon, Sendcutsend, Protolabs — standard electronics/hardware suppliers plus custom fab (Sendcutsend, Protolabs, PCBWay).

3. **Tax Exempt Orders:** Many S3 sales, S0 hurricane, and component orders marked tax-exempt (likely BST internal use or gov't contracts).

4. **Multi-Project Orders:** Several orders (mcmaster, batteryspace, digikey, jawstec, etc.) tagged "MULTIPLE PROJECT — PLEASE PROVIDE BREAKDOWN" but without detailed breakdown in task descriptions. Creates billing ambiguity.

5. **Process Debt:** Heavy backlog of received/shipped orders not marked complete creates administrative friction. Recommend:
   - Batch close all "Order Received" and "Order Shipped" items older than 30 days
   - Implement a weekly/bi-weekly task closure workflow
   - Consider automating task closure via form-based status updates

6. **One Overdue Item:** McMaster order for S2 Oklahoma project due **Feb 24, 2025** — this date appears to be a data error (past date in 2025) and should be corrected.