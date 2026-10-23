"""Offline regression suite for Asana incremental scanning.

Replays the failure where an incremental scan overwrote
asana/projects/001-13_accounting.md (four open tasks) with "Small project with
1 tasks. Reconcile CC": the scanner distilled only the tasks modified since
the last scan. Also checks that summary.md covers every project, not just the
ones rebuilt this run, and that truncated model output is never written.
Needs no credentials. Run: python test_asana_snapshot.py
"""

import json
import pathlib
import tempfile
from types import SimpleNamespace

import scanners.asana_scanner as sc
import scanners.base as base

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


def task(name, completed=False):
    return {"gid": name, "name": name, "completed": completed,
            "completed_at": "2026-10-01T00:00:00Z" if completed else None,
            "assignee": {"name": "Meredith Needham"}}


ACCOUNTING = [task("MyFAMLI+"), task("Pay Outstanding Invoices"),
              task("QB recording"), task("Reconcile CC")]


def fake_fetch(project_gid, include_completed=True, modified_since=None,
               completed_since=None):
    if modified_since:
        return [ACCOUNTING[-1]]  # only Reconcile CC changed
    return list(ACCOUNTING)


def run_scan(tmp, existing=True, corrections=None):
    sc.PROJECTS_DIR = tmp / "projects"
    sc.ASANA_KNOWLEDGE_DIR = tmp
    sc.INDEX_FILE = tmp / ".index.json"
    sc.PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    path = sc.PROJECTS_DIR / "001-13_accounting.md"
    if existing:
        path.write_text("# [001-13] Accounting\n\nold content\n")
    sc._get_project_details = lambda gid: {}
    sc._get_all_tasks_for_project = fake_fetch
    sc.time.sleep = lambda s: None
    sc.distill_to_markdown = lambda raw, system, out, max_tokens=2000, merge=True: raw
    project ={"gid": "1", "name": "[001-13] Accounting"}
    result = sc.scan_project(project, mode="incremental",
                             modified_since="2026-10-15T00:00:00",
                             corrections=corrections)
    return result, path


def test_incremental_writes_full_snapshot():
    print("incremental rebuild uses the full task list")
    with tempfile.TemporaryDirectory() as d:
        result, path = run_scan(pathlib.Path(d))
        text = path.read_text()
        check("rebuilt", result is not None, True)
        check("all four open tasks kept",
              all(t["name"] in text for t in ACCOUNTING), True)
        check("as-of stamp written by code", "_Asana snapshot as of" in text, True)
        check("stamp counts the snapshot", "4 open tasks" in text, True)
        index = json.loads((pathlib.Path(d) / ".index.json").read_text())
        check("index records counts", index["001-13_accounting.md"]["open"], 4)


def test_unchanged_project_skipped():
    print("unchanged project is not rewritten")
    with tempfile.TemporaryDirectory() as d:
        original = sc._get_all_tasks_for_project
        sc._get_all_tasks_for_project = lambda *a, **k: []
        tmp = pathlib.Path(d)
        sc.PROJECTS_DIR = tmp / "projects"
        sc.INDEX_FILE = tmp / ".index.json"
        sc.PROJECTS_DIR.mkdir()
        path = sc.PROJECTS_DIR / "001-13_accounting.md"
        path.write_text("keep me")
        sc._get_project_details = lambda gid: {}
        result = sc.scan_project({"gid": "1", "name": "[001-13] Accounting"},
                                 mode="incremental",
                                 modified_since="2026-10-15T00:00:00")
        sc._get_all_tasks_for_project = original
        check("skipped", result, None)
        check("file untouched", path.read_text(), "keep me")


def test_summary_covers_every_project():
    print("summary lists projects not rebuilt this run")
    with tempfile.TemporaryDirectory() as d:
        tmp = pathlib.Path(d)
        run_scan(tmp)
        (sc.PROJECTS_DIR / "550-1_magnetometer.md").write_text("# [550-1]\n")
        sc.get_claude_client = lambda: SimpleNamespace(messages=SimpleNamespace(
            create=lambda **k: SimpleNamespace(content=[SimpleNamespace(text="summary")])))
        sc._generate_summary()
        summary = (tmp / "summary.md").read_text()
        check("total counts every file", "Total projects: 2" in summary, True)
        check("unrebuilt project listed", "550-1_magnetometer.md" in summary, True)
        check("rebuilt project shows real counts",
              "4 open, 0 completed" in summary, True)


def test_empty_project_overwrites_stale_file():
    print("a project with nothing in the window replaces its old file")
    with tempfile.TemporaryDirectory() as d:
        tmp = pathlib.Path(d)
        sc.PROJECTS_DIR, sc.INDEX_FILE = tmp / "projects", tmp / ".index.json"
        sc.PROJECTS_DIR.mkdir()
        path = sc.PROJECTS_DIR / "001-13_compliance.md"
        path.write_text("Small project with 1 tasks.\n- [Open] stale task\n")
        sc._get_project_details = lambda gid: {}
        sc._get_all_tasks_for_project = lambda *a, **k: []
        sc.scan_project({"gid": "1", "name": "[001-13] Compliance"}, mode="1yr")
        text = path.read_text()
        check("stale task gone", "stale task" in text, False)
        check("stamped empty", "0 open tasks" in text, True)


def test_orphans_bannered_once():
    print("files for projects no longer in Asana are bannered, not deleted")
    with tempfile.TemporaryDirectory() as d:
        sc.PROJECTS_DIR = pathlib.Path(d)
        (sc.PROJECTS_DIR / "current.md").write_text("live")
        (sc.PROJECTS_DIR / "old_name.md").write_text("old")
        sc._mark_orphans({"current.md"})
        sc._mark_orphans({"current.md"})
        check("current untouched", (sc.PROJECTS_DIR / "current.md").read_text(), "live")
        old = (sc.PROJECTS_DIR / "old_name.md").read_text()
        check("orphan bannered once", old.count(sc.ORPHAN_BANNER), 1)
        check("orphan content kept", old.endswith("old"), True)


def test_truncated_output_not_written():
    print("truncated distillation never overwrites a file")
    calls = []

    def create(**kwargs):
        calls.append(kwargs["max_tokens"])
        return SimpleNamespace(stop_reason="max_tokens",
                               content=[SimpleNamespace(text="cut off mid-sent")])

    base.get_claude_client = lambda: SimpleNamespace(
        messages=SimpleNamespace(create=create))
    with tempfile.TemporaryDirectory() as d:
        path = pathlib.Path(d) / "f.md"
        path.write_text("good")
        got = base.distill_to_markdown("raw", "sys", path, max_tokens=100)
        check("returns None", got, None)
        check("existing file kept", path.read_text(), "good")
        check("retried with double budget", calls, [100, 200])


if __name__ == "__main__":
    test_incremental_writes_full_snapshot()
    test_unchanged_project_skipped()
    test_summary_covers_every_project()
    test_empty_project_overwrites_stale_file()
    test_orphans_bannered_once()
    test_truncated_output_not_written()
    if FAILURES:
        raise SystemExit(f"\n{len(FAILURES)} failure(s)")
    print("\nall asana snapshot checks passed")
