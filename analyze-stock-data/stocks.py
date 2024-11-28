from collections import Counter

import requests

STOCK_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/stocks.json"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:


def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
    - strip off leading '$',
    - if 'M' in cap value, strip it off and return value as float,
    - if 'B', strip it off, multiply by 1,000 and return
      value as float"""
    if cap == "n/a":
        return 0
    cap = cap.strip("$")
    if "M" in cap:
        return float(cap.strip("M"))
    elif "B" in cap:
        return float(cap.strip("B")) * 1000


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
    the _cap_str_to_mln_float to parse the cap values,
    return a float with 2 digit precision"""
    total_caps = 0
    for stock in data:
        if stock["industry"] == industry:
            total_caps += _cap_str_to_mln_float(stock["cap"])
    return round(total_caps, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
    the _cap_str_to_mln_float to parse the cap values"""
    return sorted(
        [(stock["symbol"], _cap_str_to_mln_float(stock["cap"])) for stock in data],
        key=lambda x: x[1],
    )[-1][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
    discard n/a"""
    stock_counters = Counter()
    for stock in data:
        if stock['sector'] != 'n/a':
            stock_counters.update([stock['sector']])
    return stock_counters.most_common(1)[0][0], stock_counters.most_common()[-1][0]
