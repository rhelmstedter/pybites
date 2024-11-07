from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    book = soup.find('div', class_='dotd-main-book')
    title = book.find('div', class_='dotd-title').text.strip()
    description = [div.text for div in book.find_all('div') if 'Build enterprise-ready' in div.text][-1].strip()
    image = book.find('img')['src']
    # link = [link['href'] for link in soup.find_all('a') if 'mastering-type' in link['href']]
    link = [link['href'] for link in soup.find_all('a', href=True) if 'application' in link['href']][1]
    return Book(title, description, image, link)



if __name__ == "__main__":
    get_book()
