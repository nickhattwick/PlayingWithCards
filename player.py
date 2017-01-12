from card import Card, deck, find_by_name
from mana import Mana
from random import shuffle
from battle import destroy, battle
from board import GameControl
import json
import jsonlog

class Player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.lose = False
        self.opponent = None
        self.board = GameControl()


    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.life, self.board.field, len(self.board.hand))

    def take_damage(self, damage):
        self.life -= damage
        print(self.name, self.life)
        if self.life <= 0:
            self._lose = True
            jsonlog.record_results(self)
            exit()

    @jsonlog.attack_log
    def attack(self, cardname):
        attacker = find_by_name(self.board.field, cardname)
        if attacker:
            if not attacker.tapped:
                attacker.tap()
                attacker.attacked = True
                print(attacker.name, " is attacking")
                self.opponent.will_block(attacker)
            else:
                print("You can't attack with that")
        else:
            print("You don't control ", cardname)

    @jsonlog.block_log
    def block(self, attacker, blocker):
        if blocker in self.board.field:
            if not blocker.blocked:
                blocker.blocked = True
                battle(self, blocker, self.opponent, attacker)

    def will_block(self, attacker):
        raise NotImplementedError()

    def who_blocks(self, attacker):
        raise NotImplementedError()

    def turn_prompt(self):
        raise NotImplementedError()


class HumanPlayer(Player):
    def turn_prompt(self):
        print("It's", self.name, "s turn.")
        print(self.name, "s Hand: ", self.board.hand)
        print(self.opponent.name, "s Hand: ", self.opponent.board.hand)
        print(self.name, "s Field: ", self.board.field)
        print(self.opponent.name, "s Field", self.opponent.board.field)
        print(self.name, "s Life: ", self.life)
        print(self.name, "s Mana: ", self.board.mana.amount)
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
            jsonlog.end_turn()
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
            blocker = find_by_name(self.board.field, chosen)
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
        creatures = [card for card in self.board.hand if card.kind == "creature"]
        while place < len(creatures):
            choice = self.board.hand[place]
            print(choice)
            if not current_card:
                if choice.cost <= self.board.mana.amount:
                    current_card = choice
                print("current card: ", current_card)
            elif (current_card.power < choice.power) and (choice.cost <= self.board.mana.amount):
                current_card = choice
                print("current card: ", current_card)

            place += 1
        if current_card:
            self.board.summon(current_card.name)

    def all_attack(self):
        for card in self.board.field:
            self.attack(card.name)

    def will_block(self, attacker):
        self.take_damage(attacker.power)

    def turn_prompt(self):
        print(self.name, "s turn")
        print(self.board.hand)
        print(self.board.playedland)
        self.board.play_land()
        self.board.tap_all()
        print("AI's Mana: ", self.board.mana.amount)
        self.auto_summon()
        self.all_attack()
        self.board.mana.amount = 0
        print(self.board.playedland)
        print("Ending AI's turn")
        jsonlog.end_turn()
        return False


class StillLearning(AutoPilot):
    def get_card_value(self, summon, summon_data):
            try:
                positive_value = summon_data[summon]["W"]
            except KeyError:
                positive_value = 0
            try:
                negative_value = summon_data[summon]["L"]
            except KeyError:
                negative_value = 0
            value = positive_value - negative_value
            return value

    def auto_summon(self):
        try:
            with open("parsed.json", 'r') as parsed:
                summon_data = json.load(parsed)
                print(summon_data)
        except FileNotFoundError:
            summon_data = None

        current_card = None
        current_card_value = None
        place = 0
        creatures = [card for card in self.board.hand if card.kind == "creature"]
        print(creatures)
        while place < len(creatures):
            choice = creatures[place]
            choice_value = None
            print("choice: ", choice)
            if choice.cost <= self.board.mana.amount:
                if not current_card:
                    current_card = choice
                    print("current card: ", current_card)
                    for summon in summon_data:
                        if summon == current_card.name:
                            print(summon)
                            current_card_value = self.get_card_value(summon, summon_data)
                    if not current_card_value:
                        current_card_value = 0
                else:
                    for summon in summon_data:
                        print(summon)
                        if summon == choice.name:
                            choice_value = self.get_card_value(summon, summon_data)
                    if not choice_value:
                        choice_value = 0
                    print(choice, choice_value, current_card, current_card_value)
                    if choice_value > current_card_value:
                        current_card = choice
                        current_card_value = choice_value
            place += 1
        if current_card:
            self.board.summon(current_card.name)
