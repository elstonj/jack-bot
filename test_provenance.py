#!/usr/bin/env python3
"""Offline regression suite for provenance-question routing.

Replays the 2026-08-25 #operations exchange that motivated the module: both of
Joshua Fromm's messages must be recognised, including "explain yourself", which
carried no question word and no "?" and so fell through to the personality
handler at the time.

Needs no credentials and makes no API calls — only the detector and prompt
wiring are exercised.

    python test_provenance.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from provenance import FACTS, PROVENANCE_SYSTEM, is_provenance_question, _fallback

FAILURES = []


def check(label, cond):
    if cond:
        print(f"  ok    {label}")
    else:
        print(f"  FAIL  {label}")
        FAILURES.append(label)


# Verbatim from #operations, 2026-08-25, plus the phrasings a person reaches for
# when they suspect they're being read.
SHOULD_MATCH = [
    "how did you know about the email from munro in my tasks",
    "explain yourself",
    "The email came in 30 minutes ago, no one told you about it yet",
    "the email wasn't sent to you..?",
    "how do you know that",
    "where did you get that",
    "who told you about the fuel cell email",
    "are you reading my email?",
    "do you read our slack dms",
    "are you monitoring my inbox",
    "do you have access to my gmail",
    "what data sources do you use",
    "why do you know what's in my inbox",
    "prove it",
    "how did you see that message",
    "are you going through my email",
]

# Must NOT hijack ordinary work questions — these belong in knowledge Q&A.
SHOULD_NOT_MATCH = [
    "what's the budget for 001-07",
    "how do I submit an expense report",
    "when is the ByLight deliverable due",
    "who is the POC for NOAA",
    "can we buy $500 of connectors",
    "how did the flight test go",
    "where is the S3 shipment",
    "tasks",
    "finances",
    "what did Josh work on yesterday",
    "how many units are left",
    "explain the ECCN classification",
]


def test_detection():
    print("\nprovenance questions detected")
    for t in SHOULD_MATCH:
        check(f"matches: {t[:55]}", is_provenance_question(t))

    print("\nordinary questions left to Q&A")
    for t in SHOULD_NOT_MATCH:
        check(f"ignores: {t[:55]}", not is_provenance_question(t))


def test_facts_are_honest():
    """The whole point is that the bot stops denying what it does."""
    print("\nfact block states the capability")
    low = FACTS.lower()
    check("says it reads every employee's inbox", "every employee" in low)
    check("names the gmail query", "newer_than:1d" in low)
    check("distinguishes metadata from bodies", "does not read" in low and "bodies" in low)
    check("states it needn't be a recipient", "recipient" in low)
    check("covers calendar", "calendar" in low)
    check("covers drive", "drive" in low)
    check("covers slack", "slack" in low)
    check("names an accountable owner", "jack elston" in low)
    check("states read-only scopes", "read-only" in low)


def test_system_prompt_forbids_denial():
    print("\nsystem prompt bans the failure mode")
    low = PROVENANCE_SYSTEM.lower()
    check("forbids denying a capability", "never deny" in low)
    check("forbids the 'someone told me' excuse", "told you" in low)
    check("drops the persona", "persona" in low)


def test_fallback_is_truthful():
    """If the API is down the answer must still be accurate, not evasive."""
    print("\noffline fallback")
    low = _fallback().lower()
    check("admits reading inboxes", "inbox" in low)
    check("says subject lines only", "subject" in low)
    check("says not bodies", "never message bodies" in low)
    check("does not deny access", "don't have access" not in low)


def test_qa_prompt_carries_facts():
    print("\nQ&A prompt backstop")
    try:
        from knowledge_qa import QA_SYSTEM_PROMPT
    except Exception as e:
        check(f"knowledge_qa imports (raised {type(e).__name__})", False)
        return
    check("DATA ACCESS block appended", "=== DATA ACCESS ===" in QA_SYSTEM_PROMPT)
    check("facts present verbatim", "newer_than:1d" in QA_SYSTEM_PROMPT)
    check("denial forbidden in Q&A too", "Never deny a capability" in QA_SYSTEM_PROMPT)


if __name__ == "__main__":
    test_detection()
    test_facts_are_honest()
    test_system_prompt_forbids_denial()
    test_fallback_is_truthful()
    test_qa_prompt_carries_facts()

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED:")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    print("All provenance checks passed.")
