"""Person Class"""


class Person:
    def __init__(self):
        self = self

    def __str__(self):
        return "I am a person"


class Father(Person):
    def __init__(self):
        self = self

    def __str__(self):
        return super().__str__() + " and cool daddy"


class Mother(Person):
    def __init__(self):
        self = self

    def __str__(self):
        return super().__str__() + " and awesome mom"


class Child(Father, Mother):
    def __init__(self):
        self = self

    def __str__(self):
        return "I am the coolest kid"
