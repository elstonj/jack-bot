# BST Financial Health Overview

## ⚠️ CRITICAL DATA QUALITY NOTICE

**The provided per-project data is severely fragmented and incomplete.** Most project summaries lack essential financial information (contracted values, invoices, payments received, expenses). The QuickBooks company-level overview provides aggregate data, but project-level reconciliation is not possible with the available documentation.

**Key Issues:**
- Project codes are inconsistent across systems (e.g., 001-00, 024-01 through 026-11 in some lists; [001-2], [043-1], [550-1] in others)
- Many projects lack budget baseline, contract award letters, or approved CLINs
- QuickBooks actuals exist but are not reliably mapped to project codes
- Multiple projects appear to aggregate multiple sub-projects under single codes
- Several projects have no financial data at all

**Recommendation:** Before proceeding with cash management, profitability analysis, or forecasting, conduct a **data reconciliation audit** to establish:
1. Authoritative project code mapping (project code ↔ contract number ↔ accounting code)
2. Complete contract award data (value, CLIN structure, performance period)
3. Current invoice and payment status for all active projects

---

## Company-Level Financial Summary (QuickBooks)

| Metric | Amount | Note |
|--------|--------|------|
| **Total Revenue (Invoiced)** | $9,988,826.98 | Apr 5, 2024 – Nov 16, 2026 |
| **Total Expenses** | $3,915,778.59 | Bills + Purchases |
| **Net Income** | $6,073,048.39 | **61% margin** |

### Revenue by Customer Class
| Class | Revenue | Expenses | Net | % of Total |
|-------|---------|----------|-----|-----------|
| **Government** | $6,880,904.00 | $1,848,577.86 | $5,031,396.14 | 69% |
| **Commercial** | $3,083,803.62 | $251,239.13 | $2,832,564.49 | 31% |
| **BST Internal** | $24,119.36 | $1,815,961.60 | -$1,791,842.24 | — |

**Key Findings:**
- **Government contracts are the profit engine** (117 active invoices; 73% net margin)
- **Commercial projects are highly profitable** (92% margin; lower volume)
- **BST Internal shows a $1.79M deficit**, reflecting company overhead allocation

---

## Accounts Receivable at Risk: ~$5.79M+

| Category | Outstanding Balance | Status |
|----------|-------------------|--------|
| **Government Projects AR** | $5,762,294.82 | High — 117 open invoices |
| **Commercial Projects AR** | $24,579.28 | **CRITICAL** — Invoice #1779 (Aug 31, 2026) is **73+ days overdue** |
| **Total A/R at Risk** | ~$5.79M | **Requires immediate collection action** |

---

## Projects Requiring Immediate Attention

### 🔴 **CRITICAL: Commercial Invoice Overdue**
- **Project:** [Unidentified Commercial]
- **Invoice #1779** | Dated Aug 31, 2026 | Amount: $24,579.28
- **Days Outstanding:** 73+ (as of report date Oct 23, 2026)
- **Action Required:** Immediate follow-up on payment status and account settlement

### 🟡 **GOVERNMENT PROJECTS: Large A/R Balances**
Based on QuickBooks data, 117 government invoices remain unpaid totaling **$5.76M**. This is typical for government contracts (net 30–60 day payment cycles), but represents significant cash flow concentration risk:

| Project Code | Identified Name | Invoiced | Status |
|--------------|-----------------|----------|--------|
| **400-5** | AFWERX SBIR Phase II (SMM) | ~$X | Archived (July 2025) |
| **550-1** | Navy SBIR Magnetometer | Active | Phase I Option + Phase II Option |
| **550-2** | Navy STTR Hazardous Weather | Completed | Delivered Sept 1, 2026 |
| **301-3** | S0 Hurricane Phase II (NOAA) | ~$X | Active; 33 platforms being delivered |
| **300-3** | 2026 IDIQ (NOAA) | ~$X | Active; 54-unit delivery underway |
| **350-4** | USGS Volcano Monitoring | ~$X | Extension to Sept 30, 2025 |
| **200-14** | NASA Autonomy SBIR Phase I | Completed | Final payment received Apr 2026 |

**Key Risk:** Government payment delays are normal, but the $5.76M concentration in 117 invoices means:
- Negative working capital if all must be paid before collections
- Limited cash for operations/equipment if delays extend beyond net 60 days
- Recommend: Accelerate collections and model worst-case payment scenarios (net 90 days)

---

## Projects Near End of Contract Period / Requiring Close Monitoring

| Project | Contract End Date | Status | Risk |
|---------|-------------------|--------|------|
| **Project 018-1: Murphy's Pond (Murray State)** | Dec 31, 2026 | Active/Invoiced | Final payments must be collected by Dec 31 |
| **Project 301-2: WPO Hurricane Phase II (Univ. Miami/NOAA)** | June 30, 2025 | Expired | Contract performance period ended; verify final payment received |
| **Project 301-3: S0 Hurricane Phase II (NOAA)** | Aug 25, 2026 (6-mo ext) | Active | Delivery phase ongoing; monitor milestones |
| **Project 300-3: 2026 IDIQ (NOAA)** | June 1, 2027 | Active | 54-unit delivery phase underway; long-term contract (5 years through 2030) |
| **Project 350-4: USGS Volcano Monitoring** | Sept 30, 2025 | Expired | Contract end date passed; verify closeout and final invoice |
| **Project 400-5: AFWERX SBIR Phase II (SMM)** | July 2025 | Archived | Completed; verify final payment reconciliation |

---

## Active/High-Value Projects (from per-project data)

### Government Contracts (Strong Pipeline)

| Project | Client | Contract Type | Estimated Value | Status | Notes |
|---------|--------|----------------|-----------------|--------|-------|
| **300-3** | NOAA | 5-year IDIQ | $X (54 platforms) | Active Delivery | Multiple S0 systems; firm fixed price with T&M options |
| **301-3** | NOAA | S0 Hurricane Phase II | ~$X | Active Delivery | 33 platforms + operations; extension granted to Aug 2026 |
| **550-1** | Navy (NAVAIR) | SBIR Phase I → Phase II | $X (magnetometer) | Phase I Option Active | Transitioning to Phase II (Jan 2027 start if exercised) |
| **550-2** | Navy (ONR) | STTR Phase I | Completed Sept 2026 | Completed | Expendable air-sea profiling systems |
| **200-14** | NASA | SBIR Phase I | $X | Archived (Complete) | Autonomy/SwiftCore development; final payment Apr 2026 |
| **200-13** | NASA Ames | Phase III R&D | $X | Active | CRATER Costa Rica; forest ecosystem monitoring |
| **350-4** | USGS | Volcano Monitoring | $X | Expired (Sept 2025) | Verify closeout |

### Commercial Projects (Strong Margin)

| Project | Client | Value | Status | Notes |
|---------|--------|-------|--------|-------|
| **031-1** | UMES | $181,510 | Delivered | S3 VTOL system; training scheduled July 2026 |
| **032-1** | Notre Dame | ~$X | Completed Oct 2025 | 2× S0 systems for hurricane season |
| **032-3** | Notre Dame | $88,705 | Due July 1, 2026 ⚠️ | 4× Sasquatch S0 units (overdue status unclear) |
| **043-2** | By Light (DISA) | $X | Completed Dec 2025 | Mustang autopilot enablement |
| **043-3** | By Light | $X | Completed Oct 2026 | M2/Halo design & build (2 units) |
| **025-09** | NASA Ames | ~$X | Completed Oct 2024 | S2 CRATER Costa Rica |
| **044-1** | EMASS | $X (per-flight-day) | Completed Sept 2026 | E2 chip integration; 11-month project |

---

## Revenue Pipeline: Upcoming Milestones

### Near-Term (Q4 2026 – Q1 2027)
- **Project 300-3 (NOAA IDIQ):** Continued 54-unit delivery phase; large ARs expected to convert
- **Project 550-1 (Navy SBIR):** Phase II option expected to start Jan 2027 (if exercised)
- **Project 032-3 (Notre Dame):** 4× Sasquatch S0 units; status requires verification (due July 1, 2026 — **overdue**)
- **Project 018-1 (Murphy's Pond):** Final invoices before Dec 31, 2026 contract close
- **Project 025-03 (UMES S3):** Training scheduled July 23–25, 2026

### Medium-Term (2027–2028)
- **Project 550-1 (Navy SBIR Phase II):** If exercised, 30-month Phase II (Jan 2027 – June 2029)
- **Project 300-3 (NOAA IDIQ):** Multi-year contract continues through 2030; annual delivery orders expected

### Proposals/Programs Under Development (At Risk)
- **Project 024-03:** NASA ROSES wildfire susceptibility (Step 2 submission, 3-year PoP if awarded Apr 2025)
- **Project 025-07, 025-08:** Navy/Air Force SBIR programs (templates incomplete; proposal stage)
- **Project 026-01, 026-02:** Arctic Edge 2027, Navy STTR Phase II (status unclear)

---

## Cash Flow & Working Capital Concerns

### Current State
- **Strong Revenue:** $9.99M invoiced (2-year span)
- **Healthy Margins:** 61% overall; 73% government, 92% commercial
- **Significant A/R:** $5.79M outstanding (58% of total revenue invoiced)

### Key Risks
1. **Government Payment Delays:** $5.76M in 117 invoices (typical net 30–60 days, sometimes net 90)
2. **Overdue Commercial Invoice:** $24,579 at 73+ days overdue
3. **Project 032-3 Status Unknown:** $88,705 Sasquatch order (3+ months overdue from July 1 due date)
4. **Internal Costs High:** $1.81M BST Internal deficit suggests significant overhead not recovered through direct projects

### Recommendations
1. **Accelerate Collections:** Target $5.76M government A/R; model net 90-day scenarios
2. **Resolve Overdue Accounts:** Immediate follow-up on Invoice #1779 ($24,579) and Project 032-3
3. **Reconcile Project Codes:** Establish authoritative mapping to avoid future tracking errors
4. **Monitor Cash Burn:** BST Internal deficit of $1.79M suggests operational costs may not be fully allocated to projects
5. **Front-Load Approvals:** Secure Phase II exercisable options (Navy 550-1) and confirm NOAA IDIQ annual delivery orders

---

## Data Gaps Preventing Deeper Analysis

The following critical information is **missing or incomplete** across the project dataset:

| Data Element | Impact | Status |
|--------------|--------|--------|
| **Contract Award Letters** | Cannot verify contracted values, CLIN structure, or payment terms | ⚠️ Missing for most projects |
| **Invoicing Status** | Cannot reconcile invoiced vs. approved amounts | ⚠️ Partial (QBO only) |
| **Payment Receipts** | Cannot confirm cash-in-hand; relies on invoice dates only | ⚠️ Not provided |
| **Expense Breakdowns** | Cannot analyze project profitability or cost trends | ⚠️ QBO has only monthly totals |
| **Asana-to-QBO Reconciliation** | Project codes don't consistently map across systems | ⚠️ Multiple naming conventions |
| **Subcontractor Status** | Cannot track open POs, vendor payments, or liability | ⚠️ Limited visibility |
| **Budget vs. Actuals** | Cannot perform variance analysis or forecast completion | ⚠️ Incomplete budget docs |

---

## Recommended Next Steps

1. **Immediate (Week 1):**
   - Resolve overdue Invoice #1779 ($24,579; commercial)
   - Verify Project 032-3 (Notre Dame Sasquatch) status and payment
   - Generate current A/R aging report (government vs. commercial)

2. **Short-Term (Weeks 2–4):**
   - Reconcile all project codes across Asana, QuickBooks, and Drive budgets
   - Obtain full contract award packages for all active government projects
   - Create unified project master list with contract values, CLINs, performance periods, and payment terms

3. **Medium-Term (Month 2):**
   - Build project-level P&L (revenue vs. expenses) for all active/recent projects
   - Forecast cash collections by quarter for 2026–2027
   - Identify which projects are contributing to BST Internal $1.79M deficit

4. **Ongoing:**
   - Implement project code standardization
   - Establish monthly A/R review process (>60 days overdue flagged)
   - Monitor milestone achievement and revenue recognition against delivery schedules

---

**Report Date:** Based on data through October 23, 2026  
**Data Sources:** QuickBooks (Apr 5, 2024 – Nov 16, 2026), Asana, Drive Budget Docs, Proposals & Reports  
**Prepared by:** BST Finance