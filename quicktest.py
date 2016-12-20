class Thing:
    def __init__(self, name, favorite_person):
        self.name = name
        self.favorite_person = favorite_person

class Person:
    def __init__(self, name, favorite_thing):
        self.name = name
        self.favorite_thing = favorite_thing

Pail = Thing("Pail", "Joe")
Joe = Person("Joe", "Pail")

print(Joe.favorite_thing)
