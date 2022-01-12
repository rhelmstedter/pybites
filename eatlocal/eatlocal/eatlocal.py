import os
from zipfile import ZipFile
import webbrowser
import requests
from io import BytesIO
# from urllib.request import urlopen


def download_bite(bite_number):
    """Download bite .zip from the platform.

    :bite_number: The number of the bite you want to download.
    :returns: None

    """
    url = "https://codechalleng.es/bites/api/downloads/bites/{bite_number}/"
    # with urlopen(url) as zipresp:
    #     with ZipFile(BytesIO(zipresp.read())) as zfile:
    #         zfile.extractall(f"./{bite_number}/")
    # print(f"Finished extracting {bite_number}")
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        z = ZipFile(BytesIO(r.content))
        z.extractall(f"./{bite_number}/")
        print(f"bite {bite_number} downloaded and extracted")
    else:
        print("No response from website")


def extract_bite(bite_number):
    """Extracts all the required files into a new directory
    named by the bite number.

    :bite_number: The number of the bite you want to extract.
    :returns: None
    """

    bite = f"pybites_bite{bite_number}.zip"

    try:
        with ZipFile(bite, "r") as zfile:
            zfile.extractall(f"./{bite_number}")

        print(f"Extracted bite {bite_number}")
        os.remove(bite)

    except FileNotFoundError:
        print("No bite found.")


def submit_bite(bite_number):
    """Submits bite by pushing to git hub and opening
    webbrowser to the bit page.

    :bite_number: The number of the bite you want to submit.
    :returns: None

    """
    os.system("git add .")
    os.system(f"git commit -m'solved bite {bite_number}'")
    os.system("git push")
    print(f"Pushed bite {bite_number} to github")
    url = f"https://codechalleng.es/bites/{bite_number}/"
    webbrowser.open(url)
