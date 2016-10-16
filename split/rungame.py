from random import shuffle
from opturn import *
from prompts import prompt
from deck import Deck


class player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.blockers = []
        self.lands = []
        self.dpile = []
        self.deck = Deck
        self.playedland = False
        self.mana = 0

    def draw(self):
        x = self.deck.pop()
        self.hand.append(x)

p1 = player('P1')
p2 = player('P2')

players = (p1, p2)

for p in players:
    p.count = 0
    shuffle(p.deck)
    while (p.count < 7):
        p.draw()
        p.count += 1

def plturn():
    p1.playedland = False
    p1.draw()
    p1.mana = len(p1.lands)
    p1.blockers = list(p1.field)
    print("Hand: ", p1.hand)
    print("Field: ", p1.field)
    print("Mana: ", p1.mana)
    prompt()

def opturn():
    print("Opponent's Turn")
    p2.draw()
    print("OP has ", len(p2.hand), " cards in hand")
    opland()

plturn()
