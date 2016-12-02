from testplayer import HumanPlayer, AutoPilot
from prompts import full_turn
from random import shuffle, choice

p1 = HumanPlayer("Player 1")
p2 = AutoPilot("Player 2")
p1.opponent = p2
p2.opponent = p1

players = (p1, p2)
for player in players:
    shuffle(player.board.deck)
    for _ in range(7):
        player.board.draw()

coin_toss = choice([True, False])
first = p1 if coin_toss else p2
second = p2 if coin_toss else p1

keep_playing = True
while keep_playing:
    keep_playing = full_turn(first)
    if not keep_playing:
        break
    keep_playing = full_turn(second)
    if not keep_playing:
        break
