
class Animal:

    animal_count = 10_000
    animals = []

    def __init__(self, name):
        self.name = name
        self.__class__.animal_count += 1
        self.__class__.animals.append(self.__str__())

    def __str__(self):
        return f"{Animal.animal_count}. {self.name.title()}"

    @classmethod
    def zoo(cls):
        return "\n".join(cls.animals)
