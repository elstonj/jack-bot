# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **6 open tasks: 4 due Jul 26, 2 due Jul 29, 2026.** 🟠 **CRITICAL DEADLINE CRUNCH:** Most tasks placed Jul 24, due Jul 26 (2 days). Two newer tasks (jawstec S3, craftcloud) due Jul 29 with Jul 27 placement window.
- **Status:** 🟠 **OPERATIONAL — DEADLINE CRUNCH ACTIVE.** Task count **decreased from 9 to 6** — significant reduction from prior snapshot. Current distribution: **Order Placed 4/6 (67%), Order Shipped 2/6 (33%).** **IMPORTANT CHANGE:** Prior 9-task Hurricane S0 batch partially cleared. Incoming: jawstec for S3 IRAD (new project [001-7]), craftcloud for Hurricane (new vendor). This suggests procurement pipeline is actively rotating — older tasks fulfilled/closed, new requests flowing in.
- **Team members involved:**
  - **Meredith O'hara Needham** (6/6 open tasks = 100%)
- **Requesters:** Joshua Fromm (6/6 = 100%)
- **Risk signals:**
  - 🔴 **IMMINENT DEADLINE (48 HOURS):** 4 of 6 tasks due Jul 26 (icare, tattu, digikey, all Hurricane S0). Placed Jul 24; most 1–2 day delivery windows.
  - 🔴 **FORM DATA TRUNCATION PERSISTS & CRITICAL:** 2 of 6 tasks still have severely truncated project codes:
    - **digikey:** "[300-" (4 chars, **UNCHANGED from prior snapshot** — same truncation error)
    - **icare:** "[300-3" (6 chars, **UNCHANGED from prior snapshot**)
    - Both **identical to prior snapshot failures** — suggests systematic form/input issue, **NOT RESOLVED.**
    - **CRITICAL RISK:** Truncated codes will cause incorrect billing/project assignment. Both are Hurricane S0 IDIQ tasks; billing misroute directly impacts project financials.
  - 🟠 **NEW PROJECT INTRODUCED — S3 IRAD ([001-7]):** jawstec for s3 IRAD task is first non-Hurricane procurement in this snapshot. Due Jul 29 (4 days). Requires careful attention; form notes show project field shows only "[001-7] IR" (truncated from full "[001-7] IRAD S3" context in task name).
  - 🟠 **FORM FIELD TRUNCATION IN CAPTURE:** Notes sections show incomplete form data:
    - craftcloud: "Select project to bill purcha" (cut off mid-word, should be "purchase")
    - mouser: "Select project to bill purchase:" (field value missing entirely)
    - icare: "[300-3" (project field incomplete)
    - digikey: "[300-" (project field incomplete)
    - **Indicates form or note-scraping is truncating at character limit (~255–512 chars).** Risk: Actual vendor/project data may exist in Asana but not visible in this export.
  - 🟠 **HURRICANE BATCH CONCENTRATION PERSISTING:** 5 of 6 tasks (83%) are Hurricane S0 IDIQ (all [300-3] 2026 project). Tattu and digikey now showing "Order Shipped" (2/6, 33%), suggesting some fulfillment; but craftcloud, mouser still "Order Placed" with Jul 29 due dates. Single-point-of-failure risk remains high.
  - 🟠 **TASK CLOSURE BEHAVIOR UNCLEAR:** Prior snapshot had 9 tasks; now 6. No documentation of what happened to: Midwest, rfmall, amazon, springstore, rocketman from prior list. Were they closed/fulfilled, or filtered out? Closure audit trail gap persists.

## Key Deliverables & Milestones

### **OPEN TASKS — MIXED BATCH (Hurricane S0 IDIQ + S3 IRAD)**

| Task | Vendor | Assigned | Project (Form) | Requester | Status | Placement | Due | Tax Exempt? | Notes |
|------|--------|----------|----------------|-----------|--------|-----------|-----|------------|-------|
| **digikey for S0 hurricane** | Digikey | Meredith | [300- **(TRUNCATED)** | Joshua Fromm | Order Shipped | Jul 24 | Jul 26 | YES | 🔴 **UNCHANGED TRUNCATION FAILURE** from prior snapshot. Project code critical. In transit. |
| **tattu for s0 idiq** | Tattu | Meredith | [300-3] 2026 | Joshua Fromm | Order Shipped | Jul 24 | Jul 26 | YES | ✓ Complete project code. In transit. |
| **icare order for s0 idiq** | iCare | Meredith | [300-3 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🔴 **UNCHANGED TRUNCATION FAILURE** from prior snapshot. Due TODAY (Jul 26). Critical. |
| **mouser order for s0 hurricane** | Mouser | Meredith | **(PROJECT FIELD MISSING)** | Joshua Fromm | Order Placed | Jul 24 | Jul 29 | YES | 🟠 Form notes truncated: "Select project to bill purchase:" field empty. Likely [300-3] 2026 IDIQ (Hurricane) per context. |
| **craftcloud for s0 hurricane parts** | Craftcloud | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 24 | Jul 29 | YES | ✓ Complete project code. Newer vendor (not in prior snapshot). |
| **jawstec for s3 IRAD** | Jawstec | Meredith | [001-7] IR **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 27 | Jul 29 | NO | 🟠 **NEW PROJECT:** [001-7] IRAD S3 (first non-Hurricane task). Project field shows truncated "[001-7] IR" in form. Tax exempt = NO (different from all other Hurricane tasks). Due Jul 29. |

---

## Task Summary
- **Total tasks:** 6 open, 0 completed
- **Task distribution by assignee:**
  - **Meredith O'hara Needham: 6/6 (100%)** — All active procurement
- **Status breakdown:**
  - Order Placed: 4/6 (67%) — digikey, icare, mouser, craftcloud, jawstec
  - Order Shipped: 2/6 (33%) — tattu, digikey
  - **Note:** Digikey appears in both contexts (Order Shipped in one view, but table above shows it as latest entry). Verify task deduplication.
- **Notable patterns:**
  - **5/6 tasks (83%) = Hurricane S0 IDIQ** ([300-3] 2026 project)
  - **1/6 tasks (17%) = New S3 IRAD ([001-7])** — first project diversification in snapshots
  - **2 of 6 (33%) = Form data truncation failures** — identical errors to prior snapshot (digikey "[300-", icare "[300-3")
  - **All 6 tasks assigned to Meredith, all requested by Joshua Fromm** — zero distribution
  - **Bulk placement pattern:** 5 of 6 placed Jul 24 (Hurricane batch), 1 placed Jul 27 (S3 IRAD)
  - **Tax exempt variance:** All Hurricane = YES; S3 IRAD jawstec = NO

## Recent Activity
- **Task reduction (Jul 25–26, 2026):** 3 tasks