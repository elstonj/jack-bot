"""Offline regression suite for commercial-sales duplicate detection.

Replays the 2026-08-10 failure: NASA Ames appeared twice on the digest because
the Asana-sourced Build never wrote its project code (212-2) into its notes, so
`_tracked_project_codes` didn't know the code was covered and the financial
sweep created a second record. Needs no credentials. Run: python test_dedup.py
"""

import json
import tempfile
import pathlib

from commercial_sales import Build
import scanners.commercial_sales_scanner as sc

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


def build(gid, customer, notes="", invoice_number=None):
    b = Build(asana_gid=gid, customer=customer)
    b.notes = notes
    b.invoice_number = invoice_number
    b.asana_task_name = customer
    return b


def test_identity_keys():
    print("\nstrong identifier extraction")
    check("government PO parsed from prose",
          "po:80NSSC25PC031" in sc._identity_keys(
              build("g", "NASA", "Due 2026-09-30. PO 80NSSC25PC031. Pallet shipping.")),
          True)
    check("invoice number from the structured field",
          "inv:1633" in sc._identity_keys(build("g", "NASA", "", "1633")), True)
    check("invoice number from prose",
          "inv:1759" in sc._identity_keys(
              build("g", "CU", "Invoice 1759 sent 2026-05-08 for $664.98")), True)
    check("estimate number parsed",
          "est:1373" in sc._identity_keys(
              build("g", "ND", "verbal order based on estimate 1373")), True)
    check("alphanumeric PO parsed",
          "po:J20265067" in sc._identity_keys(
              build("g", "ByLight", "Firm fixed price PO J20265067 signed 4/8/2026")), True)
    check("no identifiers yields an empty set",
          sc._identity_keys(build("g", "Someone", "no numbers of interest here")), set())

    # "1761-1762" must become two keys, else the overlap with a plain 1762
    # record is invisible.
    keys = sc._identity_keys(build("g", "NOAA", "", "1761-1762"))
    check("invoice range expands to each number",
          {"inv:1761", "inv:1762"} <= keys, True)
    check("open-ended range does not explode",
          len(sc._identity_keys(build("g", "X", "", "1000-9999"))), 2)


def test_duplicate_grouping():
    print("\nduplicate grouping")
    builds = {
        "1206482266586173": build("1206482266586173", "NASA Ames",
                                  "PO 80NSSC25PC031 paid", "1633"),
        "proj-212-2": build("proj-212-2", "NASA Ames Research Center",
                            "NASA Ames S2 & Parts (PO 80NSSC25PC031)"),
        "proj-018-1": build("proj-018-1", "Murray State", "unrelated order"),
    }
    groups = sc.find_duplicate_groups(builds)
    check("one group found", len(groups), 1)
    check("the NASA pair is grouped", sorted(groups[0][0]),
          ["1206482266586173", "proj-212-2"])
    check("shared key reported", groups[0][1], ["po:80NSSC25PC031"])

    check("cross-project-code duplicates are caught",
          len(sc.find_duplicate_groups({
              "proj-025-01": build("proj-025-01", "University of Notre Dame",
                                   "based on estimate 1373"),
              "proj-032-3": build("proj-032-3", "Notre Dame",
                                  "verbal order per estimate 1373"),
          })), 1)
    check("unrelated builds are not grouped",
          sc.find_duplicate_groups({
              "a": build("a", "A", "", "1001"),
              "b": build("b", "B", "", "1002"),
          }), [])


def test_discovery_guard():
    print("\ndiscovery guard")
    existing = {"1206482266586173": build("1206482266586173", "NASA Ames",
                                          "PO 80NSSC25PC031", "1633")}
    candidate = build("proj-212-2", "NASA Ames Research Center",
                      "NASA Ames S2 & Parts contract (PO 80NSSC25PC031)")
    check("a new record sharing a PO is flagged as a duplicate",
          sc._duplicate_of(candidate, existing), "1206482266586173")
    check("refreshing the record itself is not a duplicate",
          sc._duplicate_of(existing["1206482266586173"], existing), None)
    check("an unrelated record is not a duplicate",
          sc._duplicate_of(build("proj-018-1", "Murray State", "no shared ids"),
                           existing), None)


def test_exemptions():
    print("\nintentional-split exemptions")
    # UMES hardware + its training follow-on both cite invoice 1765 and must
    # stay as two cards — the split was deliberate.
    pair = {
        "proj-031-1": build("proj-031-1", "UMES", "hardware order", "1765"),
        "proj-031-1-training": build("proj-031-1-training", "UMES",
                                     "training follow-on", "1765"),
    }
    original = sc._DEDUP_EXEMPT_PATH
    tmpdir = pathlib.Path(tempfile.mkdtemp())
    empty, tmp = tmpdir / "empty.json", tmpdir / "_dedup_exempt.json"
    empty.write_text(json.dumps({"keep_separate": []}))
    tmp.write_text(json.dumps({"keep_separate": [
        {"gids": ["proj-031-1", "proj-031-1-training"], "reason": "deliberate split"}
    ]}))
    try:
        # Point at an empty file first — the committed one already exempts UMES,
        # so this check would otherwise pass for the wrong reason.
        sc._DEDUP_EXEMPT_PATH = empty
        check("without an exemption the pair is flagged",
              len(sc.find_duplicate_groups(pair)), 1)

        sc._DEDUP_EXEMPT_PATH = tmp
        check("an exempt pair is not flagged",
              sc.find_duplicate_groups(pair), [])
        check("the guard also honours the exemption",
              sc._duplicate_of(pair["proj-031-1-training"],
                               {"proj-031-1": pair["proj-031-1"]}), None)
    finally:
        sc._DEDUP_EXEMPT_PATH = original

    check("exemption file is restored", sc._DEDUP_EXEMPT_PATH, original)


def test_shipped_exemption_file_is_valid():
    print("\ncommitted exemption file")
    pairs = sc._dedup_exempt_pairs()
    check("UMES split is exempt in the committed file",
          any({"proj-031-1", "proj-031-1-training"} <= set(p) for p in pairs), True)


if __name__ == "__main__":
    print("=== commercial-sales dedup ===")
    test_identity_keys()
    test_duplicate_grouping()
    test_discovery_guard()
    test_exemptions()
    test_shipped_exemption_file_is_valid()
    print()
    if FAILURES:
        print(f"{len(FAILURES)} failure(s): {', '.join(FAILURES)}")
        raise SystemExit(1)
    print("all dedup checks passed")
