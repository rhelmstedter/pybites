from collections import defaultdict
import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = "safari.logs"
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = "🐍", "."
ADD_TO_SLACK = "sending to slack channel"

urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DATA}", SAFARI_LOGS
)


def create_chart():
    with open(SAFARI_LOGS) as logs:
        books = defaultdict(list)
        lines = logs.readlines()
        for current_line, next_line in zip(lines, lines[1:]):
            if ADD_TO_SLACK in next_line:
                date = current_line.split()[0]
                if "Python" in current_line:
                    books[date].append(PY_BOOK)
                else:
                    books[date].append(OTHER_BOOK)
        for date, book in books.items():
            print(f"{date} {''.join(book)}")
