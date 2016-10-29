from mana import Mana

class Player:
    def __init__(self, name):
        self.name = name
        self.mana = Mana(0)

Joe = Player("Joe")
print(Joe.mana.amount)
