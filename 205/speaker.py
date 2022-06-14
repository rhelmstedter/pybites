from urllib.request import urlretrieve
import os
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path(os.getenv("TMP", "/tmp"))
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = "https://bites-data.s3.us-east-2.amazonaws.com/" "pycon2019.html"

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def _parse_multi_speakers(speakers, split_char, first_names):
    for speaker in speakers.split(split_char):
        first_names.append(speaker.split()[0])


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
    speakers (class "speaker"). Note that some items contain
    multiple speakers so you need to extract them.
    Return a list of first names
    """
    if not soup:
        soup = _get_soup()
    speakers = soup.find_all("span", {"class": "speaker"})
    names = [name.text.strip(" \n") for name in speakers]
    first_names = []
    for name in names:
        if "," in name:
            _parse_multi_speakers(name, ",", first_names)
        elif "/" in name:
            _parse_multi_speakers(name, "/", first_names)
        else:
            first_names.append(name.split()[0])
    return first_names


def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
    of female speakers (female and mostly_female),
    rounded to 2 decimal places."""
    d = gender.Detector()
    count = sum(
        1
        for name in first_names
        if d.get_gender(name) == "female" or d.get_gender(name) == "mostly_female"
    )
    return round(count / len(first_names) * 100, 2)


if __name__ == "__main__":
    from rich import print

    first_names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(first_names)
    print(perc)
