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
            summon = Move("Summon", cardname)
            current_turn.moves.append(summon)

def land_log(func):
    def inner(self, *args, **kwargs):
        landchecker = current_turn.player.board.playedland
        func(self, *args, **kwargs)
        if current_turn.player.board.playedland:
            if not landchecker:
                current_turn.moves.append("Land")

def tap_log(func):
    def inner(self, *args, **kwargs):
        mana_before = current_turn.player.board.mana.amount
        func(self, *args, **kwargs)
        mana_after = current_turn.player.board.mana.amount
        if mana_after > mana_before:
            tap = Move("Tap", mana_after)
            current_turn.moves.append(tap)

def attack_log(func):
    def inner(self, *args, **kwargs):
        status_before = cardname.attacked
        func(self, *args, **kwargs)
        status_after = cardname.attacked
        if status_before == False && status_after == True:
            attack = Move("Attack", cardname)
            current_turn.moves.append(attack)

def block_log(func):
    def inner(self, *args, **kwargs):
        status_before = cardname.blocked
        func(self, *args, **kwargs)
        status_after = cardname.blocked
        if status_before == False && status_after == True:
            block = Move("Block", cardname)
            current_turn.moves.append(block)

def done_log(func):
    def inner(self, *args, **kwargs):
        current_turn.lifes.append(current_turn.player.life, current_turn.player.opponent.life)
        current_turn.boards.append(current_turn.player.board.field, current_turn.player.opponent.board.field)
        current_turn.hands.append(current_turn.player.board.hand, len(current_turn.player.opponent.board.hand))
        func(self, *args, **kwargs)


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
