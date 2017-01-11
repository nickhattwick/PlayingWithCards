from player import AutoPilot

class StillLearning(AutoPilot):
    def get_card_value(summon):
            try:
                positive_value = summon["W"]
            except KeyError:
                positive_value = 0
            try:
                negative_value = summon["L"]
            except KeyError:
                negative_value = 0
            value = positive_value - negative_value
            return value

    def auto_summon(self):
        try:
            with open("parsed.json", 'r') as parsed:
                summon_data = json.load(parsed)
        except FileNotFoundError:
            summon_data = None

        current_card = None
        current_card_value = None
        place = 0
        creatures = [card for card in self.board.hand if card.kind == "creature"]
        while place < len(creatures):
            choice = self.board.hand[place]
            choice_value = None
            print(choice)
            if not current_card:
                current_card = choice
                print("current card: ", current_card)
                for summon in summon_data:
                    if summon = current_card.name:
                        current_card_value = get_card_value(summon)
            else:
                for summon in summon_data:
                    if summon = choice.name:
                        choice_value = get_card_value(summon)
                if choice_value > current_card_value:
                    current_card = choice
                    current_card_value = choice_value
            place += 1
