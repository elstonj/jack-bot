# BST Phase II Review and Visualization Plan

## Document Metadata
- **Type:** Internal review and editorial guidance document
- **Client/Agency:** NASA (SBIR Program)
- **Program/Solicitation:** NASA SBIR Phase II – "Adaptive and Secure Autonomy for UAS" (Phase II proposal)
- **Date:** May 11, 2026
- **BST Products/Systems Referenced:** SwiftCore, SwiftSim, SwiftDeploy, S2, S3, E2, S0 airframes
- **Key Personnel:** Jack Elston (PI), Maciej Stachura (CTO), Daniel Prendergast, Ben Busby, Joshua Fromm, Sam Hild, Alex Lomis, Ethan Domagala, Beck Cotter, Ed Kase

---

## Executive Summary

This document provides a comprehensive editorial and strategic review of BST's Phase II proposal (46 pages) to NASA SBIR, identifying that the technical content is strong but suffers from a critical lack of embedded visuals and structured tables. The reviewer (Jack Elston, dated May 11, 2026) recommends inserting 7 figures, 7 tables, and 3 briefing-chart graphics before the May 15, 2026 submission deadline to maximize Factor 1 (Scientific/Technical Merit, 45% weight) and Factor 3 (Work Plan Effectiveness, 25%) scores. The plan provides sources, insertion points, and execution priority for all recommended additions.

---

## Key Findings & Assessment

### Proposal Strengths
- Section 2.3 (EMASS proof point): "strongest single section in the current draft"
- Phase I-to-Phase II narrative arc: clear and credible
- Architectural decomposition (2.5.1–2.5.2): technically accurate, aligns with Phase I Final Report
- Work plan (Part 4): appropriate task overlap and critical path
- Part 7 (Commercialization): anchored in real customer relationships (EMASS, ADONIS, NOAA IDIQ, Genesis/BNL, Navy, AFWERX) rather than speculative TAM

### Critical Gaps
**Visual density (highest-leverage gap):** Proposal references ~7 figures inline with captions ("the figure below shows...") but contains **zero embedded figures or tables outside prose**. Six placeholder image slots (image1–image6) in ProSAMS section unfilled.

**Tables (second-highest-leverage gap):**
- Technical Objectives buried in prose paragraphs; need structured 6-objective table with acceptance criteria
- Quarterly milestone plan section empty (explicitly required by NASA solicitation §3.4.3.4)
- Personnel labor allocation described in prose; reviewers expect labor matrix
- Risks scattered through task descriptions; need consolidated risk register
- Customer pipeline qualitative; need quantified table with contract values and timing

---

## Recommended Visual Assets

### Figures to Embed in Technical Proposal Body (7 total)

| # | Figure | Section | Source | Score Impact |
|---|--------|---------|--------|--------------|
| F1 | EMASS Flight 4 attitude (roll/pitch/yaw with envelope & engagement windows shaded) | 2.3 | Phase I conv. 4/29/26 `/f4_attitude.png` | **Factor 1 (HIGH)** |
| F2 | EMASS Flight 4 rotor PWM saturation (4 lift channels + servos, payload windows shaded) | 2.3 | `f4_actuators.png` (prior session) | **Factor 1 (HIGH)** |
| F3 | EMASS Flight 4 altitude + horizontal speed / ground track overlay | 2.3 | `f4_altitude_speed.png` or `f4_groundtrack.png` | **Factor 1 (MED-HIGH)** |
| F4 | SwiftCore Layered Control Architecture (Layers 1–5 + Safe Flight Controller + Arbiter) | 2.5.1 | Phase I Final Report PDF p.15–16 | **Factor 1 (HIGH)** |
| F5 | SwiftCore SW/HW Components (MCU tier + SBC tier + WASM modules, color-coded by functional level) | 2.5.2 | Phase I Final Report architecture section | **Factor 1 (HIGH)** |
| F6 | Neural network learning curves + PID-vs-ML vertical-rate command comparison | 2.5.3 | Phase I Final Report + `model3_learning_curve.png`, `model3_prediction_vs_actual.png` | **Factor 1 (MED)** |
| F7 | JSBSim flight trajectory comparison: standard altitude controller vs terrain-following | 2.5.3 | Phase I Final Report PDF p.47 | **Factor 1 (MED)** |

**Key insight:** Figures F1, F2, F4 are the highest-leverage edits. F1–F2 convert Section 2.3 from strong prose to unimpeachable proof; F4 anchors every architectural claim.

### Briefing Chart Figures (outside 46-page limit)

| # | Figure | Purpose | Source |
|---|--------|---------|--------|
| BC1 | Compact SwiftCore architecture overview (single image, condensed from F4) | Briefing chart image4 slot | Derive from F4—make half-page, high-contrast version |
| BC2 | EMASS Flight 4 hero shot OR roll-excursion attitude plot with +73° spike | Briefing chart image5 slot | `EMASS_Media/2026-04-24/YOP05872.JPG` OR cropped F1 |

### ProSAMS Submission Graphics (required)

| # | Figure | Purpose | Source |
|---|--------|---------|--------|
| P1 | TRL Progression bar chart (TRL 5–6 start → TRL 7 end, task contributions called out) | ProSAMS image1 slot | Generate new from technical objectives mapped to TRL milestones |
| P2 | Budget summary chart (cost-by-task or cost-by-quarter) | ProSAMS image2 slot | From Beck Cotter's budget input |
| P3 | Briefing chart layout reference / mockup | ProSAMS image3 slot (instructional) | NASA template + filled content |

---

## Recommended Tables

### Seven Tables to Insert (ready-to-paste versions provided in Section 4 of source document)

| # | Table | Insertion Point | Score Impact | Status |
|---|-------|-----------------|--------------|--------|
| **T1** | **Phase II Technical Objectives Summary** (6 objectives × 4 columns: title, description, acceptance criteria, primary tasks) | Part 3 (replaces prose) | **Factor 1 (HIGH) + Factor 3 (HIGH)** | Ready to paste |
| **T2** | **Task ↔ Objective Traceability Matrix** (8 tasks × 6 objectives + TRL contribution; ● = primary, ○ = supporting) | Top of Part 4.1 | **Factor 3 (HIGH)** | Ready to paste |
| **T3** | **Quarterly Milestone Schedule** (8 quarters × cost-bearing milestones; also for ProSAMS budget submission) | Part 4 "Milestone Plan" section (currently empty) | **Factor 3 (HIGH)** — required by NASA solicitation §3.4.3.4 | Ready to paste |
| **T4** | **Personnel Labor Allocation by Task** (people × tasks, LOE as % of available time across 24 months) | Part 4.4 (replaces narrative paragraphs) | **Factor 2 (HIGH) + Factor 3 (MED)** | Ready to paste |
| **T5** | **Aggregate Risk Register** (~10 risks × likelihood, impact, severity, mitigation, owner/task) | Part 4, final subsection | **Factor 3 (MED)** — risk discipline signal | Ready to paste |
| **T6** | **Customer & Commercialization Pipeline** (active customers × stage, value, Phase II linkage; ~11 entries) | Part 7.2 | **Factor 4 (HIGH)** — direct support to 5%-weighted commercialization score | Ready to paste |
| **T7** | **Capabilities Comparison: SwiftCore vs PX4/ArduPilot/Auterion/ModalAI** (side-by-side, 8 rows; green highlight BST distinctive; ⚠ indicates differentiated risk closed) | Part 2.4 (Why Conventional Approach Is Structurally Limited) | **Factor 1 (MED-HIGH)** — converts prose claims to defensible comparison | Ready to paste |

**T1 Key Content:** 6 objectives with acceptance criteria (e.g., "SwiftCore RTA Kit v1.0 released; PVS/SMT-checked attitude envelope; 100% override rate on ≥1000-case adversarial corpus; flight-validated on ≥3 airframes").

**T2 Key Feature:** Demonstrates work plan covers all objectives; missing dots are red flag for reviewers.

**T3 Key Feature:** Cost breakdown by quarter (illustrative values total $1.275M across 8 quarters); explicitly matches NASA requirement. Notes that Y1Q3–Q4 and Y2Q2 will be heavier (flight test + board fabrication); Y2Q4 lighter.

**T4 Key Feature:** Named personnel with task-level LOE percentages. PI at 25% consistent with NASA Primary Employment requirement. ~1.5 FTE total, consistent with $1.275M budget.

**T5 Key Content (11 risks identified):**
- R1: FAA Part 108 final rule slip — align safety case to published NPRM + F3269-21 baseline
- R2: Custom-board SBC supply chain — maintain 3 candidates in parallel
- R3: EMASS-side (Nanoveu) funding slip — two-phase SOW, 5+ candidate modules
- R4: Supervisor over-conservatism — envelope tuning in HWIL Monte Carlo
- R5: JSBSim multirotor model fidelity — validate against EMASS Flight 4 dataset
- R6: Boulder winter weather — spread campaign, warm-weather fallback (Lakeland, Florida)
- R7: DOE Genesis timing slip — BST internal fallback (wildfire-airspace, volcano modules)
- R8: SwiftDeploy cybersecurity from OTA updates — signed binary chain, hardware-backed keys
- R9: PVS/SMT formal methods extend beyond Task 1 — scope to one envelope class
- R10: NASA Phase II contract start slip from assumed Aug 2026 — bridge under existing SOW
- R11: Partner aircraft availability — BST fleet breadth (S0, S2, S3, E2) makes internally executable

**T6 Key Customers (11 entries):**
- **EMASS / Nanoveu:** In flight (April 2026); $90K Phase I executed, ~$90K Phase II SOW
- **ADONIS:** Phase I closed Q2 2026; reference customer
- **NOAA AOC / Hurricane Hunters:** IDIQ in execution, 20-platform DO
- **Navy SBIR Phase II (Magnetometers):** In award negotiation
- **Navy STTR Phase II Option (Hazardous Wx):** Underway
- **AFWERX Hurricane Sampling:** Submitted
- **USFS Wildfire (S2):** Active (Sunny Slope demo Aug 2025)
- **USGS Mexico Volcano (S2):** Active deployment
- **DOE Genesis Mission (BNL):** Submitted May 2026; $336K if awarded
- **USSOCOM CRADA:** In drafting
- **By Light Mustang / Halo:** Active integration
- **NextTech Solutions / JFC Canada (Arctic):** S3 Ottawa demo June 2026; Whitehorse winter Nov 2026–Apr 2027

**T7 Key Differentiators:**
- 5-layer modular hierarchy vs. monolithic (PX4/ArduPilot/Auterion/ModalAI)
- WebAssembly memory-isolated sandbox (vs. process isolation only)
- ASTM F3269-aligned RTA with two-level supervisory chain (flight-proven April 2026)