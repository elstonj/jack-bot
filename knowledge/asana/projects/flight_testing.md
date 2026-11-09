_Asana snapshot as of 2026-11-09: 6 open tasks, 17 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer**: Internal BST flight testing operations (multiple aircraft platforms and variants)
- **Dollar Value**: Not specified in Asana data
- **Timeline**: Ongoing; most recent activity November 2026
- **Status**: **Active** — 6 open tasks, 17 completed; steady testing cadence with multiple aircraft variants in RC (release candidate) testing phase
- **Team Members**: Spencer Hoehl (primary test pilot/coordinator), Alex Lomis, Ethan Domagala, Jack (QC pilot)
- **Risk Signals**: 
  - 6 open tasks with **no due dates** (unclear urgency/sequencing)
  - ERAU E2 instability issue remains unresolved (9/29 notes: issue could not be reproduced)
  - S10022 lost GPS on climbout (fix pending verification)

## Key Deliverables & Milestones
| Deliverable | Status | Notes |
|---|---|---|
| **FW0001, FW0002 RC Testing** | ✅ Completed 2026-11-04 | Firmware release candidates; requires params download before upload |
| **S10021 RC Testing (VTOL)** | ✅ Completed 2026-11-04 | VTOL-specific firmware changes validated |
| **S10005, S10011 RC Testing** | ✅ Completed 2026-11-04 | Fixed-wing platforms |
| **S10022 RC Testing** | 🔄 Open | GPS climbout loss issue fix pending verification |
| **S10022 Transition Flights** | 🔄 Open | Unassigned; prepares for VTOL transition testing |
| **E20006 RC Testing** | 🔄 Open | No progress notes |
| **S20003 RC Testing** | 🔄 Open | No progress notes |
| **ERAU E2 Instability Investigation** | 🔄 Open | Issue could not be reproduced as of 9/29; aircraft prepped for ongoing investigation |
| **Swiftab App RC Version** | 🔄 Open | Release candidate uploaded |
| **NASA S2 QC Flight** | ✅ Completed 2026-09-21 | Customer-ready vehicle (S20009); passed QC |
| **ByLight Mustang Flight Test** | ✅ Completed 2026-09-22 | Stability characterization and range testing; maintenance required post-flight |

## Task Summary
- **Total**: 23 tasks (6 open, 17 completed; ~74% completion rate)
- **By Assignee**:
  - **Spencer Hoehl**: 22 tasks (primary owner; completed ~15, 6 open)
  - **Alex Lomis**: 1 completed (S0 VTOL, ByLight Mustang pre-test coordination)
  - **Ethan Domagala**: 1 completed (ByLight Mustang test)
  - **Unassigned**: 1 open (S10022 Transition Flights)
- **Patterns**:
  - Heavy release candidate (RC) testing pipeline — 5 aircraft/firmware variants in active RC phase
  - No due dates on open tasks; due dates on completed tasks are historical (Aug–Sep 2026)
  - "Ready for Flight Testing" status predominates among completed tasks
  - QC Required field inconsistently populated

## Recent Activity
- **2026-11-04**: Batch completion of 5 RC testing tasks (FW0001, FW0002, S10005, S10011, S10021)
- **2026-10-14**: S10022 VTOL test flights and S10021 QC flights completed
- **2026-10-09**: S1 fixed-wing and FlameWheel QC firmware validation completed
- **2026-09–10**: ERAU E2 instability investigation underway; issue irreproducible with/without wind sensor mast (9/29 note)
- **2026-09-22**: ByLight Mustang flight test completed; flagged "Maintenance Required"

## Notes & Context
- **Team Feedback Override** (Daniel Prendergast, 2026-10-15 & 2026-10-16): Prendergast asserts "Mine's correct" and requests cessation of "hazing"; context unclear but may indicate data quality disputes or task assignment corrections not reflected in Asana.
- **Firmware Testing Protocol**: Pre-flight QC includes params download before firmware upload (noted on FW0001, FW0002, S10011).
- **Known Issues**:
  - ERAU E2 instability: reproducibility failed; investigation ongoing
  - S10022 GPS climbout loss: fix proposed; RC testing pending verification
  - S0 VTOL MAG signal loss / S10020 ESC power loss: resolved in completed tasks but suggests prior hardware/firmware fragility
- **Customer Activity**: NASA S2 (S20009) passed QC 2026-09-21, indicating delivery readiness
- **No Currency on Open Tasks**: Absence of due dates on 6 open items suggests either backlog items awaiting prioritization or ongoing exploratory testing without hard deadlines