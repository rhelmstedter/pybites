import string

VOWELS = "aeiou"
EXTENSIONS = [".mp3", ".jpg", ".jpeg", ".pdf", ".txt", ".mp4", ".png", ".exe"]


def uppercase_vowels(text: str) -> str:
    suffix = ""
    if text[-4:] in EXTENSIONS:
        suffix = text[-4:]
        text = text[:-4]
    elif text[-5:] in EXTENSIONS:
        suffix = text[-5:]
        text = text[:-5]
    for c in string.punctuation:
        text = text.replace(c, " ")
    text = text.lower().replace(".", " ")
    return "".join([c.upper() if c in VOWELS else c for c in text]) + suffix
