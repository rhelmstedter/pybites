import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movies = []
    for file in files:
        with open(file) as f:
            data = f.read()
            movies.append(json.loads(data))
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    return [movie["Title"] for movie in movies if "comedy" in movie["Genre"].lower()][0]


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""

    def nominations(movie):
        awards = movie["Awards"]
        return int(awards.split("&")[-1].split()[0])

    return sorted(movies, key=nominations)[-1]["Title"]


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""

    def runtime(movie):
        runtime = movie["Runtime"]
        return int(runtime.split()[0])

    return sorted(movies, key=runtime)[-1]["Title"]
