from typing import Union

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()


def get_belt(
    user_score: int, scores: list = scores, belts: list = belts
) -> Union[None, str]:

    if user_score < 10:
        return None
    elif user_score >= 1000:
        return 'red'
    else:
        for i, (low, high) in enumerate(zip(scores, scores[1:])):
            if low <= user_score < high:
                return belts[i]
