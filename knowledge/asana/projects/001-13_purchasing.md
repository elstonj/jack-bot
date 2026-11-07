_Asana snapshot as of 2026-11-07: 229 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Team:** BST (Whole Team)
- **Owner:** Meredith O'hara Needham
- **Status:** Active — high-volume operational purchasing process
- **Task Volume:** 229 open tasks, 0 completed
- **Risk Signal:** Massive backlog of 229 open purchasing requests with many orders already placed/shipped/received but not closed in Asana. This suggests a process failure: orders are being executed in the real world but task closure is not happening systematically.

**Critical Note:** The project notes direct users to submit purchasing requests via a form. The form URL is: `https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594`

## Key Observations

### Order Status Distribution (Sample from visible tasks)
- **Order Placed:** ~20 tasks (earliest due dates in Oct–Nov 2026)
- **Order Shipped:** ~4 tasks
- **Order Received:** ~40 tasks
- **Order Placed in Inventory:** ~165 tasks (majority of backlog; due dates range May 2026–Jan 2027)

### Projects Being Supported (Partial List)
- **[001-3] IRAD S0** – S0 IRAD components
- **[001-4] IRAD S0 VTOL** – VTOL-specific parts
- **[001-7] IRAD S3** – S3 sensor platform
- **[001-16] IRAD Swiftstation** – Ground control station
- **[001-18] IRAD Soil Moisture** – Environmental sensor
- **[001-23] SOCOM S0-AD** – Special operations variant
- **[043-3] Mustang Pt. 2** – ByLight platform subproject
- **[212-2] NASA S2 & Parts** – NASA partnership
- **[300-3] 2026 IDIQ (Hurricane)** – IDIQ contract vehicle
- **[451-1] INSTAAR S3 x2** – Academic partnership (2 units)
- **[550-1] Navy SBIR: Magnetometer** – Navy magnetometer development
- **[600-01] SOCOM Pope ii** – SOCOM variant
- **Shop Supplies** – General shop consumables & equipment
- **General Sales (No Specific Project)** – Commercial inventory

### Key Requesters
- **Joshua Fromm** – Dominant requester (majority of tasks)
- **Alex** / **Alex Lomis** – Hardware integration
- **Ethan** / **Ethan Domagala** – ByLight/Mustang subproject
- **Spencer** – Testing/ops
- **Dan / Dan Prendergast** – SOCOM/integration
- **Sam** – S3 repairs/fixes
- **Nate / Nathaniel Straus** – IRAD General

### Common Vendors
- **Amazon, McMaster, Digikey, Mouser** – Electronics & hardware (high frequency)
- **JawsTec, SendCutSend, Protolabs** – Fabrication/machining
- **Horizon Hobby, GetFPV** – Drone/aerial components
- **Servocity, MKS, Pololu** – Motion control
- **Clearwater Composites, RFMall** – Specialized materials

## Task Summary

### Assignee Breakdown
- **Meredith O'hara Needham:** ~20 tasks assigned (most recent purchases in Nov 2026)
- **Unassigned:** ~209 tasks (vast majority in "Order Placed in Inventory" status, suggesting completed but not closed)

### Completion Rate
- **0% formal closure rate** – All 229 tasks remain open despite order statuses indicating completion

### Notable Pattern
This is not a backlog of *pending* work; it is a **closed-loop tracking failure**. Orders are being placed, shipped, and received, but tasks are not being marked complete in Asana. This creates two problems:
1. **Data staleness** – Task due dates become meaningless (many tasks have due dates in May–July 2026 but remain open in Nov 2026)
2. **Process visibility loss** – Leadership cannot see which orders are actually outstanding vs. completed

## Recent Activity

### Immediate Deadlines (Nov 2026)
- **Nov 8:** Amazon shop supplies (Joshua Fromm) — Order Placed
- **Nov 7:** Multiple tasks due today:
  - Microhard P900/P400 for [300-3] IDIQ (Jack Elston) — Order Placed
  - Eugene Hobbies shop supplies (Joshua Fromm) — Order Placed
  - JawsTec multiple projects (Joshua Fromm) — Order Placed
  - McMaster (Alex) — Order Shipped
  - And ~25 more with "Order Placed in Inventory" status

### Mid-November Activity
- Tasks moving from "Order Placed" → "Order Shipped" → "Order Received" status
- Heavy activity on [451-1] INSTAAR S3 x2 (sales builds)
- [300-3] Hurricane IDIQ receiving ongoing support (S0 AD fixes, connectors, parts)

## Notes & Context

### Process Issue
The form-based submission system (`https://form.asana.com/?k=AYO2EiBus4sRY0G_cbPmHw&d=12804948716594`) is creating tasks, but **there is no visible task closure workflow**. Orders marked "Order Received" should be closed but remain open indefinitely, creating data decay.

### Data Quality Issues
1. **Truncated Notes:** Many order descriptions are incomplete (e.g., "jawstec for multiple projects — MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION")
2. **Orphaned Multi-Project Orders:** Several orders cannot be billed correctly because project breakdown was not provided in the description
3. **Tax Exempt Status:** Tracks 60 tax-exempt vs. 169 taxable orders (important for accounting but not enforced in form)

### Operational Insights
- **High vendor diversity:** ~50+ vendors suggests decentralized procurement by engineers (not centralized vendor contracts)
- **Rapid replenishment cycle:** Majority of orders are <$500 consumables and parts (inferred from order names)
- **Sales support tier:** Significant procurement for [451-1] INSTAAR S3 x2 suggests active customer delivery
- **Contractor support:** IDIQ vehicle ([300-3]) is a major throughput driver

### Recommendations for Future Workflow
1. **Implement task closure automation:** Orders with "Order Received" status >7 days should trigger a review or auto-close
2. **Enforce multi-project breakdown:** Block form submission if "MULTIPLE PROJECT" is selected without a detail section
3. **Consolidate approval:** Only 1 task requires approval ("ADS-B for S30002"); approval gate may be ineffective
4. **Archive old inventory:** Tasks with "Order Placed in Inventory" due >30 days in the past should move to archive

---

**Data Extraction Date:** Raw data shows orders from May 2026 through November 2026. File integrity: All 229 tasks extracted; excessive truncation at end of task list indicates data was very large but complete within token budget.