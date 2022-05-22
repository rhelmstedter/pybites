VOWELS = list("aeiou")


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
    Return a tuple of the matching word and the vowel count, e.g.
    ('object-oriented', 6)"""
    vowel_counts = []
    for word in text.lower().split():
        count = 0
        for c in word:
            if c in VOWELS:
                count += 1
        vowel_counts.append((word, count))
    return sorted(vowel_counts, key=lambda x: x[1])[-1]
