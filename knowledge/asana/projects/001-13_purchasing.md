_Asana snapshot as of 2026-11-11: 184 open tasks, 0 completed (last 90 days)._

# [001-13] Purchasing

## Overview
- **Owner:** Meredith O'hara Needham
- **Team:** Whole BST team (distributed requesters)
- **Status:** Active — high-volume purchasing operations
- **Dollar value:** Not explicitly totaled in custom fields; significant aggregate spend across 184 open purchase orders
- **Timeline:** Ongoing operational purchasing; orders span July 2026–November 2026 with some inventory-stage orders due Dec 2026–Jan 2027
- **Risk signals:** 
  - **184 open tasks with 0 completed** — substantial backlog with no closure tracking
  - Many orders marked "Order Received" or "Order Placed in Inventory" but remain open in Asana (likely requires manual closure workflow)
  - Several overdue orders (e.g., McMaster from Feb 2025, orders with "placed" dates in July–Aug 2026 still open in Nov 2026)
  - Multiple orders for MULTIPLE PROJECTS without project breakdown specified — billing ambiguity

## Key Deliverables & Milestones
This is a purchasing operations tracker, not a project with discrete deliverables. Workflow milestones:
1. **Order placement** — Requesters submit via Asana form or external systems
2. **Order placed status** — Vendor confirmation
3. **Order shipped status** — In transit
4. **Order received status** — Goods arrived
5. **Closure** — Currently not implemented; tasks remain open indefinitely

### Notable Order Clusters
- **IRAD projects** ([001-3], [001-4], [001-7], [001-16]): Jawstec, Mouser, Digikey, McMaster, SendCutSend
- **S3 Sales & INSTAAR** ([451-1]): Jawstec, MKS servos, Sendcutsend, Clearwater composites
- **Hurricane/IDIQ** ([300-3]): Microhard, Digikey, Mouser, Protolabs, Craftcloud
- **Shop supplies (ongoing):** Amazon, McMaster, Pololu, Powerwerx
- **SOCOM Pope II** ([600-01]): Aegis/Videology, Commonlands, Amazon, McMaster
- **Navy SBIR Magnetometer** ([550-1]): GetFPV, Digikey, Bartington sensors

## Task Summary
- **Total:** 184 open, 0 completed
- **Primary assignee:** Meredith O'hara Needham (most tasks), with ~40 unassigned
- **Requesters (by frequency):**
  - Joshua Fromm: ~110 orders (S3, Hurricane, multi-project, shop supplies)
  - Alex: ~20 orders (S0 VTOL, GCS, Swiftstation, Navy SBIR, SOCOM)
  - Sam: ~15 orders (S3, Hurricane, Shop supplies, Navy SBIR)
  - Others: Dan, Spencer, Ethan, Nate, Nathaniel Straus (1–5 orders each)

- **Order status distribution:**
  - Order Placed: ~15
  - Order Shipped: ~5
  - Order Received: ~25
  - Order Placed in Inventory: ~130
  - No status specified: ~9

- **Tax exempt:** Heavily used (majority marked YES for sales projects, NO for shop/internal)
- **Approval required:** Only 1 order flagged (ADS-B for S30002)

## Recent Activity
- **Last 30 days (as of mid-Nov 2026):**
  - Multiple orders due Nov 11–12, 2026 for S3 sales (Jawstec, ACP Composites, CST Sales, FLIR Camera, PTC motor grounding)
  - Orders received Nov 1–12 from Amazon, DigiKey, McMaster (Shop supplies, multiple projects)
  - One task with historical due date Feb 24, 2025 (McMaster for [039-1] S2 Oklahoma) — likely stale
  
- **Completion pattern:** No tasks marked complete; workflow appears to be "log order → track status → leave open indefinitely"

## Notes & Context

### Process Issues
1. **No closure workflow:** Orders marked "Order Received" or "Order Placed in Inventory" should be closed but remain open. This creates false sense of pending work.
2. **Multi-project ambiguity:** ~15 orders tagged "MULTIPLE PROJECT - PLEASE PROVIDE BREAKDOWN IN THE DESCRIPTION" lack project allocation detail, complicating billing.
3. **Form compliance:** Project notes state "USE THIS FORM PLEASE OR YOUR TASK WILL AUTO DELETE" — suggests some enforcement, but form submission quality varies (many incomplete project fields in notes).

### Custom Field Usage
- **Status field:** Tracks order lifecycle (Order Placed → Order Shipped → Order Received → Order Placed in Inventory)
- **Tax Exempt:** Consistently populated; used to segregate sales vs. operational purchases
- **Requires Approval:** Minimal use; only large orders flagged
- **Name of requester:** Always filled; enables requester accountability
- **Project field:** Critical for billing but often incomplete or multi-project

### Vendor Summary (top recurring)
- **Jawstec:** ~20 orders (parts for multiple IRAD, S3, Hurricane)
- **McMaster Carr:** ~15 orders (hardware, shop supplies)
- **Digikey:** ~10 orders (electronics, multiple projects)
- **Amazon:** ~15 orders (convenience items, supplies)
- **Mouser:** ~8 orders (electronics)
- **Sendcutsend/Protolabs/Craftcloud:** Fabrication services
- **Specialized:** Microhard (communications), Bartington (sensors), Jawstec (airframe parts)

### Recommendations
- **Implement order closure:** Define clear trigger for marking tasks complete (e.g., invoice received, goods verified, billing recorded).
- **Enforce project tagging:** Reject multi-project orders at form submission until requester specifies allocation.
- **Archive old orders:** Orders from May–July 2026 marked "received" should be closed to reduce clutter.
- **Clarify inventory status:** "Order Placed in Inventory" is ambiguous — does this mean received and in stock, or pending receipt?