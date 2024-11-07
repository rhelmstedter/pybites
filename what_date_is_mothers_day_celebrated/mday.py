from datetime import date, timedelta

SUNDAY = 6


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
    is celebrated assuming it's the 2nd Sunday of May."""
    may_first = date(year, 5, 1)
    delta = SUNDAY - may_first.weekday() + 7
    return may_first + timedelta(delta)
