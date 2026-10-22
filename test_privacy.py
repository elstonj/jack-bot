"""Offline regression suite for the privacy / HR screen.

Needs no credentials — the model pass is disabled throughout, so this exercises
the deterministic floor and the wiring. Run: python test_privacy.py
"""

import privacy_guard as pg

FAILURES = []


def check(label, got, want):
    ok = got == want
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    if not ok:
        print(f"       got:  {got!r}\n       want: {want!r}")
        FAILURES.append(label)


def test_channel_scope():
    print("\nchannel scope")
    check("public channel is screened", pg.is_shared_channel("C015QR6P5S4"), True)
    check("private channel is screened", pg.is_shared_channel("G0123456789"), True)
    check("DM is not screened", pg.is_shared_channel("D0AQE94HJUT"), False)
    check("empty channel id is not screened", pg.is_shared_channel(""), False)


def test_sensitive_patterns():
    print("\nsensitive pattern detection")
    for text in [
        "Re: Your 2026 compensation review",
        "Termination letter — draft for review",
        "Offer letter for the avionics role",
        "MRI follow-up appointment",
        "FMLA paperwork",
        "[001-21] Sick Leave",
        "Call with outside counsel re: litigation",
        "KPMG financial due diligence — data room access",
        "Performance improvement plan discussion",
        "Severance terms",
    ]:
        check(f"flags {text[:44]!r}", pg.contains_sensitive(text), True)

    # This company's everyday vocabulary must survive — over-redaction makes the
    # briefing useless, which is its own kind of failure.
    for text in [
        "S3 IRAD data acquisition pipeline",
        "Sensor data acquisition for the magnetometer board",
        "USPACOM FY27 Joint Warfighter proposal due today",
        "NOAA S0 Hurricane IDIQ fleet — 7 units awaiting motors",
        "Navy SBIR Magnetometer ground testing",
        "SwiftCore 3.3 release candidate",
        "Raise the flight ceiling for the Chile deployment",
        "Ship 2 S3 units to INSTAAR",
        "Friday Flyday 10:00-14:00",
        "Budget review for project 350_4",
    ]:
        check(f"allows {text[:44]!r}", pg.contains_sensitive(text), False)


def test_field_redaction():
    print("\nfield redaction (ingestion)")
    check("sensitive subject replaced",
          pg.redact_field("Re: Q3 salary adjustment"), pg.FIELD_MARKER)
    check("ordinary subject untouched",
          pg.redact_field("S3 wing shipment tracking"), "S3 wing shipment tracking")
    check("sensitive Toggl project replaced",
          pg.redact_field("[001-21] Sick Leave"), pg.FIELD_MARKER)
    check("ordinary Toggl project untouched",
          pg.redact_field("[001-14] SwiftCore 3.3"), "[001-14] SwiftCore 3.3")
    check("empty passes through", pg.redact_field(""), "")


def test_calendar_redaction():
    print("\ncalendar title redaction")
    check("sensitive title replaced, slot survives",
          pg.redact_calendar_title("1:1 re: performance improvement plan"),
          pg.CALENDAR_MARKER)
    check("medical title replaced",
          pg.redact_calendar_title("Doctor's appointment"), pg.CALENDAR_MARKER)
    check("ordinary meeting untouched",
          pg.redact_calendar_title("LM/Blackswift RAVEN catch up"),
          "LM/Blackswift RAVEN catch up")
    check("flyday untouched",
          pg.redact_calendar_title("Friday Flyday"), "Friday Flyday")


def test_line_screen():
    print("\nassembled-output screen (deterministic only)")
    section = "\n".join([
        "*<@U06KRHPQSRH>*",
        "1. Daily Purchasing Summary — keep vendor orders moving",
        "2. Prep severance paperwork for the offboarding",
        "3. Support USPACOM proposal admin needs",
        ":calendar: Office · Friday Flyday 10:00-14:00",
        ":clock1: 8.1h",
    ])
    out = pg.screen_public_text(section, use_model=False)
    lines = out.split("\n")
    check("identity header survives", lines[0], "*<@U06KRHPQSRH>*")
    check("ordinary priority survives",
          lines[1], "1. Daily Purchasing Summary — keep vendor orders moving")
    check("sensitive priority redacted", lines[2], pg.REDACTION_MARKER)
    check("later priority survives",
          lines[3], "3. Support USPACOM proposal admin needs")
    check("calendar line survives",
          lines[4], ":calendar: Office · Friday Flyday 10:00-14:00")
    check("hours line survives", lines[5], ":clock1: 8.1h")

    # A generated line must never be redacted even if it happens to contain a
    # trigger word — losing the hours line would look like a pipeline bug.
    protected = "*<@U01511MEQ90>*\n:clock1: 8.1h\n:mega: *TEAM SUMMARY*"
    check("protected lines are never touched",
          pg.screen_public_text(protected, use_model=False), protected)

    check("adjacent redactions collapse to one marker",
          pg.screen_public_text("ok line\nsalary review\nseverance terms\nok line",
                                use_model=False),
          f"ok line\n{pg.REDACTION_MARKER}\nok line")
    check("clean text passes through unchanged",
          pg.screen_public_text("1. Ship S3 units to INSTAAR", use_model=False),
          "1. Ship S3 units to INSTAAR")


def test_calendar_event_granularity():
    print("\ncalendar line screens per event, not whole-line")
    line = (":calendar: Office · Doctor's appointment 09:00-09:30 · "
            "Friday Flyday 10:00-14:00")
    out = pg.screen_public_text(line, use_model=False)
    check("sensitive event replaced, others survive",
          out,
          f":calendar: Office · {pg.CALENDAR_MARKER} · Friday Flyday 10:00-14:00")
    check("no meetings line untouched",
          pg.screen_public_text(":calendar: No meetings", use_model=False),
          ":calendar: No meetings")
    check("clean calendar line untouched",
          pg.screen_public_text(":calendar: Office · Friday Flyday 10:00-14:00",
                                use_model=False),
          ":calendar: Office · Friday Flyday 10:00-14:00")
    check("adjacent private events collapse",
          pg.screen_public_text(
              ":calendar: MRI 09:00-09:30 · therapy 10:00-11:00 · Flyday 12:00-13:00",
              use_model=False),
          f":calendar: {pg.CALENDAR_MARKER} · Flyday 12:00-13:00")


def test_extra_terms_env():
    print("\nPRIVACY_EXTRA_TERMS (company-specific codenames)")
    import os
    prior = os.environ.get("PRIVACY_EXTRA_TERMS")
    try:
        os.environ["PRIVACY_EXTRA_TERMS"] = "krateosky process, revenue questions"
        check("configured codename is flagged",
              pg.contains_sensitive("KrateoSky Process kickoff"), True)
        check("configured term is case-insensitive",
              pg.contains_sensitive("[EXTERNAL] Re: Revenue Questions"), True)
        check("calendar event with codename redacted, rest survives",
              pg.screen_public_text(
                  ":calendar: Office · Re: Revenue Questions 09:00-09:30 · "
                  "Friday Flyday 10:00-14:00", use_model=False),
              f":calendar: Office · {pg.CALENDAR_MARKER} · Friday Flyday 10:00-14:00")
        check("unrelated text still passes",
              pg.contains_sensitive("Ship S3 units to INSTAAR"), False)

        os.environ["PRIVACY_EXTRA_TERMS"] = ""
        check("clearing the env var takes effect immediately",
              pg.contains_sensitive("KrateoSky Process kickoff"), False)
    finally:
        if prior is None:
            os.environ.pop("PRIVACY_EXTRA_TERMS", None)
        else:
            os.environ["PRIVACY_EXTRA_TERMS"] = prior


def test_guarded_say():
    print("\nguarded_say transport wrapper")
    sent = []
    say = sent.append

    guarded = pg.guarded_say(say, "C015QR6P5S4")
    guarded("Prep severance paperwork")
    check("shared channel is screened", sent[-1], pg.REDACTION_MARKER)
    guarded("Ship S3 units to INSTAAR")
    check("ordinary text passes", sent[-1], "Ship S3 units to INSTAAR")

    dm_sent = []
    dm_guarded = pg.guarded_say(dm_sent.append, "D0AQE94HJUT")
    dm_guarded("Prep severance paperwork")
    check("DM is untouched", dm_sent[-1], "Prep severance paperwork")
    check("DM returns the original say", dm_guarded, dm_sent.append)


def test_model_failure_falls_back():
    print("\nmodel-pass failure degrades, never blocks")

    class Boom:
        class messages:
            @staticmethod
            def create(**_kwargs):
                raise RuntimeError("api down")

    out = pg.screen_public_text("ok line\nsalary review", client=Boom())
    check("pattern screen still applied when model errors",
          out, f"ok line\n{pg.REDACTION_MARKER}")


if __name__ == "__main__":
    print("=== privacy guard ===")
    test_channel_scope()
    test_sensitive_patterns()
    test_field_redaction()
    test_calendar_redaction()
    test_line_screen()
    test_calendar_event_granularity()
    test_extra_terms_env()
    test_guarded_say()
    test_model_failure_falls_back()
    print()
    if FAILURES:
        print(f"{len(FAILURES)} failure(s): {', '.join(FAILURES)}")
        raise SystemExit(1)
    print("all privacy checks passed")
