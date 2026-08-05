"""Offline regression tests for briefing identity handling.

Runs without any API credentials. Covers the 2026-08-05 failure: Jack Elston's
whole section was emitted a second time under Joshua Fromm's name, Alex Lomis's
real section was overwritten by a later "already covered above" stub, and the
missing-section guard passed because it only checked that a key existed.

    python test_identity.py
"""

import json
import sys
from pathlib import Path

import user_map
from user_map import _apply_canonical_names, _build_alias_index, resolve_person

UID_MAP = Path(__file__).parent / "knowledge" / "contacts" / "uid_map.json"

FAILURES = []


def check(label, got, want):
    if got == want:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}\n         got:  {got!r}\n         want: {want!r}")
        FAILURES.append(label)


def build_fake_map():
    """Mirror the live user map: uid_map people plus two who aren't in it yet."""
    with UID_MAP.open() as f:
        uid_users = json.load(f)["users"]

    entries = {}
    for u in uid_users:
        entries[u["slack_user_id"]] = {
            "email": u["primary_email"],
            "name": "",  # filled from the source-system spellings below
            "slack_user_id": u["slack_user_id"],
            "asana_user_gid": u["asana_user_gid"],
            "toggl_user_id": (u.get("toggl_user_ids") or [None])[0],
            "toggl_user_ids": u.get("toggl_user_ids") or [],
            "source_names": [],
        }

    # The spellings each source system actually returns (from the 2026-08-05
    # pipeline DEBUG dump: Slack display names + Asana account names).
    live_names = {
        "U01511MEQ90": ["Jack Elston"],
        "U014U9WMK2A": ["Maciej", "Maciej Stachura"],
        "U058LGYMEQ0": ["Alex Lomis"],
        "U0151201DMY": ["Ben", "Ben Busby"],
        "U014ZL9FLE9": ["Joshua Fromm", "Josh Fromm"],
        "U06NQAYBLRK": ["Sam Hild"],
        "U06B7GNFV0W": ["Nate", "Nate Straus"],
        # Deliberately WITHOUT the Asana spelling — resolution must come from the
        # alias pinned in uid_map.json, not from a live API being reachable.
        "U06KRHPQSRH": ["Meredith Needham"],
        "U07SN02GM5K": ["Kareem", "Kareem Ahmed"],
        "U083AAM8E9Y": ["Paige Smith"],
        "U06CCFTNBS6": ["Ethan", "Ethan Domagala"],
        "U07FN4QSNDN": ["Beck", "Beck Cotter"],
        "U04CZK4K7P0": ["Dan Prendergast"],
    }
    for sid, names in live_names.items():
        entries[sid]["source_names"] = list(names)
        entries[sid]["name"] = names[0]

    for sid, name in (("U0B8865H83V", "Spencer Hoehl"), ("U02L91J99KM", "Cory Dixon")):
        entries[sid]["source_names"] = [name]
        entries[sid]["name"] = name

    # A new hire who isn't in uid_map.json yet must still resolve, from their
    # live Slack name and email alone.
    entries["U0NEWHIRE01"] = {
        "email": "riley.okafor@blackswifttech.com", "name": "Riley Okafor",
        "slack_user_id": "U0NEWHIRE01", "asana_user_gid": "9999999999999",
        "toggl_user_id": 99999999, "toggl_user_ids": [99999999],
        "source_names": ["Riley Okafor"],
    }

    _apply_canonical_names(entries)
    users = list(entries.values())
    user_map._user_map = users
    _build_alias_index(users)
    return users


def name_of(spelling):
    user = resolve_person(spelling)
    return user["name"] if user else None


def test_name_resolution():
    print("\nname resolution")
    # Every spelling of one person collapses to one canonical name.
    check("'Josh Fromm' -> Joshua Fromm", name_of("Josh Fromm"), "Joshua Fromm")
    check("'Joshua Fromm' -> Joshua Fromm", name_of("Joshua Fromm"), "Joshua Fromm")
    check("'josh' -> Joshua Fromm", name_of("josh"), "Joshua Fromm")
    check("'Dan Prendergast' -> Dan Prendergast",
          name_of("Dan Prendergast"), "Dan Prendergast")
    check("'Daniel Prendergast' -> Dan Prendergast",
          name_of("Daniel Prendergast"), "Dan Prendergast")
    check("'Nathaniel Straus' -> Nate Straus",
          name_of("Nathaniel Straus"), "Nate Straus")
    check("\"Meredith O'hara Needham\" -> Meredith Needham",
          name_of("Meredith O'hara Needham"), "Meredith Needham")
    check("'Ben' -> Ben Busby", name_of("Ben"), "Ben Busby")
    check("'Beck' -> Beck Cotter", name_of("Beck"), "Beck Cotter")
    check("'Jack' -> Jack Elston", name_of("Jack"), "Jack Elston")
    check("'Spencer Hoehl' -> Spencer Hoehl", name_of("Spencer Hoehl"), "Spencer Hoehl")
    check("'Riley Okafor' -> Riley Okafor (not in uid_map)",
          name_of("Riley Okafor"), "Riley Okafor")
    check("pinned alias resolves without the live API spelling",
          name_of("Meredith O'hara Needham"), "Meredith Needham")

    # Things that must NOT resolve — a wrong guess is worse than no guess.
    check("'Jack Bot' does not resolve to a person", name_of("Jack Bot"), None)
    check("'Bob Smith' does not become Paige Smith", name_of("Bob Smith"), None)
    check("'Justin Baltz' (ByLight) does not resolve", name_of("Justin Baltz"), None)
    check("empty name does not resolve", name_of(""), None)

    # Jack and Josh must never collapse into each other.
    check("Jack != Josh", name_of("Jack Elston") == name_of("Josh Fromm"), False)


def test_section_validation():
    print("\nsection validation (2026-08-05 failure replay)")
    import daily_research as dr

    active = {u["name"] for u in user_map.get_all_users()} - {"Nate Straus"}

    jack_priorities = [
        "Mexico USGS AFAC flight approvals — critical path blocker (Due: 2026-08-03, overdue)",
        "LM/Blackswift RAVEN catch up — 9:30-10am today with Lockheed Martin (Due: today)",
        "USPACOM FY27 proposal — due NLT 8/7, needs a drafting push (Due: 2026-08-07)",
    ]
    raw = [
        # Alex's real section, followed later by the stub that used to clobber it.
        {"person": "Alex Lomis", "priorities": [
            "S0-VTOL avionics failure debugging — support Sam Hild on the FET/chip investigation",
            "SBIR Mag Tag-up follow-through — push Bartington/QuSpin sensor settings code",
            "Update electronics repo per Jack's file-naming/kicad cleanup ask",
        ]},
        {"person": "Beck Cotter", "priorities": [
            "LM/Blackswift RAVEN catch-up — 9:30-10am today, SOW drafting stage",
            "Genesis Mission FY26 Phase I Office Hours — supports the 2026-09-10 re-submit",
            "Monthly DOI UAS User Call — maintain the federal client relationship",
        ]},
        {"person": "Jack Elston", "priorities": jack_priorities},
        # The actual bug: Jack's section repeated under Josh's name.
        {"person": "Joshua Fromm", "priorities": list(jack_priorities)},
        {"person": "Alex Lomis", "priorities": ["already covered above"]},
        {"person": "Nate Straus", "priorities": [
            "Shop restock — order the remaining S0 airframe hardware",
            "Close out the CU IRISS repair paperwork",
            "Prep the Murray flight-test kit",
        ]},
        {"person": "Bob Smith", "priorities": [
            "KrateoSky IDIQ coordination — chase the market research thread",
            "Confirm the SOW draft timeline with the partner team",
        ]},
        # Only entry for Cory is a cross-reference — nothing to keep.
        {"person": "Cory Dixon", "priorities": ["see Beck's section above"]},
    ]
    fixture_people = {"Alex Lomis", "Beck Cotter", "Jack Elston", "Joshua Fromm",
                      "Cory Dixon"}

    accepted, issues = dr._validate_sections(raw, active)

    check("Alex keeps his real priorities, not the stub",
          accepted["Alex Lomis"]["priorities"][0].startswith("S0-VTOL avionics"), True)
    check("Alex's later duplicate rejected",
          any("duplicate section for Alex Lomis" in i for i in issues), True)
    check("stub-only section rejected",
          "Cory Dixon" not in accepted
          and any("stub/cross-reference section for Cory Dixon" in i for i in issues), True)
    check("OOO person (Nate) rejected",
          "Nate Straus" not in accepted, True)
    check("outside contact (Bob Smith) rejected",
          "Bob Smith" not in accepted and any("Bob Smith" in i for i in issues), True)
    check("Jack accepted", "Jack Elston" in accepted, True)

    # Josh's entry is well-formed and passes validation on its own — the copy is
    # only detectable by comparing bodies, which is what this guard does.
    check("Josh's copy of Jack's section survives field validation",
          "Joshua Fromm" in accepted, True)
    copies = dr._find_copied_sections(accepted)
    check("copied section detected", [(c[0], c[1]) for c in copies],
          [("Joshua Fromm", "Jack Elston")])

    for copied, _src, _ratio in copies:
        accepted.pop(copied, None)
    missing = [n for n in sorted(active) if n not in accepted]
    check("Josh is reported missing so he gets regenerated",
          "Joshua Fromm" in missing, True)
    check("Cory (stub-only) is reported missing too",
          "Cory Dixon" in missing, True)
    check("people with good sections are not reported missing",
          sorted(fixture_people & set(missing)), ["Cory Dixon", "Joshua Fromm"])


def test_rendering():
    print("\ndeterministic rendering")
    import daily_research as dr

    jack = resolve_person("Jack Elston")
    section = dr._render_section(
        jack,
        ["Mexico USGS AFAC flight approvals — critical path (Due: 2026-08-03, overdue)"],
        notes=[":white_check_mark: NOAA shipment appears complete — close it in Asana"],
        calendar_line=dr._calendar_line([
            {"summary": "Office", "start": "2026-08-05", "end": "2026-08-06"},
            {"summary": "LM/Blackswift RAVEN catch up",
             "start": "2026-08-05T09:30:00-06:00", "end": "2026-08-05T10:00:00-06:00"},
        ]),
        hours_line=dr._hours_line(jack, {1131025: {"total_hours": 3.8, "projects": {"No project": 3.8}}}),
    )
    lines = section.splitlines()
    check("header is the mention built from the user map",
          lines[0], "*<@U01511MEQ90>*")
    check("priority is numbered", lines[1].startswith("1. Mexico USGS"), True)
    check("note preserved", lines[2].startswith(":white_check_mark:"), True)
    check("all-day + timed events render",
          lines[3], ":calendar: Office · LM/Blackswift RAVEN catch up 09:30-10:00")
    check("all-unassigned hours flagged",
          lines[4], ":clock1: 3.8h (all unassigned — flag for project tagging)")

    check("no calendar events -> No meetings",
          dr._calendar_line([]), ":calendar: No meetings")
    check("no toggl record -> no time tracked",
          dr._hours_line(jack, {}), ":warning: *No time tracked yesterday*")
    check("partial unassigned hours",
          dr._hours_line(jack, {1131025: {"total_hours": 8.5,
                                          "projects": {"550_1": 4.5, "No project": 4.0}}}),
          ":clock1: 8.5h (4.0h unassigned)")
    check("multiple toggl ids sum",
          dr._hours_line(jack, {1131025: {"total_hours": 2.0, "projects": {"550_1": 2.0}},
                                9847189: {"total_hours": 1.5, "projects": {"550_1": 1.5}}}),
          ":clock1: 3.5h")

    ooo = dr._render_ooo_section(resolve_person("Nate Straus"), "Time Off Request")
    check("OOO section", ooo,
          "*<@U06B7GNFV0W>*\n:palm_tree: Out of office — Time Off Request")


def test_stub_detection_on_rendered_text():
    print("\nrendered-section stub detection")
    import daily_research as dr

    real = "*<@U058LGYMEQ0>*\n1. S0-VTOL debugging\n:calendar: No meetings"
    stub = "*<@U058LGYMEQ0>* — already covered above (Alex Lomis)."
    ooo = "*<@U06B7GNFV0W>*\n:palm_tree: Out of office — Time Off Request"
    check("real section is not a stub", dr._is_stub_section(real), False)
    check("stub section is a stub", dr._is_stub_section(stub), True)
    check("OOO section is not a stub", dr._is_stub_section(ooo), False)

    # A later stub must not overwrite an earlier real section.
    parsed = dr._parse_per_user(f"{real}\n\n{stub}", user_map.get_all_users())
    check("later stub does not clobber the real section",
          parsed["U058LGYMEQ0"].startswith("*<@U058LGYMEQ0>*\n1."), True)


def test_full_assembly():
    print("\nfull section assembly")
    import daily_research as dr

    users = user_map.get_all_users()
    user_by_name = {u["name"]: u for u in users}
    all_team = set(user_by_name)
    ooo = {"Nate Straus": "Time Off Request"}
    accepted = {
        name: {"priorities": [f"{name}'s real work item"], "notes": []}
        for name in all_team - set(ooo) - {"Kareem Ahmed"}  # Kareem never came back
    }
    calendar_data = {"Jack Elston": [
        {"summary": "LM/Blackswift RAVEN catch up",
         "start": "2026-08-05T09:30:00-06:00", "end": "2026-08-05T10:00:00-06:00"},
    ]}
    toggl = {1131025: {"total_hours": 3.8, "projects": {"550_1": 3.8}}}

    per_user, rendered, issues = dr._assemble_sections(
        all_team, user_by_name, accepted, ooo, calendar_data, toggl)

    check("every team member gets exactly one section",
          len(per_user), len(all_team))
    check("sections are keyed by the right Slack ID",
          all(f"*<@{sid}>*" == text.splitlines()[0] for sid, text in per_user.items()),
          True)
    check("nobody's section contains another person's name in the header",
          per_user["U014ZL9FLE9"].splitlines()[1], "1. Joshua Fromm's real work item")
    check("OOO renders the palm tree",
          per_user["U06B7GNFV0W"].splitlines()[1],
          ":palm_tree: Out of office — Time Off Request")
    check("missing person gets a visible placeholder, not someone else's tasks",
          ":warning: Jack Bot didn't generate priorities for Kareem Ahmed"
          in per_user["U07SN02GM5K"], True)
    check("missing person is reported as an issue",
          any("Kareem Ahmed" in i for i in issues), True)
    check("calendar comes from the calendar record",
          ":calendar: LM/Blackswift RAVEN catch up 09:30-10:00"
          in per_user["U01511MEQ90"], True)
    check("people with no calendar record show No meetings",
          ":calendar: No meetings" in per_user["U06NQAYBLRK"], True)
    check("hours come from the Toggl record",
          ":clock1: 3.8h" in per_user["U01511MEQ90"], True)
    check("people with no Toggl record show no time tracked",
          ":warning: *No time tracked yesterday*" in per_user["U06NQAYBLRK"], True)
    check("rendered order matches display-name order",
          rendered[0].splitlines()[1].startswith("1. Alex Lomis"), True)

    summary = dr._render_team_summary([
        ":rotating_light: Mexico USGS deployment — permits still outstanding",
        "- LM/Blackswift RAVEN catch-up 9:30-10am today",
    ])
    check("team summary header", summary.splitlines()[0], ":mega: *TEAM SUMMARY*")
    check("bare bullet gets a dash", summary.splitlines()[2], "- LM/Blackswift RAVEN catch-up 9:30-10am today")
    check("emoji bullet left alone", summary.splitlines()[1].startswith(":rotating_light:"), True)
    check("empty summary still posts something",
          ":warning:" in dr._render_team_summary([]), True)

    # The whole assembled document must still split cleanly for the poster.
    full = "\n\n".join([summary] + rendered)
    team_part, section_parts = dr._split_summary(full)
    check("team summary splits back out intact", team_part, summary)
    check("all sections split back out", len(section_parts), len(all_team))


def test_bot_identity_scrub():
    print("\nbot identity scrub")
    import daily_research as dr

    got = dr._scrub_bot_identity(
        "<@U0AQE94HJUT|Jack Bot> I know it's a difficult concept but how many "
        "times do I need to remind you that I'm not Jack?",
        bot_user_id="U0AQE94HJUT",
    )
    check("bot mention replaced", "U0AQE94HJUT" not in got, True)
    check("bot name replaced", "Jack Bot" not in got, True)
    check("human 'Jack' preserved", got.endswith("I'm not Jack?"), True)


if __name__ == "__main__":
    build_fake_map()
    test_name_resolution()
    test_section_validation()
    test_rendering()
    test_stub_detection_on_rendered_text()
    test_full_assembly()
    test_bot_identity_scrub()

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED: {FAILURES}")
        sys.exit(1)
    print("all identity checks passed")
