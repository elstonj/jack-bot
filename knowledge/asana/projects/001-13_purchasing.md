_Asana snapshot as of 2026-11-17: 196 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active – high-volume purchasing operations
- **Dollar value:** Not explicitly tracked in custom fields; individual orders span from ~$10 to $10,000+
- **Timeline:** Ongoing operational purchasing; most near-term orders due Nov–Dec 2026
- **Risk signals:** 
  - **196 open tasks, 0 completed** – tasks accumulate and are not being closed out
  - **Stale orders:** Many orders marked "Order Received" or "Order Placed in Inventory" with due dates from July–October 2026, suggesting task closure is not enforced
  - **Multiple MULTIPLE PROJECT entries** – many orders lack proper project breakdowns, creating billing ambiguity
  - **Unassigned tasks:** Most tasks are unassigned; only recent orders assigned to Meredith O'hara Needham

## Key Deliverables & Milestones
Not applicable – this is a purchasing operations project, not a deliverable-driven project. Orders are generated ad-hoc by requesters across the organization.

## Task Summary
- **Total tasks:** 196 open, 0 completed (all tasks remain open indefinitely)
- **Assignees:**
  - Meredith O'hara Needham: ~15 recent tasks (Nov 2026)
  - Unassigned: ~180 older/stale tasks
- **Order statuses (custom field):**
  - Order Placed: ~20 tasks
  - Order Shipped: ~6 tasks
  - Order Received: ~40 tasks
  - Order Placed in Inventory: ~100 tasks (oldest/stalest)
- **Notable patterns:**
  - Heavy use of vendors: McMaster Carr, Jawstec, Digikey, Amazon, Mouser, Protolabs, Sendcutsend
  - S3 and S0 platform components dominate (motors, composites, RF parts, servos)
  - Shop Supplies and Future Sales orders are recurring
  - Many orders lack project assignment ("MULTIPLE PROJECT – PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION")
  - **Tax Exempt status:** YES on ~60 orders (mostly sales/IRAD), NO on ~100 orders

## Recent Activity
- **Latest orders (Nov 2026, assigned to Meredith):**
  - mcmaster for various projects (Nov 16, 2026)
  - S3 motor noise fix attempt (Nov 16, 2026)
  - Dronetag DRI RID Module for [001-8] IRAD Flight Testing (Nov 13, 2026)
  - Multiple composite, protolabs, and parts orders due Nov 11–15
- **Completion rate:** 0% – no tasks are being closed, even those marked "Order Received" or "Order Shipped"
- **Vendor activity:** Steady stream of orders to composites suppliers, electronics (Digikey/Mouser), 3D printing (Protolabs/Sendcutsend), and mechanical parts

## Notes & Context
- **System friction:** The project notes emphasize "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE" – suggesting the task list is meant to feed an external form and auto-cleanup isn't working
- **Task lifecycle broken:** Tasks are created when orders are requested, status updates as "Order Placed → Shipped → Received → Placed in Inventory," but tasks are never marked complete/closed. This creates a growing backlog of zombie tasks
- **Billing ambiguity:** ~20 orders span "MULTIPLE PROJECT" with incomplete project breakdowns, making cost allocation unclear
- **Approval tracking:** "Requires Approval?" field is set, but there's no task dependency or workflow to enforce approvals for high-value orders
- **Requesters:** Joshua Fromm (majority of S3 sales/IRAD orders), Sam (S0/S3 fixes), Alex (Swiftstation/Magnetometer), Dan (SOCOM/FLIR), Ali Sulehria, Spencer, Ethan, others
- **Future Sales prevalence:** Many S3 component orders routed to "Future Sales" project, suggesting ongoing product development or build-to-stock

**Recommendation:** Implement task closure discipline. Consider archiving or bulk-closing "Order Placed in Inventory" tasks older than 60 days, or redesign the workflow to avoid task accumulation (e.g., auto-archive on status change, or use a separate purchase ledger instead of Asana tasks).