"""Offline regression suite for Q&A knowledge-file routing.

Replays the review finding that "What is the remaining budget on 550-1?"
matched "what is" as a proposal keyword, loaded all 2,571 proposals ahead of
the budget files, and pushed financial/by_project/550_1.md to index 2697, far
past the context cap. Also guards the payroll exposure: payroll journals sit in
knowledge/proposals/ and must never reach the Q&A context. Runs against the
committed knowledge files; needs no credentials. Run: python test_qa_routing.py
"""

import os

import knowledge_qa as k

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


def in_context(question):
    """Relative paths that _build_context would actually include."""
    out, total = [], 0
    for f in k.select_files(question):
        content = k._read_file(f)
        if not content.strip() or k.is_personnel_record(os.path.basename(f), content):
            continue
        if total >= k.MAX_CONTEXT_CHARS:
            break
        out.append(os.path.relpath(f, k.KNOWLEDGE_DIR))
        total += len(content)
    return out


def test_project_code_files_first():
    print("files named by a project code load first")
    ctx = in_context("What is the remaining budget on 550-1?")
    check("550-1 financials first", ctx[:1], ["financial/by_project/550_1.md"])
    ctx = in_context("How much have we spent on 212-2?")
    check("212-2 financials in context", "financial/by_project/212_2.md" in ctx, True)
    ctx = in_context("who owns 001-1?")
    check("leading zero tolerated", "projects/001_01.md" in ctx, True)


def test_no_whole_proposal_sweep():
    print("proposal questions never sweep the whole directory")
    files = k.select_files("what is the S2 used for?")
    proposals = [f for f in files if "/proposals/" in f]
    check("bounded", len(proposals) <= 16, True)


def test_word_boundaries():
    print("keywords match whole words only")
    check("rate vs accurate", k._has_kw("is this accurate", ["rate"]), False)
    check("time vs sometime", k._has_kw("sometime next week", ["time"]), False)
    check("phrase still matches", k._has_kw("what's the burn rate", ["burn rate"]), True)


def test_payroll_never_in_context():
    print("payroll records never reach the Q&A context")
    ctx = in_context("what is Brad Cheetham's gross salary on the payroll journal")
    check("no payroll files", [p for p in ctx if "payroll" in p or "match_doc" in p], [])


if __name__ == "__main__":
    test_project_code_files_first()
    test_no_whole_proposal_sweep()
    test_word_boundaries()
    test_payroll_never_in_context()
    if FAILURES:
        raise SystemExit(f"\n{len(FAILURES)} failure(s)")
    print("\nall Q&A routing checks passed")
