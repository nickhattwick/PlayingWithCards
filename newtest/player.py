from card import Card, deck
from mana import Mana
from random import shuffle
from battle.py import destroy, battle

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
        self.mana = Mana(0)
        self.lose = False
        self.opponent = None

    def draw(self):
        try:
            x = self.deck.pop()
            self.hand.append(x)
        except IndexError:
            print(self.name, " loses")
            exit()

    def move_card(self, card, start, end):
        index = self.start.index(card)
        movingcard = self.start.pop(index)
        self.end.append(card)

    def take_damage(self, damage):
        self._life -= damage
        if self._life <= 0:
            self._lose = True
            exit()

    def hand_view(self):
        for card in self.hand:
            print card.name

    def play_land(self, card):
        if card.kind == Land:
            if card in self.hand:
                move_card(card, self.hand, self.field)
            else:
                print("That card is not in your hand")
        else:
            print("That card is not a land")

    def tap_for_mana(self, card):
        if card.kind == "land":
            if card.tapped == False
                card.tapped = True
                self.mana.amount = self.mana.amount + 1
            else:
                print("That card is already tapped")
        else:
            print("That card is not a land")

    def summon(self, card):
        if card in self.hand:
            if card.kind == "creature":
                if self.mana.amount >= card.cost:
                    move_card(card, self.hand, self.fiend)
                    self.mana.amount = self.mana.amount - card.cost
                else:
                    print("Not enough mana")
            else:
                print("You can only summon creatures")
        else:
            print("That card is not in your hand")

    def attack(self, attacker):
        if attacker in self.field:
            if attacker.tapped == False:
                attacker.tapped = True
                self.opponent.block
                #IS THIS ENOUGH. MAY HAVE TO COME BACK TO THIS...

    def block(self, attacker, blocker):
        if blocker in self.field:
            battle(self, blocker, self.opponent, attacker)
