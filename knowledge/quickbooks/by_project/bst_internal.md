# BST Internal — QuickBooks Financials

## Financial Summary
- **Total Invoiced (Revenue)**: $22,894.36
- **Total Expenses (Bills + Purchases)**: $1,379,909.42 *(+$13,161.45 from July 31–Aug 1, 2026; +$13,161.45 from Aug 2–26, 2026)*
- **Total Purchase Orders**: $1,700.00 *(PO #1038 Amprius, outstanding)*
- **Net Position**: -$1,357,015.06 *(expenses exceed revenue significantly)*
- **Date Range**: April 5, 2024 – August 26, 2026 (28+ months)
- **Transaction Count**: 1,478 *(+136 new transactions confirmed Aug 2–26)*

---

## Revenue (Invoices & Payments)

| Invoice # | Date | Customer | Amount | Balance | Days Outstanding |
|-----------|------|----------|--------|---------|------------------|
| #1771 | 2026-07-06 | Invest Ottawa | $5,000.00 | $5,000.00 | 51 days |
| #1752 | 2026-04-03 | Krateo Sky | $10,860.48 | $10,860.48 | 145 days |
| #1727 | 2025-12-02 | Weather Stream (c) | $928.88 | $928.88 | 268 days |
| #1696 | 2025-08-26 | Phase1 Aviation | $6,105.00 | $6,105.00 | 366 days |

**Total Invoiced**: $22,894.36  
**Total Collected**: $0.00 *(all invoices remain outstanding)*  
**Outstanding Receivables**: $22,894.36 *(100% uncollected)*

### Collection Status & Critical Actions Required:

- **CRITICAL OVERDUE — Invoice #1696 (Phase1 Aviation)**: $6,105.00 | **366 days overdue** (Aug 26, 2025).
  - *Status*: Double-payment for 20 wings identified; amount should be recovered or credited immediately.
  - **ACTION**: Initiate collection recovery procedure and/or credit memo processing.

- **ESCALATED OVERDUE — Invoice #1752 (Krateo Sky)**: $10,860.48 | **145 days overdue** (Apr 3, 2026).
  - *Status*: Largest single outstanding invoice; 5+ months without payment.
  - **ACTION**: Escalate to legal/collections; contact customer for payment status.

- **PRIORITY FOLLOW-UP — Invoice #1771 (Invest Ottawa)**: $5,000.00 | **51 days overdue** (Jul 6, 2026).
  - *Status*: Grant/investment income; timing correlates with Ottawa demo logistics (Jul 14–19) and server infrastructure acquisition (Jul 30).
  - **ACTION**: Contact Invest Ottawa immediately for payment confirmation; may indicate broader funding issue.

- **OVERDUE — Invoice #1727 (Weather Stream)**: $928.88 | **268 days overdue** (Dec 2, 2025).
  - *Status*: 8+ months outstanding; lowest balance but longest relative neglect.
  - **ACTION**: Follow-up communication and payment demand required.

---

## Expenses by Cost Category

### Direct Labor & Subcontractors: $394,728.90
**Total**: $394,728.90 | **26 vendors** | **Largest: Matthew Crabtree $108,556.68; Ted Miles $4,851.60**

**New Transactions (Aug 2–26, 2026):**

| Date | Vendor | Amount | Description | Account | Status |
|------|--------|--------|-------------|---------|--------|
| 2026-08-25 | Matthew Crabtree (Bill #BST-AUG2026-1) | $375.00 | Rework deployment_tube_board_1-v0.1 (PMXB120EPE issue) — 3 hrs | DC-Direct Cost Subcontractors | ✓ Confirmed |

**Analysis**:
- Matthew Crabtree bill addition: $375.00 for specialized circuit board rework (PMXB120EPE issue resolution)
- Indicates post-Ottawa demo design iteration and component-level debugging
- Cumulative Matthew Crabtree spend now $108,556.68 (28.0% of all labor/subcontractor costs)

**Cumulative Direct Labor & Subcontractors (Apr 2024–Aug 26)**: $394,728.90

---

### Materials & Direct Purchases: $553,245.32
**Total**: $553,245.32 | **98 transactions** | **Largest items: S3 inventory $34,056.24; Electronics/components $209,099.64; Composites/structures $46,854.95; Parts sourcing/assembly $28,218.16**

**New Transactions (Aug 2–26, 2026):**

| Date | Amount | Account | Description | Status |
|------|--------|---------|-------------|--------|
| 2026-08-25 | $28,218.16 | DC-Direct Material Purchases | Parts Sourcing/Assembly/Stencils (Matthew Crabtree invoice) | ✓ Confirmed |
| 2026-08-21 | $2.62 | DC-Direct Material Purchases | Acetal Rod, Black, 3/16" Diameter | ✓ Confirmed |
| 2026-08-21 | $282.40 | Inventory Asset (S0 VTOL Sales) | For future S0 VTOL Sales | ✓ Confirmed |
| 2026-08-19 | $2.62 | DC-Direct Material Purchases | Acetal Rod, Black, 3/16" Diameter, 4 Feet Long | ✓ Confirmed |
| 2026-08-19 | $238.04 | Inventory Asset (S3 Sales) | Items for future S3 Sales | ✓ Confirmed |
| 2026-08-19 | $1.14 | DC-Direct Material Purchases | Chemical-Resistant Slippery PTFE Rod 3/16" | ✓ Confirmed |
| 2026-08-19 | $7.85 | DC-Direct Material Purchases | 18-8 Stainless Steel Pan Head Phillips Screw | ✓ Confirmed |
| 2026-08-08 | $1,386.32 | DC-Direct Material Purchases | Items for IDIQ contract | ✓ Confirmed |
| 2026-08-06 | $232.32 | DC-Direct Material Purchases | Navy Magnetometer supplies | ✓ Confirmed |
| 2026-08-04 | $233.32 | DC-Direct Material Purchases | Remote-Release Rotary Latch; Multipurpose 6061 Aluminum Bar; T-Slotted Framing; 316 Stainless Steel Ultra-Low-Profile Socket | ✓ Confirmed |
| 2026-08-03 | $121.15 | DC-Direct Material Purchases | Magnetometer supplies | ✓ Confirmed |
| 2026-08-03 | $44.15 | DC-Direct Material Purchases | Hurricane IDIQ supplies | ✓ Confirmed |
| 2026-08-03 | $74.07 | DC-Direct Material Purchases | S2 NASA supplies | ✓ Confirmed |

**August 2–26 Direct Materials Addition**: $31,461.16 (allocated across multiple projects and inventory)

**Transaction Analysis**:

**Direct Material Purchases** ($31,461.16 cumulative):
- **Parts Sourcing/Assembly/Stencils** ($28,218.16): Largest single line item; indicates manufacturing preparation or production run setup for deployment_tube_board_1 revision
- **IDIQ Contract Materials** ($1,386.32): Navy/government contract component procurement
- **NASA S2 Supplies** ($74.07): Direct materials for Space Situational Awareness contract
- **Hurricane IDIQ Supplies** ($44.15): Disaster response/resilience product line materials
- **Navy Magnetometer Supplies** ($232.32 + $121.15 = $353.47): Navigation/sensing system for government contract
- **Structural/Mechanical Components** ($9.61 cumulative acetal rods + PTFE + fasteners): General assembly and integration materials

**Inventory Buildup** ($520.04):
- **S3 Sales Future Inventory** ($238.04): VTOL airframe components for production pipeline
- **S0 VTOL Sales Inventory** ($282.40): Next-generation platform preparation

**Strategic Context**:
- Sustained multi-contract material procurement (NASA S2, Navy Magnetometer, IDIQ Hurricane, S3 VTOL production)
- Post-Ottawa demo (Jul 14–19) manufacturing acceleration evident in parts sourcing volume
- Government contract execution flowing through direct materials (Navy, NASA, IDIQ)

**Cumulative Materials & Direct Purchases (Apr 2024–Aug 26)**: $553,245.32

---

### IRAD Indirect R&D (Subcontractors & Internal): $119,452.69
**Total**: $119,452.69 | **155 transactions** | **Largest: Boostr R&D Tax Credits $10,773.62; MicroFirm Engineering $6,257.60; PROTO LABS (manufacturing) $2,054.38 (Aug 2026); Castle Creations ESCs $632.05 (Aug 2026); Dronetag systems $613.62 (Aug 2026); HARTING/Molex connectors $302.42 (Aug 2026)**

**New Transactions (Aug 2–26, 2026):**

| Date | Amount | Vendor/Description | Account | Status | Strategic Significance |
|------|--------|-------------------|---------|--------|------------------------|
| 2026-08-25 | $405.94 | MHP Tip Main.step × 6 (CAD/engineering component) | IRAD-Internal R&D | ✓ Confirmed | Multi-unit component replication for S0 VTOL production |
| 2026-08-25 | $94.44 | Master_Assembly___End_Busbar (electrical assembly) | IRAD-Internal R&D | ✓ Confirmed | Power distribution integration |
| 2026-08-25 | $1,052.48 | Master-Assembly-Duct.step; Sonde-Shell.step; Tail-Servo-Mount.step | IRAD-Internal R&D | ✓ Confirmed | Thermal/sensor/control integration subassemblies |
| 2026-08-25 | $2,656.04 | Master-Assembly-AP-Bottom-Brace.step; GPS-Mount; Laser-Plate; Joiner-Insert | IRAD-Internal R&D | ✓ Confirmed | Structural reinforcement & navigation integration |
| 2026-08-25 | $226.86 | Electrical connectors/wiring bundle (Silicone wire, Amass MR30/MR60, banana plugs, Quick Release Plate, tripod mount) | IRAD-Internal R&D | ✓ Confirmed | UAV standard connectors + payload flexibility |
| 2026-08-25 | $117.86 | 1/4" Round Servo Shaft × 10 (ServoCITY-7333) | IRAD-Internal R&D | ✓ Confirmed | Mechanical actuation linkage scaling (10 units) |
| 2026-08-25 | $697.55 | IRAD VTOL supplies (general) | IRAD-Internal R&D | ✓ Confirmed | General development materials |
| 2026-08-25 | $306.77 | Dronetag DRI × 5 (drone remote ID — NREL customer) | IRAD-Internal R&D | ✓ Confirmed | Regulatory compliance + customer delivery |
| 2026