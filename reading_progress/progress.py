from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int, day_of_year: int = None) -> bool:
    if not day_of_year:
        tday = datetime.now()
        day_of_year = (tday - datetime(tday.year, 1, 1)).days

    YEAR = 365
    days_per_book = YEAR / books_goal
    days_left = YEAR - day_of_year
    books_left = books_goal - books_read
    days_needed = days_per_book * books_left

    return days_left >= days_needed
