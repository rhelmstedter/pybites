from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counts = Counter(sequence.lower())
    return round(
        (counts["g"] + counts["c"])
        / sum([counts["g"], counts["c"], counts["a"], counts["t"]])
        * 100,
        2,
    )
