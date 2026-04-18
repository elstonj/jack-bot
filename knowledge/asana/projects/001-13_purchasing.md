# [001-13] Purchasing

## Overview
- **Client/customer:** Internal BST purchasing system (serves all active projects)
- **Dollar value:** Not explicitly tracked in individual tasks; high-volume operations across multiple projects
- **Timeline:** Ongoing operational project; current orders span Feb 2026 - Jun 2026
- **Status:** Active - critical operational load with 42 open tasks, 0 completed (100% open rate)
- **Team members involved:** 
  - Meredith O'hara Needham (primary processor - 2 assigned tasks)
  - Nate Straus (secondary processor - 1 assigned task)
  - 39 unassigned tasks (critical bottleneck)
- **Risk signals:** 
  - **CRITICAL:** 42 tasks all open with zero closures (100% backlog rate indicates severe processing bottleneck)
  - **39 unassigned tasks** in "Order Placed in Inventory" status, all due Jun 16, 2026 - major workflow stall
  - Most orders placed Feb-Apr 2026 but sitting in inventory pipeline with no closure activity
  - Heavy concentration on three core projects (Hurricane S0, NASA S2, IRAD S3) consuming majority of procurement capacity
  - Emerging Mustang Pt. 2 activity adding load (2 new orders assigned to Meredith/Nate with Apr 17-18 deadlines)
  - **Data inconsistency flag:** Knowledge file showed 24 tasks; raw data shows 42 open tasks - suggests significant backlog accumulation or data refresh

## Key Deliverables & Milestones
This is a purchasing workflow project rather than deliverable-based. It processes structured purchase requests through mandatory Asana forms (auto-delete if form not used).

**Current procurement focus areas (by project):**

### **Hurricane S0 [300-3]** — 12 open orders
- **Near-term (Apr 17-19):** Digikey hurricane/shop supplies (Meredith, due Apr 19)
- **Inventory pipeline (Jun 16):** Digikey (#97517061, #98248470), Amazon, SendCutSend, SkyGeek, Springstore, RFmall, Aloft Hobbies, best-in-parts, McMaster (mixed tax exempt/non-exempt)
- **Requester:** Joshua Fromm (primary), Nathaniel Straus, Nate
- **Tax exempt:** 8 of 12 orders (government IDIQ contract)
- **Vendor diversity:** Digikey, Amazon, SendCutSend, SkyGeek, Springstore, RFmall, Aloft Hobbies, best-in-parts, McMaster

### **NASA S2 [212-2]** — 10 open orders
- **Inventory pipeline (Jun 16):** Digikey, Pasternack, Aloft Hobbies, Jawstec, motors (KDE17071), batteries (2), fabric, aloft hobbies
- **Requester:** Joshua Fromm (all orders)
- **Tax exempt:** 8 of 10 orders (government contract)
- **Vendor diversity:** Digikey, Pasternack, Aloft Hobbies, Jawstec, battery suppliers, fabric vendors

### **IRAD S3 [001-7]** — 10 open orders
- **Inventory pipeline (Jun 16):** SendCutSend, Jawstec, amainhobbies, actuator parts (multiple), CAN fix boards (2), DroneCAN boards, power board parts, S3 actuator parts
- **Requester:** Joshua Fromm (3 orders), Sam (7 orders)
- **Tax exempt:** None (non-government project)
- **Vendor diversity:** SendCutSend, Jawstec, amainhobbies, custom electronics suppliers

### **Mustang Pt. 2 [043-3]** — 4 open orders
- **Near-term (Apr 17-18):** SendCutSend (Meredith, Apr 17), Jawstec (Meredith, Apr 17), SoaringUSA ByLight M2 props (Nate, Apr 18 - "Order Received" status)
- **Requester:** Alex (SendCutSend, Jawstec), Ethan Domagala (SoaringUSA)
- **Tax exempt:** None

### **IRAD S0 VTOL [001-4]** — 1 open order
- **Inventory pipeline (Jun 16):** FET TEC (#25761)
- **Requester:** Alex Lomis
- **Tax exempt:** No

### **IRAD General [001-1]** — 4 open orders
- **Inventory pipeline (Jun 16):** McMaster, Amazon Shop Supplies, McMaster shop supplies (0213), Powerwerx
- **Requester:** Nathaniel Straus (2 orders), Nate (2 orders)
- **Tax exempt:** No

### **IRAD Soil Moisture [001-18]** — 2 open orders
- **Inventory pipeline (Jun 16):** Jawstec, Amazon
- **Requester:** Ethan Domagala (both)
- **Tax exempt:** No

### **Shop Supplies** — 4 open orders
- **Inventory pipeline (Jun 16):** Amazon, McMaster, Lead Free Solder, Amazon
- **Requester:** Joshua Fromm (2), Nate (1), Sam (1)
- **Tax exempt:** No

## Task Summary
- **Total tasks:** 42 open, 0 completed (100% open rate)
- **Tasks by assignee:**
  - Meredith O'hara Needham: 2 tasks (SendCutSend Mustang, Jawstec Mustang - both Apr 17)
  - Nate Straus: 1 task (SoaringUSA ByLight M2 - Apr 18, "Order Received" status)
  - Unassigned: 39 tasks (93% of backlog - **CRITICAL BOTTLENECK**)
- **Notable patterns:**
  - **Order status distribution:** 
    - "Order Placed": 1 task (Digikey hurricane/shop, Apr 19)
    - "Order Received": 1 task (SoaringUSA M2 props, Apr 18)
    - "Order Placed in Inventory": 40 tasks (95% of backlog - stalled pipeline)
  - **Due date clustering:** 
    - **Immediate (Apr 17-19):** 4 tasks assigned to Meredith/Nate
    - **Massive future pile-up (Jun 16):** 38 unassigned tasks in "Order Placed in Inventory" status
  - **Tax exemption:** 16 of 42 orders marked tax exempt (government contracts: Hurricane S0, NASA S2)
  - **Primary requesters:** 
    - Joshua Fromm: 23 tasks (Hurricane S0, NASA S2, IRAD S3, IRAD General, Shop Supplies, IRAD Soil Moisture)
    - Sam: 8 tasks (IRAD S3 electronics, Shop Supplies solder)
    - Nate/Nathaniel Straus: 5 tasks (Hurricane, IRAD General, Shop Supplies)
    - Ethan Domagala: 3 tasks (Mustang Pt. 2, IRAD Soil Moisture)
    - Alex: 2 tasks (Mustang Pt. 2 - SendCutSend, Jawstec)
    - Alex Lomis: 1 task (IRAD S0 VTOL)
- **Vendor ecosystem:** 
  - Electronics: Digikey (11 orders), Pasternack, Jawstec (5), amainhobbies
  - Fabrication: SendCutSend (3), Aloft Hobbies (3)
  - Hobbies/components: SoaringUSA, Aloft Hobbies, Amainhobbies, RFmall, best-in-parts
  - General: Amazon (6), McMaster (3)
  - Specialty