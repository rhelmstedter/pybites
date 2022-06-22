import os
import re
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path(os.getenv("TMP", "/tmp"))
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )


def _parse_test_results(result):
    stats = re.findall(r"(\d+) =+ (\d+).*in (\d\.?\d*)", result)
    if stats and len(stats[0]) == 3:
        return stats[0][0], float(stats[0][2]) / float(stats[0][1])
    return result, 88888


def get_bite_with_fastest_avg_test(timings: list) -> str:
    """Return the bite which has the fastest average time per test"""
    return sorted(
        [_parse_test_results(line) for line in timings],
        key=lambda x: x[1]
    )[0][0]
