# BST Financial Health Overview

## ⚠️ CRITICAL DATA QUALITY ALERT

**The company-wide financial health overview cannot be reliably generated from the provided data sources.** The documentation exhibits systematic gaps that prevent accurate portfolio-level analysis:

### Primary Data Limitations:
1. **QuickBooks Export (2-day period only):** Nov 11-12, 2026 shows $129.32 expenses, $0 revenue — unrepresentative of actual operations
2. **Project Code Fragmentation:** 50+ project codes with inconsistent naming, budgeting, and status tracking across Asana, QuickBooks, Drive, and Proposals
3. **Missing Contract Values:** Majority of projects lack approved budgets, CLINs, or contract award documentation
4. **Incomplete Invoice Data:** QuickBooks export truncated (Invoice 1772 details cut off); no full AR aging report provided
5. **Inactive/Archived Projects:** Significant portion of project codes marked complete or archived; unclear which represent active revenue streams

**Recommendation:** Reconcile data sources before generating company-wide financial summaries. Request:
- Full QuickBooks P&L, Balance Sheet, and A/R aging (full fiscal year)
- Master project code mapping with client, contract value, and status
- Consolidated budget vs. actuals by project

---

## Portfolio Summary (Based on Available Data)

| Metric | Amount | Notes |
|--------|--------|-------|
| **Total Invoiced (Visible Projects)** | **~$4.1M+** | Commercial project ($3.08M) + select other projects; incomplete data |
| **Total Expenses (Visible)** | **~$251K–$500K+** | Commercial project expenses only; many projects lack expense detail |
| **Total Accounts Receivable** | **$24,579+ (minimum)** | Murphy's Pond CH4 (Invoice 1779, Aug 31, 2026 — **2.5+ months outstanding**) |
| **Estimated Remaining (all projects)** | **CANNOT CALCULATE** | Insufficient budget data across portfolio |

---

## Projects Requiring Immediate Attention

### 🔴 **RED — Aging Accounts Receivable**
| Project | Invoice # | Customer | Amount | Days Outstanding | Status |
|---------|-----------|----------|--------|-------------------|--------|
| **[018-1] Murphy's Pond CH4** | **1779** | Murray State University | **$24,579.28** | **~75 days** | **OVERDUE** — invoice dated Aug 31, 2026; no payment recorded as of Nov 12 |

**Action Required:** Immediate collection follow-up with Dr. Bassil El Masri (belmasri@murraystate.edu, 270-809-3110). Funding expiration December 31, 2026 — verify funds remain available.

---

### 🟡 **YELLOW — High-Risk Projects (Overdue Deliverables / Budget Pressure)**

| Project Code | Project Name | Client | Issue | Status |
|--------------|--------------|--------|-------|--------|
| **[024-08]** | ERAU VTOL S0 | Embry-Riddle | **OVERDUE** — original delivery Aug 2024; revised May 2025 unfulfilled | 5 unassigned critical tasks; revised delivery now 6+ months overdue as of Nov 2026 |
| **[025-04]** | S0 Hurricane Phase II / NASA SBIR | Multiple | **Data commingling** — portfolio vs. project unclear; multiple funding streams | High activity but unclear budget status |
| **[024-06]** | Portfolio aggregator | Multiple | **50+ sub-projects** — appears to be cost center rather than discrete project | No unified budget or contract document provided |
| **[200-7]** | Volcano CCRPP | Unknown | **$360K+ invoiced** but no contract/budget docs; client unknown | Significant revenue without documented approval |

---

### 🟡 **YELLOW — Projects Approaching End-of-Performance**

| Project | Deadline | Days Remaining (as of Nov 12, 2026) | Status |
|---------|-----------|---------------------------------------|--------|
| **[018-1]** Murphy's Pond CH4 | Dec 31, 2026 | **49 days** | Active; AR aging issue (see above) |
| **[301-2]** WPO Hurricane Phase II | Jun 30, 2025 | **EXPIRED** (since June 2025) | No status note; project may be closed |
| **[350-4]** USGS Chile Volcano | Sep 30, 2025 | **EXPIRED** (since Sept 2025) | May be archived |
| **[026-11]** ERAU Model S0 | Jun 25, 2026 | **EXPIRED** (since June 2026) | Marked for archival per Oct 27 directive |

---

## Revenue Pipeline (Upcoming Invoiceable Milestones)

**LIMITATION:** Asana project data provided does not include detailed milestone/deliverable timelines. Based on available project records:

### Active/Recent Projects with Ongoing Delivery:
1. **[300-3] NOAA sUAS Operations (2026 IDIQ)** — 5-year indefinite contract; 20 platforms delivered; 21-platform option exercised Aug 2026; 30 platforms planned 2027 → **Ongoing revenue stream**
2. **[026-08] NOAA UxSOC (Master IDIQ)** — Data-as-a-Service for UAS operations; SOW created Aug 30, 2026 → **Early-stage; invoice timeline unknown**
3. **[301-3] S0 Hurricane Phase II 2025** — 26 S0 aircraft + training; extension granted to Aug 25, 2026 → **May be near completion**
4. **[200-13] CRATER (Costa Rica, NASA)** — Completed Aug 20, 2025; may be invoicing final deliverables
5. **[025-03] S0 Hurricane Phase II (Air Force D2P2 SBIR)** — 24-month program; timeline not specified → **Status unclear**

### Projects with Approved but Potentially Un-Invoiced CLINs:
- **[550-1] Navy SBIR Magnetometer** — Phase II under negotiation (Jan 2027 start proposed); Phase I completed Sept 2026
- **[550-2] Navy STTR Expendable Air-sea Profiling** — Final report due Sept 1, 2026; option period completed July 6, 2026 → **May be awaiting final invoicing**
- **[400-5] AFWERX SBIR Phase II (Soil Moisture Mapping)** — Period of performance ended July 2025; final report submitted Aug 2025 → **Likely complete**

---

## Cash Flow Analysis

### Accounts Receivable (AR) — Known Positions:
- **Outstanding Total (minimum):** $24,579.28
  - Murphy's Pond CH4 (Invoice 1779): $24,579.28 — **75 days outstanding**, at risk of non-payment if funding not released before Dec 31, 2026
- **Likely Additional AR:** Multiple projects show invoices but payment status not provided in truncated QuickBooks export

**Recent Payment Trends:** Not available — QuickBooks extract limited to 2-day period (Nov 11-12, 2026) with no payment detail.

### Cash Conversion Analysis:
- **Commercial Project:** $3.08M invoiced; $2.83M net position (expenses ~$251K) → **Strong cash position** but no payment timeline visible
- **Multi-Project Portfolio:** Total invoiced likely $4M+; net position **indeterminate** without complete expense and payment data

### Facility & Unallocated Expenses:
- **Shop Supplies (Nov 2026):** $90.28 (Facilities, not allocated to project)
- **Direct Material:** $36.54 (not allocated to project)
- **Shipping:** $2.50
- **Total Unclassified:** $129.32 in 2-day period

**Implication:** Overhead allocation and cost tracking to projects is incomplete; true project profitability cannot be calculated.

---

## Critical Projects by Remaining Budget (Lowest First)

**NOTE:** This ranking cannot be completed accurately — majority of projects lack approved contract values in provided documentation. Listed below are projects with visible data:

| Project | Client | Invoiced | Estimated Contract | Remaining | Health |
|---------|--------|----------|-------------------|-----------|--------|
| **[025-05]** Hesselius E2 (CU Boulder) | University of Colorado | $15,000 | $15,000 | $0 | ✅ Complete |
| **[026-11]** ERAU Model S0 | Embry-Riddle | $2,462.50 (est.) | $2,462.50 | $0 | ✅ Complete (Archived) |
| **[026-05]** ByLight M2/Halo | By Light | $126,629 | $126,629 | $0 | ✅ Complete (Archived) |
| **[018-1]** Murphy's Pond CH4 | Murray State | $84,847 (contracted) | $84,847 | **TBD** | 🟡 YELLOW — AR aging + deadline |
| **[024-03]** NASA ROSES Wildfire | NASA | ~$518K (proposed) | $518,293 | Unknown | Unknown — no invoicing data |
| **[300-3]** NOAA IDIQ Hurricane | NOAA | ~$1M+ (est.) | Indefinite | Ongoing | 🟢 GREEN — Active, multi-year |

---

## Company-Level Financial Health Assessment

### Positive Indicators:
✅ **Strong Historical Revenue:** $3M+ invoiced on Commercial project alone; additional $1M+ across other visible projects  
✅ **Diversified Government Revenue:** NASA, NOAA, Air Force, Navy, USGS active contracts  
✅ **Recurring/Indefinite Contracts:** NOAA IDIQ (2026–2030), NOAA UxSOC (ongoing), Navy STTR Phase II options  
✅ **Commercial Growth:** Barbados, ERAU, By Light, CU Boulder, Oklahoma State, Stanford procurement activity  

### Risk Indicators:
🔴 **Aging AR:** $24.5K+ outstanding for 2.5+ months; single customer concentration risk  
🔴 **Delivery Schedule Slippage:** ERAU S0 overdue by 18+ months; 5 unassigned critical tasks  
🔴 **Data Integrity:** 50+ project codes; majority lack budgets, contracts, or expense tracking  
🔴 **End-of-Performance Compression:** Multiple projects expiring or expired (June–Dec 2025); pipeline for 2026–2027 unclear  
🔴 **Incomplete Financials:** QuickBooks export inadequate for company-wide P&L analysis  

---

## Recommendations

### Immediate (Next 30 days):
1. **AR Collections:** Contact Murray State University (Dr. Bassil El Masri) regarding Invoice 1779 ($24,579, 75 days outstanding). Verify funding remains available before Dec 31, 2026 deadline.
2. **Project Status Reconciliation:** Map all 50+ active project codes to:
   - Asana project records (milestones, deliverables, delivery dates)
   - QuickBooks invoices and expenses (financial actuals)
   - Drive budget documents (contract values, CLINs, approved budgets)
   - Proposal/award letters (client approval & period of performance)
3. **ERAU S0 Delivery Crisis:** Escalate unresolved ERAU VTOL S0 project (18+ months overdue). Clarify revised May 2025 commitment status; assign resources to unassigned critical tasks.

### Medium-term (60–90 days):
4. **Full Financial Extraction:** Request complete QuickBooks export (full fiscal year P&L, Balance Sheet, A/R aging detail, check register) for accurate cash flow and profitability analysis.
5. **Project Health Dashboard:** Create consolidated project status report (one row per project) showing:
   - Contract value (approved budget)
   - Invoiced to date
   - Expenses incurred
   - Outstanding AR
   - Period of performance (start/end dates)
   - Health status (Green/Yellow/Red)
6. **Cost Allocation:** Reclassify unallocated facility expenses ($129+) and indirect costs to projects for true project-level P&L.

### Long-term (Strategic):
7. **Revenue Pipeline Planning:** Document all proposal submissions (Stage, $, Timeline, Client) to forecast 2027–2028 revenue and identify pipeline gaps.
8. **Contract Portfolio Optimization:** Identify high-risk/low-margin projects and consider escalation or termination; focus resources on profitable, expanding contracts (NOAA, NASA, Air Force).
9. **Data Governance:** Implement integrated project-financial system (Asana-to-QuickBooks linkage) to eliminate manual reconciliation and ensure real-time budget variance visibility.

---

**This overview is based on incomplete data. Reliable company-wide financial health assessment is not possible without full QuickBooks financials and consolidated project budget documentation.**