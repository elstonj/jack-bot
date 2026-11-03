_Asana snapshot as of 2026-11-03: 58 open tasks, 6 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Project Manager:** Dan Prendergast
- **Timeline:** Active development; near-term milestones Nov 2026, major CLINs extending through May 2027
- **Status:** Active — 58 open tasks, 6 completed. Recent completions (Oct 30–Nov 2) include site visit, prototype builds, and requirements reviews. Project is in active testing and design phase.
- **Team Members:** Dan Prendergast (lead), Alex Lomis, Josh Fromm, Ethan Domagala, Ben Busby, Maciej Stachura, Jack Elston
- **Risk Signals:** Multiple imminent deadlines (Nov 2–6) for camera selection, test planning, and SOW drafting. Many milestone-level tasks unassigned or without due dates.

## Key Deliverables & Milestones

### Immediate (November 2026)
- **Camera Selection & Testing** (Nov 3–6)
  - Bench test camera start/stop; write day/night test plans (Alex Lomis, Nov 3)
  - Daytime camera tests—FoV and resolution assessments (Alex Lomis, Nov 4)
  - Nighttime camera tests—STARVIS sensor and lens filters (Alex Lomis, Nov 5)
  - Software post-processing of video (Dan Prendergast, Nov 6)
  - Select cameras; setup monthly customer PM meeting; draft SOW for CoVar (Dan Prendergast, Nov 6)
- **All-variants Common Camera Selection milestone** (Nov 11)
- **Design Changes for PCLT Flight Test milestone** (Nov 3, Josh Fromm) — includes pending questions on S0 safe separation, aircraft angle, and gap clearance
- **PCLT Test Launch at SOCOM Facility milestone** (Nov 13, Dan Prendergast)
- **Comm Protocol Design & Implementation (multiple variants)** — Nov 24 (Jack Elston), Dec 17 (Alex Lomis), Jan 20 (Alex Lomis)
- **Gimballed camera trade study** (Dan Prendergast, Nov 25)

### Q4 2026 – Q1 2027
- **Build Prototype S0 METAR** (Ethan Domagala, Dec 22)
- **Bench, Ground, and Local Flight Testing (METAR)** (Ethan Domagala, Jan 9)
- **Mechanical and Electrical Design Updates** (Josh Fromm, Nov 25–Feb 17, multiple variants)
- **Software for Payload Integration and Automation** (multiple owners and dates: Ben Busby Dec 3 & Jan 22, Maciej Stachura Mar 5, Apr 1)
- **System-level Requirements** (Dan Prendergast, Jan 4)
- **Sensor Trade Studies** (Maciej Stachura, Jan 29): Precipitation, Cloud Layer/Ceiling, Horizontal Visibility

### Q1–Q2 2027
- **PCLT Flight Test milestone** (Mar 5, Dan Prendergast)
- **CLIN 1 Closeout** (Mar 12, Dan Prendergast)
- **Operational Flight Evaluations** — multiple variants: METAR (Jan 26), Auto-METAR (Mar 5), EO/IR R&R (Mar 5), FMV (Mar 22)
- **Build Prototype S0 Auto-METAR, EO/IR R&R, EO/IR ATR, EO/IR FMV variants** (Ethan Domagala, Feb 24–Apr 2)
- **ATR Selection and Integration** (Dan Prendergast, Jan 19) — notes indicate all models unclassified, open-source training data
- **CLIN 2, 4, 5, 6 Closeouts** (Mar 12–May 31)

## Task Summary

| Metric | Count |
|--------|-------|
| **Total Tasks** | 64 (58 open, 6 completed) |
| **Completion Rate** | ~9% |

### Tasks by Assignee (Open)
- **Dan Prendergast:** 14 tasks (project lead, closeouts, milestones, decision items)
- **Ethan Domagala:** 10 tasks (build and test all S0 variants)
- **Josh Fromm:** 6 tasks (mechanical/electrical design, PCLT design changes)
- **Alex Lomis:** 6 tasks (camera testing, datalink, comm protocol)
- **Ben Busby:** 5 tasks (software integration, gimbal/UI development)
- **Maciej Stachura:** 4 tasks (sensor trade studies, software automation)
- **Jack Elston:** 1 task (comm protocol design)
- **Unassigned:** 12 tasks (mostly milestones and subtasks requiring ownership)

### Patterns
- **Heavy milestone structure:** 28+ milestone-level tasks organized by CLIN (Contract Line Item Number), suggesting a complex, multi-variant product (METAR, Auto-METAR, EO/IR R&R, ATR, FMV variants)
- **Prototyping-heavy:** Multiple "Build Prototype S0" tasks followed by bench/ground/flight testing cycles
- **Design iteration:** Mechanical, electrical, software, and hardware selection tasks staggered across variants
- **Unassigned milestones:** Comm protocol, processing hardware/radio selection, and CLIN 2/6 closeouts lack assigned owners — risk for schedule slip

## Recent Activity

**Completed (Oct 15–Nov 2):**
- SOCOM site visit and instrumented S0 launch (Josh Fromm, Oct 30) — answered critical questions on PCLT loading and S0 power accessibility
- Build prototype PCLT S0 with accelerometer (Ethan Domagala, Oct 30)
- Design and order prototype PCLT end cap (Josh Fromm, Oct 15)
- Write requirements and top-level design reviews (Dan Prendergast, Oct 30 & Nov 2)

**Immediately Upcoming (Nov 2–13):**
- Camera testing and selection cycle (Alex Lomis, Dan Prendergast)
- Monthly customer PM setup and SOW draft for CoVar (Dan Prendergast, Nov 6)
- PCLT test launch at SOCOM facility (Nov 13)

## Notes & Context

1. **Multi-variant product structure:** Project tracks 6+ payload variants (METAR, Auto-METAR, EO/IR R&R, ATR, FMV, PCLT) with separate design, build, and test pipelines. Each variant has its own milestone chain.

2. **ATR (Automatic Target Recognition) questions:** Task notes indicate all models are unclassified, open-source, with unclassified training datasets and validation results. This simplifies classification concerns.

3. **Software automation patterns:** Multiple tasks probe autonomous data collection (circular flight with cardinal heading captures, image compression, trigger/calibration functions).

4. **PCLT Flight Test preparation:** Site visit completed; remaining blockers are clarifications on safe separation (16 lb S0), aircraft mounting angle, and clearance gaps.

5. **CoVar handoff:** SOW draft due Nov 6 suggests external contractor involvement for some development work.

6. **Ownership gaps:** 12 unassigned tasks, primarily milestones (Camera Selection, Processing Hardware Selection, Radio Selection, CLIN 2/6 closeouts). Recommend assignment to prevent schedule risk.

7. **Schedule density:** Most imminent work (Nov 2–6) concentrated with Dan Prendergast and Alex Lomis. Nov 13 PCLT launch and Jan–Mar 2027 flight evaluations are critical path items.