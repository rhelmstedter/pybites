from datetime import date
import calendar


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    weekday= calendar.weekday(date.year, date.month, date.day)
    return calendar.day_name[weekday]
