from collections import Counter

from bs4 import BeautifulSoup
import requests

COMMON_DOMAINS = "https://bites-data.s3.us-east-2.amazonaws.com/" "common-domains.html"
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("div", TARGET_DIV)
    domains = []
    for row in table.find_all("tr"):
        domains.append(row.find_all("td")[2].text)
    return domains


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
    ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
    return Counter(
        [
            email.split("@")[1]
            for email in emails
            if email.split("@")[1] not in common_domains
        ]
    ).most_common()


if __name__ == "__main__":
    print(get_common_domains())
