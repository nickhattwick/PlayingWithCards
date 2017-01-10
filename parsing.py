import json
from collections import Counter, defaultdict

def get_victory_key(data, player):
    if data["winner"] == player:
        victory_key = 'W'
    elif data["loser"] == player:
        victory_key = 'L'
    else:
        raise ValueError("player neither won nor lost")
    return victory_key

def parse_log():
    with open("results.json", 'r') as results:
        data = json.load(results)

    summon_ratios = defaultdict(Counter)

    try:
        with open("parsed.json", 'r') as parsed:
            summon_data = json.load(parsed)
            for summon in summon_data:
                print(summon)
                for k, v in summon:
                    summon_ratios[k] = v

    except FileNotFoundError:
        print("no existing file")

    for turn_log in data["turns"]:
        for moves in turn_log["moves"]:
            for move in moves:
                for key in move:
                    if key == "Summon":
                        summon = move[1][0]
                        player = turn_log["player"]
                        victory_key = get_victory_key(data, player)
                        summon_ratios[summon][victory_key] += 1

    with open("parsed.json", 'w') as parsed:
        json.dump(summon_ratios, parsed)

parse_log()
