def playland():
    x = 0
    if not p1.playedland:
        while x < len(p1.hand):
            if p1.hand[x] == "l":
                print("x: ", x)
                y = p1.hand.pop(x)
                p1.lands.append(y)
                p1.mana = len(p1.lands)
                print("Mana: ", p1.mana)
                p1.playedland = True
                prompt()
            else:
                x+=1
        print("No lands in hand")
        prompt()
    else:
        print("You've already played a land this turn")
        prompt()
