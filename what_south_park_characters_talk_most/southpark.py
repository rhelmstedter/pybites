from collections import Counter, defaultdict
import csv
from io import StringIO

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    word_counts = defaultdict(Counter)
    lines = csv.DictReader(StringIO(content))
    for line in lines:
        episode = line["Episode"]
        character = line["Character"]
        words = line["Line"].strip('"\n').split()
        word_counts[character].update({episode: len(words)})

    return word_counts

if __name__ == "__main__":
    print(get_season_csv_file(1))
