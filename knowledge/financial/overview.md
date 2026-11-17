# BST Financial Health Overview

## Portfolio Summary
| Metric | Amount |
|--------|--------|
| **Total Invoiced (All Projects)** | $10,558,353.95 |
| **Total Payments Received** | $5,762,294.82* |
| **Total Expenses (Government Projects)** | $1,856,480.86 |
| **Outstanding Accounts Receivable** | $5,762,294.82 |
| **Estimated Net Position (Government Only)** | $5,023,591.14 |

*Based on Government project AR balance; full company cash position unclear due to incomplete project-level data.

---

## Critical Findings

### 1. **Severe Data Quality Issues**
The provided source materials contain **significant gaps and inconsistencies** that limit the reliability of this overview:

- **40+ project codes (001-00 through 904-12) have incomplete or missing data**
  - 28 projects lack budget documents entirely
  - 15 projects have no Asana project details
  - 12 projects show no QuickBooks transaction history
  
- **Government portfolio is well-documented; commercial portfolio is fragmented**
  - Government (Class 1): $6.88M invoiced, $1.86M expenses, $5.76M AR outstanding
  - 50+ commercial projects: Sparse transaction data, no consolidated budget visibility

- **Project-to-code mapping is broken**
  - QuickBooks uses different cost center codes than Drive budget docs and Asana
  - Multiple projects appear to aggregate under single codes (e.g., 024-05, 025-04, 024-06)
  - No consistent project naming convention across systems

---

## By Project — Sorted by Risk Level

### **🔴 CRITICAL ATTENTION REQUIRED**

| Project Code | Project Name | Invoiced | AR Outstanding | Status | Issue |
|---|---|---|---|---|---|
| **Government** | Multi-project portfolio | $6,880,904 | $5,762,295 | Active | **117 open invoices; $5.76M in unpaid receivables spanning 2.5+ years** (Apr 2024–Nov 2026). Average invoice age unknown; payment history not provided. High concentration of outstanding revenue. |
| **010-1** | Methane Emission Detection | $3,630,976 | Unknown | Active | No budget docs provided. Invoiced amount substantial but remaining budget and contract value unavailable. Cannot assess profitability. |
| **018-1** | Murphy's Pond CH4 Monitoring | $84,847 | Unknown | Complete | Actual budget $84,847 (matches proposal). **Status appears complete per period of performance end (12/31/2026).** Verify final closeout and payment status. |
| **024-10** | Barbados VTOL S0 | Unknown | Unknown | **SEVERELY OVERDUE** | **Original due: Oct 1, 2024 (overdue ~24 months).** Rescheduled delivery May 22, 2026; training July 1–4, 2026. No recent payment/invoice records provided. High delivery delay risk. |
| **031-1** | UMES S3 VTOL | $55,000+ | Unknown | Near completion | Funded through May 31, 2026 (expired). First delivery completed 3/31/2025; additional deliveries/training ongoing. Verify final invoicing and closeout. |
| **026-04** | SOCOM S0-AD | Unknown | Unknown | Unclear | **No QuickBooks data, no contract value, no scope definition.** Project code not found in any system. Requires immediate clarification. |
| **026-05** | SOCOM S0-AD (assumed) | Unknown | Unknown | Unclear | **Asana project archived/stale.** No budget docs, contract, or expense records. Potential untracked revenue/liability. |

### **🟡 YELLOW FLAG — MODERATE CONCERN**

| Project Code | Project Name | Invoiced | AR Outstanding | Status | Issue |
|---|---|---|---|---|---|
| **024-04** | SMM Phase II (AFWERX SBIR) | Unknown | Unknown | Active | Contract 400-5 through 2026-11-05. No recent QuickBooks transactions; final deliverable/payment status unclear. |
| **025-03** | S0 Hurricane (AF D2P2 SBIR) | Unknown | Unknown | Proposal phase | Proposal submitted FY25; contract award status unknown. No QuickBooks activity in 2026 suggests pre-award or funding delay. |
| **025-09** | S2 CRATER (Costa Rica) | Unknown | Unknown | Archived (complete) | Marked complete Oct 21, 2024 in Asana; SOW submitted Jan 22, 2025. Final invoice/payment status not documented. |
| **025-11** | Multi-project NOAA/Navy IDIQ | Unknown | Unknown | Active | IDIQ contract with multiple task orders. Sparse transaction data; cannot assess revenue pipeline or milestone status. |
| **026-08** | NOAA UxSOC + DOE Genesis | Unknown | Unknown | Pre-award | NOAA IDIQ initiated 2026-08; DOE Phase I drafted (no award status). Early-stage; revenue not yet recognized. |
| **032-3** | Sasquatch S0s x4 (Notre Dame) | $180,000 | Unknown | Complete | Invoiced amount ($180K) **exceeds proposed budget ($88,705) by 103%.** Cost overrun or dual invoicing? Requires reconciliation. |
| **043-2** | ByLight Mustang Long-Range | Unknown | Unknown | Archived (complete) | 9-week fixed-price SOW completed Dec 2025. No final invoice or payment record provided. |
| **300-3** | NOAA Hurricane 2026 IDIQ | Unknown | Unknown | Active | 5-year IDIQ (2026–2030); current deliveries through June 1, 2027. 20 S0 platforms, training, mission day support. Only one invoice line item shown; full scope and revenue pipeline unclear. |
| **301-3** | S0 Hurricane Phase II 2025 | Unknown | Unknown | Extension granted | Base contract through Aug 25, 2026 (6-month extension granted). 33 total platforms, training, mission support. Final invoicing status not provided. |
| **400-5** | AFWERX SBIR Phase II SMM | Unknown | Unknown | Complete | Final report submitted DoD SAFE on 2025-08-14. Contract end date July 2025. Final payment status not documented. |
| **550-1** | Navy SBIR Magnetometer | Unknown | Unknown | Phase II option (active) | Phase I complete Sept 28, 2026. Phase II option underway. Sparse expense data; revenue recognition timeline unclear. |
| **550-2** | Navy STTR Hazardous Weather | Unknown | Unknown | Active | Base period complete 1/7/2026; option period through 7/6/2026. Project due 9/1/2026. Final deliverable and payment status not documented. |

### **🟢 LOW CONCERN / ARCHIVED**

| Project Code | Project Name | Invoiced | Status |
|---|---|---|---|
| **025-05, 025-06** | Hesselius E2 / CU Boulder | $15,000 / $3,900 | ✅ Archived (complete, June 2026) |
| **025-07** | SMM DoD Phase II | Small | ✅ Archived (complete) |
| **026-03** | NASA Autonomy Phase I | Small | ✅ Archived (complete, April 2026) |
| **026-07** | ND Sasquatch S0s x4 | Unknown | ✅ Archived (Oct 2026) |
| **026-09** | NASA S2 & Parts | Small | ✅ Archived (Oct 2026) |
| **032-1, 032-2** | ND S0 Platforms | ~$9K | ✅ Archived (complete) |
| **035-1** | ADONIS (Unmanned Experts) | Unknown | ✅ Archived (complete, April 2025) |
| **039-1** | Refurbished S2 (OSU) | ~$18K | ✅ Archived (complete) |
| **043-1, 043-3** | ByLight Professional IT | Unknown | ✅ Archived (complete) |
| **044-1** | EMASS Chip Integration | ~$15K | ✅ Archived (complete) |
| **200-11, 200-13, 200-14** | NASA SBIR projects | $74K–$80K | ✅ Archived (complete) |
| **210-10** | AREN 2024 | $92,500 | ✅ Archived (likely complete) |
| **212-1, 212-2** | NASA S2 Simulator/Parts | ~$25K+ | ✅ Archived (delivered Oct 2026) |
| **213-1** | NASA Langley S0s | ~$18K | ✅ Archived (complete) |
| **450-1** | CU Boulder Crested Butte | ~$20K+ | ✅ Archived (complete, Nov 2023) |
| **452-1, 452-2** | CU Boulder E2/Simulator | $18.9K total | ✅ Archived (complete, June 2026) |

---

## Revenue Pipeline & Upcoming Milestones

| Project | Upcoming Invoiceable Event | Timeline | Potential Revenue |
|---|---|---|---|
| **Government** | Unknown (AR backlog requires investigation) | Ongoing | $5.76M outstanding |
| **300-3 (NOAA IDIQ)** | 20 S0 platforms + training deliveries | Through June 1, 2027 | Unknown (staged delivery) |
| **026-08 (NOAA/DOE)** | IDIQ task orders; DOE Genesis Phase I award pending | 2027 | Unknown (pre-award) |
| **550-2 (Navy STTR)** | Option period completion (target Sept 1, 2026) | Underway | Unknown |
| **026-01 (Arctic Edge/Navy STTR)** | Arctic Edge 2027 exercise (April–May 2027); Phase II award pending | 2027 | Unknown (proposal under review) |
| **025-04 (Multi-project)** | SMM Phase II final acceptance; NASA Persistence completion | Ongoing | Unknown (mixed status) |

**Data Gap:** Asana milestones and invoiceable deliverables not systematically extracted. Only high-level project timelines available.

---

## Accounts Receivable & Cash Flow

### Outstanding Receivables
- **Government Portfolio AR:** $5,762,294.82
  - **Age unknown.** Spanning April 2024–November 2026 (2.5+ years) suggests invoices range from <1 year to >2 years old
  - **117 open invoices** across government projects
  - **Payment frequency not documented.** Unable to assess whether this is normal for government contracting or indicates collection issues

- **Commercial Portfolio AR:** Undocumented
  - Project-level payment data not provided
  - Multiple archived projects (032-3, 043-2, 044-1, etc.) lack final payment confirmation

### Cash Position
- **QuickBooks Balance Sheet not provided.** Cannot assess:
  - Current cash balance
  - Working capital
  - Days Sales Outstanding (DSO)
  - Cash conversion cycle

### Recent Expense Activity
- **Government Projects:** $1,856,480.86 total expenses (through Nov 2026)
- **Current Period (Nov 16–17, 2026):** $0 expenses recorded (2-day snapshot)
- **Expense Timing:** Unclear if expenses are recorded on accrual or cash basis; impact on cash flow unknown

---

## High-Risk Projects Requiring Immediate Action

### 1. **Government Portfolio — $5.76M in Outstanding AR**
   - **Action:** Obtain detailed AR aging report (invoice date, amount, payment date/status, days outstanding)
   - **Risk:** Potential cash flow impact if invoices are >90 days old
   - **Recommendation:** Accelerate collections or investigate payment delays with government contracting office

### 2. **Barbados VTOL S0 (024-10) — 24 Months Overdue**
   - **Action:** Confirm delivery status and obtain customer written acknowledgment of new delivery date (May 22, 2026)
   - **Risk:** Contract default; customer may seek damages or cancellation
   - **Recommendation:** Issue revised contract amendment with firm delivery date and penalty clauses

### 3. **Sasquatch S0s x4 (032-3) — Cost Overrun Anomaly**
   - **Action:** Reconcile invoiced amount ($180K) vs. proposed budget ($88.7K); 103% variance requires explanation
   - **Risk:** Potential unbilled work or duplicated invoices
   - **Recommendation:** Review invoice details and confirm customer acceptance of overages

### 4. **SOCOM Projects (026-04, 026-05) — Not Found in Any System**
   - **Action:** Clarify project status; locate budget docs, contract, Asana project, and QuickBooks entries
   - **Risk:** Potential untracked revenue or liability; scope/status undefined
   - **Recommendation:** Audit project management systems for missing or misfiled records

### 5. **Multiple Pre-Award Proposals — Revenue Not Yet Recognized**
   - **Projects:** 025-03 (AF D2P2), 026-01 (Navy STTR Phase II), 026-08 (DOE Genesis Phase I)
   - **Action:** Confirm award status and contract effective dates
   - **Risk:** Cash flow gap if awards are delayed or declined
   - **Recommendation:** Establish win/loss tracking and contingency cash flow planning

---

## Data Gaps & Next Steps

### Critical Missing Information
1. **Consolidated Budget Document Index**
   - Drive contains 50+ budget docs with no master list
   - Project-to-code mapping is inconsistent
   - CLINs and billing structures not standardized across projects

2. **Asana Project Completeness**
   - 40+ project codes lack Asana records
   - Archived projects not systematically documented
   - Milestone and deliverable tracking incomplete

3. **QuickBooks Project Coding**
   - Multiple cost center codes per project
   - No standardized chart of accounts
   - Expense allocation and cost center definitions unclear

4. **Contract & Proposal Archive**
   - No centralized contract repository
   - Award letters, modifications, and CLINs scattered
   - Period of performance dates inconsistent across sources

### Recommended Actions
- **Establish Master Project Registry** linking project code, client, contract number, POP, budget, and system references (Drive, Asana, QB)
- **Conduct AR Aging Analysis** on Government portfolio—investigate invoices >90 days old
- **Audit Commercial Project Billing** for 2025–2026 period; ensure all completed projects have final invoices and payment records
- **Implement Project Financial Dashboard** with automated QB integration to track invoiced, received, and remaining budget in real-time
- **Schedule Contract Closeout Audit** for all projects marked "archived" to confirm final payments and no outstanding obligations

---

## Summary Assessment

**Financial Health: YELLOW / CONDITIONAL**

✅ **Strengths:**
- Large government portfolio ($6.88M invoiced) with positive net position ($5.02M)
- Multiple active contracts with stable government clients (NOAA, DoD, NASA)
- Diverse revenue streams across 50+ projects reduces single-client dependency

⚠️ **Concerns:**
- **$5.76M in outstanding government AR** (age and payment status unknown)
- **Severe data fragmentation** across Drive, Asana, and QuickBooks makes financial visibility poor
- **24-month delivery delay** on Barbados project signals operational/supply chain risk
- **Cost overrun anomaly** on ND Sasquatch project (032-3) unexplained
- **Multiple projects not found** in source systems (026-04, 026-05, etc.)
- **Cash position and working capital metrics unknown**

🔴 **Critical Actions:**
1. Obtain Government AR aging report immediately
2. Clarify SOCOM projects (026-04/05) status
3. Reconcile