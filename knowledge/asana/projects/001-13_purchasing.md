_Asana snapshot as of 2026-11-04: 225 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active — operational purchasing workflow
- **Key Process Change (2026-10-13):** Per Meredith Needham, Beck now holds the company credit card for purchases while Meredith is away. All purchase requests must still be submitted in Asana for tracking, but requesters should go to Beck to place orders or obtain the card.
- **Dollar Value:** Not aggregated in custom fields; individual line items span components, supplies, and equipment across multiple projects
- **Timeline:** Ongoing operational process; no fixed end date

## Task Summary
- **Total tasks:** 225 open, 0 completed
- **Assignee distribution:**
  - **Meredith O'hara Needham:** ~20 tasks (older/recent assignments; processing/approval role)
  - **Unassigned:** ~190 tasks (majority of backlog; awaiting processing or approval)
  - Scattered requesters: Joshua Fromm (most frequent), Sam, Alex, Dan, Spencer, Ethan, Nate, and others
  
- **Completion rate:** 0% (no closed tasks in this tracking project)
- **Status field patterns:**
  - Order Placed: ~30 tasks
  - Order Received: ~40 tasks
  - Order Shipped: ~10 tasks
  - Order Placed in Inventory: ~90 tasks
  - No status/pending: ~30 tasks

## Deliverables & Process
This is **not a project with discrete deliverables**, but rather a **purchasing intake and tracking system**. The workflow is:
1. Team member submits purchase request via Asana form (or task creation)
2. Request assigned to Meredith for review/approval
3. Request forwarded to Beck (or Meredith, when she was handling it) for execution
4. Task status updated as order progresses (Placed → Shipped → Received → Inventory)
5. Task remains open for accounting/historical tracking

## Recent Activity & Risk Signals

### High-Volume Requesters
- **Joshua Fromm:** ~130+ purchase requests across all projects (Shop Supplies, IRAD S0/S3, Hurricane IDIQ, INSTAAR S3, NASA S2, etc.)
- **Sam:** ~15 requests (mostly S3 fixes, Hurricane parts, Navy SBIR)
- **Alex:** ~20 requests (S0 VTOL, Swiftstation, Navy SBIR, SOCOM Pope)
- **Others:** Ethan (ByLight/Mustang), Dan Prendergast (SOCOM, Swiftstation), Spencer (S0 IRAD, S3, SMM)

### Notable Patterns
- **Multi-project orders:** Many orders marked "MULTIPLE PROJECT" with incomplete project breakdown (e.g., digikey, mcmaster, jawstec, protocase orders) — creates ambiguity in project cost allocation
- **Aged inventory:** Many tasks with "Order Placed in Inventory" status show original order dates from May–June 2026, suggesting backlog of items not yet allocated to specific projects or builds
- **Tax-exempt mix:** ~50% of orders are tax-exempt (tagged for government/nonprofit projects like IDIQ, INSTAAR, Navy SBIR)
- **Vendor patterns:** jawstec, digikey, mcmaster, amazon, mouser, and protolabs are the most frequently used; also specialized vendors (servocity, Bartington, SendCutSend, etc.)

### Upcoming/Overdue Dates
- **Due dates clustering at 2026-11-03 to 2026-11-07:** ~30 tasks (Joshua Fromm's recent batch for multiple projects with incomplete billable project info)
- **Due dates clustering at 2026-12-29:** ~100 tasks (default/placeholder due date; most in "Order Placed in Inventory" status)
- **Dated orders (Sep–Oct 2026):** ~20 tasks with "Order Received" or "Order Shipped" but still open in Asana (awaiting reconciliation/closure)

### Risk/Workflow Issues
1. **Unassigned backlog:** ~190 tasks unassigned — bottleneck for processing
2. **Incomplete project billables:** ~15–20 multi-project orders lack detailed breakdown, risking cost allocation errors
3. **Stale task state:** Many "Order Received" or "Order Shipped" tasks remain open; no clear closure/reconciliation step
4. **Approval bottleneck:** Only one approval authority (Meredith); now delegated to Beck for execution, but Asana still expects Meredith action
5. **Form compliance:** Project notes emphasize "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE" — but form link and enforcement unclear

## Notes & Context

### Team Guidance (Authoritative Override)
**[FEEDBACK] Meredith Needham, 2026-10-13 & 2026-10-12:**
- Beck has the credit card while Meredith is away
- Requesters should contact **Beck** to place orders or request the card
- **All purchases must still have a purchase request task in Asana** for tracking (prevents Meredith from having to chase down requesters for details)
- This workflow change is now active; respect Beck as the operational purchasing agent

### Process Observations
- Heavy reliance on form-based intake; most tasks include structured custom fields (Requires Approval?, Tax Exempt?, Name of requester, Project, Order placement date)
- Order tracking via Status field is the primary progress indicator
- No visible SLAs or escalation protocols for aged inventory or stalled approvals
- "Order Placed in Inventory" status suggests items are staged for future project builds, but without clear linkage to upcoming builds or budgets

### High-Volume Projects Visible in Purchasing
- **[300-3] 2026 IDIQ (Hurricane):** ~25 active purchase requests
- **[001-7] IRAD S3:** ~20 active purchase requests
- **[451-1] INSTAAR S3 x2:** ~15 active purchase requests
- **Shop Supplies:** ~30 active purchase requests (organization-wide)
- **General Sales:** ~15 active purchase requests
- **[001-4] IRAD S0 VTOL:** ~10 active purchase requests
- **[550-1] Navy SBIR: Magnetometer:** ~8 active purchase requests
- **[600-01] SOCOM Pope ii:** ~8 active purchase requests

---

## Recommended Actions
1. **Process the unassigned backlog:** Assign tasks to Beck for execution (per new policy) or back to Meredith for review
2. **Resolve multi-project orders:** Contact Joshua Fromm to provide detailed project breakdowns for ambiguous orders (e.g., digikey, mcmaster, jawstec multi-project tasks)
3. **Reconcile aged "Order Received" tasks:** Determine if items are in stock and ready for use, or if reconciliation is pending
4. **Clarify closure protocol:** Establish when tasks should be marked complete (on invoice receipt? on project use? on accounting entry?)