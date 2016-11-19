def game_log(func):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        with open("game_log.txt", 'a') as f:
            f.write("Called " + func.__name__)
            f.write(self.name + "s hand: " + str(self.hand) + "\n")
            f.write(self.name + "s field: " + str(self.field) + "\n")
            f.write(self.opponent.name + "s field: " + str(self.opponent.field) + "\n")
            f.write(self.name + "s LP: " + str(self.life) + "\n")
            f.write(self.opponent.name + "s LP: " + str(self.opponent.life) + "\n")
            f.write(str(self.lands))
    return(inner)
