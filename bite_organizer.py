import os
import re
import zipfile


pattern = r"pybites_bite(\d+).zip"

zip_files = [file for file in os.listdir(r".") if file.endswith(".zip")]

for bite in zip_files:
    bite_number = re.findall(pattern, bite)[0]

    if bite_number:
        print(f"Extracting bite {bite_number}")

        with zipfile.ZipFile(bite, "r") as zip_ref:
            zip_ref.extractall(f"./{bite_number}")

        os.remove(bite)

    else:
        print("No bite found.")
