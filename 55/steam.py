from collections import namedtuple
import requests
import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    r = requests.get(FEED_URL)
    feed_file = feedparser.parse(r.content)
    return [Game(entry.title, entry.link) for entry in feed_file.entries]

    
