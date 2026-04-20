# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders span Feb 2026 - Jun 2026
- **Status:** Active - critical operational load with **significant backlog reduction** (42 → 2 open tasks indicates major processing push)
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - 1 assigned task)
  - Nate Straus (secondary processor - 1 assigned task)
  - 0 unassigned tasks (major improvement from 39-task bottleneck)
- **Risk signals:** 
  - **Data reconciliation successful:** Knowledge file discrepancy resolved (42 tasks in prior snapshot now 2 open). Suggests massive batch closure/archival or system refresh occurred.
  - **Immediate deadlines:** 2 open tasks due Apr 18-19 with assigned owners (low risk if on track)
  - **Status clarity:** Both remaining tasks have clear status ("Order Placed", "Order Received") vs. prior "Order Placed in Inventory" stall

## Key Deliverables & Milestones
Purchasing workflow project (form-driven process). Current active orders:

### **Hurricane S0 [300-3]** — 1 open order
- **Due Apr 19, 2026:** Digikey hurricane/shop supplies (#98710410)
- **Assigned to:** Meredith O'hara Needham
- **Status:** Order Placed
- **Requester:** Nate
- **Tax exempt:** NO (note: prior knowledge file marked Hurricane S0 as 8/12 tax-exempt; this task marked NO — verify exemption status)
- **Vendor:** Digikey

### **Mustang Pt. 2 [043-3]** — 1 open order
- **Due Apr 18, 2026:** SoaringUSA ByLight M2 Additional Props (#17274)
- **Assigned to:** Nate Straus
- **Status:** Order Received
- **Requester:** Ethan Domagala
- **Tax exempt:** NO
- **Vendor:** SoaringUSA

## Task Summary
- **Total tasks:** 2 open, 0 completed (100% open rate)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 1 task (Digikey hurricane/shop - Apr 19)
  - Nate Straus: 1 task (SoaringUSA M2 props - Apr 18, "Order Received" status)
  - Unassigned: 0 tasks (**CRITICAL IMPROVEMENT** from 39-task bottleneck)
- **Notable patterns:**
  - **Dramatic backlog reduction:** Prior snapshot showed 42 open tasks; current snapshot shows 2 open. This indicates either:
    - Large batch closure event occurred (tasks moved to "completed" or archived)
    - System data refresh or filtering change
    - Purchasing operations significantly accelerated
  - **Order status:** Both remaining tasks in actionable states (1 "Order Placed" awaiting placement confirmation, 1 "Order Received" awaiting inventory intake)
  - **Immediate delivery window:** Both due within 1 week (Apr 18-19)
  - **No tax-exempt orders in current open set** (contrast with prior snapshot showing 16/42 tax-exempt)

## Recent Activity
- **Completed/closed:** ~40 tasks from prior snapshot (Hurricane S0, NASA S2, IRAD S3, IRAD S0 VTOL, IRAD General, Shop Supplies, IRAD Soil Moisture orders) have been processed or archived
- **Active focus:** Only 2 near-term orders remain; both in final execution phases (Meredith placing Digikey order; Nate confirming SoaringUSA receipt)
- **Jun 16 deadline pile:** The 38 unassigned "Order Placed in Inventory" tasks from prior snapshot have been **either completed, archived, or consolidated** — significant operational progress

## Notes & Context
1. **Data reconciliation:** The knowledge file's 42-task snapshot and current 2-task view suggest a major operational event occurred between snapshots. Recommend verifying:
   - Were Jun 16 inventory tasks batch-completed or auto-deleted per form policy?
   - Did a system refresh or archival occur?
   - Are closed tasks accessible in project history for audit trail?

2. **Tax exemption flag:** Digikey hurricane/shop task marked `Tax Exempt?: NO`, but prior knowledge file indicated Hurricane S0 as government IDIQ contract with 8/12 orders tax-exempt. **Verify if this single task requires exemption correction or if project exemption status changed.**

3. **Form compliance:** Project notes emphasize mandatory Asana form usage with auto-delete policy for non-compliant tasks. Both current tasks appear form-submitted (have full field data: requester, due date, project, tax status).

4. **Operational health:** 
   - ✅ Zero unassigned tasks (task ownership clear)
   - ✅ Both remaining orders in actionable final stages
   - ✅ Immediate deadlines allow rapid closure
   - ⚠️ Unknown fate of ~40 prior tasks (audit trail needed for compliance/archival verification)