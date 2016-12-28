import json

with open("results.json", 'r') as results:
        data = json.load(results)

move_ratios = {"Summon" : {}}

for turn_log in data["turns"]:
    for move in turn_log["moves"]:
        if move[0] == "Summon":
            if move[1] not in move_ratios["Summon"]:
                move_ratios["Summon"][move[1]] = {}
                if data["winner"] == turn_log["player"]:
                    move_ratios["Summon"][move[1]]["W"] = 1
                elif data["loser"] == turn_log["player"]:
                    move_ratios["Summon"][move[1]]["L"] = 1


print(data["turns"])
