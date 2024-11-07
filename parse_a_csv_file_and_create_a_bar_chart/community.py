from collections import Counter
import csv
from io import StringIO

import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    response = requests.get(CSV_URL)
    return StringIO(response.text)


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    tz_counts = Counter()
    data = csv.reader(content, delimiter=',')
    for row in data:
        tz_counts[row[-1]] += 1

    for tz, count in sorted(tz_counts.items()):
        print(f"{tz: <21}| "+ "+"*count)
    return tz_counts
