import json

all_results = {}

turn_number = 0
global turn_number

current_turn = []

class Move:
    def __init__(self, kind, detail = None):
        self.kind = kind
        self.detail = detail

class Turn:
    def __init__(self, turnplayer, number):
        self.player = turnplayer
        self.number = number
        self.moves = []
        self.lifes = [turnplayer.life, turnplayer.opponent.life]
        self.boards = [turnplayer.board.field, turnplayer.opponent.board.field]
        self.hands = [turnplayer.board.hand, len(turnplayer.opponent.board.hand)]

def begin_turn(turnplayer, number):
    current_turn = Turn(turnplayer, number)

def summon_log(func, current_turn):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        if cardname in current_turn.player.board.field:
            summon = Move(summon, cardname)
            current_turn.moves.append(summon)

def land_log(func):
    def inner(self, *args, **kwargs):
        landchecker = current_turn.player.playedland
        func(self, *args, **kwargs)
        if current_turn.player.playedland:
            if not landchecker:
                


def results_log(func):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        this_game_results = {"W": winner.name, "L": loser.name}
        all_results[game_id] = this_game_result
        with open("results.json".format, 'a') as results:
            json.dump(all_results, results)

def setup_log(firstplayer, secondplayer):
    players.append(firstplayer.name, secondplayer.name)

def turns_log(turnplayer):
    turn.player = turnplayer




#3 dictionaries
#game results dictionary - game#, winner, loser
#gamemoves dictionary - player1 moves, player2 moves
