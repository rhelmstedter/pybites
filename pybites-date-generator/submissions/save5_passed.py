from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    n = 1
    while True:
        new_date = PYBITES_BORN + timedelta(days=n*100)
        yield new_date
        n += 1