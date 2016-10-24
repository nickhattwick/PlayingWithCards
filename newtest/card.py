class Card:
    '''Represents land and creature cards.'''

    def __init__(self, kind, name, cost=0, power=0):
        self.kind = kind
        self.name = name
        self.cost = cost
        self.power = power
        self.tapped = False
