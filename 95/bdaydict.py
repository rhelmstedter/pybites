MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):
        for _birthday in self.values():
            if _birthday.month == birthday.month and _birthday.day == birthday.day:
                print(MSG.format(name))
                break
        super().__setitem__(name, birthday)
