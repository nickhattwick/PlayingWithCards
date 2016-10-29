class Mana:
    def __init__(self, amount):
        self.amount = amount

    def gain(self, other):
        self.amount = self.amount + other

    def spend(self, other):
        self.amount = self.amount - other
