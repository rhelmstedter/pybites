from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data: str) -> set:
    """Extract unique dates from DB table representation as shown in Bite"""
    dates = set()
    for line in data.splitlines():
        try:
            dates.add(datetime.strptime(line.split("|")[1].strip(), "%Y-%m-%d").date())
        except ValueError:
            pass
        except IndexError:
            pass
    return dates


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
    on coding streak.

    Note that a coding streak is defined as consecutive days coded
    since yesterday, because today is not over yet, however if today
    was coded, it counts too of course.

    So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
    the table makes for a 3 days coding streak.

    See the tests for more examples that will be used to pass your code.
    """
    if TODAY in dates:
        streak = 1
    else:
        streak = 0

    dates.add(TODAY)
    sorted_dates = sorted(dates, reverse=True)

    for day, previous in zip(sorted_dates, sorted_dates[1:]):
        if abs(day - previous).days == 1:
            streak += 1
        else:
            break

    return streak


if __name__ == "__main__":
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    calculate_streak(extract_dates(data))
