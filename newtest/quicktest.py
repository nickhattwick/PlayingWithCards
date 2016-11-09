class HumanPlayer(Player):
    def turn_prompt(self):
        print("It's", self.name, "s turn.")
        print(self.name, "s Hand: ", self.hand)
        print(self.name, "s Field: ", self.field)
        print(self..opponent.name, "s Field", self.opponent.field)
        print(self.name, "s Life: ", self.life)
        print(self.name, "s Mana: ", self.mana.amount)
        choice = input("It's your turn. What will you do? \n LAND TAP SUMMON ATTACK DONE\n")

        if choice.upper() == "LAND":
            self.play_land()

        elif choice.upper() == "VIEW":
            self.hand_view()

        elif choice.upper() == "SUMMON":
            choice = input("Which monster will you summon?")
            self.summon(choice)

        elif choice.upper() == "TAP":
            for land in self.lands:
                if not land.tapped:
                    self.tap_for_mana(land)
                print(self.mana.amount)


        elif choice.upper() == "ATTACK":
            attacker = input("Which monster will attack?")
            self.attack(attacker)

        elif choice.upper() == "DONE":
            self.mana.amount = 0
            return False

        elif choice.upper() == "QUIT":
            exit()

        else:
            print("That's not even a thing")
            self.turn_prompt()

        return True
