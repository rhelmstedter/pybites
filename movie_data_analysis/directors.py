import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "https://bites-data.s3.us-east-2.amazonaws.com/"
TMP = os.getenv("TMP", "/tmp")

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    with open(MOVIE_DATA) as data:
        movie_data = csv.DictReader(data)
        movies = defaultdict(list)
        for row in movie_data:
            title = row["movie_title"].strip("\xa0")
            year = row["title_year"]
            score = row["imdb_score"]
            director = row["director_name"]
            if year and int(year) >= 1960:
                movies[director].append(Movie(title, int(year), float(score)))
    return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
    round the mean to 1 decimal place"""
    mean = sum([movie.score for movie in movies]) / len(movies)
    return round(mean, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
    return a list of tuples (director, average_score) ordered by highest
    score in descending order. Only take directors into account
    with >= MIN_MOVIES"""
    return sorted([(director, calc_mean_score(movies)) for director, movies in directors.items() if len(movies) >= MIN_MOVIES], key=lambda x: x[1], reverse=True)
