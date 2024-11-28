from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    delta = timedelta(days=num_days)
    while True:
        start_date += delta
        for _ in range(num_bites):
            yield start_date
