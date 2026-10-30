_Asana snapshot as of 2026-10-30: 212 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview

- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active — high-volume operational procurement system
- **Dollar Value:** Not centrally tracked in custom fields; individual orders vary (components to large assemblies)
- **Timeline:** Ongoing; orders range from immediate to 6+ months out (due dates through Dec 2026)
- **Key Pattern:** All tasks use standardized Asana form requiring vendor, requester, project code, tax-exempt status, and placement date

## Task Summary

- **Total Tasks:** 212 open, 0 completed
- **All-hands project:** Nearly all tasks assigned to **Meredith O'hara Needham** (processor) or **Unassigned** (awaiting processing)
- **Task by Status:**
  - Order Placed: ~110 tasks
  - Order Received: ~60 tasks
  - Order Shipped: ~35 tasks
  - Order Placed in Inventory: ~70 tasks
  - Other/unspecified: ~7 tasks

## Key Requesters & Projects

Purchasing requests span multiple concurrent projects:

| Project | Notable Requesters | Order Count | Notes |
|---------|-------------------|------------|-------|
| [001-7] IRAD S3 | Joshua Fromm, Sam, Ethan, Alex | ~35 | Most active; components, gimbal parts, regulators, antenna |
| [451-1] INSTAAR S3 x2 | Joshua Fromm | ~20 | PCBs, servos, connectors, bearing orders for sales |
| [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm, Sam | ~35 | Tubes, servos, batteries, composites, large platform build |
| [600-01] SOCOM Pope ii | Alex, Joshua Fromm, Dan P. | ~15 | Electronics, foam toppers, components |
| [001-4] IRAD S0 VTOL | Alex | ~20 | Motors, servos, sensors, props, Dronetag, protolabs |
| [001-16] IRAD Swiftstation | Alex, Ethan | ~10 | Wiring, sensors, USB adapters, FTDI boards |
| Shop Supplies | Joshua Fromm, Ethan | ~25 | McMaster, Amazon, Digikey, tools, tapes, shipping supplies |
| [550-1] Navy SBIR: Magnetometer | Alex, Sam | ~10 | Sensors, connectors, GetFPV parts |
| [043-3] Mustang Pt. 2 | Ethan, Ethan Domagala | ~12 | Gimbal, laser, fasteners, composite tails |
| [001-1] IRAD General | Nate, Alex | ~8 | Labels, switches, clips, packaging |
| General Sales (No Specific Project) | Joshua Fromm, Alex | ~12 | Motors, props, batteries (for resale) |
| MULTIPLE PROJECT (breakdown pending) | Joshua Fromm | ~8 | Orders requiring project cost allocation; incomplete metadata |

## Recent Activity & Risk Signals

### Approaching Deadlines (Critical)

Many tasks with **Oct 2026 due dates** are still in "Order Placed" or earlier status, suggesting:
- Orders placed within past few days (Oct 8–31 window)
- Delivery expected imminently or already in transit
- No completion/close-out yet in Asana

**Sample approaching deadlines:**
- Oct 8: Microhard 10x p900, 100x p400 — [300-3] Hurricane — due date matches "place date"
- Oct 11: S3 Laser, PSKN3-24/55S Antenna — [001-7] IRAD S3
- Oct 16–17: Multiple S3 parts (jawstec, skygeek, digikey) — all "Order Placed"
- Oct 23: S3 sales orders (deans, hiawatha hobbies, voltroam) — due date matches requested placement

### Overdue Tasks (Concerning)

Several tasks have past-due dates but remain open:
- **Aug 9–Sept 12, 2026:** ~15 tasks due but still in "Order Placed" or "Order Received" (e.g., home depot, GetFPV, jawstec for S3 IRAD)
- **June–July 2026:** ~40 tasks in "Order Placed in Inventory" with Nov 7 due date assigned retroactively (appears to be catch-all placeholder)

### Status Breakdown Patterns

- **Order Placed in Inventory (~70 tasks):** Likely awaiting integration into project assembly or fulfillment. Due date **Nov 7, 2026** appears to be default/placeholder for many older requests.
- **Order Received (~60 tasks):** In receiving workflow; some dated Aug–Sept still unprocessed.
- **Order Shipped (~35 tasks):** Tracked but not yet marked complete; some from July–Aug.
- **Order Placed (~110 tasks):** Most recent; placed within last 2 months, expected delivery incoming.

## Data Quality Issues

1. **Incomplete Project Codes:** ~8 tasks list "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" (e.g., mcmaster for multiple projects, S3 RF Connectors, protolabs, digikey). These prevent accurate cost allocation.

2. **Stale Due Dates:** Large batch of tasks (70+) assigned **Nov 7, 2026** as due date despite requested order dates in May–July 2026. Suggests tasks not closed out after delivery.

3. **No Completion Tracking:** 0 completed tasks despite 212 open. Orders marked "Order Received" or "Order Shipped" should likely be closed; system appears to use status field instead of task completion.

4. **Unassigned Tasks:** ~100 tasks unassigned (awaiting Meredith review/action). May indicate backlog or new requests pending intake.

5. **Tax Exempt Status:** Tracked but not aggregated. Mix of YES/NO across projects; likely affects billing/compliance.

## Vendor Patterns

**Most Frequent Vendors:**
- McMaster Carr / McMaster (electronics, fasteners, hardware)
- Jawstec (aerospace/UAV components)
- Amazon (consumables, misc)
- Digikey (electronics, components)
- Protolabs (custom fabrication)
- Mouser (electronics)
- Sendcutsend (sheet metal fabrication)
- Horizon Hobby, GetFPV, Skygeek (hobbyist UAV suppliers)
- Composites & materials: Clearwater Composites, Composites Store, Rockwest
- Specialized: Bartington (sensors), Microhard (RF modules), Dronetag (remote ID), APC (props)

## Recommendations for AI Assistant

1. **Prioritize Oct 2026 orders** for status checks; delivery imminent.
2. **Flag "MULTIPLE PROJECT" orders** as requiring clarification before billing.
3. **Recommend closing** tasks in "Order Received" or "Order Shipped" status that are >30 days old.
4. **Use Nov 7, 2026 due date as signal** for stale/unbilled inventory—not real deadline.
5. **Cross-reference requesters** with project leads to validate project codes and priorities.
6. **Monitor Meredith's workload:** Single point of failure for 100+ open purchase orders.