"""Routing configuration for email triage.

Everything that decides *who* a message can go to lives in config.json, not in
code or in the prompt text: the people table and their handles, the finance
split between Lynn and Meredith, the external greenlist (the only non-BST
addresses a forward may ever reach), Jack's own addresses and the label names.
classify.py builds its system prompt from this file and guards.py enforces the
same lists deterministically, so the two can never disagree about the roster.

Edit config.json to reassign a responsibility; no code change needed.
"""

import json
import threading
from pathlib import Path

CONFIG_PATH = Path(__file__).with_name("config.json")

_lock = threading.Lock()
_cache = None


def _normalize(cfg):
    """Lowercase every email and precompute the lookup sets guards need."""
    jack = cfg["jack"]
    jack["email"] = jack["email"].lower()
    jack["addresses"] = sorted({a.lower() for a in jack.get("addresses", [])} | {jack["email"]})
    cfg["internal_domains"] = [d.lower() for d in cfg.get("internal_domains", [])]
    cfg["external_greenlist"] = [e.lower() for e in cfg.get("external_greenlist", [])]
    for p in cfg["people"]:
        p["email"] = p["email"].lower()
        p["aliases"] = [a.lower() for a in p.get("aliases", [])]
        p.setdefault("handles", [])
        p.setdefault("examples", [])
    cfg["people_emails"] = [p["email"] for p in cfg["people"]]
    # Any address a person writes from -> their canonical routing address.
    alias_map = {}
    for p in cfg["people"]:
        alias_map[p["email"]] = p["email"]
        for a in p["aliases"]:
            alias_map[a] = p["email"]
    cfg["alias_map"] = alias_map
    return cfg


def load_config(reload=False):
    """Return the parsed config (cached per process). reload=True rereads disk."""
    global _cache
    with _lock:
        if _cache is None or reload:
            _cache = _normalize(json.loads(CONFIG_PATH.read_text()))
        return _cache


def person_by_email(email, cfg=None):
    """Person entry for a routing address or one of its aliases, else None."""
    cfg = cfg or load_config()
    canon = cfg["alias_map"].get((email or "").lower())
    if not canon:
        return None
    return next((p for p in cfg["people"] if p["email"] == canon), None)


def is_internal(email, cfg=None):
    cfg = cfg or load_config()
    domain = (email or "").lower().rsplit("@", 1)[-1]
    return domain in cfg["internal_domains"]


def is_jack(email, cfg=None):
    cfg = cfg or load_config()
    return (email or "").lower() in cfg["jack"]["addresses"]


def label_name(key, cfg=None):
    """Label name for an action key: reviewed / forwarded / archived / spam / kept."""
    cfg = cfg or load_config()
    return cfg["labels"][key]


def is_skipped_label(name, cfg=None):
    """True for labels whose mail Jack's own filters already handle."""
    cfg = cfg or load_config()
    if name in cfg.get("skip_labels", []):
        return True
    return any(name.startswith(p) for p in cfg.get("skip_label_prefixes", []))
