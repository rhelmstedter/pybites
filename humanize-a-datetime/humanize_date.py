from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)


def pretty_date(date: datetime):
    """Receives a datetime object and converts/returns a readable string
    using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError("Please endter a valid date in the past.")
    delta = (NOW - date).total_seconds()
    for offset in TIME_OFFSETS:
        if delta < offset.offset:
            if offset.divider:
                return offset.date_str.format(int(delta / offset.divider))
            else:
                return offset.date_str.format(int(delta))
    return date.strftime("%m/%d/%y")
