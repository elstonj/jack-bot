# BST Financial Health Overview

## 🔴 CRITICAL DATA QUALITY ISSUES

**Before presenting financial analysis, critical limitations must be acknowledged:**

1. **Fragmented Project Data:** 50+ project codes provided with highly inconsistent documentation. Many projects lack:
   - Complete contract values or CLINs
   - Clear periods of performance
   - Budget vs. actual reconciliation
   - Period-end status clarity

2. **QuickBooks Data Incomplete:** 
   - Accounts receivable aging detail missing
   - Payment receipt dates not systematically provided
   - Expense categories aggregated at company level, not by project
   - No cash flow forecast

3. **Project Code Mismatches:** Multiple instances where Asana, Drive budgets, and QuickBooks use different project coding conventions, making cross-reference impossible

4. **No Consolidated Master Schedule:** Cannot determine which projects are active, archived, on-hold, or at risk without manual review of each record

---

## Portfolio Summary (Company-Wide Actuals)

| Metric | Amount | Source |
|--------|--------|--------|
| **Total Invoiced (FY to Date)** | $7,448,665.62 | QuickBooks |
| **Government Invoices** | $4,462,176.28 | QB (76 invoices) |
| **Commercial Invoices** | $2,986,489.34 | QB (1 recent) |
| **Total Expenses Recorded** | $1,572,434.98 | QB |
| **Gross Profit (Invoiced Basis)** | $5,876,230.64 | QB calc |
| **Outstanding A/R** | $3,219,865.82 | QB |
| **Government A/R** | $3,194,865.82 | 76 outstanding invoices |
| **Commercial A/R** | $25,000.00 | Invoice #1769 (EMASS, unpaid) |

---

## Active / Near-Term Projects (Sorted by Urgency)

### 🔴 HIGH PRIORITY — PROJECTS NEEDING IMMEDIATE ATTENTION

#### **Project 044-1: EMASS Chip Integration**
- **Status:** 🔴 **INDEFINITELY POSTPONED** on external blocker
- **Contract Value:** Not specified in budget docs
- **Invoiced to Date:** $25,000.00
- **Outstanding A/R:** $25,000.00 (Invoice #1769, June 9, 2026) — **UNPAID**
- **Issue:** Validation Flights #2 & #3 blocked indefinitely awaiting EMASS deliverables (DoD autopilot controller)
- **Action Required:** 
  - Escalate payment collection for Invoice #1769
  - Clarify timeline with EMASS for pending contractual work
  - Determine if project should be formally suspended or renegotiated

---

#### **Project 301-3: S0 Hurricane Phase II - 2025 (NOAA)**
- **Contracted Value:** Not clearly specified; high-volume delivery
- **Invoiced to Date:** Appears significant based on QB "Government" portfolio ($4.46M total)
- **Period of Performance:** Feb 2025 – Aug 26, 2026 (extended 6 months)
- **Scope:** 33 S0 VTOL units (26 base + 7 optional) for NOAA hurricane research
- **Status:** ✓ In delivery; training & ops support ongoing
- **Risk Flag:** High manufacturing/delivery complexity; verify schedule vs. invoicing pace
- **Action Required:**
  - Confirm delivery schedule alignment with NOAA PoP end date (Aug 26, 2026)
  - Reconcile invoiced amount with contract value
  - Identify any remaining CLINs or optional deliverables not yet invoiced

---

#### **Project 300-3: 2026 IDIQ (NOAA Hurricane)**
- **Contract Value:** $483,000 (IDIQ value)
- **Delivery Order (FY2026):** 25 S0 units + 2 ground stations
- **Period of Performance:** March 2026 – July 31, 2026
- **Invoiced to Date:** Not broken out separately from Government total
- **Status:** ⚠️ Current delivery phase active through July 2026
- **Risk Flag:** Near-term PoP deadline (July 31, 2026); verify all deliverables on track
- **Action Required:**
  - Reconcile invoiced amount vs. $483K contract value
  - Confirm delivery timeline for all 25 units + ground stations
  - Identify any undelivered CLINs or outstanding change orders

---

### 🟡 MEDIUM PRIORITY — PROJECTS WITH OUTSTANDING INVOICES OR SCHEDULE RISK

#### **Project 550-1: Navy SBIR Magnetometer**
- **Contract Value:** Not fully specified
- **Period of Performance:** Base Jan 2027 – June 2029; Current Phase I Option (Apr–Sept 2026)
- **Status:** ✓ In execution; Phase II proposal preparation underway
- **A/R Status:** Unknown from QB data; verify if invoiced
- **Action Required:**
  - Confirm Phase I invoicing completion
  - Establish Phase II proposal timeline & funding approval status

---

#### **Project 550-2 / 567-01: Navy STTR — Air-Sea Profiling (S0-AD)**
- **Contract Value:** Not specified
- **Period of Performance:** Base completed (July 2025 – Jan 2026) ✓; Option in progress (Jan–July 2026)
- **Final Deliverable Due:** Sept 1, 2026
- **Status:** ⚠️ On track but final report/deliverables critical
- **A/R Status:** Unknown; verify invoicing for completed base period
- **Action Required:**
  - Confirm all base period invoices received/paid
  - Establish payment schedule for option period work
  - Ensure final report completion by Sept 1, 2026

---

#### **Project 024-04: AFWERX SBIR Phase II (Runway Integrity / SMM)**
- **Contract Value:** Not fully specified
- **Period of Performance:** April 5, 2024 – June 5, 2026 (26 months, ending in ~2 months)
- **Status:** Nearing completion; field validation at Sunny Slope Sod Farm
- **A/R Status:** Unknown; likely invoiced but verify recent payments
- **Action Required:**
  - Confirm all deliverables on schedule for June 5, 2026 close-out
  - Prepare final invoice & close-out documentation
  - Identify any Phase III opportunity funding (if applicable)

---

#### **Project 025-04: DOE FECM Methane Monitoring**
- **Contract Value:** Not specified
- **Period of Performance:** 2025-04 through 2025-10 (partial year data available)
- **Invoiced to Date:** Included in QB "Government" total
- **Status:** Active; S2 + eddy covariance system deployment
- **A/R Status:** Unknown; verify payment status
- **Action Required:**
  - Confirm contract period end date
  - Verify budget vs. actual spend trajectory
  - Identify remaining invoiceable milestones

---

#### **Project 043-2: ByLight Mustang (Long-Range Fixed-Wing)**
- **Contract Value:** Fixed-price (amount not provided in summary)
- **Period of Performance:** Oct 6, 2025 – Dec 5, 2025 (core deliverables completed Dec 31, 2025 — 26 days late)
- **Status:** 🟡 **ARCHIVAL PENDING** — Core work complete; 2 additional flight opportunities on indefinite hold pending customer DoD autopilot controller delivery
- **A/R Status:** Check if final invoice submitted and paid
- **Action Required:**
  - Confirm final payment received for core deliverables
  - Document delay impact (26 days) and any change orders
  - Establish hold status for remaining flight work or formally close if no longer planned

---

#### **Project 043-3: ByLight M2 Design (Halo Platform)**
- **Contract Value:** Firm fixed-price (amount not provided)
- **Period of Performance:** Scope 1: Apr 3 – May 30, 2026; Scope 2: TBD upon fuselage receipt
- **Status:** Design & testing phase; awaiting customer fuselages for integration
- **A/R Status:** Likely invoicing in progress
- **Action Required:**
  - Confirm Scope 1 deliverables on schedule
  - Clarify Scope 2 timeline & contractual terms for fuselage-dependent work
  - Verify invoicing cadence matches milestones

---

### 🟢 LOWER PRIORITY — ARCHIVED / COMPLETED PROJECTS (Verify Closure)

**Confirmed Completed:**
- **400-5** (AFWERX SMM Phase II) — Archived Nov 2025 ✓
- **200-11** (NASA Persistence Demo) — Archived Nov 24, 2025; all payments received ✓
- **200-14** (NASA Autonomy SBIR Phase I) — Archived Apr 16, 2026 ✓
- **035-1** (ADONIS) — Archived Apr 10, 2026; per Jack Elston: "Do NOT list as priorities, ever again" ✓
- **025-07** (SBIR SMM Phase II DoD 22.4D) — Archived Nov 2025 ✓
- **031-1** (S3 VTOL at UMES) — Delivery complete May 29, 2026; past deadline (May 31) ⚠️
- **032-1** (ND Air S0s) — Delivery complete Oct 13, 2025 ✓
- **032-2** (ND Air Display Model) — Complete; $4,500 received ✓
- **210-11** (NASA Ames MHP for S2) — Completed Mar 27, 2025 ✓
- **025-05 & 025-06** (CU Boulder E2 Hesselius) — Both completed Jun 4, 2025 ✓

---

## Revenue Pipeline (Upcoming Invoiceable Milestones)

**⚠️ NOTE:** Without detailed Asana project boards and drive budget CLINs aligned to each project, the following is **inferred from available PoP dates and scope descriptions:**

| Project | Client | Next Milestone | Est. Invoice Date | Estimated Amount |
|---------|--------|-----------------|-------------------|------------------|
| **300-3** | NOAA (2026 IDIQ Hurricane) | Final S0 delivery + ground stations | July 2026 | Unknown |
| **301-3** | NOAA (S0 Hurricane Phase II) | Training delivery + operational support | June–Aug 2026 | Unknown |
| **024-04** | AFWERX (Runway Integrity) | Final report & closeout | June 2026 | Unknown |
| **550-2 / 567-01** | Navy STTR (Air-Sea Profiling) | Final report delivery | Sept 1, 2026 | Unknown |
| **043-3** | ByLight (M2 Halo Design) | Scope 1 completion; Scope 2 TBD | May–June 2026 | Unknown |
| **025-04** | DOE FECM (Methane Monitoring) | System deployment completion | TBD (unknown PoP end) | Unknown |

---

## Cash Flow Analysis

### Accounts Receivable Concerns

| Category | Balance | Status | Action Required |
|----------|---------|--------|-----------------|
| **Total A/R** | $3,219,865.82 | 🔴 CRITICAL | Collection acceleration needed |
| **Government A/R** | $3,194,865.82 | 🔴 Large outstanding across 76 invoices | Aging analysis required |
| **Commercial A/R** | $25,000.00 | 🔴 Invoice #1769 (EMASS, June 9) UNPAID | Escalate payment collection |
| **Receivable Days Outstanding** | Unknown | 📊 CANNOT CALCULATE | Invoice date → payment date analysis needed |

### Red Flags:
1. **$3.22M in outstanding receivables** represents 43% of total invoiced revenue — unsustainable cash position
2. **EMASS (044-1) Invoice #1769 unpaid** since June 9, 2026 — indicates customer financial distress or project dispute
3. **Government A/R aging unknown** — 76 invoices outstanding suggests mix of recent and aged items; DTRA, NOAA, DoD payment cycles vary (30–60 days typical for federal)
4. **No payment forecast provided** — cannot project when outstanding A/R will convert to cash

### Recommended Immediate Actions:
- **Generate aging A/R report** by invoice date (30/60/90+ days overdue)
- **Follow up on EMASS Invoice #1769** — determine payment status and project disposition
- **Verify federal contract payment schedules** — confirm expected payment dates for NOAA, DTRA, Navy contracts
- **Establish cash flow forecast** — model when A/R will be collected vs. upcoming expenses

---

## Projects Requiring Clarity / Data Gaps

**The following project codes appear in QB data but lack complete documentation:**

| Project | QB Activity | Issue | Action |
|---------|-------------|-------|--------|
| **004-00, 006-00, 018-20, 023-11, 024-05, 024-06, 024-07, 024-08, 024-09, 024-11, 025-02, 025-03, 025-08, 025-09, 025-12, 026-02, 026-04, 026-05, 026-09, 141-1, 200-7** | Yes | Missing budget docs, contract details, or Asana boards | Provide missing documentation or consolidate under parent project codes |
| **010-1** (Methane Detection) | $3.5M+ invoiced | No contract/budget docs; 101 QB transactions | Clarify contract structure & budget approval |
| **018-1** (Murphy's Pond) | Active | Budget docs exist; verify PoP end date (Dec 31, 2026) | Confirm remaining work & invoice schedule |

---

## Summary of Financial Health by Risk Level

### 🔴 CRITICAL RISK (Immediate Action Required)
1. **A/R Balance: $3.22M outstanding** — 43% of revenue; collection acceleration essential
2. **EMASS (044-1): $25K unpaid since June 9** — project indefinitely on hold; payment/resolution needed
3. **Project Code Fragmentation:** 50+ codes with inconsistent documentation; consolidation or clarification needed

### 🟡 MEDIUM RISK (Monitor & Plan)
1. **NOAA Deliverables (300-3, 301-3):** High manufacturing complexity; verify delivery schedules closely
2. **AFWERX Phase II Completion (024-04):** June 5 deadline approaching; confirm closeout documentation ready
3. **Navy Contract Reporting (550-1, 550-2, 567-01):** Multiple concurrent Navy programs; ensure invoicing/reporting aligned to contract requirements
4. **ByLight Fixed-Price Contracts (043-2, 043-3):** Monitor for scope creep; confirm change order process active

### 🟢 LOW RISK (Monitor Routine)
- Archived/completed projects; verify final invoices paid
- Active R&D projects (IRAD); budget authority & spending within plan

---

## Recommended Next Steps

1. **Urgent (This Week):**
   - Generate full aging A/R report; contact delinquent customers
   - Escalate EMASS Invoice #1769; determine project recovery plan
   - Create master project inventory (50+ codes → consolidated active/archived list)

2. **Short-term (This Month):**
   - Reconcile QB project codes with Asana & Drive budgets; establish single source of truth
   - Develop 12-month cash flow forecast based on contract PoP dates & payment cycles
   - Close-out documentation for 024-04 (AFWERX) and 550-2 (Navy) due June–Sept 2026

3. **Ongoing:**
   - Implement monthly project financial health dashboard (Budget vs.