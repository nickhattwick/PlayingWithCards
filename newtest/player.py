from card import Card, deck, find_by_name
from mana import Mana
from random import shuffle
from battle import destroy, battle

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.lands = []
        self.dpile = []
        self.deck = deck
        self.playedland = False
        self.mana = Mana(0)
        self.lose = False
        self.opponent = None

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.life, self.field, len(self.hand))

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

    def take_damage(self, damage):
        self.life -= damage
        print(self.name, self.life)
        if self.life <= 0:
            self._lose = True
            exit()

    def shuffle(self):
        shuffle(self.deck)

    def hand_view(self):
        for card in self.hand:
            print(card)

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

    def attack(self, cardname):
        attacker = find_by_name(self.field, cardname)
        try:
            if attacker.tapped == False:
                attacker.tapped = True
                print(attacker.name, " is attacking")
                self.opponent.block_choice(attacker)
            else:
                print("You can't attack with that")
        except:
            print("That's not on your field")

    def block(self, attacker, blocker):
        if blocker in self.field:
            battle(self, blocker, self.opponent, attacker)

    def block_choice(self, attacker):
        choice = input("Will you block? Y or N")
        if choice.upper() == "Y":
            blocker = find_by_name(self.field, choice)
            if blocker.tapped == False:
                blocker.tapped = True
                print(blocker.name, " blocks ", attacker.name)
                self.block(attacker, blocker)
        elif choice.upper() == "N":
            self.take_damage(attacker.power)
