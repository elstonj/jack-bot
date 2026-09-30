# [001-13] Accounting

## Overview
- **Team**: Meredith O'hara Needham (solo owner/assignee)
- **Timeline**: Recurring monthly tasks; current open tasks due 2026-10-02 to 2026-10-30
- **Status**: Active — ongoing monthly accounting operations
- **Risk signals**: 
  - **CRITICAL PATTERN**: Systematic completion delay — entire batches of tasks (across multiple cycles) completed on single date (2026-09-28) regardless of original due dates
  - Tasks spanning July–September due dates all marked complete 2026-09-28, indicating backlog catch-up or bulk completion event
  - Current cycle (October) showing 9 open tasks with earliest due date 2026-10-02
  - **Stale task**: "Check Late Invoices every Monday" due 2026-09-14 still open (likely residual from previous cycle)
  - **Duplicate tasks**: "Make sure all paid invoices are recorded in QB" appears twice in current open set (due 2026-10-02 and 2026-07-27)

## Key Deliverables & Milestones
Monthly recurring cycle:
1. **Pay Outstanding Invoices** — Monthly | Due: 2026-10-02
   - Process: Review unpaid invoices in Gmail folder and pay in Quickbooks
   - Note: Task consistently marked "Started, incomplete" even when completed
2. **Record Payroll in Quickbooks** — Monthly | Due: 2026-10-02
   - Process: Record payroll true wages and taxes from banking feed + Rippling Payroll Report
   - SOP: https://docs.google.com/document/d/1vGjlPEUN_BA
3. **Update Fundraising Financial Reports** — Monthly | Due: 2026-10-02
   - Process: Update reports with previous month's data
   - Location: https://drive.google.com/drive/folders/1HloGsiJWk8hx6AIyN5yCVwC
4. **Make sure all paid invoices are recorded in QB** — Monthly | Due: 2026-10-02
5. **Reconcile CC** — Monthly | Due: 2026-10-19
6. **Run Monthly P/L** — Monthly | Due: 2026-10-30
7. **Pay Wages to MyFAMLI+** — Quarterly | Due: 2026-10-03
   - Process: Login to https://famli.colorado.gov/employers and enter total wages for quarter
   - Note: Amount due listed after login
8. **Check Late Invoices every Monday** — Weekly | Due: 2026-09-14 (OVERDUE/STALE)

## Task Summary
- **Total**: 47 tasks (9 open, 38 completed)
- **Assignee**: Meredith O'hara Needham (100% of tasks)
- **Open tasks (October cycle)**:
  - Pay Outstanding Invoices (due 2026-10-02)
  - Record Payroll in Quickbooks (due 2026-10-02)
  - Update Fundraising Financial Reports (due 2026-10-02)
  - Make sure all paid invoices are recorded in QB × 2 (due 2026-10-02 and 2026-07-27)
  - Pay Wages to MyFAMLI+ (due 2026-10-03)
  - Reconcile CC (due 2026-10-19)
  - Run Monthly P/L (due 2026-10-30)
  - Check Late Invoices every Monday (due 2026-09-14 — STALE)
- **Completion pattern**: Anomaly detected — 20+ completed tasks across July–September cycles all marked complete on 2026-09-28 (single bulk completion event), suggesting Asana was updated after work was already completed or backlog catch-up occurred

## Recent Activity
- **2026-09-28**: Bulk completion event — 20+ tasks marked complete on this single date, covering work originally due across July, August, and September
  - Completed tasks include multiple cycles of: Pay Outstanding Invoices, Make sure all paid invoices recorded, Reconcile CC, Run Monthly P/L, Check Late Invoices, Record Payroll, Update Fundraising Reports
  - All marked complete despite being "Started, incomplete" or "Not started" in status field
- **Current**: October 2026 cycle tasks now open
  - 5 tasks due 2026-10-02 (compressed deadline)
  - Quarterly MyFAMLI+ task due 2026-10-03
  - One stale task (Check Late Invoices) from September still open (due 2026-09-14)

## Notes & Context
- **Status field anomaly**: Multiple completed tasks retain "Started, incomplete" or "Not started" status even after completion date recorded — suggests workflow not properly closing tasks or custom status not being updated
- **Duplicate task**: "Make sure all paid invoices are recorded in QB" appears twice in open list with different due dates (2026-10-02 and 2026-07-27). The 2026-07-27 due date is stale; may indicate task template duplication or manual task creation error
- **Workload compression**: 5 core monthly tasks all due 2026-10-02, plus quarterly MyFAMLI+ task due 2026-10-03 creates mid-month spike
- **Process dependencies**: Tasks rely on external systems (Gmail folders, Quickbooks, Rippling Payroll, Colorado FAMLI portal, Google Drive) requiring manual review and data entry
- **Rippling integration note**: Payroll task explicitly cross-references Rippling Payroll Report; consider whether Rippling can provide direct QB sync to reduce manual step
- **Weekly monitoring task**: "Check Late Invoices every Monday" is recurring weekly but appears infrequently in completed list — may indicate inconsistent execution or task not being regenerated properly
- **Recommendation**: 
  - Consolidate October 2026-10-02 tasks into single "Monthly Close" batch to reduce scheduling friction
  - Clean up duplicate task (2026-07-27 stale due date)
  - Review whether Quickbooks or Rippling offer automation to reduce manual reconciliation burden
  - Clarify task status field usage — either update custom status on completion or remove field if not actionable