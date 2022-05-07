class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self._old_record = -9999

    def __call__(self, *args, **kwargs):
        if args[0] > self._old_record:
            self._old_record = args[0]
        return self._old_record
