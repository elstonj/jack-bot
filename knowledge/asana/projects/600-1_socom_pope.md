_Asana snapshot as of 2026-11-20: 61 open tasks, 19 completed (last 90 days)._

# SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Program Manager:** Dan Prendergast
- **Priority:** High
- **Status:** **Active — Under Restructuring** (see Team Corrections below)
- **Timeline:** 
  - Current phase: Nov 2026 (component selection & hardware eval)
  - Final delivery: May 2027 (CLIN 6 closeout)
  - Key milestones: GFI answers (11/20), PCLT test launch (11/13), operational flight evals (3/5–4/24)
- **Team:** Dan Prendergast (PM, Mechanical), Jack Elston (Electrical/Firmware), Josh Fromm (Mechanical), Sam Hild (Electrical), Ethan Domagala (Build/Test), Ben Busby (Software), Maciej Stachura (Systems/Software), Alex Lomis (Test)

## Status & Recent Context
**TEAM CORRECTIONS (authoritative):**
- **[2026-11-05, 2026-11-04] Maciej:** Kanban board restructuring underway. SOCOM has "lots of tasks still on the board"; inquiring whether tasks should move to next week or if additional resources are needed. This signals resource pressure and potential task backlog.
- **[2026-11-02, 2026-10-30] Daniel Prendergast:** "Still working on refactoring the SOCOM asana project. Project and stickies will be ready by Monday morning."
- **[2026-10-27] Maciej:** Broader Asana restructuring planned: two-level planning (Asana for long-term milestones + weekly tasks; physical Kanban for weekly execution), 6-month rolling milestone plan.

**Asana currently shows 61 open tasks, 19 completed.** However, Daniel is actively refactoring the project structure, so task counts and organization are in flux.

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status | Notes |
|-----------|-------|----------|--------|-------|
| GFI: Answers re PCLT | Unassigned | 2026-11-20 | OPEN | 16lb safe separation? Mount angle? Gap specs needed. |
| PCLT Test Launch at SOCOM Facility | Dan Prendergast | 2026-11-13 | OPEN | 50 Mech Eng hrs, 12 Systems Eng hrs. |
| All-variants Common Camera Selection | Dan Prendergast | 2026-11-11 | OPEN | 10 Mech hrs, 60 Test hrs. **Status: Nearly complete** (camera already selected & ordered; "Select cameras" marked done 11/13). |
| All-variants Common Processing Hardware Selection | Jack Elston | 2026-11-18 | OPEN | 30 Electrical/Firmware hrs. VOXL2 lead time & component sourcing. |
| All-variants Common Radio Selection | Jack Elston | 2026-12-11 | OPEN | 25 Electrical/Firmware hrs. |
| All-variants Carrier Board Design & Fab | Sam Hild | 2026-12-14 | OPEN | 40 Electrical/Firmware hrs. |
| **CLIN 1 Closeout** | Dan Prendergast | 2027-03-12 | OPEN | Includes operational flight eval (3/5), design changes, proto build, testing. |
| **CLIN 2 Closeout** | Unassigned | 2027-03-12 | OPEN | EO/IR R&R variant; similar scope. |
| **CLIN 3 Closeout** | Unassigned | 2027-05-31 | OPEN | Auto-METAR variant; sensor trade studies (precipitation, cloud, visibility). |
| **CLIN 4 Closeout** | Dan Prendergast | 2027-03-12 | OPEN | ATR (automated target recognition) variant. |
| **CLIN 5 Closeout** | Dan Prendergast | 2027-05-31 | OPEN | Full-motion video (FMV) gimballed variant. |
| **CLIN 6 Closeout** | Dan Prendergast | 2027-05-31 | OPEN | Closeout slides/report. |
| **GFI: Customer begins airworthiness process** | Unassigned | 2027-01-25 | OPEN | Gate for regulatory approval. |

## Task Summary

**Totals:** 61 open, 19 completed (~24% completion rate)

**By Assignee:**
- **Dan Prendergast:** 10 open tasks (PM, design, testing lead)
- **Jack Elston:** 4 open tasks (all Electrical/Firmware, comms/radio/processing)
- **Josh Fromm:** 4 open tasks (mechanical design updates)
- **Ethan Domagala:** 8 open tasks (proto builds and flight testing)
- **Ben Busby:** 3 open tasks (software payload integration)
- **Maciej Stachura:** 4 open tasks (trade studies, software, systems)
- **Sam Hild:** 1 open task (carrier board design)
- **Unassigned:** 23 open tasks (many are parallel-track subtasks for CLINs 1–6; awaiting triage as project is refactored)

**Patterns:**
- **Heavy custom field usage:** Nearly all open tasks include hour budgets (Mechanical Engineer, Electrical/Firmware, Software, Test, Systems Engineer, Technician hours).
- **Parallel CLIN structure:** 6 customer line items (CLINs 1–6), each with parallel task tracks (design → prototyping → testing → closeout).
- **Resource concentration:** Ethan Domagala (build/test) has highest task count; Dan Prendergast has highest visibility/approval duties.
- **Many unassigned tasks:** Reflect the ongoing restructuring and need for triage.

## Recent Activity

**Completed (last week):**
- Camera selection finalized (STARVIS + Sony IMX585 tested; Hadron cameras ordered).
- PCLT test launch documentation completed (11/18).
- S0 parachute cover photos sent to customer PM (11/18).
- Site visit at SOCOM facility completed (10/30); instrumented S0 launch performed.

**Approaching Deadlines (next 2–3 weeks):**
- **PCLT Test Launch** due 2026-11-13 (overdue or imminent).
- **GFI: Answers re PCLT** due 2026-11-20 (questions about safe separation, mount angle, gap specs).
- **Camera selection task** officially due 2026-11-11 (already completed 2026-11-13, slight overage).
- **Processing hardware selection** due 2026-11-18; VOXL2 lead time & component ordering underway.

**Risk Signals:**
- **PCLT test launch deadline (11/13):** Very tight; likely completed or slipping based on "refactoring" comments.
- **Lots of SOCOM tasks on Kanban board (11/4–11/5):** Maciej flagging resource constraint; asking if tasks should move to next week or if help is available.
- **Project restructuring in progress:** Daniel Prendergast stated stickies & refined project plan would be ready "Monday morning" (est. 11/3 or 11/10), indicating fluidity and possible task churn.

## Notes & Context

1. **Six-variant product line:** This is not a single deliverable but a family:
   - CLIN 1: Base METAR (weather data collection)
   - CLIN 2: EO/IR R&R (electro-optical/infrared recce)
   - CLIN 3: Auto-METAR (autonomous weather variant)
   - CLIN 4: ATR (automated target recognition)
   - CLIN 5: FMV gimbal (full-motion video)
   - CLIN 6: Closeout

2. **Phased approach:** Each CLIN follows: design → component sourcing → proto S0 build → bench/ground/flight testing → operational evaluation → closeout. Many tasks are repeated across CLINs with variant-specific adjustments.

3. **Hardware platform evolving:** 
   - Base: RB5-class SOM (Snapdragon), Hadron camera stack, radio TBD.
   - Variants exploring: VOXL2 for processing, gimbal hardware, ATR models (unclassified), different sensors (precipitation, visibility, cloud layer for CLIN 3).

4. **Custom field tracking:** Extensive use of hour budgets per role; enables resource planning and cost tracking.

5. **Customer engagement active:** Monthly updates scheduled with SOCOM PM; site visits conducted; questions being resolved (e.g., PCLT in-flight loading, power switch access).

6. **Known open questions:**
   - PCLT safe separation mass (16 lb)?
   - Mount angle in aircraft?
   - Gap between aircraft skin and PCLT tube?
   - CoVar runtime & 64MP frame handling on RB5?
   - Datasets for ATR models (all open-source?)?
   - Autonomous collection patterns (circle + cardinal headings)?

7. **External dependencies:**
   - L3 Harris (image intensifier meeting completed 11/9).
   - Jags (FCL/DD254 sponsorship request; completed 11/10).
   - CoVar (custom software for video processing; SOW drafted 11/9).
   - SOCOM site (for PCLT test launch, airworthiness process).

---

**Next Steps (inferred from open tasks & corrections):**
- Complete PCLT test launch evaluation (due 11/13 or now overdue).
- Answer GFI questions on PCLT mounting & safe separation (due 11/20).
- Finalize processing hardware & radio selections (due 11/18–12/11).
- Begin carrier board design (Sam Hild, due 12/14).
- Support Daniel's Asana refactoring to clarify unassigned tasks and resource allocation.
- Monitor Kanban board pressure; reallocate or extend timelines if needed.