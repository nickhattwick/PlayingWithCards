from deck import *
from random import shuffle

class Player:
    def __init__(self, name):
        self.name = name
        self._life = 20
        self.hand = []
        self.field = []
        self.blockers = []
        self.lands = []
        self.dpile = []
        self.deck = Deck
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

    def take_damage(self, damage):
        self._life -= damage
        if self._life <= 0:
            self._lose = True
            exit()

    def tap_for_mana(self, card):
        if card.kind == "land":
            if card.tapped == False
                card.tapped = True
                self.mana += 1
            else:
                print("That card is already tapped")
        else:
            print("That card is not a land")

    def summon(self, card):
        if card in self.hand:
            if card.kind == "creature":
                if self.mana >= card.cost:
                    cardindex = self.hand.index(card)
                    movingcard = self.hand.pop(cardindex)
                    self.field.append(movingcard)
                    self.mana -= card.cost
                else:
                    print("Not enough mana")
            else:
                print("You can only summon creatures")
        else:
            print("That card is not in your hand")
