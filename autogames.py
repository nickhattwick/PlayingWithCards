from player import HumanPlayer, AutoPilot
from prompts import full_turn
from random import shuffle, choice
import jsonlog

p1 = AutoPilot("Player 1")
p2 = AutoPilot("Player 2")
p1.opponent = p2
p2.opponent = p1

players = (p1, p2)
first = None
second = None

game_number = 1

def all_turns():
    turn_number = 1
    while True:
        yield first, turn_number
        yield second, turn_number
        turn_number += 1

def game_loop():
    jsonlog.initiate_game(players, game_number)
    for player in players:
        shuffle(player.board.deck)
        for _ in range(7):
            player.board.draw()

    coin_toss = choice([True, False])
    first = p1 if coin_toss else p2
    second = p2 if coin_toss else p1

    keep_playing = True
    for player, turn_number in all_turns():
        print(player.name, turn_number)
        jsonlog.initiate_turn(player, turn_number)
        keep_playing = full_turn(player)
        if not keep_playing:
            break

game_loop()
