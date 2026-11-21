_Asana snapshot as of 2026-11-21: 62 open tasks, 24 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Owner:** Dan Prendergast
- **Status:** Active – multi-variant development program with structured CLINs (Contract Line Items) and phased milestones through Q2 2027
- **Team:** Jack Elston (electrical/firmware), Josh Fromm (mechanical), Sam Hild (electrical/firmware), Ethan Domagala (prototype build/test), Ben Busby (software), Maciej Stachura (software/sensors), Dan Prendergast (systems/PM), Alex Lomis (test)
- **Risk Signals:**
  - 62 open tasks vs. 24 completed; many core design and integration tasks unassigned
  - Multiple unassigned milestones approaching Jan–Mar 2027 (GFI milestones, component selection, design reviews)
  - Several design and build tasks cluster at 2026-11-20, 2027-01-01, 2027-02-01, 2027-03-15 — potential resource bottleneck
  - Comm Protocol tasks duplicated across CLINs with inconsistent assignment (Jack Elston, Unassigned)

## Key Deliverables & Milestones

| Milestone | Due | Status | Notes |
|-----------|-----|--------|-------|
| **GFI: Answers re PCLT** | 2026-11-30 | OPEN | Unassigned; clarify 16lb separation, mount angle, aircraft skin gap |
| **GFI: Customer begins airworthiness process** | 2027-01-25 | OPEN | Unassigned |
| **CLIN 1 Closeout** | 2027-03-12 | OPEN | Dan Prendergast; Operational Flight Eval due 2027-03-05 |
| **CLIN 2 Closeout (METAR)** | 2027-03-12 | OPEN | Unassigned; prototype build/test/flight eval Feb–Mar |
| **CLIN 3 Closeout (Auto-METAR)** | 2027-05-31 | OPEN | Unassigned; prototype build/test/flight eval Feb–Mar, final eval 2027-03-05 |
| **CLIN 4 Closeout (EO/IR R&R)** | 2027-03-12 | OPEN | Dan Prendergast; prototype build/test/flight eval Feb–Mar |
| **CLIN 5 Closeout (Real-time ATR)** | 2027-05-31 | OPEN | Dan Prendergast; build/test/flight eval Mar–Apr |
| **CLIN 6 Closeout (FMV Gimbal)** | 2027-05-31 | OPEN | Dan Prendergast; build/test/flight eval Feb–Mar, closeout slides due 2027-03-26 |

## Task Summary

**Totals:** 62 open, 24 completed (79.5% open rate)

**By Assignee (Open Tasks):**
- **Unassigned:** 29 tasks (47%) — including 7 milestones, critical design reviews, and prototype builds
- **Ethan Domagala:** 10 tasks (component ordering, prototype builds, bench/flight testing across CLIN 2–6)
- **Dan Prendergast:** 8 tasks (system requirements, ATR integration, operational flight evals, closeout reports)
- **Josh Fromm:** 5 tasks (mechanical/electrical design updates, PCLT flight test design)
- **Jack Elston:** 4 tasks (component/radio selection, comm protocol — 70 hrs Electrical/Firmware budgeted)
- **Ben Busby:** 2 tasks (gimbal UI dev, software for ATR variant)
- **Maciej Stachura:** 3 tasks (sensor trade studies, Auto-METAR software, no-comm transit mode)
- **Sam Hild:** 1 task (RevB SOM selection; 40 hrs Electrical/Firmware budgeted)

**Completion Rate by Assignee:**
- Dan Prendergast: 10 completed (high engagement early phase; now carrying milestone/closeout burden)
- Ethan Domagala: 3 completed (ramping up for Feb–Mar prototype surge)
- Alex Lomis: 3 completed (camera test work concluded)
- Other assignees: minimal historical completion

**Notable Patterns:**
- **Hardware bottleneck:** RB5/VOXL2 platform selection, SOM/carrier board, radio selection still open with long lead times expected
- **Duplicated comm protocol tasks:** appears in CLIN 1, 2, 4, 5 with varying hour budgets and assignees; suggests unresolved architecture
- **Heavy hour allocation:** Mechanical Engineer hours (60–70 per task), Test Engineer (40–60 per eval), Software Engineer (40–60 per variant)
- **Prototype surge:** Feb 1 – Mar 19 window has 8 prototype builds and 6+ flight evals scheduled; Ethan Domagala is critical path
- **Sensor/Algorithm work (Auto-METAR, ATR):** Maciej Stachura leading trade studies (Jan 29) and integration tasks; ATR model classification/validation questions pending

## Recent Activity

**Latest Completed (2026-11-20 or earlier):**
- PCLT Test Launch at SOCOM Facility (2026-11-20) — Dan Prendergast led; site visit and launch occurred 2026-10-30, post-test results documented
- All-variants Common Camera Selection (2026-11-20) — STARVIS/Sony IMX585 sensor selected after day/night bench and field tests (Nov 3–11)
- VOXL2 lead time confirmed and components ordered (2026-11-20)
- Hadron camera ordering (2026-11-11); CoVar SOW/requirements drafted (2026-11-09)
- Monthly customer PM update meeting established (2026-11-05)

**Immediate Upcoming (November 2026 – Early January 2027):**
- **2026-11-30:** GFI PCLT answers due (airworthiness clarifications) — currently unassigned and at risk
- **2026-12-04:** Common Radio Selection (Jack Elston) — 25 hrs budgeted
- **2026-12-15:** EMI Bench Testing (unassigned)
- **2026-12-20:** PCLT Flight Test Design Changes (Josh Fromm) — 54 hrs Mech, 6 hrs Sys, 10 hrs Tech
- **2026-12-21:** Mech/Electrical Design Updates for CLIN 3 (Josh Fromm) — 70 hrs Mech, 5 hrs Sys
- **2027-01-01:** Electrical/Firmware Updates, Comm Protocol, Component Integration tasks converge (multiple tasks, multiple assignees)
- **2027-01-04:** System-level Requirements (Dan Prendergast)
- **2027-01-07:** Order Components for Prototype S0 METAR (Ethan Domagala) — 22 hrs Mech, 40 hrs Tech

## Notes & Context

- **Program Structure:** Six CLINs (Contract Line Items) covering payload variants: CLIN 1 (base platform), CLIN 2 (METAR weather sensor), CLIN 3 (Auto-METAR), CLIN 4 (EO/IR R&R), CLIN 5 (Real-time ATR), CLIN 6 (FMV gimbal). Each has design → build → bench test → flight eval → closeout sequence.

- **PCLT (Parachute Container Lifting Tube):** Early hardware flew Oct 30, 2026 with accelerometers. Customer feedback (Nov 13 target, completed Nov 18) addressed mount angle, safe separation, and aircraft integration. Design changes now in progress (due Dec 20).

- **Platform Integration Questions:**
  - RevB carrier board for RB5-class SOMs (Sam Hild) — selection deadline slip likely; full design/fab due 2027-03-15 with 40 hrs budget
  - VOXL2 build environment and autopilot-to-SBC bridge (unassigned) — critical for multi-variant firmware
  - Autopilot-to-SBC interface spec v0 (unassigned) — foundational; due 2026-11-20 (likely at-risk)

- **Sensor/Algorithm Tracks (CLIN 3, 5):**
  - Precipitation, cloud/ceiling, horizontal visibility sensor trade studies all due 2027-01-29 (Maciej Stachura)
  - ATR (Automatic Target Recognition) model selection pending review of training data (open-source), validation results, classification status; Dan Prendergast to resolve by 2027-01-19
  - Auto-METAR collection patterns and back-end functions documented in task notes but software implementation (Maciej Stachura) not due until 2027-03-05

- **Custom Field Usage:** Extensive hour allocation by role (Electrical/Firmware, Mechanical Engineer, Test Engineer, Systems Engineer, Technician, Software Engineer). No dollar amounts captured in custom fields; contract value not provided.

- **Unassigned Risk:** 29 open tasks with no assignee include 7 milestones and critical path work (autopilot interface, VOXL2 porting, prototype S0 builds for METAR/EO-IR R&R/Auto-METAR). Assignment backlog should be cleared before 2026-11-30 to meet Q1 2027 prototype readiness.

- **Interlock with SOCOM:** Monthly PM updates in place; customer airworthiness process to begin by 2027-01-25. PCLT feedback loop active (questions outstanding, design changes in progress). Facility tests scheduled March 2027.