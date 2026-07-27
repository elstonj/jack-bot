# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project. **9 open tasks all due Jul 26, 2026 (2 days).** 🟠 **CRITICAL DEADLINE CRUNCH:** All 9 tasks are Hurricane S0 procurement, placed Jul 24, due Jul 26. Heavy concentration with minimal fulfillment buffer.
- **Status:** 🟠 **OPERATIONAL — DEADLINE CRUNCH ACTIVE.** Task count **decreased from 14 to 9** — 5 tasks from prior snapshot removed (Protolabs, S3, Sparkfun, Amazon, Digikey GCS). **Status distribution:** All 9 open tasks are "Order Placed" (8/9 = 89%) or "Order Shipped" (1/9 springstore = 11%). **SIGNIFICANT TASK REDUCTION:** Swiftstation orders (Sparkfun, Amazon, Digikey GCS) and S3 power board all closed/resolved; Protolabs also removed. Only Hurricane S0 batch remains active.
- **Team members involved:**
  - **Meredith O'hara Needham** (9/9 open tasks = 100%) — All 9 Hurricane S0 orders
- **Requesters:** Joshua Fromm (8/9 = 89%); Joshua fromm (1/9 = 11%, springstore, lowercase typo variant)
- **Risk signals:**
  - 🔴 **IMMINENT DEADLINE CRUNCH (48 HOURS):** All 9 tasks due Jul 26, 2026 (2 days). All placed Jul 24; most have 1–2 day fulfillment windows.
  - 🟠 **FORM DATA TRUNCATION UNRESOLVED & WORSENING:** 5 of 9 tasks still have severely truncated project codes:
    - digikey: "[300-" (4 chars)
    - rocketman: "[30" (3 chars)
    - jawstec: "[300-3] 2" (partial, cut off after "2")
    - icare: "[300-3" (6 chars, incomplete)
    - springstore: "[300-3" (6 chars, incomplete)
    - **4 tasks show more complete codes** (Midwest, tattu, rfmall, amazon all show "[300-3] 202..." variants)
    - **CRITICAL RISK:** Truncated codes will cause incorrect billing/project assignment. High risk of financial audit failure.
  - 🟠 **HURRICANE BATCH CONCENTRATION:** All 9 remaining tasks (100%) are Hurricane S0 parts from Joshua Fromm, all placed same day (Jul 24), all due Jul 26. **Single-point-of-failure risk:** If any critical vendor (digikey, rocketman, jawstec, etc.) delays, entire Hurricane timeline at risk. Multiple vendors with 1–2 day delivery windows.
  - 🟠 **CLOSURE AUTOMATION BEHAVIOR UNCLEAR:** Prior snapshot showed Sparkfun, Amazon, Digikey GCS all "Order Received" (4 days overdue, Jul 21 placement) remaining open despite form rule stating auto-delete. Current snapshot shows those tasks **completely removed from list.** Either: (a) auto-delete rule fired retroactively, (b) tasks manually closed/deleted, or (c) project view filtered them out. **No closure documentation provided.** Risk: audit trail gap.
  - 🟠 **FORM SUBMISSION CONSISTENCY ISSUE:** All 9 tasks show identical placement date (Jul 24) and requester name format inconsistency (Joshua Fromm vs. Joshua fromm). Suggests bulk form submission or copy-paste workflow with minimal variation — increases risk of systematic errors.

## Key Deliverables & Milestones

### **OPEN TASKS — HURRICANE S0 IDIQ BATCH (all due Jul 26, 2026)**

| Task | Vendor | Assigned | Project (Form) | Requester | Status | Placement | Due | Tax Exempt? | Notes |
|------|--------|----------|----------------|-----------|--------|-----------|-----|------------|-------|
| **digikey for S0 hurricane** | Digikey | Meredith | [300- **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🟠 Project code severely truncated. High billing risk. |
| **rocketman for s0 hurricane** | Rocketman | Meredith | [30 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🟠 Project code severely truncated (only 3 chars). Critical issue. |
| **jawstec for s0 parts** | Jawstec | Meredith | [300-3] 2 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🟠 Project code cut off mid-string. |
| **Midwest control products for s0 idiq** | Midwest | Meredith | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | ✓ Complete project code. |
| **tattu for s0 idiq** | Tattu | Meredith | [300-3] 2026 | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | ✓ Complete project code. |
| **rfmall for s0 idiq** | RFMall | Meredith | [300-3] 202 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🟠 Project code truncated (missing year digits). |
| **icare order for s0 idiq** | iCare | Meredith | [300-3 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🟠 Project code incomplete. |
| **amazon for s0 idiq** | Amazon | Meredith | [300-3] 202 **(TRUNCATED)** | Joshua Fromm | Order Placed | Jul 24 | Jul 26 | YES | 🟠 Project code truncated. |
| **springstore for s0 idiq** | Springstore | Meredith | [300-3 **(TRUNCATED)** | Joshua fromm | Order Shipped | Jul 24 | Jul 26 | YES | 🟠 Only "Order Shipped" task; in transit. Project code incomplete. Requester name lowercase variant. |

---

## Task Summary
- **Total tasks:** 9 open, 0 completed
- **Task distribution by assignee:**
  - **Meredith O'hara Needham: 9/9 (100%)** — All Hurricane S0 orders
- **Status breakdown:**
  - Order Placed: 8/9 (89%)
  - Order Shipped: 1/9 (11%, springstore)
- **Notable patterns:**
  - 100% concentration on single project (Hurricane S0 IDIQ) and single assignee (Meredith)
  - 56% task failure rate on form data validation (5 of 9 tasks have truncated project codes)
  - Bulk submission behavior: all 9 tasks placed same day (Jul 24) with identical form structure
  - Requester name typo variant: "Joshua Fromm" (8 tasks) vs. "Joshua fromm" (1 task, springstore)

## Recent Activity
- **Task removal (Jul 24–25, 2026):** 5 tasks from prior snapshot (Protolabs, S3, Sparkfun, Amazon Swiftstation, Digikey GCS Swiftstation) no longer in active task list. All had Jul 25 due dates. **No closure documentation; unclear if auto-deleted per form rule, manually closed, or project filtered.** Sparkfun, Amazon