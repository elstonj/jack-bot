_Asana snapshot as of 2026-10-24: 206 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** BST (Whole Team)
- **Status:** Active — high-volume purchasing coordination in progress
- **Dollar Value:** Not explicitly tracked in custom fields; appears to span multiple projects ranging from <$100 to likely $10k+ orders
- **Timeline:** Ongoing; peak activity in June–October 2026; some very old tasks from 2025
- **Risk Signals:** 
  - **206 open tasks, 0 completed** — task closure is not being used
  - Many tasks marked "Order Placed," "Order Shipped," or "Order Received" but remain open (stale status)
  - Oldest task dates to Feb 2025 (McMaster for S2 Oklahoma)
  - Tasks with dates well into past (Aug 2026, Sep 2026) still marked open
  - Heavy reliance on form submissions (Asana form URL in project notes) but Asana is not being used to close out purchases

## Key Deliverables & Milestones
N/A — this is a purchasing backlog, not a project with deliverables. Tasks represent individual purchase orders across multiple internal projects.

## Task Summary
- **Total Open Tasks:** 206
- **Total Completed:** 0
- **Assignee Distribution:**
  - Meredith O'hara Needham: ~95 tasks (most purchases assigned to her for processing)
  - Unassigned: ~111 tasks (waiting for action)
  
- **Requesters (most frequent):**
  - Joshua Fromm: ~80+ orders (shop supplies, S3 sales, S0 IDIQ parts)
  - Alex / Alex Lomis: ~20+ orders (S0 VTOL, Swiftstation, Magnetometer, general)
  - Sam: ~15+ orders (S3 parts, backup regulators, Magnetometer)
  - Ethan / Ethan Domagala: ~15+ orders (Mustang Pt. 2, gimbal, hardware)
  - Others: Dan, Nate, Spencer, Kareem, etc. (<10 each)

- **Order Status Breakdown (custom field):**
  - Order Placed: ~60 tasks
  - Order Received: ~40 tasks
  - Order Shipped: ~35 tasks
  - Order Placed in Inventory: ~65 tasks
  - (Blank or no status): ~6 tasks

- **Tax Exempt Status:** Mix of tax-exempt (YES for component/resale orders) and taxable (NO for shop supplies, general equipment)

## Recent Activity
**Last activities (Oct 2026 dates, most recent):**
- Multiple S3 sales orders due 10/23–10/24 (deans, hiawatha hobbies, voltroam, digikey, mcmaster, aliexpress, protocase, powerwerx, prowire usa)
- S0 IDIQ (Hurricane) parts due 10/8–10/24 (Microhard, S0 AD PSNS fix, extra dronecan boards)
- SOCOM Pope II orders due 10/15–10/24 (Amazon, foam mattress toppers, mcmaster)
- Shop supplies due 10/16–10/24

**Status Pattern:**
Many tasks dated Sep 2026, Aug 2026, Jul 2026 are marked "Order Placed," "Order Received," or "Order Shipped" but remain open in Asana. **These are not being closed out.** No tasks show as "completed" despite dozens marked with received/shipped status — suggests team is using Asana form for intake but not for closure.

## Notes & Context

1. **Process Issue:** Tasks are created via Asana form (URL in project notes), but closure workflow is missing. Tasks should be marked complete once orders arrive and are logged into inventory, but this is not happening.

2. **Billing & Project Coding:**
   - Most orders are tied to specific internal projects ([451-1] INSTAAR S3, [300-3] Hurricane IDIQ, [001-7] S3, [600-01] SOCOM Pope II, etc.)
   - Some orders marked "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN" — indicating incomplete project allocation at order time
   - Some marked "General Sales (No Specific Project)" or "Shop Supplies"

3. **Approval Flag:** One task marked "Requires Approval?: Yes" (ADS-B for S30002, $106,880 order #106880). Most others are "No."

4. **Vendor Diversity:** Heavy use of electronics suppliers (Digikey, McMaster, Mouser, Jawstec, Sparkfun, Pololu, etc.), manufacturing (Protolabs, SendCutSend, CraftCloud), and retail (Amazon, Home Depot).

5. **Volume & Frequency:** ~30–40 orders per month (based on date clustering in June–Oct 2026), primarily for S3 and S0 platform development, Hurricane IDIQ, Mustang Pt. 2, and shop inventory.

6. **Action Needed:** 
   - Implement task completion/archive workflow
   - Clean up stale "Order Received"/"Order Shipped" tasks (mark complete)
   - Add dollar amount custom field to enable budget tracking
   - Clarify project billing for "MULTIPLE PROJECT" orders before submission