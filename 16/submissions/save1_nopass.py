from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates(n):
    for number in range(n):
        yield PYBITES_BORN + timedelta(days=100)