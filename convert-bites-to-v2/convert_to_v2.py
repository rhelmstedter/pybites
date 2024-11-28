import pathlib
import json
import requests

from constants import BITES_API, URL_BASE, BITES


def create_bite_map(bites):
    bites_map = {}
    for line in bites.splitlines():
        bite, description = line.split(".", 1)
        bite_num = bite.split()[1]
        bites_map[bite_num] = description.strip().capitalize()
    return bites_map


def fetch_bites_api():
    r = requests.get(BITES_API)
    with open("bites_api_data.json", "w") as f:
        json.dump(r.json(), f, indent=2)


def format_bites_api():
    with open("bites_api_data.json") as f:
        data = json.load(f)
    return {bite["title"]: bite for bite in data}


def create_description_list(bites):
    bite_descriptions = []
    for line in bites.splitlines():
        bite, description = line.split(".", 1)
        bite_descriptions.append(description)
    return bite_descriptions


def get_dirs() -> list[pathlib.Path]:
    dirs = [d for d in pathlib.Path(".").iterdir() if d.is_dir() and d.name.isdigit()]
    return dirs


def convert_dirs(bites_map: dict, formatted_bites: dict):
    dirs = get_dirs()
    if not dirs:
        print("No old bite dirs found")
        return
    local_bites = {}
    for d in dirs:
        old_dir = d.name
        if old_dir not in bites_map:
            continue
        bite_title = bites_map.get(old_dir)
        slug = formatted_bites[bite_title]["slug"]
        local_bites[bite_title] = f"{URL_BASE}{slug}/"
        try:
            pathlib.Path(old_dir).rename(pathlib.Path(slug))
        except FileExistsError:
            continue
        except OSError:
            print(f"Failed to rename {old_dir} to {slug}")
            continue
    # Then move to the eatlocal home
    with open(".local_bites.json", "w") as f:
        json.dump(local_bites, f, indent=2)


if __name__ == "__main__":
    from rich import print

    bites_map = create_bite_map(BITES)
    formatted_bites = format_bites_api()

    convert_dirs(bites_map, formatted_bites)
