    def __lt__(self, other):
        ''' returns true if self is weaker than other.
            Elf < Dragon because elf is 1/1 and dragon is 5/5 '''
            return self.power < other.power

elf = Card(elf, 1)
dragon = Card(dragon, 5)
if elf < dragon:
