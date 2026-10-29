_Asana snapshot as of 2026-10-29: 209 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active — high-volume purchasing workflow
- **Dollar Value:** Not quantified in metadata; appears to span multiple projects ranging from small shop supplies to significant equipment orders
- **Timeline:** Orders span June 2025 through December 2026, with heaviest concentration in summer/fall 2026

**Risk Signals:**
- 209 open tasks, 0 completed — indicates task closure is not being tracked, potentially masking actual progress
- Multiple tasks with past or near-term dates (e.g., "McMaster" due 2025-02-24 is already overdue)
- Heavy reliance on custom form submission (note emphasizes "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE")
- Many tasks assigned to "Unassigned" despite being tracked as open

## Key Patterns & Observations

**Primary Requesters:**
- Joshua Fromm (highest volume — S3 sales, shop supplies, multi-project orders)
- Sam (IRAD S3 and related components)
- Alex / Alex Lomis (SOCOM Pope ii, S0 VTOL, Magnetometer)
- Ethan / Ethan Domagala (ByLight/Mustang Pt. 2 components)
- Dan Prendergast, Spencer, others (lower volume)

**Main Projects:**
- [451-1] INSTAAR S3 x2 (S3 sales)
- [001-7] IRAD S3 (numerous component orders)
- [300-3] 2026 IDIQ (Hurricane) (S0 Hurricane system)
- [600-01] SOCOM Pope ii (foam, Amazon, Aegis/Videology orders)
- [001-4] IRAD S0 VTOL (motors, servos, prototyping)
- [550-1] Navy SBIR: Magnetometer (sensors, connectors)
- [043-3] Mustang Pt. 2 (ByLight gimbal, laser, fasteners)
- Shop Supplies (standing orders across multiple vendors)
- General Sales (no project-specific designation)

**Vendor Patterns:**
- **Recurring:** McMaster Carr, Amazon, Digikey, Mouser, JawsTec, ProtoLabs, SendCutSend
- **Specialty:** Aegis/Videology, Bartington (sensors), Dronetag (remote ID), TMotor, MKS (servos), Vertiq

**Order Status Breakdown:**
- **Order Placed:** ~120 tasks (earliest: June 2026, latest: October 2026)
- **Order Shipped:** ~30 tasks
- **Order Received:** ~30 tasks
- **Order Placed in Inventory:** ~25 tasks (appears to be a holding status for future/non-urgent items)

**Tax Exempt Patterns:**
- YES: Mostly S3 sales, S0 Hurricane, IRAD projects (likely government-funded)
- NO: Shop supplies, general retail, some component orders

## Task Summary

| Status | Count |
|--------|-------|
| Open (all statuses) | 209 |
| Completed | 0 |

**Assignee Distribution:**
- Meredith O'hara Needham: ~110 tasks (primary processor)
- Unassigned: ~99 tasks (awaiting action or closure)

**Completion Rate:** 0% — **Critical:** All 209 tasks remain open despite many showing "Order Placed," "Order Shipped," or "Order Received" status. This suggests tasks are not being closed post-fulfillment.

## Recent Activity

**Approaching Deadlines (Next 2 weeks from latest task dates in October 2026):**
- jawstec for s3 parts | Due 2026-10-28
- Amazon Shop Supplies Tapes | Due 2026-10-30
- mcmaster (IRAD S3) | Due 2026-10-29
- mks servos for s3 sales | Due 2026-10-29
- Multiple shop supply orders | Due 2026-10-23–24

**Recently Completed (per Order Status field):**
- S3 Remote Id Modules | Shipped, Due Oct 10
- S3 Backup Regulators | Shipped (two instances), Due Sept 24, Sept 16
- McMaster Hardware order | Received, Due Sept 6
- GetFPV | Received, Due Sept 4

**Stale/Long-Pending:**
- McMaster | Due 2025-02-24 (project [039-1] S2 Oklahoma) — **1 year overdue**
- Multiple "Order Placed in Inventory" items dated June–July 2026 with due date 2026-11-07 (appears to be a placeholder due date)

## Notes & Context

**Form Requirement:**
Project notes direct all tasks to use a specific Asana form (https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594), with warning that non-compliant tasks auto-delete. This is the intake mechanism for the purchasing workflow.

**Data Quality Issues:**
1. **Task Closure:** 0 completed tasks suggests Asana is used for tracking order placement and status, but closed orders are not being marked complete. Manual review of "Order Received" or "Order Shipped" items needed to understand true closure rate.
2. **Unassigned Tasks:** ~99 unassigned tasks are marked open; unclear if these are pending intake, awaiting assignment, or stalled.
3. **Due Date Inconsistency:** Many "Order Placed in Inventory" tasks have a due date of 2026-11-07 (appears to be a system default), making them impossible to prioritize.
4. **Multi-Project Billing:** Several orders tagged "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" lack clear cost allocation in the visible fields.

**Custom Fields in Use:**
- Requires Approval? (Yes/No)
- Tax Exempt? (Yes/No)
- Name of requester
- Order status (Order Placed, Order Shipped, Order Received, Order Placed in Inventory)
- Project assignment
- Vendor/order description

**Process Observations:**
- Heavy reliance on Joshua Fromm for S3 and shop supply aggregation
- Meredith O'hara Needham appears to be the single point of processing/assignment
- Tax exemption is properly tracked by project type (government/internal vs. commercial)
- Orders span highly specialized vendors (JawsTec, StepGlobal, Bartington) and general retail (Amazon, McMaster)

---

**Recommendation:** Establish a task closure protocol (mark tasks complete upon receipt, not just order placement) and review the 99 unassigned tasks for processing backlog or stale entries.