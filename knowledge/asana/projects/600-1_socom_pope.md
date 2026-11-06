_Asana snapshot as of 2026-11-06: 56 open tasks, 7 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM (U.S. Special Operations Command)
- **Priority:** High
- **Timeline:** Active project spanning November 2026–May 2027
  - Immediate milestones: Camera selection and test plans (Nov 2026)
  - Major test events: PCLT flight test (Mar 2027)
  - Contract closeout: CLIN 6 complete (May 2027)
- **Status:** Active — 56 open tasks, 7 completed; recently completed site visit and early prototyping
- **Team Members:** Dan Prendergast (lead), Alex Lomis, Josh Fromm, Ethan Domagala, Ben Busby, Maciej Stachura, Jack Elston
- **Risk Signals:**
  - Multiple camera/sensor trade studies and design milestones with tight Nov–Dec 2026 deadlines
  - Several unassigned high-level tasks (camera selection, milestone rollups, security sponsorship)
  - Six CLINs (contract line items) to close out; staggered deliverables suggest complex, phased development

## Key Deliverables & Milestones

### Immediate (Nov 2026)
| Milestone | Due Date | Owner | Notes |
|-----------|----------|-------|-------|
| Write requirements & hold review | 2026-11-02 | Dan Prendergast | OVERDUE (last completed 2026-11-02; duplicate open task) |
| Bench test camera start/stop with laptop | 2026-11-03 | Alex Lomis | |
| Write day/night camera test plans | 2026-11-03 | Alex Lomis | Informal test plans for FoV/resolution assessment |
| Daytime camera tests | 2026-11-06 | Alex Lomis | Various FoV and resolution assessments |
| Software post-processing for video | 2026-11-06 | Dan Prendergast | |
| Draft SOW & Requirements (CoVar) | 2026-11-06 | Dan Prendergast | |
| Select cameras | 2026-11-06 | Dan Prendergast | Part of All-variants Common Camera Selection milestone |
| Nighttime camera tests (STARVIS) | 2026-11-10 | Alex Lomis | |
| Document camera trade study & selection | 2026-11-11 | Unassigned | |

### Near-term (Dec 2026–Jan 2027)
| Milestone | Due Date | Owner | Notes |
|-----------|----------|-------|-------|
| PCLT Test Launch at SOCOM Facility | 2026-11-13 | Dan Prendergast | Draft report due same date |
| Design Changes for PCLT Flight Test | 2026-12-11 | Josh Fromm | Includes separation verification, aircraft installation questions |
| Comm Protocol Design & Implementation (PCLT) | 2026-12-17 | Alex Lomis | |
| Build Prototype S0 METAR | 2026-12-22 | Ethan Domagala | |
| Mechanical/Electrical Updates (PCLT) | 2026-12-23 | Josh Fromm | |
| Software for Payload Integration (PCLT) | 2027-01-22 | Ben Busby | Autonomous collection patterns, image compression, triggers |
| Bench, Ground, Local Flight Testing (METAR) | 2027-01-09 | Ethan Domagala | |
| System-level Requirements | 2027-01-04 | Dan Prendergast | |

### Mid-term (Jan–Mar 2027)
| Milestone | Due Date | Owner | Notes |
|-----------|----------|-------|-------|
| Sensor Trade Studies (Precipitation, Cloud/Ceiling, Visibility) | 2027-01-29 | Maciej Stachura | Three parallel evaluations |
| Datalink radio selection & integration | 2027-01-29 | Alex Lomis | |
| Gimbal control & video UI development | 2027-01-29 | Ben Busby | |
| ATR Selection & Integration | 2027-01-19 | Dan Prendergast | Model questions recorded; all unclassified datasets & models |
| Operational Flight Evaluation (METAR) | 2027-01-26 | Dan Prendergast | |
| Build Prototype S0 EO/IR R&R | 2027-01-28 | Ethan Domagala | |
| PCLT Flight Test | 2027-03-05 | Dan Prendergast | Major test event; multiple variants align to this |
| CLIN 1 Closeout | 2027-03-12 | Dan Prendergast | |
| CLIN 2 Closeout | 2027-03-12 | Unassigned | |

### Later Phase (Mar–May 2027)
| Milestone | Due Date | Owner | Notes |
|-----------|----------|-------|-------|
| Build Prototype S0 Auto-METAR | 2027-02-24 | Ethan Domagala | |
| Build Prototype S0 EO/IR FMV variant | 2027-02-24 | Ethan Domagala | |
| EO/IR Real-time ATR variant build | 2027-04-02 | Ethan Domagala | |
| CLIN 4 Closeout | 2027-03-12 | Dan Prendergast | |
| CLIN 5 Closeout | 2027-05-28 | Dan Prendergast | |
| CLIN 6 Complete | 2027-05-31 | Unassigned | Final contract milestone |

## Task Summary

### Completion Status
- **Total:** 56 open, 7 completed (11% completion rate)
- **Completion trajectory:** Recent activity shows early-phase validation (site visit Oct 30, prototype PCLT completed Oct 30); most work ahead

### Tasks by Assignee (Open Tasks)
| Assignee | Count | Focus Areas |
|----------|-------|------------|
| Dan Prendergast | 16 | Requirements, camera selection, software post-processing, test reports, closeouts (CLIN 1–6) |
| Ethan Domagala | 11 | Prototype builds (METAR, EO/IR variants), bench/flight testing across all CLINs |
| Alex Lomis | 7 | Camera testing (day/night, bench), comm protocol design (PCLT & later variants) |
| Josh Fromm | 6 | Design changes (PCLT flight test), mechanical/electrical updates (PCLT & later) |
| Ben Busby | 4 | Software payload integration (PCLT, EO/IR real-time ATR), gimbal UI |
| Maciej Stachura | 4 | Sensor trade studies (3 parallel), software automation (Auto-METAR variant) |
| Jack Elston | 1 | Comm protocol design (initial) |
| Unassigned | 7 | Camera selection/trade-study documentation, camera/radio/processing selection milestones, CLIN 2 & 6 closeouts, aircraft integration questions |

### Notable Patterns
- **Six CLIN structure:** Project is segmented into six contract line items (PCLT, METAR, Auto-METAR, EO/IR R&R, EO/IR real-time ATR, EO/IR FMV), each with parallel design→build→test→closeout workflows
- **Camera work front-loaded:** Alex Lomis carrying most early camera validation (test plans, day/night tests, trade study documentation)
- **Ethan Domagala bottleneck risk:** 11 prototype builds across 6 variants; densest schedule Oct 2026–May 2027
- **Unassigned critical tasks:** Security sponsorship (FCL/DD254), hardware selections (camera, radio, processing), and final CLIN closeouts lack assigned owners
- **Milestones without due dates:** All-variants Common selections (Camera, Processing Hardware, Radio) and some design tasks have no target dates—likely blocked on earlier stages

## Recent Activity

- **Oct 30, 2026 (completed):**
  - Site visit and instrumented S0 launch at SOCOM facility completed by Josh Fromm
  - Prototype PCLT S0 with accelerometer completed by Ethan Domagala
  - Questions resolved on-site regarding in-flight tube loading and power switch access
  
- **Nov 2–5, 2026 (recent/completing):**
  - Monthly customer update meeting held (Nov 5)
  - Multiple requirements/design docs marked complete (Nov 2)

- **Upcoming critical path (Nov 2026):**
  - Camera test plans and bench testing begin immediately (Alex Lomis, due Nov 3)
  - Daytime/nighttime camera assessments running in parallel (due Nov 6 & Nov 10)
  - PCLT test launch scheduled Nov 13 with report due same day
  - Gimballed camera trade study (Dan Prendergast, due Nov 25)

## Notes & Context

### Payload/Variant Strategy
The project encompasses six operational variants—all sharing common components where possible:
1. **PCLT:** Pod-mounted, early flight test platform
2. **METAR:** Meteorological automated reporting sensor package
3. **Auto-METAR:** Autonomous METAR variant
4. **EO/IR R&R:** Electro-optical/infrared reconnaissance & reconnaissance variant
5. **EO/IR Real-time ATR:** EO/IR with real-time automatic target recognition (AI/ML models confirmed unclassified)
6. **EO/IR FMV:** EO/IR full-motion video variant

Each has distinct design, build, and test phases but converges on shared radio, processing, and comm protocols.

### Key Technical Questions (from task notes)
- **EO/IR ATR models:** Confirmed all training data and models are unclassified, open-source; validation results and label list pending
- **Autonomous collection patterns:** Option to fly in circle and capture at cardinal headings; back-end functions include triggers, compression, calibration
- **PCLT aircraft integration:** Safe separation for 16 lb payload, installation angle, and gap between aircraft skin and tube exit rim still under clarification

### Risk & Dependencies
- **Unassigned ownership:** Camera selection, hardware milestones, and CLIN 2/6 closeouts lack assigned leads
- **Security clearance dependency:** "Ask Jags for FCL/DD254 sponsorship" (unassigned, no due date) may gate later phases if not resolved soon
- **Prototype pipeline:** Ethan Domagala has 11 builds across 6 variants with overlapping schedules (risk of schedule compression)
- **Test facility access:** SOCOM facility availability for Nov 13 PCLT launch and Mar 2027 flight test not explicitly confirmed

### Dollar Value
No contract value visible in task data; custom field data not provided. Infer from CLIN structure that this is a phased, multi-deliverable government development contract.