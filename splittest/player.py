from deck import *
from random import shuffle

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
        try:
            x = self.deck.pop()
            self.hand.append(x)
        except:
            print(self.name, " loses")
            exit()
