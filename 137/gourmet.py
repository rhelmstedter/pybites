#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from pprint import pprint
from collections import Counter

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _calc_similarity(wine: str, cheese: str) -> float:
    """Helper to calculate similarty score.
    >>> _calc_similarity('mouse', 'house')
    4.0
    >>> _calc_similarity('parapraxis', 'explanation')
    2.5
    """
    numerator = sum((Counter(wine.lower()) & Counter(cheese.lower())).values())
    denominator = 1 + (len(wine) - len(cheese)) ** 2
    return round(numerator / denominator, 2)


def best_match_per_wine(wine_type="all"):
    """Wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score.

    >>> best_match_per_wine('red')
    ('Cabernet sauvignon', 'Dorset Blue Vinney', 13.0)
    """
    types = {
        "red": RED_WINES,
        "white": WHITE_WINES,
        "sparkling": SPARKLING_WINES,
        "all": SPARKLING_WINES + WHITE_WINES + RED_WINES,
    }
    if wine_type not in types:
        raise ValueError
    pairings = []
    for wine in types[wine_type]:
        for cheese in CHEESES:
            pairings.append((wine, cheese, _calc_similarity(wine, cheese)))
    return max(pairings, key=lambda pairing: pairing[-1])


def _top_five(wine: str) -> list[str]:
    pairing_scores = []
    for cheese in CHEESES:
        pairing_scores.append((cheese, _calc_similarity(wine, cheese)))
    pairing_scores = sorted(pairing_scores, key=lambda x: x[0])
    pairing_scores = sorted(pairing_scores, key=lambda x: x[1], reverse=True)[:5]
    return ([cheese for cheese, _ in pairing_scores])


def match_wine_5cheeses():
    """pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    >>> match_wine_5cheeses()[0]
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer'])
    >>> match_wine_5cheeses()[-1]
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    """
    all = SPARKLING_WINES + WHITE_WINES + RED_WINES
    pairings = []
    for wine in all:
        pairings.append((wine, _top_five(wine)))
    return sorted(pairings, key=lambda x: x[0])

if __name__ == "__main__":
    _calc_similarity("Cava", "Parmesan")
    _calc_similarity("Cava", "Caerphilly")
