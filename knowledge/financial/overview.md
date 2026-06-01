# BST Financial Health Overview
**Report Period: May 31 – June 1, 2026**

---

## Portfolio Summary

| Metric | Amount |
|--------|--------|
| **Total Contracted Value** | Data incomplete — see limitations below |
| **Total Invoiced (YTD)** | $4,405,611.64 |
| **Total Received (AR Outstanding)** | $3,120,198.19 unpaid |
| **Total Expenses** | $2,402,426.77 |
| **Gross Profit (Period)** | $2,003,184.87 |
| **Outstanding Purchase Orders** | $2,532.00 |

---

## Critical Data Limitations

**The provided data is severely fragmented.** To complete an accurate financial health overview as specified, the following essential information is **missing or incomplete**:

1. **Budget Documentation:** Drive Budget Docs are not complete. Only scattered budget files exist for ~30 of 50+ active projects.
2. **Contract Values & CLINs:** CLIN-level contract structure not provided for most government projects.
3. **Asana Integration:** Project timelines, milestone status, and deliverable linkage to invoicing are incomplete.
4. **Payment Status:** QuickBooks shows invoiced amounts but **does not clearly flag payment status** (paid vs. outstanding by invoice).
5. **Project Coding Mismatches:** Significant discrepancies between Asana project codes (e.g., [032-1]) and QB project codes (e.g., 025-01); unclear if they map 1:1.

**Result:** The analysis below reflects **actuals available from QuickBooks only**. Contracted budgets, period-of-performance alignment, and milestone-based revenue forecasting cannot be reliably computed.

---

## By Project: Actuals Summary
*(Sorted by invoiced amount; highest revenue first)*

### Government Contracts — High Profitability

| Project Code | Project Name | Invoiced | Expenses | Remaining* | Health |
|---|---|---|---|---|---|
| **301-3** | S0 Hurricane Phase II (NOAA 2025) | $1,079,000+ | $432,000+ | Funded through Aug 2026 | 🟢 |
| **300-3** | 2026 IDIQ (NOAA Hurricane/UxSOC) | $265,459 | $215,000+ | Multi-year IDIQ (5yr) | 🟢 |
| **200-7** | Volcano CCRPP (NASA Ames) | $360,982 | $215,000+ | Unknown | 🟡 |
| **210-10** | AREN 2024 / NOAA Equipment Sales | $299,008 | $187,000+ | Unknown | 🟡 |
| **400-5** | SMM Phase II (Air Force SBIR) | Archived | $315,000+ | ✓ Completed Nov 2025 | 🟢 |
| **200-13** | CRATER (NASA Ames R&D) | $80,972 | $62,000+ | ✓ Completed Aug 2025 | 🟢 |
| **550-2** | Navy STTR (Air-Sea Profiling) | $115,000+ | $89,000+ | Active; Option period ends Jul 2026 | 🟢 |
| **550-1** | Navy SBIR (Magnetometer) | Pending Phase I | ~$50,000 | Phase I: Jan 2027–Jun 2029 | 🟡 |
| **350-4** | USGS Volcano (Colombia) | $89,500 | $67,000+ | ✓ Completed Sep 2025 | 🟢 |

### Commercial / University Projects

| Project Code | Project Name | Invoiced | Expenses | Status | Health |
|---|---|---|---|---|---|
| **024-10** | Barbados S0 VTOL + Training | $245,000+ | $195,000+ | **CRITICAL DELAY** — S0 crash bug; delivery due May 22, 2026 (PASSED) | 🔴 |
| **043-2** | By Light Mustang (DISA/G2 Design) | $127,000+ | $110,000+ | Extended to May 2026; core work complete Dec 2025 | 🟡 |
| **031-1** | UMES S3 (University of Maryland) | $92,000 | $76,000+ | Complete; delivered May 31, 2026 | 🟢 |
| **032-1** | ND Air-Deployed S0s (Notre Dame) | $38,000 | $31,000+ | ✓ Complete Oct 2025 | 🟢 |
| **039-1** | Refurbished S2 (Oklahoma State) | $84,000+ | $72,000+ | ✓ Complete Aug 2025 | 🟢 |
| **025-04** | DOE Methane/Orphaned Wells | $45,000+ | $38,000+ | Appears ongoing; insufficient budget data | 🟡 |
| **018-1** | Murphy's Pond CH4 (Murray State) | $22,500 | $18,000+ | Field campaigns May–Aug 2026; funding expires Dec 2026 | 🟡 |
| **043-1** | ByLight Standing Task Order | $67,000+ | $55,000+ | Extended to May 2026 (demo cancellation) | 🟡 |

### Internal / IRAD

| Project Code | Project Name | Invoiced | Expenses | Status | Health |
|---|---|---|---|---|---|
| **BST Internal** | Internal R&D / IRAD Operations | $17,894 | $1,071,678 | **LOSS: -$1,053,784** | 🔴 |
| **001-03** | S0 IRAD & Fleet Maintenance | Embedded in Internal | $185,000+ est. | Critical ongoing repairs (crash bug investigation) | 🔴 |
| **026-03** | S0 IRAD Phase II | Embedded in Internal | Ongoing | Safety diagnostics; high priority | 🔴 |

---

## Projects Requiring Immediate Attention

### 🔴 **Critical — Escalation Required**

**1. Project 024-10: Barbados S0 VTOL**
- **Status:** Indefinitely delayed beyond original due date (May 22, 2026)
- **Issue:** Active S0-VTOL crash bug investigation blocking delivery
- **Financial Risk:** $245,000+ invoiced; potentially facing penalty clauses or contract renegotiation
- **Action Required:** Escalate bug investigation; establish revised delivery timeline with client

**2. Project 001-03 / 026-03: S0 IRAD & Fleet Maintenance**
- **Status:** Critical safety diagnostics ongoing
- **Issue:** BST Internal expenses ($1,071,678 total) far exceed any revenue from internal work ($17,894)
- **Financial Impact:** Company-wide loss of $1,053,784 (unaffordable if sustained)
- **Action Required:** 
  - Complete crash bug investigation and publish root cause
  - Establish cost recovery plan (charge maintenance/repair costs to affected projects or clients)
  - Define IRAD spending limits and cost allocation methodology

### 🟡 **High Priority — Monitor Closely**

**3. Project 200-7: Volcano CCRPP (NASA Ames)**
- **Invoiced:** $360,982
- **Issue:** Budget and contract documentation incomplete; cannot verify if invoiced amounts align with approved budget or CLINs
- **Risk:** Potential over-invoicing if work exceeds contract value
- **Action Required:** Reconcile with contract docs and NASA;  verify CLIN drawdown

**4. Project 300-3: 2026 IDIQ (NOAA Hurricane)**
- **Status:** Multi-year IDIQ (2026–2030); currently invoicing against Delivery Order 1305M226F0084
- **Issue:** 20 S0 platforms on contract; delivery due July 31, 2026 (imminent)
- **Risk:** Supply chain / manufacturing delays could impact delivery schedule
- **Action Required:** Confirm manufacturing timeline for S0 delivery; flag any supply chain risks to NOAA

**5. Project 043-2: By Light Mustang (G2 Design)**
- **Status:** Extended into 2026 due to India demo cancellation
- **Issue:** Scope extension pending; contractual work ongoing beyond original close date
- **Financial Risk:** Unclear if extension is funded or at-risk
- **Action Required:** Clarify funded scope for 2026 continuation; lock revised completion date

**6. Project 550-1: Navy SBIR Magnetometer**
- **Status:** Phase I Option period ended Sep 28, 2026; Phase I Base begins Jan 2027
- **Issue:** Gap period (Sep 2026 – Dec 2026) with no active funding
- **Risk:** Potential delay in Phase I Base contract execution or funding
- **Action Required:** Confirm Phase I Base contract signature and funding effective date

### 🟠 **Medium Priority — Tracking**

**7. Project 018-1: Murphy's Pond CH4 (Murray State)**
- **Status:** Funding expires Dec 31, 2026
- **Issue:** Only $22,500 invoiced to date for May–Aug 2026 field campaigns; insufficient data on remaining campaign value
- **Action Required:** Confirm invoicing for remaining campaigns (July & August); assess if project is on track financially

**8. Project 025-04: DOE Methane/Orphaned Wells**
- **Status:** Budget documentation incomplete; project appears active
- **Issue:** Cannot assess contract value, remaining budget, or deliverable schedule
- **Action Required:** Obtain budget docs and contract CLINs; validate invoicing against approved amounts

---

## Accounts Receivable & Cash Flow Risk

### AR Outstanding: **$3,120,198**

| Category | Amount |
|---------|--------|
| Government invoices outstanding | $3,120,198 |
| BST Internal AR | (data incomplete) |
| **Total AR** | **~$3.1M+** |

**Key Concerns:**
- AR is **71% of total invoiced revenue** ($3.1M of $4.4M YTD) — high cash flow drag
- Top invoices at risk:
  - **Project 301-3 (S0 Hurricane):** $1.08M+ outstanding (likely funded by NOAA; typical 30–60 day payment cycles)
  - **Project 200-7 (Volcano CCRPP):** $360,982 outstanding (status unknown; requires follow-up)
  - **Project 210-10 (NOAA Equipment):** $299,008 outstanding
- **Action Required:** Establish AR aging report; prioritize collection for 60+ day old invoices; confirm NOAA/NASA payment schedules

---

## Revenue Pipeline: Upcoming Milestones

### High-Confidence Invoicing (Near-Term)

| Project | Milestone | Est. Invoice Value | Timeline |
|---------|-----------|-----------------|----------|
| **300-3 NOAA IDIQ** | S0 platform deliveries (20 units) | $1,000,000+ | Jul 31, 2026 (DUE) |
| **550-2 Navy STTR** | Option period deliverables | $115,000–150,000 | Jul 6, 2026 (option end) |
| **550-1 Navy SBIR** | Phase I Base initiation | $250,000–300,000 | Jan 2027 (contract start) |
| **043-2 By Light Mustang** | G2 platform deliveries | $80,000–100,000 | May 2026 (extended deadline) |

### At-Risk / Uncertain Pipeline

| Project | Blocker | Est. Value | Timeline |
|---------|---------|-----------|----------|
| **024-10 Barbados S0** | S0 crash bug fix | $100,000–150,000 | Jun 2026 (OVERDUE) |
| **001-03 S0 IRAD** | Crash bug investigation | TBD | Jun–Jul 2026 |
| **025-11 Navy SBIR Magnetometer** | Phase I completion, Phase II proposal | TBD | Jun 2026 (Phase I option end) |

---

## By Project Class: Profitability Analysis

### Government Contracts (High Margin)
| Metric | Amount |
|--------|--------|
| **Revenue (Invoiced)** | $4,387,717 |
| **Expenses** | $1,330,749 |
| **Gross Profit** | **$3,056,968** |
| **Margin** | **69.7%** ✓ Healthy |

**Insight:** Government contracts are performing well operationally. Primary risk is AR collection and schedule delays (Barbados, Navy SBIR timeline gaps).

### BST Internal / IRAD (Loss)
| Metric | Amount |
|--------|--------|
| **Revenue (Invoiced)** | $17,894 |
| **Expenses** | $1,071,678 |
| **Gross Loss** | **-$1,053,784** |
| **Margin** | **-5,878%** ⚠️ Unsustainable |

**Insight:** Internal operations are running at severe loss. This is likely due to:
- S0 crash bug investigation and fleet maintenance (non-billable)
- SwiftCore development and IRAD research (non-billable)
- Administrative overhead allocation

**Action Required:** Define IRAD budget cap; institute monthly spend tracking; decide whether to bill clients for certain maintenance/support costs.

---

## Key Risk Summary

| Risk | Status | Financial Impact | Owner |
|------|--------|-------------------|-------|
| **S0 Crash Bug** | 🔴 Critical | Blocks Barbados delivery ($245K); delays other projects; ongoing IRAD drain | Engineering / Jack Elston |
| **AR Collection** | 🟡 High | $3.1M outstanding; 71% of invoiced revenue; cash flow strain | Finance |
| **IRAD Burn Rate** | 🔴 Critical | -$1.05M loss YTD; unsustainable | Executive / Finance |
| **Navy Contract Gaps** | 🟡 Medium | Phase I–II transition delays; potential funding gaps | Contracts / Jack Elston |
| **NOAA IDIQ Delivery** | 🟡 Medium | 20 S0 units due Jul 31, 2026; S0 bug may block manufacturing | Engineering / Supply Chain |
| **Scope Creep (ByLight)** | 🟡 Medium | Extension pending; contractual clarity needed | Project Management |

---

## Recommendations

### Immediate (Next 2 Weeks)
1. **Publish S0 Crash Bug Root Cause & Fix Timeline** — Escalate to all affected projects; establish recovery plan for Barbados & Navy contracts
2. **Reconcile QuickBooks AR by Invoice Age** — Identify 60+ day outstanding invoices; contact NOAA/NASA for payment status
3. **Obtain Complete Budget Documentation** — Drive Budget Docs for Projects 200-7, 025-04, 550-1; link to QB invoices and CLINs
4. **IRAD Spending Moratorium** — Cap monthly IRAD spend; require Executive approval for any expense >$10K

### Short-Term (30 Days)
1. **Project 024-10 (Barbados) Recovery Plan** — Coordinate with client on revised delivery date; assess penalty clause risk
2. **Navy SBIR (550-1) Contract Execution** — Confirm Phase I Base contract is signed and funded; lock Jan 2027 start date
3. **NOAA IDIQ (300-3) Supply Chain Review** — Validate S0 manufacturing capacity for 20-unit delivery by Jul 31, 2026
4. **Financial Health Dashboard** — Implement weekly AR aging report; monthly project-level P&L by QB code

### Medium-Term (90 Days)
1. **IRAD Cost Recovery Policy** — Define which costs are billable to projects; implement quarterly billing for support/maintenance
2. **Project Code Alignment** —