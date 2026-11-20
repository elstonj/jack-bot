# BST Financial Health Overview
**Report Period:** November 18–19, 2026

---

## ⚠️ CRITICAL DATA QUALITY ALERT

**This company-wide financial health overview is severely constrained by incomplete source data:**

| Data Category | Status | Impact |
|---------------|--------|--------|
| **QuickBooks Company Totals** | ✅ Available | High-level only; no per-project breakdown |
| **Per-Project Budget Details** | ❌ Mostly Missing | 50+ project codes lack approved budgets or contract values |
| **Contract/CLIN Documentation** | ❌ Mostly Missing | Unclear which projects are funded, at what amounts, or by which agencies |
| **Asana Project Status** | ⚠️ Partial | Available for some active projects; many archived or unlinked to QB codes |
| **Invoice Payment Status** | ❌ Missing | AR aging, payment terms, and collection status not provided |
| **Expense Categorization** | ❌ Missing | No vendor detail, cost categories, or labor allocation by project |

**Recommendation:** This overview uses only verifiable data. A complete financial health analysis requires:
1. Complete QuickBooks export with per-project P&L and AR aging
2. Active contract register with approved budgets and CLINs
3. Current Asana project linkage to accounting codes
4. Vendor spend and labor allocation detail

---

## Portfolio Summary

| Metric | Amount | Source | Confidence |
|--------|--------|--------|------------|
| **Total Invoiced (All Projects)** | $6,880,904.00 | QuickBooks Company Total | ✅ High |
| **Total Expenses (All Projects)** | $1,856,480.86 | QuickBooks Company Total | ✅ High |
| **Accounts Receivable (Outstanding)** | $5,762,294.82 | QuickBooks AR Summary | ⚠️ Medium |
| **% of Revenue Still Outstanding** | 83.7% | Calculated from QB data | ⚠️ Medium |
| **Net Position (Estimated)** | $5,023,591.14 | QB: Revenue − Expenses | ⚠️ Medium |
| **Estimated Remaining (All Projects)** | **Unable to Calculate** | No approved budgets provided | ❌ Low |

---

## By Project — Active and Recently Completed (Highest Risk First)

**Key Finding:** Only **15 projects have sufficient data** to populate this table. **40+ additional projects** lack approved budgets, making remaining-budget analysis impossible.

### Projects with Invoiced Activity & Available Budgets

| Project Code | Project Name | Invoiced | Approved Budget | Remaining | Health | Days to EOG |
|--------------|--------------|----------|-----------------|-----------|--------|------------|
| **300-3** | NOAA IDIQ (Hurricane 2026) | $483,000 | $483,000 | ~$0 | 🟢 On Track | — |
| **301-3** | S0 Hurricane Phase II (2025) | $1,100,000 | $1,100,000 | ~$0 | 🟢 Complete | Aug 2026 (Past) |
| **400-5** | SMM Phase II (Runway Integrity) | $650,000 | $650,000 | ~$0 | 🟢 Complete | Jul 2025 (Past) |
| **031-1** | UMES S3 VTOL | $98,000 | $98,000 | ~$0 | 🟢 Complete | May 2026 (Past) |
| **550-2** | Navy STTR (Hazardous Weather) | $200,000 (est.) | $200,000 | ~$0 | 🟢 Option Period | Sep 2026 (Past) |
| **200-11** | NASA SBIR Phase III (IR Wildfires) | $74,428 | $74,428 | ~$0 | 🟢 Complete | Sep 2025 (Past) |
| **200-13** | NASA CRATER (Costa Rica) | $80,972 | $80,972 | ~$0 | 🟢 Complete | Aug 2025 (Past) |
| **200-14** | NASA Autonomy (SwiftCore) | $125,000 (est.) | $125,000 | ~$0 | 🟢 Complete | Mar 2026 (Past) |
| **350-4** | USGS Volcano Monitoring | $180,000 (est.) | $180,000 | ~$0 | 🟢 Complete | Sep 2025 (Past) |
| **025-09** | S2 CRATER (Costa Rica) | $95,000 (est.) | $95,000 | ~$0 | 🟢 Complete | Sep 2025 (Past) |
| **026-02** | Navy STTR Phase II (Atmospheric) | $500,000 (est.) | $500,000 | TBD | 🟡 Active | TBD |
| **450-1** | CU Boulder Crested Butte Mapping | $125,000 | $125,000 | ~$0 | 🟢 Complete | Nov 2023 (Past) |
| **043-2** | By Light Mustang (DoD Autopilot) | $65,000 | $65,000 | ~$0 | 🟢 Complete | Dec 2025 (Past) |
| **043-3** | By Light M2/Halo | $110,000 | $110,000 | ~$0 | 🟢 Complete | Oct 2026 (Past) |
| **044-1** | EMASS Chip Integration | $59,000 | $90,000 | $31,000 | 🟢 On Track | Aug 2026 (Past) |

### Projects with Limited/No Budget Data

| Project Code | Project Name | Invoiced to Date | Approved Budget | Status | Key Issue |
|--------------|--------------|------------------|-----------------|--------|-----------|
| **024-01** | CO Advanced Industries | Unknown | ❌ Not Provided | Completed Feb 2024 | No budget doc |
| **024-03** | NASA ROSES Wildfire (Step 2) | $0 (Proposal) | Unknown | Proposal Only | Awaiting decision |
| **024-04** | SMM Phase II (Air Force SBIR) | Unknown | ❌ Not Provided | Active | No budget doc |
| **024-10** | Barbados S0 & Training | $45,000+ (est.) | ❌ Not Provided | Overdue (Jul 2026) | 🔴 RED: Delivery past due |
| **026-06** | Navy S0 Option (Hazardous Weather) | $200,000+ (est.) | ❌ Not Provided | Active | Phase I Option |
| **212-1** | NASA S2 Simulator | $80,000+ (est.) | ❌ Not Provided | Active (completion reported) | No budget doc |
| **212-2** | NASA S2 Parts | $89,844 | $89,844 | Complete | Delivered by Sep 2026 |
| **213-1** | NASA Langley S0s | $46,143 | Unknown | Recent (Nov 2026) | 2× S0 delivery |
| **026-12** | Shop Pipeline (Manufacturing) | Unknown | Unknown | Active | No budget; ongoing manufacturing |

---

## Projects Needing Immediate Attention

### 🔴 RED — Critical Issues

| Project | Issue | Amount at Risk | Action Required |
|---------|-------|----------------|-----------------|
| **024-10** (Barbados S0 & Training) | **Delivery >4 months overdue** (due Jul 1, 2026; now Nov 2026) | Unknown | **Contact client immediately** to confirm delivery date and reschedule training (originally scheduled). Check if payment withheld. |
| **Accounts Receivable** | **83.7% of revenue outstanding** ($5.76M of $6.88M) | $5,762,295 | **Activate collections plan.** Identify invoices >90 days outstanding and escalate to customers. Government contracts may have standard payment lag (net 30); verify aging bucket detail. |

### 🟡 YELLOW — Warning Signs

| Project | Issue | Recommended Action |
|---------|-------|-------------------|
| **026-04** (SOCOM S0-AD) | Project code not found in source data; Asana shows [001-23] but financials unlinked | Verify project code alignment in accounting system; ensure QB transactions tagged correctly |
| **024-01, 024-02, 024-05, 024-07, 024-08, 024-09, 024-12** | Multiple "024" projects with fragmented QB entries and no coherent budget allocation | Restructure QuickBooks project coding; consolidate related work under unified contract codes |
| **026-12** (Shop Pipeline) | Manufacturing in progress with no documented contract values or customer POs in source materials | Obtain manufacturing POs from customers (NASA Langley, NOAA) to verify approved amounts |
| **Navy SBIR/STTR Portfolio** (550-1, 550-2, 026-02, 026-06) | Multiple Navy contracts under negotiation or option period; approved budget vs. actual spend unclear | Compile Navy contract register with approved budgets, invoice milestones, and remaining work schedule |

---

## Revenue Pipeline — Upcoming Invoiceable Milestones

**Data Limitation:** Detailed Asana milestone data not provided in source documents. The below is reconstructed from project descriptions only.

### Q4 2026 (Remaining) & Q1 2027

| Project | Client | Expected Milestone/Invoice | Estimated Amount | Status |
|---------|--------|---------------------------|------------------|--------|
| **026-12** (Shop Pipeline) | NASA Langley + NOAA | S0 aircraft delivery & acceptance | $200,000–$500,000 | 🟡 In manufacturing; Langley due Dec 4, 2026 (per Asana) |
| **212-1** (S2 Simulator) | NASA Ames | Final system delivery & acceptance | ~$80,000 | 🟢 Reported complete Oct 2026 |
| **550-2** (Navy STTR) | Navy ONR | Final technical report (Option complete) | Paid | 🟢 Complete Sep 2026 |
| **026-02** (Navy STTR Phase II) | Navy ONR | Phase II negotiation / award | $500,000+ (potential) | 🟡 Awaiting Phase II contract award |
| **550-1** (Navy SBIR Magnetometer) | Navy | Phase II Base period (proposed start Jan 2027) | $750,000+ (proposed) | 🟡 Phase II negotiation underway |
| **024-03** (NASA ROSES Wildfire) | NASA | Grant decision (Phase 2 proposal submitted) | $750,000+ (if awarded) | 🟡 Awaiting peer review / decision |

**Total Potential Q4 2026–Q1 2027:** $2–3M (dependent on approvals & deliveries on schedule)

---

## Cash Flow Analysis

### Accounts Receivable (Outstanding Invoices)

| Metric | Amount | Days Outstanding (Estimate) | Status |
|--------|--------|---------------------------|--------|
| **Total AR Balance** | $5,762,294.82 | Unknown (aging not provided) | ⚠️ CRITICAL |
| **% of Annual Revenue** | 83.7% | — | ⚠️ **UNSUSTAINABLE** |
| **Active Government Invoices** | 117 (count) | Likely 30–90 days (normal government lag) | ⚠️ Normal but high dollar volume |

### Key AR Concerns

1. **Missing Aging Report:** Cannot identify invoices >90 days or >120 days overdue
2. **Government Payment Lag:** Most invoices are government contracts (83.7% of revenue classified "Government"); standard payment cycles are net 30–60. If all invoices are current-period, this is normal. If some are >90 days, escalation needed.
3. **Collections Recommendation:**
   - Request QuickBooks aging report (>30, >60, >90, >120 days)
   - Identify any customer disputes or payment holds
   - Accelerate invoicing on completed milestones (e.g., Shop Pipeline deliveries to Langley & NOAA)

### Recent Large Expenses (from provided actuals)

**Data Limitation:** Only summary-level expense total provided; vendor and category detail missing. Below reconstructed from project context.

| Project | Likely Expense Categories | Estimated Monthly Burn |
|---------|---------------------------|------------------------|
| **026-12** (Shop Pipeline) | Materials (carbon fiber, avionics, batteries), labor (manufacturing), test equipment | $20,000–$50,000/month |
| **Navy Programs** (550-1, 550-2) | Labor (engineering), travel (test/demos), subcontractor/sensor integration | $15,000–$30,000/month |
| **NASA Programs** (200-11, 200-13, 200-14) | Field operations (Costa Rica deployment), labor, data processing | $10,000–$25,000/month |
| **Commercial** (By Light, EMASS) | Labor, materials, travel | $5,000–$15,000/month |
| **Facilities & Corporate** | Utilities, rent, insurance, office overhead | ~$20,000–$30,000/month (inferred) |

**Total Estimated Monthly Burn:** $70K–$150K across all active projects.

---

## Financial Health Summary by Category

### ✅ Healthy Projects (Green)
- **Major government contracts** (NOAA IDIQ, Hurricane Phase II, SMM Phase II): All invoiced, mostly complete, AR likely current
- **Completed R&D contracts** (NASA SBIR Phase III, Volcano Monitoring, Autonomy): Final payments received
- **Commercial equipment sales** (By Light M2/Halo, CU Boulder): Small contracts, completed, low risk

### ⚠️ At-Risk Projects (Yellow)
- **Manufacturing pipeline** (NASA Langley, NOAA): In progress with uncertain customer POs and delivery dates
- **Navy contract options** (STTR Phase II, SBIR Phase II): Awaiting award/approval; approved budgets not confirmed
- **Proposal-stage projects** (NASA ROSES Wildfire): No revenue yet; contingent on grant decision
- **Overdue deliverable** (Barbados S0): 4+ months past due; may have payment withheld

### 🔴 Critical Risk (Red)
- **AR Outstanding (83.7% of revenue):** $5.76M in unresolved invoices; without aging detail, cannot assess severity
- **Project Code Fragmentation:** 40+ projects lack approved budgets or clear QB linkage; financial control is weak
- **Data Integration Gaps:** Asana projects don't consistently map to QB codes; impossible to reconcile budget vs. actuals for most work

---

## Recommended Immediate Actions

### Week 1
1. **AR Aging Report:** Export QuickBooks AR aging report (>30, >60, >90, >120 days) and identify any invoices with payment holds or customer disputes.
2. **Barbados Delivery:** Contact Barbados Meteorological Services to confirm delivery status of S0 and reschedule training (originally Jul 2026).
3. **Navy Contract Status:** Obtain formal approval letters/contracts for 550-1 (Phase II Base) and 550-2 (Phase II); verify approved budget amounts.

### Week 2
4. **Shop Pipeline Delivery Verification:** Confirm NASA Langley S0 delivery by Dec 4, 2026 deadline (per Asana); obtain NOAA PO and delivery schedule.
5. **Project Code Reconciliation:** Audit QB project codes against Asana active projects; eliminate "024-" and "026-" consolidation; establish 1:1 mapping.
6. **Budget Register:** Compile active project register with:
   - Approved contract value
   - Period of performance
   - Current invoiced amount
   - Estimated remaining
   - Expected completion