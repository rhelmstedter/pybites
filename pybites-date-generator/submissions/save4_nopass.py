from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    yield next_day  
    while True:
        next_day += PYBITES_BORN + timedelta(days=100)
        yield next_day  