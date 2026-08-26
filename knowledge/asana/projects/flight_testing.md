# Flight Testing

## Overview
- **Client/customer:** Internal BST flight testing program
- **Timeline:** Active August 2026; testing window extends through late August
- **Status:** Active — 3 open tasks, 6 recently completed (as of 2026-08-25)
- **Team members involved:** Spencer Hoehl (primary test pilot), Alex Lomis, Ethan Domagala, Maciej Stachura, Jack (pilot support)
- **Risk signals:** 
  - S0 VTOL blocked by MAG signal issue (parameters not saving); test incomplete as of 8/20
  - S10020 firmware QC revealed repeated "Hardware fault" errors on startup
  - S10020 VTOL ESC test ended in catastrophic power loss mid-transition
  - NASA S2 QC flight awaiting scheduling with Jack

## Key Deliverables & Milestones
| Task | Assignee | Target Date | Status |
|------|----------|-------------|--------|
| S1 Fixed Wing QC Flights | Spencer Hoehl | 2026-08-07 | ✅ Completed 2026-08-05 |
| Flamewheel QC Flights | Spencer Hoehl | 2026-08-07 | ✅ Completed 2026-08-05 |
| S10019 Autopilot Test | Maciej Stachura | — | ✅ Completed 2026-08-04 (low takeoff/climb issue found) |
| S10019 SOCOM ground station test | Spencer Hoehl | 2026-08-14 | ✅ Completed 2026-08-17 |
| S10020 firmware QC flight | Spencer Hoehl | — | ✅ Completed 2026-08-25 (Hardware fault errors observed) |
| S10020 VTOL ESC test | Alex Lomis | — | ✅ Completed 2026-08-21 (power loss mid-transition) |
| **S0-MAD Flight testing** | Spencer Hoehl | **2026-08-19** | 🔴 Open — In Design |
| **S0 VTOL** | Alex Lomis | **2026-08-28** | 🔴 Open — Blocked by MAG signal issue |
| **NASA S2 QC flight** | Ethan Domagala | — | 🔴 Open — Awaiting Jack to fly |

## Task Summary
- **Total:** 9 tasks (3 open, 6 completed)
- **By assignee:**
  - Spencer Hoehl: 4 completed, 1 open (80% completion rate)
  - Alex Lomis: 1 completed, 1 open (50%)
  - Maciej Stachura: 1 completed (100%)
  - Ethan Domagala: 0 completed, 1 open (0%)

## Recent Activity
- **2026-08-25:** S10020 firmware QC flight completed but revealed repeated Hardware fault errors on startup (Spencer Hoehl)
- **2026-08-21:** S10020 VTOL ESC test completed; aircraft suffered total power loss during hover-to-forward-flight transition, no recovery with boot (Alex Lomis)
- **2026-08-20:** S0 VTOL throttle-down test passed; hover test proposed but blocked by MAG signal parameter-saving issue (Alex Lomis)
- **2026-08-17:** S10019 SOCOM ground station test completed (3 days past due date)
- **2026-08-05:** S1 Fixed Wing and Flamewheel QC flights both completed on schedule (Spencer Hoehl)

## Notes & Context
- **Critical issues detected in recent testing:**
  - S10020 firmware update (dated 8/21) was intended to fix "no mag" startup issue but Hardware fault errors persisted during QC
  - S10020 VTOL ESC failure resulted in complete power loss mid-transition; aircraft unresponsive to boot
  - S0 VTOL testing blocked by MAG parameter save failure (as of 2026-08-20); root cause unclear
  
- **Ground station testing:** S10019 SOCOM GCS testing completed; requirements included multi-GCS switching during flight and proper dual-GCS operation
- **Aircraft platforms:** Testing covers S-series (S1, S0-MAD, S0 VTOL), S10000-series (S10019, S10020), and Flamewheel variants (FW001, FW002)
- **NASA commitment:** S2 QC flight (S20009) pending to clear customer readiness; requires Jack as designated pilot