from random import shuffle
from player import player

def setup():
    p1 = player('P1')
    p2 = player('P2')

    players = (p1, p2)

    for p in players:
        p.count = 0
        shuffle(p.deck)
        while (p.count < 7):
            p.draw()
            p.count += 1

    print(p1.hand)

setup()
