import json

with open("results.json", 'r') as results:
        data = json.load(results)

summon_ratios = {}

for turn_log in data["turns"]:
    for moves in turn_log["moves"]:
        for move in moves:
            for key in move:
                if key == "Summon":
                    print(move)
                    print(move[1])
                    checkpoint = False
                    while checkpoint == False
                        for summon in summon_ratios:
                            if summon == move


                    if not move[1] in summon_ratios:
                        summon_ratios[move[1]] = {}
                        if data["winner"] == turn_log["player"]:
                            summon_ratios[move[1]]["W"] = 1
                        elif data["loser"] == turn_log["player"]:
                            summon_ratios[move[1]]["L"] = 1

with open("parsed.json", 'w') as parsed:
    json.dump(move_ratios, parsed)
