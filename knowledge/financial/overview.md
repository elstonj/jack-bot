# BST Financial Health Overview

## Portfolio Summary
| Metric | Amount |
|--------|--------|
| **Total Invoiced (All Projects)** | $5,730,757.62 |
| **Total Expenses** | $1,526,809.04 |
| **Net Income (Estimated)** | $4,203,948.58 |
| **Total Accounts Receivable** | $2,633,164.17+ |
| **Outstanding Purchase Orders** | $2,410.50 |

### Revenue Composition
- **Government Contracts:** $3,900,918.28 (68% of revenue) — 72 active invoices
- **Commercial:** $1,829,839.34 (32% of revenue) — 3 transactions

---

## Critical Data Quality Issues

**⚠️ WARNING: This portfolio summary is severely limited by incomplete data provision.**

The analysis is constrained by:
1. **Missing project-level budgets** — Drive Budget Docs contain only consolidated company financials and utilities; individual project budget baselines unavailable for 30+ project codes
2. **Unmatched project codes** — Asana projects, QuickBooks invoices, and project codes frequently do NOT align (e.g., project code 024-05 shows Asana data for [001-13] Marketing Goals)
3. **Incomplete financial records** — QuickBooks export truncated for 2026-04-24 to 2026-04-25; vendor names and expense categories not fully provided
4. **Missing contract documentation** — CLINs, approved contract values, periods of performance, and scope details unavailable for majority of projects
5. **Fragmented data** — Multiple projects described as "aggregates" of sub-projects with no cost allocation detail

**Recommendation:** Before acting on any of the findings below, request complete data alignment: Asana project roster with QB project codes, full budget baseline spreadsheet, and contract register with CLINs and authorized amounts.

---

## Projects Requiring Immediate Attention

### 1. **Project 026-06 (Murphy's Pond CH₄ Monitoring)** — 🔴 RED
**Status: AT RISK — Critical timing and budget issues**

| Metric | Value |
|--------|-------|
| Invoiced to Date | $27,318.77 |
| Invoiced (2026) | $27,318.77 |
| S2 Rental Due | June 1, 2026 |
| Original Due Date | January 31, 2025 (PASSED) |
| Field Campaigns | 3 planned (May, July, August 2026) |
| Budget Documentation | None provided |

**Issues:**
- Project significantly past original due date (Jan 31, 2025); currently executing May–August 2026 flights
- No budget baseline available to assess overage or remaining contract value
- Upcoming S2 rental expense (June 1, 2026) not yet reflected in actuals
- Cannot determine if project is profitable or over budget without contract value

**Action Required:** Provide contract value, CLINs, and approved budget for Murphy's Pond. Clarify whether extension was formally approved and if additional funding was authorized.

---

### 2. **Project 010-1 (Methane Emission Detection)** — 🔴 RED
**Status: NO BUDGET BASELINE — Cannot assess financial health**

| Metric | Value |
|--------|-------|
| Invoiced to Date | $3,404,632.27 |
| Expenses Shown | $3,404,632.27 (data truncated) |
| Approved Budget | Data not available |
| Contracted Value | Data not available |
| Margin | Cannot calculate |

**Issues:**
- Large invoiced amount ($3.4M) with zero documented budget
- Expense total equals invoiced amount (suggesting data was truncated or incomplete)
- No contract documentation provided
- Impossible to determine if project is profitable, at-risk, or already over budget

**Action Required:** Provide complete contract terms, approved CLINs, and budget baseline for Project 010-1 immediately. Clarify actual expense detail (appears truncated).

---

### 3. **Project 026-2 (NOAA S0 IDIQ — 2026-2030)** — 🟡 YELLOW
**Status: MAJOR DELIVERY COMMITMENT — Monitor closely**

| Metric | Value |
|--------|-------|
| Contract Value | $26.2M (estimated, 5-year IDIQ) |
| Invoiced to Date | Not segregated in QB actuals |
| Delivery Requirement | 20 S0 units, July 31, 2026 |
| Magnetometer Calibration | Required (new capability) |
| Firmware Upgrades | Required (Vaisala RH sensors) |
| Period of Performance | 2026–2030 |

**Issues:**
- Largest contract in portfolio by value ($26.2M / 5 years)
- **Critical delivery deadline: July 31, 2026** (approximately 2 months from data date)
- Requires new integration capabilities (magnetometer calibration, Vaisala firmware) not yet evidenced in project records
- QB actuals do not segregate NOAA IDIQ invoices; cannot track spend against contract value
- No Asana project data or milestone tracking provided

**Action Required:** 
- Confirm 20-unit delivery schedule and resource allocation
- Verify magnetometer and firmware upgrades are on track for July 31 deadline
- Establish separate QB cost code for NOAA IDIQ tracking
- Provide detailed project plan with critical milestones through contract completion

---

### 4. **Project 006-00 (Navy SBIR Magnetometer Portfolio)** — 🟡 YELLOW
**Status: MULTI-PROJECT PORTFOLIO — Insufficient detail to assess**

| Metric | Value |
|--------|-------|
| Invoiced (QB actuals) | $X (not segregated) |
| Projects Included | Navy SBIR, NASA, USGS, commercial |
| Period of Performance | Ongoing (2026-04-15 through 2026-09-28 in records) |
| Budget Documentation | Provided only as consolidated overview; no line-item breakdown |

**Issues:**
- Aggregates 5+ distinct projects (Navy SBIR magnetometer, Navy STTR hazardous weather, NASA autonomy, volcano monitoring, hurricane/coastal) under single code
- No individual project budgets or contracted values provided
- Cannot assess financial health of individual efforts
- Invoicing and expense data commingled across multiple clients and funding sources

**Action Required:** Disaggregate Project 006-00 into separate QB cost codes for Navy SBIR, NASA, USGS, and commercial work. Provide individual contract values and budget baselines.

---

### 5. **Project 024-10 (Barbados VTOL S0 and Training)** — 🔴 RED
**Status: PAST DUE — Critical delivery dates at risk**

| Metric | Value |
|--------|-------|
| Original Due Date | October 1, 2024 (PASSED) |
| S0 VTOL Handoff | May 1, 2026 (CRITICAL) |
| Training Delivery | July 1–4, 2026 (CRITICAL) |
| Customer | Barbados Meteorological Services |
| Budget Status | Data not available |
| Invoiced to Date | Not provided |

**Issues:**
- Original project due date has passed (Oct 1, 2024) with no evidence of completion or re-baselining
- Two imminent critical milestones: S0 handoff (May 1) and training (July 1–4)
- No budget data provided; cannot assess cost performance
- Customer contact information provided but no recent status update in Asana or QB records

**Action Required:**
- Confirm current status of S0 VTOL delivery and training logistics
- Verify contract allows extension beyond Oct 1, 2024 deadline
- Provide updated schedule and budget forecast to completion
- Confirm training logistics (6 trainees, NetCDF data generation setup)

---

### 6. **Project 032-3 (Sasquatch S0s x 4 for Notre Dame)** — 🔴 RED
**Status: SCHEDULE DISCREPANCY — Critical clarity needed**

| Metric | Value |
|--------|-------|
| Verbal Order Placed | February 19, 2026 |
| Stated Delivery Timeline | 4 months (→ ~June 19, 2026) |
| Asana Start/Due Dates | July 1, 2026 (both) — **INCONSISTENT** |
| Proposed Budget | $88,705 |
| Invoiced to Date | Not provided |
| Customer | David Richter, Notre Dame |

**Issues:**
- **Critical discrepancy:** Verbal order implies June 19 delivery; Asana shows July 1 for both start and due dates (likely data entry error)
- Budget amount provided but no contract/PO documentation
- Only 4 units (Sasquatch S0) to be produced in <4 months; aggressive timeline
- No invoice or milestone tracking in QB actuals

**Action Required:**
- Clarify actual delivery deadline immediately with Jack Elston
- Confirm whether Asana dates (July 1) or verbal timeline (June 19) is correct
- Provide PO or formal contract for Sasquatch order
- Update Asana with correct schedule and milestones

---

## Projects with High Outstanding Invoices (Accounts Receivable)

### Government Accounts Receivable: **$2,632,499.19**

**Major contributors (inferred from large invoiced amounts):**

| Project | Invoiced | Notes |
|---------|----------|-------|
| **Project 010-1** (Methane) | $3,404,632.27 | Invoiced amount equals total expenses; AR not disaggregated in QB |
| **Project 301-3** (S0 Hurricane Phase II) | Large (not itemized) | 26 base + 7 optional units; invoicing ongoing through Aug 2026 |
| **Project 550-1** (Navy SBIR Magnetometer) | $X | Ongoing through Sept 28, 2026 |
| **Project 550-2** (Navy STTR Hazardous Weather) | $X | Final deliverable due Sept 1, 2026 |
| **Projects 200-7, 200-13, 200-14** (NASA) | Combined $500K+ | CRATER, Autonomy, and other NASA projects |

**Commercial Accounts Receivable: $664.98+** (at minimum)
- Invoice #1759 to IRISS, CU Boulder (amount: $664.98)
- ND Air Deployed S0s (Project 032-1): Potential additional AR if not fully paid

**Action Required:**
- Reconcile QB AR aging report (not provided)
- Identify top 10 overdue invoices by amount and days outstanding
- Implement collection plan for invoices >60 days
- Verify payment status for Projects 301-3 and 550-1 (large government contracts)

---

## Approved/Upcoming Invoiceable Milestones (From Asana & Proposals)

### Imminent Milestones (Next 60 Days)

| Project | Milestone | Target Date | Invoiceable Amount |
|---------|-----------|-------------|-------------------|
| **026-07** (NOAA IDIQ) | 20 S0 units delivery | July 31, 2026 | $26.2M (est. 5-year IDIQ) |
| **024-10** (Barbados) | S0 VTOL handoff | May 1, 2026 | TBD (budget unavailable) |
| **032-3** (Notre Dame Sasquatch) | 4-unit delivery | ~June 19, 2026 | $88,705 |
| **026-06** (Murphy's Pond) | Field Campaign 1 (May) | May 2026 | TBD (contract value unknown) |
| **024-10** (Barbados) | Training delivery | July 1–4, 2026 | TBD (training costs) |
| **550-2** (Navy STTR) | Final deliverable | Sept 1, 2026 | TBD (Phase I complete; Option underway) |

### Medium-Term Milestones (60–180 Days)

| Project | Milestone | Target Date | Status |
|---------|-----------|-------------|--------|
| **301-3** (S0 Hurricane Phase II 2025) | 26 base units delivery | Aug 25, 2026 | Ongoing manufacturing |
| **043-2** (By Light Mustang) | G2 prototype completion | ~Dec 31, 2025 (PASSED) | Extended; current status unclear |
| **043-3** (By Light M2 Design) | 2 Halo airframes ready | May 30, 2026 (Scope 1); June 2026 (Scope 2) | Design phase active |
| **026-09** (Navy SBIR + Clear Air) | Various (not detailed in Asana) | Through 2026-09-28 | Final reporting phase |

**Action Required:**
- Reconcile Asana milestones against QB invoice schedule
- Confirm which approved deliverables remain uninvoiced
- Identify CLINs/contract line items that can be invoiced upon milestone completion
- Set up monthly tracking of milestone status vs. revenue recognition

---

## Cash Flow Assessment

### Current Accounts Receivable Exposure
- **Total A/R:** $2,633,164.17
- **Government A/R:** $2,632,499.19 (99.97% of total)
- **Commercial A/R:** $664.98 (0.03% of total)
- **A/R as % of Total Invoiced:** 45.9% — **Very High**

**Interpretation:** BST has invoiced $5.73M YTD but collected only ~54% ($3.1M est.). Heavy reliance on government payment cycles creates cash flow risk.

### Recent Invoice Activity & Payment Trends
- **Most recent invoices:** Government dated through Sept 28, 2026; Commercial dated May 8, 2026
- **72 active government invoices** indicate high-volume billing activity
- **3 active commercial transactions** indicate limited commercial pipeline
- **Payment trends:** Not available from QB export (reconciliation detail not provided)

**Action Required:**
- Obtain aged A/R report showing days outstanding by invoice
- Track average government payment cycle (typical: 30–60 days net)
- Identify slow-paying customers or overdue accounts
- Establish DSO (Days Sales Outstanding) target (suggest: <45 days for government)

---

## Projects Reaching or Past Period of Performance End Dates

### Completed / Archived (No Further Activity Expected)

| Project | Name | End Date | Status |
|---------|------|----------|--------|
| **035-1** | ADONIS Unmanned Experts | 2026-03-01 | ✅ Archived; final invoice sent 4/10/2026 |
| **039-1** | Refurbished S2 Oklahoma State | 2025-08-19 | ✅ Completed & archived |
| **031-1** | S3 Project (UMES) | 2026-05-31 | ⏳ Active; completing soon |
| **032-1** | ND Air Deployed S0s | 2025-10-13 | ✅ Archived 10/21/2025 |
| **025-07** | SMM DoD 22.4D Phase II | 2025-07-11 | ✅ Archived; completed |
| **200-10** | 2024–25 Aeropod (AREN) | 2025-03-10 | ✅ Completed 3/10/2025 |
| **200-11** | Persistent IR Measurements (NASA SBIR III) | 2025-09-30 | ✅ Archived 11/2025 |
| **200-12** | NASA AREN '25 (AEROKATS) | 2025-08-31 | ✅ Shut down early |
| **200-14** | Autonomy (NASA SBIR Phase I) | 2026-03-27 | ✅ Archived 4/16/2026 |
| **211-1** | NASA Ames MHP | 2025-