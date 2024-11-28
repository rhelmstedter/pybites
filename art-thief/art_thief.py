"""
1. track the index of the paintings.
2. Grab all combinations of non-adjacent paintings.
3. the max sum of those combinations.
"""

from itertools import combinations


def art_thief(paintings: list[int]) -> int:
    """Return the maximum value of paintings that can be stolen."""
    if len(set(paintings)) == 1:
        return sum(paintings[i] for i in range(0, len(paintings), 2))
    if not paintings:
        return 0
    combos = []
    for i in range(1, len(paintings) + 1):
        combos.extend(list(combinations(paintings, i)))

    valid = []
    for c in combos:
        idxs = [paintings.index(p) for p in c]
        if any(abs(curr - next) == 1 for curr, next in zip(idxs, idxs[1:])):
            continue
        valid.append(list(c))
    return max(sum(theft) for theft in valid)


if __name__ == "__main__":
    art_thief([2, 8, 9])
