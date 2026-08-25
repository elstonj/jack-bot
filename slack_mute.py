"""Global Slack write guard.

Set ``JACKBOT_SLACK_MUTE=1`` to suppress every outbound Slack write in the
process. Nothing reaches Slack — no channel posts, no DM replies, no knowledge
entries, no slash-command responses — regardless of who or what triggered it.

Why it patches the SDK instead of guarding call sites: Slack writes are spread
across ~19 call sites in 9 modules (``scheduler``, ``feedback``, ``app``,
``snow_day``, ``marketing_check``, ``eldora``, ``knowledge``, plus the
``scripts/`` cron jobs), and every one of them builds its own ``WebClient``.
Guarding them individually is easy to get wrong and impossible to keep right as
new call sites appear. Patching ``slack_sdk.WebClient`` at the class level
catches all of them at the one choke point they share — including the client
Bolt builds internally, so handler ``say()`` calls are covered without touching
``app.py``'s handlers.

Reads are deliberately left alone. The nightly scan needs
``conversations_history`` / ``users_info`` / ``conversations_info`` to build
knowledge files, so muting must not break it. Only methods that produce
user-visible output are blocked.

The mute is re-checked on every call rather than at install time, so importing
this module is harmless when unmuted and the env var can be flipped at runtime.
"""

import functools
import os
import sys

_TRUTHY = {"1", "true", "yes", "on", "y"}

MUTE_ENV = "JACKBOT_SLACK_MUTE"
LOG_ENV = "JACKBOT_SLACK_MUTE_LOG"

# Methods that produce user-visible output. conversations_join is on the list
# because joining a channel posts a visible "…joined the channel" system
# message; nothing in this repo calls it, so blocking it costs no reads.
BLOCKED_METHODS = (
    "chat_postMessage",
    "chat_postEphemeral",
    "chat_update",
    "chat_delete",
    "chat_scheduleMessage",
    "chat_deleteScheduledMessage",
    "chat_meMessage",
    "chat_unfurl",
    "files_upload",
    "files_upload_v2",
    "files_delete",
    "reactions_add",
    "reactions_remove",
    "pins_add",
    "pins_remove",
    "conversations_create",
    "conversations_invite",
    "conversations_join",
    "conversations_kick",
    "conversations_archive",
    "conversations_rename",
    "conversations_setPurpose",
    "conversations_setTopic",
    "views_open",
    "views_publish",
    "views_push",
    "views_update",
)

# Callers thread replies off the parent's ts (see scheduler._post umbrella
# threading). Hand back a stable dummy so that logic runs without blowing up.
_FAKE_TS = "0000000000.000000"

_installed = False


def is_muted():
    """True when Slack writes should be suppressed."""
    return os.environ.get(MUTE_ENV, "").strip().lower() in _TRUTHY


def _log_suppressed(method, kwargs, args=()):
    """Record what would have been sent, so a muted run is still auditable."""
    channel = kwargs.get("channel") or "?"
    text = kwargs.get("text")
    if text is None and args:
        text = args[0]
    preview = str(text or "").replace("\n", " ⏎ ")[:300]
    line = f"[slack-mute] suppressed {method} -> {channel}: {preview}"
    print(line, file=sys.stderr)
    path = os.environ.get(LOG_ENV)
    if path:
        try:
            with open(path, "a") as fh:
                fh.write(line + "\n")
        except OSError:
            pass  # logging the mute must never break the caller


def _muted_response(kwargs):
    """A SlackResponse-shaped stand-in.

    Callers read the result two ways — ``resp.get("ts")`` when it's a dict and
    ``resp.data.get("ts")`` otherwise — so a plain dict satisfies the first
    branch of both checks in scheduler.py.
    """
    return {
        "ok": True,
        "muted": True,
        "ts": _FAKE_TS,
        "channel": kwargs.get("channel", ""),
        "message": {"ts": _FAKE_TS, "text": kwargs.get("text", "")},
    }


def _wrap(name, original):
    @functools.wraps(original)
    def guarded(self, *args, **kwargs):
        if is_muted():
            _log_suppressed(name, kwargs, args)
            return _muted_response(kwargs)
        return original(self, *args, **kwargs)

    guarded.__slack_mute_wrapped__ = True
    return guarded


def _patch_bolt_respond():
    """Slash-command replies bypass WebClient.

    ``respond()`` POSTs to Slack's response_url over plain HTTP, so the
    WebClient patch never sees it. /refresh-tasks is the one path that uses it.
    Best-effort: slack_bolt isn't installed in every context that imports this.
    """
    try:
        from slack_bolt.context.respond.respond import Respond
    except Exception:
        return
    original = Respond.__call__
    if getattr(original, "__slack_mute_wrapped__", False):
        return

    @functools.wraps(original)
    def guarded(self, *args, **kwargs):
        if is_muted():
            text = kwargs.get("text")
            if text is None and args:
                text = args[0]
            _log_suppressed("respond", {"channel": "response_url", "text": text})
            return None
        return original(self, *args, **kwargs)

    guarded.__slack_mute_wrapped__ = True
    Respond.__call__ = guarded


def install():
    """Patch the Slack SDK write methods. Idempotent; safe to call anywhere."""
    global _installed
    if _installed:
        return False
    try:
        from slack_sdk import WebClient
    except ImportError:
        return False

    for name in BLOCKED_METHODS:
        original = getattr(WebClient, name, None)
        if original is None:
            continue  # method absent in this SDK version
        if getattr(original, "__slack_mute_wrapped__", False):
            continue
        setattr(WebClient, name, _wrap(name, original))

    _patch_bolt_respond()
    _installed = True
    return True


# Installed on import so an entry point only needs `import slack_mute`.
install()
