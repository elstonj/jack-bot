import threading
from datetime import datetime


_lock = threading.Lock()
_cache = {
    "generated_at": None,
    "full_summary": None,
    "per_user": {},
}


def set_cache(full_summary, per_user):
    with _lock:
        _cache["generated_at"] = datetime.now()
        _cache["full_summary"] = full_summary
        _cache["per_user"] = per_user


def get_full_summary():
    with _lock:
        return _cache["full_summary"], _cache["generated_at"]


def get_user_summary(slack_user_id):
    with _lock:
        return _cache["per_user"].get(slack_user_id)


def is_stale(max_age_hours=20):
    with _lock:
        if _cache["generated_at"] is None:
            return True
        age = (datetime.now() - _cache["generated_at"]).total_seconds() / 3600
        return age > max_age_hours
