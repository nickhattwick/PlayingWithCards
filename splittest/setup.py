from random import shuffle
from player import player

def setup():
    for p in players:
        p.count = 0
        shuffle(p.deck)
        while (p.count < 7):
            p.draw()
            p.count += 1

    print(p1.hand)

setup()
