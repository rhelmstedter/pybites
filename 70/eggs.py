from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, limit):
        self.limit = limit
        self.egg = f"{choice(COLORS)} egg"
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count >= self.limit:
            raise StopIteration
        egg = self.egg
        self._count += 1
        return egg
