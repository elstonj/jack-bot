# Meeting: S0 Build and S3 Canada Tasks Discussion

| Field | Value |
|-------|-------|
| **Date** | 2026-06-01 |
| **Source** | Google Meet / Gemini notes (internal) |
| **Attendees** | Joshua Fromm, Maciej Stachura, Alex Lomis, Daniel Prendergast, Jack Elston (Sam referenced) |
| **Primary programs** | S0 "Zero" build (SOCOM S0-AD `001_23`), Navy SBIR Magnetometer (`550_1`), S3 Canada (demo to Canadian special forces), F3 builds, S2 wings |

Planning session on hardware build timelines and August demo readiness. Main benchmark for everything below is the **August demo**.

> **"S3 Canada" = the demo to the Canadian special forces.** The S3 rebuild + S3 phase-2 work in this meeting are in service of that demo. (Whether the "August demo" referenced for the magnetometer/Navy SBIR work is this same event or a separate one is not confirmed from the notes.)

## Decisions

**ALIGNED**
- **By Light support deprioritized** — reallocating resources off ByLight M2/Halo (`043_3`) toward higher-priority builds.
- **Intern tasks must be QC-able** — interns only get work that allows formal Quality Control; Nate supervises and checks all intern output.

**SHELVED**
- **No new high-powered soldering iron** — team will use existing equipment for battery assembly. (Supersedes the "Buy soldering equipment" action item below — treat the iron purchase as cancelled, not pending.)

## Action items by owner

**Daniel Prendergast**
- Build 2 GCS rack-mount units for the multi-aircraft setup (SC + GCS builds ≈ two single-aircraft builds plus extra radios).
- Order S3 parts, incl. replacement quick-release buttons (original no longer manufactured — find alternative or machine in-house).
- Finish launcher: complete design + ordering for the prototype.
- Retrieve DXF files for wing internal components.
- Calculate purchase quantities for internal wing parts.
- Procure wing internal materials (S2, long-lead).
- Obtain additional small wheeled work tables for tool organization.
- ~~Buy a new high-power soldering iron~~ — **shelved** (see Decisions).

**Daniel Prendergast + Sam**
- Build 2 battery power packs once components arrive (one needed within the week, second by 2026-06-19). Waiting on John Tech order, expected Thu 2026-06-04; build ≈ 1 day each.

**Maciej Stachura**
- Push GPS fixes: extract GPS + throttle bug fixes from the paused branch into production code; flight-test this week ahead of demo missions.
- Perform calibration: 12 IMU alignment orientations in a magnetically clear environment — **report due Wednesday 2026-06-03**.
- Verify sensor budget: check Navy SBIR (`550_1`) Phase 2 allocation to see if team can buy additional QuSpin sensors + a ground enclosure.

**Maciej Stachura + Alex Lomis**
- Test magnetometer shielding: evaluate aircraft shielding mods to resolve sensor interference (mag performing worse in ground tests than prior months; review meeting scheduled).

**Daniel Prendergast + Josh Fromm**
- Validate sensor power: verify the S0 sensor powers on successfully.

**The group**
- Modify payloads: physical mount changes + install the gimbal camera.

## Program status notes

- **S0 "Zero" build (SOCOM S0-AD `001_23`, owner Dan Prendergast)** — batch of 25–26 units; mid-July ship target, end-of-July final deadline. Full-rate construction needs to start by 1st of month. Most parts ordered; awaiting deployment tubes and motors (motor delay shouldn't stall assembly — offramps exist for final assembly). No official build guide; configuration-management strain. S0 subcomponent assembly must finish before July, Nate overseeing QC.
- **Navy SBIR Magnetometer (`550_1`, owner Alex Lomis)** — magnetometer underperforming in ground tests vs prior months; shielding eval underway. Sensor strategy: keep **QuSpin** for primary data collection, acquire a dedicated **enclosed Bartington** unit as a standardized ground reference for environmental factors. August demo treated as a benchmark / learning opportunity to practice the certification process and operational workflows even if sensor data isn't perfect.
- **F3 builds** — two F3 aircraft on a September timeline. Procurement re-evaluating parts (quick-release buttons no longer made). Gimbal payload parts expected end of week; mounting/radio integration/telemetry doable with existing methods.
- **S3 Canada (demo to Canadian special forces)** — currently reassembling the S3 for the demo; parts from China in transit; Nate to assist with reassembly. **Phase 2 not kicked off**: difficulty sourcing a 3D-printed carbon fuselage supplier; team hesitant to invest further until project value/scope is clarified.
- **S2** — deadline 2026-09-30. Wing work started; purchasing internal components remains the long-lead task needing attention.
- **Documentation / systems engineering** — critical gaps in bill-of-materials docs (lack of exhaustive BOM forces direct involvement in every order). Build-guide / "Open BOM" creation deferred to prioritize assembly; team wants to hire a test engineer to own systems-engineering / documentation responsibilities.
