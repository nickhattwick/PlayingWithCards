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
                    while checkpoint == False:
                        for summon in summon_ratios:
                            if summon == move[1]:
                                if data["winner"] == turn_log["player"]:
                                    summon_ratios[move[1][0]]["W"] += 1
                                elif data["loser"] == turn_log["player"]:
                                    summon_ratios[move[1][0]]["L"] += 1
                                checkpoint = True
                        if checkpoint == False:
                            summon_ratios[move[1][0]] = {}
                            if data["winner"] == turn_log["player"]:
                                summon_ratios[move[1][0]]["W"] = 1
                            elif data["loser"] == turn_log["player"]:
                                summon_ratios[move[1][0]]["L"] = 1
                            checkpoint = True

with open("parsed.json", 'w') as parsed:
    json.dump(summon_ratios, parsed)
