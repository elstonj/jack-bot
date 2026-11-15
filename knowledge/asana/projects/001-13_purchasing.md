_Asana snapshot as of 2026-11-15: 194 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Purpose**: Centralized purchasing task management for Black Swift Technologies
- **Owner**: Meredith O'hara Needham
- **Team**: Whole BST team
- **Status**: **Active but systemically problematic** — see below
- **Timeline**: Ongoing (all tasks remain open; no completion tracking)
- **Risk Signals**: 
  - **194 open tasks, 0 completed** — indicates tasks are not being closed out after orders are fulfilled
  - Joshua Fromm reported (2026-11-13) he may have been removed from purchasing email forward and is not receiving notifications
  - Many tasks with "Order Placed," "Order Shipped," "Order Received" statuses remain marked OPEN in Asana — this is stale data
  - Tasks with due dates spanning May 2026 through January 2027, many long past their "should place order" dates
  - No clear workflow for transitioning completed/received orders to a closed state

## Key Issue: Data Integrity
This project appears to use Asana primarily as an intake mechanism (via form submission). Orders proceed through real fulfillment (placed → shipped → received) but **tasks remain perpetually open**. The "Status" custom field (Order Placed, Order Received, etc.) reflects real-world state, but task completion does not. 

**Team feedback (2026-11-13) from Joshua Fromm indicates communication breakdown:** he is not receiving purchasing emails, suggesting he may be unable to track or act on his own requisitions.

## Task Summary
- **Total**: 194 open, 0 completed
- **Assignee Distribution**:
  - Meredith O'hara Needham: ~12 tasks (most recent/current intake)
  - Unassigned: ~180 tasks (backlog in various fulfillment states)
  - Jack Elston: 1 task (Dronetag DRI RID Module, due 2026-11-13)
- **Status Distribution** (from custom field):
  - Order Placed: ~35 tasks
  - Order Shipped: ~10 tasks
  - Order Received: ~40 tasks
  - Order Placed in Inventory: ~95 tasks (older orders, long-term storage)
  - Unspecified: ~5 tasks

## Recent Activity
- **Most Recent Assigned Tasks** (to Meredith O'hara Needham):
  - Dronetag DRI RID Module (Jack Elston, due 2026-11-13, requires approval, $, for [001-8] IRAD Flight Testing)
  - Composite envisions for S3 backorder (due 2026-11-11, Joshua Fromm request)
  - Protolabs for S3 sales (due 2026-11-15, order already placed)
  - QC kit materials (due 2026-11-15, order already placed)
  - Multiple S3 sales vendor orders (Digikey, instrumart, ACP composites, Jawstec, Hillside) due 2026-11-13–2026-11-15, all with "Order Placed" status
  - McMaster multi-project order (due 2026-11-13, order placed)
  - FLIR Hadron 640R Camera for SOCOM S0-AD (due 2026-11-12, order placed)

- **Oldest Active Tasks** (never closed):
  - McMaster order for [039-1] S2 Oklahoma (due 2025-02-24) — **overdue by ~9 months**
  - Multiple orders dated July–September 2026 with "Order Received" or "Order Placed in Inventory" status, still open

## Notes & Context
1. **Form-Based Intake**: Project notes instruct users to submit via a form (https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594) or tasks will auto-delete. This suggests high volume and automated creation.

2. **Tax & Approval Tracking**: Most tasks include "Requires Approval?" and "Tax Exempt?" fields, indicating compliance/budget controls. One task (ADS-B for S30002) explicitly requires approval; most others do not.

3. **Project Billing**: Orders are tagged to destination projects (IRAD series, SOCOM, NASA, Hurricane IDIQ, INSTAAR S3, Magnetometer, etc.). Many orders for "Future Sales" and "General Sales" categories; some tagged "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" (incomplete cost allocation).

4. **Communication Gap** (Per Joshua Fromm, 2026-11-13): Joshua is not receiving purchasing emails and suspects he was removed from a forwarding list. As a frequent requester, this represents a critical process failure for a key stakeholder.

5. **No Completion Workflow**: Despite custom "Status" field accurately tracking real-world fulfillment, Asana tasks are never marked complete. This makes the task list unintelligible for current vs. historical order status and prevents clean archival.

6. **Vendor Concentration**: Jawstec, McMaster, Digikey, and Amazon account for majority of orders. Many composite/aviation vendors (protolabs, sendcutsend, ACP Composites, Hillside Composites) indicate S3 and structural manufacturing orders.

## Recommendations for AI Assistant
- When answering "What's the status of order X?", **defer to the custom "Status" field** and the task's "When should this order be placed?" date, not the Asana due date.
- Treat unassigned + "Order Received"/"Order Placed in Inventory" tasks as **historical/closed-out**, pending reconciliation.
- Flag any task due >30 days in past as **potentially overdue or forgotten**.
- Escalate to Meredith O'hara Needham if tasks require approval or reassignment.
- **Action item**: Restore Joshua Fromm to purchasing email forward and implement task closure workflow (e.g., mark complete when received/invoiced).