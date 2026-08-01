# Sam Hild — Email Patterns

## Communication Volume
- **Total messages scanned:** 162 emails (39 new + 123 previously documented)
- **Date range:** 25 Jul 2026 – 01 Aug 2026 (8 days)
- **Volume pattern:** Massive procurement spike on 31 Jul (27/39 new messages = 69% of daily traffic). Clear shift from technical troubleshooting phase (29–30 Jul) to inventory/manufacturing fulfillment phase (31 Jul–01 Aug). 01 Aug shows cooling trend (4 messages, mostly transactional). Pattern suggests: coordinated component ordering across multiple vendors, manufacturing readiness, and system buildout cycle.

## Key Correspondents

### Senders (Incoming — Updated)

**Human Senders (Direct Communication):**

1. **Jack Elston** (elstonj@blackswifttech.com) — **3 new messages, 31 Jul** — Technical/procurement coordination
   - "Re: Additional orders" thread (10:37 UTC, 12:22 UTC, 19:45 UTC)
   - All [IMPORTANT] flagged
   - CC'd with Matt Crabtree (Waveform Engineering) and Sam Hild directly on 17:08 UTC message
   - Status: Active real-time coordination on component sourcing with external engineering partner

2. **Matt Crabtree** (matt.crabtree@waveformengineering.com) — **2 new messages, 31 Jul** — External technical partner
   - "RE: Additional orders" (01:38 UTC, 17:08 UTC)
   - Both [IMPORTANT] flagged
   - Direct communication to Jack Elston + Sam Hild CC
   - Status: Elevated to active participant in procurement decisions (not just receiving forwarded emails)

3. **Meredith Needham** (meredith.needham@blackswifttech.com) — **3 new messages, 31 Jul** — Operations/vendor coordination
   - Green Apple Cleaning follow-up (11:47 & 11:22 UTC) — facility services negotiation
   - Framework.work order status inquiry (09:18 UTC) — computing hardware tracking
   - Status: Continued vendor management and customer support routing

**Automated/Transactional (31 new messages — Manufacturing/Component Surge):**

**Manufacturing & Fabrication Services (9 messages):**
- **Protolabs** (4 messages, 31 Jul) — Order 5184-903 & 6794-871 (received → ready for manufacturing → shipped) + Invoice 100-A000840621 (01 Aug). **SIGNAL: Two concurrent orders, one shipping, one in manufacturing queue**
- **SendCutSend** (1 message, 31 Jul) — Order received ("here's what's next" status)
- **Craftcloud** (1 message, 31 Jul) — Invoice for Order #490602963468 (manufacturing service)
- **JawsTec Manufacturing** (4 messages, 31 Jul) — Orders #70260 & #70261 (dual concurrent orders, payment requests + confirmations). **SIGNAL: High-volume manufacturing orders with invoice tracking**

**RC/Propulsion Components (7 messages):**
- **ServoCity** (4 messages, 31 Jul) — Order #300046306 (order confirmation → updated → updated again → updated). **SIGNAL: Multiple status changes on single order; possibly high-priority**
- **APC Propellers** (1 message, 31 Jul) — Order received
- **Hitec RCD USA** (2 messages, 31 Jul) — Order #5791 (confirmation + status update)

**Specialized Aviation/Sensor Components (3 messages):**
- **IR-LOCK** (2 messages, 31 Jul) — Order #28043 (confirmed + shipment notification) [IMPORTANT]. **SIGNAL: Infrared optical systems; likely vision/guidance component**
- **Dronetag s.r.o.** (1 message, 31 Jul) — Payment accepted (drone identification/tracking system)

**Electronics Distribution (2 messages):**
- **DigiKey** (2 messages, 31 Jul) — Order #100742193 (PO acknowledgement + thank you). **SIGNAL: High-value component electronics order**

**Supply/Specialty Items (4 messages):**
- **SkyGeek** (1 message, 01 Aug) — "Polyurethane Topcoats for Lasting Performance" (routed to Joshua Fromm/purchasing)
- **eBay** (2 messages, 31 Jul) — Futaba 14SG & T14SG inquiries (RC transmitters — continued monitoring)
- **Toggl Track** (1 message, 31 Jul) — Time tracking platform (no subject; direct to Sam Hild)

**Other Transactional:**
- **Rippling** (1 message, 31 Jul) — Payroll confirmation (7/1–7/31 payment)

### Recipients (Updated)
- **purchasing@blackswifttech.com** (26/39 new messages routed through purchasing account — primary vendor funnel)
- **Jack Elston** (elstonj@blackswifttech.com) — 3 direct exchanges on "Additional orders"
- **Matt Crabtree** (matt.crabtree@waveformengineering.com) — 2 messages, now elevated to direct participant (not just recipient)
- **Meredith Needham** — 3 messages (vendor coordination, Framework support, Green Apple Cleaning)
- **Joshua Fromm** (joshua@greenapplecleaningcrew.com, purchasing@blackswifttech.com) — Receives SkyGeek & Craftcloud routing
- **Maciej Stachura** (purchasing@blackswifttech.com) — Receives Protolabs manufacturing updates
- **Alex Lomis** (purchasing@blackswifttech.com) — Receives Dronetag payment confirmations
- **Sam Hild** (direct) — Receives Toggl Track & Rippling notifications; CC'd on Matt Crabtree "Additional orders" messages

### Internal vs External (Updated)
- **External:** 31/39 messages (vendors, manufacturers, component suppliers)
- **Internal:** 8/39 messages (Jack Elston x3, Meredith Needham x3, Sam Hild x1 [Toggl Track direct], Rippling x1)
- **Key internal routing:** Jack Elston ↔ Matt Crabtree coordination visible in "Additional orders" thread (elevated from previous CC-only pattern)

## Topic Patterns

### Manufacturing & Production (NEW — Major Signal)

**Concurrent Manufacturing Orders (31 Jul surge):**

1. **Protolabs** (Precision machining/custom parts)
   - Order 5184-903: Received 16:54 UTC → Ready for manufacturing 18:17 UTC → Shipped 15:07 UTC (01 Aug)
   - Order 6794-871: Shipping confirmation 15:07 UTC
   - Suggests: Multiple precision components in manufacturing pipeline; 24-48 hour turnaround indicates rush/priority orders

2. **JawsTec Manufacturing** (Custom fabrication)
   - Order #70260 & #70261 (parallel orders)
   - Both received & invoiced same day (16:42–16:45 UTC)
   - Payment requests issued immediately
   - Suggests: Capacity planning or bulk component production

3. **SendCutSend** (Sheet metal/laser cutting)
   - Order received & in production queue
   - Complements Protolabs precision work

4. **Craftcloud** (Distributed manufacturing network)
   - Order #490602963468 invoiced same day

**Production Interpretation:**
- 4 concurrent manufacturing services (Protolabs, JawsTec, SendCutSend, Craftcloud) all receiving/confirming orders within 6-hour window (31 Jul 16:42–16:58 UTC)
- **Pattern suggests:** Coordinated kit/system assembly — precision parts, custom fabrication, sheet metal, and distributed manufacturing all activated simultaneously
- **Timeline:** Components ordered/confirmed 31 Jul afternoon; Protolabs shipping 01 Aug → suggests 8–16 hour expedited fulfillment