from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()
NON_ZERO_NUMBER_CARDS = "1 2 3 4 5 6 7 8 9".split() * 2
ACTION_CARDS = ["Draw Two", "Skip", "Reverse"] * 2
WILDS = ["Wild", "Wild Draw Four"] * 4
TOTAL_PER_SUIT = [0] + NON_ZERO_NUMBER_CARDS + ACTION_CARDS

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
    Return a list of UnoCard namedtuples
    (for cards w/o suit use None in the namedtuple)"""
    nums = [UnoCard(suit, value) for suit in SUITS for value in TOTAL_PER_SUIT]
    wilds = [UnoCard(None, wild) for wild in WILDS]
    return nums + wilds
