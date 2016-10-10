def plturn():
    p1.playedland = False
    p1.draw()
    p1.mana = len(p1.lands)
    p1.blockers = list(p1.field)
    print("Hand: ", p1.hand)
    print("Field: ", p1.field)
    print("Mana: ", p1.mana)

    prompt()

def opturn():
    print("Opponent's Turn")
    p2.draw()
    print("OP has ", len(p2.hand), " cards in hand")
    opland()
