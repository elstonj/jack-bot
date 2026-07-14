# BST Financial Health Overview

## ⚠️ CRITICAL DATA QUALITY ISSUES

**The following analysis is severely constrained by incomplete and fragmented data across sources:**

1. **QuickBooks P&L Report:** Only 2-day period (7/13–7/14/2026) with $10k in expenses; full monthly/quarterly view missing
2. **Project Code Mapping:** Significant mismatch between Asana project IDs (e.g., [001-14], [043-1]), QuickBooks transaction codes (e.g., 550-2, 301-3), and requested project codes (e.g., 024-05, 025-02, 026-04)
3. **Budget Documentation:** Most projects lack approved budget documents, contract CLINs, or period-of-performance details
4. **Single Large Project in QBO:** "Government Project" shows $4.49M invoiced with $3.22M outstanding AR, but cannot be disaggregated into component projects
5. **Incomplete Invoice Tracking:** QuickBooks data spans 2024–2026 but lacks consistent project-level GL coding

---

## Portfolio Summary (Based on Available Data)

| Metric | Amount | Data Quality |
|--------|--------|---------------|
| **Total Invoiced (All Sources)** | ~$20–25M (estimated) | ⚠️ Fragmented across multiple project codes |
| **Government Project Invoiced** | $4,490,094.28 | ✓ Well-documented in QBO |
| **Government Project Accounts Receivable** | $3,223,783.82 | ✓ 76 open invoices |
| **Total Expenses (QBO Gov't)** | $1,346,089.73 | ✓ Documented for gov't project only |
| **Net Position (Gov't Project)** | $3,144,004.55 | ✓ Documented for gov't project only |
| **Recent 2-Day Expenses** | $10,000.00 (materials) | ⚠️ Insufficient period for analysis |

---

## Key Findings by Priority

### 1. **URGENT: Accounts Receivable Management**

| Issue | Details |
|-------|---------|
| **Outstanding AR (Government Project)** | $3,223,783.82 across 76 invoices |
| **AR as % of Revenue** | 72% of total government contract revenue remains uncollected |
| **Risk Level** | **RED** — Significant cash flow exposure |
| **Recommendation** | Immediate AR aging analysis required; follow up on invoices >60 days past due |

---

### 2. **Data Integration Gaps Preventing Analysis**

The following **41 requested project codes lack sufficient data** for financial summary:

- **Codes with Asana tasks but no QBO mapping:** 024-01 through 024-12, 025-00 through 025-12, 026-01 through 026-09
- **Codes with QBO invoices but no budget docs:** 550-1, 550-2, 567-01, 904-12, and others
- **Portfolio/Aggregate codes unclear:** 004-00, 006-00 (appear to aggregate multiple sub-projects)
- **Proposed but incomplete:** 001-00, 010-1, 018-20, 023-11, etc.

**Impact:** Cannot produce company-wide financial overview with confidence in completeness.

---

### 3. **Projects Requiring Immediate Attention** 
*(Based on available data only)*

| Project Code | Name | Status | Issue | Action Required |
|--------------|------|--------|-------|-----------------|
| **001-00** | DTRA PLUMES (SBIR Phase I) | Proposed | No budget or contract award data | Confirm award status; obtain contract terms |
| **300-3** | 2026 IDIQ NOAA S0 Platforms | Active | Recently invoicing; 5-year contract | Monitor delivery schedule; track against IDIQ options |
| **301-3** | S0 Hurricane Phase II (NOAA) | Active | Large invoiced value; multiple deliveries outstanding | Confirm outstanding platform delivery schedule |
| **026-07** | Murphy's Pond CH₄ (Murray State) | Active | Contract expires 12/31/26 | Flight #4 scheduled late Aug/Sept 2026; confirm schedule |
| **Government Project (QBO)** | Unspecified | Active | $3.2M AR outstanding | Execute payment follow-up plan; age AR by invoice |

---

### 4. **Projects Completed/Archived** 
*(Clearing from active oversight)*

| Code | Name | Status | Notes |
|------|------|--------|-------|
| 025-07 | SBIR SMM DoD 22.4D | ✓ Closed Nov 2025 | Successfully completed; remove from active tracking |
| 200-11 | Persistence Demo (NASA) | ✓ Closed Nov 2025 | Live wildfire demo completed Aug 2025 |
| 200-14 | Adaptive Autonomy (NASA SBIR) | ✓ Closed Apr 2026 | SwiftCore module development completed |
| 400-5 | Runway Integrity/SMM Phase II | ✓ Closed Nov 2025 | Air Force contract completed successfully |
| 031-1 | S3 UMES | ✓ Completed Mar 2025 | Contract funding expired 5/31/26 |
| 032-1 | ND Air Deployed S0s | ✓ Completed Oct 2025 | Hurricane season deployment done |
| 035-1 | ADONIS (Unmanned Experts) | ✓ Completed Mar 2026 | All 5 flight test milestones completed |

---

### 5. **Revenue Pipeline & Near-Term Milestones** 
*(Where data available)*

| Project | Upcoming Milestone | Expected Invoice | Status |
|---------|-------------------|------------------|--------|
| **301-3** (NOAA S0 Hurricane) | Platform deliveries (26 base + 7 opt) | Ongoing through Aug 2026 | Active invoicing |
| **300-3** (2026 IDIQ NOAA) | 20 S0 platforms + 5-yr options | March–July 2026 (active) | Large contract, multiple delivery windows |
| **026-07** (Murphy's Pond) | Flight #4 (late Aug/Sept 2026) | Upon completion | On schedule |
| **550-1** (Navy Magnetometer) | Phase I Option (ends 9/28/26) | Ongoing through Sept 2026 | Active; Phase II proposal pending |
| **550-2** (Navy STTR Hazardous Weather) | Phase I completion + Option period extension | Ongoing through Jan 2027 | Extended via Mod P0010 |
| **024-04** (AF Runway Integrity) | Final validation/closeout | Completed (archived) | No further invoices expected |

---

### 6. **Cash Flow & Payment Trends**

| Indicator | Finding | Source |
|-----------|---------|--------|
| **Recent Payments Received** | Data incomplete; cannot assess trend | QBO P&L insufficient |
| **AR Aging** | $3.2M outstanding (Gov't Project); 76 invoices | QBO government.md |
| **Invoice Velocity** | Varies by project; NASA/NOAA projects invoicing regularly | QBO transaction data |
| **Payment Risk** | Government contracts typically slower; NOAA/Navy invoicing appears on track | Project summaries |
| **Estimated Days Sales Outstanding (DSO)** | ~260 days for Government Project (72% uncollected) | Calculated from AR/Revenue ratio |

**Recommendation:** Conduct immediate AR aging report; prioritize collection on invoices >90 days outstanding.

---

### 7. **Expense Tracking by Project** 
*(Severely Limited Data)*

| Project | Expenses Recorded | Status |
|---------|-------------------|--------|
| **Government Project (QBO)** | $1,346,089.73 | ✓ Tracked in QB system |
| **All Others** | Minimal/scattered in QB; most only invoiced, not expensed | ⚠️ Expense capture inconsistent |

**Finding:** BST is invoicing projects but appears to lack detailed expense tracking below the "Government Project" aggregate level. **Recommend implementing project-level GL coding and monthly expense reviews.**

---

## Required Data to Complete Analysis

To produce a **comprehensive company-wide financial health overview**, provide:

### 1. **QuickBooks Reconciliation**
- [ ] Full monthly P&L for 2024–2026 (current 2-day snapshot insufficient)
- [ ] Balance Sheet as of 2026-07-14 (current cash, AP, AR aging)
- [ ] Chart of Accounts with project GL mapping (identify why projects 024–026 lack QBO coding)
- [ ] Revenue recognition policy documentation

### 2. **Project Master Data**
- [ ] Master project list mapping all internal project codes (001–026, 200–567, etc.) to:
  - Asana project IDs
  - QuickBooks cost codes/classes
  - Contract numbers (SBIR, IDIQ, commercial, internal)
  - Period of performance
- [ ] CLIN breakdown for each government contract
- [ ] Approved budget vs. actual tracking template

### 3. **Budget & Contract Documentation**
- [ ] Complete budget documents for Projects 024–026, 200–300, 400–567
- [ ] Signed contracts or SOWs for all active projects
- [ ] Change order/modification logs for major contracts
- [ ] Milestone/deliverable completion status for each active project

### 4. **Accounts Receivable Detail**
- [ ] AR aging report (0–30, 30–60, 60–90, 90+ days)
- [ ] Invoice-level status (invoiced, partially paid, disputed, awaiting billing)
- [ ] Payment history by customer/contract for past 12 months
- [ ] Outstanding milestone billings or un-invoiced CLINs

### 5. **Expense Tracking**
- [ ] Project-level labor allocation (time tracking data)
- [ ] Detailed purchase order and expense reports by project
- [ ] Subcontractor/vendor invoices and allocations
- [ ] Travel, materials, and direct cost breakdowns

---

## Summary Risk Assessment

| Category | Risk Level | Comments |
|----------|-----------|----------|
| **Accounts Receivable** | 🔴 **RED** | $3.2M outstanding; 72% of government invoices unpaid; DSO ~260 days |
| **Project Data Integrity** | 🔴 **RED** | 41 project codes lack budget/contract mapping; QBO data fragmented |
| **Cash Flow Visibility** | 🟡 **YELLOW** | Large AR balance poses liquidity risk if payment delays persist |
| **Expense Tracking** | 🟡 **YELLOW** | Project-level expense capture inconsistent; need GL coding improvements |
| **Revenue Pipeline** | 🟢 **GREEN** | NOAA, Navy, NASA contracts invoicing regularly; pipeline appears healthy |
| **Contract Performance** | 🟢 **GREEN** | Completed projects closed on schedule; active projects tracking to milestones |

---

## Immediate Actions Required

1. **AR Management (Week 1)**
   - Generate detailed AR aging report for Government Project and all invoices >$10k
   - Contact customers with invoices >60 days outstanding
   - Establish weekly AR tracking dashboard

2. **Data Reconciliation (Week 2–3)**
   - Map all QuickBooks project codes to master project list
   - Audit Asana project IDs against QBO GL codes
   - Confirm contract CLINs and budget allocations

3. **Financial Reporting (Week 4)**
   - Compile complete monthly P&L for all 12 months of 2025 and YTD 2026
   - Generate per-project profitability summary (where data permits)
   - Produce cash flow forecast for next 6 months

4. **Ongoing (Monthly)**
   - Implement project-level GL coding in QuickBooks
   - Track actuals vs. budget by project and CLIN
   - Monitor AR aging and payment trends

---

**This overview is based on incomplete data. Full accuracy requires the supplemental documentation listed above.**