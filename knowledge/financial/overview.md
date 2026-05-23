# BST Financial Health Overview – Company-Wide Summary

## ⚠️ CRITICAL DATA QUALITY ISSUES

Before presenting the portfolio summary, it is essential to flag **severe data integration challenges** that limit the accuracy and completeness of this overview:

1. **Project Code Misalignment:** Many requested project codes (026-03, 026-04, 025-02, 025-03, etc.) do **not appear in QuickBooks actuals** or have unclear mappings to named projects.

2. **Incomplete Budget Documentation:** Drive Budget Docs were not fully provided. Only partial contract values and budgets are available.

3. **Missing Asana Integration:** Most projects lack milestone, deliverable, and timeline data from Asana, making remaining work estimates impossible.

4. **Fragmented Accounting:** QuickBooks data shows **multi-project aggregation by month** (e.g., "2024-08" contains SMM Phase II, Navy SBIR, USGS Mexico, etc. combined), preventing accurate per-project P&L isolation.

5. **Incomplete AR Aging:** Payment status and invoice aging details are limited; full accounts receivable aging reports were not provided.

**RECOMMENDATION:** Complete data collection (full Drive Budget Docs export, Asana project export with milestones, detailed QuickBooks trial balance by project) is required for a fully accurate financial health assessment.

---

## Portfolio Summary (Based on Available Data)

| Metric | Amount | Source / Notes |
|--------|--------|----------------|
| **Total Contracted Value (Government)** | ~$4,387,717 | QuickBooks (Government class) |
| **Total Contracted Value (Internal/Other)** | ~$17,894 | QuickBooks (BST Internal class) |
| **TOTAL COMPANY CONTRACTED REVENUE** | ~$4,405,612 | QB Year-to-Date Summary |
| **Total Invoiced to Clients** | ~$4,405,612 | QB Invoices issued |
| **Payments Received (Cash In)** | ~$1,285,414* | Estimated from QB data; incomplete AR aging provided |
| **Outstanding Accounts Receivable** | ~$3,120,198 | Government contracts (75 active invoices) |
| **Total Expenses Incurred** | ~$2,439,963 | QB Bills & Purchases |
| **Net Income (Gross Margin)** | ~$1,965,649 | Revenue - Expenses (preliminary) |
| **Estimated Remaining Revenue (All Projects)** | ~$3.1M - $5M* | Dependent on: outstanding AR collection + active pipeline invoiceable milestones |

**\*Notes:**
- **AR Recovery:** If $3.1M in outstanding Government invoices is collected in full, cash position improves significantly.
- **Remaining Revenue:** Estimated from active/near-completion projects (S0 Hurricane Phase II, Navy SBIR Magnetometer Phase II, NOAA IDIQ 300-3, NASA SBIR 200-14, etc.).
- **Project costs to completion** are not fully documented; actual remaining budgets unclear.

---

## By Project – Health Status Summary
(Sorted by **Health Risk – Red/Yellow/Green**)

### 🔴 **RED / CRITICAL ATTENTION REQUIRED**

| Project Code | Project Name | Contracted Value | Invoiced | Remaining | Outstanding AR | Health Issue |
|--------------|--------------|------------------|----------|-----------|-----------------|--------------|
| **024-10** | Barbados S0 VTOL + Training | $TBD | $0.00 | $TBD | $0 | **PAST DUE** – Original delivery 2024-10-01; S0 delivery now May 22, 2026; training July 1–4, 2026. No invoices yet. Manufacturing & logistics delay risk HIGH. |
| **031-1** | UMES S3 VTOL | $81,306 | $29,000 | ~$52,306 | $TBD | **CRITICAL FINAL PHASE** – Delivery deadline May 29, 2026 (imminent). Training July 23–25, 2026. Manufacturing phase; high execution risk. |
| **032-3** | Sasquatch S0s x 4 (Notre Dame) | ~$160,000 est. | $0.00 | ~$160,000 | $0 | **MAJOR DATA ERROR** – Asana shows 7/1/2026 start/due dates, but verbal order placed 2/19/2026 with 4-month delivery (implies ~6/19/2026 due). Conflicting timeline. **ACTION REQUIRED: Clarify delivery dates immediately.** |
| **043-2** | By Light Mustang (M1) | ~$175,000 est. | ~$150,000 | ~$25,000 | TBD | **CONTRACT EXTENDED** – Original 10/6/2025–12/5/2025; extended through May 2026 awaiting flight test opportunities. Budget tracking unclear. |
| **550-1** | Navy SBIR Magnetometer | Phased (Phase I base complete, Phase II TBD) | $173,890+ | Ongoing Phase II prep | TBD | **PHASE II NOT YET AWARDED** – Phase I completed Jan 2026; Phase II option period in progress (Apr 14–Sep 28, 2026). Future funding contingent on Phase II award. Track closely. |

### 🟡 **YELLOW / NEEDS MONITORING**

| Project Code | Project Name | Contracted Value | Invoiced | Remaining | Outstanding AR | Health Issue |
|--------------|--------------|------------------|----------|-----------|-----------------|--------------|
| **300-3** | 2026 NOAA IDIQ (20 S0 sUAS) | $5M+ (5-year IDIQ) | $1,736,000+ | $3.3M+ | ~$320K+ | **MAJOR CONTRACT** – Multi-year, firm fixed price. High per-unit cost ($180K+/platform); manufacturing lead time critical. 6 units delivered YTD; 14 remaining. Revenue visibility good but execution risk HIGH (supply chain, custom integration). |
| **301-3** | S0 Hurricane Phase II 2025 | ~$2M est. | $900,000+ | ~$1.1M | ~$650K+ | **HIGH AR BALANCE** – 33 units contracted (26 base + 7 optional). Invoicing ongoing; training & delivery through Aug 2026. AR aging unclear; prioritize collection. |
| **200-13** | CRATER (NASA Costa Rica) | $80,972 | $80,972 | $0 | $0 | **COMPLETE** – Archived. All deliverables accepted. Monitor for any final expense reconciliation. |
| **025-07** | SMM DoD 22.4D Phase II (AFWERX) | ~$200K | ~$195,000 | ~$5K | $TBD | **ARCHIVED (7/21/2025)** – Contract completion successful. Minor remaining tasks/closeout invoices possible. |
| **044-1** | EMASS Chip Integration | ~$75K est. | ~$40K | ~$35K | TBD | **INDEFINITELY POSTPONED** – External blocker (5/13/2026): EMASS has not delivered functioning controller binary. Project stalled; no work occurring. **RISK:** Scope creep if project resumes; budget erosion possible. |

### 🟢 **GREEN / ON TRACK**

| Project Code | Project Name | Contracted Value | Invoiced | Remaining | Outstanding AR | Health Status |
|--------------|--------------|------------------|----------|-----------|-----------------|--------------|
| **200-11** | Persistent IR Wildfires (NASA Phase III) | ~$285K est. | ~$285K | $0 | $0 | ✅ **COMPLETE & ARCHIVED (11/24/2025)** – All deliverables accepted; final payment received. |
| **200-14** | NASA SBIR Adaptive Autonomy (SwiftCore 3.3) | ~$150K est. | ~$150K | $0 | $0 | ✅ **COMPLETE & ARCHIVED (4/16/2026)** – SwiftCore 3.3 development complete. Ready for commercialization. |
| **026-05** | SwiftCore 3.3 (Internal R&D) | Internal project | Minimal | Minimal | N/A | ✅ **SUBSTANTIALLY COMPLETE (May 2026)** – Internal flight control software platform. Ready for release. |
| **035-1** | ADONIS (Unmanned Experts) | ~$225K est. | ~$225K | $0 | $0 | ✅ **ARCHIVED (4/10/2026)** – All deliverables complete. **PROJECT PERMANENTLY CLOSED per Jack Elston (2026-04-20): "Do NOT list as priorities ever again."** |
| **025-05 / 025-06** | Hesselius E2 (CU Boulder) | $15,000 | $15,000 | $0 | $0 | ✅ **ARCHIVED (6/4/2025)** – Inventory clearance deal complete. |
| **550-2** | Navy STTR Expendable Air-Sea Profiling | Phase I complete; Phase II option ongoing | $180K+ | Ongoing | TBD | 🟡 **OPTION PERIOD IN PROGRESS** (Jan 7–Jul 6, 2026; final deliverable Sep 1, 2026). On track. |

---

## Projects Needing Immediate Attention

### 1. **Project 024-10: Barbados S0 VTOL + Training** 🔴 **CRITICAL**
- **Issue:** Original delivery deadline **2024-10-01 has PASSED** by 7+ months.
- **Current Timeline:** S0 delivery now due **May 22, 2026**; training **July 1–4, 2026**.
- **Financial Status:** $0 invoiced; no revenue recognized.
- **Action Required:**
  - Confirm revised delivery/training schedule with Sabu Best (Barbados Met Services).
  - Establish revised invoicing milestones (advance payment, milestone-based, or final delivery).
  - Assess manufacturing/logistics capacity for May 2026 delivery.
  - Risk: Further delays will impact H2 2026 cash flow.

---

### 2. **Project 031-1: UMES S3 VTOL** 🔴 **CRITICAL**
- **Issue:** Delivery deadline **May 29, 2026** (imminent – likely weeks away).
- **Financial Status:** $29K invoiced of $81.3K contracted; $52.3K remaining.
- **Action Required:**
  - Confirm manufacturing completion status and final assembly schedule.
  - Coordinate training schedule (July 23–25, 2026) with UMES engineering team.
  - Prepare final invoices and payment terms (post-delivery or split payment).
  - Risk: Manufacturing delays will cascade to training delay and Q3 2026 cash impact.

---

### 3. **Project 032-3: Sasquatch S0s x 4 (Notre Dame)** 🔴 **CRITICAL**
- **Issue:** **DATA CONFLICT** – Asana shows 7/1/2026 start and due dates, but verbal order placed **2/19/2026** with Jack Elston's stated 4-month timeline (~6/19/2026 due).
- **Financial Status:** $0 invoiced of ~$160K estimated; full amount outstanding.
- **Action Required:**
  - **URGENT:** Clarify actual order date and delivery deadline with Jack Elston.
  - Correct Asana project dates.
  - Establish manufacturing schedule and invoicing milestones.
  - Risk: Conflicting timeline could result in missed delivery and customer dissatisfaction.

---

### 4. **Project 300-3: NOAA 2026 IDIQ (20 S0 sUAS Platforms)** 🟡 **HIGH VALUE / EXECUTION RISK**
- **Contract Value:** $5M+ (5-year IDIQ).
- **Current Status:** $1.736M invoiced; $3.3M+ remaining over contract life.
- **Outstanding AR:** ~$320K+ (estimated from payment patterns).
- **Action Required:**
  - Ensure manufacturing capacity and supply chain for remaining 14 units.
  - Track per-unit costs vs. $180K+ firm fixed price (margin erosion risk).
  - Monitor AR aging; prioritize collection of outstanding invoices.
  - Coordinate with NOAA UxSOC (Norfolk, VA) on delivery schedules.

---

### 5. **Project 301-3: S0 Hurricane Phase II 2025 (NOAA)** 🟡 **HIGH AR BALANCE**
- **Contract Value:** ~$2M (33 units: 26 base + 7 optional).
- **Current Status:** $900K+ invoiced; ~$1.1M remaining.
- **Outstanding AR:** ~$650K+ (estimated – high collection risk).
- **Action Required:**
  - Obtain **detailed AR aging report** from QB; follow up on invoices >30 days past due.
  - Prioritize payment collection (estimated $650K outstanding).
  - Coordinate final unit deliveries and training (through Aug 2026).
  - Risk: If AR is not collected by Q3 2026, cash flow will be constrained.

---

### 6. **Project 550-1: Navy SBIR Magnetometer** 🔴 **FUNDING CONTINGENCY**
- **Contract Status:** Phase I base completed Jan 2026; Phase II option period active (Apr 14–Sep 28, 2026).
- **Phase II Status:** Not yet awarded (contingent on Phase II selectivity).
- **Financial Impact:** If Phase II is **not selected**, revenue stream ends; no additional funding beyond Phase I option period.
- **Action Required:**
  - Confirm Phase II proposal status and anticipated award date.
  - Develop contingency plans if Phase II is not funded.
  - Track Phase I option period deliverables to maintain Navy relationship for future opportunities.

---

### 7. **Project 044-1: EMASS Chip Integration** 🟡 **STALLED / BUDGET RISK**
- **Status:** **Indefinitely postponed** (5/13/2026) – EMASS has not delivered functioning controller binary.
- **Financial Status:** ~$40K invoiced of ~$75K estimated; ~$35K remaining (at risk).
- **Action Required:**
  - Determine EMASS status and likelihood of resumption.
  - If resumption is unlikely, consider project closeout and margin recovery.
  - If resuming, establish hard deadlines for EMASS deliverables to avoid scope creep.
  - Risk: Budget hours may continue to accumulate with no corresponding revenue if project uncertainty persists.

---

## Revenue Pipeline – Upcoming Invoiceable Milestones

### Near-Term (Q2–Q3 2026)

| Project | Milestone | Estimated Invoice Amount | Timeline |
|---------|-----------|--------------------------|----------|
| **031-1** (UMES S3) | Final delivery invoice | ~$52,300 | May 29, 2026 |
| **024-10** (Barbados S0) | S0 delivery invoice | ~$TBD (likely $50K–$100K) | May 22, 2026 |
| **032-3** (ND Sasquatch x4) | Unit deliveries (4 units) | ~$160,000 (split across units) | June 19–July 2026 (est.) |
| **300-3** (NOAA IDIQ) | Remaining 14 units delivery | ~$2.5M–$3.3M | Ongoing through 2030; ~3–4 units/quarter |
| **301-3** (S0 Hurricane) | Final training & close-out invoices | ~$200K–$400K | Jul–Aug 2026 |
| **043-2** (By Light Mustang) | Final deliverables / close-out | ~$25K–$50K | May 2026 (contract extension) |

### Mid-Term (H2 2026 – H1 2027)

| Project | Opportunity | Estimated Value | Status |
|---------|-------------|-----------------|--------|
|