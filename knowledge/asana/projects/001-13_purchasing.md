# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; orders due Jun 22–25, 2026
- **Status:** **ACTIVE — CRITICAL RECOVERY WITH NEW CONCERNS.** Task count increased to **6 open tasks** (up from 5 in prior cycle). ⚠️ **KEY CHANGES:**
  - All 5 prior tasks now marked **"Order Placed"** status (form-based auto-status mechanism appears functional).
  - **NEW DUPLICATE TASK DETECTED:** "JawsTec- ByLight Gimbal (again)" (#69507) is a duplicate of "JawsTec- ByLight Gimbal" (#69507) — both assigned to Ethan, same project, same due date. Indicates form submission error or manual re-submission.
  - **GetFPV task now "Order Shipped"** (status advanced beyond prior "Order Placed" state).
  - **All orders remain assigned 100% to Meredith O'hara Needham** — single-point-of-failure risk unresolved.
  - **Project field truncation persists** in raw data (e.g., "[300-3] 2026 IDIQ (", "[043-3] Musta", "[550-1] Navy SBIR: Magnetomete").

- **Team members involved:**
  - **Meredith O'hara Needham** (6/6 assigned; 100% of open workload; project owner)
  - **Requesters:** Alex (2 tasks), Ethan (3 tasks), Nate (1 task)

- **Risk signals:**
  - 🔴 **DUPLICATE TASK:** "JawsTec- ByLight Gimbal (again)" is identical to existing task #69507. Requires immediate deduplication.
  - 🔴 **PERSISTENT SINGLE-POINT-OF-FAILURE: MEREDITH 100%** — All 6 orders assigned exclusively to Meredith. No delegation to team despite prior recommendations.
  - 🟡 **IMMINENT DEADLINES (JUN 22–25, 2026)** — All orders due within 1–4 days. Minimal buffer.
  - 🟡 **FORM-BASED STATUS UPDATES WORKING** — Tasks now show "Order Placed" and "Order Shipped" statuses, suggesting form mechanism is functional. However, no auto-closure yet (tasks remain open despite status changes).

## Key Deliverables & Milestones

### **DUE JUN 22–25, 2026 — 6 Tasks** *(5 unique orders + 1 duplicate)*

| Task | Due | Vendor | Assigned | Project | Requester | Status | Duplicate? |
|------|-----|--------|----------|---------|-----------|--------|-----------|
| GetFPV | Jun 22, 2026 | GetFPV | Meredith O'hara Needham | Shop Supplies | Alex | **Order Shipped** | No |
| Jawstec | Jun 23, 2026 | Jawstec | Meredith O'hara Needham | [550-1] Navy SBIR: Magnetometer | Alex | Order Placed | No |
| HiTec- ByLight | Jun 23, 2026 | HiTec- ByLight | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | No |
| JawsTec- ByLight Gimbal | Jun 23, 2026 | JawsTec- ByLight Gimbal | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | **YES (orig #69507)** |
| JawsTec- ByLight Gimbal (again) | Jun 23, 2026 | JawsTec- ByLight Gimbal | Meredith O'hara Needham | [043-3] Mustang Pt. 2 | Ethan | Order Placed | **YES (duplicate)** |
| Digikey (GCS wifi) | Jun 23, 2026 | Digikey | Meredith O'hara Needham | [300-3] 2026 IDIQ (Hurricane) | Nate | Order Placed | No |

## Task Summary

- **Total tasks:** 6 open, 0 completed
  - **5 unique orders** (GetFPV, Jawstec, HiTec-ByLight, JawsTec-ByLight Gimbal, Digikey)
  - **1 duplicate** (JawsTec-ByLight Gimbal submitted twice)
- **Tasks by assignee:**
  - **Meredith O'hara Needham:** 6/6 (100%)
- **Requester distribution:**
  - **Ethan:** 3/6 (HiTec-ByLight, JawsTec-ByLight Gimbal, JawsTec-ByLight Gimbal again)
  - **Alex:** 2/6 (Jawstec, GetFPV)
  - **Nate:** 1/6 (Digikey GCS wifi)
- **Projects covered:**
  - [043-3] Mustang Pt. 2 (3 tasks; includes 1 duplicate)
  - [550-1] Navy SBIR: Magnetometer (1 task)
  - [300-3] 2026 IDIQ (Hurricane) (1 task)
  - Shop Supplies (1 task)
- **Status distribution:**
  - **Order Placed:** 5 tasks (HiTec-ByLight, Jawstec, JawsTec-ByLight Gimbal x2, Digikey)
  - **Order Shipped:** 1 task (GetFPV)

## Recent Activity

- **Form-based status updates working:** All 5 prior tasks now marked "Order Placed" (status field functional). GetFPV advanced to "Order Shipped" — suggests orders are being executed and tracked.
- **Duplicate task created:** "JawsTec- ByLight Gimbal (again)" (#69507) is an exact duplicate of existing "JawsTec- ByLight Gimbal" (#69507). Both assigned to Ethan, both for [043-3] Mustang Pt. 2, both due Jun 23. Likely caused by:
  - Form re-submission error (requester submitted twice), OR
  - Manual re-entry by form processor, OR
  - Asana UI glitch during task creation.
  - **Action:** Immediate deduplication required. Close/delete one duplicate.
- **All orders remain 100% assigned to Meredith:** No delegation to team members despite prior cycle's recommendation.
- **Project field truncation persists:** Raw data shows incomplete project names (e.g., "[300-3] 2026 IDIQ (", "[043-3] Musta", "[550-1] Navy SBIR: Magnetomete"). Indicates custom field display or export issue in Asana.
- **Prior task (sendcutsend #SC51C906) still absent:** Remains removed from task list. Status unclear (likely legitimately closed given new tasks are functioning properly).

## Notes & Context

- **URGENT ACTIONS (IMMEDIATE):**
  1. **DEDUPLICATE JAWSTEC-BYLIGHT GIMBAL TASK IMMEDIATELY.** Close/delete "JawsTec- ByLight Gimbal (again)" and consolidate with original #69507. Confirm with Ethan whether one or two gimbals were actually needed.
  2. **Distribute purchasing workload from Meredith NOW.** All 6 tasks (5 unique) are due Jun 22–25; Meredith cannot execute alone. Delegate to:
     - **Nate Straus:** Digikey GCS wifi (1 task) — leverages prior purchasing history.
     - **Alex or another team member:** Jawst