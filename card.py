class Card:
    def __init__(self, kind, name, cost=0, power=0):
        self.kind = kind
        self.name = name
        self.cost = cost
        self.power = power

        self.tapped = False
        self.attacked = False
        self.blocked = False

    def __str__(self):
        return '{} {}'.format(self.name, self.cost)

    def __repr__(self):
        return '{}'.format(self.name)

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False


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

def find_by_name(zone, name):
    chosen_card = None
    for card in zone:
        if card.name == name:
            chosen_card = card
            break
    else:
        print("Did not find " + name + " in the zone.")
    return chosen_card
