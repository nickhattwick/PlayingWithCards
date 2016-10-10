from random import shuffle
import turns.py
import deck.py
import player.py
import yourmove.py
import turns.py
import playland.py
import summon.py
import attack.py
import block.py
import opland.py
import opsummon.py
import opblock.py

p1 = player('P1')
p2 = player('P2')

players = (p1, p2)

for p in players:
    p.count = 0
    shuffle(p.deck)
    while (p.count < 7):
        p.draw()
        p.count += 1
