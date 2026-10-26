# BST Financial Health Overview

## ⚠️ CRITICAL DATA QUALITY ISSUE

**The provided per-project data contains severe inconsistencies and gaps that prevent a reliable company-wide financial overview.** The QuickBooks export shows only **$24,119.36 in total revenue** against **$1.81M in expenses**, but individual project summaries reference **$8.2M+ in invoiced amounts** across multiple projects. This fundamental reconciliation failure indicates:

1. **Data fragmentation** — Multiple source systems (QuickBooks, Asana, Drive Budget Docs, Proposals) are not synchronized
2. **Project code mapping failures** — Many project codes (025-01 through 025-12, 026-08, etc.) have no corresponding financial data
3. **Missing invoice records** — Most active projects show invoiced amounts in project summaries but these do NOT appear in the consolidated QuickBooks company totals

**Recommendation:** Before proceeding with business decisions, reconcile:
- QuickBooks general ledger with individual project invoicing records
- Asana project budgets with actual contract values
- All outstanding AR by project

---

## Portfolio Summary (Based on Consolidated QB Data)

| Metric | Amount | ⚠️ Data Status |
|--------|--------|---|
| **Total Contracted Value (All Projects)** | $8,230,173.29 | Extracted from project summaries; NOT in QB totals |
| **Total Invoiced (QB Only)** | $24,119.36 | Company-wide QB figure (severely understated) |
| **Total Received (Payments)** | Unknown | QB AR shows $24,119.36 outstanding (uncollected) |
| **Total Expenses (QB)** | $1,809,603.50 | 31-month period (Apr 2024 – Nov 2026) |
| **Estimated Remaining** | Unknown | Cannot calculate without reliable invoice data |

---

## Projects Requiring Immediate Attention

### 1. **CRITICAL: Cash Position vs. Deficit**
- **QB Net Position:** -$1,785,484.14 (company operating at $1.79M loss)
- **AR Outstanding:** $24,119.36 (100% of QB revenue uncollected)
- **Cash Burn Rate:** ~$58,400/month average over 31 months
- **Status:** 🔴 **RED** — Unsustainable without external funding or immediate revenue acceleration

### 2. **Projects with High Invoiced Amounts (Need Payment Verification)**

| Project | Invoiced | Status | Issue |
|---------|----------|--------|-------|
| **[300-3] NOAA IDIQ** | $2,772,959.00 | Active | 5-year contract; verify payment schedule and AR aging |
| **[301-3] S0 Hurricane Phase II 2025** | $844,449.61 | Active | Large NOAA contract; confirm cash collection |
| **[550-1] Navy SBIR Magnetometer** | $905,016.00 | Transitioning Phase I→II | Transitional risk; ensure Phase II funding secured |
| **[035-1] ADONIS** | $1,249,945.00 | Archived (Apr 2026) | Project complete; verify final invoice payment |
| **[400-5] AFWERX SBIR Phase II (SMM)** | Not explicitly stated | Archived | Unclear final status; no payment data provided |

### 3. **Projects with Low/Uncertain Revenue Recognition**

| Project | Invoiced | Budget | Gap | Risk |
|---------|----------|--------|-----|------|
| **[026-05] ByLight M2/Halo** | $126,629 | $126,629 | Flat | 🟡 YELLOW — Project complete; verify acceptance |
| **[024-04] AFWERX SMM Phase II** | Unclear | ~$1.2M (inferred) | Unknown | 🟡 YELLOW — Budget/actual mismatch in data |
| **[200-13] CRATER** | $120,000 | Not stated | Unknown | 🟡 YELLOW — Archived; confirm final payment |
| **[550-2] Navy STTR Hazardous Weather** | Unclear | Not stated | Unknown | 🔴 RED — Phase I/Option complete; Phase II proposal status unclear |

### 4. **Projects with Outstanding Milestones (Uninvoiced Work)**

| Project | Scope | Expected Invoice | Risk |
|---------|-------|-------------------|------|
| **[212-2] NASA S2 & Parts** | Refurbishment + spare parts | Overdue (due 9/30/2026) | 🔴 RED — Delivery deadline passed; invoice status unknown |
| **[026-09] Same (duplicate?)** | Same scope | Same deadline | Reconciliation needed |
| **[550-1] Navy SBIR Magnetometer** | Phase II proposal submitted | Jan 2027 (if awarded) | 🟡 YELLOW — No Phase II award confirmation yet |
| **[200-12] AREN 2025** | Educational outreach | Ongoing (through 2025) | 🟡 YELLOW — Budget $117,701.50; invoiced only $92,500 |

---

## Cash Flow Analysis

### Accounts Receivable Status
- **QB AR Total:** $24,119.36 (100% of recognized QB revenue outstanding)
- **High-Value Projects (AR Status Unknown):**
  - NOAA IDIQ ($2.77M) — Payment terms/aging unknown
  - Navy SBIR Magnetometer ($905K) — Phase transition risk
  - S0 Hurricane Phase II ($844K) — Government payment delays likely
  - ADONIS ($1.25M) — Archived; final payment status unclear

### Recent Expense Activity
- **Oct 5–12, 2026:** $73,982.13 (elevated spending period)
- **Oct 12–Nov 2, 2026:** $3,999.75 (moderated spending)
- **Trend:** Spending declining but still unsustainable vs. revenue

### Collections Pipeline (Estimated)
Based on project status, assume 60–90 day government payment cycles:

| Period | Estimated Revenue | Likelihood |
|--------|-------------------|-----------|
| **Current (Oct–Nov 2026)** | $24,119 | 🟡 Low (already outstanding) |
| **Q4 2026** | Unknown | 🟡 Depends on NOAA/Navy invoicing |
| **Q1 2027** | $905K (if Navy Phase II awarded) | 🔴 Uncertain — Phase II contract not confirmed |

---

## Revenue Pipeline

### Approved but Uninvoiced Work
1. **[550-1] Navy SBIR Phase II** — Proposal submitted; Phase II contract value unknown; startup Jan 2027 (if awarded)
2. **[550-2] Navy STTR Phase II** — Proposed (status unclear); would follow Phase I completion
3. **[300-3] NOAA IDIQ Remaining Orders** — 5-year contract with significant remaining task orders; backlog unknown

### Upcoming Deliverables (Q4 2026 – Q1 2027)
- **[212-2] NASA S2 & Parts** — Overdue (30+ days past 9/30/2026 deadline)
- **[026-09] NASA S2 & Parts (Duplicate?)** — Same status
- **[200-13] CRATER** — Archived; final invoice status unclear
- **[200-14] NASA Autonomy** — Completed April 2026; final invoice should be closed

---

## Key Financial Risks & Recommendations

### 🔴 CRITICAL (Immediate Action Required)

1. **Liquidity Crisis**
   - **Finding:** $1.79M cumulative loss with minimal cash inflow
   - **Action:** 
     - Verify QB AR aging; prioritize collection of $24,119.36 + any unrecorded invoices
     - Forecast 90-day cash runway; identify external funding sources
     - Review recurring expense categories; identify cost reduction targets

2. **Data Reconciliation Failure**
   - **Finding:** QB totals ($24K revenue) vs. project summaries ($8.2M invoiced) do not match
   - **Action:**
     - Conduct full QB-to-Asana-to-Drive reconciliation
     - Identify missing invoice records in QB
     - Consolidate all AR and verify collection status by project

3. **Government Payment Delays**
   - **Finding:** $4.5M+ in active government contracts (NOAA, Navy, NASA, Air Force) with typical 60–90 day payment cycles
   - **Action:**
     - Establish AR aging report by contract
     - Follow up on NOAA IDIQ payment schedule
     - Secure Phase II contract awards for Navy programs before Phase I closeout

### 🟡 HIGH PRIORITY (Next 30 Days)

4. **Project Transition Risk (Navy Programs)**
   - **Finding:** [550-1] Magnetometer transitioning Phase I→II; [550-2] STTR Phase I complete; Phase II status unclear
   - **Action:**
     - Confirm Navy Phase II contract awards
     - Ensure continuity of funding between phases
     - Prepare Phase II proposals if not already submitted

5. **Overdue Deliverables**
   - **Finding:** [212-2]/[026-09] NASA S2 refurbishment due 9/30/2026; current date is 10/23/2026
   - **Action:**
     - Confirm project status (complete/in-progress)
     - Invoice immediately upon delivery
     - Establish recovery plan if delivery is delayed

6. **Duplicate Project Records**
   - **Finding:** Multiple project codes map to same scope (e.g., [025-05]/[025-06] Hesselius E2; [026-06]/[026-07] ERAU Model S0; [026-09]/[212-2] NASA S2)
   - **Action:**
     - Consolidate duplicate project codes in QB and Asana
     - Create unified AR aging report
     - Eliminate reporting ambiguity

### 🟠 MEDIUM PRIORITY (Next 60 Days)

7. **Budget vs. Actual Tracking**
   - **Finding:** Many projects have incomplete budget documentation; expense tracking is unreliable
   - **Action:**
     - Complete Drive Budget Docs for all active projects
     - Establish monthly budget-vs-actual review discipline
     - Flag projects with >10% budget variance

8. **Commercial Project Performance**
   - **Finding:** Several small commercial equipment sales ([024-08] ERAU, [024-10] Barbados, [031-1] UMES) with modest invoicing ($2.5K–$88K range)
   - **Action:**
     - Verify all invoices are collected
     - Identify cross-sell/upsell opportunities
     - Establish maintenance/support revenue pipeline

---

## Summary Dashboard

| Category | Status | Value |
|----------|--------|-------|
| **Company Net Position** | 🔴 RED | -$1,785,484 |
| **Monthly Cash Burn (Avg)** | 🔴 RED | ~$58,400 |
| **AR Aging (QB)** | 🔴 RED | $24,119 (100% outstanding) |
| **Government Contract Backlog** | 🟡 YELLOW | $4.5M+ (payment timing uncertain) |
| **Active Projects** | 🟡 YELLOW | 30+; 40% have data gaps |
| **Critical Deliverables Overdue** | 🔴 RED | 1 project (NASA S2, 23 days overdue) |

---

## Immediate Next Steps

1. **By EOD 10/24/2026:** Pull aged AR report by project; contact NOAA, Navy, NASA for payment status
2. **By 10/31/2026:** Reconcile QB revenue totals to project invoicing records; identify missing $8.1M in QB
3. **By 11/7/2026:** Confirm NASA S2 delivery status and invoice accordingly
4. **By 11/14/2026:** Present 90-day cash flow forecast to leadership; identify funding gaps
5. **By 11/30/2026:** Complete budget documentation for all active projects; establish monthly variance tracking