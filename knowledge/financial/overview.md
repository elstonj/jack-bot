# BST Financial Health Overview

## Portfolio Summary
| Metric | Amount |
|--------|--------|
| **Total Contracted Value** | Unable to calculate — see data limitations below |
| **Total Invoiced (QBO)** | $4,527,447.64 |
| **Total Received (QBO)** | Data not fully available |
| **Total Expenses (QBO)** | $2,641,463.16 |
| **Net Income (QBO)** | $1,885,984.48 |
| **Outstanding Accounts Receivable** | ~$3,238,242.82 |

---

## Critical Data Quality Issues

**⚠️ SIGNIFICANT LIMITATIONS IDENTIFIED:**

The source materials contain **severe structural gaps** that prevent a complete, accurate financial health assessment:

1. **Project Code Mapping Failures** (40+ projects affected)
   - Projects 004-00, 006-00, 023-11, 024-05 through 024-09, 025-02 through 025-04, 026-02 through 026-05, 026-09 **lack explicit identification** in QuickBooks data
   - Many project codes appear in Asana or budget docs but **do NOT match** invoice records in QuickBooks
   - Example: Project 025-10 labeled as "025-10" but invoiced as "[043-2]"

2. **Missing Source Documents**
   - No complete QuickBooks export with **all project codes and cost allocation hierarchies**
   - Budget documents incomplete or dated (many reference 2018–2020 consolidated data)
   - No Asana project plan details for ~50% of active projects
   - No comprehensive contract/CLIN documentation

3. **Incomplete Financial Records**
   - Payment status (received vs. outstanding) not clearly marked
   - Expense allocation to specific projects unclear for ~$2.6M in total expenses
   - AR aging not available; collection risk cannot be assessed by project

---

## Financial Position: Government vs. Internal

### QuickBooks Summary (Available Data)
| Class | Revenue | Expenses | Net Position | Status |
|-------|---------|----------|--------------|--------|
| **Government Projects** | $4,504,553.28 | $1,387,864.73 | **+$3,116,688.55** | Highly Profitable |
| **BST Internal** | $22,894.36 | $1,253,598.43 | **−$1,230,703.07** | Operating Loss |
| **TOTAL** | $4,527,447.64 | $2,641,463.16 | **$1,885,984.48** | Net Positive |

**Key Finding:** Government work is profitable; internal operations are subsidized by government margin.

---

## Projects of Highest Concern

### **1. Large Outstanding Receivables (Collection Risk)**

| Project | Latest Invoice | Amount Outstanding | Client | Issue |
|---------|---|---|---|---|
| **Project 301-3** (S0 Hurricane Phase II - 2025) | Multiple invoices through 2026 | Likely $500K+ | NOAA/University of Miami | Large platform delivery; typical 30–60 day terms; verify payment status |
| **Project 300-3** (2026 IDIQ Hurricane) | Invoice #1736 (recent) | $1M+ estimated | NOAA | 25 S0 platforms + ground stations; staged delivery; payment status unknown |
| **Project 024-08** (Multi-project aggregate) | Through Sept 2025 | ~$100K estimated | Multiple | Bundled projects; difficult to isolate AR |

**Recommendation:** Request aged AR report by project to identify delays >60 days.

---

### **2. Projects with Budget Uncertainty (Insufficient Documentation)**

| Project Code | Project Name | Status | Issue |
|---|---|---|---|
| **004-00** | Portfolio/Rollup (unclear) | Unknown | Not discretely identified in actuals |
| **006-00** | Government actuals rollup | Data only | Contains 16+ sub-projects; no budget baseline |
| **023-11** | Unknown | Critical gaps | Zero budget, contract, or scope documentation |
| **024-05 through 024-09** | Multiple (USDA, ROSES, AFWERX) | Partial mapping | QB data shows transactions but project codes don't align cleanly |
| **025-02, 025-03, 025-04** | Unknown | Data missing | No QB invoices explicitly coded to these |
| **026-02 through 026-05, 026-09** | Unknown | Not found | Requested in data but not present in QB or budget docs |

**Action Required:** Reconcile Asana project codes with QuickBooks cost codes. Many projects appear to use multiple internal naming conventions.

---

### **3. Projects with Completion/Delivery Risk**

| Project | Due Date | Status | Risk Level |
|---------|----------|--------|-----------|
| **Project 026-06** (S2 Simulator & E2 Battery) | 2026-06-30 | **OVERDUE** | 🔴 **HIGH** — Battery stuck in Mexico (customs); no clear shipping plan |
| **Project 032-3** (Sasquatch S0s × 4) | ~June 19, 2026 (inferred) | **UNCLEAR** — conflicting dates | 🔴 **HIGH** — Verbal order, no contract; Asana shows July 1 due date but order placed Feb 19; timeline unconfirmed |
| **Project 043-2** (By Light Mustang) | Originally Dec 5, 2025 | Extended to July/Aug 2026 | 🟡 **MEDIUM** — Extended for contractual test flights; track milestone progress |
| **Project 350-4** (USGS Volcano - Nevado del Ruiz) | Fall 2026 | **PAUSED** | 🟡 **MEDIUM** — Mission rescheduled; confirm funding continuation & PoP extension |

---

### **4. Projects Operating at Loss / Requiring Attention**

**BST Internal Operations:** −$1,230,703.07 net loss  
This represents ~27% of government profit, indicating **overhead absorption or planned internal investments** (e.g., R&D, fleet maintenance, internal labor). Verify that internal projects (001-XX, IRAD activities) are tracked separately and budgeted as cost centers, not revenue generators.

---

## Revenue Pipeline: Approved but Un-invoiced Work

**Data Source Limitation:** Asana project data not fully provided; unable to extract forward-looking milestone invoicing schedule.

**From Available Documents:**

| Project | Client | Upcoming Milestone | Est. Invoice Value | Timing |
|---------|--------|---|---|---|
| **024-10** (Barbados S0 VTOL) | Barbados Met Services | S0 delivery | $150K–200K est. | May 22, 2026 |
| **300-3** (NOAA IDIQ 2026) | NOAA | Remaining S0 deliveries (from 25-unit order) | $500K–$1M+ | 2026–2027 (staged) |
| **301-3** (S0 Hurricane 2025) | NOAA/UM | Remaining training/ops support invoices | $100K–$200K est. | Through Aug 2026 |
| **550-1** (Navy SBIR Magnetometer) | Navy/NAWCAD | Phase II Base (if awarded Jan 2027) | TBD | 2027–2029 (30 mo.) |
| **550-2** (Navy STTR Hazardous Weather) | Navy/ONR | Final Report & Invoice | $50K–$100K est. | Due Sept 1, 2026 |

**Visibility Gap:** Cannot calculate total revenue pipeline without:
- Approved but uninvoiced CLINs from government contracts
- Milestone schedule from Asana
- Budget documents showing remaining contract value by project

---

## Cash Flow Status

### Accounts Receivable Position
| Metric | Amount | Status |
|--------|--------|--------|
| **Government AR** | $3,238,242.82 | 76 active invoices; typical Fed terms 30–45 days |
| **BST Internal AR** | Unknown | Not provided in QB summary |
| **Total AR** | ~$3.24M+ | **SIGNIFICANT — requires aging analysis** |

**Red Flag:** AR of $3.24M against total revenue of $4.53M represents **71% of annual invoicing outstanding**. This indicates either:
- Large recent invoices (normal for government); or
- Collection delays beyond normal terms; or
- Billing pending final deliverables

**Action:** Request AR aging report showing invoices >60 days past due.

---

## Cash Flow Indicators

### Recent Significant Activity
- **Government invoicing through September 28, 2026** (future-dated; indicates forward projections exist)
- **Government contracts active:** 1,285+ confirmed transactions through July 2026
- **Outstanding POs:** $2,532.00 (Amprius $1,700 + other $832)

### Purchase Orders Outstanding
| PO # | Vendor | Amount | Project | Status |
|------|--------|--------|---------|--------|
| 1038 | Amprius | $1,700.00 | Government project | Open |
| (Other) | (Various) | $832.00 | Government project | Open |

**Assessment:** Minimal open POs suggest good materials inventory or just-in-time procurement.

---

## Ranked Project List: By Financial Status

### **GREEN (Healthy / On Track)**

| Project | Client | Revenue Status | Health |
|---------|--------|---|---|
| 301-2 | NOAA Hurricane Phase II | $360,982 invoiced; contract complete | ✓ Archived |
| 200-11 | NASA Persistence Demo | Contract paid; work accepted | ✓ Archived |
| 200-13 | CRATER (Costa Rica) | $80,972 budget; deliverable complete | ✓ Archived |
| 200-14 | NASA SBIR SwiftCore Autonomy | Phase I complete | ✓ Archived |
| 400-5 | AFWERX SBIR Soil Moisture | $X (complete); Phase II option won | ✓ Archived |
| 035-1 | ADONIS (Unmanned Experts) | Contract value $X; 100% complete | ✓ Archived |
| 039-1 | Oklahoma State S2 Refurbish | PO complete; training done | ✓ Archived |

---

### **YELLOW (Active but Monitor Closely)**

| Project | Issue | Action |
|---------|-------|--------|
| **300-3** (NOAA 2026 IDIQ) | $1M+ in 25 S0 platforms; large AR likely | Verify delivery schedule & payment terms |
| **301-3** (S0 Hurricane 2025) | 33 platforms delivered; ops/training support ongoing through Aug 2026 | Confirm all invoices submitted; track final ops billing |
| **024-10** (Barbados S0 VTOL) | Delivery due May 22, 2026; training July 2026 | Confirm readiness; invoice upon delivery |
| **043-2** (By Light Mustang) | Extended to July/Aug 2026 for contractual flights | Milestone tracking; verify contract amendment payment terms |
| **550-1** (Navy Magnetometer) | Phase II option awarded; Phase II base Jan 2027 | Confirm Phase II contract signature & funding |
| **550-2** (Navy STTR Hazardous Weather) | Final deliverables due Sept 1, 2026 | Submit final invoice on schedule |

---

### **RED (Immediate Attention Required)**

| Project | Issue | Priority |
|---------|-------|----------|
| **026-06** (S2 Simulator & E2 Battery) | **OVERDUE (due June 30)** — Battery stuck in Mexico (customs); S2 status unknown | 🔴 **CRITICAL** — Customer impact; resolve within days |
| **032-3** (Sasquatch S0s × 4) | Verbal order (Feb 19, 2026); conflicting due dates; no contract signed | 🔴 **CRITICAL** — Confirm scope, price, timeline immediately with Jack Elston |
| **023-11** | **ZERO documentation** — No budget, contract, scope, or QB data | 🔴 **CRITICAL** — Determine if active or archived; reconcile in accounting system |
| **004-00, 006-00** | **Portfolio codes** — Cannot isolate financial performance by project | 🔴 **CRITICAL** — Requires chart-of-accounts reconciliation |
| **024-05 through 024-09, 025-02 through 025-04, 026-02 through 026-05, 026-09** | **Missing QB mappings** — Asana lists projects; QB actuals don't align to project codes | 🔴 **CRITICAL** — Reconcile 50+ project codes between systems |

---

## Revenue Concentration Risk

**Government Dependency:**
- Government revenue: $4,504,553.28 (99.5% of total)
- Commercial revenue: $22,894.36 (0.5% of total)

**Risk:** Extremely high dependence on government contracts. Loss of 1–2 major NOAA or NASA contracts would dramatically impact profitability.

**Mitigation Needed:**
- Accelerate commercial product sales (Barbados, universities, private operators)
- Expand non-NOAA government customer base (Navy expanding; track SBIR/STTR success rate)

---

## Summary Recommendations

### **Immediate (Next 30 days)**

1. **Resolve Overdue Projects**
   - Project 026-06: Clarify customs issue for E2 battery; expedite S2 Simulator shipment
   - Project 032-3: Confirm scope & timeline with Jack Elston; formalize verbal order

2. **Reconcile Project Code Mappings**
   - Match all Asana project codes to QuickBooks cost codes
   - Classify projects 004-00, 006-00, 023-11 correctly
   - Map 025-02 through 025-04, 026-02 through 026-05, 026-09 to QB transactions

3. **AR Aging Analysis**
   - Request QB aging report (invoices >60 days outstanding)
   - Identify payment delays by customer
   - Priority: Verify NOAA payment patterns

### **Short-Term (30–90 days)**

4. **Budget-to-Actuals Reconciliation**
   - Compile approved contract value + CLINs for all 50+ active projects
   - Calculate remaining budget by project (to identify overruns early)
   - Forecast cash flow using staged delivery schedules (e.g., 25 S0s for NOAA)

5. **Government Contract Status Review**
   - Navy SBIR/STTR progress: Track Phase II option awards (550-1, 550-2)
   - NASA SBIR Phase III close-outs: Confirm all invoices paid (200-11, 200-13, 200-14)
   - USGS Volcano mission: Confirm Fall 2026 deployment & PoP extension

6. **Internal Cost Structure**
   - Classify internal projects (001-XX, IRAD) as cost centers, not revenue generators
   - Benchmark overhead burn rate; justify $1.23M internal loss against government margin

### **Longer-Term (90+ days)**

7. **Commercial Revenue Growth**
   - Track university/research sales pipeline (CU Boulder, ND, Oklahoma State trend)
   - Barbados platform delivery & training (May–July 2026) as proof of concept
   - Evaluate product-line profitability vs. government service contracts

8. **Project Portfolio Consolidation**
   - Eliminate zombie project codes (004-00, 006-00, 023-11)
   - Migrate all projects to unified code structure
   - Implement monthly project health dashboard (budget vs. actual, AR aging, milestone status)

---

## Data Quality Assessment

| Metric | Status | Impact |
|--------|--------|--------|
| QuickBooks Actuals | ✅ **Good** | Reliable invoicing & expense data |
| Budget Documentation | ⚠️ **Incomplete** | ~40% of active projects lack budget baselines |
|