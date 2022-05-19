from collections import defaultdict

names = "bob julian tim martin rod sara joyce nick beverly kevin".split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (5, 9),
    (6, 8),
    (7, 8),
    (8, 9),
]


def get_friend_with_most_friends(friendships, users=users):
    """Receives the friendships list of user ID pairs,
    parse it to see who has most friends, return a tuple
    of (name_friend_with_most_friends, his_or_her_friends)"""
    friend_lists = defaultdict(list)
    for friendship in friendships:
        friend_lists[friendship[0]].append(users[friendship[1]])
        friend_lists[friendship[1]].append(users[friendship[0]])
    most_popular = sorted(friend_lists.items(), key=lambda user: len(user[-1]))[-1]
    return users[most_popular[0]], most_popular[-1]
