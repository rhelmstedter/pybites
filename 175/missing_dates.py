from datetime import date, timedelta


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    sorted_dates = sorted(dates)
    first_date, last_date = sorted_dates[0], sorted_dates[-1]
    delta = (last_date - first_date).days
    full_range = [first_date + timedelta(days=n) for n in range(delta + 1)]
    return set(full_range) - set(dates)
