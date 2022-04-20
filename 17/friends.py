from itertools import permutations, combinations
from typing import Generator


def friends_teams(
    friends_teams: list, team_size: int = 2, order_does_matter: bool = False
) -> Generator[str]:
    if order_does_matter:
        return permutations(friends_teams, team_size)
    return combinations(friends_teams, team_size)
