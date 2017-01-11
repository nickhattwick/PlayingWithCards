from player import AutoPilot

class StillLearning(AutoPilot):
    def get_value(card):
            try:
                positive_value = summon["W"]
            except KeyError:
                positive_value = 0
            try:
                negative_value = summon["L"]
            except KeyError:
                negative_value = 0
            value = positive_value - negative_value
    
    def auto_summon(self):
        try:
            with open("parsed.json", 'r') as parsed:
                summon_data = json.load(parsed)
        except FileNotFoundError:
            summon_data = None

        current_card = None
        place = 0
        creatures = [card for card in self.board.hand if card.kind == "creature"]
        while place < len(creatures):
            choice = self.board.hand[place]
            print(choice)
            if not current_card:
                current_card = choice
                print("current card: ", current_card)
            else:
                current_card_value = None
                for summon in summon_data:
                    if summon = current_card.name:
                        try:
                            positive_value = summon["W"]
                        except KeyError:
                            positive_value = 0
                        try:
                            negative_value = summon["L"]
                        except KeyError:
                            negative_value = 0
                        current_card_value = positive_value - negative_value




    #def _summon(self):
        current_card = None
        place = 0
        creatures = [card for card in self.board.hand if card.kind == "creature"]
        while place < len(creatures):
            choice = self.board.hand[place]
            print(choice)
            if not current_card:
                current_card = choice
                print("current card: ", current_card)
            elif (current_card.power < choice.power) and (current_card.cost <= self.board.mana.amount):
                current_card = choice
                print("current card: ", current_card)
