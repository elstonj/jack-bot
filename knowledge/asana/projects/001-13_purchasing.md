_Asana snapshot as of 2026-11-03: 216 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Client/Customer:** Black Swift Technologies (internal procurement for all projects)
- **Dollar Value:** Not aggregated in custom fields; individual orders tracked by vendor and project
- **Timeline:** Ongoing operational function; orders span 2026
- **Status:** **ACTIVE — HIGH VOLUME QUEUE**
- **Team Members Involved:** 
  - **Primary Owner:** Meredith O'hara Needham (assignee for most active intake)
  - **Requesters:** Joshua Fromm (most frequent), Sam, Alex, Dan P., Ethan, Spencer, others
- **Risk Signals:** 
  - **216 open tasks, 0 completed** — no closure workflow evident
  - Many orders marked "Order Placed," "Order Shipped," or "Order Received" remain open in Asana
  - Orders with past "should order by" dates still open (e.g., Amazon labels due 2026-08-08 but "should order" Aug 4)
  - Heavy use of placeholder due date **2026-12-29** (~80+ tasks) suggests backlog or inventory holding queue
  - Multiple tasks with same vendor/project lacking breakdown (e.g., "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN")

---

## Key Deliverables & Milestones
This is a **procurement queue**, not a project with discrete milestones. Key patterns:

| Project | Focus | Order Volume | Notes |
|---------|-------|--------------|-------|
| **[001-7] IRAD S3** | S3 platform components | ~25 orders | Regulators, RF connectors, lasers, gimbal parts, antennas |
| **[300-3] 2026 IDIQ (Hurricane)** | S0 Hurricane IDIQ | ~30 orders | Motors, control boards, servos, composite parts |
| **[451-1] INSTAAR S3 x2** | S3 sales build | ~15 orders | MKS servos, jawstec parts, remote ID modules, hobbyist retailers |
| **[001-4] IRAD S0 VTOL** | S0 VTOL development | ~15 orders | Servos, landing gear, composites, fpv gear |
| **[001-16] IRAD Swiftstation** | Ground station | ~10 orders | GCS wiring, FTDI, OpenUPS, networking |
| **[550-1] Navy SBIR: Magnetometer** | Magnetometer sensor | ~10 orders | Sensor connectors, interfaces, FPV components |
| **Shop Supplies** | General inventory | ~25 orders | McMaster, Amazon, digikey, powerwex (tools, tape, hardware) |
| **[600-01] SOCOM Pope ii** | New project (recent) | ~10 orders | Foam, hardware, videology/aegis components |
| **General Sales** | Revenue-generating S3 sales | ~15 orders | jawstec, MKS, batteries, propellers, chargers |

---

## Task Summary

**Counts:**
- Total: **216 open**
- Completed: **0**
- Effectively closed/received but not marked done: ~50+ tasks marked "Order Received," "Order Shipped," or "Order Placed in Inventory"

**By Status (custom field):**
- Order Placed: ~80 tasks
- Order Placed in Inventory: ~80 tasks
- Order Shipped: ~20 tasks
- Order Received: ~30 tasks
- No status: ~6 tasks

**By Assignee:**
| Assignee | Count | Notes |
|----------|-------|-------|
| Meredith O'hara Needham | ~20 | Recent intake; active ownership |
| Unassigned | ~196 | Vast majority; no active owner after creation |

**Key Requesters (by frequency):**
- Joshua Fromm: ~100 orders (sales, S3 parts, multi-project)
- Sam: ~20 orders (S0/S3 engineering fixes, GCS)
- Alex: ~15 orders (S0 VTOL, Swiftstation, shop)
- Ethan / Ethan Domagala: ~10 orders (ByLight Mustang, gimbal)
- Others: Spencer, Dan P., Nate, Kareem Ahmed, etc.

---

## Recent Activity

**What Should Be Happening:**
Orders marked "Order Received" or "Order Shipped" should be **closed out** to reflect completion. Instead, they remain open.

**Examples of Stale Tasks:**
- **Amazon labels** (2026-08-08 due) — status "Order Placed," requested by Nate for [001-1] IRAD General
- **uni USB C to Ethernet Adapter** (2026-06-11 due) — ordered Jun 8, still open
- **McMaster Hardware** (2026-09-06 due) — marked "Order Received," no closure
- **GetFPV** (2026-09-04 due) — marked "Order Received," unassigned

**Recent Intake (Oct 2026):**
- S3 sales orders: Kipps hobbies, north american survival, jawstec, MKS servos, aliexpress, digikey, protocase
- IRAD S3 orders: PSKN3 antenna, S3 Laser, soldering supplies, S3 fix components
- IDIQ (Hurricane) orders: Microhard sensors, S0 AD Switch Fix
- SOCOM Pope ii: Amazon orders, Aegis/Videology, Commonlands, McMaster, foam toppers

---

## Notes & Context

### Critical Observations

1. **No Closure Workflow**
   - Tasks remain in Asana even after delivery/receipt
   - 0 completed tasks despite 50+ marked "Order Received" or "Order Shipped"
   - Suggests Asana is used for **order intake/tracking**, not project completion

2. **Heavy Multi-Project Allocation**
   - ~15 orders marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION"
   - Many lack cost/allocation detail in notes (e.g., "protolabs for multiple projects," "mcmaster for various projects")
   - Creates ambiguity in project billing

3. **Tax Exempt Status**
   - Heavy use of tax-exempt designation for vendor/sales orders (jawstec, MKS, rockwest, etc.)
   - Suggests resale/component inventory for S3 sales pipeline

4. **Requesters Rarely Follow Form**
   - Project notes state **"USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE"** — form link provided
   - Bulk of tasks appear created via form (structured custom fields present)
   - However, many incomplete/inconsistent entries (missing vendor detail, unclear project mapping)

5. **Inventory Parking Lot**
   - ~80 tasks due 2026-12-29 with status "Order Placed in Inventory"
   - Suggests these are stock builds or forward-looking purchases, not active orders
   - Dates are placeholder; actual due dates likely elsewhere or in external system

6. **Vendor Concentration**
   - jawstec, McMaster Carr, Amazon, digikey dominate
   - Also heavy use of specialized vendors: MKS (servos), Hitec, servocity, rockwest, clearwater composites

---

## Recommended Actions for AI Assistant

- **Do not trust Asana due dates as ground truth** for recent activity; many orders marked "received" are stale
- **Prioritize tasks assigned to Meredith** or recently created (Oct 2026) as active
- **Flag multi-project orders** when discussing cost allocation; request breakdown
- **Use tax-exempt status** to distinguish operational vs. resale purchases
- **Cross-reference with external procurement system** if available; this Asana queue may be export/backup only
- **For status questions:** check custom "Status" field (Order Placed, Received, Shipped, etc.) rather than task completion