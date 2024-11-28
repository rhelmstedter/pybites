

def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
    an anagram of word1, ignore case and spacing.
    About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    return sorted([c.lower() for c in word1 if c.isalnum() ]) == sorted([c.lower() for c in word2 if c.isalnum()])
