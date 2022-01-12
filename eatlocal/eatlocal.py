import os
import zipfile
import webbrowser


def extract_bite(bite_number):
    """Extracts all the required files into a new directory
    named by the bite number.

    :bite_number: The number of the bite you want to extract.
    :returns: None
    """

    bite = f"pybites_bite{bite_number}.zip"

    try:
        with zipfile.ZipFile(bite, "r") as zip_ref:
            zip_ref.extractall(f"./{bite_number}")

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
