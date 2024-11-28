from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    n = 100
    while True:
        new_date = PYBITES_BORN + timedelta(days=n)
        yield new_date
        n += 100
