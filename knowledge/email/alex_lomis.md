# Alex Lomis — Email Patterns

## Communication Volume
- **Total messages scanned:** 346 emails (325 from prior period + 21 new from 30–31 May)
- **Date range:** 18–31 May 2026 (14 days)
- **Approximate volume:** Sustained high-velocity operational/logistics messaging with **critical escalation on 30–31 May.** 30 May: ~13 emails (8 DHL shipment notifications for single tracking #4789316906, 2 promotional/gear alerts, 1 container quote, 1 USPS digest, 1 McMaster receipt). 31 May: ~8 emails (1 DHL import duty payment "Last Reminder" marked IMPORTANT, 6 DHL duplicate shipment notifications, 1 SendCutSend shipment alert).

## Key Correspondents

### Internal Government/Military Project Coordination (No new emails 30–31 May)
- **Maciej Stachura** — Sustained (prior: S0 MAD proposal coordination with Navy)
- **Joshua Fromm, Daniel Prendergast, Ethan Domagala** — Sustained (Atmolab camera integration)
- **Jack Elston** — Expanded purchasing role (battery orders)

### External Government/Military (No new activity 30–31 May)
- **Angel R. Ruiz-Reyes (CIV USN NAWCAD)** — Last contact 29 May; awaiting response

### External Logistics/Shipping (ESCALATED ACTIVITY)

**DHL Express — CRITICAL SIGNAL**
- **Tracking #4789316906:** 9 duplicate shipment notifications (30–31 May, MYT timezone 03:35–22:07)
  - 30 May: 7 notifications (16:42, 16:42, 18:52, 22:04, 22:07 MYT)
  - 31 May: 2 additional notifications (03:35, 04:36, 07:41, 08:43, 08:47, 11:02 MYT — **6 total on 31 May alone**)
  - **Duplicate pattern anomaly:** Same tracking number, repeated status updates across MYT timezone (8-hour offset from UTC)
  - **CRITICAL:** 31 May 04:13 UTC — **"Import Duty Payment Alert – Last Reminder"** flagged IMPORTANT and UNREAD
  - **Signal:** High-value Asia-Pacific shipment in customs clearance; payment bottleneck creating recurring notifications; urgency escalating (last-reminder language)
  - **Implication:** Mission-critical component delayed; likely same shipment routed from PCBWay (29 May MYT timestamp observed in prior data)

**SendCutSend**
- 31 May 06:05 UTC — "A shipment from SendCutSend is on the way"
- **Pattern:** Routed to purchasing@; active sheet metal/fabrication orders in transit

**McMaster-Carr**
- 30 May 03:16 UTC — Receipt for May 29th order
- **Sustained high-volume procurement**

### External Specialist/Hobby Vendors (NEW 30–31 May Activity)

**GetFPV** (getfpv.com)
- 30 May 18:06 UTC — "Your gear is waiting for you" (marked IMPORTANT)
- **Signal:** Possibly camera, gimbal, or FPV-related components; direct to Alex (not routed through purchasing@)
- **NEW contact pattern:** First appearance; suggests personal/technical review procurement

**eBay Search Alerts** (routed to purchasing@)
- 30 May 06:08 — "sony a5100, New: 1 NEW!" (camera body)
- 30 May 06:08 — "futaba 14sg, Receivers & Transmitters: 1 NEW!" (RF/radio control equipment)
- **Signal:** Passive market monitoring on specific components (camera + radio control systems); likely for VTOL payload or flight control system alternatives
- **Implication:** Shopping for backup/secondary components or evaluating vendor options

**Air Sea Containers** (czufra@airseadg.com)
- 30 May 14:55 UTC — "RE: Air Sea Containers | Request Quote"
- **Signal:** NEW vendor contact; logistics/containerization inquiry
- **Implication:** Possible shipping/export packaging for large assemblies or multi-unit delivery

**Speedway Motors** (via purchasing@)
- 30 May 18:00 — Promotional "Hughes Performance" transmission control
- **Signal:** Routed promotional noise; likely false positive/mailing list

**Harbor Freight** (via purchasing@)
- 30 May 17:37 — Promotional "Free Gift"
- **Signal:** Promotional noise

**USPS Informed Delivery** (via purchasing@)
- 30 May 13:25 — Daily digest
- **Signal:** Passive monitoring of BST office/PO Box incoming mail

---

## Topic Patterns

### Active Project Codes (Government/Classified)
- **Arctic Edge 2027 VTOL** — Weather/environmental data collection platform
- **S0 MAD Proposal** — Navy contract; acronym "MAD" sustained; "[Non-DoD Source]" classification tag in use

### Active Hardware Integration Projects
- **Atmolab Camera System** — Atmospheric/thermal/spectral imaging payload
- **Battery/Power Systems** — BatterySpace, battery procurement accelerating
- **Custom PCB Boards** — PCBWay (Asia-sourced)
- **Motion Control/Servos** — ServoCity, Hobbywing RPM sensors (sustained)
- **Sheet Metal/Fabrication** — SendCutSend, McMaster-Carr (structural components)

### Component Categories Visible in Subject Lines
- **Cameras:** Sony A5100 (eBay alert), Atmolab camera integration, GetFPV gear
- **Radio Control/Flight Systems:** Futaba 14SG receiver/transmitter (eBay alert), likely for VTOL flight control
- **Power/Energy:** Battery procurement (BatterySpace, DIY500AMP), charging systems
- **Mechanical:** Fasteners, structural materials (McMaster-Carr), sheet metal (SendCutSend)

---

## Communication Patterns

### Time Zone Distribution
- **UTC timezone:** DHL import duty alert (04:13), SendCutSend (06:05)
- **MYT timezone (UTC+8):** 13 DHL shipment notifications concentrated 16:42–22:07 (30 May) and 03:35–11:02 (31 May)
  - **Clustering:** Multiple notifications within 1–2 hour windows suggest system error, status update loop, or customs processing events triggering repeated alerts
- **CDT/EDT (US business hours):** McMaster, DigiKey, PCBWay (29 May activity)
- **Pattern:** Heavy Asia-Pacific logistics traffic (MYT-stamped); DHL Asia gateway clearance bottleneck

### Email Routing Patterns
- **Direct to alex.lomis@blackswifttech.com:** GetFPV gear alert (personal review), DHL import duty payment alert (account-holder responsibility), prior HR/Rippling payroll
- **Routed to purchasing@blackswifttech.com:** 85% of new vendor/logistics emails; centralized procurement system; eBay searches, USPS digest, promotional alerts also routed here (suggests broad automation/monitoring setup)

### Automation & Alert Subscriptions
- **eBay saved searches:** Sony A5100 + Futaba 14SG (component sourcing)
- **USPS Informed Delivery:** Office mail monitoring
- **DHL shipment tracking:** Automated notifications (duplicate pattern suggests subscribed to all status updates)
- **Vendor promotional subscriptions:** Speedway Motors, Harbor Freight (via purchasing@ — likely noise or broad team subscriptions)

---

## Key Relationships

### Internal Collaboration Hierarchy (by 29 May activity)
1. **Maciej Stachura** (stachura@blackswifttech.com) — Primary Navy/government contact; direct interface with NAWCAD
2. **Joshua Fromm, Daniel Prendergast** — Co-leads on Atmolab camera