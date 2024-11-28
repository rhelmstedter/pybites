from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name:str, expires:str):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        if self.expires < NOW:
            return True
