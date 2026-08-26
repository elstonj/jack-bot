#!/usr/bin/env python3
"""Offline regression suite for the global Slack write guard.

Needs no credentials and never touches the network — the passthrough case is
exercised against a dummy callable rather than a real WebClient, so running
this can never post to Slack.

    python test_slack_mute.py
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Start from a known state: the guard reads the env var on every call, so tests
# set it explicitly rather than inheriting whatever .env left behind.
os.environ.pop("JACKBOT_SLACK_MUTE", None)
os.environ.pop("JACKBOT_SLACK_MUTE_LOG", None)
os.environ.pop("JACKBOT_SLACK_REDIRECT", None)

import slack_mute  # noqa: E402

FAILURES = []


def check(label, cond):
    if cond:
        print(f"  ok    {label}")
    else:
        print(f"  FAIL  {label}")
        FAILURES.append(label)


def mute(on):
    if on:
        os.environ["JACKBOT_SLACK_MUTE"] = "1"
    else:
        os.environ.pop("JACKBOT_SLACK_MUTE", None)


def redirect(target):
    if target:
        os.environ["JACKBOT_SLACK_REDIRECT"] = target
    else:
        os.environ.pop("JACKBOT_SLACK_REDIRECT", None)


class FakeClient:
    """Stands in for WebClient so redirect tests never touch the network."""

    def conversations_info(self, channel):
        if channel.startswith("D"):
            return {"channel": {"is_im": True, "user": "U777"}}
        return {"channel": {"name": {"C_OPS": "operations"}.get(channel, "some-chan")}}

    def users_info(self, user):
        return {"user": {"real_name": "Alex Lomis"}}


def test_is_muted():
    print("\nis_muted() env parsing")
    for val in ("1", "true", "TRUE", "yes", "on", "y"):
        os.environ["JACKBOT_SLACK_MUTE"] = val
        check(f"{val!r} -> muted", slack_mute.is_muted())
    for val in ("0", "false", "no", "", "  "):
        os.environ["JACKBOT_SLACK_MUTE"] = val
        check(f"{val!r} -> not muted", not slack_mute.is_muted())
    os.environ.pop("JACKBOT_SLACK_MUTE", None)
    check("unset -> not muted", not slack_mute.is_muted())


def test_wrap_blocks_and_passes_through():
    """The core contract: swallow the call when muted, delegate when not."""
    print("\n_wrap() block / passthrough")
    calls = []

    def original(self, **kwargs):
        calls.append(kwargs)
        return {"ok": True, "ts": "real"}

    guarded = slack_mute._wrap("chat_postMessage", original)

    mute(True)
    resp = guarded(None, channel="C123", text="should not send")
    check("muted: original never invoked", calls == [])
    check("muted: response ok", resp.get("ok") is True)
    check("muted: response flagged", resp.get("muted") is True)
    check("muted: ts present for threading", bool(resp.get("ts")))
    check("muted: channel echoed", resp.get("channel") == "C123")

    mute(False)
    resp = guarded(None, channel="C123", text="real send")
    check("unmuted: original invoked", len(calls) == 1)
    check("unmuted: real response returned", resp.get("ts") == "real")
    check("unmuted: kwargs forwarded intact", calls[0]["text"] == "real send")


def test_redirect():
    """Every post lands in the target, tagged with where it was headed."""
    print("\nredirect routing")
    sent = []

    def original(self, **kwargs):
        sent.append(kwargs)
        return {"ok": True, "ts": f"ts{len(sent)}"}

    guarded = slack_mute._wrap("chat_postMessage", original)
    slack_mute._label_cache.clear()
    slack_mute._redirected_ts.clear()

    mute(False)
    redirect("C_KNOW")
    client = FakeClient()

    guarded(client, channel="C_OPS", text="team summary")
    check("rerouted to target", sent[-1]["channel"] == "C_KNOW")
    check("origin channel tagged", "#operations" in sent[-1]["text"])
    check("body preserved", "team summary" in sent[-1]["text"])

    # A DM reply must be visible without the asker ever receiving it.
    guarded(client, channel="D123", text="answer to a teammate")
    check("DM rerouted to target", sent[-1]["channel"] == "C_KNOW")
    check("DM tagged with person", "DM with Alex Lomis" in sent[-1]["text"])

    # Threading: a child whose parent also landed in the target keeps its
    # thread_ts; one from a foreign channel must be flattened or Slack rejects it.
    parent_ts = "ts1"
    guarded(client, channel="C_OPS", text="child", thread_ts=parent_ts)
    check("known parent keeps threading", sent[-1].get("thread_ts") == parent_ts)
    check("threaded child not re-tagged", not sent[-1]["text"].startswith("_[→"))

    guarded(client, channel="C_OPS", text="orphan", thread_ts="9999.0000")
    check("foreign thread_ts dropped", "thread_ts" not in sent[-1])
    check("flattened reply is marked", "thread reply" in sent[-1]["text"])

    # Already addressed to the target: leave completely alone.
    before = len(sent)
    guarded(client, channel="C_KNOW", text="knowledge entry")
    check("target-bound post untouched", sent[-1]["text"] == "knowledge entry")
    check("target-bound post still sent", len(sent) == before + 1)

    # Non-postMessage writes have no meaningful destination; drop them.
    react = slack_mute._wrap("reactions_add", original)
    before = len(sent)
    resp = react(client, channel="C_OPS", name="eyes")
    check("reaction suppressed under redirect", len(sent) == before)
    check("reaction returns stub", resp.get("muted") is True)

    redirect(None)


def test_mute_beats_redirect():
    print("\nmute takes precedence over redirect")
    sent = []

    def original(self, **kwargs):
        sent.append(kwargs)
        return {"ok": True, "ts": "x"}

    guarded = slack_mute._wrap("chat_postMessage", original)
    mute(True)
    redirect("C_KNOW")
    resp = guarded(FakeClient(), channel="C_OPS", text="nope")
    check("nothing sent", sent == [])
    check("stub returned", resp.get("muted") is True)
    mute(False)
    redirect(None)


def test_writes_patched_reads_untouched():
    """Muting must not break the reads the nightly scan depends on."""
    print("\nWebClient patch surface")
    from slack_sdk import WebClient

    for name in ("chat_postMessage", "chat_update", "chat_postEphemeral",
                 "reactions_add", "files_upload_v2", "conversations_join"):
        m = getattr(WebClient, name, None)
        check(f"{name} is guarded",
              m is not None and getattr(m, "__slack_mute_wrapped__", False))

    # These are what the scanners call; guarding them would break the scan.
    for name in ("conversations_history", "users_info", "conversations_info",
                 "auth_test", "conversations_list", "users_list"):
        m = getattr(WebClient, name, None)
        check(f"{name} left alone",
              m is None or not getattr(m, "__slack_mute_wrapped__", False))


def test_real_client_suppressed():
    """A genuine WebClient with a bogus token must not raise when muted.

    If the call actually hit Slack it would fail auth; returning cleanly proves
    the request never left the process.
    """
    print("\nreal WebClient instance, muted")
    from slack_sdk import WebClient

    mute(True)
    client = WebClient(token="xoxb-invalid-token-would-fail-if-sent")
    try:
        resp = client.chat_postMessage(channel="C0AQJNA8Y3F", text="TEST — must not send")
        check("no network call, no exception", resp.get("muted") is True)
    except Exception as e:
        check(f"no network call, no exception (raised {type(e).__name__})", False)


def test_store_entry_suppressed():
    """knowledge.store_entry is the path the nightly scan uses for [BUG]."""
    print("\nknowledge.store_entry, muted")
    from slack_sdk import WebClient
    from knowledge import store_entry

    os.environ.setdefault("KNOWLEDGE_CHANNEL", "C0AQJNA8Y3F")
    mute(True)
    client = WebClient(token="xoxb-invalid-token-would-fail-if-sent")
    try:
        store_entry(client, "BUG", "TEST — must not send")
        check("store_entry suppressed cleanly", True)
    except Exception as e:
        check(f"store_entry suppressed cleanly (raised {type(e).__name__})", False)


def test_idempotent_install():
    print("\ninstall() idempotency")
    from slack_sdk import WebClient

    before = WebClient.chat_postMessage
    check("second install() is a no-op", slack_mute.install() is False)
    check("method not double-wrapped", WebClient.chat_postMessage is before)


def test_mute_log():
    print("\nsuppression logging")
    import tempfile

    path = os.path.join(tempfile.mkdtemp(), "mute.log")
    os.environ["JACKBOT_SLACK_MUTE_LOG"] = path
    mute(True)

    from slack_sdk import WebClient
    WebClient(token="x").chat_postMessage(channel="C999", text="line one\nline two")

    written = Path(path).read_text()
    check("log file written", bool(written.strip()))
    check("records channel", "C999" in written)
    check("records text", "line one" in written)
    check("newlines flattened to one line", len(written.strip().splitlines()) == 1)
    os.environ.pop("JACKBOT_SLACK_MUTE_LOG", None)


if __name__ == "__main__":
    test_is_muted()
    test_wrap_blocks_and_passes_through()
    test_redirect()
    test_mute_beats_redirect()
    test_writes_patched_reads_untouched()
    test_real_client_suppressed()
    test_store_entry_suppressed()
    test_idempotent_install()
    test_mute_log()

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED:")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    print("All slack-mute checks passed.")
