from collections import Counter, defaultdict
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join(os.getenv("TMP", "/tmp"), 'commits')
urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/git_log_stat.out',
    commits
)


def _parse_line(line):
    """
    >>> line = "Date:   Sun Jan 14 21:40:34 2018 +1100 | 2 files changed, 50 insertions(+), 1 deletion(-)"
    >>> _parse_line(line)
    ('2018-01', 51)
    """
    date, changes = line.split('|')
    date = parse(date.split('   ')[1].strip(), ignoretz=True)
    changes = sum(int(c.split()[0]) for c in changes.split(', ')[1:])
    return f'{date:%Y-%m}', changes


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    commits_by_month = {}
    with open(commit_log) as commit_log:
        for line in commit_log.readlines():
            date, changes = _parse_line(line)
            if year and str(year) not in date:
                continue
            commits_by_month[date] = commits_by_month.get(date, 0) + changes
    least_active_month = min(commits_by_month.keys(), key=lambda x: commits_by_month[x])
    most_active_month = max(commits_by_month.keys(), key=lambda x: commits_by_month[x])
    return least_active_month, most_active_month


if __name__ == "__main__":
    import doctest
    doctest.testmod()
