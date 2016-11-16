def game_log(func):
    def inner():
        func()
        with open("game_log.txt", 'w') as f:
            f.write(self.name, "s hand: ", self.hand)
            f.write(self.name, "s field: ", self.field)
            f.write(self.opponent.name, "s field: ", self.opponent.field)
            f.write(self.name, "s LP: ", self.life)
            f.write(self.opponent.name, "s LP: ", self.opponent.life)
            f.write(self.lands)
    return(inner)
