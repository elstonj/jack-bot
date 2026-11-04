_Asana snapshot as of 2026-11-04: 58 open tasks, 6 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Owner:** Dan Prendergast
- **Status:** Active, multi-phase R&D program with multiple CLINs (contract line items). Currently in early testing and requirements phase; major milestones extend through May 2027.
- **Team Members:** Dan Prendergast, Josh Fromm, Ethan Domagala, Alex Lomis, Ben Busby, Maciej Stachura, Jack Elston
- **Risk Signals:** 
  - Asana project undergoing restructuring (see corrections, due Monday 2026-11-03)
  - One overdue task: "Write requirements and hold review" (due 2026-11-02, not yet closed in Asana despite completion feedback)
  - Multiple near-term camera testing deadlines (Nov 3–5) and critical path items due Nov 6–13

## Key Deliverables & Milestones

**Near-term (November 2026):**
- All-variants Common Camera Selection — Due 2026-11-06 (Dan Prendergast)
  - Document camera trade study — Due 2026-11-11
- PCLT Test Launch at SOCOM Facility — Due 2026-11-13 (Dan Prendergast)
  - Draft report for test results — Due 2026-11-13
- Design Changes for PCLT Flight Test — Due 2026-11-03 (Josh Fromm) ⚠️ approaching
- Comm Protocol Design & Implementation — Due 2026-11-24 (Jack Elston)
- Mechanical and Electrical Design Updates — Due 2026-11-25 (Josh Fromm)

**Medium-term (December 2026 – January 2027):**
- Software for Payload Integration and Automation (CLIN 1) — Due 2026-12-03 (Ben Busby)
- Build Prototype S0 METAR — Due 2026-12-22 (Ethan Domagala)
- Bench, Ground, and Local Flight Testing — Due 2027-01-09 (Ethan Domagala)
- Sensor Trade Studies (Precipitation, Cloud, Visibility) — Due 2027-01-29 (Maciej Stachura)
- System-level Requirements — Due 2027-01-04 (Dan Prendergast)
- CLIN 1 Closeout — Due 2027-03-12 (Dan Prendergast)

**Downstream (February – May 2027):**
- Multiple prototype builds and flight evaluations across variants (METAR, Auto-METAR, EO/IR, ATR, FMV)
- CLIN 2–6 closeouts progressing through May 2027

## Task Summary
- **Total tasks:** 58 open, 6 completed
- **Completion rate:** ~9% (6 of 64 tasks closed)
- **Tasks by assignee (open):**
  - Dan Prendergast: 13 tasks (design, requirements, testing, closeouts)
  - Ethan Domagala: 7 prototype build/test tasks
  - Josh Fromm: 5 mechanical/design tasks
  - Alex Lomis: 4 camera and comm tasks
  - Ben Busby: 3 software tasks
  - Maciej Stachura: 3 sensor trade studies + software
  - Jack Elston: 1 comm protocol task
  - Unassigned: 17 milestone/placeholder tasks (mostly lacking owners)

- **Patterns:** 
  - Heavy use of CLIN-based structure (6 contract lines, each with multiple design→build→test→closeout tasks)
  - Multiple parallel variant tracks (PCLT, METAR, Auto-METAR, EO/IR variants, ATR)
  - Significant unassigned work suggests early-stage planning; team restructure underway

## Recent Activity

**Team Actions (from corrections, authoritative):**

- **2026-11-02 & 2026-10-30:** Daniel Prendergast refactoring SOCOM Asana project structure; project and stickies planned for Monday 2026-11-03 morning. This explains task volume and unassigned items — restructuring to align with physical Kanban board and 6-month rolling milestones (per Maciej's 2026-10-27 note).

- **2026-10-08 & 2026-10-07:** SOCOM status update (Daniel Prendergast):
  - Top-level requirements derivation from five CONOPS in ROMs — complete early that week
  - Josh completing end cap CAD; sending for quote
  - Accelerometer ordered to measure ejection force profile
  - Expected delivery: late Oct or week of Oct 19 → test fire arrangement planned after

- **Recently Completed (Asana closed tasks):**
  - SOCOM site visit and instrumented S0 launch (Josh Fromm) — completed 2026-10-30
  - Build prototype PCLT S0 with accelerometer (Ethan Domagala) — completed 2026-10-30
  - Write requirements and top-level design tasks (Dan Prendergast) — completed 2026-10-30 and 2026-11-02
  - Design and order prototype PCLT end cap (Josh Fromm) — completed 2026-10-15

## Notes & Context

**Asana Restructuring in Progress (Authoritative Override):**
- Per Daniel Prendergast (2026-11-02, 2026-10-30): Project refactoring underway to simplify planning and provide better visibility
- Per Maciej (2026-10-27): Two-level planning model — Asana tracks long-term milestones and upcoming weekly tasks; physical Kanban board manages weekly engineering execution
- **Impact:** Many unassigned milestone tasks in Asana are placeholders; actual ownership and execution will be managed via Kanban board and direct team coordination

**Active Testing Track:**
- Camera selection and testing is immediate priority (tests due Nov 3–5)
- PCLT site visit completed; awaiting end cap and accelerometer arrival (week of Oct 19 or later) for first test fire
- Multiple questions from site visit require follow-up (inflight loading, power switch access, etc.)

**Multi-Variant Strategy:**
- Project encompasses at least 6 distinct CLINs/product variants:
  1. PCLT (Precision Lofted Collection Tool) — flight-test milestone 2027-03-05
  2. METAR — prototype due 2026-12-22
  3. Auto-METAR — prototype due 2027-02-24
  4. EO/IR R&R (Reconnaissance & Reconnaissance?) — prototype due 2027-01-28
  5. EO/IR Real-time ATR (Automatic Target Recognition) — prototype due 2027-04-02
  6. EO/IR FMV (Full-Motion Video) — prototype due 2027-02-24
- Each variant follows similar phase gate: requirements → design → prototype build → bench/ground/flight test → operational evaluation → closeout

**Software Integration Points:**
- Ben Busby and Maciej Stachura own payload integration and automation software; due dates range Dec 2026 – Apr 2027
- Key features noted: autonomous data collection patterns (circular flight, cardinal headings), image capture triggers, compression, UI updates
- Gimbal control and video UI development (Ben Busby) due 2027-01-29

**Dependencies & Open Questions:**
- ATR variant depends on model selection (noted: all open-source, unclassified training)
- Mechanical/electrical integration tasks (Josh Fromm) are prerequisites for prototype builds
- Radio selection and comm protocol design (Alex Lomis, Jack Elston) critical path for multiple variants