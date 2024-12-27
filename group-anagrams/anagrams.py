from collections import defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    anagrams = defaultdict(list)
    for s in strings:
        anagrams["".join(sorted(s))].append(s)
    return list(anagrams.values())


if __name__ == "__main__":
    group_anagrams()
