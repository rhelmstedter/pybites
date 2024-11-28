import pytz
from datetime import datetime, timezone
from pprint import pprint as print


MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
    they are all within schedule (MEETING_HOURS)"""
    utc = utc.replace(tzinfo=timezone.utc)
    try:
        return False not in [
            int(utc.astimezone(pytz.timezone(timezone)).strftime("%H")) in MEETING_HOURS
            for timezone in timezones
        ]
    except pytz.exceptions.UnknownTimeZoneError:
        raise ValueError


if __name__ == "__main__":
    print(TIMEZONES)
