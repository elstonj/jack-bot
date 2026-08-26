# Acellent/Stanford (Fly-By-Feel) — Project History, Obligations, and Recommended Exit

## Document Metadata
- **Type**: Internal closeout report and negotiation brief
- **Client/Agency**: Stanford University Structures and Composites Laboratory (SACL); Acellent Technologies Inc.
- **Program/Solicitation**: "Fly-By-Feel" collaboration (angle-of-attack sensing from wing-surface sensors)
- **Date**: 20 August 2026
- **BST Products/Systems Referenced**: S0, S2, S3 VTOL aircraft; MultiScat (MHP—multi-hole probe); SwiftCore avionics; pneumatic launcher
- **Key Personnel**: Jack Elston (BST, author); Maciej Stachura (CTO); Cory Dixon (BST, recipient); Prof. Fu-Kuo Chang, Dr. Tanay Topac, Luis Backhaus, David Aharon (Stanford/SACL); Dr. Amrita Kumar, Cody Gray (Acellent)

---

## Executive Summary

Black Swift has maintained a five-year, three-generation aircraft relationship (S0 → S2 → proposed S3) with Stanford's Structures and Composites Laboratory and Acellent Technologies, invoicing only $18,847 total while providing substantial free engineering, hardware, and integration support since mid-2025. The relationship is governed by an unsigned-in-substance Memorandum of Understanding (2 June 2025) with no end date, cost cap, or payment terms. BST's outstanding obligation—conducting a flight test on an S2 airframe—is no longer feasible because the S2 is end-of-life and BST has no spare airframe. The report recommends a bounded closeout deliverable (Option A: one flight test with post-processed AoA data within 60 days of hardware arrival) in exchange for mutual discharge of the MOU, with fallback options if an airframe cannot be assembled.

---

## Technical Approach

### Historical Phases

**Phase 1 (2021–2022): S0 Purchase**
- Acellent PO'd one S0 aircraft (October 2021); BST delivered.
- Stanford conducted wind-tunnel campaigns; BST provided unbilled support (log file conversion, servo diagnostics).
- Total invoiced: $13,397.

**Phase 2 (April–September 2025): S2 Re-engagement**
- Stanford/Acellent requested an S2 loan for a Fly-By-Feel demonstration at IWSHM 2025 (9–11 September).
- BST shipped S2 fuselage + right wing with installed avionics and pitot-static air data probe (July 2025, invoiced at $0).
- Loaner display kit (left wing, 2× tail surfaces, tail boom, battery, battery cap) shipped August 2025 at $6,000 insured value; returned post-conference.
- MOU drafted 2 June 2025; IWSHM static display held 9–11 September 2025.

**Phase 3 (October 2025–August 2026): Drift**
- Oct 2025: Multi-hole probe (MHP) identified as critical path for obtaining angle-of-attack; BST offered to fit one for flight testing.
- Mar–Apr 2026: Extended free avionics debugging, firmware builds, and technical consultation.
- 28 Apr 2026: Topac proposed shipping fuselage and wing back to Boulder for flight test; no subsequent scheduling occurred.
- Jul 2026: Aharon requested S2 CAD for CFD; NDA gap discovered and closed.

### Technical Scope of the MOU (2 June 2025)

The memorandum obligates BST to:
1. **Receive and inspect** Stanford's modified fuselage and wing for serviceability.
2. **Conduct a flight test** with the Stanford-modified right wing and payload on an S2 airframe.
3. **Permit Stanford/Acellent personnel** (up to two people) to attend the flight test.
4. **Deliver post-processed AoA data**, specifically angle-of-attack, airspeed, and state-estimate theta, time-aligned, with interpretation of how their wing-surface sensors correlate to true angle-of-attack.

Stanford/Acellent committed to:
1. Complete mechanical integration on the purchased right wing only (done).
2. Perform electrical integration with autopilot (incomplete; blocked on BST flight test).
3. Validate AoA determination from sensors (incomplete; blocked on BST flight test).
4. Cover all shipping; cover damage or loss to BST equipment.
5. Return all loaner components promptly (completed August 2026).

---

## Products & Capabilities Described

### **S0 Aircraft**
- First-generation platform delivered to Acellent (October 2021).
- Used for Stanford wind-tunnel testing 2021–2022.

### **S2 Aircraft**
- Mid-generation fixed-wing platform; end-of-life as of July 2025.
- Described as "well-suited" to Stanford's hardware (sensor integration, payload interfaces).
- Configuration: twin-boom pusher with single fuselage, payload bay, CAN and DB9 avionics interfaces.
- **Current status**: No spare S2 airframes in inventory; S20009 sold to NASA; sourcing difficult; product line sunset.

### **S3 VTOL**
- Next-generation platform with VTOL capability; quoted but never PO'd.
- Estimated cost ~$60,000+ for two airframes (per expired Estimate 1366).
- Pneumatic launcher quoted at ~$19,000 (never converted).

### **SwiftCore Avionics**
- Autopilot/flight control stack installed in S2 fuselage shipped July 2025.
- Supports CAN and telemetry interfaces.
- Firmware customizable; custom FIXEDWING binary compiled for Stanford (April 2026).
- Multi-hole probe (MHP) is standalone on S2; does not talk to autopilot (does not provide real-time AoA feedback to flight control).

### **Multi-Hole Probe (MHP)**
- BST-owned hardware for obtaining true angle-of-attack from flight data.
- Provides pitching and angle-of-attack characterization (sampling rate, drift, stability over extended flights).
- Not shipped to Stanford; BST proposed fitting it to the test airframe for flight testing.
- Distinct from pitot-static air data probe (donated to Stanford July 2025 at $0; already in their possession).

### **Pitot-Static Air Data Probe**
- Installed in S2 fuselage and shipped to Stanford July 2025.
- Provides airspeed, altitude, and dynamic pressure only; **does not provide angle-of-attack**.
- Donated at $0; now Stanford property.

---

## Use Cases & Applications

### **Fly-By-Feel Wing Sensor Research**
- **Goal**: Validate that wing-surface pressure or strain sensors can infer angle-of-attack without traditional probes.
- **Application**: Reduced-sensor aircraft for cost/weight/complexity reduction in UAVs.
- **Venue**: IWSHM (International Workshop on Structural Health Monitoring) 2025, Stanford, 9–11 September (static demonstration completed).
- **Flight test objective**: Fly a wing instrumented with Stanford's sensors alongside a BST multi-hole probe; post-process both datasets and demonstrate correlation, allowing Stanford to validate their alpha-inference algorithm against ground truth.

### **Potential Commercial Extensions (never funded)**
- Two additional S2 aircraft ($19,967 for parts/completion, never PO'd; price now expired due to end-of-life status).
- Two S3 VTOL aircraft with launcher (Estimate 1366; never PO'd; requires re-pricing).
- Operator training (Estimate 1367: $3,000; never PO'd).
- Taiwan government UAV procurement teaming (2025, no solicitation materialized; zero revenue).

---

## Key Results & Current Status

### **Financial Summary**
- **Total revenue (lifetime, all accounts)**: $18,847 (0.10% of BST's $18M lifetime revenue).
  - Acellent S0 PO (Oct 2021): $13,397
  - Stanford PO 63769697 (Jun 2025): $5,000 (S2 wing + components)
  - Stanford PO 63989425 (Apr 2026): $450 (small parts/shipping)
- **Quoted but never converted**: ~$42,000–$60,000+ (S2 completion parts, S3 VTOLs, launcher, operator training).
- **Value given without invoice**: Avionics + pitot-static probe installation ($0 invoice, July 2025); loaner kit assembly/use ($6,000 insured hardware, Aug 2025); custom firmware (Apr 2026); SDK/avionics debugging (Oct 2025–Apr 2026); design consultation; wind-tunnel support.
- **Estimated engineering time**: Cannot be precisely quantified (no project code in Toggl); embedded in overhead accounts (001-12 Customer Support, 001-01 General IRAD). Likely several hundred hours over five years.

### **Deliverables Status**

| # | Deliverable | Delivered? | Paid? | Notes |
|---|---|---|---|---|
| 1 | S0 aircraft, complete | ✅ | Yes ($13,397) | Oct 2021 |
| 2 | Wind-tunnel log conversion + servo support | ✅ | No | 2021–2022, goodwill |
| 3 | S2 right wing + components | ✅ | Yes ($5,000) | Jun 2025 |
| 4 | Avionics + pitot-static probe + labor | ✅ | No ($0 invoice) | Jul 2025, donated |
| 5 | Loaner display kit (IWSHM) | ✅ Shipped & returned | No | Aug 2025, $6k kit |
| 6 | SDK, API, firmware, integration support | ✅ Ongoing | No | Goodwill |
| 7 | Custom FIXEDWING firmware | ✅ | No | Apr 2026 |
| 8 | Small 2026 parts/shipping | ✅ | Yes ($450) | 2026 |
| **9** | **Receive & inspect components** | ✅ | No | **MOU obligation—components returned** |
| **10** | **Flight test on S2** | ❌ | No | **MOU obligation—NOT FEASIBLE (S2 end-of-life, no spare airframe)** |
| **11** | **Permit Stanford/Acellent attendance** | ⏳ | No | **Contingent on #10** |
| 12–17 | Inspection, training, MHP characterization, CAD | ⚠️ ⏳ | No | Offered but not funded; partially answered |

**Stanford/Acellent's obligations**:
- Mechanical integration on purchased wing: ✅ Done
- Electrical integration: ⏳ Incomplete (blocked on BST flight test, not their action)
- AoA validation: ⏳ Incomplete (blocked on BST flight test, not their action)
- Shipping/damage coverage: ✅ Honored
- Return of components: ✅ Completed

---

## Notable Details

### **Relationship Dynamics & Negotiating Profile**

**Prof. Fu-Kuo Chang** (Stanford SACL Director, principal decision-maker):
- Asserts broader agreements than exist (e.g., conflating original scope with subsequent offers).
- Requests urgently and specifically ("please do so asap").
- Dangles future volume (2 more S2s, 2 S3 VTOLs, Taiwan program) against present free work; none converted.
- Escalates when blocked (e.g., "critically delaying" email, 23 Apr 2026, requesting next-day meeting; brought Prof. Chang directly into scheduling).
- Works to a sponsor (unfunded research program; decisions gated on funding not yet secured).

**Key tactical findings**:
1. **No written counterSignature**: The MOU is styled as "Meeting Notes" with no clear countersignature. It closes with "All parties acknowledge the scope and roles outlined above" —