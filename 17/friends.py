from itertools import permutations, combinations


def friends_teams(
    friends_teams: list, team_size: int = 2, order_does_matter: bool = False
) -> list:
    if order_does_matter:
        return permutations(friends_teams, team_size)
    return combinations(friends_teams, team_size)
