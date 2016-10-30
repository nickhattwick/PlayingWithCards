from player import Player
from prompts import turn_prompt
from random import shuffle, choice

p1 = Player("Player 1")
p2 = Player("Player 2")

players = (p1, p2)
for player in players:
    shuffle(player.deck)
    for _ in range(7):
        player.draw()

first = choice("a""b")
print(first)
if first == "a":
    print("Player 1 goes first")
    turn_prompt(p1)
elif first == "b":
    print("Player 2 goes first")
    turn_prompt(p2)
