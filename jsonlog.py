import json
from card import find_by_name

all_results = {}

turn_number = 0
global turn_number

current_turn = None
archived_turns = []

# constants for Move kinds
class MoveKind:
    SUMMON, BLOCK, TAP, ATTACK, DONE = range(5)

class Move:
    def __init__(self, kind, detail = None):
        self.kind = kind
        self.detail = detail


class Turn:
    def __init__(self, turnplayer, number):
        self.player = turnplayer
        self.number = number
        self.moves = []
        self.lifes = (turnplayer.life, turnplayer.opponent.life)
        self.boards = (turnplayer.board.field, turnplayer.opponent.board.field)
        self.hands = (turnplayer.board.hand, len(turnplayer.opponent.board.hand))

    def __repr__(self):
        return "turn {} for player {}".format(self.number, self.player)

def begin_turn(turnplayer, number):
    global current_turn
    global archived_turns
    archived_turns.append(current_turn)
    current_turn = Turn(turnplayer, number)

def summon_log(func):
    global current_turn
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        cardname = args[1] # get cardname argument from summon function
        print(cardname)
        try:
            summon_check = find_by_name(current_turn.player.board.field, cardname)
            summon = Move("Summon", cardname)
            current_turn.moves.append(summon)
            for move in current_turn.moves:
                print(move.kind, move.detail)
        except ValueError:
            print("not summoned")
    return inner

def land_log(func):
    global current_turn
    def inner(*args, **kwargs):
        landchecker = current_turn.player.board.playedland
        func(*args, **kwargs)
        if current_turn.player.board.playedland:
            if not landchecker:
                land = Move("Land")
                current_turn.moves.append(land)
                for move in current_turn.moves:
                    print(move.kind, move.detail)
    return inner


def tap_log(func):
    global current_turn
    def inner(*args, **kwargs):
        mana_before = current_turn.player.board.mana.amount
        func(*args, **kwargs)
        mana_after = current_turn.player.board.mana.amount
        if mana_after > mana_before:
            tap = Move("Tap", mana_after)
            current_turn.moves.append(tap)
            for move in current_turn.moves:
                print(move.kind, move.detail)
    return inner

def attack_log(func):
    global current_turn
    def inner(*args, **kwargs):
        cardname = args[1]
        card = find_by_name(current_turn.player.board.field, cardname)
        status_before = card.attacked
        func(*args, **kwargs)
        status_after = card.attacked
        if status_before == False and status_after == True:
            attack = Move("Attack", cardname)
            current_turn.moves.append(attack)
            for move in current_turn.moves:
                print(move.kind, move.detail)
    return inner

def block_log(func):
    global current_turn
    def inner(*args, **kwargs):
        blocker = args[2]
        status_before = blocker.blocked
        func(*args, **kwargs)
        status_after = blocker.blocked
        if status_before == False and status_after == True:
            block = Move("Block", blocker.name)
            current_turn.moves.append(block)
            for move in current_turn.moves:
                print(move.kind, move.detail)
    return inner

def end_turn():
    global current_turn
    global archived_turns
    archived_turns.append(current_turn)
    print("turn logged")

def results_log(func):
    def inner(self, *args, **kwargs):
        func(self, *args, **kwargs)
        this_game_results = {"W": winner.name, "L": loser.name}
        all_results[game_id] = this_game_result
        with open("results.json".format, 'a') as results:
            json.dump(all_results, results)
    return inner

def setup_log(firstplayer, secondplayer):
    players.append(firstplayer.name, secondplayer.name)

def turns_log(turnplayer):
    turn.player = turnplayer
