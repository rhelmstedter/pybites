THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:

    def __mul__(self, mult):
        if 4 <= mult:
            return f"{THUMBS_UP} ({mult}x)"
        elif 0 < mult < 4:
            return THUMBS_UP * mult
        elif -4 < mult < 0:
            return THUMBS_DOWN * abs(mult)
        elif mult <= -4:
            return f"{THUMBS_DOWN} ({abs(mult)}x)"
        else:
            raise ValueError("Specify a number")
    __rmul__ = __mul__
