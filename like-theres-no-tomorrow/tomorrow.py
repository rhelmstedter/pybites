from datetime import date, timedelta


def tomorrow(day=date(2020, 7, 9)):
    return day + timedelta(days=1)
