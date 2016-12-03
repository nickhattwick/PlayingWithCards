class Mana:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return int(self.amount)

    def gain(self, other):
        self.amount = self.amount + other

    def spend(self, other):
        self.amount = self.amount - other
