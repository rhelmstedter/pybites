import os
import urllib.request
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, "stopwords")
harry_text = os.path.join(tmp, "harry")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt", stopwords_file
)
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/harry.txt", harry_text
)


def get_harry_most_common_word():
    with open(stopwords_file) as stopwords:
        stopwords = [word.strip("\n") for word in stopwords.readlines()]

    with open(harry_text) as text:
        text = text.read()
        words = [
            "".join([letter.lower() for letter in word if letter.isalpha()])
            for word in text.split()
        ]

    counts = Counter()
    for word in words:
        if word and word not in stopwords:
            counts.update([word])
    return counts.most_common(1)[0]
