_Asana snapshot as of 2026-10-23: 60 open tasks, 2 completed (last 365 days)._

# [600-1] SOCOM Pope

## Overview

- **Client/Customer:** SOCOM
- **Owner:** Dan Prendergast
- **Timeline:** Active development; CLIN 1 milestone due 2026-12-15; final CLIN 6 milestone due 2027-05-31
- **Status:** **ACTIVE** — Early-stage prototype development underway. Per Daniel Prendergast (2026-10-08), top-level requirements from five CONOPS will be complete early week of Oct 14; end cap CAD and accelerometer expected to arrive late week of Oct 13 or week of Oct 19.
- **Team Members:** Dan Prendergast (PM, lead), Josh Fromm (mechanical/design), Ethan Domagala (build/test), Alex Lomis (datalink/comms), Ben Busby (software/UI), Maciej Stachura (sensors/software)
- **Risk Signals:** Multiple imminent deadlines (Oct 19–27) for requirements, first site visit, and EO/IR camera selection; schedule is front-loaded and dependent on accelerometer/end cap arrival.

## Key Deliverables & Milestones

**CLIN 1 (Pope – EO/IR R&R)**  
- Due: 2026-12-15  
- Deliverables: prototype S0 with accelerometer, instrumented launch, design refinement, CAD for Rev B, closeout report

**CLIN 2 (METAR)**  
- Due: 2027-02-26  
- Deliverables: prototype S0 with precipitation/cloud/visibility sensors, bench & flight testing, closeout report

**CLIN 3 (Auto-METAR)**  
- Due: 2027-03-26  
- Deliverables: enhanced METAR with automatic reporting, operational evaluation, closeout report

**CLIN 4 (EO/IR R&R – Storage)**  
- Due: 2027-04-30  
- Deliverables: prototype with camera/storage, datalink, operational flight evaluation, closeout report

**CLIN 5 (EO/IR Real-time ATR)**  
- Due: 2027-05-14  
- Deliverables: prototype with edge compute & ATR models, full integration, closeout report

**CLIN 6 (EO/IR FMV – Gimballed)**  
- Due: 2027-05-31  
- Deliverables: gimballed camera, full-motion video UI, no-comm transit mode, closeout report

## Task Summary

- **Total Tasks:** 60 open, 2 completed (97% open)
- **Completion Rate:** ~3% (only kickoff and end cap design completed)
- **Tasks by Assignee:**
  - **Dan Prendergast:** 13 tasks (requirements, camera selection, reviews, evaluations, closeout reports)
  - **Ethan Domagala:** 11 tasks (prototype builds & testing across all CLINs)
  - **Josh Fromm:** 8 tasks (mechanical design, integration, design refinement)
  - **Ben Busby:** 6 tasks (UI/software across EO/IR, METAR, ATR, FMV variants)
  - **Maciej Stachura:** 4 tasks (sensor trade studies, software development)
  - **Alex Lomis:** 4 tasks (datalink & comms protocols across variants)
  - **Unassigned:** 2 milestone tasks (CLIN 1 & 4 milestones)

- **Key Pattern:** Project structured in six CLINs, each with write requirements → design/selection → build prototype → test → closeout. Heavy parallelization across sensor/camera variants; Ethan Domagala is build/test bottleneck.

## Recent Activity

**Completed (Oct 1–15):**
- Kickoff (Oct 1)
- End cap CAD and order (Oct 15, originally due Oct 2)

**Imminent (Next 2 weeks):**
- Write requirements and top-level design – **due Oct 19** (Dan Prendergast)
- Build prototype PCLT S0 with accelerometer – **due Oct 20** (Ethan Domagala)
- SOCOM site visit and instrumented S0 launch – **due Oct 27** (Josh Fromm)
- EO/IR camera selection and purchase – **due Oct 28** (Dan Prendergast)

**On-Track Inputs (per Daniel Prendergast, Oct 7–8):**
- Top-level requirements being derived from five CONOPS in ROMs; completion expected early week of Oct 14
- End cap CAD completed by Josh; sent for quote
- Accelerometer ordered; expected arrival late week of Oct 13 or early week of Oct 19
- First test fire planned after components arrive

## Notes & Context

- **Variant Strategy:** Project includes six CLIN variants building on core Pope platform: METAR sensors, Auto-METAR, EO/IR with recording, EO/IR with real-time ATR, and EO/IR with full-motion video gimbal. Each variant follows same spiral pattern (requirements → design → build → test → closeout).
- **Technology Decisions Pending:** EO/IR camera selection (storage vs. real-time compute requirements), ATR model provenance (unclassified datasets confirmed for one variant), gimballed camera trade study, datalink protocol across variants.
- **Test Site Dependency:** SOCOM site visit (Oct 27) is critical path; questions in task notes indicate uncertainty about inflight tube loading and power accessibility—answers will drive design refinement.
- **Supply Chain Risk:** End cap and accelerometer arrival late Oct or mid-Oct 19 week; any delay cascades to prototype build (due Oct 20) and site visit (due Oct 27).
- **Team Capacity Risk:** Ethan Domagala has 11 prototype builds across 6 CLINs; Josh Fromm responsible for mechanical integration across all variants. Schedule assumes parallel execution, which may be at risk if build or integration work slips.