_Asana snapshot as of 2026-11-01: 215 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner**: Meredith O'hara Needham
- **Team**: BST (Whole Team)
- **Status**: Active — high-volume purchasing coordination across multiple projects
- **Timeline**: Orders span May 2026 through December 2026 (many with Dec 29 holding dates)
- **Risk Signals**: 
  - **215 open tasks, 0 completed** — indicates tasks are not being closed after fulfillment
  - Significant backlog of orders with "Order Placed," "Order Shipped," "Order Received," and "Order Placed in Inventory" statuses still marked open
  - Many orders have passed their requested placement dates but remain open
  - Form-based workflow (linked in project notes) may not be automatically closing tasks

## Key Patterns & Structure

**Project Billing Categories:**
- [001-7] IRAD S3 (high volume)
- [300-3] 2026 IDIQ (Hurricane) (high volume)
- [451-1] INSTAAR S3 x2 (sales-related orders)
- [001-4] IRAD S0 VTOL
- [550-1] Navy SBIR: Magnetometer
- [001-16] IRAD Swiftstation
- [043-3] Mustang Pt. 2
- [600-01] SOCOM Pope ii
- [001-23] SOCOM S0-AD
- [001-18] IRAD Soil Moisture
- [212-2] NASA S2 & Parts
- [001-1] IRAD General
- Shop Supplies (general)
- General Sales (No Specific Project)
- MULTIPLE PROJECT (cross-project orders needing breakdown)

**Order Statuses in Use:**
- Order Placed
- Order Shipped
- Order Received
- Order Placed in Inventory
- Various vendor confirmations embedded in task names

## Task Summary

**Volume**: 215 open tasks (0 completed)

**Assigned vs. Unassigned:**
- Most tasks assigned to: **Meredith O'hara Needham** (appears to be the purchasing coordinator)
- Many tasks later marked **Unassigned** (likely after initial assignment)
- A few unassigned from start: McMaster Hardware order, GetFPV, amazon for s0 mags, etc.

**Key Requesters** (by frequency):
- Joshua Fromm (highest — ~80+ orders across shop supplies, IDIQ, S3 sales, various projects)
- Sam (S3 repairs, Hurricane parts, Magnetometer)
- Alex (SOCOM Pope ii, S0 VTOL, Magnetometer, Swiftstation)
- Ethan / Ethan Domagala (ByLight/Mustang Pt. 2 orders)
- Dan Prendergast (Customer Support, SOCOM Pope ii)
- Others: Nate, Spencer, Kareem Ahmed, Dan P., Alex Lomis

**Tax Exempt Status:**
- Heavy mix; many IDIQ, S3 sales, and shop supply orders marked YES
- Most external orders (Amazon, Digikey, etc.) marked NO

**Requires Approval:**
- Most orders marked NO
- One flagged YES: ADS-B for S30002 (#106880), RCDrone.top C-Astral SQA Motors (#12503)

## Recent Activity & Timeline Observations

**Approaching/Recent Deadlines (Oct–Nov 2026):**
- Oct 4: S3 fix (#102016142) — Order Placed, IRAD S3
- Oct 8: Microhard p900/p400 — IDIQ Hurricane
- Oct 10: S3 Laser, Soldering Supplies, S3 Remote Id Modules
- Oct 17: S0 AD PSNS Full fix, Extra dronecan programmer boards
- Oct 23–31: Heavy cluster of S3 sales orders (jawstec, mks servos, north american survival, RF connectors)
- Nov 1: S0 AD Switch Fix, Amazon Shop Supplies Tapes, mcmaster S3 order, hiawatha hobbies S3 sales
- Nov 7: Large batch of "Order Placed in Inventory" orders (mouser, Midwest control, tattu, jawstec, connectors, amazon for equipment, etc.)

**Older Orders Still Open (May–Sep 2026):**
- Many with "Order Received" or "Order Shipped" status dating to July–August still open
- Examples: rockwest for s3 sales, Jawstec S0 VTOL Pt2, horizon hobby for s0 vtol, Digikey GCS wiring, tomas liu for s3 sales, protolabs, mouser orders, SendCutSend, Dronetag, 3dr
- Suggests these require invoicing, reconciliation, or final closure before task can be marked complete

**Stale "Placement" Dates:**
- Many orders have "When should this order be placed" dates in April–July 2026, but tasks are still open in October–December
- Indicates orders were placed long ago and tasks should have been resolved

## Notable Patterns

1. **Heavy Joshua Fromm Volume**: Requestor for ~80+ orders across multiple projects—suggests he may be de facto project coordinator or supplier liaison for IDIQ Hurricane, S3 sales, and shop supplies

2. **Multi-Project Orders**: ~10+ tasks marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" — these need detailed line-item tracking (protocase, digikey various projects, jawstec for multiple projects, mcmaster for various, powerwerx, Extra dronecan boards, pololu)

3. **Vendor Relationships**: Frequent vendors include Jawstec, McMaster Carr, Digikey, Amazon, Mouser, SendCutSend, Protolabs, Servocity, Mouser, RockWest — suggests established procurement pipeline

4. **Task Closure Gap**: The fact that 215 tasks remain open with completed statuses (Order Received, Order Shipped, etc.) suggests:
   - Form submissions do not automatically close tasks
   - Manual closure workflow missing
   - Invoicing/reconciliation step required before closure
   - May need integration with accounting/finance to mark "complete"

5. **Shop Supplies Evergreen Orders**: Many shop supply orders have Dec 29, 2026 due dates with "Order Placed in Inventory" status—these appear to be standing inventory replenishment orders (mcmaster, powerwerx, wirecare, amazon, mouser)

## Recommendations for Context

- **Workflow Issue**: Task closure process needs clarification. Consider adding a reconciliation/invoicing step before marking tasks complete.
- **Multi-Project Breakdown**: Audit open "MULTIPLE PROJECT" orders to ensure proper cost allocation.
- **Joshua Fromm Bottleneck**: Given the high volume of requests, consider whether task distribution or delegation is needed.
- **Asana vs. Form Sync**: Verify that form submissions (referenced in project notes) are syncing properly with Asana to auto-close orders once received.