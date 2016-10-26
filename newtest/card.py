class Card:
    '''Represents land and creature cards.'''

    def __init__(self, kind, name, cost=0, power=0):
        self.kind = kind
        self.name = name
        self.cost = cost
        self.power = power
        self.tapped = False


'''Creates and returns a shuffled deck of Cards.'''
deck = []
for _ in range(20):
    deck.append(Card('land', "Land"))
for _ in range(6):
    deck.append(Card('creature', "Bear", 2, 2))
for _ in range(6):
    deck.append(Card('creature', "Knight", 3, 3))
for _ in range(4):
    deck.append(Card('creature', "Elemental", 4, 4))
for _ in range(2):
    deck.append(Card('creature', "Vampire", 5, 5))
    deck.append(Card('creature', "Dragon", 6, 6))
