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

def summon():
    mhand = [x for x in p1.hand if x != "l"]
    print("Monsters: ", mhand)
    mchoice = input("Which monster would you like to summon?\n")
    if str(mchoice) in mhand:
        if int(mchoice) <= p1.mana:
            y = p1.hand.index(mchoice)
            z = p1.hand.pop(y)
            p1.field.append(z)
            p1.blockers.append(z)
            p1.mana = p1.mana - int(mchoice)
            print(p1.field)
            print("Mana Left: ", p1.mana)
            prompt()
        else:
            print("You can only play monsters less than or equal to your mana")
            prompt()
    else:
        print("That's not a card in your hand")
        prompt()
