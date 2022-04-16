import re


def replace(string: str) -> str:
    pattern = ",{1,}"
    return re.sub(pattern, " ", string)


def get_users(passwd: str) -> dict:
    """Split password output by newline,
    extract user and name (1st and 5th columns),
    strip trailing commas from name,
    replace multiple commas in name with a single space
    return dict of keys = user, values = name.
    """
    return {
        replace(line.split(":")[0].strip(",")): replace(line.split(":")[4].strip(","))
        if line.split(":")[4]
        else "unknown"
        for line in passwd.strip("\n").split("\n")
    }
