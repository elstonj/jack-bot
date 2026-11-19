_Asana snapshot as of 2026-11-19: 61 open tasks, 19 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview

- **Client/Customer:** SOCOM
- **Priority:** High
- **Owner:** Dan Prendergast
- **Status:** Active — multi-year development program with structured CLINs (Contract Line Items) running through mid-2027
- **Timeline:** 
  - Current phase: Nov 2026 – May 2027
  - Key milestone: GFI (Government Furnished Info) answers due 2026-11-20
  - Final closeouts: May 2027 (CLINs 3, 5, 6)
- **Team Members:** Dan Prendergast (lead), Jack Elston, Sam Hild, Josh Fromm, Ben Busby, Ethan Domagala, Maciej Stachura, Alex Lomis
- **Dollar Value:** Not explicitly stated in custom fields; hour allocations tracked across Mechanical Engineer, Electrical/Firmware, Software, Test Engineer, Systems Engineer, and Technician roles

## Key Deliverables & Milestones

**Near-term (Nov–Dec 2026):**
- **GFI: Answers re PCLT** (Due 2026-11-20) — 16lb safe separation, mount angle, gap tolerances
- **GFI: Customer begins airworthiness process** (Due 2027-01-25)
- **All-variants Common Camera Selection** (Dan Prendergast, Due 2026-11-11) — 10 Mech Eng hrs, 60 Test Eng hrs
- **All-variants Common Processing Hardware Selection** (Jack Elston, Due 2026-11-18) — 30 Elec/Firmware hrs
- **PCLT Test Launch at SOCOM Facility** (Dan Prendergast, Due 2026-11-13) — 50 Mech Eng hrs, 12 Sys Eng hrs
- **All-variants Common Radio Selection** (Jack Elston, Due 2026-12-11) — 25 Elec/Firmware hrs
- **All-variants Carrier Board Design & Fab** (Sam Hild, Due 2026-12-14) — 40 Elec/Firmware hrs

**CLIN 1 (Baseline METAR) — Closeout 2027-03-12:**
- Prototype S0 METAR build (Ethan Domagala, Feb 2027)
- Bench, ground, local flight testing (Ethan Domagala, Feb 2027)
- Operational Flight Evaluation 1 (Due 2027-03-05) — 52 Test Eng hrs, 31 Sys Eng hrs

**CLIN 2 (EO/IR R&R variant) — Closeout 2027-03-12:**
- Prototype S0 EO/IR R&R (Ethan Domagala, Feb 2027)
- Bench, ground, local flight testing (Ethan Domagala, Feb 2027)

**CLIN 3 (Auto-METAR variant) — Closeout 2027-05-31:**
- System-level requirements (Dan Prendergast, Due 2027-01-04)
- Sensor trade studies: Precipitation, Cloud Layer, Horizontal Visibility (Maciej Stachura, Due 2027-01-29)
- Prototype S0 Auto-METAR (Ethan Domagala, Due 2027-02-24)
- Flight eval (Ethan Domagala, Due 2027-03-19)

**CLIN 4 (EO/IR Real-time ATR variant) — Closeout 2027-03-12:**
- ATR model selection & integration (Dan Prendergast, Due 2027-01-19)
- Prototype S0 (Ethan Domagala, Due 2027-04-02)
- Flight eval (Dan Prendergast, Due 2027-04-24)

**CLIN 5 (FMV variant) — Closeout 2027-05-31:**
- Gimballed camera trade study (Dan Prendergast, Due 2027-02-01)
- Gimbal control & video UI (Ben Busby, Due 2027-01-29)
- Prototype S0 EO/IR FMV (Ethan Domagala, Due 2027-02-24)
- Flight eval (Dan Prendergast, Due 2027-03-22)

**CLIN 6 (Datalink variant) — Closeout 2027-05-31:**
- Datalink radio selection (Jack Elston, Due 2027-03-10)
- No-comm transit mode (Maciej Stachura, Due 2027-02-15)
- Closeout slides/report (Dan Prendergast, Due 2027-03-26)

## Task Summary

- **Total:** 61 open, 19 completed (24% completion rate)
- **Assignee breakdown (open tasks only):**
  - Dan Prendergast: 10 tasks (requirements, camera trade study, PCLT test, milestones, ATR selection, flight evals, closeouts)
  - Ethan Domagala: 8 tasks (prototype builds and flight testing across all CLINs)
  - Josh Fromm: 3 tasks (design updates for components)
  - Jack Elston: 4 tasks (hardware/radio selection, comm protocols)
  - Ben Busby: 3 tasks (software for payload automation, gimbal UI)
  - Maciej Stachura: 3 tasks (sensor trade studies, Auto-METAR software, transit mode)
  - Sam Hild: 1 task (carrier board design)
  - **Unassigned: 29 tasks** — many foundational tasks lack clear owners (VOXL2 setup, interface specs, EMI testing, power rail design, mechanical layout)

- **Completion patterns:** 
  - Recent completions (Nov 6–18, 2026): Camera selection/testing, PCLT launch documentation, requirements
  - Early-stage work shows high degree of specialization (trade studies, hardware selection) assigned to subject-matter experts
  - Heavy use of hour tracking across roles (Mechanical Engineer, Electrical/Firmware, Software, Test Engineer, Systems Engineer, Technician)

## Recent Activity

**Completed (last 2 weeks, as of Nov 18, 2026):**
- Camera selection finalized (Nov 13)
- PCLT test launch documentation (Nov 18)
- Parachute cover photos sent to SOCOM PM (Nov 18)
- Nighttime camera tests & video post-processing (Nov 11)
- Daytime camera FoV/resolution assessments (Nov 6)
- Monthly customer update meeting scheduled (Nov 5)

**Approaching/At-Risk:**
- **GFI: Answers re PCLT** due in 2 days (2026-11-20) — blocking airworthiness process
- **All-variants Common Processing Hardware Selection** due 2026-11-18 (may already be overdue)
- Multiple unassigned tasks due 2026-11-20 (camera trade study, VOXL2 lead time, CoVar runtime validation, RB5 SOM comparison, power rail, interface spec, VOXL2 build environment, demo documentation, mechanical layout, EMI testing)
- **PCLT Test Launch** due 2026-11-13 (assigned to Dan Prendergast; Nov 18 completion doc suggests test occurred)

## Notes & Context

**Project Structure:**
- Six contract line items (CLINs) each with distinct payload variants:
  - CLIN 1: Baseline METAR (environmental sensing)
  - CLIN 2: EO/IR Reconnaissance/Recording
  - CLIN 3: Automated METAR (autonomous sensor collection)
  - CLIN 4: EO/IR Real-time ATR (automatic target recognition)
  - CLIN 5: Full-Motion Video (FMV) with gimbal
  - CLIN 6: Datalink (real-time comms)

**Technical Focus Areas:**
- **Hardware Platform:** VOXL2 + Hadron stack, RB5 SBC options, custom carrier board, PCLT (Precision Cargo Launching Tube)
- **Camera/Sensor Selection:** Multiple sensors under evaluation (STARVIS IMX585, various lenses, image intensifiers via L3 Harris); trade studies ongoing
- **Software Integration:** Bridge porting to VOXL2, autopilot-to-SBC comms protocol, payload automation patterns, real-time ATR (models confirmed unclassified/open-source)
- **Testing:** EMI bench testing (camera vs radio/GPS), nighttime performance, ground and local flight trials before operational eval

**Risk Signals:**
1. **29 unassigned open tasks** — many foundational to Nov 20 GFI deadline (VOXL2 setup, power rail, interface spec, EMI test, mechanical layout)
2. **GFI due in 2 days with unanswered questions** (safe separation, mount angle, skin gap) — may require customer coordination
3. **All-variants tasks clustered at Nov 18–Dec 14** — common hardware/radio selection is critical path for all 6 CLINs
4. **Ethan Domagala overloaded** — 8 open build/test tasks across 5 CLINs with tight 2027 timelines
5. **No due date set** for one Comm Protocol task (CLIN 4)

**Customer Engagement:**
- Monthly updates established with SOCOM PM
- Site visit completed (Oct 30) with PCLT loading and power access questions
- Airworthiness process begins after GFI answers (Jan 25 milestone)

**Tech Dependencies:**
- CoVar runtime/64MP frame handling on RB5 (critical for camera pipeline)
- VOXL2 lead time & component ordering (affects build schedule)
- Datalink radio selection impacts FMV and datalink CLINs