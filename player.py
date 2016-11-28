from card import Card, deck, find_by_name
from mana import Mana
from random import shuffle
from battle import destroy, battle
from logging import game_log
from board import GameControl

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.lose = False
        self.opponent = None
        self.board = GameControl

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.life, self.field, len(self.hand))

    def take_damage(self, damage):
        self.life -= damage
        print(self.name, self.life)
        if self.life <= 0:
            self._lose = True
            exit()

    def turn_start(self):
        self.board.draw

    def attack(self, cardname):
        attacker = find_by_name(self.field, cardname)
        if attacker:
            if not attacker.tapped:
                attacker.tap()
                print(attacker.name, " is attacking")
                self.opponent.will_block(attacker)
            else:
                print("You can't attack with that")
        else:
            print("You don't control ", cardname)


    def block(self, attacker, blocker):
        if blocker in self.field:
            battle(self, blocker, self.opponent, attacker)

    def will_block(self, attacker):
        raise NotImplementedError()

    def who_blocks(self, attacker):
        raise NotImplementedError()

    def turn_prompt(self):
        raise NotImplementedError()


class HumanPlayer(Player):
    @game_log
    def turn_prompt(self):
        print("It's", self.name, "s turn.")
        print(self.name, "s Hand: ", self.hand)
        print(self.opponent.name, "s Hand: ", self.opponent.hand)
        print(self.name, "s Field: ", self.field)
        print(self.opponent.name, "s Field", self.opponent.field)
        print(self.name, "s Life: ", self.life)
        print(self.name, "s Mana: ", self.mana.amount)
        choice = input("It's your turn. What will you do? \n LAND TAP SUMMON ATTACK DONE\n")

        if choice.upper() == "LAND":
            self.board.play_land()

        elif choice.upper() == "SUMMON":
            choice = input("Which monster will you summon?")
            self.board.summon(choice)

        elif choice.upper() == "TAP":
            self.board.tap_all()


        elif choice.upper() == "ATTACK":
            attacker = input("Which monster will attack?")
            self.attack(attacker)

        elif choice.upper() == "DONE":
            self.board.mana.amount = 0
            return False

        elif choice.upper() == "QUIT":
            exit()

        else:
            print("That's not even a thing")
            self.turn_prompt()

        return True

    def hand_view(self):
        for card in self.hand:
            print(card)


    def will_block(self, attacker):
        resolved = False
        while not resolved:
            choice = input("Will you block? Y or N")
            if choice.upper() == "Y":
                resolved = True
                self.who_blocks(attacker)
            elif choice.upper() == "N":
                self.take_damage(attacker.power)
                resolved = True
            else:
                print("Y or N?")

    def who_blocks(self, attacker):
        resolved = False
        while not resolved:
            chosen = input("Who will you block with?")
            blocker = find_by_name(self.field, chosen)
            if blocker:
                if blocker.tapped == False:
                    blocker.tapped = True
                    print(blocker.name, " blocks ", attacker.name)
                    resolved = True
                    self.block(attacker, blocker)
                else:
                    print("You can't block with a creature that's already tapped")
            else:
                print("You don't control that")

class AutoPilot(Player):
    def auto_summon(self):
        current_card = None
        place = 0
        creatures = [card for card in self.hand if card.kind == "creature"]
        while place < len(creatures):
            choice = self.hand[place]
            print(choice)
            if not current_card or current_card.power < choice.power:
                current_card = choice
            place += 1
        if current_card:
            self.summon(current_card.name)

    def all_attack(self):
        for card in self.field:
            self.attack(card.name)

    def will_block(self, attacker):
        self.take_damage(attacker.power)

    @game_log
    def turn_prompt(self):
        print(self.name, "s turn")
        print(self.hand)
        self.play_land()
        self.tap_all()
        print("AI's Mana: ", self.mana.amount)
        self.auto_summon()
        self.all_attack()
        self.mana.amount = 0
        print("Ending AI's turn")
        return False
