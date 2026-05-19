"""Dry-run smoke test for commercial_sales_inquiry.

Runs the inquiry handler against the live Build/SupportCase JSONs without
posting to Slack (chat_postMessage is intercepted). Three scenarios:

  1. Josh's exact 2026-05-18 message — no matching record → stub flow.
  2. UMES / ERAU question about a field that's populated (ship_to) → answer.
  3. Question about a populated build with an empty field → owner ping +
     KNOWLEDGE_GAP (gap write is intercepted so #jackbot-knowledge stays clean).

Run:
    source venv/bin/activate && python test_commercial_sales_inquiry.py
"""

from __future__ import annotations

import os
import sys
from dotenv import load_dotenv

load_dotenv()


class FakeSlackClient:
    """No-op slack client — captures any would-be posts."""
    def __init__(self):
        self.posted = []

    def chat_postMessage(self, **kwargs):
        self.posted.append(kwargs)
        return {"ok": True}


def main(argv):
    verbose = "--verbose" in argv

    from commercial_sales_inquiry import (
        is_inquiry_intent,
        handle_inquiry,
        handle_inquiry_followup,
        PENDING,
    )

    # 1. Intent classification --------------------------------------------
    print("== intent classification ==")
    cases = [
        ("do the two s0 display units get shipped to the same address?", True),
        ("what's the point of contact for UMES?", True),
        ("are the parts in for the SOCOM build?", True),
        ("hello", False),
        ("the snow is heavy today", False),
        ("can we fly at BMA?", False),  # has 'fly' but no inquiry kw
    ]
    for msg, expect in cases:
        got = is_inquiry_intent(msg)
        mark = "OK" if got == expect else "FAIL"
        print(f"  [{mark}] expect={expect} got={got}  {msg!r}")

    # 2. No-match branch — Josh's original message ------------------------
    print("\n== Josh's question (no Build for 'two S0 display units') ==")
    fake = FakeSlackClient()
    josh_msg = "do the two s0 display units get shipped to the same address or different addresses?"
    resp = handle_inquiry(
        josh_msg,
        user_id="U014ZL9FLE9",
        channel_id="C014L88992B",
        slack_client=fake,
        asker_name="Joshua Fromm",
    )
    print(resp)
    print(f"_(fake posts: {len(fake.posted)}; pending state: "
          f"{list(PENDING.keys())})_")

    # 3. Match + field populated — ERAU 4 S0 VTOL has ship_to set ---------
    PENDING.clear()
    print("\n== ERAU shipping address (field populated) ==")
    fake = FakeSlackClient()
    resp = handle_inquiry(
        "what's the shipping address for the ERAU S0 VTOL order?",
        user_id="U01511MEQ90",
        channel_id="C014L88992B",
        slack_client=fake,
        asker_name="Jack Elston",
    )
    print(resp)

    # 4. Match + field empty — Oklahoma S0 has ship_to=None ---------------
    PENDING.clear()
    print("\n== Oklahoma S0 shipping address (field empty) ==")
    fake = FakeSlackClient()
    resp = handle_inquiry(
        "where is the Oklahoma State S0 shipping to?",
        user_id="U01511MEQ90",
        channel_id="C014L88992B",
        slack_client=fake,
        asker_name="Jack Elston",
    )
    print(resp)
    print(f"_(fake posts (KNOWLEDGE_GAP would be one): {len(fake.posted)})_")
    if verbose and fake.posted:
        for p in fake.posted:
            print(f"  >> {p}")

    print("\nDone.")


if __name__ == "__main__":
    main(sys.argv[1:])
