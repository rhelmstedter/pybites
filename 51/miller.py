"""Bite 51."""
from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')
MILLER_TO_EARTH_HOURS = 1/(8760*7)


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    duration = (PY2_DEATH_DT - start_date).total_seconds()
    return round(duration/(60*60), 2)


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    duration = (PY2_DEATH_DT - start_date).total_seconds()
    earth_hours = duration/(60*60)
    miller_mins = earth_hours*MILLER_TO_EARTH_HOURS*60
    return round(miller_mins, 2)
