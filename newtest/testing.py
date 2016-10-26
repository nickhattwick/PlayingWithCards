from card import Card, deck
from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self._life = 20
        self.hand = []
        self.field = []
        self.lands = []
        self.dpile = []
        self.deck = deck
        self.playedland = False
        self.mana = 0
        self.lose = False

    def draw(self):
        try:
            x = self.deck.pop()
            self.hand.append(x)
        except IndexError:
            print(self.name, " loses")
            exit()

p1 = Player('P1')
p2 = Player('P2')

players = (p1, p2)

for p in players:
    p.count = 0
    shuffle(p.deck)
    while (p.count < 7):
        p.draw()
        p.count += 1

for card in p1.hand:
    print(card.name)
