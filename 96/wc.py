import os


def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""
    file_name = os.path.basename(file_)
    with open(file_) as file:
        lines = file.readlines()
        words = []
        chars = []
        for line in lines:
            chars.append(len(line))
            for word in line.split():
                words.append(word)
    return f"{len(lines)}\t{len(words)}\t{sum(chars)}\t{file_name}"


if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
