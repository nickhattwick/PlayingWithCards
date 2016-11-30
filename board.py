from card import Card, deck, find_by_name
from mana import Mana
from random import shuffle
from battle import destroy, battle
from logging import game_log

class GameControl:

    def __init__(self):
        self.hand = []
        self.field = []
        self.lands = []
        self.dpile = []
        self.deck = deck
        self.playedland = False
        self.mana = Mana(0)

        self.attributes = [self.hand, self.field, self.lands, self.dpile, self.deck, self.playedland, self.mana]
        self.functions = [self.draw, self.move_card, self.play_land, self.tap_for_mana, self.tap_all, self.summon, self.untap_all]

    def draw(self):
        try:
            x = self.deck.pop()
            self.hand.append(x)
        except IndexError:
            print(self.name, " loses")
            exit()

    def move_card(self, card, fromzone, endzone):
        index = fromzone.index(card)
        movingcard = fromzone.pop(index)
        endzone.append(movingcard)

    def play_land(self):
        x = 0
        if not self.playedland:
            while x < len(self.hand):
                if self.hand[x].name == "Land":
                    chosenland = self.hand[x]
                    self.move_card(chosenland, self.hand, self.lands)
                    self.playedland = True
                    print("Played a land")
                    break
                else:
                    x+=1
        else:
            print("You've already played a land this turn")

    def tap_for_mana(self, card):
        if card.kind == "land":
            if not card.tapped:
                card.tapped = True
                self.mana.amount = self.mana.amount + 1
            else:
                print("That card is already tapped")
        else:
            print("That card is not a land")

    def tap_all(self):
        for land in self.lands:
            if not land.tapped:
                self.tap_for_mana(land)
            print(self.mana.amount)


    def summon(self, cardname):
        if cardname in (card.name for card in self.hand):
            card = find_by_name(self.hand, cardname)
            if card.kind == "creature":
                if self.mana.amount >= card.cost:
                    self.move_card(card, self.hand, self.field)
                    self.mana.amount = self.mana.amount - card.cost
                    print(card.name, " was summoned")
                else:
                    print("Not enough mana")
            else:
                print("You can only summon creatures")
        else:
            print("That card is not in your hand")

    def untap_all(self):
        for card in self.field:
            card.untap
        for land in self.lands:
            land.untap

board = GameControl()
