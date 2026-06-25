# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; orders due Jun 22–26, 2026
- **Status:** **ACTIVE — CRITICAL WORKLOAD SPIKE & DUPLICATE TASK UNRESOLVED.** Task count increased from **6 to 9 open tasks** (50% growth). ⚠️ **KEY CONCERNS:**
  - **DUPLICATE TASK PERSISTS:** "JawsTec- ByLight Gimbal (again)" (#69507) remains unresolved — appears to be exact duplicate of "JawsTec- ByLight Gimbal" (#69507).
  - **3 NEW TASKS ADDED:** Amazon shop supplies, Amazon Lava Lamp bulb, Digikey for IDIQ (distinct from prior GCS wifi order). Form-based submission system appears to be functioning and attracting new requests.
  - **Status progression visible:** 3 tasks now "Order Shipped" (GetFPV, Digikey GCS wifi, Digikey for IDIQ) vs. 1 in prior cycle — orders are executing.
  - **ALL 9 TASKS 100% ASSIGNED TO MEREDITH O'HARA NEEDHAM** — Single-point-of-failure risk **CRITICAL and unaddressed.** Workload has increased 50% with no delegation.
  - **NEW REQUESTERS ADDED:** Joshua Fromm (2 tasks) in addition to prior requesters (Ethan, Alex, Nate).
  - **Project field truncation continues** in raw data.

- **Team members involved:**
  - **Meredith O'hara Needham** (9/9 assigned; 100% of open workload; project owner)
  - **Requesters:** Ethan (3 tasks), Joshua Fromm (2 tasks), Alex (2 tasks), Nate (1 task)

- **Risk signals:**
  - 🔴 **UNRESOLVED DUPLICATE TASK:** "JawsTec- ByLight Gimbal (again)" (#69507) matches "JawsTec- ByLight Gimbal" (#69507) — identical vendor, amount due, requester (Ethan), project. Deduplication recommended in prior cycle but NOT EXECUTED.
  - 🔴 **CRITICAL SINGLE-POINT-OF-FAILURE:** Meredith at 100% capacity (9 tasks due Jun 22–26). No mitigation despite prior risk flagging.
  - 🟠 **IMMINENT DEADLINES:** 7 tasks due Jun 22–25; 2 due Jun 26. **TODAY IS LIKELY JUN 21 OR LATER** — minimal execution buffer remaining.
  - 🟡 **NEW REQUESTER ONBOARDING:** Joshua Fromm submitting via form (2 tasks). Indicates form mechanism is working but may attract increased volume without corresponding workload distribution.

## Key Deliverables & Milestones

### **DUE JUN 22–26, 2026 — 9 Tasks** *(8 unique + 1 duplicate)*

| Task | Due | Vendor | Assigned | Project | Requester | Status | Duplicate? |
|------|-----|--------|----------|---------|-----------|--------|-----------|
| GetFPV (#1001480217) | Jun 22, 2026 | GetFPV | Meredith O'hara Needham | Shop Supplies | Alex | **Order Shipped** | No |
| Digikey (GCS wifi) (#99989011) | Jun 23, 2026 | Digikey | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | **Order Shipped** | No |
| Jawstec (#69507) | Jun 23, 2026 | Jawstec | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | Order Placed | No |
| HiTec- ByLight (#5526) | Jun 23, 2026 | HiTec- ByLight | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | No |
| JawsTec- ByLight Gimbal (#69507) | Jun 23, 2026 | JawsTec- ByLight Gimbal | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | **YES (original)** |
| JawsTec- ByLight Gimbal (again) (#69507) | Jun 23, 2026 | JawsTec- ByLight Gimbal | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | **YES (DUPLICATE)** |
| Digikey for IDIQ (#009799) | Jun 24, 2026 | Digikey | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Joshua Fromm | **Order Shipped** | No |
| Amazon for shop supplies | Jun 24, 2026 | Amazon | Meredith O'hara Needham | Shop Supplies | Joshua Fromm | Order Placed | No |
| Amazon- Lava Lamp bulb | Jun 24, 2026 | Amazon | Meredith O'hara Needham | [001-1] IRAD General | Ethan | Order Placed | No |

## Task Summary

- **Total tasks:** 9 open, 0 completed
  - **8 unique orders** (GetFPV, Digikey GCS wifi, Jawstec, HiTec-ByLight, JawsTec-ByLight Gimbal, Digikey for IDIQ, Amazon shop supplies, Amazon Lava Lamp bulb)
  - **1 duplicate** (JawsTec-ByLight Gimbal submitted twice under identical task ID #69507)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 9/9 (100%)
- **Requester distribution:**
  - **Ethan:** 3/9 (HiTec-ByLight, JawsTec-ByLight Gimbal x2, Amazon Lava Lamp bulb)
  - **Joshua Fromm:** 2/9 (Amazon shop supplies, Digikey for IDIQ) — *NEW REQUESTER*
  - **Alex:** 2/9 (Jawstec, GetFPV)
  - **Nate:** 1/9 (Digikey GCS wifi)
- **Projects covered:**
  - [043-3] Mustang Pt. 2 (2 tasks; includes 1 duplicate)
  - [300-3] 2026 IDIQ (Hurricane) (2 tasks; distinct Digikey orders)
  - [550-1] Navy SBIR: Magnetometer (1 task)
  - [001-1] IRAD General (1 task)
  - Shop Supplies (2 tasks)
- **Status distribution:**
  - **Order Shipped:** 3 tasks (GetFPV, Digikey GCS wifi, Digikey for IDIQ)
  - **Order Placed:** 6 tasks (Jawstec, HiTec-ByLight, JawsTec-ByLight Gimbal x2, Amazon shop supplies, Amazon Lava Lamp bulb)

## Recent Activity

- **Form-based purchasing system actively in use:** 3 new orders submitted via form (Amazon shop supplies, Amazon Lava Lamp bulb, Digikey for IDIQ). Form mechanism is functional and attracting requests from new requesters (Joshua Fromm).
- **Order execution progressing:** 3 tasks now "Order Shipped" (GetFPV, Digikey GCS wifi, Di