from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()
NUMBER_CARDS = "0 1 2 3 4 5 6 7 8 9".split()
ACTION_CARDS = ["Draw Two", "Skip", "Reverse"]
WILDS = ["Wild", "Wild Draw Four"]
TOTAL_PER_SUIT = NUMBER_CARDS + NUMBER_CARDS[1:] + ACTION_CARDS + ACTION_CARDS
TOTAL_WILDS = WILDS + WILDS + WILDS + WILDS

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
    Return a list of UnoCard namedtuples
    (for cards w/o suit use None in the namedtuple)"""
    nums = [UnoCard(suit, value) for suit in SUITS for value in TOTAL_PER_SUIT]
    wilds = [UnoCard(None, wild) for wild in TOTAL_WILDS]
    return nums + wilds
