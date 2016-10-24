class Card:
    '''Represents land and creature cards.'''

    def __init__(self, kind, name, cost=0, power=0):
        self.kind = kind
        self.name = name
        self.cost = cost
        self.power = power
        self.tapped = False

    def __lt__(self, other):
        ''' returns true if self is weaker than other.
            Elf < Dragon because elf is 1/1 and dragon is 5/5 '''
        return self.power < other.power

elf = Card("creature", "elf", 1, 1)
dragon = Card("creature", "dragon", 5, 5)
if elf < dragon:
    print('yup')
else:
    print('nope')
