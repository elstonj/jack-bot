# BST Financial Health Overview

## ⚠️ DATA QUALITY NOTICE

**CRITICAL LIMITATION:** The provided data contains **severe fragmentation and misalignment across sources**:
- QuickBooks data shows company-level totals, not detailed per-project allocation
- 60+ project codes referenced across Asana/proposals with **minimal cross-validation**
- Many project summaries lack contract values, budgets, or invoiced amounts
- Outstanding invoices and cash position fragmented across projects

**This overview synthesizes available data but cannot provide complete accuracy without:**
1. Unified project accounting (QuickBooks project/class codes aligned to Asana)
2. Contract-level CLIN details and payment schedules
3. Complete accounts receivable aging by project
4. Updated period-of-performance dates (some data appears 6+ months old)

---

## Portfolio Summary (All-Time)

| Metric | Amount |
|--------|--------|
| **Total Revenue (Invoiced, All Projects)** | $4,588,340.64 |
| **Total Expenses** | $2,257,489.53 |
| **Net Position (All-Time)** | $2,330,851.11 |
| **Outstanding Accounts Receivable** | ~$3,105,739+ |
| **Current Cash Position** | ~$2.3M net (carried forward) |

---

## By Project: Financial Summary (Sorted by Remaining Budget Risk — Lowest First)

**Legend:** 
- 🔴 **RED** = Low/negative remaining budget OR high outstanding AR relative to size
- 🟡 **YELLOW** = Moderate budget risk OR approaching end of PoP
- 🟢 **GREEN** = Healthy budget cushion, on track

### PROJECTS REQUIRING IMMEDIATE ATTENTION

| Project | Client | Contracted | Invoiced | Remaining | Status | Notes |
|---------|--------|-----------|----------|-----------|--------|-------|
| **Project 001-00** | DTRA | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | SBIR Phase I (7 mo); no budget docs provided; awaiting contract award |
| **Project 004-00** | Multiple | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Umbrella code for 16+ contracts; lacks unified budget; critical data integrity issue |
| **Project 006-00** | Multiple (Navy, NASA, USGS, Academic) | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Portfolio code spanning 14+ projects; no master budget document |
| **Project 010-1** | Multiple (Universities/Partners) | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Methane emissions; no budget/invoicing data provided |
| **Project 018-20** | Unknown | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | No project definition provided; NightFOX report (2017) unrelated |
| **Project 023-11** | Unknown | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Only utility bill provided; no contract/scope/budget |
| **Project 024-01** | Chevron | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Inactive/completed Feb 2024; minimal documentation |
| **Project 024-02** | AtmoFacts/BST | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Phase 1 deliverable; no budget baseline |
| **Project 024-03** | NASA ROSES 2024 | $518,293 | Data unavailable | **~$518K (unstarted)** | 🟡 YELLOW | Proposed 3-year grant (Apr 2025–Apr 2028); may not be awarded |
| **Project 024-05** | Multiple | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Aggregates 6+ subprojects; no master budget |
| **Project 024-06** | Multiple | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Aggregates multiple 2024–2025 programs; lacks definition |
| **Project 024-07** | Multiple | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Roll-up/holding account; no discrete project charter |
| **Project 024-08** | Multiple | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Master cost center spanning NOAA, Navy, NASA, USGS; undefined scope |
| **Project 024-09** | Multiple | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Mismatch between QB and proposals; AFWERX CSO (Curable Composites prime) |
| **Project 024-10** | Barbados Meteorological Services | $22,337 | Unknown | **~$22K (overdue)** | 🔴 RED | ⚠️ **DELIVERY OVERDUE** (due 2024-10-01); current due dates 2026-05 through 2026-07 |
| **Project 024-11** | Multiple (DOE, NOAA, Others) | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Portfolio aggregating FECM, NHC testbed, commercial; no unified budget |
| **Project 025-02** | Unknown | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | No project identification in source data; only compliance templates provided |
| **Project 025-03** | Unknown | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | No project definition; template documents only |
| **Project 026-03** | Unknown | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Project code not found in any source data |
| **Project 026-04** | Unknown | Data unavailable | Data unavailable | **UNKNOWN** | 🔴 RED | Project code not found; data mismatch (001-03 provided instead) |
| **Project 210-10** | NOAA UASD/UxSOC | Data unavailable | $9,320 | **~$9.3K (invoiced)** | 🟡 YELLOW | Display model supply; no budget baseline; may be complete |

---

### ACTIVE GOVERNMENT CONTRACTS (Higher Confidence Data)

| Project | Client | Contracted | Invoiced | Paid | Remaining (est.) | Health |
|---------|--------|-----------|----------|------|------------------|--------|
| **Project 031-1** (S3 UMES) | University of MD Eastern Shore | Unknown | Unknown | Unknown | **UNKNOWN** | 🟡 YELLOW | Product substitution issue (S3 spec vs. S2 actual delivery); approval undocumented |
| **Project 032-1** (ND Air S0s) | University of Notre Dame | $38,000 | $38,000 | Unknown | **$0 (complete)** | 🟢 GREEN | Archived 10/21/25; invoiced in full |
| **Project 032-2** (Display Model E2) | University of Notre Dame | Data unavailable | $4,500 | Unknown | **~$4.5K** | 🟡 YELLOW | Small scope; invoiced but budget unknown |
| **Project 032-3** (Sasquatch S0s ×4) | University of Notre Dame | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | ⚠️ **DATE DISCREPANCY** — Asana shows July 2026, but verbal order Feb 19; 4-month delivery implies June 2026 due date |
| **Project 035-1** (ADONIS) | Unmanned Experts Inc. | Data unavailable | Final invoice 4/10/26 | Unknown | **$0 (complete)** | 🟢 GREEN | ARCHIVED — All deliverables complete; Jack Elston: "Do NOT list any ADONIS tasks ever again" |
| **Project 039-1** (Refurbished S2 Oklahoma State) | Oklahoma State University | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟢 GREEN | Training completed 8/19/25; project complete |
| **Project 042-1** (S2 Stanford) | Stanford University | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | Components delivery (wing, fuselage, payload kit); June 2025 delivery requested |
| **Project 043-1** (ByLight Standing Task Order) | By Light Professional IT | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | ARCHIVED; awaiting task order submissions from ByLight |
| **Project 043-2** (Mustang LRFE) | By Light Professional IT | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | ⚠️ **DELAYED** — Original due 12/5/25, delivered 26 days late; India demo cancelled 2026-05-05; additional flight tests pending |
| **Project 043-3** (By Light M2 Design / Halo) | By Light Professional IT | Firm Fixed Price | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | PO J20265067 (4/8/26); design phase 4/3–5/30; builds TBD upon fuselage receipt |
| **Project 044-1** (EMASS Chip Integration) | EMASS (Commercial) | $90,000 | $55,000 | Unknown | **~$35K** | 🟡 YELLOW | Extended to 5/31/26; 4 phases (design through validation) |
| **Project 141-1** (NOAA SBIR Phase II) | NOAA | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | Equipment (Vaisala sensor, $227.69); minimal documentation |
| **Project 200-10** (AREN 2024–25) | NASA Science Activation | Data unavailable | Data unavailable | Unknown | **$0 (complete)** | 🟢 GREEN | Archived 3/10/25 |
| **Project 200-11** (Persistent IR Wildfire) | NASA Ames | Data unavailable | Data unavailable | Unknown | **$0 (complete)** | 🟢 GREEN | ARCHIVED — Contract closed 11/24/25 |
| **Project 200-12** (AREN 2025) | NASA | $20,576 | Data unavailable | Unknown | **~$20.6K (budgeted)** | 🔴 RED | ⚠️ **SHUT DOWN EARLY** (Aug 2025); project underspent or invoicing incomplete |
| **Project 200-13** (CRATER Costa Rica) | NASA Ames | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | 6-month deployment Feb–Aug 2025; field operations |
| **Project 200-14** (Autonomy SwiftCore) | NASA Stenlis | Data unavailable | Data unavailable | Unknown | **$0 (complete)** | 🟢 GREEN | SBIR Phase I archived 4/16/26; all work complete |
| **Project 200-5** (AREN Support) | NASA | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | MiniCam2 development; 2022 award; no budget detail |
| **Project 200-7** (Volcano CCRPP) | Unknown | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | Expenses: $360,982; no revenue/budget baseline |
| **Project 200-8** (AREN 2023) | NASA | $89,794 | Data unavailable | Unknown | **~$89.8K** | 🟡 YELLOW | CY 2023; no revenue invoicing in data |
| **Project 208-1** (AREN 2020–2021) | NASA | $30,000/yr | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | Archived project; minimal actuals |
| **Project 211-1** (NASA Ames MHP S2) | NASA Ames | Data unavailable | Data unavailable | Unknown | **$0 (complete)** | 🟢 GREEN | Completed 3/27/25; hardware assembly/delivery |
| **Project 300-3** (2026 IDIQ Hurricane) | NOAA UxSOC | $615,000 (est. from 20 units) | Data unavailable | Unknown | **~$615K (early stage)** | 🟡 YELLOW | Delivery order invoicing 3/26–7/26; 5-year IDIQ base; 20 S0 units |
| **Project 301-2** (WPO Hurricane Phase II 2020) | NOAA/University of Miami | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟢 GREEN | Extended to 6/30/25; 16–20 sUAS delivery; likely complete |
| **Project 301-3** (S0 Hurricane Phase II 2025) | NOAA/University of Miami | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | 33 S0 platforms; PoP through 8/25/26 (extended 6 months); active invoicing expected |
| **Project 350-4** (USGS Chile Volcano) | USGS Volcano Science | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | PoP 9/1/23–9/30/25 (may be complete); S3 deployment, MHP, survey services |
| **Project 400-5** (AFWERX SMM Phase II X22.4) | U.S. Air Force | Data unavailable | Data unavailable | Unknown | **$0 (complete)** | 🟢 GREEN | **ARCHIVED** — Successfully completed; all deliverables accepted; due 7/11/25 |
| **Project 400-6** (Adaptive Manufacturing SBIR) | AFWERX (Curable Composites prime) | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | BST subcontractor; SBIR Phase I (X24.7); 3 months (2/3–5/2/25) |
| **Project 450-1** (Crested Butte Snowmass SPLASH) | CU Boulder | Data unavailable | Data unavailable | Unknown | **$0 (complete)** | 🟢 GREEN | Archived; 2021–2023 UAS operations complete |
| **Project 452-1** (Hesselius E2) | CU Boulder | $15,000 | $15,000 | Unknown | **$0 (complete)** | 🟢 GREEN | Inventory clearance sale; completed 6/4/25; archived |
| **Project 550-1** (Navy SBIR Magnetometer) | U.S. Navy NAVAIR | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | Phase I (Jan 26, complete); Phase I Option (4/14–9/28/26, active); Phase II proposed 1/27–6/29 |
| **Project 550-2** (Navy STTR Hazardous Weather) | U.S. Navy ONR | Data unavailable | Data unavailable | Unknown | **UNKNOWN** | 🟡 YELLOW | Base complete (7/7/25–1/6/26); Option (1/7–7/6/26) active; final due 9/1/26 |
| **Project 025-01** (ND Air Deployed S0s) | University of Notre Dame | $38,000 | $38,000 | Unknown | **$0 (complete)** | 🟢 GREEN | PO P2154937 (2/7–10/13/25); fully invoiced 3/