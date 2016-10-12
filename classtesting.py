class Card:
    def __init__(self, name, cost = 0):
        self.name = name
        self.cost = cost

class Monster(Card):
    def __init__(self, name, cost, power):
        self.name = name
        self.cost = cost
        self.power = power

class Spell(Card):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost



d = Spell("d", 3)

def effect():
    print p2.field
    target = input("Which monster would you like to destroy")
    target = str(target)
    try:
        x = p2.field.index(target)
        p2.field.pop(x)
        print(target, " was destroyed")
    except

def cpeffect():
