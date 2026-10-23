#!/usr/bin/env python3
"""Build a scrubbed copy of knowledge/ for the team's "Ask Black Swift
Technologies" Claude project.

That project is shared with every team member, so this keeps work information
(projects, tasks, budgets, project financials, channel summaries, proposals)
and drops personal information:

- Whole sources that are personal by nature are never read: per-person email
  digests, Toggl hours, the contact directory, QuickBooks transactions,
  per-person cost/rate breakdowns, purchases, bot internals.
- Whole files are dropped when they are payroll/expense documentation, HR /
  PTO / sick-leave projects, or carry export-control or CUI markings (those
  must not go to a third-party workspace at all).
- Within kept files, lines are dropped when they trip privacy_guard's
  compensation / medical / personnel / legal / M&A patterns (plus
  PRIVACY_EXTRA_TERMS), or pair an employee's name with a pay rate. Email
  addresses and phone numbers are masked.

Output is a handful of bundled markdown files in export/claude_project/ (few
large files upload far more reliably than ~3,000 small ones), plus
_excluded.md listing every dropped file and why. That manifest stays local —
review it, never upload it.

Usage: python scripts/export_claude_project.py [--out DIR]
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_DIR))

from privacy_guard import contains_sensitive, is_personnel_record  # noqa: E402

KNOWLEDGE = PROJECT_DIR / "knowledge"
DEFAULT_OUT = PROJECT_DIR / "export" / "claude_project"

# Bundle name -> globs under knowledge/. Anything not listed is not exported.
BUNDLES = {
    "projects": ["projects/*.md"],
    "asana_tasks": ["asana/summary.md", "asana/projects/*.md"],
    "budgets": ["budgets/*.md"],
    "project_financials": ["financial/overview.md", "financial/by_project/*.md"],
    "slack_channels": ["slack/*.md"],
    "drive_and_meetings": ["drive/*.md", "meetings/*.md"],
    "proposals": ["proposals/*.md"],
}

# Keep each bundle part well under the project upload limit.
MAX_PART_BYTES = 4_000_000

# Project knowledge holds ~7.5 MB in total and the full proposals text is
# ~13 MB, so proposals export as a digest: title, metadata and executive
# summary, capped per file. Every proposal stays findable; the full text
# stays in Jack Bot.
DIGEST_BUNDLES = {"proposals"}
DIGEST_SECTIONS = 2
DIGEST_MAX_CHARS = 1200


def _digest(text):
    """Leading sections of a proposal (metadata + executive summary), capped."""
    out, sections, size = [], 0, 0
    for line in text.splitlines():
        if line.startswith("## "):
            sections += 1
            if sections > DIGEST_SECTIONS:
                break
        if size + len(line) > DIGEST_MAX_CHARS:
            break
        out.append(line)
        size += len(line) + 1
    return "\n".join(out)

_RESTRICTED = re.compile(
    r"Distribution Statement [B-F]\b|CUI//|\bCUI\b.{0,40}\bmarking"
    r"|ITAR[- ]controlled|subject to (?:the )?ITAR|export[- ]controlled"
    r"|controlled unclassified information|NOFORN|\bFOUO\b",
    re.I,
)
_EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")
_PHONE = re.compile(r"(?<!\d)(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]\d{3}[-.]\d{4}(?!\d)")
_RATE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?\s?(?:/\s?h(?:ou)?r|per hour)", re.I)
_LAST_FIRST = re.compile(r"\b[A-Z][a-z]+, [A-Z][a-z]+\b")


def _employee_names():
    """First and last names from the roster, for rate-line screening."""
    roster = KNOWLEDGE / "contacts" / "employees.md"
    names = set()
    if roster.exists():
        for m in re.finditer(r"^- \*\*([^*]+)\*\*", roster.read_text(), re.M):
            names.update(p for p in m.group(1).split() if len(p) > 2)
    return names


def _scrub_lines(text, employee_re):
    kept, dropped = [], 0
    for line in text.splitlines():
        if contains_sensitive(line) or (
            _RATE.search(line)
            and (employee_re.search(line) or _LAST_FIRST.search(line))
        ):
            dropped += 1
            continue
        line = _EMAIL.sub("[email]", line)
        kept.append(_PHONE.sub("[phone]", line))
    return "\n".join(kept), dropped


def build(out_dir):
    names = _employee_names()
    employee_re = re.compile(
        r"\b(?:" + "|".join(map(re.escape, sorted(names))) + r")\b"
    ) if names else re.compile(r"(?!x)x")

    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()

    scan_state = KNOWLEDGE / ".scan_state.json"
    as_of = date.today().isoformat()
    if scan_state.exists():
        stamps = [v for v in json.loads(scan_state.read_text()).values()
                  if isinstance(v, str)]
        if stamps:
            as_of = max(stamps)[:10]

    excluded = []
    stats = {}
    for bundle, globs in BUNDLES.items():
        files = sorted({p for g in globs for p in KNOWLEDGE.glob(g)})
        parts, current, size = [], [], 0
        lines_dropped = 0
        for path in files:
            rel = path.relative_to(KNOWLEDGE)
            text = path.read_text(errors="replace")
            if is_personnel_record(path.name, text):
                excluded.append((rel, "payroll/HR/leave document"))
                continue
            if _RESTRICTED.search(text):
                excluded.append((rel, "export-control / CUI marking"))
                continue
            if bundle in DIGEST_BUNDLES:
                text = _digest(text)
            body, dropped = _scrub_lines(text, employee_re)
            lines_dropped += dropped
            if not body.strip():
                continue
            chunk = f"\n\n---\n<!-- source: knowledge/{rel} -->\n\n{body}\n"
            if current and size + len(chunk) > MAX_PART_BYTES:
                parts.append(current)
                current, size = [], 0
            current.append(chunk)
            size += len(chunk)
        if current:
            parts.append(current)

        for i, chunks in enumerate(parts, 1):
            suffix = f"_part{i}" if len(parts) > 1 else ""
            header = (
                f"# BST knowledge: {bundle.replace('_', ' ')}{suffix.replace('_', ' ')}\n\n"
                f"Knowledge as of {as_of}. Generated nightly from Jack Bot's "
                f"knowledge files; personal information removed. Figures are "
                f"distilled summaries; confirm anything contractual against "
                f"the source system.\n"
            )
            (out_dir / f"{bundle}{suffix}.md").write_text(header + "".join(chunks))
        stats[bundle] = (len(files), len(parts), lines_dropped)

    manifest = ["# Excluded from the Claude project export (do not upload)", ""]
    manifest += [f"- `{rel}`: {why}" for rel, why in excluded]
    (out_dir / "_excluded.md").write_text("\n".join(manifest) + "\n")

    digest = hashlib.sha256()
    for p in sorted(out_dir.glob("*.md")):
        if p.name != "_excluded.md":
            digest.update(p.name.encode() + p.read_bytes())
    (out_dir / ".digest").write_text(digest.hexdigest() + "\n")
    return stats, excluded


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    stats, excluded = build(args.out)
    for bundle, (n_files, n_parts, n_lines) in stats.items():
        print(f"{bundle:20s} {n_files:5d} files -> {n_parts} part(s), "
              f"{n_lines} lines scrubbed")
    print(f"{len(excluded)} files excluded; see {args.out / '_excluded.md'}")


if __name__ == "__main__":
    main()
