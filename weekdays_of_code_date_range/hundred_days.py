from datetime import date

from dateutil.rrule import rrule
from dateutil.rrule import DAILY

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
    start_date up till 100 weekdays later, so +100 days
    skipping Saturdays and Sundays"""
    datetimes = list(
        rrule(
            DAILY,
            dtstart=start_date,
            byweekday=range(5),
            count=100,
        )
    )
    return [date(dt.year, dt.month, dt.day) for dt in datetimes]
