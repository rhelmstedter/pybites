import requests
from bs4 import BeautifulSoup

cached_so_url = "https://bites-data.s3.us-east-2.amazonaws.com/so_python.html"


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
    parse the questions out of the html with BeautifulSoup,
    filter them by >= 1m views ("..m views").
    Return a list of (question, num_votes) tuples ordered
    by num_votes descending (see tests for expected output).
    """
    r = requests.get(url).content
    soup = BeautifulSoup(r, "html.parser")
    questions = soup.find_all("div", {"class": "question-summary"})
    q_stats = []
    for q in questions:
        try:
            views = q.find("div", {"class": "views supernova"}).text
            question = q.find("h3").text
            num_votes = q.find("strong").text
            if "m" in views:
                q_stats.append((question, int(num_votes)))
        except AttributeError:
            pass
    return sorted(q_stats, key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    from rich import print
    print(top_python_questions())
