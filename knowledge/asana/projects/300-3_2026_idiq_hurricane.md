# [300-3] 2026 IDIQ (Hurricane)

## Overview
- **Client/Customer:** NOAA (National Oceanic and Atmospheric Administration) — Uncrewed Systems Operations Center (UxSOC)
- **Dollar Value:** **$1,111,000 total IDIQ**
  - Original Delivery Order #1305M226F0084: $483,000 (20 UAS + 2 ground stations)
  - Option 2 (enacted August 5, 2026): 34 additional S0s, new funding $628,000
- **Contract Details:** 
  - IDIQ #1305M226D0012
  - Delivery Order #1305M226F0084 (original)
  - Additional POF0344 (Option 2)
  - Ongoing partnership since 2018 (SBIR Phase I 2018, Phase II 2019–2020)
- **Timeline:** 
  - **Original final delivery deadline: 2026-07-31** ✅ **PASSED — Project now in post-delivery invoicing phase**
  - **Current deliveries:**
    - 20 UAS for NOAA: Aug 2026 ✅
    - 13 S0s (Option 2): Due Oct 30, 2026
    - 21 S0s (Option 2): Due Nov 30, 2026 (option exercised 2026-08-05)
    - 30 S0s (additional, emerging): Due June 1, 2027
  - **Invoicing schedule:**
    - Original DO: Invoices 1–5 ✅ submitted; Invoice 6 ($72k) **due 2026-09-11**
    - Option 2 (POF0344): Invoice 1 ($58.5k) ✅ **submitted 2026-08-03**; Invoice 2 ($58.5k) **due 2026-09-14**; Invoice 3 ($117k) due 2026-10-05
- **Status:** **✅ ORIGINAL DELIVERY ORDER COMPLETE — Post-delivery invoicing in progress.** Ground station delivery completed 2026-07-29 (17 days late). All major firmware/hardware milestones now complete. **Option 2 ($628k, 34 S0s) is active scope with Oct 30 and Nov 30, 2026 delivery dates. Potential third tranch of 30 S0s emerging for June 1, 2027 delivery (not yet formalized in contracts).** Invoice 1 (POF0344) successfully submitted on deadline. Invoices 6 and 2 (POF0344) approaching critical deadlines.
- **Team Members:** 
  - **Meredith O'hara Needham** (project owner, invoice submissions)
  - **Jack Elston** (firmware/software)
  - **Sam Hild** (QC, hardware validation)
  - **Nate Straus** (platform rebuild, S0 builds, servo assembly)
  - **Maciej Stachura** (platform validation, magnetic calibration, parameter file validation)
  - **Josh Fromm** (GCS assembly, ground station delivery)
  - **Ben Busby** (web-based controller development)
  - **Nick Pawlenko** (UxSOC liaison) — transitioned to UxSOC HQ 5/29/26; UASD expanded team now handles operational coordination
- **Risk Signals:** 
  - ⚠️ **Original deadline 2026-07-31 passed; delivery completion delayed ~17–28 days on critical path items**
  - ⚠️ **Web-based controller due 2026-07-31 — STATUS UNKNOWN; confirm with Ben Busby**
  - ⚠️ **Invoice 6 deadline 2026-09-11** — critical path; final shipment documents required
  - ⚠️ **Invoice 2 (POF0344) deadline 2026-09-14** — imminent
  - ⚠️ **Multiple unassigned S0 build tasks** with no due dates or past-due dates (servo wiring, linkage construction, power switch builds) — may block Oct 30 and Nov 30 Option 2 deliveries
  - ⚠️ Option 2 adds $628k and 34 units with tight back-to-back delivery windows (Oct 30 and Nov 30, 2026)
  - ⚠️ Potential emerging scope (30 additional S0s, June 1, 2027) in project notes — not yet formalized; contract amendments/new delivery orders likely required

## Key Deliverables & Milestones

**Original Delivery Order (#1305M226F0084) — $483,000:**
- ✅ 20 UAS for NOAA (shipped Aug 2026)
- ✅ 2 rack-mount ground stations (delivered 2026-07-29, 17 days late)

**Option 2 (POF0344) — $628,000 (34 S0s total):**
- 13 S0s: due Oct 30, 2026
- 21 S0s: due Nov 30, 2026

**Potential Future Scope (not yet contracted):**
- 30 S0s: due June 1, 2027 (project due date listed in Asana; formalization pending)

**Invoice Schedule:**

| Invoice | Contract | Amount | Due Date | Status |
|---------|----------|--------|----------|--------|
| 1 of 6 | CLIN 1001 (DO F0084) | $36,000 | 2026-03-13 | ✅ Submitted |
| 2 of 6 | CLIN 1001 (DO F0084) | $54,000 | 2026-04-14 | ✅ Submitted |
| Travel | CLIN 1001 (DO F0084) | $18,000 | 2026-04-15 | ✅ Submitted |
| 3 of 6 | CLIN 1001 (DO F0084) | $54,000 | 2026-05-04 | ✅ Submitted (3 days early) |
| 4 of 6 | CLIN 1001 (DO F0084) | $72,000 | 2026-06-05 | ✅ Submitted 2026-07-02 (27 days late) |
| 5 of 6 | CLIN 1001 (DO F0084) | $72,000 | 2026-07-06 | ✅ Submitted 2026-07-02 (4 days early) |
| **6 of 6** | **CLIN 1001 (DO F0084)** | **$72,000** | **2026-09-11** | ⏳ **OPEN — Pending final shipment documents** |
| **1 of 3** | **POF0344 (Option 2)** | **$58,500** | **2026-08-03** | ✅ **SUBMITTED 2026-08-03** |
| **2 of 3** | **POF0344 (Option 2)** | **$58,500** | **2026-09-14** | ⏳ **OPEN — APPROACHING DEADLINE** |
| **3 of 3** | **POF0344 (Option 2)** | **$117,000** | **2026-10-05** | ⏳ **OPEN** |

**Hardware & Firmware Milestones (Original DO):**
| Task | Owner | Due Date | Status |
|------|-------|----------|--------|
| Hardware ship (SHOW s0's + tripods) | — | 2026-05-19 | ✅ Early |
| Deployment tube firmware finalization | Jack Elston | 2026-06-04 | ✅ 2026-07-16 (42 days late) |
| AP & PSNS firmware finalization | Jack Elston | 2026-