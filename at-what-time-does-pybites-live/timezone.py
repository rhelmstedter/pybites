from zoneinfo import ZoneInfo
from datetime import datetime

AUSTRALIA = ZoneInfo("Australia/Sydney")
SPAIN = ZoneInfo("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes
    """
    utc_dt = naive_utc_dt.replace(tzinfo=ZoneInfo("UTC"))
    aus_dt = utc_dt.astimezone(AUSTRALIA)
    es_dt = utc_dt.astimezone(SPAIN)
    return aus_dt, es_dt
