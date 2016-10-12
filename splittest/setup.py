class player:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.hand = []
        self.field = []
        self.blockers = []
        self.lands = []
        self.dpile = []
        self.deck = Deck
        self.playedland = False
        self.mana = 0

    def draw(self):
        x = self.deck.pop()
        self.hand.append(x)

Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)

Deck.extend(("2","2","2","2","2","2","3","3","3","3","3","3","4","4","4","4","5","5","6"))

def main():
	print('This should not have happened')

if __name__ == "__main__": main()

p1 = player('P1')
p2 = player('P2')

players = (p1, p2)

for p in players:
    p.count = 0
    shuffle(p.deck)
    while (p.count < 7):
        p.draw()
        p.count += 1
