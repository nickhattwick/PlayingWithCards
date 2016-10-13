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



destroy = Spell("Destroy", 3):

    def effect():
        print p2.field
        target = input("Which monster would you like to destroy?")
        target = str(target)
        try:
            x = p2.field.index(target)
            y = p2.field.pop(x)
            p2.dpile.append(y)
            print(target, " was destroyed")
        except:
            effect()

powerup = Spell("PowerUp", 2):

    def effect():
        print p1.field
        target = input("Which monster would you like to power up?")
        target = str(target)
        try:
            



def cpeffect():
