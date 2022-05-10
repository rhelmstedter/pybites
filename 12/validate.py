from collections import namedtuple

User = namedtuple("User", "name role expired")
USER, ADMIN = "user", "admin"
SECRET = "I am a very secret token"

julian = User(name="Julian", role=USER, expired=False)
bob = User(name="Bob", role=USER, expired=True)
pybites = User(name="PyBites", role=ADMIN, expired=False)
USERS = (julian, bob, pybites)


# define exception classes here
class UserDoesNotExist(Exception):
    pass


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


# my way
def get_secret_token(username):
    for user in USERS:
        if user.name == username:
            username = user
    if username not in USERS:
        raise UserDoesNotExist
    elif username.expired:
        raise UserAccessExpired
    elif username.role != ADMIN:
        raise UserNoPermission
    return SECRET


# solution: construct a dictionary based on the names. Then, look up the namedtuple by passing in `username`.
def _get_user(username):
    users = {user.name: user for user in USERS}
    return users.get(username)


def get_secret_token(username):
    user = _get_user(username)
    if not user:
        raise UserDoesNotExist

    if user.expired:
        raise UserAccessExpired

    if user.role != ADMIN:
        raise UserNoPermission

    return SECRET
