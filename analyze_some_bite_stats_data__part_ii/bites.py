import csv
import os
from pathlib import Path
from urllib.request import urlretrieve

data = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_levels.csv'
TMP = Path(os.getenv("TMP", "/tmp"))
stats = TMP / 'bites.csv'

if not stats.exists():
    urlretrieve(data, stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, newline='') as bite_stats:
        data = csv.reader(bite_stats, delimiter=';')
        bite_diffs = []
        for row in data:
            bite, difficulty = row
            if bite.startswith("Bite ") and difficulty != 'None':
                bite = bite.split()[1].strip('.')
                bite_diffs.append((bite, float(difficulty)))
        return [bite for bite, difficulty in sorted(bite_diffs, key=lambda x: x[1], reverse=True)][:N]
