from enum import Enum


class Hand(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


LEFT_HAND_CHARS = set("QWERTASDFGZXCVB")
RIGHT_HAND_CHARS = set("YUIOPHJKLNM")


def get_hand_for_word(word: str) -> Hand:
    """
    Use the LEFT_HAND_CHARS and RIGHT_HAND_CHARS sets to determine
    if the passed in word can be written with only the left or right
    hand, or if both hands are needed.
    """
    word = set(word.upper())
    if LEFT_HAND_CHARS & word and RIGHT_HAND_CHARS & word:
        return Hand.BOTH
    if RIGHT_HAND_CHARS & word:
        return Hand.RIGHT
    else:
        return Hand.LEFT
