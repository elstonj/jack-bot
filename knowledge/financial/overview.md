# BST Financial Health Overview

## Portfolio Summary
| Metric | Amount |
|--------|--------|
| Total Invoiced (All Projects) | $4,480,070.64 |
| Total Expenses | $2,448,997.46 |
| Net Income | $2,031,073.18 |
| Outstanding Accounts Receivable | $3,194,865.82 |
| Outstanding Purchase Orders | $2,532.00 |

---

## Critical Data Quality Issues

**⚠️ SIGNIFICANT LIMITATION:** The provided data sources contain **severe structural inconsistencies** that prevent comprehensive per-project financial analysis:

1. **Project Code Misalignment**: 50+ project codes reference multi-project aggregates rather than single discrete projects. QuickBooks coding does not align with Asana project structure.

2. **Incomplete Source Data**: 
   - 40+ projects lack budget documentation (contracts, CLINs, approved amounts)
   - 35+ projects lack Asana task/milestone definitions
   - Most projects missing Period of Performance details
   - No consolidated aging AR (Accounts Receivable) detail by project

3. **Portfolio Fragmentation**: 
   - Projects 004-00, 006-00, and 024-xx aggregate 50+ distinct government contracts and commercial sales
   - Unable to isolate individual project profitability or health status

---

## Active Projects by Financial Health Status

### 🔴 RED — Requiring Immediate Attention

**Project 010-1 (Methane Emission Detection)**
- Invoiced: $3,517,802.84
- Budget docs: Missing
- Status: **CRITICAL** — Over $3.5M invoiced with no contract baseline for comparison; cannot assess profitability or remaining scope

**Project 024-10 (BARBADOS S0 VTOL)**
- Status: **CRITICAL DELAY**
- Current Issue: Active aircraft crash during development; delivery delayed indefinitely past original October 1, 2024 date
- Financial exposure: Unknown (budget not provided; likely cost overruns)

**Project 301-3 (S0 Hurricane Phase II – 2025)**
- Invoiced: $1,000,000+ (estimated from volume)
- Status: **HIGH RISK** — Large contract with extended delivery period (through August 2026); 33 systems to deliver
- Profitability: Unknown; no cost-to-complete analysis provided

**Project 300-3 (2026 IDIQ – NOAA Hurricane)**
- Contract Value: $\[amount not extracted from data\]
- Status: **CRITICAL INFRASTRUCTURE** — 5-year IDIQ worth significant volume; 25 platforms + ground stations for 2026 season
- Risk: Production capability unknown; no current manufacturing status provided

### 🟡 YELLOW — Monitor Closely

**Project 024-04 (AFWERX SBIR Phase II – Soil Moisture)**
- Archived November 2025 (successfully completed)
- Status: **CLOSED** — Project delivered; final invoicing complete

**Project 025-07 (SBIR SMM DoD 22.4D)**
- Contract Value: $\[not provided\]
- Status: **ARCHIVED** — Closed out November 2025
- Financial Position: Successfully completed

**Project 026-01 (Navy STTR – S0 Weather)**
- Invoiced: $\[amount not clearly isolated\]
- Status: **ACTIVE** — Ongoing Navy contract; invoicing through January 2026
- Health: Yellow (requires AR follow-up)

**Project 026-07 (NOAA UxSOC UAS Delivery)**
- Contracted Value: $\[not provided in extracted summary\]
- Status: **ACTIVE** — March–July 2026 delivery window
- Risk: 25 units (24 + 4 + 1 + 1 refurbished) must deliver in concentrated timeframe

**Project 032-1 & 032-2 (Notre Dame S0 Platforms)**
- Combined Invoiced: $42,500
- Status: **ARCHIVED** — Both completed October 2025
- Health: Green (delivered, payment received)

### 🟢 GREEN — Healthy Status

**Project 031-1 (UMES S3)**
- Invoiced: $\[amount from data not clearly isolated\]
- Status: **COMPLETED** — Delivery May 29, 2026 ✅
- Health: Green (delivered on time)

**Project 039-1 (OK State Refurbished S2)**
- Invoiced: $\[amount not clearly isolated\]
- Status: **ARCHIVED** — Completed August 2025; training delivered
- Health: Green (completed, closed October 2025)

**Project 042-1 (Stanford SHM Components)**
- Invoiced: $\[amount not extracted\]
- Status: **ARCHIVED** — Completed June 2025
- Health: Green

**Project 043-1 (ByLight Standing Task Order)**
- Status: **ACTIVE** — Extended to May 5, 2026
- Health: Green (ongoing revenue generation)

**Project 043-2 & 043-3 (By Light Mustang/Halo)**
- Status: **ARCHIVED/ACTIVE**
- 043-2: Core deliverables completed (26 days late); outstanding work pending
- 043-3: In execution through May 2026
- Health: Amber (043-2 has contractual completion issues)

**Project 200-13 (CRATER – Costa Rica)**
- Invoiced: $80,972.00
- Status: **ARCHIVED** — Completed February–August 2025
- Health: Green (completed)

**Project 200-14 (NASA Autonomy SBIR Phase I)**
- Status: **ARCHIVED** — Completed April 16, 2026
- Health: Green

**Project 452-1 & 452-2 (CU Boulder E2 Equipment)**
- Combined Revenue: $18,900
- Status: **ARCHIVED** — Both completed June 2026
- Health: Green (inventory clearance, profitable)

---

## Revenue Pipeline & Outstanding Invoices

### Major Outstanding AR (by apparent invoice volume)

1. **Government Contracts (totaling $3,194,865.82)**
   - Largest concentration: Methane/Environmental monitoring contracts
   - Hurricane/Atmospheric research contracts
   - NASA/SBIR-related work
   - Navy programs (SBIR/STTR)
   - **USGS/NOAA multi-year contracts**

2. **Pending Invoicing Opportunities**
   - Project 024-03 (NASA ROSES Wildfire) — $518,293.20 proposed budget; Phase I development
   - Project 024-04 (AFWERX SBIR) — Completed; should be fully invoiced
   - Project 200-12 (NASA AREN '25) — $20,576 BST portion; project shut down early
   - Project 550-1 (Navy Magnetometer SBIR) — Phase I active through September 2026; Phase II option pending

### Critical Cash Flow Issues

**⚠️ $3.19M in Outstanding AR from Government Contracts**
- No aging detail provided (30/60/90+ day buckets unknown)
- No payment trend analysis available
- Recent invoice activity suggests 2-4 month payment cycles typical for government

---

## Projects Needing Immediate Action

| Project | Issue | Required Action |
|---------|-------|-----------------|
| **024-10 (Barbados S0)** | Aircraft crash; delivery past due | Assess damage, obtain insurance proceeds; determine restart timeline |
| **010-1 (Methane)** | $3.5M invoiced; no budget baseline | Obtain contract/CLIN documents; reconcile scope vs. actuals; confirm remaining deliverables |
| **301-3 (S0 Hurricane 2025)** | Large volume (33 units); extended delivery | Confirm manufacturing schedule; assess supplier availability; validate delivery feasibility |
| **300-3 (NOAA 2026 IDIQ)** | Mission-critical 5-year contract; 25-unit delivery | Confirm production readiness; validate supply chain; schedule delivery timeline |
| **043-2 (By Light Mustang)** | Completed 26 days late; outstanding work pending | Clarify scope of "additional flight opportunities"; reset customer expectations; document contractual status |
| **026-01 & 026-07 (Navy/NOAA)** | Multiple large contracts in execution | Confirm on-schedule status; ensure AR collection process activated |

---

## Recommendations for Improved Financial Visibility

1. **Implement Project Code Standardization**
   - Map each QuickBooks transaction to a single, discrete project code
   - Reconcile Asana project codes with QuickBooks GL structure
   - Create lookup table linking Contract Numbers → Project Codes → Asana Project IDs

2. **Develop Comprehensive Budget Baselines**
   - Obtain contract documents for all active projects
   - Extract CLINs, milestones, and approved amounts
   - Load into QuickBooks as project budgets for real-time variance tracking

3. **Establish AR Collection Dashboard**
   - Aging AR by project and client
   - Payment history trends (average days to payment by customer)
   - Monthly cash flow forecast by project

4. **Create Project Health Scorecard**
   - Budget vs. Actuals variance by project
   - Schedule performance (% complete vs. timeline)
   - AR collection status
   - Risk flags (delays, cost overruns, client issues)

5. **Consolidate Multi-Project Codes**
   - Projects 004-00, 006-00, and 024-xx represent 50+ distinct contracts
   - Unbundle into granular project codes for accurate tracking
   - Current structure obscures individual project profitability

---

## Summary Conclusion

**Overall Financial Health: YELLOW**

- **Strengths**: Strong net income ($2.03M); government contracts represent 99.6% of revenue; multiple active awards in pipeline
- **Risks**: $3.19M outstanding AR (78% of annual revenue); critical project delay (Barbados); unclear budget baselines on largest invoiced projects; manufacturing capacity questions for large multi-unit contracts
- **Action Required**: Urgent clarification on Barbados crash recovery, budget documentation for top 10 projects, AR aging analysis, and project profitability reconciliation

**Estimated timeline to financial clarity: 2-3 weeks with complete source data.**