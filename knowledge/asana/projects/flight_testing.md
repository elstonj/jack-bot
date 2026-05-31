# Flight Testing

## Overview
- **Client/Customer:** Internal BST project
- **Timeline:** Active flight testing operations; all current tasks completed as of March 2024
- **Status:** Active — templates and test procedures established; all current tasks completed
- **Team members:** Maciej Stachura, Nate Straus
- **Risk signals:** None — no open tasks or overdue items

## Key Deliverables & Milestones
- **S10019 Controller Test** — Completed 2024-02-29 (Maciej Stachura)
  - Reusable milestone template with standardized pre-flight, in-flight, and post-flight checklist
  - Includes vehicle-specific fix checks, code updates (Autopilot, Tablet), flight readiness checks, and post-flight procedures
- **S10019 Wind Test** — Completed 2024-02-29 (Maciej Stachura)
  - Reusable milestone template with battery charging, payload checks, flight readiness, log upload, and post-flight procedures
  - References vehicle inventory projects (Multi-rotor, S1, S2) for aircraft-specific tasks
- **S01001 Hover Test** — Completed 2024-02-29 (Maciej Stachura)
  - Template for testing
- **FW0001, FW0002, S10005, S10011** — Completed 2024-03-08 (Nate Straus)
  - Template validation and refinement tasks

## Task Summary
- **Total tasks:** 0 open, 8 completed (plus 16+ completed subtasks)
- **Assignees:**
  - Maciej Stachura: 3 main tasks + 2 milestones (S01001 Hover Test, S10019 Controller Test, S10019 Wind Test, S10019 Winds) — 100% complete
  - Nate Straus: 4 template tasks (FW0001, FW0002, S10005, S10011) — 100% complete
  - Unassigned: 16 subtasks across milestones (all completed)

## Recent Activity
- **2024-03-11:** Maciej Stachura completed S10019 Winds task with note "Template for testing. Removing non-applicable sections after creation"
- **2024-03-08:** Nate Straus completed four template validation tasks (S10005, FW0002, S10011, FW0001) with notes "Template for testing. Removing non-applicable sections after creation"
- **2024-02-29:** Both milestone templates (Controller Test and Wind Test) and Hover Test completed; all subtasks finalized including:
  - Code updates (Autopilot, Tablet)
  - Flight readiness checks (with conditional deletion for aircraft type)
  - Battery charging and payload checks
  - Log uploads to https://logparse.bst.aero/
  - Post-flight repair and bug tracking procedures
  - Movement through status workflow (Flight Readiness Complete → Flight Test Completed → Post Flight Completed)

## Notes & Context
The two main milestone templates (S10019 Controller Test and S10019 Wind Test) function as **reusable operational documents** for BST flight test campaigns. Active template refinement by both team members (removing non-applicable sections, conditionalizing aircraft-type-specific steps) indicates these are evolving working documents.

**Template Structure:**
- Vehicle-specific fix checks reference inventory projects by aircraft type (Multi-rotor, S1, S2)
- Code update procedures for Autopilot and Tablet components
- Conditional sections (e.g., "DELETE if not fixed wing", "DELETE if no payload testing")
- Standard log upload workflow and post-flight tracking
- Status workflow: Flight Readiness Complete → Flight Test Completed → Post Flight Completed

No dollar values tracked in Asana for this project.