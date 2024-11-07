class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self._record = float("-inf")

    def __call__(self, score):
        self._record = max(self._record, score)
        return self._record
