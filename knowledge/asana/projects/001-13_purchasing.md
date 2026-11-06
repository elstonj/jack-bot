_Asana snapshot as of 2026-11-06: 228 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** ACTIVE — High-volume purchasing operations; 228 open tasks, 0 completed
- **Dollar Value:** Not explicitly stated in custom fields; orders range from small supplies to major component purchases across multiple vendors
- **Timeline:** Orders span May 2026 through January 2027, with heavy clustering around June–November 2026
- **Risk Signals:** 
  - **Extreme backlog:** 228 open tasks with no closure mechanism visible
  - **Many overdue or approaching-deadline orders** with "Order Placed," "Order Shipped," or "Order Received" status still marked open
  - **Incomplete project billing:** Numerous tasks flagged "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" (no project assigned for cost allocation)
  - **Stale data:** Orders dated May–August 2026 with status "Order Received" or "Order Shipped" still open, suggesting tasks are not being closed after fulfillment

## Key Deliverables & Milestones
No traditional milestones; this is a purchasing workflow project. Key patterns:

| Project/Vendor Pattern | Count | Notes |
|---|---|---|
| Shop Supplies orders | ~30 | Recurring consumables, tools, equipment |
| [300-3] 2026 IDIQ (Hurricane) | ~25 | Major IDIQ contract requiring multiple component orders |
| [001-7] IRAD S3 | ~20 | Gimbal, power, antenna, and RF components |
| [451-1] INSTAAR S3 x2 | ~15 | Motors, servos, structural parts for 2-unit build |
| [001-4] IRAD S0 VTOL | ~12 | VTOL airframe, motors, landing gear, prototyping |
| [550-1] Navy SBIR: Magnetometer | ~10 | Sensors, connectors, interface boards |
| [600-01] SOCOM Pope ii | ~8 | Recent project; equipment and consumables |
| [043-3] Mustang Pt. 2 | ~6 | Gimbal, fasteners, laser components |

**Major Recurring Vendors:** Jawstec, McMaster Carr, Digikey, Amazon, Mouser, SendCutSend, ProtoCut, Microhard

## Task Summary
- **Total Tasks:** 228 open, 0 completed
- **Assignees:**
  - **Meredith O'hara Needham:** ~25 tasks (active reviewer/purchaser)
  - **Unassigned:** ~200 tasks (likely awaiting fulfillment confirmation or closure)
  
- **Status Breakdown (visible in custom field):**
  - Order Placed: ~80 tasks
  - Order Placed in Inventory: ~110 tasks
  - Order Shipped: ~20 tasks
  - Order Received: ~18 tasks

- **Tax Exempt Field Usage:**
  - YES: ~100 tasks (internal projects, IDIQ, sales)
  - NO: ~128 tasks (commercial supplies, external purchases)

- **Notable Pattern:** Tasks remain open even after "Order Received" or "Order Placed in Inventory" status, indicating **no closure workflow**. The "Placed in Inventory" status suggests items have arrived but tasks are not being marked complete.

## Recent Activity
- **Most Recent Orders (due dates November 2026):** 
  - McMaster Carr, Digikey, Datapro, Minibox orders for multiple projects (due 11/5–11/7)
  - Mouser, Midwest Control Products, Tattu for Hurricane IDIQ
  - Jawstec, Connectors for S0 GCS
  
- **October Orders:** Heavy purchasing for S3 sales (servos, bearings, hobbies vendors), Shop Supplies, Hurricane IDIQ
  
- **Stale Tasks (July–September with "Order Received"):** Jawstec, MKS, 3DR, Horizon Hobby, ProtoCut, SendCutSend, Dronetag — these orders arrived weeks/months ago but remain open in Asana

- **No recent completions:** Zero closed tasks suggests the project uses Asana for requisition logging but not fulfillment tracking/sign-off

## Notes & Context

1. **Form-Based Intake:** Project notes direct all requesters to use a specific Asana form or "your task will auto delete." This is the primary purchasing intake mechanism.

2. **Multi-Project Billing Problem:** ~40–50 tasks are tagged "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" with incomplete project fields. This creates accounting/cost-allocation friction and blocks proper project charging.

3. **Task Lifecycle Breakdown:** 
   - Tasks are created from form submissions
   - Status field updated as order progresses (Placed → Shipped → Received)
   - **But:** Tasks are never marked complete, creating a 228-item graveyard of fulfilled orders
   - Suggests: Need a formal "closure" step (e.g., receipt confirmation, invoice match) or archive workflow

4. **Requesters:** Primarily Joshua Fromm (~120 tasks), Alex (~30), Dan/Dan Prendergast (~8), Sam (~15), Ethan/Ethan Domagala (~10), Spencer (~5), Nate (~3)

5. **Tax Exempt Status:** Heavily used custom field; likely tied to invoicing/accounting integration (many S3, IRAD, and IDIQ orders marked tax-exempt as internal R&D or government contract work)

6. **Vendor Concentration:** 
   - Jawstec: ~40+ orders (custom fabrication, parts)
   - McMaster Carr: ~30+ orders (fasteners, hardware, pneumatics)
   - Amazon: ~25+ orders (general supplies, electronics)
   - Digikey, Mouser: ~20 each (electronics, test gear)
   - Smaller vendors (SendCutSend, Protolabs, servocity, etc.): 5–10 each

7. **Known Issues for Follow-up:**
   - **Backlog Management:** No visible closure process; tasks accumulate indefinitely
   - **Project Allocation:** "MULTIPLE PROJECT" tag prevents accurate cost tracking
   - **Approval Bottleneck:** Some tasks flagged "Requires Approval: Yes" but remain unresolved (e.g., ADS-B for S3, RCDrone.top motors)
   - **Inventory Disconnect:** Orders marked "Placed in Inventory" but not removed from active task list

---

**Recommendation:** This project functions as a **purchase order log** rather than a workflow. Consider implementing a closure trigger (e.g., invoice received, receipt scanned) to auto-archive fulfilled tasks and reduce the open count to actionable items only.