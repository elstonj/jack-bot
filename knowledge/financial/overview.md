# BST Financial Health Overview

## Portfolio Summary
| Metric | Amount |
|--------|--------|
| **Total Invoiced (All Projects)** | $7,448,665.62 |
| **Total Expenses** | $2,705,557.95 |
| **Net Income (Company-wide)** | $4,743,107.67 |
| **Accounts Receivable Outstanding** | ~$3,219,865.82 |
| **Outstanding Purchase Orders** | $4,509.50 |

---

## Company-Level Performance by Classification

### Revenue & Profitability by Project Class

| Class | Revenue | Expenses | Net Position | Margin | Status |
|-------|---------|----------|--------------|--------|--------|
| **Government** | $4,462,176.28 | $1,333,093.50 | $3,129,082.78 | **70%** | ✓ Highly Profitable |
| **Commercial** | $2,986,489.34 | $240,948.72 | $2,745,540.62 | **92%** | ✓ Highly Profitable |
| **BST Internal** | $17,894.36 | $1,131,515.73 | **-$1,113,621.37** | **-6,123%** | ⚠️ **CRITICAL LOSS** |

**Key Finding:** Company is operationally profitable at $4.7M, but **BST Internal project is a significant drain**, spending 63x more than it generates. This appears to be infrastructure/R&D overhead misclassified or under-billed.

---

## Projects Requiring Immediate Attention

### 🔴 CRITICAL: BST Internal Project
- **Net Loss:** -$1,113,621.37
- **Revenue:** Only $17,894.36
- **Expenses:** $1,131,515.73
- **Issue:** Massive cost center with minimal billable revenue
- **Action Required:** Review cost allocation, determine if this is strategic R&D or administrative overhead. Consider re-allocation to billable projects or establish internal charge-backs.

---

### 🟡 HIGH A/R BALANCE — CASH FLOW RISK

| Project/Class | Outstanding A/R | Invoice Count | Status |
|----------------|-----------------|----------------|--------|
| **Government Projects** | **$3,194,865.82** | 76 invoices | ⚠️ Very Large Balance |
| **EMASS Chip Integration [044-1]** | $25,000.00 | 1 invoice | ⚠️ Overdue |
| **Krateo Sky** | ~$10,800+ | Partial data | ⚠️ Partial data |
| **TOTAL A/R** | **~$3,219,865.82** | — | ⚠️ **HIGH RISK** |

**Cash Flow Concern:** $3.2M outstanding represents 43% of total invoiced revenue. Government invoices often have 30–60 day terms, but this volume requires active follow-up to avoid liquidity strain.

---

## Notable Completed/Archived Projects (Recently Closed)

These projects represent completed work with final invoicing:

| Project Code | Project Name | Client | Status | Final Revenue |
|--------------|--------------|--------|--------|----------------|
| **400-5** | Runway Integrity (SMM Phase II) | U.S. Air Force SBIR | ✓ Closed Nov 2025 | ~$XXX |
| **200-11** | Persistent IR Measurements (NASA Phase III) | NASA Ames | ✓ Closed Nov 2025 | ~$XXX |
| **025-07** | SMM DoD 22.4D SBIR | U.S. Air Force | ✓ Completed July 2025 | ~$XXX |
| **200-10** | 2024–25 Aeropod (AREN) | NASA | ✓ Completed March 2025 | ~$XXX |
| **031-1** | UMES S3 Delivery | University of Maryland | ✓ Completed May 2026 | Invoice pending training |
| **452-1** | Hesselius E2 (CU Boulder) | CU Boulder | ✓ Completed June 2025 | $15,000 |

---

## Active High-Value Projects (In Progress or Recently Active)

| Project Code | Project Name | Client | Contract Value | Status | Key Milestone/Risk |
|--------------|--------------|--------|-----------------|--------|-------------------|
| **300-3 / 550-2** | 2026 IDIQ Hurricane (NOAA UxSOC) | NOAA | **$25 units + 2 ground stations** | **In Production** | **Delivery Due: 2026-07-31** ⚠️ FIRM DEADLINE |
| **301-3** | S0 Hurricane Phase II 2025 | NOAA/Univ Miami | **~$XXX (IDIQ DO)** | In Execution | Extended to Aug 2026 |
| **024-04 / 025-07** | SMM Phase II (Air Force) | U.S. Air Force SBIR | **~$XXX** | Archived/Completed | Final reporting complete |
| **025-04** | DOE Methane Monitoring | DOE FECM | **~$XXX** | In Development | FluxMapper™ TRL advancement |
| **550-1** | Navy SBIR Magnetometer | NAVAIR | **30-month Phase II** | Phase I Option Active | Development ongoing; Phase II proposal submitted |
| **550-2** | Navy STTR Hazardous Weather | Office of Naval Research | **Phase I + Option Complete** | Final Report Due 9/1/26 | Expendable S0 VTOL development |
| **025-01 / 032-1** | ND Air-Deployed S0s | University of Notre Dame | $38,000 | ✓ Completed Oct 2025 | Archived successfully |
| **024-10** | Barbados S0 VTOL & Training | Barbados Met Services | $XXX (full funded) | Delivery Due July 2026 | Training scheduled July 1–4, 2026 |

---

## Revenue Pipeline: Upcoming Invoiceable Milestones

### Government Contracts (Near-Term)
1. **NOAA IDIQ (300-3, 301-3)** — S0 platform deliveries through July 2026
2. **Navy SBIR Magnetometer (550-1)** — Phase II development invoicing through June 2029
3. **Navy STTR Hazardous Weather (550-2)** — Final report due Sept 1, 2026
4. **DoD SMM Phase II (024-04)** — Completed; final closeout invoices issued

### Commercial/University Contracts (Upcoming)
1. **Barbados Meteorological Services (024-10)** — S0 delivery + training (July 2026)
2. **CU Boulder (various E2/S2 projects)** — Display models and simulators
3. **Notre Dame (032-3)** — 4x Sasquatch S0 units (expected ~June 2026 completion; verbal order, Asana notes production not yet started)

### NASA/Research Contracts (Ongoing)
1. **NASA ROSES 2024 Wildfire Susceptibility (024-03)** — 3-year Phase II through 2028
2. **NASA Phase III Persistent IR (200-11)** — Archived/Completed
3. **NASA AREN Science Activation (200-12)** — Archived/Completed Aug 2025

---

## Data Quality Issues & Recommendations

### Critical Information Gaps
1. **Project Codes 004-00, 006-00, 023-11, 024-05, 024-06, 024-07, 024-08, 024-09, 025-02, 025-03, 025-08, 025-09, 025-12, 026-02, 026-03, 026-04, 026-05, 026-06, 026-09** lack clear project identification, budget documentation, or formal scope definition in the source data.

2. **Asana vs. QuickBooks Mismatch:** Many project codes in QuickBooks do not correspond to distinct Asana projects, suggesting either:
   - Cost allocation/overhead codes rather than discrete projects
   - Archival/inactive codes with incomplete documentation
   - Invoicing structure that differs from project management structure

3. **BST Internal Project (Profit Center Issue):** The $1.1M net loss requires immediate clarification:
   - Is this internal R&D / IRAD (Investment in Research & Development)?
   - Are costs being improperly allocated vs. billed?
   - Should overhead be distributed across revenue-generating projects?

### Recommendations for Next Steps
1. **Reconcile QuickBooks project codes with Asana project structure** — ensure 1:1 mapping where possible
2. **Clarify BST Internal project cost allocation** — establish charge-back mechanism or consolidate under billable projects
3. **Implement weekly A/R aging report** — address $3.2M outstanding with collections focus on government invoices
4. **Establish project closure procedures** — ensure archived projects have final invoices and expense reconciliation
5. **Develop forward-looking cash flow forecast** — integrate NOAA IDIQ ($25 units) delivery timeline with payment terms

---

## Summary: Company Health Assessment

| Factor | Status | Notes |
|--------|--------|-------|
| **Profitability** | ✓ Strong | $4.7M net income; 64% overall margin |
| **Revenue Concentration** | ⚠️ High Risk | 60% from Government; 40% from Commercial; dependency on government contracts |
| **Cash Flow** | 🔴 At Risk | $3.2M A/R outstanding (43% of invoiced revenue); payment terms likely 30–60 days |
| **Project Portfolio** | ⚠️ Mixed | Strong government pipeline (Navy, NOAA, Air Force); data quality issues in internal allocation |
| **Cost Structure** | 🔴 Problem Area | BST Internal project ($1.1M loss) requires immediate intervention |
| **Upcoming Major Deliverables** | ⏰ Time-Sensitive | NOAA IDIQ due 7/31/26 (25 units); Barbados S0 training 7/1–4/26 |

**Bottom Line:** BST is operationally profitable with a strong government customer base, but faces **cash flow pressure** from high A/R balances and must address the **BST Internal cost center loss** to optimize financial health.